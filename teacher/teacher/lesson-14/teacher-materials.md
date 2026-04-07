# Opettajan materiaalit

## Oppitunnin tavoitteet

Tämän tunnin jälkeen opiskelija:
1. Ymmärtää, että hyvin suunniteltu botti rakentuu **neljästä rakennuspaliikasta**: tarkoitus, rooli, ohjeet ja rajaukset.
2. Osaa kirjoittaa **järjestelmäpromptin**, joka ohjaa botin käyttäytymistä johdonmukaisesti.
3. Ymmärtää, että **ammattilaisuus** ja **persoonallisuus** eivät ole sama asia — ja miksi ammattilaisuus tulee aina ensin.
4. Osaa kirjoittaa **esimerkki-interaktioita**, jotka testaavat, toimiiko ohjeistus todellisuudessa.
5. Ymmärtää, että "oma botti" ei ole vain nimetty ChatGPT, vaan **räätälöity AI-järjestelmä** selkeällä tarkoituksella.

---

## Yleisiä väärinkäsityksiä

### 1. "Oma botti on vain ChatGPT, jolle annetaan nimi ja muutama ohjeistus."

**Todellisuus:** Hyvin suunniteltu botti on paljon enemmän. Sillä on selkeä tarkoitus, syvä osaaminen, johdonmukainen käyttäytyminen ja tietyt rajaukset. Se on **räätälöity järjestelmä**, ei pelkkä alias.

### 2. "Rooli on persoonallisuus — bottia pitää tehdä hauskaksi."

**Todellisuus:** Rooli ja persoonallisuus eivät ole sama. **Ammattilaisuus** (kompetenssi, tarkkuus, tietämys) on pakollista. **Persoonallisuus** (tapa välittää sitä) on valinnainen. Ammattilaismainen voi olla ystävällinen tai suora — molemmat voivat olla ammattilaismaisia. Mutta epäpätevä ei ole koskaan ammattilaismainen.

### 3. "Järjestelmäprompti on pitkä tekstisarja — en halua kirjoittaa sitä."

**Todellisuus:** Järjestelmäprompti on botin **sydän**. Se määrittää kaiken. Ilman sitä botti on sekava. Kirjoittamisen vaiva on kannattava — se on kuin arkitehtuuri ennen rakentamista.

### 4. "Rajaukset ovat negatiivisia — miksi ottaa huomioon, mitä botti EI saa tehdä?"

**Todellisuus:** Rajaukset ovat **turvallisuusmekanismi**. Ne suojaavat käyttäjää väärältä tiedolta ja bottia sopimattomista tilanteista. Hyvät rajaukset tekevät botista **vastuullisen**, ei rajoittuvan.

### 5. "Esimerkki-interaktiot ovat turhaa — botti toimii tai ei toimi."

**Todellisuus:** Esimerkki-interaktiot ovat **testausväline**. Ne osoittavat, toimiiko ohjeistus todellisuudessa vai tarvitseeko sitä korjausta. Ilman niitä et tiedä, mitä botti tekee ennen kuin se on oikeassa käytössä.

---

## Opettajan fasilitointiohjeet

### Ennen lähiosaa

- Valitse yksi konkreettinen botti (esim. Python-tutori, IT-helpdesk, asiakaspalvelu)
- Testaa neljä rakennuspalikkaa etukäteen
- Kirjoita malli-järjestelmäprompti (3–4 kappaletta)
- Valmista 2–3 esimerkki-interaktiota, joissa näytetään:
  - Normaali tilanne (botti toimii normaalisti)
  - Vaikea tilanne (botti kieltäytyy tai ohjaa)
  - Epäselvä tilanne (botti pyytää tarkennusta)

### Lähiosassa (90 minuuttia)

1. **Tehtävä 14.1** (20 min): Näytä kolme rakennuspalikkaa live-esittelyllä
2. **Tehtävä 14.2** (25 min): Ryhmät kirjoittavat omien bottienensa järjestelmäpromptin
3. **Tehtävä 14.3** (15 min): Näytä esimerkki-interaktiot ja niiden merkitys
4. **Vapaa harjoittelu** (25 min): Opiskelijat työskentelevät omien bottienaan

Kotitehtävä: Täydentää botin suunnittelua ja järjestelmäpromptin seuraavaan tunnille.

### Yleinen neuvo

- **Tarkoituksen merkitys:** Opiskelijat sekoittavat usein "olla hyödyllinen" ja "auttaa opiskelijoita ymmärtämään X:ää interaktiivisten esimerkkien kautta". Näytä eroa. "Hyödyllinen" on liian epämääräinen. "Auttaa ymmärtämään X:ää" on mitattavissa.
- **Rooli antaa luottamusta:** Kun sanot "botti on kokenut tutori", käyttäjä luottaa enemmän. Roolilla on voimaa. Se ei ole persoonallisuus, se on **uskottavuus**.
- **Ohjeet tekevät botista johdonmukaisen:** Ilman ohjeita botti vastaisi satunnaisesti. Ohjeet varmistavat, että se käyttäytyy samalla tavalla joka kerta.
- **Rajaukset ovat rakkaus:** Kun botti tietää, mitä se ei saa tehdä, se on turvallinen ja vastuullinen. "En osaa" on parempi kuin "minulla ei ole aavistustakaan".

---

## Tarkistustehtävät (oppimisen varmistaminen)

### 1. Botin tarkoitus
**"Mikä on hyvä botin tarkoitus? Miksi 'olla hyödyllinen' ei ole hyvä vastaus?"**
- *Mitä etsit:* Opiskelija ymmärtää, että hyvä tarkoitus on **konkreettinen** ja **mitattavissa**. "Auttaa opiskelijoita ymmärtämään Python-loopeita" on parempi kuin "olla hyödyllinen".

### 2. Rooli ja persoonallisuus
**"Mitä on rooli ja mitä on persoonallisuus? Ovatko ne sama asia?"**
- *Mitä etsit:* Opiskelija ymmärtää, että **rooli** on identiteetti (kokenut tutori), **persoonallisuus** on tapa (ystävällinen, suora). Ammattilaisuus ensin, persoonallisuus toiseksi.

### 3. Järjestelmäpromptin neljä osaa
**"Mitä järjestelmäpromptin tulee sisältää?"**
- *Mitä etsit:* Opiskelija osaa nimetä: identiteetti, tarkoitus, ohjeet, rajaukset.

### 4. Rajaukset käytännössä
**"Miksi rajaukset ovat tärkeitä? Anna esimerkki."**
- *Mitä etsit:* Opiskelija ymmärtää, että rajaukset suojaavat käyttäjää ja bottia. Esim: "IT-helpdesk-botti ei vastaa sijoituskysymyksiin, koska se vaatii rahoitustaustaa."

### 5. Esimerkki-interaktiot
**"Mitä esimerkki-interaktiot näyttävät?"**
- *Mitä etsit:* Opiskelija ymmärtää, että ne testaavat, toimiiko ohjeistus todellisuudessa. Ne osoittavat, miten botti käyttäytyy eri tilanteissa.

---

## Yleisiä vaikeuksia ja niihin vastaamisen strategiat

### Vaikeus 1: Opiskelijat kirjoittavat liian epämääräisen tarkoituksen

**Mitä kuuluu:** "Botin tarkoitus on auttaa ihmisiä."

**Vastaus:** "Kuka? Mitä asiassa? Miten mittaat onnistumisen?"

**Strategia:** Pyydä, että he kirjoittavat uudelleen. Tarkoitus = **kuka** + **mitä** + **miten**. "Auttaa opiskelijoita ymmärtämään Python-loopeita interaktiivisten esimerkkien kautta."

### Vaikeus 2: Opiskelijat miettivät, että rooli on liiallista

**Mitä kuuluu:** "Miksi botti tarvitsee roolin? Se on vain AI."

**Vastaus:** "Rooli antaa botille **uskottavuuden**. Kun sanot, että botti on kokenut tutori, käyttäjä luottaa enemmän. Se on testattu psykologinen vaikutus."

**Strategia:** Näytä kaksi vastusta: ilman roolia ja roolin kanssa. Kysy: "Kumpaa luottaisit enemmän?"

### Vaikeus 3: Opiskelijat sekoittavat ohjeet ja rajaukset

**Mitä kuuluu:** "Eikö rajaukset ole samaa kuin ohjeet?"

**Vastaus:** "Ei. Ohjeet kertovat mitä botti tekee. Rajaukset kertovat mitä se ei tee."

**Strategia:** Anna esimerkki:
- Ohje: "Aloita aina peruskäsitteestä"
- Rajaus: "En kirjoita valmiita projekteja"

### Vaikeus 4: Opiskelijat eivät näe esimerkki-interaktioiden arvoa

**Mitä kuuluu:** "Miksi kirjoittaa näytelmiä? Botti vain vastaa tai ei vastaa."

**Vastaus:** "Näet silloin, toimiiko ohjeistus. Muuten et tiedä ennen kuin botti on oikeassa käytössä — ja saattaa olla liian myöhäistä."

**Strategia:** Näytä väärä esimerkki-interaktio — näytä, mitä botti tekee jos ohjeistus on huono. "Näetkö nyt, miksi tämä on tärkeää?"

### Vaikeus 5: Opiskelijat pelkäävät, että järjestelmäprompti on liian pitkä

**Mitä kuuluu:** "En halua kirjoittaa neljää kappaletta tekstiä."

**Vastaus:** "Tämä on kuin arkitehtuuri ennen rakentamista. Vaiva kannattaa — hyvin suunniteltu botti on yhtä arvokas kuin huolimattomasti suunniteltu."

**Strategia:** Näytä lyhyt, huono järjestelmäprompti vs. yksityiskohtainen. Pyydä vertaamaan tuloksia. Näytä ero.

---

## Oppimisresurssit

1. **Opiskelijan itseopiskelumateriaali (self-study.md):** Kaikki perusideat ovat siellä.

2. **Esimerkit omista botteista:**
   - Analysoi hyviä Custom GPT:jä
   - Huomaa, millä tavalla ne on konfiguroitu
   - Reverse-engineer: mitä ne tekevät?

3. **Järjestelmäpromptin esimerkit:**
   - Python-tutori-botti
   - IT-helpdesk-botti
   - Asiakaspalvelu-botti

4. **Testaus ja iteraatio:**
   - Näytä, miten botti muuttuu kun ohjeistusta muokataan
   - Live-testi: muuta rohkeasti, näytä vaikutus

5. **Opiskelijoiden omat botit:** Pyydä opiskelijoita esittelemään omansa seuraavalla tunnilla.

---

## Oppitunnin rakenne ja merkitys

Tämä oppitunti on silta kohti omien räätälöityjen bottien rakentamista. Opiskelijat näkevät, että:
- Hyvä botti ei ole sattuma — se on harkittu suunnittelu
- Järjestelmäprompti on botin sydän
- Ammattilaisuus vaatii yksityiskohtia

Seuraavassa oppitunnissa opiskelijat rakentavat ja testaavat omia bottejaan näiden periaatteiden pohjalta.

---

## Eriyttäminen ja tuen tarpeet

### Jos opiskelija on jumissa tarkoituksen kirjoittamisessa
Ohjaa hänet ajattelemaan: "Kuka käyttää bottia? Mitä varten? Miten mittaat onnistumisen?"

### Jos opiskelija ei näe roolin arvoa
Näytä konkreettisesti kahden botin vertailu: yksi ilman roolia ("Botti"), yksi roolilla ("Kokenut Python-tutori, 10 vuotta"). Kysy: "Kumpi tuntuu ammattilaisemmalta?"

### Jos opiskelija ei osaa kirjoittaa ohjeita
Anna malli-ohjeet ja pyydä häntä mukauttamaan ne omalle bottille. Ohjeet ovat usein yksinkertaisia, konkreettisia lauseita.

### Jos opiskelija ei näe rajausten merkitystä
Selitä: "Rajaukset suojaavat bottia tekemästä vaarallisia tai vääriä asioita. Hyvin rajattu botti on vastuullinen botti."
