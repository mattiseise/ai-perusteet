# Opettajavetoiset tehtävät

## Tehtävä 5.1: Konteksti-ikkunan näkyminen — Live-vertailu

### Tavoite
Näyttää opiskelijoille konkreettisesti, kuinka tieto häviää konteksti-ikkunasta pitkissä keskusteluissa. Rakentaa ymmärrys siitä, miksi hallinta on välttämätöntä.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
- Valitse IT-lokin tai virheilmoitusten sarja (noin 1000-2000 tokenia), joka sisältää useita virheitä.
- Tai kirjoita synteettinen 10-kysymyksisen ketjun juonen.

**Oppitunnilla (20 min):**

1. **Johdanto (2 min):**
   - Kerro: "Tekoälylla on muisti, joka on rajallinen. Kuvittele, että opettajalla on muistikirja, jossa on vain 128 sivua. Kun se täyttyy, vanhat sivut poistetaan."

2. **Näytös: Pitkä keskustelu (8 min):**
   - Avaa tekoälyä ruudulla.
   - Lähetä iso konteksti alussa: "Rooli: Olet Linux-järjestelmänhallitsija. Tausta: Serveri kaatuu satunnaisesti. Tavoite: Löytää loki-virhe ja korjata."
   - Lähetä sitten 10 kysymystä peräkkäin, kaikki liittyen samaan ongelmaan, mutta eri kulmiinsa.
   - **Merkitse tarkkailemasi**: Milläs kohtaa malli alkaa "unohtaa" alkuperäisen kontekstin?
     - Kohtaa, jossa malli antaa vastauksen, joka olisi ollut parempi, jos se olisi muistanut "Linux-järjestelmänhallitsija" -roolin?
     - Millä kysymyksellä malli lopettaa viittaamisen alkuperäiseen ongelmaan?

3. **Analyysi (5 min):**
   - Kysy opiskelijoilta:
     - "Huomasitteko, kuinka vastauksena muuttuivat noin 7. tai 8. kysymyksen jälkeen?"
     - "Mikä tieto näytti hävinneen?"
     - "Kuinka moniko kysymyksistä muistivat alkuperäisen kontekstin? Kuinka moniko eivät?"

4. **Johtopäätös (5 min):**
   - Piirä tauluun:
     ```
     Konteksti (80 tokenia) + Q1 (30) + A1 (50) + Q2 (30) + A2 (50) ... 
     Yhteensä: 128 000 - paljonko jää jäljellä?
     ```
   - Selitä: "Näet, kuinka nopeasti ikkuna täyttyy. Siksi tarvitaan strategia!"

### Odotettu oppimistulos
- Opiskelijat näkevät konkreettisesti "unohdetun tiedon" ongelman.
- He ymmärtävät, että konteksti-ikkuna ei ole pelkkä teoreettinen käsite — se vaikuttaa oikeasti vastauksiin.

---

## Tehtävä 5.2: Pilkkomisen suunnitteleminen — Ohjattu harjoitus

### Tavoite
Opettaa opiskelijoille, miten suuri projekti pilkotaan hallittaviksi osiksi ennen tekoälyn käyttöä. Rakentaa hallinnollinen ajattelu.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
- Valitse iso IT-tehtävä. Esimerkiksi: "Analysoida 3000 rivin tietokanta-skeema" tai "Debugata 50 000 rivin logia".

**Oppitunnilla (25 min):**

1. **Asetusmuutos (2 min):**
   - Kerro: "Nyt ajatellaan älykästi. Ennen kuin käytät tekoälyä isoon tehtävään, sinun täytyy pilkota se. Tehdään se yhdessä."

2. **Vaihe 1: Ymmärrä tehtävän koko (4 min):**
   - Näytä tehtävä (esim. tietokanta-skeema tai logi).
   - Kysy: "Kuinka monta tokenia tämä on?" (Kopioitaan malliin tai arvioidaan: ~4 merkkiä/token)
   - Keskustele: "Mahtuuko kaikki yhteen konteksti-ikkunaan?"

3. **Vaihe 2: Pilkko vaiheeksi (8 min):**
   - Piirä tauluun: Kuinka pilkoisit tämän?
   - Tietokanta-esimerkki:
     ```
     Osa 1: Analysoida taulukot 1-50
     Osa 2: Analysoida taulukot 51-100
     Osa 3: Analysoida taulukot 101-150
     Osa 4: Yhteenveto kaikista
     ```
   - Logi-esimerkki:
     ```
     Osa 1: Analysoida logia aika 08:00-10:00
     Osa 2: Analysoida logia aika 10:00-12:00
     ...
     Osa 5: Yhteenveto kaikista virheistä
     ```
   - Kysy: "Kuinka monta osaa tarvitaan? Miksi näin moneksi?"

4. **Vaihe 3: Ankkurointi jokaiseen osaan (6 min):**
   - Kirjoitaa tauluun: Mitä ankkuroitaisit jokaisessa osassa?
   - Esimerkiksi:
     ```
     Osa 1: "Analysoitu 3000 rivin tietokannan taulukot. Taulukot 1-50 nyt. Tulevat osat: 51-100, 101-150, jne. Jokainen osa arvioidaan."
     Osa 2: "Edellisen osan (1-50) tulokset: [yhteenveto]. Nyt taulukot 51-100."
     ```
   - Selitä: "Näin malli ei unohda, vaikka ikkuna täyttyisikään."

5. **Lopullinen suunnitelma (5 min):**
   - Kirjoita tauluun lopullinen "projektisuunnitelma":
     ```
     Projekti: [nimi]
     Kokonaisuus: X tokenia
     Ikkuna: Y tokenia
     Osia: Z
     Strategia: Pilkkominen + Ankkurointi
     Dokumentointi: [jokaisesta osasta tehdään yhteenveto]
     ```
   - Kerro: "Tämä on ammattitaitoinen lähestymistapa. Näin johtavat IT-tiimit suurten projekteja tekoälyn kanssa."

### Odotettu oppimistulos
- Opiskelijat näkevät, että suuren projektin hallinta vaatii suunnittelua.
- He ymmärtävät kolmea strategiaa: pilkkominen, tiivistys, ankkurointi.
- He pystyvät luomaan omia suunnitelmia omille projekteille.
