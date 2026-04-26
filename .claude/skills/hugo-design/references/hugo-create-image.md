# hugo-create-image

Generate a new image for a Hugo page using FLUX.2-pro via the image-generator MCP.

## Triggers
"generate image", "create image", "AI image", "FLUX", "no image exists", "image for fighter", "event banner"

## When to Use
- No suitable image exists and one needs to be created from scratch
- Generating a fighter portrait, event banner, OG image, or hero image
- Iterating on image variations before committing

## When NOT to Use
- Uploading or resizing an existing asset → use `hugo-add-images`

## Prerequisites

The `image-generator` MCP server must be running at `http://localhost:3002`:

```bash
cd mcp-apps/image-generator && dotnet run
```

Registered in `.mcp.json` as `"image-generator"`.

## Supported Image Types

Call `mcp__image-generator__ListImageTypes` for the full table. Relevant types for SuperLeague.TV:
`fighter-portrait`, `event-banner`, `hero-background`, `og-image`

## 3-Step Generation Workflow

**Step 1 — List & Select**
Call `mcp__image-generator__ListImageTypes`, show table, ask user for: type, description, filename (kebab-case slug).
For `event-banner`: also ask for the fight night name.

**Step 2 — Optional Preview**
Call `mcp__image-generator__PreviewPrompt` to show the expanded FLUX prompt before spending API credits.

**Step 3 — Generate**
Call `mcp__image-generator__GenerateImage`:
```json
{ "description": "...", "imageType": "fighter-portrait", "filename": "first-last", "subfolder": "fighters" }
```

The MCP builds the FLUX prompt, calls Azure AI Foundry, streams the PNG inline to chat, saves to the correct `assets/images/` subfolder, and returns ready-to-paste front matter YAML.

## Notes
- Generation takes 10–30 seconds
- Output saved as PNG under `src/superleague.tv/assets/images/`
- Apply the returned YAML to the target fighter or event page's `portrait` or `banner` field
