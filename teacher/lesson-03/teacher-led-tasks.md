# Opettajavetoiset tehtävät

## Tehtävä 3.1: Seuraavan sanan ennustaminen — Luokkakeskustelu ja demo

### Tavoite
Näyttää konkreettisesti, miten kielimalli tekee päätelmiä yksi sana kerrallaan.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
Valmista teksti, jossa sanat puuttuvat:
"Seuraavaksi hän avasi ____ ja luki kirjeistä. Kaikki olivat ____."

Projisoi tai kirjoita liitutaululle.

**Toteutus (20 minuuttia):**

1. **Avaus (2 min):** "Nyt harjoittelemme, miten kielimalli ajattelee. Se arvaa seuraavaa sanaa kerran. Osaatko sinä?"

2. **Jokaisen sanan arvaus (10 min):**
   - Ensimmäinen sana: "avasi ____"
   - Kysy luokalta: "Mikä sana tulee seuraavaksi?"
   - Keräää 5-6 ehdotusta liitutaululle.
   - Kysy: "Mitä yhteistä näillä sanoilla on?"
   - Näytä ChatGPT:n vastaus samalla kehotuksella.
   
   - Toinen sana: "Kaikki olivat ____"
   - Sama prosessi.

3. **Analyysi (5 min):**
   - "Näette, että malli valitsee *todennäköisintä* sanaa. Se ei tiedä, mikä on oikea. Se vain tietää, mitkä sanat näkyvät usein tässä yhteydessä datassa."
   - Kirjoita lautaan: "Next-token prediction = arvaus todennäköisyyden perusteella, sana kerrallaan."

4. **Johtopäätös (3 min):**
   - "Siksi ChatGPT näyttää älykäältä — mutta se tekee yhden arvausta kerrallaan."

### Odotettu oppimistulos

Opiskelijat näkevät:
- Kielimalli ei "ajattele" koko vastausta — se ennustaa joka sana.
- "Älykkyys" tulee siitä, että sanojen yhdistelmät ovat usein toimivia.
- Malli voi mennä pieleen missä tahansa vaiheessa.

---

## Tehtävä 3.2: Hallusinaatiot live — Näytä virhe ja analysoi

### Tavoite
Osoittaa, että kielimalli tekee vakuuttavan näköisiä mutta väärä vastauksia.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
Keksitään kolme kysymystä, joille kielimalli antaa väärän vastauksen:
1. Ei-olemassa oleva kirja/elokuva
2. Fakta vuodesta 2026 (jonka tiedät olevan väärä)
3. Henkilö, jolle antaa väärän roolin

Esimerkiksi:
- "Kuka kirjoitti romaanin 'Suuri Älyntestaus'?" (ei ole)
- "Mikä on Suomen pääkaupunkina 2026?" (Helsinki, mutta mukaansa saattaa tulla väärä)
- "Kuka on Teknillisen korkeakoulun rehtori 2026?" (tietää, että malli voi haluavansa, mutta tarkista tosiasiallisesti)

**Toteutus (20 minuuttia):**

1. **Avaus (2 min):** "Näytän teille, miten kielimalli voi valehdelleen vakuuttavasti. Tätä kutsutaan hallusinaatioksi."

2. **Testi 1 live (5 min):**
   - Kysy ChatGPT:ltä: "Kuka kirjoitti 'Suuri Älyntestaus'?"
   - ChatGPT antaa vastauksen (joka on väärä).
   - Kysy luokalta: "Näyttääkö oikeilta? Miten tiedämme, onko se väärä?"
   - Selitä: "Malli näki tekstissä sanoja 'kirjoitti', 'romaani', 'suuri' yhdessä niin usein, että se arvasi tämän yhdistelmän."

3. **Testi 2 ja 3 (8 min):**
   - Sama prosessi.
   - Kysy jokaisen jälkeen: "Ovatko parametrit 'antava valehdella' vai 'arvaavat väärin'?"

4. **Analyysi (5 min):**
   - Kirjoita lautaan:
   ```
   HALLUSINAATIO = malli ennustaa vääriä sanoja todennäköisyyden perusteella
   VAARA: vastaukset näyttävät oikeilta, joten käyttäjä voi uskoa niitä.
   ```
   - Kysy: "Missä ammattitehtävissä hallusinaatiot olisivat vaarallisimpia?" (Lääketiede, oikeus, liikesalaisuudet...)

### Odotettu oppimistulos

Opiskelijat näkevät:
- Kielimalli ei tiedä, onko vastaus oikein.
- Hallusinaatiot ovat turvallisuusriski.
- Ammattilaisena sinun täytyy validoida vastauksia, ei sokeasti luottaa.

---

## Tehtävä 3.3: Lämpötilan ymmärtäminen — Pareittain keskustelu

### Tavoite
Ymmärtää, miksi lämpötila on tärkeä parametri ja kuinka sitä käytetään käytännössä.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
Keksi kaksi tehtävää:
1. Tarkkaa vastaus tarvitseva: "Kuka voitti Worldin Cup 1998?" (matala lämpötila)
2. Luova: "Kirjoita runon syksystä" (korkea lämpötila)

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
   - Selitä: "Tämä tehtävä vaatii matalan lämpötilan — haluan oikean vastauksen, ei vaihtelua."
   - Kysy: "Entä jos lämpötila olisi korkea? Mitä voisi tapahtua?" (Väärä vastaus, koska malli arvaa.)

3. **Tehtävä 2: Luovuus (5 min):**
   - Kysy: "Kirjoita runo syksystä."
   - Selitä: "Tämä tehtävä hyötyy korkeammasta lämpötilasta — haluan vaihtelua, luovuutta."
   - Jos matala: Sama runo joka kerta (tylsää).
   - Jos korkea: Eri runot, mutta joskus outoja sanoja.

4. **Johtopäätös (2 min):**
   - Ammattilaisena: Valitse lämpötila tehtävän mukaan.
   - Kriittiset: matala. Luovat: korkea.

### Odotettu oppimistulos

Opiskelijat näkevät:
- Lämpötila on "säätö" luovuudelle ja johdonmukaisuudelle.
- Ei ole yksi "oikea" lämpötila — se riippuu tehtävästä.
