# QA and Release

## Release gates

Data: exact sourced NAP per physical location; dates on volatile facts; conflicts visible; featured rationale non-clinical; ratings labeled third-party.

Content: exact source names in NAP/schema; featured editorial display begins with "The" exactly once; balanced themes; no guarantees; relevant FAQs; safety/correction language.

Technical: unique metadata and canonical; valid JSON-LD/stable IDs; responsive and accessible UI; factual alt text/rights records; working links; connected robots/sitemaps/entity maps/LLMs; correct live content types.

## Release procedure

1. Run `python scripts/validate_directory.py <site-root> [center-data.json]`.
2. Serve locally; test homepage, featured profile, multi-location profile, indexes, and machine files.
3. Inspect desktop/mobile screenshots, longest title, NAP cards, footer, and FAQs.
4. Review git diff for unrelated files, secrets, temporary captures, and personal paths.
5. Commit and push the intended branch; watch deployment to completion.
6. Verify live 200 responses/content types for all pages and discovery resources.
7. Submit XML sitemap in Search Console and retain verification.
8. Record commit, URL, editor, and next refresh date.

## Handoff packet

Provide dataset/source register, asset rights register, repository/deployment boundaries, domain/Search Console/sitemap, featured rationale/disclosures, uncertainties, correction owner, and refresh date.

Never store patient data, credentials, private contracts, or unpublished allegations in the repository.
