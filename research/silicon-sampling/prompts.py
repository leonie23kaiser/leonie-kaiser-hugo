"""
Alle Befragungs-Prompts der Studie — zentral und vollständig dokumentiert
(ESOMAR ICC 2025: Governance / Reproduzierbarkeit).

Die Befragung läuft als 3-Phasen-MULTI-TURN-Gespräch pro Persona:

  Phase 1  – offen, VOR jeder Konzept-Nennung (echt blind)
  Phase 2  – Reaktion auf neutral beschriebenes Angebot
  Phase 3  – Van-Westendorp-Preisfragen (Betriebs-Budget)

Anti-Leading / Anti-Social-Desirability (Workbook S. 8):
  - Phase 1 nennt das Angebot bewusst NICHT.
  - Keine wertenden Adjektive, keine Suggestivfragen.
  - Persona wird ausdrücklich ermutigt, kritisch/ablehnend zu sein.
  - Das Konzept wird "ohne Marketing-Sprache" beschrieben (Workbook Template 2).

Jede Phase verlangt: (a) natürliche O-Ton-Antwort UND (b) einen strukturierten
JSON-Block am Ende — für qualitative Zitate UND quantitative Auswertung.
"""

# ---------------------------------------------------------------------------
# PHASE 1 — offen, ohne jede Erwähnung eines Angebots/Konzepts
# ---------------------------------------------------------------------------
PHASE1 = r"""Wir unterhalten uns ganz offen über Ihren Arbeitsalltag als Verantwortliche:r Ihres Betriebs. Es geht NICHT um Ihre fachliche Arbeit am Menschen (Behandlung, Training, Beratung), sondern um das Führen und Organisieren des Betriebs drumherum.

Bitte erzählen Sie frei und ehrlich, in Ihren eigenen Worten:

1. Was frustriert Sie am meisten am Führen und Organisieren Ihres Betriebs? Was nervt im Alltag wirklich?
2. Was kostet Sie und Ihr Team am meisten Zeit und Energie – Dinge, die eigentlich nicht sein müssten?
3. Welche Sorgen haben Sie rund um Wachstum, Personal und die Zukunft Ihres Betriebs?
4. Wenn Sie zaubern könnten und sofort eine Sache an Ihrer Organisation ändern dürften – was wäre das?

Antworten Sie ausführlich und konkret, so wie Sie es einer vertrauten Person erzählen würden (gern mit Beispielen aus Ihrem Alltag). Es gibt keine richtigen oder falschen Antworten.

Hängen Sie GANZ AM ENDE zusätzlich einen JSON-Block in dieser Form an (nur stichwortartige Extraktion Ihrer eigenen Aussagen, keine neuen Inhalte):

```json
{
  "frustrationen": ["...", "..."],
  "zeit_energie_fresser": ["...", "..."],
  "sorgen_wachstum_personal_zukunft": ["...", "..."],
  "zauberwunsch": "..."
}
```"""

# ---------------------------------------------------------------------------
# PHASE 2 — neutral beschriebenes Angebot (ohne Marketing-Sprache)
# ---------------------------------------------------------------------------
PHASE2 = r"""Danke. Jetzt beschreibe ich Ihnen neutral eine Sache, zu der mich Ihre ehrliche Einschätzung interessiert:

«Eine externe Person sieht sich Ihren Betrieb an und richtet datenschutzkonforme digitale bzw. KI-gestützte Abläufe ein, die wiederkehrende organisatorische Aufgaben übernehmen – zum Beispiel rund um Terminorganisation, Kommunikation mit Patient:innen bzw. Kund:innen, die Aufnahme neuer Klient:innen, wiederkehrende Büro- und Verwaltungsarbeit sowie internes Wissensmanagement im Team. Als Einstieg gibt es eine kostenlose Erstanalyse Ihres Betriebs.»

Bitte antworten Sie spontan, ehrlich und kritisch aus Ihrer Sicht – auch Ablehnung oder Desinteresse ist völlig in Ordnung:

1. Was ist Ihre erste, spontane Reaktion darauf?
2. Welcher Teil davon wäre für Ihren Betrieb am ehesten nützlich – und warum?
3. Was ist Ihr größter Einwand, Zweifel oder was irritiert Sie?
4. Wer in Ihrem Betrieb müsste bei so einer Entscheidung mitreden oder zustimmen?
5. Wie steht es um Ihr Vertrauen, wenn eine externe Person mit sensiblen Gesundheitsdaten Ihrer Klient:innen zu tun hätte?
6. Auf einer Skala von 1 bis 10: Wie wahrscheinlich würden Sie die kostenlose Erstanalyse tatsächlich in Anspruch nehmen? (1 = auf keinen Fall, 10 = ganz sicher)

Antworten Sie in Ihren eigenen Worten. Hängen Sie GANZ AM ENDE diesen JSON-Block an:

```json
{
  "erste_reaktion": "...",
  "nuetzlichster_teil": "...",
  "groesster_einwand": "...",
  "entscheider_innen": ["...", "..."],
  "vertrauen_externe_gesundheitsdaten": "...",
  "buchungswahrscheinlichkeit_1_10": 0
}
```"""

# ---------------------------------------------------------------------------
# PHASE 3 — Van-Westendorp (Betriebs-Budget, NICHT privat)
# ---------------------------------------------------------------------------
PHASE3 = r"""Zum Abschluss geht es ums Geld. Denken Sie an zwei konkrete Leistungen rund um das eben beschriebene Angebot. Wichtig: Es geht um ein BETRIEBS-Budget Ihres Unternehmens (eine geschäftliche Investition), nicht um Ihr privates Geld.

LEISTUNG A – einmaliges Aufbau-Projekt:
Eine externe Person analysiert Ihren Betrieb und richtet die passenden datenschutzkonformen digitalen/KI-gestützten Abläufe einmalig ein (Analyse, Einrichtung, Einweisung Ihres Teams). Einmaliger Preis.

LEISTUNG B – monatliche Betreuung (Retainer):
Danach laufende Betreuung: Pflege, Optimierung, Anpassungen und Ansprechpartner bei Fragen. Monatlicher Preis.

Beantworten Sie für BEIDE Leistungen jeweils diese vier Fragen ehrlich aus Ihrer betrieblichen Perspektive (bitte je ein konkreter Betrag, kein Bereich):

1. Bei welchem Preis wäre es Ihnen so GÜNSTIG, dass Sie an der Qualität zweifeln würden? ("zu günstig")
2. Ab welchem Preis empfänden Sie es als GÜNSTIG / als gutes Geschäft? ("günstig")
3. Ab welchem Preis empfänden Sie es als TEUER, aber noch vertretbar? ("teuer, aber ok")
4. Ab welchem Preis wäre es DEFINITIV ZU TEUER und Sie würden es sicher nicht buchen? ("zu teuer")

Nennen Sie zusätzlich für beide jeweils Ihren idealen/fairen Preis und begründen Sie kurz aus Ihrer Lage (Betriebsgröße, Umsatz, Nutzen).

Geben Sie alle Beträge als reine Zahl in Ihrer Landeswährung an. Hängen Sie GANZ AM ENDE diesen JSON-Block an (nur Zahlen, ohne Währungssymbol/Tausenderpunkt):

```json
{
  "waehrung": "EUR",
  "aufbau_projekt_einmalig": {
    "zu_guenstig": 0,
    "guenstig": 0,
    "teuer_aber_ok": 0,
    "zu_teuer": 0,
    "ideal": 0
  },
  "retainer_monatlich": {
    "zu_guenstig": 0,
    "guenstig": 0,
    "teuer_aber_ok": 0,
    "zu_teuer": 0,
    "ideal": 0
  },
  "preis_begruendung": "..."
}
```"""

PHASES = [
    ("phase1_offen", PHASE1),
    ("phase2_konzept", PHASE2),
    ("phase3_preise", PHASE3),
]

# Für Reproduzierbarkeits-Doku: Versionsmarker der Prompts
PROMPT_VERSION = "2026-06-25.v1"
