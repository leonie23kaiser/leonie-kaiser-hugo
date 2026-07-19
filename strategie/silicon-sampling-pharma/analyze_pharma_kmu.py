#!/usr/bin/env python3
"""
Auswertung der Silicon-Sampling-Studie "Pharma- & Gesundheits-KMU".

Liest sampling_pharma_kmu.json (bzw. die Checkpoints) und erzeugt:
  - auswertung_pharma_kmu.json  (maschinenlesbar)
  - report_pharma_kmu.md        (lesbarer Report, ESOMAR-gekennzeichnet)

Schwerpunkte: Pain Points + woertliche O-Toene, Teilbranchen-Unterschiede,
Entscheider-Mapping, Van Westendorp (gesamt + je Teilbranche), Regulatorik.

Synthetische Daten gemaess ESOMAR ICC Code 2025 -- Hypothesen, keine Fakten.
"""
import os
import re
import glob
import json
import statistics
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CKPT_DIR = os.path.join(HERE, "checkpoints")
OUT_JSON = os.path.join(HERE, "auswertung_pharma_kmu.json")
OUT_MD = os.path.join(HERE, "report_pharma_kmu.md")

ESOMAR = ("> **⚠️ Synthetische Daten — ESOMAR ICC Code 2025.** Alle Ergebnisse stammen aus "
          "KI-Personas (Modell `claude-sonnet-4-6`), **nicht** aus echten Befragungen. Sie sind "
          "**Hypothesen, keine Fakten**, und ersetzen keine reale Marktforschung. Vor "
          "Investitions- oder Preisentscheidungen mit echten Interviews validieren.")


def load():
    rows = []
    for f in sorted(glob.glob(os.path.join(CKPT_DIR, "persona_*.json"))):
        with open(f, encoding="utf-8") as fh:
            rows.append(json.load(fh))
    return rows


# ---------------------------------------------------------------------------
# Van Westendorp
# ---------------------------------------------------------------------------

def vw_valid(d):
    """Gibt (tc, ch, ex, te) zurueck, wenn monoton zu_guenstig<guenstig<teuer<zu_teuer."""
    try:
        tc = float(d["zu_guenstig"]); ch = float(d["guenstig"])
        ex = float(d["teuer"]); te = float(d["zu_teuer"])
    except (TypeError, ValueError, KeyError):
        return None
    if not (0 < tc < ch < ex < te):
        return None
    return tc, ch, ex, te


def _cum_curves(vals):
    """vals: Liste von (tc,ch,ex,te). Liefert Preisgitter + 4 Kurven in %."""
    n = len(vals)
    prices = sorted({v for t in vals for v in t})
    curves = {"too_cheap": [], "cheap": [], "expensive": [], "too_expensive": []}
    for x in prices:
        # zu guenstig: Anteil, der Preis <= x als zu guenstig empfindet (fallend)
        tc = sum(1 for (a, b, c, d) in vals if x <= a) / n
        # guenstig (guenstig-oder-billiger): Anteil mit guenstig-Schwelle >= x (fallend)
        ch = sum(1 for (a, b, c, d) in vals if x <= b) / n
        # teuer: Anteil mit teuer-Schwelle <= x (steigend)
        ex = sum(1 for (a, b, c, d) in vals if x >= c) / n
        # zu teuer: Anteil mit zu-teuer-Schwelle <= x (steigend)
        te = sum(1 for (a, b, c, d) in vals if x >= d) / n
        curves["too_cheap"].append(tc)
        curves["cheap"].append(ch)
        curves["expensive"].append(ex)
        curves["too_expensive"].append(te)
    return prices, curves


def _intersect(prices, y1, y2):
    """Erster Schnittpunkt zweier monoton gegenlaeufiger Kurven (lineare Interpolation)."""
    for i in range(1, len(prices)):
        d0 = y1[i - 1] - y2[i - 1]
        d1 = y1[i] - y2[i]
        if d0 == 0:
            return prices[i - 1]
        if d0 * d1 < 0:
            t = d0 / (d0 - d1)
            return prices[i - 1] + t * (prices[i] - prices[i - 1])
    # kein Vorzeichenwechsel -> naehester Punkt
    idx = min(range(len(prices)), key=lambda i: abs(y1[i] - y2[i]))
    return prices[idx]


def van_westendorp(price_dicts):
    vals = [v for v in (vw_valid(d) for d in price_dicts) if v]
    if len(vals) < 5:
        return {"n_valide": len(vals)}
    prices, c = _cum_curves(vals)
    opp = _intersect(prices, c["too_cheap"], c["too_expensive"])   # Optimal Price Point
    ipp = _intersect(prices, c["cheap"], c["expensive"])            # Indifference Price Point
    pmc = _intersect(prices, c["too_cheap"], c["expensive"])        # Point of Marginal Cheapness
    pme = _intersect(prices, c["cheap"], c["too_expensive"])        # Point of Marginal Expensiveness
    idle = [t[1] for t in vals] + [t[2] for t in vals]  # zwischen guenstig..teuer
    return {
        "n_valide": len(vals),
        "OPP": round(opp),
        "IPP": round(ipp),
        "PMC": round(pmc),
        "PME": round(pme),
        "akzeptanzspanne": [round(pmc), round(pme)],
        "median_teuer_aber_ok": round(statistics.median([t[2] for t in vals])),
    }


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------

def _num(x):
    try:
        return int(round(float(x)))
    except (TypeError, ValueError):
        return None


PAIN_GROUPS = {
    "Dokumentation & Nachweispflichten": ["dokument", "nachweis", "template", "formular", "sop", "protokoll", "berichte", "papier"],
    "Regulatorik & Zulassung (MDR/IVDR/GMP)": ["regulat", "mdr", "ivdr", "gmp", "zulassung", "compliance", "audit", "swissmedic", "behoerd", "richtlinie", "guidance", "norm", "ce"],
    "Qualitaetsmanagement & QM-Prozesse": ["qm", "qualit", "capa", "abweichung", "pruef"],
    "Verwaltung & wiederkehrende Buerokratie": ["verwaltung", "buerokrat", "admin", "papierkram", "manuell", "excel", "doppelt", "mehrfach", "tippen"],
    "Personal, Fachkraefte & Wissensbindung": ["personal", "fachkraft", "fachkraefte", "recruit", "mitarbeit", "wissen", "onboard", "abhaengig", "schluesselperson", "fluktuation"],
    "IT-/Systemfragmentierung & Datensilos": ["system", "tool", "schnittstelle", "silo", "integration", "software", "insel", "medienbruch", "erp"],
    "Vertrieb, Kunden & Kommunikation": ["vertrieb", "kunde", "crm", "angebot", "kommunikation", "marketing", "anfrage", "lead"],
    "Kennzahlen, Finanzen & Steuerung": ["kennzahl", "controlling", "umsatz", "finanz", "liquid", "auslastung", "reporting", "transparenz"],
    "Wachstum, Skalierung & Nachfolge": ["wachstum", "skalier", "nachfolge", "uebergabe", "expansion"],
    "Lieferkette, Logistik & Beschaffung": ["liefer", "logist", "beschaffung", "lager", "bestand", "supply"],
}


def classify_pain(tag, quote):
    """Ordnet einen Pain Point GENAU EINER besten Kategorie zu (Tag staerker
    gewichtet als das Zitat), damit Haeufigkeiten nicht durch Mehrfachtreffer
    aufgeblaeht werden."""
    tl = (tag or "").lower()
    ql = (quote or "").lower()
    best, best_score = "Sonstiges", 0
    for grp, kws in PAIN_GROUPS.items():
        score = sum(3 for k in kws if k in tl) + sum(1 for k in kws if k in ql)
        if score > best_score:
            best, best_score = grp, score
    return best


def analyze(rows):
    n = len(rows)
    by_branche = defaultdict(list)
    for r in rows:
        by_branche[r["persona"]["teilbranche"]].append(r)

    # --- Pain Points gruppiert + O-Toene ---
    pain_counter = Counter()
    pain_quotes = defaultdict(list)
    pain_by_branche = defaultdict(Counter)
    for r in rows:
        seen = set()
        br = r["persona"]["teilbranche"]
        for pp in r["structured"].get("pain_points", []) or []:
            grp = classify_pain(pp.get("tag", ""), pp.get("quote", ""))
            if grp not in seen:
                pain_counter[grp] += 1          # je Persona max. 1 pro Gruppe
                pain_by_branche[br][grp] += 1
                seen.add(grp)
            q = (pp.get("quote") or "").strip()
            if q and len(q) > 15:
                pain_quotes[grp].append(q)

    # --- Wuensche ---
    wish_counter = Counter()
    for r in rows:
        for w in r["structured"].get("wuensche", []) or []:
            wish_counter[(w or "").strip()[:120]] += 1

    # --- Buchung / Vertrauen / Regulatorik ---
    def collect(field_path):
        out = []
        for r in rows:
            cur = r["structured"]
            for k in field_path:
                cur = (cur or {}).get(k) if isinstance(cur, dict) else None
            v = _num(cur)
            if v is not None:
                out.append(v)
        return out

    booking = collect(["phase2", "buchungswahrscheinlichkeit"])
    trust = collect(["phase2", "vertrauen_score"])
    reg = collect(["regulatorik", "huerde_score"])
    digi = collect(["digitalreife_geaeussert"])
    levels = collect(["phase2", "entscheidungsebenen"])

    # Entscheider-Rollen
    dec_counter = Counter()
    for r in rows:
        for d in r["structured"].get("phase2", {}).get("entscheider", []) or []:
            dec_counter[(d or "").strip()] += 1

    # Grundstimmung
    mood = Counter(r["structured"].get("grundstimmung", "n/a") for r in rows)

    # Regulatorik-Vertrauensbildner
    reg_builders = Counter()
    reg_quotes = []
    for r in rows:
        for b in r["structured"].get("regulatorik", {}).get("vertrauensbildner", []) or []:
            reg_builders[(b or "").strip()[:80]] += 1
        zq = r["structured"].get("regulatorik", {}).get("zitat")
        if zq and len(zq) > 20:
            reg_quotes.append(zq.strip())

    # Van Westendorp gesamt
    vw_proj = van_westendorp([r["structured"]["phase3"]["projekt_einmalig"] for r in rows])
    vw_ret = van_westendorp([r["structured"]["phase3"]["retainer_monatlich"] for r in rows])

    # Van Westendorp + Kennzahlen je Teilbranche
    seg = {}
    for br, rs in sorted(by_branche.items(), key=lambda kv: -len(kv[1])):
        b_book = [_num(x["structured"]["phase2"].get("buchungswahrscheinlichkeit")) for x in rs]
        b_book = [x for x in b_book if x is not None]
        b_reg = [_num(x["structured"].get("regulatorik", {}).get("huerde_score")) for x in rs]
        b_reg = [x for x in b_reg if x is not None]
        b_digi = [_num(x["structured"].get("digitalreife_geaeussert")) for x in rs]
        b_digi = [x for x in b_digi if x is not None]
        seg[br] = {
            "n": len(rs),
            "buchung_avg": round(statistics.mean(b_book), 1) if b_book else None,
            "regulatorik_huerde_avg": round(statistics.mean(b_reg), 1) if b_reg else None,
            "digitalreife_avg": round(statistics.mean(b_digi), 1) if b_digi else None,
            "vw_projekt": van_westendorp([x["structured"]["phase3"]["projekt_einmalig"] for x in rs]),
            "vw_retainer": van_westendorp([x["structured"]["phase3"]["retainer_monatlich"] for x in rs]),
            "top_pains": pain_by_branche[br].most_common(4),
        }

    return {
        "n": n,
        "pain_points": pain_counter.most_common(),
        "pain_quotes": {k: v for k, v in pain_quotes.items()},
        "wuensche_top": wish_counter.most_common(20),
        "booking": booking, "trust": trust, "reg": reg, "digi": digi, "levels": levels,
        "decision_roles": dec_counter.most_common(15),
        "mood": mood.most_common(),
        "reg_builders": reg_builders.most_common(15),
        "reg_quotes": reg_quotes,
        "vw_projekt": vw_proj,
        "vw_retainer": vw_ret,
        "segmente": seg,
    }


def best_quotes(quotes, k=5):
    """Dedupliziert und bevorzugt praegnante Saetze (~30-180 Zeichen) fuer Copy."""
    seen, uniq = set(), []
    for q in quotes:
        key = q.lower()[:60]
        if key in seen:
            continue
        seen.add(key)
        uniq.append(q)

    def score(q):
        n = len(q)
        if n < 30:
            return 3
        if n <= 180:
            return 0        # ideale Copy-Laenge
        if n <= 300:
            return 1
        return 2

    return sorted(uniq, key=score)[:k]


def stat(xs):
    if not xs:
        return "n/a"
    return f"Ø {statistics.mean(xs):.1f} (Median {statistics.median(xs):.0f}, n={len(xs)})"


def eur(v):
    return f"{v:,.0f} €".replace(",", ".") if isinstance(v, (int, float)) else "n/a"


def vw_line(vw):
    if vw.get("n_valide", 0) < 5:
        return f"zu wenige valide Antworten (n={vw.get('n_valide', 0)})"
    return (f"OPP **{eur(vw['OPP'])}** · IPP {eur(vw['IPP'])} · "
            f"Akzeptanzspanne {eur(vw['akzeptanzspanne'][0])}–{eur(vw['akzeptanzspanne'][1])} "
            f"(n valide {vw['n_valide']})")


def write_report(a, meta):
    L = []
    L.append("# Silicon Sampling — Pharma- & Gesundheits-KMU (DACH, 10–50 Mitarbeitende)\n")
    L.append(ESOMAR + "\n")
    L.append(f"*Modell: `claude-sonnet-4-6` · Personas ausgewertet: **{a['n']}** · "
             f"Methode: dreistufige blinde Mehrturn-Befragung (offen → Angebot → Van Westendorp) + "
             f"strukturierte Extraktion · Skeptiker-Quote bewusst > 40 %.*\n")
    L.append("**Zielgruppe:** " + meta.get("zielgruppe", "") + "\n")

    # Kennzahlen
    L.append("## Kernkennzahlen (gesamt)\n")
    L.append(f"- **Buchungswahrscheinlichkeit** kostenlose Erstanalyse (1–10): {stat(a['booking'])}")
    L.append(f"- **Vertrauen ggü. Externen** mit sensiblen Daten (1–5): {stat(a['trust'])}")
    L.append(f"- **Regulatorik-/Compliance-Hürde** (1–5): {stat(a['reg'])}")
    L.append(f"- **Digitalreife** (geäußert, 1–5): {stat(a['digi'])}")
    L.append(f"- **Entscheidungsebenen** je Deal (1–4): {stat(a['levels'])}")
    L.append("")
    L.append("**Van Westendorp (gesamt):**")
    L.append(f"- Einmaliges Aufbau-Projekt: {vw_line(a['vw_projekt'])}")
    L.append(f"- Monatlicher Betreuungs-Retainer: {vw_line(a['vw_retainer'])}")
    L.append("")
    L.append("**Grundstimmung der Personas:** " +
             ", ".join(f"{m} ({c})" for m, c in a["mood"]) + "\n")

    # Pain Points
    L.append("## Häufigste Pain Points (gruppiert, nach Häufigkeit)\n")
    L.append("*Unabhängig aus den Personas entstanden — keine Vorgabe. Zahl = Personas, die das Thema nannten.*\n")
    for grp, cnt in a["pain_points"]:
        share = cnt / a["n"] * 100
        L.append(f"### {grp} — {cnt} Nennungen ({share:.0f} %)")
        for q in best_quotes(a["pain_quotes"].get(grp, []), 5):
            L.append(f"> „{q}“")
        L.append("")

    # Wünsche
    L.append("## Wünsche / „per Zauberei sofort ändern“ (Top-Nennungen)\n")
    for w, c in a["wuensche_top"][:15]:
        L.append(f"- {w}" + (f" _(×{c})_" if c > 1 else ""))
    L.append("")

    # Segmentvergleich
    L.append("## Teilbranchen-Unterschiede\n")
    L.append("*Ausdrücklich die Unterschiede — Schmerz, Zahlungsbereitschaft, Digitalreife.*\n")
    L.append("| Teilbranche | n | Ø Buchung | Ø Reg.-Hürde | Ø Digitalreife | Projekt-OPP | Retainer-OPP |")
    L.append("|---|:--:|:--:|:--:|:--:|:--:|:--:|")
    for br, s in a["segmente"].items():
        po = s["vw_projekt"].get("OPP"); ro = s["vw_retainer"].get("OPP")
        L.append(f"| {br} | {s['n']} | {s['buchung_avg'] or 'n/a'} | "
                 f"{s['regulatorik_huerde_avg'] or 'n/a'} | {s['digitalreife_avg'] or 'n/a'} | "
                 f"{eur(po) if po else 'n/a'} | {eur(ro) if ro else 'n/a'} |")
    L.append("")
    L.append("### Dominante Pain Points je Teilbranche\n")
    for br, s in a["segmente"].items():
        pains = ", ".join(f"{g} ({c})" for g, c in s["top_pains"])
        L.append(f"- **{br}** (n={s['n']}): {pains}")
    L.append("")

    # Entscheider
    L.append("## Wer entscheidet, wer ist betroffen (Buy-in-Mapping)\n")
    L.append(f"Mittlere Entscheidungsebenen je Deal: {stat(a['levels'])}. "
             "Am häufigsten genannte mitentscheidende Rollen:\n")
    for role, c in a["decision_roles"]:
        L.append(f"- {role} _(×{c})_")
    L.append("")

    # Regulatorik
    L.append("## Regulatorik & Compliance als eigenes Thema\n")
    L.append(f"**Höhe der Hürde:** {stat(a['reg'])} auf Skala 1–5 "
             "(1 = kein Thema, 5 = maximaler Blocker).\n")
    L.append("**Was Vertrauen schaffen würde (Personas, nach Häufigkeit):**")
    for b, c in a["reg_builders"]:
        L.append(f"- {b} _(×{c})_")
    L.append("\n**O-Töne zu Datenschutz / Compliance:**")
    for q in a["reg_quotes"][:12]:
        L.append(f"> „{q}“")
    L.append("")

    # Methodik
    L.append("## Methodik & Reproduzierbarkeit\n")
    L.append(f"- **Modell:** `claude-sonnet-4-6` (Anthropic)")
    L.append(f"- **Personas:** {meta.get('personas_geplant', '?')} geplant, {a['n']} ausgewertet · Seed `{meta.get('seed')}`")
    L.append("- **Ablauf je Persona:** System-Prompt mit Persona-Attributen → Phase 1 (offen, "
             "vor jeder Konzept-Nennung) → Phase 2 (wörtlich vorgelesenes Angebot) → Phase 3 "
             "(Van-Westendorp-Preisschwellen) → strukturierte Extraktion (separater Analyse-Prompt).")
    L.append("- **Bias-Gegenmaßnahmen:** blinde/neutrale Fragen ohne Leading; Pain Points entstehen "
             "vor Konzept-Nennung; Skeptiker-Quote > 40 %; Personas dürfen ablehnen/desinteressiert sein.")
    L.append("- **Van Westendorp:** nur valide, monoton geordnete Antworten (zu_günstig < günstig "
             "< teuer < zu_teuer); OPP/IPP/PMC/PME per linearer Interpolation.")
    L.append("- **Rohdaten & Prompts:** `sampling_pharma_kmu.json` (inkl. vollständiger Prompts), "
             "Checkpoints je Persona unter `checkpoints/`.")
    L.append("- **Grenzen:** *geäußerte*, nicht *tatsächliche* Präferenzen; LLM-Homogenität kann "
             "Mehrheitsmeinungen überzeichnen; Preise sind Hypothesen, kein echter Markttest. "
             "Vor Entscheidungen mit 10–20 echten Interviews je Top-Segment validieren.")
    L.append("")
    L.append("<sub>Synthetische Marktforschung gemäß ESOMAR ICC Code 2025. KEINE echten "
             "Befragungsdaten. Ergebnisse sind Hypothesen.</sub>")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(L))


def main():
    rows = load()
    if not rows:
        raise SystemExit("Keine Checkpoints gefunden.")
    meta = {}
    sp = os.path.join(HERE, "sampling_pharma_kmu.json")
    if os.path.exists(sp):
        with open(sp, encoding="utf-8") as f:
            j = json.load(f)
        meta = {k: j.get(k) for k in ("zielgruppe", "seed", "personas_geplant")}
    a = analyze(rows)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(a, f, ensure_ascii=False, indent=1)
    write_report(a, meta)
    print(f"Ausgewertet: {a['n']} Personas -> {OUT_MD}")
    print("Buchung:", stat(a["booking"]), "| Reg-Hürde:", stat(a["reg"]))
    print("VW Projekt:", vw_line(a["vw_projekt"]))
    print("VW Retainer:", vw_line(a["vw_retainer"]))


if __name__ == "__main__":
    main()
