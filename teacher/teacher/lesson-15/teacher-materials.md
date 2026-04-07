# Opettajan materiaalit — Oma botti II

## Oppimisen tavoitteet tälle tunnille

Tämän tunnin jälkeen opiskelija:
1. Ymmärtää, että **tietopohja** on kriittinen osa hyvää bottia — se on tieto, jonka perusteella botti vastaa.
2. Osaa tunnistaa eri tietopohjan lähteitä ja tietää, milloin kussakin on parasta käyttää.
3. Ymmärtää **rajaukset** käytännön tasolla — kuinka ne kirjoitetaan ja miksi ne suojaavat sekä käyttäjää että bottia.
4. Osaa **testata** bottia systemaattisesti kolmella tavalla: positiivisesti, negatiivisesti ja reunatapauksissa.
5. Ymmärtää **iteraation** — että testaaminen ja parantaminen on jatkuva prosessi, ei kertaluonteinen työ.
6. Osaa dokumentoida testejään selkeästi, jotta näkee mitä toimii ja mikä tarvitsee parantamista.

Punainen lanka: "Kohti tuotantokvaliteettista bottia" — Tämä oppitunti opettaa, miten tehdään botti, joka ei vain toimi vaan **toimii luotettavasti**.

---

## Yleisiä väärinkäsityksiä

### 1. "Tietopohja on valinnainen — botti osaa kaikki mitä ChatGPT tietää."

**Todellisuus:** ChatGPT:llä on yleinen tieto joka opetettiin harjoitusdatalla. Se ei tiedä:
- Organisaation sisäisiä prosesseja
- Ajankohtaista tai muuttuvaa tietoa
- Salaista tai yksityistä dataa
- Hyper-spesifikoituja ohjeita

Ilman tietopohjaa botti arvailee ja antaa väärää tietoa.

### 2. "Rajaukset ovat rajoittavia ja epäystävällisiä."

**Todellisuus:** Rajaukset ovat **vastuullisia**. Ne osoittavat käyttäjälle, mitä botti osaa ja mitä ei. Se on parempi kuin että botti antaa virheellisiä neuvoja, joihin käyttäjä luottaa.

Esimerkki: "En osaa antaa sijoitusneuvoja" on parempi kuin että botti antaa väärän tai vaarallisen neuvon.

### 3. "Testaaminen on yksinkertaista — ajat kysymyksen ja katso mitä tapahtuu."

**Todellisuus:** Oikea testaaminen on systemaattista ja suunniteltua. Se sisältää:
- Positiivisia testejä (mitä pitäisi toimia)
- Negatiivisia testejä (mitä ei pitäisi toimia)
- Reunatapauksia (outoja tilanteita)

Satunnainen testaaminen jättää piilotetut ongelmat löytämättä.

### 4. "Iteraatio on merkki siitä, että suunnittelu epäonnistui."

**Todellisuus:** Iteraatio on **normaali** osa bottin kehitystä. Ensimmäinen versio harvoin on täydellinen. Hyvät botit syntyvät testaamalla, parannuksilla ja uudella testaamisella.

### 5. "Tietopohjaa ei tarvitse päivittää — kerran tehty, aina voimassa."

**Todellisuus:** Tietopohja vanhentuu nopeasti. Jos organisaation prosessit muuttuvat ja tietopohja ei päivity, botti antaa vanhentunutta tietoa. Vanhentuneet ohjeet voivat aiheuttaa:
- Käyttäjien tekemät virheelliset päätökset
- Turvallisuusongelmia
- Asiakastyytyväisyyden laskua

---

## Opettajan fasilitointiohjeet

### Ennen lähiosaa

- Valitse yksi yksinkertainen, testattava botti
  - Esim. IT-helpdesk, opastus, tietojen haku
  - Varmista, että sillä on selkeä tarkoitus ja rajaukset

- Valmista yksi dokumentti (PDF tai teksti)
  - Esim. FAQ, käyttöohje, tai prosessikuvaus
  - Tämä on tietopohja, jonka käytät live-demossa

- Testaa botti ilman tietopohjaa
  - Mitä se vastaa?
  - Onko vastaus epämääräinen tai väärä?

- Lataa dokumentti botille
  - Näytä prosessi selvästi
  - Testaa uudelleen samalla kysymyksellä
  - Näytä ero

- Valmista testauspohja
  - Näytä, kuinka positiivinen, negatiivinen ja reunatapaus-testit dokumentoidaan
  - Antaa opiskelijoille selkeä pohja

### Lähiosassa (90 minuuttia)

1. **Tehtävä 15.1** (20 min): Live-demo — tietopohjadokumentin vaikutus
2. **Tehtävä 15.2** (30 min): Ryhmät testaavat bottia systemaattisesti
3. **Tehtävä 15.3** (20 min): Keskustelu rajauksista ja turvallisuudesta
4. **Vapaa harjoittelu** (20 min): Opiskelijat aloittavat opiskelijatehtävät

### Yleinen neuvo

- **Tietopohjasta**: Selitä, että se on bottiin syötetty tieto. Se ei ole arvausta — se on faktaa, jonka perusteella botti vastaa. Tietopohjan laatu määrittää vastausten laadun.

- **Rajauksista**: Näytä, että rajaukset eivät ole negatiivisia. Ne ovat vastuullisia. Ne suojaavat käyttäjää ja bottia.

- **Testauksesta**: Selitä, että satunnainen testaaminen ei riitä. Systemaattinen testaaminen löytää ongelmia, joita satunnainen testaaminen ei löydä.

- **Iteraatiosta**: Näytä, että testaaminen → korjaus → testaaminen uudelleen on normaali prosessi. Se ei ole merkki epäonnistumisesta.

---

## Tarkistustehtävät (oppimisen varmistaminen)

### 1. Tietopohjasta
**"Miksi botti tarvitsee tietopohjaa? Eikö se osaa kaiken, mitä ChatGPT tietää?"**
- *Mitä etsit:* Opiskelija ymmärtää, että ChatGPT tietää yleistä asiaa, mutta ei organisaation sisäisiä asioita, ajankohtaista tietoa tai spesifikoituja ohjeita. Tietopohja tekee botista **räätälöidyn**.

### 2. Rajauksista
**"Miksi botti tarvitsee rajauksia? Eikö se voi vain vastata kaikkeen?"**
- *Mitä etsit:* Opiskelija ymmärtää, että rajaukset suojaavat käyttäjää väärältä tiedolta ja bottia sopimattomista tilanteista. Ne tekevät botista **vastuullisen**.

### 3. Positiivisesta testauksesta
**"Mitä positiivinen testaus tarkoittaa?"**
- *Mitä etsit:* Opiskelija ymmärtää, että positiivinen testaus testaa asioita, joiden pitäisi toimia. Se varmistaa, että botti osaa perustyönsä.

### 4. Negatiivisesta testauksesta
**"Mitä negatiivinen testaus tarkoittaa? Miksi se on tärkeä?"**
- *Mitä etsit:* Opiskelija ymmärtää, että negatiivinen testaus testaa asioita, joiden EI pitäisi toimia. Se varmistaa, että botti osaa sanoa "ei" ja suojata itseään.

### 5. Reunatapauksista
**"Anna esimerkki reunatapauksesta. Miksi se on tärkeä testata?"**
- *Mitä etsit:* Opiskelija antaa esimerkin (tyhjä viesti, pitkä sekava kysymys, sama kysymys monesti) ja ymmärtää, että reunatapaukset osoittavat botin robustisuuden.

### 6. Iteraatiosta
**"Miksi testaamista täytyy tehdä uudelleen ja uudelleen?"**
- *Mitä etsit:* Opiskelija ymmärtää, että kun löytää ongelmia, hän korjaa ja testaa uudelleen. Tämä on normaali prosessi, ei merkki epäonnistumisesta.

---

## Yleisiä vaikeuksia ja niihin vastaamisen strategiat

### Vaikeus 1: Opiskelijat sanovat "Mikä ero tietopohjalla ja ilman?"

**Mitä kuuluu:** "Eikö botti osaa vastata kysymyksiin ilman tietopohjaa?"

**Vastaus:** "Osaa, mutta väärin. Ilman tietopohjaa se arvailee. Tietopohjalla se käyttää oikeaa tietoa."

**Strategia:** Näytä live-demo:
1. Kysy botilta: "Mikä on [organisaation sisäinen prosessi]?"
2. Näytä vastaus: epämääräinen tai väärä
3. Lataa dokumentti
4. Kysy samalla kysymyksellä uudelleen
5. Näytä vastaus: tarkka ja dokumentista peräisin

Voima on näyttää **eroa**.

### Vaikeus 2: Opiskelijat sanovat "Miksi rajaus estää hyödyllisiä asioita?"

**Mitä kuuluu:** "Jos botti voi vastata kaikkeen, miksi rajata sen?"

**Vastaus:** "Koska botti ei voi vastata oikein kaikkeen. Parempi sanoa 'En osaa' kuin antaa vaarallinen neuvo."

**Strategia:** Anna konkreettinen esimerkki:
- "IT-helpdesk-botti saa kysymyksen: 'Kuinka sijoitan rahaa osakemarkkinoille?'"
- "Se voi arvailla ja antaa väärää neuvoa, jota käyttäjä luottaa."
- "Tai se voi sanoa: 'En osaa antaa sijoitusneuvoja. Ota yhteyttä rahoituspalveluidemme tiimiin.'"
- "Kumpaa haluat käyttäjän kuuleman?"

### Vaikeus 3: Opiskelijat sanovat "Testaaminen on liian monimutkaista"

**Mitä kuuluu:** "Miksi kolme testityyppiä? Eikö riitä, että kysin muutaman kysymyksen?"

**Vastaus:** "Satunnainen testaaminen jättää ongelmia löytämättä. Systemaattinen testaaminen löytää ne."

**Strategia:** Näytä, mitä satunnainen testaaminen ei löydä:
- Satunnainen testaaminen: "Kysin 3 kysymystä, kaikki menivät hyvin. Botti on valmis."
- Systemaattinen testaaminen: "Testaan 15 positiivista, 5 negatiivista, 5 reunatapaus-testiä. Löydän kolme ongelmakohtaa. Korjaan ne ja testaan uudelleen."

Näytä, kuinka systemaattinen testaaminen löytää piilotettuja ongelmia.

### Vaikeus 4: Opiskelijat sanovat "Iteraatio on merkki epäonnistumisesta"

**Mitä kuuluu:** "Jos botti on hyvä ensimmäisellä kerralla, sitä ei tarvitse parantaa."

**Vastaus:** "Ensimmäinen versio ei ole koskaan täydellinen. Hyviä botteja kehitetään testaamalla, parannuksilla ja uudella testaamisella."

**Strategia:** Näytä iteraation prosessi:
1. Alustava ohjeistus
2. Testit
3. Ongelmat löytyvät
4. Korjaukset
5. Uudet testit
6. Parantuminen
7. (Toistetaan kunnes riittävän hyvä)

Selitä, että tämä on **normaalia** ja **ammattilaismaista**.

### Vaikeus 5: Opiskelijat sanovat "Tietopohja vanhentuu, joten en päivitä sitä"

**Mitä kuuluu:** "Jos prosessit muuttuvat, botti tulee vanhentuneeksi. Miksi siis ylläpitää sitä?"

**Vastaus:** "Juuri siksi. Ylläpito on **kriittinen**. Vanhentuneet ohjeet aiheuttavat enemmän vahinkoa kuin hyötyä."

**Strategia:** Anna esimerkki:
- "IT-helpdesk-botti, jonka ohjeet ovat 6 kuukautta vanhoja"
- "Käyttäjä seuraa ohjeita, jotka eivät enää kelpaa"
- "Käyttäjä tekee väärän asian tai turvallisuus kärsii"
- "Parempi ettei ole bottia kuin että se antaa vaarallista tietoa"

---

## Oppimisresurssit, joihin opettaja voi viitata

1. **Opiskelijamateriaalit (student-study ja student-tasks):** Kaikki perusideat ovat siellä.

2. **Tietopohjat käytännössä:**
   - Dokumentti: PDF, Word, teksti
   - Data: CSV, tietokanta, API
   - Reaaliaikainen: verkko, sensori, API

3. **Rajaukset esimerkkejä:**
   - IT-helpdesk: vain IT-aiheet
   - Asiakaspalvelu: julkinen info, ei yksityisiä tietoja
   - Opetus: pedagogisia neuvoja, ei koodiin vastauksia valmiina

4. **Testaus-dokumentaatio:**
   - Taulukko: testityyppi, kysymys, odotettu vastaus, saatu vastaus, tulos
   - Analyysi: mitä meni hyvin, mitä meni huonosti
   - Korjaukset: mitä muutit ja mitä paransi

5. **Iteraation esimerkit:**
   - Kierros 1: ohjeistus → testit → ongelmat
   - Kierros 2: korjaukset → testit → parantuminen
   - Kierros 3: (tarpeen mukaan)

---

## Punainen lanka: "Kohti tuotantokvaliteettista bottia"

Oppituntisarja (neljä oppituntia):
- **Edellisellä tunnilla**: Opiskelijat oppivat, kuinka suunnitella botti järjestelmäpromptin avulla
- **Tällä tunnilla**: Opiskelijat oppivat, kuinka varustetaan botti tiedolla, rajauksilla ja testaamisella
- **Seuraavalla tunnilla**: Opiskelijat oppivat rakentaa todellisen Custom-GPT:n (käytännöntoteutus)
- **Myöhemmissä tunneissa**: Opiskelijat rakentavat monimutkaisia, tuotantokvaliteettisia botteja

Tämä oppitunti on kriittinen, koska se opettaa:
- Että laatu ei tule ilmaiseksi
- Että testaus on jatkuva prosessi
- Että rajaukset tekevät botista **vastuullisen**
- Että tietopohja on **kriittinen** hyvälle botille

---

## Eriyttäminen ja tuen tarpeet — testaus ja parantaminen

### Case study oppitunnin alussa
Live-demo on opiskelijoille konkreettinen esimerkki. Se näyttää:
- Miten tietopohja muuttaa vastauksia
- Miten rajaukset kirjoitetaan
- Miten testaus dokumentoidaan

Vähentää epävarmuutta: "Miten aloitan testaamisen?"

### Jos olet jumissa -osio
Opiskelijatehtäviin on lisätty mallipohjat (taulukot, dokumentaatiomuoto). Ohjaa epävarmaksi tuntevat opiskelijat näihin ennen tehtävän alkua.

### Tukipisteet

| Oppitunti | Kriittinen kohta | Tuen muoto |
|-----------|-----------------|-----------|
| Edellinen | Botin suunnittelu | Case study + live-demo |
| **Tämä** | **Testaaminen systemaattisesti** | **Live-demo + ryhmäharjoitus + mallipohjat** |
| Seuraava | Todellisen Custom-GPT:n rakentaminen | Step-by-step ohje |
| Myöhemmät | Monimutkaisen botin testaaminen | Itsenäiset testauskaaviot |

### Myöhemmät oppitunnit vaativat tästä tunnista ymmärrystä
Jos opiskelijat eivät ymmärrä, miksi testaus ja rajaukset ovat tärkeitä, he:
- Rakentavat botteja, jotka antavat virheellistä tietoa
- Eivät tiedä, miten vaatia bottia toimimaan oikein
- Luottavat siihen, että ensimmäinen versio on täydellinen (eivät iteroi)

Siksi **varmista, että jokainen opiskelija saa käytännön kokemuksen testauksesta** tämän oppitunnin aikana.

---

## Vihjeet opettajalle

**Milloin botti tarvitsee tietopohjaa:**
- Kun sillä täytyy vastata organisaation sisäisistä asioista
- Kun vastausten täytyy olla tarkkoja ja ajankohtaisia
- Kun yleinen ChatGPT-tieto ei riitä

**Milloin botti tarvitsee rajauksia:**
- Aina, kun botti voi vahingoittaa käyttäjää väärin tietämällä
- Kun botti käsittelee herkkiä tietoja
- Kun botin toiminta-alue on rajattu

**Mitä testata:**
- Positiivisesti: perustehtävät
- Negatiivisesti: turvallisuus ja rajaukset
- Reunatapauksissa: robustisuus ja epätavallisten tilanteiden käsittely

**Miten dokumentoida testit:**
- Taulukko: testityyppi, input, expected output, actual output, result
- Analyysi: mitä onnistui, mitä epäonnistui
- Korjaukset: mitä muutetaan seuraavalla kierroksella

---

## Yhteenveto opettajalle

Tämä oppitunti on käänteentekevä. Opiskelijat näkevät, että:
1. Botti ei ole vain nimetty ChatGPT
2. Hyvä botti rakentuu **suunnittelusta, tiedosta, rajauksista ja testauksesta**
3. Testaaminen on jatkuva prosessi
4. Rajaukset tekevät botista **vastuullisen**, ei rajoittavan

Tämän oppitunnin jälkeen opiskelijat ovat valmiita rakentamaan **oikeita, tuotantokvaliteettisia botteja**, ei vain leikkiä.
