# hugo-seo-compare

Compare two SEO audit snapshots to track progress and catch regressions.

## Triggers
"SEO diff", "compare seo", "seo before after", "seo progress", "audit comparison"

## When to Use
- Measure SEO gains sprint-over-sprint
- Identify newly introduced regressions since the last audit
- Produce `.seo/YYYY-MM-DD/SEO_AUDIT-{TYPE}-comparrison.md`
- Verify that a specific SEO fix landed as expected

## Which Files to Compare

1. Read `.seo/readme.md` to find the latest run entries and identify the audit type
2. Compare only within the same audit type: `General` with `General`, `Technical` with `Technical`
3. **Same-day rule**: compare earliest `hhmm` vs latest `hhmm` for that type on that day
4. **Cross-day fallback**: if only one same-type file exists today, use the latest same-type file from the previous date folder as baseline

## Comparison Process

1. Read both audit files in full
2. For every section identify: ✅ moved from ⚠️/❌ | ⚠️ still unresolved | 🆕 new items
3. Score the health delta (e.g. `7.2/10 → 7.8/10`)
4. Write or overwrite the matching typed comparison file
5. Do not append a new score row in `.seo/readme.md` unless a new audit snapshot was created in the same workflow

## Output Structure

```markdown
# SEO Comparison — YYYY-MM-DD
> Type: General or Technical
> Baseline: hh:mm → Current: hh:mm
## Score: X.X/10 → Y.Y/10
| Category | Before | After | Delta |
## ✅ Improvements
## ⚠️ Remaining Gaps (priority order)
## 🆕 New Additions
---
## Direct Side-by-Side Comparison
### [Dimension]
| Aspect | Before | After | Impact |
```

## Key SEO Dimensions to Compare

| Dimension | Check |
|-----------|-------|
| Meta descriptions | 140–165 chars on all pages |
| JSON-LD schema | Organization, Course, Service present and valid |
| OG / Twitter Card | Implemented in `head.html` |
| `lastmod` | Reflects actual update dates |
| Legal pages | Privacy Policy + Terms present |
| Core Web Vitals | LCP, CLS, INP pass thresholds |
| Robots.txt | Allows crawlers, references sitemap |

## Comparison File Naming

- General series: `SEO_AUDIT-GENERAL-comparrison.md`
- Technical series: `SEO_AUDIT-TECHNICAL-comparrison.md`

Keep the comparison file aligned to the audit type being compared.
