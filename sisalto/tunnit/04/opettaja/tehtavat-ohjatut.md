# Opettajavetoiset tehtävät

## Tehtävä 4.1: Sama kysymys, kaksi kontekstia — käytännön vertailu luokassa

### Tavoite

Tehtävän tavoitteena on havainnollistaa, kuinka paljon **konteksti** ja **prompti** vaikuttavat tekoälyn vastauksen hyödyllisyyteen. Opiskelijat näkevät konkreettisesti, että parempi vastaus ei synny pelkästään “paremmasta kysymyksestä”, vaan hyvästä kontekstista ja sen pohjalta rakennetusta täsmällisestä promptista.

**Opettajan painotus:** Korosta, että konteksti antaa tekoälylle taustatiedon ja prompti kertoo, mitä tekoälyn pitää tehdä. Hyvä vastaus syntyy yleensä näiden kahden yhteistyöstä.

### Opettajan ohjeet ja fasilitointi

**Valmistelu noin 5 minuuttia ennen oppituntia:**

1. Valitse aihe opiskelijoiden arjesta. Sopivia ovat esimerkiksi **harrastusprojektin suunnittelu**, **kesätyöhakemus**, **treeniohjelma** tai **koulutehtävän jäsentely**. Jos ryhmällä on IT-taustaa, voit käyttää myös teknistä aihetta.
2. Kirjoita valmiiksi kaksi kyselyä samasta aiheesta:
   - **Heikko kysymys:** yksittäinen lause ilman kontekstia, esimerkiksi `Kuinka teen hyvän kesätyöhakemuksen?`
   - **Hyvä kysymys:** sisältää vahvan kontekstin, kuten roolin, taustan, tavoitteen, rajaukset ja esimerkin, sekä täsmällisen promptin, jossa määritellään tehtävä, rooli, rajat, formaatti ja mahdolliset esimerkit.

### Toteutus noin 20 minuuttia

1. **Johdanto noin 3 minuuttia:**


   Näytä opiskelijoille molemmat kysymykset rinnakkain ruudulla.

   Kerro opiskelijoille:

   > Käytämme samaa tekoälyä kaksi kertaa. Ensimmäisellä kerralla kysymys on heikko ja ilman kontekstia. Toisella kerralla annamme hyvän kontekstin ja täsmällisen promptin. Lopuksi vertaamme vastauksia.
2. **Kysely 1: ilman kontekstia ja heikolla promptilla noin 5 minuuttia:**

   1. Lähetä heikko kysymys tekoälylle opiskelijoiden nähden.
   2. Lue vastaus ääneen tai näytä se ruudulla.
   3. Kysy luokalta:
      - Kuinka hyödyllinen tämä vastaus on?
      - Mitä tietoa vastauksesta puuttuu?
      - Mitkä kontekstin osat puuttuivat kysymyksestä?
      - Kuinka pitkä vastaus on? Voitte arvioida sanamäärän tai rivien määrän.
      - Mille osaamistasolle vastaus näyttää olevan suunnattu?
3. **Kysely 2: hyvällä kontekstilla ja täsmällisellä promptilla noin 5 minuuttia:**

   1. Lähetä hyvä kysymys samalle tekoälylle.
   2. Lue vastaus ääneen tai näytä se ruudulla.
   3. Kysy luokalta:
      - Kuinka paljon hyödyllisempi tämä vastaus on?
      - Mitkä kontekstin osat auttoivat tekoälyä?
      - Millä tavalla prompti teki pyynnöstä täsmällisen?
      - Voisiko tätä vastausta käyttää suoraan omassa projektissa? Miksi tai miksi ei?
4. **Analyysi ja pohdinta noin 7 minuuttia:**

   Kirjoita taululle tai näytä seuraava vertailutaulukko:

   | Arvioitava asia | Vastaus 1: heikko kysymys | Vastaus 2: hyvä konteksti ja prompti |
   | --- | --- | --- |
   | **Pituus** |  |  |
   | **Tarkkuus** |  |  |
   | **Soveltuvuus opiskelijan tilanteeseen** |  |  |
   | **Osaamistaso** |  |  |
   | **Käytännön hyödynnettävyys** |  |  |

   Keskustelkaa yhdessä:

   - Muuttuiko tekoäly vai muuttuivatko konteksti ja prompti?
   - Mitä kontekstin osia käytettiin?
   - Mitkä promptin elementit tekivät pyynnöstä selkeän?
   - Kumpi vaikutti vastaukseen enemmän: konteksti vai prompti?

### Fasilitointikysymykset

- Jos opiskelija sanoo, että ensimmäinen vastaus oli hyvin yleinen, kysy: **Miksi se oli yleinen? Mitä tekoäly ei tiennyt tilanteesta?**
- Jos opiskelija sanoo, että toinen vastaus oli pidempi, kysy: **Oliko pituus ongelma vai oliko vastaus tarkempi ja paremmin kohdistettu?**
- Kysy lopuksi: **Konteksti antaa pohjan ja prompti esittää pyynnön. Kumpi oli tässä esimerkissä tärkeämpi?**

**Esimerkki opetukseen**

Kirjoita taululle lause: “Huono prompti pakottaa tekoälyn arvaamaan tilanteen. Hyvä konteksti vähentää arvailua.” Palaa tähän ajatukseen, kun opiskelijat vertaavat vastauksia.

### Odotettu oppimistulos

Tehtävän jälkeen opiskelijat ymmärtävät, että:

- **konteksti** ja **prompti** yhdessä vaikuttavat tekoälyn vastauksen laatuun,
- hyvä konteksti ja täsmällinen prompti voivat säästää aikaa ja tuottaa käyttökelpoisempia vastauksia,
- kontekstin osat ja promptin elementit voidaan tunnistaa käytännön esimerkeistä,
- hyvä konteksti ja hyvä prompti eivät ole sama asia, vaikka ne toimivat yhdessä.

---

## Tehtävä 4.2: Kontekstin ja promptin rakentaminen yhdessä — ohjattu kirjoittaminen ryhmässä

### Tavoite

Tehtävän tavoitteena on harjoitella **kontekstin** ja **promptin** rakentamista vaihe vaiheelta opettajan ohjauksessa. Opiskelijat näkevät, miten viiden komponentin konteksti ja viiden elementin prompti toimivat yhdessä.

**Opettajan painotus:** Konteksti on pohja, prompti on sen päälle rakennettu pyyntö. Jos konteksti puuttuu, tekoäly joutuu arvaamaan. Jos prompti on epäselvä, tekoäly ei tiedä tarkasti, mitä sen pitäisi tehdä.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**

1. Valitse arkinen ongelma, jonka opiskelijat tunnistavat. Sopiva aihe on esimerkiksi **puhelin ei yhdistä kodin WiFi-verkkoon** tai muu vastaava arjen pulma.
2. Kirjoita taululle tai diaan:
   - viiden komponentin kontekstin malli,
   - viiden elementin promptin malli.

### Asetelman muutos noin 2 minuuttia

Kerro opiskelijoille:

> Nyt rakennamme sekä kontekstin että promptin yhdessä vaiheittain. Konteksti on pohja, prompti on kysymys tai tehtävänanto sen päälle.

---

### Kontekstin rakentaminen noin 15 minuuttia

#### Vaihe 1: Rooli noin 3 minuuttia

Kirjoita taululle:

KONTEKSTI — Rooli: \_\_\_\_\_\_

Kysy opiskelijoilta:

- Keitä olemme tässä ongelmassa?
- Mikä on osaamistasomme?
- Vastaako tekoäly opiskelijalle, aloittelijalle vai vastuulliselle käyttäjälle?

Täyttäkää yhdessä esimerkiksi:

`Olen tavallinen käyttäjä, en tekninen asiantuntija. Käytän Android-puhelinta.`

**Selitys:** Rooli auttaa tekoälyä valitsemaan sopivan vastaustason.

#### Vaihe 2: Taustatieto noin 3 minuuttia

Kirjoita taululle:

Taustatieto: \_\_\_\_\_\_

Kysy opiskelijoilta:

- Mitä olemme jo yrittäneet?
- Mitä tiedämme järjestelmästä?
- Mikä virhe tai ongelma on havaittu?

Täyttäkää esimerkiksi:

`Muut laitteet yhdistävät verkkoon normaalisti. Puhelin näkee verkon, mutta yhteys epäonnistuu. Olen jo kokeillut käynnistää puhelimen uudelleen.`

**Selitys:** Taustatieto auttaa tekoälyä välttämään arvailua ja toistamasta asioita, jotka on jo kokeiltu.

#### Vaihe 3: Tavoite noin 3 minuuttia

Kirjoita taululle:

Tavoite: \_\_\_\_\_\_

Kysy opiskelijoilta:

- Mitä haluamme saavuttaa?
- Miksi tämä ongelma pitää ratkaista?
- Miltä onnistunut lopputulos näyttää?

Täyttäkää esimerkiksi:

`Haluan saada puhelimen yhdistettyä kotiverkkoon.`

**Selitys:** Tavoite kohdistaa vastauksen siihen, mitä käyttäjä oikeasti yrittää saada aikaan.

#### Vaihe 4: Rajaukset noin 2 minuuttia

Kirjoita taululle:

Rajaukset: \_\_\_\_\_\_

Kysy opiskelijoilta:

- Mitä emme halua tehdä?
- Mitä lähestymistapoja haluamme välttää?
- Mihin vastaus ei saa käyttää aikaa?

Täyttäkää esimerkiksi:

`En halua nollata reititintä, koska muut laitteet toimivat. Haluan ensin ymmärtää, mistä puhelimen ongelma johtuu.`

**Selitys:** Rajaukset poistavat turhia tai riskialttiita vaihtoehtoja.

#### Vaihe 5: Esimerkki noin 2 minuuttia

Kirjoita taululle:

Esimerkki: \_\_\_\_\_\_

Kysy opiskelijoilta:

- Voimmeko antaa virheilmoituksen?
- Voimmeko näyttää komennon tai koodinäytteen?
- Mikä konkreettinen havainto auttaa tekoälyä ymmärtämään ongelman?

Täyttäkää esimerkiksi:

Esimerkki näytöllä näkyvästä viestistä: "Yhdistetään…"

Sitten ilmestyy: "Todennusvirhe".

**Selitys:** Esimerkki auttaa tekoälyä näkemään tarkasti, mitä tilanteessa tapahtuu.

#### Lopullinen konteksti noin 2 minuuttia

Kirjoita kaikki osat yhteen:

> Olen tavallinen käyttäjä, en tekninen asiantuntija, ja käytän Android-puhelinta. Puhelin ei yhdistä kodin WiFi-verkkoon, vaikka muut laitteet yhdistävät normaalisti. Puhelin näkee verkon, mutta yhteys epäonnistuu, ja olen jo kokeillut käynnistää puhelimen uudelleen. Tavoitteeni on saada puhelin yhdistettyä. En halua nollata reititintä, koska muut laitteet toimivat. Näytöllä lukee ensin "Yhdistetään…" ja sitten "Todennusvirhe".

Kerro opiskelijoille:

> Konteksti on valmis. Seuraavaksi rakennamme sen päälle täsmällisen promptin.

---

### Promptin rakentaminen noin 12 minuuttia

#### Vaihe 6: Promptin tavoite noin 2 minuuttia

Kirjoita taululle:

PROMPTI — Tavoite: \_\_\_\_\_\_

Kysy opiskelijoilta:

- Mitä haluamme tekoälyn tekevän juuri nyt?
- Haluammeko selityksen, listan, vaiheittaisen ohjeen vai tarkistuslistan?

Täyttäkää esimerkiksi:

`Auta minua selvittämään, miksi puhelin ei yhdistä WiFi-verkkoon.`

**Selitys:** Promptin tavoite kertoo tekoälylle, mikä tehtävä sen pitää suorittaa.

#### Vaihe 7: Promptin rooli noin 2 minuuttia

Kirjoita taululle:

Rooli promptissa: \_\_\_\_\_\_

Kysy opiskelijoilta:

- Millä tasolla tekoälyn pitää vastata?
- Haluammeko vastauksen aloittelijalle, opiskelijalle vai asiantuntijalle?

Täyttäkää esimerkiksi:

`Vastaa kuin opettaisit aloittelijaa. Älä käytä liian syvälle menevää tekniikkaa.`

**Selitys:** Rooli varmistaa, että vastaus on sopivalla tasolla.

#### Vaihe 8: Rajat noin 2 minuuttia

Kirjoita taululle:

Rajat: \_\_\_\_\_\_

Kysy opiskelijoilta:

- Mitä emme halua vastauksessa?
- Mihin ongelman osaan tekoälyn pitää keskittyä?
- Mitä ratkaisuja pitää välttää turvallisuuden tai oppimisen vuoksi?

Täyttäkää esimerkiksi:

`Älä ehdota reitittimen nollausta. Keskity puhelimen asetuksiin.`

**Selitys:** Rajat pitävät vastauksen fokuksessa ja vähentävät turhia tai riskialttiita ehdotuksia.

#### Vaihe 9: Formaatti noin 2 minuuttia

Kirjoita taululle:

Formaatti: \_\_\_\_\_\_

Kysy opiskelijoilta:

- Miten haluamme vastauksen muotoiltavan?
- Tarvitaanko numeroitu lista, taulukko, tarkistuslista vai lyhyt yhteenveto?

Täyttäkää esimerkiksi:

`Vastaa numeroituina vaiheina. Selitä jokaisen vaiheen kohdalla, mitä tehdään ja miksi se tehdään.`

**Selitys:** Formaatti tekee vastauksesta helpommin käytettävän.

#### Vaihe 10: Esimerkki noin 2 minuuttia

Kirjoita taululle:

Esimerkki hyvästä vastaustyylistä: \_\_\_\_\_\_

Kysy opiskelijoilta:

- Voimmeko näyttää mallin siitä, millainen vastaus olisi hyödyllinen?
- Miltä yksi hyvä vaihe voisi näyttää?

Täyttäkää esimerkiksi:

Vaihe 1: Unohda verkko puhelimen asetuksista ja yhdistä uudelleen salasanalla. Tämä poistaa vanhan, ehkä virheellisen tallennetun salasanan.

**Selitys:** Esimerkki tekee vaatimuksista konkreettisia.

#### Lopullinen prompti noin 2 minuuttia

Kirjoita taululle lopullinen täsmällinen prompti, joka hyödyntää aiemmin rakennettua kontekstia:

> Auta minua selvittämään, miksi puhelin ei yhdistä WiFi-verkkoon. Vastaa kuin neuvoisit aloittelijaa. Älä käytä liian teknistä kieltä, äläkä ehdota reitittimen nollausta. Keskity puhelimen asetuksiin. Vastaa numeroituina vaiheina. Selitä jokaisen vaiheen kohdalla, mitä tehdään ja miksi se tehdään. Esimerkiksi: “Vaihe 1: Unohda verkko puhelimen asetuksista ja yhdistä uudelleen salasanalla. Tämä poistaa vanhan, ehkä virheellisen tallennetun salasanan.”

Kerro opiskelijoille:

> Tämä on täsmällinen, kontekstiin perustuva prompti. Se ei vain kysy apua, vaan kertoo, missä tilanteessa olemme, mitä haluamme, mitä emme halua ja millaisessa muodossa vastauksen pitää olla.

### Fasilitointikysymykset

- Mitä tapahtuisi, jos jättäisimme roolin pois kontekstista?
- Kuinka erilainen vastaus olisi ilman taustatietoja?
- Mitä eroa on kontekstin roolilla ja promptin roolilla?
- Voimmeko käyttää samaa promptia ilman kontekstia? Miksi tai miksi ei?
- Mikä osa paransi vastausta eniten: rooli, taustatieto, tavoite, rajaus vai esimerkki?

### Odotettu oppimistulos

Tehtävän jälkeen opiskelijat ymmärtävät, että:

- jokaisella kontekstin komponentilla ja promptin elementillä on oma tarkoituksensa,
- **konteksti** on pohja ja **prompti** on sen päälle rakennettu tarkka pyyntö,
- omasta kysymyksestä voi tunnistaa puuttuvia kontekstin tai promptin osia,
- konteksti ja prompti toimivat yhdessä: konteksti antaa taustatiedon ja prompti ohjaa toimintaa.

---

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- selittää, miten **konteksti** vaikuttaa tekoälyn vastauksen laatuun,
- erottaa **konteksti** ja **prompti** toisistaan,
- tunnistaa hyvän kontekstin keskeiset osat, kuten roolin, taustatiedon, tavoitteen, rajaukset ja esimerkin,
- tunnistaa hyvän promptin elementit, kuten tavoitteen, roolin, rajat, formaatin ja esimerkit,
- rakentaa arkiseen ongelmaan kontekstin ja sen pohjalle täsmällisen promptin,
- arvioida, miksi yksi tekoälyn vastaus on hyödyllisempi kuin toinen.

---
