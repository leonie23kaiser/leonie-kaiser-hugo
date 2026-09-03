# optimize

Update SEO metadata and structured data on individual Hugo pages.

## Triggers
"meta description", "title tag", "schema markup", "lastmod", "open graph", "structured data", "Course schema", "Service schema"

## When to Use
- Write or improve a page's `<title>`, meta description, or Open Graph fields
- Add or update JSON-LD schema markup (Course, Service, Organization)
- Refresh `lastmod` timestamps in front matter after content changes

## Key Rules

- **Meta descriptions**: 140–165 characters. Set via `description:` in front matter.
- **Title tags**: ≤60 chars. No suffix is appended — `<title>` renders `{{ .Title }}`
  verbatim (home page uses `site.Title`). Put the brand in the title yourself when
  it helps, e.g. `KI für Gesundheitspraxen – Leonie Kaiser`.
- **lastmod**: Read from front matter only. `enableGitInfo` is on, but the
  frontmatter cascade is pinned to `["lastmod", "date"]` in
  `config/_default/config.toml` so the Git commit time never wins. Format:
  `lastmod: 'YYYY-MM-DD'`.
- **Language**: the site is single-language de-AT, Sie-Form. All titles,
  descriptions and schema strings are German. Brand voice is canonical in
  `AGENTS.md`.
- **Do not add inline schema to templates.** Edit `layouts/partials/schema.html` only.

## JSON-LD Partial Location

`src/growthtogether.at/layouts/partials/schema.html` — one `@graph` covering
Person + Organization + Service + FAQPage + AggregateRating + Reviews +
BreadcrumbList + AboutPage + ContactPage + WebSite + Speakable. Included from
`partials/head.html`.

Build JSON-LD with `dict` + `jsonify`, never string templates (repo convention).

## Schema Types by Page Condition

| Condition | Schema Type |
|-----------|-------------|
| `.IsHome` | `Person` + `Organization` + `WebSite` (@graph) |
| `type: "branche"` (Leistungsseiten, data in `data/branchen.yaml`) | `Service` + `FAQPage` |
| `type: "faq"` | `FAQPage` |
| `type: "referenzen"` | `AggregateRating` + `Review` |
| `section: "journal"` (Blog) | `BlogPosting` |
| `type: "ueber-mich"` / `impressum` | `AboutPage` / `ContactPage` |

## Blog Post (`journal`) — Required Front Matter Fields

```yaml
title: "≤60 Zeichen, Sie-Form"
description: "140–165 Zeichen"
date: 2026-09-02
lastmod: '2026-09-02'      # nur setzen, wenn inhaltlich überarbeitet
category: "EU AI Act"      # erscheint im Label über der Überschrift
cover: "images/…​.png"       # läuft durch partials/picture.html (WebP + srcset)
coverAlt: "Beschreibung"
ctaHeadline / ctaText      # thema-bezogener CTA, siehe AGENTS.md §12
```

## Leistungsseiten (`type: "branche"`) — Datenquelle

Inhalt kommt nicht aus dem Markdown, sondern aus `data/branchen.yaml`
(Felder: `slug`, `branche`, `schmerz`, `intro`, `usecases`, `beispiel`, `faq`).
Titel und Description dort ändern, nicht im Layout.

## Implementation Pattern

Always use `dict` + `jsonify | safeJS` — never string-interpolate JSON-LD:

```go-html-template
{{- $schema := dict "@context" "https://schema.org" "@type" "Service" "name" .Title -}}
<script type="application/ld+json">{{ $schema | jsonify | safeJS }}</script>
```

## Verify Schema in Browser

```js
JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent)
```

## Find Pages Without Description

```bash
grep -rLE "^description:" src/growthtogether.at/content --include="*.md"
```
