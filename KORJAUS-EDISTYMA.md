# Korjaushandoffin edistymä (ajastetun putken tila)

*Tämä tiedosto on ajokertojen välinen muisti. Jokainen ajokerta LUKEE tämän,
tekee seuraavan keskeneräisen kokonaisuuden, PÄIVITTÄÄ rastit ja committaa.
Ajokerrat eivät muista toisiaan — git-historia + tämä tiedosto ovat ainoa
jatkuvuus. Lähtötilanne: Codexin WIP-commit haaralla `korjaus-handoff`.*

Merkinnät: `[ ]` kesken · `[~]` työn alla · `[x]` valmis ja verifioitu.

## P0 — kohderyhmä
- [~] Yleisölupaus yhtenäistetty (kurssiopas, generate_site.py, sivut.py, meta/JSON-LD/llms.txt)  ← Codex aloittanut
- [ ] educationalLevel → perustaso/aloittelija; oppilaitosnäkymä erikseen
- [ ] 3 OSP -väite täsmennetty
- [ ] Korvauslinjan mukaiset muutokset aktiivilähteissä (ei sokkokorvausta)
- [ ] Tehtäviin ≥3 reittiä (arki/opiskelu/työ)
- [ ] Allowlist dokumentoitu; `test_yleiso.py` vihreä

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
- 2026-07-15 — WIP committoitu, handoff + edistymätiedosto luotu, putki ajastettu.
