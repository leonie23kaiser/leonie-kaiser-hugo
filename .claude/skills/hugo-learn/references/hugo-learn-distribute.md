# hugo-learn-distribute — Documentation & Context Distribution

## When to Use

- A feature was implemented and docs need updating
- A new skill or agent was added and existing docs/agents need to reference it
- A convention changed and multiple files need to reflect it
- After `hugo-learn-analyze` identifies missing doc updates

## Prerequisites

- Know which files changed (from the implementation or from analysis output)
- Know which docs and agents are affected (use the doc map below)

## Step-by-Step Workflow

### 1. Identify Changed Files

List all files that were created or modified during the implementation.

### 2. Map to Affected Docs

Use this mapping to determine which docs need updating:

| Changed file area | Docs to update |
| --- | --- |
| `src/content-creator-team/` | `docs/tooling-agent-team.md`, `docs/spec/hugo-content-creators/` |
| `src/api.integrations.at/` | `docs/tooling-agent-team.md`, `docs/spec/hugo-content-creators/api-integration.spec.md` |
| `.github/skills/` | `docs/content-skill-routing.md`, `docs/content-hugo-skills.md` |
| `.github/agents/` | `docs/tooling-agent-team.md` |
| `src/website/layouts/` | `docs/content-layout-patterns.md`, `docs/content-layout-catalog.md` |
| `src/website/static/css/` | `docs/design-design-system.md` |
| `docs/spec/` | `docs/README.md` (if new spec folder) |

### 3. Map to Affected Agents

| Changed doc | Agents that reference it |
| --- | --- |
| `docs/tooling-agent-team.md` | All agents (general reference) |
| `docs/content-skill-routing.md` | `hugo-expert` |
| `docs/design-design-system.md` | `hugo-designer` |
| `docs/content-layout-patterns.md` | `hugo-coder` |
| `docs/spec/hugo-content-creators/` | `maf.agent.md`, `dotnet.agent.md` |

### 4. Produce Docs Handoff

For each affected doc, produce a handoff block following the [docs handoff convention](../../hugo-docs/references/docs-handoff-convention.md):

```
## Docs Agent Handoff

**Files changed:**
- {file} — {what changed}

**Affected docs:**
- {doc} — needs {update description}

**Affected agents:**
- {agent} — needs {reference update}

**Action:** @hugo-documentation verify and apply updates.
```

### 5. Delegate to Docs Agent

All actual doc writes go through the `hugo-documentation` agent:

- **In Claude Code**: Delegate directly to the docs agent
- **In VS Code Copilot**: Output the handoff block for the user to action, or invoke `hugo-docs` skill

## Agent Context Map

Each agent has docs it reads and skills it invokes. When changes affect these, the agent file may need updating:

| Agent | Key docs it reads | Skills it invokes |
| --- | --- | --- |
| hugo-coder | layout-patterns, template-boilerplate, angular-elements | hugo-create-*, hugo-attach-*, hugo-learn |
| hugo-designer | design-system, image-generation-config | hugo-change-colors, hugo-add-images, hugo-learn |
| hugo-playwright | mcp-servers, troubleshooting | hugo-debug-ui, hugo-mcp-reference, hugo-learn |
| hugo-planner | All docs/ (reads broadly) | None (research-only) |
| Hugo Expert | project-structure, getting-started | hugo-expert, hugo-plan-feature, hugo-learn |
| MAF Agent | spec/hugo-content-creators/ | microsoft-foundry, microsoft-foundry-agent-framework-code-gen |
| .NET Expert | spec/hugo-content-creators/api-integration | net-cli, net-conventions |
