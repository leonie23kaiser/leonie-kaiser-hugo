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
- **Länge nach Beitragsart:** Fachbeitrag 900–1.400 · tiefer Leitfaden 1.500–2.200 ·
  persönlicher Post 600–1.000 Wörter.
- **Build zur Kontrolle:** `hugo --source src/growthtogether.at -D -F` (extended,
  `--buildFuture` wegen Zukunftsdatum). Fehlt Hugo im Container → extended-Binary von
  GitHub-Releases laden. Der CI-Deploy hat Hugo ohnehin.
- **Nicht deployen, nicht nach `main` mergen.** Draft bleibt auf dem Branch; `public/` nicht
  committen (ignoriert).

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
