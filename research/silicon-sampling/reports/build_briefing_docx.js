const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, VerticalAlign,
  NumberFormat, LevelFormat } = require('docx');
const fs = require('fs');

const TEAL = "086584", TEAL6 = "5FA2A0", GOLD = "CF982B", VIOLET = "6B2C8C",
      INK = "1D2228", MUTE = "5B6572", SOFT = "EDF7F2", LINE = "ECE3D8";

// ---- Helpers --------------------------------------------------------------
const H1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });
const H2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });
const H3 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun(t)] });
const P  = (runs, opts={}) => new Paragraph({ spacing: { after: 120, line: 276 }, ...opts,
  children: Array.isArray(runs) ? runs : [new TextRun(runs)] });
const T  = (text, o={}) => new TextRun({ text, ...o });
const bullet = (runs) => new Paragraph({ numbering: { reference: "bullets", level: 0 },
  spacing: { after: 80, line: 276 }, children: Array.isArray(runs) ? runs : [new TextRun(runs)] });
const num = (runs, ref="numbers") => new Paragraph({ numbering: { reference: ref, level: 0 },
  spacing: { after: 80, line: 276 }, children: Array.isArray(runs) ? runs : [new TextRun(runs)] });

// O-Ton (verbatim quote)
const quote = (text, tag) => new Paragraph({
  spacing: { before: 60, after: 140, line: 264 },
  indent: { left: 360 },
  border: { left: { style: BorderStyle.SINGLE, size: 18, color: TEAL6, space: 12 } },
  children: [ T("„" + text + "”  ", { italics: true, color: INK }),
              T("— " + tag, { italics: true, color: MUTE, size: 18 }) ]
});

const cell = (children, { w, head=false, fill } = {}) => new TableCell({
  width: { size: w, type: WidthType.DXA },
  shading: fill ? { fill, type: ShadingType.CLEAR } : undefined,
  borders: { top:{style:BorderStyle.SINGLE,size:1,color:LINE}, bottom:{style:BorderStyle.SINGLE,size:1,color:LINE},
             left:{style:BorderStyle.SINGLE,size:1,color:LINE}, right:{style:BorderStyle.SINGLE,size:1,color:LINE} },
  margins: { top: 90, bottom: 90, left: 130, right: 130 },
  verticalAlign: VerticalAlign.TOP,
  children: Array.isArray(children) ? children : [new Paragraph({ children:[
    new TextRun({ text: children, bold: head, color: head ? "FFFFFF" : INK }) ]})]
});

function table2(rows, w1, w2) {
  return new Table({
    width: { size: w1+w2, type: WidthType.DXA }, columnWidths: [w1, w2],
    rows: rows.map((r, i) => new TableRow({
      tableHeader: i===0,
      children: [ cell(r[0], { w: w1, head: i===0, fill: i===0 ? TEAL : (i%2? "FFFFFF":SOFT) }),
                  cell(r[1], { w: w2, head: i===0, fill: i===0 ? TEAL : (i%2? "FFFFFF":SOFT) }) ]
    }))
  });
}

const children = [];

// ---- Cover ----------------------------------------------------------------
children.push(new Paragraph({ spacing: { after: 60 }, children: [
  T("SILICON-SAMPLING-STUDIE · STRATEGIE-BRIEFING", { color: GOLD, bold: true, size: 18 }) ]}));
children.push(new Paragraph({ spacing: { after: 60 },
  children: [ T("Wie Sie kleine Gesundheits- & Wellness-Betriebe gewinnen", { bold:true, size: 44, color: TEAL }) ]}));
children.push(P([ T("Kommunikations- & Positionierungs-Leitfaden für Ihre KI-Consulting-Angebote — abgeleitet aus 220 synthetischen Personas (DACH).", { size: 24, color: MUTE }) ]));
children.push(new Paragraph({
  spacing: { before: 120, after: 120 },
  shading: { fill: "FFF7E6", type: ShadingType.CLEAR },
  border: { top:{style:BorderStyle.SINGLE,size:4,color:GOLD}, bottom:{style:BorderStyle.SINGLE,size:4,color:GOLD},
            left:{style:BorderStyle.SINGLE,size:4,color:GOLD}, right:{style:BorderStyle.SINGLE,size:4,color:GOLD} },
  children: [ T("⚠ Synthetische Daten gemäß ESOMAR ICC Code 2025. ", { bold:true, color: INK }),
    T("Befragt wurden KI-Personas, keine echten Menschen. Alle Aussagen sind Hypothesen und Sprach-Rohmaterial — keine validierten Fakten. Vor strategischen Festlegungen mit 10–20 echten Gesprächen prüfen.", { color: INK }) ]}));

// ---- 1. Auf einen Blick ---------------------------------------------------
children.push(H1("Auf einen Blick"));
children.push(bullet([ T("Konstante Auslastung ist NICHT ihr Schmerz. ", {bold:true}),
  T("Nur ~4–6 % sprechen Auslastung/freie Kapazitäten an. 72 % verbinden Wachstumssorgen mit Personal & Organisation — nicht mit fehlender Nachfrage. Viele haben Wartelisten.") ]));
children.push(bullet([ T("Der Kern-Schmerz ist „alles hängt an mir“ + Verwaltungs-Wildwuchs. ", {bold:true}),
  T("Verkaufen Sie das Ergebnis — wieder Inhaberin sein statt Lückenfüllerin — nicht „KI“.") ]));
children.push(bullet([ T("Vertrauen ist Ihr Wettbewerbsvorteil. ", {bold:true}),
  T("Datenschutz bei Gesundheitsdaten + „wer betreut das danach?“ sind die größten Bremsen. Genau hier punkten Ihre Ausbildungs-Schwerpunkte (AI-Act, Datenschutz, TÜV-Siegel, laufende Betreuung).") ]));
children.push(bullet([ T("Sprechen Sie die Inhaberin direkt an — und nehmen Sie das Team früh mit. ", {bold:true}),
  T("Entscheidung fällt intern (Inhaber:in 36 %, Team/Praxismanagement 55 %).") ]));
children.push(bullet([ T("Kein Verkaufsdruck, keine Floskeln, keine kalte Chatbot-Anmutung. ", {bold:true}),
  T("Die Personas reagieren allergisch darauf. Konkret, ehrlich, auf Augenhöhe — in der Sie-Form.") ]));

// ---- 2. Auslastung --------------------------------------------------------
children.push(H1("Ihre Frage: Kam „konstante Auslastung“ vor?"));
children.push(P([ T("Kurz: kaum — und das ist eine wichtige, ehrliche Erkenntnis. ", {bold:true}),
  T("Ein Mangel an Auslastung oder Nachfrage ist nicht der zentrale Schmerz dieser Zielgruppe. Die Zahlen aus den 220 Personas:") ]));
children.push(bullet([ T("Nur ~4 % ", {bold:true}), T("klagen über fehlenden Überblick über Auslastung/freie Kapazitäten (ein Sichtbarkeits-, kein Nachfrage-Problem).") ]));
children.push(bullet([ T("~6 % ", {bold:true}), T("nennen No-Shows/Absagen, die vorhandene Kapazität verschwenden.") ]));
children.push(bullet([ T("72 % ", {bold:true}), T("verknüpfen Wachstum/Zukunft mit Personal & Organisation — mehrere sagen ausdrücklich, sie hätten genug oder zu viel Nachfrage.") ]));
children.push(P([ T("Typische O-Töne:", {bold:true}) ]));
children.push(quote("Ich könnte wahrscheinlich mehr Umsatz machen. Wir haben eine gute Auslastung, Warteliste sogar manchmal. Aber wenn ich wachse, brauch ich mehr Personal — und Personal ist mein größtes Thema.", "P013, Personal-Training-Studio"));
children.push(quote("Der Überblick über Auslastung und freie Kapazitäten fehlt einfach. Wenn ich wissen will, wie ausgelastet Mirjam nächste Woche ist, muss ich sie persönlich fragen. Das ist 2026, das sollte nicht so sein.", "P126, Physiotherapiepraxis"));
children.push(P([ T("Empfehlung zur Ansprache: ", {bold:true}),
  T("Werben Sie nicht mit „mehr Kund:innen / volle Auslastung“ — das verfehlt den Schmerz und klingt nach Marketing-Agentur. Wenn Sie Auslastung ansprechen, dann über die echte Brücke: "),
  T("„Holen Sie mehr aus der Auslastung, die Sie ohnehin haben — keine Stunde mehr an No-Shows verlieren, jederzeit sehen, wer wann frei ist.“", {italics:true, color: TEAL}) ]));

// ---- 3. Wie Sie helfen ----------------------------------------------------
children.push(H1("Wie Sie diesen Betrieben am besten helfen"));
children.push(P([ T("Die größten Pain Points decken sich fast deckungsgleich mit den Schwerpunkten Ihrer KI-Consultant-Ausbildung. Das ist Ihr Angebots-Fundament — Sie müssen nichts erfinden, sondern nur zuordnen:") ]));
children.push(table2([
  ["Was die Betriebe quält (Häufigkeit)", "Womit Sie es lösen (aus Ihrer Ausbildung)"],
  ["Verwaltung, Bürokratie & Abrechnung — 88 %", "Modul 2 (Effizienz Kernprozesse) + Modul 3 (Automatisierung No-Code & KI-Agenten); Ihre geprüften n8n-Workflows für Verwaltung & Wissensmanagement"],
  ["Personal finden, halten, führen — 72 %", "Wissensmanagement & Onboarding-Automatisierung; dokumentierte, „gelebte“ Prozesse, die das Team entlasten"],
  ["Termine & No-Shows — 67 %", "Automatisierte Terminorganisation, Erinnerungen, Wartelisten — Modul 2/3; konkret, sofort spürbar"],
  ["Kommunikation mit Klient:innen — 60 %", "Smarte, datenschutzkonforme Kanal-Bündelung & Antwort-Workflows — ohne den persönlichen Ton zu verlieren"],
  ["„Alles hängt an mir“ — 40 %", "Ihr KI-Consulting-Workflow (Modul 1): Abläufe so aufsetzen, dass der Betrieb ohne die Inhaberin als Flaschenhals läuft"],
], 4280, 5080));
children.push(P([ T("Was die Personas sich am sehnlichsten wünschen — fast immer dasselbe Bild: ein System, das läuft, ohne dass sie der Knotenpunkt sind:") ], { spacing:{ before:160, after:80 } }));
children.push(quote("Ein Team, das eigenständig und sicher entscheiden kann — funktionierende Strukturen und Zuständigkeiten ohne mich als Flaschenhals.", "P025, Wunsch „per Zauberei“"));
children.push(quote("Terminplanung und Abrechnung laufen automatisch und sauber — ohne abendlichen Aufwand und ohne dass alles in meinem Kopf hängt.", "P143, Wunsch „per Zauberei“"));

// ---- 4. Einwände entkräften ----------------------------------------------
children.push(H1("Die 4 Zweifel, die Sie aktiv ausräumen müssen"));
children.push(P([ T("Damit diese Menschen keine Zweifel haben, dass "), T("Sie", {italics:true}),
  T(" ihnen helfen können, müssen Sie die Top-Einwände beantworten, "),
  T("bevor", {bold:true}), T(" sie gestellt werden — auf der Website und im Erstgespräch. Ihre Ausbildung liefert für jeden Einwand einen echten Beleg:") ]));
children.push(table2([
  ["Der Zweifel (O-Ton)", "Ihre Antwort — mit Beleg"],
  ["Zeitaufwand & Umstellung bleibt an mir hängen (häufigster Einwand, 56×)", "Festes, schlankes Aufbau-Projekt mit Einweisung des Teams; Sie übernehmen die Einrichtung, nicht die Inhaberin. Ergebnis-Versprechen: Zeit zurückgewinnen, nicht Zeit kosten."],
  ["Datenschutz bei sensiblen Gesundheitsdaten (45×)", "Ihr Schwerpunkt Modul 4: DSGVO, EU-AI-Act, Haftung + sichere Cloud-/On-Premise-Lösungen. Machen Sie das sichtbar — das ist Ihr stärkstes Verkaufsargument, kein Kleingedrucktes."],
  ["Versteckte Folgekosten hinter der Gratis-Analyse (39×)", "Transparente Fixpreise nennen, bevor gefragt wird. Die kostenlose Erstanalyse klar als unverbindliche Standort­bestimmung positionieren — ohne Abschlussdruck."],
  ["„Wer betreut das, wenn Sie wieder weg sind?“ (30×)", "Genau dafür der monatliche Betreuungs-Retainer — als Vertrauens-Anker von Anfang an, nicht als Zusatzverkauf. Plus: Anbindung an den KI-Beraterverbund."],
], 4280, 5080));
children.push(P([ T("Zwei weitere, leisere Sorgen — unbedingt mitdenken:") ], { spacing:{ before:160, after:80 } }));
children.push(quote("Angst vor Unpersönlichkeit durch Automatisierung — Beziehungsqualität ist unser Kernwert.", "P028, Personal-Training-Studio"));
children.push(quote("Versteht jemand Externes wirklich schnell genug, wie diese Praxis funktioniert?", "P211, Physiotherapiepraxis"));
children.push(P([ T("→ Antwort: ", {bold:true}),
  T("Betonen Sie, dass Automatisierung das Persönliche "), T("schützt", {italics:true}),
  T(" (Routine weg, mehr Zeit für Menschen) — und nutzen Sie die kostenlose Erstanalyse als echtes Zuhören, um zu zeigen, dass Sie den Betrieb verstehen, bevor Sie etwas vorschlagen.") ]));

// ---- 5. Trust-Moat / Credentials -----------------------------------------
children.push(H1("Ihr Vertrauens-Vorsprung: zeigen, nicht verstecken"));
children.push(P([ T("Bei sensiblen Gesundheitsdaten kauft niemand von jemandem, dem er nicht vertraut. Ihre Ausbildung gibt Ihnen genau die Belege, die diese Zielgruppe sucht. Platzieren Sie sie sichtbar:") ]));
children.push(bullet([ T("TÜV-Rheinland-geprüftes Zertifikat", {bold:true}), T(" — externes Gütesiegel, das Seriosität signalisiert.") ]));
children.push(bullet([ T("KI-Kompetenz nach EU-AI-Act (Art. 4)", {bold:true}), T(" — Sie sprechen die Sprache der Regulierung, die genau ihre Datenschutz-Angst adressiert.") ]));
children.push(bullet([ T("Datenschutz-/Recht-Spezialisierung (Modul 4)", {bold:true}), T(" — machen Sie einen sichtbaren „Datenschutz & DSGVO“-Baustein auf Ihrer Seite.") ]));
children.push(bullet([ T("Laufende Betreuung & Beraterverbund", {bold:true}), T(" — beantwortet die „wer hilft danach?“-Frage schon vor dem ersten Gespräch.") ]));

// ---- 6. Wie kommunizieren -------------------------------------------------
children.push(H1("Wie Sie kommunizieren — Ton & Stil"));
children.push(H3("Tun"));
children.push(bullet("Sie-Form, B2B, auf Augenhöhe — wie eine Kollegin, die das Tagesgeschäft kennt."));
children.push(bullet("Das Ergebnis in den Vordergrund: „wieder führen statt verwalten“, „Feierabend ohne Laptop“."));
children.push(bullet("Konkret und mit Beispielen aus dem Praxisalltag (Termine, Absagen, Onboarding, Abrechnung)."));
children.push(bullet("Datenschutz & Folgekosten proaktiv ansprechen — Transparenz schafft Vertrauen."));
children.push(bullet("Betonen: das Persönliche bleibt; KI nimmt die Routine, nicht die Beziehung."));
children.push(H3("Lassen"));
children.push(bullet("„KI / Automatisierung / digitale Transformation“ als Aufmacher — Mittel, nicht Botschaft."));
children.push(bullet("Marketing-Floskeln, Hype, Superlative — die Personas reagieren ausdrücklich allergisch."));
children.push(bullet("Verkaufsdruck bei der kostenlosen Erstanalyse („Ich mag keine Verkaufsgespräche“)."));
children.push(bullet("Generische Versprechen ohne Branchenbezug — wirkt wie „von der Stange“."));
children.push(bullet("Tech-Jargon und kalte, anonyme Chatbot-Anmutung."));

// ---- 7. Fertige Textbausteine ---------------------------------------------
children.push(H1("Fertige Textbausteine (Sie-Form, direkt nutzbar)"));
children.push(P([ T("Rohmaterial aus den O-Tönen — bitte an Ihre Brand Voice anpassen.", { italics:true, color: MUTE }) ]));

children.push(H3("Headline-Optionen"));
children.push(bullet([ T("Damit wieder ", {}), T("Sie", {italics:true}), T(" den Betrieb führen — und nicht der Betrieb Sie.", {bold:true}) ]));
children.push(bullet([ T("Schluss mit „alles hängt an mir“.", {bold:true}) ]));
children.push(bullet([ T("Sie führen Ihre Praxis. Nicht Ihren Posteingang.", {bold:true}) ]));
children.push(bullet([ T("Ihr Team läuft. Auch wenn Sie nicht im Raum sind.", {bold:true}) ]));

children.push(H3("Subline / Erklärsatz"));
children.push(quote("Ich richte Ihrem Betrieb datenschutzkonforme Abläufe ein, die Termine, Klient:innen-Aufnahme und wiederkehrende Verwaltung übernehmen — DSGVO- und EU-AI-Act-konform, mit TÜV-geprüfter Methodik. Damit Sie sich wieder um Ihre Menschen kümmern, nicht um Papierkram.", "Vorschlag"));

children.push(H3("Datenschutz-Baustein"));
children.push(quote("Sie arbeiten mit sensiblen Gesundheitsdaten — ich auch. Datenschutz, EU-AI-Act und sichere Cloud- oder On-Premise-Lösungen sind kein Nachgedanke, sondern Ausgangspunkt jedes Systems, das ich für Sie aufsetze.", "Vorschlag"));

children.push(H3("Call-to-Action für die Erstanalyse"));
children.push(quote("Kostenlose Erstanalyse — ohne Verkaufsgespräch. Wir schauen gemeinsam, wo Ihr Betrieb täglich Zeit verliert. Sie bekommen eine konkrete Einschätzung, ob und wo sich Automatisierung lohnt. Ob Sie danach mit mir arbeiten, entscheiden Sie in Ruhe.", "Vorschlag"));

children.push(H3("Einwand-Vorwegnahme (FAQ / Abschnitt)"));
children.push(bullet([ T("„Und wer betreut das danach?“ ", {bold:true}), T("— Ich bleibe Ihr Ansprechpartner. Die laufende Betreuung sorgt dafür, dass die Systeme mitwachsen — Sie stehen nie allein da.") ]));
children.push(bullet([ T("„Kostet mich das am Ende mehr Zeit?“ ", {bold:true}), T("— Die Einrichtung übernehme ich. Ihr Team wird eingewiesen. Sie gewinnen Zeit, statt welche zu investieren.") ]));
children.push(bullet([ T("„Wird das dann unpersönlich?“ ", {bold:true}), T("— Im Gegenteil: Die Technik übernimmt die Routine, damit für Ihre Klient:innen mehr echte Zeit bleibt.") ]));

children.push(H3("E-Mail-/Erstkontakt-Opener"));
children.push(quote("Sie sind Therapeut:in, Trainer:in, Gesundheitsexpert:in — und verbringen trotzdem halbe Abende mit Terminen, Abrechnung und Nachfassen. Genau hier setze ich an: Ich richte Ihnen die Abläufe so ein, dass das von selbst läuft — datenschutzkonform und ohne dass Sie zur IT-Abteilung werden.", "Vorschlag"));

// ---- 8. Preis -------------------------------------------------------------
children.push(H1("Preis-Kommunikation (Orientierung)"));
children.push(P([ T("Aus der Van-Westendorp-Auswertung (synthetisch, nur Korridor — nicht als exakte Zahl lesen):") ]));
children.push(bullet([ T("Einmaliges Aufbau-Projekt: ", {bold:true}), T("optimaler Preispunkt ~2.167 €, Akzeptanzspanne ~1.740–3.667 €. Ein Fixpreis-Einstiegspaket am unteren Rand entkräftet den Folgekosten-Einwand.") ]));
children.push(bullet([ T("Monatlicher Retainer: ", {bold:true}), T("optimaler Preispunkt ~220 €/Monat, Akzeptanzspanne ~193–386 €/Monat. „Überschaubar, planbar“ war das wiederkehrende Wort — kommunizieren Sie ihn als kalkulierbare Betriebsausgabe.") ]));
children.push(P([ T("Wording, das in den Antworten immer wieder auftauchte: ", {}),
  T("„überschaubar, planbar, vertretbar“", {italics:true, color: TEAL}),
  T(" — und „ich zahle für echten laufenden Support, nicht für eine Hotline, die niemand abhebt“. Greifen Sie das auf.") ]));

// ---- 9. Methodik ----------------------------------------------------------
children.push(H1("Methodik & Grenzen"));
children.push(P([ T("Grundlage: 220 synthetische Personas (kleine Gesundheits-/Wellness-Betriebe mit Team, AT/DE/CH), befragt mit dem Modell claude-sonnet-4-6 in drei blinden Phasen (offene Schmerzpunkte, Reaktion auf das Angebot, Van-Westendorp-Preise). Vollständige Personas, Prompts und Rohdaten sind im Projekt-Repository dokumentiert und reproduzierbar.") ]));
children.push(P([ T("ESOMAR ICC Code 2025: ", {bold:true}),
  T("Dies sind synthetische Daten. Sie ersetzen keine echte Marktforschung. Die Befunde sind Hypothesen und Sprach-Rohmaterial — besonders wertvoll für Tonalität und Textentwürfe, aber vor strategischen oder finanziellen Festlegungen mit 10–20 echten Gesprächen zu validieren. Bekannte Grenzen: gesprochene Präferenz statt echtem Verhalten; mögliche Homogenisierung; leichte Häufung bei Preisangaben.") ]));

// ---- Document -------------------------------------------------------------
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 21, color: INK } } },
    paragraphStyles: [
      { id:"Heading1", name:"Heading 1", basedOn:"Normal", next:"Normal", quickFormat:true,
        run:{ size: 30, bold:true, font:"Arial", color: TEAL },
        paragraph:{ spacing:{ before: 320, after: 140 }, outlineLevel:0,
          border:{ bottom:{ style:BorderStyle.SINGLE, size:6, color: LINE, space: 6 } } } },
      { id:"Heading2", name:"Heading 2", basedOn:"Normal", next:"Normal",
        run:{ size: 25, bold:true, font:"Arial", color: TEAL }, paragraph:{ spacing:{ before: 220, after: 110 }, outlineLevel:1 } },
      { id:"Heading3", name:"Heading 3", basedOn:"Normal", next:"Normal",
        run:{ size: 22, bold:true, font:"Arial", color: VIOLET }, paragraph:{ spacing:{ before: 160, after: 80 }, outlineLevel:2 } },
    ]
  },
  numbering: { config: [
    { reference:"bullets", levels:[{ level:0, format:LevelFormat.BULLET, text:"•", alignment:AlignmentType.LEFT,
      style:{ paragraph:{ indent:{ left: 460, hanging: 260 } } } }] },
    { reference:"numbers", levels:[{ level:0, format:LevelFormat.DECIMAL, text:"%1.", alignment:AlignmentType.LEFT,
      style:{ paragraph:{ indent:{ left: 460, hanging: 260 } } } }] },
  ]},
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 },
      margin: { top: 1300, right: 1300, bottom: 1300, left: 1300 } } },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(process.argv[2], buf);
  console.log("OK", buf.length, "bytes");
});
