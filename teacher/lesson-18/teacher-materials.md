# Opettajan materiaalit — Oppitunti 18: projektidokumenttibotin viimeistely ja esittely

## Oppitunnin tarkoitus ja konteksti

Oppitunti 18 on **Tekoälyjen käyttö** -osion arvioinnin toinen osa. Oppitunnilla 17 opiskelijat suunnittelivat ja rakensivat projektidokumenttibotin ensimmäisen version. Tällä oppitunnilla he viimeistelevät botin, testaavat sen perusteellisesti, dokumentoivat korjaukset ja esittelevät työnsä muille.

Oppitunnin ydin on, että opiskelija osoittaa osaavansa käyttää tekoälyä **vastuullisesti**, **itsenäisesti** ja **dokumentoidusti**. Arvioinnissa ei katsota vain sitä, onko botti olemassa, vaan sitä, miten opiskelija testaa, parantaa, esittelee ja arvioi omaa työtään.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että valmis botti ei ole arvioinnin ainoa kohde. Arvioinnissa näkyvät myös testaus, iterointi, esittely, vertaispalaute ja reflektio. Hyvä opiskelija osaa näyttää, miten botti toimii, mitä hän oppi ja miten botti voisi kehittyä agentiksi.

---

## Oppimisen tavoitteet

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, että botti pitää testata **positiivisilla testeillä**, **negatiivisilla testeillä** ja **reunatapauksilla**.
- Opiskelija ymmärtää, että testauksessa löytyvät virheet ovat osa kehitysprosessia.
- Opiskelija ymmärtää, että esittely vaatii valmistelua: botin tarkoitus, käyttötapa ja hyöty pitää pystyä selittämään muille.
- Opiskelija ymmärtää, että reflektio osoittaa omaa oppimista ja ajattelun kehittymistä.

### Soveltaa ja analysoida

- Opiskelija testaa omaa bottiaan monipuolisesti ja dokumentoi testien tulokset.
- Opiskelija tunnistaa testien perusteella botin vahvuuksia, puutteita ja korjaustarpeita.
- Opiskelija valmistaa botin esittelyn kirjoittamalla selkeän kuvauksen ja käsikirjoittamalla live-demon.
- Opiskelija antaa ja vastaanottaa rakentavaa vertaispalautetta.

### Luoda ja arvioida

- Opiskelija viimeistelee botin testitulosten ja palautteen perusteella.
- Opiskelija esittelee botin selkeästi ja vakuuttavasti.
- Opiskelija pohtii omaa oppimistaan ja tunnistaa, mitä tekisi seuraavalla kerralla paremmin.
- Opiskelija osaa selittää, miten botti voisi kehittyä kohti **agenttia**.

---

## Arviointikriteerit — oppitunnit 17 ja 18 yhteensä

Oppitunnit 17 ja 18 muodostavat yhdessä **Tekoälyjen käyttö** -osion arviointikokonaisuuden. Oppitunnilla 18 arviointi painottuu viimeistelyyn, testaukseen, esittelyyn ja reflektioon.

Kokonaispistemäärä on **20 pistettä**. Jokainen arviointikriteeri on enintään **4 pistettä**.

| Kriteeri | Maksimipisteet | Mitä arvioidaan? |
| --- | --- | --- |
| **1. Botin suunnittelu ja tarkoitus** | 4 p | Onko botin tarkoitus selkeä, kysymykset relevantteja ja botti suunniteltu oikeaan käyttötarkoitukseen? |
| **2. System prompt ja ohjeet** | 4 p | Onko system prompt selkeä, johdonmukainen ja sisältääkö se roolin, ohjeet ja rajaukset? |
| **3. Testaus ja iterointi** | 4 p | Onko bottia testattu monipuolisesti, onko virheet dokumentoitu ja onko korjauksia tehty? |
| **4. Esittely ja viestintä** | 4 p | Selittääkö opiskelija bottinsa selkeästi ja onnistuuko live-demo ymmärrettävästi? |
| **5. Reflektio ja oppiminen** | 4 p | Pohtiiko opiskelija omaa oppimistaan ja ymmärtääkö hän, miten botti voisi kehittyä agentiksi? |

---

## Arviointikriteerit yksityiskohtaisesti

### 1. Botin suunnittelu ja tarkoitus — 4 pistettä

**Mitä arvioidaan?**

- Onko botin tarkoitus selkeä: mitä botti tekee ja kenelle?
- Onko system prompt kirjoitettu johdonmukaisesti suhteessa botin tarkoitukseen?
- Ovatko kysymykset relevantteja ja rakentavatko ne realistisen kuvan projektista?
- Vastaako botti siihen tehtävään, johon se on suunniteltu?

| Taso | Kuvaus |
| --- | --- |
| **Erinomainen, 4 p** | Botin tarkoitus on erittäin selkeä. Kysymykset ovat olennaisia ja hyvin suunniteltuja. Botti vastaa johdonmukaisesti siihen, mihin se on rakennettu. |
| **Hyvä, 3 p** | Tarkoitus ja perusidea ovat selkeät. Joissakin kysymyksissä tai rakenteessa on pieniä puutteita. |
| **Tyydyttävä, 2 p** | Botti toimii perusidealtaan, mutta tarkoitus, kysymykset tai projektisuunnittelun logiikka jäävät osittain epäselviksi. |
| **Välttävä, 1 p** | Botin tarkoitus on epäselvä tai botti ei vastaa realistisesti siihen tehtävään, johon se on tarkoitettu. |

---

### 2. System prompt ja ohjeet — 4 pistettä

**Mitä arvioidaan?**

- Onko **system prompt** kirjoitettu selkeästi?
- Noudattaako botti promptin ohjeita johdonmukaisesti?
- Onko botille annettu selkeä rooli?
- Ovatko rajaukset eksplisiittiset eli kerrotaanko, mitä botti ei tee?

| Taso | Kuvaus |
| --- | --- |
| **Erinomainen, 4 p** | System prompt on erittäin selkeä. Botti noudattaa ohjeita johdonmukaisesti. Rooli ja rajaukset ovat hyvin määriteltyjä. |
| **Hyvä, 3 p** | Prompt on hyvä ja botti noudattaa sitä pääosin. Rooli ja rajaukset ovat mukana, mutta eivät kaikilta osin täsmällisiä. |
| **Tyydyttävä, 2 p** | Prompt on olemassa ja toimiva, mutta sitä pitäisi selkeyttää. Botti noudattaa ohjeita vaihtelevasti. |
| **Välttävä, 1 p** | Prompt on puutteellinen tai epäselvä. Botti ei noudata ohjeita johdonmukaisesti. |

> **Arviointivinkki:** Jos botti toimii hyvin sattumalta mutta prompt on epäselvä, pisteytä promptin laatu erikseen. Hyvä lopputulos ei yksin korvaa puutteellista ohjeistusta.

---

### 3. Testaus ja iterointi — 4 pistettä

**Mitä arvioidaan?**

- Onko botti testattu **positiivisilla testeillä**, **negatiivisilla testeillä** ja **reunatapauksilla**?
- Onko testaus dokumentoitu selkeästi?
- Löysikö opiskelija ongelmia tai kehittämiskohteita?
- Korjasiko opiskelija ongelmia ja testasiko hän bottia uudelleen?

| Taso | Kuvaus |
| --- | --- |
| **Erinomainen, 4 p** | Testaus on perusteellista kaikissa kategorioissa. Virheitä on löydetty, dokumentoitu, korjattu ja testattu uudelleen. Uudelleentestaus osoittaa parantumista. |
| **Hyvä, 3 p** | Testaus on monipuolista ja dokumentoitua. Ongelmia on löydetty ja joitakin korjauksia tehty. |
| **Tyydyttävä, 2 p** | Testaus on olemassa, mutta se voisi olla kattavampaa. Dokumentaatio tai iterointi jää osittain vajaaksi. |
| **Välttävä, 1 p** | Testaus on minimaalista tai dokumentointi puuttuu. Bottia ei ole testattu merkittävästi. |

#### Testausdokumentin suositeltu rakenne

| Testityyppi | Syöte | Odotettu vastaus | Saatu vastaus | Korjaus tai johtopäätös |
| --- | --- | --- | --- | --- |
| **Positiivinen testi** | Käyttäjä antaa selkeän projektikuvauksen. | Botti kysyy olennaisia kysymyksiä ja etenee loogisesti. |  |  |
| **Negatiivinen testi** | Käyttäjä pyytää bottia tekemään koko projektin hänen puolestaan. | Botti kieltäytyy tekemästä kaikkea valmiiksi ja ohjaa käyttäjää suunnittelussa. |  |  |
| **Reunatapaus** | Käyttäjä antaa epäselvän viestin, kuten ”tee suunnitelma”. | Botti pyytää tarkennuksia eikä oleta puuttuvia tietoja. |  |  |

---

### 4. Esittely ja viestintä — 4 pistettä

**Mitä arvioidaan?**

- Selittääkö opiskelija bottinsa tarkoituksen selkeästi?
- Ymmärtääkö yleisö, mitä botti tekee ja miksi se on hyödyllinen?
- Sujuuko live-demo tai vaihtoehtoinen esittely ymmärrettävästi?
- Onko esittely vakuuttava ja valmisteltu?

| Taso | Kuvaus |
| --- | --- |
| **Erinomainen, 4 p** | Selitys on erittäin selkeä ja vakuuttava. Live-demo sujuu hyvin, ja yleisö ymmärtää heti, mitä botti tekee ja miksi siitä on hyötyä. |
| **Hyvä, 3 p** | Esittely on selkeä ja demo onnistuu pääosin. Tarkoitus välittyy yleisölle. |
| **Tyydyttävä, 2 p** | Esittely onnistuu, mutta siinä on epäselvyyksiä tai demo ei ole täysin valmisteltu. |
| **Välttävä, 1 p** | Esittely on sekava, demo ei onnistu tai yleisö ei ymmärrä, mitä botti tekee. |

#### Esittelykäsikirjoituksen minimirakenne

1. **Botin nimi ja tarkoitus:** mitä botti tekee?
2. **Kohderyhmä:** kenelle botti on tarkoitettu?
3. **Lyhyt käyttötapaus:** millaisessa tilanteessa bottia käytetään?
4. **Live-demo:** yksi selkeä käyttäjätilanne.
5. **Lopputulos:** mitä botti tuottaa?
6. **Yksi kehityskohde:** mitä parantaisit seuraavaksi?

---

### 5. Reflektio ja oppiminen — 4 pistettä

**Mitä arvioidaan?**

- Pohtiiko opiskelija omaa oppimisprosessiaan?
- Osaako hän kertoa, mikä onnistui ja mikä oli vaikeaa?
- Ymmärtääkö hän, mitä tekisi seuraavalla kerralla toisin?
- Pohtiiko hän, miten botti voisi kehittyä agentiksi?

| Taso | Kuvaus |
| --- | --- |
| **Erinomainen, 4 p** | Reflektio on syvä ja pohtiva. Opiskelija ymmärtää omaa oppimistaan ja esittää perusteltuja ajatuksia siitä, miten botti voisi kehittyä agentiksi. |
| **Hyvä, 3 p** | Reflektio on hyvä ja osoittaa selkeää ymmärrystä oppimisesta ja kehittämisestä. |
| **Tyydyttävä, 2 p** | Reflektio on olemassa, mutta se jää osittain yleiseksi tai pinnalliseksi. |
| **Välttävä, 1 p** | Reflektio on hyvin lyhyt, pinnallinen tai ei liity tehtävään. |

#### Reflektion apukysymykset opiskelijalle

- Mikä botin rakentamisessa onnistui parhaiten?
- Mikä oli vaikeinta?
- Mitä muutit testauksen perusteella?
- Mitä tekisit toisin, jos aloittaisit alusta?
- Miten botti voisi kehittyä agentiksi, joka ei vain keskustele vaan myös tekee asioita?

---

## Arviointiprosessi

### Aineistot, jotka opettaja tarkistaa

| Aineisto | Mihin kriteeriin liittyy? | Mitä opettaja tarkistaa? |
| --- | --- | --- |
| **Testausdokumentti, tehtävä 18.1** | Kriteeri 3 | Ovatko testit monipuolisia, dokumentointi selkeää ja korjaukset perusteltuja? |
| **Esittelykäsikirjoitus, tehtävä 18.2** | Kriteerit 1 ja 4 | Onko botin kuvaus selkeä ja onko demo realistisesti suunniteltu? |
| **Vertaisarviot, tehtävä 18.3** | Kriteerit 4 ja 5 | Antoiko opiskelija rakentavaa palautetta ja miten muut arvioivat hänen bottiaan? |
| **Reflektio, tehtävä 18.4** | Kriteeri 5 | Onko reflektio syvä vai pinnallinen, ja näkyykö oma oppiminen? |

### Pisteyttämisen periaate

Jokainen kriteeri arvioidaan asteikolla 1–4 pistettä. Kokonaispistemäärä on 20 pistettä. Useimmat hyväksytyt suoritukset sijoittuvat todennäköisesti välille **15–18 pistettä**. Erinomainen suoritus, 18–20 pistettä, edellyttää erityisen selkeää suunnittelua, testausta, esittelyä ja reflektiota.

**Opettajan arviointimuistutus:** Arvioi erikseen botin laatu, esittelytaidot ja reflektio. Hyvä botti ei automaattisesti tarkoita erinomaista esittelyä, eikä epävarma esittely tarkoita, että botti olisi huono.

---

## Yleisimmät arviointidilemmat

| Tilanne | Ratkaisu |
| --- | --- |
| Opiskelija löysi virheitä testauksessa, mutta korjaukset eivät onnistuneet täydellisesti. | Arvioi iterointiprosessia, ei vain lopputulosta. Virheiden löytäminen ja korjausyritys osoittavat oppimista. |
| Esittely oli hidas tai epävarma, mutta botti toimi hyvin. | Erottele esittelytaito botin laadusta. Kriteeri 4 voi olla matalampi, mutta kriteerit 1–3 voivat olla korkeammat. |
| Reflektio on lyhyt, mutta sisältö on olennaista. | Älä arvioi vain pituutta. Lyhyt mutta tarkka reflektio voi olla hyvä. |
| Kaksi opiskelijaa teki samankaltaiset botit. | Samankaltaisuus ei yksin tarkoita kopiointia. Arvioi system prompt, testaus, dokumentaatio ja reflektio erikseen. Jos tekstit ovat identtiset, keskustele opiskelijoiden kanssa. |

---

## Fasilitointiohjeet

### Oppitunnin rakenne, 90 minuuttia

| Vaihe | Aika | Tavoite |
| --- | --- | --- |
| **Johdanto ja tavoitteen kirkastus** | 5 min | Muistuta, että tänään viimeistellään, testataan ja esitellään botti. |
| **Tehtävä 18.1: testaus ja iterointi** | 25 min | Opiskelijat testaavat botin positiivisilla, negatiivisilla ja reunatapauksilla. |
| **Tehtävä 18.2: esittelyn valmistelu** | 15 min | Opiskelijat kirjoittavat lyhyen esittelykäsikirjoituksen ja valitsevat demo-skenaarion. |
| **Tehtävä 18.3: esittelyt ja vertaispalaute** | 35 min | Opiskelijat esittelevät bottinsa ja antavat rakentavaa palautetta toisilleen. |
| **Tehtävä 18.4: reflektio** | 10 min | Opiskelijat kirjoittavat, mitä oppivat ja miten botti voisi kehittyä agentiksi. |

### Johdantolause opettajalle

> Viimeksi rakensitte projektidokumenttibotin ensimmäisen version. Tänään katsomme, kestääkö botti testauksen, osaako se toimia vaikeammissakin tilanteissa ja pystyttekö esittelemään sen niin, että muut ymmärtävät sen hyödyn.

---

## Luokkatehtävien ohjeistus

### TT-A: Testaa ja viimeistele botti

**Tavoite:** Opiskelija varmistaa, että botti toimii luotettavasti eri tilanteissa.

**Tee näin:**

1. Tee yksi positiivinen testi: käyttäjä antaa selkeän projektikuvauksen.
2. Tee yksi negatiivinen testi: käyttäjä pyytää jotakin, mitä botin ei kuulu tehdä.
3. Tee yksi reunatapaustesti: käyttäjä antaa epäselvän, puutteellisen tai ristiriitaisen pyynnön.
4. Kirjaa jokaisesta testistä syöte, odotettu vastaus, saatu vastaus ja johtopäätös.
5. Korjaa system promptia tai kysymyksiä, jos testit paljastavat ongelmia.
6. Testaa korjattu versio uudelleen.

**Aika-arvio:** 25 minuuttia

---

### TT-B: Valmistele botin esittely

**Tavoite:** Opiskelija osaa esitellä botin tarkoituksen, hyödyn ja toimintatavan selkeästi.

**Esittelyn pitää vastata seuraaviin kysymyksiin:**

- Mikä botin nimi on?
- Mihin ongelmaan botti auttaa?
- Kuka hyötyy botista?
- Miten botti toimii käytännössä?
- Mikä on yksi asia, jota paransit testauksen perusteella?

**Esittelyn mallirunko:**

1. Bottini nimi on...

2. Sen tarkoitus on auttaa käyttäjää...

3. Näytän lyhyen demon tilanteesta, jossa...

4. Testauksessa huomasin, että...

5. Paransin bottia muuttamalla...

**Aika-arvio:** 15 minuuttia

---

### TT-C: Esittely ja vertaispalaute

**Tavoite:** Opiskelija harjoittelee oman työn esittelyä ja rakentavan palautteen antamista.

**Ohje esittelijälle:**

1. Esittele botin tarkoitus lyhyesti.
2. Näytä yksi live-demo tai varademo.
3. Kerro yksi testauksessa löytynyt ongelma ja miten korjasit sen.
4. Kerro yksi kehitysidea seuraavaa versiota varten.

**Ohje palautteen antajalle:**

- Kerro yksi asia, joka oli selkeä tai onnistunut.
- Kerro yksi konkreettinen kehitysehdotus.
- Vältä yleistä palautetta, kuten ”ihan hyvä” tai ”huono”.
- Perustele palautteesi.

**Rakentavan palautteen malli:** ”Ymmärsin hyvin, että botti auttaa projektin aikataulutuksessa. Seuraavaksi voisit lisätä testin tilanteesta, jossa käyttäjä antaa ristiriitaisia tietoja.”

**Aika-arvio:** 35 minuuttia

---

### TT-D: Reflektio

**Tavoite:** Opiskelija pohtii omaa oppimistaan ja yhdistää botin rakentamisen tulevaan Agentit-osioon.

**Kirjoita lyhyt reflektio, jossa vastaat vähintään neljään kysymykseen:**

- Mikä botin rakentamisessa onnistui parhaiten?
- Mikä oli vaikeinta?
- Mitä muutit testauksen perusteella?
- Mitä tekisit seuraavalla kerralla toisin?
- Miten botti voisi kehittyä agentiksi?

**Aika-arvio:** 10 minuuttia

---

## Eriyttäminen

### Opiskelijat, joilla on vaikeuksia

- **Testauksen tuki:** anna valmis esimerkkitesti ja tee yhdessä yksi positiivinen ja yksi negatiivinen testi.
- **Esittelyn tuki:** anna valmis esittelyrunko ja harjoittele opiskelijan kanssa 1–2 minuutin demo.
- **Reflektion tuki:** anna kysymykset valmiina: mikä meni hyvin, mikä oli vaikeaa, mitä tekisit toisin?
- **Teknisen ongelman tuki:** salli esittely kuvakaappausten tai käsikirjoituksen avulla, jos botti ei toimi live-tilanteessa.

### Opiskelijat, joilla on vahvat taidot

- Pyydä opiskelijaa testaamaan bottia eri kielellä tai eri käyttäjäroolilla.
- Pyydä lisäämään esittelyyn visuaalinen elementti, kuten dia, prosessikaavio tai ennen–jälkeen-vertailu.
- Pyydä opiskelijaa pohtimaan, mitä työkaluja agentti tarvitsisi, jos projektidokumenttibotti kehittyisi agentiksi.
- Pyydä opiskelijaa tunnistamaan agentin turvallisuusriskejä, esimerkiksi liialliset oikeudet, virheelliset toiminnot tai puutteellinen seuranta.

---

## Virheskenaarioiden hallinta

### Botti ei toimi esittelyssä

Jos botti ei toimi esittelyhetkellä, pyydä opiskelijaa kokeilemaan uudelleen. Jos ongelma jatkuu, anna hänen esitellä botti käsikirjoituksen, kuvakaappausten tai tallennetun esimerkin avulla.

**Opettajan huomio:** Älä vähennä pisteitä pelkästä teknisestä ongelmasta, jos opiskelijan valmistelu, dokumentaatio ja ymmärrys ovat kunnossa. Merkitse arviointiin, että kyseessä oli tekninen ongelma esittelyssä.

### Botti on yksityinen tai ”salattu”

Yksityinen botti on hyväksyttävä, jos opiskelija pystyy osoittamaan sen toiminnan riittävällä tavalla. Tarvittaessa pyydä kuvakaappauksia, videota tai dokumentoitua testiaineistoa.

### Palaute on liian kriittistä tai loukkaavaa

Keskeytä tilanne ja ohjaa opiskelijoita rakentavaan palautteeseen. Mallinna parempi muotoilu:

> ”Sen sijaan, että sanomme ’tämä on huono’, sanomme: ’Tässä kohdassa käyttäjä voi jäädä epävarmaksi. Voisit lisätä tarkentavan kysymyksen.’”

---

## Dokumentaation säilyttäminen

Kerää ja säilytä seuraavat aineistot arvioinnin tueksi:

- **Testausdokumentit:** näyttävät, miten bottia testattiin ja parannettiin.
- **Esittelykäsikirjoitukset:** näyttävät, miten opiskelija ymmärtää botin tarkoituksen ja hyödyn.
- **Vertaisarvioinnit:** näyttävät palautteen antamisen ja vastaanottamisen taitoa.
- **Reflektiot:** näyttävät oppimisen kehittymistä.
- **Linkit, kuvakaappaukset tai tallenteet:** auttavat todentamaan botin toimintaa.

Näitä aineistoja voi hyödyntää myös Tekoälyjen käyttö -osion päätösraportissa, opiskelijoiden portfolioissa ja Agentit-osion johdannossa.

---

## Silta Agentit-osioon

Oppitunti 18 toimii siltana seuraavaan kokonaisuuteen. Projektidokumenttibotti on vielä botti: se keskustelee, kysyy ja kokoaa tietoa. Agentti vie tämän ajatuksen pidemmälle: se voi käyttää työkaluja, hakea tietoa, tehdä toimenpiteitä ja seurata prosessia useassa vaiheessa.

Arvioinnin aikana opettajan kannattaa kirjata muistiin:

1. **Vahvat opiskelijat:** ketkä osoittivat erityisen hyvää suunnittelua, testausta tai esittelyä?
2. **Tukea tarvitsevat opiskelijat:** ketkä tarvitsevat lisää apua agentin arkkitehtuurin ymmärtämiseen?
3. **Hyvät esimerkkibotit:** mitkä botit voidaan näyttää Agentit-osion alussa esimerkkeinä hyvästä suunnittelusta?

**Opettajan muistutus:** Kun opiskelija ymmärtää, miten botti suunnitellaan, testataan ja esitellään, hänellä on hyvä pohja ymmärtää seuraavaksi agentteja: järjestelmiä, jotka eivät vain vastaa vaan toimivat.

---

## Arviointiesimerkit

### Esimerkki 1: erinomainen suoritus

**Opiskelija A: ”Projektin analysoija -botti”**

| Kriteeri | Pisteet | Perustelu |
| --- | --- | --- |
| Botin suunnittelu ja tarkoitus | 4/4 | Tarkoitus on selkeä ja kysymykset tukevat projektisuunnittelua hyvin. |
| System prompt ja ohjeet | 4/4 | Rooli, toimintatapa ja rajaukset ovat hyvin kirjoitettuja. |
| Testaus ja iterointi | 4/4 | Kuusi testiä, selkeä dokumentaatio, promptia korjattu ja uudelleentestaus osoittaa parannusta. |
| Esittely ja viestintä | 3/4 | Esittely onnistui hyvin, mutta oli hieman nopea. |
| Reflektio ja oppiminen | 4/4 | Syvä reflektio ja hyviä ajatuksia siitä, miten botti voisi kehittyä agentiksi. |

**Yhteensä:** 19/20

---

### Esimerkki 2: tyydyttävä suoritus

**Opiskelija B: ”Yksinkertainen projektibotti”**

| Kriteeri | Pisteet | Perustelu |
| --- | --- | --- |
| Botin suunnittelu ja tarkoitus | 2/4 | Perusidea on olemassa, mutta tarkoitus jää osittain yleiseksi. |
| System prompt ja ohjeet | 2/4 | Prompt toimii, mutta rajaukset eivät ole riittävän eksplisiittisiä. |
| Testaus ja iterointi | 2/4 | Kolme testiä tehty, mutta korjauksia on vähän ja dokumentointi jää perustasolle. |
| Esittely ja viestintä | 3/4 | Esittely onnistui ja botti saatiin näytettyä ymmärrettävästi. |
| Reflektio ja oppiminen | 2/4 | Reflektio on olemassa, mutta se jää melko pinnalliseksi. |

**Yhteensä:** 11/20

**Mahdollinen palaute:** ”Botti toimii perustasolla ja esittely onnistui. Seuraavaksi kannattaa vahvistaa system promptia, lisätä selkeät rajaukset ja testata bottia monipuolisemmin. Reflektiossa voisit kertoa tarkemmin, mitä opit ja miten kehittäisit bottia agentiksi.”

---

## Lisäresurssit opettajalle

- **Bloom’n taksonomia:** arviointi kohdistuu erityisesti analysointiin, arviointiin ja luomiseen.
- **Metakognitio:** reflektio auttaa opiskelijaa tunnistamaan omaa oppimistaan ja ajattelunsa kehittymistä.
- **Vertaisarviointi:** kehittää kriittistä ajattelua, palautteen antamista ja yhteistyötaitoja.
- **Agentit-osioon siirtyminen:** hyvät botit voidaan nostaa esiin esimerkkeinä siitä, miten suunniteltu botti voi kehittyä toimivaksi agentiksi.

---

## Viimeinen vinkki opettajalle

Muista, että kyseessä ovat IT-alan ensimmäisen vuoden opiskelijat. Monille opiskelijoille botin rakentaminen, testaaminen, dokumentointi ja esittely ovat jo merkittävä saavutus. Arvioi tarkasti, mutta kannustavasti.

Kannusta niitä, jotka onnistuivat hyvin. Tue niitä, joilla prosessi jäi kesken. Tämän osion tärkein tavoite on, että opiskelija ymmärtää tekoälyn vastuullisen, itsenäisen ja dokumentoidun käytön perustan. Agentit-osiossa nämä taidot syvenevät.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että onnistunut botti ei ole vain valmis tekninen tuotos. Se on suunniteltu, testattu, parannettu, dokumentoitu ja esitelty. Tämän työn kautta opiskelija osoittaa, että hän osaa käyttää tekoälyä tavoitteellisesti ja vastuullisesti.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Mitä bottisi osaa nyt, ja mitä sen pitäisi vielä osata, jotta siitä voisi tulla agentti?

> **Lopetuslause opettajalle:** Botti vastaa kysymyksiin. Agentti toimii tavoitteellisesti. Tänään viimeistelitte ensimmäisen askeleen kohti sitä ajattelua.

:contentReference[oaicite:0]{index=0}

---
