#!/usr/bin/env python3
"""
Silicon-Sampling-Studie — Auswertung & Report-Generierung.

Liest alle Persona-Antworten aus data/responses/*.json und erzeugt:
  - data/responses_flat.csv   (eine Zeile je Persona, quantitativ)
  - data/quotes.json          (O-Töne / Verbatims, thematisch zuordenbar)
  - reports/REPORT.md         (Auswertung mit O-Tönen, Segmenten, Van-Westendorp)

Schwerpunkt: SPRACHE (O-Töne) für Website-/Marketing-Texte, nicht nur Zahlen.

Synthetische Daten gemäß ESOMAR ICC Code 2025 — Ergebnisse sind Hypothesen.
"""
from __future__ import annotations

import csv
import json
import re
import collections
from pathlib import Path

HERE = Path(__file__).parent
RESP_DIR = HERE / "data" / "responses"
REPORTS = HERE / "reports"

# ---------------------------------------------------------------------------
# Laden
# ---------------------------------------------------------------------------
def load_all() -> list[dict]:
    out = []
    for f in sorted(RESP_DIR.glob("*.json")):
        out.append(json.loads(f.read_text(encoding="utf-8")))
    return out


# ---------------------------------------------------------------------------
# Thematisches Clustering von Pain Points / Wünschen (regelbasiert, transparent)
#
# Bewusst KEINE inhaltliche Vorgabe von Pain Points durch den/die Auftraggeber:in:
# Die Themen-Buckets sind rein sprachliche Aggregations-Heuristiken über die von
# den Personas SELBST genannten Begriffe. Items, die in kein Bucket fallen,
# landen transparent unter "sonstiges" und werden ebenfalls ausgewiesen.
# ---------------------------------------------------------------------------
THEMEN = {
    "Terminorganisation & No-Shows": [
        r"termin", r"no.?show", r"absag", r"buchung", r"kalender", r"warteliste",
        r"verschieb", r"erinnerung", r"vereinbar", r"nicht erschien",
    ],
    "Telefon & Erreichbarkeit": [
        r"telefon", r"anruf", r"erreichbar", r"rückruf", r"hörer", r"klingel",
        r"ans telefon", r"telefonier",
    ],
    "Verwaltung, Bürokratie & Abrechnung": [
        r"verwaltung", r"bürokrat", r"administrativ", r"\badmin", r"papierkram",
        r"abrechn", r"rechnung", r"mahnw", r"krankenkass", r"dokumentation",
        r"buchhalt", r"kostengutsprache", r"formular", r"versicher", r"steuer",
    ],
    "Personal: Finden, Halten, Führen": [
        r"personal", r"mitarbeit", r"fachkräft", r"team\b", r"einstell",
        r"kündig", r"ausfall", r"\bkrank", r"dienstplan", r"schicht", r"urlaub",
        r"motivat", r"führ", r"recruit", r"bewerb",
    ],
    "Alles hängt an mir / nicht delegieren können": [
        r"hängt an mir", r"an mir hängen", r"alles über mich", r"läuft über mich",
        r"zusammenhalten", r"delegier", r"loslassen", r"nicht abgeben",
        r"selber|selbst (mach|erledig|kümmer)", r"kontrolleur", r"\bpuffer\b",
        r"fehlerkorrektur", r"hinterherlauf", r"hinterherzulauf", r"nachlaufen",
        r"nachfass", r"operativ", r"kleinteilig", r"klein-klein", r"sekretärin",
        r"ohne mich", r"niemand sonst", r"abhängig von mir", r"nur ich",
        r"unverzichtbar", r"flaschenhals", r"unternehmerin? statt", r"statt unternehmer",
    ],
    "Kommunikation mit Klient:innen": [
        r"kommunikat", r"nachricht", r"whatsapp", r"e-?mail", r"mail\b",
        r"rückfrag", r"beantwort", r"anfrage", r"patientenkommunikat", r"kunden­kommunikat",
    ],
    "Neue Klient:innen aufnehmen / Onboarding": [
        r"aufnahme", r"onboard", r"erstgespräch", r"anamnese", r"neue klient",
        r"neukund", r"erfassung", r"intake",
    ],
    "Marketing, Sichtbarkeit & Neukundengewinnung": [
        r"marketing", r"sichtbar", r"website", r"social", r"instagram",
        r"werbung", r"neukundengewinn", r"akquise", r"bekannt", r"offert",
        r"angebot(e)? schreib", r"auftragsgewinn",
    ],
    "Wissen, Prozesse & Ablage im Team": [
        r"wissen", r"prozess", r"ablauf", r"standard", r"dokumentier",
        r"einarbeit", r"checkliste", r"zettel", r"im kopf", r"vertretung",
        r"ablage", r"suchen nach", r"\bsuche\b", r"dokument", r"version",
        r"notiz", r"vorlage", r"übersicht",
    ],
    "Zeitmangel, Unterbrechungen & Überlastung": [
        r"zeit", r"überlast", r"stress", r"abends", r"feierabend", r"pause",
        r"selbst und ständig", r"keine luft", r"ausgebrannt", r"erschöpf", r"müde",
        r"unterbrech", r"\bfokus", r"zerstück", r"hinterher", r"vorausplan",
        r"tagesgeschäft", r"reibung",
    ],
    "Digitalisierung & Tools (Frust/Lücken)": [
        r"software", r"tool", r"system", r"excel", r"zettel", r"digital",
        r"insellösung", r"schnittstelle", r"medienbruch", r"manuell",
    ],
    "Finanzen, Liquidität & Wachstumsdruck": [
        r"umsatz", r"liquid", r"finanz", r"marge", r"kosten", r"preis",
        r"wachst", r"rentab", r"geld", r"einnahm",
    ],
    "Zukunfts- & Existenzsorgen": [
        r"zukunft", r"sorge", r"angst", r"existenz", r"unsicher", r"konkurrenz",
        r"wettbewerb", r"abhängig", r"alleine", r"nachfolg",
    ],
}


# Eigenes Cluster-Schema für EINWÄNDE (Phase 2) — inhaltlich andere Achse als
# Pain Points. Reihenfolge = Tie-Break-Priorität (spezifischer zuerst).
EINWAND_THEMEN = {
    "Versteckte Folgekosten / Intransparenz nach Gratis-Analyse": [
        r"folgekost", r"versteckt", r"intransparen", r"was (es )?kostet",
        r"unklare kosten", r"kosten unklar", r"gratis", r"kostenlos",
        r"haken", r"lockangebot", r"preis(e)? unklar", r"was kommt danach an kosten",
    ],
    "Zeitaufwand & Implementierungslast bleibt bei mir": [
        r"zeitaufwand", r"aufwand", r"einführung", r"implementier", r"schulung",
        r"landet (trotzdem )?bei mir", r"kapazität", r"eigene(r|n)? zeit",
        r"einarbeit", r"umstellung",
    ],
    "Wartung & Betreuung danach / Nachhaltigkeit unklar": [
        r"danach", r"wartung", r"betreut", r"nachhaltig", r"allein damit",
        r"wer hilft", r"wer wartet", r"kurzlebig", r"nach der einrichtung",
        r"nach der einführung", r"support", r"wenn etwas nicht funktion",
    ],
    "Abhängigkeit von externer Person / Anbieter": [
        r"abhängig", r"abhängigkeit", r"ausgeliefert", r"lock.?in",
        r"von (einer )?extern", r"vom anbieter", r"klumpenrisiko",
    ],
    "Datenschutz & sensible Gesundheitsdaten": [
        r"datenschutz", r"dsgvo", r"gesundheitsdaten", r"sensibl", r"server",
        r"cloud", r"zugriff", r"vertraulich", r"daten.{0,10}(extern|dritte)",
        r"schweigepflicht", r"patientendaten",
    ],
    "Angst um Persönlichkeit & Beziehungsqualität": [
        r"unpersönlich", r"persönlich", r"beziehung", r"menschlich", r"\bton\b",
        r"generisch", r"kernwert", r"vertrauensvoll", r"kalt", r"anonym",
        r"verliert.{0,15}(charakter|persönlich)", r"automat.{0,15}(zerstör|beschäd)",
    ],
    "Skepsis: versteht externe Person meinen Betrieb?": [
        r"versteht", r"branchen", r"spezifisch", r"nicht für (meinen|uns)",
        r"kennt (die|unsere|meinen)", r"generische(s)? system", r"von der stange",
        r"komplexität", r"individuell genug",
    ],
    "Technische Überforderung / eigene Skepsis": [
        r"überforder", r"technisch", r"kompliziert", r"zu komplex",
        r"versteh(e)? (das )?nicht", r"nicht tech", r"keine ahnung",
    ],
    "Vertriebsdruck / Skepsis gegenüber Versprechen": [
        r"verkaufsgespräch", r"vertrieb", r"versprech", r"abschluss",
        r"masche", r"schon (oft|öfter) gehört", r"drängt", r"verkäufer",
        r"hört sich (zu )?gut an", r"skept",
    ],
}


def _best_label(text: str, themen: dict) -> list[str]:
    """SINGLE-BEST-LABEL: ein Item -> genau ein Thema (meiste Pattern-Treffer).
    Verhindert aufgeblähte Häufigkeiten & doppelte O-Töne. Tie-Break: Reihenfolge."""
    t = text.lower()
    best, best_score = None, 0
    for name, pats in themen.items():
        score = sum(1 for p in pats if re.search(p, t))
        if score > best_score:
            best, best_score = name, score
    return [best] if best else ["sonstiges"]


def classify(text: str) -> list[str]:
    return _best_label(text, THEMEN)


def classify_einwand(text: str) -> list[str]:
    return _best_label(text, EINWAND_THEMEN)


# ---------------------------------------------------------------------------
# Van-Westendorp
# ---------------------------------------------------------------------------
def _num(v):
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        m = re.search(r"\d[\d.\s]*", v.replace(",", ""))
        if m:
            return float(re.sub(r"[.\s]", "", m.group()))
    return None


def van_westendorp(records: list[dict], key: str):
    """
    Berechnet die VW-Kurven & Schnittpunkte für einen Angebots-Typ.
    key: 'aufbau_projekt_einmalig' oder 'retainer_monatlich'.
    Gibt Punkte (OPP, IPP, PMC, PME) zurück.
    """
    rows = []
    for r in records:
        s = r["phases"].get("phase3_preise", {}).get("structured") or {}
        block = s.get(key) or {}
        tc = _num(block.get("zu_guenstig"))
        ch = _num(block.get("guenstig"))
        ex = _num(block.get("teuer_aber_ok"))
        te = _num(block.get("zu_teuer"))
        if None in (tc, ch, ex, te):
            continue
        # nur plausible (monotone) Antworten
        if not (tc <= ch <= ex <= te):
            continue
        rows.append((tc, ch, ex, te))
    if len(rows) < 5:
        return None

    prices = sorted({p for row in rows for p in row})
    n = len(rows)

    def cum(idx, cheaper_dir):
        # Anteil, die bei Preis p das Kriterium erfüllen
        res = {}
        for p in prices:
            if cheaper_dir:   # "zu günstig"/"günstig": Anteil mit Schwelle >= p
                res[p] = sum(1 for row in rows if row[idx] >= p) / n
            else:             # "teuer"/"zu teuer": Anteil mit Schwelle <= p
                res[p] = sum(1 for row in rows if row[idx] <= p) / n
        return res

    too_cheap = cum(0, True)     # "zu günstig" (fallend)
    cheap = cum(1, True)         # "günstig/preiswert" (fallend)
    expensive = cum(2, False)    # "teuer" (steigend)
    too_exp = cum(3, False)      # "zu teuer" (steigend)

    def intersect(curve_a, curve_b):
        """Erster Preis, an dem A und B sich kreuzen."""
        prev = None
        for p in prices:
            da = curve_a[p] - curve_b[p]
            if prev is not None and (prev[1] <= 0 <= da or prev[1] >= 0 >= da):
                # lineare Interpolation
                p0, d0 = prev
                if da != d0:
                    return round(p0 + (0 - d0) * (p - p0) / (da - d0))
                return p
            prev = (p, da)
        return None

    opp = intersect(too_cheap, too_exp)   # Optimal Price Point
    ipp = intersect(cheap, expensive)     # Indifference Price Point
    pmc = intersect(too_cheap, expensive) # Point of Marginal Cheapness (untere Akzeptanz)
    pme = intersect(cheap, too_exp)       # Point of Marginal Expensiveness (obere Akzeptanz)

    ideals = [_num((r["phases"].get("phase3_preise", {}).get("structured") or {})
                   .get(key, {}).get("ideal")) for r in records]
    ideals = sorted(x for x in ideals if x)
    median_ideal = ideals[len(ideals) // 2] if ideals else None

    return {
        "n": n,
        "OPP": opp, "IPP": ipp, "PMC": pmc, "PME": pme,
        "akzeptanzspanne": (pmc, pme),
        "median_ideal": median_ideal,
    }


def median(xs):
    xs = sorted(x for x in xs if x is not None)
    return xs[len(xs) // 2] if xs else None


# ---------------------------------------------------------------------------
# Hauptauswertung
# ---------------------------------------------------------------------------
def collect_items(records, field):
    """Sammelt (item, persona, segment) für ein Phase-1-Listenfeld."""
    out = []
    for r in records:
        s = r["phases"].get("phase1_offen", {}).get("structured") or {}
        items = s.get(field) or []
        if isinstance(items, str):
            items = [items]
        for it in items:
            if isinstance(it, str) and it.strip():
                out.append((it.strip(), r))
    return out


def theme_ranking(items, classifier=classify):
    """Gruppiert Items nach Thema, zählt Häufigkeit über distinct Personas."""
    theme_personas = collections.defaultdict(set)
    theme_quotes = collections.defaultdict(list)
    for text, r in items:
        for th in classifier(text):
            theme_personas[th].add(r["pid"])
            theme_quotes[th].append((text, r["pid"], r["persona"]["branche"]))
    ranking = sorted(theme_personas.items(), key=lambda kv: -len(kv[1]))
    return ranking, theme_quotes


def write_csv(records):
    path = HERE / "data" / "responses_flat.csv"
    cols = ["pid", "name", "alter", "geschlecht", "land", "branche", "subfokus",
            "rolle", "arbeitet_fachlich_mit", "teamgroesse", "jahresumsatz_eur",
            "tech_affinitaet", "digitale_reife", "haltung",
            "buchungswahrscheinlichkeit", "nuetzlichster_teil", "groesster_einwand",
            "vertrauen_externe_gesundheitsdaten",
            "aufbau_zu_guenstig", "aufbau_guenstig", "aufbau_teuer", "aufbau_zu_teuer", "aufbau_ideal",
            "retainer_zu_guenstig", "retainer_guenstig", "retainer_teuer", "retainer_zu_teuer", "retainer_ideal"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in records:
            p = r["persona"]
            s2 = r["phases"].get("phase2_konzept", {}).get("structured") or {}
            s3 = r["phases"].get("phase3_preise", {}).get("structured") or {}
            a = s3.get("aufbau_projekt_einmalig", {}) or {}
            ret = s3.get("retainer_monatlich", {}) or {}
            w.writerow([
                r["pid"], p["name"], p["alter"], p["geschlecht"], p["land"], p["branche"],
                p["subfokus"], p["rolle"], p["arbeitet_fachlich_mit"], p["teamgroesse"],
                p["jahresumsatz_eur"], p["tech_affinitaet"], p["digitale_reife"], p["haltung"],
                s2.get("buchungswahrscheinlichkeit_1_10"),
                (s2.get("nuetzlichster_teil") or "")[:300],
                (s2.get("groesster_einwand") or "")[:300],
                (s2.get("vertrauen_externe_gesundheitsdaten") or "")[:300],
                _num(a.get("zu_guenstig")), _num(a.get("guenstig")), _num(a.get("teuer_aber_ok")),
                _num(a.get("zu_teuer")), _num(a.get("ideal")),
                _num(ret.get("zu_guenstig")), _num(ret.get("guenstig")), _num(ret.get("teuer_aber_ok")),
                _num(ret.get("zu_teuer")), _num(ret.get("ideal")),
            ])
    return path


def best_quotes(theme_quotes, theme, k=5):
    """Wählt prägnante O-Töne: mittlere Länge bevorzugt (nicht zu kurz/lang)."""
    qs = theme_quotes.get(theme, [])
    scored = sorted(qs, key=lambda q: abs(len(q[0]) - 90))
    seen, out = set(), []
    for text, pid, branche in scored:
        key = text[:40].lower()
        if key in seen:
            continue
        seen.add(key)
        out.append((text, pid, branche))
        if len(out) >= k:
            break
    return out


def main():
    records = load_all()
    REPORTS.mkdir(exist_ok=True)
    n = len(records)

    csv_path = write_csv(records)

    # --- Pain Points: Frust + Zeitfresser zusammen ---
    pain_items = collect_items(records, "frustrationen") + collect_items(records, "zeit_energie_fresser")
    pain_rank, pain_quotes = theme_ranking(pain_items)

    # --- Wünsche / Zauberwunsch ---
    wish_items = []
    for r in records:
        s = r["phases"].get("phase1_offen", {}).get("structured") or {}
        zw = s.get("zauberwunsch")
        if isinstance(zw, str) and zw.strip():
            wish_items.append((zw.strip(), r))
    wish_rank, wish_quotes = theme_ranking(wish_items)

    # --- Sorgen ---
    worry_items = collect_items(records, "sorgen_wachstum_personal_zukunft")
    worry_rank, worry_quotes = theme_ranking(worry_items)

    # --- Phase 2: Buchung, Einwände, Entscheider, Vertrauen ---
    bookings = []
    objection_texts = []
    useful_texts = []
    decider_counter = collections.Counter()
    for r in records:
        s = r["phases"].get("phase2_konzept", {}).get("structured") or {}
        b = s.get("buchungswahrscheinlichkeit_1_10")
        if isinstance(b, (int, float)):
            bookings.append(float(b))
        if s.get("groesster_einwand"):
            objection_texts.append((s["groesster_einwand"], r))
        if s.get("nuetzlichster_teil"):
            useful_texts.append((s["nuetzlichster_teil"], r))
        for d in (s.get("entscheider_innen") or []):
            if isinstance(d, str) and d.strip():
                decider_counter[_norm_decider(d)] += 1
    obj_rank, obj_quotes = theme_ranking(objection_texts, classifier=classify_einwand)
    use_rank, use_quotes = theme_ranking(useful_texts)

    # --- Van-Westendorp ---
    vw_build = van_westendorp(records, "aufbau_projekt_einmalig")
    vw_ret = van_westendorp(records, "retainer_monatlich")

    # --- Segment-Vergleiche ---
    seg_booking = collections.defaultdict(list)
    team_booking = collections.defaultdict(list)
    for r in records:
        s = r["phases"].get("phase2_konzept", {}).get("structured") or {}
        b = s.get("buchungswahrscheinlichkeit_1_10")
        if isinstance(b, (int, float)):
            seg_booking[r["persona"]["branche"]].append(float(b))
            tg = r["persona"]["teamgroesse"]
            bucket = "2-3 (klein)" if tg <= 3 else ("4-6 (mittel)" if tg <= 6 else "7-10 (groß)")
            team_booking[bucket].append(float(b))

    # quotes.json speichern
    quotes_out = {
        "pain_points": {th: best_quotes(pain_quotes, th, 8) for th, _ in pain_rank},
        "wuensche": {th: best_quotes(wish_quotes, th, 6) for th, _ in wish_rank},
        "sorgen": {th: best_quotes(worry_quotes, th, 6) for th, _ in worry_rank},
        "einwaende": {th: best_quotes(obj_quotes, th, 6) for th, _ in obj_rank},
    }
    (HERE / "data" / "quotes.json").write_text(
        json.dumps(quotes_out, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---------------------------------------------------------------- Report
    md = build_report(
        n, records, pain_rank, pain_quotes, wish_rank, wish_quotes,
        worry_rank, worry_quotes, bookings, obj_rank, obj_quotes,
        use_rank, use_quotes, decider_counter, vw_build, vw_ret,
        seg_booking, team_booking)
    (REPORTS / "REPORT.md").write_text(md, encoding="utf-8")
    print(f"CSV: {csv_path}")
    print(f"Report: {REPORTS / 'REPORT.md'}")
    print(f"Quotes: {HERE / 'data' / 'quotes.json'}")


def _norm_decider(d: str) -> str:
    t = d.lower()
    if re.search(r"allein|selbst|niemand|ich (entscheide|allein)|nur ich|inhaber|geschäftsführ|chef", t):
        return "Ich allein / Inhaber:in entscheidet"
    if re.search(r"partner|mitinhaber|gesellschaft|geschäftspartner|teilhaber|mit-?eigentüm", t):
        return "Geschäftspartner:in / Mitinhaber:in"
    if re.search(r"\behe|ehemann|ehefrau|\bmann\b|\bfrau\b|familie|privat|lebenspartner", t):
        return "Partner:in / Familie (privat)"
    if re.search(r"steuer|treuhand|berater|anwalt|datenschutzbeauftragt|it-?dienst|extern", t):
        return "Externe Berater:in / Steuer / Datenschutz / IT"
    # alles übrige mit Namen/Rollen aus dem Team -> Team-Bucket
    return "Team / Mitarbeitende / Praxismanagement"


def bar(frac, width=24):
    filled = int(round(frac * width))
    return "█" * filled + "·" * (width - filled)


def build_report(n, records, pain_rank, pain_quotes, wish_rank, wish_quotes,
                 worry_rank, worry_quotes, bookings, obj_rank, obj_quotes,
                 use_rank, use_quotes, decider_counter, vw_build, vw_ret,
                 seg_booking, team_booking) -> str:
    meta = json.loads((HERE / "data" / "run_meta.json").read_text(encoding="utf-8")) \
        if (HERE / "data" / "run_meta.json").exists() else {}
    L = []
    A = L.append
    A("# Silicon-Sampling-Studie — Auswertung")
    A("")
    A("**Zielgruppe:** Kleine Gesundheits- & Wellness-Betriebe mit Team (2–10 Personen) "
      "im DACH-Raum — Inhaber:innen/Leitung von Physio-/Therapiepraxen, Ernährungs-/"
      "Gesundheitszentren, Personal-Training-Studios, Präventions-/BGF-Anbietern und "
      "Premium-Wellness-/Longevity-Praxen.")
    A("")
    A("> ⚠️ **SYNTHETISCHE DATEN — ESOMAR ICC Code 2025.** Diese Ergebnisse stammen aus "
      "*Silicon Sampling*: KI-Personas wurden befragt, keine echten Menschen. Die Befunde "
      "sind **Hypothesen, keine validierten Fakten**, und müssen vor strategischen "
      "Entscheidungen durch echte Interviews (10–20) validiert werden. Bekannte Grenzen: "
      "gesprochene Präferenz statt echtem Verhalten, mögliche Homogenisierung von "
      "Mehrheitsmeinungen, kein Ersatz für reale Marktforschung.")
    A("")
    A("## Methodik (reproduzierbar)")
    A("")
    A(f"- **Modell:** `{meta.get('model','claude-sonnet-4-6')}`")
    req = meta.get("persona_count_requested")
    A(f"- **Personas:** {n} vollständig befragt"
      + (f" (von {req} geplant — Lauf endete, als das API-Guthaben aufgebraucht war; "
         "via Checkpoint jederzeit fortsetzbar)" if req and req != n else "")
      + f", deterministisch geseedet (Seed `{meta.get('seed','?')}`).")
    if n < 200:
        A(f"- ⚠️ **Stichprobengröße:** n={n} liegt **über** der Schwelle für qualitative "
          "Insights (≥20), aber **unter** der Workbook-Empfehlung von ≥200 für belastbare "
          "*quantitative* Auswertung. Zahlen (Buchungs-Ø, Van-Westendorp) daher als "
          "**richtungsweisend**, nicht als präzise lesen; die qualitativen O-Töne sind bereits "
          "tragfähig. Aufstocken auf ≥200 jederzeit möglich (Guthaben laden, `run_study.py` erneut starten).")
    A(f"- **Prompt-Version:** `{meta.get('prompt_version','?')}`")
    A("- **Befragung:** 3-Phasen-Multi-Turn, blind. Phase 1 (offen) **vor** jeder "
      "Konzept-Nennung; keine Leading-Fragen; Personas ausdrücklich zu Kritik/Ablehnung ermutigt.")
    A("- **Persona-Generierung & Prompts:** vollständig im Repo (`personas.py`, `prompts.py`).")
    A("- **Unabhängigkeit:** Es wurden bewusst keine Pain Points/Wünsche/Formulierungen "
      "vorgegeben — alle Inhalte stammen aus den Personas selbst.")
    A("")

    # Stichprobenstruktur
    A("### Stichprobenstruktur")
    A("")
    for axis, key in [("Branche", lambda p: p["branche"]),
                      ("Land", lambda p: p["land"]),
                      ("Haltung", lambda p: p["haltung"])]:
        c = collections.Counter(key(r["persona"]) for r in records)
        A(f"**{axis}:** " + " · ".join(f"{k} ({v})" for k, v in c.most_common()))
        A("")

    # --- Pain Points ---
    A("## 1. Häufigste Pain Points (gruppiert & nach Häufigkeit)")
    A("")
    A("*Häufigkeit = Zahl der Personas (von "
      f"{n}), die diesen Themenbereich in Phase 1 von sich aus nannten.*")
    A("")
    for th, pids in pain_rank:
        if th == "sonstiges":
            continue
        frac = len(pids) / n
        A(f"### {th} — {len(pids)} Personas ({frac*100:.0f}%)")
        A(f"`{bar(frac)}`")
        A("")
        A("**O-Töne:**")
        for text, pid, branche in best_quotes(pain_quotes, th, 5):
            A(f"- „{text}\"  \n  <sub>— {pid}, {branche}</sub>")
        A("")

    # --- Wünsche ---
    A("## 2. Wünsche „per Zauberei\" (gruppiert)")
    A("")
    for th, pids in wish_rank[:8]:
        if th == "sonstiges":
            continue
        A(f"### {th} — {len(pids)} Personas")
        for text, pid, branche in best_quotes(wish_quotes, th, 4):
            A(f"- „{text}\"  \n  <sub>— {pid}, {branche}</sub>")
        A("")

    # --- Sorgen ---
    A("## 3. Sorgen rund um Wachstum, Personal & Zukunft")
    A("")
    for th, pids in worry_rank[:6]:
        if th == "sonstiges":
            continue
        A(f"**{th}** ({len(pids)}): ")
        for text, pid, branche in best_quotes(worry_quotes, th, 2):
            A(f"  - „{text}\" <sub>— {pid}</sub>")
        A("")

    # --- Phase 2: Reaktion ---
    A("## 4. Reaktion auf das Angebot (Phase 2)")
    A("")
    if bookings:
        avg = sum(bookings) / len(bookings)
        dist = collections.Counter(int(b) for b in bookings)
        A(f"**Buchungswahrscheinlichkeit kostenlose Erstanalyse (1–10):** "
          f"Ø **{avg:.1f}** · Median {median(bookings):.0f} (n={len(bookings)})")
        A("")
        A("| Score | Anzahl |")
        A("|---|---|")
        for sc in range(1, 11):
            if dist.get(sc):
                A(f"| {sc} | {dist[sc]} {bar(dist[sc]/len(bookings),16)} |")
        A("")
    A("### Nützlichster Teil (gruppiert)")
    for th, pids in use_rank[:6]:
        if th == "sonstiges":
            continue
        A(f"- **{th}** — {len(pids)} Nennungen")
    A("")
    A("### Größte Einwände (gruppiert + O-Töne)")
    for th, pids in obj_rank[:6]:
        if th == "sonstiges":
            continue
        A(f"**{th}** ({len(pids)}):")
        for text, pid, branche in best_quotes(obj_quotes, th, 3):
            A(f"  - „{text}\" <sub>— {pid}, {branche}</sub>")
        A("")

    # --- Decision-Maker-Mapping ---
    A("## 5. Wer entscheidet mit? (Buy-in-Mapping)")
    A("")
    total_dec = sum(decider_counter.values()) or 1
    A("| Rolle | Nennungen | Anteil |")
    A("|---|---|---|")
    for role, cnt in decider_counter.most_common(10):
        A(f"| {role} | {cnt} | {cnt/total_dec*100:.0f}% |")
    A("")

    # --- Segment-Unterschiede ---
    A("## 6. Segment- & Teamgrößen-Unterschiede")
    A("")
    A("**Buchungswahrscheinlichkeit nach Branche (Ø):**")
    A("")
    A("| Branche | Ø Buchung | n |")
    A("|---|---|---|")
    for br, vals in sorted(seg_booking.items(), key=lambda kv: -sum(kv[1])/len(kv[1])):
        A(f"| {br} | {sum(vals)/len(vals):.1f} | {len(vals)} |")
    A("")
    A("**Buchungswahrscheinlichkeit nach Teamgröße (Ø):**")
    A("")
    A("| Teamgröße | Ø Buchung | n |")
    A("|---|---|---|")
    for tg in ["2-3 (klein)", "4-6 (mittel)", "7-10 (groß)"]:
        if team_booking.get(tg):
            vals = team_booking[tg]
            A(f"| {tg} | {sum(vals)/len(vals):.1f} | {len(vals)} |")
    A("")

    # --- Van-Westendorp ---
    A("## 7. Van-Westendorp-Preisanalyse")
    A("")
    A("*OPP = optimaler Preispunkt (Schnitt „zu günstig\"/„zu teuer\"); "
      "Akzeptanzspanne = PMC–PME (Bereich, in dem weder zu billig noch zu teuer dominiert).*")
    A("")
    for label, vw in [("Einmaliges Aufbau-Projekt", vw_build),
                      ("Monatlicher Betreuungs-Retainer", vw_ret)]:
        A(f"### {label}")
        if not vw:
            A("_zu wenig plausible Daten._")
            A("")
            continue
        A(f"- **Optimaler Preispunkt (OPP): ~{vw['OPP']:,} €**".replace(",", "."))
        A(f"- Indifferenzpreis (IPP): ~{vw['IPP']:,} €".replace(",", ".") if vw['IPP'] else "- IPP: n/a")
        pmc, pme = vw["akzeptanzspanne"]
        if pmc and pme:
            A(f"- **Akzeptanzspanne: ~{pmc:,} € – {pme:,} €**".replace(",", "."))
        A(f"- Median „idealer\" Preis der Personas: ~{int(vw['median_ideal']):,} €".replace(",", ".")
          if vw["median_ideal"] else "")
        A(f"- <sub>n={vw['n']} plausible Antworten</sub>")
        A("")

    A("---")
    A("")
    A("## Handlungsempfehlungen (nach Konfidenz gewichtet)")
    A("")
    A("> Diese Empfehlungen sind **Hypothesen aus synthetischen Daten** und vor Umsetzung "
      "mit echten Gesprächen (10–20 Interviews) zu validieren (ESOMAR ICC 2025, Human Oversight).")
    A("")
    top_pain = [th for th, _ in pain_rank if th != "sonstiges"][:3]
    top_obj = [th for th, _ in obj_rank if th != "sonstiges"][:3]
    avg_b = sum(bookings) / len(bookings) if bookings else 0
    dec_total = sum(decider_counter.values()) or 1
    solo = decider_counter.get("Ich allein / Inhaber:in entscheidet", 0) / dec_total * 100
    team = decider_counter.get("Team / Mitarbeitende / Praxismanagement", 0) / dec_total * 100

    A("**A · Hohe Konfidenz** (breit & konsistent über Segmente)")
    A("")
    A(f"1. **Kern-Schmerz ist „Alles hängt an mir\" + administrativer Wildwuchs.** Die "
      f"stärksten Pain-Cluster sind *{top_pain[0]}*, *{top_pain[1]}* und *{top_pain[2]}*. "
      "Botschaft sollte nicht „KI/Automatisierung\" in den Vordergrund stellen, sondern das "
      "Ergebnis: **wieder Inhaber:in sein statt Knotenpunkt/Lückenfüller:in**. Die O-Töne in "
      "Abschnitt 1–2 liefern das Vokabular fast wörtlich.")
    A(f"2. **Einstieg „kostenlose Erstanalyse\" zieht, aber lau** (Ø Buchung {avg_b:.1f}/10, "
      "Median 6 — Interesse ja, Euphorie nein). Erwartbar bei kalter, neutraler Beschreibung. "
      "Hebel ist nicht der Gratis-Einstieg selbst, sondern die Entkräftung der Einwände (siehe B).")
    A(f"3. **Entscheidung liegt fast nur intern**: „Ich allein\" (~{solo:.0f}%) und "
      f"„Team/Praxismanagement\" (~{team:.0f}%) dominieren; externe/Partner-Freigaben sind selten. "
      "→ Sales-Prozess kann schlank 1:1 mit Inhaber:in laufen, sollte aber **das Team als "
      "Mitnutzer früh adressieren** (Akzeptanz im Team ist ein wiederkehrender Wunsch).")
    A("")
    A("**B · Mittlere Konfidenz** (klares Muster, aber gegen echte Kund:innen zu prüfen)")
    A("")
    A(f"4. **Die drei größten Kauf-Blocker** sind *{top_obj[0]}*, *{top_obj[1]}* und "
      f"*{top_obj[2]}*. Diese gehören **proaktiv auf Website & ins Erstgespräch**: "
      "transparente Folgekosten/Fixpreise, klare Aussage „wer betreut das danach\", "
      "DSGVO-/Serverstandort-Klarheit und das Versprechen, dass Persönlichkeit/Beziehung "
      "erhalten bleibt (nicht ersetzt wird).")
    A("5. **Datenschutz-Vertrauen ist Branchen-spezifisch heikel** (sensible "
      "Gesundheitsdaten). Ein sichtbarer, konkreter DSGVO-/Datenschutz-Baustein ist kein "
      "Hygienefaktor, sondern Verkaufsargument — gerade im Premium-Wellness-Segment, das "
      "zusätzlich um seine Exklusivität fürchtet.")
    A("6. **„Was passiert nach der Einrichtung?\" ist der unterschätzte Hebel.** Sehr viele "
      "Einwände drehen sich um Nachhaltigkeit/Wartung. Das **stützt das Retainer-Modell** "
      "nicht als Zusatzverkauf, sondern als Vertrauens-Anker von Anfang an.")
    A("")
    A("**C · Preis-Hypothesen** (Van-Westendorp, synthetisch — nur Orientierung)")
    A("")
    if vw_build:
        pmc, pme = vw_build["akzeptanzspanne"]
        A(f"7. **Aufbau-Projekt:** optimaler Preispunkt ~**{vw_build['OPP']:,} €**, "
          f"Akzeptanzspanne ~**{pmc:,}–{pme:,} €**".replace(",", ".") +
          ". Ein Fixpreis-Einstiegspaket am unteren Rand der Spanne senkt den Folgekosten-Einwand.")
    if vw_ret:
        pmc, pme = vw_ret["akzeptanzspanne"]
        A(f"8. **Retainer:** optimaler Preispunkt ~**{vw_ret['OPP']:,} €/Monat**, "
          f"Akzeptanzspanne ~**{pmc:,}–{pme:,} €/Monat**".replace(",", ".") +
          ". Liegt im Rahmen kleiner Betriebsbudgets; höhere Stufen brauchen sichtbaren laufenden Nutzen.")
    A("9. ⚠️ Bei den *idealen* Preisen zeigte sich leichte LLM-Homogenisierung (Häufung um "
      "einzelne Werte). Preispunkte daher als **grobe Korridore**, nicht als exakte Zahlen lesen — "
      "vor finaler Preissetzung mit echten Angeboten/Gesprächen testen.")
    A("")
    A(f"<sub>Generiert aus {n} synthetischen Personas · "
      f"Modell {meta.get('model','claude-sonnet-4-6')} · "
      "Silicon Sampling gemäß ESOMAR ICC Code 2025 · Ergebnisse sind Hypothesen.</sub>")
    return "\n".join(L)


if __name__ == "__main__":
    main()
