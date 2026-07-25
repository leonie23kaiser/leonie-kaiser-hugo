# Blog-Einzelkonzepte — Leonie Kaiser Journal

*Detail-Briefings pro Beitrag: Keyword, Search-Intent, Content-Gap, Meta, interne Links
und H1/H2/H3-Outline. Grundlage: `strategie/blog-konzept.md` (Gesamtstrategie, schmerz-
geführt + Compliance-first), `strategie/service-katalog.md` (Leistungen & Beispiel-Szenarien
als Rohmaterial für die Outlines), `strategie/linkedin-profil.md` (E-E-A-T), `AGENTS.md`
(Brand Voice, kanonisch). Stand: 2026-07-15.*

> Suchvolumen und Wettbewerb sind vor dem Schreiben grob gegen die reale Google-Suche
> (Autocomplete, „Ähnliche Fragen", Search Console) zu prüfen — die Keywords hier sind
> begründete Vorschläge, keine gemessenen Zahlen.

> **CTA-Grundsatz (alle Posts):** genau **ein** CTA — die kostenlose KI-Potenzialanalyse
> (kanonisch in AGENTS.md §12; kein Newsletter vorhanden). Das *Framing* pro Post
> variieren (segmentspezifisches Ergebnis + ggf. Referenz), damit der CTA passend statt
> generisch wirkt — nie „kostenlos, kein Verkaufsgespräch".

> **Diese drei sind das Launch-Paket:** #1 Vorstellung (persönlich), #2 No-Shows am
> Segment Physiotherapie, #3 Datenschutz. Erst diese drei ausarbeiten, dann schaut Leonie,
> wie es ihr damit geht — **danach** die weiteren.

---

## Aufbau eines Blogposts (Layout, Bilder, hervorgehobene Elemente)

Deine Frage: „Wie sieht die Struktur eines einzelnen Blogposts aus, wo gibt es Bilder,
Boxen etc.?" — So ist ein Beitrag aufgebaut (das Journal-Layout `layouts/journal/single.html`
liefert Rahmen + CTA; alles dazwischen kommt aus dem Markdown-Text):

1. **Kopfbereich (automatisch):** kleines Kategorie-Label · **H1 (Titel)** · Kurzbeschreibung ·
   Meta-Zeile (Autorin, Datum, Lesezeit).
2. **Beitragsbild (Hero), empfohlen:** ein Bild direkt unter dem Titel — setzt die Stimmung
   und macht die Vorschau (Social/LinkedIn) attraktiv.
3. **Einstieg:** 2–3 Sätze, die den Schmerz/Wunsch aufgreifen (gern ein O-Ton der Zielgruppe).
4. **Fließtext mit H2/H3-Zwischenüberschriften**, scanbar. Alle 2–3 Absätze ein optisches
   Element, damit es nicht „wall of text" wird:
   - **Hervorhebungs-Box (Callout):** ein Merksatz, eine Definition oder ein Praxis-Tipp,
     farblich abgesetzt (z. B. dezent in Teal). Gut für „Auf einen Blick"-Kästen.
   - **Aufzählungen / nummerierte Listen** für Schritte und Ursachen.
   - **Zwischen-Bild oder einfache Grafik** (z. B. „Vorher → Nachher", ein Ablauf in 3
     Schritten) — lockert auf und eignet sich fürs Teilen.
   - **Zitat/Kunden-O-Ton** als abgesetztes Blockzitat.
5. **Beispielszenario-Box** (klar als *illustrativ* gekennzeichnet) — abgesetzt.
6. **FAQ-Block** (3–5 Fragen) — SEO/GEO.
7. **CTA-Box (automatisch):** die Potenzialanalyse in einer farbigen Box am Ende.
8. **Tags** (Pills) + „Mehr aus dem Journal" (automatisch).

> **Technischer Hinweis (fürs Dev/Umsetzung):** Hervorhebungs-Boxen und Beispiel-Boxen
> gibt es im Layout noch nicht als fertige Bausteine — die bauen wir bei der Umsetzung
> einmal als wiederverwendbare Shortcodes (`{{< callout >}}`, `{{< beispiel >}}`). Bilder
> laufen über die bestehende Bild-Pipeline (`assets/images/` + `picture.html`).

### Bilder — Vorschläge & Ablauf
**Ablauf, wie von dir vorgeschlagen:** Ich liefere pro Beitrag **Bild-Ideen** (Motiv +
Stimmung + Suchbegriffe für die Bilddatenbank). **Du suchst passende Bilder** aus und gibst
sie mir. **Dann erstelle ich** ALT-Texte (barrierefrei + SEO), Bildunterschriften, den
Dateinamen (sprechend, mit Keyword) und die Social-/Hashtag-Vorschläge fürs Teilen. Pro
Beitrag reichen meist **1 Hero-Bild + 1 Zwischenbild**. Motiv-Grundsätze: echt und ruhig,
keine Stockfoto-Klischees (kein „Roboterhand tippt Hologramm"), Menschen/Praxisalltag statt
Tech, hell und warm zur Marke. Konkrete Bild-Ideen stehen unten bei jedem der drei Posts.

---

## Keyword gegen die reale Suche prüfen (Kurzanleitung)

Die Keywords in diesem Doc sind begründete Vorschläge — **vor dem Schreiben** kurz gegen
die echte Google-Suche gegenchecken. 10 Minuten pro Post genügen, alles kostenlos:

1. **Google-Autocomplete.** Keyword ins Suchfeld tippen und schauen, was Google
   automatisch vorschlägt — das sind reale, häufige Suchanfragen. Oft findet sich hier
   eine bessere, konkretere Formulierung als die geplante.
2. **„Ähnliche Fragen" / „Nutzer fragen auch" (People Also Ask).** Der aufklappbare
   Frageblock mitten in den Suchergebnissen. Jede Frage ist ein potenzieller H2 oder
   FAQ-Eintrag — **direkt als Struktur übernehmen.**
3. **„Ähnliche Suchanfragen"** ganz unten auf der Ergebnisseite — liefert verwandte
   Begriffe (semantische Keywords) für den Text.
4. **Die Ergebnisseite selbst lesen.** Wer rankt auf Seite 1? Sind es Software-Anbieter
   (dann haben wir eine inhaltliche Lücke, siehe Content-Gap) oder starke Fachartikel?
   Passt die Antwortlänge zu unserem geplanten Beitrag? Ist die Suchintention wirklich
   informierend (Blog-tauglich) oder rein kommerziell (dann eher eine Landingpage)?
5. **Google Trends** (trends.google.com) — zeigt, ob ein Thema steigt oder fällt, und
   erlaubt Vergleich zweier Formulierungen. Region auf Österreich/DACH stellen.
6. **Kostenlose Keyword-Tools für Volumen-Schätzung:** Google Keyword Planner (mit
   Google-Ads-Konto), AnswerThePublic (Fragen rund ums Thema), Ubersuggest (begrenzt
   gratis). Zahlen sind grobe Richtwerte, keine Wahrheit — die Intention zählt mehr.
7. **Sobald der Blog live ist: Google Search Console.** Das ehrlichste Werkzeug — zeigt,
   für welche Begriffe die Seite *tatsächlich* erscheint. Nach 6–8 Wochen prüfen und die
   Beiträge auf real gesuchte Formulierungen nachschärfen (`lastmod` neu).

**Faustregel:** Lieber ein etwas kleineres, sehr konkretes Long-Tail-Keyword mit klarer
Intention als ein großes, hart umkämpftes Kopf-Keyword. Wir gewinnen über Spezifik und
Vertrauen, nicht über Volumen.

---

## Post #1 — Vorstellung mit Leser-Hook

### Eckdaten
- **Primär-Keyword:** „Praxis hängt an der Inhaberin" — **dieser Post hat ein echtes
  Keyword-Thema**, er ist nicht nur ein „Über mich". Titel/H1 und Zwischenüberschriften
  tragen das Schmerz-Thema; die persönliche Geschichte ist die Antwort darauf.
- **Long-Tail (im Text/FAQ):** alles hängt an mir Praxis · Praxis läuft nur mit mir · als
  Inhaberin alles selbst machen · zu viel Verwaltung in der Praxis · Praxis delegieren lernen
- **Sekundär/semantisch:** Flaschenhals Praxis, erst Prozesse dann Tool, KI für kleine
  Gesundheitspraxen
- **Target Intent:** Awareness (Problem-Erkennen + Vertrauen) — Suchvolumen kleiner als bei
  #2/#3, aber vorhanden; #1 ist damit kein toter SEO-Anker.
- **Format/Länge:** persönlicher Beitrag mit Schmerz-Aufhänger, **700–1.000 Wörter**, ~4 min
- **Kategorie (Front-Matter):** „KI in der Praxis"

### Interne Links
- **Hub:** `/ueber-mich/` (primär)
- **Weiter:** eine Praxisseite als Beispiel (`/ki-fuer-physiotherapie-praxen/`),
  `/eu-ai-act/` beim Datenschutz-Satz
- **CTA:** Potenzialanalyse (Calendly)

### Content-Gap / einzigartiger Winkel
Klassische „Über mich"-Texte langweilen und ranken nicht. Der Kniff: Der Post beginnt
beim **Schmerz der Leserin**, nicht beim Lebenslauf. Leonies Vorstellung wird zur Antwort
auf ein Problem, das die Zielgruppe selbst in Worte fasst. Das differenziert von der
anonymen Anbieterstimme der Software-Konkurrenz — hier spricht ein Mensch mit Haltung.

### Outline
**H1: „Ohne mich läuft hier nichts" — warum in kleinen Praxen alles an der Leitung hängt**

*(SEO-Hinweis: H1 und die H2 tragen das Keyword-Thema „alles hängt an der Leitung/Inhaberin".
Frühere Varianten wie „Der Satz, den ich immer wieder höre" sind menschlich schön, aber ohne
Keyword — deshalb bekommt jede H2 einen suchbaren Kern.)*

- **H2: Wenn die Praxis nur mit Ihnen läuft**
  - Einstieg mit dem O-Ton der Zielgruppe; das Gefühl, Behandlung, Führung und Organisation
    zugleich zu stemmen. Leserin erkennt sich wieder.
- **H2: Warum in kleinen Praxen alles an der Leitung hängt**
  - H3: Sie behandeln, führen und organisieren — oft alles zugleich
  - H3: Jedes neue Tool macht es zuerst komplizierter, nicht einfacher
- **H2: Wer ich bin — und warum mich gerade dieses Problem nicht loslässt**
  - Kurz und konkret: 20+ Jahre Berufserfahrung, davon 10+ Jahre in regulierten
    Gesundheits- und Pharmaunternehmen (Merck Healthcare, AbbVie, Baxter) in
    Digitalisierung, Marketing und Projekten — dort den Umgang mit sensiblen Daten und
    komplexen, regulierten Abläufen von innen kennengelernt. Danach mehrere Jahre
    **Selbstständige und Kleinbetriebe begleitet, mit Fokus auf effiziente Systeme und
    tragfähige Abläufe, die operative Überlastung reduzieren** — heute KI & Digitalisierung
    für Praxen. Erfahrung benennen, ohne zu prahlen. *(Ehrlich einordnen: Digitalisierung/
    Marketing/Projekte in regulierten Konzernen, kein klinischer Patientendaten-Bezug —
    Leonie war im Marketing. Pharma als Herkunft der Datenschutz-Sorgfalt, nicht als
    Zielmarkt — siehe Positionierung.)*
- **H2: Wofür ich stehe (und wogegen)**
  - H3: KI nicht um jeden Preis — erst die Prozesse, dann das Werkzeug
  - H3: Datenschutz ist der Ausgangspunkt, nicht das Kleingedruckte
  - H3: Wenn KI nicht die Lösung ist, sage ich Ihnen das
- **H2: Was Sie hier im Blog erwartet**
  - Ausblick auf die Themen (Termine & Abläufe, Datenschutz, Sichtbarkeit). Brücke zu Post #2.
- **CTA:** Potenzialanalyse, gerahmt als „gemeinsam schauen, wo Ihre Praxis Zeit verliert".

### Meta-Description (Entwurf, 140–160)
> Wer steckt hinter dieser KI-Beratung? Warum ich kleinen Gesundheitspraxen helfe, ihren
> Alltag zu entlasten — und wofür ich dabei stehe: erst die Prozesse, dann das Werkzeug.

### Bild-Ideen (du suchst aus, ich mache ALT-Text & Co.)
- **Hero:** Leonie echt und nahbar (Porträt in ruhiger, heller Umgebung) — oder eine
  Praxisleiterin, die kurz durchatmet. Stimmung: ruhig, souverän, warm.
- **Zwischenbild:** ein aufgeräumter Schreibtisch / ein Moment „Zeit für den Menschen"
  (Behandlerin im Gespräch, nicht am Papierkram). Suchbegriffe: „Therapeutin Gespräch",
  „Praxis Empfang ruhig", „Selbstständige Pause Büro".

*(FAQ-Block bei diesem persönlichen Post optional — persönlicher Ton statt How-to.)*

---

## Post #2 — No-Shows in der Physiotherapie-Praxis senken

### Eckdaten
- **Primär-Keyword:** „No-Shows Physiotherapie reduzieren"
- **Sekundär/semantisch:** Terminausfälle Praxis senken, Absagequote reduzieren,
  Terminerinnerung Physiotherapie, verpasste Termine Praxis, Terminorganisation
  automatisieren, DSGVO-konforme Terminerinnerung
- **Target Intent:** Consideration (Problem bekannt, Lösungswege werden verglichen)
- **Segment-Label:** Physiotherapie-Praxis (steht im Titel; Thema gilt für alle Praxen)
- **Format/Länge:** Standard-Fachbeitrag, **1.100–1.400 Wörter**, ~6 min
- **Kategorie:** „Termine & Anfragen"

### Interne Links
- **Hub:** `/ki-fuer-physiotherapie-praxen/` (deckt sich mit `schmerz:` in branchen.yaml)
- **Weiter:** `/eu-ai-act/` (Datenschutz-Abschnitt), später Post #10 (Erinnern vs. Zurückholen)
- **CTA:** Potenzialanalyse, flankiert mit dem Physio-Beispielszenario

### Content-Gap / einzigartiger Winkel
*Sachlich, nicht abwertend (Brand-Voice): wir sagen, was wir zusätzlich bieten — nicht,
dass andere schlecht arbeiten.* Die deutschen Top-Ergebnisse sind überwiegend Terminplaner-
und Praxissoftware-Anbieter. Sie liefern gute Werkzeuge, hören aber naturgemäß dort auf, wo
Leonie weitermacht:
1. **Sie liefern ein Werkzeug** — Leonie ordnet zuerst die Abläufe, dann kommt das Werkzeug
   (tool-agnostisch).
2. **Prozentzahlen zur Wirkung stehen oft ohne Kontext** — Leonie nennt Zahlen nur mit
   Quelle und ordnet sie ehrlich ein.
3. **„DSGVO-konform" bleibt häufig ein Stichwort** — Leonie erklärt Art. 9, AVV und
   EU-Hosting verständlich.
4. **Erinnern und Zurückholen werden oft in einen Topf geworfen** — Leonie trennt beides
   sauber (den gebuchten Termin absichern vs. Kundschaft zurückholen, die länger nicht da war).

### Outline
**H1: No-Shows in der Physiotherapie-Praxis senken: was wirklich hilft**

- **H2: Warum ein ausgefallener Termin in einer Privatpraxis doppelt weh tut**
  - H3: Die Lücke im Kalender kostet Umsatz — und lässt sich nicht nachholen
  - H3: Warum das in einer Selbstzahler-Praxis mehr wiegt als bei vollen Kassenterminen
- **H2: Die vier häufigsten Ursachen für Terminausfälle**
  - H3: Der Termin wird schlicht vergessen
  - H3: Die Erinnerung kommt zu spät — oder gar nicht
  - H3: Absagen und Umbuchen ist zu umständlich
  - H3: Keine Warteliste für kurzfristig frei gewordene Termine
- **H2: Was wirklich hilft — der Reihe nach**
  - H3: Erinnerung im 24–48-Stunden-Fenster (der wirksamste Einzelhebel)
  - H3: Absage mit einem Klick — und eine Warteliste, die die Lücke füllt
    - *So funktioniert es:* In der Erinnerung ist ein Absage-/Umbuchen-Link. Sagt jemand ab,
      wird der Slot frei markiert und automatisch der nächsten passenden Person aus der
      Warteliste angeboten (per SMS/Mail, „Der Termin am … ist frei geworden — möchten Sie?").
      Wer zuerst bestätigt, bekommt ihn. So füllt sich die Lücke ohne Telefon-Pingpong.
  - H3: Ausfallgebühr als Option — wenn, dann sauber vereinbart *(siehe Hinweis unten)*
  - H3: Erst der Ablauf, dann das Werkzeug (warum ein Tool allein selten reicht)
- **H2: Datenschutz: Warum schon der Terminanlass ein Gesundheitsdatum ist**
  - Kurz-Einordnung Art. 9, SMS/WhatsApp-Vorsicht, EU-Hosting/AVV. Verlinkt auf `/eu-ai-act/`.
- **H2: So gehen wir das an — ein Beispielszenario** *(illustrativ gekennzeichnet)*
  - Rohmaterial: `service-katalog.md` **Szenario A (Physiopraxis, Termin-Journey)** +
    Physio-Beispiel in `branchen.yaml`: Online-Buchung → automatische Erinnerung →
    Wartelisten-Nachbesetzung. „Sie richten nichts selbst ein."
- **H2: Häufige Fragen** (FAQ / AI-Overview)
  - Wie viele No-Shows sind normal in einer Physiotherapie-Praxis?
  - Sind automatisierte Terminerinnerungen per SMS oder WhatsApp DSGVO-konform?
  - Darf ich eine Ausfallgebühr verlangen — und wie mache ich das sauber?
  - Brauche ich dafür eine eigene IT?
- **CTA:** Potenzialanalyse + konkretes Physio-Ergebnis.

> **Hinweis Ausfallgebühr (zu deiner Frage):** Ja, das kann man anbieten — als *ergänzenden*
> Hebel, nicht als Kern. Sauberer Ablauf: (1) **vorab vereinbaren** — eine kurze Klausel bei
> der Terminbuchung/im Behandlungsvertrag (z. B. „Absage bitte bis 24 h vorher, sonst € X").
> (2) **Fair gestalten** — nur bei zu später/keiner Absage, mit klarer Frist. (3) **Einheben:**
> entweder Rechnung nachträglich, oder eine hinterlegte Karte/Anzahlung bei der Online-Buchung.
> Wichtig: Der Ton bleibt freundlich — die Gebühr ist Rahmen, nicht Drohung; die eigentliche
> Lösung sind Erinnerung + Warteliste. *(Kein Rechts-Rat — die genaue Klausel gehört zur
> Rechtsberatung; wir liefern den Ablauf, nicht die Vertragsformulierung.)*
>
> **Hinweis zu „Erinnern vs. Zurückholen":** Die Unterscheidung Terminerinnerung ↔
> Wiedereinladung ist bewusst **nicht** hier, sondern Kern von **Post #10** — sonst
> überschneiden sich die beiden Beiträge.

### Meta-Description (Entwurf, 140–160)
> No-Shows kosten Ihre Praxis Umsatz und Nerven. Was gegen Terminausfälle wirklich hilft —
> von der richtigen Erinnerung bis zur Warteliste — und wie Datenschutz mitgedacht wird.

### Bild-Ideen
- **Hero:** freundlicher Praxis-Empfang / ruhiger Terminkalender am Tablet — hell, aufgeräumt.
  Suchbegriffe: „Physiotherapie Praxis Empfang", „Terminkalender Tablet Praxis".
- **Zwischenbild/Grafik:** kleine 3-Schritt-Grafik „Erinnerung → Absage-Link → Warteliste
  füllt den Slot". (Kann ich als einfache Grafik beschreiben, du/das Dev setzt sie um.)

---

## Post #3 — Praxis-Alltag: Welche Daten darf ich in ChatGPT eingeben?

### Eckdaten
- **Primär-Keyword:** „welche Daten darf ich in ChatGPT eingeben"
- **Fokus (wichtig):** Es geht darum, **was Sie überhaupt eintippen sollten/dürfen und wo
  es brenzlig wird** — praktische Orientierung für den Alltag. Dass sensible Patientendaten
  nicht ungeschützt hineingehören, ist klar und wird nur **kurz** eingeordnet, nicht breit
  ausgewalzt.
- **Long-Tail (im Text/FAQ):** Gesundheitsdaten KI Datenschutz · ChatGPT in der Praxis ·
  Datenschutzgesetz KI Praxis · welche Daten KI eingeben · EU-Hosting KI-Tool ·
  Auftragsverarbeitungsvertrag KI
- **Titel-Hinweis:** im Titel bewusst „Datenschutzgesetz" (verständlich für die
  Zielgruppe) statt „DSGVO Art. 9"; die präzise Rechtsgrundlage steht im Text, nicht im Titel.
- **Target Intent:** Consideration (konkrete Sorge, sucht belastbare Antwort)
- **Format/Länge:** Tiefer Leitfaden, **1.500–2.000 Wörter**, ~9 min — ein Ranking-Anker
- **Kategorie:** „Datenschutz & EU AI Act"

### Interne Links
- **Hub:** `/eu-ai-act/` (Autoritäts-Pillar)
- **Weiter:** alle drei Praxisseiten (je nach Datentyp), Post #2 (Terminerinnerung)
- **CTA:** Potenzialanalyse, gerahmt als „datenschutzsichere Einrichtung"

### Content-Gap / einzigartiger Winkel
Zum Thema kursieren viele Vereinfachungen — von „ChatGPT ist verboten" bis „ist doch alles
DSGVO-konform". Was fehlt, ist eine **verständliche, praktische Orientierung**: Welche Daten
kann ich bedenkenlos eintippen, welche besser nicht, und wo wird es heikel? Leonies Winkel:
ruhig und konkret statt alarmierend — sie erklärt, was ein sicheres Setup ausmacht
(EU-Hosting, AVV, keine Trainings-Nutzung, Datenminimierung). **Autoritätsanker früh im
Text:** Leonie kennt regulierte, datensensible Umgebungen aus 10+ Jahren in Gesundheits-
und Pharmaunternehmen. Ruhig statt alarmierend, keine Rechtsberatung — Orientierung mit
klarem Hinweis, wo die Juristin/der DSB gefragt ist.

### Outline
**H1: Welche Daten darf ich in ChatGPT eingeben? Was das Datenschutzgesetz für Ihre Praxis bedeutet**

- **H2: Die kurze Antwort — und warum sie ein „Es kommt darauf an" ist**
  - Klartext gleich oben (LLM-/Snippet-tauglich): nicht pauschal verboten, aber nicht ohne
    sauberes Setup. Was „sauberes Setup" heißt, klärt der Beitrag.
- **H2: Welche Daten können rein — und welche besser nicht** *(der praktische Kern)*
  - H3: Meist unkritisch: allgemeine Texte, Vorlagen, Entwürfe ohne Personenbezug
    (z. B. eine allgemeine Aufklärung formulieren, einen Standardbrief entwerfen)
  - H3: Heikel: alles, was eine **Person + eine Gesundheitsangabe** verbindet (Name +
    Diagnose/Termin­anlass/Befund) — hier wird es schnell zur „besonderen Kategorie"
  - H3: Die einfache Faustregel: **anonymisieren oder weglassen** — die KI braucht den
    echten Namen fast nie
- **H2: Kurz eingeordnet: das Datenschutzgesetz (DSGVO Art. 9)**
  - *Kurz halten, nicht ausufern.* **Was ist „Art. 9 / besondere Kategorien"?** Das sind
    besonders geschützte Daten — u. a. **Gesundheitsdaten**. Für sie gelten strengere
    Regeln als für einen normalen Namen oder eine Adresse. Schon der Anlass eines Termins
    („Rückenschmerzen") kann dazugehören.
- **H2: Was ein sicheres Setup ausmacht**
  - H3: EU-Hosting, wo möglich · H3: AVV (Auftragsverarbeitungsvertrag) mit dem Anbieter
  - H3: Trainings-Nutzung abschalten (damit Eingaben nicht weiterverwendet werden)
  - H3: Datenminimierung — nur so viel wie nötig
- **H2: Muss ich Daten verschlüsseln? (deine Frage)**
  - Ehrlich einordnen: **Der wirksamste Schutz im Alltag ist, sensible Daten gar nicht
    erst hineinzugeben** (anonymisieren/weglassen) plus ein Anbieter mit EU-Hosting + AVV.
    Zusätzliche Verschlüsselung einzelner Eingaben ist im Praxisalltag meist zu aufwändig
    und nicht der richtige Hebel — Datensparsamkeit + sauberes Setup bringen mehr. Für die
    Ablage/Übertragung im Hintergrund sorgt das richtige Werkzeug (Transportverschlüsselung
    ist dort Standard).
- **H2: Wie wir das in der Praxis lösen** *(Beispielszenario, illustrativ)*
  - Werkzeuge, die das von Grund auf richtig aufsetzen (Sprache aus branchen.yaml-FAQ).
- **H2: Häufige Fragen** (FAQ / AI-Overview)
  - Ist der Einsatz von ChatGPT in einer Praxis grundsätzlich problematisch?
  - Welche Daten kann ich unbedenklich eingeben?
  - Was ist ein Auftragsverarbeitungsvertrag und brauche ich den?
  - Muss ich meine Eingaben verschlüsseln?
- **Hinweis-Kasten:** Dieser Beitrag ersetzt keine Rechtsberatung; im Zweifel DSB/Anwalt.
- **CTA:** Potenzialanalyse — „wir richten Werkzeuge ein, die sensible Daten von Anfang an richtig behandeln".

### Meta-Description (Entwurf, 140–160)
> Welche Daten können in ChatGPT und welche besser nicht? Was das Datenschutzgesetz für Ihre
> Praxis bedeutet und woran Sie ein sicheres Setup erkennen — verständlich und praxisnah.

### Bild-Ideen
- **Hero:** ruhiger Schreibtisch mit Laptop, im Hintergrund unscharf eine Praxis — seriös,
  aufgeräumt (kein „Hacker im Dunkeln", kein Alarm-Vibe). Suchbegriffe: „Datenschutz Büro
  Laptop hell", „Praxis Verwaltung Computer".
- **Zwischenbild/Grafik:** einfache Ampel- oder Zwei-Spalten-Grafik „kann rein / besser
  nicht" — praktisch und teilbar.

---

## Posts #4–#10 — folgen nach dem Launch

Gleiche Struktur (Eckdaten · interne Links · Content-Gap · Outline · Meta). Reihenfolge
und Themen siehe Redaktionsplan in `strategie/blog-konzept.md`, Abschnitt 8 — inklusive
der **Wunsch-Themen**, die neben den Schmerz-Themen laufen:
- **Auffindbarkeit / GEO (#5):** „Damit Ihre Praxis online und in KI-Antworten gut gefunden wird."
- **Website-Assistent (#6):** besseres Kundenerlebnis, Anfragen sofort beantwortet.
- **Termine erinnern & Kundschaft zurückholen (#10):** die zwei Nachrichten-Typen sauber getrennt.

Werden **erst nach Freigabe der ersten drei** ausgearbeitet — so ist Tonfall und Tiefe
einmal an #1–#3 justiert, bevor die restlichen entstehen.
