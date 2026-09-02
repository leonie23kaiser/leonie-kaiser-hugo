#!/usr/bin/env python3
"""
Silicon-Sampling-Pipeline -- Studie "Pharma- & Gesundheits-KMU (DACH, 10-50 MA)".

Dreistufige, blinde Mehrturn-Befragung je synthetischer Persona + strukturierte
Extraktion. Modell: claude-sonnet-4-6 (Anthropic). API-Calls parallelisiert,
je Persona ein Checkpoint => bei Abbruch geht nichts verloren.

    ANTHROPIC_API_KEY=... python3 run_pharma_kmu.py [N] [--workers W]

Synthetische Marktforschung gemaess ESOMAR ICC Code 2025. KEINE echten
Befragungsdaten. Ergebnisse sind Hypothesen, keine Fakten.
"""
import os
import re
import sys
import json
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

import anthropic

from personas import generate_personas, SEED

MODEL = "claude-sonnet-4-6"
HERE = os.path.dirname(os.path.abspath(__file__))
CKPT_DIR = os.path.join(HERE, "checkpoints")
OUT_FILE = os.path.join(HERE, "sampling_pharma_kmu.json")

ZIELGRUPPE = ("Kleine und mittlere Unternehmen aus der Pharma- und "
              "Gesundheitsbranche im deutschsprachigen Raum (AT/DE/CH), "
              "typischerweise 10-50 Mitarbeitende -- keine Grosskonzerne.")

# ---------------------------------------------------------------------------
# PROMPTS  (vollstaendig dokumentiert fuer Reproduzierbarkeit)
# ---------------------------------------------------------------------------

def persona_system_prompt(p):
    return f"""Du verkoerperst eine reale Person in einem anonymen Marktforschungs-Interview. Du bist NICHT ein KI-Assistent und brichst diese Rolle nie. Du weisst nicht, was der Interviewer verkaufen oder herausfinden will.

DEINE PERSON:
- Vorname: {p['vorname']} ({p['geschlecht']}, {p['alter']} Jahre, {p['land']})
- Rolle: {p['rolle']}
- Unternehmen: {p['teilbranche']}, {p['mitarbeitende']} Mitarbeitende, Umsatz {p['umsatzklasse']}
- Digitalisierungsreife: {p['tech_reife_beschreibung']} (Stufe {p['tech_reife']}/5)
- Grundhaltung: {p['haltung']} -- {p['haltung_beschreibung']}

WIE DU ANTWORTEST:
- In der Ich-Form, so wie DIESE Person wirklich reden wuerde -- im eigenen Ton (nuechtern, direkt, manchmal umgangssprachlich; {p['land']}-Faerbung erlaubt, aber nicht uebertreiben).
- Konkret und mit echten Details aus deinem Arbeitsalltag, KEINE Marketing- oder Beratersprache.
- Ehrlich gemaess deiner Grundhaltung. Wenn du skeptisch, vorsichtig oder desinteressiert bist, dann zeig das ehrlich -- beschoenige nichts, sei ruhig knapp oder abweisend. Sei KEIN gefaelliger Ja-Sager.
- Erfinde keine Begeisterung, die diese Person nicht haette. Reguliert-vorsichtige Menschen bleiben vorsichtig.
- Laenge: 4-9 Saetze pro Antwort, ausser die Frage verlangt Zahlen.
- Bleib strikt in der Rolle. Erwaehne nie, dass du eine KI oder Persona bist. Keine Meta-Kommentare."""


PHASE1 = """Dieses Gespraech ist anonym, es geht um nichts Bestimmtes -- ich moechte einfach Ihren Arbeitsalltag verstehen. Bitte antworten Sie offen:

Was frustriert Sie am meisten am FUEHREN und ORGANISIEREN Ihres Unternehmens -- also nicht am fachlichen Kerngeschaeft selbst, sondern am Drumherum? Welche Prozesse oder Aufgaben kosten Sie und Ihr Team am meisten Zeit oder Ressourcen, ohne dass es das eigentlich muesste? Welche Sorgen haben Sie mit Blick auf Wachstum, Personal, Regulatorik und die Zukunft? Und: Wenn Sie eine Sache per Zauberei sofort aendern koennten -- was waere das?"""


PHASE2 = """Danke. Jetzt beschreibe ich Ihnen kurz etwas -- voellig unverbindlich, sagen Sie mir einfach ehrlich, was Sie davon halten:

"Stellen Sie sich vor, jemand von aussen schaut sich Ihr Unternehmen genau an und richtet Ihnen -- datenschutz- und regulatorisch konform -- massgeschneiderte KI- und Automatisierungs-Systeme ein. Zum Beispiel fuer Dokumentation, Qualitaets- und Regulatory-Prozesse, Vertrieb und Kundenkommunikation, internes Wissensmanagement oder wiederkehrende Verwaltungsarbeit. Der Einstieg ist eine kostenlose Erstanalyse Ihres Unternehmens."

Bitte sagen Sie mir ehrlich:
1. Was waere -- wenn ueberhaupt -- der fuer Sie nuetzlichste Teil daran?
2. Was ist Ihr groesster Einwand oder Zweifel?
3. Wer in Ihrem Unternehmen muesste bei so etwas mitentscheiden?
4. Wie sehr wuerden Sie einem Externen ueberhaupt vertrauen, der mit Ihren sensiblen und regulierten Daten arbeitet?
5. Und ganz konkret: Wie wahrscheinlich ist es auf einer Skala von 1 bis 10, dass Sie so eine kostenlose Erstanalyse tatsaechlich buchen wuerden? Bitte nennen Sie eine Zahl und sagen Sie kurz, warum."""


PHASE3 = """Zuletzt noch zum Geld -- angenommen, Sie fuenden das Angebot grundsaetzlich passend. Es gaebe zwei Bestandteile: (A) ein EINMALIGES Aufbau-Projekt (Analyse + Einrichtung der Systeme) und (B) einen laufenden MONATLICHEN Betreuungs-Retainer.

Denken Sie an ein Unternehmens-Budget in Ihrer Branche und Groesse -- und daran, wie Beschaffung in einem regulierten Umfeld laeuft. Bitte nennen Sie fuer BEIDE Bestandteile jeweils vier konkrete Euro-Betraege:

Fuer das EINMALIGE Aufbau-Projekt:
- Zu teuer: So teuer, dass Sie es gar nicht in Betracht ziehen wuerden.
- Teuer, aber vertretbar: Teuer, aber Sie wuerden es noch ernsthaft ueberlegen.
- Guenstig: Ein gutes, attraktives Angebot.
- Zu guenstig: So billig, dass Sie an der Qualitaet zweifeln wuerden.

Fuer den MONATLICHEN Betreuungs-Retainer (pro Monat):
- Zu teuer / Teuer aber vertretbar / Guenstig / Zu guenstig (dieselbe Logik).

Bitte jeweils eine konkrete Zahl in Euro nennen -- auch wenn es nur ein grober Bauchwert ist. Wenn Sie zu einem Punkt ehrlich keine Zahl nennen wollen, sagen Sie das."""


EXTRACT_SYSTEM = """Du bist ein sorgfaeltiger Analyse-Assistent fuer Marktforschung. Du erhaeltst das Transkript eines dreistufigen Interviews mit einer Person. Extrahiere ausschliesslich, was die Person TATSAECHLICH gesagt hat. Erfinde nichts. Wenn eine Angabe fehlt, nutze null bzw. eine leere Liste. Zitate muessen WOERTLICH aus dem Transkript stammen (exakt, inkl. Formulierung der Person). Antworte NUR mit gueltigem JSON, ohne Kommentar, ohne Markdown-Zaun."""

EXTRACT_INSTR = """Extrahiere aus dem folgenden Interview-Transkript dieses JSON-Objekt (Werte auf Deutsch):

{
  "pain_points": [ {"tag": "kurzer Kategorie-Tag, 2-4 Woerter", "quote": "woertliches Zitat aus Phase 1"} ],
  "wuensche": ["kurze Stichpunkte, was die Person sich wuenscht / per Zauberei aendern wuerde"],
  "sorgen": ["Stichpunkte zu Wachstum/Personal/Regulatorik/Zukunft, die genannt wurden"],
  "phase2": {
    "nuetzlichster_teil": "kurze Zusammenfassung oder null",
    "groesster_einwand": "kurze Zusammenfassung oder null",
    "einwand_zitat": "woertliches Zitat oder null",
    "entscheider": ["genannte mitentscheidende Rollen, z.B. Geschaeftsfuehrung, QM-Leitung, Beirat"],
    "entscheidungsebenen": "ganze Zahl 1-4, wie viele Ebenen mitentscheiden muessen (Schaetzung aus Aussage)",
    "vertrauen_extern": "niedrig | mittel | hoch (Vertrauen ggue Externen mit sensiblen Daten)",
    "vertrauen_score": "ganze Zahl 1-5 (1=sehr misstrauisch, 5=sehr vertrauensvoll)",
    "buchungswahrscheinlichkeit": "ganze Zahl 1-10 oder null"
  },
  "phase3": {
    "projekt_einmalig": {"zu_teuer": Zahl|null, "teuer": Zahl|null, "guenstig": Zahl|null, "zu_guenstig": Zahl|null},
    "retainer_monatlich": {"zu_teuer": Zahl|null, "teuer": Zahl|null, "guenstig": Zahl|null, "zu_guenstig": Zahl|null}
  },
  "regulatorik": {
    "huerde_score": "ganze Zahl 1-5 (1=kein Thema, 5=maximale Huerde/Blocker)",
    "vertrauensbildner": ["was wuerde Vertrauen schaffen, falls genannt (z.B. Zertifikate, AV-Vertrag, Serverstandort, Referenzen)"],
    "zitat": "woertliches Zitat zu Datenschutz/Compliance oder null"
  },
  "digitalreife_geaeussert": "ganze Zahl 1-5 (wie digital/automatisiert wirkt der Betrieb laut Aussagen)",
  "grundstimmung": "enthusiastisch | offen | neutral | skeptisch | ablehnend"
}

Alle Euro-Betraege als reine Zahl ohne Waehrungszeichen/Tausenderpunkt (z.B. 5000, nicht \"5.000 EUR\"). Nur das JSON zurueckgeben.

TRANSKRIPT:
"""

PROMPTS_META = {
    "phase1": PHASE1,
    "phase2": PHASE2,
    "phase3": PHASE3,
    "extract_system": EXTRACT_SYSTEM,
    "extract_instruction": EXTRACT_INSTR,
    "persona_system_template": persona_system_prompt({
        "vorname": "<VORNAME>", "geschlecht": "<G>", "alter": "<A>", "land": "<L>",
        "rolle": "<ROLLE>", "teilbranche": "<BRANCHE>", "mitarbeitende": "<N>",
        "umsatzklasse": "<UMSATZ>", "tech_reife": "<R>",
        "tech_reife_beschreibung": "<REIFE_TEXT>", "haltung": "<HALTUNG>",
        "haltung_beschreibung": "<HALTUNG_TEXT>",
    }),
}

# ---------------------------------------------------------------------------
# API mit Backoff
# ---------------------------------------------------------------------------
_client = anthropic.Anthropic()
_print_lock = threading.Lock()


def _log(msg):
    with _print_lock:
        print(msg, flush=True)


def call(system, messages, max_tokens=900, tries=6):
    delay = 2.0
    for attempt in range(tries):
        try:
            r = _client.messages.create(
                model=MODEL, max_tokens=max_tokens, system=system, messages=messages)
            return r.content[0].text, r.usage
        except (anthropic.RateLimitError, anthropic.APIStatusError, anthropic.APIConnectionError) as e:
            status = getattr(e, "status_code", None)
            if status in (400, 401, 403):  # nicht retrybar
                raise
            if attempt == tries - 1:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 30)
    raise RuntimeError("unreachable")


def parse_json(text):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    # erstes { ... letztes }
    a, b = text.find("{"), text.rfind("}")
    if a != -1 and b != -1:
        text = text[a:b + 1]
    # rohe Steuerzeichen entfernen (haeufige Ursache fuer JSONDecodeError)
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", text)
    return json.loads(text)


def interview(p):
    """Fuehrt das komplette 3-Phasen-Interview + Extraktion fuer eine Persona."""
    sys_prompt = persona_system_prompt(p)
    msgs = []
    usage_tot = {"in": 0, "out": 0}

    def add_usage(u):
        usage_tot["in"] += u.input_tokens
        usage_tot["out"] += u.output_tokens

    # Phase 1
    msgs.append({"role": "user", "content": PHASE1})
    a1, u = call(sys_prompt, msgs, max_tokens=700); add_usage(u)
    msgs.append({"role": "assistant", "content": a1})
    # Phase 2
    msgs.append({"role": "user", "content": PHASE2})
    a2, u = call(sys_prompt, msgs, max_tokens=800); add_usage(u)
    msgs.append({"role": "assistant", "content": a2})
    # Phase 3
    msgs.append({"role": "user", "content": PHASE3})
    a3, u = call(sys_prompt, msgs, max_tokens=700); add_usage(u)
    msgs.append({"role": "assistant", "content": a3})

    transcript = (f"[PHASE 1 -- Frage]\n{PHASE1}\n\n[Antwort]\n{a1}\n\n"
                  f"[PHASE 2 -- Frage]\n{PHASE2}\n\n[Antwort]\n{a2}\n\n"
                  f"[PHASE 3 -- Frage]\n{PHASE3}\n\n[Antwort]\n{a3}")

    # Extraktion -- mit Parse-Retry (LLM liefert gelegentlich kaputtes JSON)
    structured = None
    last_err = None
    for _ in range(3):
        ex_text, u = call(EXTRACT_SYSTEM,
                          [{"role": "user", "content": EXTRACT_INSTR + transcript}],
                          max_tokens=1500); add_usage(u)
        try:
            structured = parse_json(ex_text)
            break
        except (json.JSONDecodeError, ValueError) as e:
            last_err = e
    if structured is None:
        raise last_err

    return {
        "persona": p,
        "transcript": {"phase1": a1, "phase2": a2, "phase3": a3},
        "structured": structured,
        "usage": usage_tot,
    }


def ckpt_path(pid):
    return os.path.join(CKPT_DIR, f"persona_{pid:03d}.json")


def run_one(p):
    path = ckpt_path(p["id"])
    if os.path.exists(path):
        return p["id"], "skip", 0.0
    try:
        res = interview(p)
    except Exception as e:
        return p["id"], f"ERROR {type(e).__name__}: {str(e)[:120]}", 0.0
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)
    # grobe Kostenschaetzung (Sonnet-Groessenordnung: 3/M in, 15/M out USD)
    cost = res["usage"]["in"] / 1e6 * 3 + res["usage"]["out"] / 1e6 * 15
    return p["id"], "ok", cost


def merge(personas):
    done = []
    for p in personas:
        path = ckpt_path(p["id"])
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                done.append(json.load(f))
    out = {
        "studie": "Silicon Sampling -- Pharma- & Gesundheits-KMU (DACH, 10-50 Mitarbeitende)",
        "disclaimer_esomar": ("Synthetische Marktforschung gemaess ESOMAR ICC Code 2025. "
                               "Daten stammen aus KI-Personas (Modell claude-sonnet-4-6), "
                               "NICHT aus echten Befragungen. Ergebnisse sind Hypothesen, "
                               "keine Fakten, und ersetzen keine reale Marktforschung."),
        "modell": MODEL,
        "zielgruppe": ZIELGRUPPE,
        "seed": SEED,
        "personas_geplant": len(personas),
        "personas_abgeschlossen": len(done),
        "methodik": ("Dreistufige, blinde Mehrturn-Befragung je Persona (Phase 1 offen "
                      "vor jeder Konzept-Nennung; Phase 2 Reaktion auf woertlich "
                      "vorgelesenes Angebot; Phase 3 Van-Westendorp-Preisschwellen fuer "
                      "einmaliges Aufbau-Projekt + monatlichen Retainer) + strukturierte "
                      "Extraktion. Keine Vorgabe von Pain Points/Einwaenden; diese "
                      "entstehen frei. Skeptiker-Quote bewusst >= 40%."),
        "prompts": PROMPTS_META,
        "ergebnisse": done,
    }
    tmp = OUT_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    os.replace(tmp, OUT_FILE)
    return len(done)


def main():
    n = 200
    workers = 6
    args = sys.argv[1:]
    skip = False
    for i, a in enumerate(args):
        if skip:
            skip = False
            continue
        if a == "--workers" and i + 1 < len(args):
            workers = int(args[i + 1])
            skip = True
        elif a.isdigit():
            n = int(a)

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY fehlt.")
    os.makedirs(CKPT_DIR, exist_ok=True)

    personas = generate_personas(n)
    todo = [p for p in personas if not os.path.exists(ckpt_path(p["id"]))]
    _log(f"[start] {n} Personas, {len(todo)} offen, {workers} Worker, Modell {MODEL}")

    total_cost, ok, err = 0.0, 0, 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(run_one, p): p for p in todo}
        for i, fut in enumerate(as_completed(futs), 1):
            pid, status, cost = fut.result()
            total_cost += cost
            if status == "ok":
                ok += 1
            elif status.startswith("ERROR"):
                err += 1
            done_total = ok + (n - len(todo))
            if i % 5 == 0 or status.startswith("ERROR"):
                _log(f"[{i}/{len(todo)}] p{pid}: {status} | fertig gesamt~{done_total} "
                     f"| ~${total_cost:.2f} | {time.time()-t0:.0f}s")
            # laufend mergen, damit sampling_pharma_kmu.json immer aktuell ist
            if i % 10 == 0:
                merge(personas)

    total_done = merge(personas)
    _log(f"[fertig] abgeschlossen {total_done}/{n} | Fehler {err} | ~${total_cost:.2f} "
         f"| {time.time()-t0:.0f}s | -> {OUT_FILE}")


if __name__ == "__main__":
    main()
