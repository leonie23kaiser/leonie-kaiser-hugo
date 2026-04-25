# hugo-maf-eval — Agent Evaluation & Prompt Optimization

## When to Use

- Setting up evaluation datasets from agent traces
- Running batch evaluations on any agent in the pipeline
- Comparing evaluation runs to measure prompt improvements
- Optimizing agent prompts (Writer, Reviewer, Researcher, etc.)
- Tracking quality metrics over time

## Prerequisites

- Foundry project access (`agentic-hugo`)
- Existing agent deployed (at least locally via `python main.py`)
- `microsoft-foundry` skill loaded for Foundry eval tooling

## Key Concepts

### Evaluation Flow

```
Agent traces → Dataset curation → Eval run → Results → Prompt iteration
```

1. **Collect traces**: Run the agent on sample inputs, capture input/output pairs
2. **Curate dataset**: Select representative examples, add expected outputs
3. **Run eval**: Batch-evaluate the agent against the dataset
4. **Compare**: Diff results against previous runs
5. **Optimize**: Iterate on prompts based on eval findings

### What to Evaluate Per Agent

| Agent | Key metrics | Eval criteria |
| --- | --- | --- |
| Writer | Voice adherence, structure, SEO quality | No hype words, correct heading structure, practitioner tone |
| Reviewer | Verdict accuracy, feedback specificity | Catches real issues, doesn't false-positive on good text |
| Translator | Terminology accuracy, register consistency | DACH terms correct, formal-Sie maintained, product names untranslated |
| Researcher (Phase 3) | Source relevance, brief completeness | All claims sourced, no hallucinated URLs, duplication check works |
| Publisher (Phase 3) | Format compliance, manifest validity | Hugo frontmatter correct, social posts within char limits |

## Foundry Eval Tooling

Use the `microsoft-foundry` skill for:

- Creating eval datasets from traces: curate input/output pairs from agent runs
- Running batch eval: evaluate agent against dataset with scoring rubric
- Comparing runs: diff two eval runs to measure improvement
- Prompt optimization: automated prompt iteration based on eval results

### Dataset Structure

```json
{
  "samples": [
    {
      "input": "Optimize this text: ...",
      "expected_output": "The optimized version...",
      "metadata": { "page": "ai-transformation", "phase": 1 }
    }
  ]
}
```

### Eval Storage

```
src/content-creator-team/
  .foundry/
    datasets/       # Local eval dataset cache
    evaluators/     # Local evaluator cache
    results/        # Eval results per run
```

## Prompt Optimization Workflow

1. Run current prompt against eval dataset → baseline score
2. Identify weak areas from eval results (e.g. "Writer uses hype words in 3/10 samples")
3. Iterate on the prompt (add constraints, examples, or negative examples)
4. Re-run eval → compare against baseline
5. If improved, update the prompt constant in `main.py`
6. If degraded, revert and try a different approach

## Quality Gates

Before deploying a prompt change:

- Eval score must not regress on any metric
- At least 10 diverse samples in the eval dataset
- Writer + Reviewer prompts evaluated together (they interact)

## Spec Reference

Agent prompts and quality criteria: [agents-and-workflow.spec.md](../../../docs/spec/hugo-content-creators/agents-and-workflow.spec.md)
