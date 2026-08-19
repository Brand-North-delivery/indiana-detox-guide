# Production Schedule and Gates

Use this as a dependency schedule, then map it to calendar dates and named owners in the project state. Durations are planning ranges, not promises.

## Phase schedule

| Phase | Typical range | Can run in parallel | Exit evidence |
|---|---:|---|---|
| 0. Intake and access | 0.5-2 days | repository/domain inventory | locked brief, access map, risk log |
| 1. Discovery and evidence | 2-7 days | provider, GBP, official-site, authority, review, and media research | candidate register, location records, claim citations, conflict log |
| 2. Architecture and design | 1-4 days | topical map, entity model, wireframes, design tokens, templates | URL inventory, link graph, schema plan, approved representative layouts |
| 3. Production build | 3-10 days | data ingestion, page templates, topic copy, media, profiles, discovery files | complete local build with no placeholder content |
| 4. Integrated QA | 1-4 days | factual, editorial, technical, visual, accessibility, structured-data reviews | blocker count zero; validator and crawler evidence |
| 5. Deployment and launch | 0.5-2 days plus DNS propagation | deploy preview, domain preparation, Search Console | production deploy, canonical host, HTTPS and redirect checks |
| 6. Handoff and maintenance | 0.5-1 day | documentation and owner training | handoff packet, cadence, correction route, next review date |

## Workstreams

- **Editorial:** brief, inclusion policy, editor's choice, disclosures, comparisons, tone, factual sign-off.
- **Research:** provider/location identity, authoritative claims, programs, reviews, citations, conflict tracking.
- **Content:** homepage, profiles, topical map, FAQs, source notes, safety language, internal-link anchors.
- **Design/media:** design system, responsive templates, assets, alt/captions, video, asset register, visual QA.
- **Engineering:** repository, generators/data model, schema, sitemaps, entity maps, `llms.txt`, analytics, forms, performance.
- **Release:** accessibility, browser/device checks, deployment, DNS/TLS/redirects, Search Console, monitoring, handoff.

Parallel work is allowed only after its inputs are stable. For example, profile rendering may begin from the approved data schema while research continues, but publishable prose cannot convert an unverified claim into fact.

## Daily control loop

1. Read the brief, state, unresolved decisions, and latest evidence dates.
2. Select the highest-priority unblocked gate, not the most visually interesting task.
3. Execute research/build/review work and attach outputs to the gate.
4. Run affected deterministic checks immediately.
5. Update gate status, owner, evidence, blocker, and next action.
6. Continue while useful work remains; request input only for a true external or editorial blocker.

## Recurring maintenance schedule

- **Weekly:** uptime, redirect chain, TLS, forms/phones, broken internal/external links, deployment failures.
- **Monthly:** GBP NAP/hours/rating count, closures, major program changes, correction inbox, Search Console coverage.
- **Quarterly:** provider programs, licensing/accreditation evidence, insurance language, topic freshness, competitor and topical-gap review, schema/discovery validation.
- **Semiannual:** full editorial comparison review, accessibility and performance audit, asset rights review, design-system consistency.
- **Immediate:** closure, enforcement action, ownership change, safety complaint requiring editorial review, broken conversion path, domain/TLS failure, or substantiated correction.

Each scheduled run creates a dated maintenance record, updates only supported facts, re-runs affected gates, and deploys only after QA. Never refresh dates without refreshing evidence.
