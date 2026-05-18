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

- **Homepage:** `params.seoHomeTitle` → `"Leonie Kaiser – KI & Business Consulting · Wien"`
- **Other pages:** `<page.Title> – <params.seoSiteTitle>` → e.g. `"Impressum – Leonie Kaiser"`

Update `seoSiteTitle` and `seoHomeTitle` in `config/_default/params.toml`.

### OG image fallback chain

The `og:image` value is picked in this order:

1. Page frontmatter `ogImage` (if set)
2. Page frontmatter `image` (if set)
3. `static/images/og-default.png` (the global fallback, 1200×630, branded)

When adding a blog post or case study with a unique cover, set `image: "images/cases/foo.jpg"` in the frontmatter — OG and Twitter will pick it up automatically.

## Canonical URL

Hugo emits `<link rel="canonical">` automatically from `baseURL` + page permalink. Currently `https://leoniekaiser.com/<path>/`.

## RSS discovery

Not active. `config.toml` sets `outputs.home = ['HTML']` only — no RSS feed is generated. Re-enable when blog content goes live by adding `'RSS'` to `outputs.home` and `outputs.section`.

## JSON-LD structured data (`partials/seo-jsonld.html`)

Uses Hugo `dict` + `jsonify` — no string templates, type-safe. Per Alexander's pattern.

### Homepage — `Person` + `WebSite` with `@graph`

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Person",
      "@id": "https://leoniekaiser.com/#person",
      "name": "Leonie Kaiser",
      "url": "https://leoniekaiser.com/",
      "description": "KI & Business Consultant aus Niederösterreich. Über 20 Jahre globale Projekterfahrung…",
      "sameAs": [
        "https://linkedin.com/in/leoniekaiser/"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://leoniekaiser.com/#website",
      "url": "https://leoniekaiser.com/",
      "name": "Leonie Kaiser – KI & Business Consulting",
      "inLanguage": "de-AT",
      "publisher": { "@id": "https://leoniekaiser.com/#person" }
    }
  ]
}
```

**Fields populated from `params.toml`:**

| JSON-LD field | Source |
|---|---|
| `name` | `params.orgName` (fallback `site.Title`) |
| `description` | `params.authorBio` (overrides `params.description`) |
| `url` | `site.BaseURL` |
| `sameAs[]` | `params.social.*` (only non-empty values) |

To add a new social profile: drop the URL into `params.toml` `[social]` and it appears in `sameAs`.

### Blog post — `Article` (future)

The partial has a ready branch for `section == "blog"` single pages:

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "...",
  "description": "...",
  "url": "https://leoniekaiser.com/blog/post-slug/",
  "inLanguage": "de-AT",
  "datePublished": "2026-04-25",
  "dateModified": "2026-04-25",
  "image": { "@type": "ImageObject", "url": "..." },
  "articleSection": "...",
  "keywords": "a, b, c",
  "author":    { "@id": "https://leoniekaiser.com/#person" },
  "publisher": { "@id": "https://leoniekaiser.com/#person" }
}
```

Fields are pulled from frontmatter:

| JSON-LD field | Source |
|---|---|
| `headline` | `.Title` |
| `description` | `.Description` (or `.Summary`) |
| `datePublished` | `.Date` |
| `dateModified` | `.Lastmod` |
| `image` | `.Params.image` (absolute URL) |
| `articleSection` | first `categories[]` entry |
| `keywords` | `tags[]` joined with `, ` |
| `author` / `publisher` | always Person `@id` (Leonie) |

The Article branch activates automatically once content lands at `content/blog/<slug>.md`. No code change needed.

## Sitemap

Hugo emits `sitemap.xml` automatically. Current entries: `/`, `/impressum/`, `/datenschutz/`, plus the empty `categories/` and `tags/` listing pages (Hugo defaults).

## Robots

`static/robots.txt` controls crawler rules. Current state — check the file to confirm.

## Audit checklist (manual, before deploy)

1. View source on `/`. Confirm:
   - `<title>` matches `seoHomeTitle`
   - `og:image` is the new branded `og-default.png`
   - JSON-LD validates (paste into Schema.org Validator)
2. Test OG preview at `https://www.opengraph.xyz/url/https%3A%2F%2Fleoniekaiser.com`
3. Test Twitter card at `https://cards-dev.twitter.com/validator` (legacy URL — Twitter no longer hosts this; alternative: post to a private LinkedIn or Slack to preview the unfurl)
4. Run Lighthouse mobile — target SEO ≥ 95, Performance ≥ 90, Accessibility ≥ 95
