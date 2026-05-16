# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Project

Hugo static-site for **Leonie Kaiser — KI & Business Consulting** (live: growthtogether.at).

- Hugo project root: `src/growthtogether.at/`
- Live deployment: **GitHub Pages** (`.github/workflows/deploy-pages.yml`) on the **growthtogether.at** custom domain via `static/CNAME`. After client sign-off the DNS is moved to **leoniekaiser.com**.
- **Full documentation: [docs/readme.md](docs/readme.md)** and **[ONBOARDING.md](ONBOARDING.md)** for Leonie's local Claude-Code workflow.

Hugo **v0.123+ extended** required.

## Site shape

Single-page marketing site with anchor-based navigation. The page builder is `layouts/_default/home.html`, today rendering content from `content/_index.md` front-matter and inline markup (data-driven `site.yaml` refactor deferred — old version kept as `.bak-simply-ai`). Plus four standalone pages: `/ueber-mich/`, `/faq/`, `/impressum/`, `/datenschutz/` — each backed by `layouts/<slug>/single.html` keyed by `type:` in the content front-matter.

No content collections, no taxonomies. Single-author, single-language (de-AT). Voice: **Sie-Form** (B2B KI-Beratung).

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

- **Never `git add -A` / `git add .` / `git add --all` / `git add *`** — always specify files explicitly.
- **Never deploy without explicit go-ahead** — live site is a paying client (Leonie Kaiser, growthtogether.at).
- **Live domain:** `growthtogether.at` (not `leoniekaiser.com` despite the brand name).
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
