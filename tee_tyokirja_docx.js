// Tämä skripti generoi downloads/ai-perusteet-tyokirja.docx -tiedoston.
// Aja: npm install docx && node tee_tyokirja_docx.js  (repon juuressa)
// HUOM: pidä sisältö synkassa downloads/ai-perusteet-tyokirja.md:n kanssa —
// md on sisällön lähde, tämä skripti tuottaa tyylitellyn Word-version.
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType,
  Footer, PageNumber, TableLayoutType,
} = require('docx');
const fs = require('fs');

// Kurssin väripaletti
const DARK = '1B2336';      // otsikot (diat)
const BODY = '3A4253';      // leipäteksti (diat)
const MUTED = '5A6478';     // toissijainen
const KICKER = '7E88A8';    // mono-kickerit
const BLUE = '3B5BDB';      // teoria / pääaksentti (diat)
const VIOLET = '8449B8';    // käyttö (printtitumma violetti)
const TEAL = '007A8A';      // agentit (printtitumma teal)
const LINE = 'D8DCE8';      // täyttöviivat
const BORDER = 'E2E5EE';    // taulukkoreunat
const SHADE = 'F4F6FB';     // infolaatikko (--bg-paper)
const SHADEBLUE = 'EEF1FE'; // taulukon otsikkorivi

const SANS = 'Helvetica Neue';
const MONO = 'Helvetica Neue';

const CONTENT_W = 9026; // A4 - 2x1440 marginaalit

// --- apurit ---------------------------------------------------------------
const kicker = (text, color = BLUE) => new Paragraph({
  spacing: { before: 60, after: 40 },
  children: [new TextRun({ text, font: MONO, size: 15, color, characterSpacing: 30 })],
});

const h2 = (text, color) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 320, after: 60 },
  border: { left: { style: BorderStyle.SINGLE, size: 24, color, space: 12 } },
  children: [new TextRun({ text, font: SANS, size: 30, bold: true, color: DARK })],
});

const h3 = (text, color) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  spacing: { before: 240, after: 40 },
  children: [new TextRun({ text, font: SANS, size: 24, bold: true, color })],
});

const body = (text, opts = {}) => new Paragraph({
  spacing: { after: 120, line: 288 },
  children: [new TextRun({ text, font: SANS, size: 21, color: BODY, italics: opts.italics || false })],
});

const note = (text) => new Paragraph({
  spacing: { after: 160, line: 276 },
  children: [new TextRun({ text, font: SANS, size: 19, color: MUTED, italics: true })],
});

// Infolaatikko (tietosuoja) — kevyt tausta + sininen vasen palkki
const infoBox = (text) => new Table({
  layout: TableLayoutType.FIXED,
  width: { size: CONTENT_W, type: WidthType.DXA },
  columnWidths: [CONTENT_W],
  borders: {
    top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
    left: { style: BorderStyle.SINGLE, size: 24, color: BLUE }, right: { style: BorderStyle.NONE },
    insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
  },
  rows: [new TableRow({ children: [new TableCell({
    width: { size: CONTENT_W, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: SHADE },
    margins: { top: 140, bottom: 140, left: 200, right: 200 },
    children: [new Paragraph({
      spacing: { after: 0, line: 276 },
      children: [new TextRun({ text, font: SANS, size: 20, color: BODY })],
    })],
  })] })],
});

// Täytettävä kenttä: lihavoitu label
const field = (label) => new Paragraph({
  spacing: { before: 160, after: 80 },
  children: [new TextRun({ text: label, font: SANS, size: 21, bold: true, color: DARK })],
});

// Vastauslaatikko: kehystetty kirjoitusalue (renderöityy kaikissa ohjelmissa)
const answerBox = (lines = 1) => {
  const paras = [];
  for (let i = 0; i < lines; i++) paras.push(new Paragraph({
    spacing: { after: i === lines - 1 ? 0 : 240 },
    children: [new TextRun({ text: ' ', font: SANS, size: 21 })],
  }));
  return new Table({
    layout: TableLayoutType.FIXED,
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    borders: {
      top: { style: BorderStyle.SINGLE, size: 6, color: LINE },
      bottom: { style: BorderStyle.SINGLE, size: 6, color: LINE },
      left: { style: BorderStyle.SINGLE, size: 6, color: LINE },
      right: { style: BorderStyle.SINGLE, size: 6, color: LINE },
      insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
    },
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      margins: { top: 100, bottom: 140, left: 140, right: 140 },
      children: paras,
    })] })],
  });
};

// Kenttä + vastauslaatikko
const fieldLines = (label, lines = 1) => [field(label), answerBox(lines), spacerP()];

// Taulukko, jossa otsikkorivi + tyhjiä täyttörivejä
const fillTable = (headers, emptyRows, colWidths) => {
  const mkCell = (text, isHead) => new TableCell({
    width: { size: colWidths[0], type: WidthType.DXA }, // korvataan alla per sarake
    margins: { top: 90, bottom: 90, left: 120, right: 120 },
    shading: isHead ? { type: ShadingType.CLEAR, fill: SHADEBLUE } : undefined,
    children: [new Paragraph({
      spacing: { after: 0 },
      children: [new TextRun({ text, font: SANS, size: isHead ? 19 : 20, bold: isHead, color: isHead ? DARK : BODY })],
    })],
  });
  const headRow = new TableRow({ tableHeader: true, children: headers.map((t, i) => {
    const c = mkCell(t, true); c.options.width = { size: colWidths[i], type: WidthType.DXA }; return c;
  })});
  const rows = [headRow];
  for (let r = 0; r < emptyRows; r++) {
    rows.push(new TableRow({ children: headers.map((_, i) => {
      const c = mkCell(' ', false); c.options.width = { size: colWidths[i], type: WidthType.DXA }; return c;
    })}));
  }
  return new Table({
    layout: TableLayoutType.FIXED,
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: colWidths,
    borders: {
      top: { style: BorderStyle.SINGLE, size: 6, color: BORDER },
      bottom: { style: BorderStyle.SINGLE, size: 6, color: BORDER },
      left: { style: BorderStyle.SINGLE, size: 6, color: BORDER },
      right: { style: BorderStyle.SINGLE, size: 6, color: BORDER },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 6, color: BORDER },
      insideVertical: { style: BorderStyle.SINGLE, size: 6, color: BORDER },
    },
    rows,
  });
};

const spacer = (h = 120) => new Paragraph({ spacing: { after: h }, children: [] });
const spacerP = () => new Paragraph({ spacing: { after: 40 }, children: [] });

// --- dokumentti -----------------------------------------------------------
const children = [
  // Kansiotsikko: kicker + iso otsikko + sininen palkki (diojen identiteetti)
  new Paragraph({
    spacing: { after: 60 },
    children: [new TextRun({ text: 'AI · PERUSTEET — AVOIN VERKKOKURSSI', font: MONO, size: 17, color: KICKER, characterSpacing: 40 })],
  }),
  new Paragraph({
    spacing: { after: 80 },
    border: { left: { style: BorderStyle.SINGLE, size: 36, color: BLUE, space: 14 } },
    children: [new TextRun({ text: 'Työkirja', font: SANS, size: 64, bold: true, color: DARK })],
  }),
  body('Tämä työkirja on henkilökohtainen työjälkesi: tallenna tänne promptisi, kokeiden tulokset, lähteet ja tekemäsi korjaukset, koska kurssisivusto ei tallenna niitä puolestasi. Voit täyttää tiedostoa tekstieditorissa tai tekstinkäsittelyohjelmassa ja tulostaa sen PDF:ksi.'),
  infoBox('Älä tallenna työkirjaan muiden ihmisten henkilötietoja tai luottamuksellista aineistoa — sama periaate, jonka opit kurssilla tekoälypalveluiden käytöstä, koskee myös omia muistiinpanojasi.'),
  spacer(160),
  field('Nimi tai oma tunniste:'),
  answerBox(1),
  spacerP(),
  note('Jos palautat työkirjan opettajalle tai oppilaitokselle, nimestä näkyy, kenen työ on kyseessä. Itsenäisenä opiskelijana voit jättää kohdan tyhjäksi.'),

  // Oma reittini
  h2('Oma reittini', BLUE),
  body('Kurssin tehtävissä valitset itse, millaisiin tilanteisiin sovellat oppimaasi. Kirjaa valintasi tähän kerran, niin sinun ei tarvitse miettiä niitä jokaisen tehtävän kohdalla uudelleen — ja lukija näkee yhdellä silmäyksellä, miten teit kurssin.'),
  ...fieldLines('Konteksti, johon sovellan oppimaani (arki tai harrastus / opiskelu / työelämän rooliskenaario):', 1),
  ...fieldLines('Työkalu, jolla teen kokeet (saatavilla oleva chat / annettu esimerkkitulos / dokumentoitu kuivaharjoittelu ilman tiliä):', 1),
  ...fieldLines('Minne tallennan tämän työkirjan ja tuotokseni:', 1),

  // OSA 1 — Teoria
  kicker('OSA 1 · TEORIA', BLUE),
  h2('Todistusaineistot 1–3', BLUE),

  h3('Todistusaineisto 1: syöte, kolme tulosta ja mekanismiselitys', BLUE),
  ...fieldLines('Tarkka prompti tai annettu syöte:', 2),
  ...fieldLines('Tulos 1:', 1),
  ...fieldLines('Tulos 2:', 1),
  ...fieldLines('Tulos 3:', 1),
  ...fieldLines('Mitä tulosten vaihtelu kertoo:', 2),

  h3('Todistusaineisto 2: kontekstin katoamis- ja palautusloki', BLUE),
  ...fieldLines('Mitä tietoa tarvittiin:', 1),
  ...fieldLines('Milloin tieto katosi:', 1),
  ...fieldLines('Miten palautin tiedon:', 1),
  ...fieldLines('Mitä tästä seuraa käytännössä:', 2),

  h3('Todistusaineisto 3: väite–lähde–tulos–korjaus', BLUE),
  fillTable(['Tarkistettava väite', 'Luotettava lähde', 'Tulos', 'Korjattu muoto'], 3, [2482, 2256, 1806, 2482]),

  // OSA 2 — Käyttö
  kicker('OSA 2 · KÄYTTÖ', VIOLET),
  h2('Promptipankin kortti', VIOLET),
  ...fieldLines('Tavoite:', 1),
  ...fieldLines('Kohderyhmä tai käyttötilanne:', 1),
  ...fieldLines('Tarvittava konteksti:', 1),
  ...fieldLines('Lähdeaineisto:', 1),
  ...fieldLines('Vaiheet:', 2),
  ...fieldLines('Haluttu muoto:', 1),
  ...fieldLines('Versio 1 ja tulos:', 2),
  ...fieldLines('Korjaus:', 1),
  ...fieldLines('Versio 2 ja tulos:', 2),

  h2('Botin prosessinäyttö', VIOLET),
  ...fieldLines('Tarkoitus ja rajat:', 1),
  ...fieldLines('Järjestelmäprompti:', 3),
  ...fieldLines('Tietopohja tai annettu testiaineisto:', 1),
  ...fieldLines('Positiivinen testi ja tulos:', 1),
  ...fieldLines('Negatiivinen testi ja tulos:', 1),
  ...fieldLines('Reunatapaus ja tulos:', 1),
  ...fieldLines('Tehty korjaus ja uudelleentesti:', 2),
  ...fieldLines('Toteutus / kuivaharjoittelu:', 1),

  // OSA 3 — Agentit
  kicker('OSA 3 · AGENTIT', TEAL),
  h2('Agentin prosessinäyttö', TEAL),
  ...fieldLines('Ongelma, jonka agentti ratkaisee:', 1),
  ...fieldLines('Miksi prompti tai tavallinen työnkulku ei yksin riitä:', 2),
  ...fieldLines('Solmukaavio ja työkalusopimus:', 3),
  ...fieldLines('Oikeudet, hyväksyntäportit ja eskalointi:', 2),
  ...fieldLines('Työkalukutsut, tulokset, virheet ja lyhyet päätösperustelut:', 3),
  ...fieldLines('3 normaalia testiä:', 2),
  ...fieldLines('3 reunatapausta:', 2),
  ...fieldLines('3 turvallisuustestiä:', 2),
  ...fieldLines('Vähintään kaksi korjauksen jälkeistä uudelleentestiä:', 2),
  ...fieldLines('2–3 minuutin demon tai puolustuksen muistiinpanot:', 2),

  // Lähteet
  kicker('KOKO KURSSI', KICKER),
  h2('Lähteet', BLUE),
  fillTable(['Lähde', 'Mitä tarkistin', 'Tarkistuspäivä'], 4, [3610, 3610, 1806]),
];

const doc = new Document({
  styles: { default: { document: { run: { font: SANS, size: 21, color: BODY } } } },
  sections: [{
    properties: { page: { margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      border: { top: { style: BorderStyle.SINGLE, size: 6, color: BORDER, space: 8 } },
      children: [
        new TextRun({ text: 'AI · Perusteet — aiperusteet.fi · CC BY-SA 4.0 · sivu ', font: MONO, size: 15, color: KICKER }),
        new TextRun({ children: [PageNumber.CURRENT], font: MONO, size: 15, color: KICKER }),
      ],
    })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync('downloads/ai-perusteet-tyokirja.docx', buf);
  console.log('kirjoitettu', buf.length, 'tavua');
});
