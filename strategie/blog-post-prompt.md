# Blog-Post-Schreib-Prompt (Journal, leoniekaiser.com)

*Wiederverwendbarer Prompt, um einen einzelnen Journal-Beitrag als Draft auszuarbeiten.
Aufruf: einfach die Post-Nummer nennen (z. B. „Schreib Blogpost #4 nach diesem Prompt").
Claude holt sich Titel, Keyword, Kategorie und Outline selbst aus den Konzept-Dateien.*

---

## SCHRITT 0 — Post identifizieren (nur die Nummer nötig)

Eingabe ist nur eine **Nummer N**. Ermittle selbst aus dem Repo:
1. Öffne `strategie/blog-konzept.md`, Abschnitt 8 (Redaktionsplan-Tabelle). Nimm aus der
   Zeile **#N**: Working Title, Primär-Keyword, Intent, Kategorie (· Segment), interne Links.
2. Öffne `strategie/blog-einzelkonzepte.md` und suche das **ausgearbeitete Einzelkonzept
   zu #N** (Eckdaten, Content-Gap, H1/H2/H3-Outline, Meta, Bild-Ideen).

> **BREMSE (nicht verhandelbar):** Existiert zu #N **kein ausgearbeitetes Einzelkonzept**
> in `blog-einzelkonzepte.md`, dann **STOPP** — kurz melden „Für #N gibt es noch kein
> Einzelkonzept, soll ich es zuerst ausarbeiten?" und **nicht** eigenmächtig eine Outline
> erfinden. Hintergrund: Laut Plan werden zuerst #1–#3 gelauncht; #4 ff. werden erst
> nachträglich einzeln ausgearbeitet. Nur mit vorliegendem Einzelkonzept weiterschreiben.

Fehlt eine der Quell-Dateien oder ist ein Wert unklar → nachfragen, nicht raten.

## SCHRITT 1 — Kontext aus dem Repo lesen (Pflicht, vor dem Schreiben)

**Vorab:**
- **Branch:** Auf `claude/seo-blog-concept-m5v60r` arbeiten — dort liegen alle Konzepte,
  `service-katalog.md` und `linkedin-profil.md` (noch nicht auf `main`).
- **Hugo-Projektwurzel ist `src/growthtogether.at/`** — alle Layout-/Content-/Data-Pfade
  mit diesem Prefix lesen.

Lies vollständig:
- `AGENTS.md` — kanonische Brand Voice, **bindend** (Ton, Gendern, Blacklist, „nicht
  abwertend über andere / kein Panik-Vibe", CTA-Grundsatz, SEO-Disziplin).
- `strategie/blog-konzept.md` — Gesamtstrategie: Zielgruppe „Martina, 47", Buyer-Journey,
  Kategorien, Ehrlichkeits-Regel, Artikel-Aufbau & Länge nach Beitragsart.
- `strategie/blog-einzelkonzepte.md` — das Einzelkonzept zu **genau diesem Post**: das ist
  dein **inhaltliches Skelett** (Keyword, Content-Gap, Outline, interne Links, Bild-Ideen),
  keine Vorlage zum Umformulieren.
- `strategie/service-katalog.md` — Rohmaterial für Beispiele/Szenarien (falls im
  Einzelkonzept ein Beispielszenario vorgesehen ist).
- `strategie/linkedin-profil.md` — E-E-A-T-Fakten. **Nur wörtlich belegte Angaben**
  verwenden, nichts dazuerfinden. (Leonie war im Marketing/Projekten in regulierten
  Konzernen — **kein** klinischer Patientendaten-Bezug.)
- `src/growthtogether.at/data/branchen.yaml` — falls der Post ein Segment-Label trägt
  (z. B. Physiotherapie).
- `src/growthtogether.at/layouts/journal/single.html` — technischer Rahmen: was
  **automatisch** kommt (Kopfbereich mit Kategorie/Titel/Meta, CTA-Box am Ende, Tags,
  „Mehr aus dem Journal") und was du im Markdown-Body selbst baust.

**Ton-Referenz:** Es gibt (Stand jetzt) **noch keine veröffentlichten Journal-Posts** —
Post #1 ist der erste. Nutze als Stimmen-Referenz `src/growthtogether.at/content/ueber-mich.md`
und die Use-Case-/FAQ-Texte in `data/branchen.yaml` (dort steckt Leonies Stimme schon drin).
Sobald echte Posts existieren, zusätzlich 1–2 davon lesen.

## SCHRITT 2 — Keyword kurz gegenchecken

Vor dem Volltext das Primär-Keyword aus dem Einzelkonzept gedanklich gegen eine reale
Google-Suche prüfen (Autocomplete-Logik, „Ähnliche Fragen"). Fällt dir eine konkretere
oder natürlichere Formulierung auf → **vorschlagen** statt stillschweigend zu übernehmen
oder zu verwerfen.

## SCHRITT 3 — Struktur des Beitrags (Vorgabe)

- **Einstieg:** 2–3 Sätze, die den Schmerz/Wunsch der Leserin aufgreifen, gern mit O-Ton.
- **Fließtext mit H2/H3 laut Einzelkonzept-Outline.** Alle 2–3 Absätze ein optisches
  Element (Hervorhebungs-/Callout-Box, Liste, Zwischen-Bild-Vorschlag), damit kein
  „wall of text" entsteht.
- **Beispielszenario-Box** nur, wenn im Einzelkonzept vorgesehen — explizit als
  *illustrativ* kennzeichnen (kein realer Kundenfall).
- **FAQ-Block** am Ende, 3–5 Fragen, kurz und direkt (SEO/GEO). **Aber:** Wenn das
  Einzelkonzept den FAQ-Block als *optional* markiert (z. B. beim persönlichen Post),
  dann nur einbauen, wenn er echt hilft — sonst weglassen.
- **Kein eigener CTA-Text** — die CTA-Box kommt automatisch aus dem Layout. Du lieferst
  nur das **Framing im Schlussabsatz**, das zur Potenzialanalyse hinführt (konkretes,
  branchenspezifisches Ergebnis) — **NIE** „kostenlos, kein Verkaufsgespräch".
- **Am Ende zwei Bild-Ideen** (Motiv + Stimmung + Suchbegriffe für die Bilddatenbank) für
  Hero- und Zwischenbild — keine Bilder selbst erzeugen/verlinken. Falls das Einzelkonzept
  schon Bild-Ideen enthält, diese aufgreifen/verfeinern.

**Front Matter** nach dem Schema aus `blog-konzept.md` (Abschnitt 7):
`title`, `description` (140–160 Zeichen), `date`, `lastmod`, `author: "Leonie Kaiser"`,
`category` (eine der 6 Kategorien, aus Schritt 0), `readingTime` (aus Wortzahl ≈ 200
Wörter/min), `tags`, `draft: true`.
- **Titel-Tag ≤ 60 Zeichen** (AGENTS.md §13). Ist der Working Title länger (evokativ), zwei
  Optionen: (a) langen, sprechenden Titel behalten (Google kürzt in der SERP — für
  persönliche/Marken-Posts ok), oder (b) ein kürzeres `title` + die volle Phrase als erste
  Zeile/H1 im Body. Im Zweifel Option (a), aber bewusst entscheiden und kurz vermerken.

## SCHRITT 4 — Ehrlichkeits-Regel (nicht verhandelbar)

Keine erfundenen Fallzahlen, Sterne, Referenzen oder Kundenstimmen. Prozentzahlen aus
fremden Quellen nur mit Quellenangabe. Genau ein CTA-Framing pro Post, kein Newsletter.
Nicht abwertend über Wettbewerb (AGENTS.md) — sachlich sagen, was Leonie *zusätzlich* bietet.

## SCHRITT 5 — Wie es NICHT klingen darf

Der Text muss lesen, als hätte Leonie ihn selbst zwischen zwei Terminen runtergeschrieben —
nicht wie ein generierter Ratgeberartikel. Konkret vermeiden:
- Textbaustein-Einstiege wie „In der heutigen schnelllebigen Welt …", „Stellen Sie sich vor …".
- Symmetrische Dreier-Aufzählungen und Floskeln wie „spielt eine entscheidende Rolle",
  „ist von zentraler Bedeutung".
- Weichspüler-Konjunktionen im Übermaß: „zudem", „darüber hinaus", „nicht zuletzt" als
  Standard-Übergang zwischen jedem Absatz.
- Künstliche Ausgewogenheit („einerseits … andererseits") ohne echten Standpunkt.
- Ein Fazit-Absatz, der die Einleitung zusammenfasst („Zusammenfassend lässt sich sagen …").
- Gleichförmige Satz- und Absatzlängen — stattdessen Rhythmus variieren, auch mal ein
  kurzer Satz.
- Hedging wie „Es ist wichtig zu beachten, dass …" statt einer klaren Aussage.
- Generische Beispiele — stattdessen konkret aus `service-katalog.md` / dem Einzelkonzept.

Stattdessen: konkrete Praxisalltag-Details, klare Haltung („KI nicht um jeden Preis — erst
die Prozesse, dann das Werkzeug"), Sie-Anrede, aktive Verben statt Substantivketten,
gelegentlich direkte Ansprache der Leserin statt neutraler Beschreibung.

## SCHRITT 6 — Output

1. **Draft-Datei anlegen:** `src/growthtogether.at/content/journal/<slug>.md`
   (Slug aus der URL im Einzelkonzept, z. B. `no-shows-physiotherapie-senken`). Vollständiger
   Markdown-Body **inkl. Front Matter**, `draft: true`. `date` auf einen **Dienstag** setzen
   (Launch-/Veröffentlichungs-Takt).
2. **Bauen zur Kontrolle:** `hugo --source src/growthtogether.at -D` — muss fehlerfrei
   durchlaufen (Draft rendert mit `-D`). Bei Fehlern fixen.
3. **Nicht deployen, nicht nach `main` mergen** — Draft bleibt auf dem Branch, Leonie
   sichtet. Commit klein und sprechend.
4. **Kurz-Report** am Ende: welche internen Links (laut Einzelkonzept) gesetzt wurden und
   welche noch nicht (z. B. Zielseite existiert nicht); getroffene Titel-Entscheidung
   (Option a/b); die zwei Bild-Ideen; offene Punkte für Leonies Sichtung.
