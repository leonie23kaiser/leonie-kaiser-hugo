# Content Model

Leonie's site has **no content collections in the classic Hugo sense and no `data/site.yaml`.** The homepage is built by a hardcoded template (`layouts/_default/home.html`) that reads only `content/_index.md`'s front matter (title/description for SEO) — the sections themselves (hero, "Kennen Sie das?", Leistungen, Datenschutz, Über mich, Prozess, Testimonials, Potenzialanalyse-Promo, Kontakt) are written directly in the template's HTML, not pulled from a data file.

The one real data-driven pattern is `data/branchen.yaml`, which powers the four "Leistungsbereich" sub-pages via the `branche` layout.

## `content/` tree

```
content/
  _index.md                         → homepage front matter only (title/description)
  ueber-mich.md                     → /ueber-mich/
  faq.md                            → /faq/ (also feeds FAQPage JSON-LD, see below)
  eu-ai-act/_index.md               → /eu-ai-act/  (type: eu-ai-act)
  dsgvo/_index.md                   → /dsgvo/      (type: dsgvo)
  leistungen/_index.md              → /leistungen/ (type: leistungen, overview page)
  leistung-termine-anfragen/_index.md      → /leistungen/termine-und-anfragen/
  leistung-dokumentation-wissen/_index.md  → /leistungen/dokumentation-und-wissen/
  leistung-nachsorge-bindung/_index.md     → /leistungen/nachsorge-und-kundenbindung/
  leistung-sichtbarkeit-inhalte/_index.md  → /leistungen/sichtbarkeit-und-inhalte/
  journal/_index.md                 → /blog/ (list page, alias /journal/)
  journal/<slug>.md                 → /blog/<slug>/ (individual posts)
  impressum.md                      → /impressum/
  datenschutz.md                    → /datenschutz/
```

Each `leistung-*` folder's `type: branche` front matter is what routes it to `layouts/branche/single.html`, which then looks up its matching entry in `data/branchen.yaml` by `branche_slug`. The four "Leistungsbereich" content folders are otherwise near-empty — all the actual copy lives in `branchen.yaml`.

## `data/branchen.yaml` — the four Leistungsbereiche

One list, one entry per Leistungsbereich (currently 4: Termine & Anfragen, Dokumentation & Wissen, Nachsorge & Kundenbindung, Sichtbarkeit & Inhalte). Read by `layouts/branche/single.html`, matched to the requesting page via `branche_slug` in the page's front matter.

```yaml
- slug: termine-anfragen                # matches content front matter's branche_slug
  url: /leistungen/termine-und-anfragen/
  branche: "Termine & Anfragen"         # H1 / card title
  schmerz: "..."                        # pain-point paragraph
  intro: "..."                          # benefit one-liner
  usecases:
    - titel: "..."
      desc: "..."
  beispiel:                             # illustrative (not a real client) scenario
    ausgangssituation: "..."
    vorgehen: "..."
    ergebnis: "..."
  faq:
    - q: "..."
      a: "..."
```

Editing conventions (per the file's own header comment): Sie-Form, gendered neutrally, no bullet-point fragments in `beispiel` (full sentences only), `Gedankenstriche` used sparingly, `beispiel` scenarios are explicitly illustrative and must never reference a real client. Brand voice rules are in `AGENTS.md` (repo root), which is canonical for wording.

## `content/journal/` — blog posts

Front matter fields actually read by `layouts/journal/list.html` and `layouts/journal/single.html`:

```yaml
---
title: "..."
slug: "..."                 # explicit slug (permalink uses config.toml's journal permalink /blog/:slug/)
description: "..."          # SEO + og:description
date: 2026-08-04
lastmod: 2026-08-04
author: "Leonie Kaiser"      # defaults to "Leonie Kaiser" if omitted
cover: "images/blog/cover-x.png"       # under assets/images/blog/
coverAlt: "..."              # defaults to .Title if omitted
coverCredit: "photographer / source"   # shown as a small credit line on the post
category: "..."              # single category, shown as a filter pill on /blog/
readingTime: 6                # minutes, shown as "N min Lesezeit"
tags: ["...", "..."]          # feeds JSON-LD keywords
draft: false
---
```

`summary` (front matter, optional) overrides the auto-generated teaser on the list page; falls back to `.Summary | plainify | truncate 160`.

Cover images live in `assets/images/blog/` and go through the `picture.html` pipeline. See `assets/images/blog/CREDITS.md` for image sourcing/licensing notes.

## `content/faq.md` — dual-source, keep in sync

**This file has a trap.** The `faqs:` front-matter list feeds *only* the Schema.org `FAQPage` JSON-LD. The visible FAQ accordion is hardcoded separately in `layouts/faq/single.html`. Both lists must stay identical (same questions, same order, matching answers) — the file itself has a comment warning about this. Whenever an FAQ answer changes, edit **both** files.

## `content/eu-ai-act/_index.md` and `content/dsgvo/_index.md`

Same pattern: `type: eu-ai-act` / `type: dsgvo` routes to a dedicated layout (`layouts/eu-ai-act/single.html`, `layouts/dsgvo/single.html`). Unlike `faq.md`, both layouts loop `.Params.faqs` directly (`{{ range .Params.faqs }}`) — **single source**, front matter drives both the visible accordion and the JSON-LD, no duplication trap here. Both feed `schema_type: "Article"` and get `BreadcrumbList` treatment via `partials/schema.html` — see [seo-jsonld.md](seo-jsonld.md).

## `content/impressum.md` and `content/datenschutz.md`

Standard Hugo single pages — front matter (`title`, `description`, `type`, `url`, `sitemap`) + Markdown body, rendered by `layouts/_default/single.html`.

## When to add a new Leistungsbereich

1. Add an entry to `data/branchen.yaml` with a unique `slug`.
2. Create `content/leistung-<name>/_index.md` with `type: branche`, `branche_slug: <slug>`, and matching `url`.
3. Link it from `layouts/leistungen/single.html` (the overview page) and anywhere else that lists all Leistungsbereiche (e.g. `layouts/branche/single.html`'s cross-links, footer if applicable).
4. Update `strategie/service-katalog.md` and `tools/pdf-templates/service-katalog/service-katalog.html` if the PDF catalogue should list it too — those are edited and regenerated by hand, not templated from `branchen.yaml`.

## When to add a new standalone page type

1. Add `content/<slug>/_index.md` (or `content/<slug>.md`) with a `type:` front-matter key.
2. Add `layouts/<type>/single.html`.
3. If it needs FAQ/Article/AboutPage JSON-LD, extend `partials/schema.html`'s conditionals (matched on `.Type`).
