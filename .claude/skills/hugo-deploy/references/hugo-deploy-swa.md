# hugo-deploy-swa

Deploy and configure a Hugo site on Azure Static Web Apps using GitHub Actions, OIDC, and the SWA CLI when local emulation or SWA runtime configuration is needed.

## Triggers
"deploy hugo", "swa deploy", "github actions deployment", "oidc deployment", "fix workflow", "swa init", "swa start", "staticwebapp.config", "swa cli"

## When to Use
- Triggering or debugging a deploy to prod or blue SWA environment
- Fixing a failing GitHub Actions workflow step
- Setting up or rotating OIDC deployment tokens
- Running SWA CLI locally to validate routes, auth, and API integration
- Creating or updating `staticwebapp.config.json`
- Initializing SWA CLI config correctly with `swa init`

## Scope Split

- Use this reference for SWA deployment flow, SWA CLI usage, and SWA runtime configuration.
- Use the repository's `docs/` for project-specific workflow names, secret names, deployment paths, and environment inventory.
- Keep infrastructure creation and identity setup in `hugo-setup-iac`.

## ⚠️ Parameter File Convention (integrations.at)

`infra/azd-main.parameters.json` uses **fully hardcoded values only** — no `${AZURE_*}` environment variable substitutions. When updating deployment values, edit the parameter file directly. Never introduce `${...}` substitutions.

## Key Insight: OIDC + SWA Deploy Action

`azure/static-web-apps-deploy@v1` **cannot use the OIDC session directly**. After `azure/login@v2`, retrieve the SWA deployment token via Azure CLI and pass it explicitly.

## SWA CLI Rules

- Install the CLI with `npm install -D @azure/static-web-apps-cli` when the repo does not already provide it.
- Always use `swa init` to generate `swa-cli.config.json`.
- Never hand-author `swa-cli.config.json` from scratch.
- `staticwebapp.config.json` is the runtime config file and can be created or edited directly.

## Configuration Files

| File | Purpose | Rule |
| --- | --- | --- |
| `swa-cli.config.json` | Local SWA CLI configuration | Generate with `swa init`; customize only after generation |
| `staticwebapp.config.json` | Runtime routing, auth, headers, and API runtime | Can be created or edited manually |

Example `staticwebapp.config.json`:

```json
{
  "navigationFallback": {
    "rewrite": "/index.html",
    "exclude": ["/images/*", "/css/*"]
  },
  "routes": [
    { "route": "/api/*", "allowedRoles": ["authenticated"] }
  ],
  "platform": {
    "apiRuntime": "node:20"
  }
}
```

## SWA CLI Workflow

Use this workflow when the task includes local SWA setup, runtime config validation, or direct SWA CLI deployment.

```bash
# 1. Install CLI if needed
npm install -D @azure/static-web-apps-cli

# 2. Initialize SWA config
npx swa init

# 3. Build the site if the repo requires a build step
npm run build

# 4. Run the local SWA emulator
npx swa start

# 5. Authenticate only when a direct CLI deployment is required
npx swa login

# 6. Deploy if using the CLI path
npx swa deploy --env production
```

## Common SWA CLI Commands

```bash
npx swa init
npx swa init --yes
npx swa start
npx swa start ./dist
npx swa start ./dist --api-location ./api
npx swa start http://localhost:3000
npx swa deploy
npx swa deploy --env production
npx swa deploy --dry-run
```

## Local Emulation Notes

- Use `swa start` to validate route rewriting, authentication flows, and API proxying before deployment.
- For API-backed sites, pass `--api-location` or configure it through `swa init` output.
- For dev-server-backed sites, point `swa start` at the dev server URL instead of the built output.
- Common emulator port is `4280`; Angular dev servers commonly use `4200`.

## Verified Workflow Pattern

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: actions/checkout@v4
    with: { fetch-depth: 0 }

  - name: Setup Hugo
    uses: peaceiris/actions-hugo@v2
    with: { hugo-version: '0.121.0', extended: true }

  - name: Build Hugo Site
    run: hugo --source <site-source> --minify

  - name: Azure Login (Workload Identity)
    uses: azure/login@v2
    with:
      client-id: ${{ secrets.<AZURE_CLIENT_ID> }}
      tenant-id: ${{ secrets.<AZURE_TENANT_ID> }}
      subscription-id: ${{ secrets.<AZURE_SUBSCRIPTION_ID> }}

  - name: Get SWA Deployment Token
    run: |
      SWA_TOKEN=$(az staticwebapp secrets list \
        --name <swa-name> \
        --resource-group <resource-group> \
        --query "properties.apiKey" -o tsv)
      echo "::add-mask::$SWA_TOKEN"
      echo "SWA_DEPLOYMENT_TOKEN=$SWA_TOKEN" >> $GITHUB_ENV

  - name: Deploy to Static Web Apps
    uses: azure/static-web-apps-deploy@v1
    with:
      azure_static_web_apps_api_token: ${{ env.SWA_DEPLOYMENT_TOKEN }}
      repo_token: ${{ secrets.GITHUB_TOKEN }}
      action: upload
      app_location: <built-app-path>
      output_location: ""
```

Use the repository's `docs/` and workflow files for exact values.

## Deployment Checklist

1. Confirm the repository's documented build and output path in `docs/`.
2. Confirm whether the project deploys through GitHub Actions, SWA CLI, or both.
3. If using OIDC in GitHub Actions, log in with `azure/login@v2`, then fetch the SWA deployment token explicitly.
4. If using SWA CLI locally, run `swa init` before `swa start` or `swa deploy`.
5. Validate `staticwebapp.config.json` placement and route behavior before deployment.

## Project Workflow Inventory

| File | Environment | Trigger | SWA Name |
|------|-------------|---------|----------|
| `hugo-deploy-swa.yml` | Prod | push `master`, `workflow_dispatch` | `integrations-website` |
| `hugo-deploy-swa-blue.yml` | Blue | `workflow_dispatch` | `integrations-website-blue` |
| `hugo-deploy-swa-elements-blue.yml` | Blue + Angular Element | `workflow_dispatch` | `integrations-website-blue` |

## Project Secrets

Read the repository's `docs/` and workflow files for the exact secret inventory used by this project.

Generic command pattern:

```bash
gh secret set <NAME> --body "<value>" --repo <owner>/<repo>
```

## Troubleshooting

| Issue | Guidance |
| --- | --- |
| Client routes return 404 | Add or fix `navigationFallback` in `staticwebapp.config.json` |
| API endpoints return 404 | Check `apiLocation`, API runtime, and function exports |
| Build output not found | Verify build output matches `app_location` or SWA CLI output settings |
| Local auth does not work | Use the emulator auth endpoints such as `/.auth/login/<provider>` |
| Config appears ignored | Ensure `staticwebapp.config.json` is placed in the deployed app source or output folder |
| Deployment token problems | Regenerate or re-fetch the deployment token before deploying |
| OIDC login succeeds but deploy fails | Confirm the workflow fetches and passes the SWA deployment token explicitly |

Useful debug commands:

```bash
npx swa start --verbose log
npx swa deploy --dry-run
npx swa --print-config
```

## `lastmod` in CI

The prod workflow auto-updates `lastmod` in any changed content `.md` file between checkout and build. `enableGitInfo` is NOT enabled — `lastmod` comes from front matter.
