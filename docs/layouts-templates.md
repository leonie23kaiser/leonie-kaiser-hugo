# Layouts & Templates

All templates live in `src/growthtogether.at/layouts/`. Hugo resolves templates from most-specific to least-specific.

## Base template

`_default/baseof.html` — HTML skeleton:

```go-html-template
<!doctype html>
<html lang="{{ site.Language.LanguageCode | default `de-AT` }}">
  <head>
    {{ partial "head.html" . }}
  </head>
  <body>
    {{ partial "nav.html" . }}
    {{ block "main" . }}{{ end }}
    {{ partial "footer.html" . }}
    {{ partial "cookie-banner.html" . }}
    {{ partial "scripts.html" . }}
  </body>
</html>
```

Nav, footer, and the cookie banner are rendered directly in `baseof.html` (not block-overridable) — every page gets all three.

## Page-type layouts

| Front matter `type:` | File | Used for |
|---|---|---|
| *(home content)* | `_default/home.html` | Homepage — hardcoded sections, not data-driven (see below) |
| `leistungen` | `leistungen/single.html` | `/leistungen/` overview page |
| `branche` | `branche/single.html` | The 4 Leistungsbereich pages, content pulled from `data/branchen.yaml` |
| `journal` (section) | `journal/list.html` | `/blog/` |
| *(journal post)* | `journal/single.html` | `/blog/<slug>/` |
| `faq` | `faq/single.html` | `/faq/` — hardcoded accordion, see [content-model.md](content-model.md) for the dual-source trap |
| `eu-ai-act` | `eu-ai-act/single.html` | `/eu-ai-act/` |
| `dsgvo` | `dsgvo/single.html` | `/dsgvo/` |
| `ueber-mich` | `ueber-mich/single.html` | `/ueber-mich/` |
| `impressum` | `impressum/single.html` | `/impressum/` |
| `datenschutz` | `datenschutz/single.html` | `/datenschutz/` |
| *(404)* | `_default/404.html` | 404 page |
| — | `_default/_markup/render-link.html` | overrides Markdown link rendering |

`_default/list.html` and `_default/single.html` exist as generic fallbacks but every real content type above has its own dedicated layout — Hugo's most-specific-wins resolution means the generic fallbacks rarely fire.

### `home.html` — the homepage

**Not data-driven.** Every section (hero, "Kennen Sie das?" pain points, "Was ich für Sie tue" / Leistungen teaser, Datenschutz/Compliance-first, Über mich, Prozess, Testimonials, "KI-Potenzialanalyse"-Promo, Kontaktformular) is hardcoded HTML directly in this template. Only `content/_index.md`'s front matter (`title`, `description`) feeds it — there's no equivalent of a `data/site.yaml` to edit section copy. To change homepage copy, edit `home.html` directly.

Anchor IDs used by nav/footer links: `#leistungen`, `#kontakt`. (`#about` and `#workshop`, referenced by the stale `menus.toml`, don't exist on the current homepage — see [config.md](config.md).)

## Partials

All in `layouts/partials/`.

### `head.html`

Outputs `<head>` contents:
- charset, viewport, theme-color (`#086584`), color-scheme (`light`)
- `<title>`: `site.Title` on the homepage, `.Title` on every other page (no `seoHomeTitle`/`seoSiteTitle` concatenation — those params exist in `params.toml` but aren't currently wired into `head.html`'s title logic)
- meta description (page-specific `.Description` or `site.Params.description` fallback)
- OG + Twitter card tags, `og:image` fallback chain: page `.Params.image` → `.Params.ogImage` → `images/og-default.png`
- canonical link, favicons (`.ico`, `.svg`, `apple-touch-icon.png`)
- Self-hosted font preloads: `satoshi-400/500/700`, `cabinet-grotesk-700/800`
- Brand CSS: dev = raw, prod = minified + fingerprinted + SRI
- Calls `partials/schema.html`
- Google Analytics (`gtag.js`), production-only, gated behind `site.Params.gaID` and defaulting `analytics_storage` to `denied` until cookie consent

### `nav.html`

Sticky top nav. Logo left ("Leonie Kaiser" + "KI & Digitalisierung" subtitle), hardcoded link list right (Leistungen · Über mich · Blog · FAQ · Kontakt) + a "Termin buchen" CTA button linking to the Calendly URL. Mobile menu (`.mmenu`) is a separate hardcoded block toggled via `scripts.html`, not CSS-only.

**Not menu-driven** — despite `menus.toml` existing, this partial doesn't read `site.Menus`.

### `footer.html`

Two-row footer: brand block + link row (Leistungen · Über mich · Blog · EU AI Act · DSGVO · FAQ · Kontakt), then a legal row (copyright, Hugo-setup credit link, Datenschutzerklärung, Impressum). Also not menu-driven.

### `cookie-banner.html`

Cookie consent banner (notwendige Cookies + optional Google Analytics). Not present in earlier versions of this doc — added alongside the `gaID` GA integration.

### `picture.html`

Responsive image partial using Hugo's asset pipeline. Call signature:

```go-html-template
{{ partial "picture.html" (dict
  "src"    "images/blog/cover-x.png"
  "alt"    "..."
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

Generates a `<picture>` element with WebP `<source>` + original-format `<img>` fallback, both with `srcset` and `sizes`. Falls back to a plain `<img>` (relative path, no resizing) if `resources.Get` returns nil — i.e. if `src` isn't actually under `assets/`.

**Caveat, still true today:** several existing photos are pre-rendered in `static/images/` (`.jpg`/`.webp` pairs) and referenced directly by inline `<picture>` blocks in `home.html` and elsewhere — not via this partial. New images (e.g. blog covers) go through `assets/images/` + this partial. See [assets-styles.md](assets-styles.md).

### `schema.html`

(Was named `seo-jsonld.html` in earlier versions of this doc — renamed.) Emits one `<script type="application/ld+json">` per page with a single `@graph`, built via `dict` + `jsonify` (type-safe, no string templates). See [seo-jsonld.md](seo-jsonld.md) for the full breakdown of what's in the graph on which page type.

### `scripts.html`

Inline JS: mobile menu open/close, scroll-position class for sticky-header shadow, cookie-banner interaction, and the scroll-reveal `IntersectionObserver` (`.reveal` / `.reveal-in` classes used throughout `home.html` and other layouts for fade-in-on-scroll). No external JS dependencies.

## Shortcodes

### `card.html`

```markdown
{{< card >}}
## Heading
Body text.
{{< /card >}}
```

Wraps content in a styled card container. Available for use in Markdown bodies; not used by any current hardcoded layout section.

### `youtube.html`

```markdown
{{< youtube id="abc123XYZ" >}}
```

Embeds via `youtube-nocookie.com` for DSGVO-friendly embedding. Not currently used on any live page.

## Render hooks

### `_default/_markup/render-link.html`

Overrides Markdown link rendering (e.g. adding `target="_blank" rel="noopener"` to external links automatically). Affects Markdown bodies in `content/*.md` — most of the site's actual copy lives in hardcoded template HTML instead, so this hook's reach is limited to true Markdown-body content (legal pages, journal posts).

## Stray files (not used by the build)

`layouts/partials/footer.html.bak`, `header.html.bak`, `seo-jsonld.html.bak`, and `layouts/_default/home.html.bak-simply-ai` are leftover backups from an earlier "Simply AI" brand iteration. Hugo ignores `.bak` files and files without a recognised layout name. Safe to ignore; ask before deleting if you're not sure why they're still there.
