---
name: hugo-config
description: >-
  Master skill for configuration management in the integrations.at Hugo CMS: feature flags, environment
  config params, and Azure infrastructure. Delegates to the correct narrow leaf skill.
  Use when toggling a feature flag per environment, updating a named config parameter, setting up or
  updating Bicep infrastructure, or deploying infrastructure changes. Triggers on: "toggle feature",
  "enable feature", "disable feature", "update config", "feature flag", "infrastructure", "bicep", "IaC".
license: Complete terms in LICENSE.txt
---

# hugo-config — Configuration & Infrastructure Router

Routes configuration and infrastructure requests to the appropriate narrow leaf skill. Do not implement directly — delegate immediately.

## When to Use This Skill

- Turning a feature flag on or off for a specific environment (local / blue / green)
- Updating a named config parameter (e.g. `apiBaseUrl`) per environment
- Setting up or modifying Azure Static Web Apps infrastructure via Bicep
- Provisioning managed identities, roles, or OIDC credentials

**Trigger keywords:** `toggle`, `enable`, `disable`, `feature flag`, `config param`, `update config`, `infrastructure`, `bicep`, `IaC`, `provision`, `managed identity`

## Delegate Map

| Request type                                  | Leaf skill to invoke                                       |
| --------------------------------------------- | ---------------------------------------------------------- |
| Toggle a boolean feature flag per environment | [`hugo-toggle-feature`](references/hugo-toggle-feature.md) |
| Update a named config param per environment   | [`hugo-update-config`](references/hugo-update-config.md)   |
| Set up or update Azure infrastructure (Bicep) | [`hugo-setup-iac`](references/hugo-setup-iac.md)           |

> `hugo-expert` is the top-level router. For deployment pipeline changes, delegate to `hugo-deploy` instead.

## Example Prompts

- "Enable the vitals feature flag in the production environment."
- "Update the apiBaseUrl config param in the blue environment."
- "Set up the Azure infrastructure for a new SWA staging slot."
- "Add a new managed identity for the skills API."
