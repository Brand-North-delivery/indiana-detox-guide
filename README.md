# Indiana Detox Guide

Static directory-style guide for comparing Indiana detox and residential addiction treatment centers.

The page is intentionally informational and should not be treated as medical advice. Provider details should be verified directly before admission decisions.

## Local preview

```sh
python -m http.server 4177
```

Then open `http://127.0.0.1:4177`.

## Repeatable team workflow

The complete production handoff is in [TEAM-SOP.md](TEAM-SOP.md). The reusable Codex skill is in [`skills/treatment-directory-builder`](skills/treatment-directory-builder) and includes research, content, media/EXIF, schema/AEO, discovery, QA, a source-data template, and a deterministic validator.

Validate a generated directory before release:

```sh
python skills/treatment-directory-builder/scripts/validate_directory.py . path/to/center-data.json
```

To share the skill independently, distribute the entire `skills/treatment-directory-builder` directory without removing its `references`, `assets`, `scripts`, or `agents` subdirectories.
