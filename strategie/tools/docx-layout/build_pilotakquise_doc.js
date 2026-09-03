const { Paragraph, TextRun, Packer } = require("docx");
const fs = require("fs");
const path = require("path");
const L = require("./brand-layout");
const { h1, h2, h3, docTitle, metaLine, divider, callout, p, bold, italic, bullet, numbered, makeTable, buildDocument } = L;

function boldLine(label, text) {
  return p([bold(label + " "), new TextRun(text)]);
}

const children = [
  docTitle("Pilot-Akquise: die ersten echten Praxis-Cases gewinnen"),
  metaLine("Operative Vorlage. Ziel: 3–5 Pilotprojekte (gestaffelt bis Jahresende), um erste echte Fälle mit Zahlen und belastbare, namentliche Testimonials zu bekommen. Das Zeitfenster vor der offiziellen Zertifizierung ist ideal dafür — der Lehrgangsabschluss ist keine rechtliche Voraussetzung für Kunden (siehe strategie-konzept.md, Kap. 7). In Brand Voice: Sie-Form, ruhig, kein Hype."),

  callout([bold("Ausrichtung 2026-07-14: schmerz-geführt, breit akquirieren. "), new TextRun({ italics: true, color: L.MUTE, text: "Nicht auf ein Segment beschränken — angesprochen wird über den homogenen Kern-Schmerz (Termine, Nachsorge, Doku, Abrechnung) + Compliance-first (Datenschutz als Vertrauensmittel). Wer zuerst anbeißt und einen echten Case liefert, zählt. Für die aktive Ansprache trotzdem bei den Tier-1-Zielsegmenten (Physio, privatärztliche Gesundheitszentren) beginnen — dort am ehesten gewinnbar. Priorisierte Zielsegment-Landkarte: segmente.md, silicon-sampling.md." })]),
  callout([bold("Reihenfolge — kombinieren, nicht nacheinander: "), new TextRun({ italics: true, color: L.MUTE, text: "keine separate Marktumfrage-Runde (10–20 Interviews) vor der Pilot-Akquise. Die Erstgespräche mit potenziellen Pilotpraxen sind selbst schon die Marktvalidierung — gleiche 30 Minuten, gleiche Fragen zu Kernschmerz und Zahlungsbereitschaft, plus die 3 Messfragen unten. Zwei getrennte Runden kosten nur Zeit, ohne dass am Ende ein Case dabei herauskommt." })]),
  divider(),

  h1("Das Pilot-Angebot (was Sie anbieten)"),
  p("Eine kompakte KI-Potenzialanalyse plus 2–3 zusammenhängende, fertig eingerichtete Automatisierungen in einem Themenfeld (z. B. die gesamte Termin-Journey: Buchung, Erinnerung, Lückenfüllung, Recall — oder Erstanamnese + Dokumentations-Vorlage + Nachsorge) — kostenfrei oder stark vergünstigt. Im Gegenzug: ehrliches Feedback, ein Testimonial und die Einwilligung, die Praxis unter ihrem echten Namen (nicht anonymisiert) als Case zu zeigen — inklusive Zahlen."),
  bullet([bold("Für Sie: "), new TextRun("der erste echte Praxis-Fall mit mehreren Vorher/Nachher-Werten für Ihre Story Bank — ein einzelner Automatisierungs-Schritt liefert dafür zu wenig Substanz.")]),
  bullet([bold("Für die Praxis: "), new TextRun("ein spürbarer erster Hebel, ohne Risiko.")]),
  bullet([new TextRun("Klar begrenzen: „2–3 zusammenhängende Automatisierungen, ein Themenfeld, definierter Umfang“ — kein offenes Fass.")]),
  p([bold("Warum der echte Name statt Anonymisierung: "), new TextRun("Eine anonymisierte Zahl („eine Physiopraxis mit 5 Mitarbeitenden spart X Stunden“) wirkt schnell wie ein erfundenes Beispiel — genau das widerspricht der Ehrlichkeits-Regel (strategie-konzept.md, Kap. 4). Ein Case mit echtem Praxisnamen, echtem Logo (mit Einwilligung) ist der stärkere Vertrauensbeleg. Wer nicht namentlich genannt werden will, wird kein Pilot-Case — dann eignet sich die Praxis für ein reguläres, bezahltes Projekt ohne Case-Study-Verpflichtung.")]),
  p([bold("Wen ansprechen: "), new TextRun("breit — jede kleine Gesundheitspraxis mit dem Kern-Schmerz, Schwerpunkt aber auf Tier 1 (Physio/Therapiepraxen, privatärztliche Gesundheitszentren), weil dort am ehesten gewinnbar (siehe segmente.md). Idealerweise aus dem eigenen Netzwerk, sonst DACH-weit remote. Persönliche Einführung schlägt Kaltakquise. "), new TextRun({ italics: true, color: L.MUTE, text: "(Kein Wien-Fokus — Leonie arbeitet remote und ist nicht durchgehend in Österreich; „lokal“ heißt hier „übers Netzwerk gefunden“, nicht „vor Ort“.)" })]),
  divider(),

  h1("Anschreiben-Vorlage (E-Mail / LinkedIn-DM)"),
  callout([bold("Betreff: "), new TextRun("Kurzer Vorschlag für Ihre Praxis — KI-Pilot, ehrlich gerechnet")]),
  callout("Guten Tag Frau [Name],"),
  callout("ich baue gerade meine Arbeit als KI- & Business-Consultant gezielt für Praxen im Bereich Gesundheit und Wohlbefinden auf — und suche dafür eine Praxis für ein Pilotprojekt."),
  callout([bold("Konkret: "), new TextRun("Ich schaue mir mit Ihnen an, wo im Praxisalltag Zeit verloren geht, und richte die ersten zusammenhängenden Automatisierungs-Schritte fertig ein — datenschutzkonform. Für Sie kostenfrei; im Gegenzug würde ich mir Ihr ehrliches Feedback und — wenn es Ihnen etwas gebracht hat — ein kurzes Testimonial wünschen.")]),
  callout("Kein „KI macht alles über Nacht“ — ich fange bei Ihren Abläufen an, nicht beim Tool. Hätten Sie in den nächsten zwei Wochen 30 Minuten für ein erstes Gespräch?"),
  callout("Herzliche Grüße"),
  callout("Leonie Kaiser"),
  p([new TextRun({ italics: true, color: L.MUTE, text: "(Segment-Twist je Ansprache: Physio/Therapie → „zwischen Behandlungen, Terminen und Nachsorge“; Longevity → „zwischen Erstgesprächen, Laborwerten und Kundenreise“.)" })]),
  divider(),

  h1("Zusätzliche Fragen im Erstgespräch (Marktforschung nebenbei, keine separate Umfrage)"),
  p("Keine separate Marktumfrage — aber jedes Erstgespräch mit einem echten Interessenten ist eine Gelegenheit, über die Pflichtfelder des Potenzialanalyse-Tools hinaus ein paar Fragen zu stellen, die den Service verbessern und die Zielgruppe schärfer kennenlernen. Das Tool selbst erhebt bereits: Betrieb (Größe, Typ), Digitalisierungsstufe, Ziele, Engpässe, Quick Wins. Ergänzend im Gespräch (mündlich, nicht im Tool):"),
  bullet([new TextRun("„Wie haben Sie versucht, das bisher zu lösen — was haben Sie schon probiert, und woran ist es gescheitert?“ (zeigt echte Alternativen/Konkurrenz, nicht nur den Status quo)")]),
  bullet([new TextRun("„Was hätte Sie bisher davon abgehalten, so etwas umzusetzen?“ (Zeit, Geld, Vertrauen, Unklarheit was „KI“ überhaupt bedeutet — hilft, echte Kaufhürden statt vermuteter zu kennen)")]),
  bullet([new TextRun("„Wie sind Sie auf mich aufmerksam geworden?“ (Kanal-Tracking — welche Akquise-Kanäle wirklich funktionieren)")]),
  bullet([new TextRun("„Wer wäre außer Ihnen noch an so einer Entscheidung beteiligt?“ (Buy-in-Struktur — besonders relevant bei Gemeinschaftspraxen mit mehreren Partner:innen)")]),
  bullet([new TextRun("„Wenn es funktioniert, wie zufrieden wären Sie, wenn Sie X Stunden pro Woche zurückbekommen — was wäre Ihnen das wert?“ (informelle Preis-Sondierung, ergänzt die Van-Westendorp-Werte aus der Studie mit echten Reaktionen)")]),
  p([new TextRun({ italics: true, color: L.MUTE, text: "(Hinweis zum Tool selbst: Die Betriebstyp-Auswahl in static/analyse/index.html enthält noch „Ästhetische Praxis“, „Personal-Training/Fitness-Studio“ und „Ernährungsberatung“ — das gehört in den Scope der Website-Session; dort ansprechen, falls die Liste auf die jetzt 2 Start-Segmente angepasst werden soll.)" })]),
  divider(),

  h1("Welche Daten erhoben werden (für die Case Study)"),
  h3("Vor dem Projekt (Ausgangswert, im Erstgespräch erfragen)"),
  numbered([new TextRun("„Wie viele Stunden pro Woche kostet Sie das Organisatorische aktuell — Termine, Abrechnung, Nachfassen, Doku?“")]),
  numbered([new TextRun("Kurzbeschreibung der Ausgangssituation in eigenen Worten (wird zur „Situation“ im Case-Study-Aufbau).")]),
  numbered([new TextRun("Praxis-Eckdaten für den Case: Name, Ort/Segment, Anzahl Mitarbeitende, Website/Social (mit Einwilligung, siehe unten).")]),
  h3("Nach dem Projekt (Wirkung, ~2–4 Wochen nach Umsetzung erfragen)"),
  numbered([new TextRun("„Wie viele Stunden pro Woche sind es jetzt — und welche Aufgaben laufen automatisch?“")]),
  numbered([new TextRun("„Nach wie vielen Tagen war die erste spürbare Entlastung da?“")]),
  numbered([new TextRun("Ein kurzes O-Ton-Zitat der Praxisleitung (2–3 Sätze, wörtlich).")]),
  numbered([new TextRun("Optional, falls vorhanden und aussagekräftig: ein Vorher/Nachher-Screenshot des betroffenen Ablaufs (z. B. Kalenderansicht, Vorlagen-Ordner) — nur mit Einwilligung und ohne Patienten-/Kundendaten im Bild.")]),
  p([new TextRun("→ Werte direkt in den "), bold("Testimonial- & Wirkungs-Tracker"), new TextRun(" eintragen (Fall-Typ: Ziel-Segment). Nach ~5 solchen Fällen haben Sie eigene Durchschnittswerte, die Sie zitieren dürfen.")]),
  divider(),

  h1("Welche Einwilligung Sie brauchen"),
  p("Vor der Veröffentlichung eines Cases schriftlich (E-Mail reicht, kein Notar nötig) bestätigen lassen — kurzer Text, den die Praxisleitung per Antwort-Mail freigibt:"),
  callout("„Ich bin einverstanden, dass Leonie Kaiser · KI & Digitalisierung die Zusammenarbeit mit [Praxisname] als Case Study auf Website, LinkedIn und Google Business Profile veröffentlicht — inklusive Praxisname, Ort, genannter Kennzahlen und des folgenden Zitats: „[Zitat]“. Diese Einwilligung gilt bis auf Widerruf.“"),
  bullet([bold("Was die Einwilligung konkret abdeckt: "), new TextRun("Praxisname + Logo (falls verwendet) · die genannten Vorher/Nachher-Zahlen · das Zitat · ggf. Screenshot.")]),
  bullet([bold("Was NICHT gebraucht wird: "), new TextRun("keine Patienten-/Kundendaten der Praxis selbst — die Case Study zeigt nur die Zusammenarbeit mit der Praxisleitung, nie Gesundheitsdaten von deren Kundschaft.")]),
  bullet([bold("Widerrufsrecht "), new TextRun("ausdrücklich zusichern — schafft Vertrauen und ist bei personenbezogenen Daten (auch Praxisnamen als Unternehmensdaten) ohnehin sauberer Stil.")]),
  divider(),

  h1("Case-Study-Aufbau: Situation → Konflikt → Lösung → Beweis"),
  p("Fertige Struktur zum Befüllen pro Pilot-Fall:"),
  numbered([bold("Situation: "), new TextRun("Wer ist die Praxis (Name, Segment, Größe), was macht sie besonders?")]),
  numbered([bold("Konflikt: "), new TextRun("Welcher der 5 Kern-Schmerzen (Termin-Engpass, Doku, Nachsorge, Flaschenhals-Leitung, Datenschutz-Sorge) war hier konkret spürbar — mit der Ausgangszahl aus Messfrage 1.")]),
  numbered([bold("Lösung: "), new TextRun("Was wurde konkret eingerichtet, in wie vielen Tagen, wie wurde das Team eingewiesen.")]),
  numbered([bold("Beweis: "), new TextRun("Die Wirkung aus Messfragen 4–5, plus das O-Ton-Zitat. Kurz, konkret, nachprüfbar — keine gerundeten Marketing-Superlative.")]),
  p("→ Landet unter echtem Praxisnamen in brand_data.md / story_bank.md und ersetzt dort Schritt für Schritt die bisherigen Fundament-Belege (frühere, nicht-KI-bezogene Testimonials) durch echte KI-Referenzen."),
  divider(),

  metaLine("Brand Voice: AGENTS.md. Haltung: brand_position.md. Metriken/Story Bank: brand_data.md."),
];

const doc = buildDocument(children, "Pilot-Akquise-Strategie · Vertraulich, nur intern");

const outDir = path.join(__dirname, "output");
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync(path.join(outDir, "Pilot-Akquise-Strategie.docx"), buffer);
  console.log("done: output/Pilot-Akquise-Strategie.docx");
});
