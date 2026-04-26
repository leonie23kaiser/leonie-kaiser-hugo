# hugo-create-lab

Create a hands-on prompt lab from a completed implementation task.

## When to Use
- Turning a solved bug fix, refactor, or workflow into a step-by-step lab
- Building guided exercises with prompts, validation steps, and key code snippets
- Capturing the real reasoning path from an implementation so it can be reused
- Requires a completed, working implementation to draw from

## Do Not Use
- The user only wants API, architecture, or code documentation with no exercise format
- The task has not been explored enough to identify the real pain point and solution path
- The output should be a marketing page, article, or general-purpose guide

## Inputs to Gather

Before writing the lab, identify:

1. The original pain point.
2. The concrete workflow that solved it.
3. The prompts or decisions that moved the task forward.
4. The most instructive code blocks that represent the solution.
5. The validation step that proved the change worked.

## Output Guidance

- Follow the repository's `docs/` guidance for where labs live and how they should be indexed.
- Prefer the lab structure and naming conventions documented in `docs/` over hardcoded paths in the skill.
- Keep the lab based on the actual implementation path, not an imagined ideal sequence.

Recommended structure:

1. `# Lab: ...` title
2. `## The Pain Point`
3. Numbered steps with prompt examples
4. A short takeaway after each major step
5. A final validation or end-to-end proof step

## Recommended Workflow

### Step 1: Reconstruct the Task

- Review the files changed during the implementation.
- Identify what was broken, repetitive, fragile, or easy to forget.
- Name the pain in one or two sentences.

### Step 2: Extract the Learning Sequence

- Start from the first useful prompt or decision.
- Capture the discovery sequence that led to the fix.
- Include the point where the main design decision became clear.

### Step 3: Choose the Best Code Blocks

- Prefer the new config or data shape.
- Prefer the core rendering, integration, or transformation logic.
- Prefer the wiring point that activates the feature or workflow.
- Avoid trivial boilerplate.

### Step 4: Add Validation

- Include the exact verification step used.
- State what success looked like.

### Step 5: Reflect into Reuse

- End with a compact loop showing how the workflow generalizes.
- Make the lab useful for future similar changes.

## Quality Check

- Confirm the lab reflects the real implementation path.
- Confirm the prompts are specific and reusable.
- Confirm the code snippets are the most instructive ones.
- Confirm the final location and indexing follow the repository's `docs/` guidance.
- Confirm the lab reads like a workshop guide, not a changelog.