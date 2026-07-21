/**
 * Renderöi somekuvat selaimessa oikeilla kirjasimilla.
 *
 * Taustaa: OG-kuvat (assets/og/) tehtiin alun perin ilman talletettua
 * generointitapaa, joten niiden päivittäminen olisi vaatinut työn toistamista
 * käsin. Tämä skripti pitää menetelmän tallessa.
 *
 * Kirjasimet (Newsreader, Hanken Grotesk) haetaan Google Fontsista ajon aikana,
 * joten ajo vaatii verkkoyhteyden. Skripti KAATUU jos kirjasimet eivät lataudu —
 * muuten tuloksena olisi hiljaisesti väärällä fontilla renderöity kuva.
 *
 * Käyttö:
 *   npx playwright install chromium   # kerran
 *   node scripts/somekuvat/renderoi.mjs
 *
 * Tuotokset kirjoitetaan ~/Pictures/ (eivät kuulu sivuston assetteihin).
 */
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import os from 'node:os';

const DIR = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(os.homedir(), 'Pictures');

const KORTIT = [
  { tiedosto: 'ig-1080.html',      koko: [1080, 1080], ulos: 'aiperusteet-ig-1080.png' },
  { tiedosto: 'ig-1080x1350.html', koko: [1080, 1350], ulos: 'aiperusteet-ig-1080x1350.png' },
];

// Minimipalvelin: Chromium ei lataa Google Fontsia file:// -sivulle.
const srv = createServer(async (req, res) => {
  try {
    res.end(await readFile(path.join(DIR, decodeURIComponent(req.url.slice(1)))));
  } catch { res.statusCode = 404; res.end('ei löydy'); }
}).listen(0);
const portti = srv.address().port;

const selain = await chromium.launch();
for (const k of KORTIT) {
  const sivu = await selain.newPage({
    viewport: { width: k.koko[0], height: k.koko[1] }, deviceScaleFactor: 1,
  });
  await sivu.goto(`http://127.0.0.1:${portti}/${k.tiedosto}`, { waitUntil: 'networkidle' });
  await sivu.evaluate(() => document.fonts.ready);
  const fontit = await sivu.evaluate(() => ({
    newsreader: document.fonts.check('600 97px Newsreader'),
    hanken: document.fonts.check('600 26px "Hanken Grotesk"'),
  }));
  if (!fontit.newsreader || !fontit.hanken) {
    console.error(`VIRHE: kirjasimet eivät latautuneet (${k.tiedosto}):`, fontit);
    process.exitCode = 1; break;
  }
  const polku = path.join(OUT, k.ulos);
  await sivu.locator('.card').screenshot({ path: polku });
  console.log(`${k.ulos}  ${k.koko[0]}x${k.koko[1]}  →  ${polku}`);
  await sivu.close();
}
await selain.close();
srv.close();
