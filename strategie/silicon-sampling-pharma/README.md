# Silicon Sampling — Pharma- & Gesundheits-KMU (DACH)

Eigenständige Silicon-Sampling-Studie, **getrennt** von den Praxen- und Solo-Studien
(`strategie/silicon-sampling.md`). Zielgruppe: **kleine und mittlere Unternehmen der
Pharma- und Gesundheitsbranche im DACH-Raum, 10–50 Mitarbeitende — keine Großkonzerne**
(Medizinprodukte-/Diagnostik-Hersteller, Regulatory-/Pharmakovigilanz-/CRO-Dienstleister,
Auftragslabore, Nahrungsergänzung/OTC, Großhandel/Vertrieb, Health-IT, u. a.).

> **⚠️ Synthetische Daten — ESOMAR ICC Code 2025.** Ergebnisse stammen aus KI-Personas
> (Modell `claude-sonnet-4-6`), **nicht** aus echten Befragungen. Sie sind **Hypothesen,
> keine Fakten**. Vor Investitions- oder Preisentscheidungen mit echten Interviews validieren.

## Methodische Unabhängigkeit

Vorgegeben wurde **nur die Zielgruppe**. Pain Points, Wünsche, Einwände, Formulierungen
und Preise entstehen **frei aus den Personas** — es wurden keine inhaltlichen Vorlagen
(auch nicht aus der Praxen-Studie) eingespeist. Phase 1 ist blind, vor jeder
Konzept-/Angebots-Nennung; keine Leading-Fragen; Skeptiker-/Vorsichtig-Quote bewusst > 40 %;
Personas dürfen ablehnen oder desinteressiert sein.

## Ablauf je Persona (4 API-Calls)

1. **Phase 1 (offen):** Frust am Führen/Organisieren, Zeitfresser, Sorgen (Wachstum/Personal/
   Regulatorik/Zukunft), „per Zauberei sofort ändern".
2. **Phase 2 (Angebot):** Reaktion auf ein neutral beschriebenes Angebot (externe Analyse +
   datenschutz-/regulatorisch konforme KI-/Automatisierungs-Systeme, kostenlose Erstanalyse).
   Nützlichster Teil, größter Einwand, Mitentscheider, Vertrauen ggü. Externen mit sensiblen
   Daten, Buchungswahrscheinlichkeit 1–10.
3. **Phase 3 (Van Westendorp):** 4 Preisschwellen für ein einmaliges Aufbau-Projekt **und**
   einen monatlichen Betreuungs-Retainer (Unternehmensbudget, reguliertes Beschaffungsumfeld).
4. **Extraktion:** separater Analyse-Prompt → strukturiertes JSON (Zahlen, Tags, wörtliche Zitate).

Die **vollständigen Prompts** liegen in `run_pharma_kmu.py` und werden zusätzlich in
`sampling_pharma_kmu.json` unter `prompts` gespeichert (Reproduzierbarkeit).

## Dateien

| Datei | Inhalt |
|---|---|
| `personas.py` | Deterministische Persona-Generierung (Seed `20260719`), Skeptiker-Quote |
| `run_pharma_kmu.py` | Befragungs-Engine: 3 Phasen + Extraktion, parallel, Checkpoint je Persona |
| `analyze_pharma_kmu.py` | Auswertung: Pain Points, O-Töne, Teilbranchen, Van Westendorp, Regulatorik |
| `sampling_pharma_kmu.json` | **Ergebnis-Datei** (Rohdaten + Prompts + Metadaten), gemerged |
| `report_pharma_kmu.md` | Lesbarer Report (ESOMAR-gekennzeichnet) |
| `auswertung_pharma_kmu.json` | Maschinenlesbare Auswertung |
| `checkpoints/` | Zwischenstände je Persona (gitignored; stecken gemerged in der Ergebnis-Datei) |

## Ausführen

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...        # niemals committen
python3 run_pharma_kmu.py 200 --workers 8  # resümiert automatisch aus checkpoints/
python3 analyze_pharma_kmu.py              # erzeugt Report + Auswertung
```

Der Lauf ist **abbruchsicher**: jede fertige Persona wird sofort als Checkpoint
gespeichert; ein Neustart überspringt Erledigtes. `sampling_pharma_kmu.json` wird
laufend aktualisiert.

- **Modell:** `claude-sonnet-4-6` (Anthropic)
- **Van Westendorp:** nur valide, monoton geordnete Antworten (zu_günstig < günstig < teuer
  < zu_teuer); OPP/IPP/PMC/PME per linearer Interpolation, auch je Teilbranche.
