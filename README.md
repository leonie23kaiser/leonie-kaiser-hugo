# leoniekaiser.com

Hugo-Site für **Leonie Kaiser — KI & Business Consulting**. Live unter
[leoniekaiser.com](https://leoniekaiser.com), gehostet auf GitHub Pages.

Zielgruppe: kleine Dienstleistungsunternehmen (3–20 MA), v.a. Beratung,
Gesundheit, wissensintensive Services. Voice: Sie-Form, B2B, DSGVO/EU-AI-Act-konform.

## Status

**Phase 3 live.** Brand-Voice-Guard, SEO/GEO-Stack (FAQ + AggregateRating-Schema,
llms.txt, robots.txt mit AI-Bot-Allowlist), `/eu-ai-act/`-Authority-Pillar,
4 Branchen-Landings aus `data/branchen.yaml`, Journal mit future-dated Drafts
(Cron Montag 05:00 UTC, `--buildFuture`, HITL-Issue-Notify an `leonie23kaiser`
mit Label `journal-live`), Testimonials von Pilot-Kundinnen.

## Stack

- Hugo Extended **0.123.7**
- Self-hosted Fonts: **Cabinet Grotesk** (Display) + **Satoshi** (UI), kein Google Fonts
- Brand-Tokens: Teal `#086584` / Gold `#CF982B` / Violett `#6B2C8C` / Beige `#FAF0E9`
- Eine zentrale CSS-Datei: `assets/css/brand.css`
- Bilder: Source in `assets/images/`, `partials/picture.html` generiert WebP + responsive srcset
- Schema.org JSON-LD `@graph`: Person + Organization + Service + FAQPage + AggregateRating + Reviews + BreadcrumbList
- Deploy: GitHub Pages via `.github/workflows/deploy-pages.yml`, custom domain `leoniekaiser.com`

## Site-Struktur

- `/` — Home (Hero, Leistungen, Prozess, Journal-Teaser, CTA)
- `/ueber-mich/`, `/faq/`, `/impressum/`, `/datenschutz/`
- `/referenzen/`, `/eu-ai-act/` (Authority-Pillar)
- `/journal/` + `/journal/<slug>/`
- `/ki-fuer-<branche>/` (programmatisch aus `data/branchen.yaml`)

**Single-CTA pro Seite:** Buchung der kostenlosen 30-min KI-Potenzialanalyse via
Calendly (`https://calendly.com/leonie-kaiser/ki-potentialanalyse`).

## Doku

- **`AGENTS.md`** — Brand-Voice-Guard für KI-Assistenten (Sie-Form, Wort-Whitelist/Blacklist, Persona Martina), **kanonisch**.
- **`CLAUDE.md`** — Hugo-Konventionen, Brand-Tokens, Working-Patterns.
- **`ONBOARDING.md`** — Leonies persönlicher Workflow (claude.ai-Connector + exe.dev-VM).
- **`docs/`** — Architektur, Content-Model, Layouts, Deploy, SEO/JSON-LD, Alexander-Konventionen.

## Entwicklung

```bash
hugo server --source src/growthtogether.at -D    # dev-server inkl. drafts
hugo --source src/growthtogether.at --minify     # production build
```

*Hinweis: Der Source-Ordner heißt historisch noch `src/growthtogether.at/`. Die
live Domain ist `leoniekaiser.com`, der Ordnername bleibt aus Git-Historien-Gründen
so wie er ist — nicht umbenennen.*
