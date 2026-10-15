# WebMCP — die Website noch einmal bauen, diesmal für Agenten

Stand 21.09.2026. Geschrieben nach drei Rollouts an echten Kundenseiten und dem Vergleich mit Alex Kastils Umsetzung
auf integrations.at.

## Worum es geht

Ein KI-Assistent kann eine normale Website nur **lesen** und muss raten, was etwas kostet oder
wann es stattfindet. Mit WebMCP kann er sie stattdessen **fragen**: Die Seite meldet Werkzeuge
an, der Assistent ruft sie auf und bekommt strukturierte Antworten aus der echten Quelle.

Alex Kastil sinngemäß: *„Im Prinzip muss man die ganze Webseite über WebMCP noch einmal machen —
diesmal für Agenten. Die optische Seite lässt du wie sie ist."* Und: *„Wer hier nicht optimiert,
wird nicht einmal gefunden, da kann die Seite noch so gut aussehen."*

🔴 **Frist: Chrome führt WebMCP nur im Origin-Trial, Ende 17.11.2026.** Ohne gültiges Token
melden sich die Werkzeuge bei **keinem** Besucher an — ohne Fehlermeldung. Das Token kommt je
Domain aus der Chrome-Origin-Trial-Konsole und steht als
`<meta http-equiv="origin-trial" content="…">` im `<head>`, eingehängt mit Priorität 1.
**Vor dem 17.11.2026 erneuern oder die Konstante leeren** — ein leeres Meta-Tag wäre schlechter
als keines, es sieht nach Einbau aus und wirkt nicht.

## Die zwei Hälften

**1. Imperativ — Werkzeuge per Skript.**
```js
function kontextFinden() {
  if (typeof document !== 'undefined' && document.modelContext
    && typeof document.modelContext.registerTool === 'function') { return document.modelContext; }
  if (typeof navigator !== 'undefined' && navigator.modelContext
    && typeof navigator.modelContext.registerTool === 'function') { return navigator.modelContext; }
  return null;
}
```
🔴 **Die API ist am 21.07.2026 von `navigator.modelContext` nach `document.modelContext`
umgezogen.** Wer nur die alte Stelle kennt, registriert nichts — und merkt es nicht, weil kein
Fehler kommt. Immer beide prüfen, `document` zuerst.

**2. Deklarativ — Attribute am vorhandenen Formular.** Das ist der billigste Schritt mit der
größten Wirkung und zugleich der Punkt, an dem die meisten Seiten null Punkte holen.

```html
<form toolname="anfrage_senden"
      tooldescription="Übermittelt eine unverbindliche Anfrage an … Erwartet: …
        Dies ist KEINE Buchung: verbindlich gebucht wird ausschließlich …">
  <input name="…" type="email" required autocomplete="email"
         pattern="[^@\s]+@[^@\s]+\.[^@\s]+"
         aria-label="E-Mail-Adresse für die Antwort"
         toolparamdescription="E-Mail-Adresse der anfragenden Person. Pflichtfeld.">
```

🔴 **`toolparamdescription` an JEDEM Feld** ist Alex' eigentlicher Kniff — er steht in keiner
Anleitung, nur in seinem Quelltext. Ohne ihn kann ein Agent bei Feldern wie `avia_1_1` oder
`name-1` unmöglich wissen, welches die E-Mail-Adresse ist.

**Die Beschreibung sagt, WAS zurückkommt bzw. erwartet wird**, nicht nur was das Werkzeug tut.
Und sie zieht die Grenze: Ein Agent **bereitet vor und übergibt an den Menschen**, er schließt
nichts ab. Das ist auch Shopifys Muster — Warenkorb ja, Kasse Mensch.

## Der Wissenskatalog (Alex' acht Bausteine)

1. Kundenfragen und Antworten · 2. Leistungen und Einzugsgebiete · 3. **Fachkunde und Nachweise**
· 4. Häufige Fragen · 5. **Transparente Preise** · 6. Regeln und Abläufe (Storno, Zahlung,
Fristen) · 7. Bewertungen und Stimmen · 8. echte Gesprächsmitschriften.

*Altes Internet* = SEO, Keywords, Backlinks. *Neues Internet* = belegte Inhalte, Struktur, ein
Agent, der für die Marke sprechen kann.

🔴 **Baustein 3 richtig gemacht:** Ein Nachweis, dessen Beleg-Adresse auf das **eigene**
Impressum zeigt, ist Selbstauskunft, kein Nachweis. Brauchbar sind **fremde** Prüfstellen:
- Firmenbuch über die öffentliche JustizOnline-Schnittstelle
  (`/jop/service/fba/<FN>` — **ohne** `secure/`-Präfix, also ohne Anmeldung)
- UID über die EU-VIES-REST-Abfrage (`…/vies/rest-api/ms/<LAND>/vat/<NR>`)
Jeder Eintrag bekommt ein ehrliches Feld `beleg_art: selbstauskunft | fremdauskunft` und
`unabhaengig_pruefbar: true|false`. Was nicht belegbar ist (Ausstellungsdatum, Ablauf,
Zertifikatsnummer), wird **weggelassen**, nicht geschätzt.

🔴 **JustizOnline ist eine Angular-Anwendung — der HTTP-Status der Seite beweist nichts**, jeder
Pfad liefert dieselbe Hülle. Eine Prüf-URL gilt erst als geprüft, wenn die **Daten** kommen.

## Messen — hier geht fast alles schief

**1. Der Prüfer scannt EINE URL.** webmcpverify.com bewertet genau die Adresse, die man eingibt.
Liegt das Formular auf `/kontakt/` und man scannt die Startseite, sind A1 (deklarative
Registrierung, 15 Punkte) und A3 (Feldqualität, 10 Punkte) **immer null** — egal wie gut gebaut
wurde. Erst die Seite mit dem Formular scannen, dann urteilen.

**2. Caches verdecken den eigenen Bau.** Antwortkopf **vor** dem Körper lesen: `cf-cache-status`,
`age`, `wpo-cache-status`, `x-*-cache`. Ein `HIT` mit `age > 0` macht jede Aussage über den
Körper wertlos. Nach jedem Deploy leeren, 8–10 s warten, dann messen.

**3. `<script src>` ist nicht die Ladung.** Zusammenfasser (WP-Optimize, Autoptimize, WP Rocket)
bündeln Fußbereich-Skripte und laden sie per `loadAsync(...)` aus einem Inline-Schnipsel — im
HTML steht dann **kein** `<script src="…">`. Die Werkzeuge stecken im Bündel. Suchen nach
`loadAsync`, `data-src`, Bündelpfaden — **und die Bündeldatei selbst laden und darin greppen**.

**4. Der belastbarste Beleg ist der Browser:** `document.modelContext` auslesen und ein Werkzeug
per `executeTool` antworten lassen. Was dort antwortet, ist da.

**Bewertungsraster (webmcpverify):** A Tool Registration 40 % (A1 deklarativ 15, A2 imperativ 15,
A3 Feldqualität 10) · B AI Discoverability 30 % (Schema 8, llms.txt 7, Meta 5, OG 5, robots 5) ·
C Security & Compatibility 20 % · D Best Practices 10 % (sprechende Verb-Namen, Beschreibungen
über 20 Zeichen, vollständiges inputSchema, `readOnlyHint`).

## Wo der Eingriff hingehört

🔴 **Bei Baukasten-Seiten (Nicepage, Enfold, Elementor) NIE in den Seiteninhalt.** Nicepage
speichert doppelt (`_np_html` für den Editor, `_np_publish_html` für die Auslieferung) und
überschreibt beim nächsten Veröffentlichen alles. Enfold schreibt `post_content` beim Speichern
aus `_aviaLayoutBuilderCleanData` zurück.

**Der Weg, der hält:** ein eigenes Plugin, das serverseitig in die Ausgabe eingreift —
`do_shortcode_tag` für ein einzelnes Shortcode-Ergebnis, oder ein Ausgabepuffer bei
`template_redirect`. Serverseitig ist Pflicht: **Der Prüfer liest statisches HTML**, Attribute,
die erst JavaScript setzt, zählen nicht.

Beim Puffer auf die **Priorität** achten: Ein Performance-Plugin, das selbst puffert, muss außen
liegen, damit das Ergebnis auch im HTML-Cache landet. Ein Puffer mit negativer Priorität läuft
**nach** dem eigenen — was dort erzeugt wird (z. B. eine ausgetauschte Fußzeile), sieht der
eigene Filter nie.

## Formular-Fallen (teuer, alle real passiert)

🔴 **`name`-Attribute nicht ändern**, solange das Formular-Plugin darüber die Mail-Zuordnung
macht. Ausnahme, aber nur mit Beleg: Elemente, die **kein** Feld des Baukastens sind (siehe
unten) — dort hängt keine Zuordnung dran.

🔴 **`type="tel"` kann das Feld stillschweigend killen.** Enfolds `contact.js` sammelt nur
`textarea, select, input[type=text], input[type=checkbox], input[type=hidden], input[type=email]`.
Ein auf `tel` umgestelltes Feld wäre **nie** in der Mail gelandet. Stattdessen `type="text"` +
`inputmode="tel"` + `autocomplete="tel"` + `pattern`.

🔴 **`type="date"`** verhindert Zeiträume („27.12. bis 31.12.") — bei Buchungsanfragen falsch.

🔴 **Ein Eingabeelement im HTML ist noch kein Feld des Formularsystems.** Neun Häkchen, die als
roher HTML-Block im Inhalt eines Textfelds standen, wurden beim Absenden verworfen — der
Mailtext wird aus den **deklarierten** Elementen gebaut. Zusätzlich sammelt Enfolds JS Häkchen
als `dataObj[name] = true`: gleicher Schlüssel ⇒ der letzte überschreibt alle, und der `value`
(„Snowboardkurse") geht verloren. **`name[]` heilt das nicht**, der Verlust passiert im Browser.
Abhilfe: je Häkchen ein eigener Name, und den Mailtext über den passenden Filter ergänzen.

🔴 **Prüfen heißt absenden.** Nach jeder Übernahme eines fremden Formulars einmal wirklich
absenden und die angekommene Mail Feld für Feld gegen das sichtbare Formular halten. Der
Augenschein am Formular beweist nichts.

🔴 **Fremde Formulardienste sind ein stiller Ausfallpunkt.** Ein Nicepage-Formular postet an
`forms.nicepagesrv.com`; läuft der Tarif aus, greift ein Kontingent von 50 Einsendungen
insgesamt — danach kommt nichts mehr an, **ohne Fehlermeldung**, und die Seite meldet weiter
„Ihre Anfrage wurde versendet!". Bei einem Kundenprojekt so passiert, monatelang unbemerkt.

## robots.txt — meistens der falsche Hebel

Zwei fehlende Punkte im Prüfer verlocken dazu, ausdrückliche `Allow`-Zeilen je KI-Bot
einzutragen. Vorher nachsehen: **Ist die Seite ohnehin schon für alle offen?** Dann wäre es ein
grüner Haken ohne Wirkung. Die einzige wirksame Änderung wäre die **umgekehrte** — Trainings-
Crawler aussperren —, und das ist eine Sichtbarkeitsentscheidung des Kunden, kein Handwerk.

Unterscheiden: **auf Nutzeranfrage** holende Assistenten (`ChatGPT-User`, `Claude-User`,
`PerplexityBot`) gegen **Trainings-Crawler** (`GPTBot`, `CCBot`, `Bytespider`). Wer Sichtbarkeit
will, ohne den Volltext zum Mitnehmen anzubieten, erlaubt die ersten und sperrt die zweiten.

Bei virtuellen robots.txt (Rank Math) ist eine Änderung **nicht per Datei zurückdrehbar**, nur
über die Plugin-Einstellungen — schlechte Umkehrbarkeit für wenig Wirkung.

## llms.txt und llms-full.txt

`/llms.txt` = die Kurzfassung, `/llms-full.txt` = der ganze Bestand. 🔴 **Berechnet ausliefern,
nicht als statische Datei** — aus derselben Quelle, aus der auch die Werkzeuge antworten. Eine
statische Datei veraltet still, eine berechnete kann es nicht. `X-Robots-Tag: noindex` setzen.

Inhalt nur Belegtes: Betrieb, Leistungen mit Preisen, Termine mit Buchungslink, FAQ, Standorte,
Nachweise, Bedingungen. Widersprüche zwischen `llms.txt` und dem Schema sind teuer — Assistenten
lesen **beides**. Klassiker: Standort im Schema, Firmensitz in der llms.txt, beide unkommentiert.
Dann beide nennen und **benennen**, welcher welcher ist.

## Vorgehen bei einer neuen Kundenseite

1. **Bestand messen**, nicht raten: Formulare finden (wo, welches Plugin, wohin posten sie),
   Schema, llms.txt, robots.txt, Caches, Origin-Trial-Token.
2. **Token holen** für die Domain und einhängen (Priorität 1). Ohne Token wirkt nichts.
3. **Deklarativ zuerst** — `toolname`/`tooldescription`/`toolparamdescription` am vorhandenen
   Formular, serverseitig. Billigster Schritt, 25 von 100 Punkten.
4. **Werkzeuge** aus der besten vorhandenen Quelle ableiten (Buchungssystem-JSON-LD, eigene
   REST-Route, Seiteninhalte) — nie aus dem Gedächtnis, nie erfunden. Täglicher Auffrisch-Lauf.
5. **Jede Änderung mit Selbstsicherung**: vorher/nachher am ausgelieferten HTML vergleichen
   (`name`-Listen, Feldzahlen, sichtbarer Text) und **sich selbst verwerfen**, wenn etwas
   abweicht, das nicht abweichen darf.
6. **Sicherung außerhalb des Webroots** und ein Ein-Schritt-Rückweg, der im Bericht steht.
7. **Messen wie oben** — Cache leeren, richtige URL, Bündel öffnen, im Browser gegenprüfen.

## Beispielstand

| Seite | Werkzeuge | Besonderheit |
|---|---|---|
| integrations.at (Alex, Maßstab) | 11 | `list_certifications` mit `credentialId`/`credentialUrl`/Transcript |
