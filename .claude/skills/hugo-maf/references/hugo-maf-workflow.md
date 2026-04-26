# hugo-maf-workflow — Agent Workflow Authoring

## When to Use

- Adding a new agent (Researcher, Publisher, etc.) to `src/content-creator-team/main.py`
- Changing workflow topology (linear → branching, sequential → concurrent)
- Adding HITL (human-in-the-loop) gates after Reviewer
- Configuring retry/revision logic (APPROVED / REVISE / REJECT)
- Wiring `SkillsProvider` or `FileAgentSkillsProvider` for per-agent skills

## Prerequisites

- Python 3.14+ with `agent-framework` and `agent-framework-foundry` installed
- `.env` configured with `PROJECT_ENDPOINT`, `MODEL_DEPLOYMENT_NAME`
- Running Foundry project (`agentic-hugo`)

## Key Files

| File | Purpose |
| --- | --- |
| `src/content-creator-team/main.py` | Agent definitions, workflow builder, operation router |
| `src/content-creator-team/skills/` | Per-agent skill directories (writer/, reviewer/, etc.) |
| `src/content-creator-team/agent.yaml` | Agent schema metadata for VS Code Foundry extension |
| `docs/spec/hugo-content-creators/agents-and-workflow.spec.md` | Full agent prompts and workflow patterns |

## Workflow Patterns

### Sequential Chain

```python
workflow = (
    WorkflowBuilder(
        name="OptimizeWorkflow",
        start_executor=writer,
        output_executors=[writer, reviewer],
    )
    .add_edge(writer, reviewer)
    .build()
)
```

### With Revision Loop

The Reviewer returns JSON with `verdict: "APPROVED" | "REVISE" | "REJECT"`. The router agent dispatches accordingly:

- `REVISE` → retry Writer (max 2 rounds)
- `REJECT` → halt, notify human
- `APPROVED` → continue to next stage

### Branching (Phase 3: Post-Review Parallel)

After Reviewer approves, Publisher and Translator run concurrently:

```python
# Pseudo-pattern — actual API may vary with MAF 1.0 GA
workflow = (
    WorkflowBuilder(name="ArticleWorkflow", ...)
    .add_edge(researcher, writer)
    .add_edge(writer, reviewer)
    .add_edge(reviewer, publisher)   # parallel group
    .add_edge(reviewer, translator)  # parallel group
    .build()
)
```

### HITL Gate

```python
# Pause after Reviewer for human approval
workflow.with_request_info(agents=["reviewer"])
```

### Adding a New Agent

1. Define the agent with `Agent(client, name=..., instructions=..., tools=..., context_providers=...)`
2. Add its skill directory under `skills/<agent-name>/`
3. Wire it into the `WorkflowBuilder` with `.add_edge()`
4. Update the operation router if it's part of a new operation
5. Update `docs/spec/hugo-content-creators/agents-and-workflow.spec.md`

## Agent Prompt Conventions

- Module-level string constants for readability
- Domain expertise section listing integrations.at's 4 pillars
- Voice section (authoritative practitioner, no AI hype)
- Structured output format (JSON for Reviewer, markdown for Writer)
- Phase-specific variants (Phase 1 vs Phase 3 prompts)

## Spec Reference

Full agent prompts and orchestration patterns: [agents-and-workflow.spec.md](../../../docs/spec/hugo-content-creators/agents-and-workflow.spec.md)
