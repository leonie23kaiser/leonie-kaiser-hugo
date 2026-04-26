# hugo-plan-feature

Full feature-planning workflow for new Hugo CMS capabilities spanning multiple files.

## Triggers
"plan this", "how should we approach", "let's design", "add X to all cards", "unify X with Y", "add a new feature", "planner", "design this"

## When to Use
- Request touches 3+ files across templates, CSS, JS, content
- Cross-cutting UI pattern needs scoping before any code is written
- Requires user sign-off on a plan before implementation begins
- Output is a multi-file spec folder in `docs/spec/<name>/` with `readme.md` as the root document

## Output Mode

Always write feature plans as a spec folder under `docs/spec/<name>/`. Start with a single `readme.md` file. Keep it lean and only include sections the task actually needs. When the readme reaches ~60+ lines, split out specialized sections into focused `*.spec.md` files (like `hooks.spec.md`, `templates.spec.md`) and add a short table of contents at the top of readme.md linking to them.

## The 6-Step Workflow

### 1. Receive task + attachments
Read screenshots, mockups, or references. Note: component types shown, desired interaction, existing feature to unify with. Do NOT start gathering context yet.

### 2. Short Review & Structuring (Hugo Expert — do not delegate)
- Run `search_subagent` to find: affected files, existing patterns being extended, relevant docs
- Record only unresolved questions that were explicitly raised in the discussion, and set sensible defaults only for those
- Pick a kebab-case feature name (convention: `card-actions`, `topic-session`, `agent-learning-loop`)
- Delegate immediately to `hugo-planner` with a fully structured prompt

### 3. Planner Plans; Docs Agent Writes Spec
- `hugo-planner` researches and produces doc content
- `hugo-documentation` creates the spec folder and writes `readme.md`

Start with `readme.md` containing only the core sections needed to explain the change. As the spec grows beyond ~60 lines, split out detailed sections into `*.spec.md` files and add a TOC at the top of readme.md.

**Default readme.md sections:**
- Status + Goal
- Current State
- Proposed Solution
- Files in Scope
- Implementation Phases

Add sections like `Out of Scope`, `Open Questions`, or a summary table only when the user explicitly asks for them. `Open Questions` should only list questions that already came up in the discussion and are still unanswered.

**When to split (after ~60 lines):**

| File | Focus |
| --- | --- |
| `hooks.spec.md` | Detailed hook configuration, scripts, examples |
| `templates.spec.md` | Template markup contracts, before/after examples |
| `styles.spec.md` | CSS variables, selectors, responsive behavior |
| `content.spec.md` | Content authoring impact, front matter schema |

Do not create files proactively. Only split when readme.md becomes unwieldy.

### ⛔ HARD GATE
Do NOT proceed to step 4 until `docs/spec/{name}/` exists on disk with at least `readme.md` complete.

### 4. User Sign-Off
Present the spec folder. Ask for explicit approval before any implementation.

### 5. Implementation
Delegate to the appropriate agents based on the implementation phases and files in scope in the spec.

### 6. Post-Implementation Docs
Update `docs/spec/{name}/readme.md` status to `Implemented`. If fully complete, move content to `docs/` main index. Call `hugo-learn` with a summary of what changed.

## Naming Rules

| Item | Rule |
| --- | --- |
| Feature name | Always kebab-case |
| Spec-folder path | `docs/spec/<name>/` |
| Root document | `readme.md` (always, start here) |
| When to split | After readme.md exceeds ~60 lines |
| Split-documents | `*.spec.md` suffix (e.g., `hooks.spec.md`) |

Examples:

- Early stage: `docs/spec/card-actions/readme.md` (single file)
- Mature spec: `docs/spec/agent-learning-loop/readme.md` + `docs/spec/agent-learning-loop/hooks.spec.md`
