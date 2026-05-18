# Leonie Kaiser — Hugo Site Documentation

Hugo static-site for **Leonie Kaiser — KI & Business Consulting** (live: leoniekaiser.com).  
Hugo root: `src/growthtogether.at/`.

## Contents

| Document | What it covers |
|---|---|
| [Architecture](architecture.md) | Project layout, tech stack, build pipeline, deploy path |
| [Configuration](config.md) | `config.toml`, `params.toml`, `menus.toml` |
| [Content Model](content-model.md) | `data/site.yaml` section schemas + content pages |
| [Layouts & Templates](layouts-templates.md) | `home.html` page builder, partials, shortcodes |
| [Assets & Styles](assets-styles.md) | `brand.css`, image pipeline, `picture.html` partial |
| [SEO & JSON-LD](seo-jsonld.md) | Meta tags, OG/Twitter cards, structured data |
| [Content Workflow](content-workflow.md) | How to edit hero, services, swap images |
| [Deploy](deploy.md) | Current rsync-to-KAS + planned Azure SWA migration |
| [ALEXANDER.md](ALEXANDER.md) | Original briefing notes (kept for context) |

## Quick start

```bash
hugo server --source src/growthtogether.at -D    # dev server with drafts → http://localhost:1313
hugo --source src/growthtogether.at --minify     # production build → src/growthtogether.at/public/
```

Requires Hugo **v0.123+ extended** (WebP + asset pipeline).

## Site shape

Single-page marketing site. Anchor-based navigation. The page builder is `layouts/_default/home.html` reading from `data/site.yaml`. Plus two legal pages: `/impressum/` and `/datenschutz/`.

No content collections, no taxonomies. Single-author, single-language (de-AT).

## Reference repository

This site mirrors the patterns from [`aeshilion/superleague-hugo`](https://github.com/aeshilion/superleague-hugo). Look there first for pattern questions. Local sibling: `../superleague-hugo/`.

Alexander's working conventions are captured in `kobra-knowledge/alexander/working-method.md`.
