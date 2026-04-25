# hugo-css-grid

Use CSS Grid for structured two-dimensional layouts and responsive area-based compositions.

## When to Use

- Building or debugging complex two-dimensional layouts.
- Designing named layout regions with `grid-template-areas`.
- Tuning responsive grid breakpoints.
- Diagnosing alignment and track sizing issues in browser tools.

## Core Concepts

- Use `display: grid` or `display: inline-grid` on the container.
- Define tracks with `grid-template-columns` and `grid-template-rows`.
- Use `gap` for spacing.
- Use `grid-auto-columns`, `grid-auto-rows`, and `grid-auto-flow` for implicit tracks.
- Use `fr`, `minmax()`, `repeat()`, `auto-fit`, and `auto-fill` intentionally.

## `grid-template-areas`

Use named areas when the layout is structural and should stay readable.

```css
.layout {
  display: grid;
  gap: 10px;
  grid-template-columns: 220px 1fr;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
}

.layout-header { grid-area: header; }
.layout-sidebar { grid-area: sidebar; }
.layout-main { grid-area: main; }
.layout-footer { grid-area: footer; }
```

Responsive grids can redefine only the area strings at different breakpoints.

```css
.layout {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-areas:
    "header"
    "main"
    "sidebar"
    "footer";
}

@media (min-width: 680px) {
  .layout {
    grid-template-columns: 220px 1fr;
    grid-template-areas:
      "header header"
      "sidebar main"
      "footer footer";
  }
}
```

## Browser Verification

- Inspect grid containers in browser tools rather than guessing track boundaries.
- Turn on grid overlays, area names, line names, and track sizes where available.
- Verify layout behavior at `320px`, `768px`, and `1280px`.
- Confirm the design still reflows correctly and does not require horizontal scrolling for normal content.

## Docs-First Note

- Use the repository's `docs/` for layout-specific patterns and breakpoint conventions.
- Use this reference for reusable CSS Grid reasoning, not for project-specific template decisions.