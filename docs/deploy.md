# Deploy

Leonie's site has **two deploy paths**:

1. **Azure Static Web Apps** (active CI/CD target) — auto-deploys on push to `main`.
2. **rsync-to-KAS** (legacy, still serving live traffic) — manual fallback until DNS-Cutover.

DNS for `growthtogether.at` still points to KAS. Cutover to SWA is pending Leonie's go-ahead (registrar access + final domain decision).

## Active — Azure Static Web Apps (CI/CD)

### Resources

| Item | Value |
|---|---|
| Azure Account | `office@projekt-entwicklung.at` |
| Subscription | `Azure subscription 1` (`ee869573-d7f5-422f-af3e-3d9d450a834d`) |
| Tenant | `08dd661d-3de5-4275-8753-d2dd426670b2` |
| Resource Group | `rg-leonie-growthtogether` (West Europe) |
| SWA Resource | `swa-growthtogether` (Free SKU) |
| Default hostname | `https://purple-island-01f081e03.7.azurestaticapps.net/` |
| Managed Identity | `mi-github-leonie` (Client-ID `26ad15bb-5552-4e93-a11d-1bc30b15844c`) |
| Identity role | Contributor on `rg-leonie-growthtogether` |

### Workload Identity Federation (no secrets in CI)

Federated credential on `mi-github-leonie`:

- **Subject:** `repo:aeshilion/leonie-kaiser-hugo:ref:refs/heads/main`
- **Issuer:** `https://token.actions.githubusercontent.com`
- **Audience:** `api://AzureADTokenExchange`

GitHub repo secrets (no client secret — OIDC only):

- `AZURE_CLIENT_ID` — Managed Identity Client-ID
- `AZURE_TENANT_ID`
- `AZURE_SUBSCRIPTION_ID`

### Workflow

`.github/workflows/deploy-swa.yml`:

```
on: push to main, paths: src/growthtogether.at/** + workflow file
→ checkout
→ Hugo 0.135.0 extended (peaceiris/actions-hugo@v3)
→ hugo --source src/growthtogether.at --minify --gc
→ azure/login@v2 with WIF (id-token: write)
→ az staticwebapp secrets list → SWA deployment token
→ Azure/static-web-apps-deploy@v1, app_location=src/growthtogether.at/public, skip_app_build=true
```

First deploy (commit `e84984e`) verified green, default hostname returns 200.

### Trigger a deploy

- **Automatic:** push to `main` touching `src/growthtogether.at/**`.
- **Manual:** `gh workflow run deploy-swa.yml --ref main` (or run from GitHub UI).

### Pre-deploy checklist

1. Local build green: `hugo --source src/growthtogether.at --minify` exit 0.
2. Local browse: `hugo server --source src/growthtogether.at` on `http://localhost:1313`.
3. Mobile check (iPhone 14 emulation), all sections render.
4. JSON-LD validates (Schema.org Validator).
5. Lighthouse mobile — target SEO ≥ 95, Performance ≥ 90.
6. **Explicit go-ahead from Emanuel before pushing to `main`.** Live site is a paying client.

### Post-deploy checks

1. Watch GitHub Actions run: `gh run watch` or web UI.
2. `curl -I https://purple-island-01f081e03.7.azurestaticapps.net/` — expect `200 OK`.
3. Browse default hostname in incognito — confirm fresh content.
4. Test `/impressum/` and `/datenschutz/` — `200 OK`.
5. Once DNS is switched: same checks against `https://growthtogether.at/`.

### Rollback

SWA keeps previous deployments — revert by re-running the workflow on a previous commit, or `git revert` and push. Worst case: switch DNS back to KAS (still serving the last rsync'd build until decommissioned).

## Pending — DNS-Cutover (Phase 6 step 6)

**Blocked on Leonie:**

- Decision: `growthtogether.at` (current) vs. `leoniekaiser.com` (alternative).
- Registrar/DNS access (currently All-Inkl. KAS DNS).
- Confirmation that MX/SPF/DMARC exist and what the current values are (must NOT be touched).
- Subdomain inventory (anything besides apex + `www`?).

**Switch procedure (when ready):**

1. In Azure Portal → SWA `swa-growthtogether` → Custom domains → Add `growthtogether.at`.
2. Azure issues a TXT validation record (`_dnsauth.growthtogether.at` with a token).
3. At All-Inkl. KAS DNS:
   - Add `TXT _dnsauth` with the Azure-provided token.
   - For apex `growthtogether.at`: ALIAS / ANAME → `purple-island-01f081e03.7.azurestaticapps.net` (KAS doesn't support ALIAS — fallback: A-records to SWA's published IPs, or migrate DNS to Cloudflare).
   - For `www`: CNAME → `purple-island-01f081e03.7.azurestaticapps.net`.
   - **Leave MX, SPF (TXT), DMARC (TXT) untouched.**
4. Wait for Azure to validate the TXT record (minutes to a few hours).
5. Azure auto-issues Let's Encrypt cert.
6. Verify `https://growthtogether.at/` resolves to SWA (`curl -I` should show Azure server headers).
7. Keep KAS rsync alive ~1–2 weeks as fallback. Then decommission.

**If switching to `leoniekaiser.com` instead:**

- Update `baseURL` in `src/growthtogether.at/config/_default/config.toml`.
- Update absolute URLs in `data/site.yaml` and `partials/seo-jsonld.html`.
- Add Custom Domain `leoniekaiser.com` in Azure SWA.
- Set 301 redirect from `growthtogether.at` → `leoniekaiser.com` (either via SWA `staticwebapp.config.json` once both domains are bound, or at the registrar level).
- Optional: rename `src/growthtogether.at/` → `src/leoniekaiser.com/` (convention only).

## Legacy — rsync to All-Inkl. KAS

Still serving `https://growthtogether.at/` until DNS-Cutover. Don't deploy here unless explicitly asked.

### Hosting

- **Provider:** All-Inkl.com (KAS)
- **Account:** w02124ee (shared with mountaingolf.eu / dasAuto)
- **SSH host:** `w01b2e95.kasserver.com`
- **SSH user:** `ssh-w02124ee`
- **Webroot:** `www/htdocs/w02124ee/growthtogether.at/`
- **TLS:** Let's Encrypt via KAS auto-issuance

Credentials: `kobra-knowledge/quick.md` and `~/.config/shelley/AGENTS.md` (`mountaingolf` codeword).

### Manual deploy command

```bash
hugo --source src/growthtogether.at --minify --baseURL https://growthtogether.at/

rsync -avz --delete src/growthtogether.at/public/ \
  ssh-w02124ee@w01b2e95.kasserver.com:www/htdocs/w02124ee/growthtogether.at/
```

With `sshpass`:

```bash
sshpass -p '<password>' rsync -avz --delete \
  src/growthtogether.at/public/ \
  ssh-w02124ee@w01b2e95.kasserver.com:www/htdocs/w02124ee/growthtogether.at/
```

### Decommission plan (post-cutover)

1. After DNS cutover + 1–2 weeks of SWA stability: archive last KAS `public/` snapshot locally.
2. Remove KAS webroot contents (or replace with a `410 Gone` placeholder).
3. Remove this section from the docs once decommissioned.

## Cost

| Item | Cost |
|---|---|
| Azure SWA Free tier | € 0 / month (100 GB bandwidth, 0.5 GB storage) |
| Custom domain on SWA | included |
| Workload Identity | included (no Azure AD premium needed) |
| KAS hosting | shared account, no Leonie-specific cost line |

The migration is a **workflow play**, not a cost play — auto-deploy on push, no manual rsync, branch previews possible.

## Tmux dev session

For active work, keep a long-running Hugo dev server in a tmux session `hugo-leonie` on port 1314:

```bash
tmux new -s hugo-leonie
cd ~/diamonds/kunden/kobra/leonie-kaiser-hugo
hugo server --source src/growthtogether.at -D --port 1314
```

Detach: `Ctrl-b d`. Reattach: `tmux attach -t hugo-leonie`.
