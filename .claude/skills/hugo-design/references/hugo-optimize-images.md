# hugo-optimize-images

Optimize existing Hugo image assets by generating modern compressed siblings for larger source files.

## When to Use

- Reviewing image-heavy sections for size reductions.
- Generating `.webp` and `.avif` siblings for larger `.png` or `.jpg` assets.
- Running the current Sharp-based helper against Hugo image folders.

## What This Reference Covers

- Where the optimization helper lives.
- Which image folders and formats it scans.
- What the helper writes and what it does not change.
- How to run it from the co-located skill script folder.

## Helper Location

The helper lives under:

`.claude/skills/hugo-design/scripts/image-optimization/`

Key files:

- `scripts/image-optimization/optimize.js`
- `scripts/image-optimization/package.json`

## Current Behavior

- Scans `src/superleague.tv/assets/images/`.
- Limits work to `fighters` and `events` subfolders.
- Processes `.png`, `.jpg`, and `.jpeg` files.
- Skips files smaller than 100 KB.
- Writes sibling `.webp` and `.avif` files.
- Does not replace originals automatically.
- Does not update front matter or templates automatically.

## Run the Helper

```bash
cd .claude/skills/hugo-design/scripts/image-optimization
npm install
npm run optimize
```

## Note

SuperLeague uses Hugo's built-in asset pipeline (`picture.html` partial) to serve WebP srcsets at build time. Manual optimization siblings are useful for images served from `static/` (outside the pipeline) or for pre-build size reduction.

## Docs-First Note

- Use `hugo-add-images` for placement, naming, and front matter work.
