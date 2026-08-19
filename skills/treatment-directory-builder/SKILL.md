---
name: treatment-directory-builder
description: Plan, research, build, audit, publish, and maintain independent treatment-center directory websites through a guided intake and gated production workflow. Use for new or expanding rehab, detox, mental-health, or behavioral-health guides that need provider research, topical maps, accessible media, entity SEO, AEO, schema, discovery files, deployment, and live QA; do not use to operate a provider's clinical or admissions systems.
---

# Treatment Directory Builder

Deliver a complete, source-backed guide that helps readers compare documented fit and safety factors without implying clinical endorsement or guaranteed outcomes. Treat provider claims as sourced, dated assertions and project completion as a set of observable release gates.

## Operating Modes

Classify the request before acting:

- **New build:** run the full intake and initialize project control files.
- **Expansion:** audit the current site and brief, ask only for decisions needed by the requested expansion, then re-run affected gates.
- **Refresh:** update volatile evidence, preserve the audit trail, rebuild affected outputs, and verify the live site.
- **Audit:** make no production changes unless asked; report gate failures, evidence gaps, and prioritized fixes.

## Guided Start

For a new build, read [intake-and-governance.md](references/intake-and-governance.md). Ask one to three focused questions at a time and continue until all blocking decisions are answered or explicitly delegated. At minimum establish:

- guide name, canonical domain, publisher, accountable editor, and repository owner;
- geography, priority cities/regions, treatment scope, audience, and exclusions;
- provider inclusion criteria, target count, editor's choice, rationale, and commercial relationships;
- available brand files, provider assets, screenshots, video, licenses, and missing-media plan;
- topical priorities, conversion policy, phone/form ownership, analytics, Search Console, hosting, and refresh cadence.

Write accepted answers into a project-owned brief based on [project-brief.example.json](assets/project-brief.example.json). Never silently decide editor's choice, commercial disclosure, clinical inclusion criteria, or domain ownership.

For an empty repository, initialize the control files without overwriting existing work:

```bash
python scripts/init_project.py <project-root>
```

## Production Controller

Create a project state file from [production-state.example.json](assets/production-state.example.json). Read [production-schedule.md](references/production-schedule.md) to sequence work and [orchestration-and-iteration.md](references/orchestration-and-iteration.md) before delegating or running repeated review cycles.

Advance one phase at a time:

1. **Brief locked:** blocking decisions, owners, disclosures, target areas, and definition of done are recorded.
2. **Evidence ready:** candidate and source registers exist; every location identity and publishable claim has evidence or a visible `verify` status.
3. **Architecture ready:** information architecture, topical map, URL inventory, entities, templates, internal-link plan, and media plan are approved.
4. **Build complete:** pages, data, media, schema, discovery files, analytics/verification files, and responsive interactions are implemented.
5. **QA passed:** automated, editorial, factual, visual, accessibility, schema, and discovery gates pass with no release blockers.
6. **Live verified:** deployment, canonical domain, redirects, HTTPS, response codes, content types, sitemap, robots, forms/phones, and representative mobile/desktop pages work in production.
7. **Handoff complete:** repository, access boundaries, source and asset registers, known limitations, correction path, and maintenance schedule are documented.

Do not mark a phase complete because files exist. Record evidence for each gate in the state file. Continue iterating while an actionable failure remains; stop for user input only when a decision, credential, permission, licensed asset, or external account action cannot be safely inferred or completed.

## Build References

- Before collecting provider facts, read [research-and-sourcing.md](references/research-and-sourcing.md).
- Before defining the topical map, comparisons, profiles, or FAQs, read [content-and-comparison.md](references/content-and-comparison.md).
- Before acquiring or generating images/video, read [media-and-metadata.md](references/media-and-metadata.md).
- Before writing schema or discovery files, read [schema-aeo-and-discovery.md](references/schema-aeo-and-discovery.md).
- Before release, read [qa-and-release.md](references/qa-and-release.md).

## Non-Negotiable Invariants

- Use exact source names in NAP blocks and structured data. Do not add `The` to a legal or GBP name.
- For the featured editorial description only, prefix `The ` when the name does not already begin with it; never produce `The The`.
- Describe editor's choice as a disclosed editorial fit/example, never an overall clinical-quality or outcome ranking.
- Keep physical locations separate. Never combine addresses, phones, ratings, review counts, programs, or credentials across campuses.
- Date volatile facts, distinguish first-party claims from authoritative verification, and expose unresolved conflicts.
- Paraphrase review themes and link to the live profile. Do not republish substantial review text or use third-party ratings as outcome evidence.
- Do not claim licensing, accreditation, medical staffing, insurance, continuous coverage, outcomes, or availability without direct evidence.
- Do not add third-party ratings to `AggregateRating` or `Review` schema by default.
- Keep guide-owned `@id` values on the canonical guide domain; use official and Google URLs as identity and source references.
- Every substantive page needs purposeful, rights-cleared media, contextual alt text, intrinsic dimensions, caption/provenance where needed, and an asset-register record. Utility verification files are exempt.
- Every public page must be reachable through ordinary HTML links. Machine files supplement navigation; they do not replace it.
- Keep canonicals, schema IDs, sitemap URLs, robots references, entity maps, `llms.txt`, redirects, and the production domain consistent.
- Direct emergencies to 911 and clinical decisions to qualified professionals and provider verification.

## Definition Of Done

A project is complete only when all seven production phases are `passed`, the two validators pass, the internal crawler has no broken links, representative desktop/mobile screenshots have been reviewed, live-domain checks pass without redirect loops, and the handoff packet names the next review date and owner.

Run:

```bash
python scripts/validate_workflow.py project-brief.json production-state.json
python scripts/validate_directory.py <site-root> [center-data.json]
```

Report the production URL, commit, evidence date, unresolved non-blocking limitations, and scheduled refresh. Never describe a site as perfect; describe which gates passed and what residual risk remains.
