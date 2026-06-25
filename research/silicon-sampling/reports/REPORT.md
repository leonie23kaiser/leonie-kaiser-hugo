# Silicon-Sampling-Studie — Auswertung

**Zielgruppe:** Kleine Gesundheits- & Wellness-Betriebe mit Team (2–10 Personen) im DACH-Raum — Inhaber:innen/Leitung von Physio-/Therapiepraxen, Ernährungs-/Gesundheitszentren, Personal-Training-Studios, Präventions-/BGF-Anbietern und Premium-Wellness-/Longevity-Praxen.

> ⚠️ **SYNTHETISCHE DATEN — ESOMAR ICC Code 2025.** Diese Ergebnisse stammen aus *Silicon Sampling*: KI-Personas wurden befragt, keine echten Menschen. Die Befunde sind **Hypothesen, keine validierten Fakten**, und müssen vor strategischen Entscheidungen durch echte Interviews (10–20) validiert werden. Bekannte Grenzen: gesprochene Präferenz statt echtem Verhalten, mögliche Homogenisierung von Mehrheitsmeinungen, kein Ersatz für reale Marktforschung.

## Methodik (reproduzierbar)

- **Modell:** `claude-sonnet-4-6`
- **Personas:** 99 vollständig befragt (von 220 geplant — Lauf endete, als das API-Guthaben aufgebraucht war; via Checkpoint jederzeit fortsetzbar), deterministisch geseedet (Seed `20260625`).
- ⚠️ **Stichprobengröße:** n=99 liegt **über** der Schwelle für qualitative Insights (≥20), aber **unter** der Workbook-Empfehlung von ≥200 für belastbare *quantitative* Auswertung. Zahlen (Buchungs-Ø, Van-Westendorp) daher als **richtungsweisend**, nicht als präzise lesen; die qualitativen O-Töne sind bereits tragfähig. Aufstocken auf ≥200 jederzeit möglich (Guthaben laden, `run_study.py` erneut starten).
- **Prompt-Version:** `2026-06-25.v1`
- **Befragung:** 3-Phasen-Multi-Turn, blind. Phase 1 (offen) **vor** jeder Konzept-Nennung; keine Leading-Fragen; Personas ausdrücklich zu Kritik/Ablehnung ermutigt.
- **Persona-Generierung & Prompts:** vollständig im Repo (`personas.py`, `prompts.py`).
- **Unabhängigkeit:** Es wurden bewusst keine Pain Points/Wünsche/Formulierungen vorgegeben — alle Inhalte stammen aus den Personas selbst.

### Stichprobenstruktur

**Branche:** Physiotherapie-/Therapiepraxis (21) · Ernährungs-/Gesundheitszentrum (20) · Personal-Training-Studio (20) · Präventions-/BGF-Anbieter (19) · Wellness-/Longevity-Praxis (Premium) (19)

**Land:** CH (37) · DE (33) · AT (29)

**Haltung:** neugierig-offen (21) · skeptisch (20) · pragmatisch-abwägend (17) · überfordert / zu wenig Zeit (14) · desinteressiert / sieht keinen Bedarf (12) · früher Anwender / probiert gern Neues (10) · stark skeptisch (5)

## 1. Häufigste Pain Points (gruppiert & nach Häufigkeit)

*Häufigkeit = Zahl der Personas (von 99), die diesen Themenbereich in Phase 1 von sich aus nannten.*

### Verwaltung, Bürokratie & Abrechnung — 82 Personas (83%)
`████████████████████····`

**O-Töne:**
- „Administrative Kleinteiligkeit durch unterschiedliche Krankenkassen-Logiken und -Formulare"  
  <sub>— P104, Präventions-/BGF-Anbieter</sub>
- „Abrechnung mit Krankenkassen und Heilmittelverordnungen bindet zu viele manuelle Schritte"  
  <sub>— P006, Physiotherapie-/Therapiepraxis</sub>
- „Kundenanfragen (Abrechnung, Abo-Pausen, Termine) landen direkt bei Birgit statt beim Team"  
  <sub>— P178, Personal-Training-Studio</sub>
- „Rechnungswesen und Leistungserfassung landen immer wieder bei mir statt delegiert zu sein"  
  <sub>— P195, Wellness-/Longevity-Praxis (Premium)</sub>
- „Buchhaltungsvorbereitung passt nie zum komplexen Angebotsstruktur, bleibt manuell hängen"  
  <sub>— P037, Ernährungs-/Gesundheitszentrum</sub>

### Personal: Finden, Halten, Führen — 78 Personas (79%)
`███████████████████·····`

**O-Töne:**
- „Ewiges Koordinieren von Dienstplänen, Urlauben und Klientenpräferenzen mit Papier und Excel"  
  <sub>— P056, Physiotherapie-/Therapiepraxis</sub>
- „Perfektionismus kombiniert mit fehlenden Prozessen führt dazu, Aufgaben nicht loszulassen"  
  <sub>— P124, Präventions-/BGF-Anbieter</sub>
- „Wöchentliche Dienstplanung mit komplexen Variablen (Urlaub, Krankenstand, Kassenverträge)"  
  <sub>— P061, Physiotherapie-/Therapiepraxis</sub>
- „Systeme werden eingeführt aber nicht eingehalten, muss ständig nachhalten oder selbst machen"  
  <sub>— P006, Physiotherapie-/Therapiepraxis</sub>
- „Doppelrolle Behandlung und Führung zerfetzt den Tag – keine ruhige Zeit für Führungsaufgaben"  
  <sub>— P056, Physiotherapie-/Therapiepraxis</sub>

### Terminorganisation & No-Shows — 66 Personas (67%)
`████████████████········`

**O-Töne:**
- „Papierkalender und WhatsApp statt einheitlichem System führen zu Doppelbuchungen und Chaos"  
  <sub>— P085, Wellness-/Longevity-Praxis (Premium)</sub>
- „Terminkoordination täglich aufwändig und fehleranfällig durch fehlende gemeinsame Übersicht"  
  <sub>— P080, Wellness-/Longevity-Praxis (Premium)</sub>
- „Unübersichtlichkeit durch Papierkalender und Excel-Listen, Terminpannen die peinlich sind"  
  <sub>— P203, Personal-Training-Studio</sub>
- „Mehrschrittige Terminkommunikation (Anruf, Zettel, Rückruf) statt automatisierter Buchung"  
  <sub>— P027, Ernährungs-/Gesundheitszentrum</sub>
- „Keine feste Assistenz: Terminkoordination und Organisationsaufgaben fallen unstrukturiert an"  
  <sub>— P034, Präventions-/BGF-Anbieter</sub>

### Kommunikation mit Klient:innen — 57 Personas (58%)
`██████████████··········`

**O-Töne:**
- „Interne Kommunikation chaotisch, läuft über WhatsApp und Zettel, kein strukturierter Kanal"  
  <sub>— P130, Wellness-/Longevity-Praxis (Premium)</sub>
- „Teamkommunikation funktioniert nicht – alles landet undifferenziert in einer WhatsApp-Gruppe"  
  <sub>— P085, Wellness-/Longevity-Praxis (Premium)</sub>
- „Fragmentierte interne Kommunikation über mehrere Kanäle (Software, WhatsApp, E-Mail, Zettel)"  
  <sub>— P001, Physiotherapie-/Therapiepraxis</sub>
- „Interne Kommunikation chaotisch – verschiedene Kanäle, Informationen kommen nicht überall an"  
  <sub>— P127, Ernährungs-/Gesundheitszentrum</sub>
- „Interne Kommunikation über verschiedene Kanäle (WhatsApp, E-Mail, Zettel) – kein roter Faden"  
  <sub>— P198, Personal-Training-Studio</sub>

### Digitalisierung & Tools (Frust/Lücken) — 46 Personas (46%)
`███████████·············`

**O-Töne:**
- „Praxissoftware vorhanden aber nicht vernetzt/genutzt, vieles läuft über WhatsApp und Zettel"  
  <sub>— P013, Personal-Training-Studio</sub>
- „Zu viel manuelle Koordination trotz kleinem Team – Leiterin als menschliche Schnittstelle"  
  <sub>— P104, Präventions-/BGF-Anbieter</sub>
- „Manuelle Verwaltung von Abo-Mutationen (Pause, Kündigung, Wechsel) ohne Systemunterstützung"  
  <sub>— P173, Personal-Training-Studio</sub>
- „Fehlende oder instabile Automatisierungen/Schnittstellenprobleme trotz Technikaffinität"  
  <sub>— P172, Ernährungs-/Gesundheitszentrum</sub>
- „Manuelle Terminverwaltung per Telefon und Zettel – besonders bei Krankheitsausfällen aufwändig"  
  <sub>— P056, Physiotherapie-/Therapiepraxis</sub>

### Wissen, Prozesse & Ablage im Team — 43 Personas (43%)
`██████████··············`

**O-Töne:**
- „Kleinigkeiten und Entscheidungen eskalieren zu mir, weil Prozesse nicht dokumentiert sind"  
  <sub>— P172, Ernährungs-/Gesundheitszentrum</sub>
- „Zu viel Administration läuft über mich, weil klare Systeme und dokumentierte Abläufe fehlen"  
  <sub>— P199, Präventions-/BGF-Anbieter</sub>
- „Onboarding neuer Mitarbeitender – Wissen steckt nicht in Dokumenten, sondern in meinem Kopf"  
  <sub>— P151, Physiotherapie-/Therapiepraxis</sub>
- „Fehlende verlässliche Abläufe trotz dokumentierter Prozesse – niemand liest die Dokumentation"  
  <sub>— P126, Physiotherapie-/Therapiepraxis</sub>
- „Prozesse und Standards müssen immer wieder neu erklärt werden – hängt zu sehr an meiner Person"  
  <sub>— P195, Wellness-/Longevity-Praxis (Premium)</sub>

### Alles hängt an mir / nicht delegieren können — 42 Personas (42%)
`██████████··············`

**O-Töne:**
- „Lande regelmässig bei Aufgaben, die delegierbar wären, aber Teamgrösse lässt das nicht zu"  
  <sub>— P100, Wellness-/Longevity-Praxis (Premium)</sub>
- „Zu viel läuft über mich als Leitung – bin selbst der Engpass, übergebe Verantwortung schwer"  
  <sub>— P174, Präventions-/BGF-Anbieter</sub>
- „Lange, ineffiziente Angebotsphase bei neuen Firmenkunden mit viel Nachfassen und Anpassen"  
  <sub>— P034, Präventions-/BGF-Anbieter</sub>
- „Operative Wochenplanung und Abwesenheitsmanagement ohne festes System läuft immer über mich"  
  <sub>— P083, Personal-Training-Studio</sub>
- „Nachlaufen bei liegengebliebenen Aufgaben, Dinge selber erledigen weil es schneller geht"  
  <sub>— P001, Physiotherapie-/Therapiepraxis</sub>

### Zeitmangel, Unterbrechungen & Überlastung — 22 Personas (22%)
`█████···················`

**O-Töne:**
- „Sitzt abends spät noch vor dem Laptop wegen mangelnder Delegation durch fehlende Strukturen"  
  <sub>— P124, Präventions-/BGF-Anbieter</sub>
- „Keine Zeit, strukturelle Verbesserungen wirklich umzusetzen, weil immer etwas dazwischenkommt"  
  <sub>— P007, Ernährungs-/Gesundheitszentrum</sub>
- „Zerstückelung des Alltags – Planung wird ständig durch Unvorhergesehenes unterbrochen"  
  <sub>— P009, Präventions-/BGF-Anbieter</sub>
- „Reibung zwischen eigenen Qualitätsvorstellungen und tatsächlicher Umsetzung im Alltag"  
  <sub>— P180, Wellness-/Longevity-Praxis (Premium)</sub>
- „Neue Ideen und Konzepte kommen nicht zur Umsetzung, weil Tagesgeschäft alles frisst"  
  <sub>— P005, Wellness-/Longevity-Praxis (Premium)</sub>

### Neue Klient:innen aufnehmen / Onboarding — 17 Personas (17%)
`████····················`

**O-Töne:**
- „Manuelles Neukunden-Onboarding kostet pro Person 1,5–2 Stunden ohne standardisierten Prozess"  
  <sub>— P083, Personal-Training-Studio</sub>
- „Onboarding neuer Trainer ohne verschriftlichten Prozess – immer wieder dieselben Erklärungen"  
  <sub>— P178, Personal-Training-Studio</sub>
- „Unstrukturierter Neukunden-Erstkontakt über verschiedene Kanäle ohne Nachverfolgung"  
  <sub>— P078, Personal-Training-Studio</sub>
- „Onboarding neuer Klientinnen noch zu viel Handarbeit, Halbautomatisierung nach Softwarewechsel kaputt"  
  <sub>— P150, Wellness-/Longevity-Praxis (Premium)</sub>
- „Kein strukturiertes Onboarding, Einarbeitung läuft uneinheitlich und nebenbei"  
  <sub>— P171, Physiotherapie-/Therapiepraxis</sub>

### Telefon & Erreichbarkeit — 12 Personas (12%)
`███·····················`

**O-Töne:**
- „Anrufbeantworter wird von Patienten kaum genutzt, trotzdem muss jemand abhören und zurückrufen"  
  <sub>— P011, Physiotherapie-/Therapiepraxis</sub>
- „Einzelnes Anrufen aller betroffenen Klienten bei Ausfall einer Kollegin kostet Stunden"  
  <sub>— P056, Physiotherapie-/Therapiepraxis</sub>
- „Klienten kontaktieren über mehrere Kanäle (Handy, Mail, Telefon), alles landet manuell beim Team"  
  <sub>— P125, Wellness-/Longevity-Praxis (Premium)</sub>
- „Zeitaufwändige manuelle Kommunikation (Telefon, Mail, Anrufbeantworter, Rückrufe)"  
  <sub>— P196, Physiotherapie-/Therapiepraxis</sub>
- „Urlaubsplanung und Einsatzplanung über Excel und Telefon, besonders bei Ausfällen"  
  <sub>— P009, Präventions-/BGF-Anbieter</sub>

### Marketing, Sichtbarkeit & Neukundengewinnung — 5 Personas (5%)
`█·······················`

**O-Töne:**
- „Angebote schreiben ohne Vorlagen – jedes Mal von null, halber Tag für ein Angebot"  
  <sub>— P124, Präventions-/BGF-Anbieter</sub>
- „Marketing und Social Media läuft abends nach 21 Uhr nebenbei – nicht nachhaltig"  
  <sub>— P033, Personal-Training-Studio</sub>
- „Langes, unübersichtliches Hin-und-Her bei Offerten und Auftragsgewinnung"  
  <sub>— P099, Präventions-/BGF-Anbieter</sub>
- „Konkurrenten mit weniger Substanz dominieren sichtbarer den Markt"  
  <sub>— P035, Wellness-/Longevity-Praxis (Premium)</sub>
- „Zu wenig Zeit um bekannte Probleme selbst zu lösen"  
  <sub>— P061, Physiotherapie-/Therapiepraxis</sub>

### Zukunfts- & Existenzsorgen — 3 Personas (3%)
`█·······················`

**O-Töne:**
- „Abhängigkeit des Betriebs von meiner eigenen Person strukturell nicht gelöst"  
  <sub>— P200, Wellness-/Longevity-Praxis (Premium)</sub>
- „Fühlt sich nach 12 Jahren noch zu abhängig von ihrer eigenen Präsenz"  
  <sub>— P201, Physiotherapie-/Therapiepraxis</sub>
- „Abhängigkeit von einzelnen Schlüsselpersonen"  
  <sub>— P055, Wellness-/Longevity-Praxis (Premium)</sub>

### Finanzen, Liquidität & Wachstumsdruck — 1 Personas (1%)
`························`

**O-Töne:**
- „Interner Flickenteppich trotz gutem Außenauftritt und solidem Umsatz"  
  <sub>— P085, Wellness-/Longevity-Praxis (Premium)</sub>

## 2. Wünsche „per Zauberei" (gruppiert)

### Verwaltung, Bürokratie & Abrechnung — 31 Personas
- „Team arbeitet konsequent und eigenverantwortlich nach gemeinsam definierten Abläufen – ohne dass ich ständig nachsteuern muss"  
  <sub>— P202, Ernährungs-/Gesundheitszentrum</sub>
- „Ein vollständig integriertes System für Buchung, Dokumentation, Abrechnung und Dienstplanung – ohne aufwendiges Implementierungsprojekt"  
  <sub>— P061, Physiotherapie-/Therapiepraxis</sub>
- „Ein durchgängig vernetztes digitales System von Terminbuchung über Dokumentation bis Abrechnung – keine Insellösungen mehr, alles in einem"  
  <sub>— P171, Physiotherapie-/Therapiepraxis</sub>
- „Alle administrativen Abläufe (Termine, Abrechnung, Kommunikation, Klientendaten) in einem einzigen, einfach nutzbaren System zusammenführen"  
  <sub>— P007, Ernährungs-/Gesundheitszentrum</sub>

### Terminorganisation & No-Shows — 28 Personas
- „Vollständig automatisierter Erstkundenprozess – von Anfrage bis gebuchtem Termin ohne manuelle Eingriffe"  
  <sub>— P052, Ernährungs-/Gesundheitszentrum</sub>
- „Vollautomatische Terminverwaltung mit Warteliste, Absagen und Bestätigungen – ohne manuellen Aufwand im Team"  
  <sub>— P181, Physiotherapie-/Therapiepraxis</sub>
- „Alle im Team haben zur selben Zeit dieselbe Information – einheitliche, sofort sichtbare Terminverwaltung für alle"  
  <sub>— P032, Ernährungs-/Gesundheitszentrum</sub>
- „Vollautomatischer Ablauf für Terminbuchung, Erinnerungen, Rechnungsstellung und Klientenkommunikation – ohne manuellen Eingriff"  
  <sub>— P027, Ernährungs-/Gesundheitszentrum</sub>

### Wissen, Prozesse & Ablage im Team — 17 Personas
- „Funktionierende, einheitliche und wirklich gelebte Prozesse – die ohne meine ständige Anwesenheit laufen"  
  <sub>— P147, Ernährungs-/Gesundheitszentrum</sub>
- „Ein einfaches, wirklich genutztes System für Projektübersicht und Teamaufgaben – ohne dass ich es ständig pushen muss"  
  <sub>— P084, Präventions-/BGF-Anbieter</sub>
- „Implizites Wissen aus meinem Kopf sauber dokumentiert und im Team verankert – damit die Praxis nicht von meiner Anwesenheit abhängt"  
  <sub>— P036, Physiotherapie-/Therapiepraxis</sub>
- „Klare, dokumentierte und gelebte Prozesse für alle Alltagssituationen, damit ich nicht mehr alles selbst steuern und entscheiden muss"  
  <sub>— P058, Personal-Training-Studio</sub>

### Personal: Finden, Halten, Führen — 16 Personas
- „Prozesse werden vom Team selbstständig und konsequent gelebt – ohne dass ich täglich eingreife oder nachfassen muss"  
  <sub>— P053, Personal-Training-Studio</sub>
- „Ein zentrales System für Terminplanung, Dienstplan, Kommunikation und Dokumentation – das das gesamte Team konsistent und ohne Widerstand nutzt"  
  <sub>— P176, Physiotherapie-/Therapiepraxis</sub>
- „Automatischer wöchentlicher Überblick über freie Kapazitäten, Dienstplan-Status und fehlende Einträge – ohne selbst alles zusammentragen zu müssen"  
  <sub>— P131, Physiotherapie-/Therapiepraxis</sub>
- „Echte, gelebte Delegation: Team plant, entscheidet und kommuniziert selbstständig – ich bin Inhaberin, nicht Knotenpunkt und Lückenfüllerin für alles"  
  <sub>— P001, Physiotherapie-/Therapiepraxis</sub>

### Kommunikation mit Klient:innen — 3 Personas
- „Vollautomatischer, nahtloser Interessenten- und Onboarding-Prozess – von Erstanfrage bis laufendem Kundenverhältnis – ohne manuellen Aufwand meinerseits"  
  <sub>— P033, Personal-Training-Studio</sub>
- „Intelligentes System, das alle Kommunikationskanäle filtert, vorsortiert und mit Antwortvorschlägen oder automatischen Aktionen verarbeitet – praxisspezifisch, nicht generisch"  
  <sub>— P060, Wellness-/Longevity-Praxis (Premium)</sub>
- „Ein einheitliches, von allen genutztes System für Kundenmanagement und interne Kommunikation, das Angebotsprozesse halbautomatisiert und mich als menschlichen Knotenpunkt ersetzt – um 6–8 Stunden pro Woche zurückzugewinnen"  
  <sub>— P034, Präventions-/BGF-Anbieter</sub>

### Neue Klient:innen aufnehmen / Onboarding — 2 Personas
- „Vollständig automatisierter, schlanker Akquise- und Angebotsprozess – von Erstgespräch bis Nachverfolgung – ohne manuellen Aufwand"  
  <sub>— P079, Präventions-/BGF-Anbieter</sub>
- „Funktionierendes, automatisiertes Neukunden-Onboarding, das trotzdem persönlich wirkt – ohne manuellen Aufwand für mich oder mein Team"  
  <sub>— P083, Personal-Training-Studio</sub>

### Digitalisierung & Tools (Frust/Lücken) — 1 Personas
- „Vollautomatisierter, medienbruchfreier Klienten-Onboarding- und Nachsorgeprozess mit sauberem Datenfluss ins CRM – ohne manuelles Nachfassen, aber mit hochwertigem persönlichem Erscheinungsbild"  
  <sub>— P010, Wellness-/Longevity-Praxis (Premium)</sub>

### Telefon & Erreichbarkeit — 1 Personas
- „Alle Informationen (Termine, Urlaube, Krankmeldungen, Patientenkommunikation, Abrechnung) an einem einzigen, von allen genutzten Ort – ein echter Echtzeit-Überblick ohne Hinterhertelefonieren"  
  <sub>— P076, Physiotherapie-/Therapiepraxis</sub>

## 3. Sorgen rund um Wachstum, Personal & Zukunft

**Personal: Finden, Halten, Führen** (92): 
  - „Qualitätsverlust bei Wachstum, Qualitätsanspruch schwer auf neue Mitarbeitende übertragbar" <sub>— P054</sub>
  - „Schwierigkeit, fachlich gute Mitarbeitende für kleine Praxis zu gewinnen und einzuarbeiten" <sub>— P080</sub>

**Finanzen, Liquidität & Wachstumsdruck** (62): 
  - „Wachstum bedeutet mehr Komplexität und Verlust des eigenen fachlichen Kontakts zu Klienten" <sub>— P030</sub>
  - „Wachstum (z.B. zweiter Standort) nicht möglich wegen fehlender stabiler interner Strukturen" <sub>— P053</sub>

**Zukunfts- & Existenzsorgen** (51): 
  - „Kein Wachstumswille, aber Angst vor Bedeutungsverlust und mangelnder Wettbewerbsfähigkeit" <sub>— P029</sub>
  - „Abhängigkeit vom eigenen Dasein – Betrieb läuft nur weil Florian täglich alles zusammenhält" <sub>— P131</sub>

**Wissen, Prozesse & Ablage im Team** (21): 
  - „Wissen und Prozesse stecken nur im Kopf – keine Dokumentation für Nachfolge oder Übergabe" <sub>— P197</sub>
  - „Zu viel hängt an der eigenen Person – Wissen, Netzwerk, Kundenbeziehungen nicht übertragbar" <sub>— P204</sub>

**Alles hängt an mir / nicht delegieren können** (16): 
  - „Wachstum (z.B. zweiter Standort) operativ nicht stemmbarer ohne bessere interne Strukturen" <sub>— P028</sub>
  - „Zu tief im Operativen verstrickt, um Wachstum (zweiter Standort) realistisch anzugehen" <sub>— P108</sub>

## 4. Reaktion auf das Angebot (Phase 2)

**Buchungswahrscheinlichkeit kostenlose Erstanalyse (1–10):** Ø **5.8** · Median 6 (n=99)

| Score | Anzahl |
|---|---|
| 3 | 1 ················ |
| 4 | 12 ██·············· |
| 5 | 14 ██·············· |
| 6 | 47 ████████········ |
| 7 | 25 ████············ |

### Nützlichster Teil (gruppiert)
- **Terminorganisation & No-Shows** — 41 Nennungen
- **Neue Klient:innen aufnehmen / Onboarding** — 19 Nennungen
- **Wissen, Prozesse & Ablage im Team** — 16 Nennungen
- **Kommunikation mit Klient:innen** — 12 Nennungen
- **Personal: Finden, Halten, Führen** — 6 Nennungen
- **Verwaltung, Bürokratie & Abrechnung** — 4 Nennungen

### Größte Einwände (gruppiert + O-Töne)
**Zeitaufwand & Implementierungslast bleibt bei mir** (28):
  - „Unklare Folgekosten nach der Erstanalyse und hoher eigener Zeitaufwand während der Einführungsphase befürchtet" <sub>— P013, Personal-Training-Studio</sub>
  - „Zeitaufwand für Einführung und Schulung; Angst, dass es mehr kostet als bringt; eigene technische Überforderung" <sub>— P173, Personal-Training-Studio</sub>
  - „Unklare Folgekosten und unbekannter Einführungsaufwand – kein Budget und keine Kapazität für komplizierte Implementierung" <sub>— P153, Personal-Training-Studio</sub>

**Datenschutz & sensible Gesundheitsdaten** (19):
  - „Datenschutz bei Gesundheitsdaten (DSG Schweiz) und fehlende Nachbetreuung nach Einrichtung – keine interne IT-Ressource vorhanden" <sub>— P106, Physiotherapie-/Therapiepraxis</sub>
  - „Datenschutz bei sensiblen Gesundheitsdaten ist kritisch; Zweifel an Nachhaltigkeit externer Lösungen und fehlender Betreuung nach Einrichtung" <sub>— P152, Ernährungs-/Gesundheitszentrum</sub>
  - „Datenschutz bei Gesundheitsdaten ist nicht nur Formalität – echte Haftungsfrage; außerdem Zweifel an Nachhaltigkeit ohne laufende externe Betreuung" <sub>— P034, Präventions-/BGF-Anbieter</sub>

**Versteckte Folgekosten / Intransparenz nach Gratis-Analyse** (17):
  - „Wer wartet das System danach – fehlende interne IT-Kapazität; versteckte Folgekosten hinter kostenloser Erstanalyse" <sub>— P179, Präventions-/BGF-Anbieter</sub>
  - „Aufwand beim Einrichten zu gross für zwei-Personen-Betrieb; Unklarheit über Folgekosten nach kostenloser Erstanalyse" <sub>— P154, Präventions-/BGF-Anbieter</sub>
  - „Intransparenz über Folgekosten nach der Gratis-Analyse; Zweifel ob externe Person BGF-spezifische Komplexität schnell genug versteht" <sub>— P079, Präventions-/BGF-Anbieter</sub>

**Wartung & Betreuung danach / Nachhaltigkeit unklar** (14):
  - „Unklar was KI-gestützt konkret bedeutet; Sorge um fehlende Unterstützung nach der Einrichtung – wer hilft wenn etwas nicht funktioniert?" <sub>— P084, Präventions-/BGF-Anbieter</sub>
  - „System wird eingerichtet und dann bin ich allein damit; außerdem unklar was KI-gestützt konkret bedeutet und ob Entscheidungen abgegeben werden" <sub>— P032, Ernährungs-/Gesundheitszentrum</sub>
  - „Fehlende Nachhaltigkeit nach Projektabschluss und Angst vor zu generischer Lösung, die den spezifischen Gesundheitsbetrieb nicht wirklich abbildet" <sub>— P132, Ernährungs-/Gesundheitszentrum</sub>

**Abhängigkeit von externer Person / Anbieter** (11):
  - „Zeitaufwand für die Einrichtung, den ich selbst nicht habe – und Angst vor Abhängigkeit von einer externen Person, wenn das System läuft" <sub>— P123, Personal-Training-Studio</sub>
  - „Zeitinvestition meinerseits für Einblick und Erklärungen; Angst vor neuer Abhängigkeit von externer Person ohne eigene Wartungsfähigkeit" <sub>— P133, Personal-Training-Studio</sub>
  - „Generische Kommunikation würde Premium-Positionierung beschädigen; Abhängigkeit von externem Anbieter ohne eigene Wartungskompetenz danach" <sub>— P010, Wellness-/Longevity-Praxis (Premium)</sub>

**Angst um Persönlichkeit & Beziehungsqualität** (6):
  - „Angst vor Unpersönlichkeit durch Automatisierung (Beziehungsqualität ist unser Kernwert) und versteckter Aufwand bei Implementierung" <sub>— P028, Personal-Training-Studio</sub>
  - „Nachhaltigkeit nach Einrichtung unklar; außerdem Sorge, dass Automatisierung den persönlichen, vertrauensvollen Ton in der Klientenkommunikation zerstört" <sub>— P172, Ernährungs-/Gesundheitszentrum</sub>
  - „Wer pflegt das System nach der Einrichtung? Und: Passt die Lösung zum Premium-Ton unserer Kommunikation – oder wirkt sie generisch und schadet der Glaubwürdigkeit?" <sub>— P195, Wellness-/Longevity-Praxis (Premium)</sub>

## 5. Wer entscheidet mit? (Buy-in-Mapping)

| Rolle | Nennungen | Anteil |
|---|---|---|
| Team / Mitarbeitende / Praxismanagement | 134 | 53% |
| Ich allein / Inhaber:in entscheidet | 92 | 37% |
| Externe Berater:in / Steuer / Datenschutz / IT | 24 | 10% |
| Geschäftspartner:in / Mitinhaber:in | 2 | 1% |

## 6. Segment- & Teamgrößen-Unterschiede

**Buchungswahrscheinlichkeit nach Branche (Ø):**

| Branche | Ø Buchung | n |
|---|---|---|
| Wellness-/Longevity-Praxis (Premium) | 6.1 | 19 |
| Personal-Training-Studio | 5.9 | 20 |
| Physiotherapie-/Therapiepraxis | 5.8 | 21 |
| Ernährungs-/Gesundheitszentrum | 5.8 | 20 |
| Präventions-/BGF-Anbieter | 5.6 | 19 |

**Buchungswahrscheinlichkeit nach Teamgröße (Ø):**

| Teamgröße | Ø Buchung | n |
|---|---|---|
| 2-3 (klein) | 5.7 | 24 |
| 4-6 (mittel) | 6.1 | 33 |
| 7-10 (groß) | 5.7 | 42 |

## 7. Van-Westendorp-Preisanalyse

*OPP = optimaler Preispunkt (Schnitt „zu günstig"/„zu teuer"); Akzeptanzspanne = PMC–PME (Bereich, in dem weder zu billig noch zu teuer dominiert).*

### Einmaliges Aufbau-Projekt
- **Optimaler Preispunkt (OPP): ~2.250 €**
- Indifferenzpreis (IPP): ~2.825 €
- **Akzeptanzspanne: ~1.750 € – 3.792 €**
- Median „idealer" Preis der Personas: ~2.200 €
- <sub>n=99 plausible Antworten</sub>

### Monatlicher Betreuungs-Retainer
- **Optimaler Preispunkt (OPP): ~225 €**
- Indifferenzpreis (IPP): ~312 €
- **Akzeptanzspanne: ~200 € – 390 €**
- Median „idealer" Preis der Personas: ~320 €
- <sub>n=99 plausible Antworten</sub>

---

## Handlungsempfehlungen (nach Konfidenz gewichtet)

> Diese Empfehlungen sind **Hypothesen aus synthetischen Daten** und vor Umsetzung mit echten Gesprächen (10–20 Interviews) zu validieren (ESOMAR ICC 2025, Human Oversight).

**A · Hohe Konfidenz** (breit & konsistent über Segmente)

1. **Kern-Schmerz ist „Alles hängt an mir" + administrativer Wildwuchs.** Die stärksten Pain-Cluster sind *Verwaltung, Bürokratie & Abrechnung*, *Personal: Finden, Halten, Führen* und *Terminorganisation & No-Shows*. Botschaft sollte nicht „KI/Automatisierung" in den Vordergrund stellen, sondern das Ergebnis: **wieder Inhaber:in sein statt Knotenpunkt/Lückenfüller:in**. Die O-Töne in Abschnitt 1–2 liefern das Vokabular fast wörtlich.
2. **Einstieg „kostenlose Erstanalyse" zieht, aber lau** (Ø Buchung 5.8/10, Median 6 — Interesse ja, Euphorie nein). Erwartbar bei kalter, neutraler Beschreibung. Hebel ist nicht der Gratis-Einstieg selbst, sondern die Entkräftung der Einwände (siehe B).
3. **Entscheidung liegt fast nur intern**: „Ich allein" (~37%) und „Team/Praxismanagement" (~53%) dominieren; externe/Partner-Freigaben sind selten. → Sales-Prozess kann schlank 1:1 mit Inhaber:in laufen, sollte aber **das Team als Mitnutzer früh adressieren** (Akzeptanz im Team ist ein wiederkehrender Wunsch).

**B · Mittlere Konfidenz** (klares Muster, aber gegen echte Kund:innen zu prüfen)

4. **Die drei größten Kauf-Blocker** sind *Zeitaufwand & Implementierungslast bleibt bei mir*, *Datenschutz & sensible Gesundheitsdaten* und *Versteckte Folgekosten / Intransparenz nach Gratis-Analyse*. Diese gehören **proaktiv auf Website & ins Erstgespräch**: transparente Folgekosten/Fixpreise, klare Aussage „wer betreut das danach", DSGVO-/Serverstandort-Klarheit und das Versprechen, dass Persönlichkeit/Beziehung erhalten bleibt (nicht ersetzt wird).
5. **Datenschutz-Vertrauen ist Branchen-spezifisch heikel** (sensible Gesundheitsdaten). Ein sichtbarer, konkreter DSGVO-/Datenschutz-Baustein ist kein Hygienefaktor, sondern Verkaufsargument — gerade im Premium-Wellness-Segment, das zusätzlich um seine Exklusivität fürchtet.
6. **„Was passiert nach der Einrichtung?" ist der unterschätzte Hebel.** Sehr viele Einwände drehen sich um Nachhaltigkeit/Wartung. Das **stützt das Retainer-Modell** nicht als Zusatzverkauf, sondern als Vertrauens-Anker von Anfang an.

**C · Preis-Hypothesen** (Van-Westendorp, synthetisch — nur Orientierung)

7. **Aufbau-Projekt:** optimaler Preispunkt ~**2.250 €**. Akzeptanzspanne ~**1.750–3.792 €**. Ein Fixpreis-Einstiegspaket am unteren Rand der Spanne senkt den Folgekosten-Einwand.
8. **Retainer:** optimaler Preispunkt ~**225 €/Monat**. Akzeptanzspanne ~**200–390 €/Monat**. Liegt im Rahmen kleiner Betriebsbudgets; höhere Stufen brauchen sichtbaren laufenden Nutzen.
9. ⚠️ Bei den *idealen* Preisen zeigte sich leichte LLM-Homogenisierung (Häufung um einzelne Werte). Preispunkte daher als **grobe Korridore**, nicht als exakte Zahlen lesen — vor finaler Preissetzung mit echten Angeboten/Gesprächen testen.

<sub>Generiert aus 99 synthetischen Personas · Modell claude-sonnet-4-6 · Silicon Sampling gemäß ESOMAR ICC Code 2025 · Ergebnisse sind Hypothesen.</sub>