# hugo-create-area-page

Create a new area page with multi-section steps, a sidebar, and a banner.

## Triggers
"create area page", "new area", "cloud native page", "agentic ai page", "m365 page", "steps + sidebar"

## When to Use
- Building a top-level practice area (Cloud Native, Agentic AI, M365)
- Page needs left-column step groups and a right-column sidebar panel
- Content type `area`, layout `steps-layout`

## When NOT to Use
- 3-column engagement flow with no sidebar → use `hugo-create-service-page`

## Front Matter Schema

```yaml
---
title: "Area Name"
layout: "steps-layout"
type: "page"
description: "SEO description"
url: "/areas/area-slug/"
banner:
  title: "..."
  image: "/images/areas/area-slug/banner.jpg"
  image_position: "center"
  bullets:
    - "Bullet one"
stepsSection:
  sidebarVariant: agentic-ai   # or: cloud-native | m365-copilot
  heading: "Heading text"
  stats:
    - number: "3×"
      label: "faster delivery"
  steps:
    - step: 1
      stepLabel: "Understand"
      stepColor: "#6366f1"
      title: "..."
      description: "..."
      outcome: "..."
      tags:
        - label: "Discovery"
          warm: false
  relatedItems:
    - "/classes/some-class/"
---
```

## File Location
`content/areas/[area-name]-page.md`

## Step Flow
1. Gather: area name, sidebar variant, banner image path, step count
2. Per step: label, stepColor (hex), title, description, outcome, tags
3. Create the `.md` file with the schema above
4. Verify at `localhost:1313/areas/[area]/`

## Sidebar Variant Choices
- `agentic-ai` — AI/automation context
- `cloud-native` — cloud infrastructure context
- `m365-copilot` — Microsoft 365 / Copilot context

## Notes
- `banner.image_position` is now wired to the template via inline `style="object-position: <value>"` — see repo memory
- `relatedItems` drives the "What We Can Build On" sidebar panel via `layouts/partials/sidebars/related-panel.html`
