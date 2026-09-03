# hugo-setup-vitals

Set up automated Core Web Vitals monitoring via GitHub Agentic Workflow (`gh-aw`).

## Triggers
"core web vitals", "LCP INP CLS", "performance monitoring", "gh-aw", "PageSpeed Insights monitoring"

## When to Use
- Close the "Core Web Vitals not measured" SEO audit gap
- Configure daily LCP / INP / CLS regression alerts via PageSpeed Insights
- Install and authenticate the `gh-aw` CLI

## Prerequisites

```bash
gh extension install github/gh-aw
gh aw init   # once per repo
```

## COPILOT_GITHUB_TOKEN (Critical)

The agent **silently exits with 0 turns** if this token is missing — no error shown. Create a **fine-grained PAT** (not classic, starts with `github_pat_...`):

- **Account permissions → Copilot Requests**: Read-only ← this is the required permission

```bash
gh aw secrets bootstrap   # interactive; detects all missing secrets
# or directly:
gh aw secrets set COPILOT_GITHUB_TOKEN --value "github_pat_..."
```

Common mistakes: classic PAT (`ghp_` prefix), missing Copilot Requests permission, secret not set.

## Workflow File

Source at `.github/workflows/hugo-vitals.md` — **never edit the compiled `.lock.yml` directly**. Recompile after any frontmatter edit:

```bash
gh aw compile
```

## Critical Permissions Rules

| Rule | Reason |
|------|--------|
| Do NOT add `issues: write` | `gh-aw` strict mode blocks it — use `safe-outputs.create-issue` instead |
| DO add `issues: read` + `pull-requests: read` | Required by `github` toolset with `[default]` toolsets |
| Use `chrome` ecosystem identifier | `pagespeedinsights.googleapis.com` causes compile warning; `chrome` unlocks all `*.googleapis.com` |

## Workflow Frontmatter Pattern

```yaml
permissions:
  contents: read
  issues: read
  pull-requests: read
tools:
  github:
    toolsets: [default]
  chrome-devtools: {}
network:
  allowed:
    - defaults
    - chrome
safe-outputs:
  create-issue:
    max: 1
```

See `setup-agentic-wf` skill for full setup sequence.
