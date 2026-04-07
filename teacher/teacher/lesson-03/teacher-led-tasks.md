# Opettajavetoiset tehtävät

## Tehtävä 3.1: Seuraavan sanan ennustaminen — luokkakeskustelu ja demo

### Tavoite
Näyttää konkreettisesti, miten kielimalli tekee päätelmiä yksi sana kerrallaan.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**
Valmista teksti, josta sanoja puuttuu:
"Seuraavaksi hän avasi ____ ja luki kirjeistä. Kaikki olivat ____."

Projisoi teksti tai kirjoita se liitutaululle.

**Toteutus (20 minuuttia):**

1. **Avaus (2 min):** "Nyt harjoittelemme, miten kielimalli ajattelee. Se arvaa seuraavan sanan kerrallaan. Osaatko sinä?"

2. **Jokaisen sanan arvaus (10 min):**
   - Ensimmäinen sana: "avasi ____"
   - Kysy luokalta: "Mikä sana tulee seuraavaksi?"
   - Kerää 5–6 ehdotusta liitutaululle.
   - Kysy: "Mitä yhteistä näillä sanoilla on?"
   - Näytä ChatGPT:n vastaus samalla kehotteella.
   
   - Toinen sana: "Kaikki olivat ____"
   - Sama prosessi.

3. **Analyysi (5 min):**
   - "Näette, että malli valitsee *todennäköisimmän* sanan. Se ei tiedä, mikä on oikea. Se vain tietää, mitkä sanat esiintyvät usein tässä yhteydessä datassa."
   - Kirjoita taululle: "Next-token prediction = arvaus todennäköisyyden perusteella, sana kerrallaan."

4. **Johtopäätös (3 min):**
   - "Siksi ChatGPT näyttää älykkäältä — mutta se tekee yhden arvauksen kerrallaan."

### Odotettu oppimistulos

Opiskelijat näkevät:
- Kielimalli ei "ajattele" koko vastausta — se ennustaa jokaisen sanan.
- "Älykkyys" tulee siitä, että sanojen yhdistelmät ovat usein toimivia.
- Malli voi mennä pieleen missä tahansa vaiheessa.

---

## Tehtävä 3.2: Hallusinaatiot livenä — näytä virhe ja analysoi

### Tavoite
Osoittaa, että kielimalli tekee vakuuttavan näköisiä mutta vääriä vastauksia.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**
Keksi kolme kysymystä, joihin kielimalli antaa väärän vastauksen:
1. Ei-olemassa oleva kirja/elokuva
2. Fakta vuodesta 2026 (jonka tiedät olevan väärä)
3. Henkilö, jolle se antaa väärän roolin

Esimerkiksi:
- "Kuka kirjoitti romaanin 'Suuri Älyntestaus'?" (ei ole olemassa)
- "Mikä on Suomen pääkaupunki vuonna 2026?" (Helsinki, mutta malli saattaa antaa väärän vastauksen)
- "Kuka on Teknillisen korkeakoulun rehtori vuonna 2026?" (tiedät, että malli voi arvata väärin, mutta tarkista asia tosiasiallisesti)

**Toteutus (20 minuuttia):**

1. **Avaus (2 min):** "Näytän teille, miten kielimalli voi vaikuttaa vakuuttavalta, vaikka se olisi väärässä. Tätä kutsutaan hallusinaatioksi."

2. **Testi 1 livenä (5 min):**
   - Kysy ChatGPT:ltä: "Kuka kirjoitti 'Suuri Älyntestaus'?"
   - ChatGPT antaa vastauksen (joka on väärä).
   - Kysy luokalta: "Näyttääkö tämä oikealta? Miten tiedämme, onko se väärä?"
   - Selitä: "Malli näki tekstissä sanoja 'kirjoitti', 'romaani' ja 'suuri' yhdessä niin usein, että se arvasi tämän yhdistelmän."

3. **Testit 2 ja 3 (8 min):**
   - Sama prosessi.
   - Kysy jokaisen jälkeen: "Valehtelevatko parametrit vai arvaavatko ne väärin?"

4. **Analyysi (5 min):**
   - Kirjoita taululle:
   ```
   HALLUSINAATIO = malli ennustaa vääriä sanoja todennäköisyyden perusteella
   VAARA: vastaukset näyttävät oikeilta, joten käyttäjä voi uskoa niitä.
   ```
   - Kysy: "Missä ammattitehtävissä hallusinaatiot olisivat vaarallisimpia?" (Lääketiede, oikeus, liikesalaisuudet...)

### Odotettu oppimistulos

Opiskelijat näkevät:
- Kielimalli ei tiedä, onko vastaus oikein.
- Hallusinaatiot ovat turvallisuusriski.
- Ammattilaisena sinun täytyy validoida vastaukset, ei luottaa niihin sokeasti.

---

## Tehtävä 3.3: Lämpötilan ymmärtäminen — pareittain käytävä keskustelu

### Tavoite
Ymmärtää, miksi lämpötila on tärkeä parametri ja kuinka sitä käytetään käytännössä.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**
Keksi kaksi tehtävää:
1. Tarkkaa vastausta tarvitseva: "Kuka voitti World Cupin 1998?" (matala lämpötila)
2. Luova: "Kirjoita runo syksystä" (korkea lämpötila)

**Toteutus (15 minuuttia):**

1. **Peruskäsite (3 min):**
   - Selitä: "Lämpötila kontrolloi, kuinka satunnaisia vastaukset ovat."
   - Piirrä kaavio:
   ```
   Lämpötila 0.1 → Sama vastaus aina
   Lämpötila 0.5 → Jonkin verran vaihtelua
   Lämpötila 1.0+ → Paljon satunnaisuutta
   ```

2. **Tehtävä 1: Tarkkuus (5 min):**
   - Kysy: "Kuka voitti World Cupin 1998?"
   - Selitä: "Tämä tehtävä vaatii matalan lämpötilan — haluan oikean vastauksen, en vaihtelua."
   - Kysy: "Entä jos lämpötila olisi korkea? Mitä voisi tapahtua?" (Väärä vastaus, koska malli arvaa.)

3. **Tehtävä 2: Luovuus (5 min):**
   - Kysy: "Kirjoita runo syksystä."
   - Selitä: "Tämä tehtävä hyötyy korkeammasta lämpötilasta — haluan vaihtelua ja luovuutta."
   - Jos matala: Sama runo joka kerta (tylsää).
   - Jos korkea: Eri runoja, mutta joskus outoja sanoja.

4. **Johtopäätös (2 min):**
   - Ammattilaisena: valitse lämpötila tehtävän mukaan.
   - Kriittiset tehtävät: matala. Luovat tehtävät: korkea.

### Odotettu oppimistulos

Opiskelijat näkevät:
- Lämpötila on "säätö" luovuudelle ja johdonmukaisuudelle.
- Ei ole yhtä "oikeaa" lämpötilaa — se riippuu tehtävästä.