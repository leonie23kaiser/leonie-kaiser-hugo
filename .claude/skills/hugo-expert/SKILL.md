---
name: hugo-expert
description: Top-level router for Hugo work in this repository. Use when the request is ambiguous, spans multiple Hugo concerns, or you need help choosing between create, design, debug, plan, docs, config, deploy, and SEO workflows. Triggers on Hugo architecture questions, multi-step site work, and "which Hugo skill should I use" requests.
user-invocable: true
---

# Hugo Expert

Top-level router for Hugo work in this repository.

## When to Use This Skill

- The request is Hugo-related but the correct master skill is not obvious yet.
- The task spans multiple Hugo concerns such as content, design, docs, deployment, or SEO.
- You need a single entry point for Hugo architecture questions or multi-step site work.

## Routing Rule

- Use `hugo-expert` when the request is ambiguous or cross-cutting.
- Route to the most specific master skill as soon as the intent is clear.
- Use the repository's `docs/` for project-specific structure, workflows, and conventions instead of embedding long handbook content here.

## Master Skill Map

| Master skill | Use when |
| --- | --- |
| `hugo-create` | Building new pages, sections, layouts, or content types |
| `hugo-design` | Making visual changes such as colors, spacing, images, or banners |
| `hugo-debug` | Investigating layout bugs, regressions, or UI behavior problems |
| `hugo-plan` | Scoping features, planning multi-file work, or stepwise restructuring |
| `hugo-docs` | Writing, updating, promoting, or syncing documentation |
| `hugo-config` | Managing feature flags, config values, or infrastructure-related config |
| `hugo-deploy` | Handling CI/CD, Azure Static Web Apps deployment, domains, or vitals |
| `hugo-seo` | Auditing or improving SEO, metadata, structured data, or vitals |
| `hugo-maf` | Working on the content-creator backend: agent workflows, tools, .NET↔Python bridge, deploy, eval |
| `hugo-learn` | Analyzing sessions for learnings, distributing doc updates, syncing agent context |

## Docs Handoff

When any master skill or agent edits files under `docs/`, it **must** produce a docs agent handoff block at the end of its output. See `hugo-docs` → [`docs-handoff-convention`](../hugo-docs/references/docs-handoff-convention.md).

## Full Delegation Reference

For the complete team map, decision tree, handoff conventions, parallel dispatch rules, and anti-patterns, see [`team-delegation-pattern`](references/team-delegation-pattern.md).

**Every delegation must include a Handoff Context Block** with 2–5 doc references. The receiving agent reads these before searching. See the "Handoff Context Block (Mandatory)" section and Doc-Reference Lookup Table in the delegation reference.

## Docs-First Pointers

- Use `docs/content-hugo-skills.md` for the current Hugo skill architecture.
- Use `docs/tooling-agent-team.md` for the current repo-local agent map.
- Use the relevant `docs/` page for project-specific implementation details before applying a master skill.

## Example Prompts

- "Use /hugo-expert to decide which Hugo skill should handle this request."
- "I need help choosing between Hugo docs, design, and deploy work."
- "This Hugo change spans content, CSS, and deployment. Route it correctly."
