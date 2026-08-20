# Schema, AEO, and Discovery

## Stable entity IDs

Use guide-owned canonical IDs consistently:

- `/#website`, `/#organization`
- `/centers/{slug}/#page`
- `/centers/{slug}/#center` for one location
- `/centers/{slug}/#{city}` for multiple locations

Use official and Google URLs as identity/source references, not as replacements for guide IDs.

## Schema by page

- Homepage: `WebSite`, `WebPage`, real publisher `Organization`, `ItemList`
- Profile: `WebPage` plus one `MedicalBusiness`/`MedicalOrganization` per physical location
- Sitemap/entity map: `CollectionPage` and `ItemList`
- FAQ: `FAQPage` only when visible content and current eligibility rules support it

Include exact NAP and URLs. Never add unsupported specialties, hours, prices, ratings, or accreditation. Avoid third-party `AggregateRating`/`Review` markup unless rights and current policy clearly allow it.

## AEO

Answer named questions immediately; use consistent entities; make key paragraphs independently understandable; link claims to exact program pages; date volatile facts; publish provenance and verification questions; align title, H1, canonical, visible text, and schema.

## Discovery chain

1. `robots.txt` allows intended crawling and provides the absolute XML `Sitemap:` URL. Optional comments may label HTML sitemap, entity map, and `llms.txt` without inventing directives.
2. `sitemap.xml` lists canonical pages with accurate `lastmod`.
3. `sitemap.html` visibly links every page and discovery file.
4. `entitymap.html` explains the complete subject graph: geography; clearly labeled guide-defined regions; treatment and substance definitions; levels-of-care taxonomy; guide -> profile -> physical location relationships; and official identity references.
5. `entitymap.json` mirrors stable IDs, definitions, relationships, source URLs, provenance, and date. Do not assign a provider to a clinical level of care without authoritative, location-specific evidence.
6. `llms.txt` summarizes scope, method, profiles, featured rationale, sources, citation, and safety.

The HTML sitemap and entity map cross-link, list the complete inventory, and link relevant machine files. Link those discovery surfaces from a small utility location where useful, but do not force sitemap, EntityMap, or `llms.txt` links into every page header or footer. Priority topic pages should be reached through semantically aligned homepage FAQs and limited page-to-page chains; use a crawl test to prove complete reachability.

For addiction-treatment guides, include plain-language concepts such as substance use disorder, drug rehab, alcohol rehab, medical detox, residential treatment, outpatient treatment, co-occurring care, medications for addiction treatment, continuing care, and in-scope substances. Include the current ASAM continuum from official ASAM sources, label it educational, and state that ASAM level is not a ranking. Treat geographic groupings as editorial navigation regions unless they exactly reproduce a cited government boundary.

```text
User-agent: *
Allow: /

# Canonical crawler discovery
Sitemap: https://example.com/sitemap.xml

# Human and entity discovery
# HTML-Sitemap: https://example.com/sitemap.html
# Entity-Map: https://example.com/entitymap.html
# LLMs: https://example.com/llms.txt
```

Validate JSON-LD, XML, canonical consistency, unique IDs, reachability, live status, and content type.
