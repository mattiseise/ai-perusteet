# Opettajavetoiset tehtävät

## Tehtävä 11.1: Prompt-rakentamisen demo — Live-workshop

### Tavoite
Näyttää opiskelijoille konkreettisesti, kuinka hyvän promptin rakentaminen toimii ja mitä eroa sillä on huonoon promptiin.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu (ennen lähiosaa):**
- Kirjoita taululle tai kalvoihin viisi elementtiä: tavoite, rooli, rajat, formaatti, esimerkki.
- Valmistele huono prompt: "Kirjoita funktio validoinnille."
- Valmistele sama tehtävä hyvänä promptina.
- Jos mahdollista, avaa ChatGPT tai Claude projektorilla.

**Tehtävän vaiheet (25 min):**

1. **Johdanto (2 min):**
   - "Tänään harjoittelemme sellaista, mitä ammattilaiset tekevät päivittäin: kirjoitamme hyviä prompteja. Näytän ensin huonon, sitten parannelen sen."

2. **Huono prompt — Live-esitys (6 min):**
   - Näytä projektorilla tai taululle huono prompt.
   - Selitä: "Tämä prompt on epäselvä. Miten tekoäly voi vastata hyvin, jos ei tiedä...?" — listaa mitä puuttuu.
   - Jos pääsy ChatGPT:hen: testaa prompt live. Opiskelijat näkevät, että vastaus on yleinen ja epäspesifi.

3. **Parannettu prompt — Vaihe vaiheelta (10 min):**
   - Aloita samasta huonosta promptista.
   - Lisää **tavoite**: "Mitä täsmälleen haluan? Ei vain 'validointi' — validoin sähköpostiosoitetta!"
   - Lisää **rooli**: "Kuka tekee? Python-kehittäjä vai JavaScript-kehittäjä?"
   - Lisää **rajat**: "Kuinka tiukka validaatio? Hyväksytkö plus-osoitteita? Alias-osoitteita?"
   - Lisää **formaatti**: "Haluan koodia? Regex-patternin? Selityksen?"
   - Lisää **esimerkki**: "Miltä oikea koodi näyttää? Anna esimerkki."
   - Näytä parannettu prompt kokonaisuudessaan.
   - Jos pääsy ChatGPT:hen: testaa parannettu prompt. Opiskelijat näkevät eron — vastaus on tarkempi, paremmin rakennettu, käyttökelpoisempi.

4. **Vertailu (4 min):**
   - Kuvakaappaus tai kirjoita molemmat vastaukset rinnakkain.
   - Kysy: "Mitä eroja näette? Kumpi on parempi? Miksi?"
   - Johtopäätös: "Parempi prompt = parempi vastaus. Ammattilaisesti investoit neljä minuuttia promptin kirjoittamiseen, säästät 20 minuuttia vastauksen korjaamisessa."

5. **Opiskelijoiden oma harjoitus (3 min):**
   - Anna hyvä esimerkki ja annetaan opiskelijoille kaksi minuuttia harjoitella omalla kehotuksella.
   - Kolme vapaehtoista: "Näytä minut sinun parantamasi prompt."

### Odotettu oppimistulos
- Opiskelijat näkevät konkreettisesti, mitä tekee hyvän promptin
- Opiskelijat näkevät eron huonon ja hyvän välillä
- Opiskelijat ovat valmiita tekemään omia harjoituksia

---

## Tehtävä 11.2: Iteratiivinen prompt-rakentaminen — Pienryhmät

### Tavoite
Oppia rakentamaan kontekstia kierros kierrokselta, näkemään, kuinka tekoäly parantuu jokaisen jatkopromptin myötä.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
- Jaa luokka pienryhmiin (2–3 henkilöä).
- Jokainen ryhmä saa yhden "tehtävän":
  1. Rakenna Python-validointifunktio
  2. Rakenna JavaScript-formaattointifunktio
  3. Rakenna SQL-kyselyiden optimointi

**Tehtävän vaiheet (30 min):**

1. **Ryhmien ja tehtävien jakaminen (2 min):** Jaa tehtävät tasaisesti.

2. **Kierros 1 — Perus-prompt (5 min):**
   - Jokainen ryhmä kirjoittaa perus­promptin: "Kirjoita [tehtävä]."
   - Jos pääsy tekoälyyn: testaa.
   - Tulokset: perus­vastaus, mutta epätarkka.

3. **Kierros 2 — Lisää spesifikaatiota (5 min):**
   - Jatkoprompti: "Lisää kommentit ja docstring. Tee siitä tuotanto­kelpoinensa."
   - Tulokset: parempi, mutta vielä puutteellinen.

4. **Kierros 3 — Lisää testejä (5 min):**
   - Jatkoprompti: "Nyt kirjoita vähintään kolme testejä. Sisällytä edge-caset."
   - Tulokset: kokonaisempi ratkaisu.

5. **Kierros 4 — Viimeinen hienosäätö (5 min):**
   - Jatkoprompti: "Paranna error-käsittelyä. Lisää yksityiskohtaiset virhesanomat."
   - Tulokset: ammattilaisesti laadultaan vastaus.

6. **Raportointi (8 min):**
   - Kukin ryhmä näyttää lopputuloksensa (tai kuvaa sen taululle).
   - Ryhmä selittää: "Näillä jatko­prompteilla paransi vastaus näin."
   - Koota yhteen: "Neljä kierrosta rakentivat kontekstia. Ammattilaisesti näin teemme parempia tuloksia."

### Odotettu oppimistulos
- Opiskelijat näkevät, että iteraatio toimii
- Opiskelijat ymmärtävät, kuinka konteksti rakentuu
- Opiskelijat ovat valmiita käyttämään tätä omissa projekteissaan

---

## Tehtävä 11.3: Prompt vs. konteksti — Luokkakeskustelu ja analyysit

### Tavoite
Auttaa opiskelijoita ymmärtämään ero promptin ja kontekstin välillä ammattilaisesti.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
- Valitse todellinen ammattilaisella tapaus. Esimerkiksi:
  - Asiakaspalvelun sähköpostin kirjoittaminen (konteksti: asiakas on arvokas, pettynyt, odottaa pahoittelua)
  - IT-tukitiketin kuvailu (konteksti: vaaditaan järjestelmät, virhekoodi, laitteet)
  - Koodin dokumentaatio (konteksti: keille dokumentaatio on tarkoitettu, millainen tekninen taso)

**Tehtävän vaiheet (20 min):**

1. **Johdanto (2 min):**
   - "Prompt ei ole konteksti. Prompt on 'mitä haluan tehdä nyt'. Konteksti on 'mikä on tausta-aine'."
   - Annetaan esimerkki: "Jos kysyn 'Kirjoita sähköposti', se on prompt. Mutta KUKA kirjoittaa? Kenelle? Mistä syystä? Nämä ovat konteksti."

2. **Ensimmäinen tapaus — Pelkkä prompt (5 min):**
   - Näytä prompt ilman kontekstia: "Kirjoita asiakaspalvelun sähköposti valitukseen."
   - Jos pääsy tekoälyyn: testaa. Näytä vastaus.
   - Kysy: "Mitä puuttuu? Onko sävy oikea? Onko se asiakkaalle sopiva?"

3. **Toinen tapaus — Sama prompt + konteksti (5 min):**
   - Lisää konteksti: "Asiakas oli asiakaalla 5 vuotta, otti yhteyttä kahdesti, odottaa pahoittelua."
   - Näytä parannettu prompt kontekstilla.
   - Testaa tekoälyllä. Näytä vastaus.
   - Kysy: "Mikä muuttui? Onko se parempi? Miksi konteksti muutti vastausta?"

4. **Vertailu ja johtopäätös (5 min):**
   - Rinnakkaista molemmat vastaukset.
   - Kysy luokalta: "Kumpi sähköposti voisi mennä asiakkaalle? Kumpi olisi väärä?"
   - Johtopäätös: "Ammattilaisesti konteksti on yhtä tärkeä kuin prompt. Joskus tärkeämpi."

5. **Opiskelijoiden oma tapaus (3 min):**
   - Kysy: "Missä ammattilaisessa tilanteessa konteksti voisi olla kriittinen?"
   - Esimerkkejä: lääkäri ja potientin taustat, tuomari ja tapauksen historia, ohjaaja ja oppilaan tausta.

### Odotettu oppimistulos
- Opiskelijat näkevät eron promptin ja kontekstin välillä
- Opiskelijat ymmärtävät, että konteksti määrää laadun
- Opiskelijat osaa ajatella ammattilaisesti: "Mikä konteksti tarvitaan tälle tehtävälle?"
