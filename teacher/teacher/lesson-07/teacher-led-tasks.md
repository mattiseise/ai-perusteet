# Opettajavetoiset harjoitukset: Gen AI:n luonne

## Harjoitus 1: Sama prompti, eri mallit — epädeterminismin demonstraatio

### Tavoite
Näyttää käytännössä, miksi tulokset vaihtelevat ja että tämä johtuu mallin rakenteesta, ei käyttäjän virheestä.

### Ohjeet ja vaiheet

**Kesto: 15 minuuttia**

1. **Valmistelu (5 min ennen oppituntia):**
   - Avaa useita AI-malleja selaimessasi (esim. ChatGPT, Claude, Google Gemini).
   - Kirjoita samankaltainen prompti kaikille malleille.

   **Esimerkkiprompti:**
   ```
   Kirjoita lyhyt koodinpätkä (5-10 riviä), joka
   tekee seuraavaa: lue tiedosto nimeltä "data.txt",
   laske rivien lukumäärä ja tulosta tulos.
   ```

2. **Luokkaharjoitus (10 min):**
   - Näytä opetusnäytöllä ChatGPT:n vastaus.
   - Kysy: "Kuka voi ennustaa, mitä Claude sanoo?"
   - Näytä Clauden vastaus. Vertaa:
     - Onko syntaksi sama vai eri?
     - Onko mukana kommentteja? Entä virheitä?
     - Millainen on kokonaistyyli?
   - Näytä Google Geminin vastaus. Vertaa jälleen.

3. **Keskustelu:**
   - "Miksi vastaukset ovat erilaisia, vaikka kaikki mallit on koulutettu samankaltaisilla teksteillä?"
   - Johdattele opiskelijat ymmärtämään: *mallit tekevät todennäköisyyspohjaisia valintoja*, eivät hakuun perustuvia tai deterministisiä algoritmeja.
   - Mainitse lämpötila: "Jokainen malli valitsee hieman eri 'reittejä' seuraavien sanojen joukosta."

4. **Johtopäätös:**
   - "Tämä on ominaisuus, ei vika. Epädeterminismi mahdollistaa luovuuden."
   - "Mutta se merkitsee sitä, ettei samaa vastausta saa aina uudelleen."

**Opettajan muistiinpanot:**
- Ole valmis siihen, että jotkin vastaukset saattavat sisältää hallusinaatioita (esim. väärän funktion). Käytä sitä opetuksessa!
- Jos vastaukset ovat hyvin samankaltaisia, selitä: "Koska kaikkien mallien koulutusdata on samankaltaista, usein samankaltaiset vastaukset ovat todennäköisimpiä."

---

## Harjoitus 2: Hallusinaatioiden metsästys — ryhmän analyysi

### Tavoite
Oppia tunnistamaan hallusinaatioita ja ymmärtämään niiden mekanismia.

### Ohjeet ja vaiheet

**Kesto: 20 minuuttia**

1. **Ryhmän jakaminen (2 min):**
   - Jaa opiskelijat 3–4 henkilön ryhmiin.
   - Anna jokaiselle ryhmälle eri "hallusinaatio-case".

2. **Case-tutkimukset (valitse 2–3):**

   **Case 1 (Tekniikka):**
   AI-malli sanoo: "Pythonissa funktiota `urllib3.get_json(url)` käytetään JSON-datan hakemiseen."
   - Tarkista: Onko tämä funktio olemassa?
   - Miksi malli hallusinoi sen?

   **Case 2 (Historia):**
   AI-malli sanoo: "Suomen ensimmäinen pääministeri oli Mikael Agricola."
   - Tarkista: Kuka oli ensimmäinen pääministeri?
   - Miksi malli sekoitti asian?

   **Case 3 (API-dokumentaatio):**
   AI-malli dokumentoi API-päätepisteen: "GET /users/{id}/profile — palauttaa käyttäjän profiilin ja salasanan."
   - Tarkista: Palauttaisiko API koskaan salasanan?
   - Miksi malli ehdotti turvatonta toimintoa?

3. **Ryhmän tehtävä (10 min):**
   - Tutkikaa tapauksianne.
   - Täyttäkää taulukko:

   | Väite | Oikein vai väärä | Missä tarkistit | Hallusinaation merkkejä | Miksi malli hallusinoi |
   |---|---|---|---|---|
   | [AI:n väite] | | | | |

4. **Esittäminen (8 min):**
   - Jokainen ryhmä esittelee löydöksensä 2–3 minuutissa.
   - Opettaja korostaa: "Hallusinaatiot eivät ole ilmiselviä. Malli esittää ne täysin vakaasti."

**Opettajan muistiinpanot:**
- Valmistele case-tutkimukset etukäteen — testaa ne kaikissa malleissa (ChatGPT, Claude jne.).
- Hallusinaatiot vaihtelevat malleittain, joten jokaisen mallin käyttäytyminen on mielenkiintoista.
- Jos ryhmällä on vaikeuksia hallusinaation löytämisessä, anna vihje: "Onko väite liian yksityiskohtainen? Onko se 'näyttävä' mutta epävarma?"

---

## Harjoitus 3: Verifiointiprosessin suunnittelu

### Tavoite
Opettaa opiskelijoille, miten integroida AI-apu ammatilliseen työnkulkuun ilman, että hallusinaatiot pääsevät virheiksi.

### Ohjeet ja vaiheet

**Kesto: 25 minuuttia**

1. **Skenaario (5 min):**
   Esitä seuraava skenaario:

   "Sinulla on tehtävä kirjoittaa SQL-kysely tietokantaan, joka hakee kaikki asiakkaat, joiden maksu on erääntynyt yli 30 päivää. Käytät ChatGPT:tä koodin kirjoittamisen tukena."

2. **Ryhmäkeskustelu — verifiointivaiheet (10 min):**
   Jaa opiskelijat pienryhmiin ja kysy:

   - **Vaihe 1:** Ennen kuin kysyt ChatGPT:ltä — mitä sinun täytyy jo tietää? (Tietokannan sarakkeet? Päivämäärämuodot?)
   - **Vaihe 2:** Miten kirjoitat promptin? Mitä yksityiskohtia pyydät?
   - **Vaihe 3:** Miten analysoit vastauksen? Mistä merkeistä epäilet hallusinaatiota?
   - **Vaihe 4:** Miten testaat koodia ennen käyttöä? (Testidata? Lokit?)
   - **Vaihe 5:** Miten dokumentoit? (Miksi valitsit ChatGPT:n vastauksen sellaisenaan?)

3. **Esittäminen (10 min):**
   - Jokainen ryhmä esittelee yhden vaiheen 2–3 minuutissa.
   - Opettaja kirjoittaa "verifiointiprosessin" taululle.

   **Esimerkkiprosessi:**
   ```
   1. Ymmärrä tietokannan rakenne (tarkista dokumentaatiosta)
   2. Kirjoita spesifinen prompt (sisällytä sarakkeiden nimet)
   3. Analysoi vastaus (vertaa dokumentaatioon, tarkista syntaksi)
   4. Testaa heikolla testidatalla (ennen oikeaa dataa)
   5. Dokumentoi: "ChatGPT ehdotti X, otin sen koska Y, muutin Z koska..."
   ```

**Opettajan muistiinpanot:**
- Korosta: **verifiointiprosessi ei ole opiskelijoiden oma idea — se on ammatillinen standardi.**
- Jos opiskelijat sanovat "Tämä on liian monimutkaista", vastaa: "Kyllä, siksi monet yritykset tekevät virheitä tekoälyn kanssa. Sinä olet se, joka tekee sen oikein."

---

## Opettajan tärkeitä huomioita

**Avainviesti 1: Epädeterminismi on ominaisuus, ei vika.**
- Johdonmukaisuus ja luovuus ovat saman välineen kaksi päätä.
- Opettajat neuvovat usein: "Käytä matalan lämpötilan asetuksia teknisten tehtävien kanssa, korkeampia ideointiin."

**Avainviesti 2: "Näyttävä" ei ole "oikea".**
- Hallusinaatiot voivat kuulostaa täysin itsevarmoilta.
- IT-ammattilaisella on sisäinen "kuulostaa oikealta" -anturi, mutta sekään ei aina toimi.
- **Verifiointia ei voi ohittaa.**

**Avainviesti 3: Vastuu on käyttäjällä.**
- Jos annat asiakkaalle AI-avusteisen raportin, sinä vastaat sen oikeellisuudesta.
- Malli ei ole syyllinen — sinä olet.
- Tämä ei ole pelottelua — tämä on ammattilaisuutta.

---

## Sisäänrakennetut keskustelun herättäjät

**Jos opiskelijat sanovat:** "Entä jos käytän yksinkertaisesti AI:tä sellaisenaan, ilman verifiointia?"
**Vastaa:** "Silloin riskit kohdistuvat sinuun ja organisaatioosi. Tekniikan kanssa hallusinaatiot ovat erityisen vaarallisia, koska koodi voi epäonnistua tuotannossa tai avata tietoturva-aukkoja."

**Jos opiskelijat sanovat:** "Tämä tekee tekoälystä käyttökelvottoman."
**Vastaa:** "Ei. Se tekee siitä sopivasta käytöstä riippuvaisen. Samoin kuin saha — sillä voi katkaista ranteen, mutta se on silti hyödyllinen työkalu, kun sitä käyttää oikein."