# Silicon-Sampling-Studie — Auswertung

**Zielgruppe:** Kleine Gesundheits- & Wellness-Betriebe mit Team (2–10 Personen) im DACH-Raum — Inhaber:innen/Leitung von Physio-/Therapiepraxen, Ernährungs-/Gesundheitszentren, Personal-Training-Studios, Präventions-/BGF-Anbietern und Premium-Wellness-/Longevity-Praxen.

> ⚠️ **SYNTHETISCHE DATEN — ESOMAR ICC Code 2025.** Diese Ergebnisse stammen aus *Silicon Sampling*: KI-Personas wurden befragt, keine echten Menschen. Die Befunde sind **Hypothesen, keine validierten Fakten**, und müssen vor strategischen Entscheidungen durch echte Interviews (10–20) validiert werden. Bekannte Grenzen: gesprochene Präferenz statt echtem Verhalten, mögliche Homogenisierung von Mehrheitsmeinungen, kein Ersatz für reale Marktforschung.

## Methodik (reproduzierbar)

- **Modell:** `claude-sonnet-4-6`
- **Personas:** 220 vollständig befragt, deterministisch geseedet (Seed `20260625`).
- **Prompt-Version:** `2026-06-25.v1`
- **Befragung:** 3-Phasen-Multi-Turn, blind. Phase 1 (offen) **vor** jeder Konzept-Nennung; keine Leading-Fragen; Personas ausdrücklich zu Kritik/Ablehnung ermutigt.
- **Persona-Generierung & Prompts:** vollständig im Repo (`personas.py`, `prompts.py`).
- **Unabhängigkeit:** Es wurden bewusst keine Pain Points/Wünsche/Formulierungen vorgegeben — alle Inhalte stammen aus den Personas selbst.

### Stichprobenstruktur

**Branche:** Physiotherapie-/Therapiepraxis (44) · Ernährungs-/Gesundheitszentrum (44) · Personal-Training-Studio (44) · Präventions-/BGF-Anbieter (44) · Wellness-/Longevity-Praxis (Premium) (44)

**Land:** CH (76) · DE (76) · AT (68)

**Haltung:** neugierig-offen (45) · pragmatisch-abwägend (42) · skeptisch (35) · überfordert / zu wenig Zeit (33) · desinteressiert / sieht keinen Bedarf (29) · früher Anwender / probiert gern Neues (21) · stark skeptisch (15)

## 1. Häufigste Pain Points (gruppiert & nach Häufigkeit)

*Häufigkeit = Zahl der Personas (von 220), die diesen Themenbereich in Phase 1 von sich aus nannten.*

### Verwaltung, Bürokratie & Abrechnung — 193 Personas (88%)
`█████████████████████···`

**O-Töne:**
- „Administrative Systeme sind nicht vernetzt – Kalender, Abrechnung, Dossiers laufen separat"  
  <sub>— P046, Physiotherapie-/Therapiepraxis</sub>
- „Administrative Kleinteiligkeit durch unterschiedliche Krankenkassen-Logiken und -Formulare"  
  <sub>— P104, Präventions-/BGF-Anbieter</sub>
- „Kleinkram-Administration die sich nicht erledigt (Offerten in Word, manuelles PDF-Versand)"  
  <sub>— P214, Präventions-/BGF-Anbieter</sub>
- „Monatliche Abrechnung: Stundenlisten, Rechnungen, Zahlungsverfolgung – stupide Fleißarbeit"  
  <sub>— P098, Personal-Training-Studio</sub>
- „Abrechnung mit Krankenkassen: unterschiedliche Formulare, Fristen, hoher manueller Aufwand"  
  <sub>— P157, Ernährungs-/Gesundheitszentrum</sub>

### Personal: Finden, Halten, Führen — 159 Personas (72%)
`█████████████████·······`

**O-Töne:**
- „Permanente Doppelrolle als Führungsperson und Fachperson – nie ganz in einer Rolle präsent"  
  <sub>— P187, Ernährungs-/Gesundheitszentrum</sub>
- „Personalplanung läuft über selbstgebastelte Excel-Tabelle – fehleranfällig und zeitraubend"  
  <sub>— P208, Personal-Training-Studio</sub>
- „Ewiges Koordinieren von Dienstplänen, Urlauben und Klientenpräferenzen mit Papier und Excel"  
  <sub>— P056, Physiotherapie-/Therapiepraxis</sub>
- „Perfektionismus kombiniert mit fehlenden Prozessen führt dazu, Aufgaben nicht loszulassen"  
  <sub>— P124, Präventions-/BGF-Anbieter</sub>
- „Kommunikation im Team läuft über viele verschiedene Kanäle, Julia als zentraler Verteiler"  
  <sub>— P157, Ernährungs-/Gesundheitszentrum</sub>

### Terminorganisation & No-Shows — 148 Personas (67%)
`████████████████········`

**O-Töne:**
- „Papierkalender und WhatsApp statt einheitlichem System führen zu Doppelbuchungen und Chaos"  
  <sub>— P085, Wellness-/Longevity-Praxis (Premium)</sub>
- „Kein einheitliches System – Papierkalender, WhatsApp und handschriftliche Notizen parallel"  
  <sub>— P163, Personal-Training-Studio</sub>
- „Terminkollisionen durch dezentrale Kalenderführung – Klienten standen vor besetzten Räumen"  
  <sub>— P167, Ernährungs-/Gesundheitszentrum</sub>
- „Terminkoordination täglich aufwändig und fehleranfällig durch fehlende gemeinsame Übersicht"  
  <sub>— P080, Wellness-/Longevity-Praxis (Premium)</sub>
- „Unübersichtlichkeit durch Papierkalender und Excel-Listen, Terminpannen die peinlich sind"  
  <sub>— P203, Personal-Training-Studio</sub>

### Kommunikation mit Klient:innen — 131 Personas (60%)
`██████████████··········`

**O-Töne:**
- „Kommunikation mit Klient:innen über zu viele verschiedene Kanäle (WhatsApp, Anruf, E-Mail)"  
  <sub>— P095, Wellness-/Longevity-Praxis (Premium)</sub>
- „Interne Kommunikation chaotisch, läuft über WhatsApp und Zettel, kein strukturierter Kanal"  
  <sub>— P130, Wellness-/Longevity-Praxis (Premium)</sub>
- „Informationen versickern in verschiedenen Kanälen (WhatsApp, Mail, Praxissoftware, Zettel)"  
  <sub>— P187, Ernährungs-/Gesundheitszentrum</sub>
- „Wiederkehrende Unterbrechungen durch Rückfragen, die ein klares Regelwerk verhindern würde"  
  <sub>— P110, Wellness-/Longevity-Praxis (Premium)</sub>
- „Unstrukturierte Mehrkanalkommunikation mit Klientinnen (WhatsApp, Mail, Telefon gemischt)"  
  <sub>— P183, Personal-Training-Studio</sub>

### Digitalisierung & Tools (Frust/Lücken) — 105 Personas (48%)
`███████████·············`

**O-Töne:**
- „Praxissoftware vorhanden aber nicht vernetzt/genutzt, vieles läuft über WhatsApp und Zettel"  
  <sub>— P013, Personal-Training-Studio</sub>
- „Zu viel manuelle Koordination trotz kleinem Team – Leiterin als menschliche Schnittstelle"  
  <sub>— P104, Präventions-/BGF-Anbieter</sub>
- „Manuelle Verwaltung von Abo-Mutationen (Pause, Kündigung, Wechsel) ohne Systemunterstützung"  
  <sub>— P173, Personal-Training-Studio</sub>
- „Fehlende Systeme: Papier, Zettel, mündliche Absprachen – unzuverlässig bei Abwesenheiten"  
  <sub>— P087, Ernährungs-/Gesundheitszentrum</sub>
- „Kollegin Bettina schwer für digitale Tools zu begeistern, dadurch viel Erklärungsaufwand"  
  <sub>— P112, Ernährungs-/Gesundheitszentrum</sub>

### Wissen, Prozesse & Ablage im Team — 96 Personas (44%)
`██████████··············`

**O-Töne:**
- „Angebotserstellung für Firmenkunden jedes Mal von Grund auf, kein standardisierter Prozess"  
  <sub>— P049, Präventions-/BGF-Anbieter</sub>
- „Immer wiederkehrendes manuelles Onboarding neuer Klientinnen ohne standardisierten Prozess"  
  <sub>— P098, Personal-Training-Studio</sub>
- „Langwierige, unstrukturierte Einarbeitung neuer Mitarbeitender ohne Handbuch oder Prozesse"  
  <sub>— P170, Wellness-/Longevity-Praxis (Premium)</sub>
- „Kleinigkeiten und Entscheidungen eskalieren zu mir, weil Prozesse nicht dokumentiert sind"  
  <sub>— P172, Ernährungs-/Gesundheitszentrum</sub>
- „Zu viel Administration läuft über mich, weil klare Systeme und dokumentierte Abläufe fehlen"  
  <sub>— P199, Präventions-/BGF-Anbieter</sub>

### Alles hängt an mir / nicht delegieren können — 87 Personas (40%)
`█████████···············`

**O-Töne:**
- „Wird in Kontrolleur-/Koordinatorrolle gedrängt, die nicht zur eigenen Persönlichkeit passt"  
  <sub>— P088, Personal-Training-Studio</sub>
- „Nachfassen bei Interessenten nach Offerten – mental belastend, fühlt sich wie 'betteln' an"  
  <sub>— P144, Präventions-/BGF-Anbieter</sub>
- „Lande regelmässig bei Aufgaben, die delegierbar wären, aber Teamgrösse lässt das nicht zu"  
  <sub>— P100, Wellness-/Longevity-Praxis (Premium)</sub>
- „Zu viel läuft über mich als Leitung – bin selbst der Engpass, übergebe Verantwortung schwer"  
  <sub>— P174, Präventions-/BGF-Anbieter</sub>
- „Lange, ineffiziente Angebotsphase bei neuen Firmenkunden mit viel Nachfassen und Anpassen"  
  <sub>— P034, Präventions-/BGF-Anbieter</sub>

### Zeitmangel, Unterbrechungen & Überlastung — 44 Personas (20%)
`█████···················`

**O-Töne:**
- „Sitzt abends spät noch vor dem Laptop wegen mangelnder Delegation durch fehlende Strukturen"  
  <sub>— P124, Präventions-/BGF-Anbieter</sub>
- „Ständige Unterbrechungen durch Teamfragen, die eigentlich strukturell gelöst sein sollten"  
  <sub>— P205, Wellness-/Longevity-Praxis (Premium)</sub>
- „Keine Zeit, strukturelle Verbesserungen wirklich umzusetzen, weil immer etwas dazwischenkommt"  
  <sub>— P007, Ernährungs-/Gesundheitszentrum</sub>
- „Zerstückelung des Alltags – Planung wird ständig durch Unvorhergesehenes unterbrochen"  
  <sub>— P009, Präventions-/BGF-Anbieter</sub>
- „Reibung zwischen eigenen Qualitätsvorstellungen und tatsächlicher Umsetzung im Alltag"  
  <sub>— P180, Wellness-/Longevity-Praxis (Premium)</sub>

### Neue Klient:innen aufnehmen / Onboarding — 34 Personas (15%)
`████····················`

**O-Töne:**
- „Manuelles Neukunden-Onboarding kostet pro Person 1,5–2 Stunden ohne standardisierten Prozess"  
  <sub>— P083, Personal-Training-Studio</sub>
- „Neukundenaufnahme auf Papier, manuelle Übertragung in Excel, Fehler und Nachfragen inklusive"  
  <sub>— P167, Ernährungs-/Gesundheitszentrum</sub>
- „Onboarding neuer Trainer ohne verschriftlichten Prozess – immer wieder dieselben Erklärungen"  
  <sub>— P178, Personal-Training-Studio</sub>
- „Unstrukturierter Neukunden-Erstkontakt über verschiedene Kanäle ohne Nachverfolgung"  
  <sub>— P078, Personal-Training-Studio</sub>
- „Angefangene Projekte (z.B. Onboarding-Dokument) bleiben liegen wegen Tagesgeschäft"  
  <sub>— P092, Ernährungs-/Gesundheitszentrum</sub>

### Telefon & Erreichbarkeit — 29 Personas (13%)
`███·····················`

**O-Töne:**
- „Chaotische, dezentrale Kommunikation im Team (SMS, Anruf, Zettel – kein einheitlicher Kanal)"  
  <sub>— P038, Personal-Training-Studio</sub>
- „Ungefilterte Zwischenfragen von Klienten per Telefon/Nachricht ohne strukturierten Kanal"  
  <sub>— P015, Wellness-/Longevity-Praxis (Premium)</sub>
- „Telefonisches Nachfassen bei Interessenten – viele gehen verloren, weil Rückruf zu spät kommt"  
  <sub>— P163, Personal-Training-Studio</sub>
- „Freitags das Gefühl, nichts Wesentliches geschafft zu haben trotz viel Telefonieren und Suchen"  
  <sub>— P215, Wellness-/Longevity-Praxis (Premium)</sub>
- „Anrufbeantworter wird von Patienten kaum genutzt, trotzdem muss jemand abhören und zurückrufen"  
  <sub>— P011, Physiotherapie-/Therapiepraxis</sub>

### Marketing, Sichtbarkeit & Neukundengewinnung — 13 Personas (6%)
`█·······················`

**O-Töne:**
- „Offertenwesen: aufwändige individuelle Angebote mit tiefer Abschlussquote und kaum Feedback"  
  <sub>— P189, Präventions-/BGF-Anbieter</sub>
- „Muss selbst Marketing/Content machen (Instagram, Newsletter) obwohl das nicht meine Stärke ist"  
  <sub>— P145, Wellness-/Longevity-Praxis (Premium)</sub>
- „Muss als Chefin aktiv nachfragen, um Grundinfos zu bekommen – sollte auf einen Blick sichtbar sein"  
  <sub>— P017, Ernährungs-/Gesundheitszentrum</sub>
- „Angebote und Offerten jedes Mal fast neu erstellen, keine funktionierende Vorlage"  
  <sub>— P039, Präventions-/BGF-Anbieter</sub>
- „Angebote schreiben ohne Vorlagen – jedes Mal von null, halber Tag für ein Angebot"  
  <sub>— P124, Präventions-/BGF-Anbieter</sub>

### Zukunfts- & Existenzsorgen — 6 Personas (3%)
`█·······················`

**O-Töne:**
- „Abhängigkeit des Betriebs von meiner eigenen Person strukturell nicht gelöst"  
  <sub>— P200, Wellness-/Longevity-Praxis (Premium)</sub>
- „Gesamtüberblick liegt nur bei mir, starke Abhängigkeit von meiner Person"  
  <sub>— P110, Wellness-/Longevity-Praxis (Premium)</sub>
- „Fühlt sich nach 12 Jahren noch zu abhängig von ihrer eigenen Präsenz"  
  <sub>— P201, Physiotherapie-/Therapiepraxis</sub>
- „Kontrollverlust bei Delegation – Angst, dass Qualität leidet"  
  <sub>— P194, Präventions-/BGF-Anbieter</sub>
- „Abhängigkeit von einzelnen Schlüsselpersonen"  
  <sub>— P055, Wellness-/Longevity-Praxis (Premium)</sub>

### Finanzen, Liquidität & Wachstumsdruck — 6 Personas (3%)
`█·······················`

**O-Töne:**
- „Nachfassen bei Hochpreis-Kunden läuft manuell und wird vergessen – kostet konkret Umsatz"  
  <sub>— P210, Wellness-/Longevity-Praxis (Premium)</sub>
- „Aktualisierung von Preisen auf Webseite und Printmaterialien immer wieder aufwändig"  
  <sub>— P095, Wellness-/Longevity-Praxis (Premium)</sub>
- „Fehlender Einstieg in Automatisierung durch Unklarheit über Aufwand und Kosten"  
  <sub>— P075, Wellness-/Longevity-Praxis (Premium)</sub>
- „Preisdiskussionen mit Kunden (mitbekommen, auch wenn nicht direkt involviert)"  
  <sub>— P188, Personal-Training-Studio</sub>
- „Fehlende Strukturen trotz fast 500k Umsatz – Betrieb hat nicht mitgewachsen"  
  <sub>— P067, Ernährungs-/Gesundheitszentrum</sub>

## 2. Wünsche „per Zauberei" (gruppiert)

### Verwaltung, Bürokratie & Abrechnung — 73 Personas
- „Ein integriertes System für Dienstplanung, Terminverwaltung und Abrechnung – kein manueller Abgleich, kein Engpass-Ich mehr"  
  <sub>— P121, Physiotherapie-/Therapiepraxis</sub>
- „Team arbeitet konsequent und eigenverantwortlich nach gemeinsam definierten Abläufen – ohne dass ich ständig nachsteuern muss"  
  <sub>— P202, Ernährungs-/Gesundheitszentrum</sub>
- „Terminplanung und Abrechnung laufen automatisch und sauber – ohne abendlichen Aufwand und ohne dass alles in meinem Kopf hängt"  
  <sub>— P143, Personal-Training-Studio</sub>
- „Ein einziges System für Termine, Kundendaten, Abrechnung und Teamkommunikation – das funktioniert und vom Team wirklich genutzt wird"  
  <sub>— P167, Ernährungs-/Gesundheitszentrum</sub>

### Terminorganisation & No-Shows — 58 Personas
- „Vollständig automatisierter Erstkundenprozess – von Anfrage bis gebuchtem Termin ohne manuelle Eingriffe"  
  <sub>— P052, Ernährungs-/Gesundheitszentrum</sub>
- „Vollautomatische Terminverwaltung mit Warteliste, Absagen und Bestätigungen – ohne manuellen Aufwand im Team"  
  <sub>— P181, Physiotherapie-/Therapiepraxis</sub>
- „Digitale Terminplanung und interne Kommunikation, die einfach funktioniert – ohne grossen Einrichtungsaufwand"  
  <sub>— P016, Physiotherapie-/Therapiepraxis</sub>
- „Alle im Team haben zur selben Zeit dieselbe Information – einheitliche, sofort sichtbare Terminverwaltung für alle"  
  <sub>— P032, Ernährungs-/Gesundheitszentrum</sub>

### Wissen, Prozesse & Ablage im Team — 36 Personas
- „Funktionierende, einheitliche und wirklich gelebte Prozesse – die ohne meine ständige Anwesenheit laufen"  
  <sub>— P147, Ernährungs-/Gesundheitszentrum</sub>
- „Betrieb funktioniert eigenständig ohne mich – klare Prozesse, dokumentiertes Wissen, selbstständig arbeitendes Team"  
  <sub>— P048, Personal-Training-Studio</sub>
- „Ein einfaches, wirklich genutztes System für Projektübersicht und Teamaufgaben – ohne dass ich es ständig pushen muss"  
  <sub>— P084, Präventions-/BGF-Anbieter</sub>
- „Implizites Wissen aus meinem Kopf sauber dokumentiert und im Team verankert – damit die Praxis nicht von meiner Anwesenheit abhängt"  
  <sub>— P036, Physiotherapie-/Therapiepraxis</sub>

### Personal: Finden, Halten, Führen — 33 Personas
- „Prozesse werden vom Team selbstständig und konsequent gelebt – ohne dass ich täglich eingreife oder nachfassen muss"  
  <sub>— P053, Personal-Training-Studio</sub>
- „Gelebte Eigenverantwortung im Team – klares Rollenmodell mit echten Entscheidungskompetenzen, das im Alltag wirklich funktioniert"  
  <sub>— P072, Ernährungs-/Gesundheitszentrum</sub>
- „Team, das wirklich selbstständig und nach klaren Regeln entscheiden kann – ohne dass ich jedes Mal Anker und Entscheidungsinstanz bin"  
  <sub>— P045, Wellness-/Longevity-Praxis (Premium)</sub>
- „Ein einziges, zentrales System das Termine, Kommunikation, Aufgaben und Mitarbeiterinformationen bündelt – und das das Team wirklich nutzt"  
  <sub>— P020, Wellness-/Longevity-Praxis (Premium)</sub>

### Kommunikation mit Klient:innen — 7 Personas
- „Eine funktionierende interne Koordinations- und Kommunikationsstruktur, die läuft ohne dass ich ständig Feuerwehr spielen muss"  
  <sub>— P044, Präventions-/BGF-Anbieter</sub>
- „Auftragsabwicklung von Erstanfrage bis Zahlungseingang läuft automatisch und zuverlässig – ohne dauerndes manuelles Nachschauen und mentale Belastung"  
  <sub>— P144, Präventions-/BGF-Anbieter</sub>
- „Vollautomatischer, nahtloser Interessenten- und Onboarding-Prozess – von Erstanfrage bis laufendem Kundenverhältnis – ohne manuellen Aufwand meinerseits"  
  <sub>— P033, Personal-Training-Studio</sub>
- „Funktionierende Ablauf- und Entscheidungsstrukturen, die den Betrieb auch ohne mich am Laufen halten – klare Prozesse für Anfragen, Angebote, interne Kommunikation"  
  <sub>— P159, Präventions-/BGF-Anbieter</sub>

### Digitalisierung & Tools (Frust/Lücken) — 6 Personas
- „Alle Tools vernetzt, ein einziges funktionierendes System für Termine, Kundendaten, Rechnungen und interne Notizen – und ein Team, das es wirklich nutzt"  
  <sub>— P097, Ernährungs-/Gesundheitszentrum</sub>
- „Alles in einem System zusammenführen: Kundenverwaltung, Buchungen, Zahlungen und Einsatzplanung auf einen Blick – kein Zettelchaos, keine getrennten Tools"  
  <sub>— P168, Personal-Training-Studio</sub>
- „Ein integriertes System das Kundenanfrage, Angebot, Auftragserfassung, Rechnungsstellung und Mahnwesen automatisch verbindet – ohne manuelle Brücken zwischen Tools"  
  <sub>— P214, Präventions-/BGF-Anbieter</sub>
- „Ein zentrales Dashboard, das alle vorhandenen Systeme (Software, Kalender, Mail, Buchhaltung) automatisch vernetzt – sodass ich nicht mehr selbst der Klebstoff zwischen Insellösungen sein muss"  
  <sub>— P120, Wellness-/Longevity-Praxis (Premium)</sub>

### Alles hängt an mir / nicht delegieren können — 2 Personas
- „Team, das eigenständig und sicher entscheiden kann – funktionierende Strukturen und Zuständigkeiten ohne mich als Flaschenhals"  
  <sub>— P025, Wellness-/Longevity-Praxis (Premium)</sub>
- „Ein kohärentes, automatisiertes Prozesssystem für Anfragen, Angebote und Nachfassaktionen – das ohne mich als manuellem Flaschenhals funktioniert"  
  <sub>— P134, Präventions-/BGF-Anbieter</sub>

### Neue Klient:innen aufnehmen / Onboarding — 2 Personas
- „Vollständig automatisierter, schlanker Akquise- und Angebotsprozess – von Erstgespräch bis Nachverfolgung – ohne manuellen Aufwand"  
  <sub>— P079, Präventions-/BGF-Anbieter</sub>
- „Funktionierendes, automatisiertes Neukunden-Onboarding, das trotzdem persönlich wirkt – ohne manuellen Aufwand für mich oder mein Team"  
  <sub>— P083, Personal-Training-Studio</sub>

## 3. Sorgen rund um Wachstum, Personal & Zukunft

**Personal: Finden, Halten, Führen** (203): 
  - „Schwierigkeit, qualifiziertes Personal zu gewinnen und zu halten gegen größere Arbeitgeber" <sub>— P014</sub>
  - „Qualitätsverlust bei Wachstum, Qualitätsanspruch schwer auf neue Mitarbeitende übertragbar" <sub>— P054</sub>

**Finanzen, Liquidität & Wachstumsdruck** (135): 
  - „Wachstum bedeutet mehr Komplexität und Verlust des eigenen fachlichen Kontakts zu Klienten" <sub>— P030</sub>
  - „Wachstum (z.B. zweiter Standort) nicht möglich wegen fehlender stabiler interner Strukturen" <sub>— P053</sub>

**Zukunfts- & Existenzsorgen** (105): 
  - „Kein Wachstumswille, aber Angst vor Bedeutungsverlust und mangelnder Wettbewerbsfähigkeit" <sub>— P029</sub>
  - „Abhängigkeit vom eigenen Dasein – Betrieb läuft nur weil Florian täglich alles zusammenhält" <sub>— P131</sub>

**Wissen, Prozesse & Ablage im Team** (49): 
  - „Nachfolge ungeklärt: Suche nach unternehmerisch denkenden Ergotherapeuten kaum realistisch" <sub>— P041</sub>
  - „Keine klare Nachfolgeperspektive – zu viel Wissen und Prozesse stecken im Kopf der Leitung" <sub>— P088</sub>

**Digitalisierung & Tools (Frust/Lücken)** (31): 
  - „Bremse mich selbst beim Wachstum aus, weil das bestehende System mehr Kunden nicht trägt" <sub>— P210</sub>
  - „Frage, ob Beziehungsqualität gegen skalierbare digitale Angebote kommunizierbar bleibt" <sub>— P060</sub>

## 4. Reaktion auf das Angebot (Phase 2)

**Buchungswahrscheinlichkeit kostenlose Erstanalyse (1–10):** Ø **5.8** · Median 6 (n=220)

| Score | Anzahl |
|---|---|
| 3 | 1 ················ |
| 4 | 32 ██·············· |
| 5 | 38 ███············· |
| 6 | 93 ███████········· |
| 7 | 56 ████············ |

### Nützlichster Teil (gruppiert)
- **Terminorganisation & No-Shows** — 101 Nennungen
- **Neue Klient:innen aufnehmen / Onboarding** — 42 Nennungen
- **Wissen, Prozesse & Ablage im Team** — 28 Nennungen
- **Kommunikation mit Klient:innen** — 22 Nennungen
- **Personal: Finden, Halten, Führen** — 15 Nennungen
- **Verwaltung, Bürokratie & Abrechnung** — 9 Nennungen

### Größte Einwände (gruppiert + O-Töne)
**Zeitaufwand & Implementierungslast bleibt bei mir** (56):
  - „Unklare Folgekosten nach der Erstanalyse und hoher eigener Zeitaufwand während der Einführungsphase befürchtet" <sub>— P013, Personal-Training-Studio</sub>
  - „Zeitaufwand für Einführung und Schulung; Angst, dass es mehr kostet als bringt; eigene technische Überforderung" <sub>— P173, Personal-Training-Studio</sub>
  - „Zweifel, dass externe Person die Spezifik des Betriebs versteht; keine Zeit und Nerven für langen Umstellungsprozess" <sub>— P165, Wellness-/Longevity-Praxis (Premium)</sub>

**Datenschutz & sensible Gesundheitsdaten** (45):
  - „Datenschutz bei sensiblen Gesundheitsdaten; Angst vor Aufwand der Umstellung und Widerstand im Team" <sub>— P042, Ernährungs-/Gesundheitszentrum</sub>
  - „Datenschutz und rechtliche Sicherheit bei sensiblen Gesundheitsdaten; Zweifel ob Team neue Systeme wirklich annimmt" <sub>— P212, Ernährungs-/Gesundheitszentrum</sub>
  - „Datenschutz bei Gesundheitsdaten (DSG Schweiz) und fehlende Nachbetreuung nach Einrichtung – keine interne IT-Ressource vorhanden" <sub>— P106, Physiotherapie-/Therapiepraxis</sub>

**Versteckte Folgekosten / Intransparenz nach Gratis-Analyse** (39):
  - „Angst vor Entpersönlichung des Studios durch Automatisierung, und Unklarheit über Folgekosten nach der Erstanalyse" <sub>— P183, Personal-Training-Studio</sub>
  - „Wer wartet das System danach – fehlende interne IT-Kapazität; versteckte Folgekosten hinter kostenloser Erstanalyse" <sub>— P179, Präventions-/BGF-Anbieter</sub>
  - „Angst vor einer Lösung, die nicht wirklich passt und brachliegt; Intransparenz über Folgekosten nach der Erstanalyse" <sub>— P092, Ernährungs-/Gesundheitszentrum</sub>

**Wartung & Betreuung danach / Nachhaltigkeit unklar** (30):
  - „Zu schnelles Setup versteht den Betrieb nicht wirklich; fehlende Nachhaltigkeit wenn externe Person geht und Team das System nicht trägt" <sub>— P025, Wellness-/Longevity-Praxis (Premium)</sub>
  - „Unklar was KI-gestützt konkret bedeutet; Sorge um fehlende Unterstützung nach der Einrichtung – wer hilft wenn etwas nicht funktioniert?" <sub>— P084, Präventions-/BGF-Anbieter</sub>
  - „System wird eingerichtet und dann bin ich allein damit; außerdem unklar was KI-gestützt konkret bedeutet und ob Entscheidungen abgegeben werden" <sub>— P032, Ernährungs-/Gesundheitszentrum</sub>

**Abhängigkeit von externer Person / Anbieter** (24):
  - „Komplexität durch KI überfordert ältere Mitarbeitende; Abhängigkeit von externer Person, die nach Einrichtung nicht mehr verfügbar ist" <sub>— P065, Wellness-/Longevity-Praxis (Premium)</sub>
  - „Zeitaufwand für die Einrichtung, den ich selbst nicht habe – und Angst vor Abhängigkeit von einer externen Person, wenn das System läuft" <sub>— P123, Personal-Training-Studio</sub>
  - „Zeitinvestition meinerseits für Einblick und Erklärungen; Angst vor neuer Abhängigkeit von externer Person ohne eigene Wartungsfähigkeit" <sub>— P133, Personal-Training-Studio</sub>

## 5. Wer entscheidet mit? (Buy-in-Mapping)

| Rolle | Nennungen | Anteil |
|---|---|---|
| Team / Mitarbeitende / Praxismanagement | 308 | 55% |
| Ich allein / Inhaber:in entscheidet | 203 | 36% |
| Externe Berater:in / Steuer / Datenschutz / IT | 49 | 9% |
| Partner:in / Familie (privat) | 2 | 0% |
| Geschäftspartner:in / Mitinhaber:in | 2 | 0% |

## 6. Segment- & Teamgrößen-Unterschiede

**Buchungswahrscheinlichkeit nach Branche (Ø):**

| Branche | Ø Buchung | n |
|---|---|---|
| Ernährungs-/Gesundheitszentrum | 5.9 | 44 |
| Wellness-/Longevity-Praxis (Premium) | 5.9 | 44 |
| Physiotherapie-/Therapiepraxis | 5.8 | 44 |
| Präventions-/BGF-Anbieter | 5.7 | 44 |
| Personal-Training-Studio | 5.6 | 44 |

**Buchungswahrscheinlichkeit nach Teamgröße (Ø):**

| Teamgröße | Ø Buchung | n |
|---|---|---|
| 2-3 (klein) | 5.6 | 50 |
| 4-6 (mittel) | 5.9 | 68 |
| 7-10 (groß) | 5.8 | 102 |

## 7. Van-Westendorp-Preisanalyse

*OPP = optimaler Preispunkt (Schnitt „zu günstig"/„zu teuer"); Akzeptanzspanne = PMC–PME (Bereich, in dem weder zu billig noch zu teuer dominiert).*

### Einmaliges Aufbau-Projekt
- **Optimaler Preispunkt (OPP): ~2.167 €**
- Indifferenzpreis (IPP): ~2.740 €
- **Akzeptanzspanne: ~1.740 € – 3.667 €**
- Median „idealer" Preis der Personas: ~2.200 €
- <sub>n=220 plausible Antworten</sub>

### Monatlicher Betreuungs-Retainer
- **Optimaler Preispunkt (OPP): ~220 €**
- Indifferenzpreis (IPP): ~318 €
- **Akzeptanzspanne: ~193 € – 386 €**
- Median „idealer" Preis der Personas: ~320 €
- <sub>n=220 plausible Antworten</sub>

---

## Handlungsempfehlungen (nach Konfidenz gewichtet)

> Diese Empfehlungen sind **Hypothesen aus synthetischen Daten** und vor Umsetzung mit echten Gesprächen (10–20 Interviews) zu validieren (ESOMAR ICC 2025, Human Oversight).

**A · Hohe Konfidenz** (breit & konsistent über Segmente)

1. **Kern-Schmerz ist „Alles hängt an mir" + administrativer Wildwuchs.** Die stärksten Pain-Cluster sind *Verwaltung, Bürokratie & Abrechnung*, *Personal: Finden, Halten, Führen* und *Terminorganisation & No-Shows*. Botschaft sollte nicht „KI/Automatisierung" in den Vordergrund stellen, sondern das Ergebnis: **wieder Inhaber:in sein statt Knotenpunkt/Lückenfüller:in**. Die O-Töne in Abschnitt 1–2 liefern das Vokabular fast wörtlich.
2. **Einstieg „kostenlose Erstanalyse" zieht, aber lau** (Ø Buchung 5.8/10, Median 6 — Interesse ja, Euphorie nein). Erwartbar bei kalter, neutraler Beschreibung. Hebel ist nicht der Gratis-Einstieg selbst, sondern die Entkräftung der Einwände (siehe B).
3. **Entscheidung liegt fast nur intern**: „Ich allein" (~36%) und „Team/Praxismanagement" (~55%) dominieren; externe/Partner-Freigaben sind selten. → Sales-Prozess kann schlank 1:1 mit Inhaber:in laufen, sollte aber **das Team als Mitnutzer früh adressieren** (Akzeptanz im Team ist ein wiederkehrender Wunsch).

**B · Mittlere Konfidenz** (klares Muster, aber gegen echte Kund:innen zu prüfen)

4. **Die drei größten Kauf-Blocker** sind *Zeitaufwand & Implementierungslast bleibt bei mir*, *Datenschutz & sensible Gesundheitsdaten* und *Versteckte Folgekosten / Intransparenz nach Gratis-Analyse*. Diese gehören **proaktiv auf Website & ins Erstgespräch**: transparente Folgekosten/Fixpreise, klare Aussage „wer betreut das danach", DSGVO-/Serverstandort-Klarheit und das Versprechen, dass Persönlichkeit/Beziehung erhalten bleibt (nicht ersetzt wird).
5. **Datenschutz-Vertrauen ist Branchen-spezifisch heikel** (sensible Gesundheitsdaten). Ein sichtbarer, konkreter DSGVO-/Datenschutz-Baustein ist kein Hygienefaktor, sondern Verkaufsargument — gerade im Premium-Wellness-Segment, das zusätzlich um seine Exklusivität fürchtet.
6. **„Was passiert nach der Einrichtung?" ist der unterschätzte Hebel.** Sehr viele Einwände drehen sich um Nachhaltigkeit/Wartung. Das **stützt das Retainer-Modell** nicht als Zusatzverkauf, sondern als Vertrauens-Anker von Anfang an.

**C · Preis-Hypothesen** (Van-Westendorp, synthetisch — nur Orientierung)

7. **Aufbau-Projekt:** optimaler Preispunkt ~**2.167 €**. Akzeptanzspanne ~**1.740–3.667 €**. Ein Fixpreis-Einstiegspaket am unteren Rand der Spanne senkt den Folgekosten-Einwand.
8. **Retainer:** optimaler Preispunkt ~**220 €/Monat**. Akzeptanzspanne ~**193–386 €/Monat**. Liegt im Rahmen kleiner Betriebsbudgets; höhere Stufen brauchen sichtbaren laufenden Nutzen.
9. ⚠️ Bei den *idealen* Preisen zeigte sich leichte LLM-Homogenisierung (Häufung um einzelne Werte). Preispunkte daher als **grobe Korridore**, nicht als exakte Zahlen lesen — vor finaler Preissetzung mit echten Angeboten/Gesprächen testen.

<sub>Generiert aus 220 synthetischen Personas · Modell claude-sonnet-4-6 · Silicon Sampling gemäß ESOMAR ICC Code 2025 · Ergebnisse sind Hypothesen.</sub>