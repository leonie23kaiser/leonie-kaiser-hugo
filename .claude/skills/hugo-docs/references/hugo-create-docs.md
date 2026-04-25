# hugo-create-docs

Write and maintain documentation files in the `docs/` folder.

## When to Use
- Writing a new doc after implementing a feature or convention change
- Updating an existing `docs/` file to reflect changes made in code or templates
- Running a full docs-alignment pass across the whole `docs/` set
- The Hugo Documentation agent owns all `docs/*` writes — never edit from another agent

## Workflow Proven In This Repo

The current repo pass validated these rules:

1. Use `docs/readme.md` as the execution order.
2. Work one TOC item at a time.
3. Read only the minimum code, content, workflow, or infra files needed to verify the active doc.
4. If a doc is too long, split it into focused child docs instead of only compressing the text.
5. Update `docs/readme.md` immediately after every create, rename, split, or removal.
6. Prefer current repo reality over historical explanations or speculative future wording.

## Strict Ordered Cleanup Workflow

Use this sequence when the request is a full docs audit, cleanup, or alignment pass.

1. Read `docs/readme.md` first and treat it as the only execution order.
2. Read the current TOC item.
3. Read only the validating repo files needed for that active doc.
4. Fix that doc before touching the next TOC item.
5. If the structure changes, update `docs/readme.md` immediately.
6. Only run a global consistency sweep after the full TOC pass is complete.

## Compactness Rule

- Keep docs within the repo line-budget target.
- If a doc grows too large, split it into focused child docs and keep the parent as a short hub when useful.
- Do not leave legacy sections appended below a rewrite.

## Recovery Rule

If a docs pass goes off track, restart the current TOC item from the old source content rather than continuing from an already-shortened rewrite. In practice this means reloading the pre-edit document from git, then redoing the split or alignment correctly before moving to the next TOC item.

## Practical Notes

- Parent docs can stay as short hub pages when detail is moved into children.
- Exception handling belongs to the active item only. If the user explicitly allows a larger doc for one item, keep that exception local instead of changing the global rule.
- Do not batch unrelated docs together just because they share a topic area.

## Anti-Patterns

- Do not read the whole repo before starting the first TOC item.
- Do not rewrite multiple unrelated docs in one speculative batch.
- Do not postpone `docs/readme.md` updates until the end.
- Do not mix live documentation with speculative future-state text unless the file is explicitly a spec.

## Completion Check

- `docs/readme.md` matches the live docs set.
- Touched docs reflect current code and workflows.
- Oversized docs were split instead of only shortened.
- Rewritten docs contain no leftover legacy appendices.

## Reference Skills

- For the older Hugo docs workflow: [Full skill instructions](../../../../.claude/skills/hugo-create-docs/SKILL.md)
