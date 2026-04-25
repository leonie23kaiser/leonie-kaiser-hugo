# hugo-looped-discussion

Guided planning mode for iterative Hugo work where the user wants the conversation to proceed in explicit loops instead of broad autonomous planning.

## Triggers
"work in a loop", "looped discussion", "step by step", "represent this", "show the current state", "one step at a time", "iterate with me"

## When to Use
- The user wants planning or restructuring to happen in short discussion loops
- Each turn should represent the current state before moving to the next decision
- Only one planning decision, rule change, or small patch set should happen per loop
- The user wants strong control over sequencing instead of a full end-to-end plan in one pass

## When NOT to Use
- The user wants a full up-front feature plan across multiple files in one pass -> use `hugo-plan-feature`
- The user wants durable operating rules for a longer restructuring session -> also apply `hugo-stepwise-execution`
- The user is ready for implementation instead of planning -> route to the appropriate implementation skill

## Loop Contract

Each loop should follow this pattern:

1. Restate the exact request for the current loop.
2. Represent the current state in a compact format.
3. Make or apply one bounded planning change.
4. Report exactly what changed.
5. Stop and wait for the next loop instruction.

## Operating Rules

- Do not batch multiple planning decisions into one loop unless the user explicitly asks for it.
- Prefer compact representations over long prose.
- Preserve user formatting preferences when representing state.
- If files are changed, keep the patch burst small and visible.
- If new drift is discovered, report it as the next loop instead of silently expanding scope.

## Output Shapes

Use whichever compact representation best matches the current loop:

| Shape | Use when |
| --- | --- |
| Short numbered list | The user wants a quick state or next-step summary |
| Compact markdown table | The user wants a stable comparison or memory/state view |
| Single decision note | The loop is only recording one accepted rule or constraint |

## Example Prompts

- "Use the hugo-plan looped discussion flow for this skill refactor."
- "Work in a loop and represent the current routing state before each patch."
- "Let's do this one planning step at a time and stop after each change."