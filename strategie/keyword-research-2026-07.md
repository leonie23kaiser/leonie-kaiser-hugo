# Keyword-Research (Answer-the-Public-Testabo, Juli 2026)

*Ergebnisse aus einer einwöchigen Testabo-Upgrade-Phase eines Keyword-/Content-Tools
(„Answer the Public"-artig, Domain-Abdeckungs-Check + KI-Prompt-Recherche). Stand: 2026-07-29.
Diente der Vorbereitung der Google-Ads-Kampagne und der Blog-Themenplanung. Testabo wird
gekündigt; diese Datei ist die dauerhafte Ablage der Erkenntnisse.*

## Ausgangslage & Ablauf

1. Tool hat aus der Domain (leoniekaiser.com) automatisch 134 Keywords vorgeschlagen,
   verteilt auf 8 Themen-Cluster (Google-Ads-Themen: EU AI Act, DSGVO-Tools, Praxisabläufe,
   Zeitersparnis, Patientenkommunikation, Kosten-Einwand, Einführung ohne Vorwissen, Longevity).
2. **Lücke entdeckt:** Die beiden Physio-spezifischen Themen („KI in der Physiopraxis
   einführen", „Physiopraxis Digitalisierung 2026") hatten trotz Priorität (Tier 1,
   „ideales Aushängeschild" laut `segmente.md`) zunächst **keine** generierten Keywords.
   Manuell nachselektiert (8 Physio-Keywords aus Tool-Vorschlägen).
3. Domain-Keyword-Limit des Tarifs: 100 manuelle Keywords. Die ursprünglichen 134 wurden
   auf 100 gekürzt (Dopplungen und Heilpraktiker-Nische — Tier 3 — rausgenommen).
4. Nach Upload zeigte sich: „100 angefragt · 100 bereits überwacht" bedeutete, dass alle
   100 bereits im Tool bekannt waren (kein echter Zuwachs). Für echten Zuwachs wurden **100
   neue, von Claude gebrainstormte Keywords** ergänzt (Dokumentation/Teamwissen, Nachsorge/
   Recall, Abrechnung, Longevity-Detail, **Ernährungsberatung/Diätologie** [bis dahin komplett
   unbedient, obwohl eines der drei Start-Segmente], Vertrauen/Referenzen, Sichtbarkeit/GEO,
   Persona-O-Töne). Diese sind **nicht** durch echtes Suchvolumen verifiziert, sondern aus
   `AGENTS.md`/`segmente.md`/`service-katalog.md`-Schmerzpunkten abgeleitet.
5. Domain-Abdeckung insgesamt: **234 Keywords getrackt, 0 % vollständig abgedeckt, ~50 %
   teilweise, ~50 % nicht abgedeckt.** Kein Ranking messbar (neue/traffic-arme Domain, erwartbar).

## KI-Prompt-Recherche (GEO) für die ersten 10 priorisierten Keywords

Für 10 ausgewählte Keywords (Conversion-nah, Tier-1-Segmente, EU-AI-Act-Differenzierung,
Persona-Treffer) wurde eine tiefere Einzelrecherche gemacht: je Keyword ~25 KI-Prompt-Varianten
(13 ChatGPT + 12 Gemini) mit Absichts-Klassifizierung (informativ/kommerziell/navigational).

**Befund:** Die Spalten „Sentiment" und „Marken" waren in 21 von 22 geprüften Sheets
**komplett leer** — sowohl für Österreich als auch (stichprobenartig mit 3 Keywords getestet)
für Deutschland. Das ist also kein Österreich-spezifisches Datenmangel-Problem, sondern
eine generelle Grenze dieses Tools/Features. **Konsequenz:** keine weiteren Länder-Tests
nötig, die Prompt-Varianten selbst (der eigentlich nützliche Teil für FAQ-/Content-Struktur)
sind unabhängig vom Land gleich ergiebig.

## Validierter erster Blogartikel-Cluster

Thema **„Die Praxis hängt an der Leitung / entlasten / delegieren"** — alle 6 Keywords
bereits im 234er-Keyword-Pool getrackt, aber **ohne dedizierten Artikel** (aktuell nur über
die generische Seite „Dokumentation & Wissen automatisieren" bzw. „Nachsorge & Kundenbindung"
mit 40–45 % Teil-Abdeckung referenziert):

- Praxis delegieren
- Praxisinhaber überlastet
- alles hängt an mir Praxis
- Praxisorganisation verbessern
- Praxisleitung entlasten
- Aufgaben abgeben Praxis

Passt zum homogenen Kern-Schmerz Nr. 4 aus `segmente.md` („Alles hängt an der Leitung —
Behandlung, Führung und Verwaltung in einer Person") und zum O-Ton „Ohne mich läuft hier
nichts — das ist kein Betrieb, das bin ich." Guter, validierter Kandidat für den ersten
dedizierten Blogartikel dieser Themenrunde.

**Update 2026-07-30 — wichtige Korrektur:** Die 6 Phrasen oben zeigten in Google Trends
(12 Monate, DE) durchgehend **0** und im Google Keyword Planner **kein Volumen / „Competition:
Unknown"**. Das sind Themen-Labels des SEO-Tools, keine echten Suchanfragen — niemand tippt
„Praxisorganisation verbessern" exakt so. Das Thema dahinter bleibt aber valide (siehe unten).

## Runde 2: Reale Trends-/Planner-/Google-direkt-Daten für breitere Kopf-Begriffe (2026-07-30)

*Nachdem die 6 Seed-Phrasen oben als Nullvolumen entlarvt wurden, wurden breitere,
realistischere Kopf-Begriffe getestet — sowohl für Blogpost #1 als auch site-weit für die
Kampagne. Wichtigster Befund: **hohes Suchvolumen heißt nicht automatisch richtige
Zielgruppe** — bei mehreren Begriffen weicht die tatsächliche Suchintention (laut Google
Ähnliche-Fragen/Ähnliche-Suchanfragen) stark von Leonies Zielgruppe ab.*

| Begriff | Trends-Signal (DE, 12 Mon.) | Reale Suchintention laut Google-direkt | Passt zur Zielgruppe? |
|---|---|---|---|
| **praxismanagerin** | stark, konstant übers Jahr, Peak 100 | Gehalt, Stellenangebote, Ausbildung, IHK, Studium | **Nein** — Jobsuchende/Ausbildungsinteressierte, nicht Praxisinhaberinnen |
| **praxismanagement** | solide, konstant | Weiterbildung, Gehalt, Studium, Quereinstieg (nur „Physiotherapie"-Variante trifft) | **Teilweise** — überwiegend Ausbildungs-/Karriere-Intent |
| **eu ai act** | klar steigend, Spike Ende Juni/Anfang Juli 2026 (100/91) | Zusammenfassung, PDF, Umsetzung Deutschland, Risikoklassen, „is it mandatory" | **Ja** — passender Informations-Intent, allerdings großes/kompetitives Themenfeld (IBM, Deloitte tauchen mit auf) |
| **ki beratung** | niedrig, leicht steigend | Mittelstand, Handwerk, für Unternehmen, Jobs, Deloitte | **Teilweise** — reale B2B-KI-Beratungs-Nachfrage, aber generisch/stark umkämpft, nicht gesundheitsspezifisch |
| **dsgvo ki** | niedrig, aber real | Welches KI-Tool ist DSGVO-konform, Ist ChatGPT DSGVO-konform, KI und Datenschutz | **Ja** — trifft ihre Differenzierung fast direkt |
| **praxissoftware** | niedrig, real | Vergleich, Tomedo, Medatixx, MEDISTAR, Zahnarzt, Hausarzt (Software-**Produkt**-Vergleiche) | **Nein** — Leute suchen Praxisverwaltungs-Software zum Kaufen, nicht KI-Beratung; würde außerdem gegen die „tool-agnostisch"-Positionierung aus `AGENTS.md` laufen |
| **potenzialanalyse** (allein) | niedrig | Schule, 8. Klasse, Arbeitsagentur, Fragebogen PDF, Mitarbeiter-Test | **Nein** — der Begriff ist im Deutschen von Schul-/Personalauswahl-Assessments besetzt; **„KI-Potenzialanalyse" als zusammengesetzter Begriff verwenden**, nie „Potenzialanalyse" allein |
| dsgvo (generisch, zum Vergleich) | riesig, dominant | — | zu breit, nur als Kontext-Baseline |

**Konsequenz für Blogpost #1 und generell:** Begriffe mit Suchvolumen nicht blind übernehmen —
immer die „Weitere Fragen" / „Wird auch oft gesucht"-Liste aus Google direkt gegenprüfen, ob
die Suchintention zu **inhabergeführten Gesundheits-/Wellness-Praxen** passt (nicht zu
Jobsuchenden, Softwarekäufer:innen oder Schul-Assessments). Für Blogpost #1 bleibt der
inhaltliche Kern („Alles hängt an der Leitung", Delegieren, Entlasten) richtig — nur eben
nicht unter den Kopf-Begriffen „Praxismanagerin"/„Praxismanagement" bewerben, da deren
Publikum überwiegend ein anderes ist. **EU AI Act** ist der stärkste, zielgruppengerechte
Befund dieser Runde und verdient Priorität — der Spike Ende Juni/Anfang Juli 2026 sollte bei
Gelegenheit auf einen echten Auslöser (Frist, Nachrichtenereignis) geprüft werden.

## Offene Content-Lücken (Stand 2026-07-29)

- Physio: jetzt gut bedient (eigene Themen-Cluster + Keywords vorhanden).
- Longevity: dünner bedient als Physio, sollte nachgezogen werden.
- **Ernährungsberatung/Diätologie: nach wie vor kein einziges dediziertes Content-Stück**,
  nur die 10 von Claude gebrainstormten Keywords (Gruppe 6, unten) als Ausgangspunkt.

## Anhang A: Die 100 final getrackten Keywords (nach Kürzung von 134)

```
datenschutz ki gesundheit · zeitersparnis digitalisierung praxis · patientenkommunikation
automatisieren · praxisdigitalisierung 2026 · ki-automatisierung praxis · digitalisierung
praxis investition · praxisabläufe automatisieren · automatische terminerinnerung praxis ·
digitalisierung physiopraxis schritt für schritt fahrplan 2026 · praxis ki-prozesse
optimieren · digitalisierung für nicht-techniker · terminverwaltung automatisieren praxis ·
wie sollte ich meine physiopraxis bis 2026 digital aufstellen · digitale transformation
physiotherapie österreich 2026 · welche ki-tools eignen sich speziell für
physiotherapiepraxen · einfache ki tools praxis · ki in der physiotherapiepraxis schritt für
schritt einführen · ki ohne vorkenntnisse praxis · physiopraxis ki · ki beratung praxis
kosten · ki tools für physiotherapeuten dach · longevity praxis österreich · dsgvo ki tools
praxis · no-code tools praxis · eu ai act praxis · kleine privatpraxen digitalisierung ·
nachsorge automatisieren · dokumentation automatisieren · welche tools eignen sich zur
automatisierten kommunikation mit patienten in kleinen praxen · datenschutzkonforme
automatisierung sensibler patientendaten · praxisdigitalisierung nutzen für
einzelunternehmer gesundheit · ki chatbot für patientenanfragen in gesundheitspraxen ·
praxis digitalisierung roi · eu ai act pflichten für kleine gesundheitspraxen verständlich
erklärt · wie viel zeit spare ich wirklich durch die digitalisierung meiner praxis · praxis
digitalisierung kosten · wie viel zeit spare ich durch digitalisierung meiner privatpraxis ·
automatisierung gesundheitsbereich · online-terminbuchung praxis · wann lohnt sich ein ki
consultant für eine gesundheitspraxis · kundenbindung praxis · digitalisierung privatpraxis ·
patientenkommunikation in der praxis dsgvo konform automatisieren · physiopraxis
digitalisierung trends und pflichten 2026 · künstliche intelligenz physiotherapie
praxisalltag · lohnt sich eine ki-beratung für eine kleine praxis mit begrenztem budget ·
physiopraxis digitalisierung · ai act risikoklassen für praxen im gesundheitsbereich ·
kommunikation mit klienten automatisieren physiotherapie osteopathie · ki beratung für
kleine privatpraxen kosten und nutzen im vergleich · auftragsverarbeitungsvertrag ki tools
gesundheitspraxis · was kostet die einführung von ki in einer kleinen gesundheitspraxis
realistisch · ki für gesundheitspraxen · welche digitalisierungsschritte sind für
physiotherapiepraxen bis 2026 besonders wichtig · bewertungsanfragen automatisieren · eu
hosting lösungen für gesundheitsdaten in der praxis · administrative aufgaben in der praxis
mit ki automatisieren · praxis-handbuch digital · praxiseffizienz steigern durch smarte
automatisierung · zeitaufwand praxisverwaltung reduzieren mit ki tools · welche ki-tools
sind dsgvo-konform für gesundheitspraxen mit sensiblen patientendaten · eu ai act umsetzung
privatpraxis österreich deutschland · wie führe ich ki in meiner physiotherapiepraxis ein
ohne it-kenntnisse · ki beratung fixpreise für praxen ohne it abteilung · physiopraxis
prozesse automatisieren · mehr patienten betreuen ohne mehr arbeitszeit investieren ·
gesundheitspraxis österreich · kann ich ki in meiner praxis nutzen wenn ich keine
technik-erfahrung habe · praxisprozesse ohne programmierkenntnisse automatisieren · wie
starte ich als praxisinhaberin mit ki wenn ich nicht technikaffin bin · ki-strategie
gesundheit · papierkram reduzieren praxis · erste ki tools für praxen die keine
technik-erfahrung haben · wie stelle ich sicher dass ki-software in meiner praxis
dsgvo-konform ist · zeitersparnis praxis · physiotherapie zukunft digital · physiotherapie
digitalisieren · ki-assistent erstanfragen · digitalisierung dach-raum · ki-strategie praxis
· ki potenzialanalyse praxis kostenlos dach · warteliste automatisieren · ki physiotherapie
praxis · praxis ki starten · potenzialanalyse praxis · ki für einsteiger praxis · ki
einführung physiopraxis · ki in der praxis einführen ohne technisches vorwissen schritt für
schritt · praxisleitung entlasten · physiopraxis 2026 · ki-einsatz dokumentation ·
praxisinhaber überlastet · ki beratung gesundheit · alles hängt an mir praxis · ki
einführung praxis kosten erfahrungen dach · patientenkommunikation ki · longevity praxis
digital · no-shows reduzieren · ki physiotherapie · dsgvo artikel 9
```

## Anhang B: Die 100 neuen, von Claude gebrainstormten Keywords (unvalidiert)

*Abgeleitet aus `AGENTS.md`-O-Tönen, `segmente.md`-Segmenten und `service-katalog.md`-
Leistungen. Kein echtes Suchvolumen geprüft — vor Einsatz in Ads/Content gegen echte Daten
validieren (Keyword Planner o. Ä.).*

**Dokumentation & Teamwissen:** praxiswissen sichern team · vertretung praxis erleichtern ·
einarbeitung neue mitarbeiterin praxis · praxis handbuch vorlagen erstellen · wissen im kopf
einer person praxis risiko · behandlungsdokumentation ki unterstützung · berichte an
zuweisende ärzte automatisieren · vorlagen bibliothek praxis erstellen · ki protokoll
behandlungsnotizen · praxiswissen zentral ablegen

**Nachsorge, Recall, Bewertungen:** recall sequenz praxis einrichten · ehemalige patienten
reaktivieren praxis · bewertungsanfrage nach termin automatisch · empfehlungsmarketing praxis
automatisieren · patientenbindung nach behandlung verbessern · follow-up nach erstberatung
automatisieren · mitgliedschaft erinnerung praxis automatisch · kundenbindung ohne
mehraufwand praxis · nachsorge fällt hinten runter lösung · stammkundschaft praxis halten ki

**Termine, Warteliste, Erstanfragen:** warteliste automatisch nachbesetzen praxis ·
chat-assistent erstanfragen praxis website · telefonassistent praxis außerhalb
öffnungszeiten · selbstbuchungslink praxis einrichten · terminausfälle reduzieren praxis ·
rezeption entlasten telefon praxis · faq automatisiert beantworten praxis · anfragen per
whatsapp automatisieren praxis · terminlücken automatisch füllen · erstanfrage ohne
medizinische auskunft automatisieren

**Abrechnung & Verwaltung:** kassenabrechnung automatisieren praxis · abrechnung praxis zeit
sparen · verwaltungsaufgaben delegieren ohne personal · rechnungsstellung praxis
automatisieren · buchhaltung entlastung praxis ki · monatsabschluss praxis übersicht schaffen
· praxis profitabilität überblick behalten · verwaltungschaos praxis lösen · doppelte
dateneingabe praxis vermeiden · praxissoftware schnittstellen verbinden

**Longevity / privatärztliche Gesundheitszentren:** membership verwaltung longevity praxis ·
iv-therapie abrechnung automatisieren · executive health praxis digitalisierung · longevity
zentrum patientenkommunikation · präventionsmedizin praxis ki einsatz · hormontherapie praxis
verwaltung digital · longevity praxis wien · check-up praxis terminorganisation · longevity
zentrum dsgvo · privatärztliches gesundheitszentrum automatisierung

**Ernährungsberatung/Diätologie:** ernährungsberatung praxis digitalisierung ·
beratungsprotokoll ernährungsberatung ki · wochenpläne automatisiert erstellen
ernährungsberatung · diätologie praxis verwaltung · rezeptvorschläge vorlage
ernährungsberatung · ernährungsberatung nachsorge automatisieren · diätologin praxis ki
einführen · ernährungsdaten dsgvo art 9 · ernährungsberatung terminverwaltung · diätologie
praxis österreich digitalisierung

**Vertrauen, Referenzen, Ablauf:** referenzen ki beratung gesundheitspraxis · erfahrungen ki
potenzialanalyse praxis · case study ki automatisierung physiopraxis · vertrauenswürdige ki
beratung gesundheit · persönliche betreuung ki einführung praxis · transparente preise ki
beratung praxis · feste ansprechpartnerin datenschutz praxis · ki beratung ohne
verkaufsdruck praxis · ki potenzialanalyse ablauf praxis · was passiert bei der
potenzialanalyse

**Regional AT** *(niedrigste Priorität, vermutlich geringes Volumen):* ki beratung
niederösterreich praxis · ki digitalisierung praxis wien · gesundheitspraxis salzburg ki · ki
beratung praxis tirol · digitalisierung praxis oberösterreich · ki consultant für praxen in
österreich · praxis automatisierung burgenland · gesundheitspraxis kärnten digital · ki
beratung praxis steiermark · praxisdigitalisierung vorarlberg

**Sichtbarkeit/GEO:** praxis von ki assistenten gefunden werden · geo optimierung
gesundheitspraxis · praxis sichtbarkeit ki suche · content vorlagen praxis social media ·
newsletter vorlage praxis erstellen · praxis in chatgpt gefunden werden · praxis website
ki-suchmaschinen · praxis social media ki entwürfe · praxis auffindbarkeit ki assistenten ·
praxis inhalte klingen wie ich ki

**Persona-O-Töne:** ohne mich läuft nichts praxis lösung · fünf tools die nicht miteinander
reden praxis · mitarbeiterin geht wissen weg praxis · wir arbeiten wie vor zehn jahren praxis
· wissen wo anfangen ki praxis · ki ausprobiert aber nichts halbes praxis · profitabilität am
monatsende praxis unklar · zeit mit terminkoordination statt patienten · therapeutin keine
buchhalterin praxis · rezeptionistin krank praxis fällt aus

## Anhang C: GEO-Prompt-Recherche — Rohdaten je Keyword (AT, 10 Keywords getestet)

| Keyword | ChatGPT-Prompts | Gemini-Prompts | Sekundäre Absicht erkannt |
|---|:--:|:--:|:--:|
| welche ki tools sind dsgvo konform für praxen mit gesundheitsdaten | 13 | 12 | 8 / 2 |
| wie führe ich ki in meiner physiotherapiepraxis ein ohne it-kenntnisse | 13 | 12 | 8 / 5 |
| lohnt sich eine ki beratung für eine kleine physiotherapiepraxis | 13 | 12 | 7 / 8 |
| wie viel zeit spare ich als physiotherapeutin durch digitalisierung | 13 | 12 | 9 / 1 |
| welche ki tools eignen sich für eine kleine physiotherapiepraxis in österreich | 13 | 12 | 11 / 12 |
| was kostet ki beratung für eine gesundheitspraxis und wann amortisiert sie sich | 13 | 12 | 7 / 6 |
| kann ich ki in meiner praxis einführen wenn ich keine ahnung von technik habe | 13 | 12 | 11 / 8 |
| welche digitalisierungsschritte sollte eine physiotherapiepraxis 2026 umsetzen | 13 | 12 | 10 / 6 |
| welche pflichten hat eine gesundheitspraxis laut eu ai act | 13 | 12 | 8 / 2 |
| was bedeutet der eu ai act für meine physiotherapiepraxis in österreich | 13 | 12 | 9 / 7 |

Sentiment- und Marken-Spalten waren in 21 von 22 Sheets leer (auch nach DE-Stichprobe mit 3
Keywords) — generelle Tool-Grenze, kein AT-spezifisches Datenproblem.

---

*Quelle: Chat-Session 2026-07-29 (Google-Ads-Kampagne + Keyword-Research). Bezug:
`segmente.md`, `service-katalog.md`, `angebotsvorschlaege.md`, `AGENTS.md`.*
