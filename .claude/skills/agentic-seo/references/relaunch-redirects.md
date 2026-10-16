# Relaunch-Weiterleitungen — Verfahren und Fallen

**Erprobt an einem Relaunch** (Contao 92 Seiten DE/EN/NL → WordPress 19 Seiten DE).
189 Weiterleitungen gesetzt, alle nachgemessen. Dieses Blatt ist die Anleitung für den nächsten Fall.

## Der Schaden, um den es geht

Nach einem Relaunch greift bei WordPress+Rank Math oft eine **Pauschalregel**
(`redirections_fallback: homepage`): Jede unbekannte Adresse springt auf die Startseite.
Google wertet das als **Soft 404** und gibt die Empfehlungskraft eingehender Links **nicht** weiter
([Google: Site move with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)).

**Probe, ob die Pauschalregel greift:** eine frei erfundene Adresse abrufen.
Landet `/frei-erfunden-xyz123.html` auf der Startseite statt auf 404 → Fallback ist aktiv.

## Schritt 1 — Bestand ermitteln

```bash
# Alle je archivierten Adressen (belastbare Untergrenze)
curl --compressed "http://web.archive.org/cdx/search/cdx?url=<domain>*&output=json&collapse=urlkey&fl=original,timestamp&filter=statuscode:200"
```
Dazu, falls vorhanden: CMS-Archiv (Contao `tl_page`), Sitemaps der alten Seite.
**Die echte Zahl der betroffenen Links steht in der Search Console** unter
*Links → Externe Links → Meistverlinkte Seiten*. Von außen ist sie nicht messbar.

## Schritt 2 — Zuordnen

Je alter Adresse: thematisch passende neue Seite. Wo es keinen Nachfolger gibt (FAQ, Jobs, Verleih),
ist **410 die ehrliche Antwort**, keine Weiterleitung — Google nimmt die Adresse sauber aus dem Index.

**Fremdsprachige Adressen:** Wenn die neue Website einsprachig ist, der **Buchungs-/Shop-Teil aber
mehrsprachig**, gehören `/en/…` und `/nl/…` auf dessen Sprachfassung. Slugs vorher prüfen — sie sind
meist übersetzt (`/en/ski-courses-children/`, `/nl/skilessen-kinderen/`), nicht wörtlich abgeleitet.

## Schritt 3 — Einbauen (zwei Ebenen!)

**Deutsche/Standard-Adressen → Rank Math** (Datenbank, `<prefix>_rank_math_redirections`).
`sources` ist ein serialisiertes PHP-Array:
```
a:1:{i:0;a:3:{s:7:"pattern";s:<LEN>:"<pfad-ohne-fuehrenden-slash>";s:10:"comparison";s:5:"exact";s:6:"ignore";s:0:"";}}
```
Einspielen als lesbare SQL-Datei mit `wp db query < datei.sql` — **kein Wegwerf-PHP-Skript**
(sichtbare Befehle).

🔴 **Fremdsprachige Adressen brauchen die `.htaccess`.** Läuft WPML im Verzeichnis-Modus
(`icl_sitepress_settings.language_negotiation_type: 1`), fängt es `/en/` und `/nl/` ab, **bevor**
Rank Math überhaupt gefragt wird. Nur eine Regel auf Webserver-Ebene wirkt davor.

## Die vier Fallen der `.htaccess`

1. **`Redirect` ist Präfix-Match.** `Redirect 301 /en/ …` fängt *alles* unter `/en/` ab. Deshalb:
   **spezifischste Pfade zuerst, Sprachwurzeln ganz ans Ende.** Sortierung nach Pfadlänge absteigend.
2. **Query-Strings funktionieren nicht.** `Redirect 410 /nl/tarieven?pdf=58` ist wirkungslos —
   Apache ignoriert alles ab `?`. Solche Zeilen weglassen.
3. **Umlaute brauchen beide Schreibweisen** — die dekodierte *und* die prozentkodierte:
   ```
   Redirect 301 /kinder/kinder-anfänger.html /kinderkurse/
   Redirect 301 /kinder/kinder-anf%C3%A4nger.html /kinderkurse/
   ```
4. **Vorher kopieren.** Ein Tippfehler in der `.htaccess` legt die ganze Website mit 500 lahm.
   Nach dem Einbau **sofort die Startseite abrufen**.

## Schritt 4 — Rauchprobe, die zählt

```bash
# seriell, ohne www, mit echtem User-Agent; parallele Läufe erzeugen falsche Timeouts
curl -sI --max-time 25 -A 'Mozilla/5.0' "https://<domain><pfad>"
```
Prüfen: Statuscode **und** `Location`. Erwartet 301 bzw. 410.
Bei 410 gibt es kein `Location` — das ist richtig, nicht kaputt.

🔴 **Nach dem Eingriff den ganzen Umkreis messen, nicht nur das Geänderte:** Startseite, Sitemap,
robots.txt. Ein `wp rewrite flush
--skip-plugins` beim Aufräumen amputierte die Sitemap-Route, und die lief danach in genau den
Redirect-Fallback, den wir gerade reparierten.

## Zeitfenster

Google verwirft das Signal einer Adresse, sobald sie erneut besucht und als Soft 404 eingestuft
wird — laufend, Adresse für Adresse. Google empfiehlt, Weiterleitungen **mindestens ein Jahr** zu
halten. Je früher nach dem Relaunch, desto mehr lässt sich retten.

## Messmethodik — Pflicht bei jedem Website-Befund

🔴 **Nie am ausgelieferten Quelltext urteilen, wenn die Seite Widgets oder eine SPA einbindet.**
Shop-Widgets ersetzen leere Platzhalter-Links erst im Browser; die leeren Reste bleiben mit
**0×0 px** im DOM stehen. Am 05.09.2026 waren dadurch *drei von vier* Hauptbefunden eines
Kunden-PDFs Artefakte (`gotcha-quelltext-statt-gerendertes-dom`).

```js
// im gerenderten DOM messen, mit Sichtbarkeitstest:
function sichtbar(el){const r=el.getBoundingClientRect(),s=getComputedStyle(el);
  return r.width>0 && r.height>0 && s.display!=='none' && s.visibility!=='hidden';}
// href-ATTRIBUT vs. href-PROPERTY vergleichen — Widgets setzen oft nur die Property
// document.body.innerText statt HTML: was dort nicht steht, sieht kein Gast
```
Und wo möglich: **klicken**. Ein Befund über eine Schaltfläche, die nie angeklickt wurde, ist kein Befund.
