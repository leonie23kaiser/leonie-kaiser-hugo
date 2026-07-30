---
name: verify-visual
description: Abnahme-Standard für alles Visuelle (Video, Cards/PNGs, HTML-Seiten, Kurs-Folien, PDFs) — messen UND ansehen, nie nur Exit-Codes trauen. Ffprobe/Pegel/Frame-Extraktion für Video, Headless-Screenshot für HTML, Sichtprüfung als Pflichtschritt vor "fertig". Adaptiert aus Alex' ffmpeg-assembly-Verify-Loop, generalisiert für EAP. Triggers: video prüfen, abnahme, verify, frames ansehen, pegel, stumm, sichtprüfung, screenshot-check, folien prüfen, card prüfen, render prüfen, sieht das gut aus.
---

# verify-visual

**Kein visuelles Artefakt gilt als fertig, bevor es jemand ANGESEHEN hat** — Messwerte allein
lügen (Datei existiert, Pegel misst normal, und trotzdem ist das falsche Bild unter dem Beat,
die Card abgeschnitten oder der Player stumm). Herkunft: Alex' Verify-Loop (ffmpeg-assembly-Leaf),
Erfahrung deckungsgleich mit EAPs check-overflow-Lehren (Blindflecken entstehen, wo nur gemessen wird).

## Video (nach jedem Schnitt/Render)

```bash
# 1) Profil: erwartet 1920x1080 / 30 fps / yuv420p, aac 48 kHz
ffprobe -v error -show_entries stream=width,height,r_frame_rate,pix_fmt -select_streams v:0 -of csv=p=0 final.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 final.mp4

# 2) Ton an 2-3 Stellen: Narration ~ -24 bis -30 dB mean (NICHT silent)
ffmpeg -hide_banner -ss <t> -t 6 -i final.mp4 -af volumedetect -f null - 2>&1 | grep mean_volume

# 3) Frames früh/mittig/spät extrahieren und ANSEHEN (Read auf die PNGs)
ffmpeg -y -ss <t> -i final.mp4 -frames:v 1 frame_<t>.png
```

Beim Ansehen prüfen: liegt unter jedem Beat die richtige Ebene (Diagramm unter VO, Avatar bei
ON-CAM, keine Platzhalter vergessen)? Text lesbar, nichts beschnitten?

**Concat-Gotcha (Pflicht):** nach jedem Concat ein Re-Mux mit durchgehender Audio-Neucodierung,
sonst spielen manche Player stumm:
`ffmpeg -i concat.mp4 -c:v copy -af "aresample=async=1:first_pts=0" -c:a aac -movflags +faststart final.mp4`

## Cards / HTML / Folien

- HTML→PNG am Mac: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new
  --disable-gpu --screenshot=out.png --window-size=1920,1080 --hide-scrollbars file://…`
- Den Screenshot IMMER per Read ansehen (Umbrüche, Überlauf, Schriftersatz, Farben auf dunklem Grund).
- Kurs-Folien: `preview-course`/`check-overflow` messen — zusätzlich Stichproben-Folien ansehen
  (die check-overflow-Blindflecken-Lehre: → [[course-factory-bildclip-fix]]).

## Prinzip hinter allem

1. **Messen** (Profil, Dauer, Pegel, Exit-Codes) fängt die groben Fehler.
2. **Ansehen** (Frames, Screenshots, Stichproben) fängt die peinlichen.
3. Erst wenn beides grün ist, "fertig" melden — und im Bericht sagen, WAS angesehen wurde.
