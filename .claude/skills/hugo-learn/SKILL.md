---
name: hugo-learn
description: >-
  Master skill for learning from sessions and distributing documentation updates
  in the integrations.at project. Delegates to the correct leaf skill.
  Use when analyzing a conversation session for learnings, distributing doc updates
  after a feature change, or syncing agent context.
  Triggers on: "reflect", "review session", "what did we do", "session summary",
  "learnings", "improve skills", "update docs", "update context", "sync context",
  "doc distribution", "analyze conversation", "learning loop".
license: Complete terms in LICENSE.txt
---

# hugo-learn — Learning & Doc Distribution Router

Routes session analysis and documentation distribution requests to the appropriate leaf skill. Do not implement directly — delegate immediately.

## When to Use This Skill

- After a work session, to capture what happened and extract learnings
- After implementing a feature, to distribute doc updates to all affected agents
- When you want to analyze `.conversation/data/` for patterns and improvements
- When a new skill or agent was added and existing docs need to know about it
- When the user says "reflect", "what did we learn", "sync context", or "update docs"

**Trigger keywords:** `reflect`, `review session`, `learnings`, `analyze conversation`, `learning loop`, `update docs`, `sync context`, `doc distribution`, `what did we do`, `improve skills`

## Delegate Map

| Request type | Leaf skill to invoke |
| --- | --- |
| Analyze a conversation session for patterns, mistakes, and learnings | [`hugo-learn-analyze`](references/hugo-learn-analyze.md) |
| Distribute doc updates after a feature or convention change | [`hugo-learn-distribute`](references/hugo-learn-distribute.md) |

> After analysis produces findings, the distribute leaf handles the actual doc and agent file updates — always via the `hugo-documentation` agent (see docs handoff convention).

## Relationship to Other Skills

| Skill | Relationship |
| --- | --- |
| `hugo-docs` | hugo-learn triggers doc writes; hugo-docs routes them to the docs agent |
| `hugo-plan` | Plans produce doc changes; hugo-learn captures session learnings from planning sessions |
| `hugo-maf` | Backend work produces spec changes; hugo-learn analyzes sessions for handoff gaps |

## Supersedes

This skill replaces:

| Old skill | Location | Merged into |
| --- | --- | --- |
| `hugo-learn` | `.claude/skills/hugo-learn/` | `hugo-learn-distribute` (doc map + agent context map) |
| `hugo-reflect` | `.claude/skills/hugo-reflect/` | `hugo-learn-analyze` (session analysis workflow) |
| `agent-learning-loop` | `.github/skills/agent-learning-loop/` | `hugo-learn-analyze` (Copilot session review) |

The `.claude/` versions remain for backward compatibility but this `.github/skills/` version is the canonical one.

## Example Prompts

- "Analyze this conversation session for learnings and skill gaps."
- "Review the last 3 sessions in .conversation/data/ for patterns."
- "Distribute doc updates after the content-creator Phase 3 spec changes."
- "Sync agent context after we added the hugo-maf skill tree."
