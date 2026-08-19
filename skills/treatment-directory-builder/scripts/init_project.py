#!/usr/bin/env python3
"""Initialize treatment-directory control files without overwriting project data."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
ASSETS = SKILL_ROOT / "assets"
FILES = {
    "project-brief.example.json": "project-brief.json",
    "production-state.example.json": "production-state.json",
    "center-data.example.json": "center-data.json",
    "url-inventory.example.csv": "url-inventory.csv",
    "source-register.example.csv": "source-register.csv",
    "asset-register.example.json": "asset-register.json",
    "maintenance-log.example.md": "maintenance-log.md",
}


def initialize(target: Path) -> list[Path]:
    target.mkdir(parents=True, exist_ok=True)
    conflicts = [target / output for output in FILES.values() if (target / output).exists()]
    if conflicts:
        names = ", ".join(path.name for path in conflicts)
        raise FileExistsError(f"Refusing to overwrite existing control files: {names}")
    created: list[Path] = []
    for source, output in FILES.items():
        destination = target / output
        shutil.copyfile(ASSETS / source, destination)
        created.append(destination)
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", default=".", help="Project root to initialize")
    args = parser.parse_args()
    try:
        created = initialize(Path(args.target).resolve())
    except FileExistsError as exc:
        print(exc)
        return 1
    print("Created treatment-directory project controls:")
    for path in created:
        print(f"- {path}")
    print("Next: complete the guided intake, replace example values, and run validate_workflow.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
