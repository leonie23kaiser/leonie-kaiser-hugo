# Word-Layout-Toolkit — Leonie Kaiser (Teal-Branding)

Erzeugt aus Markdown ein `.docx` im festen Marken-Layout: Arial-Grundschrift,
Teal-Überschriften, getönte Tabellenköpfe, Zitat-Randlinie, Fußzeile mit Seitennummer.

**Zweck:** Damit alle Threads Word-Dokumente im **gleichen** Look ausgeben, ohne das
Layout neu zu bauen. Einfach dieses Skript nutzen statt eigene Konverter schreiben.

## Einmalig einrichten

```bash
cd strategie/tools/docx-layout
npm init -y
npm install docx        # erzeugt lokales node_modules (NICHT committen, via .gitignore)
```

Node 18+ genügt. `prep.py` braucht nur Python 3.

## Verwenden

```bash
# 1) Markdown flachklopfen (Absätze zusammenführen, Links -> Text)
python3 prep.py mein-text.md mein-text.prepped.md

# 2) DOCX bauen
node md2docx_konzept.js mein-text.prepped.md ergebnis.docx
```

## Unterstützt

`#`–`####` Überschriften · Tabellen · Bullet-/Nummern-Listen · `> Zitat` ·
`**fett**` · `*kursiv*` · `` `code` `` · `---` Trennlinie.

## Layout anpassen

Alles Wichtige steht oben in `md2docx_konzept.js`:

- **Farben:** `TEAL 086584` · `TEAL6 5FA2A0` · `TEAL_LIGHT E7F4F4` · `INK 1D2228` · `MUTE 5B6572` · `LINE CCCCCC`.
- **Überschriften-Größen:** Block `paragraphStyles` (Half-Points: H1 34 / H2 27 / H3 23 / H4 21).
- **Fußzeile:** Abschnitt `footers` — der Disclaimer-Text ist auf synthetische Silicon-Sampling-Daten
  gemünzt. Für andere Dokumente den Text ersetzen oder leeren.

> Hinweis: Die Marken-Tokens spiegeln `params.toml` / `CLAUDE.md`. Bei Brand-Updates hier mitziehen.
