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

Im Repo liegt eine Datei `CLAUDE.md` — die kennt deine Brand-Farben, die Sie-Form, die FAQ-Kategorien, was Tabu ist. Claude liest sie bei jedem Chat mit. Du musst Brand-Voice also nicht jedes Mal erklären.

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
| Seite zeigt alte Inhalte | 1–2 Minuten warten, dann Strg+Shift+R (Hard Reload) im Browser |
| GitHub Actions ist rot (siehe Tab „Actions") | Screenshot an uns schicken |
| Claude versteht den Wunsch nicht | Konkreter werden: welche Seite, welcher Abschnitt, welcher Text |
| Pull Request ist verwirrend | *„Erkläre mir den PR in einfachen Worten"* fragen |
| Etwas Großes geht schief | Kurz anrufen, wir helfen sofort |

---

## 8. Für später: lokal arbeiten (optional, nicht nötig)

Wenn du irgendwann mal **vor dem Mergen** sehen willst, wie die Änderung aussieht (Live-Preview), gibt es einen Weg mit deinem Mac-Terminal. Das ist **nicht** für den Alltag — nur falls du Lust auf mehr Kontrolle hast. Sag uns Bescheid, wir richten's mit dir ein. Brauchst du im Normalfall **nicht**.

---

## 9. Wichtige Links auf einen Blick

- 🌐 **Live-Seite:** https://leoniekaiser.com
- 📦 **Dein Repo:** https://github.com/leonie23kaiser/leonie-kaiser-hugo
- ⚙️ **Pages-Einstellungen:** https://github.com/leonie23kaiser/leonie-kaiser-hugo/settings/pages
- 🔨 **Build-Status:** https://github.com/leonie23kaiser/leonie-kaiser-hugo/actions
- 🤖 **Claude.ai:** https://claude.ai
- 🔌 **Claude Connectors:** https://claude.ai/settings/connectors

Viel Spaß mit deiner neuen Seite. ✨
