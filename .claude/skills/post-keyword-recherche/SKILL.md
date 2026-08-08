---
name: post-keyword-recherche
description: >
  Nimmt Leonies "Keyword-Check Post #N"-Ergebnisse entgegen, wenn sie Seed-Begriffe und
  Recherche-Daten (Google Keyword Planner, AnswerThePublic, Google Trends, Google direkt)
  aus ihrem separaten "Blog & Posts"-Thread (dessen `blog-post`-Skill, Schritt 2) hier
  einfügt oder danach fragt, wie sie weitermachen soll. Nutze diesen Skill IMMER, wenn
  Leonie Seed-Keywords für einen Blogpost postet, Screenshots/CSVs von Google Keyword
  Planner/Trends/Google-Suche zu Praxis-/Gesundheits-Keywords teilt, oder fragt, was sie
  als Nächstes für die Keyword-Recherche eines Posts tun soll — auch ohne den Skill-Namen
  zu nennen. Führt den in `strategie/keyword-check.md` beschriebenen Zielgruppen-Intent-
  Check aus, hält die Entscheidung in `strategie/keyword-research-*.md` fest und liefert
  eine copy-paste-fertige Zusammenfassung zum Zurückgeben in den Blog-Thread.
---

# Post-Keyword-Recherche

Dieser Thread ist die Werkbank für den Keyword-Check, den der `blog-post`-Skill im
„Blog & Posts"-Thread bei jedem neuen Post anstößt (dort Schritt 2) und dann auf Leonies
Ergebnis wartet. Sie bringt Seeds + Recherche-Ergebnisse hierher, weil hier der tiefere
Zielgruppen-Check passiert, bevor das Ergebnis zurück in den anderen Thread geht und dort
mit Schritt 3 (Headline-Vorschläge) weitergeht.

**Wichtig: Nicht die Tool-Anleitung neu erfinden.** `strategie/keyword-check.md` ist die
kanonische Anleitung (Google Keyword Planner, AnswerThePublic, Google Trends, Google
direkt, Report-Template) — dieselbe Datei, aus der auch der `blog-post`-Skill seine
Checkliste zieht. Lies sie, statt die vier Schritte hier zu wiederholen; wenn sich dort
etwas ändert, gilt es hier automatisch mit.

## Was dieser Skill zusätzlich leistet

Der eigentliche Mehrwert dieses Skills ist der **Zielgruppen-Intent-Check**, beschrieben
im Abschnitt „Zielgruppen-Intent-Check" von `strategie/keyword-check.md`: Ein Keyword mit
Suchvolumen ist nicht automatisch ein gutes Keyword — mehrfach stellte sich heraus, dass
die Leute, die danach suchen, gar nicht Leonies Zielgruppe sind (Jobsuchende statt
Praxisinhaberinnen, Softwarekäufer:innen statt Beratungssuchende, Schul-Assessments statt
KI-Potenzialanalyse). Führe diesen Check bei **jedem** Keyword aus dem aktuellen Batch aktiv
durch — gegen `AGENTS.md` (Zielgruppe §1, Wort-Blacklist §9) und `strategie/segmente.md`
(Anker-Kriterien, Anti-Zielgruppe, Segment-Landkarte) —, nicht nur bei den schon bekannten
Fällen aus der Datei.

## Ablauf

1. **Seeds entgegennehmen.** Wenn noch keine Ergebnisse dabei sind, verweise auf die
   Checkliste in `strategie/keyword-check.md` und warte, bis Leonie liefert (CSV,
   Screenshot oder Text). Kündigt sie an, dass mehr folgt ("warte, ich schick dir noch
   ...") — tatsächlich warten, nicht mit Teilergebnissen loslegen.
2. **Nie Daten erfinden.** Fehlt ein Feld, ehrlich „kein Volumen" / „nicht durchgeführt" /
   „keine Daten geliefert" schreiben. Bei Bedarf mit `WebSearch` echte, aktuelle
   Content-Ideen ergänzen — immer klar kennzeichnen, dass das keine der vier offiziellen
   Quellen ersetzt.
3. **Intent-Check durchführen** (siehe oben) und ein Verdikt je Keyword(-gruppe) bilden:
   passt / passt teilweise / passt nicht, mit Begründung aus den echten Daten.
4. **Report-Template ausfüllen** — genau das Format, das Leonie mitgeschickt hat (lange
   oder kurze Version, siehe `strategie/keyword-check.md`), ergänzt um den Intent-Check.
5. **Ins Repo schreiben.** Suche nach vorhandenen `strategie/keyword-research-*.md`-Dateien
   und ergänze die neueste um einen neuen datierten Abschnitt (`## Post #N: <Thema>
   (<Datum>)`) — nur eine neue Datei anlegen, wenn wirklich keine existiert. Struktur der
   Datei übernehmen (H2-Abschnitte, Intent-Match-Tabelle, „Finale Keyword-Entscheidung"
   am Schluss). Dann `git add <genau diese eine Datei>` (nie `-A`/`.`), committen, direkt
   auf `main` pushen (Leonies Konvention laut `CLAUDE.md`). Vor dem Push immer
   `git fetch origin main` und bei Abweichungen sauber mergen — der `blog-post`-Skill
   arbeitet parallel im selben Repo und pusht ebenfalls auf `main` (siehe dessen eigene
   Regel dazu in Schritt 10). Kurz melden, was committet/gepusht wurde.
6. **Zusammenfassung für den Blog-Thread liefern** — copy-paste-fertig, im selben Format
   wie Leonies Template, plus empfohlenes finales Keyword-Set und eine Ein-Satz-Begründung
   mit Bezug auf `AGENTS.md`/`segmente.md`. Das gibt sie im anderen Thread ein, damit
   dessen Schritt 3 (Headline-Vorschläge) starten kann.

## Ton

Chat mit Leonie ist immer **Du-Form, Deutsch** — sie ist Site-Inhaberin, keine
Entwicklerin. Befund zuerst, dann Empfehlung, dann nächster Schritt.
