---
name: hugo-design
description: >-
  Master skill for all visual design changes on the SuperLeague.TV Hugo site: colors, spacing, typography,
  images, banners, and design tokens. Delegates to the correct narrow leaf skill.
  Use when updating brand colors, changing CSS variables, generating or swapping images, updating fighter
  portraits, or adjusting visual layout. Triggers on: "change color", "update spacing", "new banner image",
  "generate image", "update fighter image", "fix the look", "design tokens", "typography".
license: Complete terms in LICENSE.txt
---

# hugo-design — Visual Design Router

Routes visual and design change requests to the appropriate narrow leaf skill. Do not implement directly — delegate immediately.

## When to Use This Skill

- Updating global CSS variables (colors, spacing, font sizes)
- Adding or replacing images (fighter portraits, event banners, OG images)
- Generating a new AI image for a page using the image-generator MCP
- Updating or replacing a fighter portrait
- Adjusting banner image cropping or focal point
- Applying a design system change site-wide

**Trigger keywords:** `change color`, `update spacing`, `new image`, `generate image`, `banner`, `design tokens`, `CSS variable`, `typography`, `fighter portrait`, `visual`

## Delegate Map

| Request type                               | Leaf skill to invoke                                                     |
| ------------------------------------------ | ------------------------------------------------------------------------ |
| Update CSS variables (colors, spacing)     | [`hugo-change-colors`](references/hugo-change-colors.md)                 |
| Add / organize image files                 | [`hugo-add-images`](references/hugo-add-images.md)                       |
| Optimize existing image assets             | [`hugo-optimize-images`](references/hugo-optimize-images.md)             |
| Generate AI image via FLUX.2-pro           | [`hugo-create-image`](references/hugo-create-image.md)                   |
| Update a fighter portrait image            | [`hugo-update-fighter-portrait`](references/hugo-update-fighter-portrait.md) |
| Build or debug CSS Grid layouts            | [`hugo-css-grid`](references/hugo-css-grid.md)                           |
| Design system or visual component guidance | [`hugo-frontend-design`](references/hugo-frontend-design.md)             |

> For purely structural template changes, delegate to layout editing directly.

## Example Prompts

- "Update the primary brand color across the whole site."
- "Generate a banner image for the next fight night."
- "Replace the fighter portrait for Valon Basha."
- "Add the new OG image for the homepage."
