# hugo-change-colors

Update CSS variables for colors, spacing, and typography site-wide.

## Triggers
"change color", "update brand color", "change spacing", "CSS variable", "design token"

## When to Use
- Changing the primary, secondary, or accent brand colors
- Updating spacing scale, font sizes, or border-radius tokens
- Applying a design token change that affects the whole site

## CSS Variables File

`src/superleague.tv/assets/css/brand.css` — all variables defined in `:root`.

> **Note:** CSS is served through Hugo Pipes. `brand.css` is the single source of truth — minified and fingerprinted with SRI in production. Edit the source file directly; do not add separate CSS files.

## Key Variable Categories

```css
/* Brand palette */
--sl-red:    #E1061A   /* primary accent */
--sl-red-2:  #ff2a3a   /* hover variant */
--sl-black:  #0A0A0A   /* page background */
--sl-ink:    #141414   /* card backgrounds */
--sl-ink-2:  #1c1c1e   /* elevated surfaces */
--sl-line:   #2a2a2e   /* borders/dividers */
--sl-white:  #FFFFFF
--sl-mute:   #b8b8bd   /* secondary text */
--sl-gold:   #C9A55A   /* title fights / highlight */

/* Semantic aliases */
--sl-bg:     var(--sl-black)
--sl-fg:     var(--sl-white)
--sl-accent: var(--sl-red)

/* Typography */
--sl-font-ui:      'Inter', system-ui, ...
--sl-font-display: 'Oswald', 'Arial Black', Impact, ...

/* Layout */
--sl-radius:    4px
--sl-container: 1240px
```

## Workflow

1. Identify the variable: `grep` in `src/superleague.tv/assets/css/brand.css`
2. Update the value in the `:root` block
3. Hugo Pipes picks up the change automatically on the next build
4. Verify visually across affected pages (fighters list, events, homepage)
