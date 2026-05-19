# Architecture

## Tech stack

| Layer | Choice |
|---|---|
| Static site generator | Hugo v0.123+ extended |
| Styling | Single `assets/css/brand.css` (no framework) |
| Fonts | Cabinet Grotesk (display) + Satoshi (UI), self-hosted (DSGVO) |
| Images | Hugo asset pipeline → WebP + srcset |
| JavaScript | Minimal inline (mobile menu, scroll class) |
| Deployment | rsync to KAS (current) → Azure Static Web Apps + Workload Identity (planned) |

## Repository layout

The repo mirrors `aeshilion/superleague-hugo`. Hugo project root is **NOT** the repo root — it lives under `src/growthtogether.at/`.

```
leonie-kaiser-hugo/
├── .claude/skills/         37 skills (hugo-* family + copywriting, content-strategy, ...)
├── .mcp.json               13 MCP servers (context7, playwright, image-generator, ...)
├── CLAUDE.md               Leonie-specific working rules
├── docs/                   this documentation
├── src/growthtogether.at/  ← Hugo project root
└── design/                 wireframe-v1.html (reference only)
```

## Hugo project layout

All paths below are relative to `src/growthtogether.at/`.

```
config/_default/
  config.toml       baseURL, language, markup, outputs, imaging, minify
  params.toml       brand colors, org info, contact, social
  menus.toml        main nav (anchor-based) + footer (legal pages)

content/
  _index.md         home (frontmatter only — body comes from data/site.yaml + home.html)
  impressum.md
  datenschutz.md

layouts/
  _default/
    baseof.html     HTML skeleton
    home.html       single-page builder, ~234 lines, reads data/site.yaml
    list.html       generic section list (unused so far)
    single.html     legal pages (impressum, datenschutz)
    404.html
    _markup/render-link.html
  partials/
    head.html       meta, OG, preload, brand CSS bundle, fonts
    header.html     sticky nav with anchor links
    footer.html     2-column, social
    picture.html    responsive <picture> partial (WebP + srcset)
    seo-jsonld.html JSON-LD: Person + WebSite (home) / Article (blog — future)
    scripts.html    mobile menu toggle
  shortcodes/
    card.html
    youtube.html

assets/
  css/brand.css     ~490 lines, single source of truth
  images/           source PNGs for the asset pipeline + reserve/ (alternates)

data/
  site.yaml         all editable copy (hero, stats, services, about, workshop,
                    process, testimonials, contact — 11 top-level sections)

static/
  favicon.ico, favicon.svg, apple-touch-icon.png, robots.txt
  fonts/            Cabinet Grotesk + Satoshi (.woff2)
  images/           pre-rendered .jpg+.webp pairs for active photos +
                    og-default.png, workshop-unique-genius.jpg

archetypes/
  default.md
```

## Data flow

```
data/site.yaml
  │
  └─► layouts/_default/home.html  (one read: $s := site.Data.site)
         │
         └─► 7 page sections (hero, leistungen, about, workshop, prozess, testimonials, kontakt)
               │
               └─► public/index.html
```

Images used by the home page builder come from two sources:
- `assets/images/*.png` (source) → Hugo pipeline → WebP/JPG variants
- `static/images/*.{jpg,webp}` (pre-rendered pairs, copied as-is)

The pre-rendered pairs in `static/` are a historical artefact — future work should consolidate everything to the `assets/` pipeline (see `content-workflow.md`).

## Build behaviour

- **Dev** (`hugo server --source src/growthtogether.at -D`): CSS served raw, drafts included, live reload.
- **Prod** (`hugo --source src/growthtogether.at --minify`): CSS minified + fingerprinted + SRI hash injected into `<link>` tag (see `partials/head.html`). HTML minified (`config.toml` → `[minify]`). Images converted to WebP with multiple srcset widths.

## Deployment

**Current:** rsync to All-Inkl. KAS

```bash
hugo --source src/growthtogether.at --minify --baseURL https://growthtogether.at/
rsync -avz --delete src/growthtogether.at/public/ \
  ssh-w02124ee@w01b2e95.kasserver.com:www/htdocs/w02124ee/growthtogether.at/
```

**Planned:** GitHub Actions → Azure Static Web Apps with Workload Identity Federation (mirrors `superleague-hugo` deploy pattern). See `deploy.md`.

## Taxonomies

None. Hugo's default taxonomies (categories, tags) are unused — no content collections exist. Hugo emits empty `categories/` and `tags/` listing pages by default; these can be ignored or disabled later if desired.
