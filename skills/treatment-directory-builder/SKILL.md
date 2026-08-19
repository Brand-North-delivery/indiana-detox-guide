---
name: treatment-directory-builder
description: Research, build, audit, and publish independent treatment-center directory websites with sourced provider data, transparent comparisons, center profiles, accessible media, entity SEO, AEO, schema, sitemaps, and deployment QA. Use for repeatable rehab, detox, mental-health, or behavioral-health guide projects; do not use to operate a provider's clinical or admissions systems.
---

# Treatment Directory Builder

Build an independent guide that helps readers verify fit and safety without implying clinical endorsement or guaranteed outcomes. Treat every provider claim as a sourced, dated assertion.

## Required Workflow

1. Define geography, treatment category, audience, provider count, featured editor's-choice facility, publisher, domain, and update date.
2. Read [research-and-sourcing.md](references/research-and-sourcing.md). Research each physical location and record evidence before writing.
3. Populate [center-data.example.json](assets/center-data.example.json) for every provider/location. Keep editorial labels separate from exact Google Business Profile and provider names.
4. Read [content-and-comparison.md](references/content-and-comparison.md). Build the directory, comparison method, center profiles, FAQs, disclaimers, and internal links.
5. For images, read [media-and-metadata.md](references/media-and-metadata.md). Never fabricate EXIF, licensing, provenance, or visual claims.
6. Read [schema-aeo-and-discovery.md](references/schema-aeo-and-discovery.md). Implement stable entity IDs, JSON-LD, `robots.txt`, XML/HTML sitemaps, HTML/JSON entity maps, and `llms.txt`.
7. Read [qa-and-release.md](references/qa-and-release.md). Run the validator, inspect desktop/mobile renders, test links, and deploy only after release gates pass.

## Non-Negotiable Invariants

- Use exact source names in NAP blocks and structured data. Do not add "The" to a legal/GBP name.
- For the featured editor's-choice description only, create `featuredDisplayName`: prefix `The ` when the name does not already begin with `The `; never produce `The The ...`.
- Describe editor's choice as an editorial fit/example, never a clinical-quality or outcome ranking.
- Separate physical locations. Never combine addresses, phones, ratings, or review counts from different campuses.
- Date volatile facts: ratings, review counts, hours, accreditation, programs, insurance, and phone records.
- Paraphrase review themes and link to the live profile. Do not republish substantial review text.
- Do not claim licensing, accreditation, medical staffing, insurance, 24/7 coverage, outcomes, or availability without direct evidence.
- Do not put third-party ratings into `AggregateRating` or `Review` schema unless the publisher has a defensible right to display and mark them up and the visible page satisfies current search policy.
- Keep guide-owned `@id` values on the guide domain; use official and Google URLs as identity/source references.
- Make every public page reachable through ordinary HTML links. Machine files supplement navigation; they do not replace it.
- Direct emergencies to 911 and medical decisions to qualified professionals and provider verification.

## Deliverables

- Responsive directory homepage with transparent method and provider shortlist
- One indexable profile per provider, with one NAP block per physical location
- Relevant FAQ taxonomy and visible answers; FAQ schema only when policy-eligible
- Source register and review/update dates
- Accessible, licensed media with factual alt text, caption, dimensions, and metadata record
- Page-level JSON-LD and a canonical cross-page entity-ID strategy
- `robots.txt`, `sitemap.xml`, `sitemap.html`, `entitymap.html`, `entitymap.json`, and `llms.txt`
- Validation report, deployment URL, commit, and update cadence

Run `python scripts/validate_directory.py <site-root> [center-data.json]` before release.
