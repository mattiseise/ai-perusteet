# Opettajan materiaalit — Oppitunti 17

## Oppitunnin tarkoitus ja konteksti

Tämä oppitunti 17 on Tekoälyjen käyttö -osion arvioinnin **ensimmäinen osa** kahdesta. Se keskittyy **suunnitteluun ja rakentamisen aloittamiseen**. Oppitunti 18 on viimeistely ja esittely.

Oppitunnin tavoite: Opiskelijat suunnittelevat ja rakentavat uuden Custom GPT -botin, projektidokumenttibotin, joka kysyy käyttäjältä oikeita kysymyksiä projektista, kokoaa vastaukset järjestelmälliseksi projektisuunnitelmaksi ja toimii mentorin tavalla.

Opiskelijat osoittavat taidot botin tarkoituksen, roolin ja kysymyspatteriston suunnittelussa. He kirjoittavat system promptin, joka johtaa botin käyttäytymistä. He testaavat botin käytännöllisissä tilanteissa ja iteratiivisesti parantavat sitä testaustulosten perusteella. He dokumentoivat prosessin selkeästi.

---

## Osaamistavoitteet

Oppitunnin jälkeen opiskelijat osaavat määritellä botin tarkoituksen, roolin ja ohjeet. He osaavat suunnitella järjestelmällisen kysymysketjun projektisuunnittelua varten ja kirjoittaa selkeän system promptin, joka johtaa botin käyttäytymistä. He osaavat testata bottia käytännöllisissä tilanteissa ja dokumentoida prosessia niin, että joku toinen voi ymmärtää rakentamisen. He osaavat iteratiivisesti parantaa bottia testaustulosten perusteella.

## Arviointikriteerit — Tekoälyjen käyttö -osio, osa 1/2

Tämä oppitunti on arvioinnin ensimmäinen osa. Arviointia jatketaan oppitunnilla 18. Yhdessä oppitunnit 17 ja 18 muodostavat kokonaisarvioinnin.

### Arviointikohteet (40 pistettä yhteensä)

Oppitunnilla 17 arvioidaan noin 60 % arvioinnista.

---

**Pisteytys:**
- **Erinomainen (5):** 36–40 p
- **Hyvä (4):** 32–35 p
- **Tyydyttävä (3):** 28–31 p
- **Välttävä (2):** 20–27 p
- **Hylätty (1):** 0–19 p

## Arviointikohteet yksityiskohtaisesti (8 p per kohta)

### 1. Botin suunnittelu ja rooli (8 p)
**Mitä arvioidaan:**
- Onko botin tarkoitus selkeä (auttaa projektin suunnitteluun)?
- Onko rooli vastaava (projektin mentor/asiantuntija)?
- Ovatko ohjeet selkeät (miten kysyi, miten kuunteli, miten koota)?
- Ovatko rajaukset sopivat?
- Onko kysymyspatteristo (tehtävä 17.1) järjestelmällinen ja kattava?

**Erittäin hyvä esimerkki (8 p):**
- Tarkoitus: "Auttaa opiskelijaa luomaan selkeän projektisuunnitelman järjestelmällisten kysymysten avulla"
- Rooli: "Olet projektin mentor, jolla on 10 vuoden kokemus projektinjohdosta"
- Ohjeet: 4–5 konkreettista ohjetta siitä, miten botti kysyy
- Rajaukset: 2–3 selkeää rajausta
- Kysymyspatteristo: 15–20 hyvin järjestettyä kysymystä viiteen ryhmään

**Heikko esimerkki (1–2 p):**
- Tarkoitus: Epäselkeä tai "auta minua"
- Rooli: Puuttuu tai liian epämääräinen
- Ohjeet: "Kysy oikeita kysymyksiä"
- Rajaukset: Puuttuvat
- Kysymyspatteristo: Alle 10 kysymystä tai satunnaisia

### 2. System promptin kirjoitus (8 p)

**Mitä arvioidaan:**
- Sisältääkö prompti identiteetin, tarkoituksen, ohjeet ja rajaukset?
- Ovatko ohjeet selkeät kielimallille?
- Onko promptissa näkyvissä, miten botti käyttäytyy?
- Onko se 300–500 sanaa vai lyhyempi?

**Erittäin hyvä esimerkki (8 p):**
- System prompt sisältää kaikki neljä osaa selkeästi
- Jokainen osa on ammatillisesti kirjoitettu
- Ohjeet ovat konkreettisia (esim. "Kysy ensin lyhyt projektikuvaus, sitten käyttäjät, sitten tarkoitus...")
- Prompt on noin 300–500 sanaa
- Promptista näkyy, miten botti käyttäytyy käytännössä

**Heikko esimerkki (1–2 p):**
- Prompt on vain muutama lause
- Se ei sisällä rajauksia tai ohjeet ovat epäselviä
- Se näyttää olevan generoitu suoraan AI:stä ilman muokkausta
- Ohjeet ovat epämääräisiä ("ole auttavainen")

### 3. Testaus ja validointi (8 p)

**Mitä arvioidaan:**
- Kuinka monta testiskenaariotapaa on dokumentoitu?
- Ovatko testit järkevät ja kattavia (sekä onnistumiset että epäonnistumiset)?
- Ovatko testidokumentit selkeät (syöte, odotus, tulos)?

**Erittäin hyvä esimerkki (8 p):**
- Kaksi täyttä testiskenaariotapaa dokumentoitua
- Jokaisen testin perusteella analysoitu: mitä osia toimi, mitä ei
- Testidokumentti näyttää botin vastaukset selkeästi
- Analyysi näyttää, mitkä osat toimivat hyvin ja mitkä eivät
- Testit ovat erilaisia (yksinkertainen vs. monimutkainen projekti)

**Heikko esimerkki (1–2 p):**
- Vain 1 testi tai testit ovat samankaltaisia
- Testidokumentti puuttuu tai on epäselvä
- Ei analyysia

### 4. Iteraatio ja parantaminen (8 p)

**Mitä arvioidaan:**
- Löysikö opiskelija ongelmia testeissä?
- Muuttiko hän system promptia sen perusteella?
- Ovatko muutokset dokumentoituja?
- Näkyykö kriittinen ajattelu?

**Erittäin hyvä esimerkki (8 p):**
- Opiskelija löysi ongelman (esim. "Botti kysyi liian vähän käyttäjistä")
- Hän muutti system promptin (lisäsi 2 kysymystä "Kenelle?"-osioon)
- Hän testasi uudelleen samalla projektilla
- Hän dokumentoi muutokset ja näytti, että parantui

**Heikko esimerkki (1–2 p):**
- Ei havaittu ongelmia tai
- Ongelmia löydettiin, mutta ei muutettu
- Dokumentaatio puuttuu

### 5. Dokumentaatio ja prosessin selkeyttäminen (8 p)

**Mitä arvioidaan:**
- Onko kokonaisuutena dokumentoitu tehtävät 17.1–17.4?
- Näkyykö prosessi alusta loppuun?
- Ovatko kuvakaappaukset tai linkit botiin olemassa?
- Näkyykö opiskelijan ymmärrys aiheesta?

**Erittäin hyvä esimerkki (8 p):**
- 3–4 A4-sivua dokumentaatiota
- Tehtävät 17.1–17.4 selkeästi dokumentoituja
- Kuvakaappaukset botista ja testeistä
- Yhteenveto siitä, mitä opittiin
- Teksti on oman käden tekemää, ei kopioitua

**Heikko esimerkki (1–2 p):**
- Dokumentaatio on alle 1 sivu
- Tehtävät dokumentoituja epäselvästi
- Kuvakaappauksia puuttuu
- Ei yhteenvetoa

---

## Yleisiä väärinkäsityksiä ja korjausvinkkejä

### Väärinkäsitys 1: "System prompt ei ole niin tärkeä"

**Opiskelija ajattelee:** "Voin vain kirjoittaa botille, että kysy projektista, ja se tekee oikein."

**Opettajan vastaus:** "Kielimalli on kuin neuvonantaja, joka ei tiedä kontekstia. Se tarvitsee yksityiskohtaiset ohjeet: Kuka sinä olet? Mitä sinun pitää tehdä? Miten? Miksi? Jos et kerro nämä, botti tekee arvauksia ja menee väärin."

**Korjaus:** Näytä konkreettinen esimerkki. Live-demo samalla botilla kahdella eri promptilla. Näytä ero.

### Väärinkäsitys 2: "Yksi testi riittää"

**Opiskelija ajattelee:** "Testasin botin yhdellä projektikuvauksella, se toimi. Valmista!"

**Opettajan vastaus:** "Hyvä alku! Mutta entä jos toinen käyttäjä on erilainen? Entä jos kuvaus on epäselvä? Kaksi eri testiä, molemmat erilaiset, näyttää, että botti on robustimpi kuin yksi testi."

**Korjaus:** Kehoita tekemään kaksi täysin erilaista testiskenaariotapaa (esim. yksi yksinkertainen projekti, yksi monimutkainen).

### Väärinkäsitys 3: "Jos botti epäonnistuu, se on huono työ"

**Opiskelija ajattelee:** "Botti unohti käyttäjän vastauksen. Olen epäonnistunut. En tarvitse tehdä muuta."

**Opettajan vastaus:** "Et ollut epäonnistunut — olet tekemässä täsmälleen sitä, mitä pitäisi. Löysit ongelman! Nyt dokumentoi se. Muuta system promptia. Testaa uudelleen. Tämä on iteraatio — se osoittaa kriittistä ajattelua."

**Korjaus:** Kerro, että ongelmat ovat hyviä. Ne opettavat. Dokumentoidaan ja korjataan.

### Väärinkäsitys 4: "Dokumentaatio on turhaa"

**Opiskelija ajattelee:** "Botti toimii, miksi pitäisi kirjoittaa raporttia?"

**Opettajan vastaus:** "Dokumentaatio näyttää ajattelusi. Se näyttää, mitä testit osoittivat, mitä muutit ja miksi. Ilman dokumentaatiota opettaja näkee vain lopputuloksen, ei prosessia. Prosessi on se, josta saa pisteitä."

**Korjaus:** Näytä, mitä dokumentaatiosta etsitään: tehtävät 17.1–17.4, testit, muutokset, analyysit.

---

## Fasilitointiohjeet

### Tuntien rakentaminen

1. **Johdanto (5 min):** Yhdistä opiskelijoiden omaan kokemukseen. "Entä jos aloitatte projektin ilman suunnitelmaa?"

2. **Live-demo (15 min):** Näytä toimiva botti ja kuinka se toimii. Tämä konkretisoi, mihin pyritään.

3. **Ryhmätyö (20 min):** Ryhmät ideoivat kysymykset. Tämä aktivoi opiskelijoita ja osoittaa, ettei ole vain yksi oikea vastaus.

4. **Yhteinen analyysi (10 min):** Nämä ovat kriteerit, joilla arvioidaan. Opiskelijat näkevät, mitä odotetaan.

5. **Opiskelijat aloittavat (30+ min):** Opiskelijat alkavat tehtävät 17.1–17.4. Kierrä luokassa, auta jumiin jääneita.

### Yleisiä apukysymyksiä, kun opiskelija on jumissa

**"En osaa kirjoittaa hyvää system promptia"**
- "Mitä haluamasi botin pitäisi tehdä? (Kysy oikeita kysymyksiä projektista)"
- "Mikä botti on? (Ekspertti, mentori, assistentti?)"
- "Mitä se EI saa tehdä?"
- Nämä kolme asiaa ovat runko. Kirjoita nämä ensin."

**"Testaus on vaikeaa"**
- "Kuvittele kaksi erilaista ihmistä. Ensimmäinen sanoo [yksinkertainen projekti]. Toinen sanoo [monimutkainen projekti]. Kun botti vastaa, kirjoita ylös: Mitä se kysyi? Oliko järkevää?"

**"Botti ei toiminut"**
- "Hyvä! Dokumentoi mikä meni pieleen. Mitä muuttaisit system promptiin? Testaa uudelleen."

**"Minulla on 50 kysymystä"**
- "Voi olla liian monta. Muista: hyvä botti kysyy tarpeeksi, mutta ei liikaa. Valitse 15–20 tärkeintä. Loput voidaan kysyä myöhemmin."

## Eriyttäminen

### Haastava versio opiskelijoille, jotka haluavat lisää

Pyydä opiskelijaa lisäämään kysymyksiä: Entä riskit? Entä kilpailijat? Entä roolien jaot tiimissä? He voivat kehittää monimutkaisen suunnittelun, jossa botti tekee ensin lyhyen suunnitelman, sitten syvää, sitten erittäin syvää. He voivat lisätä kielten tuen ja tehdä botista monikielisen, joka osaa vastata projektikysymyksiin usealla kielellä.

### Yksinkertaistettu versio opiskelijoille, jotka tarvitsevat apua

Jätä tehtävä 17.1 helpommaksi antamalla valmiit 15 kysymystä, jolloin opiskelijoiden pitää vain valita parhaat. Jätä tehtävä 17.2 helpommaksi antamalla puolivalmis system prompt, jonka opiskelija täydentää. Jätä testaus (17.3) helpommaksi antamalla ennalta kirjoitetut testiskenaarioita, jotka opiskelija vain ajaa. Voit jättää vaatimatta tehtävää 17.4 — pelkästään 17.1–17.3 riittää arviointiin.

## Aika ja aikataulutus

Johdanto ja demo kestää 20 minuuttia oppitunnilla. Ryhmätyö ja analyysi kestää 30 minuuttia oppitunnilla. Opiskelijat työskentelevät tehtävistä 17.1–17.4 noin 40+ minuuttia oppitunnilla ja kotona. Yhteensä noin 90 minuuttia oppitunti ja kotityö.

Oppitunnilla 17 fokus on johdantoon ja demoon. Opiskelijat voivat aloittaa tehtävät, mutta suurin työ tapahtuu luokan jälkeen ja valmistaudutaan oppitunnille 18.

## Yhteys muihin oppitunteihin ja viimeistelyoppituntiin

Tämä oppitunti on silta. Oppitunneilla 14–15 opiskelijat oppivat botin suunnittelusta ja testaamisesta. Oppitunnilla 17 he rakentavat botin, joka perustuu näihin taitoihin.

Seuraavalla kerralla (oppitunti 18) he viimeisttelevät, parantavat ja esittelevät botin. Yhdessä suunnitteluoppitunnilla ja viimeistelyoppitunnilla ovat Tekoälyjen käyttö -osion arvioinnin ensimmäinen osa.

Tulevilla oppitunneilla (oppitunnit 19–27) Agentit-osio rakentaa tällä botilla. Projektidokumenttibotti on agenteille pohja — agentti on botti, joka tekee enemmän.
