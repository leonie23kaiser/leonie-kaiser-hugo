# Deploy

**Live deploy is GitHub Pages.** No Azure, no rsync, no KAS hosting — those were an earlier, since-abandoned plan. If you're reading old commit history or notes that mention Azure Static Web Apps, workload identity federation, or an rsync-to-KAS deploy: that infrastructure doesn't exist anymore, don't act on it.

## Workflow — `.github/workflows/deploy-pages.yml`

```yaml
on:
  push:
    branches: [main]
    paths:
      - 'src/growthtogether.at/**'
      - '.github/workflows/deploy-pages.yml'
  workflow_dispatch:
  schedule:
    - cron: '0 8 * * 2'   # Tuesday 08:00 UTC
```

Three triggers:
1. **Push to `main`** touching `src/growthtogether.at/**` or the workflow file itself.
2. **Manual dispatch** (`workflow_dispatch` — run from the Actions tab or `gh workflow run deploy-pages.yml`).
3. **Weekly cron, Tuesdays 08:00 UTC** — exists specifically to publish **future-dated blog posts** on schedule (see below). This means the site can go live with new content even without a push, on that day.

### Build job

```bash
hugo --source src/growthtogether.at --minify --gc --buildFuture --baseURL "https://leoniekaiser.com/"
```

Hugo 0.135.0 extended, installed fresh each run (`.deb` package, not a cached action). `--buildFuture` is what makes the cron trigger meaningful — without it, future-dated journal posts wouldn't publish until a push happened after their date.

### Deploy job

Standard `actions/deploy-pages@v4` after `actions/upload-pages-artifact@v3` uploads `src/growthtogether.at/public`. Custom domain is `leoniekaiser.com`, set via `static/CNAME` — not configured through this workflow.

### Notify job — HITL for journal posts

Runs after every successful deploy. Scans `content/journal/*.md`, and for any post whose `date` falls within the last 7 days (i.e. just went live) and isn't a draft, opens a GitHub issue titled `Journal live: <slug>` (label `journal-live`, assigned to `leonie23kaiser`) if one doesn't already exist for that post. This is the **human-in-the-loop check** for blog content — a post can go live automatically via the Tuesday cron without anyone pushing, so this is how Leonie finds out and can review/pull it if needed.

**Never bypass this notify step for customer-visible posts.** If you build a different publishing path for journal content, it must open the same kind of review issue — see `CLAUDE.md`'s HITL-Notification section.

## Trigger a deploy

- **Automatic:** push to `main` touching `src/growthtogether.at/**`.
- **Automatic (content only, no push):** the Tuesday cron, if any journal post's `date` has arrived.
- **Manual:** `gh workflow run deploy-pages.yml --ref main`, or from the GitHub Actions UI.

## Pre-deploy checklist

1. Local build green: `hugo --source src/growthtogether.at --minify` exits 0, no warnings that matter.
2. Local browse: `hugo server --source src/growthtogether.at -D` on `http://localhost:1313`, check the changed pages.
3. JSON-LD still validates if `schema.html` or any front matter it reads changed (Schema.org Validator or Google's Rich Results Test).
4. **Explicit go-ahead from Leonie before pushing to `main`.** Live site is a paying client — this is a hard rule, not a suggestion.

## Post-deploy checks

1. Watch the GitHub Actions run (Actions tab, or `gh run watch` if you have `gh` available).
2. Browse `https://leoniekaiser.com/` — confirm the change is live (GitHub Pages CDN can take a minute or two to reflect a new deploy).
3. Spot-check any page you changed, plus `/impressum/` and `/datenschutz/` as a baseline sanity check.
4. If a journal post just went live via the Tuesday cron, expect a `journal-live` issue — that's the review prompt, not a bug.

## Rollback

GitHub Pages serves whatever the last successful `deploy-pages.yml` run published. To roll back: `git revert` the offending commit(s) on `main` and push (triggers a new deploy with the reverted content), or re-run the workflow against an earlier commit via `workflow_dispatch` on that ref. There's no separate "previous deployment" UI to click back to — the fix is always a new deploy from the desired source state.

## Branch strategy note

Session convention in this repo (see `CLAUDE.md`): develop on a feature branch, only fast-forward/push to `main` on explicit request, since a push to `main` touching `src/growthtogether.at/**` immediately triggers a live deploy. Changes to `docs/`, `strategie/`, or other paths outside `src/growthtogether.at/**` don't trigger the workflow at all — those can be pushed to `main` more freely without a "deploy" implication, but still follow whatever explicit instruction was given for that session.
