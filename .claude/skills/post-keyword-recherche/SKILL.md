---
name: post-keyword-recherche
description: >
  Begleitet Leonies Keyword-Recherche für einen einzelnen Blogpost, wenn sie eine
  "Seed-Begriffe für Post #N"-Liste (oder ein Report-Template mit Google Keyword
  Planner / AnswerThePublic / Google Trends / Google direkt-Abschnitten) aus ihrem
  separaten "Blog & Posts"-Thread hier einfügt. Nutze diesen Skill IMMER, wenn Leonie
  Seed-Keywords für einen Blogpost postet, einen "Keyword-Check" für einen Post
  verlangt, Screenshots/CSVs von Google Keyword Planner, Google Trends oder Google-
  Suche zu Praxis-/Gesundheits-Keywords teilt, oder fragt, was sie als Nächstes für
  die Keyword-Recherche eines Posts tun soll — auch wenn sie den Skill-Namen nicht
  nennt. Deckt den vollständigen Ablauf ab: Recherche-Checkliste ausgeben, echte
  Ergebnisse gegen die Zielgruppe aus AGENTS.md/segmente.md auf Intent-Fehlpassung
  prüfen, Report-Template ausfüllen, Ergebnisse in strategie/keyword-research-*.md
  festhalten und committen, und eine copy-paste-fertige Zusammenfassung für den
  Blog-Thread liefern.
---

# Post-Keyword-Recherche

Ein einzelner, wiederkehrender Workflow: Leonies „Blog & Posts"-Thread plant Blogartikel
und gibt ihr pro Post ein paar Seed-Keywords plus ein Report-Template mit. Sie bringt das
hierher, weil dieser Thread (du) weder Google Ads noch Google Trends noch Google selbst
live bedienen kann — das sind Leonies eigene Browser-Recherchen. Deine Aufgabe ist nicht,
diese Daten zu erfinden, sondern den Ablauf zu führen und das, was sie zurückbringt,
kritisch auszuwerten.

## Warum das mehr ist als Copy-Paste

Der wertvollste Teil dieses Skills ist nicht das Ausfüllen des Formulars — das ist der
Intent-Check (siehe unten). In der bisherigen Recherche (Post #1) stellte sich mehrfach
heraus, dass ein Keyword mit echtem Suchvolumen trotzdem falsch war, weil die Leute, die
danach suchen, gar nicht Leonies Zielgruppe sind. Das ist die Falle, die dieser Skill jedes
Mal aktiv umgehen soll — nicht nur Zahlen berichten, sondern beurteilen, wer wirklich sucht.

## Ablauf

### 1. Seeds bestätigen und Checkliste ausgeben

Wenn Leonie Seeds für Post #N postet, bestätige kurz, worum es geht (Post-Thema, falls aus
`Blog_Posts_13.docx` oder einem ähnlichen Redaktionsplan im Repo ersichtlich), dann gib ihr
die vier Schritte, die sie selbst durchführen muss:

- **① Google Keyword Planner** — `ads.google.com`, Tools → Planung → Keyword-Planer →
  „Neue Keywords entdecken". Standort AT (bei Bedarf zusätzlich DE), Sprache Deutsch.
  Volumen + Wettbewerb je Keyword.
- **② AnswerThePublic** — ihr Testabo ist ausgelaufen; die Gratis-Version zeigt nur noch
  einen Domain-Abdeckungs-Check (Status/Referenzseite), keine echten Fragen/Volumen mehr.
  Behandle das als Bestätigung „Content-Lücke ja/nein", nicht als Recherche-Quelle.
- **③ Google Trends** — `trends.google.com`, die Seeds gegeneinander vergleichen, 12 Monate,
  Region AT (bei Bedarf DE). Richtung + „Verwandte Suchanfragen" notieren.
- **④ Google direkt** — Inkognito-Fenster, Region AT. Pro Begriff: Autocomplete, „Ähnliche
  Fragen", „Ähnliche Suchanfragen" ganz unten. **Das ist der wichtigste Schritt** — hier
  zeigt sich die echte Suchintention, nicht nur ob überhaupt gesucht wird.

Warte, bis sie Ergebnisse bringt — als CSV, Screenshot oder Text. Wenn sie ankündigt, dass
mehr Screenshots folgen ("warte, ich schick dir noch..."), warte tatsächlich, bevor du
auswertest, statt mit Teilergebnissen loszulegen.

### 2. Intent-Check — für jedes Keyword einzeln

Bevor du irgendein Keyword als „gut" empfiehlst, prüfe: **Wer sucht das wirklich, laut den
„Ähnliche Fragen"/"Ähnliche Suchanfragen" aus Schritt ④?** Nicht nur, ob Volumen da ist.

Lies dazu `AGENTS.md` (Abschnitt 1: Zielgruppe + Anti-Zielgruppe; Abschnitt 9: Wort-
Blacklist) und `strategie/segmente.md` (Anker-Kriterien, explizite Ausschlüsse,
Segment-Landkarte) — nicht nur einmal überfliegen, sondern bei jedem neuen Keyword-Batch
wieder gegenprüfen, weil die Muster sich wiederholen. Bereits gefundene Fallen, zur
Orientierung (nicht abschließend — bei jedem neuen Begriff neu denken):

- „Praxismanagerin"/„Praxismanagement" hatten starkes Volumen, aber die Ähnliche-Fragen
  drehten sich um Gehalt, Stellenangebote, Ausbildung, IHK — das ist die Suche von
  Jobsuchenden/Auszubildenden, nicht von Praxisinhaberinnen.
- „Praxissoftware" zeigte reale Nachfrage, aber nach konkreten Konkurrenzprodukten
  (Tomedo, Medatixx, MEDISTAR) zum Kaufen/Vergleichen — nicht nach Beratung, und es würde
  Leonie in die Rolle eines Software-Vergleichsportals drängen, was ihrer „tool-agnostisch"-
  Positionierung in `AGENTS.md` widerspricht.
- „Potenzialanalyse" allein (ohne „KI-") ist im deutschen Sprachraum stark von Schul-/
  Personalauswahl-Assessments besetzt (Potenzialanalyse Schule, 8. Klasse, Arbeitsagentur).

Der Skill hat seinen Wert dadurch, dass er dieses Muster bei **jedem** neuen Post aktiv
sucht, nicht nur bei den bereits bekannten Fällen. Frage dich bei jedem Begriff: Klingen die
„Ähnliche Fragen" nach einer inhabergeführten Gesundheits-/Wellness-Praxis mit sensiblen
Patientendaten (Anker-Kriterien in `segmente.md`) — oder nach etwas anderem (Job, Software-
Kauf, Ausbildung, ein anderes Berufsfeld, Konsument:innen statt B2B)?

Verdikt pro Keyword: **passt** / **passt teilweise** / **passt nicht** — mit einer kurzen
Begründung aus den echten „Ähnliche Fragen"-Daten, die Leonie geliefert hat.

### 3. Nie Daten erfinden

Wenn Leonie ein Feld nicht beliefert hat (z. B. AnswerThePublic übersprungen, Google direkt
für 2 von 6 Begriffen fehlt), schreib ehrlich „kein Volumen" / „nicht durchgeführt" /
„keine Daten geliefert" — nie eine plausible Zahl raten. Falls du zusätzliche Content-Ideen
brauchst, weil eine Recherche-Quelle fehlt, darfst du mit `WebSearch` echte, aktuelle
Suchergebnisse zum Thema holen — aber kennzeichne das immer klar als „aus echter Websuche,
kein AnswerThePublic-/Trends-Export" (siehe Beispiel bei Post #1 im Repo), damit Leonie nie
denkt, das sei eine der vier offiziellen Quellen.

### 4. Report-Template ausfüllen

Leonies Templates variieren leicht zwischen Posts (mal die lange Checkliste mit
nummerierten Schritten, mal das kurze „Keyword-Check Post #N — Seeds: ..."-Format). Füll
genau das Format, das sie mitgeschickt hat, mit den echten Werten aus Schritt 1–3 — ergänzt
um den Intent-Check-Satz je Keyword-Gruppe.

### 5. Ins Repo schreiben

Suche zuerst nach vorhandenen `strategie/keyword-research-*.md`-Dateien im Repo und ergänze
die neueste um einen neuen datierten Abschnitt (`## Post #N: <Thema> (<Datum>)`) — leg nur
dann eine neue Datei an, wenn wirklich keine existiert. Orientiere dich an der bestehenden
Struktur der Datei (H2-Abschnitte, Tabellen für Intent-Match-Übersichten, ein
„Finale Keyword-Entscheidung"-Absatz am Ende jedes Post-Abschnitts).

Dann: `git add <genau diese eine Datei>` (nie `git add -A`/`-A`/`.`), committen mit einer
kurzen, sprechenden Nachricht, direkt auf `main` pushen (Leonies Repo-Konvention laut
`CLAUDE.md`: kein Feature-Branch, kein PR, außer sie sagt explizit etwas anderes). Melde ihr
kurz, was committet/gepusht wurde.

### 6. Zusammenfassung für den Blog-Thread

Am Ende: ein sauberer, copy-paste-fertiger Block im selben Format wie Leonies eigenes
Template, plus das empfohlene finale Keyword-Set für diesen Post und eine Ein-Satz-
Begründung, die sich auf `AGENTS.md`/`segmente.md` bezieht (nicht nur „hat Volumen"). Genau
das gibt sie im anderen Thread wieder ein.

## Ton

Chat mit Leonie ist immer **Du-Form, Deutsch** (nicht die Sie-Form, die für Website-Texte
gilt) — sie ist die Site-Inhaberin, keine Entwicklerin. Kurz und konkret, wie im Rest dieses
Threads: Befund zuerst, dann Empfehlung, dann nächster Schritt.
