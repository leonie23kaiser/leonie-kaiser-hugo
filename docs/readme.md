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
| [Content Workflow](content-workflow.md) | How to edit homepage/Leistungsbereich/blog copy, swap images, "who edits what" table |
| [Deploy](deploy.md) | GitHub Pages workflow, cron-published blog posts, HITL notify, pre/post-deploy checklist |
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

**Live deploy is GitHub Pages**, via `.github/workflows/deploy-pages.yml`, on the `leoniekaiser.com` custom domain (`static/CNAME`). Push to `main` touching `src/growthtogether.at/**` triggers it; a weekly cron also runs it to publish future-dated blog posts on schedule. Full detail, including the pre-deploy checklist and the HITL review issue for newly-live posts, in [deploy.md](deploy.md).

## Reference repository

This site mirrors patterns from [`aeshilion/superleague-hugo`](https://github.com/aeshilion/superleague-hugo). Look there first for pattern questions.

Alexander's working conventions are captured in `kobra-knowledge/alexander/working-method.md`.
