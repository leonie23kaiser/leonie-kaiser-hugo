---
name: hugo-docs
description: >-
  Master skill for writing, updating, and promoting documentation in the integrations.at Hugo CMS project.
  Delegates to the correct narrow leaf skill.
  Use when writing new docs, updating existing docs after a code change, creating hands-on labs, or syncing
  agent context. Triggers on: "update docs", "write docs", "create lab", "sync context", "document this",
  "update readme", "keep docs current".
license: Complete terms in LICENSE.txt
---

# hugo-docs — Documentation Router

Routes documentation write, update, and promotion requests to the appropriate narrow leaf skill. Do not implement directly — delegate immediately.

## When to Use This Skill

- Writing new documentation after implementing a feature
- Updating `docs/` files to reflect changes made in code or templates
- Creating a hands-on prompt lab from a completed implementation
- Distributing context updates across agent files and existing docs
- Promoting a finished spec from `docs/spec/` to permanent `docs/`

**Trigger keywords:** `update docs`, `write docs`, `document`, `create lab`, `update context`, `sync agents`, `keep docs current`, `release feature doc`, `update readme`

## Delegate Map

| Request type                                      | Leaf skill to invoke                                         |
| ------------------------------------------------- | ------------------------------------------------------------ |
| Distribute context updates to all agents and docs | [`hugo-learn`](../hugo-learn/SKILL.md) (routes to `hugo-learn-distribute`) |
| Analyze a session for doc gaps and skill improvements | [`hugo-learn`](../hugo-learn/SKILL.md) (routes to `hugo-learn-analyze`) |
| Write or update documentation files               | [`hugo-create-docs`](references/hugo-create-docs.md)         |
| Create a hands-on prompt lab from a task          | [`hugo-create-lab`](references/hugo-create-lab.md)           |

> `hugo-expert` is the top-level router. The `hugo-documentation` agent **owns all writes to `docs/*`** — never edit docs directly from another agent.

## Docs Handoff Convention

Any agent or skill that edits `docs/`, `docs/spec/`, agent files, or skill routing docs **must** produce a handoff block. See [`docs-handoff-convention`](references/docs-handoff-convention.md) for the format and triggers.

## Example Prompts

- "Update the design-system doc after the color palette change."
- "Write a lab for the new Angular Elements integration."
- "Sync agent context after we added the content-targeting feature."
