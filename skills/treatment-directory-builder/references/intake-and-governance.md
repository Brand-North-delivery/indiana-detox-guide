# Guided Intake and Governance

Use this reference for new builds and whenever an expansion changes scope, ownership, monetization, geography, or editorial preference.

## Interview behavior

Ask one to three questions per turn. Begin with decisions that change research scope or legal/editorial posture. Explain why a question matters when the answer changes cost, risk, or architecture. Summarize accepted answers after each round and record them in the project brief.

Offer a recommendation when useful, but label it as a recommendation. Infer only reversible, low-risk implementation details from the existing codebase. Never infer editor's choice, commercial relationships, clinical claims, phone ownership, form routing, domain ownership, licensed-media rights, or permission to publish.

If the user says "use your judgment," record the delegated decision and rationale. If answers conflict, surface the conflict before research or publishing. Do not repeatedly ask answered questions.

## Intake rounds

### 1. Identity and ownership

Ask for the guide/product name, canonical domain, publisher, accountable editor, repository organization, deployment owner, launch target, and who approves factual/editorial changes.

### 2. Audience and scope

Ask who the guide serves, treatment categories, age/population scope, geography, priority cities/counties/regions, travel intent, exclusions, and whether the guide is educational, commercial, provider-owned, or independent.

### 3. Editorial model

Ask which facility is editor's choice, why it fits a declared use case, whether any compensation/referral/ownership relationship exists, which alternatives must appear, and which comparison dimensions readers should see. If no editor's choice is selected, leave the designation unset.

### 4. Provider and evidence policy

Ask target provider count, inclusion/exclusion criteria, minimum evidence required, authoritative registries, recency threshold, treatment levels/substances to cover, review-source policy, and how unresolved conflicts should be displayed.

### 5. Topical and geographic priorities

Ask the areas that matter most for search and users: statewide versus city pages, regional definitions, treatment types, substances, insurance/cost, admissions, family/recovery, and special populations. Ask for the first three commercial or editorial priorities, not an unbounded keyword list.

### 6. Brand, media, and experience

Ask whether brand guidelines, logos, fonts, colors, photography, provider approvals, screenshots, video, maps, or testimonials exist and where rights records live. Establish whether missing media may be generated, captured from public provider pages for commentary, sourced under license, or must await supplied assets.

Ask about desired tone, reference sites, accessibility target, navigation expectations, forms, call buttons, maps, filters, and features that must not appear.

### 7. Technical and measurement

Ask for framework preference or existing stack, hosting, domain/DNS owner, analytics, consent requirements, Search Console verification, sitemap submission, redirects, email/form destination, and production access boundaries.

### 8. Maintenance and sign-off

Ask who owns corrections, monthly/quarterly refreshes, provider removals, review snapshots, program/accreditation changes, broken-link monitoring, security updates, and final launch approval.

## Brief lock gate

The brief is locked when these fields are explicit: canonical domain; publisher/editor; audience; geography and priority areas; treatment scope and exclusions; provider criteria/count; editor's choice or `null`; commercial disclosure; asset status; conversion policy; hosting/repository; launch approver; maintenance owner; definition of done.

Unknown non-blocking facts may remain as tracked questions. Do not label a brief locked while any of the above is merely assumed.
