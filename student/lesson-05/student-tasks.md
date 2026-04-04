# Opiskelutehtävät

## Tehtävä 5.1: Konteksti-ikkunan hallinta — Token-laskenta ja pilkkomisen käytäntö

### Tavoite
Ymmärtää käytännössä, miten suuria IT-tehtäviä pilkotaan, jotta tekoälyn konteksti-ikkuna ei täyttyisi. Harjoitella dokumentointi- ja ankkurointitekniikkaa.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

1. **Valitsette suuri IT-tehtävä**, jonka normaalisti käsittelisitte tekoälyn kanssa useassa vaiheessa. Esimerkiksi:
   - 5000 rivin SQL-tietokanta-skeeman analysointi
   - 3000 rivin lokitiedoston debugging
   - 2000 rivin koodin refaktorointi

2. **Arvioidaan tehtävän tokeni-koko:**
   - Kopioi tehtävä ChatGPT:hin tai toiseen malliin, joka näyttää token-luvun.
   - Dokumentoi: "Tämä tehtävä on noin X tokenia."
   - Vertaa mallin konteksti-ikkunaan. Jos ikkuna on 128 000 tokenia, miten monta toistoa tehtävää mahtuisi?

3. **Pilkotaan tehtävä pienemmiksi osiksi:**
   - Suunnittelulta, kuinka jaat tehtävän. Esimerkiksi:
     - "Tietokanta: Analysoitaan taulukot 1-50, sitten 51-100, sitten 101-150"
     - "Logi: Analysoitaan tunnin välein (6 eri logia)"
     - "Koodi: Pilkotaan moduuleittain (3-4 moduulia)"
   - Dokumentoi pilkkomissuunnitelma taulukkoon:

| Osa | Tokenit | Pääkysymys | Ankkuri (mitä toistaa seuraavassa osassa) |
|-----|---------|-----------|---------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

4. **Ankkurointitekniikan harjoitus:**
   - Kirjoita "ankkuri-konteksti", jonka käytät jokaisen osan alussa:
     - "Projektierityinen: [yhteenveto siitä mitä teet]"
     - "Edellisen osan tulokset: [yhteenveto edellisesta osasta]"
     - "Seuraavaksi: [mitä teet tässä osassa]"

5. **Dokumentaatio:**
   - Luo yhden sivun dokumentti, joka näyttää suunnitelmasi:
     - Tehtävä ja sen koko
     - Pilkkomisstrategia
     - Ankkuri-kontekstit jokaista osaa varten

### Odotettu tuotos
- Täytetty pilkkomis-taulukko
- Ankkuri-konteksti-mallit (3-4 kpl)
- 1-sivuinen suunnitelma-dokumentti

**Jos teet tehtävän yksin:**
Valitse itsellesi sopiva tehtävä ja tee kaikki vaiheet. Testaa suunnitelmaasi dokumentoimalla sitä.

---

## Tehtävä 5.2: Pitkä projekti pilkottuna — Kahden päivän simulaatio

### Tavoite
Simuloida oikeaa pitkää IT-projektia tekoälyn kanssa, jossa konteksti-ikkuna hallitaan pilkomisen ja ankkuroinnin avulla. Nähdä käytännössä, miten tieto säilyttää järkevyydelle.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

1. **Valitsette simuloidun 2-päivän projektin.** Voi olla:
   - "Tietokannan suunnittelu": Päivä 1 analysoidaan vaatimukset, Päivä 2 suunnitellaan rakenne
   - "Ohjelman debuggaaminen": Päivä 1 etsitään virhe, Päivä 2 korjataan
   - "Dokumentaation kirjoittaminen": Päivä 1 raakaluonnos, Päivä 2 editointi

2. **Päivä 1 — Ensimmäinen keskustelu:**
   - Kirjoitatte alustavalle tekoälylle ankkuri-kontekstin:
     - Rooli, tausta, tavoite, rajaukset, esimerkit (kuten oppitunnissa 4)
     - Lisäksi: "Tämä on 2-päivän projekti. Älä unohda näitä vaatimuksia."
   - Teette ensimmäisen tehtävää koskevan kysymyksen.
   - Dokumentoitte tekoälyn vastauksen ja erityisesti **olennainen tieto**, joka täytyy muistaa.

3. **Siirtymä päivän 1:sta 2:een (dokumentointi):**
   - Tiivistetään Päivä 1:n tulokset 200-300 sanaan.
   - Dokumentoitte: "Mitä saimme selville? Mitä täytyy muistaa? Mitkä ovat avain-oivallukset?"

4. **Päivä 2 — Toinen keskustelu (puhdas ikkuna):**
   - Aloitatte **uudelta** tekoälyltä (uusi chat, puhdas ikkuna).
   - Kirjoitatte päivittynyt ankkuri-konteksti:
     - "Jatkamme 2-päivän projektista. Päivä 1 tulokset: [yhteenveto]."
     - Toistatte oleellisen taustan (jotka voivat olla unohdettu).
     - Esitätte Päivä 2:n tehtävän.
   - Dokumentoitte vastauksen.

5. **Analyysi — Vertailu kahden päivän välillä:**
   - Vastasiko Päivä 2:n vastaus johdonmukaisesti Päivä 1:n kanssa?
   - Oliko tekoäly palauttava muistin Päivä 1:stä ankkuroinnin avulla?
   - Mitä olisi mennyt pieleen ilman dokumentointia?

### Odotettu tuotos
- Dokumentti, joka sisältää:
  - Päivä 1 ankkuri-konteksti
  - Päivä 1 tulokset (lyhennetty)
  - Päivä 2 ankkuri-konteksti (päivitetty)
  - Päivä 2 tulokset
  - Vertailu-analyysi: Oliko projekti johdonmukainen? Oliko tieto säilynyt?

**Jos teet tehtävän yksin:**
Simuloi projektin kaksi päivää oikeasti. Kirjoita dokumentointia ja katso, miten hyvin muisti toimii ilman ankkurointia vs. ankkuroinnilla.
