#!/usr/bin/env python3
"""Validate a treatment-directory project brief and production state."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

PHASES = (
    "brief-locked", "evidence-ready", "architecture-ready", "build-complete",
    "qa-passed", "live-verified", "handoff-complete",
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(
    mapping: dict,
    fields: tuple[str, ...],
    label: str,
    errors: list[str],
    allow_empty: tuple[str, ...] = (),
) -> None:
    for field in fields:
        value = mapping.get(field)
        if field not in mapping or value is None or (field not in allow_empty and value in ("", [])):
            errors.append(f"{label} missing {field}")


def validate(brief: dict, state: dict) -> list[str]:
    errors: list[str] = []
    require(brief.get("project", {}), ("name", "mode", "canonicalBaseUrl", "publisher", "accountableEditor", "repositoryOwner", "deploymentOwner", "launchApprover"), "project", errors)
    require(brief.get("audience", {}), ("primary", "geography", "priorityAreas", "treatmentScope", "exclusions"), "audience", errors)
    require(brief.get("editorial", {}), ("providerTargetCount", "inclusionCriteria", "exclusionCriteria", "commercialRelationship", "comparisonDimensions", "reviewPolicy"), "editorial", errors)
    require(brief.get("brandAndMedia", {}), ("missingMediaPolicy", "assetOwner", "accessibilityTarget"), "brandAndMedia", errors)
    require(brief.get("conversionAndPrivacy", {}), ("leadFormEnabled", "phoneOwnership", "privacyReviewOwner"), "conversionAndPrivacy", errors)
    require(brief.get("technical", {}), ("stack", "hosting", "domainDnsOwner", "searchConsoleOwner", "productionBranch"), "technical", errors)
    require(brief.get("maintenance", {}), ("correctionOwner", "weeklyOwner", "monthlyOwner", "quarterlyOwner", "nextReviewDate"), "maintenance", errors)
    require(brief, ("definitionOfDone", "openQuestions"), "brief", errors, allow_empty=("openQuestions",))

    base = brief.get("project", {}).get("canonicalBaseUrl", "")
    parsed = urlparse(base)
    if parsed.scheme != "https" or not parsed.netloc or not base.endswith("/"):
        errors.append("project canonicalBaseUrl must be an absolute HTTPS URL ending in /")

    editorial = brief.get("editorial", {})
    if bool(editorial.get("editorsChoiceExactName")) != bool(editorial.get("editorsChoiceRationale")):
        errors.append("editor's choice name and rationale must both be set or both be null")

    phases = state.get("phases", {})
    for phase in PHASES:
        item = phases.get(phase)
        if not isinstance(item, dict):
            errors.append(f"production state missing phase {phase}")
            continue
        require(item, ("status", "owner", "evidence", "blockers"), f"phase {phase}", errors, allow_empty=("evidence", "blockers"))
        if item.get("status") not in {"pending", "in-progress", "passed", "blocked"}:
            errors.append(f"phase {phase} has invalid status")
        if item.get("status") == "passed" and not item.get("evidence"):
            errors.append(f"phase {phase} is passed without evidence")
        if item.get("status") == "passed" and item.get("blockers"):
            errors.append(f"phase {phase} is passed with blockers")

    if state.get("currentPhase") not in PHASES:
        errors.append("currentPhase is missing or invalid")
    blockers = state.get("metrics", {}).get("releaseBlockers", 0)
    if not isinstance(blockers, int) or blockers < 0:
        errors.append("releaseBlockers must be a non-negative integer")
    if phases.get("handoff-complete", {}).get("status") == "passed":
        require(state.get("release", {}), ("commit", "deployId", "productionUrl", "verifiedAt", "nextReviewDate"), "release", errors)
        if any(phases.get(phase, {}).get("status") != "passed" for phase in PHASES):
            errors.append("handoff-complete cannot pass before every phase passes")
        if blockers != 0:
            errors.append("handoff-complete requires zero release blockers")
    return errors


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: validate_workflow.py <project-brief.json> <production-state.json>", file=sys.stderr)
        return 2
    try:
        errors = validate(load(Path(sys.argv[1])), load(Path(sys.argv[2])))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Workflow validation failed: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("Workflow validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Treatment directory workflow validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
