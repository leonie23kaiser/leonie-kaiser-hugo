# hugo-create-service-page

Create a new service page with a 3-column engagement flow (no sidebar).

## Triggers
"create service page", "engagement flow", "consulting service page", "3-column steps"

## When to Use
- Describing a specific consulting or delivery service
- 3-column `engagement` layout with sequential steps, no sidebar
- Service delivery methodology page

## When NOT to Use
- Needs a sidebar → use `hugo-create-area-page`

## Front Matter Schema

```yaml
---
title: "Service Name"
layout: "steps-layout"
type: "page"
description: "SEO description"
url: "/service-slug/"
aliases:
  - "/services/service-slug/"
banner:
  title: "..."
  image: "/images/services/service-slug/cover.jpg"
  image_position: "center"
  bullets:
    - "Bullet one"
engagementSteps:
  label: "5-Step Cloud Journey"
  title: "Transform to Cloud"
  description: "..."
  steps:
    - step: 1
      stepLabel: "Assess"
      icon: "📊"
      title: "Current State Analysis"
      challenge: "The problem being solved"
      description: "What we do"
      outcome: "Deliverable"
---
```

## File Location
`content/services/[service-name]-page.md`

## Step Flow
1. Gather: service name, engagement label, banner image, step count
2. Per step: number, label, icon, title, challenge, description, outcome, optional tags
3. Create the `.md` file
4. Verify 3-column layout on desktop at `localhost:1313/services/[slug]/`

## Notes
- `aliases` can redirect legacy URLs
- Steps render as 3-col grid on desktop, single column on mobile
- To extend with more steps after creation, use `hugo-add-step`
