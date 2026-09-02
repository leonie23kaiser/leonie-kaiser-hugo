const { Paragraph, TextRun, Packer } = require("docx");
const fs = require("fs");
const path = require("path");
const L = require("./brand-layout");
const { h1, h2, h3, docTitle, divider, callout, p, bold, italic, bullet, numbered, makeTable, buildDocument } = L;

function boldLine(label, text) {
  return p([bold(label + " "), new TextRun(text)]);
}

const children = [
  docTitle("Netzwerk-Strategie: Aufbau & Nutzung (LinkedIn, Facebook, Events)"),
  boldLine("Stand:", "2026-07-23"),
  boldLine("Vertraulich:", "nur für den internen Gebrauch."),
  boldLine("Ergänzt:", "linkedin-kundentargetierung.md (Track-B-Netzwerk-Kartierung, Reconnect-Vorlagen, Content-Plan). Dieses Dokument ist die übergeordnete Netzwerk-Strategie über alle Kanäle."),
  boldLine("Basis:", "Slides „The Three Forms of Networking“ / Connector-Theorie / Networking-Test / Maintenance & Harvesting / LinkedIn-KPI-Analyse, plus Zeitbudget (3–4 Std./Woche) und bestehende Netzwerke (WKÖ-Fachgruppe, EPU-Netzwerk NÖ)."),
  divider(),

  h1("1. LinkedIn-Profil-Audit"),
  p([bold("Update: "), new TextRun("Audit auf Basis des tatsächlichen Profil-Exports (PDF) und der Screenshots — nicht mehr nur der öffentlichen Such-Indexierung. Headline und Über-mich-Text wurden bereits überarbeitet, deutlich besser als der ursprüngliche Stand.")]),

  makeTable([2200, 3000, 4880], [
    ["Checkpunkt", "Status", "Bewertung"],
    ["Individualisierte URL", "linkedin.com/in/leoniekaiser", "Sehr gut — nichts zu tun."],
    ["Headline", "„KI & Digitalisierung für kleine Praxen in Gesundheit & Wohlbefinden | Mehr Zeit fürs Kerngeschäft – EU AI Act & DSGVO konform umgesetzt“", "Deutlich besser als vorher — deutsche Keywords, beide Kern-Themen (Gesundheitspraxen, Compliance), passt zur Website. Bewusst Track-A-fokussiert, kein Track-B-Keyword — das ist hier richtig so."],
    ["Banner-Bild", "Lila-blaues Banner mit Text „KI & Digitalisierung für kleine Privatpraxen · Gesundheit & Wohlbefinden … einfach und datenschutzkonform umgesetzt“", "Verstärkt die Headline visuell. Farben grob im violett/teal-Bereich der Brand-Tokens — bei Gelegenheit gegen die exakten Hex-Werte aus params.toml prüfen, nicht dringend."],
    ["Profilbild", "Rund, mit dekorativem Rahmen „CONSCIOUS CONSULTANT · CERTIFIED“", "Der Rahmen wirkt eher wie aus einer Coaching-/Community-Ästhetik und erklärt sich für Track-B-Betrachter:innen (Pharma-QM/RA) nicht selbst. Entfernen oder gegen ein schlichtes Portrait ohne Rahmen tauschen wäre die Empfehlung, muss aber nicht sofort passieren."],
    ["Standort (Hauptprofil)", "Felixdorf, Niederösterreich, Österreich", "Das ist tatsächlich schon korrekt nach der eigenen SEO-Regel „kein Wien“ aus AGENTS.md — bitte nicht auf Wien ändern (siehe Kap. 1a)."],
    ["Firma", "Leonie Kaiser Consulting", "Weiterhin zu prüfen: „Consulting“ im Firmennamen jetzt schon zu führen, könnte mit der Gewerbe-Abgrenzung kollidieren (aktuell freies Gewerbe „KI & Digitalisierung“, „Consulting“ offiziell erst ab November 2026). Mit WKÖ/Gewerbe-Auskunft absichern."],
    ["Über-mich-Text", "Vollständig, Sie-Form, nennt EU AI Act/DSGVO, Ehrlichkeits-Punkt, Track-B-Laufbahn (Merck Healthcare, AbbVie, Baxter), CTA mit Calendly-Link", "Inhaltlich sehr stark und exakt auf Markenstimme. Technisches Detail: im PDF-Export laufen mehrere Sätze ohne Leerzeichen ineinander (z. B. „geht.Termine“, „Menschen.Wie“). Bitte live auf LinkedIn prüfen, ob das dort auch so aussieht — falls ja, Absätze/Leerzeichen nachziehen."],
    ["Top-Kenntnisse (erste 3)", "KI-Verordnung, Datenschutz-Grundverordnung (DSGVO), Digitale Transformation", "Gute, konkrete Keywords — „KI-Verordnung“ ist die korrekte deutsche Bezeichnung für EU AI Act, besser als ein Anglizismus."],
    ["Sprachen", "Deutsch (Muttersprache), Englisch (verhandlungssicher), Spanisch (gute Kenntnisse)", "Deckt die „Mehrsprachig“-Differenzierung aus AGENTS.md Kap. 11 ab."],
    ["Berufserfahrung", "Vollständig — Leonie Kaiser Consulting, Merck Group (2 Rollen), AbbVie, KED Pharmaceuticals, Baxter Innovations (2 Rollen)", "Komplett und lückenlos, zeigt durchgehend ~13 Jahre reguliertes Pharma-/Medtech-Umfeld (2005–2018) — genau die Track-B-Glaubwürdigkeit für die Reconnect-Strategie."],
    ["Ausbildung", "Lighthouse Business Academy, MSMK Madrid, FH Wiener Neustadt", "Vollständig."],
    ["Alte Aktivität", "Ein Post von 2023 mit Zusatz „Soulful Simplicity in Business“ taucht noch auf", "Nicht dringend, Featured-Bereich bei Gelegenheit prüfen."],
  ]),

  h2("1a. Wichtig: Standort vs. Kontaktinformationen sind zwei verschiedene Felder"),
  p("Das erklärt, warum eine Änderung nicht sofort überall ankommt: LinkedIn hat zwei getrennte Orts-Felder, die nichts miteinander zu tun haben."),
  numbered([bold("1. Haupt-Standort "), new TextRun("(steht direkt unter dem Namen/der Headline, z. B. „Felixdorf, Niederösterreich, Österreich“) — wird bearbeitet über „Profil bearbeiten“ (Stift-Symbol oben im Profilbereich), nicht über die Kontaktinformationen.")]),
  numbered([bold("2. Kontaktinformationen → Adresse "), new TextRun("— ein eigenständiges Feld, nur über den Link „Kontaktinformationen“ sichtbar, wird über einen anderen Dialog bearbeitet.")]),
  callout([bold("Wichtiger als die technische Lösung: "), new TextRun({ italics: true, color: L.MUTE, text: "Nach der eigenen SEO-Regel aus AGENTS.md („kein Wien in Marketing-Texten, stattdessen Niederösterreich/DACH — sonst suggeriert es fälschlich „vor Ort in Wien“) sollte keines der beiden Felder auf Wien stehen. Empfehlung: beide Felder auf „Niederösterreich / Österreich“ bzw. „ortsunabhängig, DACH-weit“ konsistent halten." })]),
  divider(),

  h1("2. Die drei Formen des Networking — auf die zwei Tracks gemappt"),
  p("Operational (aktuelle Arbeit effizient erledigen), Personal (Weiterentwicklung, Empfehlungen), Strategic (zukünftige Prioritäten, Unterstützung von innen und außen verschaffen). Die meisten betreiben nur die ersten beiden — der Hebel liegt im dritten."),
  makeTable([1600, 2680, 5800], [
    ["Form", "Zweck", "Konkret"],
    ["Operational", "Aktuelle Arbeit unterstützen", "WKÖ-Fachgruppe, EPU-Netzwerk NÖ: Wissen zu Gewerbe-/Praxisfragen, die das Tagesgeschäft direkt betreffen."],
    ["Personal", "Eigene Entwicklung, Empfehlungen erhalten", "Alumni des KI-Consulting-Lehrgangs, Women in AI Österreich: Peer-Austausch, Sichtbarkeit in der KI-Berater-Community, Empfehlungen unter Kolleginnen."],
    ["Strategic", "Zukünftige Prioritäten + Unterstützung von innen und außen", "Die Verbindung zwischen zwei Welten, die sonst nichts miteinander zu tun haben: Pharma-/Medtech-Compliance-Welt (Track B) und Gesundheitspraxen-Welt (Track A). Das ist die „Leverage: Creating Inside-Outside Links“-Rolle."],
  ]),
  p([bold("Konsequenz: "), new TextRun("Die meisten Berater:innen pflegen nur Personal Networking. Der größte ungenutzte Vorteil liegt in der strukturellen Position zwischen zwei Welten — die Strategie ist bewusst darauf ausgelegt, das aktiv zu nutzen statt es dem Zufall zu überlassen.")]),
  divider(),

  h1("3. Kanäle im Überblick"),
  h2("3.1 LinkedIn — Strategic Networking, Kern für Track B"),
  p("Bereits im Detail geplant in linkedin-kundentargetierung.md (Reconnect-Vorlagen, Content-Plan, Startsequenz). Ergänzend hier die Social-Selling-Index-Logik (SSI) als laufender Kompass:"),
  numbered([bold("1. Professionelle Marke etablieren "), new TextRun("→ Profil-Überarbeitung (Kap. 1) + wöchentliche Fach-Posts")]),
  numbered([bold("2. Die richtigen Menschen finden "), new TextRun("→ Track-B-Kartierung + LinkedIn-Suche nach „Ähnliche Profile“ bei bereits identifizierten QM/RA-Kontakten")]),
  numbered([bold("3. Mit Insights interagieren "), new TextRun("→ auf Beiträge von Tier-1/2-Kontakten kommentieren, bevor sie angeschrieben werden (Vorwärmung, günstiger als Kaltansprache)")]),
  numbered([bold("4. Beziehungen aufbauen "), new TextRun("→ Reconnect-Sequenz aus linkedin-kundentargetierung.md, Kapitel 2 „Reconnect ohne Pitch — Nachrichten-Vorlagen“ (Vorlagen A/B/C + „Der leichte Weg vom Reconnect zum fachlichen Gespräch“)")]),
  h3("Konkrete Profil-Checkliste — Stand nach Audit (Kap. 1)"),
  bullet("Kurzbeschreibung mit Kernkompetenz-Keywords — vorhanden und stark"),
  bullet("Skills: aktuell 3 sichtbar (KI-Verordnung, DSGVO, Digitale Transformation) — auf 5 ausbauen, z. B. um „Gesundheitspraxen“ und „Pharma-Compliance“ ergänzen"),
  bullet("Berufserfahrung & Ausbildung — vollständig, inkl. Pharma-/Medtech-Laufbahn"),
  bullet("Empfehlungen (Recommendations) von früheren Kolleg:innen/Kund:innen einholen — noch offen, passt gut in die Reconnect-Gespräche aus Track B"),
  bullet("Gruppen: den beiden genannten beitreten (siehe 3.3)"),

  h2("3.2 Facebook — Vorschlag: Track A, lokal/persönlich, nicht strategisch"),
  p([bold("Rolle: "), new TextRun("Facebook eignet sich für Track A deutlich besser als für Track B. Die Zielgruppe dort — kleine, inhabergeführte Gesundheitspraxen — ist auf Facebook eher vertreten als Pharma-QM-Entscheider:innen, die praktisch ausschließlich auf LinkedIn unterwegs sind. Facebook wird zum lokalen/regionalen Sichtbarkeits-Kanal, nicht zum zweiten LinkedIn.")]),
  bullet("Gruppen-Beitritt statt eigene Seite zuerst: regionale niederösterreichische Unternehmerinnen-/Gesundheits-Netzwerke suchen (z. B. „Unternehmerinnen Niederösterreich“, regionale WKÖ-Gruppen, Physio-/Wellness-Praxis-Gruppen AT). Eine eigene Unternehmensseite lohnt sich erst mit vorhandener Reichweite."),
  bullet("Andere Tonalität als LinkedIn: weniger fachlich-tief, mehr persönlich/nahbar — passt zur „Martina“-Zielgruppe, die eher über Vertrauen und Sympathie entscheidet."),
  bullet("Cross-Posting-Logik: Cross-Posten heißt nicht 1:1 kopieren, sondern denselben Kerninhalt für den jeweiligen Kanal anders formulieren — den LinkedIn-Post persönlicher/nahbarer für Facebook umschreiben, statt für jeden Kanal ein komplett neues Thema zu entwickeln."),
  bullet("Kein Facebook für Track B: dort bleibt LinkedIn der einzige relevante Kanal, das spart Aufwand."),

  h2("3.3 Vor Ort — Events & Verbände (Personal + Strategic Networking)"),
  callout([bold("Rein internes Planungsinstrument — keine öffentliche Verfügbarkeits-Zusage. "), new TextRun({ italics: true, color: L.MUTE, text: "Diese Vor-Ort-Planung dient ausschließlich dem eigenen Netzwerkaufbau (Verbände, Peers, Track-B-Reconnects) und widerspricht nicht der nach außen kommunizierten Positionierung „remote, kein Vor-Ort-Service im Standardangebot“ (siehe AGENTS.md Kap. 11). Nach außen wird das nicht als Verfügbarkeit beworben — persönliche Treffen ergeben sich situativ aus dieser internen Planung, sie werden nicht vorab angeboten." })]),
  p("Vor-Ort-Networking ist kein Rand-/Ausnahmefall, sondern ein aktiv geplanter, gleichwertiger zweiter Pfeiler neben LinkedIn und Facebook — EPU-Netzwerk-, KI-Vortrags- und WKÖ-Veranstaltungen in NÖ/Wien. Die Gesamtstrategie deckt damit zwei Ebenen ab: soziale Medien (LinkedIn, Facebook) und Vor-Ort-AT (planbar, regelmäßig)."),
  h3("AT — planbar, regelmäßig"),
  bullet([bold("WKÖ-Fachgruppe (bestehend): "), new TextRun("Aktiv Veranstaltungen besuchen statt nur Mitgliedschaft halten. Guter Ort für Track A (andere Gewerbetreibende mit Praxen als Kundschaft — Multiplikatoren-Potenzial ähnlich der Steuerberatungs-Idee).")]),
  bullet([bold("EPU-Netzwerk NÖ (bestehend): "), new TextRun("Gleiche Logik — regelmäßige Teilnahme statt passive Mitgliedschaft. Oft branchenübergreifend, gut für „Strategic Networking“ — bewusst Menschen zusammenbringen, die sich sonst nicht kennen würden.")]),
  bullet([bold("KI-Vorträge/-Events Wien/NÖ: "), new TextRun("Allgemeine KI-Vortrags- und Meetup-Szene — guter Ort sowohl für Track-A-Sichtbarkeit (als Rednerin/Teilnehmerin) als auch für Track-B-Zufallstreffer (Pharma-/Medtech-Leute mit KI-Interesse sind dort überproportional vertreten).")]),
  p("Kategorien, nach denen konkret gesucht werden kann (bewusst als Kategorien statt geratener Namen, da sich Formate/Termine laufend ändern — selbst aktuell recherchieren):"),
  numbered([bold("1. Meetup-/Eventbrite-Gruppen "), new TextRun("mit Filter „AI“ / „KI“ / „Machine Learning“ / „Digitalisierung“, Standort Wien")]),
  numbered([bold("2. WKÖ-eigene Digitalisierungs-/KI-Veranstaltungsreihen "), new TextRun("— oft über die Landesgeschäftsstelle NÖ oder eigene Digital-Ausschüsse innerhalb von Fachgruppen, unabhängig von der eigenen Fachgruppe")]),
  numbered([bold("3. Coworking-Spaces mit offenem Event-Programm "), new TextRun("— viele Wiener Coworking-Spaces veranstalten regelmäßig Tech-/KI-Talks, oft auch für Nicht-Mitglieder")]),
  numbered([bold("4. Offene universitäre Vortragsreihen "), new TextRun("— Gastvorträge zu KI-Themen an TU Wien, WU Wien oder FH-Standorten in NÖ")]),
  numbered([bold("5. Digital-/Tech-Konferenzen mit Networking-Teil "), new TextRun("— gezielt auf den Networking-Teil statt nur das Programm achten")]),
  numbered([bold("6. Xing-Lokalgruppen "), new TextRun("— in AT/DE teils noch parallel zu LinkedIn für regionale Business-Events relevant")]),
  numbered([bold("7. Frauennetzwerke im Tech-/Digitalbereich "), new TextRun("über Women in AI hinaus — z. B. lokale Chapter internationaler Frauen-in-Tech-Communities")]),
  h3("Digital ergänzend"),
  bullet([bold("Women in AI Österreich: "), new TextRun("Sinnvoll — Sichtbarkeit in der KI-Community, außerdem teils Entscheiderinnen aus Unternehmen, die für Track B relevant sein können. Profil dort mit der gleichen Positionierung wie auf LinkedIn füllen. Auch hier auf Vor-Ort-Termine (Meetups, Stammtische) achten, nicht nur als Online-Community nutzen.")]),
  bullet([bold("KI Beraterportal / gründer.de: "), new TextRun("Eher ein Verzeichnis-/Sichtbarkeits-Tool als ein Networking-Ort im engeren Sinn — gut für GEO/Auffindbarkeit. Eintrag anlegen, aber keine zusätzliche Pflegezeit einplanen.")]),
  bullet([bold("LinkedIn-Gruppen: "), new TextRun("thematisch zu EU AI Act/DSGVO im Mittelstand, KI-Consulting-DACH, sowie Pharma-/Life-Science-Gruppen für Track B — dort mitlesen und gelegentlich kommentieren, nicht selbst posten.")]),

  h2("3.4 Vor-Ort-Kalender 2026"),
  p("Kein durchgehender AT-Aufenthalt, sondern Blöcke — dazwischen nicht vor Ort. Die Vor-Ort-Aktivität bündelt sich deshalb gezielt in den tatsächlichen AT-Fenstern statt auf einen künstlichen „1 Event pro Monat“-Rhythmus zu setzen. Dazwischen läuft nur die digitale Schiene normal weiter."),
  makeTable([2600, 1680, 5800], [
    ["Zeitraum", "Status", "Fokus"],
    ["Jetzt (Ende Juli) – 12.08.", "Nicht in AT", "Digitale Schiene läuft normal (Kap. 4). Für den Block ab 13.08. schon jetzt 1–2 Termine anfragen — bei reagierenden Track-B-Reconnects gezielt „Ich bin ab 13. August wieder in Österreich, hätten Sie da Zeit für einen Kaffee?“ anbieten."],
    ["13.08. – 04.09. (≈ 3 Wochen)", "In AT — Präsenzblock 1", "Ziel: 2–3 persönliche Treffen (Mix Track A/B/Multiplikator) + 1–2 Vor-Ort-Termine (WKÖ, EPU oder KI-Event). Termine vor Anreise fixieren, nicht vor Ort improvisieren."],
    ["05.09. – Ende September", "Nicht in AT", "Digitale Schiene weiter, Nachbereitung Block 1 (Kontakt-Tabelle aktualisieren), Vorbereitung Block 2."],
    ["Anfang Okt. – Mitte Nov. (≈ 6 Wochen)", "In AT — Präsenzblock 2, größtes Fenster", "Mehr Kapazität als Block 1: mehrere Events, mehr Treffen. Bester Moment für die erste bewusste „Vorstellung“ zwischen zwei Kontakten."],
    ["Mitte Nov. – Ende Nov.", "Nicht in AT", "Digitale Schiene, Nachbereitung Block 2."],
    ["Dezember", "In AT — Präsenzblock 3", "Kürzeres Fenster, oft Jahresabschluss-Termine bei Verbänden — nachfragen. Guter Zeitpunkt für Jahresrückblick in der Kontakt-Tabelle."],
  ]),
  p([bold("Praktische Konsequenz für die Reconnect-Nachrichten: "), new TextRun("Bei Track-B-Kontakten in Wien/NÖ lohnt es sich, in der Nachricht direkt auf einen konkreten Präsenzblock Bezug zu nehmen, statt allgemein „mal wieder treffen“ zu schreiben — das macht aus einer vagen Absicht einen konkreten Termin.")]),
  divider(),

  h1("4. Maintenance & Harvesting — das Networking-System"),
  p("Pflege ist kein Zufall, sondern ein System. Bei 3–4 Std./Woche Budget realistisch aufgeteilt."),
  h2("Kontakt-Tracking (Tabelle, z. B. Google Sheet oder Notion — kein separates CRM-Tool nötig)"),
  makeTable([2800, 7280], [
    ["Spalte", "Inhalt"],
    ["Name", "—"],
    ["Segment", "Track A / Track B / Multiplikator / Connector / Peer"],
    ["Letzter Kontakt — Datum", "Datum des letzten Kontakts"],
    ["Letzter Kontakt — Art", "z. B. Reconnect-Nachricht, Kommentar auf Post, Call, Event-Treffen"],
    ["Was ich anbieten kann", "z. B. Fachartikel, Vorstellung an X"],
    ["Nächster Schritt", "z. B. „in 3 Monaten nachfassen“"],
    ["Notiz", "gemeinsame Interessen, private Themen (Hochzeit, Jobwechsel etc.)"],
  ]),
  h2("Wöchentliche Routine (3–4 Std.)"),
  bullet("~1 Std. LinkedIn: 1 Post veröffentlichen + 15–20 Min. gezieltes Kommentieren bei Zielkontakten"),
  bullet("~30 Min. Facebook: 1 Cross-Post + Gruppen-Mitlesen"),
  bullet("~1 Std. Reconnect-/Nachfass-Nachrichten (aus der Kontakt-Tabelle: wer ist „fällig“?)"),
  bullet("~1–1,5 Std. ein persönlicher Kontaktpunkt pro Woche — abwechselnd Track A, Track B, Multiplikator, reiner Personal-Contact ohne Agenda. Format richtet sich danach, was gerade ansteht: persönliches Treffen (Kaffee/Lunch/Event), wenn ohnehin vor Ort in Wien/NÖ und die Person dort sitzt — aktiv einplanen, nicht dem Zufall überlassen; Video-/Telefon-Call, wenn kein Vor-Ort-Zusammentreffen ansteht."),
  h2("Bezogen auf die AT-Präsenzblöcke (statt starrem Monats-Rhythmus, siehe Kap. 3.4)"),
  bullet("Innerhalb jedes AT-Präsenzblocks: mindestens 1–2 Vor-Ort-Termine plus 2–3 persönliche Treffen mit Netzwerkkontakten"),
  bullet("Zwischen den Blöcken: Kontakt-Tabelle durchgehen, wer seit über 3 Monaten still ist — kurze „Denk an dich“-Nachricht, sowie Termine für den nächsten Block vorbereiten"),
  bullet("Bewusst eine Vorstellung machen — zwei Menschen aus dem Netzwerk zusammenbringen, die sich noch nicht kennen, aber voneinander profitieren könnten. Ein AT-Präsenzblock ist dafür der ideale Moment."),
  divider(),

  h1("5. Fahrplan bis Jahresende — integriert über alle Kanäle"),
  p("Folgt dem tatsächlichen Kalender (Kap. 3.4) statt einer abstrakten Wochen-Zählung. Digitale Schritte (LinkedIn, Facebook, Reconnects) laufen durchgehend unabhängig vom Standort; die Vor-Ort-Schritte sind an die drei Präsenzblöcke gebunden."),
  h2("Jetzt – 12.08. (Remote-Phase, vor Block 1)"),
  bullet("LinkedIn-Profil-Feinschliff: Standort-Verwechslung klären (Kap. 1a), Profilbild-Rahmen prüfen, Über-mich-Formatierung live checken"),
  bullet("Bei Women in AI Österreich und KI Beraterportal Profil anlegen"),
  bullet("2–3 passende Facebook-Gruppen suchen und beitreten"),
  bullet("Track-B-Reconnects an die identifizierten Tier-1-/Tier-2-Kontakte starten (siehe linkedin-kundentargetierung.md)"),
  bullet("Für Block 1 vorbereiten: 2–3 Termine mit Kontakten in Wien/NÖ anfragen, 1–2 Veranstaltungen aus Kap. 3.3 recherchieren und fixieren"),
  h2("13.08. – 04.09. (Präsenzblock 1)"),
  bullet("Vorbereitete Termine wahrnehmen: mindestens 2–3 persönliche Treffen, mindestens 1 Vor-Ort-Event/Verbandstermin"),
  bullet("Bei jedem Termin gezielt auch neue Menschen ansprechen, nicht nur bekannte Gesichter"),
  bullet("Direkt im Anschluss an jeden Termin: Kontakt-Tabelle (Kap. 4) aktualisieren, solange der Eindruck noch frisch ist"),
  h2("05.09. – Ende September (Remote-Phase)"),
  bullet("Facebook: erste eigene Beiträge (Cross-Posts aus LinkedIn-Content, Track-A-Ton)"),
  bullet("Nachbereitung Block 1 abschließen, Vorbereitung Block 2 beginnen"),
  h2("Anfang Okt. – Mitte Nov. (Präsenzblock 2 — größtes Fenster)"),
  bullet("Mehrere Vor-Ort-Termine und Events, mehr Kapazität als Block 1"),
  bullet("Erste bewusste „Vorstellung“ zwischen zwei Netzwerk-Kontakten versuchen — ideal direkt bei einem Termin"),
  bullet("Auswertung zwischendurch: Welche Kanäle bringen tatsächlich Gespräche — LinkedIn, Facebook oder Vor-Ort? Zeit entsprechend nachjustieren."),
  h2("Mitte Nov. – Ende Nov. (Remote-Phase)"),
  bullet("Prüfen, wer im Netzwerk selbst als Connector auffällt (viele Verbindungen, kennt viele Welten) — gezielt pflegen"),
  bullet("Vorbereitung Präsenzblock 3"),
  h2("Dezember (Präsenzblock 3)"),
  bullet("Jahresabschluss-Termine der Verbände mitnehmen, falls vorhanden (nachfragen, siehe Kap. 3.4)"),
  bullet("Kontakt-Tabelle: erste 3-Monats-Nachfass-Runde bei allen, die seit Sommer still waren"),
  bullet("Kurzer Jahresrückblick: was hat über die drei Präsenzblöcke tatsächlich funktioniert, was für 2027 anpassen"),

  callout([italic("Nächster Schritt: Standort-Feld klären (Kap. 1a), Profilbild-Rahmen entscheiden, Über-mich-Formatierung live auf LinkedIn prüfen, Skills auf 5 ausbauen — dann ist Kap. 1 abgeschlossen.")]),
];

const doc = buildDocument(children, "Netzwerk-Strategie · Vertraulich, nur intern");

const outDir = path.join(__dirname, "output");
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync(path.join(outDir, "Netzwerk-Strategie.docx"), buffer);
  console.log("done: output/Netzwerk-Strategie.docx");
});
