# Deploy

Leonie's site has **two deploy paths**: the current rsync-to-KAS workflow (used for live deploys today) and the planned Azure Static Web Apps migration (mirrors `superleague-hugo`).

## Current — rsync to All-Inkl. KAS

### Hosting

- **Provider:** All-Inkl.com (KAS)
- **Account:** w02124ee
- **SSH host:** `w01b2e95.kasserver.com`
- **SSH user:** `ssh-w02124ee`
- **Webroot:** `www/htdocs/w02124ee/growthtogether.at/`
- **Domain:** growthtogether.at (DNS at All-Inkl.)
- **TLS:** Let's Encrypt via KAS auto-issuance

Credentials are in `kobra-knowledge/quick.md` and `~/.config/shelley/AGENTS.md` (`mountaingolf` codeword — same KAS account hosts dasAuto/mountaingolf.eu).

### Deploy command

```bash
# 1. Build for production
hugo --source src/growthtogether.at --minify --baseURL https://growthtogether.at/

# 2. Sync to KAS
rsync -avz --delete src/growthtogether.at/public/ \
  ssh-w02124ee@w01b2e95.kasserver.com:www/htdocs/w02124ee/growthtogether.at/
```

With `sshpass` (credentials in keyring — see `quick.md`):

```bash
sshpass -p '<password>' rsync -avz --delete \
  src/growthtogether.at/public/ \
  ssh-w02124ee@w01b2e95.kasserver.com:www/htdocs/w02124ee/growthtogether.at/
```

### Pre-deploy checklist

1. Build is green: `hugo --source src/growthtogether.at --minify` exit 0.
2. Local browse looks right: `hugo server --source src/growthtogether.at` and open `http://localhost:1313`.
3. Mobile check: emulate iPhone 14, scroll the whole page, all sections render.
4. JSON-LD validates (paste from view-source into Schema.org Validator).
5. Lighthouse mobile run — target SEO ≥ 95, Performance ≥ 90.
6. **Explicit go-ahead from Emanuel before deploying.** Never auto-deploy.

### Post-deploy checks

1. `curl -I https://growthtogether.at/` — expect `200 OK`, `cache-control` headers reasonable.
2. Browse `https://growthtogether.at/` in incognito — confirm fresh content (KAS doesn't aggressively cache HTML).
3. Test `/impressum/` and `/datenschutz/` — expect `200 OK`.
4. Spot-check OG: paste URL into LinkedIn/Slack post composer, confirm preview.

### Rollback

Keep the previous `public/` build under `~/diamonds/kunden/kobra/leonie-kaiser-hugo/.deploy-history/<timestamp>/` before deploying. To rollback: rsync that folder back to the webroot.

(History folder doesn't exist yet — add it once we automate the deploy.)

## Planned — Azure Static Web Apps + Workload Identity

Mirrors the `superleague-hugo` deploy pattern. Goal: zero-credentials CI deploy, automatic per-PR previews, lower cost than KAS hosting.

### Target architecture

```
GitHub push (main)
  → .github/workflows/hugo-deploy-swa.yml triggers on src/growthtogether.at/**
  → Hugo 0.135.0 build
  → azure/login@v2 with Workload Identity (no secrets)
  → deploy to Azure Static Web Apps
  → custom domain growthtogether.at → SWA endpoint
```

### Migration steps (not yet executed)

1. **Provision SWA resource** in Azure subscription. Region: West Europe. Name: `swa-growthtogether-prod`. SKU: Free (sufficient for marketing site traffic).
2. **Set up Workload Identity Federation:**
   - Create user-assigned managed identity in Azure.
   - Add federated credential trusting `repo:aeshilion/leonie-kaiser-hugo:ref:refs/heads/main`.
   - Grant SWA contributor role to the identity.
   - Stash `AZURE_CLIENT_ID` (and `TENANT_ID`, `SUBSCRIPTION_ID`) as GitHub secrets.
3. **Copy workflow** from `superleague-hugo/.github/workflows/hugo-deploy-swa.yml`. Adjust:
   - Path filter: `src/growthtogether.at/**`
   - Build command: `hugo --source src/growthtogether.at --minify`
   - SWA app/output paths
4. **First deploy** triggers automatically on next push to `main`. Verify deploy succeeds and the SWA preview URL renders correctly.
5. **Domain cutover:**
   - In Azure SWA, add custom domain `growthtogether.at`.
   - At All-Inkl. DNS, switch CNAME/A record to SWA endpoint.
   - Wait for SSL provisioning (SWA auto-issues).
   - Verify `https://growthtogether.at/` resolves to SWA, not KAS.
6. **Decommission KAS:** keep KAS deploy alive for 1–2 weeks as fallback. Then archive `public/` from KAS and remove the rsync workflow.

### Why not now?

- The KAS deploy works.
- DNS cutover is irreversible-ish during the TTL window. Want to do it deliberately, not bundled into restructure work.
- The bigger payoff is when `superleague-hugo` deploys to SWA — that's the proof-of-concept Marcus is paying for. Leonie can follow.

### Cost estimate

| Item | Cost |
|---|---|
| Azure SWA Free tier | € 0 / month (100 GB bandwidth, 0.5 GB storage — plenty for a marketing site) |
| Custom domain | included in Free tier |
| KAS hosting (today) | shared with mountaingolf.eu / dasAuto, no Leonie-specific cost line |

Migrating to SWA is **not** a cost play — it's a workflow play. Auto-deploy on push, no rsync, branch previews.

## Tmux dev session

For active work, the project keeps a long-running Hugo dev server in a tmux session called `hugo-leonie` on port 1314 (1313 is the default — 1314 keeps it free if a second site spins up).

```bash
tmux new -s hugo-leonie
cd ~/diamonds/kunden/kobra/leonie-kaiser-hugo
hugo server --source src/growthtogether.at -D --port 1314
```

Detach: `Ctrl-b d`. Reattach: `tmux attach -t hugo-leonie`.
