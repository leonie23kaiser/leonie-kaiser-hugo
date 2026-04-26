# hugo-seo-optimize

Update SEO metadata and structured data on individual Hugo pages.

## Triggers
"meta description", "title tag", "schema markup", "lastmod", "open graph", "structured data", "Course schema", "Service schema"

## When to Use
- Write or improve a page's `<title>`, meta description, or Open Graph fields
- Add or update JSON-LD schema markup (Course, Service, Organization)
- Refresh `lastmod` timestamps in front matter after content changes

## Key Rules

- **Meta descriptions**: 140–165 characters. Set via `description:` in front matter.
- **Title tags**: ≤60 chars. Site auto-appends ` – Integrations IT Solutions` to `{{ .Title }}`.
- **lastmod**: Read from front matter only — `enableGitInfo` is off. Format: `lastmod: 'YYYY-MM-DD'`.
- **Do not add inline schema to templates.** Edit `layouts/partials/ui-components/schema-jsonld.html` only.

## JSON-LD Partial Location

`src/integrations.at/layouts/partials/ui-components/schema-jsonld.html` — included in `head.html` after `<link rel="canonical">`.

## Schema Types by Page Condition

| Condition | Schema Type |
|-----------|-------------|
| `.IsHome` | `Organization` + `WebSite` (@graph) |
| `type: "classes"` | `Course` |
| `layout: "steps-layout"` or `type: "services"` | `Service` |

## Course Schema — Required Front Matter Fields

```yaml
description: "140–165 char description"
duration: 4          # → timeRequired: "P4D"
level: "Intermediate"
tags: ['Tag1']       # → keywords (comma-joined)
```

## Implementation Pattern

Always use `dict` + `jsonify | safeJS` — never string-interpolate JSON-LD:

```go-html-template
{{- $schema := dict "@context" "https://schema.org" "@type" "Course" "name" .Title -}}
<script type="application/ld+json">{{ $schema | jsonify | safeJS }}</script>
```

## Verify Schema in Browser

```js
JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent)
```

## Find Pages Without Description

```powershell
Get-ChildItem "src/integrations.at/content" -Filter "*.md" -Recurse |
  Where-Object { (Get-Content $_.FullName -Raw) -notmatch 'description:' } |
  Select-Object Name
```
