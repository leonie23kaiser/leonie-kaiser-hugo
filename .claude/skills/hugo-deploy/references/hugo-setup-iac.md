# hugo-setup-iac

Deploy and manage Azure infrastructure for Hugo Static Web Apps using Bicep.

## Triggers
"setup azure infra", "bicep deploy", "workload identity setup", "new swa environment", "blue environment", "managed identity"

## When to Use
- Setting up a new SWA environment (prod or blue/staging) from scratch
- Configuring Workload Identity Federation for GitHub Actions OIDC
- Deploying managed identities and assigning Azure roles
- Updating existing Bicep modules in `infra/`

## ⚠️ Always Read Config First

`.hugo/hugo.config.json` — read this BEFORE any Azure operation. Never ask for subscription ID, tenant ID, resource group, or client IDs.

After any deployment, **write outputs back to `.hugo/hugo.config.json`** immediately.

## ⚠️ Verify Bicep API Versions via microsoft-learn

Never assert Bicep resource API versions or resource property schemas from memory. Always verify via `microsoft-learn/microsoft_docs_search` or `microsoft-learn/microsoft_docs_fetch` before using any API version or writing any `resource '...'` declaration. Missing or wrong API versions cause silent validation failures that only surface at `azd up` time.

## Azure Values

| Setting | Value |
|---------|-------|
| Subscription | `5e525bff-201c-49f0-bc0c-a5d35d4705ec` (Hosting) |
| Tenant | `d92b247e-90e0-4469-a129-6a32866c0d0a` |
| Resource Group | `rg-integrations-website` |
| Location | `westeurope` |
| Blue MI Client ID | `ecfca7b0-e9e4-4a9e-bda4-ebea3be4d6cb` |

## IaC File Structure

| File | Scope | Purpose |
|------|-------|---------|
| `infra/main.bicep` | `subscription` | Prod: creates RG + SWA + Managed Identity + App Insights |
| `infra/main.parameters.json` | — | Prod parameters |
| `infra/blue.bicep` | `resourceGroup` | Blue/staging: SWA + Managed Identity |
| `infra/blue.parameters.json` | — | Blue parameters |
| `infra/modules/staticwebapp.bicep` | `resourceGroup` | Shared SWA module |
| `infra/modules/managedidentity.bicep` | `resourceGroup` | Managed Identity + federated credential |
| `infra/modules/swa-custom-domain.bicep` | `resourceGroup` | Custom domain binding (optional) |

## Key Design Decisions

- Blue and prod **share** `rg-integrations-website` — do not create a separate RG for staging
- Pass `resourceName: swaName` explicitly to avoid auto-suffix on SWA names
- Deploy with `bindCustomDomain=false` initially; set up DNS first; then redeploy with `bindCustomDomain=true`
- **Valid SWA regions**: `westeurope`, `eastus2`, `westus2`, `centralus`, `eastasia` — `eastus` is **not** valid

## Federated Credential Subject Format

```
repo:<org>/<repo>:ref:refs/heads/<branch>
```

- Prod (master): `repo:alexander-kastil/integrations.at:ref:refs/heads/master`
- Blue (classes): `repo:alexander-kastil/integrations.at:ref:refs/heads/classes`
