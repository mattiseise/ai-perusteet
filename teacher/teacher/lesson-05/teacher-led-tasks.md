# Opettajavetoiset tehtävät

## Tehtävä 5.1: Konteksti-ikkunan rajoitukset — live-vertailu

### Tavoite
Näyttää opiskelijoille konkreettisesti, kuinka tieto häviää konteksti-ikkunasta pitkissä keskusteluissa. Rakentaa ymmärrys siitä, miksi hallinta on välttämätöntä.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**
- Valitse IT-loki tai virheilmoitusten sarja (noin 1000–2000 tokenia), joka sisältää useita virheitä.
- Tai kirjoita synteettinen 10 kysymyksen ketju.

**Oppitunnilla (20 min):**

1. **Johdanto (2 min):**
   - Kerro: "Tekoälyllä on muisti, joka on rajallinen. Kuvittele opettajaa, jolla on muistikirja vain 128 sivulla. Kun se täyttyy, vanhat sivut poistetaan."

2. **Näytös: pitkä keskustelu (8 min):**
   - Avaa tekoäly ruudulla.
   - Lähetä iso konteksti alussa: "Rooli: Olet Linux-järjestelmänhallitsija. Tausta: palvelin kaatuu satunnaisesti. Tavoite: löytää lokivirhe ja korjata se."
   - Lähetä sitten 10 kysymystä peräkkäin. Kaikki liittyvät samaan ongelmaan, mutta tarkastelevat sitä eri näkökulmista.
   - **Merkitse tarkkailemasi:** Missä kohtaa malli alkaa "unohtaa" alkuperäisen kontekstin?
     - Kohta, jossa malli antaa vastauksen, joka olisi ollut parempi, jos se olisi muistanut "Linux-järjestelmänhallitsija"-roolin?
     - Millä kysymyksellä malli lopettaa viittaamisen alkuperäiseen ongelmaan?

3. **Analyysi (5 min):**
   - Kysy opiskelijoilta:
     - "Huomasitteko, kuinka vastaukset muuttuivat noin 7. tai 8. kysymyksen jälkeen?"
     - "Mikä tieto näytti häviävän?"
     - "Kuinka moni kysymyksistä muisti alkuperäisen kontekstin? Kuinka moni ei?"

4. **Johtopäätös (5 min):**
   - Piirrä tauluun:
     ```
     Konteksti (80 tokenia) + Q1 (30) + A1 (50) + Q2 (30) + A2 (50) ...
     Yhteensä: 128 000 – paljonko jää jäljelle?
     ```
   - Selitä: "Näet, kuinka nopeasti ikkuna täyttyy. Siksi tarvitaan strategia!"

### Odotettu oppimistulos
- Opiskelijat näkevät konkreettisesti "unohdetun tiedon" ongelman.
- He ymmärtävät, että konteksti-ikkuna ei ole pelkkä teoreettinen käsite – se vaikuttaa oikeasti vastauksiin.

---

## Tehtävä 5.2: Pilkkomisen suunnitteleminen – ohjattu harjoitus

### Tavoite
Opettaa opiskelijoille, miten suuri projekti pilkotaan hallittaviksi osiksi ennen tekoälyn käyttöä. Rakentaa strategista ja järkevää ajattelua.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**
- Valitse iso IT-tehtävä. Esimerkiksi: "Analysoida 3000 rivin tietokantaskema" tai "Debugata 50 000 rivin lokia".

**Oppitunnilla (25 min):**

1. **Asetusmuutos (2 min):**
   - Kerro: "Nyt ajatellaan älykkäästi. Ennen kuin käytät tekoälyä isoon tehtävään, sinun on pilkottava se. Tehdään se yhdessä."

2. **Vaihe 1: Ymmärrä tehtävän koko (4 min):**
   - Näytä tehtävä (esim. tietokantaskema tai loki).
   - Kysy: "Kuinka monta tokenia tämä on?" (Kopioi malliin tai arvioi: ~4 merkkiä/token.)
   - Keskustele: "Mahtuuko kaikki yhteen konteksti-ikkunaan?"

3. **Vaihe 2: Pilko vaiheiksi (8 min):**
   - Piirrä tauluun: Kuinka pilkkoisit tämän?
   - Tietokantaesimerkki:
     ```
     Osa 1: Analysoida taulukot 1–50
     Osa 2: Analysoida taulukot 51–100
     Osa 3: Analysoida taulukot 101–150
     Osa 4: Yhteenveto kaikista
     ```
   - Lokiesimerkki:
     ```
     Osa 1: Analysoida lokia ajalta 08:00–10:00
     Osa 2: Analysoida lokia ajalta 10:00–12:00
     ...
     Osa 5: Yhteenveto kaikista virheistä
     ```
   - Kysy: "Kuinka monta osaa tarvitaan? Miksi juuri niin monta?"

4. **Vaihe 3: Ankkurointi jokaiseen osaan (6 min):**
   - Kirjoita tauluun: Mitä ankkuroisit jokaisessa osassa?
   - Esimerkiksi:
     ```
     Osa 1: "Analysoitu 3000 rivin tietokannan taulukot. Taulukot 1–50 nyt. Tulevat osat: 51–100, 101–150, jne. Jokainen osa arvioidaan."
     Osa 2: "Edellisen osan (1–50) tulokset: [yhteenveto]. Nyt taulukot 51–100."
     ```
   - Selitä: "Näin malli ei unohda, vaikka ikkuna täyttyisikin."

5. **Lopullinen suunnitelma (5 min):**
   - Kirjoita tauluun lopullinen "projektisuunnitelma":
     ```
     Projekti: [nimi]
     Kokonaisuus: X tokenia
     Ikkuna: Y tokenia
     Osia: Z
     Strategia: Pilkkominen + ankkurointi
     Dokumentointi: [jokaisesta osasta tehdään yhteenveto]
     ```
   - Kerro: "Tämä on ammattitaitoinen lähestymistapa. Näin johtavat IT-tiimit hallitsevat suuria projekteja tekoälyn kanssa."

### Odotettu oppimistulos
- Opiskelijat näkevät, että suuren projektin hallinta vaatii suunnittelua.
- He ymmärtävät kolme strategiaa: pilkkominen, tiivistys, ankkurointi.
- He pystyvät luomaan omia suunnitelmia omiin projekteihinsa.

---

## Tehtävä 5.3: Kontekstin katoaminen livenä – epäonnistumisen demonstraatio

### Tavoite
Näyttää opiskelijoille reaaliaikaisesti, kuinka malli unohtaa kontekstin ilman varoitusta. Rakentaa ymmärrys siitä, miksi ammattilaisen on aina tarkistettava vastaukset.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**
- Valmistele etukäteen noin 20 kysymyksen sarja, jotka kuormittavat konteksti-ikkunaa.
- Testaa, millä kohdalla valitsemasi malli alkaa unohtaa alkuperäiset rajaukset.

**Oppitunnilla (20 min):**

1. **Asetus (3 min):**
   - Kerro: "Nyt teemme kokeen. Katsotaan, kuinka luotettava tekoälyn muisti todella on."
   - Avaa tekoäly ja anna selkeä alkurajaus: "Käytämme Ubuntu 22.04:ää, PostgreSQL:ää ja Python 3.9:ää. Älä ehdota Windows-ratkaisuja."
   - Kysy kolme kysymystä, jotka liittyvät tähän ympäristöön. Malli vastaa oikein.

2. **Kuormittaminen (7 min):**
   - Kysy nopeasti 15–20 eri aihetta koskevaa kysymystä. Opiskelijat seuraavat.
   - Älä muistuta rajauksista missään kohtaa.

3. **Paljastus (5 min):**
   - Kysy: "Miten asennan tietokantapalvelimen?"
   - Jos malli ehdottaa Windows-ratkaisua tai väärää tietokantaa, pysäytä: "Huomasitteko? Se unohti. Ja se ei kertonut meille."
   - Jos malli muistaa, kysy: "Entä käyttöjärjestelmä?" ja jatka kunnes jotain unohtuu.

4. **Korjaus livenä (2 min):**
   - Toista rajaukset: "Muistathan, käytämme Ubuntu 22.04:ää ja PostgreSQL:ää."
   - Kysy sama kysymys. Näytä, kuinka ankkurointi korjaa tilanteen.

5. **Keskustelu (3 min):**
   - "Mitä opimme? Malli ei varoittanut. Se ei sanonut 'en muista'. Se antoi väärän vastauksen yhtä vakuuttavasti kuin oikean."
   - "Ammattilaisena sinun vastuullasi on huomata tämä – malli ei tee sitä puolestasi."

### Odotettu oppimistulos
- Opiskelijat kokevat emotionaalisesti merkittävän hetken: "Se ei kertonut unohtaneensa."
- He ymmärtävät, miksi ankkurointi ja dokumentointi ovat välttämättömiä.
- He oppivat, että virhe ei ole häpeällinen – sen tunnistaminen on ammattitaitoa.