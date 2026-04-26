# hugo-add-step

Add a new step to an existing Hugo service or area page's `stepsSection`.

## Triggers
"add step", "new plugin step", "extend service page", "add engagement phase", "stepsSection"

## When to Use
- Extending an existing page with a new plugin, phase, or engagement item
- Adding to a specific named `group` within `stepsSection`
- Modifies front matter only — does not create a new page

## When NOT to Use
- Creating a new page → use `hugo-create-service-page` or `hugo-create-area-page`
- Changing step group headings or layout → edit front matter directly

## Prerequisites
- Target page has `layout: "steps-layout"` with a `stepsSection:` block
- Know which `group` id to add to (e.g. `core`, `extend`, `social`)

## Step YAML Schema

```yaml
- step: 3                          # sequential number WITHIN the group (not global)
  stepLabel: "Plugin - Optional"   # short label above title
  group: "extend"                  # must match a stepGroups[].id
  type: "plugin"                   # "plugin" = body-only card (no challenge/outcome)
  icon: "📅"
  title: "Schedule & Timetable Plugin"
  body: "Decision-maker copy. 2-3 sentences: problem → what we deliver → outcome."
```

## Field Rules

| Field | Required | Notes |
|-------|----------|-------|
| `step` | Yes | Sequential integer within the group. Check existing steps in that group; use next number. |
| `stepLabel` | Yes | 1–3 words. Optional plugins: `"[Name] Plugin - Optional"`. Core phases: action verbs. |
| `group` | Yes | Must match an `id` in `stepGroups`. Common: `core`, `extend`, `social`. |
| `type` | Yes | `"plugin"` renders `body` only. Omit for challenge/outcome cards. |
| `icon` | Yes | Single emoji. |
| `title` | Yes | 3–6 words, benefit-oriented. |
| `body` | Yes | 2–4 sentences, decision-maker voice. Problem → what we do → business outcome. Max 60 words. |

## Workflow

1. Read the target page front matter — identify `group` id and highest existing `step` in that group
2. Write the step YAML block using the schema above
3. Append at the end of all steps for that group (keep group steps contiguous in the file)
4. Verify `step` is sequential within the group and `group` matches a `stepGroups[].id`
