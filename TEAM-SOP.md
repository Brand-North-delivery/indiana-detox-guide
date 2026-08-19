# Treatment Directory Production SOP

This is the human operating procedure for `skills/treatment-directory-builder`. It covers a new geography/category guide, a site expansion, and recurring refreshes. The skill is the agent entrypoint; the project brief and production state are the shared source of truth.

## 1. Start the project

Invoke the skill with a plain request such as:

```text
Start a new treatment directory project. Interview me, create the brief and production state, and continue through research, build, deployment, and live QA until every release gate passes.
```

For an empty repository, initialize the durable control files first:

```bash
python skills/treatment-directory-builder/scripts/init_project.py .
```

This creates the brief, production state, provider dataset, URL inventory, source register, asset register, and maintenance log without overwriting existing files.

The agent asks one to three focused questions at a time. Expect questions about:

- guide name, canonical domain, publisher, editor, repository, hosting, launch owner;
- audience, treatment scope, priority states/cities/regions, exclusions, travel intent;
- provider count, inclusion rules, editor's choice, rationale, commercial relationships;
- important topic clusters, substances, geographic pages, cost/insurance and family priorities;
- brand kit, logos, provider images, screenshots, video, licenses, missing-asset policy;
- forms, phone ownership, analytics, privacy, Search Console, DNS, maintenance owners.

Answer decisions directly or explicitly delegate them. The agent must not infer editor's choice, sponsorship, clinical inclusion rules, asset rights, form routing, or domain ownership.

## 2. Lock the brief

Copy `assets/project-brief.example.json` into the new repository as `project-brief.json` and replace every example value. A new build does not enter provider research until the brief records:

- canonical domain and accountable publisher/editor;
- audience, geography, priority areas, treatment scope, populations, exclusions;
- provider target and inclusion/exclusion criteria;
- editor's choice or `null`, rationale, and commercial disclosure;
- comparison dimensions and review policy;
- topical priorities and regional model;
- asset inventory and missing-media policy;
- conversion, phone, analytics, consent, hosting, domain, Search Console, and maintenance owners;
- measurable definition of done.

Create `production-state.json` from the skill template. Use it for status, evidence, blockers, metrics, release IDs, and next actions. A chat summary is not a substitute.

## 3. Schedule and assign work

Use the dependency schedule in `references/production-schedule.md`. Assign named owners to Editorial, Research, Content, Design/Media, Engineering, and Release. Work may run in parallel only after its inputs are stable and ownership surfaces do not conflict.

Every delegated assignment specifies source inputs, allowed claims, deliverable path/format, exclusions, and completion test. One controller owns the brief, canonical IDs, design tokens, production state, integration, and release decision.

## 4. Research providers and locations

Create a candidate list from state provider records, accreditation locators, official provider pages, and Google Business Profiles. Record inclusion and exclusion decisions. Exclude providers that cannot be confidently matched to an in-scope physical location and documented relevant service.

The provider object represents a brand/editorial profile. The location object represents one physical facility. Never cross addresses, phones, hours, reviews, credentials, or programs between locations.

For each location capture exact GBP name, NAP, hours, official site, Google URL, rating/count, review date/distribution where visible, balanced themes, and conflicts. Verify programs, licensing, and accreditation through first-party or authoritative sources. Record claims and evidence before prose.

Do not bypass controls, collect patient data, publish allegations, or treat directory/marketing language as authoritative proof.

## 5. Define editor's choice

Choose for a declared editorial use case, never overall clinical quality. Publish dimensions, evidence, commercial relationship, and limitations. Preserve exact source names in NAP, title where appropriate, data, and schema.

In the editorial description only, prefix `The` exactly once:

```text
featuredDisplayName = exactName begins with "The " ? exactName : "The " + exactName
```

Use three sentences when requested: documented clinical scope; setting; concrete distinguishing features. Attribute provider claims and state what readers must verify.

## 6. Build the topical and entity maps

Create a URL inventory before drafting. Each row records URL, primary intent, audience stage, parent hub, evidence, media, schema type, inbound links, outbound links, and status.

Plan around the brief's priority areas, not generic keyword volume alone. Cover only useful, differentiated intents across treatment types, substances, cost/insurance, admissions, families/recovery, special populations, and clearly labeled geographic regions. Merge thin or competing pages.

Define the guide, publisher, geography, editorial regions, providers, physical locations, programs, substances, treatment terms, and current official levels-of-care framework. Do not assign a provider an ASAM level without location-specific evidence.

## 7. Design and build representative templates

Build the usable directory as the first screen, not a marketing landing page. Establish design tokens and approve representative examples before propagation:

- homepage and comparison experience;
- single-location and multi-location profiles;
- treatment, substance, planning, family, and geographic topic pages;
- HTML sitemap/entity map and utility states;
- longest title, largest NAP block, longest button, image, and video cases.

Keep pages calm, specific, accessible, and efficient. Use stable responsive dimensions. No lead form unless the brief authorizes it and privacy/compliance ownership is recorded. Phone links must identify their owner.

## 8. Produce content and internal links

Generate committed static HTML from structured data when the site has a substantial topical map. Each topic requires unique intent, a direct opening answer, decision points, provider-verification questions, visible authoritative sources, safety language, unique metadata/schema, purposeful media, and natural links to its hub, related topics, and relevant profiles.

Internal-link model:

```text
homepage -> hubs + comparison + profiles + discovery pages
hubs -> child topics + relevant profiles
topics -> parent hub + 4-8 related topics + useful profile + discovery footer
profiles -> comparison + relevant topics + sitemap + entity map
sitemap.html <-> entitymap.html
robots.txt -> sitemap.xml
sitemap.xml -> every canonical public page + discovery resources
llms.txt -> main sections + profiles + entity/discovery files + safety/source notes
```

Use descriptive anchors. Avoid orphan pages, boilerplate link blocks, circular redirects, and absolute preview-domain links.

## 9. Acquire and document media

Every substantive page needs purposeful owned, licensed, permitted, provider-approved, or guide-generated media. Utility verification and machine files are exempt.

For each asset record public path, source URL, owner, rights basis, acquisition/capture date, attribution, dimensions, file size, SHA-256, transformations, factual alt text, caption, editor, and review date. Never invent EXIF, GPS, camera, authorship, copyright, or location claims. Strip sensitive metadata.

Provider screenshots must be dated and labeled as screenshots. Generic/generated imagery must explicitly say it does not depict the provider. Provider video must be responsive, titled, source-labeled, lazy-loaded where appropriate, and represented by matching `VideoObject` schema.

## 10. Implement schema, AEO, and discovery

Use one canonical HTTPS base and stable guide-owned `@id` values. Keep visible copy and schema aligned. Add the appropriate page/entity graph for the homepage, profiles/locations, topics, images/video, breadcrumbs, and collection/discovery pages.

Create and connect `robots.txt`, `sitemap.xml`, `sitemap.html`, `entitymap.html`, `entitymap.json`, and `llms.txt`. Use official and Google URLs as sources/identity references. Do not mark up third-party Google reviews as guide-owned `Review` or `AggregateRating` by default.

Search Console verification files stay unchanged at the root. Canonicals, schema, sitemap, robots, entity maps, `llms.txt`, Open Graph URLs, and redirects must use the production domain, never a GitHub or deploy-preview hostname.

## 11. Iterate through QA

Run the review loop in this order: data truth, content utility, architecture/internal links, experience/accessibility, technical/schema/discovery, then production/domain. Convert every failure into a production-state item with severity, owner, evidence, and retest.

Required checks:

```bash
python skills/treatment-directory-builder/scripts/validate_workflow.py project-brief.json production-state.json
python skills/treatment-directory-builder/scripts/validate_directory.py . center-data.json
```

Also crawl internal links; parse all JSON-LD/JSON/XML; verify image/video loads and metadata; inspect every template at representative desktop/mobile widths; test keyboard/focus, overflow, longest content, forms/phones, and error states; review the git diff for unsupported claims, secrets, temporary files, and domain mismatches.

Continue fixing and retesting while an actionable failure remains. Stop only for an unresolved editorial decision, source conflict, credential/permission, licensed asset, external account action, or unavailable testing capability. “Looks good” is not a release gate.

## 12. Preview, deploy, and verify live

Use a preview deploy where supported, then deploy production only after local and preview gates pass. Record commit and deploy ID.

Verify the canonical host, alternate-host one-hop redirects, authoritative/public DNS agreement, HTTPS/TLS, no redirect loops, expected commit content, response codes/content types, every sitemap URL, images/video, forms/phones, analytics/consent, robots, sitemap, entity maps, and `llms.txt`. Submit the XML sitemap in Search Console.

Do not diagnose DNS from one resolver. Compare authoritative nameservers, public resolvers, and the local resolver; account for TTL and propagation before changing records.

## 13. Handoff and maintenance

Hand off the locked brief, final production state, source/provider dataset, candidate/conflict log, asset register, URL inventory, entity/link map, repository and hosting boundaries, domain/DNS ownership, Search Console verification, editor's-choice rationale/disclosure, correction route, known limitations, recovery procedure, commit/deploy ID, and next review date.

Schedule:

- weekly uptime, TLS/redirect, forms/phones, broken links, deploy failures;
- monthly GBP NAP/hours/reviews, closures, program changes, corrections, Search Console;
- quarterly programs, licensing/accreditation, insurance language, topic gaps/freshness, schema/discovery;
- semiannual editorial comparison, accessibility/performance, asset rights, design consistency;
- immediate response to closures, enforcement/ownership changes, substantiated corrections, broken conversion, or domain/TLS failure.

Never update a review date without refreshing its evidence. Preserve the audit trail.

## Completion rule

The project is finished only when all seven production-state phases are `passed`, both validators and the crawler pass, representative desktop/mobile reviews pass, the canonical live domain passes DNS/TLS/redirect and content checks, release blockers are zero, and the handoff names owners and the next review date. Report residual non-blocking risk; do not call a website perfect merely because it launched.
