# SEO & JSON-LD

## Meta tags (`partials/head.html`)

Every page outputs:

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#086584">
<meta name="color-scheme" content="light">

<title>...</title>
<meta name="description" content="...">

<meta property="og:locale" content="de_AT">
<meta property="og:site_name" content="...">
<meta property="og:type" content="website">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:url" content="...">
<meta property="og:image" content="...">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="...">
<meta name="twitter:description" content="...">
<meta name="twitter:image" content="...">

<link rel="canonical" href="...">
```

### Title format

- **Homepage:** `site.Title` (from `config.toml`)
- **Every other page:** `.Title` (page front matter) — used as-is, **not** appended with a site-name suffix.

`params.toml`'s `seoHomeTitle` and `seoSiteTitle` are **not used** by this logic (dead params, kept for now — see [config.md](config.md)). To change the homepage title, edit `config.toml`'s `title`.

### OG image fallback chain

The `og:image` value is picked in this order:

1. Page frontmatter `image` (if set)
2. Page frontmatter `ogImage` (if set — overrides `image` if both are present)
3. `static/images/og-default.png` (the global fallback, 1200×630, branded)

Blog posts currently use `cover`/`coverAlt` (see [content-model.md](content-model.md)) for the on-page image, which is a separate field from `image`/`ogImage` — set `image:` too if a post needs a distinct OG/Twitter image.

## Canonical URL

Hugo emits `<link rel="canonical">` automatically from `baseURL` + page permalink: `https://leoniekaiser.com/<path>/`.

## RSS

**Active.** `config.toml` sets `outputs.home = ['HTML','RSS']` — the homepage RSS feed is generated at `/index.xml`.

## JSON-LD structured data (`partials/schema.html`)

Renamed from `seo-jsonld.html` at some point — the file is now `schema.html`. Uses Hugo `dict` + `jsonify` throughout (type-safe, no string templates). Every page emits **one `<script type="application/ld+json">` with a single `@graph`**, assembled conditionally depending on page type/section.

### Always present, on every page

- **`Person`** (`@id` `#person`) — Leonie: `name`, `jobTitle`, `description`, `url` (`/ueber-mich/`), `image`, `sameAs` (LinkedIn), `worksFor` → Organization `@id`, `knowsAbout`, `knowsLanguage`, `address`.
- **`ProfessionalService`** (`@id` `#organization`) — `name`, `alternateName`, `description`, `url`, `logo`, `image`, `founder` → Person `@id`, `vatID`, `areaServed` (AT/DE/CH), `address`, `contactPoint` (email, phone, languages), and a `hasOfferCatalog` listing the three service tiers (Potenzialanalyse, Strategie & Beratung, Implementierung & Automatisierung) as `Offer`/`Service` pairs.
- **`WebSite`** (`@id` `#website`) — `url`, `name` (`site.Title`), `inLanguage`, `publisher` → Organization `@id`.
- **`ContactPage`** (`@id` `#contactpage`) — points at `/#kontakt` (the homepage contact form section).

### Conditional, added to the same `@graph` when applicable

| Condition | Adds |
|---|---|
| Page has `.Params.faqs` front matter | `FAQPage` with `mainEntity` built from each `{q, a}` pair |
| `.Type == "ueber-mich"` | `AboutPage`, `mainEntity` → Person `@id` |
| `.Section == "journal"` and it's a single post (not the list page) | `Article` — `headline`, `description`, `datePublished`/`dateModified`, `author`/`publisher` → Person/Org `@id`, plus `image` (from `.Params.featured_image`, if set) and `keywords` (from `.Params.tags`) |
| Not the homepage | `BreadcrumbList` — Start → (Blog →) current page. Journal posts get a 3-level trail (Start / Blog / post); everything else gets 2 levels |
| Homepage or `.Type == "ueber-mich"` | `WebPage` with a `SpeakableSpecification` targeting `h1`, `.htagline`, `.lead-speakable` |

**Every page that sets `faqs:` in front matter gets `FAQPage` automatically** — this is how `/faq/`, `/eu-ai-act/`, and `/dsgvo/` all emit valid FAQ rich-result markup without page-specific code in `schema.html`.

**Note a gap vs. `CLAUDE.md`'s project summary:** that file lists the `@graph` as including `Service`, `AggregateRating`, and `Reviews` types. As of this writing, `schema.html` does **not** emit any of those three (services are nested `Offer`/`Service` dicts inside the Organization's `hasOfferCatalog`, not standalone top-level types, and there's no ratings/reviews data anywhere). If someone adds them to `schema.html`, this doc is the place to record what they look like.

### Blog post `Article` — no longer "future"

Earlier drafts of this doc described the `Article` branch as dormant, waiting for the first blog post. The blog is live (`content/journal/`, first post published 2026-08-04) — the `Article` branch fires automatically for every post under `/blog/<slug>/`.

## Sitemap

Hugo emits `sitemap.xml` automatically (`config.toml`'s `[sitemap]` sets `changefreq = 'monthly'`, `priority = 0.7` as defaults; individual pages override via their own `sitemap:` front matter). No `categories/`/`tags/` listing pages — `disableKinds = ["taxonomy", "term"]` in `config.toml` removes them entirely.

## Robots & AI/GEO

`static/robots.txt` controls crawler rules — AI bots are explicitly allowed (not blocked). `static/llms.txt` is an AI/GEO-oriented plain-text summary of the site (services, packages, pages) aimed at LLM-based assistants and search — keep it in sync when service pages, packages, or pricing change; nothing generates it automatically.

## Audit checklist (manual, before deploy)

1. View source on `/`. Confirm:
   - `<title>` matches `config.toml`'s `title`
   - `og:image` is the branded `og-default.png` (or a page-specific override)
   - JSON-LD validates (paste into Schema.org Validator or Google's Rich Results Test)
2. Test OG preview at `https://www.opengraph.xyz/url/https%3A%2F%2Fleoniekaiser.com`
3. Test a social unfurl (Twitter's legacy card validator is gone; preview via a private LinkedIn or Slack post instead)
4. Run Lighthouse mobile — target SEO ≥ 95, Performance ≥ 90, Accessibility ≥ 95
