# hugo-custom-domain-swa

Bind a custom domain to an Azure Static Web Apps environment.

## Triggers
"custom domain", "bind domain", "CNAME setup", "blue.integrations.at", "DNS validation", "domain binding"

## When to Use
- Adding `blue.integrations.at` or another hostname to a SWA slot
- Setting up TXT validation or CNAME DNS records
- Troubleshooting domain validation failures in M365 DNS

## Key Insight: Always Use TXT Token Validation

Default CNAME-first approach fails with `CNAME Record is invalid` if DNS doesn't exist yet. Always use `--validation-method dns-txt-token`.

## Step-by-Step Process

```bash
# 1. Initiate binding and immediately Ctrl+C (token is already generated)
az account set --subscription 5e525bff-201c-49f0-bc0c-a5d35d4705ec
az staticwebapp hostname set \
  --name integrations-website-blue \
  --resource-group rg-integrations-website \
  --hostname blue.integrations.at \
  --validation-method dns-txt-token 2>&1
# Ctrl+C after the WARNING appears

# 2. Get the validation token
az staticwebapp hostname show \
  -n integrations-website-blue -g rg-integrations-website \
  --hostname blue.integrations.at \
  --query "validationToken" -o tsv
```

## Required DNS Records

| Type | Host | Value | TTL |
|------|------|-------|-----|
| `TXT` | `_dnsauth.blue` | `<validationToken>` | 3600 |
| `CNAME` | `blue` | `red-coast-07b078e03.4.azurestaticapps.net` | 3600 |

## ⚠️ Microsoft 365 DNS

M365 DNS is **authoritative** when Microsoft nameservers are used. Always add records in **M365 Admin Center** (Settings → Domains → integrations.at → DNS records), not at the registrar. Host field only needs the subdomain part (`_dnsauth.blue`, `blue`).

## Verify DNS Propagation

```bash
nslookup -type=TXT _dnsauth.blue.integrations.at
nslookup blue.integrations.at
```

## Finalize Binding (after DNS propagates)

```bash
az deployment group create \
  --name "blue-infra" \
  --resource-group rg-integrations-website \
  --template-file infra/blue.bicep \
  --parameters infra/blue.parameters.json bindCustomDomain=true

az staticwebapp hostname list \
  --name integrations-website-blue \
  --resource-group rg-integrations-website -o table
```

## Project Values

| Environment | Custom Domain | SWA Default Hostname |
|-------------|--------------|----------------------|
| Blue | `blue.integrations.at` | `red-coast-07b078e03.4.azurestaticapps.net` |
| Prod | `integrations.at` | (see `.hugo/hugo.config.json`) |
