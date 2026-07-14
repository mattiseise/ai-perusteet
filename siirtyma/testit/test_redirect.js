#!/usr/bin/env node
/*
 * Redirect-testi (hyväksymiskriteeri e).
 * Poimii index.html:n hash-mappauksen (var R={...}) ja simuloi ohjaussivun logiikan
 * jokaiselle redirectit.md-taulukon vanhalle osoitteelle (27 tuntia × kaikki tabit +
 * briefit + tuntematon) ja vertaa lukittuun odotettuun.
 *
 * Aja: node siirtyma/testit/test_redirect.js
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const html = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');

// Poimi var R={...}; (redirect-taulukko)
const m = html.match(/var R=(\{.*?\});/s);
if (!m) { console.error('VIRHE: var R={...} ei löydy index.html:stä'); process.exit(1); }
const R = JSON.parse(m[1]);

// Simuloi ohjaussivun logiikka (sama kuin index.html:n IIFE)
function dest(h) {
  if (R[h]) return R[h];
  const mm = h.match(/^(lesson-\d{2})\//);
  if (mm && R[mm[1]]) return R[mm[1]];
  return null; // tuntematon → ei ohjausta (jää valintasivulle)
}

const ASSESSMENT = new Set(['18', '27']);
function expected(nn, tab) {
  const isA = ASSESSMENT.has(nn);
  switch (tab) {
    case '':
    case 'selfstudy': return `/kurssi/tunti-${nn}/`;
    case 'practice':  return isA ? `/kurssi/tunti-${nn}/` : `/kurssi/tunti-${nn}/#harjoittele`;
    case 'vocab':     return isA ? `/kurssi/tunti-${nn}/` : `/kurssi/tunti-${nn}/#sanasto`;
    case 'stasks':    return `/luokka/tunti-${nn}/#tehtavat`;
    case 'slides':    return `/luokka/tunti-${nn}/#diat`;
    case 'tltasks':   return isA ? `/kurssi/tunti-${nn}/` : `/opettaja/tunti-${nn}/`;
    case 'tmats':     return `/opettaja/tunti-${nn}/`;
    default:          return `/kurssi/tunti-${nn}/`; // tuntematon tab
  }
}

let checks = 0, fails = 0;
function check(hash, exp) {
  checks++;
  const got = dest(hash);
  if (got !== exp) {
    fails++;
    console.error(`FAIL  #${hash}  odotettu=${exp}  saatu=${got}`);
  }
}

const tabs = ['', 'selfstudy', 'practice', 'vocab', 'stasks', 'slides', 'tltasks', 'tmats', 'quux'];
for (let i = 1; i <= 27; i++) {
  const nn = String(i).padStart(2, '0');
  for (const tab of tabs) {
    const hash = tab === '' ? `lesson-${nn}` : `lesson-${nn}/${tab}`;
    check(hash, expected(nn, tab));
  }
}
// Briefit
check('brief-osp1', '/kurssi/teoria/lopputyo/');
check('brief-osp2', '/kurssi/kaytto/lopputyo/');
check('brief-osp3', '/kurssi/agentit/lopputyo/');
// Tuntemattomat hashit → ei ohjausta (null)
for (const h of ['lesson-99', 'garbage', 'brief-osp9', 'lesson-05']) {
  checks++;
  const got = dest(h);
  const exp = h === 'lesson-05' ? '/kurssi/tunti-05/' : null;
  if (got !== exp) { fails++; console.error(`FAIL  #${h}  odotettu=${exp}  saatu=${got}`); }
}

console.log(`${checks} tarkistusta, ${fails} virhettä.`);
process.exit(fails ? 1 : 0);
