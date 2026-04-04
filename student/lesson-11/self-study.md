# Promptit I: selkeä tehtävänanto

## Johdanto: Miksi sama kysymys antaa erilaisia vastauksia

Yleinen kokemus: kysyt ChatGPT:tä "Mitä on verkko?", ja saat vastauksen. Huomenna kysyt täsmälleen samaa, ja vastaus on hieman erilainen. Tai kysyt "Kirjoita funktio, joka validoi sähköpostiosoitteen", ja malli antaa koodia, joka on sekavaa tai puutteellista.

Ongelma ei ole tekoälyssä — ongelma on sinun kysymyksessä. Kysymys ei ole *selkeä tehtävänanto*. Se on vain kysymys. Ammattilaisesti hyvä prompt ei ole sama kuin hyvä kysymys. Prompt on **täydellinen tehtävänanto**, joka kertoo tekoälylle:

- Mitä täytyy tehdä (tavoite)?
- Kuka tekee sen (rooli)?
- Mitä rajoit­tuksia on (mitä EI tehdä)?
- Miten vastaus tulee muotoilla (output­formaatti)?
- Millä kielellä?
- Millaisia esimerkkejä haluat nähdä?

Kun kirjoitat näin selkeän promptin, tekoäly antaa parempia, johdonmukaisempia ja käyttökelpoisempia vastauksia. Tämä oppitunti opettaa sinulle hyvän promptin rakentamisen ammattilaisesti.

## Osa 1: Hyvän promptin rakenne — viisi peruselementtiä

Hyvä prompt rakentuu viidestä osasta. Et tarvitse kaikkia joka promptiin — mutta tietäminen, mitkä osat voit käyttää, tekee sinusta paremman käyttäjän.

**1. Tavoite (goal):** Mitä haluat? "Kirjoita tämä", "Selitä tämä", "Paranna tämä". Tavoite on selkeä lause, joka sanoo, mitä tekoäly tekee.

**2. Rooli (role):** Kuka tekoäly on? "Olet Python-kehittäjä", "Olet opettaja", "Olet tietoturva­asiantuntija". Rooli auttaa mallia omaksumaan oikean näkökulman.

**3. Rajat (constraints):** Mitä EI tehdä? "Älä käytä monimutkaisia SQL-kyselyitä", "Kirjoita maksimissaan 3 lausetta", "Älä mainitse hintoja". Rajat antavat mallille selkeän alueen.

**4. Output­formaatti (format):** Miten haluat vastauksen? "Vastaa JSON-muodossa", "Kirjoita taulukko", "Anna vaihe­kohtaiset ohjeet". Formaatti varmistaa, että saat käyttökelpoisen tuloksen.

**5. Esimerkit (examples):** Näytä yksittäinen esimerkki siitä, mitä haluat. "Esimerkiksi: INPUT: 'terve', OUTPUT: 'Terve! Kuinka voin auttaa?'". Esimerkit tekevät vaatimuksesta konkreettisemmiksi.

Ammattilaisesti nämä viisi elementtiä ovat sinun perustyökalusarja. Sitä enemmän tietoja annat, sitä parempia vastauksia saat.

> **Pysähdy hetkeksi:** Ajattele viimeistä kertaa, kun kysyit ChatGPT:tä jotain. Mitä viidestä elementistä annoit? Mitä puuttui? Olisiko tieto­parempi vastaus ollut, jos olisit antanut puuttuvat elementit?

## Osa 2: Ero promptin ja kontekstin välillä

Tässä on tärkeä käsitteellinen ero, joka hämmentää monina: **prompt ei ole sama kuin konteksti**.

Prompt on *tehtävänanto* — se, mitä nyt haluat tekoälyn tekevän. Konteksti on *ympäröivä tieto* — kaikki tieto, jonka tekoäly tarvitsee sen tehtävän ratkaisemiseksi hyvin.

Esimerkiksi: "Kirjoita sähköposti asiakaalle, joka valittui palvelusta." On prompt. Mutta konteksti voi olla: "Asiakas otti yhteyttä 2 kertaa. Ensimmäisellä kerralla hän ei saanut vastausta 48 tunnissa. Toisella kerralla hän sai vastauksen, mutta se ei ratkaisut hänen ongelmaansa." Konteksti on kriittinen — ilman sitä tekoäly ei osaa kirjoittaa oikein sävyä olevaa sähköpostia.

Ammattilaisesti opit rakentamaan kontekstia iteratiivisesti. Ensimmäisessä promptissa annat tehtävän. Seuraavassa promptissa annat kontekstia ("Asiakas on arvokas pitkäaikainen asiakas"). Seuraavassa vielä lisää ("Hän oli hämmentynyt, ei vihainen"). Jokainen iteraatio terävöittää vastauksen.

Monella opiskelijalla on ongelma: he ajattelevat, että "hyvä prompt" on yksi iso teksti, jossa on kaikki tarvittava. Oikeasti ammattilaiset **rakentavat kontekstia kierros kierrokselta**. Ensimmäinen prompt kertoo, mitä haluat. Toinen prompt antaa taustatietoja. Kolmas prompt pyytää muutosta. Neljäs prompt "ok, hyväksi, mutta..". Tämä iteratiivinen prosessi on ammattilaiset kutsuvat "prompt engineeringiksi".

> **Pysähdy hetkeksi:** Miksi iteratiivinen kontekstin rakentaminen olisi parempi kuin "kaiken kerralla" -prompti? Mitä ammattilaisesti voisi mennä pieleen, jos yrität kertoa kaiken kerralla?

## Osa 3: Huonosta promptista hyvään — käytännön esimerkki

Katsotaan konkreettinen esimerkki. Alla on huono prompt ja hyvä prompt samasta tehtävästä.

**Huono prompt:**
"Kirjoita funktio joka validoi sähköpostiosoitteen."

Miksi se on huono? Koska se ei sisällä:
- Roolia: Oletko kehittäjä? Opettaja?
- Rajoituksia: Kuinka tiukka validaatio? Hyväksytkö "+"-merkin? Kuinka pitkä osoite?
- Formaattia: Halutko koodin? Regex-patternin? Selityksen?
- Esimerkkejä: Mitä "oikea" osoite on? Mitä "väärä"?

Tekoäly tekee arauksia joka kohdassa ja antaa sinulle jonkun version, joka *saattaa* olla sinun tarpeisiisi.

**Hyvä prompt:**
"Olet Python-kehittäjä. Kirjoita funktio nimellä `validate_email()`, joka ottaa merkkijonon ja palauttaa True, jos se on validi sähköpostiosoite, False muuten. Käytä regex-kuviota. Hyväksy vain näitä muotoja: name@example.com. Hylkää välilyönnit ja erikoismerkit. Formaatti: Python-funktio, 5-10 riviä, kommenteilla. Esimerkki: validate_email('test@example.com') palauttaa True, validate_email('test @example.com') palauttaa False."

Miksi se on hyvä?
- Rooli: "Python-kehittäjä" — malli tietää kontekstit.
- Tavoite: "kirjoita funktio" — selkeä.
- Rajat: "vain näitä muotoja", "hylkää välilyönnit" — tarkka.
- Formaatti: "Python-funktio, 5-10 riviä" — malli tietää pituuden.
- Esimerkit: Kaksi tapausta — mitä pitäisi onnistua, mitä epäonnistua.

Ammattilaisesti hyvä prompt säästää aikaa. Joudut ehkä käyttämään enemmän aikaa promptin kirjoittamiseen, mutta saat parempia tuloksia ja vähemmän iteraatioita.

## Osa 4: Kontekstin rakentaminen ammattilaisesti

Kun käytät tekoälyä ammattilaisesti, et yleensä pysty antamaan kaikkea yhdessä promptissa. Joskus et edes tiedä, mitä sinun täytyy pyytää, kunnes näet ensimmäisen vastauksen.

Ammattilaiset rakentavat kontekstia *iteratiivisesti*:

**Kierros 1:** "Kirjoita Python-funktio, joka validoi sähköpostiosoitteen."
- Saat: perus regex-funktio

**Kierros 2:** "Lisää tuki plus-osoitteisiin (test+tag@example.com). Lisää docstring."
- Saat: parannettu versio

**Kierros 3:** "Nyt kirjoita testit tälle funktiolle. Sisällytä vähintään 5 tapausta."
- Saat: test-suite

**Kierros 4:** "Muuta testit pytest-muotoon ja lisää seuraavat edge-caset: osoite ilman TLD:tä, osoite yli 254 merkin."
- Saat: täydellinen test-suite

Jokainen kierros rakentaa edellisen päälle. Tekoäly "muistaa" kontekstin jokaisessa kierroksessa (riippuen siitä, mitä mallia käytät ja onko se yhdessä sessioissa vai eri sessioissa).

Ammattilaisesti tämä on tehokas. Et yritä ennustaa kaikkea etukäteen. Teet iteratiivisesti, näet tuloksia ja parannella.

## Yhteenveto

Hyvä prompt on **strukturoitu tehtävänanto**, ei satunnainen kysymys. Se sisältää viisi osaa: tavoite, rooli, rajat, formaatti ja esimerkit. Tärkeämpi kuin yksi suurenmoinen prompt on **iteratiivinen prosessi**: alusta yksinkertainen prompt, anna kontekstia kierros kierrokselta, paranna tuloksia vaihe vaiheelta. Ammattilaisesti opit, että "hyvä prompt-kirjoitus" tarkoittaa tarkkoja tehtävänantoja ja joustavia iteraatioita, ei joitain mystisiä salaisuuksia.
