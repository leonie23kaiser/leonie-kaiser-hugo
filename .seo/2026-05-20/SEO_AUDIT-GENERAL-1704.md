# SEO Audit – Leonie Kaiser (leoniekaiser.com)
**Typ:** GENERAL  
**Datum:** 2026-05-20  
**Zeit:** 17:04  
**Methode:** Codebase-Inspektion (Hugo-Templates, Front Matter, Schema, Konfiguration)  
**Baseline:** Keine (erster Audit dieser Serie)

---

## Gesamt-Score

| Dimension | Score | Trend |
|---|---|---|
| Crawlability & Indexation | 6/10 | – |
| Technische Grundlagen | 7/10 | – |
| Schema-Abdeckung | 8/10 | – |
| On-Page SEO | 7/10 | – |
| Content-Qualität & interne Verlinkung | 3/10 | – |
| Authority & Trust Signals | 6/10 | – |
| **Gesamt** | **6/10** | – |

---

## 1. Crawlability & Indexation

### ❌ KRITISCH: Doppeltes robots.txt – statische Datei überschreibt Template

`config.toml` hat `enableRobotsTXT = true` und `layouts/robots.txt` ist als Template angelegt (mit `absURL` für Sitemap, mehr Bot-Regeln). Gleichzeitig liegt `static/robots.txt` im Repo. In Hugo gilt: `static/`-Dateien überschreiben generierte Ausgaben **immer**. Das Ergebnis: Das Template in `layouts/robots.txt` wird nie ausgeliefert.

Die aktive `static/robots.txt` fehlen:
- `User-agent: ChatGPT-User` (im Template vorhanden)
- `User-agent: Bingbot` (im Template vorhanden)
- `User-agent: OAI-SearchBot` (im Template vorhanden)
- `Allow: /llms.txt` (explizite Freigabe für AI-Scraper)

**Fix:** `static/robots.txt` löschen, `enableRobotsTXT = true` bleibt → Hugo generiert aus `layouts/robots.txt`.

### ❌ KRITISCH: Alle Journal-Artikel sind `draft: true`

7 Journal-Beiträge, alle mit `draft: true`. Ohne `hugo -D`-Flag sind diese in der Produktion unsichtbar: nicht indexiert, nicht in der Sitemap, generieren keinen organischen Traffic.  
Ältester Entwurf: `wo-fange-ich-mit-ki-an.md` (2026-05-18). Mindestens dieser sollte sofort veröffentlicht werden.

### ⚠️ llms.txt veraltet und unvollständig

`static/llms.txt` listet weder die Journal-URLs noch die `/ki-fuer-*/`-Seiten. Letztes Update: 2026-05-16. Da die Datei statisch ist und nicht aus Hugo-Daten generiert wird, muss sie manuell gepflegt werden.  
Fehlende Einträge:
- Journal-Index: `https://leoniekaiser.com/journal/`
- Branche-Seiten (4x ki-fuer-*)
- EU AI Act: `https://leoniekaiser.com/eu-ai-act/`

### ✅ Gut: Sitemap

Sitemap via Hugo generiert (`sitemap.xml`), in robots.txt korrekt referenziert. Priority- und Changefreq-Werte auf Seitenebene gepflegt (EU AI Act: 0.85, Journal: 0.8, Branchen: 0.75).

---

## 2. Technische Grundlagen

### ❌ Hero-Bild mit `loading="lazy"` – LCP-Killer

In `layouts/_default/home.html:22`:
```html
<img src="/images/Bild-1.png" alt="Leonie Kaiser" loading="lazy">
```
Das Hero-Bild ist das LCP-Element (Largest Contentful Paint). `loading="lazy"` verzögert den Ladevorgang und verschlechtert den LCP-Score direkt. Muss auf `loading="eager" fetchpriority="high"` geändert werden.

Gleiches gilt für `Bild-2.png` in der Über-mich-Sektion (above the fold auf vielen Viewports), ebenfalls `loading="lazy"`.

### ⚠️ Favicon: Unvollständige Implementierung

`partials/head.html` referenziert nur:
```html
<link rel="icon" href="/images/Logo.png" type="image/png">
```
Im `static/`-Root liegen aber: `favicon.ico`, `favicon.svg`, `apple-touch-icon.png` – diese werden nicht verlinkt. Browser-kompatible Favicon-Kette fehlt:
- `<link rel="icon" href="/favicon.svg" type="image/svg+xml">`
- `<link rel="shortcut icon" href="/favicon.ico">`
- `<link rel="apple-touch-icon" href="/apple-touch-icon.png">`

### ⚠️ Font-Preload unvollständig

Nur 2 von 5 Fonts werden vorgeladen:
```html
<link rel="preload" href="/fonts/satoshi-400.woff2" ...>
<link rel="preload" href="/fonts/cabinet-grotesk-800.woff2" ...>
```
Fehlend: `satoshi-500.woff2`, `satoshi-700.woff2`, `cabinet-grotesk-700.woff2`  
Konsequenz: FOUT (Flash of Unstyled Text) bei fettgedruckten/mittleren Texten.

### ⚠️ Bilder: PNG statt WebP in Templates

`home.html` referenziert `.png`-Dateien direkt (`Bild-1.png`, `Bild-2.png`, `Angela-Caine.png`, etc.), obwohl `.webp`-Pendants in `static/images/` vorhanden sind. Das `partials/picture.html`-Partial mit responsivem `srcset` wird im Home-Template nicht verwendet.

### ✅ Gut: Canonical, OG, Twitter Card

Canonical-Tag in `head.html` korrekt via `.Permalink`. Vollständige OG-Implementierung (og:locale=de_AT, og:image, og:image:width/height). Twitter Card `summary_large_image`. `og-default.png` in `static/images/` vorhanden.

### ✅ Gut: CSS-Fingerprinting + SRI

`brand.css` wird in Produktion minifiziert, fingerprinted und mit SRI-Hash ausgeliefert – korrekte Performance-Basis.

### ✅ Gut: Hugo-Konfiguration

`enableGitInfo = true` (lastmod aus Git), Minify aktiviert, Imaging-Pipeline konfiguriert (Lanczos, quality 82).

---

## 3. Schema-Abdeckung

### ⚠️ Person.url zeigt auf Site-Root statt /ueber-mich/

In `partials/schema.html`:
```go
"url" $base
```
Für die Person sollte `"url"` auf die Über-mich-Seite zeigen, nicht auf die Homepage. Richtig wäre:
```go
"url" (printf "%sueber-mich/" $base)
```

### ⚠️ ContactPage fehlt (laut CLAUDE.md vorgesehen)

CLAUDE.md listet `ContactPage` als Teil des `@graph`. Die Implementierung in `schema.html` fehlt. Google nutzt ContactPage-Markup für Knowledge-Panel-Daten.

### ⚠️ AggregateRating: Nur 3 Bewertungen

`ratingCount: 3` ist der absolute Mindestwert für Google-Darstellung. Sobald mehr Referenzen vorliegen, sollte dieser Wert erhöht werden.

### ⚠️ Organization.logo verweist auf .png

```go
"logo" (printf "%simages/Logo.png" $base)
```
Google empfiehlt für das Organisations-Logo ein Bild mit 1:1-Verhältnis und mindestens 112×112px. Die `.webp`-Version wäre bevorzugt; alternativ sicherstellen, dass `Logo.png` diese Anforderungen erfüllt.

### ✅ Gut: Breite Schema-Abdeckung

Person + ProfessionalService + WebSite + FAQPage (auf FAQ- und EU-AI-Act-Seite) + AboutPage + Article (Journal) + BreadcrumbList + Speakable + WebPage – sehr solide Basis.

### ✅ Gut: Structured Data via dict + jsonify

Kein String-Template-Missbrauch. Sauber implementiert, kein Syntaxfehler-Risiko.

---

## 4. On-Page SEO

### ⚠️ Meta-Description Homepage zu lang

```
KI-Beraterin in Wien: maßgeschneiderte KI-Strategie, No-Code-Automatisierung und EU AI Act Compliance für Einzelunternehmer und KMU in Österreich. Kostenfreie Potenzialanalyse.
```
**178 Zeichen** – Google kürzt bei ~155–160 Zeichen. Das Wort „Kostenfreie Potenzialanalyse" am Ende fällt weg. Empfehlung: auf ≤155 Zeichen kürzen.

### ⚠️ Über-mich-Meta-Description leicht zu lang

```
Leonie Kaiser, KI-Beraterin in Wien mit über 20 Jahren Erfahrung. Spezialisierung auf Agentic AI, Claude Code, EU AI Act & DSGVO Compliance für Einzelunternehmer und KMU.
```
**170 Zeichen** – ebenfalls über 155-Zeichen-Grenze.

### ⚠️ Title-Tag Homepage: 75 Zeichen (grenzwertig)

```
Leonie Kaiser | KI-Beratung Wien – Strategie, Automatisierung & EU AI Act
```
Google zeigt typischerweise bis ~60–65 Zeichen im Desktop-SERP an, bis ~78px Pixelbreite. Das `&`-Zeichen (1 px-Ersparnis) und Kürzung wäre empfehlenswert.

### ⚠️ Lokale Inkonsistenz: Wien vs. Felixdorf

Alle Marketing-Texte und Meta-Tags sagen „KI-Beraterin in Wien", die strukturierten Daten (schema.html, params.toml) nennen „Felixdorf, Niederösterreich". Für lokales SEO und Google Business sollte eine konsistente Hauptstadt (Wien oder Felixdorf/NÖ) verwendet werden.

### ✅ Gut: H1-Tags

Jede Seite hat genau einen H1. Home: „KI, die wirklich für Sie arbeitet." – klar, markenbezogen. Branche-Seiten: H1 aus front-matter `title`.

### ✅ Gut: Strukturierte Heading-Hierarchie

Home: H1 → H2 (Sektionen) → H3 (Karten/Schritte) – korrekte Hierarchie.

---

## 5. Content-Qualität & Interne Verlinkung

### ❌ KRITISCH: Null veröffentlichte Blog-Artikel

7 Artikel existieren, alle `draft: true`. Kein indexierbarer Long-Tail-Content, kein thematisches Cluster, kein internes Linking-Netz. Der Journal-Bereich generiert heute keinen SEO-Wert.

**Sofortmaßnahme:** `wo-fange-ich-mit-ki-an.md` (2026-05-18) fertigstellen und `draft: false` setzen.

### ⚠️ Branche-Seiten: Keine internen Links untereinander

`/ki-fuer-physiotherapie-praxen/` verlinkt nicht auf `/ki-fuer-psychotherapie-praxen/` oder `/ki-fuer-coaches/`, obwohl thematische Überlappung besteht. Auch kein Link auf den Journal-Bereich.

### ⚠️ Keine internen Links von Journal → Service-Seiten (und umgekehrt)

Journal-Artikel (sobald veröffentlicht) sollten auf `/faq/`, `/eu-ai-act/` und Branche-Seiten verlinken. Aktuell keine solche Struktur erkennbar.

### ⚠️ Fehlende Keyword-Cluster-Strategie sichtbar

Kein Pillar-Page-Konzept erkennbar. `/eu-ai-act/` könnte als Cluster-Hub für die 3 geplanten Compliance-Artikel funktionieren, ist aber nicht als solcher aufgebaut.

### ✅ Gut: Seitenanzahl und URL-Struktur

10+ indexierbare URLs mit sauberen, semantischen Slugs. Programmatische Branche-Seiten folgen `ki-fuer-*`-Muster.

---

## 6. Authority & Trust Signals

### ⚠️ Nur 1 externe Verlinkung (LinkedIn)

`sameAs` in Person-Schema zeigt nur auf LinkedIn. Keine Erwähnung auf Branchen-Verzeichnissen, Fachportalen oder Medien-Erwähnungen sichtbar.

### ⚠️ Zertifizierungs-Badge prominent, aber ohne Quellennachweis

Der „Certified Consultant"-Stempel ist auf der Homepage sichtbar, aber der Schema-Graph enthält keine `hasCredential`-Eigenschaft und keine Verlinkung auf die ausstellende Organisation.

### ✅ Gut: AI/GEO-Präsenz gut vorbereitet

llms.txt vorhanden, alle relevanten AI-Bots erlaubt, Speakable-Markup implementiert. Gute Basis für AI-Zitierbarkeit (ChatGPT, Perplexity, Claude).

### ✅ Gut: Datenschutz & Compliance-Signale

Impressum, Datenschutz, DSGVO-Checkbox im Formular, cookiefreie Fonts (selbst gehostet) – starke Vertrauenssignale für österreichische Zielgruppe.

---

## Priorisierter Backlog

### P0 – Sofort (diese Woche)

| # | Maßnahme | Datei(en) | Aufwand |
|---|---|---|---|
| 1 | `static/robots.txt` löschen → Hugo-Template wird aktiv | `static/robots.txt` | 5 Min |
| 2 | Hero-Bild: `loading="lazy"` → `loading="eager" fetchpriority="high"` | `layouts/_default/home.html:22` | 5 Min |
| 3 | Mind. 1 Journal-Artikel veröffentlichen (`draft: false`) | `content/journal/wo-fange-ich-mit-ki-an.md` | 30–60 Min |

### P1 – Diese Woche

| # | Maßnahme | Datei(en) | Aufwand |
|---|---|---|---|
| 4 | Vollständige Favicon-Kette in `head.html` eintragen | `layouts/partials/head.html` | 10 Min |
| 5 | Homepage Meta-Description auf ≤155 Zeichen kürzen | `content/_index.md` | 10 Min |
| 6 | Über-mich Meta-Description kürzen | `content/ueber-mich.md` | 10 Min |
| 7 | `Person.url` auf `/ueber-mich/` korrigieren | `layouts/partials/schema.html` | 5 Min |
| 8 | `ContactPage`-Schema ergänzen | `layouts/partials/schema.html` | 20 Min |
| 9 | Fehlende Font-Preloads ergänzen (satoshi-500, satoshi-700, cabinet-grotesk-700) | `layouts/partials/head.html` | 10 Min |

### P2 – Nächste 2 Wochen

| # | Maßnahme | Datei(en) | Aufwand |
|---|---|---|---|
| 10 | `llms.txt` um Journal- und Branche-URLs erweitern | `static/llms.txt` | 15 Min |
| 11 | Wien/Felixdorf-Inkonsistenz klären und schema.html/params.toml angleichen | `config/_default/params.toml`, `schema.html` | 20 Min |
| 12 | Home-Template: WebP-Bilder via `picture.html`-Partial einsetzen (Bild-1, Bild-2, Testimonials) | `layouts/_default/home.html` | 60 Min |
| 13 | Interne Links zwischen Branche-Seiten einfügen | `layouts/branche/single.html` | 30 Min |
| 14 | Alle verbleibenden Journal-Artikel finalisieren und veröffentlichen | `content/journal/*.md` | 2–4 h |

### P3 – Mittelfristig (30 Tage)

| # | Maßnahme | Aufwand |
|---|---|---|
| 15 | `hasCredential` in Person-Schema für Zertifizierung ergänzen | 15 Min |
| 16 | Title-Tag Homepage auf ≤65 Zeichen optimieren | 10 Min |
| 17 | Pillar-Page-Struktur aufbauen: EU AI Act als Hub + Journal-Artikel als Cluster | 4+ h |
| 18 | Google Search Console einrichten und Sitemap einreichen | 30 Min |
| 19 | Google Business Profile anlegen (Lokale Sichtbarkeit Wien/NÖ) | 45 Min |
| 20 | Externe Authority-Signale: Eintrag in AT-KI-Verzeichnisse, WKO-Expertenliste | 2+ h |

---

## Notizen zur Methode

- Kein Live-Runtime-Check (lokaler Dev-Server nicht gestartet) – Audit basiert auf Codebase-Inspektion
- Alle Journal-Artikel sind Drafts → Produktions-Sitemap wurde nicht inspiziert
- Core Web Vitals (LCP/INP/CLS) wurden nicht gemessen – separater Technical Audit empfohlen
