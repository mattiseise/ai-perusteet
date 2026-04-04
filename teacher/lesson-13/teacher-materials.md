# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

Tämän lohkon jälkeen opiskelija:
1. Ymmärtää, että AI:n vastauksen hyödyllisyys riippuu siitä, miten pyyntö on kirjoitettu.
2. Osaa valita sopivan formaatin (JSON, taulukko, lista, skripti) sen perusteella, miten tulosta käytetään.
3. Osaa kirjoittaa täsmällisen pyynnön, joka sisältää muodon, rakenteen ja rajoitukset.
4. Ymmärtää "hyötykäyttö"-käsitteen: vastaus on ammattilaiselle hyödyllinen vain, jos se on käyttökelpoinen sellaisenaan.

---

## Yleisiä väärinkäsityksiä

### 1. "AI:n antama vastaus on aina käyttökelpoinen, jos se näyttää järkevältä."

**Todellisuus:** Näkeminen ja käyttäminen ovat eri asioita. Teksti voi näyttää hyvältä, mutta jos se ei ole oikeassa muodossa, sitä ei voi integroida järjestelmiin eikä jakaa tehokkaasti.

### 2. "Formaatilla ei ole merkitystä — ne ovat kaikki tietoa."

**Todellisuus:** Formaatti määrää, miten tietoa voi käyttää. JSON voidaan parsea ohjelmalla. Vapaa teksti täytyy lukea ja jäsennellä käsin.

### 3. "Joka pyyntö tuottaa saman tuloksen riippumatta siitä, miten sen kirjoittaa."

**Todellisuus:** Tarkka, strukturoitu pyyntö tuottaa paljon paremman tuloksen kuin epämääräinen pyyntö. Ammattilaiset tietävät tämän ja kirjoittavat pyyntöjään vastaavasti.

### 4. "Hyötykäyttö on 'vain' käyttämisen kyse — sillä ei ole erityistä merkitystä."

**Todellisuus:** Hyötykäyttö on ammattilaisuuden ydin. Se tarkoittaa, että osaat ottaa mitä saat ja muuttaa sen työkaluksi — ei vain tiedoksi.

---

## Opettajan fasilitointiohjeet

### Ennen lähiosaa

- Testaa kaikki esimerkit AI:lla (ChatGPT, Copilot tai vastaava) ennen tunnille tulemista.
- Tallenna sekä huono että hyvä pyyntö ja vastaus — näytä ne live tai kuvakaappausten avulla.
- Varmista, että sinulla on pääsy joihinkin tyypillisiin formaatteihin: JSON-tiedosto, CSV, Markdown-taulukko, Shell-skripti.

### Lähiosassa (90 minuuttia)

- Aloita konkreettisilla esimerkeillä (Tehtävä 13.3), ei teorialla.
- Osoita selvästi, miten pyyntö muuttuu — näytä molemmat versiot rinnakkain.
- Keskitä huomio siihen, että hyvä pyyntö tuottaa käyttökelpoisen tuloksen, huono pyyntö ei.
- Liitä kaikki ammattilaiseen kontekstiin: "Yrityksessä sinun täytyy osata tämä."

### Yleinen neuvo

- Monet opiskelijat ajattelevat, että AI on maginen — "se antaa vain vastauksen". Selvitä, että AI on työkalu, jonka tehokkuus riippuu siitä, miten sille sanotaan.
- Näytä, että ammattilaiset kirjoittavat pyyntöjään hyvin huolellisesti — ei siksi, että ovat perfektionisteja, vaan koska he tietävät, että laatu riippuu pyynnöstä.
- Käytä termia "hyötykäyttö" usein — se on tämän oppitunnin ydin.

---

## Tarkistustehtävät (Checking-for-Understanding)

### 1. Formaatin valinta
**"Sinulla on lista 20 Linux-komennosta. Haluat jakaa sen tiimille GitHub Wikiin. Missä muodossa annat sen AI:lle?"**
- *Mitä etsit:* Opiskelija sanoo Markdown (koska se on helppo muuttaa HTML:ksi) tai selittää muuta valintaa järkevästi.

### 2. Pyyntö-kirjoitus
**"Kirjoita pyyntö, joka tuottaa JSON-tiedoston käyttäjien rooleista. Mitä sinun täytyy sanoa AI:lle?"**
- *Mitä etsit:* Opiskelija mainitsee JSON-muodon, kentät, rakenteen ja mahdolliset rajoitukset.

### 3. Hyötykäyttö
**"Mikä on ero 'hyödyllisen' ja 'mielenkiintoisen' vastauksen välillä?"**
- *Mitä etsit:* Opiskelija ymmärtää, että hyödyllinen vastaus on käytettävissä ammattilaisessa työssä sellaisenaan, mielenkiintoinen on vain informatiivinen.

### 4. Integraatio
**"Miksi skriptin tai koodin formaatti on tärkeä, kun pyynnöt sitä AI:lle?"**
- *Mitä etsit:* Opiskelija ymmärtää, että jos koodi ei ole oikeassa muodossa, sitä ei voi suoraan ajaa tai integroi järjestelmiin.

### 5. Rajoitukset
**"Miksi sinun täytyy kertoa AI:lle 'max 20 sanaa per kohta' tai 'kuusi rivi'?"**
- *Mitä etsit:* Opiskelija ymmärtää, että rajoitukset tekevät tuloksesta hallittavamman ja johdonmukaisemman.

---

## Yleisiä vaikeuksia ja niihin vastaamisen strategiat

### Vaikeus 1: Opiskelijat eivät näe eroa "pyyntö" ja "strukturoitu pyyntö" välillä

**Mitä kuuluu:** "Eikö 'Luoksi Python-skripti' ole tarpeeksi? Miksi täytyy sanoa 'Kirjoita Python-skripti, joka ottaa argumenteiksi tiedostonimen ja tulostaa sen sisällön – ei kahdeksaa linjaa pitemmällä koodilla'?"

**Vastaus:** "Ensimmäinen on osittain, toinen on täsmälliset. Toinen tuottaa paremman tuloksen, koska AI tietää, mitä haluat."

**Strategia:** Näytä kahden pyynnön vastaukset rinnakkain. Näytä, kuinka täsmällinen pyyntö tuottaa paremman tuloksen.

### Vaikeus 2: Opiskelijat ajattelevat, että kaikki formaatit ovat "samaa" tietoa

**Mitä kuuluu:** "Entä jos se on taulukko vai JSON — sisältö on sama!"

**Vastaus:** "Oikein, tieto on sama. Mutta käyttö on eri. Taulukko on ihmisen luettava. JSON voidaan parsea ohjelmalla. Skripti voidaan ajaa."

**Strategia:** Näytä käytännön esimerkki. Esimerkiksi: "Jos haluat tallentaa tämän tietokantaan, JSON on paljon helpompi kuin teksti."

### Vaikeus 3: Opiskelijat eivät osaa valita oikeaa formaattia

**Mitä kuuluu:** "Miten minä tiedän, pitäisikö se olla JSON vai CSV vai Markdown?"

**Vastaus:** "Kysy itseltäsi: Kuka tarvitsee tätä? Ja mitä he tekevät sillä? Jos he syöttävät taulukkoon, CSV. Jos he integroivat API:hin, JSON. Jos he lukevat dokumentaatiosta, Markdown."

**Strategia:** Yhdessä miettiminen. Kerro realistiset skenaariot. Auta opiskelijoita purkamaan "kuka, mitä, miten".

### Vaikeus 4: Opiskelijat kirjoittavat epämääräisiä pyyntöjä

**Mitä kuuluu:** "Tuota dokumentaatio käyttöohjeista."

**Vastaus:** "Liian epämääräinen. Minä kysyn: Missä muodossa? Markdown? Teksti? Kuvia? Kuinka pitkä per osio? Kuinka monta osaa? Kuka lukee tämän?"

**Strategia:** Harjoita pyyntöjen kirjoittamista yhdessä. Kysy kysymyksiä, jotka tekevät pyyntöä täsmällisemmäksi.

---

## Oppimisresurssit, joihin opettaja voi viitata

1. **Builder-materiaali (content/lessons/lesson-13.md):** Kaikki käsitteet ovat siellä. Vahvista erityisesti "hyötykäyttö"-osio.

2. **Konkreettiset esimerkit:** Etsi todellisia projekteja GitHubista, joissa on hyvä dokumentaatio, README-tiedostot tai JSON-konfiguraatiotiedostot. Näytä, miten ammattilaiset kirjoittavat pyyntöjä.

3. **API-dokumentaatio:** Hae esimerkki API:sta, joka käyttää JSON-muotoa. Näytä, miksi formaatti on täsmällinen — koska ohjelmat käyttävät sitä.

4. **Opiskelijoiden omat esimerkit:** Pyydä opiskelijoita tuomaan todellisia esimerkkejä. "Missä olet nähnyt taulukkoa? Mikä oli formaatti? Miksi se valittiin?"

