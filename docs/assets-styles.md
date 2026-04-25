# Assets & Styles

## CSS — `assets/css/brand.css`

Single source of truth for all styles, ~490 lines. No CSS framework. All components inline in this one file.

### Build behaviour

- **Dev:** served raw via Hugo's dev server.
- **Prod:** minified, fingerprinted, and SRI hash injected into the `<link>` tag automatically by `partials/head.html`.

Never create additional CSS files. Add new styles to `brand.css` until the file exceeds ~10 component groups, then split per Alexander's pattern.

### Brand tokens (CSS custom properties)

These mirror `params.toml`. **If a colour changes, update both files.**

```css
:root {
  --lk-teal-900:    #086584;   /* primary — buttons, links, accents */
  --lk-teal-600:    #5FA2A0;   /* secondary — gradients, hover */
  --lk-teal-50:     #EDF7F2;   /* soft section background */
  --lk-teal-100:    #E7F4F4;   /* highlights */
  --lk-gold:        #CF982B;   /* labels */
  --lk-gold-soft:   #F1C50E;   /* sparse highlights */
  --lk-violet:      #6B2C8C;   /* eyebrows, secondary CTA */
  --lk-violet-soft: #EFE6F6;   /* pill background */
  --lk-violet-line: #D9C5E8;   /* pill border */
  --lk-beige:       #FAF0E9;   /* page background */
  --lk-ink:         #1d2228;   /* body text */
  --lk-mute:        #5b6572;   /* secondary text */
  --lk-line:        #ece3d8;   /* borders, separators */
}
```

### Typography

| Role | Font | Weight | Source |
|---|---|---|---|
| Headlines, hero, eyebrows | Cabinet Grotesk | 700 / 800 | self-hosted (`static/fonts/`) |
| Body, UI labels | Satoshi | 400 / 500 / 700 | self-hosted (`static/fonts/`) |

Fonts are **self-hosted** for DSGVO compliance — no Google Fonts CDN. Files live in `static/fonts/`:

```
static/fonts/
  cabinet-grotesk-700.woff2
  cabinet-grotesk-800.woff2
  satoshi-400.woff2
  satoshi-500.woff2
  satoshi-700.woff2
```

The two most-used weights (`satoshi-400`, `cabinet-grotesk-800`) are preloaded in `partials/head.html` to avoid FOIT/FOUT on the LCP heading.

## Image pipeline

Hugo's asset pipeline processes images placed under `assets/images/` at build time.

### `picture.html` partial

All new images should be rendered through `layouts/partials/picture.html`. It:

1. Loads the image via `resources.Get` from `assets/`
2. Resizes to each width in the `widths` slice
3. Converts to WebP (primary `<source>`) + keeps original format (fallback `<img>`)
4. Outputs a `<picture>` with `srcset` + `sizes`

```go-html-template
{{ partial "picture.html" (dict
  "src"    "images/leonie-portrait-hero.png"
  "alt"    "Leonie Kaiser – KI & Business Consultant"
  "sizes"  "(max-width: 700px) 100vw, 33vw"
  "widths" (slice 400 800 1200)
  "eager"  true
  "ratio"  "1/1"
) }}
```

| Param | Type | Description |
|---|---|---|
| `src` | string | Path under `assets/` |
| `alt` | string | Alt text |
| `class` | string | Optional CSS class |
| `sizes` | string | `sizes` attribute (default `"(max-width: 700px) 100vw, 33vw"`) |
| `widths` | slice | Pixel widths to generate (default `(slice 400 800 1200)`) |
| `eager` | bool | `true` for LCP — disables lazy load, adds `fetchpriority="high"` |
| `ratio` | string | CSS `aspect-ratio` value (e.g. `"3/4"`, `"16/9"`) |

### Image locations — the current dual setup

Leonie's repo has two image folders. **This is intentional but messy** — future work should consolidate.

| Folder | Contents | Notes |
|---|---|---|
| `assets/images/` | Source PNGs (`leonie-kaiser-portrait.png`, `simply-ai-banner.png`, `workshop-unique-genius.png`, `logo.png`) + `reserve/` (10 alternates) | Goes through Hugo pipeline when referenced via `picture.html` |
| `static/images/` | Pre-rendered `.jpg` + `.webp` pairs of currently active hero/about/banner photos + `og-default.png` | Copied as-is to `public/` — bypasses pipeline |

The live `home.html` references the **`static/` pre-renders** directly via inline `<picture>` blocks, not via `picture.html`. This was a pragmatic shortcut from the photo-update commits (April 2026) to ship fast without re-rendering through Hugo.

**Future cleanup (no spec yet):**
1. Move source PNGs from `assets/images/reserve/` and pre-renders from `static/images/` into a clean `assets/images/<section>/` layout.
2. Replace inline `<picture>` blocks in `home.html` with `picture.html` partial calls.
3. Delete the pre-rendered pairs in `static/`.

Until then: when adding a new image, prefer the pipeline path (`assets/` + `picture.html`) for anything new. Don't add more pre-rendered pairs.

### `assets/images/reserve/`

The `reserve/` subfolder holds alternate / unused photos kept on disk for fast swaps without re-export from the source files. Examples: alternate hero portraits, the previous Simply AI banner, the previous workshop image. Do not delete — they're our fallback library.

## Static files

Files in `static/` are copied as-is to `public/`. Currently:

| File | Purpose |
|---|---|
| `favicon.ico` / `favicon.svg` / `apple-touch-icon.png` | site icons, referenced from `head.html` |
| `robots.txt` | search engine crawl rules |
| `fonts/*.woff2` | self-hosted webfonts |
| `images/*.{jpg,webp}` | pre-rendered photo pairs (see above) |
| `images/og-default.png` | OpenGraph fallback (1200×630) |

## Adding a new image

For a NEW image (not replacing existing):

1. Drop the source PNG/JPG into `src/growthtogether.at/assets/images/<sensible-subfolder>/`.
2. In `home.html` (or wherever), call:
   ```go-html-template
   {{ partial "picture.html" (dict
     "src" "images/<subfolder>/<your-file>.png"
     "alt" "..."
     "sizes" "(max-width: 700px) 100vw, 800px"
     "widths" (slice 400 800 1200)
     "ratio" "<aspect>"
   ) }}
   ```
3. Hugo generates WebP + JPEG variants on next build.

For REPLACING an existing photo (and the existing photo is one of the `static/` pre-renders): see `content-workflow.md`.
