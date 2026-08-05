# Architecture

## Tech stack

| Layer | Choice |
|---|---|
| Static site generator | Hugo v0.123+ extended (CI pins v0.135.0) |
| Styling | Single `assets/css/brand.css` (no framework), ~830 lines |
| Fonts | Cabinet Grotesk (display) + Satoshi (UI), self-hosted (DSGVO) |
| Images | Hugo asset pipeline → WebP + srcset (partially — see [assets-styles.md](assets-styles.md)) |
| JavaScript | Minimal inline (`partials/scripts.html`): mobile menu, scroll-reveal, cookie banner |
| Analytics | Google Analytics (`gtag.js`), production-only, consent-gated via cookie banner |
| Deployment | GitHub Pages via `.github/workflows/deploy-pages.yml`, custom domain `leoniekaiser.com` |

## Repository layout

The repo mirrors `aeshilion/superleague-hugo` for pattern questions. Hugo project root is **NOT** the repo root — it lives under `src/growthtogether.at/` (kept as the directory name intentionally; the live domain is `leoniekaiser.com`, not `growthtogether.at` — see [config.md](config.md)).

```
leonie-kaiser-hugo/
├── .claude/skills/         skill definitions (hugo-* family + blog-post, copywriting, ...)
├── .github/workflows/      deploy-pages.yml (GitHub Pages CI/CD)
├── AGENTS.md               canonical brand voice guard
├── CLAUDE.md               working rules for AI assistants in this repo
├── docs/                   this documentation
├── strategie/              internal strategy/positioning/pricing docs (not published)
└── src/growthtogether.at/  ← Hugo project root
```

## Hugo project layout

All paths below are relative to `src/growthtogether.at/`.

```
config/_default/
  config.toml       baseURL, language, markup, outputs, imaging, minify, sitemap
  params.toml       brand colors, org info, contact, social, gaID
  menus.toml        stale — not read by nav.html/footer.html, see config.md

content/
  _index.md         homepage (front matter only — home.html is hardcoded, not data-driven)
  ueber-mich.md, faq.md, impressum.md, datenschutz.md
  eu-ai-act/_index.md, dsgvo/_index.md
  leistungen/_index.md                        overview page
  leistung-*/_index.md                        4 Leistungsbereich pages, type: branche
  journal/_index.md, journal/<slug>.md        blog

layouts/
  _default/
    baseof.html     HTML skeleton
    home.html       homepage, hardcoded sections (no data/site.yaml — it doesn't exist)
    single.html, list.html   generic fallbacks, rarely used (every real type has its own layout)
    404.html
    _markup/render-link.html
  <type>/single.html   one per content type: leistungen, branche, journal, faq,
                       eu-ai-act, dsgvo, ueber-mich, impressum, datenschutz
  partials/
    head.html       meta, OG, preload, brand CSS bundle, fonts, GA
    nav.html        sticky nav, hardcoded links (not menus.toml-driven)
    footer.html     2-row footer, hardcoded links
    cookie-banner.html
    picture.html    responsive <picture> partial (WebP + srcset)
    schema.html     JSON-LD @graph — see seo-jsonld.md
    scripts.html    mobile menu, scroll-reveal, cookie banner interaction
  shortcodes/
    card.html, youtube.html

assets/
  css/brand.css     single source of truth for styles
  images/           source images for the asset pipeline: testimonials, blog/, reserve/

data/
  branchen.yaml     content for the 4 Leistungsbereich pages (not "all editable copy" —
                     the homepage itself is hardcoded, see content-model.md)

static/
  favicon.ico/svg, apple-touch-icon.png, robots.txt, llms.txt, CNAME
  fonts/            Cabinet Grotesk + Satoshi (.woff2)
  images/           pre-rendered .png+.webp pairs + og-default.png
  downloads/        service-katalog.pdf (generated, not hand-edited)
  analyse/          standalone Potenzialanalyse micro-tool, separate from main templates

archetypes/
  default.md
```

**There is no `data/site.yaml`.** Earlier versions of this doc (and of the site) had one; the current homepage is hardcoded HTML in `layouts/_default/home.html`. See [content-model.md](content-model.md) for what actually drives content today.

## Data flow

```
content/_index.md (front matter only: title, description)
  │
  └─► layouts/_default/home.html   (hardcoded sections, no data read)
         │
         └─► public/index.html

data/branchen.yaml
  │
  └─► layouts/branche/single.html   (matched via branche_slug in content front matter)
         │
         └─► public/leistungen/<slug>/index.html
```

Images used by the site come from two sources — see [assets-styles.md](assets-styles.md) for the full breakdown and the current cleanup status:
- `assets/images/*` (source) → Hugo pipeline → WebP/original-format variants, via `picture.html`
- `static/images/*.{png,webp}` (pre-rendered pairs, copied as-is) — still used by most inline `<picture>` blocks in `home.html` and other layouts; new content (e.g. blog covers) uses the pipeline path instead.

## Build behaviour

- **Dev** (`hugo server --source src/growthtogether.at -D`): CSS served raw, drafts included, live reload.
- **Prod** (`hugo --source src/growthtogether.at --minify --gc --buildFuture`): CSS minified + fingerprinted + SRI hash injected into `<link>` tag (`partials/head.html`). HTML minified (`config.toml` → `[minify]`). `--buildFuture` is required in CI so future-dated journal posts publish on schedule — see [deploy.md](deploy.md).

## Deployment

GitHub Pages. Push to `main` touching `src/growthtogether.at/**` (or the workflow file itself) triggers `.github/workflows/deploy-pages.yml`, which also runs on a Tuesday-morning cron to publish future-dated journal posts and on manual dispatch. Full detail in [deploy.md](deploy.md).

## Taxonomies

None. `config.toml` sets `disableKinds = ["taxonomy", "term"]` — Hugo's default `categories/`/`tags/` listing pages are actively disabled, not just unused. Journal posts still carry `categories`/`tags` front matter, but only as plain metadata (feeds JSON-LD `keywords`, feeds the category-filter pills on `/blog/`) — not as Hugo taxonomy pages.
