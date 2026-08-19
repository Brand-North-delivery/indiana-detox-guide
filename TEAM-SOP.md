# Treatment Directory Production SOP

This SOP is the human handoff companion to `skills/treatment-directory-builder`. Use it to create a new geography/category guide or refresh an existing one.

## 1. Brief and ownership

Name the geography, treatment category, audience, canonical domain, publisher, accountable editor, target provider count, editor's-choice facility, selection rationale, commercial relationships, launch date, and refresh cadence. Do not research or write until ownership and disclosure status are explicit.

## 2. Repository and data model

Create a new repository from a clean working baseline. Copy `assets/center-data.example.json` from the skill to a project-owned data file. Keep facts in this dataset/source register before placing them in prose.

The provider object represents a brand/editorial profile. The location object represents one physical facility. A provider can have multiple location objects, but an address, phone, rating, and review count must never cross location boundaries.

## 3. Provider discovery

Build a candidate list from state provider records, accreditation locators, official provider pages, and Google Business Profiles. Record inclusion criteria. Exclude providers that cannot be confidently matched to an in-scope physical location or documented service.

Search each facility by exact name plus city/state. Verify the listing heading and street before recording data. Capture exact GBP name, NAP, hours, website, Google URL, rating/count, visible distribution, date, and review themes. Then verify programs, licensing, and accreditation against first-party/authoritative sources.

Follow `references/research-and-sourcing.md`. Do not bypass technical controls, scrape patient data, or treat a directory claim as proof.

## 4. Editor's choice

Choose for a declared editorial use case, never overall clinical quality. Publish the dimensions and limitations. In the editorial description, put `The` before the facility name exactly once. Preserve the exact provider/GBP name everywhere factual: NAP, title when appropriate, source register, and schema.

Example rule:

```text
featuredDisplayName = exactName begins with "The " ? exactName : "The " + exactName
```

Use three sentences for the featured description: clinical scope; setting; concrete distinguishing features. Attribute public claims and tell readers what to confirm.

## 5. Content production

Build the actual directory as the first screen. Include scope/update date, calm safety language, transparent four-dimension comparison, provider shortlist, evidence matrix, and semantic FAQ clusters. Add one profile per provider with one NAP block per location, dated Google snapshot, balanced review themes, program links, and tailored questions.

Do not publish a lead-generation form unless the brief explicitly requires it and privacy/compliance review is complete. Never imply that the guide is the provider or that a phone routes to the guide when it is a provider number.

For a full topical hub, keep page content in a structured source model and generate committed static HTML. Every topic needs unique intent, a direct opening answer, decision points, provider-verification questions, visible authoritative sources, safety language, unique metadata and schema, and 4-8 related guides. Do not rely on client-side JavaScript to supply the primary crawlable copy.

## 6. Media

Use owned/licensed/permitted media. For a provider homepage screenshot, record URL, date, viewport, rights basis, hashes, and edits. Write factual contextual alt text, a dated caption, intrinsic dimensions, and a descriptive filename. Strip sensitive EXIF; never invent EXIF/GPS/camera/copyright. Follow `references/media-and-metadata.md` and maintain the asset register.

## 7. Entity SEO, schema, and AEO

Use canonical guide-owned entity IDs consistently. Add homepage `WebSite`/`WebPage`/`ItemList`; profile `WebPage` plus one location entity per facility; collection schema on sitemap/entity pages. Use official and Google URLs as references. Do not add third-party rating schema by default.

Make the entity map a subject knowledge layer, not merely a provider list. Define the geography, explicitly labeled editorial regions, treatment terms, substances, and the current official levels-of-care framework. Cite authoritative sources and never assign a clinical level to a provider without location-specific evidence.

Write answers that lead with the direct response and preserve qualifications. Align title, H1, canonical, copy, and schema. The Grove-style featured entity may receive deeper program relationships, but all providers need accurate entity identity.

## 8. Discovery files and internal linking

Create and connect:

```text
robots.txt -> sitemap.xml
sitemap.xml -> homepage + profiles + sitemap.html + entitymap.html
homepage footer -> sitemap.html + entitymap.html
sitemap.html <-> entitymap.html
sitemap.html -> every profile and machine file
entitymap.html -> every profile + official identity references
every profile -> homepage + sitemap.html + entitymap.html
llms.txt -> main sections + profiles + entity/discovery files + source/safety notes
entitymap.json -> stable IDs + relationships + provenance
```

Use a Search Console verification file at site root when supplied. Do not modify its token.

## 9. QA and publishing

Run the skill validator with the project dataset. Parse every schema block, JSON file, and XML file. Crawl internal links. Verify image loads, alt text, no overlap, keyboard controls, mobile/desktop layouts, canonical URLs, and external location identity.

Review the git diff; commit; push; watch deployment; and verify live 200 responses and correct content types. Submit `sitemap.xml` in Search Console. Record commit, release URL, editor, known gaps, and next review date.

## 10. Maintenance

Refresh volatile GBP facts monthly and program/accreditation facts quarterly. Investigate closures, regulatory changes, and corrections immediately. Preserve an audit trail. Never overwrite a conflict without documenting the source and editorial decision.

The complete operational rules live in the skill references; this SOP is the release sequence, not a substitute for those controls.
