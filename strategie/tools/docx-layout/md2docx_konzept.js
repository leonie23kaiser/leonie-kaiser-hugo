// Minimaler Markdown -> DOCX Renderer (docx-js) fuer den Silicon-Sampling-Report.
// Unterstuetzt: #..#### Headings, Tabellen, Bullet-/Nummern-Listen, > Zitate,
// **fett**, *kursiv*, `code`, --- Trenner. Brand-Farben (Teal).
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, VerticalAlign,
  Header, Footer, PageNumber,
} = require("docx");

const TEAL = "086584", TEAL6 = "5FA2A0", TEAL_LIGHT = "E7F4F4";
const INK = "1D2228", MUTE = "5B6572", LINE = "CCCCCC";
const CONTENT_W = 12240 - 2 * 1080; // 0.75" Raender -> 10080 DXA

const inPath = process.argv[2], outPath = process.argv[3];
const lines = fs.readFileSync(inPath, "utf8").split(/\r?\n/);

// ---- Inline-Parser: **fett**, *kursiv*, `code` ----
function parseInline(text, base = {}) {
  const runs = [];
  const re = /(\*\*[^*]+\*\*|`[^`]+`|\*[^*\n]+\*)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const tok = m[0];
    if (tok.startsWith("**")) runs.push(new TextRun({ text: tok.slice(2, -2), bold: true, ...base }));
    else if (tok.startsWith("`")) runs.push(new TextRun({ text: tok.slice(1, -1), font: "Consolas", ...base }));
    else runs.push(new TextRun({ text: tok.slice(1, -1), italics: true, ...base }));
    last = m.index + tok.length;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), ...base }));
  if (runs.length === 0) runs.push(new TextRun({ text: "", ...base }));
  return runs;
}

function splitCells(line) {
  let s = line.trim();
  if (s.startsWith("|")) s = s.slice(1);
  if (s.endsWith("|")) s = s.slice(0, -1);
  return s.split("|").map((c) => c.trim());
}
const isSep = (line) => splitCells(line).every((c) => /^:?-{2,}:?$/.test(c));

function colWidths(n) {
  if (n <= 1) return [CONTENT_W];
  const w0 = Math.round(CONTENT_W * 0.26);
  const rest = Math.floor((CONTENT_W - w0) / (n - 1));
  const ws = [w0];
  for (let i = 1; i < n; i++) ws.push(rest);
  ws[n - 1] += CONTENT_W - ws.reduce((a, b) => a + b, 0);
  return ws;
}

function makeTable(block) {
  const header = splitCells(block[0]);
  const dataRows = block.slice(1).filter((l) => !isSep(l)).map(splitCells);
  const n = header.length;
  const ws = colWidths(n);
  const border = { style: BorderStyle.SINGLE, size: 1, color: LINE };
  const borders = { top: border, bottom: border, left: border, right: border };
  const mkCell = (txt, i, head) => new TableCell({
    width: { size: ws[i], type: WidthType.DXA },
    shading: head ? { fill: TEAL_LIGHT, type: ShadingType.CLEAR, color: "auto" } : undefined,
    borders,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({
      spacing: { after: 0 },
      children: parseInline(txt, { size: 16, bold: head ? true : undefined, color: head ? TEAL : INK }),
    })],
  });
  const rows = [new TableRow({ tableHeader: true, children: header.map((c, i) => mkCell(c, i, true)) })];
  for (const r of dataRows) {
    const cells = [];
    for (let i = 0; i < n; i++) cells.push(mkCell(r[i] || "", i, false));
    rows.push(new TableRow({ children: cells }));
  }
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: ws, rows });
}

const HMAP = { 1: HeadingLevel.HEADING_1, 2: HeadingLevel.HEADING_2, 3: HeadingLevel.HEADING_3, 4: HeadingLevel.HEADING_4 };

const children = [];
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  const t = line.trim();
  if (t === "") continue;

  // Tabelle
  if (t.startsWith("|")) {
    const block = [];
    while (i < lines.length && lines[i].trim().startsWith("|")) { block.push(lines[i]); i++; }
    i--;
    if (block.length >= 2) { children.push(makeTable(block)); children.push(new Paragraph({ spacing: { after: 80 }, children: [] })); }
    continue;
  }
  // Trenner
  if (/^---+$/.test(t)) { children.push(new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: TEAL6 } }, spacing: { before: 120, after: 120 }, children: [] })); continue; }
  // Heading
  let m = t.match(/^(#{1,4})\s+(.*)$/);
  if (m) {
    const lvl = m[1].length;
    children.push(new Paragraph({ heading: HMAP[lvl], children: parseInline(m[2]) }));
    continue;
  }
  // Blockquote (O-Ton)
  if (t.startsWith(">")) {
    let txt = t.replace(/^>\s?/, "");
    // umbrochenes **fett** ueber mehrere > Zeilen zusammenfuehren (nur bei unbalanciertem **)
    while (((txt.split("**").length - 1) % 2 === 1) && i + 1 < lines.length && lines[i + 1].trim().startsWith(">")) {
      i++;
      txt += " " + lines[i].trim().replace(/^>\s?/, "");
    }
    children.push(new Paragraph({
      indent: { left: 360 },
      spacing: { after: 40 },
      border: { left: { style: BorderStyle.SINGLE, size: 12, color: TEAL6, space: 8 } },
      children: parseInline(txt, { italics: true, color: MUTE }),
    }));
    continue;
  }
  // Bullet
  m = t.match(/^[-*]\s+(.*)$/);
  if (m) { children.push(new Paragraph({ bullet: { level: 0 }, spacing: { after: 20 }, children: parseInline(m[1]) })); continue; }
  // Nummerierte Zeile (Nummer als Text beibehalten)
  m = t.match(/^(\d+)\.\s+(.*)$/);
  if (m) {
    children.push(new Paragraph({
      indent: { left: 360, hanging: 240 }, spacing: { after: 20 },
      children: [new TextRun({ text: m[1] + ". ", bold: true }), ...parseInline(m[2])],
    }));
    continue;
  }
  // Normaler Absatz
  children.push(new Paragraph({ spacing: { after: 100 }, children: parseInline(t) }));
}

const heading = (id, name, size, outline, color) => ({
  id, name, basedOn: "Normal", next: "Normal", quickFormat: true,
  run: { size, bold: true, font: "Arial", color },
  paragraph: { spacing: { before: 260, after: 120 }, outlineLevel: outline, keepNext: true },
});

const doc = new Document({
  creator: "Silicon Sampling Pipeline",
  title: "Strategisches Konzept — Leonie Kaiser",
  styles: {
    default: { document: { run: { font: "Arial", size: 21, color: INK } } },
    paragraphStyles: [
      heading("Heading1", "Heading 1", 34, 0, TEAL),
      heading("Heading2", "Heading 2", 27, 1, TEAL),
      heading("Heading3", "Heading 3", 23, 2, TEAL),
      heading("Heading4", "Heading 4", 21, 3, TEAL6),
    ],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 } } },
    footers: {
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: "Synthetische Daten (ESOMAR ICC 2025) · Hypothesen, keine Fakten · Seite ", size: 16, color: MUTE }),
          new TextRun({ children: [PageNumber.CURRENT], size: 16, color: MUTE }),
        ],
      })] }),
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(outPath, buf); console.log("DOCX geschrieben:", outPath, buf.length, "bytes"); });
