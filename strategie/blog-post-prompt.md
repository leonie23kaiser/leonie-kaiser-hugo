# Blog-Post-Schreib-Prompt (Journal, leoniekaiser.com)

*Wiederverwendbarer Prompt, um einen einzelnen Journal-Beitrag auszuarbeiten — in **zwei
Phasen**. Aufruf: „**Bereite Blogpost #N vor**". Claude macht dann erst die Vorbereitung
(Keyword-Check + 3 Titelvorschläge), meldet, was es von Leonie braucht, und **stoppt**.
Erst nach Leonies Rückmeldung folgt die Ausarbeitung.*

---

## Zwei-Phasen-Ablauf (wichtig)

- **Phase 1 — Vorbereitung** (Schritte 0–2): Post identifizieren, Keyword prüfen, 3 Titel
  vorschlagen → an Leonie übergeben, **STOPP**. Kein Volltext.
- **Phase 2 — Ausarbeitung** (Schritte 3–7): erst nach Leonies Rückmeldung (Titelwahl,
  Keyword-Ok, Anmerkungen) den vollständigen Draft schreiben, bauen, berichten.

So kann Leonie mit einem einzigen Satz starten („Bereite Blogpost #1 vor") und bekommt
zurück, was sie entscheiden muss, bevor geschrieben wird.

---

# PHASE 1 — VORBEREITUNG

## SCHRITT 0 — Post identifizieren (nur die Nummer nötig)

Eingabe ist nur eine **Nummer N**. Ermittle selbst:
1. `strategie/blog-konzept.md`, Abschnitt 8 (Redaktionsplan): Zeile **#N** → Working Title,
   Primär-Keyword, Intent, Kategorie (· Segment), interne Links.
2. `strategie/blog-einzelkonzepte.md`: das **ausgearbeitete Einzelkonzept zu #N**
   (Eckdaten, Content-Gap, H1/H2/H3-Outline, Meta, Bild-Ideen).

> **BREMSE (nicht verhandelbar):** Gibt es zu #N **kein ausgearbeitetes Einzelkonzept**,
> dann **STOPP** — melde „Für #N gibt es noch kein Einzelkonzept, soll ich es zuerst
> ausarbeiten?" und **erfinde keine Outline**. (Laut Plan sind zuerst #1–#3 dran; #4 ff.
> werden erst nachträglich einzeln ausgearbeitet.)

Fehlt eine Quelldatei oder ist ein Wert unklar → nachfragen, nicht raten.

## SCHRITT 1 — Minimal-Kontext für die Vorbereitung

Für Phase 1 genügt: die #N-Zeile aus `blog-konzept.md`, das Einzelkonzept #N, und
`AGENTS.md` §13 (SEO-Disziplin: Keyword zuerst, Title-Tag ≤ 60 Zeichen, eine H1).

## SCHRITT 2 — Keyword prüfen + 3 Titel vorschlagen

**Keyword-Check (so weit ohne Bezahl-Tools möglich):**
- Das Primär-Keyword aus dem Einzelkonzept per **Web-Suche** gegen die reale Google-Suche
  halten: Wer rankt (Software-Anbieter = inhaltliche Lücke, oder starke Fachartikel)?
  Welche verwandten Begriffe / „Ähnliche Fragen" tauchen auf? Ist die Suchintention
  informierend (Blog-tauglich)?
- Daraus eine kurze Einschätzung: Keyword so lassen, oder eine konkretere/natürlichere
  Formulierung vorschlagen (mit Begründung).
- **Grenze offen benennen:** Echte Suchvolumen-Zahlen brauchen ein Keyword-Tool (Google
  Keyword Planner o. Ä.). Leonie fragen, ob sie das Volumen noch prüfen will oder ob die
  qualitative Einschätzung reicht.

**3 Titelvorschläge** liefern, die auf dem (ggf. geschärften) Keyword aufbauen — bewusst
unterschiedlich:
- eine **evokative** Variante (starker Hook, darf > 60 Zeichen sein — Google kürzt in der
  SERP, für persönliche/Marken-Posts ok),
- eine **SEO-knappe** Variante (≤ 60 Zeichen, Keyword vorn, passt komplett in die SERP),
- eine **such-/nutzenorientierte** Variante (nah an der realen Suchphrase).
Zu jedem Titel: Zeichenzahl + welches Keyword er trägt. Eine Empfehlung aussprechen.
*(Hinweis: Im Layout ist `title` zugleich H1 **und** `<title>`-Tag — es gibt kein
separates SEO-Titel-Feld. Der gewählte Titel ist also beides.)*

## ÜBERGABE an Leonie (Ende Phase 1)

Melde kompakt: (a) Keyword-Einschätzung + ob Volumen-Check gewünscht, (b) die 3 Titel mit
Empfehlung, (c) sonstige Entscheidungen, die vor dem Schreiben helfen. Dann **STOPP** und
auf Leonies Rückmeldung warten. **Noch keinen Volltext schreiben.**

---

# PHASE 2 — AUSARBEITUNG (erst nach Leonies Rückmeldung)

## SCHRITT 3 — Vollen Kontext lesen

**Vorab:** Auf Branch `claude/seo-blog-concept-m5v60r` arbeiten (dort liegen Konzepte,
`service-katalog.md`, `linkedin-profil.md`). Hugo-Projektwurzel ist `src/growthtogether.at/`.

Lies vollständig:
- `AGENTS.md` — kanonische Brand Voice, **bindend** (Ton, Gendern, Blacklist, „nicht
  abwertend über andere / kein Panik-Vibe", CTA-Grundsatz).
- `strategie/blog-konzept.md` — Zielgruppe „Martina, 47", Kategorien, Ehrlichkeits-Regel,
  Aufbau & Länge nach Beitragsart.
- `strategie/blog-einzelkonzepte.md` — das Einzelkonzept zu #N = **inhaltliches Skelett**
  (keine Vorlage zum Umformulieren).
- `strategie/service-katalog.md` — Rohmaterial für Beispiele/Szenarien (falls vorgesehen).
- `strategie/linkedin-profil.md` — E-E-A-T-Fakten, **nur wörtlich Belegtes** (Leonie war im
  Marketing/Projekten in regulierten Konzernen — **kein** klinischer Patientendaten-Bezug).
- `src/growthtogether.at/data/branchen.yaml` — falls Segment-Label (z. B. Physiotherapie).
- `src/growthtogether.at/layouts/journal/single.html` — technischer Rahmen: Kopfbereich,
  **CTA-Box (automatisch)**, Tags, „Mehr aus dem Journal".

**Ton-Referenz:** Solange es noch keine veröffentlichten Journal-Posts gibt, nutze
`src/growthtogether.at/content/ueber-mich.md` und die Use-Case-/FAQ-Texte in
`data/branchen.yaml` (dort steckt Leonies Stimme). Später 1–2 echte Posts lesen.

## SCHRITT 4 — Struktur des Beitrags

- **Einstieg:** 2–3 Sätze, die den Schmerz/Wunsch der Leserin aufgreifen, gern mit O-Ton.
- **Fließtext mit H2/H3 laut Einzelkonzept-Outline.** Alle 2–3 Absätze ein optisches
  Element (Hervorhebungs-/Callout-Box als Blockzitat, Liste, Zwischen-Bild-Marker), damit
  kein „wall of text" entsteht.
- **Beispielszenario-Box** nur, wenn im Einzelkonzept vorgesehen — explizit als
  *illustrativ* kennzeichnen (kein realer Kundenfall).
- **FAQ-Block** am Ende, 3–5 Fragen (SEO/GEO). **Aber:** markiert das Einzelkonzept FAQ als
  *optional* (z. B. persönlicher Post), nur einbauen, wenn er echt hilft.
- **Kein eigener CTA-Text** — die CTA-Box kommt automatisch aus dem Layout. Nur das
  **Framing im Schlussabsatz** hinführen (konkretes, branchenspezifisches Ergebnis) — **NIE**
  „kostenlos, kein Verkaufsgespräch".
- **Bild-Marker** als HTML-Kommentare an den Stellen für Hero-/Zwischenbild; die eigentlichen
  Bild-Ideen kommen in den Report (keine Bilder erzeugen/verlinken).

**Front Matter** (Schema aus `blog-konzept.md` Abschnitt 7):
`title`, `slug`, `description` (140–160 Zeichen), `date`, `lastmod`, `author: "Leonie Kaiser"`,
`category` (eine der 6 Kategorien), `readingTime` (Wortzahl ÷ ~200), `tags`, `draft: true`.
- **`slug` IMMER explizit setzen** (z. B. `slug: "praxis-haengt-an-der-leitung"`). Grund:
  Der Permalink ist `/blog/:slug/` — ohne `slug`-Feld baut Hugo die URL aus dem Titel,
  inklusive Umlauten → hässliche, schlechte URL.
- **Titel-Wert = der in Phase 1 gewählte Titel.** Enthält er Anführungszeichen, den
  YAML-Wert in **Single Quotes** setzen und deutsche „…“ verwenden (sonst bricht das
  Front-Matter). `date` auf einen **Dienstag** (Veröffentlichungs-Takt).

## SCHRITT 5 — Ehrlichkeits-Regel (nicht verhandelbar)

Keine erfundenen Fallzahlen, Sterne, Referenzen, Kundenstimmen. Fremd-Prozentzahlen nur mit
Quelle. Genau ein CTA-Framing, kein Newsletter. Nicht abwertend über Wettbewerb — sachlich
sagen, was Leonie *zusätzlich* bietet.

## SCHRITT 6 — Wie es NICHT klingen darf

Der Text muss lesen, als hätte Leonie ihn zwischen zwei Terminen selbst geschrieben — nicht
wie ein generierter Ratgeber. Vermeiden:
- Baustein-Einstiege („In der heutigen schnelllebigen Welt …", „Stellen Sie sich vor …").
- Symmetrische Dreier-Aufzählungen; Floskeln („spielt eine entscheidende Rolle").
- Weichspüler-Übergänge im Übermaß („zudem", „darüber hinaus", „nicht zuletzt").
- Künstliche Ausgewogenheit („einerseits … andererseits") ohne Standpunkt.
- Zusammenfassungs-Fazit („Zusammenfassend lässt sich sagen …").
- Gleichförmige Satz-/Absatzlängen — Rhythmus variieren, auch mal ein kurzer Satz.
- Hedging („Es ist wichtig zu beachten, dass …") statt klarer Aussage.
- Generische Beispiele — stattdessen konkret aus `service-katalog.md` / Einzelkonzept.

Stattdessen: konkrete Praxisalltag-Details, klare Haltung („KI nicht um jeden Preis — erst
die Prozesse, dann das Werkzeug"), Sie-Anrede, aktive Verben, gelegentlich direkte Ansprache.

## SCHRITT 7 — Output

1. **Draft-Datei anlegen:** `src/growthtogether.at/content/journal/<slug>.md`, vollständiger
   Markdown-Body **inkl. Front Matter**, `draft: true`.
2. **Build zur Kontrolle:** `hugo --source src/growthtogether.at -D -F` (extended;
   `-F`/`--buildFuture` wegen des Zukunftsdatums). Muss fehlerfrei durchlaufen; prüfen, dass
   der Post unter `/blog/<slug>/` rendert, Titel/Überschriften/interne Links/CTA-Box da sind.
   *(Ist `hugo` im Container nicht installiert: extended-Binary von den GitHub-Releases laden
   und lokal ausführen. Der CI-Deploy hat Hugo ohnehin — der Live-Build funktioniert also
   unabhängig davon.)*
3. **Nicht deployen, nicht nach `main` mergen.** Draft bleibt auf dem Branch; Leonie sichtet.
   Commit klein und sprechend (die gebaute `public/`-Ausgabe nicht committen — ist ignoriert).
4. **Kurz-Report:** gesetzte/offene interne Links, Titel-/Slug-Entscheidung, Build-Ergebnis,
   die zwei Bild-Ideen, offene Punkte für Leonies Sichtung.
