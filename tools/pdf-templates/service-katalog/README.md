# Service-Katalog PDF – Quelle & Regenerierung

Diese HTML-Datei ist die Quelle für den herunterladbaren Service-Katalog
(`src/growthtogether.at/static/downloads/service-katalog.pdf`), verlinkt auf der
Leistungsseite (`/leistungen/`) als Lead-Magnet zur Potenzialanalyse.

Hugo kann keine PDFs erzeugen. Das PDF wird per Chromium-Headless-Druck aus dieser
HTML-Datei gerendert (in dieser Umgebung unter `/opt/pw-browsers/chromium-*/chrome-linux/chrome`
vorinstalliert; lokal reicht jedes aktuelle Chrome/Chromium).

## Inhalt aktuell halten

Diese Datei ist ein eigenständiges Layout, **kein** Hugo-Template — die Inhalte müssen
manuell mit `strategie/service-katalog.md` und den freigegebenen Website-Texten
(`src/growthtogether.at/layouts/leistungen/single.html`, `data/branchen.yaml`) synchron
gehalten werden. Bei Preis- oder Paketnamen-Änderungen: hier UND auf der Website anpassen.

## Neu generieren

```bash
CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome   # oder lokal: chromium/google-chrome
"$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=../../../src/growthtogether.at/static/downloads/service-katalog.pdf \
  "file://$(pwd)/service-katalog.html"
```

Danach `hugo --source src/growthtogether.at --minify` und prüfen, dass
`/downloads/service-katalog.pdf` im Build landet.
