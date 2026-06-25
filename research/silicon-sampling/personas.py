"""
Persona-Generierung für die Silicon-Sampling-Studie.

Personas werden DETERMINISTISCH aus einem Seed erzeugt (nicht von der API
"erfunden"), damit die Studie reproduzierbar ist und die Diversität aktiv
kontrolliert wird (Gegenmaßnahme gegen "Response Homogeneity",
Workbook S. 8). Jede Persona trägt >= 12 Attribute (Workbook-Empfehlung:
8-12) über demografische, psychografische, kontextuelle und
Verhaltens-Dimensionen.

WICHTIG (methodische Unabhängigkeit): Hier werden NUR strukturelle Attribute
gesetzt (Branche, Rolle, Alter, Haltung ...). Es werden BEWUSST KEINE
Pain Points, Wünsche, Einwände oder O-Töne vorgegeben — diese sollen
ausschließlich aus der Befragung der Personas entstehen.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, asdict
from typing import Optional

# --- Achsen der Diversität -------------------------------------------------

BRANCHEN = [
    "Physiotherapie-/Therapiepraxis",
    "Ernährungs-/Gesundheitszentrum",
    "Personal-Training-Studio",
    "Präventions-/BGF-Anbieter",
    "Wellness-/Longevity-Praxis (Premium)",
]

# realistische Sub-Disziplinen je Branche (nur Kontext, keine inhaltl. Vorgabe)
SUBFOKUS = {
    "Physiotherapie-/Therapiepraxis": [
        "klassische Physiotherapie", "Sportphysio & Reha", "Osteopathie",
        "Ergotherapie", "Logopädie im Verbund", "manuelle Therapie & Faszien",
    ],
    "Ernährungs-/Gesundheitszentrum": [
        "Ernährungsberatung", "Diätologie", "Stoffwechsel & Darmgesundheit",
        "Gewichtsmanagement", "ganzheitliches Gesundheitszentrum",
    ],
    "Personal-Training-Studio": [
        "1:1 Personal Training", "Small-Group-Training", "EMS-Studio",
        "Functional-Training-Box", "Frauen-Fitness-Studio",
    ],
    "Präventions-/BGF-Anbieter": [
        "betriebliche Gesundheitsförderung", "Rückenschule & Prävention",
        "Stress-/Resilienz-Programme", "Gesundheitscoaching für Firmen",
    ],
    "Wellness-/Longevity-Praxis (Premium)": [
        "Longevity & Healthspan", "Medical Wellness", "Spa & Privatklinik-nah",
        "Hormone & Performance", "Privatpraxis Premium-Prävention",
    ],
}

ROLLEN = [
    # (Label, arbeitet fachlich noch mit?)
    ("Inhaberin/Inhaber, rein unternehmerisch (kaum noch fachlich am Menschen)", False),
    ("Mitarbeitende Leitung (führt UND arbeitet selbst fachlich mit)", True),
]

LAENDER = ["AT", "DE", "CH"]

# Haltung zum Thema Digitalisierung/KI — bewusst inkl. skeptisch/desinteressiert
HALTUNGEN = [
    "neugierig-offen", "pragmatisch-abwägend", "skeptisch", "stark skeptisch",
    "desinteressiert / sieht keinen Bedarf", "überfordert / zu wenig Zeit",
    "früher Anwender / probiert gern Neues",
]
# Gewichtung: Skepsis & Desinteresse bewusst gut vertreten
HALTUNG_WEIGHTS = [0.18, 0.20, 0.16, 0.10, 0.12, 0.14, 0.10]

# Digitale Reife: 1 = "wie vor zehn Jahren", 5 = "erste Tools laufen schon"
REIFE_LABEL = {
    1: "digital wie vor zehn Jahren (Papierkalender, Telefon, Excel-Listen)",
    2: "wenig digital (Online-Kalender, sonst manuell)",
    3: "teils digital (Praxissoftware vorhanden, aber kaum vernetzt)",
    4: "ordentlich digital (Software + erste Automatisierungen)",
    5: "schon erste KI-/Automatisierungs-Tools im Einsatz",
}

PERSOENLICHKEIT = [
    "bodenständig", "ehrgeizig", "vorsichtig", "kostenbewusst", "perfektionistisch",
    "herzlich-beziehungsorientiert", "nüchtern-zahlengetrieben", "chaotisch-kreativ",
    "kontrollbedürftig", "gelassen", "ungeduldig", "gewissenhaft",
    "harmoniebedürftig", "durchsetzungsstark", "zurückhaltend",
]

# Namen je Land/Geschlecht (klein gehalten, nur für Authentizität)
VORNAMEN = {
    ("DE", "weiblich"): ["Sabine", "Nicole", "Katrin", "Andrea", "Julia", "Stefanie", "Petra", "Christine", "Melanie", "Franziska"],
    ("DE", "männlich"): ["Thomas", "Michael", "Stefan", "Andreas", "Markus", "Daniel", "Tobias", "Christian", "Sebastian", "Jan"],
    ("AT", "weiblich"): ["Birgit", "Eva", "Manuela", "Karin", "Sandra", "Bettina", "Doris", "Verena", "Elisabeth", "Theresa"],
    ("AT", "männlich"): ["Markus", "Gerald", "Hannes", "Reinhard", "Florian", "Wolfgang", "Lukas", "Roman", "Bernhard", "Klaus"],
    ("CH", "weiblich"): ["Daniela", "Corinne", "Barbara", "Simone", "Nadine", "Claudia", "Ramona", "Fabienne", "Janine", "Tanja"],
    ("CH", "männlich"): ["Marco", "Beat", "Reto", "Patrick", "Stefan", "Lukas", "Roger", "Pascal", "Andreas", "Matthias"],
}
VORNAMEN_DIVERS = ["Kim", "Robin", "Sascha", "Alex", "Toni", "Charlie"]

WAEHRUNG = {"AT": "EUR", "DE": "EUR", "CH": "CHF"}


@dataclass
class Persona:
    pid: str
    name: str
    alter: int
    geschlecht: str
    land: str
    branche: str
    subfokus: str
    rolle: str
    arbeitet_fachlich_mit: bool
    teamgroesse: int
    jahresumsatz_eur: int
    tech_affinitaet: int          # 1-5
    digitale_reife: int           # 1-5
    digitale_reife_label: str
    haltung: str
    persoenlichkeit: list
    jahre_selbststaendig: int
    waehrung: str

    def system_prompt(self) -> str:
        """Baut den Rollen-System-Prompt (Workbook Template 1, Ich-Perspektive)."""
        traits = ", ".join(self.persoenlichkeit)
        fachlich = (
            "Sie arbeiten neben der Leitung selbst noch fachlich mit Klient:innen."
            if self.arbeitet_fachlich_mit else
            "Sie sind v. a. unternehmerisch/organisatorisch tätig und arbeiten "
            "kaum noch direkt am Menschen."
        )
        umsatz_txt = f"{self.jahresumsatz_eur:,}".replace(",", ".")
        return f"""Du verkörperst ab jetzt vollständig und konsistent eine reale Person und bleibst die GANZE Befragung über in dieser Rolle. Antworte durchgehend in der Ich-Perspektive, in deiner eigenen, natürlichen Sprache (deutschsprachiger Raum), mit deinen Werten, Sorgen und deiner Wortwahl. Sei spezifisch, authentisch und ehrlich – auch kritisch oder ablehnend, wenn es zu dir passt. Vermeide Marketing-Sprache und glatte Werbefloskeln. Antworte NICHT zu brav oder sozial erwünscht; sag offen, wenn dich etwas nervt, langweilt oder skeptisch macht.

WER DU BIST:
- Name: {self.name}, {self.alter} Jahre, {self.geschlecht}, in {self.land}.
- Betrieb: {self.branche} – Schwerpunkt {self.subfokus}.
- Rolle: {self.rolle}. {fachlich}
- Team: {self.teamgroesse} Personen (inkl. dir). Jahresumsatz rund {umsatz_txt} {self.waehrung}.
- Seit {self.jahre_selbststaendig} Jahren selbstständig/in Leitung.
- Digitaler Stand: {self.digitale_reife_label}.
- Tech-Affinität: {self.tech_affinitaet}/5. Grundhaltung gegenüber Digitalisierung/Technik im Betrieb: {self.haltung}.
- Persönlichkeit: {traits}.

Du kennst deinen Betriebsalltag genau und sprichst aus eigener Erfahrung. Du bist KEINE KI und brichst nie aus der Rolle aus. Erfinde realistische Details deines Alltags, wo es passt, aber bleib konsistent mit den Angaben oben."""

    def to_dict(self) -> dict:
        return asdict(self)


def _weighted_revenue(rng: random.Random, branche: str, teamgroesse: int) -> int:
    """Umsatz 150k–800k, grob korreliert mit Teamgröße + Premium-Aufschlag."""
    base = 150_000 + (teamgroesse - 2) / 8 * 450_000
    if branche.startswith("Wellness-/Longevity"):
        base *= rng.uniform(1.15, 1.6)      # Premium-Segment höher
    if branche.startswith("Präventions"):
        base *= rng.uniform(0.9, 1.25)
    noise = rng.uniform(0.7, 1.35)
    val = int(base * noise)
    val = max(150_000, min(800_000, val))
    return int(round(val, -3))              # auf 1000 gerundet


def generate_personas(n: int = 220, seed: int = 20260625) -> list[Persona]:
    """Erzeugt n diverse, reproduzierbare Personas."""
    rng = random.Random(seed)
    personas: list[Persona] = []
    for i in range(n):
        land = rng.choice(LAENDER)
        # Geschlecht: divers selten, sonst gemischt (Gesundheitsbranche eher weiblich)
        r = rng.random()
        geschlecht = "divers" if r < 0.03 else ("weiblich" if r < 0.62 else "männlich")
        branche = BRANCHEN[i % len(BRANCHEN)]            # gleichmäßige Branchen-Streuung
        subfokus = rng.choice(SUBFOKUS[branche])
        rolle_label, fachlich = rng.choice(ROLLEN)
        teamgroesse = rng.randint(2, 10)
        alter = rng.randint(28, 62)
        tech = rng.randint(1, 5)
        # digitale Reife korreliert lose mit Tech-Affinität
        reife = max(1, min(5, tech + rng.choice([-1, 0, 0, 1])))
        haltung = rng.choices(HALTUNGEN, weights=HALTUNG_WEIGHTS, k=1)[0]
        traits = rng.sample(PERSOENLICHKEIT, k=rng.randint(2, 3))
        jahre = max(1, min(alter - 24, rng.randint(2, 30)))

        if geschlecht == "divers":
            name = rng.choice(VORNAMEN_DIVERS)
        else:
            name = rng.choice(VORNAMEN[(land, geschlecht)])

        personas.append(Persona(
            pid=f"P{i+1:03d}",
            name=name,
            alter=alter,
            geschlecht=geschlecht,
            land=land,
            branche=branche,
            subfokus=subfokus,
            rolle=rolle_label,
            arbeitet_fachlich_mit=fachlich,
            teamgroesse=teamgroesse,
            jahresumsatz_eur=_weighted_revenue(rng, branche, teamgroesse),
            tech_affinitaet=tech,
            digitale_reife=reife,
            digitale_reife_label=REIFE_LABEL[reife],
            haltung=haltung,
            persoenlichkeit=traits,
            jahre_selbststaendig=jahre,
            waehrung=WAEHRUNG[land],
        ))
    return personas


if __name__ == "__main__":
    import json, collections, sys
    ps = generate_personas()
    print(f"{len(ps)} Personas erzeugt.\n")
    for axis, key in [
        ("Branche", lambda p: p.branche),
        ("Land", lambda p: p.land),
        ("Haltung", lambda p: p.haltung),
        ("Geschlecht", lambda p: p.geschlecht),
        ("Digitale Reife", lambda p: p.digitale_reife),
        ("Rolle fachlich?", lambda p: p.arbeitet_fachlich_mit),
    ]:
        c = collections.Counter(key(p) for p in ps)
        print(f"== {axis} ==")
        for k, v in sorted(c.items(), key=lambda x: str(x[0])):
            print(f"   {k}: {v}")
        print()
    if "--dump" in sys.argv:
        print(json.dumps(ps[0].to_dict(), ensure_ascii=False, indent=2))
        print("\n--- SYSTEM PROMPT BEISPIEL ---\n")
        print(ps[0].system_prompt())
