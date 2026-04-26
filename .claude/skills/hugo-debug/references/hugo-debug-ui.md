# hugo-debug-ui

Verify and debug Hugo UI changes using Chrome DevTools MCP — screenshots, computed styles, DOM state, and CSS cascade.

## Triggers
"check implementation", "layout bug", "CSS not applying", "inspect element", "computed style", "wrong layout", "accordion broken", "specificity", "!important"

## When to Use
- A layout, banner, or component looks wrong after a code change
- CSS is not applying or is being overridden (specificity / `!important`)
- An interactive element (accordion, menu, modal) is not behaving correctly
- Taking a screenshot to verify visual result after an edit

## MCP Tool Roles

| Tool | Layer | Purpose |
|------|-------|---------|
| `mcp_chrome-devtoo_*` | Visual / DOM | Screenshots, snapshots, computed styles, click interactions, viewport resize |
| `mcp_debugmcp_*` | JS logic | Breakpoints, step-through execution, variable inspection |
| `grep_search` + `evaluate_script` | Static CSS | Cascade tracing, specificity, `!important` detection without browser |

Use Chrome DevTools to observe **what** is happening visually. Use DebugMCP to understand **why** JS behaves that way. Use static CSS analysis to trace cascade before opening a browser.

## Chrome DevTools Usage Pattern

```
1. mcp_chrome-devtoo_list_pages        → get existing pageId (always reuse)
2. mcp_chrome-devtoo_navigate_page     → reload if needed
3. mcp_chrome-devtoo_take_screenshot   → capture visual state
4. mcp_chrome-devtoo_take_snapshot     → inspect a11y tree + DOM
5. mcp_chrome-devtoo_resize_page       → check at 320px, 768px, 1200px
```

## Static CSS Analysis Workflow (No Browser Required)

```
# 1. Find all rules matching a selector
grep_search { query: ".card-title", includePattern: "src/integrations.at/assets/css/**" }

# 2. Find !important overrides
grep_search { query: "!important", includePattern: "src/integrations.at/assets/css/**" }

# 3. Check CSS variable definitions and overrides
grep_search { query: "--my-variable", includePattern: "src/integrations.at/assets/css/**" }
```

Watch for CSS variables redefined in component scopes — the scoped definition silently wins for descendants.

## Computed Value Verification

```js
// In mcp_chrome-devtoo_evaluate_script:
() => {
  const el = document.querySelector('.card-title');
  const s = window.getComputedStyle(el);
  return { color: s.color, fontSize: s.fontSize, display: s.display };
}
```

If computed value matches static analysis prediction → correct. If not → specificity conflict or `!important`.

## Specificity Quick Reference

`inline > #id > .class / [attr] / :pseudo-class > element`

A single `#id` (0,1,0,0) beats unlimited `.class` chains (0,0,N,0).

## CSS Asset Location

Source files: `src/integrations.at/assets/css/` (11 files, concatenated by Hugo Pipes).
Do NOT search generated bundles — search the source `.css` files only.
