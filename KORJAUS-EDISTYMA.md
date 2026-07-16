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
- [~] Ei-interaktiiviset .ai-demot responsiivisiksi (viewBox/width%/height auto)  ← osin
- [ ] Interaktiiviset 07/20/24 aito mobiilitaitto (pinottu, ≥44px, ≥12–14px)
- [ ] Yhteinen komponentti + site.css; sivuvieritys-fallback poistettu
- [ ] prefers-reduced-motion + SVG-semantiikka (title/desc/role/aria-hidden)
- [ ] Diat: koko näytön painike mobiilissa ≥44px
- [ ] Playwright-mobiilitestit 320/375/390/430/768 vihreät

## P1 — sisältövirheet
- [ ] Tunti 01 (ML ≠ kaikki AI)  · [ ] Tunti 02 (akselit)  · [ ] Tunti 19 (kuusiosainen lista, ei "sielu")
- [ ] Tunti 23 (päättely vs. loki)  · [ ] Tunti 24 (ei "tuhoa kaikki käskyt")

## P1 — rytmi ja arviointi
- [ ] Päällekkäisyys 04/12, 10/11, 07/24 · ydinkysymys+tuotos per tunti
- [ ] Tunti 16 valinnainen labra · [ ] aikamitoitus 19 & 27
- [ ] Luokkatunnit: perus/tuki/syventävä reitti + tuotos
- [ ] Teoria-lopputyö: prosessinäyttö · [ ] rubriikin tasokuvaukset
- [~] Aloitussivu (sisalto/aloitus.md)  ← Codex aloittanut · [ ] toimittajariippumaton vaihtoehto

## P2 — lähteet, a11y, ylläpito
- [ ] Lähteet + tarkistuspäivä jokaiseen teoria.md:hen
- [ ] Tab-semantiikka + aria-live + reflektiolabelit
- [ ] Tuntien 16 & 27 H1/blockquote-korjaukset · [ ] lukuaika näkyvästä tekstistä
- [x] Riippuvuusversiot kiinnitetty · [x] LICENSE juuressa · [x] verify-pino (Codex)
- [ ] Tarkoitukselliset virheet merkitty/tehtäväistetty

## Julkaisuportti (vasta kun kaikki yllä `[x]`)
- [ ] `python3 generate_site.py` puhtaasti
- [ ] `npm run verify:all` vihreä (sisältö + js + Playwright/a11y)
- [ ] Ei vaakasivuylivuotoa 320–768 px
- [ ] Merge `korjaus-handoff` → `main`, push (Netlify deploy), tag `korjaus-valmis`
- [ ] (Tagi laukaisee Hermes-watchdogin → Telegram-ilmoitus Matille)

## Ajopäiväkirja (uusin ylimmäs, 1 rivi/ajokerta)
- 2026-07-16 — P0 kohderyhmä VALMIS: auditointi 3 subagentilla (33 löydöstä), korjaukset 38 lähdetiedostoon, skanneri+allowlist laajennettu, portit läpi (pedagoginen HYVÄKSYTTY, Börje puhdas), generate+verify vihreä; verify:browser ajettu taustalla (tulos kirjattu alle jos poikkeaa). Push-oikeus kuntoon (PAT). Interaktiivinen Cowork-ajo.
- 2026-07-15 — WIP committoitu, handoff + edistymätiedosto luotu, putki ajastettu.
