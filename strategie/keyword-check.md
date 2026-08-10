# Keyword- & Long-Tail-Check (vor jedem Blogpost)

*Erster Schritt jedes Blogposts: das Keyword prüfen, **bevor** Headline und Text entstehen.
Leonie führt die Tests durch (Suchvolumen braucht ein Tool), Claude liefert die Seed-Begriffe
und liest die reale Trefferseite qualitativ. Erst mit dem Ergebnis kommen die Headlines —
damit das validierte Keyword in der Headline sitzt.*

**Ablauf:** Claude nennt zu Post #N 4–6 **Seed-Begriffe** → Leonie prüft sie in den Tools
unten und trägt die Ergebnisse ins Report-Template ein → Claude wählt daraus das
Primär-Keyword + Long-Tail und macht **3 Headline-Vorschläge**.

---

## Die Tools (beim ersten Mal Schritt für Schritt; später genügt das Report-Template)

### 1. Google Keyword Planner — *Suchvolumen + Wettbewerb (das Wichtigste)*
Voraussetzung: ein (kostenloses) Google-Ads-Konto. Man muss **keine** Kampagne schalten.
1. `ads.google.com` einloggen. Falls Google zum Kampagnen-Assistenten drängt: unten
   „Zu den Kampagnen wechseln" / „Expertenmodus" wählen, keine Kampagne erstellen.
2. Oben rechts **Tools** (Schraubenschlüssel-Symbol) → **Planung** → **Keyword-Planer**.
3. **„Neue Keywords entdecken"** → die Seed-Begriffe eingeben (mehrere, mit Komma).
4. Rechts oben **Standort = Österreich** (optional zusätzlich Deutschland), **Sprache =
   Deutsch** einstellen. „Ergebnisse anzeigen".
5. Notieren je Begriff: **„Durchschnittl. Suchanfragen/Monat"** (Spanne, z. B. 100–1.000)
   und **„Wettbewerb"** (niedrig / mittel / hoch). Auch die vorgeschlagenen verwandten
   Keywords mit gutem Volumen mitnehmen.
> Faustregel: Ein Long-Tail mit **kleinem, aber echtem** Volumen und **niedrigem Wettbewerb**
> ist meist besser als ein großer, hart umkämpfter Kopfbegriff.

### 2. AnswerThePublic — *echte Fragen (werden H2 / FAQ)*
1. `answerthepublic.com` → Seed-Begriff eingeben.
2. **Sprache = German**, **Land = Austria** (oder Germany für mehr Volumen). „Search".
3. Es erscheint ein Rad/Liste mit **Fragen** (was/wie/warum/wo…), Präpositionen, Vergleichen.
4. Notieren: die 5–8 relevantesten **Fragen** und Long-Tail-Phrasen.
> Kostenlos nur wenige Suchen/Tag — daher gezielt 1–2 Seeds prüfen.

### 3. Google Trends — *Interesse über Zeit + verwandte Suchanfragen*
1. `trends.google.com` → Begriff eingeben.
2. **Region = Österreich** (oder Deutschland), **Zeitraum = letzte 12 Monate**.
3. Verlauf ansehen (steigend/fallend/saisonal). Mehrere Begriffe über **„+ Vergleichen"**
   gegeneinander stellen.
4. Unten **„Verwandte Suchanfragen"** (Top + Steigend) notieren — sehr wertvoll für reale
   Formulierungen.

### 4. Google direkt — *Autocomplete + „Ähnliche Fragen" + „Ähnliche Suchanfragen"* (0 Kosten)
1. Google öffnen (am besten **Inkognito-Fenster**, Region AT).
2. Seed tippen → **Autocomplete-Vorschläge** notieren (das sind reale häufige Suchen).
3. Suche absenden → mittendrin der Block **„Ähnliche Fragen" / „Nutzer fragen auch"** →
   die passenden Fragen notieren (werden H2/FAQ).
4. Ganz unten **„Ähnliche Suchanfragen"** notieren.

*(Optional, wenn vorhanden: Ubersuggest / Sistrix / SEMrush — gleiche Logik: Volumen +
verwandte Begriffe. Nicht nötig, wenn 1–4 gemacht sind.)*

---

## Report-Template (das schickt Leonie zurück)

```
Keyword-Check Post #N — Seeds: <von Claude genannt>

Google Keyword Planner:
- <keyword> — <Volumen/Monat> — <Wettbewerb>
- …

AnswerThePublic:
- <Top-Fragen / Long-Tail-Phrasen>

Google Trends:
- <steigend/fallend> · Verwandte Suchanfragen: <…>

Google direkt (Autocomplete / Ähnliche Fragen / Ähnliche Suchanfragen):
- <Notizen>
```

**Ab dem zweiten Mal** genügt diese Kurzform — Claude schreibt nur noch die Zeilen mit
den Tool-Namen und Leonie füllt die Ergebnisse ein.

---

## Zielgruppen-Intent-Check (Pflichtschritt, bevor ein Keyword übernommen wird)

*Aus der Recherche zu Post #1 gelernt (siehe `strategie/keyword-research-2026-07.md`,
„Runde 2"): **hohes Suchvolumen heißt nicht automatisch richtige Zielgruppe.** Ein
Keyword erst dann als gut bewerten, wenn auch geprüft ist, WER laut den „Ähnliche
Fragen"/„Ähnliche Suchanfragen" wirklich sucht — nicht nur ob überhaupt gesucht wird.*

Bereits gefundene Fallen (zur Orientierung, bei jedem neuen Begriff neu denken):
- „Praxismanagerin"/„Praxismanagement" — starkes Volumen, aber die Ähnliche-Fragen drehten
  sich um Gehalt, Stellenangebote, Ausbildung, IHK: Jobsuchende/Auszubildende, nicht
  Praxisinhaberinnen.
- „Praxissoftware" — reale Nachfrage, aber nach konkreten Konkurrenzprodukten (Tomedo,
  Medatixx, MEDISTAR) zum Kaufen/Vergleichen, nicht nach Beratung — würde außerdem gegen die
  „tool-agnostisch"-Positionierung in `AGENTS.md` laufen.
- „Potenzialanalyse" allein (ohne „KI-") ist im Deutschen stark von Schul-/
  Personalauswahl-Assessments besetzt (Schule, 8. Klasse, Arbeitsagentur).

**Check:** Passt die reale Suchintention laut Google direkt zu einer inhabergeführten
Gesundheits-/Wellness-Praxis mit sensiblen Patientendaten (Anker-Kriterien in
`strategie/segmente.md`, Zielgruppe/Anti-Zielgruppe in `AGENTS.md` §1) — oder nach etwas
anderem (Job, Software-Kauf, Ausbildung, ein anderes Berufsfeld, Konsument:innen statt B2B)?
Verdikt pro Keyword: **passt** / **passt teilweise** / **passt nicht**, mit Begründung aus
den echten Daten. Nie eine Zahl oder Suchintention raten, wenn keine Daten geliefert wurden —
ehrlich „kein Volumen"/„nicht durchgeführt" schreiben.
