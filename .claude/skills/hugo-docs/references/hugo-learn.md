# hugo-learn

Distribute context updates across agent files, skills, and existing docs after a feature or convention change.

## Execution Discipline

1. Work in visible batches of about 3 to 5 file modifications, then stop so the updated files can be seen on disk before the next batch.
2. Do not bundle unrelated cleanup into the current docs-sync pass just because it was discovered during review.
3. If broader drift is found, record it as the next batch instead of silently expanding the current one.
4. If a patch starts failing or a file looks corrupted, reduce scope immediately and fix the broken file first.
5. Prefer several small documentation sync passes over one large catch-all patch.
6. After each batch, report which files landed on disk before proposing the next documentation sync step.

## Triggers
"update docs", "update context", "write documentation", "keep docs current", "sync agents", "doc distribution"

## When to Use
- A new feature, pattern, or agent was added and all relevant docs need syncing
- Keeping skill descriptions, agent prompts, and `docs/` files in sync
- After `hugo-release-feature` runs, cascade the new doc reference everywhere

## ⚠️ Delegation Rule
**All documentation writes go through `hugo-documentation` agent via `hugo-docs`.** Other agents report what changed; the docs agent writes the files.

## Documentation Map

| Doc | When to Update | Triggered by |
|-----|----------------|--------------|
| `docs/basics-getting-started.md` | Dev environment changes, new prerequisites | Hugo Expert |
| `docs/basics-project-structure.md` | New/deleted directories, renamed paths | Hugo Expert |
| `docs/basics-common-tasks.md` | New content types, workflow patterns | hugo-coder |
| `docs/content-layout-patterns.md` | New layout types, front matter schema | hugo-coder |
| `docs/content-template-boilerplate.md` | New template/partial conventions | hugo-coder |
| `docs/basics-hugo-configuration.md` | Hugo config changes, new params | hugo-coder |
| `docs/advanced-angular-elements.md` | Angular Element integration pattern changes | hugo-coder |
| `docs/features-action-behaviors.md` | New notification types or data-attribute APIs | hugo-coder |
| `docs/design-design-system.md` | New CSS variables, color tokens, spacing | hugo-designer |
| `docs/design-image-generator-config.md` | New FLUX prompt templates, image types | hugo-designer |
| `docs/tooling-mcp-servers.md` | New MCP server, new tools, updated capabilities | hugo-playwright |
| `docs/basics-troubleshooting-faq.md` | New known issues / fixes | hugo-playwright |
| `docs/content-hugo-skills.md` | New skill added, skill renamed/deprecated | Hugo Expert |
| `docs/features/*.md` | Created during planning; promoted after integration | hugo-documentation |

## Labs

Labs in `labs/` are step-by-step exercises. Use the `hugo-create-lab` skill to convert a completed task into a lab.

## How to Delegate to Docs Agent

Tell the `hugo-documentation` agent:
- Which doc to update (e.g. `docs/design-design-system.md`)
- What changed in code (e.g. "Added `--color-brand-subtle` CSS variable")
- Where the change lives (e.g. `src/integrations.at/assets/css/base.css`)
- Which agent made the change

When the update spans several docs, send the docs agent only the first small batch and list the remaining files as follow-up work rather than folding them into the same patch.
