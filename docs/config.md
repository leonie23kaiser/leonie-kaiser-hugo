# Configuration

All config lives in `src/growthtogether.at/config/_default/` as three split files.

## config.toml

Site-level Hugo settings.

```toml
baseURL = 'https://growthtogether.at/'
languageCode = 'de-at'
defaultContentLanguage = 'de'
title = 'Leonie Kaiser – KI & Business Consulting'

enableRobotsTXT = true
enableEmoji = true

[markup.goldmark.renderer]
  unsafe = true            # allow raw HTML in markdown body

[outputs]
  home = ['HTML']          # no RSS for now — add when blog launches

[imaging]
  quality = 82
  resampleFilter = 'Lanczos'

[minify]
  minifyOutput = true
```

**Note:** the brand name is "Leonie Kaiser" but the live domain is **growthtogether.at**. The `leoniekaiser.com` domain is unused (historical).

## params.toml

Brand tokens, org metadata, and contact details consumed by layouts and partials.

### Brand tokens

These are mirrored as CSS custom properties in `assets/css/brand.css`. **If a colour changes, update both files.**

```toml
brandTeal900    = "#086584"   # Primary / buttons / links
brandTeal600    = "#5FA2A0"   # Secondary / gradients / hover
brandTeal50     = "#EDF7F2"   # Soft section background
brandTeal100    = "#E7F4F4"   # Highlights
brandGold       = "#CF982B"   # Labels
brandGoldSoft   = "#F1C50E"   # Sparse highlights
brandViolet     = "#6B2C8C"   # Eyebrow text, secondary CTA
brandVioletSoft = "#EFE6F6"   # Pill background
brandVioletLine = "#D9C5E8"   # Pill border
brandBeige      = "#FAF0E9"   # Page background
brandInk        = "#1d2228"   # Body text
brandMute       = "#5b6572"   # Secondary text
brandLine       = "#ece3d8"   # Borders, separators
```

### Org & contact

```toml
seoSiteTitle = "Leonie Kaiser"
seoHomeTitle = "Leonie Kaiser – KI & Business Consulting · Wien"
description  = "KI & Business Consulting aus Wien/Niederösterreich. Von der Potenzialanalyse bis zur Umsetzung – einfach, ethisch, wirksam. Mit über 20 Jahren Erfahrung im globalen Projektmanagement."

orgName   = "Leonie Kaiser"
orgLegal  = "Leonie Kaiser"
orgRole   = "KI & Business Consultant"
orgCity   = "Felixdorf, Niederösterreich"
orgRegion = "AT-3"
orgCountry= "AT"

authorName = "Leonie Kaiser"
authorBio  = "KI & Business Consultant aus Niederösterreich. Über 20 Jahre globale Projekterfahrung…"

email    = "hello@leoniekaiser.com"
phone    = "+43 670 775 60 60"
phoneRaw = "+436707756060"
calendly = "https://calendly.com/leonie-kaiser/ki-potentialanalyse"
linkedin = "https://linkedin.com/in/leoniekaiser/"

[social]
  linkedin  = "https://linkedin.com/in/leoniekaiser/"
  instagram = ""
  youtube   = ""
```

**Empty `social.*` keys are filtered out** by `seo-jsonld.html` (only non-empty entries are emitted as `sameAs`).

## menus.toml

Defines two menu groups. The main menu is **anchor-based** (one-page site).

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
  name   = "Prozess"
  url    = "/#prozess"
  weight = 30

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

Anchor IDs match `<section id="...">` in `layouts/_default/home.html`. To rename a section, change the `id`, the menu `url`, and the section heading consistently.

## When to edit which file

| Change | File |
|---|---|
| Brand colour | `params.toml` + `assets/css/brand.css` |
| Phone, email, Calendly link | `params.toml` |
| LinkedIn URL | `params.toml` (under `[social]` and as top-level `linkedin`) |
| New social channel | `params.toml` (add to `[social]`) + `assets/css/brand.css` (icon) |
| New menu item | `menus.toml` |
| Site title / SEO defaults | `params.toml` |
| Hugo image quality, output formats, minify | `config.toml` |
