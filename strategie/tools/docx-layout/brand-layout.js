// Geteiltes Marken-Layout für Leonie-Kaiser-Strategiedokumente.
// Abgeleitet aus der XML-Struktur von StrategieGesamtdokumentLeonieKaiser.docx.
// Layout hier NICHT verändern — nur die Fußzeile pro Dokument anpassen (siehe buildDoc-Aufruf).

const {
  Document, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, VerticalAlign, BorderStyle, AlignmentType,
  Footer, PageNumber,
} = require("docx");

const TEAL_900 = "086584";
const TEAL_600 = "5FA2A0";
const TEAL_100 = "E7F4F4";
const INK = "1D2228";
const MUTE = "5B6572";
const LINE = "CCCCCC";

const PAGE = {
  size: { width: 12240, height: 15840 }, // US Letter
  margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 },
};
const TEXT_WIDTH = 12240 - 1080 - 1080; // 10080

function docStyles() {
  return {
    default: {
      document: { run: { font: "Arial", size: 21, color: INK } },
      heading1: {
        run: { font: "Arial", bold: true, color: TEAL_900, size: 34 },
        paragraph: { spacing: { before: 260, after: 120 }, keepNext: true, outlineLevel: 0 },
      },
      heading2: {
        run: { font: "Arial", bold: true, color: TEAL_900, size: 27 },
        paragraph: { spacing: { before: 260, after: 120 }, keepNext: true, outlineLevel: 1 },
      },
      heading3: {
        run: { font: "Arial", bold: true, color: TEAL_900, size: 23 },
        paragraph: { spacing: { before: 260, after: 120 }, keepNext: true, outlineLevel: 2 },
      },
      heading4: {
        run: { font: "Arial", bold: true, color: TEAL_600, size: 21 },
        paragraph: { spacing: { before: 260, after: 120 }, keepNext: true, outlineLevel: 3 },
      },
    },
  };
}

function h1(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_1 }); }
function h2(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_2 }); }
function h3(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_3 }); }
function h4(children) {
  const ch = typeof children === "string" ? [new TextRun(children)] : children;
  return new Paragraph({ children: ch, heading: HeadingLevel.HEADING_4 });
}

function docTitle(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_1 }); }

// Italic meta line directly under the title (z. B. "Stand ... / Vertraulich ...")
function metaLine(children) {
  const ch = typeof children === "string" ? [new TextRun({ text: children, italics: true })] : children;
  return new Paragraph({ children: ch, spacing: { after: 100 } });
}

// Horizontal-rule-artiger Divider zwischen großen Abschnitten
function divider() {
  return new Paragraph({
    border: { bottom: { color: TEAL_600, space: 1, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { before: 120, after: 120 },
  });
}

// Callout/Zitat-Block mit linker Randlinie (für Blockquotes, Vorschläge, Hinweise)
function callout(children) {
  const ch = typeof children === "string" ? [new TextRun({ text: children, italics: true, color: MUTE })] : children;
  return new Paragraph({
    children: ch,
    border: { left: { color: TEAL_600, space: 8, style: BorderStyle.SINGLE, size: 12 } },
    indent: { left: 360 },
    spacing: { after: 40 },
  });
}

function p(children, opts = {}) {
  const ch = typeof children === "string" ? [new TextRun(children)] : children;
  return new Paragraph({ children: ch, spacing: { after: 100 }, ...opts });
}
function bold(text) { return new TextRun({ text, bold: true }); }
function italic(text) { return new TextRun({ text, italics: true }); }

function bullet(children, level = 0) {
  const ch = typeof children === "string" ? [new TextRun(children)] : children;
  return new Paragraph({ children: ch, bullet: { level }, spacing: { after: 20 } });
}
function numbered(children) {
  const ch = typeof children === "string" ? [new TextRun(children)] : children;
  return new Paragraph({ children: ch, spacing: { after: 20 } });
}

function cell(text, opts = {}) {
  const { header = false, width } = opts;
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: header ? { type: ShadingType.CLEAR, color: "auto", fill: TEAL_100 } : undefined,
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 1, color: LINE },
      bottom: { style: BorderStyle.SINGLE, size: 1, color: LINE },
      left: { style: BorderStyle.SINGLE, size: 1, color: LINE },
      right: { style: BorderStyle.SINGLE, size: 1, color: LINE },
    },
    children: [new Paragraph({
      spacing: { after: 0 },
      children: [new TextRun({ text, bold: header, color: header ? TEAL_900 : INK, size: 16 })],
    })],
  });
}
function makeTable(columnWidths, rows) {
  return new Table({
    columnWidths,
    width: { size: columnWidths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: "auto" },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: "auto" },
      left: { style: BorderStyle.SINGLE, size: 4, color: "auto" },
      right: { style: BorderStyle.SINGLE, size: 4, color: "auto" },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: "auto" },
      insideVertical: { style: BorderStyle.SINGLE, size: 4, color: "auto" },
    },
    rows: rows.map((r, i) => new TableRow({
      tableHeader: i === 0,
      children: r.map((val, ci) => cell(val, { header: i === 0, width: columnWidths[ci] })),
    })),
  });
}

// Fußzeile — pro Dokument individuell (einziges Element, das sich zwischen den
// Strategiedokumenten unterscheiden soll).
function makeFooter(captionText) {
  return new Footer({
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: captionText + " · Seite ", color: MUTE, size: 16 }),
          new TextRun({ children: [PageNumber.CURRENT], color: MUTE, size: 16 }),
        ],
      }),
    ],
  });
}

function buildDocument(children, footerCaption) {
  return new Document({
    styles: docStyles(),
    sections: [{
      properties: { page: PAGE },
      footers: { default: makeFooter(footerCaption) },
      children,
    }],
  });
}

module.exports = {
  TEAL_900, TEAL_600, TEAL_100, INK, MUTE, LINE, PAGE, TEXT_WIDTH,
  h1, h2, h3, h4, docTitle, metaLine, divider, callout, p, bold, italic,
  bullet, numbered, cell, makeTable, makeFooter, buildDocument,
};
