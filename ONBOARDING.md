# Onboarding — Hallo Leonie 👋

Deine Website lebt jetzt in deinem eigenen GitHub-Repo:
**https://github.com/leonie23kaiser/leonie-kaiser-hugo**

Du arbeitest komplett **im Browser** — kein Terminal, kein VS Code nötig.
Claude.ai ist dein Editor, GitHub ist deine Festplatte, GitHub Pages ist dein Hosting. Alles drei reden miteinander.

Wer hier mitliest und nicht Leonie ist: das ist ihre Anleitung. Bitte nicht ohne Rückfrage abändern.

---

## 1. Wie das Ganze funktioniert (in einem Bild)

```
Du chattest mit Claude  →  Claude bearbeitet Dateien im GitHub-Repo  →  GitHub baut die Seite neu  →  ~1 Min später live auf leoniekaiser.com
```

Konkret:
- Du schreibst Claude im Browser, was du ändern willst.
- Claude macht einen **Pull Request** (PR) im Repo — das ist ein Vorschlag mit Vorher/Nachher.
- Du klickst auf GitHub auf **Merge** → die Änderung geht live.
- Wenn etwas schiefläuft: einfach den PR **nicht mergen**, dann passiert auch nichts.

---

## 2. Einmalige Einrichtung (5 Minuten)

### Schritt A — Custom Domain in GitHub eintragen

1. Öffne https://github.com/leonie23kaiser/leonie-kaiser-hugo/settings/pages
2. Bei **Custom domain** trage ein: `leoniekaiser.com`
3. **Save** klicken
4. Nach ~10 Minuten: Haken bei **Enforce HTTPS** setzen

(DNS-Records bei deinem Domain-Provider haben wir vorher gemeinsam eingestellt — falls die Seite nach 30 Min noch nicht auf leoniekaiser.com zu sehen ist: melden, wir schauen drauf.)

### Schritt B — Claude mit GitHub verbinden

1. Öffne https://claude.ai/settings/connectors
2. Bei **GitHub** auf **Connect** klicken
3. Bei GitHub einloggen (dein Login: `leonie23kaiser`)
4. **Authorize Claude** bestätigen
5. Bei „Repository access" → **Only select repositories** → wähle `leonie-kaiser-hugo` → **Install**

Fertig. Ab jetzt kann Claude in jedem Chat das Repo sehen.

---

## 3. So machst du eine Änderung

1. Öffne https://claude.ai → **New chat**
2. Unten beim Anhang-Symbol (📎) → **GitHub** → wähle `leonie-kaiser-hugo`
3. Schreib einfach, was du willst. Zum Beispiel:

> *„Ändere auf der Startseite den Hero-Untertitel auf ‚KI-Strategie für KMU in Wien'. Mach einen Pull Request."*

4. Claude liest die Datei, zeigt dir den geplanten Text, fragt nochmal nach. Du sagst **„passt, los"**.
5. Claude erstellt den **Pull Request** im Repo.
6. Du gehst auf GitHub (Link bekommst du im Chat), schaust den **Files changed**-Tab an — das ist die Vorher-Nachher-Ansicht.
7. Klick auf **Merge pull request** → **Confirm merge**.
8. Nach ~1 Minute ist die Änderung live auf leoniekaiser.com.

---

## 4. Beispiel-Sätze, die du Claude sagen kannst

| Was du willst | Was du tippst |
|---|---|
| Text auf Startseite ändern | *„Auf der Startseite im Hero: ändere den Satz X auf Y. PR machen."* |
| Neue FAQ-Frage | *„Füge eine FAQ-Frage hinzu: ‚Wie lange dauert ein KI-Projekt?' Kategorie: zusammenarbeit. Antwort: …"* |
| Über-mich-Text aktualisieren | *„Auf der Über-mich-Seite: füge folgenden Abschnitt ein: …"* |
| Telefonnummer überall tauschen | *„Ersetze die Telefonnummer überall im Repo durch +43 670 123 4567."* |
| Calendly-Link austauschen | *„Tausche alle calendly.com-Links auf https://calendly.com/leonie-kaiser/neu"* |
| Testimonial ändern | *„Im Abschnitt ‚Was Kund:innen sagen' das zweite Testimonial: ersetze Name auf X und Text auf Y."* |
| Bild austauschen | (Bild per Drag&Drop in den Chat) + *„Ersetze damit das Hero-Bild."* |
| Rechtschreibfehler | *„Im Footer steht ‚Beratug', soll ‚Beratung' heißen."* |

**Profi-Tipp:** Du musst nicht wissen, in welcher Datei der Text steht. Sag einfach *„auf der Startseite im Hero"* oder *„im FAQ-Bereich"*, Claude findet's selbst.

---

## 5. Was du wissen solltest

### Claude liest deine Marken-Regeln automatisch

Im Repo liegen zwei Dateien, die Claude bei **jedem Chat** mitliest:

- **`AGENTS.md`** — dein Brand-Voice-Vertrag: Sie-Form, kein Sternchen-Gendern, „Chaos reduzieren"-Motiv, Wort-Whitelist, Wort-Blacklist (kein „revolutionär", kein „Gamechanger" usw.), Conversion-Ziel = Potenzialanalyse. **Diese Datei ist kanonisch** — bei Konflikt mit anderen Anweisungen gewinnt sie.
- **`CLAUDE.md`** — die technischen Repo-Regeln: Brand-Farben (#086584 Teal, #CF982B Gold, #6B2C8C Violett), Schriftarten, FAQ-Kategorien, was Tabu ist (z.B. nie `git add -A`).

Du musst Brand-Voice also nicht jedes Mal erklären. Wenn Claude trotzdem mal abdriftet (z.B. duzt statt siezt): einfach sagen *„AGENTS.md beachten"* — sitzt sofort wieder.

### Das „Repo-Gedächtnis" — wie Claude sich Dinge merkt

Claude selbst hat **kein Langzeitgedächtnis** zwischen Chats. Jeder neue Chat startet bei Null.

**Aber:** Alles, was im Repo steht, ist sein Gedächtnis. Konkret:

- `AGENTS.md` + `CLAUDE.md` → deine Brand-Voice & Konventionen (siehe oben)
- `content/journal/*.md` → alle bisherigen Journal-Posts (Claude liest sie als Referenz für Stil und Themen)
- `content/faq/*.md` → bestehende FAQ-Fragen (damit er keine Dopplungen baut)
- `data/branchen.yaml` → deine Branchen-Texte (Physio, Psycho, Coaching, Ernährungsberatung)
- Git-Historie → alle früheren Änderungen sind nachvollziehbar

Wenn du in einem neuen Chat schreibst *„schreib einen Journal-Post wie den letzten"*, schaut Claude in den Ordner, liest die letzten Posts, übernimmt Stil + Aufbau. Genau dafür ist die GitHub-Anbindung gemacht.

**Was Claude im Repo speichern kann (wenn du willst):**
Du kannst Claude bitten *„merk dir das in einer Notiz-Datei"*. Er legt dann z.B. `docs/leonie-notizen.md` an. Das ist dein persönlicher Notiz-Block im Repo — bleibt für immer da, jeder neue Claude-Chat liest mit.

Beispiel: *„Merk dir bitte: meine Lieblings-Beispiele für Physio-Praxen sind Praxis Müller in Salzburg und Therapiezentrum Kaltenleutgeben. Verwende die in Zukunft wenn ein Beispiel gebraucht wird."* → Claude legt das in `docs/leonie-notizen.md` ab, du musst es nie wieder sagen.

### Direkt commit statt PR

Wenn du dir sicher bist (z.B. Tippfehler), sag *„commit direkt auf main, kein PR nötig"* — dann ist es sofort live, ohne den Umweg über die Merge-Bestätigung.

### Pull Request rückgängig

Änderung doch nicht gut? Auf GitHub den PR einfach **nicht mergen** und **Close** klicken. Schon gemergt? Sag Claude *„revertiere den letzten Commit"* — er macht einen Rück-PR.

### Du brauchst keine technischen Begriffe

„Mach einen PR" reicht. Du musst nicht wissen, was Hugo, Markdown, YAML oder Frontmatter bedeutet. Claude erklärt dir, was er macht, wenn du fragst.

---

## 6. Was du **nicht** tun solltest

- ❌ **Pages-Domain ändern**, ohne Bescheid zu sagen — sonst geht die Seite offline.
- ❌ **Im GitHub-Ordner `public/` etwas editieren** — der wird bei jedem Build überschrieben.
- ❌ **Den `main`-Branch löschen** — das ist dein Live-Stand.
- ❌ **Größere Layout-Umbauten allein versuchen** („mach das Design ganz neu"). Für sowas: kurz melden, wir machen das gemeinsam.

Falls Claude doch was kaputt macht: nicht mergen → kein Schaden. Schon gemergt und Seite weiß? → uns sofort schreiben, wir revertieren in 30 Sekunden.

---

## 7. Wenn etwas nicht funktioniert

| Problem | Was du machst |
|---|---|
| Seite zeigt alte Inhalte | 1–2 Minuten warten, dann Strg+Shift+R (Hard Reload) im Chrome |
| GitHub Actions ist rot (siehe Tab „Actions") | Screenshot an uns schicken |
| Claude versteht den Wunsch nicht | Konkreter werden: welche Seite, welcher Abschnitt, welcher Text |
| Pull Request ist verwirrend | *„Erkläre mir den PR in einfachen Worten"* fragen |
| Etwas Großes geht schief | Kurz anrufen, wir helfen sofort |

---

## 8. Variante 2 — Eigene Cloud-Werkstatt auf exe.dev (Chromebook-freundlich)

Du hast zusätzlich zur claude.ai-Variante eine **eigene Cloud-VM** auf exe.dev:
**`leonie-kaiser.exe.xyz`**. Darauf läuft:

- **Shelley** (dein eigener Claude-Code-Agent, kein claude.ai-Connector nötig)
- **Hugo-Vorschau-Server**, der deine Live-Seite in Echtzeit baut

Der Vorteil gegenüber claude.ai: Du **siehst beim Tippen, wie sich die Seite
verändert**. Keine PRs, keine Wartezeit, keine Wiederholung von Brand-Voice-Regeln.

### So arbeitest du damit (typischer Tag)

1. Browser-Tab 1: **https://leonie-kaiser.shelley.exe.xyz/** → dein Shelley-Chat.
2. Browser-Tab 2: **https://leonie-kaiser.exe.xyz/** → Live-Vorschau deiner Seite
   (lädt automatisch neu, wenn Shelley etwas ändert).
3. Du sagst Shelley auf Deutsch, was du willst:
   > *„Schreib mir einen Journal-Eintrag über DSGVO und KI-Tools."*
   > *„Ändere den Hero-Untertitel auf der Startseite auf X."*
   > *„Füge eine neue Branchen-Seite für Steuerberater hinzu."*
4. Shelley editiert, du schaust im Vorschau-Tab, sagst „passt" oder „nochmal
   anders".
5. Wenn alles okay: *„commit und push"* → geht live auf leoniekaiser.com.

### Was Shelley alles weiß

Genau wie der claude.ai-Connector liest Shelley `AGENTS.md` + `CLAUDE.md` + alle
bestehenden Inhalte mit. **Zusätzlich** liegt auf der VM eine
`~/.config/shelley/AGENTS.md`, die ihr sagt:

- Du heißt Leonie, sie spricht dich mit **Du** an (nur Website-Texte sind Sie-Form).
- Repo liegt unter `~/leonie-kaiser-hugo/`.
- Vorschau-URL ist die exe.xyz.
- Niemals deployen ohne dein OK.
- Schrittweise arbeiten, bei größeren Sachen erst Plan vorlegen.

### Wenn die Vorschau mal nicht lädt

Der Hugo-Server läuft in einer „tmux-Session" namens `hugo`. Sag Shelley einfach:
> *„Die Vorschau geht nicht, starte den Hugo-Server neu."*

### Wann claude.ai, wann VM?

| Use-Case | claude.ai-Connector | VM / Shelley |
|---|:---:|:---:|
| Schneller Tippfehler-Fix | ✓ | |
| Eine FAQ-Frage ergänzen | ✓ | |
| Längerer Journal-Artikel mit Live-Preview | | ✓ |
| Neue Branchen-Seite bauen + sofort schauen | | ✓ |
| Bild austauschen + Ergebnis sehen | | ✓ |
| Layout-Anpassung sehen wollen | | ✓ |
| Unterwegs am Handy schnell was tippen | ✓ | |

Beide Wege ändern dasselbe Repo, also: kein Konflikt, du kannst jederzeit
zwischen den Varianten wechseln.

### Falls die VM mal aus ist

exe.dev kann die VM aus Kostengründen pausieren. Im exe.dev-Dashboard
(https://exe.dev) siehst du deine VMs und kannst sie mit einem Klick wieder
starten. Beim ersten Aufruf nach Pause kann es ein paar Sekunden dauern, bis
Hugo wieder bereit ist.

---

## 9. Wichtige Links auf einen Blick

- 🌐 **Live-Seite:** https://leoniekaiser.com
- 📦 **Dein Repo:** https://github.com/leonie23kaiser/leonie-kaiser-hugo
- ⚙️ **Pages-Einstellungen:** https://github.com/leonie23kaiser/leonie-kaiser-hugo/settings/pages
- 🔨 **Build-Status:** https://github.com/leonie23kaiser/leonie-kaiser-hugo/actions
- 🤖 **Claude.ai:** https://claude.ai
- 🔌 **Claude Connectors:** https://claude.ai/settings/connectors

Viel Spaß mit deiner neuen Seite. ✨
