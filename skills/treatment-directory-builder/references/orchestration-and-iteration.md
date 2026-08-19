# Agent Orchestration and Iteration

Use this reference when multiple agents/workstreams are available or the project needs repeated quality cycles.

## Controller role

One controller owns the brief, production state, dependency order, integration decisions, and release status. Delegate bounded outputs, not "make the site perfect." Every assignment names inputs, allowed sources, deliverable path/format, evidence requirements, exclusions, and completion test.

Agents may research, draft, implement, or audit in parallel when they do not edit the same ownership surface. The controller resolves conflicts and integrates changes. Never allow separate agents to invent competing canonical domains, entity IDs, provider names, or design tokens.

## Recommended specialist passes

- **Research pass:** one provider/location set at a time; return evidence records and conflicts, not marketing prose.
- **Topical-map pass:** cluster intents, user journeys, geographic priorities, cannibalization risks, and internal-link relationships.
- **Content pass:** write only from approved evidence and templates; flag unsupported claims.
- **Media pass:** source/generate/capture assets, record rights/provenance, and provide factual alt/captions.
- **Schema/discovery pass:** map visible entities and relationships; validate canonical consistency and crawl discovery.
- **Design pass:** implement representative templates first, then propagate after desktop/mobile approval.
- **Adversarial QA pass:** seek factual conflation, unsupported claims, broken journeys, accessibility failures, schema mismatch, and domain/redirect errors.

## Iteration loop

Run each review in this order:

1. **Data truth:** location boundaries, exact names, dates, citations, conflicts, disclosures.
2. **Content utility:** direct answers, intent coverage, decision support, balanced language, no repetition or thin pages.
3. **Architecture:** crawl depth, semantic anchors, hub/cluster links, breadcrumbs, orphan and duplicate-intent checks.
4. **Experience:** representative desktop/mobile screenshots, navigation, long text, forms/phones, keyboard/focus, image/video rendering.
5. **Technical:** HTML, assets, performance, metadata, canonical, schema, robots, sitemap, entity map, `llms.txt`.
6. **Production:** deploy output, canonical host, redirects, DNS/TLS, live links/content types, analytics/Search Console.

Convert every failure into a state-file gate item with severity, owner, evidence, and retest. Fix blockers and regressions first. Re-run the smallest affected tests, then the full release suite before launch.

## Stop conditions

Continue autonomously while a documented failure has a safe, authorized fix. Do not loop on subjective polish after all acceptance criteria pass. Stop and request input when:

- the editor's choice, disclosure, inclusion rule, or target geography is unresolved;
- access, credentials, DNS, publishing permission, or licensed assets are required;
- sources materially conflict and the editorial resolution changes publication;
- a live external mutation requires authorization or human verification;
- the requested outcome cannot be tested with available tools.

Record blocked work and proceed with independent work. Completion means all release gates pass, not that no future improvement is imaginable.

## Required completion report

Report scope delivered, production URL, commit/deploy ID, evidence review date, page/profile/topic counts, validator and crawler results, representative visual checks, domain/redirect/TLS status, Search Console/sitemap status, residual non-blocking risks, and next scheduled review.
