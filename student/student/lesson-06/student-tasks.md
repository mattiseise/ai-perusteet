# Opiskelutehtävät

## Tehtävä 6.1: Näyttö vai kuvaus — multimodaalisen kontekstin voima

### Tavoite
Ymmärtää käytännössä, kuinka kuvakaappaus ja muut multimodaaliset tietomuodot muuttavat tekoälyn kykyä auttaa IT-ongelmassa. Nähdä, missä multimodaalisuus auttaa eniten ja missä se saattaa olla turha.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

1. **Valitkaa IT-ongelma**, joka sisältää visuaalisen elementin. Esimerkiksi:
   - Virheilmoitus näytöllä
   - Verkon konfiguraationäyttö
   - Tietokannan hallintaohjelman käyttöliittymävika
   - Lokien tulostus päätteessä (näkyy väreillä ja muotoilulla)
   - Sovelluksen kaatumisviesti

2. **Kerätkää kaksi versiota kontekstista:**

   **Versio A (vain teksti):** Kuvailkaa ongelma sanoin ilman kuvia. Kirjoittakaa, mitä näette, minkä värinen virhe on ja mitä tekstiä näkyy. Olkaa niin tarkkoja kuin mahdollista, mutta älkää käyttäkä kuvakaappausta.

   **Versio B (multimodaalinen):** Sama tekstikuvaus sekä kuvakaappaus ongelmasta, lokin relevantti osio (jos soveltuu) ja/tai koodin vika-alue (jos soveltuu).

3. **Lähettäkää molemmat tekoälylle** (mieluiten samalle mallille, esim. Claude, ChatGPT-4V):
   - Kysykää sama kysymys kahdesti — ensin versiolla A, sitten versiolla B.
   - Dokumentoikaa molemmat vastaukset.

4. **Vertailutaulukko:**

| Aspekti | Versio A (vain teksti) | Versio B (multimodaalinen) |
|---------|------------------------|---------------------------|
| Vastauksen spesifisyys | | |
| Tutkittavien ratkaisujen lukumäärä | | |
| Vastauksessa mainittu visuaalinen tieto | | |
| Kuinka hyödyllinen vastaus oli (1-5) | | |
| Token-kustannus (arvio) | | |
| Vastausaika | | |

5. **Analyysi (2–4 lausetta):**
   - Kumpi versio oli parempi ja miksi?
   - Millä tavoin multimodaalinen lähestyminen muutti tekoälyn vastausta?
   - Missä tilanteissa multimodaalinen input olisi olennainen vs. turha?

### Odotettu tuotos
- Täytetty vertailutaulukko
- Kirjallinen analyysi edellä olevista kysymyksistä

**Jos teet tehtävän yksin:**
Valitse itsellesi IT-ongelma. Kirjoita tekstikuvaus. Ota kuvakaappaus tai kerää lokit. Tee molemmat testit ja vertaa.

---

## Tehtävä 6.2: Multimodaalisen kontekstin rakentaminen — käytännön ongelma

### Tavoite
Oppia rakentamaan tehokas multimodaalinen konteksti oikeasta IT-ongelmasta käyttämällä tekstiä, kuvakaappauksia, lokeja ja koodia strategisesti. Harjoitella päätöksentekoa: mitä sisällytetään, mikä redaktoidaan, mikä jätetään pois.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

1. **Valitkaa todellinen IT-projekti tai ongelma**, jota käsittelette nyt tai jota muistaatte. Esimerkiksi:
   - Tietokanta on hidas tai ei vastaa
   - Verkkopalvelu kaatuilee satunnaisesti
   - Ohjelman käyttöliittymässä on bugi
   - Palvelin on kriittisellä hetkellä poikki
   - Sovellus kuluttaa liikaa muistia tai CPU:ta

2. **Kerätkää multimodaalista materiaalia:**

   - **Teksti:** Kirjoittakaa lyhyesti (2–3 lausetta) ongelma, mitä yrityitte tehdä ja mikä meni pieleen
   - **Kuvakaappaus(set):** Ottakaa 1–2 kuvakaappausta, jotka näyttävät ongelman
   - **Lokit:** Kopioikaa relevantti loki-osio (10–20 riviä, ei 500), poistaen salaisuudet
   - **Koodi (jos relevanttia):** Näyttäkää kyseinen koodin osa (10–20 riviä), joissa ongelma esiintyy

3. **Dokumentoikaa kukin osa taulukossa:**

| Materiaali | Sisältö | Token-arvio | Miksi tärkeä? | Redaktoitu? |
|-----------|---------|-------------|---------------|-----------|
| Teksti | [mitä kirjoitit] | | | Kyllä/Ei |
| Kuvakaappaus 1 | [kuvaus] | | | Kyllä/Ei |
| Loki | [mitä rivejä, esim. rivit 45-65] | | | Kyllä/Ei |
| Koodi | [funktio/luokka/komennot] | | | Kyllä/Ei |

4. **Testatkaa multimodaalinen konteksti:**
   - Kootkaa kaikki materiaali yhdeksi kysymykseksi tekoälylle (multimodaalinen malli, esim. Claude tai ChatGPT-4V)
   - Kysykää selkeä kysymys: "Mitä tämä ongelma on ja miten sen korjaisin?"
   - Dokumentoikaa: "Tekoälyn vastaus käytti seuraavaa materiaalia: [mikä oli hyödyllisintä]"
   - Ajattelkaa: "Olisiko vastaus parempi tai huonompi ilman kuvakaappauksia, lokeja tai koodia?"

5. **Arvio strategiasta (3–5 lausetta):**
   - Mikä osa multimodaalisesta kontekstista oli arvokkain?
   - Mikä olisi ollut turhaa tai voinut jäädä pois?
   - Kuinka muuttaisitte kontekstia seuraavalla kerralla?
   - Mitä opitte multimodaalisuudesta ja strategisesta kontekstin rakentamisesta?

### Odotettu tuotos
- Täytetty materiaalitaulukko
- Yhden sivun raportti, joka sisältää:
  - Mikä projekti tai ongelma oli
  - Miten kasasitte multimodaalisen kontekstin
  - Mitä materiaalia tekoäly käytti eniten
  - Mikä toimi ja mikä ei
  - Oppimasi asiat multimodaalisuudesta ja kontekstin hallinnasta

**Jos teet tehtävän yksin:**
Dokumentoi oma IT-ongelmasi kerätyllä multimodaalisella kontekstilla. Testaa tekoälylle. Reflektoi ja kirjoita, mitä oppit.

---

## Tehtävä 6.3: Turvallisuus ja päätöksenteko — millainen konteksti on valmis?

### Tavoite
Oppia tunnistamaan turvallisuusriskit multimodaalisessa kontekstissa ja tekemään päätöksiä siitä, mitä voi jakaa ja mitä tulee redaktoida. Ymmärtää, missä tilanteissa multimodaalinen input on oikea valinta.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

1. **Teille annetaan neljä skenaariota.** Kussakin tilanteessa tekoäly auttaisi, mutta konteksti sisältää potentiaalisia turvallisuusongelmia. Toimitkaa jokaisessa näin:

   **Skenaario 1: Tietokantayhteyden ongelma**
   ```
   Loki näyttää:
   2024-03-14 10:23:45 ERROR: Failed to connect to database
   2024-03-14 10:23:46 ERROR: Connection string: postgresql://admin:MyPassword123!@db.company.com:5432/users
   2024-03-14 10:23:47 ERROR: Connection timeout
   ```
   - Mitä tulee redaktoida?
   - Miten muotoilisit tämän turvallisesti tekoälylle?

   **Skenaario 2: API-integraaation debuggaus**
   ```
   Kuvakaappaus näyttää:
   POST /api/v1/payment
   Authorization: Bearer sk-live-4eC39HqLyjWDarhtT1ZdV7UL
   Body: {
     "amount": 19999,
     "card_token": "tok_visa_4242424242424242"
   }
   Response: 401 Unauthorized
   ```
   - Mitä tulee redaktoida?
   - Mikä tieto on kriittistä ongelman ratkaisemiseksi?

   **Skenaario 3: Verkko-ongelma ja lokitiedostot**
   ```
   Logi sisältää:
   2024-03-14 14:30:00 INFO: User login: john.smith@company.com
   2024-03-14 14:30:01 INFO: Processing transaction for customer ID: CUST_12345
   2024-03-14 14:30:02 ERROR: Network timeout
   2024-03-14 14:30:03 INFO: Customer data: {name: John Smith, SSN: 123-45-6789, ...}
   ```
   - Mitä tulee redaktoida tai poistaa kokonaan?
   - Mitkä tiedot ovat turvallisuuskritiikin alaiset?

   **Skenaario 4: Konfiguraatiotiedoston jakaminen**
   ```json
   {
     "app_name": "PaymentProcessor",
     "environment": "production",
     "database": {
       "host": "db.prod.company.com",
       "port": 5432,
       "user": "app_user",
       "password": "C0mp1ex!P@ssw0rd2024"
     },
     "api_keys": {
       "stripe": "sk_live_51234567890abcdef",
       "twilio": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
     },
     "external_services": {
       "slack_webhook": "https://hooks.slack.com/services/T123/B456/xxxxxx"
     }
   }
   ```
   - Voitko jakaa tämän tiedoston tekoälylle ollenkaan?
   - Jos kyllä, mitä redaktoit?
   - Mikä on parempi ratkaisu?

2. **Tehtävä kutakin skenaariota varten:**
   - **Tunnista:** Mitä turvallisuusriskejä näet?
   - **Redaktoi:** Kirjoita turvallinen versio materiaalista
   - **Perustele:** Miksi nämä tiedot ovat herkkiä? Mitä haittaa voisi tulla?
   - **Päätä:** Voitko silti auttaa tekoälyä redaktion jälkeen? Entä ilman näitä tietoja?

3. **Päätöskehikko — milloin multimodaalinen input on oikea valinta:**

Täytä tämä taulukko jokaiselle skenaariolle:

| Skenaario | Multimodaalinen input auttaa? | Kyllä, jos | Ei, koska | Turvallisuusriski | Ratkaisu |
|-----------|-------------------------------|-----------|-----------|-------------------|----------|
| Skenaario 1 | | | | | |
| Skenaario 2 | | | | | |
| Skenaario 3 | | | | | |
| Skenaario 4 | | | | | |

4. **Yhteenveto ja oppiminen:**
   - Mikä on pahin turvallisuusriski, jonka näit?
   - Kuinka varmistaisit, että konteksti on turvallinen ennen kuin jaat sen?
   - Mitä salaisuuksia näkemällä hyökkääjä voisi tehdä jokaisissa skenaarioissa?

### Odotettu tuotos
- Neljän skenaarion turvallisuusanalyysi ja redaktoitu versio
- Täytetty päätöskehikko-taulukko
- 2–3 lauseen yhteenveto: "Oppin turvallisuudesta ja multimodaalisen kontekstin jakamisesta..."

**Jos teet tehtävän yksin:**
Tee kaksi skenaariosta täydellisesti (analyysi + redaktointi + taulukko).

---

## Tehtävien palautus

Palauta tehtävät Moodlen kautta ryhmän nimellä tai henkilökohtaisesti. Sisällytä:
- Kaikki taulukot ja dokumentaatio
- Kuvakaappaukset (jos soveltuu)
- Lyhyt tekstianalyysi kunkin tehtävän lopussa

Arviointiperusteet:
- **6.1:** Vertailun laatu, analyysin syvyys
- **6.2:** Materiaalin relevanssi, multimodaalisen kontekstin tehokkuus, strateginen ajattelu
- **6.3:** Turvallisuusriskeille herkkyyden taso, redaktion tarkkuus, päätöksenteon perustelut
