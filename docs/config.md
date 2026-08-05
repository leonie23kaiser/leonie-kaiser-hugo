# Configuration

All config lives in `src/growthtogether.at/config/_default/` as three split files.

## config.toml

Site-level Hugo settings.

```toml
baseURL = 'https://leoniekaiser.com/'
languageCode = 'de-AT'
defaultContentLanguage = 'de'
title = 'KI & Digitalisierung für Praxen – Strategie & EU AI Act | Leonie Kaiser'

enableRobotsTXT = true
enableGitInfo = true
enableEmoji = true

disableKinds = ["taxonomy", "term"]

[markup.goldmark.renderer]
  unsafe = true

[permalinks]
  journal = "/blog/:slug/"

[outputs]
  home = ['HTML','RSS']

[imaging]
  quality = 82
  resampleFilter = 'Lanczos'

[minify]
  minifyOutput = true

[sitemap]
  changefreq = 'monthly'
  priority = 0.7
  filename = 'sitemap.xml'
```

**Note:** `leoniekaiser.com` is the live custom domain (set via `static/CNAME`, deployed through GitHub Pages — see [deploy.md](deploy.md)). The Hugo source directory is still named `src/growthtogether.at/` for historical reasons; don't rename it, it doesn't reflect the live domain.

`disableKinds = ["taxonomy", "term"]` — there are no categories/tags listing pages. The `journal` section (blog) still uses `categories`/`tags` as plain front-matter metadata for JSON-LD (`keywords`), just not as Hugo taxonomy pages.

## params.toml

Brand tokens, org metadata, and contact details consumed by layouts and partials.

### Brand tokens

These are mirrored as CSS custom properties in `assets/css/brand.css`. **If a colour changes, update both files.**

```toml
brandTeal900   = "#086584"   # Primär / Buttons / Links
brandTeal600   = "#5FA2A0"   # Sekundär / Verläufe / Hover
brandTeal50    = "#EDF7F2"   # Hellgrün alt. Sections
brandTeal100   = "#E7F4F4"   # Hellblau Highlights
brandGold      = "#CF982B"   # Labels
brandGoldSoft  = "#F1C50E"   # Highlights sparsam
brandViolet    = "#6B2C8C"   # Akzent: Eyebrows, Sekundär-CTA
brandVioletSoft= "#EFE6F6"   # Pill-Background
brandVioletLine= "#D9C5E8"   # Pill-Border
brandBeige     = "#FAF0E9"   # Seiten-Hintergrund
brandInk       = "#1d2228"
brandMute      = "#5b6572"
brandLine      = "#ece3d8"
```

### Org & contact

```toml
description = "KI & Digitalisierung für kleine Gesundheitspraxen: Prozesse automatisieren, EU AI Act und DSGVO sicher umsetzen. Ortsunabhängig im DACH-Raum. Kostenfreie Potenzialanalyse."
seoSiteTitle = "Leonie Kaiser"
seoHomeTitle = "Leonie Kaiser – KI & Digitalisierung für Praxen"

orgName  = "Leonie Kaiser"
orgLegal = "Leonie Kaiser"
orgRole  = "KI- & Digitalisierungs-Expertin"
orgCity  = "Niederösterreich"
orgRegion= "AT-3"
orgCountry="AT"

authorName = "Leonie Kaiser"
authorBio  = "KI- & Digitalisierungs-Expertin aus Niederösterreich. Über 20 Jahre Projekterfahrung im Gesundheitsbereich, u. a. bei Merck, AbbVie, Baxter. Strategische, menschenzentrierte Digitalisierung und KI für kleine Gesundheitspraxen im DACH-Raum."

email    = "hello@leoniekaiser.com"
phone    = "+43 670 775 60 60"
phoneRaw = "+436707756060"
calendly = "https://calendly.com/leonie-kaiser/ki-potentialanalyse"
linkedin = "https://linkedin.com/in/leoniekaiser/"
gaID     = "G-8BVZ596FR9"

[social]
  linkedin  = "https://linkedin.com/in/leoniekaiser/"
  instagram = ""
  youtube   = ""
```

**`orgCity` is intentionally just `"Niederösterreich"`**, not a specific town — no exact location is published for a home-based solo practice.

**`seoHomeTitle` and `seoSiteTitle` are currently dead params** — defined here but not referenced anywhere in `layouts/`. The actual `<title>` logic in `partials/head.html` uses `site.Title` (from `config.toml`) on the homepage and `.Title` (page front matter) everywhere else, with no concatenation. To change the homepage `<title>`, edit `config.toml`'s `title`, not `seoHomeTitle`.

**`gaID`** feeds Google Analytics in `partials/head.html`. It's only loaded `{{- if and hugo.IsProduction site.Params.gaID }}` (production builds only) and initialises with `gtag('consent','default',{'analytics_storage':'denied'})` — analytics stays off until the visitor accepts via the cookie banner (`partials/cookie-banner.html`).

**Empty `social.*` keys are filtered out** by `schema.html` (only non-empty entries are emitted as `sameAs`).

## menus.toml

```toml
[[main]]
  name   = "Leistungen"
  url    = "/#leistungen"
  weight = 10

[[main]]
  name   = "Über mich"
  url    = "/#about"
  weight = 20

[[main]]
  name   = "Workshop"
  url    = "/#workshop"
  weight = 25

[[main]]
  name   = "Kontakt"
  url    = "/#kontakt"
  weight = 40

[[footer]]
  name   = "Impressum"
  url    = "/impressum/"
  weight = 10

[[footer]]
  name   = "Datenschutz"
  url    = "/datenschutz/"
  weight = 20
```

**This file is stale and currently unused.** The real navigation is hardcoded directly in `layouts/partials/nav.html` (Leistungen · Über mich · Blog · FAQ · Kontakt) and `layouts/partials/footer.html` (adds EU AI Act · DSGVO · Datenschutzerklärung · Impressum), neither of which reads `site.Menus`. `#about` and `#workshop` don't exist as anchors on the current homepage. Don't trust `menus.toml` to reflect the live nav — check `nav.html`/`footer.html` directly, or update both together if you add a menu-driven nav later.

## When to edit which file

| Change | File |
|---|---|
| Brand colour | `params.toml` + `assets/css/brand.css` |
| Phone, email, Calendly link | `params.toml` |
| LinkedIn URL | `params.toml` (under `[social]` and as top-level `linkedin`) |
| New social channel | `params.toml` (add to `[social]`) + `assets/css/brand.css` (icon) |
| Nav / footer links | `layouts/partials/nav.html` and `layouts/partials/footer.html` directly (not `menus.toml`) |
| Homepage `<title>` | `config.toml` (`title`) — **not** `params.toml`'s `seoHomeTitle`/`seoSiteTitle` (unused, see above) |
| Meta description fallback | `params.toml` (`description`) |
| Hugo image quality, output formats, minify, sitemap | `config.toml` |
