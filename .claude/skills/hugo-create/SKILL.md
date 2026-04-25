---
name: hugo-create
description: >-
  Master skill for building new Hugo CMS pages, sections, and content types on the integrations.at site.
  Delegates to the correct narrow leaf skill based on what needs to be built.
  Use when creating area pages, service pages, training classes, adding engagement steps, or integrating
  Angular Elements. Triggers on: "create a page", "add a new class", "new service page", "add a step",
  "build a section", "new content type", "integrate a widget", "scaffold a layout".
license: Complete terms in LICENSE.txt
---

# hugo-create — Page & Content Creation Router

Routes content creation requests to the appropriate narrow leaf skill. Do not implement directly — delegate immediately.

## When to Use This Skill

- Creating a new area page (e.g. Cloud Native, Agentic AI, M365)
- Creating a new service page with a 3-column engagement flow
- Creating a new training class with curriculum modules
- Adding an engagement step to an existing service or area page
- Integrating a pre-built Angular Element (Web Component) into a content page

**Trigger keywords:** `create`, `add a new`, `build a page`, `new class`, `new service`, `scaffold`, `new section`, `add step`, `integrate widget`

## Delegate Map

| Request type                          | Leaf skill to invoke                                                             |
| ------------------------------------- | -------------------------------------------------------------------------------- |
| New area page (steps + sidebar)       | [`hugo-create-area-page`](references/hugo-create-area-page.md)                   |
| New service page (3-column flow)      | [`hugo-create-service-page`](references/hugo-create-service-page.md)             |
| New training class                    | [`hugo-create-class`](references/hugo-create-class.md)                           |
| Add a step to an existing page        | [`hugo-add-step`](references/hugo-add-step.md)                                   |
| Scaffold a reusable steps layout      | [`hugo-create-layout-page`](references/hugo-create-layout-page.md)               |
| Embed Angular Element (Web Component) | [`hugo-integrate-angular-element`](references/hugo-integrate-angular-element.md) |

> `hugo-expert` is the top-level router. If the request is ambiguous or spans multiple concerns, defer back to `hugo-expert`.

## Example Prompts

- "Create a new area page for DevOps with steps and a sidebar."
- "Add a new training class: GitHub Copilot Fundamentals, 2 days, intermediate."
- "Add a 'Design Review' step to the cloud-native service page."
- "Scaffold a reusable steps-based layout partial for a new content pattern."
- "Integrate the skills-list Angular Element on the class detail page."
