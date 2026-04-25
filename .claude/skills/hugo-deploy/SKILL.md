---
name: hugo-deploy
description: >-
  Master skill for CI/CD, deployment, and hosting operations for the integrations.at Hugo site on Azure
  Static Web Apps. Delegates to the correct narrow leaf skill.
  Use when deploying to Azure SWA, fixing GitHub Actions workflows, setting up OIDC authentication,
  binding custom domains, or configuring Core Web Vitals monitoring. Triggers on: "deploy", "deployment",
  "GitHub Actions", "workflow", "CI/CD", "custom domain", "DNS", "SWA", "OIDC", "workload identity".
license: Complete terms in LICENSE.txt
---

# hugo-deploy — Deployment & CI/CD Router

Routes deployment, CI/CD, and hosting requests to the appropriate narrow leaf skill. Do not implement directly — delegate immediately.

## When to Use This Skill

- Deploying the Hugo site to Azure Static Web Apps (prod or blue)
- Debugging or fixing a failing GitHub Actions build/deploy workflow
- Setting up or rotating OIDC Workload Identity Federation secrets
- Binding a custom domain to a SWA environment
- Setting up automated Core Web Vitals monitoring

**Trigger keywords:** `deploy`, `deployment`, `GitHub Actions`, `workflow`, `CI/CD`, `pipeline`, `custom domain`, `DNS`, `CNAME`, `SWA`, `OIDC`, `workload identity`, `vitals monitoring`

## Delegate Map

| Request type                                       | Leaf skill to invoke                                             |
| -------------------------------------------------- | ---------------------------------------------------------------- |
| Deploy Hugo site to Azure SWA (prod or blue)       | [`hugo-deploy-swa`](references/hugo-deploy-swa.md)               |
| Set up or update Azure infrastructure (Bicep/OIDC) | [`hugo-setup-iac`](references/hugo-setup-iac.md)                 |
| Bind a custom domain to a SWA environment          | [`hugo-custom-domain-swa`](references/hugo-custom-domain-swa.md) |
| Set up Core Web Vitals automated monitoring        | [`hugo-setup-vitals`](references/hugo-setup-vitals.md)           |

> `hugo-expert` is the top-level router. For infrastructure-only changes (no deploy), prefer `hugo-config` → `hugo-setup-iac`.

## Example Prompts

- "Fix the failing GitHub Actions deployment workflow."
- "Deploy the Hugo site to the blue staging environment."
- "Bind blue.integrations.at as a custom domain on the SWA blue slot."
- "Set up automated Core Web Vitals monitoring via GitHub Agentic Workflow."
