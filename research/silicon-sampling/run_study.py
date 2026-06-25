#!/usr/bin/env python3
"""
Silicon-Sampling-Studie — Befragungs-Runner.

Befragt jede Persona in 3 Phasen (Multi-Turn, blind) über die Anthropic-API
(Modell: claude-sonnet-4-6). Parallelisiert mit Concurrency-Limit, Retry mit
Backoff und CHECKPOINT pro Persona (Resume nach Abbruch).

Aufruf:
    export ANTHROPIC_API_KEY=...        # Key NIE im Repo speichern
    python run_study.py --limit 10      # Pilot
    python run_study.py                 # voller Lauf (alle Personas)
    python run_study.py --concurrency 8 # Parallelität anpassen

Synthetische Daten gemäß ESOMAR ICC Code 2025 — Ergebnisse sind Hypothesen.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
import time
from pathlib import Path

from anthropic import AsyncAnthropic
from anthropic import APIStatusError, APIConnectionError, RateLimitError

from personas import generate_personas, Persona
from prompts import PHASES, PROMPT_VERSION

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 3000  # genug Headroom, damit O-Ton-Prosa + JSON-Block nie abgeschnitten werden
HERE = Path(__file__).parent
RESP_DIR = HERE / "data" / "responses"
RUN_META = HERE / "data" / "run_meta.json"

JSON_BLOCK_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL)


def extract_json(text: str) -> dict | None:
    """Holt den letzten ```json ...```-Block aus der Antwort."""
    matches = JSON_BLOCK_RE.findall(text)
    if not matches:
        # Fallback: letzte geschweifte Klammer-Gruppe versuchen
        brace = re.findall(r"(\{(?:[^{}]|\{[^{}]*\})*\})", text, re.DOTALL)
        matches = brace[-1:] if brace else []
    for raw in reversed(matches):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            continue
    return None


def prose_only(text: str) -> str:
    """Antworttext ohne den JSON-Block (für O-Töne)."""
    return JSON_BLOCK_RE.sub("", text).strip()


async def call_with_retry(client, **kwargs):
    """API-Call mit exponentiellem Backoff bei Rate-Limit/Overload/Netz."""
    delay = 2.0
    last_exc = None
    for attempt in range(6):
        try:
            return await client.messages.create(**kwargs)
        except (RateLimitError, APIConnectionError) as e:
            last_exc = e
        except APIStatusError as e:
            if e.status_code in (429, 500, 502, 503, 529):
                last_exc = e
            else:
                raise
        await asyncio.sleep(delay)
        delay = min(delay * 2, 32)
    raise last_exc


async def interview_persona(client, persona: Persona, sem: asyncio.Semaphore) -> dict:
    """Führt die 3-Phasen-Befragung für eine Persona durch (Multi-Turn)."""
    out_path = RESP_DIR / f"{persona.pid}.json"
    if out_path.exists():
        return json.loads(out_path.read_text(encoding="utf-8"))  # Resume

    async with sem:
        system = persona.system_prompt()
        messages: list[dict] = []
        result = {
            "pid": persona.pid,
            "persona": persona.to_dict(),
            "model": MODEL,
            "prompt_version": PROMPT_VERSION,
            "phases": {},
            "usage": {"input_tokens": 0, "output_tokens": 0},
        }
        for phase_key, phase_prompt in PHASES:
            messages.append({"role": "user", "content": phase_prompt})
            resp = await call_with_retry(
                client,
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=system,
                messages=messages,
            )
            text = "".join(b.text for b in resp.content if b.type == "text")
            messages.append({"role": "assistant", "content": text})
            result["phases"][phase_key] = {
                "text": prose_only(text),
                "structured": extract_json(text),
                "raw": text,
            }
            result["usage"]["input_tokens"] += resp.usage.input_tokens
            result["usage"]["output_tokens"] += resp.usage.output_tokens

        out_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return result


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="nur erste N Personas (Pilot)")
    ap.add_argument("--concurrency", type=int, default=6)
    ap.add_argument("--count", type=int, default=220, help="Persona-Anzahl")
    ap.add_argument("--seed", type=int, default=20260625)
    args = ap.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("FEHLER: ANTHROPIC_API_KEY ist nicht gesetzt.")

    RESP_DIR.mkdir(parents=True, exist_ok=True)
    personas = generate_personas(n=args.count, seed=args.seed)
    if args.limit:
        personas = personas[: args.limit]

    done = sum(1 for p in personas if (RESP_DIR / f"{p.pid}.json").exists())
    print(f"Modell: {MODEL} | Personas: {len(personas)} | bereits fertig: {done} "
          f"| Concurrency: {args.concurrency}")

    client = AsyncAnthropic(max_retries=0)
    sem = asyncio.Semaphore(args.concurrency)
    start = time.time()
    completed = 0

    tasks = [interview_persona(client, p, sem) for p in personas]
    for coro in asyncio.as_completed(tasks):
        try:
            r = await coro
            completed += 1
            bl = (r["phases"].get("phase2_konzept", {}).get("structured") or {})
            print(f"  [{completed}/{len(personas)}] {r['pid']} fertig "
                  f"(Buchung 1-10: {bl.get('buchungswahrscheinlichkeit_1_10', '?')})")
        except Exception as e:
            completed += 1
            print(f"  [{completed}/{len(personas)}] FEHLER: {type(e).__name__}: {e}")

    elapsed = time.time() - start
    # Run-Metadaten für Reproduzierbarkeit
    RUN_META.write_text(json.dumps({
        "model": MODEL,
        "prompt_version": PROMPT_VERSION,
        "persona_count": len(personas),
        "seed": args.seed,
        "concurrency": args.concurrency,
        "elapsed_seconds": round(elapsed, 1),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "esomar_note": "Synthetische Daten (Silicon Sampling) gemaess ESOMAR ICC Code 2025. "
                       "Ergebnisse sind Hypothesen, keine validierten Fakten.",
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nFertig in {elapsed:.0f}s. Antworten in {RESP_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
