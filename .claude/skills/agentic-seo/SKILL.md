---
name: agentic-seo
description: >-
  Master skill for SEO auditing, optimization, and Core Web Vitals tracking on the leoniekaiser.com Hugo site.
  Delegates to the correct narrow leaf skill.
  Use when auditing SEO health, updating meta descriptions or title tags, adding structured data (JSON-LD),
  comparing audit snapshots, setting up performance monitoring, optimizing for AI/GEO citation, writing
  AEO content blocks, or planning programmatic SEO pages. Triggers on: "SEO audit", "meta description",
  "structured data", "schema markup", "title tags", "open graph", "core web vitals", "LCP", "CLS", "INP",
  "seo compare", "seo optimize", "ranking", "sitemap", "GEO", "AI citation", "AI Overviews", "llms.txt",
  "programmatic SEO", "pSEO", "answer engine", "featured snippets", "E-E-A-T", "content patterns".
license: Complete terms in LICENSE.txt
---

# agentic-seo — SEO & Performance Router

Routes SEO, structured data, and performance requests to the appropriate leaf skill references. For full audits, default to the core audit references first and load additional leaf skills only when the user explicitly asks for them or when a confirmed public finding requires them.

## Site Context (leoniekaiser.com)

| | |
|---|---|
| Live-Domain | `leoniekaiser.com` (GitHub Pages, `.github/workflows/deploy-pages.yml`) |
| Hugo-Root | `src/growthtogether.at/` (Verzeichnisname ist historisch, nicht umbenennen) |
| Sprache | de-AT, einsprachig, **Sie-Form**. Brand Voice kanonisch in `AGENTS.md` |
| Zielgruppe | kleine Gesundheitspraxen DACH, siehe `strategie/segmente.md` |
| JSON-LD | ein `@graph` in `layouts/partials/schema.html`, gebaut mit `dict` + `jsonify` |
| robots.txt | generiert aus `layouts/robots.txt` (KI-Bots ausdrücklich erlaubt) |
| llms.txt | `static/llms.txt` |
| CSS | eine Datei: `assets/css/brand.css`, fingerprinted + SRI |
| Bilder | Quellen in `assets/images/`, `partials/picture.html` erzeugt WebP + srcset |

**Vor jeder Textänderung `AGENTS.md` lesen.** Bei Konflikt zwischen diesem Skill
und `AGENTS.md` gewinnt `AGENTS.md` — insbesondere Wort-Blacklist (§9) und
CTA-Regeln (§12). Keine Ranking-Versprechen: die Seite darf laut Positionierung
Auffindbarkeit verbessern, aber keine Platzierungen zusagen.

## Default Execution Rule (Full Analysis)

Unless the user explicitly restricts scope (e.g. "only check technical SEO", "just update the meta tags"), load and apply the core audit references in this order:

1. Load `references/audit-general.md` — health review & roadmap
2. Load `references/audit-technical.md` — technical runtime audit + technical SEO foundations
3. Load `references/on-page.md` — titles, headings, E-E-A-T, internal linking
4. Load `references/ai-geo.md` — AI Overviews, GEO, llms.txt, AI bot rules
5. Load `references/schema-markup.md` — JSON-LD schema templates
6. Load `references/audit-compare.md` — before/after snapshot comparison, but only after the current audit is fully scored

Load these only when the user explicitly asks for them or when the task changes from auditing to implementation/planning:

- `references/optimize.md`
- `references/content-patterns.md`
- `references/programmatic.md`
- `references/setup-vitals.md`

Run findings from the core audit set in sequence. Consolidate into a single prioritized output unless the user asks for separate reports per area.

## Blocking Audit Boundary

- For SEO audits in this repository, score only what a crawler can discover from `robots.txt`, `sitemap.xml`, visible navigation, and public links reachable from audited pages.
- Do not create findings from hidden Hugo structure, front matter, `headless`, `build.render`, `build.list`, non-public section indexes, `hugo.toml` menu internals, or checked-in generated output unless those details leak into public runtime output.
- Do not force-check guessed routes or hidden collection URLs unless they appear in the visible nav, sitemap, robots rules, public HTML, or the user explicitly names them.
- Use code inspection only to confirm the root cause of a public finding. Code inspection is not audit evidence by itself.
- Do not score local preview host/port mismatches as SEO defects. Treat them as audit-environment notes unless the same mismatch is visible on a public deployment or the user explicitly asks to debug the local setup.

## Local-First Audit Policy

- For audits and optimization work in this repository, use the local Hugo preview or other local/dev instance first.
- Reuse an existing local app and browser session when the user has already provided one.
- Prefer browser/runtime inspection over terminal-driven process discovery.
- Do not test production URLs by default.
- Only inspect production when the user explicitly asks for production validation.
- Core Web Vitals monitoring setup remains a separate workflow and may target production when the user asks for monitoring infrastructure.

## When to Use This Skill

- Running a full SEO health audit across the site
- Updating meta descriptions, title tags, or Open Graph data for a page
- Adding or updating JSON-LD structured data (Course, Service, Organization schemas)
- Comparing two SEO audit snapshots to measure progress
- Setting up or monitoring Core Web Vitals (LCP, INP, CLS)
- Optimizing for AI citation, GEO, and answer engine visibility

**Trigger keywords:** `SEO audit`, `seo check`, `meta description`, `title tag`, `open graph`, `schema markup`, `JSON-LD`, `structured data`, `core web vitals`, `LCP`, `CLS`, `INP`, `ranking`, `sitemap`, `lastmod`, `seo compare`, `GEO`, `AI citation`, `AI Overviews`, `llms.txt`, `programmatic SEO`, `pSEO`, `answer engine`, `featured snippets`, `E-E-A-T`, `content patterns`

## Delegate Map

| Leaf skill reference | Covers |
| --- | --- |
| [`audit-general`](references/audit-general.md) | General SEO health review, scoring, and backlog |
| [`audit-technical`](references/audit-technical.md) | Technical runtime audit + crawlability, indexation, CWV, mobile, HTTPS, hreflang |
| [`optimize`](references/optimize.md) | Meta tags, OG data, JSON-LD schema updates |
| [`audit-compare`](references/audit-compare.md) | Before/after audit snapshot comparison |
| [`setup-vitals`](references/setup-vitals.md) | Core Web Vitals automated monitoring setup |
| [`on-page`](references/on-page.md) | Titles, meta descriptions, headings, E-E-A-T, internal linking |
| [`ai-geo`](references/ai-geo.md) | AI Overviews, ChatGPT/Perplexity citation, GEO methods, llms.txt |
| [`schema-markup`](references/schema-markup.md) | JSON-LD templates for all schema types |
| [`content-patterns`](references/content-patterns.md) | AEO/GEO content block patterns (definition, FAQ, stats, quotes) |
| [`programmatic`](references/programmatic.md) | Programmatic SEO at scale — 12 playbooks, templates, locations |

> `hugo-expert` is the top-level router. For deployment of monitoring infrastructure, coordinate with `hugo-deploy`.

## Example Prompts

- "Run an SEO audit." → loads all leaf skills, produces consolidated report
- "Run a full SEO audit of the site." → same, full analysis across all dimensions
- "Run only a technical SEO audit." → loads `audit-technical` only
- "Update the meta description and JSON-LD schema for the training page." → loads `optimize` only
- "Compare the March SEO audit against the February baseline." → loads `audit-compare` only
- "Set up automated Core Web Vitals monitoring for leoniekaiser.com." → loads `setup-vitals` only
