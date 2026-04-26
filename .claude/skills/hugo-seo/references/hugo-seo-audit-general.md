# hugo-seo-audit-general

Run a broader SEO health audit across the integrations.at Hugo site.

This is the code-first and strategy-oriented audit. It should answer the bigger SEO question: how healthy is the site overall, what moved since the last broad review, and what should be fixed next across technical foundations, on-page SEO, content quality, and authority.

## Local-First Execution Policy

- Use the local Hugo preview or another local/dev URL first when page examples are needed.
- Do not inspect production URLs unless the user explicitly asks for production validation.
- If the local preview is unavailable, continue with codebase inspection and clearly call out the missing runtime checks.

## Triggers
"general seo audit", "seo health review", "overall seo audit", "seo roadmap", "why am i not ranking"

## When to Use
- Produce a broad SEO snapshot for the whole site
- Review titles, descriptions, heading structure, canonical setup, schema coverage, content quality, and authority signals
- Summarize progress across audits at an executive level
- Build or refresh a prioritized SEO backlog

## Preferred Audit Inputs

1. Repository code inspection for templates, front matter, and generated assets
2. Local Hugo preview for representative spot checks
3. Existing `.seo/` snapshots, comparison files, and relevant workflow or issue history

## Audit Output Convention

General audits use the `GENERAL` series:

```
.seo/YYYY-MM-DD/SEO_AUDIT-GENERAL-hhmm.md         ← general audit snapshot
.seo/YYYY-MM-DD/SEO_AUDIT-GENERAL-comparrison.md  ← latest general comparison
.seo/readme.md                                    ← runs log + type-specific charts
```

`hhmm` is the 24-hour zero-padded run time. Each run is a full snapshot.

## Baseline-Finding Algorithm

1. List `.seo/{today}/` and find `SEO_AUDIT-GENERAL-*.md`
2. Sort by `hhmm` descending and use the latest same-type run as baseline
3. If no same-type file exists today, scan earlier date folders for the latest `SEO_AUDIT-GENERAL-*.md`
4. If no typed general baseline exists yet, fall back to the latest legacy untyped broad audit and note the fallback explicitly
5. Write the new audit as `SEO_AUDIT-GENERAL-{current hhmm}.md`
6. Auto-generate or update `SEO_AUDIT-GENERAL-comparrison.md`
7. Append a `General` row in `.seo/readme.md` and update only the general chart

## Runs Log

Append to `.seo/readme.md` under `## SEO Runs` with newest rows first:

| Date | Time | Type | Score | Technical SEO | On-Page SEO | Content Quality | Authority |

Only update the general progression chart when this skill writes a new run.

## Audit Priority Order

1. Crawlability and indexation
2. Technical foundations and schema coverage
3. On-page optimization
4. Content quality and internal linking
5. Authority, trust signals, and off-site gaps
