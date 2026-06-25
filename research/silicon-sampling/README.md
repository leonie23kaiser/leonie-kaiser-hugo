# Silicon-Sampling-Studie — Gesundheits- & Wellness-Betriebe (DACH)

Ausführbare Silicon-Sampling-Studie nach der Methodik des Workbooks
*„Silicon Sampling – Workbook für KI-Consultants"* (KI Consultant, Stand April 2026).

> ⚠️ **SYNTHETISCHE DATEN — ESOMAR ICC Code 2025.** Befragt wurden KI-Personas,
> keine echten Menschen. Alle Ergebnisse sind **Hypothesen, keine validierten
> Fakten**, und müssen vor strategischen Entscheidungen durch echte Interviews
> (10–20) validiert werden. Silicon Sampling ist ein Ergänzungs-Tool, kein
> Ersatz für echte Marktforschung.

## Zielgruppe

Kleine Gesundheits- & Wellness-Betriebe **mit Team (2–10 Personen)** im
deutschsprachigen Raum (AT/DE/CH): Inhaber:innen bzw. mitarbeitende Leitung von
Physio-/Therapiepraxen, Ernährungs-/Gesundheitszentren, Personal-Training-Studios,
Präventions-/BGF-Anbietern und Premium-Wellness-/Longevity-Praxen. Jahresumsatz
typisch €150k–800k.

## Forschungsfrage

1. Was frustriert diese Betriebe an **Führung & Organisation** (nicht an der
   fachlichen Arbeit am Menschen)? Welche Pain Points, Wünsche, Sorgen?
2. Wie reagieren sie auf ein Angebot „datenschutzkonforme KI-/Automatisierungs-
   Systeme einrichten lassen, kostenlose Erstanalyse als Einstieg"? Nutzen,
   Einwände, Buy-in, Vertrauen, Buchungswahrscheinlichkeit?
3. Welche Preise (Van-Westendorp) gelten für ein einmaliges Aufbau-Projekt und
   einen monatlichen Betreuungs-Retainer — bei **Betriebs-Budget**?

## Methodische Unabhängigkeit

Es wurden **bewusst keine** Pain Points, Wünsche, Einwände oder Formulierungen
vorgegeben. Personas tragen nur strukturelle Attribute (Branche, Rolle, Alter,
Haltung …); alle inhaltlichen Aussagen entstehen unabhängig aus der Befragung.

## Aufbau

| Datei | Zweck |
|---|---|
| `personas.py` | Deterministische, geseedete Generierung von 220 diversen Personas (≥12 Attribute, inkl. skeptischer/desinteressierter Profile). |
| `prompts.py` | Alle Befragungs-Prompts (Phase 1 offen/blind, Phase 2 Konzept, Phase 3 Van-Westendorp), vollständig dokumentiert. |
| `run_study.py` | Parallele 3-Phasen-Befragung über die Anthropic-API, Checkpoint pro Persona, Resume nach Abbruch. |
| `analyze.py` | Auswertung: Pain-Point-Cluster + O-Töne, Segment-/Teamgrößen-Vergleich, Decision-Maker-Mapping, Van-Westendorp (OPP + Akzeptanzspanne). |
| `data/responses/*.json` | Rohantworten je Persona (O-Ton-Prosa + strukturierter JSON-Block). |
| `data/responses_flat.csv` | Quantitative Auswertungstabelle (eine Zeile je Persona). |
| `data/quotes.json` | Kuratierte O-Töne, thematisch zugeordnet. |
| `data/run_meta.json` | Reproduzierbarkeits-Metadaten (Modell, Seed, Prompt-Version, Laufzeit). |
| `reports/REPORT.md` | Auswertungsbericht mit O-Tönen & ESOMAR-Kennzeichnung. |

## Reproduzieren

```bash
python3 -m venv .venv
.venv/bin/pip install anthropic
export ANTHROPIC_API_KEY=...        # Key NIE im Repo speichern

# Personas prüfen (geseedet, ohne API)
.venv/bin/python personas.py

# Pilot (10 Personas)
.venv/bin/python run_study.py --limit 10

# Voller Lauf (220 Personas, parallel, mit Resume)
.venv/bin/python run_study.py --count 220 --concurrency 8

# Auswertung & Report
.venv/bin/python analyze.py
```

- **Modell:** `claude-sonnet-4-6`
- **Persona-Seed:** `20260625` (220 Personas)
- **Resume:** Bereits vorhandene `data/responses/<pid>.json` werden übersprungen —
  ein abgebrochener Lauf läuft beim Neustart genau dort weiter.

## ESOMAR-Compliance (ICC Code 2025)

- **Transparenzpflicht:** Alle Outputs sind als synthetische Daten gekennzeichnet.
- **Human Oversight:** Befunde sind Hypothesen; Validierung mit echten Interviews
  erforderlich.
- **Governance:** Modell, Prompts, Persona-Design und Seed vollständig dokumentiert.
- **Grenzen:** gesprochene Präferenz statt echtem Verhalten; mögliche
  Homogenisierung von Mehrheitsmeinungen; kein Ersatz für reale Marktforschung.
