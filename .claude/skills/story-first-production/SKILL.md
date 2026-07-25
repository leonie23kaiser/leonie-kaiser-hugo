---
name: story-first-production
description: Story-first-Doc-Pipeline für jede Produktion mit redaktionellem Anteil (Werbevideo, Kurs-Video, Marketing-Clip, Demo, Case-Study). Ein Dokument ist der Chef (05-story.md), alles andere folgt ihm; Autoren-Entscheidungen werden GEFRAGT, nie angenommen. Adaptiert aus Alex' promo-video-Prozess (ai-teacher), generalisiert für EAP. Triggers: werbevideo, promo, marketing-video, storyboard, story-first, produktion aufsetzen, video planen, case study video, demo-video, clip produzieren.
---

# story-first-production

Der EAP-Standard, wie eine Produktion mit redaktionellem Anteil aufgesetzt wird — bevor irgendein
Asset gebaut wird. Herkunft: Alex' `promo-video`-Leaf (ai-teacher, wine71-Produktion), bewiesen
am fastlane-Werbevideo (2026-07-19: Story → Storyboard → Narration → Rohschnitt an einem Abend).

## Kernprinzip

**Das Story-Dokument ist die redaktionelle Wahrheit.** Wenn Story und Storyboard (oder Schnitt,
oder Cards) sich widersprechen, gewinnt die Story und das andere wird nachgezogen — nie umgekehrt.

## Ordner-Konvention (ein Ordner pro Produktion)

```text
<produktions-repo>/
  README.md          Layout-Karte + Status-Checkliste
  docs/              nummerierte Produktions-Docs (03-storyboard, 05-story, …)
  assets/            erzeugte Assets (renders/, cards/, voice-samples/)
  tools/             Orchestrator-Skripte (Render, Assembly)
  deliverables/      NUR die Abhol-Artefakte für den Kunden/Emanuel
```

Eigenes Repo pro Produktion (EAP-Regel „ein Projekt = ein Repo"). Fremdmaterial (z. B. ein
Partner-Klon) bleibt read-only referenziert, wird nie hineinkopiert oder verändert:
**Lesen beim Partner, schreiben nur bei uns.**

## Die Doc-Pipeline (nummeriert, nur was gebraucht wird)

1. `05-story.md` ZUERST (trotz Nummer): Positionierung, Logline, Akt-Struktur mit Quellen-Spalte,
   Motive, Editorial-Entscheidungen. Rang: höchste Autorität.
2. `03-storyboard.md`: getimte Segmente, VO- vs ON-CAM-Text (TTS-fertig), Shot-Zuordnung auf
   konkretes Material, Overlays, Cutdown-Map (Hochformat) + Loop-Clips/GIFs.
3. Weitere Nummern (Prompt-History, Teaching-Guide, Produktionsplan) nur bei Bedarf.

## Autoren-Entscheidungen: FRAGEN, nie annehmen

In `05-story.md` als eigener Block, jede mit Datum + Entscheider:

- **Kosten-Modus:** echte Zahlen (auditierbar, müssen aufs Ledger stimmen) ODER Sample-Zahlen
  (Methode zeigen, Zahlen klar illustrativ). Nie stillschweigend vererben.
- **Sprache** (DE/EN) und ob eine Zweitfassung aus derselben Timeline kommt.
- **Stimme/Avatar:** VO+Untertitel vs ON-CAM; wessen Avatar/Stimme.
- **Länge/Plattform-Prio, Deadline.**

## Editorial-Regeln (vererbt, überall durchsetzen)

- **Remix vor Neudreh:** erst prüfen, welches Material existiert; neu gebaut wird nur, was fehlt.
- **Jeder gezeigte Prompt ist wortwörtlich** aus den Transkripten, Tippfehler inklusive.
- **Belege statt Hype:** jede Behauptung hat ein sichtbares Artefakt (grüne Tests, Rechnung, Live-Site).
- **Das Beeindruckende nie dramatisieren** — als Fakt feststellen, weitergehen; Spannung liegt in dem,
  was danach kommt.
- **Werbung bleibt leicht:** eine Intro-Card, dezente Lower-Thirds, eine CTA-Card. Die Story verkauft.
- **Narration-locked:** die gerenderte Tonspur ist die Timing-Autorität, Bilder passen sich dem Ton an.
- Keine Gedankenstriche in generiertem Text (Doppelpunkt, Komma, Klammern). Für Kunden-Content:
  konsistente Anrede wählen und dabei bleiben.

## Ausbau-Format für längere Produktionen (ab ~5 min, aus Alex' Shooting-Script-Disziplin)

- **Shot-Tabelle** statt Segment-Prosa: Shot-ID, Timecode/Dauer, Modus (ON-CAM/VO/CARD), Narration,
  Visual-ID, Lower-Third, Übergang.
- **Doppelspur-Narration:** Display-Text (für Captions) UND TTS-Variante (Zahlen/Abkürzungen
  ausgeschrieben: "H T T P S", "zwanzig sechsundzwanzig") — nur wo sie abweichen.
- **Durchgängige Lower-Thirds** als Ein-Satz-Belege (halten stumme Zuschauer im Film).
- **Teaching-Guide als Zwilling:** pro Abschnitt das 5-Teile-Rezept (Ziel / Prompt-Template +
  Original-Prompt / was passiert / Checkpoint / Gotchas) — wird direkt zu Kursmaterial
  (Doppel-Verwertung: Video verkauft DL, Guide füttert den eigenen Kurs).

## Danach

Produktion mechanisch abarbeiten (Narration-Render → Assets → Assembly), Abnahme mit dem
`verify-visual`-Skill (messen UND ansehen), Lernen zurückspielen via `eap-reflect`.

## Screencast-Klasse (UI-Schulungsvideos, seit 21.07.2026)

App lokal mit Demo-DB starten (nie Produktionsdaten filmen), Playwright dreht Takes je
Storyboard-Segment: `record_video_dir` je Context, Cursor-Overlay per `add_init_script`
(Div folgt mousemove, mousedown schrumpft = Klick-Feedback), DB-Zustände zwischen Takes per
sqlite umstellen (Continuity), am Dreh-Rechner nicht ausführbare Klicks per `page.route`
abfangen und mit 302 auf den ECHTEN Erfolgs-Screen antworten. Schnitt narration-locked
(`tpad`-Freeze, identisches Encode-Profil, concat), zuletzt `loudnorm=I=-16`.
Komplettes Rezept: Brain-Notiz `2026-07-21-screencast-schulungsvideo-playwright`,
Bewährt in mehreren EAP-Videoproduktionen (u. a. 91-s-Video in einer Session).
