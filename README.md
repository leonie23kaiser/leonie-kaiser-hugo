# leonie-kaiser-hugo

Hugo-Seite für Leonie Kaiser. Geplanter Bereich: Gedächtnistraining, Leben mit Demenz, geistige Fitness im Alter.

## Status

**Phase 1: Gerüst steht, wartet auf Inhalte.** Alle Texte sind TODO-Platzhalter. Die Seitenstruktur ist inspiriert von memominds.de (siehe `_legacy/scrape/README.md`), Texte müssen aber von Leonie selbst kommen.

## Stack

- Hugo 0.123+ (extended) — `hugo server -D` für lokale Entwicklung
- Config split: `config/_default/{config,params,menus}.toml`
- Brand CSS: `assets/css/brand.css` (Salbei + Terrakotta, Lora + Inter)
- Resource-Pipeline für Bilder: `assets/images/` + Partial `layouts/partials/picture.html` (WebP + JPEG fallback, srcset)
- SEO: JSON-LD via `layouts/partials/seo-jsonld.html` (Person @graph auf Home, Article auf Blog), OG/Twitter-Tags, RSS discovery

Selbe Patterns wie SuperLeague-Site, nachgezogen aus Alexander Kastil's `hugo-cms-samples` (integrations.at).

## Inhalte

- Sections: `geistige-fitness`, `leben-mit-demenz`, `blog`, `ressourcen`
- Blog-Kategorien: Lebensqualität, Gedächtnistraining, Pflege und Angehörige, Vorsorge und Prävention, Demenz Verstehen, Aktives Altern
- 9 Blog-Post-Stubs (alle `draft: true`)
- Einzel-Ressourcen: Spiele, Alltagsübungen, Ratgeber, Digitale Helfer, Gehirnjogging, Alltagshilfen

## Urheberrecht / Content-Herkunft

Grundstruktur, Navigation und Headings basieren auf memominds.de als Referenz. **Kein** Body-Text wurde übernommen. Vor Go-Live müssen alle Paragraphen Leonies eigene Worte sein. Siehe `_legacy/scrape/README.md`.

## Entwicklung

```
hugo server -D
```

Geht auf http://localhost:1313.
