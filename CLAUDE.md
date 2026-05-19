# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Project

Hugo static-site for **Leonie Kaiser — KI & Business Consulting** (live: leoniekaiser.com).

- Hugo project root: `src/growthtogether.at/`
- Live deployment: **GitHub Pages** (`.github/workflows/deploy-pages.yml`) on the **leoniekaiser.com** custom domain via `static/CNAME`. After client sign-off the DNS is moved to **leoniekaiser.com**.
- **Full documentation: [docs/readme.md](docs/readme.md)** and **[ONBOARDING.md](ONBOARDING.md)** for Leonie's local Claude-Code workflow.

Hugo **v0.123+ extended** required.

## Site shape

Marketing site with anchor-based home + standalone pages. The home builder is `layouts/_default/home.html`, today rendering content from `content/_index.md` front-matter and inline markup. Standalone pages backed by `layouts/<slug>/single.html` keyed by `type:` in the content front-matter:

- `/ueber-mich/`, `/faq/`, `/impressum/`, `/datenschutz/` (originals)
- `/referenzen/` (Phase 3, type `referenzen`)
- `/eu-ai-act/` (Phase 3 Authority-Pillar, type `eu-ai-act`)
- `/journal/` + `/journal/<slug>/` (Phase 3 Blog, layouts under `layouts/journal/`)
- `/ki-fuer-<branche>/` (Phase 3 Programmatic, type `branche`, data in `data/branchen.yaml`)

**Brand-Voice-Guard:** `AGENTS.md` ist kanonisch für alle KI-Assistenten, die Texte schreiben. Bei Konflikt: AGENTS.md > sonstiges.

No content collections, no taxonomies. Single-author, single-language (de-AT). Voice: **Sie-Form** (B2B KI-Beratung).

## Sprachregelung (wichtig)

- **In Texten für die Website (alles in `content/`, `data/`, sichtbare Strings): konsequent Sie-Form**, B2B-Zielgruppe „Martina". Brand Voice in `AGENTS.md` ist kanonisch.
- **Im Chat mit Leonie selbst: Du-Form, Deutsch.** Sie ist die Site-Inhaberin, kennt KI als Anwenderin, aber ist keine Entwicklerin. Erklär kurz was du vorhast, frag bei größeren Sachen nach, halte Commits klein und sprechend.

FAQ accordion + category filter (`Alle / KI-Strategie / Kosten / EU AI Act & DSGVO / Tools & Technik / Zusammenarbeit`) live in `layouts/faq/single.html` + `partials/scripts.html`.

Schema.org JSON-LD `@graph` in `partials/schema.html`: Person + Organization + Service + FAQPage + AggregateRating + Reviews + BreadcrumbList + AboutPage + ContactPage + WebSite + Speakable. AI/GEO file at `static/llms.txt`; AI bots explicitly allowed in `static/robots.txt`.

## Brand tokens (mirror `params.toml`)

| Token | Value | Use |
|---|---|---|
| `--lk-teal-900` | `#086584` | Primary, buttons, links |
| `--lk-teal-600` | `#5FA2A0` | Secondary, gradients, hover |
| `--lk-teal-50` | `#EDF7F2` | Soft section background |
| `--lk-teal-100` | `#E7F4F4` | Highlights |
| `--lk-gold` | `#CF982B` | Labels |
| `--lk-gold-soft` | `#F1C50E` | Sparse highlights |
| `--lk-violet` | `#6B2C8C` | Eyebrows, secondary CTA |
| `--lk-violet-soft` | `#EFE6F6` | Pill background |
| `--lk-violet-line` | `#D9C5E8` | Pill border |
| `--lk-beige` | `#FAF0E9` | Page background |
| `--lk-ink` | `#1d2228` | Body text |
| `--lk-mute` | `#5b6572` | Secondary text |
| `--lk-line` | `#ece3d8` | Borders, separators |

Fonts: **Cabinet Grotesk** (display, self-hosted) + **Satoshi** (UI, self-hosted) — DSGVO-konform, no Google Fonts.

## Commands

Run from repo root:

```bash
hugo server --source src/growthtogether.at -D       # dev server with drafts
hugo --source src/growthtogether.at --minify        # production build
```

## Working patterns — MANDATORY

### Stepwise execution (always enforced)

Every session follows [`hugo-stepwise-execution`](.claude/skills/hugo-plan/references/hugo-stepwise-execution.md):

1. Restate understanding of the request and plan **before** any action.
2. Small sequential patches — max 3–5 file changes per burst.
3. After each burst, **report what landed on disk** before proposing the next step.
4. Only do what was explicitly asked — no speculative work.
5. Discovered drift → report as next step, never silently expand the current one.
6. Broken file → fix it first before combining with broader cleanup.

### hugo-plan — use when scope is unclear or wide

Invoke `/hugo-plan` when a request touches 3+ files across concerns, needs design before coding, or the user asks "how should we approach…". Plan is signed off before implementation starts.

### hugo-learn — use after sessions

Invoke `/hugo-learn` after significant work to capture learnings (`reflect`, `update docs`, `sync context`) and keep `docs/` current.

## Repository conventions

- **Branch-Strategie: direkt auf `main` pushen.** Kein Feature-Branch, kein PR — außer Leonie sagt explizit etwas anderes.
- **Never `git add -A` / `git add .` / `git add --all` / `git add *`** — always specify files explicitly.
- **Never deploy without explicit go-ahead** — live site is a paying client (Leonie Kaiser, leoniekaiser.com).
- **Live domain:** `leoniekaiser.com` (not just a vanity URL — actual live host. Source dir intentionally still named src/growthtogether.at; do not rename).
- **Image pipeline first:** all source images in `assets/images/`. The `partials/picture.html` partial generates WebP + responsive srcset at build time. Avoid pre-rendered pairs in `static/`.
- **Single CSS file:** `assets/css/brand.css` is the only stylesheet. Auto-fingerprinted + SRI in prod via `partials/head.html`.
- **JSON-LD via `dict` + `jsonify`:** never string templates. See `partials/seo-jsonld.html`.
- **Single-language:** de-AT only. No i18n setup needed unless the client explicitly asks.

## Related projects

- `aeshilion/superleague-hugo` — the reference repository this site mirrors. Look there first for pattern questions.
- `kobra-knowledge/alexander/working-method.md` — captured Alexander conventions.
- `kobra-knowledge/alexander/leonie-current-state.md` — Phase 0 recon notes.

## Knowledge capture — proaktiv schreiben

Bei substanziellen Erkenntnissen **selbst commiten + pushen**, kurz melden. Drei Ziele:

- **Diese CLAUDE.md / `docs/`** → Hugo-Patterns, Brand-Token-Updates, KAS-rsync-Quirks, self-hosted-Fonts-Lessons, partials/picture.html-Edge-Cases.
- **`kobra-knowledge/alexander/`** (`working-method.md`, `leonie-current-state.md`) → Alexander-Reviews, übernommene/abgelehnte Patterns mit Mail-Datum, Phase-Übergänge.
- **`eap-knowledge`** → Pricing/Hugo-Setup-Erfahrung wenn projektübergreifend relevant (Vergleich SuperLeague vs Leonie).

Trigger: Hugo-Bug der >30min gefressen hat, Alexander-Mail mit Pattern-Empfehlung, Branding-Update von Leonie, KAS-Deploy-Issue. Nicht: CSS-Tweaks, Tippfehler.

## Notes-Repo: `../leonie-knowledge/`

Neben diesem Site-Repo liegt ein zweites Repo `leonie-knowledge` (GitHub:
`leonie23kaiser/leonie-knowledge`). Das ist Leonies persönliches Notiz- und
Wissens-Archiv — kein Code, nur Markdown.

Struktur:
- `notes/raw/YYYY-MM-DD-slug.md` → Roh-Einwürfe (Claude schreibt hier rein)
- `notes/wiki/` → kondensiertes Wissen (entsteht durch „compile wiki")
- `CLAUDE.md` im Notes-Repo erklärt Format + DSGVO-Regeln

**Wann ins Notes-Repo schreiben:**
- Strategische Überlegung zu Positionierung, Zielgruppe, Pricing
- Beobachtung aus Kundengesprächen, die sich auf andere Kunden übertragen lässt
- Gelerntes Pattern (Tool, Technik, Workflow) das über dieses Projekt hinaus
  nützlich ist
- Recherche-Ergebnis, das Leonie später wieder brauchen wird

**Wann NICHT:**
- Site-spezifische Tech-Lessons → die gehören in diese `CLAUDE.md`
- Kundennamen, Klardaten, sensible Infos → DSGVO-Regel im Notes-Repo lesen
- Tagesgeschäft-Kram, Tippfehler-Fixes

**Workflow:**
1. Markdown nach `../leonie-knowledge/notes/raw/<datum>-<slug>.md` schreiben
2. Header: `# Titel`, `**Captured:** <Datum>`, `**Tags:** [...]`
3. `cd ../leonie-knowledge && git add notes/raw/<file> && git commit -m "raw: <slug>" && git push`
4. Kurz an Leonie melden: „hab eine Notiz zu X angelegt, compile wiki bei
   Gelegenheit"

**Lesen / Suchen:**
```
grep -ri "<Begriff>" ../leonie-knowledge/notes/
```

**Compile bleibt manuell** — Leonie sagt „compile wiki", dann verdichtet Claude
die raw-Files in `notes/wiki/`. Niemals direkt in `wiki/` schreiben.
