const { Paragraph, TextRun, Packer } = require("docx");
const fs = require("fs");
const path = require("path");
const L = require("./brand-layout");
const { h1, h2, h3, docTitle, metaLine, divider, callout, p, bold, italic, bullet, numbered, makeTable, buildDocument } = L;

function boldLine(label, text) {
  return p([bold(label + " "), new TextRun(text)]);
}

const children = [
  docTitle("Social-Media-Konzept (Schwerpunkt LinkedIn)"),
  boldLine("Stand:", "2026-10-16."),
  boldLine("Zweck:", "Konkretisiert den LinkedIn-Absatz aus website-traffic-strategie.md (dort nur grob: 1 Post/Woche, Themen Haltung/Lehrgang/Branchenbeobachtungen, Start diese Woche)."),
  boldLine("Baut auf:", "netzwerk-strategie.md Kap. 3–5 auf (Kanäle, SSI-Logik, Maintenance-System, Fahrplan) — wiederholt das dort Stehende nicht, sondern ergänzt es um Content-Säulen, Posting-Rhythmus im Detail, Blog↔LinkedIn-Verlinkung und Post-Vorlagen."),
  boldLine("Brand Voice:", "Sie-Form, alle Regeln aus AGENTS.md gelten für LinkedIn-Posts genauso wie für Website-Texte (explizit erwähnt in AGENTS.md Zeile 344: „Social“ zählt als Kundentext)."),
  divider(),

  h1("0. Zeitbudget-Bezug — wie sich die beiden Budgets zueinander verhalten"),
  p("Es gibt zwei Zeitangaben in den Strategie-Dateien, die auf den ersten Blick widersprüchlich wirken:"),
  bullet([new TextRun("netzwerk-strategie.md Kap. 4 (Stand 2026-07-23): 3–4 Std./Woche für das gesamte „Networking-System“ — LinkedIn (~1 Std.), Facebook (~30 Min.), Reconnect-/Nachfass-Nachrichten (~1 Std.), 1 persönlicher Kontaktpunkt (~1–1,5 Std.).")]),
  bullet([new TextRun("website-traffic-strategie.md Kap. 2 (Stand 2026-10-13, aktueller): 5+ Std./Woche für Blog + LinkedIn + Pilot zusammen, davon ~2 Std. für LinkedIn (1 Post + 15–20 Min. gezieltes Kommentieren).")]),
  callout([bold("Auflösung: "), new TextRun({ italics: true, color: L.MUTE, text: "Die 5+ Std. aus website-traffic-strategie.md sind der aktuell gültige Gesamt-Rahmen. Die ~2 Std./Woche LinkedIn darin sind reine Content-Zeit (Post schreiben + veröffentlichen + gezieltes Kommentieren) — das gestaltet dieses Konzept aus. Reconnect-Nachrichten, Facebook-Cross-Posts, Kontakt-Tabellen-Pflege und persönliche Kontaktpunkte bleiben im separaten 3–4-Std.-Netzwerk-Budget aus netzwerk-strategie.md Kap. 4 — die beiden Budgets werden nicht addiert, sie decken unterschiedliche Aktivitäten ab." })]),
  divider(),

  h1("1. Content-Säulen"),
  p("Vier Säulen, abgeleitet aus den in website-traffic-strategie.md Phase 1 genannten Themen plus dem expliziten Traffic-Ziel „neue Blogposts in LinkedIn-Beiträgen referenzieren“:"),
  makeTable([700, 2200, 5200, 2000], [
    ["#", "Säule", "Worum es geht", "Quelle"],
    ["1", "Haltung", "Fachliche Position zu KI, Datenschutz, EU AI Act in kleinen Praxen — kein Verkauf, eine Meinung.", "brand_position.md, AGENTS.md"],
    ["2", "Lehrgangs-Einblicke", "Was im KI-Consultant-Lehrgang (Gründer.de) diskutiert wird, eigene Einordnung, Transfer auf die Zielgruppe.", "Laufender Lehrgang"],
    ["3", "Branchenbeobachtungen", "Beobachtungen/Trends zu kleinen Gesundheitspraxen und KI — reine Einordnung, keine Verkaufsabsicht (Phase-1-Regel: noch keine Pilot-Werbung).", "Eigene Recherche, segmente.md"],
    ["4", "Blog-Cross-Post", "Eigenständiger LinkedIn-Text zu einer zentralen These aus einem neuen Blogpost, mit Link zum vollständigen Beitrag.", "blog-konzept.md, Journal"],
  ]),
  p([bold("Phase-1-Einschränkung "), new TextRun("(gilt für alle vier Säulen): keine Pilot-/Akquise-Werbung, keine Case-Study-Inhalte — es gibt noch keine echten Fälle (siehe website-traffic-strategie.md Kap. 2). Säule 5 „Pilot-Cases/Testimonials“ kommt erst in Phase 2 dazu, sobald der erste Pilot läuft (siehe Kap. 4 unten).")]),
  divider(),

  h1("2. Posting-Rhythmus im Detail"),
  p("1 Post/Woche, fester Bestandteil des ~2-Std.-LinkedIn-Budgets aus Kap. 0. Zwei Fälle:"),
  bullet([bold("Woche mit neuem Blogpost: "), new TextRun("Dieser Post ist die Woche — Säule 4 (Blog-Cross-Post). Kein zusätzlicher Post daneben, das Budget bleibt bei 1/Woche.")]),
  bullet([bold("Woche ohne neuen Blogpost "), new TextRun("(aktuell der Normalfall, solange der Blog laut Phase 1 nicht im Wochentakt läuft): Rotation durch Säule 1 → 2 → 3 → wieder 1 …")]),
  p("Das ergibt in der Praxis grob jede 3.–4. Woche einen Blog-Cross-Post, sobald der Blog wieder regelmäßiger läuft (Phase-2-Trigger aus website-traffic-strategie.md: „sobald sich LinkedIn-Posting 2–3 Wochen stabil anfühlt“). Bis dahin dominiert die Rotation 1–2–3."),
  p([bold("Tag: Donnerstag "), new TextRun("(festgelegt 2026-10-16). Zwei Tage Abstand zum Blog-Rhythmus (Dienstag) — Blogpost und LinkedIn-Cross-Post fallen nicht auf denselben Tag. Donnerstag gilt im B2B-Kontext zudem als engagement-starker LinkedIn-Tag, ohne mit dem Blog-Tag zu kollidieren.")]),
  p([bold("Die 15–20 Min. gezieltes Kommentieren "), new TextRun("(Teil desselben Budgets) folgen der SSI-Logik aus netzwerk-strategie.md Kap. 3.1, Punkt 3: auf Beiträge von Tier-1/2-Kontakten kommentieren, bevor sie angeschrieben werden — eine Vorwärmung, die in die Kontakt-Tabelle aus Kap. 4 dort einfließt, aber zeitlich zu diesem Budget hier zählt.")]),
  divider(),

  h1("3. Blog ↔ LinkedIn: wie sich die Kanäle gegenseitig verlinken"),
  p([bold("Hauptrichtung (Traffic-Ziel): "), new TextRun("Blog → LinkedIn. Jeder neue Blogpost bekommt einen eigenen LinkedIn-Post (Säule 4). Wichtig, um echten Mehrwert statt Duplicate Content zu erzeugen:")]),
  bullet([bold("Kein 1:1-Teaser. "), new TextRun("Der LinkedIn-Post fasst den Blogpost nicht zusammen, sondern greift eine zugespitzte These oder einen einzelnen Aspekt daraus auf und entwickelt sie in eigenen Worten weiter.")]),
  bullet([bold("Link-Platzierung: "), new TextRun("Empfehlung, den Link zum Blogpost in den ersten Kommentar zu setzen statt in den Haupttext — gängige LinkedIn-Praxis, weil Posts mit externem Link im Text seltener ausgespielt werden."), new TextRun({ italics: true, color: L.MUTE, text: " (Das ist meine Empfehlung, nicht aus einer der Quelldateien.)" })]),
  bullet([bold("Format: "), new TextRun("siehe Vorlage „Blog-Cross-Post“ in Kap. 4.")]),
  p([bold("Nebenrichtung "), new TextRun("(ergänzend, nicht im Traffic-Ziel explizit gefordert, aber naheliegend): Wenn eine Säule-1/3-Beobachtung thematisch zu einem älteren Blogpost passt, darf der Link dort mit rein. Kein Pflichtbestandteil jedes Posts, nur wenn es inhaltlich passt.")]),
  p([bold("Facebook bleibt außen vor: "), new TextRun("Die Cross-Posting-Logik LinkedIn → Facebook ist bereits in netzwerk-strategie.md Kap. 3.2 beschrieben (Kerninhalt umformulieren, nicht kopieren, persönlicherer Ton) — wird hier nicht dupliziert.")]),
  divider(),

  h1("4. Vorlage pro Post-Typ"),
  p("Alle vier Formate: Sie-Form, Brand Voice (AGENTS.md) — insbesondere keine Verkaufsrhetorik-Phrasen, keine Wischiwaschi-Hedges, „tool-agnostisch“ nie im Post-Text, keine erfundene Erfahrung in der Gesundheitspraxen-Beratung selbst."),

  h3("4.1 Haltung (Säule 1)"),
  numbered([bold("Hook "), new TextRun("— eine zugespitzte Aussage oder Frage, 1 Satz.")]),
  numbered([bold("Standpunkt "), new TextRun("— 3–5 Sätze, warum das so ist, ohne Verkaufsabsicht.")]),
  numbered([bold("Praxis-Bezug "), new TextRun("— ein konkretes, kleines Beispiel aus dem Praxisalltag (keine erfundenen Kundenfälle).")]),
  numbered([bold("Abschluss "), new TextRun("— eine echte Frage an die Leser:innen, die tatsächlich zum Thema passt.")]),

  h3("4.2 Lehrgangs-Einblick (Säule 2)"),
  numbered([bold("Was gerade im Lehrgang dran war "), new TextRun("— 1–2 Sätze, konkret.")]),
  numbered([bold("Eigene Einordnung "), new TextRun("— was davon für die Zielgruppe relevant ist, nicht nur „war spannend“.")]),
  numbered([bold("Transfer "), new TextRun("— ein Satz, der die Brücke zur eigenen Arbeit schlägt.")]),
  numbered([new TextRun("Optional: Frage an andere Lehrgangsteilnehmer:innen/die Community.")]),

  h3("4.3 Branchenbeobachtung (Säule 3)"),
  numbered([bold("Beobachtung "), new TextRun("— ein konkreter Trend/eine Entwicklung bei kleinen Gesundheitspraxen und KI, 1–2 Sätze.")]),
  numbered([bold("Einordnung "), new TextRun("— was das für die Zielgruppe bedeutet, sachlich, ohne Dramatisierung.")]),
  numbered([bold("Kein Verkaufsschluss "), new TextRun("— Phase 1 explizit ohne Pilot-/Akquise-Bezug.")]),

  h3("4.4 Blog-Cross-Post (Säule 4)"),
  numbered([bold("Hook aus der These "), new TextRun("— der zugespitzte Punkt aus dem Blogpost, eigenständig für LinkedIn formuliert.")]),
  numbered([bold("Kurze Entfaltung "), new TextRun("— 3–4 Sätze, warum der Punkt wichtig ist.")]),
  numbered([bold("Übergang zum Blogpost "), new TextRun("— „Den ganzen Beitrag mit [Detailpunkt] gibt's hier:“ — Link im ersten Kommentar.")]),
  numbered([new TextRun("Kein zusätzlicher CTA zur Potenzialanalyse in Phase 1 (erst ab Phase 2).")]),
  divider(),

  h1("5. Phase-Bezug (keine Dopplung zu website-traffic-strategie.md)"),
  makeTable([1600, 2200, 6300], [
    ["Phase", "Zeitraum", "Was für dieses Konzept gilt"],
    ["Phase 1", "Jetzt – Ende November", "Nur Säulen 1–3 aktiv + Säule 4 sobald ein Blogpost erscheint. Kein Pilot-/Akquise-Bezug in keinem Post."],
    ["Phase 2", "Ab Ende November/Dezember", "Blog geht auf Wochentakt (Trigger: 2–3 Wochen stabiles LinkedIn-Posting) → Säule 4 wird regelmäßiger. Pilot-Akquise startet → neue Säule 5 „Pilot-Cases/Testimonials“ möglich, sobald der erste echte Fall da ist."],
  ]),
  divider(),

  metaLine("Quellen: website-traffic-strategie.md (übergeordneter Fahrplan, Zeitbudget), netzwerk-strategie.md Kap. 3–5 (Kanäle, SSI-Logik, Maintenance-System), blog-konzept.md (Blog-Seite der Verlinkung), linkedin-profil.md (Profiltexte). Brand Voice kanonisch: AGENTS.md."),
];

const doc = buildDocument(children, "Social-Media-Konzept · Intern");

const outDir = path.join(__dirname, "output");
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync(path.join(outDir, "Social-Media-Konzept.docx"), buffer);
  console.log("done: output/Social-Media-Konzept.docx");
});
