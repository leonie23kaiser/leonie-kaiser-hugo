---
name: hugo-attach-action-behavior
description: Attaches global UI notifications (hover hints, click feedback, toast messages) to Hugo layout elements using data attributes. Use when the user asks to add an action behavior, hover hint, click popup, or notification to a card, button, or link. Do not use for dense lists.
---

# hugo-attach-action-behavior

## Overview

This skill helps you easily add elegant, centralized UI notifications to interactive elements (like Cards, Buttons, Avatars) inside Hugo templates. It leverages a global JavaScript handler driven entirely by declarative HTML data attributes (`data-notify-hover`, `data-notify-click`), meaning you **do not** need to write or generate any custom JavaScript or CSS for the user.

## When to Use

- Adding a hover hint to a UI Card (e.g., "Explore this class").
- Adding a success toast when a user clicks a button (e.g., "✓ Email copied").
- Enhancing standalone interactive elements.

## When NOT to Use

- **Dense Lists/Sidebars:** Do not attach hover behaviors to tightly packed lists. This creates a jarring "strobe light" UI effect at the bottom of the screen as the user moves their mouse.

## The Syntax

You can attach one or both of these attributes directly to the target HTML element:

1. **Hover Hint (Desktop Discovery):**
   `data-notify-hover="Your hint text"`
   _(This renders an accent-colored notification and is automatically suppressed on touch/mobile devices)._

2. **Click Status (Universal Feedback):**
   `data-notify-click="<span class='global-notification-success-icon'>✓</span> Your success text"`
   _(This renders a dark, persistent toast. Always include the span with the checkmark if indicating a successful action)._

## Step-by-Step Instructions for the Agent

When a user asks you to add an action behavior or notification:

1. **Identify the HTML target** in the requested layout file (e.g., `src/superleague.tv/layouts/...`).
2. **Inject the data attributes** into the HTML tag alongside existing attributes.
3. **Make it Dynamic (Crucial):** If the target is a repeatable element like a Card inside a Hugo loop (`{{ range .Pages }}`), use Go templating to inject the context into the attribute.
   - _Example:_ `data-notify-hover="Read: {{ .Title }}"`
4. **Preserve Functionality:** Never overwrite existing `onclick`, `href`, or classes. The notification system passively listens to the DOM.

### Migrating from legacy `title` / `onmouseover` patterns

When migrating existing elements that use native browser tooltips or inline JS hover effects:

- **Remove** the `title` attribute (replaced by `data-notify-hover`).
- **Remove** inline `onmouseover` / `onmouseout` handlers used only for visual hover feedback (e.g., `this.style.transform='scale(1.05)'`). The notification system provides the feedback instead.
- **Remove** the CSS `transition` property added solely for that scale effect if no other transition is needed.
- **Keep** `onclick`, `href`, `target`, `rel`, and all semantic/functional attributes untouched.

```html
<!-- Before -->
<a href="{{ . }}" target="_blank"
   title="Contact me on LinkedIn"
   style="... transition: transform 0.2s;"
   onmouseover="this.style.transform='scale(1.05)'"
   onmouseout="this.style.transform='scale(1)'">

<!-- After -->
<a href="{{ . }}" target="_blank"
   data-notify-hover="Contact me on LinkedIn"
   style="...">
```

## Examples

### 1. Simple Status Button

```html
<button class="btn"
  onclick="copyLinkToClipboard()"
  data-notify-hover="Copy link"
  data-notify-click="<span class='global-notification-success-icon'>✓</span>Link copied">
  Share
</button>
```

### 2. Dynamic Card (Inside a Hugo layout)

```html
{{ range .Pages }}
  <div class="card"
       data-notify-hover="Explore {{ .Title }}"
       data-notify-click="Opening..."
       onclick="window.location='{{ .RelPermalink }}'">
      <h3>{{ .Title }}</h3>
  </div>
{{ end }}
```

## References

For deep architectural details, see: [docs/action-behaviors-notifications.md](../../../docs/action-behaviors-notifications.md)
