# Media, Alt Text, and Metadata

## Rights and provenance

Use only owned, commissioned, licensed, provider-approved, public-domain, or otherwise permitted media. Record source URL, owner, rights basis, acquisition date, attribution, and edits. Never remove watermarks or expose patient/private data.

## Homepage screenshots

Capture a current visible browser rendering when needed. Include enough context to identify the provider and facility; omit browser chrome, chats, and personal data. Record URL, date, viewport, and transformations. Caption it as a homepage screenshot with capture date.

## Alt text

Describe purpose and meaningful visible content, not keywords.

- Identify provider and visible subject.
- Say "screenshot" for screenshots.
- Include location only when supported.
- Never infer "luxury," "safe," or clinical capability from appearance.
- Use `alt=""` for decorative images.

Pattern: `Screenshot of [provider] homepage showing [specific visible subject] in [supported location].`

## File preparation

Use descriptive lowercase filenames, responsive formats/sizes, intrinsic dimensions, and visual-quality checks. Prefer AVIF/WebP for photos and PNG when screenshot text needs lossless rendering.

## EXIF, IPTC, and XMP

Metadata must be factual. Never invent camera, GPS, authorship, copyright, or dates.

- Screenshots have no meaningful camera EXIF. Record source, date, creator/publisher, description, and rights in an asset register or factual XMP/IPTC fields.
- Preserve required rights/credit metadata.
- Strip sensitive GPS, device IDs, usernames, and filesystem paths before publishing.
- Record original/output SHA-256 hashes and transformations.
- Do not rely on EXIF for SEO; visible context, alt text, captions, filenames, dimensions, performance, and entities matter more.

Useful factual fields: `Title`, `Description`, `Creator`, `CopyrightNotice`, `CreditLine`, `Source`, `DateCreated`, `WebStatementOfRights`, `DigitalSourceType`.

Maintain path/public URL, hashes, source, rights, dates, alt/caption, dimensions, size, transformations, editor, and review date for every asset.
