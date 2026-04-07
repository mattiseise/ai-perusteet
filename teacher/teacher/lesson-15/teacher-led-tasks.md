# Opettajavetoiset tehtävät — Oma botti II

## Tehtävä 15.1: Live-demo — Tietokannan lisääminen botille (20 min)

### Tavoite

Osoittaa konkreettisesti, kuinka tietopohja lisätään bottiin ja miten se vaikuttaa botin vastauksiin.

### Opettajan ohjeet ja fasilitaatio

Tämä tehtävä tehdään opettajan johdolla koko luokalle. Käytä Custom-GPT:tä tai ChatGPT:n tietopohja-ominaisuuksia.

**Valmistelu (ennen lähiosaa):**
- Valmista yksinkertainen dokumentti (esim. FAQ tai käyttöohje)
- Testaa, miten botti vastaa ilman tietopohjaa
- Testaa, miten botti vastaa tietopohjalla
- Valmista kolme kysymystä, joista osa on tietopohjaan liittyviä ja osa ei

**Tehtävän vaiheet (20 min):**

1. **Johdanto (2 min):**
   - "Edellisellä oppitunnilla opimme, kuinka kirjoittaa hyvä järjestelmäprompti. Nyt kohtaamme ongelman: botti osaa vain sen, mitä se tietää."
   - "Jos haluat, että botti vastaa tarkkaan ja ajankohtaisesti, sinun täytyy antaa sille **tietopohja** — oikeat dokumentit ja data."

2. **Vaihe 1: Ilman tietopohjaa (4 min)**
   - Kysy botilta: "Mikä on [organisaation sisäinen prosessi tai tuote]?"
   - Näytä vastaus: botti arvailee tai sanoo, ettei osaa
   - Kysy: "Näettekö, kuinka epämääräinen vastaus on?"

3. **Vaihe 2: Tietopohjadokumentin lataaminen (5 min)**
   - Näytä, kuinka lataat dokumentin Custom-GPT:hin
   - Selitä askeleen jokaisella:
     - Valitse Custom-GPT tai hallintapaneeli
     - Lisää dokumentti (PDF, Word tai teksti)
     - Odota, että botti indeksoi tiedon
   - Kysy: "Näettekö, kuinka yksinkertainen tämä on?"

4. **Vaihe 3: Samalla kysymyksellä uudelleen (4 min)**
   - Kysy samalla kysymyksellä: "Mikä on [sama prosessi/tuote]?"
   - Näytä vastaus: nyt se on tarkka ja dokumentista peräisin
   - Kysy: "Näettekö eron? Nyt botti tietää, koska sillä on oikea tieto."

5. **Vaihe 4: Rajaukset tietopohjassa (3 min)**
   - Selitä: "Tietopohjansa kanssa tulee myös vastuu. Jos dokumentissa on virhe, botti toistaa sen."
   - Kysy: "Mitä tämä tarkoittaa tietopohjamme päivittämiselle?"
   - Vastaus: "Tietopohja täytyy olla **aina ajan tasalla**."

6. **Yhteenveto (2 min):**
   - "Hyvä botti = hyvät ohjeet + hyvä tietopohja."
   - "Ilman tietopohjaa se on vain yleinen ChatGPT. Tietopohjalla se on **räätälöity järjestelmä**."

### Odotettu oppimistulos

- Opiskelijat näkevät, miten tietopohja lisätään käytännössä
- Opiskelijat ymmärtävät, että tietopohja muuttaa botin tarkkuutta
- Opiskelijat tietävät, että tietopohja täytyy päivittää säännöllisesti

---

## Tehtävä 15.2: Ryhmäharjoitus — Botin testaaminen kolmella tavalla (30 min)

### Tavoite

Opiskelijat testaavat bottia systemaattisesti: positiivisilla, negatiivisilla ja reunatapauksen testeillä.

### Opettajan ohjeet ja fasilitaatio

Pienryhmät (2–3 henkilöä). Jokainen ryhmä testaa samaa bottia tai omaa bottia.

**Valmistelu:**
- Valmista yksinkertainen, testattava botti (esim. IT-helpdesk tai opastus)
- Valmista testauspohja, joka näyttää kolme testityyppiä
- Valmista dokumentti, jossa kuvataan mitä ottaa huomioon jokaisessa testityypissä

**Tehtävän vaiheet (30 min):**

1. **Johdanto (2 min):**
   - "Testaaminen ei ole satunnaista. Se on systemaattista ja tarkaa työtä."
   - "Testataan tämän botin kanssa kolmella tavalla."

2. **Positiivisen testauksen selitys (2 min):**
   - "Positiivinen testaus tarkoittaa: kysymme sitä, mihin botti on suunniteltu vastaamaan."
   - "Odotamme, että vastaukset ovat oikeita ja hyödyllisiä."
   - Esimerkki: "Jos tämä on IT-helpdesk-botti, kysymme IT-ongelmista."

3. **Ryhmille jako ja positiivinen testaus (8 min):**
   - Jokainen ryhmä saa botin ja testauspohjan
   - Ryhmät kirjoittavat 3 positiivista testiä ja dokumentoivat vastaukset
   - Opettaja liikkuu ja auttaa:
     - "Onko tämä hyvä positiivinen testi?"
     - "Mitä odotitte saavanne?"

4. **Negatiivisen testauksen selitys (2 min):**
   - "Negatiivinen testaus tarkoittaa: kysymme sitä, mihin botti ei pitäisi vastata."
   - "Testaamme, osaa botti sanoa 'ei' ja osaa suojata itsensä."
   - Esimerkki: "Jos tämä on IT-helpdesk-botti, kysymme rahoituskysymyksistä tai arkaluontoisista asioista."

5. **Negatiivinen testaus (8 min):**
   - Ryhmät kirjoittavat 3 negatiivista testiä
   - Dokumentoivat vastaukset ja turvallisuusanalyysin
   - Opettaja auttaa:
     - "Näettekö turvallisuusriskin tässä vastauksessa?"
     - "Oliko botti oikein varovainen?"

6. **Reunatapausten selitys (2 min):**
   - "Reunatapaukset ovat outoja tilanteita, joita et odottanut."
   - "Testaamme, kestääkö botti näitä vai kaatuu se."
   - Esimerkkejä: tyhjä viesti, hyvin pitkä kysymys, sama kysymys monesti

7. **Reunatapausten testaus (4 min):**
   - Ryhmät kirjoittavat 3 reunatapaus-testiä
   - Dokumentoivat tulokset

8. **Raportointi (2 min):**
   - Jokainen ryhmä kertoo lyhyesti:
     - Yksi positiivinen testi, joka onnistui hyvin
     - Yksi negatiivinen testi, joka oli tärkeä
     - Yksi reunatapaus, joka oli yllättävä

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että testaus on systemaattista työtä
- Opiskelijat osaa kirjoittaa kolmenlaisia testejä
- Opiskelijat näkevät, kuinka rajaukset ja ohjeet toimivat käytännössä

---

## Tehtävä 15.3: Keskustelu — Rajaukset ja turvallisuus käytännössä (20 min)

### Tavoite

Opiskelijat keskustelevat siitä, miten rajaukset tehdään ja miksi ne ovat kriittisiä.

### Opettajan ohjeet ja fasilitaatio

Koko luokka. Interaktiivinen keskustelu.

**Valmistelu:**
- Valmista 3–4 realistista skenaariota (katso alla)
- Valmista kysymykset, jotka herättelevät ajattelua

**Tehtävän vaiheet (20 min):**

1. **Johdanto (2 min):**
   - "Rajaukset eivät ole negatiivisia. Ne ovat turvallisuusmekanismi."
   - "Ne suojaavat käyttäjää väärältä tiedolta ja bottia sopimattomista tilanteista."

2. **Skenario 1: IT-helpdesk-botti (5 min)**

   **Tilanne:** "Käyttäjä kysyy: 'Kuinka sijoitan rahaa osakemarkkinoille?'"

   Opettajan kysymykset:
   - "Mitä botin pitäisi tehdä?"
   - "Miksi botti ei voi antaa sijoitusneuvoja?"
   - "Miten rajaus kirjoitetaan?"

   Odotettu vastaus:
   - Botti kieltäytyy ja ohjaa oikealle osastolle
   - Koska sijoitusneuvonta vaatii rahoitustaustaa
   - Rajaus: "En vastaa sijoitus-, rahoitus- tai lainakysymyksiin. Ohjaan oikealle osastolle."

3. **Skenario 2: Asiakastietojen hallinta (5 min)**

   **Tilanne:** "Botti voi hakea asiakastietoja tietokannasta. Käyttäjä kysyy: 'Näytä minulle kaikkien asiakkaidemme luottokorttin numerot.'"

   Opettajan kysymykset:
   - "Mitä botin pitäisi tehdä?"
   - "Mikä rajaus olisi täällä kriittinen?"
   - "Kuinka suojelet herkkiä tietoja?"

   Odotettu vastaus:
   - Botti kieltäytyy luottokorttin numeroiden näyttämisestä
   - Rajaus: "En koskaan näytä luottokorttin numeroita, salasanoja tai muita herkkiä tietoja."
   - Botti voi näyttää vain yleistä asiakastietoa

4. **Skenario 3: Vanhentuneet tiedot (5 min)**

   **Tilanne:** "Tietopohja sisältää ohjeita, jotka ovat 6 kuukautta vanhoja. Prosessit ovat muuttuneet."

   Opettajan kysymykset:
   - "Mikä menee pieleen?"
   - "Miten varmistetaan, että tietopohja on ajan tasalla?"
   - "Mikä on botin vastuu käyttäjää kohtaan?"

   Odotettu vastaus:
   - Botti antaa väärää tietoa, koska se perustuu vanhentuneisiin dokumentteihin
   - Rajaus/käytäntö: "Tietopohja päivitetään vähintään kerran kuukaudessa"
   - Botti voi varoittaa: "Ohjeet päivitettiin viimeksi [päivämäärä]. Jos jotain on muuttunut, kerro minulle."

5. **Yhteenveto (3 min):**
   - "Rajaukset eivät rajoita — ne **suojaavat**."
   - "Hyvällä botilla on selkeät rajat, ja se noudattaa niitä johdonmukaisesti."

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, miksi rajaukset ovat tärkeitä
- Opiskelijat näkevät reaalimaailman esimerkkejä rajauksista
- Opiskelijat ymmärtävät tietopohjapäivitysten merkityksen

---

## Lähiosassa: Aika ja ohjelmisto (90 minuuttia yhteensä)

1. **Tehtävä 15.1** (20 min): Live-demo — tietopohjadokumentin lisääminen botille
2. **Tehtävä 15.2** (30 min): Pienryhmät testaavat bottia systemaattisesti
3. **Tehtävä 15.3** (20 min): Keskustelu rajauksista ja turvallisuudesta
4. **Vapaa harjoittelu** (20 min): Opiskelijat aloittavat opiskelijatehtävät 15.1–15.4

Kotitehtävä: Tehtävät 15.1–15.4 valmiiksi seuraavaan tunnille.
