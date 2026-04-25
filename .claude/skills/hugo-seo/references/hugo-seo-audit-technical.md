# hugo-seo-audit-technical

Run a stricter technical SEO audit against the local preview.

This is the runtime-focused audit. It should verify what the browser actually renders on representative local routes and capture issues that code inspection alone can miss: rendered metadata, JSON-LD output, Lighthouse failures, shared CTA defects, contrast problems, accessible-name mismatches, and other template-level regressions.

## Local-First Execution Policy

- Audit the local Hugo preview or another local/dev URL by default.
- Reuse an existing local browser session if one is already running.
- Do not open or inspect production URLs unless the user explicitly asks for production testing.
- If the local preview is unavailable, continue with code inspection and clearly note that runtime verification could not be completed.

## Triggers
"technical seo audit", "local seo audit", "runtime seo audit", "lighthouse seo audit", "chrome devtools seo"

## When to Use
- Validate a local optimization sprint before or after code changes
- Check rendered titles, descriptions, canonicals, links, headings, JSON-LD, and images on key routes
- Confirm whether a fix actually landed in runtime output
- Produce a technical-only series that can be compared without mixing in broader strategic audits

## Preferred Audit Inputs

1. Local Hugo preview URL, for example `http://localhost:1313/`
2. Chrome DevTools checks on representative routes such as `/`, `/classes/`, a class detail page, an area page, `robots.txt`, and `sitemap.xml`
3. Local code inspection for root-cause confirmation when a runtime defect appears

## Audit Output Convention

Technical audits use the `TECHNICAL` series:

```
.seo/YYYY-MM-DD/SEO_AUDIT-TECHNICAL-hhmm.md         ← runtime audit snapshot
.seo/YYYY-MM-DD/SEO_AUDIT-TECHNICAL-comparrison.md  ← latest technical comparison
.seo/readme.md                                      ← runs log + type-specific charts
```

## Baseline-Finding Algorithm

1. List `.seo/{today}/` and find `SEO_AUDIT-TECHNICAL-*.md`
2. Sort by `hhmm` descending and use the latest same-type run as baseline
3. If no same-type file exists today, scan earlier date folders for the latest `SEO_AUDIT-TECHNICAL-*.md`
4. If no typed technical baseline exists yet, mark the run as the first technical snapshot instead of comparing it to a general audit
5. Write the new audit as `SEO_AUDIT-TECHNICAL-{current hhmm}.md`
6. Auto-generate or update `SEO_AUDIT-TECHNICAL-comparrison.md`
7. Append a `Technical` row in `.seo/readme.md` and update only the technical chart

## Runs Log

Append to `.seo/readme.md` under `## SEO Runs` with newest rows first:

| Date | Time | Type | Score | Technical SEO | On-Page SEO | Content Quality | Authority |

Only update the technical progression chart when this skill writes a new run.

## Verification Notes

- Prefer browser inspection over raw HTML fetches for schema and rendered metadata.
- `web_fetch` and `curl` cannot reliably detect runtime JSON-LD. Verify with:

```js
document.querySelectorAll('script[type="application/ld+json"]')
```

- Treat Lighthouse issues as runtime evidence, then confirm the root cause in templates or CSS before prescribing fixes.

## Audit Priority Order

1. Crawlability and rendered metadata on local routes
2. Canonicals, schema output, and structured-data correctness
3. Lighthouse SEO, accessibility, and best-practices failures caused by shared templates
4. CTA text quality, contrast, accessible names, and other repeated UI defects
5. Re-run guidance for confirming the next local plateau