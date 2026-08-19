#!/usr/bin/env python3
"""Validate treatment-directory discovery files, profile schema, and optional data."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse


REQUIRED_FILES = (
    "index.html",
    "robots.txt",
    "sitemap.xml",
    "sitemap.html",
    "entitymap.html",
    "entitymap.json",
    "llms.txt",
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def json_ld_blocks(text: str) -> list[str]:
    return re.findall(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )


def validate_site(root: Path, data_path: Path | None) -> list[str]:
    errors: list[str] = []
    for name in REQUIRED_FILES:
        if not (root / name).is_file():
            fail(errors, f"Missing required file: {name}")

    robots = (root / "robots.txt").read_text(encoding="utf-8")
    match = re.search(r"^Sitemap:\s*(https?://\S+)$", robots, re.MULTILINE)
    if not match:
        fail(errors, "robots.txt needs one absolute Sitemap: URL")

    try:
        tree = ET.parse(root / "sitemap.xml")
        locs = [node.text for node in tree.findall("{*}url/{*}loc") if node.text]
        if not locs or any(not urlparse(loc).scheme for loc in locs):
            fail(errors, "sitemap.xml must contain absolute URL locations")
        for required in ("sitemap.html", "entitymap.html"):
            if not any(loc.endswith(required) for loc in locs):
                fail(errors, f"sitemap.xml does not list {required}")
    except (ET.ParseError, OSError) as exc:
        fail(errors, f"Invalid sitemap.xml: {exc}")

    try:
        entity_map = json.loads((root / "entitymap.json").read_text(encoding="utf-8"))
        if not entity_map.get("entities"):
            fail(errors, "entitymap.json has no entities")
    except (json.JSONDecodeError, OSError) as exc:
        fail(errors, f"Invalid entitymap.json: {exc}")

    html_files = [root / "index.html", root / "sitemap.html", root / "entitymap.html"]
    html_files += list((root / "centers").glob("*/index.html")) if (root / "centers").exists() else []
    ids: set[str] = set()
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        blocks = json_ld_blocks(text)
        if not blocks:
            fail(errors, f"Missing JSON-LD: {path.relative_to(root)}")
        for block in blocks:
            try:
                payload = json.loads(block)
            except json.JSONDecodeError as exc:
                fail(errors, f"Invalid JSON-LD in {path.relative_to(root)}: {exc}")
                continue
            nodes = payload.get("@graph", [payload]) if isinstance(payload, dict) else []
            for node in nodes:
                entity_id = node.get("@id") if isinstance(node, dict) else None
                if entity_id and urlparse(entity_id).scheme and entity_id in ids:
                    fail(errors, f"Duplicate schema @id: {entity_id}")
                elif entity_id and urlparse(entity_id).scheme:
                    ids.add(entity_id)
        if "sitemap.html" not in text and path.parent.name in {"centers", root.name}:
            pass  # Layout conventions vary; reachability is checked through sitemap.html.

    sitemap_html = (root / "sitemap.html").read_text(encoding="utf-8")
    for profile in (root / "centers").glob("*/index.html") if (root / "centers").exists() else []:
        slug = profile.parent.name
        if f"centers/{slug}/" not in sitemap_html:
            fail(errors, f"HTML sitemap does not link profile: {slug}")

    if data_path:
        try:
            data = json.loads(data_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            fail(errors, f"Invalid center data: {exc}")
            return errors
        for provider in data.get("providers", []):
            name = provider.get("exactName", "<unnamed>")
            if provider.get("featured"):
                display = provider.get("featuredDisplayName", "")
                if not display.startswith("The ") or display.startswith("The The "):
                    fail(errors, f"Featured display name must start with The exactly once: {name}")
            if not provider.get("locations"):
                fail(errors, f"Provider has no physical locations: {name}")
            for location in provider.get("locations", []):
                for field in (
                    "exactGbpName", "streetAddress", "addressLocality", "addressRegion",
                    "postalCode", "phoneE164", "googleProfileUrl", "napObservedAt"
                ):
                    if not location.get(field):
                        fail(errors, f"{name} location missing {field}")
                if "rating" in location and not location.get("reviewObservedAt"):
                    fail(errors, f"{name} rating lacks reviewObservedAt")
    return errors


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print("Usage: validate_directory.py <site-root> [center-data.json]", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve()
    data_path = Path(sys.argv[2]).resolve() if len(sys.argv) == 3 else None
    errors = validate_site(root, data_path)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Treatment directory validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
