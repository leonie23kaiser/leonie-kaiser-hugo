# hugo-plan-plugin

Scope and catalog a new Hugo CMS plugin from existing customer projects or shortcodes.

## Triggers
"plan plugin", "analyze shortcode", "plugin catalog", "sellable plugin", "customer project feature"

## When to Use
- Analyzing an existing shortcode or data-driven feature for plugin potential
- Mapping customer implementations to sellable engagement steps
- Building a plugin catalog entry for the "Agentic Plugins & Integrations" group
- Source is a real customer project or shortcode library

## When NOT to Use
- Adding a single already-defined step → use `hugo-add-step`
- Writing the actual plugin implementation

## Workflow

### Phase 1: Discovery

**1.1** Read customer project `docs/readme.md`.

**1.2** Inventory `layouts/shortcodes/` — list all shortcode files.

**1.3** For each shortcode determine:
- Data source? (`site.Data.*`, page params, API)
- UI rendered? (table, grid, carousel, form)
- Page-scoped or global?
- Interactive behavior? (filters, tabs, lightbox)
- Non-developer editable? (JSON file, data folder)

**1.4** Score plugin potential:

| Criteria | Score |
|----------|-------|
| Reusable across customers | High / Medium / Low |
| Business value (decision-maker appeal) | High / Medium / Low |
| Implementation complexity | Low / Medium / High |
| Data model simplicity | Simple / Complex |

Skip features scoring Low on both reusability AND business value.

### Phase 2: Plugin Definition

```yaml
plugin:
  name: "Schedule & Timetable"
  source_shortcode: "timetable.html"
  data_source: "site.Data.schedule (JSON)"
  ui_components:
    - "Weekly grid table (desktop)"
    - "Card list (mobile)"
    - "Filter pills by category"
  business_value: "Staff updates schedules via JSON — no developer, no CMS login"
  complexity: "Medium"
  reusability: "High — any business with recurring schedules"
```

### Phase 3: Map to Engagement Steps

For each qualifying plugin, write the step entry following the `hugo-add-step` schema (see `hugo-add-step.md`). Decision-maker voice: problem → what we build → business outcome. Max 60 words.
