# hugo-stepwise-execution

Persistent execution rules for step-by-step skill restructuring work.

## When to Use
- The user wants work done step by step instead of broad autonomous exploration.
- A skill restructuring or refactor needs explicit operating rules before any action.
- The team wants a persistent place to store and evolve restructuring rules over time.

## Session Operating Rules

1. Work step by step.
2. Prefer small sequential patches over large patch bursts.
3. Limit a patch burst to about 3 to 5 file modifications, then stop so the result is visible on disk before continuing.
4. After each patch burst, report what landed on disk before proposing the next step.
5. Only do what the user explicitly asks for.
6. Before taking any action, restate the understanding of the request and the plan.
7. Keep using that pattern for the full session unless the user changes it.
8. Treat todo updates as a priority-1 progress signal during longer-running work.
9. Update the todo list when a task starts, when a major step completes, and when work direction changes enough that the visible progress would otherwise become misleading.
10. If one file is broken, fix that file first instead of combining it with broader cleanup.
11. Do not do speculative "we will need this later anyway" work in the current step.
12. If additional drift is discovered, report it as the next step instead of silently expanding the current one.

## Restructuring Bucket

1. Check the skill against the current docs before changing structure.
2. Identify whether the skill content is outdated, duplicated, or no longer aligned with the documented model.
3. Update the skill when the docs show drift, not just its folder layout or naming.
4. Replace repo-specific paths, repo-specific file names, and hardwired project assumptions with references to the repository's `docs/` wherever possible.
5. Rewrite examples and guidance so the skill stays reusable across projects, and point users to `docs/` for project-specific details.
6. Keep only the minimum project-specific details that are truly part of the skill's purpose.
7. After each restructure, verify references, delegate maps, and linked sub-items still resolve cleanly.
8. Prefer GitHub Copilot skill-local references and `docs/` references over external dependencies.
9. Clean up orphaned artifacts created by renames, moves, splits, or older skill layouts.
10. Split larger restructures into visible sub-steps so failed patches do not hide or roll together multiple unrelated outcomes.
11. If a patch fails, retry with a smaller scope rather than escalating into a bigger combined patch.

## Duplicate Absorption Pattern

Use this pattern when a standalone skill duplicates a reference owned by a master skill:

1. Compare the standalone skill and the reference for semantic match, not just title match.
2. Check the docs to see whether either version is outdated.
3. Move the richer, still-valid guidance into the surviving reference.
4. Rewrite surviving guidance to be docs-first and reusable across repositories.
5. Verify all links and delegate maps point to the surviving reference.
6. Delete the redundant standalone skill.
7. Remove orphaned artifacts left by the deletion.

## Maintenance Rule

- Update this file whenever new execution rules are agreed during restructuring work.
- Treat this file as the source of truth for future skill restructuring sessions under `hugo-plan`.