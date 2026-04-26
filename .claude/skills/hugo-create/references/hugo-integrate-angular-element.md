# hugo-integrate-angular-element

Embed a pre-built Angular Element (Web Component) into a Hugo static page.

## Triggers
"angular element", "web component", "interactive widget", "skills-list", "defer load angular"

## When to Use
- Adding an interactive widget (e.g. `skills-list`) to a class or service page
- Page needs client-side interactivity not suited to Go templates
- The Angular Element is already built and published to `static/ng-elements/`

## Integration Pattern (4 Steps)

### 1. Publish the Bundle

```bash
# From repo root — publish path for skills-list:
npm run deploy:element
# Copies dist/skills-list/browser/main.js → src/integrations.at/static/ng-elements/skills-list/main.js
```

Served at `/ng-elements/skills-list/main.js`. Angular Element bundles in `static/` must **not** be processed by Hugo Pipes (they need a stable, predictable URL).

### 2. Page-Scoped Front Matter Opt-In

```yaml
elementDemo:
  enabled: true
  width: 320
  title: "Skills Demo"
  description: "Interact with the element."
  skills:
    - name: "Signals"
      description: "Reactive state management"
```

### 3. Conditional Template Rendering

Check `elementDemo.enabled` — render a placeholder container, **not** the element itself:

```html
{{ with .Params.elementDemo }}{{ if .enabled }}
<aside aria-labelledby="demo-title">
  <div id="element-container" class="element-wrapper"></div>
</aside>
{{ end }}{{ end }}
```

### 4. Defer Load + Create After Paint

```html
<script src="{{ "ng-elements/skills-list/main.js" | relURL }}" defer></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  requestAnimationFrame(function () {
    var container = document.getElementById('element-container');
    if (!container) return;
    var el = document.createElement('skills-list');
    el.width = {{ .width | default 320 }};
    el.skills = {{ .skills | jsonify | safeJS }};
    container.appendChild(el);
  });
});
</script>
```

## Key Repo Notes
- `static/ng-elements/` hosts stable-URL bundles — do NOT process with Hugo Pipes
- Deploy script: `npm run deploy:element` at repo root
- Reference template: `layouts/classes/class-detail.html`
- Docs: `docs/angular-elements-integration.md`
