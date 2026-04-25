---
name: hugo-debug
description: >-
  Master skill for debugging Hugo CMS layout issues, visual regressions, CSS problems, and agent simulations.
  Delegates to the correct narrow leaf skill.
  Use when something looks wrong in the browser, a layout is broken, CSS is not applying, a component
  behaves unexpectedly, or you want to simulate what agents would do. Triggers on: "debug", "fix layout",
  "broken", "CSS not applying", "looks wrong", "simulate", "dry run", "reflect", "regression".
license: Complete terms in LICENSE.txt
---

# hugo-debug — Debugging & Simulation Router

Routes debugging and simulation requests to the appropriate narrow leaf skill. Do not implement directly — delegate immediately.

## When to Use This Skill

- A layout, banner, or component looks wrong in the browser
- CSS is not applying or is being overridden unexpectedly
- An interactive element (accordion, menu, card) is not behaving correctly
- You want to simulate what an agent team would do without making real changes
- You want to reflect on a recent session to capture learnings

**Trigger keywords:** `debug`, `fix`, `broken`, `not working`, `layout issue`, `CSS override`, `simulate`, `dry run`, `reflect`, `regression`, `looks wrong`, `inspect`

## Delegate Map

| Request type                             | Leaf skill to invoke                           |
| ---------------------------------------- | ---------------------------------------------- |
| UI bug — CSS, layout, DOM state          | [`hugo-debug-ui`](references/hugo-debug-ui.md) |
| Simulate agent team without file changes | [`hugo-dry-run`](references/hugo-dry-run.md)   |
| Reflect on recent session for learnings  | [`hugo-reflect`](references/hugo-reflect.md)   |

> `hugo-expert` is the top-level router. For build errors (not visual bugs), inspect `hugo server` output directly.

## Example Prompts

- "The banner image is cropped wrong on mobile — debug and fix."
- "The accordion on the class detail page is not opening — investigate."
- "Dry run: what would the team do if I asked you to add a skills widget?"
- "Reflect on today's session and capture any new patterns."
