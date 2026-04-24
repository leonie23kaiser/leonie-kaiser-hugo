# memominds.de Scrape

**Zweck:** Struktur-Referenz für Leonies neue Seite. **NICHT** Text-Quelle.

- `sitemap_index.xml`, `post-sitemap.xml`, `page-sitemap.xml` — Sitemaps von memominds.de (Stand siehe `<lastmod>`).
- `pages.txt`, `posts.txt` — extrahierte URLs.
- `raw/*.html` — komplette Seiten-HTMLs (nur lokal, nicht deployen).
- `extract.py` — zieht Titel, Meta-Description, Headings, Kategorien, Tags in `structure.json`.
- `structure.json` — strukturierte Übersicht (29 Seiten, 9 Blog-Posts, 6 Kategorien).

## Was wir übernehmen (Urheberrecht)

- **Seiten-/Navigationsstruktur** (Home, Geistige Fitness, Leben mit Demenz, Blog, Ressourcen, Über mich).
- **Blog-Kategorien**: LEBENSQUALITÄT, GEDÄCHTNISTRAINING, PFLEGE UND ANGEHÖRIGE, VORSORGE UND PRÄVENTION, DEMENZ VERSTEHEN, AKTIVES ALTERN.
- **Ressourcen-Sub-Struktur**: Spiele, Alltagsübungen, Ratgeber, Digitale Helfer, Gehirnjogging, Alltagshilfen.
- **Headings-Schema** (H1 pro Artikel, H2-Abschnitte) als Platzhalter.

## Was wir NICHT übernehmen

- Copy-Text (Paragraphen-Inhalte). Die müssen von Leonie kommen — selbst verfasst oder mit eigener Stimme umgeschrieben.
- Bilder (urheberrechtlich geschützt; eigene Fotos / Stock-Fotos).
- Logo / Farbpalette / Fonts.

## Regenerieren

```
curl -sS https://memominds.de/sitemap_index.xml -o sitemap_index.xml
curl -sS https://memominds.de/post-sitemap.xml -o post-sitemap.xml
curl -sS https://memominds.de/page-sitemap.xml -o page-sitemap.xml
grep -oP '(?<=<loc>)[^<]+' post-sitemap.xml > posts.txt
grep -oP '(?<=<loc>)[^<]+' page-sitemap.xml > pages.txt
# dann raw-fetch + python3 extract.py
```
