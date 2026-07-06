# Second Brain — KI-Consulting Lehrgang

*Erstellt: Juni 2026 | Für: Leonie Kaiser*

Dein Kurswissen abrufbar machen — ohne Server, ohne Wartung, ohne Technik-Stress.
Du brauchst: GitHub-Account (hast du), Claude.ai-Account (hast du). Das war's.

---

## Setup — einmalig, ~10 Minuten

### Schritt 1 — Privates Repo anlegen

1. Geh auf https://github.com/new
2. Repository name: `ki-lehrgang-brain`
3. **Private** auswählen (nicht Public)
4. Haken bei „Add a README file"
5. **Create repository**

---

### Schritt 2 — Ordnerstruktur anlegen

Im neuen Repo auf **Add file → Create new file** klicken.

Lege diese Dateien an (jeweils Name eingeben, etwas reinschreiben, committen):

```
CLAUDE.md              ← deine Hausregeln für Claude
raw/platzhalter.md     ← hier kommen rohe Notizen rein
destilliert/index.md   ← hier baut Claude das Wissen auf
```

**Inhalt `CLAUDE.md`** — kopiere das rein:

```markdown
# Wer ich bin
Leonie Kaiser, KI- & Business-Consultant.
Zielgruppe: kleine Dienstleistungsunternehmen (3–20 MA),
v.a. Gesundheit, Beratung, wissensintensive Services.

# Wofür ich dieses Wissen nutze
- Klienten-Workshops vorbereiten und vereinfachen
- Blogartikel für leoniekaiser.com / growthtogether.at
- Eigene Tool- und Methodenauswahl

# Wie du mit diesem Repo arbeitest
- Neue Rohmaterialien landen in raw/ (unstrukturiert ist ok)
- Destilliertes, aufbereitetes Wissen gehört nach destilliert/
- Beim Destillieren: Praxisbeispiele immer behalten,
  Theorie zusammenfassen, Quelle vermerken (Modul X, Datum)
- Nichts löschen — ergänzen und verknüpfen
```

---

### Schritt 3 — Claude.ai verbinden

1. https://claude.ai/settings/connectors öffnen
2. Bei **GitHub** → **Connect** (falls nicht schon verbunden)
3. Bei „Repository access" → **Only select repositories**
4. `ki-lehrgang-brain` auswählen → **Install & Authorize**

---

## Alltag — so funktioniert's

### Nach jeder Kurseinheit (5 Minuten)

Notizen, Screenshots, PDFs direkt ins Repo hochladen:
- GitHub → `raw/` → **Add file → Upload files**
- Dateinamen mit Datum: `2026-06-modul3-notizen.md`
- Kein schöner Text nötig — Stichwörter reichen

---

### Einmal pro Woche (10 Minuten)

Neuer Chat auf claude.ai, Repo anhängen (📎 → GitHub → `ki-lehrgang-brain`), dann schreiben:

> *„Schau in raw/ nach neuen Files seit dem letzten Mal.
> Ergänze die passenden Seiten in destilliert/ —
> neue Erkenntnisse rein, nichts überschreiben, Quelle vermerken.
> Wenn ein Thema noch keine eigene Seite hat, leg sie an."*

Claude liest, strukturiert, verknüpft. Du schaust drüber, sagst „passt" oder „ändere X", dann commit.

---

### Wenn du etwas suchst

Repo anhängen, dann einfach fragen:

> *„Was weiß ich bisher über RAG-Systeme?"*
> *„Welche Tools für No-Code-Automatisierung hab ich notiert?"*
> *„Was aus Modul 4 könnte ich in einem Workshop für Physiotherapeuten verwenden?"*

---

## Beispiel-Struktur nach ein paar Wochen

```
ki-lehrgang-brain/
├── CLAUDE.md
├── raw/
│   ├── 2026-06-modul1-notizen.md
│   ├── 2026-06-modul2-screenshots/
│   └── 2026-06-modul5-handout.pdf
└── destilliert/
    ├── index.md                    ← Übersicht aller Themen
    ├── prompting-patterns.md
    ├── tools-uebersicht.md
    ├── use-cases-gesundheit.md
    ├── automatisierung-no-code.md
    └── workshop-vorlagen.md
```

---

## Das war's

Kein Server. Keine App. Keine Wartung.
Nur ein Repo, Claude, und deine Notizen — und das Wissen bleibt auffindbar.
