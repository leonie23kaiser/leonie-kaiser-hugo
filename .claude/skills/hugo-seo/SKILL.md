---
name: hugo-seo
description: >-
  Master skill for SEO auditing, optimization, and Core Web Vitals tracking on the integrations.at Hugo site.
  Delegates to the correct narrow leaf skill.
  Use when auditing SEO health, updating meta descriptions or title tags, adding structured data (JSON-LD),
  comparing audit snapshots, or setting up performance monitoring. Triggers on: "SEO audit", "meta description",
  "structured data", "schema markup", "title tags", "open graph", "core web vitals", "LCP", "CLS", "INP",
  "seo compare", "seo optimize", "ranking", "sitemap".
license: Complete terms in LICENSE.txt
---

# hugo-seo — SEO & Performance Router

Routes SEO, structured data, and performance requests to the appropriate narrow leaf skill. Do not implement directly — delegate immediately.

## Required Execution Rule

- After choosing a route from the delegate map, you MUST load and follow the referenced leaf skill file before doing any SEO work.
- The router skill alone is not enough context to execute an audit, optimization, comparison, or vitals task.
- Example: for a general SEO audit, first load `references/hugo-seo-audit-general.md`, then execute that workflow.
- If the leaf skill is not loaded yet, stop routing and load it before continuing.

## Local-First Audit Policy

- For audits and optimization work in this repository, use the local Hugo preview or other local/dev instance first.
- Do not test production URLs by default.
- Only inspect production when the user explicitly asks for production validation.
- Core Web Vitals monitoring setup remains a separate workflow and may target production when the user asks for monitoring infrastructure.

## When to Use This Skill

- Running a full SEO health audit across the site
- Updating meta descriptions, title tags, or Open Graph data for a page
- Adding or updating JSON-LD structured data (Course, Service, Organization schemas)
- Comparing two SEO audit snapshots to measure progress
- Setting up or monitoring Core Web Vitals (LCP, INP, CLS)

**Trigger keywords:** `SEO audit`, `seo check`, `meta description`, `title tag`, `open graph`, `schema markup`, `JSON-LD`, `structured data`, `core web vitals`, `LCP`, `CLS`, `INP`, `ranking`, `sitemap`, `lastmod`, `seo compare`

## Delegate Map

| Request type                                | Leaf skill to invoke                                                 |
| ------------------------------------------- | -------------------------------------------------------------------- |
| General SEO health review or roadmap        | [`hugo-seo-audit-general`](references/hugo-seo-audit-general.md)     |
| Technical local runtime SEO audit           | [`hugo-seo-audit-technical`](references/hugo-seo-audit-technical.md) |
| Update meta tags, OG data, JSON-LD schema   | [`hugo-seo-optimize`](references/hugo-seo-optimize.md)               |
| Compare before/after SEO audit snapshots    | [`hugo-seo-compare`](references/hugo-seo-compare.md)                 |
| Set up Core Web Vitals automated monitoring | [`hugo-setup-vitals`](references/hugo-setup-vitals.md)               |

> `hugo-expert` is the top-level router. For deployment of monitoring infrastructure, coordinate with `hugo-deploy`.

## Example Prompts

- "Run a general SEO audit of the site and give me the broader backlog."
- "Run a technical SEO audit against the local agentic-ai area page."
- "Update the meta description and JSON-LD schema for the training page."
- "Compare the March SEO audit against the February baseline."
- "Set up automated Core Web Vitals monitoring for integrations.at."
