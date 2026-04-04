# Opettajavetoiset tehtävät

## Tehtävä 12.1: Monimutkaisen ongelman pilkkominen — Luokkasimulatio

### Tavoite
Näyttää opiskelijoille, kuinka ammattilaiset jakavat monimutkaisen ongelman osiin ja rakentavat ratkaisua iteratiivisesti.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu (ennen lähiosaa):**
- Valitse monimutkainen, mutta realistinen IT-ongelma (esim. käyttäjän kirjautumis-järjestelmä, hakualgoritmilla hausta, tietojen analysointi).
- Valmistele koko prosessi etukäteen ChatGPT:n kanssa, niin osaat näyttää konkreettisesti.
- Ota kuvakaappaukset jokaisesta kierroksesta.

**Tehtävän vaiheet (40 min):**

1. **Johdanto (3 min):**
   - "Tänään näytän, kuinka ammattilaiset ratkaisevat monimutkaisia ongelmia. He eivät koskaan kysy tekoälyä 'ratkaise kaikki tämä'. He pilkkovat sen osiin."

2. **Ongelman esittäminen (2 min):**
   - Näytä ongelmasi (esim. "Rakenna käyttäjän kirjautumis-järjestelmä").
   - Kysy: "Tämä on iso. Miten pilkkoisimme sen?"

3. **Pilkkoon vaiheet (5 min):**
   - Opiskelijat kertovat, mitkä osat ovat oleellisia.
   - Kirjoita taululle (esim. validointi, tallennus, email, virheenkäsittely, testit).
   - Kyse: "Mitkä ovat kriittiset osat?"

4. **Kierros 1 — Perus­prompt (8 min):**
   - Näytä projektorilla ensimmäinen prompt.
   - Aja se ChatGPT:ssä live (tai näytä kuvakaappaus).
   - Kysy: "Mitä saimme? Riittävä-kö tämä?"
   - Vastaus: "Ei vielä — me tarvitsemme lisää kontekstia."

5. **Kierros 2 — Konteksti (8 min):**
   - Näytä seuraava prompt, joka sisältää spesifisen tietokannan, teknologian, vaatimukset.
   - Testaa. Näytä, miten vastaus parantui.
   - Kysy: "Näettekö eron? Konteksti ratkaisee."

6. **Kierros 3 — Iteraatio (8 min):**
   - Näytä seuraava prompt, joka kertoo "nyt lisää error-käsittely, nyt lisää testit".
   - Testaa. Näytä, kuinka ratkaisu kypsyy.
   - Kyse: "Ammattilaisesti — kuinka monta kierrosta tarvittiin?"

7. **Yhteenveto (6 min):**
   - Näytä koko prosessi: kuusi kierrosta, jokainen parannustelu edellisestä.
   - Kirjoita taululle: "Ammattilaisesti: Pilkkoa → Kierros 1: Pohja → Kierrokset 2-6: Konteksti, iteraatio, parannus."
   - Korostaa: "Aika ensimmäisen promptin kirjoittamisessa säästää aikaa myöhemmin."

### Odotettu oppimistulos
- Opiskelijat näkevät konkreettisesti, kuinka prosessi toimii
- Opiskelijat ymmärtävät pilkkaamisen merkityksen
- Opiskelijat ovat valmiita tekemään omia harjoituksia

---

## Tehtävä 12.2: Ryhmien omien ongelmien ratkaisu — Ohjattu harjoitus

### Tavoite
Opiskelijat käyttävät pilkkaamisen ja iteraation strategiaa omassaan valitsemassaan IT-ongelmassa.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
- Valmistele 3-4 "ongelmaa", joista opiskelijat voivat valita:
  1. Hakualgoritmit (hakea tuotteita, käyttäjiä, artikkeleita)
  2. Tietojen validointi (sähköposti, puhelinnumero, osoite)
  3. Raportit ja analyysit (laskea keskiarvoja, trendit)
  4. Käyttäjähallinto (kirjautuminen, oikeudet, roollit)

**Tehtävän vaiheet (45 min):**

1. **Ryhmien muodostus ja ongelmien valinta (3 min):**
   - Jaa luokka ryhmiin (2–3 henkilöä).
   - Kukin ryhmä valitsee yhden ongelmista.

2. **Pilkkaaminen (5 min):**
   - Ryhmä piirtää tai kirjoittaa prosessin osaa.
   - Esimerkiksi: "Hakualgoritmille: (1) käyttöliittymä, (2) hakulogiikka, (3) tulostus, (4) testit."

3. **Kierros 1 — Perusrakenne (8 min):**
   - Ryhmä kirjoittaa yksinkertaisen promptin.
   - Jos pääsy tekoälyyn: testaa.
   - Dokumentoi: "Saimme perusversion, mutta epätarkka."

4. **Kierros 2 — Spesifikaatio (8 min):**
   - Ryhmä antaa kontekstia: teknologia, tietokanta, vaatimukset.
   - Testaa parantunut versio.
   - Dokumentoi: "Nyt se on tarkempi."

5. **Kierros 3 — Parannus (8 min):**
   - Ryhmä pyytää lisäominaisuuksia: virheenkäsittely, performance, testit.
   - Testaa lopullinen versio.
   - Dokumentoi: "Ammattilaisesti käyttökelpoinen."

6. **Raportointi (8 min):**
   - Kukin ryhmä näyttää prosessiaan (2 min per ryhmä).
   - "Pilkkasimme ongelman X osaan, rakensimme kontekstia Y kierroksella, saavuimme Z:iin."

### Odotettu oppimistulos
- Opiskelijat näkevät prosessin toimivan omissa ongelmissaan
- Opiskelijat dokumentoivat jokaisen kierroksen
- Opiskelijat ymmärtävät, että iteraatio on normaalia

---

## Tehtävä 12.3: Oikeasta koodista ammattilaiseksi — Refactoring­harjoitus

### Tavoite
Oppia parantamaan olemassa olevaa koodia tekoälyn kanssa, dokumentoimalla muutoksia kierros kierrokselta.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
- Valitse "huono" koodi esimerkiksi oppilaiden omista projekteista (tai valmis huono esimerkki).
- Koodissa tulisi olla parantamisen varaa: yksinkertainen logiikka, puuttuvat kommentit, huono error-käsittely, ei testejä.

**Tehtävän vaiheet (30 min):**

1. **Koodin esittely (3 min):**
   - Näytä koodi projektorilla.
   - Kyse: "Mitä näette? Mitä tässä voitaisiin parantaa?"
   - Kerää opiskelijoiden ideat taululle.

2. **Kierros 1 — Analyysi (7 min):**
   - Prompt: "Tässä on Python-funktio: [liitä koodi]. Mikä tässä on huonosti? Mitä pitäisi parantaa?"
   - Testaa tekoälyllä (tai näytä kuvakaappaus).
   - Dokumentoi: "Tekoäly löysi nämä ongelmat: ..."

3. **Kierros 2 — Perusparannukset (7 min):**
   - Prompt: "Paranna koodia lisäämällä kommentit, tekemällä siitä selkeämpi, lisäämällä dokumentaatio-stringit."
   - Näytä parannettu versio.
   - Dokumentoi: "Koodi on nyt helpompi lukea."

4. **Kierros 3 — Vahvistus ja virheenkäsittely (7 min):**
   - Prompt: "Lisää virheenkäsittely. Mitä tapahtuu, jos syöte on väärää? Lisää validointi."
   - Näytä versio, joka käsittelee virheet.
   - Dokumentoi: "Nyt koodi on tuotanto-kelpoin."

5. **Kierros 4 — Testit (3 min):**
   - Prompt: "Kirjoita testit tälle funktiolle. Sisällytä normal cases ja edge cases."
   - Näytä test-suite.
   - Dokumentoi: "Nyt voimme olla varmoja, että koodi toimii."

6. **Yhteenveto (3 min):**
   - Rinnakkaa alkuperäinen ja lopullinen koodi.
   - Kyse: "Mitä muuttui? Miksi ammattilaisesti tämä on tärkeää?"

### Odotettu oppimistulos
- Opiskelijat näkevät, että olemassa oleva koodi voidaan parantaa
- Opiskelijat ymmärtävät, että iteraatio tekee koodista paremmaksi
- Opiskelijat osaa ajatella refactoringista ammattilaisesti
