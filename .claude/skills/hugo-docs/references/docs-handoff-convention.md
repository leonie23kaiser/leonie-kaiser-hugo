# Docs Agent Handoff Convention

Any agent or skill that creates or edits files under `docs/`, `docs/spec/`, or `docs/features/` **must** produce a handoff block at the end of its output.

## When to Trigger

A docs handoff is required when any of these files are touched:

- `docs/*.md` (any doc file)
- `docs/spec/**/*.md` (spec files)
- `docs/features/*.md` (feature docs)
- `docs/content-skill-routing.md` (skill routing)
- `docs/tooling-agent-team.md` (agent team map)
- `.github/agents/*.agent.md` (agent definitions — docs agent verifies consistency)
- `.github/skills/**/SKILL.md` (new skills — docs agent updates routing docs)

## Handoff Block Format

At the end of the response that touched docs files, output:

```
## Docs Agent Handoff

**Files changed:**
- docs/tooling-agent-team.md — [what changed]
- docs/content-skill-routing.md — [what changed]

**Why:** [one-line reason]

**Action:** @hugo-documentation verify changes and update cross-references.
```

## Who Produces the Handoff

| Agent/Skill | Produces handoff when |
| --- | --- |
| Hugo Planner | Plan output includes doc file changes |
| hugo-maf (any leaf) | Spec or agent-team doc updated |
| hugo-plan (any leaf) | Feature spec created or promoted |
| hugo-create (any leaf) | New content type needs doc entry |
| hugo-design (any leaf) | Design system doc updated |
| Any agent editing `docs/` directly | Always |

## Who Receives the Handoff

The `hugo-documentation` agent owns all writes to `docs/`. In practice:

- **In Claude Code**: The docs agent can be spawned directly via agent delegation
- **In VS Code Copilot**: Output the handoff block so the user can switch to the docs agent, or invoke `hugo-docs` / `hugo-learn` skill to trigger the update

## What the Docs Agent Does on Receiving a Handoff

1. Reads each changed file to verify structure and tone
2. Checks cross-references (do other docs link to this correctly?)
3. Updates `docs/README.md` if a new doc was added
4. Updates agent files if they reference the changed doc
5. Confirms completion or flags issues

## Receiving Agent: Read-First Protocol

Every agent that receives a handoff (from Hugo Expert or any other delegator) **must** follow this protocol:

1. **Read every file** listed under "Read first" in the Handoff Context Block — before calling `grep_search`, `semantic_search`, `file_search`, or any other search tool
2. **If a listed file does not exist**, inform the user: "Doc `{path}` is missing — should I create it or proceed without it?"
3. **If a listed doc/spec appears outdated** (contradicts the codebase), flag it to the user before proceeding
4. **Priority chain**: docs → specs → inform the user. Never guess when docs or specs are available
5. **After completing work**, verify that every "Read first" doc is still accurate — if your changes invalidated a doc, produce a docs handoff block to trigger an update
