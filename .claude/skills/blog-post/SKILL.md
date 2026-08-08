---
name: blog-post
description: >-
  Geführter, mehrstufiger Ablauf für einen neuen Blogpost auf leoniekaiser.com — vom
  Redaktionsplan über Keyword-Check, Headline-Auswahl und Outline-Freigabe bis zum fertigen
  Text (inkl. Word-Doc zum Korrekturlesen), Bildvorgaben und Hugo-Build-Check. Jeder Schritt
  wartet auf Leonies Freigabe, bevor der nächste beginnt. Use when: "nächsten Blogpost
  schreiben", "Post #<N> starten", "blog post erstellen", "weiter im Redaktionsplan", oder
  wenn ein Blogpost-Text fehlt/überarbeitet werden soll.
---

# blog-post — Geführter Blogpost-Workflow

Orchestriert die Erstellung eines einzelnen Journal-Beitrags für leoniekaiser.com in klaren,
einzeln freizugebenden Schritten. Dieser Skill schreibt keine eigenen Brand-Voice-Regeln —
er verweist auf die bestehenden Quelldateien, damit es **eine Wahrheit pro Thema** bleibt
(nicht duplizieren, wenn sich dort etwas ändert, gilt es hier automatisch mit).

**Quelldateien (immer zuerst lesen, in dieser Reihenfolge):**
1. `AGENTS.md` — Brand-Voice-Guard, kanonisch. Bei Konflikt gewinnt diese Datei.
2. `strategie/blog-konzept.md` — Redaktionsplan (18 Themen, Kategorien, Reihenfolge).
3. `strategie/blog-einzelkonzepte.md` — Einzelkonzept des jeweiligen Posts (Keyword-Vorschlag,
   Outline-Skizze, Bild-Ideen), falls für die Post-Nummer schon vorhanden.
4. `strategie/blog-konventionen.md` — Session-Learnings: verbotene Wörter/Phrasen, Struktur,
   Front-Matter-Schema, Artikel-Typografie.
5. `strategie/keyword-check.md` — Anleitung für den Keyword-Check (Tools, Ablauf, Report-Format).
6. `strategie/blog-post-prompt.md` — der ursprüngliche 2-Phasen-Schreibprompt (Ehrlichkeits-
   Regel, „Wie es NICHT klingen darf", Output-Schritte). Dieser Skill folgt seiner Struktur.

**Nicht verhandelbar, aus allen bisherigen Runden gelernt:**
- Kein übertriebener Experten-/Erfahrungsanspruch, keine pauschalen Abwertungen, keine
  Personifizierung von Institutionen, keine Verkaufsrhetorik-Phrasen, „verpflichten"
  vermeiden (auch verneint), „tool-agnostisch" nur intern — siehe `AGENTS.md` §9.
- **„Tool" ist die richtige Wortwahl für Software**, nicht „Werkzeug" (`AGENTS.md` §9,
  2026-08-Korrektur).
- Zahlen/Zitate nur mit echter, **ursprünglicher** Quelle — bei Sekundärquellen (z. B.
  Fachmagazin, das einen Report zusammenfasst) ehrlich als solche kennzeichnen, nicht dem
  Primärbericht zuschreiben, wenn er es nicht wörtlich sagt.

---

## Ablauf (jeder Schritt wartet auf Leonies Antwort, bevor der nächste beginnt)

### Schritt 1 — Redaktionsplan & Thema bestätigen
- `strategie/blog-konzept.md`, Abschnitt „Die ersten 18 Beiträge" öffnen.
- Wenn Leonie eine Post-Nummer nennt: Titel, Kategorie, Primär-Keyword-Vorschlag und
  Hub-Link aus der Tabelle zusammenfassen und **kurz bestätigen lassen**, bevor es weitergeht
  (Themen können sich seit dem letzten Blick verschoben haben — siehe Merge-Historie).
- Wenn keine Nummer genannt wird: den nächsten offenen Post in Reihenfolge vorschlagen.
- Prüfen, ob unter `strategie/blog-einzelkonzepte.md` schon ein Einzelkonzept für diesen Post
  existiert — falls ja, dessen Keyword-Vorschlag und Bild-Ideen als Ausgangspunkt nehmen.

### Schritt 2 — Keyword-Check anstoßen
- 4–6 **Seed-Begriffe** zum Thema vorschlagen (aus dem Redaktionsplan-Keyword abgeleitet).
- Das Report-Template aus `strategie/keyword-check.md` ausgeben (Kurzform ab dem zweiten Mal,
  volle Anleitung nur, wenn Leonie explizit danach fragt oder es ihr erstes Mal ist).
- **Stopp. Auf Leonies Testergebnisse warten** — nicht selbst weiterschreiben.

### Schritt 3 — 3 Headline-Vorschläge
- Erst nachdem die Keyword-Ergebnisse da sind: Primär-Keyword + Long-Tail auswählen und
  **3 Headline-Varianten** vorschlagen (Keyword natürlich integriert, ≤ 60 Zeichen wo möglich).
- Auf Leonies Auswahl/Feedback warten.

### Schritt 4 — Outline zeigen
- H2/H3-Gliederung passend zum gewählten Titel und Einzelkonzept skizzieren (keine
  Fließtext-Passagen, nur Struktur + 1 Stichwort pro Abschnitt).
- **Stopp. Auf Feedback warten**, bevor der Volltext entsteht — Struktur-Änderungen sind vor
  dem Schreiben billiger als danach.

### Schritt 5 — Volltext schreiben
- Nach `strategie/blog-post-prompt.md` (Struktur, Länge nach Beitragsart, Ehrlichkeits-Regel,
  „Wie es NICHT klingen darf") und `AGENTS.md` (Brand Voice, Wort-Blacklist).
- Front-Matter komplett gemäß Schema in `blog-konventionen.md` §5 (`slug` **immer** explizit,
  `description` 140–160 Zeichen **die das Thema transportiert, nicht nur „wer bin ich"**,
  `draft: true`).
- FAQ-Block nur wenn er echten SEO/GEO-Wert hat (bei stark persönlichen Posts optional).

### Schritt 6 — Text + Kurzzusammenfassung + Word-Doc gemeinsam liefern
- **Immer alle drei zusammen ausgeben:** den vollständigen Beitragstext, die `description`
  (die Kurzzusammenfassung, die auf der Seite oberhalb des Titelbilds erscheint — sichtbar im
  Chat, nicht nur im Front-Matter versteckt) **und** das Word-Doc zum Korrekturlesen.
  (Leonie, 2026-08.)
- **Word-Doc-Export gehört hierher, nicht ans Ende:** Zweck ist Korrekturlesen des Texts, das
  passiert direkt bei der Textabgabe, nicht erst nach Bildern/Build-Check. Über den
  bestehenden `md2docx.js`-Konverter (Pfad im Scratchpad der Session) in ein .docx wandeln —
  Front-Matter/HTML-Kommentare vorher entfernen, H1 + Kurzzusammenfassung oben einfügen. Vor
  dem Versand per `zipfile`/Textsuche prüfen, dass kein Absatz beim Konvertieren verloren
  ging. Bei späteren Text-Überarbeitungsrunden (nach Feedback) das Doc erneut mitliefern, wenn
  sich der Text spürbar geändert hat. (Leonie, 2026-08 — Korrektur: ursprünglich war das
  Schritt 8, ergibt aber nur beim Textentstehen Sinn.)

### Schritt 7 — Bildvorgaben (erst jetzt, nach dem Text)
- Bewusst **nach** dem fertigen Text, nicht davor — Bildideen müssen zum tatsächlichen Winkel
  passen, der sich durch Leonies Feedback in Schritt 4/5 noch verschoben haben kann.
- **Hero + optional 1 Zwischenbild** vorschlagen (Motiv, Stimmung, Suchbegriffe — siehe
  Vorlage in `blog-einzelkonzepte.md`, Abschnitt „Bild-Ideen"). Leonie sucht/liefert das
  passende Foto; danach `cover`/`coverAlt`/`coverCredit` im Front-Matter ergänzen.
- ALT-Texte und (falls Stockfoto/KI-generiert) Bildunterschrift mit Quelle liefern — bei
  KI-generierten Bildern als „© KI-generiert mit ‹Tool›, ‹Jahr›" (siehe
  `assets/images/blog/CREDITS.md`).
- Mobile Kartenansicht (`/blog/`-Übersicht) und Post-Seite jeweils per Screenshot prüfen,
  sobald ein echtes Bild vorliegt.

### Schritt 8 — Build-Check
- `hugo --source src/growthtogether.at -D --buildFuture --minify --quiet` — muss fehlerfrei
  durchlaufen. Prüfen: Post rendert unter `/blog/<slug>/`, Titel/Überschriften/interne
  Links/CTA-Box vorhanden, Cover korrekt (falls gesetzt).
- Bei Zweifeln an Layout/Abstand: kurz mit Playwright-Screenshot verifizieren, nicht raten.

### Schritt 9 — Übergabe
- **Nicht deployen, nicht nach `main` mergen** ohne Leonies ausdrückliches Go — Draft bleibt
  auf dem Branch (`draft: true`), sie sichtet zuerst.
- Kurz-Report: gesetzte/offene interne Links, Titel-/Slug-Entscheidung, Build-Ergebnis, Datei-
  pfad, offene Punkte.
- Erst wenn Leonie „live schalten"/„deployen" sagt: `draft: false`, committen, nach `main`
  pushen — das löst automatisch Build + Deploy + die HITL-Notify-GitHub-Issue aus
  (`.github/workflows/deploy-pages.yml`, Job `notify`). Vor dem Push nach `main` immer erst
  `git fetch origin main` und bei Abweichungen mergen (Konflikte einzeln mit Leonie klären,
  nicht automatisch auflösen, wenn beide Seiten inhaltlich widersprechen).

---

## Wann diesen Ablauf NICHT von vorn durchlaufen

- **Reines Feedback zu einem bestehenden Post** (Formulierung, Struktur, Bild) → direkt die
  betroffene Stelle ändern, nicht wieder bei Schritt 1 anfangen.
- **Nur der Redaktionsplan soll sich ändern** (Reihenfolge, neue Themen) → das ist
  `blog-konzept.md` direkt bearbeiten, kein Blogpost-Ablauf.
