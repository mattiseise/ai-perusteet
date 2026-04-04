# Opettajavetoiset harjoitukset: Gen AI:n luonne

## Harjoitus 1: Sama promt, eri mallit — epädeterminismin demonstraatio

### Tavoite
Näyttää käytännössä, miksi tulokset vaihtelevat ja että tämä johtuu mallin rakenteesta, ei käyttäjän virheestä.

### Ohjeet ja vaiheet

**Kesto: 15 minuuttia**

1. **Valmistelu (5 min ennen oppituntia):**
   - Avaa useita AI-malleista selaimessasi (esim. ChatGPT, Claude, Google Gemini)
   - Kirjoita samankaltainen promt kaikille malleille

   **Esimerkki promt:**
   ```
   Kirjoita lyhyt koodinpätkä (5-10 riviä), joka
   tekee seuraavaa: lue tiedosto nimeltä "data.txt",
   laske rivien lukumäärä ja tulosta tulos.
   ```

2. **Luokkaharjoitus (10 min):**
   - Näytä opetusnäytöllä ChatGPT:n vastaus.
   - Kysy: "Kuka voi ennustaa, mitä Claude sanoo?"
   - Näytä Claude-vastaus. Vertaa:
     - Syntaksi sama vai eri?
     - Kommentit? Virheet?
     - Kokonaistyyli?
   - Näytä Google Gemini-vastaus. Vertaa jälleen.

3. **Keskustelu:**
   - "Miksi vastaukset ovat eri, vaikka kaikki mallit on kouluttu samankaltaisilla teksteillä?"
   - Johdattele opiskelijat ymmärtämään: *mallit tekevät todennäköisyyspohjaisia valintoja*, eivät hakuisia deterministisiä algoritmeja.
   - Mainitse lämpötila: "Jokainen malli valitsee hieman eri 'reittejä' seuraavien sanojen joukosta."

4. **Johtopäätös:**
   - "Tämä on ominaisuus, ei vika. Epädeterminismi mahdollistaa luovuuden."
   - "Mutta se merkitsee: älä luota siihen, että saat aina saman vastauksen."

**Opettajan muistiinpanot:**
- Ole valmis, että jotkut vastaukset saattavat sisältää hallusinaatioita (esim. väärä funktio). Käytä sitä opetuksessa!
- Jos vastaukset ovat hyvin samankaltaisia, selitä: "Koska kaikkien mallien koulutusdata on samankaltaista, usein samankaltaiset vastaukset ovat todennäköisimpiä."

---

## Harjoitus 2: Hallusinaatioiden metsästys — ryhmän analyysi

### Tavoite
Oppia tunnistamaan hallusinaatioita ja ymmärtämään niiden mekanismi.

### Ohjeet ja vaiheet

**Kesto: 20 minuuttia**

1. **Ryhmän jakaminen (2 min):**
   - Jaa opiskelijat 3–4 henkilön ryhmiin.
   - Anna jokaiselle ryhmälle eri "hallusinaatio-casetutkimus".

2. **Case-tutkimukset (valitse 2–3):**

   **Case 1 (Tekniikka):**
   AI-malli sanoo: "Pythonissa funktiota `urllib3.get_json(url)` käytetään JSON-datan hakemiseen."
   - Tarkista: Onko tämä funktio olemassa?
   - Miksi malli halusinoi sen?

   **Case 2 (Historia):**
   AI-malli sanoo: "Suomen ensimmäinen pääministeri oli Mikael Agricola."
   - Tarkista: Kuka oli ensimmäinen pääministeri?
   - Miksi malli sekoitti sen?

   **Case 3 (API-dokumentaatio):**
   AI-malli dokumentoi API-päätepisteen: "GET /users/{id}/profile — palauttaa käyttäjän profiilin ja salasanan."
   - Tarkista: Olisiko API koskaan palauttaa salasanan?
   - Miksi malli ehdotti turvattoman toiminnon?

3. **Ryhmän tehtävä (10 min):**
   - Tutkikaa tapauksianne.
   - Täyttää taulukko:

   | Väite | Oikein vai väärä | Missä tarkistit | Hallusinaation merkkejä | Miksi malli hallusinoi |
   |---|---|---|---|---|
   | [AI:n väite] | | | | |

4. **Esittäminen (8 min):**
   - Jokainen ryhmä esittelee löydöksensä 2–3 minuuttia.
   - Opettaja korostaa: "Hallusinaatiot eivät ole ilmiselviä. Malli väittää ne täysin vakaasti."

**Opettajan muistiinpanot:**
- Valmistele case-tutkimukset etukäteen — testaa ne kaikissa malleissa (ChatGPT, Claude jne.).
- Hallusinaatiot vaihtelevat malleittain, joten jokaisen mallin käyttäytyminen on mielenkiintoista.
- Jos ryhmällä on vaikeuksia hallusinaation löytämisessä, anna vihje: "Onko väite liian yksityiskohtainen? Onko se 'näyttävä' mutta epävarma?"

---

## Harjoitus 3: Verifiointiprosessin suunnittelu

### Tavoite
Opettaa opiskelijoille, miten integroida AI-apu ammatilliseen työnkulkuun ilman hallusinaatioiden pääsyä virheiksi.

### Ohjeet ja vaiheet

**Kesto: 25 minuuttia**

1. **Skenaario (5 min):**
   Esitä seuraava skenaario:

   "Sinulla on tehtävä kirjoittaa SQL-kysely tietokantaan, joka hakee kaikki asiakkaat, joiden maksu on erääntynyt enemmän kuin 30 päivää. Käytät ChatGPT:tä koodin auttamiseen."

2. **Ryhmäkeskustelu — verifiointivaiheet (10 min):**
   Jaa opiskelijat pienryhmiin ja kysy:

   - **Vaihe 1:** Ennen kuin kysyt ChatGPT:tä — mitä sinun täytyy jo tietää? (Tietokannan sarakkeet? Päivämäärä-muodot?)
   - **Vaihe 2:** Miten kirjoitat promptin? Mitä yksityiskohtia pyydät?
   - **Vaihe 3:** Miten analysoiv vastauksen? Mistä merkeistä epäilet hallusinaatiota?
   - **Vaihe 4:** Miten testat koodia ennen käyttöä? (Testidata? Lokit?)
   - **Vaihe 5:** Miten dokumentoit? (Miksi valitsit ChatGPT:n vastauksen muodossa?)

3. **Esittäminen (10 min):**
   - Jokainen ryhmä esittelee yhden vaiheen 2–3 minuuttia.
   - Opettaja kirjoittaa "verifiointiprosessin" taululle.

   **Esimerkki prosessi:**
   ```
   1. Ymmärrä tietokannan rakenne (tarkista dokumentaatiosta)
   2. Kirjoita spesifinen prompt (sisällytä sarakkeiden nimet)
   3. Analysoi vastaus (vertaa dokumentaatioon, tarkista syntaksi)
   4. Testaa heikolla testidatalla (ennen oikeaa dataa)
   5. Dokumentoi: "ChatGPT ehdotti X, otin sen koska Y, muutin Z koska..."
   ```

**Opettajan muistiinpanot:**
- Korostaa: **verifiointiprosessi ei ole opiskelijoiden oma idea — se on ammatillinen standardi.**
- Jos opiskelijat sanovat "Tämä on liian monimutkaista", vastaa: "Kyllä, siksi monet yritykset tekevät virheitä tekoälyllä. Sinä olet ne, jotka tekevät sen oikein."

---

## Opettajan tärkeitä kohtia

**Avainviesti 1: Epädeterminismi on ominaisuus, ei vika.**
- Johdonmukaisuus ja luovuus ovat kaksi päätä samasta välineestä.
- Opettajat usein neuvovat: "Käytä matalan lämpötilan asetuksia tekniikan kanssa, korkeampia ideointiin."

**Avainviesti 2: "Näyttävä" ei ole "oikea".**
- Hallusinaatiot voivat kuulostaa täydellisen itsevarmilta.
- IT-ammattilaisella on sisäinen "kuulostaa oikealta" -anturi, mutta se ei aina toimi.
- **Verifiointia ei voi ohittaa.**

**Avainviesti 3: Vastuu on käyttäjällä.**
- Jos annat asiakkaalle AI-avusteisen raportin, sinä vastaat sen oikeellisuudesta.
- Malli ei ole syyllinen — sinä olet.
- Tämä ei ole pelottelua — tämä on ammattilaisuus.

---

## Sisäänrakennetut keskustelun herättäjät

**Jos opiskelijat sanovat:** "Entä jos käytän yksinkertaisesti AI:tä sellaisenaan, ilman verifiointia?"
**Vastaa:** "Silloin riskit ovat sinussa ja organisaatiossasi. Tekniikan kanssa hallusinaatiot ovat erityisen vaarallisia, koska koodi voi epäonnistua tuotannossa tai avata tietoturva-aukkoja."

**Jos opiskelijat sanovat:** "Tämä tekee tekoälystä käyttökelvoton."
**Vastaa:** "Ei. Se tekee siitä riippuvaisen sopivasta käytöstä. Samoin kuin sahaa — sahalla voi katkaista rannetta, mutta se on silti hyödyllinen työkalu, kun käyttää sitä oikein."

