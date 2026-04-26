# Content Model

Leonie's site has **no content collections** — it's a single-page builder. The editable copy lives in `data/site.yaml`. The two legal pages live in `content/` as standard Hugo pages.

## `data/site.yaml` — 11 top-level sections

The page builder `layouts/_default/home.html` reads `site.Data.site` once and walks each section.

### `hero`

```yaml
hero:
  badge: "Simply AI · Wien · Niederösterreich"
  headline_line1: "KI-Strategie & Automatisierung"
  headline_line2: "…einfach umgesetzt."
  tagline: "..."            # one short line under headline
  lead: "..."               # paragraph
  cta_primary: "Kostenfreie Potenzialanalyse"
  cta_primary_icon: "📅"     # emoji prefix on button
  cta_primary_href: "#kontakt"
  cta_secondary: "Leistungen ansehen"
  cta_secondary_href: "#leistungen"
  photo: "images/leonie-portrait-hero.jpg"      # JPEG fallback
  photo_webp: "images/leonie-portrait-hero.webp" # WebP source
  photo_alt: "Leonie Kaiser – KI & Business Consultant"
```

LCP image — the hero photo is preloaded as `fetchpriority=high` from `partials/head.html`.

### `stats`

```yaml
stats:
  - { value: "20+", label: "Jahre Erfahrung" }
  - { value: "3",   label: "Kernleistungen" }
  - { value: "100%", label: "Remote & hybrid möglich" }
```

### `trust`

List of strings rendered as a row of trust badges/pills under the hero.

```yaml
trust:
  - "20+ Jahre globale Projekterfahrung"
  - "Merck · AbbVie · Baxter"
  - "EU AI Act & DSGVO konform"
  - "Remote & Hybrid · AT & DACH"
```

### `services` — the three core offers

```yaml
services:
  eyebrow: "Leistungen & Preise"
  heading: "Was ich für Sie tue"
  sub: "..."
  items:
    - tag: "Gratis · Erstgespräch"   # pill above card title
      tag_style: "gold"             # "gold" | "gold-on-featured"
      title: "KI-Potenzialanalyse"
      text: "..."
      points:                       # bullet list inside card
        - "Aktuellen Digitalisierungsgrad analysieren"
        - "..."
      price: "Kostenlos"
      price_note: "30 Min. · Online · Unverbindlich"
      featured: false               # the middle card is highlighted with featured: true
```

Currently 3 items: KI-Potenzialanalyse (free), KI-Strategie & Beratung (featured), Umsetzung.

### `about`

```yaml
about:
  eyebrow: "Über mich"
  heading: "Strategie, KI & die menschliche Komponente"
  paragraphs:                       # list of strings, each becomes a <p>
    - "..."
    - "..."
  pills_label: "Erfahrung aus Unternehmen wie:"
  pills:                            # company logos as text pills
    - "Merck"
    - "AbbVie"
    - "..."
  values:                           # 3-column value cards
    - { icon: "🧭", color: "teal",   title: "Strategisch", text: "..." }
    - { icon: "🔬", color: "violet", title: "Forschungsbasiert", text: "..." }
    - { icon: "💛", color: "gold",   title: "Menschlich", text: "..." }
```

### `cert` — current education / certificate-in-progress

```yaml
cert:
  label: "Aktuell in Ausbildung"
  title: "KI Consultant Zertifikatslehrgang"
  tags:                  # 5 chips
    - "..."
  badge_label: "Zertifizierung"
  badge_date: "Juni 2026"
```

### `about_extra` — portrait + Conscious Consultant badge

```yaml
about_extra:
  portrait: "images/leonie-about-thoughtful.jpg"
  portrait_webp: "images/leonie-about-thoughtful.webp"
  portrait_alt: "..."
  badge: "images/conscious-consultant-badge.jpg"
  badge_webp: "images/conscious-consultant-badge.webp"
  badge_alt: "..."
  badge_caption: "Conscious Consultant Certified"
```

Rendered as a 4:5 portrait card with a 140 px (mobile: 100 px) round badge overlaid bottom-right.

### `workshop` — free workshop teaser

```yaml
workshop:
  eyebrow: "Kostenfreier Workshop"
  kicker: "Your Unique Genius"
  heading: "Finden Sie Ihre Einzigartigkeit – und gewinnen Sie die Kunden, die wirklich zu Ihnen passen."
  lead: "..."
  points:                # 3-bullet checklist
    - "..."
  cta_label: "Informiert bleiben"
  cta_href: "#kontakt"
  meta: "Online · Teilnahme kostenfrei · Nächster Termin folgt in Kürze"
  image: "images/workshop-unique-genius.jpg"
  image_alt: "..."
```

### `process` — 3-step engagement flow

```yaml
process:
  eyebrow: "Mein Prozess"
  heading: "In 3 Schritten zu Ihrer KI-Lösung"
  sub: "..."
  steps:
    - { num: "1", title: "Potenzialanalyse", text: "..." }
    - { num: "2", title: "Strategie", text: "..." }
    - { num: "3", title: "Umsetzung", text: "..." }
```

### `testimonials` — placeholder until real ones land

```yaml
testimonials:
  eyebrow: "Referenzen"
  heading: "Was Kund:innen sagen"
  placeholder_title: "Testimonials folgen in Kürze ✨"
  placeholder_text: "..."
```

When real testimonials arrive, replace the placeholder with `items: [...]` (schema TBD when first ones come in).

### `contact` — booking card + contact form copy

```yaml
contact:
  eyebrow: "Kontakt"
  heading: "Jetzt gemeinsam starten"
  sub: "..."
  card_title: "Kostenfreie KI-Potenzialanalyse"
  card_text: "30 Minuten · Online · Völlig unverbindlich. Ich zeige Ihnen, ..."
  card_cta: "Termin auswählen"            # links to params.toml → calendly
  form_title: "Nachricht senden"
  form_sub: "Ich antworte innerhalb von 24 Stunden."
  form_success: "Danke! Ich melde mich innerhalb von 24 Stunden."
  form_submit: "Nachricht absenden"
```

The Calendly URL itself is in `params.toml` (`calendly = "https://calendly.com/..."`).

## `content/` — standalone pages

### `content/_index.md`

```yaml
---
title: "Leonie Kaiser – KI & Business Consulting"
description: "..."
---
```

Frontmatter only. The body comes from `home.html` walking `data/site.yaml`.

### `content/impressum.md` and `content/datenschutz.md`

Standard Hugo single pages — frontmatter (`title`, `description`) + Markdown body, rendered by `layouts/_default/single.html`.

## When to add a new section

1. Add a key to `data/site.yaml` with the field schema.
2. Add a `<section>` block to `layouts/_default/home.html` reading `$s.<your-key>`.
3. Add a `<section id="...">` anchor + a matching `[[main]]` entry in `menus.toml`.
4. Style in `assets/css/brand.css`.

Document the new section's schema here.

## When to introduce a real content collection

E.g. blog posts, case studies, or workshop event pages — then create `content/blog/`, `content/cases/`, archetypes for each, and add a layout under `layouts/<section>/`. The `seo-jsonld.html` partial already has an `Article` branch ready for blog posts.
