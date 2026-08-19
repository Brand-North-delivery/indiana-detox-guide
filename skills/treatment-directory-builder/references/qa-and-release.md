# QA and Release

## Release gates

Data: exact sourced NAP per physical location; dates on volatile facts; conflicts visible; featured rationale non-clinical; ratings labeled third-party.

Content: exact source names in NAP/schema; featured editorial display begins with "The" exactly once; balanced themes; no guarantees; relevant FAQs; safety/correction language.

Technical: unique metadata and canonical; valid JSON-LD/stable IDs; responsive and accessible UI; factual alt text/rights records; working links; connected robots/sitemaps/entity maps/LLMs; correct live content types.

Project control: locked brief; evidence attached to every passed phase; zero release blockers; no unresolved decision that changes scope, disclosure, identity, conversion ownership, or canonical domain.

Design and experience: representative templates reviewed before propagation; all substantive pages contain purposeful media; no clipping, overlap, layout shift, unreadable controls, inaccessible focus, or mobile horizontal overflow; videos are responsive, titled, and source-labeled.

Production: one canonical HTTPS host; alternate hosts redirect in one hop; DNS answers from authoritative and public resolvers agree; no redirect loop; production pages contain the expected commit; forms and phone links reach their declared owners.

## Release procedure

1. Run `python scripts/validate_workflow.py project-brief.json production-state.json` and `python scripts/validate_directory.py <site-root> [center-data.json]`.
2. Run the internal crawler and parse every HTML, JSON-LD, JSON, XML, and discovery resource.
3. Serve locally; test homepage, editor's-choice profile, multi-location profile, longest topic title, indexes, images, video, and machine files.
4. Inspect representative desktop/mobile screenshots and measured overflow for every template class; test keyboard navigation and visible focus.
5. Review the git diff for unsupported claims, domain inconsistencies, unrelated files, secrets, temporary captures, and personal paths.
6. Create a preview deploy when supported; verify the same test matrix before production.
7. Commit and push the intended branch; watch production deployment to completion.
8. Verify live response codes, content types, canonical host, redirects, TLS, expected commit content, forms/phones, assets, sitemap, robots, entity maps, and `llms.txt`.
9. Submit XML sitemap in Search Console and retain verification without modifying its token.
10. Update production-state evidence and record commit, deploy ID, URL, editor, known limitations, and next refresh date.

## Handoff packet

Provide dataset/source register, asset rights register, repository/deployment boundaries, domain/Search Console/sitemap, featured rationale/disclosures, uncertainties, correction owner, and refresh date.

Also provide the locked brief, final production state, URL inventory, content/entity ownership map, recurring schedule, access that still requires a human owner, and a concise recovery procedure for deployment or domain failure.

Never store patient data, credentials, private contracts, or unpublished allegations in the repository.
