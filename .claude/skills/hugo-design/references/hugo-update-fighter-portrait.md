# hugo-update-fighter-portrait

Set or replace the portrait image for a fighter profile page.

## Triggers
"update fighter portrait", "fighter image", "replace portrait", "fighter photo", "fighter picture"

## When to Use
- Swapping the existing fighter portrait for a new file
- Image is already saved (or being provided) to `assets/images/fighters/`
- Updates the `portrait` field in the fighter page's front matter

## Target Paths
- **Image storage**: `src/superleague.tv/assets/images/fighters/<fighter-slug>.<ext>`
- **Content file**: `src/superleague.tv/content/fighters/<fighter-slug>.md` → `portrait` frontmatter field

## Pipeline Note

Fighter portraits go through the `picture.html` Hugo partial (WebP + srcset). Place the image in `assets/images/fighters/` — **not** in `static/images/fighters/` — for pipeline processing. The `static/images/fighters/` folder is for unprocessed fallbacks only.

## Front Matter Update

```yaml
portrait: "images/fighters/first-last.jpg"   # path relative to assets/
```

## Workflow

1. Copy the new image to `src/superleague.tv/assets/images/fighters/<slug>.<ext>`
2. Update the `portrait` field in `src/superleague.tv/content/fighters/<slug>.md`
3. Run `hugo server -D` from `src/superleague.tv/` and verify the fighter page renders correctly at `http://localhost:1313/fighters/<slug>/`

## Verify

Check the fighters list at `http://localhost:1313/fighters/` and the single fighter page to confirm the portrait appears at the correct aspect ratio.
