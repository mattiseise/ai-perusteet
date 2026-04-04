# Opettajavetoiset tehtävät

## Tehtävä 13.3: Näytä ero — huono vs. hyvä pyyntö

### Tavoite

Osoittaa konkreettisesti, miten erittäin strukturoitu pyyntö muuttaa AI:n outputin laadun ja hyödyllisyyden.

### Opettajan ohjeet ja fasilitaatio

Tämä tehtävä tehdään opettajan johdolla koko luokalle.

**Valmistelu (ennen lähiosaa):**
- Valmista kolme eri tehtävää: asennusohje, tarkistuslista, vertailu.
- Testaa kutakin tehtävää AI:lla sekä huonolla että hyvällä pynnöllä.
- Kopioitu vastaukset tai ota kuvakaappaukset.

**Tehtävän vaiheet (25 min):**

1. **Johdanto (2 min):** "Pyyntöjen laatu vaikuttaa vastauksen hyödyllisyyteen. Katsotaan, mitä eroa on."

2. **Esimerkki 1: Asennusohje (8 min)**
   - Näytä huono pyyntö: "Kuinka asennetaan Docker?"
   - Näytä AI:n huono vastaus: tekstissä 47 sanatonta vaihetta, sekaisin.
   - Kysy luokalta: "Voiko joku seurata tätä suoraan?"
   - Näytä hyvä pyyntö: "Tuota numeroitu vaiheistus Dockerin asennuksesta Ubuntu 22.04:lle. Jokainen vaihe on yksi rivi komentoa plus yksi rivi selitystä. Sisällytä 6–8 vaihetta."
   - Näytä AI:n hyvä vastaus: selkeät numeroidut vaiheet.
   - Kysy: "Kuinka paljon helpompi tämä on seurata?"

3. **Esimerkki 2: Tarkistuslista (8 min)**
   - Näytä huono pyyntö: "Luoksi code review checklist."
   - Näytä vastauksesta pätkä: pörö teksti ilman rakennetta.
   - Näytä hyvä pyyntö: "Tuota Markdown-muotoinen tarkistuslista code reviewille. Rakenne: kolme osiota (Koodi, Testit, Dokumentaatio), jokaisessa 3 tarkistusehdot muodossa '☐ [vaatimus]'."
   - Näytä strukturoitu vastaus: selkeä lista, jonka voi kopioida suoraan GitHub Wikiin.
   - Kysy: "Kuka voisi käyttää tätä? Kuinka paljon nopeammin?"

4. **Esimerkki 3: Vertailu (6 min)**
   - Näytä huono pyyntö: "Vertaa React ja Vue"
   - Näytä vastauksesta pätkä: pitkät kappaleet, ei rakennetta.
   - Näytä hyvä pyyntö: "Tuota Markdown-taulukko, jossa on sarakkeet: Ominaisuus | React | Vue. Sisällytä nämä rivit: Syntaksi, Suorituskyky, Oppimiskäyrä, Yhteisö, Kirjastot. Pidä jokainen vastaus alle 15 sanaan."
   - Näytä taulukko: voit nähdä eron yhdellä silmäyksellä.
   - Kysy: "Miksi taulukko on parempi kuin teksti vertailussa?"

5. **Yhteenveto (1 min):** Kolme tärkeää asiaa:
   - Kirjoita **täsmällinen** pyyntö: formaatti, rakenne, rajoitukset.
   - Selkeä pyyntö tuottaa käyttökelpoisen outputin.
   - Ammattilaiset ovat tyypillisesti hyvin tarkkoja pyyntöissään.

### Odotettu oppimistulos

- Opiskelijat näkevät, että pyyntöjen laadulla on merkitystä
- Opiskelijat ymmärtävät, että "ammattilaiset" eivät vain käytä AI:ta — he sanovat sille, mitä haluavat
- Opiskelijat ovat valmiita harjoittelemaan omissa tehtävissään

---

## Tehtävä 13.4: Pienryhmä-harjoitus: Rakenteiden suunnittelu

### Tavoite

Opiskelija oppii ajattelemaan, mitä rakennetta hän tarvitsee ennen pyyntöä.

### Opettajan ohjeet ja fasilitaatio

Tämä tehtävä tehdään pienryhmissä (2–3 henkilöä), joita opettaja valvoo.

**Valmistelu:**
- Jaa ryhmille neljä eri skenaariota
- Varmista, että opiskelijoilla on pääsy AI:hin

**Tehtävän vaiheet (20 min):**

1. **Skenaarion jakelu (1 min):** Jokainen ryhmä saa yhden skenaarion.

2. **Suunnittelu: Mitä rakennetta tarvitset? (8 min)** Ryhmä miettii ja kirjoittaa:
   - Mikä on tehtävä?
   - Kuka käyttää tätä tulosta?
   - Missä muodossa data olisi hyödyllisin?
   - Mitä kenttiä tai osioita?
   - Mitä rajoituksia (määrä, pituus, rakenne)?

3. **Kirjoita pyyntö (8 min):** Ryhmä kirjoittaa **täsmällisen** pyynnön AI:lle.

4. **Raportointi (3 min):** Ryhmä sanoo:
   - Tehtävä ja valittu formaatti
   - Yksi tärkeä vaatimus tai rajoitus
   - Yksi sana siitä, miksi tämä formaatti valittiin

### Skenaariot

**Skenaario A:** Tiimin piti dokumentoida "hyvä commit-viesti" -käytännöt. Jokainen tiimiläinen tekee commiteja eri tavalla. Sinun täytyy luoda dokumentti, jonka kaikki voisivat noudattaa.

**Skenaario B:** Olet IT-tukihenkilö ja sinulla on 15 yleistä kysymystä, joita asiakkaat kysyvät joka päivä. Haluat luoda dokumentin, jonka voit jakaa nopeasti.

**Skenaario C:** Sinulla on projekti, ja haluat tallentaa jokaisen tiimin jäsenen yhteystiedot ja roolit järjestelmään, joka käyttää JSON-muotoa.

**Skenaario D:** Sinulla on lista viiden IT-alan ammattilaisen sertifikaateista (hinta, pituus, vaikeusaste, arvo markkinoilla). Haluat vertailla niitä helposti.

### Odotettu oppimistulos

- Opiskelijat näkevät, että formaatin valinta on strateginen, ei sattumanvarainen
- Opiskelijat osaa ajatella "kuka tarvitsee tätä ja missä muodossa"
- Opiskelijat tekevät parempia pyyntöjä seuraavissa harjoituksissa

