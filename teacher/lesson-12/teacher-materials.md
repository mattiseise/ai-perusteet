# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

Tämän lohkon jälkeen opiskelija:
1. Osaa pilkkoa monimutkaisen IT-ongelman pienempiin hallittaviin osiin.
2. Ymmärtää, kuinka rakentaa kontekstia iteratiivisesti jatkoprompteilla.
3. Osaa liittää olemassa olevaa aineistoa (koodi, teksti) tekoälylle analyysia varten.
4. Osaa testata ja dokumentoida jokaisen iteraation vaikutusta.
5. Osaa soveltaa näitä taitoja ammattilaisiin IT-projekteihin.

---

## Yleisiä väärinkäsityksiä

### 1. "Voin pyytää tekoälyä ratkaisemaan koko ongelman kerralla suurella promptilla."

**Todellisuus:** Suuret, monimutkaisia promtit johtavat usein epäselkeihin tai huonoihin vastauksiin. Ammattilaisesti pilkkoa isot ongelmat osiin ja ratkaise jokainen erikseen.

### 2. "Jos en osaa määritellä koko ongelmaa etukäteen, en voi pyytää tekoälyä."

**Todellisuus:** Ammattilaiset eivät tiedä kaikkea etukäteen. He rakentavat kontekstia iteratiivisesti — jokainen kierros opettaa mitä seuraavaksi pitää tehdä.

### 3. "Tekoäly voi ottaa koodin ja parantaa sen ilman apua."

**Todellisuus:** Tekoäly parantaa koodia paremmin, kun annat kontekstia: teknologia, tietokanta, vaatimukset, mitä parantaa. Konteksti ratkaisee laadun.

### 4. "Kun tekoäly antaa vastauksen, se on valmis käyttää."

**Todellisuus:** Ammattilaisesti testaa ja validoit jokaisen vastauksen. Tekoäly voi tehdä virheitä. Ammattilaisesti validointi on pakollista.

### 5. "Iteraatio tarkoittaa, että en osaa käyttää tekoälyä hyvin."

**Todellisuus:** Iteraatio on ammattilaisella normaalia. Ammattilaiset iteraavat kaikkea — siis se on merkki että käytät tekoälyä järkevästi.

---

## Opettajan fasilitointiohjeet

### Ennen lähiosaa

- Valitse monimutkainen IT-ongelma ja ratkaise se täysin etukäteen tekoälyn kanssa. Dokumentoi kaikki kierrokset, kuvakaappaukset, lopputulokset.
- Valmistele "huono" koodi-esimerkki, jota voit parantaa live-opetustapauksessa.
- Testaa prosessit etukäteen, niin osaat näyttää sujuvasti.
- Ota kuvakaappaukset jokaisesta kierroksesta, jotta voit näyttää rinnakkain.

### Lähiosassa (90 minuuttia)

- Aloita live-demolla monimutkaisen ongelman pilkkomisesta (Tehtävä 12.1). Opiskelijat näkevät koko prosessin.
- Liitä ohjattu harjoitus (Tehtävä 12.2), jossa opiskelijat tekevät itse omassa tempossaan.
- Pääty refactoring-harjoitukseen (Tehtävä 12.3), jossa näytät, kuinka olemassa oleva koodi paranetaan.
- Korostaa läpi koko ajan: "Ammattilaisesti iteraatio on pakollista. Et ratkaise kaikkea kerralla."

### Yleinen neuvo

- Monet opiskelijat pelkäävät, että heidän promptinsa ovat "huonoja" tai että iteraatio merkitsee epäonnistumista. Korjaa tämä: ammattilaiset iteraavat päivittäin.
- Näytä, että iteraatio säästää aikaa. "Ensimmäisen promptin kirjoittamiseen kuluva aika säästää moninkertaisesti myöhemmin."
- Kannusta testaamista ja dokumentointia. "Ammattilaisesti testaat jokaisen kierroksen. Et kulje sokeasti tekoälyn mukaan."
- Linkitä oikeisiin IT-projekteihin. "Tämä on se, mitä tehtävät päivittäin — rakentavat ratkaisuja kierros kierrokselta."

---

## Tarkistustehtävät (Checking-for-Understanding)

### 1. Pilkkaaminen
**"Sinulla on monimutkainen ongelma: rakenna tietokannan backup-järjestelmä. Kuinka pilkkoisit sen osiin?"**
- *Mitä etsit:* Opiskelija listaa loogisia osia: yhteys, varmuuskopiointi, virheenkäsittely, logitus, testit. Osaa perustella valintoja.

### 2. Kontekstin rakentaminen
**"Kirjoitit promptin. Sait vastauksen, joka oli lähellä oikeaa. Mitä kontekstia lisäisit seuraavassa promptissa?"**
- *Mitä etsit:* Opiskelija ymmärtää, mitä tietoa puuttuu vastauksen parantamiseksi. Osaa sanoa spesifisia asioita.

### 3. Lähdeaineiston liittäminen
**"Sinulla on Python-funktio, jonka haluat parantaa. Miten annat sen tekoälylle analysoitavaksi?"**
- *Mitä etsit:* Opiskelija tietää liittää koodin promptiin ja selittää, mitä halutaan parantaa.

### 4. Testaaminen ja validointi
**"Tekoäly antoi koodin. Mitä teet ennen kuin käytät sitä tuotannossa?"**
- *Mitä etsit:* Opiskelija osaa testata, validoida, dokumentoida. Osaa sanoa, mitä varmuusvaatimuksia on ammattilaisesti.

### 5. Ammattilaisesti soveltaminen
**"Kuvaile prosessi, jolla ratkaisit monimutkaisen ongelman tekoälyn kanssa. Mitä olivat kriittiset vaiheet?"**
- *Mitä etsit:* Opiskelija kuvaa pilkkaamisen, iteraation, testaamisen, dokumentoinnin. Näyttää ymmärtävän ammattilaisesta prosessia.

---

## Yleisiä vaikeuksia ja niihin vastaamisen strategiat

### Vaikeus 1: Opiskelijat yrittävät ratkaista koko ongelman yhdessä promptissa

**Mitä kuuluu:** "Kirjoitä koko käyttäjän kirjautumis-järjestelmä."

**Vastaus:** "Se on liian iso. Ammattilaisesti et pyydä sitä — pilkkoa se osiin. Ensin validointi, sitten tallennus, sitten email..."

**Strategia:** Näytä live-demo, jossa kysyt tekoälylle suuren ongelman. Näytä huono vastaus. Sitten pilkkoa ja näytä parempia vastauksia. Konkreettinen vertailu auttaa.

### Vaikeus 2: Opiskelijat eivät tiedä, mitä kontekstia antaa

**Mitä kuuluu:** "Miten minä tiedän, mitä kontekstia tarvitaan?"

**Vastaus:** "Et tiedä etukäteen. Saat vastauksen, katso sitä, ajattele: 'Puuttuu mitä?' ja pyydä seuraavassa promptissa. Iteraatio opettaa."

**Strategia:** Näytä iteratiivisesti, kuinka konteksti rakentuu. Ensimmäinen vastaus on huono, toinen parempi, kolmas vielä parempi. Opiskelijat näkevät prosessia.

### Vaikeus 3: Opiskelijat luulevat, että tekoälyn vastaus on automaattisesti oikea

**Mitä kuuluu:** "Tekoäly sanoi, että näin pitää tehdä, joten näin pitää tehdä."

**Vastaus:** "Ei. Ammattilaisesti testaat jokaisen vastauksen. Tekoäly voi tehdä virheitä. Sinun vastuulla on validoida."

**Strategia:** Näytä tapaus, jossa tekoäly antaa virheen — esim. väärä SQL-syntaksi, puuttuva error-käsittely. Osoita, että testaaminen on kriittistä.

### Vaikeus 4: Opiskelijat eivät dokumentoi prosessia

**Mitä kuuluu:** "Miksi minun täytyy kirjoittaa muistiin jokaisen kierroksen?"

**Vastaus:** "Ammattilaisesti dokumentointi on pakollista. Seuraavaan projektiin tarvitset muistioita. Opit siitä. Asiakas haluaa nähdä prosessin."

**Strategia:** Osoita, miten dokumentaatio auttaa. Näytä esimerkiksi kaksi ryhmää: toinen dokumentoi, toinen ei. Dokumentoiva ryhmä osaa selittää prosessiaan, toinen ei.

### Vaikeus 5: Opiskelijat alkavat turhauttua iteraatioista

**Mitä kuuluu:** "Kuinka monta kierrosta vielä? Haluan valmiin ratkaisun."

**Vastaus:** "Ammattilaisesti iteraatio on normaalia. Ratkaisut eivät synny taikuudella. Rakentamme niitä kierros kierrokselta. Tämä on ammattilaisesti realistista."

**Strategia:** Näytä todellinen ammattilaiselle projekti, jossa iteraatio kestää. Osoita, että monimutkaisia ongelmia ei ratkaista yhdessä kerrassa missään — tekoälyn kanssa tai ilman.

---

## Oppimisresurssit, joihin opettaja voi viitata

1. **Builder-materiaali (lesson-12.md):** Pilkkaaminen, kontekstin rakentaminen, case-tutkimus — kaikki oleellinen on siellä. Varmista tutustuminen.
2. **Live-demot:** Testaa prosessit etukäteen ja dokumentoi kuvakaappaukset. Näytä prosessia rinnakkain.
3. **Ammattilaiset esimerkit:** Etsi todellisia IT-projekteja, joissa iteraatio on ollut kriittinen. Näytä opiskelijoille.
4. **Opiskelijoiden omat projektit:** Kannusta heitä soveltamaan näitä strategioita omissa IT-projekteissaan.

---

## Lisämateriaalia opettajalle

### Esimerkkejä pilkkamisesta

**Ongelma:** Rakenna hakujärjestelmä tietokantaan.
**Osaa:**
1. Tietokannan yhteyden rakentaminen
2. Hakulogiikan implementointi
3. Tulosten muotoilu
4. Virheenkäsittely
5. Suorituskyky ja indeksointi
6. Testaaminen

### Kontekstin rakentamisen tarkistuslist

- Teknologia: Mitä käytetään? (Python, JavaScript, SQL)
- Tietokanta: Minkä tietokannan kanssa? Mikä on rakenne?
- Vaatimukset: Mitä täytyy tehdä? Mitä ei?
- Yleisö: Kenelle koodi on? (opiskelijat, ammattilaiset, asiakkaat)
- Rajat: Kuinka pian? Kuinka iso? Kuinka nopeasti?

### Testaamisen merkitys ammattilaisesti

- Unit-testit: Jokainen funktio testataan
- Integration-testit: Osät testataan yhdessä
- Edge case-testit: Erityiset tilanteet
- Performance-testit: Nopeus ja tehokkuus
- Security-testit: Turvallisuus

### Ammattilaiselle kuuluvat dokumentaatiot

- Prosessi-dokumentaatio: Miten ratkaisu rakennettiin
- Koodi-dokumentaatio: Kommentit, docstrings
- Käyttäjä-dokumentaatio: Miten käyttää
- Test-dokumentaatio: Mitä testattiin, miten
- Deployment-dokumentaatio: Miten ottaa käyttöön

---

## Esimerkki: Täydellinen iteratiivinen prosessi

**Tehtävä:** Rakenna API-päätepiste, joka hakee käyttäjiä tietokannasta.

**Kierros 1:**
```
Prompt: "Kirjoita Flask-sovellus, joka hakee käyttäjät tietokannasta."
Tulos: Perus-endpoint, ei virheenkäsittelyä, ei dokumentaatiota
```

**Kierros 2:**
```
Prompt: "Käytämme SQLite-tietokantaa. Taulu 'users' on rakennettu näin: [liitä rakenne]. Lisää virheenkäsittely ja dokumentaatio."
Tulos: Paremmin rakennetu, mutta vielä puutteellinen
```

**Kierros 3:**
```
Prompt: "Lisää kyselyparametrit: hae käyttäjä nimen perusteella, email-osoitteen perusteella, ID:n perusteella. Palauta JSON-muodossa."
Tulos: Monipuolisempi API
```

**Kierros 4:**
```
Prompt: "Lisää rate-limiting (max 100 pyynnöt per minuutti). Lisää logging. Lisää CORS-tuki."
Tulos: Tuotanto-kelpoin API
```

**Kierros 5:**
```
Prompt: "Kirjoita testit näille tapauksille: validi ID, virheellinen ID, SQL injection -yritys, rate limit ylitys."
Tulos: Täydellinen, testattu ratkaisu
```

Tämä on ammattilaisesti realistinen prosessi — viisi kierrosta, jokainen lisää arvoa, lopullinen tulos on käyttökelpoinen ja turvallinen.
