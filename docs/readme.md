# Leonie Kaiser — Hugo Site Documentation

Hugo static-site for **Leonie Kaiser — KI & Digitalisierung** (live: leoniekaiser.com).
Hugo root: `src/growthtogether.at/`.

## Contents

| Document | What it covers |
|---|---|
| [Architecture](architecture.md) | Project layout, tech stack, build pipeline, deploy path |
| [Configuration](config.md) | `config.toml`, `params.toml`, `menus.toml` (and what's actually still wired up) |
| [Content Model](content-model.md) | `content/` tree, `data/branchen.yaml`, blog post front matter, the FAQ dual-source trap |
| [Layouts & Templates](layouts-templates.md) | `home.html`, page-type layouts, partials, shortcodes |
| [Assets & Styles](assets-styles.md) | `brand.css`, image pipeline, `picture.html` partial |
| [SEO & JSON-LD](seo-jsonld.md) | Meta tags, OG/Twitter cards, `schema.html`'s `@graph` |
| [Content Workflow](content-workflow.md) | How to edit copy, swap images |
| [Deploy](deploy.md) | ⚠️ Stale — actual deploy is GitHub Pages, see the Deploy section below |
| [ALEXANDER.md](ALEXANDER.md) | Original briefing notes (kept for context) |

## Quick start

```bash
hugo server --source src/growthtogether.at -D    # dev server with drafts → http://localhost:1313
hugo --source src/growthtogether.at --minify     # production build → src/growthtogether.at/public/
```

Requires Hugo **v0.123+ extended** (WebP + asset pipeline).

## Site shape

Marketing site with an anchor-based homepage plus standalone pages — not a single-page site anymore. The homepage (`layouts/_default/home.html`) is hardcoded HTML, not driven by a data file; only `content/_index.md`'s front matter (title/description) feeds it. Standalone pages, keyed by `type:` in content front matter:

- `/ueber-mich/`, `/faq/`, `/impressum/`, `/datenschutz/`
- `/eu-ai-act/`, `/dsgvo/` — authority-pillar pages, each with front-matter-driven FAQ
- `/leistungen/` overview + four Leistungsbereich pages (`/leistungen/termine-und-anfragen/`, `/leistungen/dokumentation-und-wissen/`, `/leistungen/nachsorge-und-kundenbindung/`, `/leistungen/sichtbarkeit-und-inhalte/`), content sourced from `data/branchen.yaml`
- `/blog/` + `/blog/<slug>/` — journal/blog, live since August 2026

No content collections in the classic sense, no taxonomies (`disableKinds = ["taxonomy", "term"]`). Single-author, single-language (de-AT).

**Brand-Voice-Guard:** `AGENTS.md` (repo root) is canonical for all AI assistants writing copy. If anything here conflicts with `AGENTS.md`, `AGENTS.md` wins.

## Deploy

**Live deploy is GitHub Pages**, via `.github/workflows/deploy-pages.yml`, on the `leoniekaiser.com` custom domain (`static/CNAME`).

**[deploy.md](deploy.md) is stale and describes a different, no-longer-current setup** (Azure Static Web Apps + rsync-to-KAS fallback, growthtogether.at DNS) — that wasn't in scope for this pass to fix, but don't trust it for the actual deploy path. Go by `.github/workflows/deploy-pages.yml` and `static/CNAME` directly, or ask to have `deploy.md` brought current too.

## Reference repository

This site mirrors patterns from [`aeshilion/superleague-hugo`](https://github.com/aeshilion/superleague-hugo). Look there first for pattern questions.

Alexander's working conventions are captured in `kobra-knowledge/alexander/working-method.md`.
