# Google-Qualitätsrisiko — Helpful Content, KI-Inhalte, Ranking-Updates

Stand 10.10.2026. Prüfliste nach dem Vorbild von Alexander Kastils Skill `check-google-rating` (MIT), in eigenen Worten und um die österreichische KMU-Lage erweitert.
Ergebnis ist eine **Risikoeinschätzung mit Belegen**, keine Ranking-Prognose. Google sagt selbst, dass
Daten der Quality Rater nicht direkt ins Ranking eingehen — also nie „Google bewertet dich mit X“ schreiben.

Laden, wenn der Nutzer fragt: „google bewertung“, „ranking eingebrochen“, „helpful content“,
„ist die seite google-tauglich“ (auch: Traffic-Einbruch, KI-Texte, Core Update).

## Eingaben

Eine oder mehrere URLs · eine Domain (Stichprobe) · ein Entwurf (Text/Datei) vor der Veröffentlichung ·
optional das Datum, ab dem der Verkehr fiel. Ist unklar, was vorliegt: einmal fragen, sonst loslegen.
Kundenseiten (WordPress/Nicepage, kein lokaler Stand) nur lesend und nur mit genannter URL; Live-Änderungen
bleiben Vorschlag (siehe Vorschaltregeln in `SKILL.md`).

## Schritt 1 — Maßstab live laden

Googles Seiten ändern sich oft. Zur Laufzeit abrufen (WebFetch) und je Seite das Datum „Last updated“
notieren; nichts aus dem Gedächtnis zitieren:

- `developers.google.com/search/docs/fundamentals/creating-helpful-content`
- `developers.google.com/search/docs/fundamentals/using-gen-ai-content`
- `developers.google.com/search/docs/essentials/spam-policies` (Abschnitt „scaled content abuse“)

Steht dort ein Kriterium, das unten fehlt, nimmst du es in diese Prüfung auf und nennst es im Bericht.
Lässt sich eine Seite nicht abrufen: sagen, welche, und das Urteil als „Maßstab veraltet möglich“ markieren.

## Schritt 2 — Ranking-Updates der letzten 90 Tage

Quelle: `status.search.google.com/summary`, genauer mit Start und Ende: `…/incidents.json`.

- Core-, Spam- und sonstige Ranking-Updates der letzten 90 Tage mit Startdatum und Dauer auflisten.
- Ein noch laufendes Update ausdrücklich markieren (Messungen davor/danach sind dann unsicher).
- Nennt der Nutzer ein Einbruchsdatum: sagen, in welches Update-Fenster es fällt — oder dass keines passt.
  **Nur Korrelation.** Nie „das Update hat die Seite getroffen“ schreiben; andere Ursachen (Relaunch ohne
  Weiterleitungen, Tracking-Umbau, Saison, Technik) sind erst auszuschließen → `relaunch-redirects.md`,
  `audit-technical.md`.

## Schritt 3 — Inhalte einsammeln

- URL: abrufen; bei Sperre oder reinem JavaScript-Rendering den Browser nehmen oder den Text erbitten.
- Domain: höchstens acht Seiten — Start, Über uns, eine Autorenseite, vier bis fünf typische Inhaltsseiten
  (neueste und verkehrsstärkste, falls bekannt). Auf Schablonen und Beinahe-Dubletten achten.
- Entwurf: Datei oder Text direkt lesen.
- Mitnehmen: title, Meta-Beschreibung, JSON-LD, Alt-Texte, Autorenzeile, Veröffentlichungs- und Änderungsdatum.

## Schritt 4 — Bewerten (Pass / Risk / Fail, je mit Beleg)

Jedes Kriterium bekommt **eine Zeile Beleg**: ein kurzes Zitat (unter 15 Wörter) oder eine Beschreibung.
Ohne Beleg keine Wertung — dann „nicht beurteilbar“ und warum.

**Hauptinhalt**
- Aufwand: sichtbare Handarbeit, eigene Analyse, eigene Werkzeuge/Medien. Fail bei erkennbarer Massenware ohne Redaktion.
- Eigenständigkeit: Information oder Blickwinkel, den es anderswo nicht gibt. Fail, wenn nur umformuliert wird.
- Handwerk: klar geschrieben, sauber gemacht, Werkzeuge funktionieren.
- Richtigkeit: drei bis fünf Tatsachenbehauptungen per Websuche gegenprüfen, Fehler nennen. Strenger bei
  Gesundheit, Geld, Sicherheit, Recht (YMYL).

**Wer, Wie, Warum**
- Wer: Autorenzeile, wo sie zu erwarten ist; Autorenseite mit echtem Hintergrund. Fail bei erfundenen
  Personen, KI-Porträts, falschen Titeln.
- Wie: Hinweis auf KI/Automatisierung, wo ein Leser berechtigt fragen würde, wie der Inhalt entstand.
- Warum: für Menschen geschrieben, nicht um Suchverkehr einzufangen.

**Suchmaschine-zuerst-Warnzeichen**
- viele Themen abseits des Kerngeschäfts · Trendjagd ohne Zielgruppe · Aufblähen auf eine Wortzahl ·
  Antworten auf Fragen ohne Antwort (unbestätigte Termine u. Ä.) · Datum geändert ohne inhaltliche Änderung ·
  Zusammenfassungen fremder Quellen ohne Mehrwert.

**Vertrauenssignale (E-E-A-T)**
- Quellen genannt, Über-uns, Kontakt, Erfahrung aus erster Hand sichtbar.

**Generative KI**
- Anzeichen ungeprüfter KI-Ausgabe: erfundene Fakten, Floskeln, widersprüchliche Angaben.
- Metadaten (title, Beschreibung, JSON-LD, Alt-Texte) stimmen mit der Seite überein.
- Onlineshop: KI-Bilder mit IPTC-DigitalSourceType `TrainedAlgorithmicMedia`, KI-Produktdaten gekennzeichnet.

**Seitenerlebnis**
- Nur Offensichtliches (aufdringliche Einblendungen, kaputtes Layout am Handy). Core Web Vitals nicht
  schätzen — PageSpeed Insights bzw. `setup-vitals.md` empfehlen.

## Zusatz für österreichische KMU-Seiten

Zusätzlich zu Schritt 4, jeweils Pass / Risk / Fail mit Beleg:

1. **Impressum und E-Commerce-Gesetz (ECG):** Impressum von jeder Seite in einem Klick erreichbar; Name bzw.
   Firma, Anschrift, E-Mail, Unternehmensgegenstand, Firmenbuchnummer und -gericht bzw. UID, soweit zutreffend;
   Aufsichts-/Kammerangaben bei reglementierten Gewerben. Fehlt etwas: als Rechtsrisiko melden, nicht
   als Rechtsberatung — Klärung mit dem Kunden bzw. Anwalt.
2. **Firmen- und Autorensignale:** stimmen Firmenname, Adresse und Telefon über Impressum, Kontaktseite,
   JSON-LD (`Organization`/`LocalBusiness`) und ggf. Google-Unternehmensprofil überein? Echte Personen mit
   nachprüfbarer Rolle statt anonymer „Redaktion“; Referenzen/Bewertungen nur, wenn belegbar.
3. **KI-Kennzeichnung (Art. 50 KI-VO, seit 02.08.2026):** Chat-Assistenten, KI-Stimmen und -Avatare brauchen
   einen **sichtbaren** Hinweis bei der ersten Interaktion, nicht nur in AGB/Datenschutz; Stimmklon einer
   echten Person = Deepfake-Fall mit dokumentierter Einwilligung. Redigierte Texte, KI-Illustrationen ohne
   echte Personen, WebMCP und llms.txt sind nicht kennzeichnungspflichtig. Aktuellen Stand der Auslegung
   vor dem Urteil bei RTR/Kommissions-FAQ nachlesen.
4. **Stimmigkeit prüfen:** Sagt die Seite „von Menschen geschrieben“ oder zeigt sie eine Menschen-Autorenzeile,
   obwohl Teile KI-erzeugt sind? Sagt die Datenschutzerklärung, welche KI-Dienste Daten bekommen? Weicht
   Seite, Datenschutz und Hinweis voneinander ab, ist das ein Befund — sowohl für Google („Wie“) als auch
   rechtlich.

## Schritt 5 — Bericht

1. Gesamturteil **Niedrig / Mittel / Hoch** mit zwei Sätzen Begründung.
2. Update-Kontext aus Schritt 2 (nur Korrelation, laufende Updates markiert).
3. Befundtabelle: Kriterium · Pass/Risk/Fail · Beleg (inkl. Zusatz).
4. Die wichtigsten Korrekturen, nach Wirkung geordnet, jede konkret — bei Texten der Ersatztext, nicht die Beschreibung.
5. Verwendete Maßstabs-Versionen (Seitenname + „Last updated“).
6. Quellenliste.

Einzelne Seite oder Entwurf: Bericht in der Antwort. Domain-Prüfung oder zum Weitergeben: als Dokument ablegen.

## Regeln

- **Keine Kennzahl erfinden** (Verkehr, Positionen, Web-Vitals-Werte). Sagen, was zum Messen nötig wäre
  (Search Console, PageSpeed Insights, Analytics-Zugang).
- Zitate unter 15 Wörtern, höchstens eines je Quelle; sonst umschreiben.
- Trennen: was Googles Dokumente sagen — und was dein eigenes Urteil ist.
- Kein Ranking-Versprechen. Update-Zusammenhang bleibt Korrelation.
- Nichts an einer Live-Seite ändern ohne OK des Seiteninhabers; Rechtsfragen (Impressum, Art. 50) als Hinweis, nicht als Rechtsauskunft.
