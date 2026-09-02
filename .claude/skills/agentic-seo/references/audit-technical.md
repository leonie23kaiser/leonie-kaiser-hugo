# audit-technical

Run a stricter technical SEO audit against the local preview.

This is the runtime-focused audit. It should verify what the browser actually renders on representative local routes and capture issues that code inspection alone can miss: rendered metadata, JSON-LD output, Lighthouse failures, shared CTA defects, contrast problems, accessible-name mismatches, and other template-level regressions.

## 🚫 BLOCKING: Do NOT Read `.seo/` Until Audit Is Complete

**The `.seo/` directory is off-limits during audit execution.** Do NOT list, read, search, or inspect any file under `.seo/` until AFTER every audit section is written and all scores are assigned. Reason: prior audit findings contaminate the fresh snapshot. The only time `.seo/` is touched is during the Baseline-Finding Algorithm (after scoring), comparison file generation (after scoring), and the Runs Log update (after writing).

## 🚫 BLOCKING: No Baseline in Audit Body

**Every run is a fresh independent snapshot.** The baseline only exists at the very end — in the auto-generated `SEO_AUDIT-TECHNICAL-comparrison.md` file — and only as a numeric comparison. Violations:

- ❌ Do NOT label findings as "Persists", "New finding", "Improved", or "Resolved (by architecture)"
- ❌ Do NOT mention a previous audit, baseline date, or prior score in the header, Executive Summary, or any audit section
- ❌ Do NOT reference "the last audit", "previous run", or a prior date anywhere in the body
- ✅ State every finding on its own merits as if this is the FIRST audit ever run
- ✅ Only invoke the Baseline-Finding Algorithm AFTER all sections are written and scored

## 🚫 BLOCKING: Audit Only Public Crawl Surface

- Build the audited route set from `robots.txt`, `sitemap.xml`, visible navigation, and public links discovered from those pages.
- Do not force-check guessed routes or hidden collection URLs unless they are exposed in public runtime output or explicitly named by the user.
- Do not create findings from hidden Hugo structure, front matter, `headless`, `build.render`, `build.list`, `hugo.toml` menu internals, or checked-in generated output unless they leak into public runtime output.
- Use code inspection only to confirm the root cause of a public runtime defect.
- Do not score local preview host/port mismatches as SEO defects. They are local audit-environment notes unless the same mismatch exists on a public deployment or the user explicitly asks to debug the local setup.

## Local-First Execution Policy

- Audit the local Hugo preview or another local/dev URL by default.
- Reuse an existing local browser session if one is already running.
- Do not start a new preview process when the user has already provided a running app.
- Prefer browser/runtime inspection over terminal-driven discovery.
- Do not open or inspect production URLs unless the user explicitly asks for production testing.
- If the local preview is unavailable, limit the audit to public artifacts the user explicitly provided and clearly note that runtime verification could not be completed.

## Triggers
"technical seo audit", "local seo audit", "runtime seo audit", "lighthouse seo audit", "chrome devtools seo"

## When to Use
- Validate a local optimization sprint before or after code changes
- Check rendered titles, descriptions, canonicals, links, headings, JSON-LD, and images on key routes
- Confirm whether a fix actually landed in runtime output
- Produce a technical-only series that can be compared without mixing in broader strategic audits

## Preferred Audit Inputs

1. Local Hugo preview URL, for example `http://localhost:1313/`
2. Browser checks on `robots.txt`, `sitemap.xml`, visible navigation, and representative public routes discovered from those sources
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
- Do not turn local preview host/port differences into SEO findings or score deltas unless the same issue is visible on a public deployment.
- `web_fetch` and `curl` cannot reliably detect runtime JSON-LD. Verify with:

```js
document.querySelectorAll('script[type="application/ld+json"]')
```

- Treat Lighthouse issues as runtime evidence, then confirm the root cause in templates or CSS before prescribing fixes.

## Audit Priority Order

1. Crawlability and rendered metadata on public routes discovered from nav, sitemap, and robots
2. Canonicals, schema output, and structured-data correctness on those public routes
3. Lighthouse SEO, accessibility, and best-practices failures caused by shared templates on public pages
4. CTA text quality, contrast, accessible names, and other repeated UI defects visible on public pages
5. Re-run guidance for confirming the next local plateau

---

## Technical SEO Reference

Core technical foundations — crawlability, indexation, performance, mobile, security, URL structure, and international SEO.

### Crawlability

#### robots.txt

```text
User-agent: *
Allow: /

# Block admin/private areas only
Disallow: /admin/
Disallow: /api/
Disallow: /private/

# DO NOT block /static/ or CSS/JS — needed for rendering

# AI bots (see ai-geo.md for full list)
User-agent: GPTBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: https://example.com/sitemap.xml
```

**Check for:**
- No unintentional blocks on important pages
- Sitemap URL referenced
- AI bots not blocked (critical for AI citation — see `ai-geo.md`)
- CSS/JS files accessible (Google needs them to render pages)

#### XML Sitemap

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2024-01-15</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

**Best practices:**
- Max 50,000 URLs or 50MB per file — use sitemap index for larger sites
- Include only canonical, indexable URLs
- Update `lastmod` when content actually changes
- Submit to Google Search Console and Bing Webmaster Tools
- Separate sitemaps by content type (blog, products, pages)

#### Site Architecture

Score only the public crawl surface. Do not treat intentionally hidden or non-public collection routes as defects unless they appear in visible navigation, `sitemap.xml`, `robots.txt`, or public HTML.

- Important pages within 3 clicks of homepage
- Logical hierarchy with breadcrumbs
- No orphan pages (every page reachable from navigation or internal links)
- Crawl budget: manage parameterized URLs, faceted navigation, session IDs

### Indexation

#### Diagnosing Index Issues

| Check | Method |
|-------|--------|
| Index status | `site:domain.com` in Google |
| Coverage details | Search Console → Indexing → Pages |
| Indexed vs. expected | Compare GSC count to actual page count |

#### Common Indexation Problems

- `noindex` tags on pages that should rank
- Canonicals pointing the wrong direction
- Redirect chains or loops
- Soft 404s (pages returning 200 but showing "not found" content)
- Duplicate content without canonical tags
- Blocked resources (CSS/JS) preventing rendering

#### Canonicalization Rules

- Every page has a canonical tag (self-referencing on unique pages)
- HTTP → HTTPS consistent
- www vs. non-www consistent (pick one, redirect the other)
- Trailing slash consistent across the site
- Pagination: self-referencing canonical per page (never canonical page 2+ to page 1)

```html
<link rel="canonical" href="https://example.com/current-page">
```

### Core Web Vitals & Speed

#### Targets

| Metric | Good | Needs Work | Poor |
|--------|------|------------|------|
| LCP (Largest Contentful Paint) | < 2.5s | 2.5–4s | > 4s |
| INP (Interaction to Next Paint) | < 200ms | 200–500ms | > 500ms |
| CLS (Cumulative Layout Shift) | < 0.1 | 0.1–0.25 | > 0.25 |

#### Key Speed Factors

- **TTFB** (Time to First Byte) — server response, hosting, CDN
- **Image optimization** — compress, use WebP/AVIF, set explicit width/height, lazy load below fold
- **JavaScript** — defer non-critical JS, eliminate render-blocking scripts
- **CSS** — inline critical CSS, defer non-critical
- **Fonts** — `font-display: swap`, preload key fonts
- **Caching** — proper cache headers, CDN for static assets

**Tools:** PageSpeed Insights, Chrome DevTools, Search Console CWV report

### Mobile

- Responsive design (not a separate m. subdomain)
- Same content as desktop (mobile-first indexing)
- Viewport configured: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- Tap targets ≥ 48px with adequate spacing
- No horizontal scroll
- Font size ≥ 16px (no zooming needed)
- No intrusive interstitials

### HTTPS & Security

- HTTPS across entire site
- Valid SSL certificate (check expiry)
- No mixed content (all assets served over HTTPS)
- HTTP → HTTPS 301 redirects
- HSTS header (bonus): `Strict-Transport-Security: max-age=31536000; includeSubDomains`

### URL Structure

```
✅ Good:
https://example.com/services/software-integration
https://example.com/blog/how-to-integrate-apis

❌ Poor:
https://example.com/p?id=12345
https://example.com/services/item/category/sub/software-integration-2024-sale
```

**Rules:**
- Hyphens, not underscores
- Lowercase only
- Keep short (< 75 characters)
- Include target keywords naturally
- Avoid parameters where possible
- Consistent trailing slash strategy

### International SEO (Hreflang)

Only relevant for multi-language or multi-regional sites.

#### Implementation Options

Three equivalent methods — pick one and be consistent:
1. HTML `<link>` tags in `<head>`
2. HTTP `Link` response headers
3. XML sitemap `<xhtml:link>` entries (preferred for 10+ locales — no page weight)

```html
<!-- Every page must include itself (self-referencing entry) -->
<link rel="alternate" hreflang="en" href="https://example.com/page">
<link rel="alternate" hreflang="de" href="https://example.com/de/page">
<link rel="alternate" hreflang="x-default" href="https://example.com/page">
```

#### Critical Rules

- **Self-referencing entry required** on every page — missing this invalidates all hreflang for that page
- **Reciprocal links required** — if A points to B, B must point back to A
- **Valid codes only** — ISO 639-1 language + optional ISO 3166-1 region (`en`, `en-GB` — never `en-UK`)
- **`x-default` required** — points to language selector or default locale
- **All target URLs must return 200, be indexable, and match their canonical**
- **Never cross-locale canonical** — if French page canonicals to English, it suppresses the French version entirely

#### Common Hreflang Errors

| Error | Consequence |
|-------|-------------|
| Missing self-referencing entry | All hreflang ignored for that page |
| No return tag (A→B but not B→A) | Pair dropped |
| Invalid code (e.g., `en-UK`) | Silently ignored — use `en-GB` |
| Hreflang target is 404 or blocked | Cluster discarded |
| HTML and sitemap annotations disagree | Conflicting pair dropped |
| Cross-locale canonical | Suppresses the non-canonical locale |

#### Locale URL Structure

- **Recommended:** Subdirectories (`/en/`, `/de/`)
- **Acceptable:** Subdomains or ccTLDs
- **Avoid:** URL parameters (`?lang=en`)
- Never use IP-based or Accept-Language content negotiation — Googlebot uses US IPs with no Accept-Language header

#### Content Quality for Locales

- Translate ALL page content (title, description, headings, body) — not just boilerplate/nav
- AI-translated content is acceptable but must add genuine value; scaled thin translations trigger scaled content abuse policy
- Thin locale pages drag down site-wide quality — don't create locale pages you can't make genuinely helpful
- Don't noindex thin locales or cross-locale canonical — fix the content instead

### Common Technical Issues by Site Type

| Site Type | Watch For |
|-----------|-----------|
| Hugo / Static sites | Sitemap configuration, canonical format, trailing slash consistency |
| SaaS | JS-rendered content not indexed, app routes blocked, auth walls |
| E-commerce | Faceted navigation duplicates, parameterized URLs, out-of-stock pages |
| Multi-language | Hreflang errors, cross-locale canonicals, untranslated content |
| Large sites | Crawl budget, redirect chains, orphan pages |
