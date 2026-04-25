/**
 * Hugo Create Layout Page Skill
 * Generates reusable Hugo layout pages with multi-step card components
 *
 * Usage: /hugo-create-layout-page [layout-name] [feature-name]
 */

const fs = require('fs');
const path = require('path');

module.exports = {
  name: 'hugo-create-layout-page',
  description: 'Generate a new Hugo multi-step layout page component',

  async execute(args, context) {
    const { layoutName, featureName, steps = 6, colors = {} } = args;

    if (!layoutName || !featureName) {
      throw new Error('Required: layoutName and featureName parameters');
    }

    // Default colors
    const defaultColors = {
      background: '#f6f5f2',
      headerBg: '#ffffff',
      cardBg: '#ffffff',
      labelColor: '#60a5fa',
      titleColor: '#ffffff',
      emphasisColor: '#60a5fa',
      textColor: '#6b7280',
      borderColor: '#e5e7eb',
      ...colors,
    };

    // Generate partial file content
    const partialContent = generatePartialFile(
      layoutName,
      featureName,
      defaultColors,
    );

    // Generate frontmatter template
    const frontmatterTemplate = generateFrontmatterTemplate(
      layoutName,
      featureName,
      steps,
    );

    // Create the partial file
    const partialPath = path.join(
      context.projectRoot || process.cwd(),
      `src/integrations.at/layouts/partials/ui-components/layout-${layoutName}-steps.html`,
    );

    // Create frontmatter example
    const examplePath = path.join(
      context.projectRoot || process.cwd(),
      `docs/layout-example-${layoutName.toLowerCase()}.md`,
    );

    try {
      // Ensure directory exists
      const partialDir = path.dirname(partialPath);
      if (!fs.existsSync(partialDir)) {
        fs.mkdirSync(partialDir, { recursive: true });
      }

      // Write partial file
      fs.writeFileSync(partialPath, partialContent);

      // Write example file
      fs.writeFileSync(examplePath, frontmatterTemplate);

      return {
        success: true,
        message: `✅ Layout pages created successfully!`,
        files: {
          partial: partialPath,
          example: examplePath,
        },
        nextSteps: [
          `1. Review docs/ for the current page layout that should include the new partial.`,
          `2. Include the partial from the relevant layout or reusable partial chain.`,
          `3. Copy the frontmatter structure from: ${examplePath}`,
          `4. Add content to the target markdown file under src/integrations.at/content/.`,
        ],
      };
    } catch (error) {
      throw new Error(`Failed to create layout files: ${error.message}`);
    }
  },
};

function generatePartialFile(layoutName, featureName, colors) {
  return `{{ with .Params.${featureName}Steps }}
<section class="${layoutName}-section">
  <div class="${layoutName}-header" {{ with $.Params.banner.image }}style="background-image: url('{{ . }}')"{{ end }}>
    <div class="${layoutName}-header-inner">
      <div class="${layoutName}-label">{{ .label }}</div>
      <h2 class="${layoutName}-title">{{ .title | safeHTML }}</h2>
      <p class="${layoutName}-description">{{ .description }}</p>
    </div>
  </div>

  <div class="${layoutName}-container">
    <div class="${layoutName}-cards">
      {{ range .steps }}
      <div class="${layoutName}-card">
        <div class="card-step-header">
          <span class="card-icon">{{ .icon }}</span>
          <div class="card-step">Step {{ printf "%02d" .step }} · {{ .stepLabel }}</div>
        </div>
        <div class="card-title">{{ .title }}</div>
        <div class="card-challenge">{{ .challenge }}</div>
        <div class="card-description">{{ .description }}</div>
        <div class="card-outcome">{{ .outcome }}</div>
        <div class="card-tags">
          {{ range .tags }}
          <span class="tag">{{ . }}</span>
          {{ end }}
        </div>
      </div>
      {{ end }}
    </div>
  </div>

  <style>
    /* Main Section */
    .${layoutName}-section {
      background: ${colors.background};
    }

    /* Container */
    .${layoutName}-container {
      max-width: 1170px;
      margin: 0 auto;
      padding: 5rem 15px;
      width: 100%;
    }

    /* Header */
    .${layoutName}-header {
      text-align: center;
      max-width: 100%;
      padding: 6rem 2rem 5rem;
      background: ${colors.headerBg};
      border-bottom: 1px solid ${colors.borderColor};
      position: relative;
      overflow: hidden;
      background-size: cover;
      background-position: center;
    }

    .${layoutName}-header::before {
      content: '';
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.5);
      z-index: 0;
    }

    .${layoutName}-header-inner {
      max-width: 820px;
      margin: 0 auto;
      position: relative;
      z-index: 1;
    }

    .${layoutName}-label {
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: ${colors.labelColor};
      margin-bottom: 1rem;
    }

    .${layoutName}-title {
      font-size: clamp(2rem, 4.5vw, 3.2rem);
      font-weight: 900;
      letter-spacing: -1.5px;
      line-height: 1.08;
      margin-bottom: 1.2rem;
      color: ${colors.titleColor};
    }

    .${layoutName}-title em {
      font-style: italic;
      font-family: 'Lora', serif;
      color: ${colors.emphasisColor};
      font-weight: 400;
    }

    .${layoutName}-description {
      font-family: 'Lora', serif;
      font-size: 1rem;
      color: #e5e7eb;
      line-height: 1.75;
      font-style: italic;
    }

    /* Cards Grid */
    .${layoutName}-cards {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.2rem;
    }

    .${layoutName}-card {
      background: ${colors.cardBg};
      border: 1px solid ${colors.borderColor};
      border-radius: 12px;
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      transition: box-shadow 0.2s, transform 0.18s;
    }

    .${layoutName}-card:hover {
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
      transform: translateY(-2px);
    }

    /* Card Content */
    .card-step-header {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      margin-bottom: 1rem;
    }

    .card-step {
      font-size: 0.62rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: ${colors.textColor};
    }

    .card-icon {
      font-size: 1.5rem;
      flex-shrink: 0;
    }

    .card-title {
      font-size: 1rem;
      font-weight: 800;
      letter-spacing: -0.2px;
      line-height: 1.25;
      margin-bottom: 0.65rem;
      min-height: 2.5rem;
    }

    .card-challenge {
      font-size: 0.75rem;
      background: ${colors.background};
      border: 1px solid #d1d5db;
      border-radius: 6px;
      padding: 0.5rem 0.75rem;
      color: #6b7280;
      font-style: italic;
      margin-bottom: 0.75rem;
      line-height: 1.5;
    }

    .card-description {
      font-size: 0.85rem;
      color: #374151;
      line-height: 1.68;
      flex: 1;
    }

    .card-outcome {
      margin-top: 1rem;
      font-size: 0.82rem;
      font-weight: 700;
      color: #111827;
      display: flex;
      align-items: flex-start;
      gap: 0.4rem;
      line-height: 1.4;
    }

    .card-outcome::before {
      content: "→";
      flex-shrink: 0;
      color: #374151;
    }

    .card-tags {
      margin-top: 0.85rem;
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem;
    }

    .tag {
      font-size: 0.62rem;
      font-weight: 600;
      padding: 0.25rem 0.65rem;
      border-radius: 100px;
      background: #f3f4f6;
      border: 1px solid ${colors.borderColor};
      color: #6b7280;
    }

    /* Responsive */
    @media (max-width: 900px) {
      .${layoutName}-cards {
        grid-template-columns: 1fr 1fr;
      }
    }

    @media (max-width: 540px) {
      .${layoutName}-cards {
        grid-template-columns: 1fr;
      }

      .${layoutName}-section {
        padding: 3rem 1.5rem;
      }
    }
  </style>
</section>
{{ end }}`;
}

function generateFrontmatterTemplate(layoutName, featureName, steps) {
  const stepsTemplate = Array.from(
    { length: steps },
    (_, i) => `
    - step: ${i + 1}
      stepLabel: "Step ${i + 1}"
      icon: "📝"
      title: "Step Title Here"
      challenge: "The challenge or problem this addresses..."
      description: "Detailed description of what happens in this step..."
      outcome: "The positive outcome or deliverable..."
      tags:
        - "Tag 1"
        - "Tag 2"
        - "Tag 3"`,
  ).join('');

  return `# ${featureName.charAt(0).toUpperCase() + featureName.slice(1)} Steps - Frontmatter Example

Add this to your page's markdown frontmatter:

\`\`\`yaml
---
title: "Your Page Title"
layout: "full-width"
description: "Page description..."
${featureName}Steps:
  label: "Section Label"
  title: "Main Title with <br /><em>emphasis</em>"
  description: "Description text here..."
  steps:${stepsTemplate}
---
\`\`\`

## Implementation Steps

1. Create your markdown file under \`src/integrations.at/content/\` following the current page-type pattern from \`docs/\`.
2. Add the frontmatter above with your custom content.
3. Include the generated partial from the relevant layout or reusable partial chain:
  \`\`\`html
  {{ partial "ui-components/layout-${layoutName}-steps.html" . }}
  \`\`\`
4. Customize colors in the partial if needed.
5. Test using the repository's current Hugo workflow documented in \`docs/\`.

## Color Customization

Edit the CSS variables in the partial file:

- \`background\`: Section background color
- \`headerBg\`: Banner/header background
- \`labelColor\`: Section label color
- \`titleColor\`: Main title color
- \`emphasisColor\`: Emphasis/accent color

## Variable Reference

- \`label\` - Small label above main title
- \`title\` - Main heading (supports HTML \`<br />\` and \`<em>\`)
- \`description\` - Subtitle text
- \`steps\` - Array of step objects
  - \`step\` - Numeric step number (1-based)
  - \`stepLabel\` - Step name
  - \`icon\` - Emoji or icon character
  - \`title\` - Card title
  - \`challenge\` - Problem/challenge statement
  - \`description\` - Detailed description
  - \`outcome\` - Expected result
  - \`tags\` - Array of tag labels
`;
}
