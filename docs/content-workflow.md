# Content Workflow

All commands run from the **repo root** (not from `src/growthtogether.at/`). The `--source` flag tells Hugo where the project lives.

```bash
hugo server --source src/growthtogether.at -D     # → http://localhost:1313
hugo --source src/growthtogether.at --minify      # → src/growthtogether.at/public/
```

## Edit hero copy

Open `src/growthtogether.at/data/site.yaml` → `hero:` block.

```yaml
hero:
  badge: "Simply AI · Wien · Niederösterreich"
  headline_line1: "KI-Strategie & Automatisierung"
  headline_line2: "…einfach umgesetzt."
  tagline: "..."
  lead: "..."
  cta_primary: "Kostenfreie Potenzialanalyse"
  cta_primary_href: "#kontakt"
```

Change the strings, save, the dev server reloads automatically.

## Add a new service card

`data/site.yaml` → `services.items:` is a list. Append a new YAML object with the same shape:

```yaml
services:
  items:
    - tag: "Gratis · Erstgespräch"
      tag_style: "gold"
      title: "..."
      text: "..."
      points: ["...", "..."]
      price: "Kostenlos"
      price_note: "30 Min. · Online"
      featured: false
```

Fields:

| Field | Required | Notes |
|---|---|---|
| `tag` | yes | Pill above the title |
| `tag_style` | yes | `"gold"` or `"gold-on-featured"` (use the second one if `featured: true`) |
| `title` | yes | Card heading |
| `text` | yes | Description paragraph |
| `points` | yes | Bullet list (3–5 items work best) |
| `price` | yes | e.g. `"Auf Anfrage"`, `"Kostenlos"`, `"ab € 1.500"` |
| `price_note` | optional | Below price |
| `featured` | yes | Only ONE card should have `featured: true` (visually highlighted) |

The grid auto-adjusts to 3 or 4 cards. Beyond 4, talk to the dev about layout.

## Replace a photo (the right way — pipeline)

For portraits, banners, badges:

1. Drop the new source PNG into `src/growthtogether.at/assets/images/<sensible-name>.png` (high-res, e.g. 1600 px wide).
2. Update the relevant `picture.html` call to point to the new file.
3. Hugo regenerates WebP + JPEG variants on next build.

## Replace a photo (current pragmatic way — pre-renders)

The live `home.html` still uses pre-rendered `static/images/<name>.{jpg,webp}` pairs for the hero/about/banner photos. To swap one:

1. Pre-render a JPEG and WebP at the same dimensions (e.g. 800×800 hero, 800×960 about portrait, 1200×400 banner).
2. Save both as `static/images/<name>.jpg` and `static/images/<name>.webp` (overwrite or new name).
3. If new name: update the file path in `home.html`'s inline `<picture>` block.

Keep the source PNG in `assets/images/reserve/` so we can re-render later.

**Image dimension cheat-sheet (current site):**

| Slot | Dimensions | Aspect | Notes |
|---|---|---|---|
| Hero portrait | 800×800 | 1/1 | Round mask via CSS, LCP image (`fetchpriority="high"`) |
| About portrait | 800×960 | 4/5 | Card with 20px radius, badge overlay bottom-right |
| Conscious Consultant badge | 1080×1080 | 1/1 | Round, scaled to 140 px (mobile 100 px) |
| Simply AI banner | varies | wide | Above workshop section |
| Workshop image | varies | landscape | Left of workshop copy block |
| OG default | 1200×630 | 1.91/1 | Static, branded |

## Add a workshop date / event details

`data/site.yaml` → `workshop:` block. Edit `meta:` for the next-date string:

```yaml
workshop:
  meta: "Online · Teilnahme kostenfrei · Nächster Termin: 15. Mai 2026, 18:00"
  cta_label: "Anmelden"
  cta_href: "https://calendly.com/leonie-kaiser/your-unique-genius"
```

When the workshop becomes a real event with multiple dates, promote it to a content collection (`content/workshops/`).

## Add a real testimonial (when one arrives)

Replace the placeholder in `data/site.yaml` → `testimonials:`:

```yaml
testimonials:
  eyebrow: "Referenzen"
  heading: "Was Kund:innen sagen"
  items:
    - quote: "Leonie hat unser Team in 4 Wochen von KI-Skepsis zu erstem Live-Use-Case begleitet."
      author: "Max Muster"
      role: "GF, Beispiel GmbH"
      photo: "images/testimonials/max-muster.jpg"   # optional, in assets/
```

**Then update `home.html`:** the current testimonials section renders the placeholder block. Add an `{{ if .items }}…{{ else }}…{{ end }}` branch to render the items list when it's present. (Dev work, not editable copy.)

## Update Calendly URL

`config/_default/params.toml`:

```toml
calendly = "https://calendly.com/leonie-kaiser/<new-event-type>"
```

The contact card CTA picks it up automatically. The Calendly button in the hero (if it links to `#kontakt` and from there to the URL) also follows.

## Add a menu item

`config/_default/menus.toml`:

```toml
[[main]]
  name   = "Blog"
  url    = "/blog/"
  weight = 35              # between Workshop (25) and Prozess (30) — reorder numerically
```

If the URL is an anchor (`/#xyz`), the corresponding `<section id="xyz">` must exist in `home.html`.

## Edit Impressum / Datenschutz

Standard Markdown. Edit `src/growthtogether.at/content/impressum.md` or `datenschutz.md`. Frontmatter has `title` + `description`, body is plain Markdown. Rendered by `layouts/_default/single.html`.

## Update brand colours

**Two places must change in lockstep:**

1. `config/_default/params.toml` — the `brand*` keys
2. `src/growthtogether.at/assets/css/brand.css` — the `:root { --lk-* }` block at the top

If you only update one, the JSON-LD / OG / theme-color meta tags will drift from the visual design.

## Draft / preview before publish

- `hugo server --source src/growthtogether.at -D` shows drafts (`draft: true` in frontmatter).
- Open `http://localhost:1313/` in the browser. Live reload is on.
- For mobile preview, use Chrome devtools or `browser_emulate iphone_14`-style tooling.

## Publish (deploy)

See [deploy.md](deploy.md). **Do not deploy without explicit go-ahead** — live site is a paying client.

## Quick reference — "who edits what"

| Task | File(s) |
|---|---|
| Hero / services / about / workshop / process / contact copy | `data/site.yaml` |
| Phone, email, Calendly, LinkedIn | `params.toml` |
| Brand colour | `params.toml` + `brand.css` |
| Menu | `menus.toml` |
| Impressum / Datenschutz | `content/impressum.md` / `datenschutz.md` |
| New image (proper way) | `assets/images/...` + `picture.html` call in `home.html` |
| New image (quick way) | `static/images/...{jpg,webp}` + inline `<picture>` in `home.html` |
| New testimonial | `data/site.yaml` testimonials block + small `home.html` change |
| Layout / new section | `home.html` + `data/site.yaml` + `menus.toml` + CSS |
