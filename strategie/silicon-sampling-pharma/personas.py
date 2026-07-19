"""
Persona-Generierung fuer die Silicon-Sampling-Studie
"Pharma- & Gesundheits-KMU (DACH, 10-50 Mitarbeitende)".

Deterministisch (fixer Seed) => reproduzierbar. Die Attribute werden bewusst
breit gestreut und NICHT auf einen homogenen Kern getrimmt. Es werden KEINE
Pain Points, Wuensche oder Einwaende vorgegeben -- diese entstehen frei im
Interview (methodische Unabhaengigkeit).

Synthetische Daten gemaess ESOMAR ICC Code 2025.
"""
import random

SEED = 20260719

# --- Teilbranchen (bewusst heterogen, keine Grosskonzerne) -------------------
# gewicht = grobe relative Haeufigkeit in der Stichprobe
TEILBRANCHEN = [
    ("Medizinprodukte-Hersteller (Klasse I-IIb, klein/mittel)", 12),
    ("Diagnostik-/IVD-Hersteller", 8),
    ("Regulatory-Affairs-Dienstleister (Zulassung/MDR/IVDR)", 10),
    ("Pharmakovigilanz-Dienstleister", 6),
    ("Klinische-Studien-Dienstleister / kleine CRO", 8),
    ("Auftragslabor (Analytik / QC / Mikrobiologie)", 8),
    ("Nahrungsergaenzungs-/Supplement-Anbieter", 10),
    ("Gesundheits-/OTC-Produkt-Anbieter (Wellness, Kosmetik-nah)", 8),
    ("Grosshandel/Vertrieb medizinische Produkte & Hilfsmittel", 10),
    ("Gesundheits-Software / Health-IT / e-Health", 8),
    ("Spezialisierter Gesundheits-Dienstleister (Homecare, Hilfsmittelversorgung)", 6),
    ("Lohnhersteller / CMO fuer Pharma & Supplements", 6),
]

# --- Rollen ------------------------------------------------------------------
ROLLEN = [
    ("Geschaeftsfuehrung / Inhaber:in", 30),
    ("Bereichsleitung Operations", 12),
    ("Leitung Qualitaetsmanagement (QM/QA)", 14),
    ("Leitung Regulatory Affairs", 10),
    ("Leitung Vertrieb / Marketing", 12),
    ("Leitung Produktion / Logistik", 8),
    ("Kaufmaennische Leitung / Verwaltung", 8),
    ("Operativ verantwortlich (Projekt-/Teamleitung)", 6),
]

LAENDER = [("DE", 55), ("AT", 25), ("CH", 20)]

# Umsatzklassen grob an 10-50 MA gekoppelt
UMSATZ = [
    ("unter 1 Mio EUR", 10),
    ("1-3 Mio EUR", 25),
    ("3-7 Mio EUR", 28),
    ("7-15 Mio EUR", 22),
    ("15-30 Mio EUR", 12),
    ("30-50 Mio EUR", 3),
]

# Digitalisierungs-/Tech-Reife 1..5
TECH_REIFE = [
    (1, "arbeitet stark manuell, Papier/Excel dominiert, kaum Systeme", 18),
    (2, "einzelne Inselloesungen, viel Excel, wenig Integration", 27),
    (3, "etablierte Fachsysteme (ERP/QMS/CRM), aber getrennt, kaum Automatisierung", 27),
    (4, "gut digitalisiert, erste Automatisierungen, noch keine KI", 18),
    (5, "digital affin, erste KI-Pilotprojekte laufen bereits", 10),
]

# Haltung / Persoenlichkeit. Skeptisch/vorsichtig/desinteressiert bewusst >= 40 %.
HALTUNG = [
    ("aufgeschlossen", "neugierig auf Effizienzgewinne, aber nicht naiv", 22),
    ("pragmatisch-abwaegend", "interessiert nur bei klarem, belegbarem Nutzen", 30),
    ("neutral-vorsichtig", "grundsaetzlich offen, aber zurueckhaltend und abwartend", 16),
    ("regulatorisch-vorsichtig", "Compliance/Haftung stehen ueber allem, sehr risikoscheu", 14),
    ("skeptisch", "misstrauisch gegenueber Externen und KI-Versprechen", 12),
    ("desinteressiert", "sieht keinen Bedarf, wenig veraenderungsbereit, abweisend", 6),
]
SKEPTISCH_TAGS = {"neutral-vorsichtig", "regulatorisch-vorsichtig", "skeptisch", "desinteressiert"}

GESCHLECHT = [("weiblich", 42), ("maennlich", 55), ("divers", 3)]

VORNAMEN = {
    ("DE", "weiblich"): ["Sabine", "Katrin", "Nicole", "Andrea", "Julia", "Petra", "Christine", "Melanie", "Franziska", "Kerstin"],
    ("DE", "maennlich"): ["Thomas", "Michael", "Stefan", "Andreas", "Markus", "Jens", "Oliver", "Daniel", "Frank", "Sebastian"],
    ("AT", "weiblich"): ["Barbara", "Sandra", "Elisabeth", "Verena", "Bettina", "Michaela", "Cornelia", "Doris"],
    ("AT", "maennlich"): ["Gerald", "Wolfgang", "Christoph", "Reinhard", "Josef", "Bernhard", "Klaus", "Hannes"],
    ("CH", "weiblich"): ["Nadia", "Corinne", "Sabrina", "Franziska", "Regula", "Simone", "Claudia"],
    ("CH", "maennlich"): ["Marco", "Reto", "Beat", "Patrick", "Lukas", "Urs", "Fabian", "Roman"],
}


def _weighted(rng, items):
    """items: Liste von (wert, ..., gewicht) -- letztes Element ist Gewicht."""
    weights = [it[-1] for it in items]
    return rng.choices(items, weights=weights, k=1)[0]


def generate_personas(n=200, seed=SEED):
    rng = random.Random(seed)
    personas = []
    for i in range(n):
        branche = _weighted(rng, TEILBRANCHEN)[0]
        rolle = _weighted(rng, ROLLEN)[0]
        land = _weighted(rng, LAENDER)[0]
        umsatz = _weighted(rng, UMSATZ)[0]
        reife = _weighted(rng, TECH_REIFE)
        haltung = _weighted(rng, HALTUNG)
        geschlecht = _weighted(rng, GESCHLECHT)[0]

        # Mitarbeitende 10-50, grob an Umsatz gekoppelt
        lo, hi = 10, 50
        if "unter 1" in umsatz or "1-3" in umsatz:
            hi = 25
        elif "30-50" in umsatz:
            lo = 30
        mitarbeitende = rng.randint(lo, hi)

        alter = rng.randint(30, 62)

        gkey = geschlecht if geschlecht in ("weiblich", "maennlich") else rng.choice(["weiblich", "maennlich"])
        vorname = rng.choice(VORNAMEN[(land, gkey)])

        personas.append({
            "id": i + 1,
            "vorname": vorname,
            "geschlecht": geschlecht,
            "alter": alter,
            "land": land,
            "teilbranche": branche,
            "rolle": rolle,
            "mitarbeitende": mitarbeitende,
            "umsatzklasse": umsatz,
            "tech_reife": reife[0],
            "tech_reife_beschreibung": reife[1],
            "haltung": haltung[0],
            "haltung_beschreibung": haltung[1],
            "ist_skeptisch": haltung[0] in SKEPTISCH_TAGS,
        })
    return personas


if __name__ == "__main__":
    ps = generate_personas(200)
    import collections
    skept = sum(p["ist_skeptisch"] for p in ps)
    print(f"{len(ps)} Personas, davon {skept} skeptisch/vorsichtig/desinteressiert "
          f"({skept/len(ps)*100:.0f}%)")
    for key in ("teilbranche", "rolle", "land", "tech_reife", "haltung"):
        c = collections.Counter(p[key] for p in ps)
        print(f"\n== {key} ==")
        for k, v in c.most_common():
            print(f"  {v:3d}  {k}")
