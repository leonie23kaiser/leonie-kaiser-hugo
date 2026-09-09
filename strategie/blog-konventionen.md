# Blog-Redaktions-Konventionen (Session-Learnings)

*Konsolidierte Vorgehensweisen, Do/Don't-Wörter und Struktur-Regeln für das Journal auf
leoniekaiser.com. Ergänzt die ausführlichen Dateien und fasst die Entscheidungen aus der
Session vom 2026-07 an einem Ort zusammen. Stand: 2026-07-28.*

**Verwandte Dateien:** `AGENTS.md` (kanonische Brand Voice) · `strategie/blog-konzept.md`
(Strategie, Kategorien, Redaktionsplan) · `strategie/blog-einzelkonzepte.md` (Einzelbriefings
#1–#3) · `strategie/blog-post-prompt.md` (Schreib-Ablauf) · `strategie/keyword-check.md`
(Keyword-Prüfung) · `strategie/service-katalog.md` · `strategie/linkedin-profil.md`.

---

## 1. Ablauf pro Blogpost (zwei Phasen)

> **Pflichtlektüre zuerst:** `strategie/keyword-research-2026-07.md` — bereits getrackte
> Keywords (234, Anhang A+B), reale Recherche + Warnung zu volumenstarken Begriffen an der
> falschen Zielgruppe. Neue Erkenntnisse dort ergänzen, keine neue Datei anlegen.

1. **„Bereite Blogpost #N vor"** → Phase 1: **Keyword-Check zuerst** (Claude liefert Seeds
   + qualitative SERP-Lesung; **Leonie misst das Volumen** in Google Keyword Planner,
   AnswerThePublic, Google Trends, Google-Autocomplete — siehe `keyword-check.md`).
2. Mit dem Keyword-Ergebnis: **3 Headline-Vorschläge** (Keyword steckt in der Headline),
   dann **STOPP**.
3. Leonie wählt Headline + gibt Anmerkungen → **Phase 2**: Volltext schreiben, Hugo-Build,
   Report. Details: `blog-post-prompt.md`.
4. **Bremse:** Gibt es zu #N kein ausgearbeitetes Einzelkonzept, erst nachfragen — keine
   Outline erfinden (nur #1–#3 sind ausgearbeitet).

## 2. Wörter & Phrasen, die zu vermeiden sind

### 2a. Begriffs-Entscheidungen dieser Session
| Nicht mehr | Stattdessen | Warum |
|---|---|---|
| „Wellness" (Gesundheits-/Wellness-Praxen) | „Gesundheitspraxen" / „Gesundheit & Wohlbefinden" | klingt nach Wohlfühl-/Massage-Salon |
| „Medical-Wellness" | „privatärztliche Gesundheitszentren" | dito, klarer Fachbegriff |
| „Recall" / „Reminder" | „Terminerinnerung" · „Wiedereinladung" / „Kundschaft zurückholen" | Zielgruppe kennt das Fachwort nicht |
| „Membership" (im Blog) | umschreiben (z. B. „Mitgliedschaft") oder weglassen | verwirrt die Leserin |
| „das brauchen Sie nicht" | „Wenn KI nicht die Lösung ist, sage ich Ihnen das" | freundlicher, gleiche Haltung |
| „einkippt" (Daten) | „ungeprüft in ein KI-Tool gelangen" | zu leger |
| „KI- und Prozessberatung" | „KI & Digitalisierung" | konsistent mit LinkedIn/Positionierung |
| „kennt KI vom Hörensagen" | „hat ChatGPT & Co. schon ausprobiert, weiß aber nicht, wie für die Praxis" | realistischer |
| „Ästhetik" als Start-Segment | nicht als Start-Seite (nur Blog/Einzelanfrage) | schwächt Gesundheitsdaten-Anker |

### 2b. Ton-Regeln (auch in AGENTS.md verankert)
- **Nicht abwertend über Wettbewerb.** Keine „Wunderzahlen"/„die machen es falsch"-Vergleiche,
  kein Von-oben-herab. Sachlich sagen, was Leonie *zusätzlich* bietet.
- **Kein Angst-/Panik-Vibe.** Datenschutz/EU AI Act ruhig und lösungsorientiert erklären,
  nie mit Drohkulisse („Panikmache").
- **CTA nie mit** „kostenlos, kein Verkaufsgespräch" bewerben — stattdessen ein konkretes,
  branchenspezifisches Ergebnis nennen.
- **Gendern:** neutrale Form + Paarform, **kein** Doppelpunkt/Sternchen („Kundschaft",
  „Team", „Praxisleitung", „Inhaberinnen und Inhaber").
- **Kein „Wien"** in SEO/Marketing → „Niederösterreich" / „Österreich/DACH".

### 2c. Anti-KI-Slop (klingt-generiert-Verbot)
Vermeiden: Baustein-Einstiege („In der heutigen schnelllebigen Welt …", „Stellen Sie sich
vor …") · symmetrische Dreier-Aufzählungen · Floskeln („spielt eine entscheidende Rolle",
„von zentraler Bedeutung") · Weichspüler-Übergänge im Übermaß („zudem", „darüber hinaus",
„nicht zuletzt") · künstliche Ausgewogenheit ohne Standpunkt · Zusammenfassungs-Fazit
(„Zusammenfassend …") · gleichförmige Satz-/Absatzlängen · Hedging („Es ist wichtig zu
beachten, dass …") · generische Beispiele. **Stattdessen:** konkreter Praxisalltag, klare
Haltung, Sie-Anrede, aktive Verben, Rhythmus variieren, gelegentlich direkte Ansprache.

**Ergänzung nach AI-Detection-Check Post #6 (Leonie, 2026-09):** Ein AI-Detection-Tool hat
ganze Absätze als „Strong/Moderate AI patterns" markiert. Betroffen waren vor allem zwei
Muster: (1) glatte Gegensatz-Sätze nach dem Schema „nicht X, sondern Y" / „dort ergänzen,
wo X, nicht dort ersetzen, wo Y" statt einer konkreten Situation; (2) Aufzählungen/
Schritt-Listen, bei denen jede Zeile exakt demselben Satzbau folgt („Tun Sie X, bevor/statt
Y"). Vor Abgabe gegenlesen: Kommt „nicht X, sondern Y" mehrfach im selben Abschnitt vor?
Lesen sich alle Punkte einer Liste syntaktisch identisch? Beides umformulieren — mit einer
einzelnen, konkreten Situation (eine Kundin, ein Montag, ein Beispiel-Tool) statt einer
abstrakten Regel, und mit unterschiedlichem Satzanfang je Listenpunkt. Details/Beispiele:
`AGENTS.md` §9.

**Nachtrag (Leonie, 2026-09):** Wortweises Umformulieren reicht oft nicht — der Detector
flaggt danach die nächste Stelle. Was tatsächlich half (Post #6, zweite Prüfrunde): eine
**durchgehende Beispiel-Szene** über mehrere Absätze ziehen statt pro Absatz ein neues
generisches Beispiel; in Listen **Satztyp mischen** (Imperativ, Aussagesatz, Zitat, kurzer
Satz — nicht jede Zeile im selben Muster); die Kontrast-Aussage einer Zwischenüberschrift
**nicht direkt danach im Fließtext wiederholen**; **keine zwei+ rhetorischen Fragen**
hintereinander. Details: `AGENTS.md` §9.

**Zweiter Nachtrag nach externem Lektorat (Leonie, 2026-09):** Kontrast-Sätze sind an
sich kein Problem — problematisch wird es erst, wenn ein Text durchgehend nach demselben
Schema Gegensatz → Verallgemeinerung → Schlussfolgerung läuft. Zusätzlich beachten: dieselbe
Beispiel-Szene nicht zwei-, dreimal in verschiedenen Abschnitten neu erzählen (ein starkes
Beispiel reicht, spätere Abschnitte bauen darauf auf); keine absoluten Verallgemeinerungen
(„merkt sofort", „fast immer", „meist von selbst" — stattdessen „wird meist schnell
sichtbar", „entsteht häufig, wenn …"); wiederkehrende Formeln („Das ist kein Grund …",
„Entscheidend ist …", „Genau an dieser Stelle …") nicht mehrfach im selben Text. Externes
Lektorat auch kritisch prüfen: Vorschläge, die der Zielgruppen-Sprache (Kundin/Kundschaft
statt Patientin, siehe `AGENTS.md` §1) oder dem Angst-Verbot (§9) widersprechen, **nicht**
übernehmen. Details: `AGENTS.md` §9.

**Dritter Nachtrag (Leonie, 2026-09):** Wenn derselbe Text mehrfach flaggt wird, liegt es
meist an einem **Makro-Muster pro Absatz** (abstrakte These → Beispiel → verallgemeinernder
Schluss-Satz), nicht mehr an einzelnen Wörtern. Konkret: keinen generalisierenden Schluss-Satz
an jeden Absatz hängen (auf dem konkreten Detail enden reicht); FAQ-Antworten mit der Handlung
beginnen, nicht mit einer Diagnose-These davor; Listenpunkte wirklich unterschiedlich bauen
(Länge, Beispiel ja/nein, Handlung vs. Konsequenz); konkrete, leicht „unrunde" Details (eine
Zahl, ein beiläufiger Nebensatz) statt glatter Kausalketten. Details: `AGENTS.md` §9.

**Vierter Nachtrag — Grundproblem (Leonie, 2026-09), nach fünf Prüfrunden am selben Text:**
Wortweises Umformulieren hat wiederholt nicht gereicht, weil der Fehler nicht in einzelnen
Wörtern lag, sondern in einer **Satzbau-Gewohnheit**: fast jeder Satz ist ein in sich
geschlossenes, sauber aufgelöstes Mini-Argument (Situation nennen, im selben/nächsten
Halbsatz tidy erklären). Jede Korrekturrunde hat neue Wörter in dieselbe Satzarchitektur
eingesetzt — deshalb flaggte dieselbe Stelle immer wieder neu. **Wichtig:** Ein
Grammarly-artiges Tool wird bei klarer, professionell strukturierter B2B-Sprache vermutlich
nie auf null gehen — genau diese Klarheit verlangt auch Abschnitt 4 der Brand Voice, und das
externe Lektorat riet ausdrücklich davon ab, den Text künstlich unperfekt zu machen. Flaggt
eine Stelle nach zwei Überarbeitungsrunden **am Satzbau** (nicht nur am Wortlaut) weiterhin,
ist das kein Signal für eine dritte Wortersatz-Runde, sondern ein Punkt, an dem Leonie aktiv
gefragt wird, wie weit Richtung „bewusst unperfekt" gegangen werden soll. Details: `AGENTS.md`
§9.

**Fünfter Nachtrag — fachliche Präzision statt AI-Detection (Leonie, 2026-09):** Ein
drittes, inhaltlich orientiertes Lektorat (kein AI-Detector) hat einen anderen Fehlertyp
gefunden: zu absolute Alleinursache-Aussagen („X, das war der ganze Grund"), eine
Formulierung, die implizit einen bestehenden Kanal komplett abschafft (Telefon-Terminvergabe
klang wie abgeschafft, obwohl nur die parallele Handübertragung gemeint war), ein
Rollen-Label, das nicht zur beschriebenen Aufgabe passte („Umsetzer" für reines
Selbst-Ausprobieren), und eine zu binär formulierte Datenschutz-Frage bei Gesundheitsdaten
(„passt das Tool, oder nicht?" statt eines Prüfauftrags). Vor Abgabe gegenlesen: Klingt eine
Aussage nach der einzigen Ursache für ein mehrursächliches Problem? Klingt ein Umsetzungsschritt
nach Abschaffung eines Kanals, den er nicht abschaffen soll? Passt ein Rollen-Label exakt zur
beschriebenen Aufgabe? Ist eine Datenschutz-Aussage bei Gesundheitsdaten ein echter Prüfauftrag
statt einer Ja/Nein-Frage? Details: `AGENTS.md` §9.

### 2d. Brand-Blacklist (AGENTS.md §9)
Superlative („die beste Lösung", „einzigartig", „revolutionär") · Hype („disruptiv",
„Gamechanger", „KI-Revolution") · Floskeln („state of the art") · Anglizismen („booken",
„nice", „cool") · Bürokratendeutsch („im Rahmen von", „zur Verfügung stellen") · Tech-Bro-Ton
· Tool-/Produktnamen in Kundentexten (tool-agnostisch bleiben).

## 3. Erwünschte Haltung & Kern-Sätze
- „KI nicht um jeden Preis — erst die Prozesse, dann das Werkzeug."
- „Datenschutz ist der Ausgangspunkt, nicht das Kleingedruckte."
- „Wenn KI nicht die Lösung ist, sage ich Ihnen das."
- Immer **Zeit-Gewinn zusammen mit Erlebnis-Gewinn** nennen (nicht nur Entlastung).
- **Pharma-Erfahrung** nur als Herkunft der Datenschutz-Sorgfalt (Marketing/Projekte in
  regulierten Konzernen — **kein** klinischer Patientendaten-Bezug, Leonie war im Marketing).

## 4. Struktur eines Beitrags
1. **Hero-Bild** (Marker im Body, Bild-Idee im Report).
2. **Einstieg:** 2–3 Sätze, Schmerz/Wunsch der Leserin, gern O-Ton.
3. **Fließtext H2/H3** laut Einzelkonzept; alle 2–3 Absätze ein optisches Element
   (Callout-Box als Blockzitat, Liste, Zwischenbild-Marker) — kein „wall of text".
   **Echten Mehrwert liefern, nicht nur Themen anreißen:** Wo es passt, konkrete
   Schritt-für-Schritt-Anleitungen statt nur abstrakter Prinzipien (nummerierte Liste,
   z. B. „Wie Sie anfangen"), und eine übersichtliche Box mit den wichtigsten Punkten,
   wenn ein Abschnitt eine Aufzählung von Kern-Elementen enthält (`.highlight-box` aus
   `brand.css`, siehe Post #4). Leser sollen am Ende mehr Antworten haben als Fragen,
   nicht umgekehrt. (Leonie, 2026-08.)
4. **Beispielszenario-Box** nur wenn vorgesehen, als *illustrativ* gekennzeichnet.
5. **FAQ** (3–5 Fragen) — beim persönlichen Post optional.
6. **Schluss:** CTA-Framing (die CTA-Box kommt automatisch aus dem Layout), branchen-
   spezifisches Ergebnis.
7. **Zwei Bild-Ideen** im Report (Motiv + Stimmung + Suchbegriffe).

**Bild-Ablauf:** Claude liefert Ideen → Leonie sucht Bilder in der Datenbank → Claude macht
ALT-Text, Bildunterschrift, sprechenden Dateinamen, Hashtags/Social. Motiv: echt, ruhig,
warm; keine Stock-Klischees (kein „Roboterhand tippt Hologramm").

## 5. Front Matter & Technik
```yaml
title: '…'            # bei Anführungszeichen: Single Quotes + deutsche „…“
slug: "kurz-mit-keyword"   # IMMER explizit (Permalink /blog/:slug/ — sonst URL aus Titel, mit Umlauten)
description: "…"      # 140–160 Zeichen, Sie-Form, ein Nutzen
date: 2026-08-04      # ein Dienstag (Publikations-Takt)
lastmod: 2026-08-04
author: "Leonie Kaiser"
category: "…"          # eine der 6 Kategorien (siehe §6)
readingTime: 4         # Wortzahl ÷ ~200
tags: ["…", "…"]
draft: true
```
- **Titel = H1 = `<title>`-Tag** (kein separates SEO-Feld). ≤ 60 Zeichen ideal; evokativ
  länger ist bei persönlichen/Marken-Posts ok (Google kürzt in der SERP).
- **Länge nach Beitragsart:** Fachbeitrag **1.300–1.800** · tiefer Leitfaden 1.500–2.200 ·
  persönlicher Post 600–1.000 Wörter. **Korrektur (Leonie, 2026-09):** Fachbeitrag-Spanne
  angehoben, war zu niedrig — mehrfach als zu kurz/oberflächlich zurückgemeldet, auch noch
  bei ~1.200 Wörtern. Wortzahl ist aber nur ein Signal, nicht das Ziel selbst: Tiefe zuerst
  (konkrete Beispiele, Gegenszenarien mitdenken, siehe §4), dann erst die Zahl prüfen.
- **Build zur Kontrolle:** `hugo --source src/growthtogether.at -D -F` (extended,
  `--buildFuture` wegen Zukunftsdatum). Fehlt Hugo im Container → extended-Binary von
  GitHub-Releases laden. Der CI-Deploy hat Hugo ohnehin.
- **Nicht deployen, nicht nach `main` mergen.** Draft bleibt auf dem Branch; `public/` nicht
  committen (ignoriert).

### Artikel-Typografie (CSS, einmal fixiert)
Der Artikeltext läuft durch `.page-content` (`layouts/journal/single.html`). Die Regeln dafür
stehen in `assets/css/brand.css`, Abschnitt „Journal/Article body typography" (Ende der Datei):
- **Überschriften-Abstand:** H2/H3 im Fließtext hatten ursprünglich **keinen** Abstand nach
  oben (globaler `margin:0`-Reset) — dadurch klebten sie am vorherigen Absatz. Jetzt: H2
  `margin-top: var(--s10)`, H3 `margin-top: var(--s8)`, erstes Element ohne Top-Abstand.
- **Überschriften-Größe:** H2 = `var(--lg)`, H3 = ein Stück kleiner (`clamp(1.05rem,1rem + .3vw,1.25rem)`).
  H2 war anfangs `var(--xl)` — praktisch so groß wie die H1 der Seite, kaum zu unterscheiden.
- **Blockzitat (`>` im Markdown):** bekommt jetzt Teal-Balken links, hellgrüner Hintergrund,
  kursiv — vorher unsichtbar (kein Rahmen, kein Abstand, sah wie normaler Text aus).
- **Links im Fließtext:** Teal (`--teal-d`), unterstrichen — vorher browser-default (schwarz/blau).
- **Bild im Fließtext, Text drumherum:** `<figure class="float-right">` bzw. `float-left`
  (Klassen in `brand.css`) — auf Mobile automatisch nicht mehr geflotet, sondern zentriert
  (`@media max-width:640px`). H2/H3 haben `clear:both`, damit eine Überschrift nie neben
  einem geflloteten Bild "klemmt".
- **Goldmark-Link-Bug (wichtig für Formulierungen):** Hugo/Goldmark fügt bei jedem
  Markdown-Link (`[Text](/url/)`) ein unsichtbares Newline direkt vor dem schließenden
  `</a>` ein. Folgt danach ein Leerzeichen + Wort, gleicht sich das aus (sieht normal aus).
  **Folgt aber direkt ein Satzzeichen ohne Leerzeichen** (z. B. `[DSGVO](/dsgvo/).`), rendert
  der Browser eine sichtbare Lücke vor dem Satzzeichen. **Workaround:** an solchen Stellen
  rohes HTML statt Markdown-Syntax verwenden — `<a href="/dsgvo/">DSGVO</a>.` (funktioniert,
  weil `markup.goldmark.renderer.unsafe = true` gesetzt ist). Betrifft potenziell jeden
  Blogpost, nicht nur diesen. (Leonie, 2026-08.)
- Bei neuen Journal-/Artikel-Layouts (z. B. später `/dsgvo/`, `/eu-ai-act/` falls die auch
  Markdown-Fließtext bekommen) prüfen, ob `.page-content` wiederverwendet werden kann, statt
  denselben Abstands-Bug erneut einzubauen.

## 6. Kategorien, Balance, Publikation
- **6 Kategorien** (an den Services): Termine & Anfragen · Dokumentation & Wissen ·
  Kundenbindung & Nachsorge · Sichtbarkeit · Datenschutz & EU AI Act · KI in der Praxis.
- **Segment** (z. B. Physiotherapie) = **Label im Titel**, keine eigene Kategorie.
- **Schmerz- und Wunsch-Themen etwa gleich oft** (nicht überwiegend Probleme). Datenschutz
  als durchgehende Vertrauens-Schiene.
- **Takt:** 1 Beitrag/Woche; Launch mit **#1–#3 gleichzeitig**; Veröffentlichung
  **Dienstagvormittag** (Deploy Di 08:00 UTC ≈ 09–10 AT).
- **HITL:** Neu live gegangene Posts erzeugen ein `journal-live`-Issue → Mail an Leonie.
  Kein stilles Auto-Publish.

## 7. SEO/GEO & Ehrlichkeit (Kurzform)
- **Long-Tail schlägt Kopf-Keyword.** Ein Primär-Keyword pro Post, natürlich in H1/H2/Text.
- **Interne Verlinkung:** jeder Post auf ≥ 1 Hub-Seite (Praxisseite / `/eu-ai-act/`) +
  1–2 Beiträge derselben Kategorie.
- **FAQ-Block** für AI Overviews; FAQPage-Schema als Ausbaustufe.
- **Ehrlichkeit (nicht verhandelbar):** kein Fake-Social-Proof, keine erfundenen Zahlen/
  Referenzen; Beispielszenarien als *illustrativ* kennzeichnen; fremde Prozentzahlen nur
  mit Quelle; genau **ein** CTA (Potenzialanalyse via Calendly), kein Newsletter.
