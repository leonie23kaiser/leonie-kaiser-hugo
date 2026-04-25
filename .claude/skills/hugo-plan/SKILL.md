---
name: hugo-plan
description: >-
  Master skill for planning, scoping, and releasing Hugo CMS features and plugins on the integrations.at site.
  Delegates to the correct narrow leaf skill.
  Use when scoping a new feature, planning a plugin, structuring a multi-file change, or promoting a
  completed feature spec to permanent docs.
  Triggers on: "plan", "scope", "how should we approach",
  "design this", "feature spec", "plugin catalog", "release feature", "promote spec", "stepwise",
  "restructure skills", "refactor skills", "looped discussion", "work in a loop", "represent this".
license: Complete terms in LICENSE.txt
---

# hugo-plan — Feature Planning & Release Router

Routes planning, scoping, and release requests to the appropriate narrow leaf skill. Do not implement directly — delegate immediately.

## When to Use This Skill

- A request touches 3 or more files across different concerns
- You need to design a new cross-cutting UI pattern before coding
- You want to scope or catalog a new plugin from an existing customer project
- A completed spec in `docs/spec/` needs to be promoted to permanent `docs/` documentation
- The user wants planning to happen in explicit discussion loops with visible state between steps

**Trigger keywords:** `plan`, `scope`, `how should we`, `design this`, `approach`, `feature spec`, `plugin`, `catalog`, `release`, `promote spec`, `new feature`, `looped discussion`, `work in a loop`, `represent this`

## Delegate Map

| Request type                                             | Leaf skill to invoke                                               |
| -------------------------------------------------------- | ------------------------------------------------------------------ |
| Full feature planning workflow (3+ files, cross-cutting) | [`hugo-plan-feature`](references/hugo-plan-feature.md)             |
| Scope / catalog a plugin from a customer project         | [`hugo-plan-plugin`](references/hugo-plan-plugin.md)               |
| Release a completed spec folder to permanent docs        | [`hugo-release-feature`](references/hugo-release-feature.md)       |

> **Default behavior**: The Hugo Planner agent enforces [`hugo-looped-discussion`](references/hugo-looped-discussion.md) and [`hugo-stepwise-execution`](references/hugo-stepwise-execution.md) rules by default on every planning session. These are not opt-in — they define how the planner works unless the user explicitly asks for a quick one-pass overview.

> `hugo-expert` is the top-level router. Once a plan is signed off by the user, route implementation to `hugo-coder` or `hugo-designer`.

## Docs Handoff

When a plan creates or updates files under `docs/` or `docs/spec/`, produce a docs agent handoff block. See `hugo-docs` → [`docs-handoff-convention`](./../hugo-docs/references/docs-handoff-convention.md).

## Example Prompts

- "Plan a content-targeting feature for sidebar cards."
- "Scope a plugin from our customer's shortcode library."
- "How should we approach adding topic tags to all class cards?"
- "Release the action-command spec to permanent documentation."
- "Use the stepwise execution rules for this skill refactor."
- "Work in a loop and represent each planning step before the next patch."
