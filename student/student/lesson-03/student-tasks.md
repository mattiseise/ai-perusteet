# Opiskelutehtävät

## Todistusaineisto 1: Miten kone oikeasti tuottaa tekstiä

Tämä on ensimmäinen kolmesta todistusaineistosta, jotka keräät Teoria-osion aikana. Käytät näitä todistusaineistoja Teoria-osion arvioitavassa tehtävässä "Tuomaripöydän päätös — asiantuntijalausunto tekoälystä" (oppitunti 9). Säilytä tämä huolellisesti.

### Tehtävä

Selitä omin sanoin (150–200 sanaa), miten kielimalli tuottaa tekstiä. Käytä apuna tämän oppitunnin käsitteitä: tokenit, parametrit, next-token prediction, lämpötila.

Kirjoita niin, että henkilö, joka ei ole koskaan käyttänyt tekoälyä, ymmärtäisi selityksesi. **Älä käytä tekoälyä tämän kirjoittamiseen** — tarkoituksena on, että sinä prosessoit oppimaasi.

Vastaa lisäksi yhteen kysymykseen: Jos kielimalli ei "ymmärrä" tekstiä, vaan ennustaa todennäköisyyksiä, mitä se tarkoittaa vastauksen luotettavuuden kannalta?

### Miksi tämä on tärkeä

"Tuomaripöydän päätös" -tehtävässä sinun täytyy analysoida skenaario, jossa tekoälyn toimintaperiaatteet aiheuttavat käytännön ongelman. Tämä todistusaineisto on valmis pohja sille analyysille — kun kirjoitat lausuntoasi, voit viitata siihen suoraan ja osoittaa ymmärryksesi tekoälyn mekanismeista.

Alla olevat harjoitustehtävät auttavat sinua keräämään kokemuksia ja havaintoja, joita voit hyödyntää todistusaineiston kirjoittamisessa.

---

## Tehtävä 3.1: Oman kielimallin testaaminen — Next-Token Simulation

### Tavoite
Ymmärtää käytännössä, miten next-token prediction toimii ja miksi malli tekee virheitä. Tämän tehtävän havainnot ovat hyödyllisiä todistusaineiston kirjoittamisessa — näet omin silmin, miten ennustaminen toimii.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

**Vaihe 1: Manuaalinen ennustus**
Anna tekstinpätkä:
"Koodi on kirjoitettu Pythonissa. Seuraava askel on..."

Ryhmä ennustaa yksitellen, mikä sana tulee seuraavaksi. Kirjoita kaikki vastaukset ylös.

**Vaihe 2: Vertailu ChatGPT:hen**
Kopioi sama teksti ChatGPT:hen. Anna kehotus: "Jatka vain seuraavalla sanalla."

Dokumentoi ChatGPT:n vastaus.

**Vaihe 3: Analyysi**
Pohdi: Oliko ChatGPT:n vastaus jonkun teistä vastaus? Jos ei, miksi se valitsi toisen sanan? Mikä on todennäköisin, ja mikä on "oikea" vastaus?

### Odotettu tuotos

Dokumentti, jossa on ryhmän ennustukset, ChatGPT:n vastaus ja analyysi siitä, miksi seuraava sana on vaikea ennustaa.

**Jos teet tehtävän yksin:**
Tee vaiheet 1–2. Anna oma ennustuksesi ja ChatGPT:n vastaus, ja pohdi sitten eroja.

---

## Tehtävä 3.2: Hallusinaatiot — tunnista väärät tiedot

### Tavoite
Nähdä konkreettisesti, miten kielimalli voi luoda vakuuttavan mutta väärän vastauksen. Tämä kokemus auttaa sinua todistusaineistossa selittämään, miksi tekoälyyn ei voi luottaa sokeasti.

### Ohjeet (pareittain tai yksin)

Kysy ChatGPT:ltä tai vastaavalta mallilta kolme hyvin spesifiä kysymystä, joiden vastauksen voit tarkistaa. Esimerkiksi: "Kuka ohjasi elokuvan 'Suuri Mahtava'?" (ei ole olemassa), "Mikä on Suomen 8. suurin kaupunki vuonna 2026?" tai "Kuka on Teknillisen korkeakoulun rehtori vuonna 2026?"

Dokumentoi jokaisen vastauksen kohdalla: mitä ChatGPT vastasi, onko vastaus oikein vai väärin, ja jos väärin — miksi malli saattoi "uskotella" näin.

### Odotettu tuotos

Dokumentti, jossa on kolme kysymystä ja ChatGPT:n vastaukset, tarkistus oikeasta vastauksesta ja lyhyt analyysi (3–5 lausetta) siitä, miten ja miksi kielimalli tuottaa hallusinaatioita.

**Jos teet tehtävän yksin:**
Tee tehtävä yhdellä kysymyksellä ja vastauksella. Analysoi se.

---

## Tehtävä 3.3: Lämpötilan vaikutus — kokeile satunnaisuuden tasoa

### Tavoite
Ymmärtää, miten lämpötila vaikuttaa kielimallin luovuuteen ja johdonmukaisuuteen. Tämä auttaa todistusaineistossa selittämään, miksi tekoäly on epädeterministinen.

### Ohjeet (pareittain tai yksin)

Jos sinulla on pääsy malliin, jossa voit säätää lämpötilaa tai luovuustasoa:

**Testi 1: Matala lämpötila (0.2)** — Anna kehotus: "Kirjoita lyhyt runo keväästä, 4 riviä." Toista sama kehotus kolme kertaa ja dokumentoi kaikki vastaukset.

**Testi 2: Korkea lämpötila (0.9)** — Anna sama kehotus kolme kertaa ja dokumentoi vastaukset.

**Analyysi:** Kumpi lämpötila tuotti samankaltaisia runoja? Kumpi tuotti erilaisia? Kumpi on parempi runon kirjoittamiseen ja miksi?

### Odotettu tuotos

Dokumentti, jossa on kolme runoa matalalla ja kolme korkealla lämpötilalla, vertailu tuloksista ja johtopäätös siitä, milloin käyttäisit mitäkin asetusta.

**Jos sinulla ei ole pääsyä lämpötilasäätöön:**
Tee tehtävä samoin, mutta dokumentoi miksi lämpötilan säätäminen voisi olla hyödyllistä.
