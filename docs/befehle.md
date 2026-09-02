# Was du Claude sagen kannst

Übersicht über alle Skills in diesem Repo — sortiert danach, wie nützlich sie
für dich sind. Ein Skill ist eine gespeicherte Arbeitsanleitung: Claude hält
sich dann an einen festen Ablauf, statt jedes Mal neu zu improvisieren.

**Zwei Wege, einen Skill zu starten:**

1. **Einfach sagen, was du willst** — Claude erkennt meistens selbst, welcher
   Skill passt. Das ist der normale Weg.
2. **Mit Schrägstrich aufrufen**, z. B. `/blog-post`. Nutze das, wenn du sicher
   gehen willst, dass genau dieser Ablauf startet.

Wenn du unsicher bist: frag einfach „welcher Skill passt hier?".

---

## 1 · Für dich und diese Seite gebaut

Diese vier sind auf leoniekaiser.com zugeschnitten. Die nutzt du am häufigsten.

### `/blog-post` — neuen Blogpost schreiben

Geführter Ablauf vom Redaktionsplan bis zum fertigen Text. Jeder Schritt wartet
auf deine Freigabe: Themenwahl → Keyword-Check → Überschriften zur Auswahl →
Gliederung → Text → Word-Dokument zum Korrekturlesen → Bildvorgaben → Build-Check.

*Sag zum Beispiel:*
- „nächsten Blogpost schreiben"
- „Post #6 starten"
- „weiter im Redaktionsplan"

### `/post-keyword-recherche` — Keyword-Check auswerten

Wenn du Zahlen aus Google Keyword Planner, Trends oder AnswerThePublic hast und
wissen willst, ob ein Thema trägt. Prüft gegen deine Zielgruppe, hält die
Entscheidung in `strategie/keyword-research-*.md` fest.

*Sag zum Beispiel:*
- „hier die Keyword-Daten für Post #6" *(dann Screenshots oder Zahlen einfügen)*
- „was soll ich als Nächstes für die Keyword-Recherche machen?"

### `/agentic-seo` — SEO und Auffindbarkeit

Prüft die Seite auf SEO-Gesundheit, technische Fehler, Überschriftenstruktur,
strukturierte Daten (JSON-LD), Auffindbarkeit in KI-Suchen (GEO, `llms.txt`) und
Ladegeschwindigkeit. Auf deine Seite angepasst.

*Sag zum Beispiel:*
- „mach einen SEO-Audit"
- „prüf, ob KI-Assistenten meine Seite sauber erfassen können"
- „schreib eine bessere Meta-Description für /leistungen/"
- „stimmen meine strukturierten Daten?"

Ein Wort zur Erwartung: Der Skill sagt dir, was technisch und inhaltlich im Weg
steht. Er kann keine Platzierungen versprechen, und er soll es auch nicht — das
wäre gegen deine eigene Positionierung.

### `/hugo-plan` und `/hugo-learn` — Planen und Nachbereiten

`hugo-plan` nutzt du, wenn eine Änderung größer ist und du erst einen Plan
sehen willst, bevor irgendetwas passiert. `hugo-learn` am Ende einer längeren
Sitzung, damit Gelerntes in der Doku landet.

*Sag zum Beispiel:*
- „wie sollten wir das angehen?"
- „mach mir einen Plan dafür"
- „halt fest, was wir heute gelernt haben"

---

## 2 · Regelmäßig nützlich

### Dokumente erstellen

| Skill | Wofür | Beispielsatz |
|---|---|---|
| `create-docx` / `docx` | Word-Dokumente | „gib mir die Texte als Word-Doc zum Korrekturlesen" |
| `pdf-creator` / `pdf` | PDFs erstellen, zusammenfügen, Text herausziehen | „mach ein PDF daraus" |
| `create-pptx` / `pptx` | PowerPoint | „bau mir eine Präsentation zu X" |
| `xlsx` | Excel | „mach mir eine Vorlage für …" |

### Texte und Marketing

| Skill | Wofür | Beispielsatz |
|---|---|---|
| `copywriting` | Seitentexte schreiben oder überarbeiten | „überarbeite den Text auf der Leistungsseite" |
| `content-strategy` | Themen planen, worüber überhaupt schreiben | „worüber soll ich als Nächstes schreiben?" |
| `social-content` | Social-Media-Beiträge, Redaktionsplan | „mach mir LinkedIn-Posts aus diesem Blogartikel" |
| `linkedin-article` | Lange LinkedIn-Artikel | „schreib einen LinkedIn-Artikel über …" |
| `marketing-psychology` | Warum Menschen kaufen, Denkmodelle | „welche psychologischen Hebel greifen bei Praxisinhaberinnen?" |
| `brand` | Markenstimme, Konsistenz prüfen | „passt dieser Text zu meiner Brand Voice?" |
| `cold-email` | Kaltakquise-Mails | *siehe Hinweis unten* |

**Hinweis zu `cold-email`:** Kaltakquise per E-Mail ist in Österreich nach § 174
TKG ohne vorherige Einwilligung heikel. Der Skill schreibt gute Mails — ob du
sie versenden darfst, ist eine andere Frage. Für Bestandskontakte und
Nachfass-Mails nach einem Gespräch ist er unproblematisch.

### Bilder und Gestaltung

| Skill | Wofür | Beispielsatz |
|---|---|---|
| `banner-design` | Banner für Social Media, Website, Anzeigen | „entwirf ein LinkedIn-Titelbild" |
| `design` | Logos, Farbsysteme, Gestaltungsrichtlinien | „zeig mir Varianten für …" |
| `mermaid-expert` | Diagramme und Ablaufgrafiken | „zeichne mir den Ablauf als Diagramm" |
| `verify-visual` | Visuelles wirklich prüfen, nicht nur behaupten | „schau dir das Ergebnis wirklich an" |

### Werkzeuge

| Skill | Wofür | Beispielsatz |
|---|---|---|
| `git-history-ops` | Wenn Git klemmt (Datei zu groß, Konflikte) | „der Push wird abgelehnt" |
| `x-read-article` | X/Twitter-Beiträge lesen, die sonst blockiert sind | „lies mir diesen X-Post vor" |
| `get-working-time` | Wie viel Zeit steckt tatsächlich im Projekt | „wie viele Stunden habe ich hier reingesteckt?" |
| `find-skills` | Weitere Skills suchen und installieren | „gibt es einen Skill für …?" |

---

## 3 · Eingebaute Befehle (keine Skills)

Die tippst du direkt im Claude-Code-Fenster:

| Befehl | Wirkung |
|---|---|
| `/help` | Hilfe |
| `/clear` | Gespräch zurücksetzen, wenn es zu lang wird |
| `/config` | Einstellungen |
| `/mcp` | Externe Verbindungen (z. B. n8n) autorisieren |
| `/fast` | Schnellerer Antwortmodus |
| `/artifacts` | Deine veröffentlichten Seiten auflisten |

---

## 4 · Ignorieren

Diese sind für andere Projekte gedacht (Alexanders Seite integrations.at,
SuperLeague.TV) oder für Software-Entwicklung, die dich nicht betrifft. Sie
schaden nicht, sie greifen bei dir nur nicht sinnvoll:

`angular-conventions` · `dotnet-conventions` · `copilot-sdk` · `create-wif` ·
`create-agent-team` · `agent-learning-loop` · `agentic-eval` ·
`context7-auto-research` · `visualize-conversation` · `sequential-navigation` ·
`setup-agentic-wf` · `story-first-production` · `ui-styling` · `ui-ux-pro-max` ·
`design-system` · `slides` · `create-ebook` · `hugo-attach-action-behavior` ·
`hugo-config` · `hugo-create` · `hugo-debug` · `hugo-deploy` · `hugo-design` ·
`hugo-docs` · `hugo-expert` · `hugo-maf` · `hugo-mcp-reference` ·
`hugo-seo` *(durch `agentic-seo` ersetzt, siehe unten)*

**Zu `hugo-seo`:** Das ist die ältere, kleinere Fassung von `agentic-seo` und
noch auf integrations.at ausgerichtet. Sie steht vorerst daneben, damit wir
vergleichen können. Wenn `agentic-seo` sich bewährt, kann `hugo-seo` weg.

---

## Wenn nichts passt

Du musst keinen Skill kennen. Sag einfach, was du erreichen willst — auf
Deutsch, in ganzen Sätzen. Claude sucht sich den passenden Ablauf selbst, und
wenn keiner passt, arbeitet er ohne.
