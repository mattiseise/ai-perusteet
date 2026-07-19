# Korjaushandoffin edistymä (ajastetun putken tila)

*Tämä tiedosto on ajokertojen välinen muisti. Jokainen ajokerta LUKEE tämän,
tekee seuraavan keskeneräisen kokonaisuuden, PÄIVITTÄÄ rastit ja committaa.
Ajokerrat eivät muista toisiaan — git-historia + tämä tiedosto ovat ainoa
jatkuvuus. Lähtötilanne: Codexin WIP-commit haaralla `korjaus-handoff`.*

Merkinnät: `[ ]` kesken · `[~]` työn alla · `[x]` valmis ja verifioitu.

## P0 — kohderyhmä
- [x] Yleisölupaus yhtenäistetty (kurssiopas, generate_site.py, sivut.py, meta/JSON-LD/llms.txt) — keskitetty kurssi.yaml:iin, generoitu sivusto käyttää
- [x] educationalLevel → perustaso/aloittelija; oppilaitosnäkymä erikseen (kurssi.yaml: "Aloittelija / perustaso", JSON-LD:ssä)
- [x] 3 OSP -väite täsmennetty (laajuuskuvaus: kurssi.yaml, kurssiopas, aloitus.md, llms.txt)
- [x] Korvauslinjan mukaiset muutokset aktiivilähteissä (ei sokkokorvausta) — 2026-07-16: myös skanneria kiertäneet taivutusmuodot (omalta alaltasi, organisaatiosi, yrityksesi, työkaverisi, oppilaitoksesi ym.) korjattu 38 lähdetiedostosta, ml. tunti 13 dia (cairosvg-tarkistettu)
- [x] Tehtäviin ≥3 reittiä (arki/opiskelu/työ) — auditoitu kaikki 27 tuntia + lopputyöt (3 Opus-subagenttia), 34 korjausta; annetut rooliskenaariot säilytetty
- [x] Allowlist dokumentoitu; `test_yleiso.py` vihreä — skanneriin 12 uutta taivutusmuotopatternia, 6 perusteltua allowlist-riviä

## P0 — mobiiligrafiikat
- [x] Ei-interaktiiviset .ai-demot responsiivisiksi — 23 staattista demoa reflow-kortilla (≤430 px), fitAiDemos-skaalaus 431–680 px -välillä (main-merge, reflow ensisijainen Matin linjauksella)
- [x] Interaktiiviset 07/20/24 aito mobiilitaitto (pinottu, ≥44px, ≥12–14px; fitAiDemos ohittaa ne)
- [x] Yhteinen komponentti + site.css (annotate_demos + _DEMO_MOBILE_MODELS); sivuvieritys-fallback poistettu
- [x] prefers-reduced-motion (globaali site.css + demokohtaiset) + SVG-semantiikka: diat 344 kpl role=img+title (generaattori annotoi), tunnin 16 koriste-SVG aria-hidden
- [x] Diat: koko näytön painike ≥44px (site.css min-width/height 44px, ei kavennettu mobiilissa)
- [x] Playwright-mobiilitestit 320/375/390/430/768 vihreät (5/5 + axe 96 sivua)

## P1 — sisältövirheet
- [x] Tunti 01 (ML ≠ kaikki AI)  · [x] Tunti 02 (akselit)  · [x] Tunti 19 (kuusiosainen lista, ei "sielu")
- [x] Tunti 23 (päättely vs. loki)  · [x] Tunti 24 (ei "tuhoa kaikki käskyt")

## P1 — rytmi ja arviointi
- [x] Päällekkäisyys 04/12, 10/11, 07/24 · ydinkysymys+tuotos per tunti (rajaus + oma tuotos joka tunnilla, Codex)
- [x] Tunti 16 valinnainen labra · [x] aikamitoitus 19 & 27 (27: testivaatimus yhtenäistetty 9+2:een kaikissa lähteissä 2026-07-19)
- [x] Luokkatunnit: 90 min -taulukko + tuki/syventävä reitti + tallennettava tuotos kaikissa 27 tuntisuunnitelmassa
- [x] Teoria-lopputyö: prosessinäyttö (prompti/loki, ≥3 korjausta, lähteet, puolustus) · [x] rubriikin tasokuvaukset (5 tasoa, kaikki 3 lopputyötä)
- [x] Aloitussivu (sisalto/aloitus.md, livenä /kurssi/-etusivulla; työkirja md+Word+PDF-tulostus) · [x] toimittajariippumaton vaihtoehto (aloitus.md + tunti 18 + lopputyörubriikit)

## P2 — lähteet, a11y, ylläpito
- [x] Lähteet + tarkistuspäivä jokaiseen teoria.md:hen (27/27, test_content.py vartioi; tuotetiedot "Tilanne heinäkuussa 2026" -laatikoissa)
- [x] Tab-semantiikka + aria-live + reflektiolabelit (tablist/tab/tabpanel + nuolinäppäimet; test_a11y.py vartioi)
- [x] Tuntien 16 & 27 H1/blockquote-korjaukset (1 H1/tiedosto, ei sisäkkäisiä lainauksia) · [x] lukuaika näkyvästä tekstistä (_VisibleTextParser ohittaa style/script/svg/demo-UI:n)
- [x] Riippuvuusversiot kiinnitetty · [x] LICENSE juuressa · [x] verify-pino (Codex)
- [x] Tarkoitukselliset virheet merkitty/tehtäväistetty — loppukatselmus 2026-07-19 PUHDAS (112 tehtävää, 73 spot-segmenttiä flag+explain, tunnin 07 väitedemot merkitty ✗ keksitty)

## Julkaisuportti (vasta kun kaikki yllä `[x]`)
- [x] `python3 generate_site.py` puhtaasti (2026-07-19)
- [x] `npm run verify:all` vihreä (sisältö + js + Playwright/a11y, 5/5 + axe 96 sivua)
- [x] Ei vaakasivuylivuotoa 320–768 px (Playwright-testit 1–2)
- [x] Merge `korjaus-handoff` → `main`, push (Netlify deploy), tag `korjaus-valmis`
- [x] (Tagi laukaisee Hermes-watchdogin → Telegram-ilmoitus Matille)

## Ajopäiväkirja (uusin ylimmäs, 1 rivi/ajokerta)
- 2026-07-19 (ilta, interaktiivinen istunto Matin kanssa) — KAIKKI VALMIS JA JULKAISTU: Matti linjasi mobiiliristiriidan (reflow ensisijainen, fitAiDemos fallbackiksi) → main mergetty haaralle konfliktiratkaisulla (fitAiDemos ohittaa interaktiivit + jättää reflow-kortin stagen lapseksi). 3 auditointiagenttia kartoitti Codexin WIP:n todellisen tilan: P0 mobiili, P1 rytmi ja P2 olivat valtaosin jo tehtyjä, rastit vanhentuneita. Täydennetty aukot: diojen SVG-semantiikka (344 diaa, generaattoriannotointi), tunnin 16 koriste-SVG, tunnin 27 testivaatimus 15→9+2 (pedagoginen tarkistus HYVÄKSYTTY + Börje), työkirjan Word-vienti, tarkoituksellisten virheiden loppukatselmus (PUHDAS). Kaikki portit vihreät → merge mainiin + tag korjaus-valmis.
- 2026-07-19 — P1 sisältövirheet VALMIS (tunnit 01/02/19/23/24): Codexin WIP oli jo kirjoittanut korjaukset lähteisiin, mutta rasteja ei ollut päivitetty. Verifioitu jokaista P1-vaatimusta vasten + itsenäinen pedagoginen tarkistus (Opus-subagentti) → KOKONAISVERDIKTI HYVÄKSYTTY, kaikki 5 PASS, ei termilukkorikkeitä. generate+verify vihreä. ESTE (P0 mobiiligrafiikat): Matti pushasi mainiin 2026-07-19 21:50 (807188a) JS-skaalaukseen perustuvan fitAiDemos-korjauksen, joka on ristiriidassa toimeksiannon "aito uudelleentaitto, ei prosenttiskaalausta" -vaatimuksen JA haaran valmiin reflow-lähestymistavan (.ai-demo__mobile-model) kanssa. Kumpi jää voimaan on Matin päätös — en arvaa villisti. Haara jätetty main-mergen taakse (turvallista); mobiiligrafiikkayksikkö odottaa Matin linjausta ennen kuin sen voi viedä valmiiksi ja mergetä. Playwright TOIMII tässä sandboxissa (macOS, chromium asennettu) toisin kuin edellisellä Linux-ajolla.
- 2026-07-16 — P0 kohderyhmä VALMIS: auditointi 3 subagentilla (33 löydöstä), korjaukset 38 lähdetiedostoon, skanneri+allowlist laajennettu, portit läpi (pedagoginen HYVÄKSYTTY, Börje puhdas), generate+verify vihreä. ESTE: verify:browser ei aja tässä sandboxissa (chromiumin järjestelmäkirjastot puuttuvat, ei root-oikeuksia) — dian 13 muutos verifioitu cairosvg-renderöinnillä; Playwright-portti ajettava julkaisuportilla ympäristössä, jossa selain toimii. Push-oikeus kuntoon (PAT). Interaktiivinen Cowork-ajo.
- 2026-07-15 — WIP committoitu, handoff + edistymätiedosto luotu, putki ajastettu.
