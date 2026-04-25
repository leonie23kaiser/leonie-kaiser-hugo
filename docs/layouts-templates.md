# Layouts & Templates

All templates live in `src/growthtogether.at/layouts/`. Hugo resolves templates from most-specific to least-specific.

## Base template

`_default/baseof.html` (14 lines) — HTML skeleton with three blocks:

| Block | Default content |
|---|---|
| `head` | calls `partials/head.html` |
| `main` | filled by each page-type layout |
| `scripts` | calls `partials/scripts.html` |

Header and footer partials are rendered directly inside `<body>` (not block-overridable).

## Page-type layouts

| File | Used for |
|---|---|
| `_default/home.html` | The homepage — single-page builder, ~234 lines, reads `data/site.yaml` |
| `_default/single.html` | `/impressum/`, `/datenschutz/` |
| `_default/list.html` | unused (no content collections yet) |
| `_default/404.html` | 404 page |
| `_default/_markup/render-link.html` | overrides Markdown link rendering |

### `home.html` — the page builder

Reads `{{ $s := site.Data.site }}` once, then walks 7 sections:

| Anchor `id` | YAML key | Layout |
|---|---|---|
| `top` | `hero` (+ `stats`, `trust`) | hero with `<picture>` portrait + 3 stat tiles + trust badges |
| `leistungen` | `services` | 3-card grid, middle card `featured: true` is highlighted |
| `about` | `about` (+ `cert`, `about_extra`) | bio paragraphs, company pills, 3 value cards, certificate strip, portrait + Conscious Consultant badge overlay |
| `workshop` | `workshop` | image left, copy + 3-bullet checklist + CTA right |
| `prozess` | `process` | 3 numbered step cards |
| (no id) | `testimonials` | currently placeholder copy |
| `kontakt` | `contact` | booking card + contact form |

## Partials

All in `layouts/partials/`.

### `head.html`

Outputs `<head>` contents:
- charset, viewport, theme-color (`#086584`), color-scheme (`light`)
- SEO title (home: `seoHomeTitle`, other: `<title> – <seoSiteTitle>`)
- meta description (page-specific or `params.description` fallback)
- OG + Twitter card tags with dynamic `og:image` (page `image` param → `og-default.png` fallback)
- canonical link
- favicons (`.ico`, `.svg`, `apple-touch-icon.png`)
- Self-hosted font preload: `satoshi-400.woff2`, `cabinet-grotesk-800.woff2`
- Brand CSS: dev = raw, prod = minified + fingerprinted + SRI
- Calls `seo-jsonld.html`

### `header.html` (17 lines)

Sticky top nav. Logo on left ("Leonie Kaiser" + "KI & Business Consulting" subtitle), main menu items on right. No mobile hamburger logic in markup — mobile menu opens via `scripts.html` toggle.

### `footer.html` (20 lines)

Two-column footer: brand block + legal links (Impressum, Datenschutz). Social icons from `params.social.*` (only non-empty entries are rendered).

### `picture.html`

Responsive image partial using Hugo's asset pipeline. Call signature:

```go-html-template
{{ partial "picture.html" (dict
  "src"    "images/leonie-portrait-hero.jpg"
  "alt"    "Leonie Kaiser – KI & Business Consultant"
  "sizes"  "(max-width: 700px) 100vw, 33vw"
  "widths" (slice 400 800 1200)
  "eager"  true
  "ratio"  "1/1"
) }}
```

| Param | Type | Description |
|---|---|---|
| `src` | string | Path under `assets/` (e.g. `"images/foo.jpg"`) |
| `alt` | string | Alt text |
| `class` | string | Optional CSS class on `<img>` |
| `sizes` | string | Default `"(max-width: 700px) 100vw, 33vw"` |
| `widths` | slice | Pixel widths to generate, default `(slice 400 800 1200)` |
| `eager` | bool | If `true`: `loading="eager"` + `fetchpriority="high"` (LCP images) |
| `ratio` | string | CSS `aspect-ratio` value (e.g. `"3/4"`, `"16/9"`) — added inline |

Generates a `<picture>` element with WebP `<source>` + original-format `<img>` fallback, both with `srcset` and `sizes`. Falls back to a static `<img>` if `resources.Get` returns nil.

**Caveat:** images must be in `assets/` (not `static/`) for the pipeline to work. Many of Leonie's photos are currently pre-rendered in `static/images/` and referenced directly by `home.html` as `<picture>` blocks — not via `picture.html`. Future cleanup: move sources to `assets/`, render via partial.

### `seo-jsonld.html`

Emits `<script type="application/ld+json">` using `dict` + `jsonify` (type-safe, no string templates):

| Page context | Schema type |
|---|---|
| Homepage | `Person` (Leonie) + `WebSite`, `@graph` with `@id` cross-refs |
| Future blog post (`section == "blog"`, single page) | `Article` with author/publisher pointing to Person `@id` |

The `Person` block pulls `orgName`, `description`, `authorBio`, and `social.*` (filtered for non-empty) from `params.toml`.

### `scripts.html`

Minimal inline JS: mobile menu open/close toggle and a scroll-position class on `<body>` for sticky-header shadow. No external JS dependencies, no analytics.

## Shortcodes

### `card.html`

```markdown
{{< card >}}
## Heading
Body text.
{{< /card >}}
```

Wraps content in a styled card container. Currently unused on the home page (the page builder generates its own card layouts), but available for legal/blog pages.

### `youtube.html`

Embeds a YouTube video via `youtube-nocookie.com` for DSGVO-friendly embedding:

```markdown
{{< youtube id="abc123XYZ" >}}
```

Not used on the live home page (no videos yet).

## Render hooks

### `_default/_markup/render-link.html`

Overrides Markdown link rendering. Useful for adding `target="_blank" rel="noopener"` to external links automatically. Affects markdown bodies in `content/*.md`.
