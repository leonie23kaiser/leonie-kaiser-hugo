# Für Alexander

Hi Alexander,

kurzes Briefing zu diesem zweiten Repo. SuperLeague-hugo ist der Haupt-Case – dieses hier (Leonie Kaiser) ist ein **zweites Hugo-Projekt mit dem gleichen Stack**, um zu sehen, ob das Muster skaliert. Du musst hier nicht viel reviewen, aber ein Blick wäre wertvoll.

## Kontext

- **Kundin:** Leonie Kaiser, Gedächtnistraining + Leben mit Demenz.
- **Status:** **Phase 1, Gerüst steht, Inhalte fehlen.** Alle Body-Texte sind explizite `TODO`-Platzhalter. Leonie schreibt ihre eigenen Inhalte, die kommen später drauf.
- **Referenz-Struktur:** memominds.de (hab ich mit Leonies OK gescrapt). **Nur** Navigation, Headings, Kategorien wurden übernommen – kein Body-Text. Scrape-Daten liegen unter `_legacy/scrape/`, raw HTMLs sind gitignored (Copyright).

## Warum das Repo Sinn macht für dich

Gleiche Patterns wie SuperLeague, anderer Use-Case: **Content-/Blog-Site statt Sport-Portal**. Das zeigt dass die Alexander-Blueprint-Patterns portabel sind.

## Was identisch zu SuperLeague ist

- `config/_default/{config,params,menus}.toml` split
- `assets/css/brand.css` mit fingerprint+minify+SRI
- `layouts/partials/picture.html` (responsive WebP)
- `layouts/partials/seo-jsonld.html` (dict+jsonify, aber hier `Person` + `Article` statt Sport-Org)
- `layouts/partials/head.html` (full OG/Twitter, RSS discovery, theme-color)
- 404, robots.txt, favicon.svg/ico, og-default

## Was anders ist

- **Content-Typ:** Blog mit 9 Post-Stubs, 6 Kategorien (Lebensqualität, Gedächtnistraining, Pflege und Angehörige, Vorsorge und Prävention, Demenz verstehen, Aktives Altern).
- **Design:** warm/wellness statt combat – Salbei `#6A8D73` + Terrakotta `#D4A373` + Creme `#F5F1E8`, Lora Serif + Inter.
- **Alle Posts sind `draft: true`**, weil Platzhalter.

## Struktur

```
leonie-kaiser-hugo/
├── _legacy/scrape/           # memominds.de scrape-tooling (nur Struktur)
│   ├── README.md             # copyright-notes
│   ├── extract.py            # html → structure.json
│   ├── generate-stubs.py     # structure.json → TODO-markdown-stubs
│   └── raw/                  # gitignored
├── config/_default/          # split wie integrations.at
├── content/
│   ├── blog/                 # 9 Post-Stubs, draft: true
│   ├── geistige-fitness/
│   ├── leben-mit-demenz/
│   ├── ressourcen/           # 9 Sub-Pages (Spiele, Übungen, Ratgeber, Apps…)
│   └── ueber-mich.md | impressum.md | ...
├── data/hero.json
├── assets/                   # identisch-patterned zu SuperLeague
├── static/
└── layouts/                  # identisch-patterned
```

## Dev-Setup

```bash
git clone https://github.com/aeshilion/leonie-kaiser-hugo.git
cd leonie-kaiser-hugo
hugo server -D                # -D wichtig, sonst siehst du nix (alles draft)
# → http://localhost:1313
```

## Wo deine Meinung helfen würde

1. **"draft: true" als Default – ok oder anti-Pattern?** Alternative wäre `unlisted` o.ä. Ich wollte verhindern, dass versehentlich Platzhalter-Text live geht.
2. **Blog-Categories als Hugo-Taxonomy:** aktuell `categories` + `tags` (Hugo-Standard). Bei deinem Blog-Setup hattest du glaube ich was Eigenes?
3. **Warum nicht Astro/Next:** weil wir bei SuperLeague schon Hugo haben und Emanuel nur einen Stack pflegen will. Vernünftig oder würdest du anders entscheiden?

## Wichtig bei Urheberrecht

Das Repo enthält **keine** memominds-Texte. Alle Headings sind `##` Platzhalter, alle Descriptions sind TODO. `_legacy/scrape/raw/` ist gitignored. Vor Go-Live ersetzt Leonie alle Paragraphen durch ihre eigenen Worte.

## Kontakt

Emanuel Althuber – emanuel@artforyoung.com.
