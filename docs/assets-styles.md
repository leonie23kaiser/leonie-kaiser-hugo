# Assets & Styles

## CSS — `assets/css/brand.css`

Single source of truth for all styles, ~830 lines and growing. No CSS framework. All components inline in this one file.

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
  "alt"    "Leonie Kaiser – KI- & Digitalisierungs-Expertin"
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
| `assets/images/` | Testimonial photos (`Angela-Caine.png`, `Megan-Bailey.png`, `Mor-Yelvington.png`), `Bild-1.png`, `logo.png`, `leonie-kaiser-portrait.png`, `simply-ai-banner.png`, `workshop-unique-genius.png`, `reserve/` (alternates), and `blog/` (blog post covers + `CREDITS.md`) | Goes through Hugo's asset pipeline when referenced via `picture.html` |
| `static/images/` | Pre-rendered `.png` + `.webp` pairs (`Bild-1`, `Bild-2`, `Logo`, `CCC-Stempel`, `background`, `leonie-portrait-hero`, `leonie-about-thoughtful`, `conscious-consultant-badge`, mobile-specific hero variants, `simply-ai-banner-new`, `workshop-unique-genius`) + `og-default.png`, plus a `blog/` subfolder with SVG placeholder covers | Copied as-is to `public/` — bypasses the pipeline entirely |

`home.html` and most other layouts reference the **`static/` pre-renders** directly via inline `<picture>` blocks, not via `picture.html`. This predates the current codebase and hasn't been cleaned up.

**Blog covers are the one place doing it the "right" way already:** `content/journal/*.md`'s `cover:` front matter points at `assets/images/blog/`, and `layouts/journal/list.html`/`single.html` render them through `picture.html`. `static/images/blog/` also has a few SVG placeholder covers left over from before real cover photos existed — check `content/journal/*.md`'s `cover:` value to see which is actually live for a given post before assuming either is unused.

**Future cleanup (no spec yet):**
1. Move remaining pre-renders from `static/images/` into `assets/images/<section>/`.
2. Replace inline `<picture>` blocks in `home.html` (and other layouts) with `picture.html` partial calls.
3. Delete the pre-rendered pairs in `static/` once migrated, and remove any now-unused SVG placeholder covers from `static/images/blog/`.

Until then: when adding a new image, prefer the pipeline path (`assets/` + `picture.html`) — the blog cover pattern above is the template to copy. Don't add more pre-rendered pairs to `static/`.

### `assets/images/reserve/`

The `reserve/` subfolder holds 11 alternate / unused photos kept on disk for fast swaps without re-export from the source files. Examples: alternate hero portraits, the previous Simply AI banner, the previous workshop image. Do not delete — they're our fallback library.

## Static files

Files in `static/` are copied as-is to `public/`. Currently:

| File / folder | Purpose |
|---|---|
| `favicon.ico` / `favicon.svg` / `apple-touch-icon.png` | site icons, referenced from `head.html` |
| `robots.txt` | search engine crawl rules — AI bots explicitly allowed |
| `llms.txt` | AI/GEO plain-text site summary, hand-maintained (see [seo-jsonld.md](seo-jsonld.md)) |
| `CNAME` | GitHub Pages custom domain file — `leoniekaiser.com` |
| `fonts/*.woff2` | self-hosted webfonts |
| `images/*.{png,webp}` | pre-rendered photo pairs (see above) + `og-default.png` |
| `images/blog/` | legacy SVG placeholder covers (mostly superseded by real photos, see above) |
| `downloads/service-katalog.pdf` | downloadable service catalogue. **Generated**, not hand-edited: edit `tools/pdf-templates/service-katalog/service-katalog.html` and re-render (e.g. via a headless-Chromium `page.pdf()` script) — see recent commit history on that file for the render approach used. |
| `analyse/` | standalone HTML micro-tool (Potenzialanalyse-Präsentationsgenerator), maintained separately from the main site templates |

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
