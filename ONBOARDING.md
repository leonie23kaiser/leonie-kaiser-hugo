# Onboarding — Hallo Leonie 👋

Dieses Repository ist deine eigene Website. Du kannst alles selbst ändern — am einfachsten mit **Claude Code** lokal auf deinem Mac. Diese Datei zeigt dir den Weg von Null bis „Änderung live".

Wer hier mitliest und nicht Leonie ist: das ist ihre Anleitung. Bitte nicht ohne Rückfrage abändern.

---

## 1. Was ist hier?

- **Hugo Static-Site** für deine Marke „Leonie Kaiser — KI & Business Consulting"
- Aktuell live unter **growthtogether.at** (Staging). Sobald du grünes Licht gibst, ziehen wir die Domain um auf **leoniekaiser.com**.
- Hosting: **GitHub Pages** (gratis, kein Server zu warten). Bei jedem `git push` auf den `main`-Branch baut GitHub die Seite neu und veröffentlicht sie.

Wichtige Verzeichnisse:

```
src/growthtogether.at/
├── content/         ← Texte (Markdown). Hier änderst du am häufigsten was.
│   ├── _index.md    ← Startseite
│   ├── ueber-mich.md
│   ├── faq.md
│   ├── impressum.md
│   └── datenschutz.md
├── layouts/         ← HTML-Templates. Hier nur ran, wenn du Struktur ändern willst.
├── assets/css/      ← Das einzige Stylesheet: brand.css
├── static/          ← Bilder, Fonts, robots.txt, llms.txt, CNAME (= Domain).
└── config/_default/ ← params.toml (Marken-Variablen), config.toml (Hugo-Setup)
```

---

## 2. Einmalig einrichten (auf deinem Mac)

```bash
# Hugo installieren (extended-Version)
brew install hugo

# Repo klonen (URL bekommst du nach dem Account-Transfer)
git clone git@github.com:<dein-github-name>/leonie-kaiser-hugo.git
cd leonie-kaiser-hugo

# Claude Code installieren (falls noch nicht da)
#   → https://docs.claude.com/claude-code
```

Version prüfen: `hugo version` sollte `v0.123` oder höher anzeigen, mit `extended`.

---

## 3. Lokal arbeiten

Ein Terminal-Fenster für den Live-Preview offen lassen:

```bash
hugo server --source src/growthtogether.at -D
```

Dann im Browser: **http://localhost:1313**. Jede Datei-Änderung lädt die Seite automatisch neu — du siehst deine Updates in Echtzeit.

Wenn du fertig bist, einmal CTRL+C im Terminal, das stoppt den Server.

---

## 4. Mit Claude Code arbeiten

Im Repo-Ordner:

```bash
claude
```

Claude liest automatisch `CLAUDE.md` (im Repo-Root) und kennt damit deine Marken-Farben, Voice, Strukturen. Beispiel-Prompts:

- *„Schreib die FAQ-Antwort zu ‚Was kostet die KI-Potenzialanalyse?' um — kürzer, mit klarem CTA am Ende."*
- *„Füge eine neue FAQ-Frage hinzu: ‚Wie lange dauert ein KI-Projekt?'. Kategorie: Zusammenarbeit."*
- *„Tausche das Bild im Hero gegen das neue Portrait `static/images/leonie-2026.jpg` aus."*
- *„Aktualisiere das Datum im Footer auf heute."*
- *„Mein Telefon hat sich geändert — bitte überall ersetzen: +43 670 123 4567."*

Claude macht die Änderung, du siehst sie sofort im lokalen Preview. Wenn alles passt:

```bash
git add <konkrete-dateien>      # NIE `git add .`
git commit -m "content: FAQ-Antwort kostenklar formuliert"
git push
```

GitHub Actions baut dann automatisch und deployed in ~1 Minute auf growthtogether.at.

---

## 5. Was du **niemals** machst

- ❌ **`git add -A` / `git add .` / `git add *`** — immer einzelne Dateien angeben. Sonst kommen ungewollte Sachen ins Repo.
- ❌ **Domain wechseln, ohne Bescheid zu sagen** — `static/CNAME` enthält die Live-Domain. Nicht einfach umändern, sonst geht die Seite offline.
- ❌ **Direkt im `public/`-Ordner editieren** — der wird bei jedem Build überschrieben.
- ❌ **Bilder in `static/images/` ohne WebP-Variante hochladen** — Hugo erwartet beide Formate für die responsive `picture`-Partial. Tipp: `cwebp -q 85 bild.png -o bild.webp`.

---

## 6. Häufige Aufgaben

### Neue FAQ-Frage hinzufügen
Datei: `src/growthtogether.at/layouts/faq/single.html` — Block `<div class="faq-item" data-cat="...">` kopieren. Kategorien: `strategie`, `kosten`, `compliance`, `tools`, `zusammenarbeit` (mehrere mit Space getrennt). Schema.org-FAQPage in `partials/schema.html` mitziehen.

### Testimonial ändern
Datei: `src/growthtogether.at/layouts/_default/home.html` — Sektion „Was Kund:innen sagen". Bild ins `static/images/` legen (PNG + WebP). Auch in `partials/schema.html` (Reviews + AggregateRating) updaten.

### Termin-Link tauschen (Calendly)
Suche nach `calendly.com/leonie-kaiser` und ersetze überall. Claude erledigt das in einem Rutsch.

### Brand-Farbe ändern
Datei: `src/growthtogether.at/config/_default/params.toml` und `src/growthtogether.at/assets/css/brand.css` (CSS-Variablen oben). Sag Claude *„Ändere `--teal-d` auf #0A7090 und passe alle Stellen an"* — er findet alles.

### Auf leoniekaiser.com umziehen
Wenn du bereit bist:
1. Sag uns Bescheid — wir prüfen, dass alles passt.
2. `static/CNAME` von `growthtogether.at` auf `leoniekaiser.com` ändern.
3. DNS bei deinem Domain-Provider: `A`-Records auf GitHub Pages IPs (`185.199.108.153 / .109.153 / .110.153 / .111.153`).
4. In GitHub: Settings → Pages → Custom Domain auf `leoniekaiser.com`.
5. „Enforce HTTPS" anhaken (nach ~30 Min verfügbar).

---

## 7. Hilfe & Notfall

- **Seite ist down / Build schlägt fehl**: Schau in GitHub → Tab „Actions". Die rote Zeile zeigt den Fehler. Screenshot an uns reicht.
- **Letzte Änderung rückgängig**: `git revert HEAD && git push`. Claude kennt das.
- **Bei größeren Sachen** (Layout-Umbau, neue Sub-Page, technische Fragen): einfach melden, das machen wir gemeinsam.

Viel Spaß mit deiner neuen Seite. ✨
