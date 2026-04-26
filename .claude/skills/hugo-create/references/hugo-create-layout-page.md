# hugo-create-layout-page

Scaffold a reusable Hugo multi-step layout partial and example front matter for a new content pattern.

## When to Use

- Creating a new reusable steps-based layout pattern.
- Generating a partial for workflows, pricing tiers, roadmaps, or similar card-based sequences.
- Creating starter front matter for a new multi-step page pattern.

## Inputs

1. `layoutName` such as `roadmap`, `pricing`, or `engagement`.
2. `featureName` such as `roadmap`, `pricing`, or another front matter key root.
3. Optional step count.
4. Optional color overrides.

## Output

- A Hugo partial under the current repo layout partials tree.
- An example markdown file in `docs/` with starter front matter.
- Next-step guidance for integrating the new partial into the correct page layout.

## Script

Use the co-located script:

`scripts/hugo-create-layout-page.js`

## Docs-First Rule

- Check the repository's `docs/` for current Hugo layout patterns before generating a new layout.
- Use current repo layout names and partial locations rather than older examples.
- Keep generated file names lowercase.