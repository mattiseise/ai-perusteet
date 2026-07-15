# Opettajan materiaalit — kontekstin antaminen

## Oppimisen tavoitteet tälle lohkolle

**Pedagoginen rajaus suhteessa tuntiin 4:** Älä käytä tuntia kontekstin ja promptin perusmääritelmien uudelleenopettamiseen. Palauta ero yhdellä esimerkillä ja siirry soveltavaan tuotokseen: uudelleen käytettävä prompti, nimetty lähdeaineisto, pilkotut osatehtävät sekä ennen–jälkeen-testillä perusteltu iterointi.

Tämän lohkon tavoitteena on, että opiskelija ymmärtää, miksi **konteksti** ratkaisee tekoälyn vastausten laadun. Oppitunnin ydin on, että tekoäly ei automaattisesti tiedä käyttäjän tilannetta, osaamistasoa, tavoitetta tai käyttötarkoitusta. Mitä paremmin opiskelija osaa antaa kontekstin, sitä täsmällisempiä, hyödyllisempiä ja asiallisesti käyttökelpoisempia vastauksia hän saa.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, että parempi **konteksti** tuottaa yleensä parempia vastauksia.
- Opiskelija tietää, mitä kontekstiin kuuluu: **kuka olet**, **mitä haluat**, **mihin käytät vastausta**, **mitä tiedät jo** ja **miten haluat vastauksen rakennetuksi**.
- Opiskelija ymmärtää, että tekoäly tekee oletuksia, jos käyttäjä ei anna riittävää kontekstia.
- Opiskelija ymmärtää, että kontekstin antaminen on asiallinen taito, ei turhaa lisätekstiä.

### Soveltaa ja analysoida

- Opiskelija osaa rakentaa kontekstia asteittain: hän lisää tietoa kierros kierrokselta, kunnes tekoäly ymmärtää tehtävän paremmin.
- Opiskelija osaa vertailla heikkoa ja hyvää promptia ja tunnistaa, mikä kontekstissa parantaa vastausta.
- Opiskelija osaa käyttää **lähdeaineistoa**, kuten tekstiä, koodia tai dokumenttia, tekoälyn kontekstina.
- Opiskelija osaa pilkkoa suuren tehtävän pienempiin, hallittaviin osiin.

### Luoda ja arvioida

- Opiskelija osaa kirjoittaa täsmällisen promptin, jossa konteksti on rakennettu tarkoituksenmukaisesti.
- Opiskelija osaa käyttää **iteraatiota**: hän tarkentaa pyyntöä tekoälyn vastauksen perusteella.
- Opiskelija osaa arvioida, milloin tekoälyn vastaus on liian yleinen ja mitä kontekstia seuraavaksi pitäisi lisätä.
- Opiskelija ymmärtää, että vastuullinen käyttäjä ei vain kysy tekoälyltä, vaan ohjaa sitä tietoisesti.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että konteksti ei ole sattumanvaraista lisätietoa. Se on strateginen valinta siitä, mitä tekoälyn pitää tietää, jotta se voi auttaa oikein. Vastuullinen käyttäjä miettii ensin tilanteen, tavoitteen ja rajaukset — vasta sitten hän kirjoittaa promptin.

---

## Pedagoginen lähestymistapa

### Ydinviesti: konteksti ohjaa tekoälyn ajattelusuuntaa

Oppitunti kannattaa aloittaa hyvin yksinkertaisella esimerkillä. Kirjoita tekoälylle ensin: **”Kerro verkoista.”** Sen jälkeen lisää kontekstia vaiheittain: opiskelijan ikä, opiskeluala, osaamistaso, tavoite, vastausmuoto ja käytettävissä oleva aika. Näin opiskelijat näkevät konkreettisesti, miten sama aihe muuttuu eri vastaukseksi, kun konteksti tarkentuu.

> **Sama aihe, eri konteksti — täysin erilainen vastaus.**

Korosta opiskelijoille:

- **Lyhyt prompti** voi toimia, jos tehtävä on yksinkertainen.
- **Asiallisessa tehtävässä** tekoäly tarvitsee yleensä enemmän taustaa.
- **Konteksti ei tarkoita pitkää sekavaa tekstiä**, vaan olennaisten tietojen valintaa.
- **Hyvä konteksti säästää aikaa**, koska tarkentavia kierroksia tarvitaan vähemmän.

### Kontekstin osat

Opiskelijoiden kannattaa opetella yksinkertainen tarkistuslista. Hyvässä kontekstissa ei tarvitse aina olla kaikkea, mutta opiskelijan pitää osata miettiä, mitkä osat ovat kyseisessä tilanteessa tärkeitä.

| Kontekstin osa | Mitä se kertoo tekoälylle? | Esimerkki |
| --- | --- | --- |
| **Kuka olet?** | Käyttäjän rooli ja osaamistaso. | ”Olen 15-vuotias IT-opiskelija ilman ohjelmointitaustaa.” |
| **Mitä haluat?** | Tehtävän tavoite. | ”Haluan oppia verkkojen perusteet 30 minuutissa.” |
| **Mihin käytät vastausta?** | Vastauksen käyttötarkoitus. | ”Käytän vastausta kokeeseen valmistautumiseen.” |
| **Mitä tiedät jo?** | Lähtötaso ja aiempi osaaminen. | ”Tiedän, että laitteet voivat olla samassa verkossa, mutta en ymmärrä IP-osoitteita.” |
| **Mitä et tiedä?** | Kohdat, joissa opiskelija tarvitsee apua. | ”En ymmärrä, mikä ero on reitittimellä ja kytkimellä.” |
| **Miten haluat vastauksen?** | Rakenne, taso ja formaatti. | ”Anna ensin selitys, sitten kolme esimerkkiä ja lopuksi testikysymykset.” |

### Kontekstin rakentaminen asteittain

Kontekstin rakentamista kannattaa opettaa vaiheittaisena taitona. Opiskelijan ei tarvitse osata kirjoittaa täydellistä promptia heti ensimmäisellä kerralla. Tärkeää on, että hän huomaa, mitä vastauksesta puuttuu, ja osaa lisätä seuraavalla kierroksella oikeaa tietoa.

**Pyyntö 1:** Kerro verkoista.

**Pyyntö 2:** Kerro verkoista. Olen 15-vuotias opiskelija.

**Pyyntö 3:** Kerro verkoista. Olen 15-vuotias IT-opiskelija ja haluan konkreettisia esimerkkejä.

**Pyyntö 4:** Kerro verkoista. Olen 15-vuotias IT-opiskelija ilman ohjelmointitaustaa. Haluan oppia 30 minuutissa. Anna selitys, kolme esimerkkiä, yleiset virheet ja viisi testikysymystä.

Kun näytät nämä neljä pyyntöä, pyydä opiskelijoita arvioimaan, mikä muuttui vastauksissa. Ohjaa heitä huomaamaan, että tekoäly ei vain vastannut pidemmin, vaan eri tasolla, eri rakenteella ja eri käyttötarkoitusta varten.

---

## Pilkkominen ja lähdeaineiston käyttö

### Pilkkominen tekee suuresta tehtävästä hallittavan

**Pilkkominen** tarkoittaa suuren tehtävän jakamista pienempiin osiin. Opiskelijat saattavat ajatella, että tämä vie enemmän aikaa kuin ”kaikki kerralla” -pyyntö. Käytännössä pilkkominen parantaa vastauksen laatua, koska jokaisella pyynnöllä on selkeämpi tavoite.

> **Iso tehtävä ei ole yksi suuri prompti. Se on sarja pieniä, hyvin ohjattuja pyyntöjä.**

Esimerkiksi tehtävä **”Kirjoita dokumentaatio verkkoturvallisuudesta”** voidaan pilkkoa näin:

1. **Perustiedot:** mitä verkkoturvallisuus tarkoittaa?
2. **Riskit:** mitkä ovat kolme yleistä verkkoturvallisuuden riskiä?
3. **Käytännön suojaus:** miten kotiverkko tai koulun verkko suojataan?
4. **Esimerkit:** millaisia tilanteita opiskelija voi kohdata arjessa?
5. **Testikysymykset:** miten opiskelija voi tarkistaa osaamisensa?

### Lähdeaineisto tekee vastauksesta täsmällisemmän

**Lähdeaineiston antaminen** tarkoittaa, että opiskelija antaa tekoälylle tekstin, koodin, raportin, lokin tai muun materiaalin, jonka perusteella tekoälyn pitää vastata. Tämä on tärkeää, koska tekoäly ei muuten näe opiskelijan todellista tilannetta.

Esimerkiksi jos opiskelija haluaa parantaa raporttia, heikko pyyntö on:

Miten parannan raporttia?

Vahvempi pyyntö on:

Tässä on raporttimme. Paranna sitä seuraavista näkökulmista:

1. Johdanto on liian lyhyt.

2. Johtopäätelmät ovat pinnalliset.

3. Lähdeviitteet puuttuvat. Anna ensin palautetta, älä kirjoita koko raporttia uudelleen.

**Opettajan huomio:** Muistuta tietosuojasta. Lähdeaineistoa voi antaa tekoälylle vain, jos sen jakaminen on sallittua. Opiskelijoiden, asiakkaiden, potilaiden tai yrityksen sisäisiä tietoja ei saa syöttää julkiseen palveluun ilman lupaa ja asianmukaista arviointia.

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”Konteksti on vain erilaisten tietojen sanomista.”

**Korjaava näkökulma:** Konteksti ei ole satunnainen taustatietojen kasa. Se on strateginen valinta siitä, mitä tekoälyn pitää ymmärtää. Vastuullinen käyttäjä miettii, mikä tieto vaikuttaa vastauksen tasoon, näkökulmaan, rajaukseen ja käyttötarkoitukseen.

### Väärinkäsitys 2: ”Tekoäly osaa arvata kontekstin, vaikka en sanoisi sitä.”

**Korjaava näkökulma:** Tekoäly tekee oletuksia, jos konteksti puuttuu. Esimerkiksi ”Kerro verkoista” voi tarkoittaa tietokoneverkkoja, sosiaalisia verkostoja, kalastusverkkoja tai peliverkkoja. Jos käyttäjä ei kerro tilannetta, tekoäly arvaa — ja arvaus voi mennä väärään suuntaan.

### Väärinkäsitys 3: ”Kontekstin antaminen tekee pyynnöstä liian pitkän.”

**Korjaava näkökulma:** Hyvä ensimmäinen pyyntö voi olla pidempi, mutta se säästää usein aikaa myöhemmin. Kun tekoäly ymmärtää tilanteen heti paremmin, käyttäjän ei tarvitse korjata ja tarkentaa vastausta yhtä monta kertaa.

> Pidempi hyvä pyyntö on usein nopeampi kuin monta lyhyttä epäselvää pyyntöä.

### Väärinkäsitys 4: ”Pilkkominen vie enemmän aikaa kuin kaiken kysyminen kerralla.”

**Korjaava näkökulma:** Pilkkominen voi näyttää hitaammalta, mutta se tekee työstä hallittavampaa. Jokainen osa voidaan tarkistaa, parantaa ja yhdistää myöhemmin. Usein lopputulos on parempi ja virheitä syntyy vähemmän.

### Väärinkäsitys 5: ”Lähdeaineiston antaminen tarkoittaa, että kopioin tekoälyn vastauksen.”

**Korjaava näkökulma:** Lähdeaineiston antaminen ei tarkoita kopiointia. Se tarkoittaa, että tekoäly saa nähdä todellisen materiaalin, jota sen pitää analysoida, selittää, parantaa tai kommentoida. Opiskelija vastaa silti lopullisesta tekstistä ja ratkaisuista.

---

## Opettajan fasilitointiohjeet

### Ennen lähiosaa, noin 20 minuuttia

1. **Testaa itse kontekstin rakentaminen.** Valitse yksi aihe, esimerkiksi ”Verkon perusteet”, ja tee neljä asteittain tarkentuvaa pyyntöä.
2. **Tallenna vastaukset.** Ota kuvakaappaukset tai kopioi vastaukset talteen, jotta voit näyttää erot myös ilman live-demoa.
3. **Valmistele esimerkit.** Tee valmiiksi hyvä ja huono kontekstiesimerkki, pilkkomisesimerkki, lähdeaineistoesimerkki ja iteraatioesimerkki.
4. **Varmista pääsy tekoälypalveluun.** Testaa palvelu ennen tuntia ja valmistele varasuunnitelma, jos verkko ei toimi.

### Lähiosan rakenne, 90 minuuttia

| Vaihe | Aika | Tavoite |
| --- | --- | --- |
| **Johdanto** | 5 min | Motivoi aihe: konteksti ratkaisee vastauksen laadun. |
| **Osio 1: live-demo neljällä kontekstilla** | 30 min | Näytä, miten vastaukset muuttuvat, kun konteksti tarkentuu. |
| **Osio 2: pienryhmät** | 30 min | Opiskelijat rakentavat kontekstia eri skenaarioihin. |
| **Osio 3: iteraatioharjoitus** | 20 min | Opiskelijat harjoittelevat jatkokysymysten ja tarkennusten rakentamista. |
| **Yhteenveto** | 5 min | Kokoa ydinoivallus: vastuullinen käyttäjä rakentaa kontekstia tietoisesti. |

### Johdantolause opettajalle

> Viimeksi opimme käyttämään tekoälyä. Tänään opimme jotain yhtä tärkeää: konteksti ratkaisee vastauksen laadun. Sama aihe voi tuottaa täysin erilaisen vastauksen sen mukaan, mitä kerrot tilanteestasi.

---

## Yleisiä haasteita ja ratkaisuja

| Haaste | Miten ohjaat? |
| --- | --- |
| Opiskelija kysyy, miksi pitää kirjoittaa niin pitkä pyyntö. | Näytä, että hyvä ensimmäinen pyyntö vähentää turhia tarkennuskierroksia. Korosta, että konteksti on ajansäästöä, ei ylimääräinen vaiva. |
| Opiskelija ei tiedä, mitä kontekstia antaa. | Kysy: kuka olet, mitä haluat, mihin käytät vastausta, mitä tiedät jo ja missä tarvitset apua? |
| Opiskelija tekee liian lyhyen ensimmäisen pyynnön. | Näytä elävä esimerkki siitä, miten vastaus jää yleiseksi ja epäosuvaksi ilman kontekstia. |
| Opiskelija ei tiedä, onko konteksti riittävä. | Käytä testiä: voisiko toinen opiskelija lukea pyynnön ja ymmärtää, mitä tilanteessa tarvitaan? |
| Opiskelija ei näe iteraation hyötyä. | Näytä neljä kierrosta samasta aiheesta ja pyydä opiskelijoita arvioimaan, miksi viimeinen vastaus on hyödyllisempi kuin ensimmäinen. |

---

## Luokkatehtävien ohjeistus

### TT-A: Neljä kontekstia samaan aiheeseen

**Tavoite:** Opiskelija näkee, miten kontekstin lisääminen muuttaa tekoälyn vastausta.

**Tehtävä:** Opiskelija antaa tekoälylle saman aiheen neljällä eri tavalla. Jokaisessa kierroksessa konteksti tarkentuu.

**Ohje opiskelijalle:**

1. Kirjoita ensimmäinen pyyntö ilman kontekstia, esimerkiksi: **”Kerro verkoista.”**
2. Lisää toisella kierroksella oma roolisi ja osaamistasosi.
3. Lisää kolmannella kierroksella tavoite ja käyttötarkoitus.
4. Lisää neljännellä kierroksella haluttu vastausrakenne, esimerkit ja tarkistus- tai testikysymykset.
5. Vertaa vastauksia ja kirjoita, mikä muuttui.

| Kierros | Mitä lisättiin? | Miten vastaus muuttui? |
| --- | --- | --- |
| **1** | Ei kontekstia. |  |
| **2** | Rooli ja osaamistaso. |  |
| **3** | Tavoite ja käyttötarkoitus. |  |
| **4** | Vastausrakenne, esimerkit ja testikysymykset. |  |

**Aika-arvio:** 25–30 minuuttia

---

### TT-B: Kontekstin rakentaminen pienryhmissä

**Tavoite:** Opiskelija harjoittelee kontekstin rakentamista erilaisiin tilanteisiin.

**Tehtävä:** Ryhmä saa yhden skenaarion ja kirjoittaa siihen hyvän kontekstin ja promptin.

| Skenaario | Mitä kontekstia tarvitaan? | Mahdollinen hyvä prompti |
| --- | --- | --- |
| Opiskelija ei ymmärrä Python-funktioita. | Osaamistaso, tavoite, halutut esimerkit ja yleiset virheet. |  |
| Ryhmä haluaa parantaa keskeneräistä raporttia. | Raportin teksti, arviointikriteerit, ongelmakohdat ja haluttu palautetyyli. |  |
| Opiskelija valmistautuu tietoturvakokeeseen. | Kokeen aihealue, opiskelijan osaamistaso, vaikeat kohdat ja harjoitustapa. |  |
| Opiskelija haluaa selittää virheilmoituksen Linuxissa. | Komento, virheilmoitus, mitä oli tarkoitus tehdä ja mitä on jo kokeiltu. |  |

**Aika-arvio:** 25–30 minuuttia

---

### TT-C: Iteraation rakentaminen

**Tavoite:** Opiskelija ymmärtää, että tekoälytyöskentely on usein usean kierroksen prosessi.

**Tehtävä:** Opiskelija valitsee oppimisaiheen ja kirjoittaa neljä pyyntöä, joista jokainen rakentuu edellisen päälle.

**Esimerkki:**

1. **Kierros 1:** Kerro Python-funktioista.
2. **Kierros 2:** Lisää kolme konkreettista esimerkkiä.
3. **Kierros 3:** Lisää kolme yleistä virhettä, joita opiskelijat tekevät.
4. **Kierros 4:** Tee kolme testikysymystä, joissa virheellinen vastaus on helppo tehdä.

**Ohje opiskelijalle:**

- Älä kirjoita neljää satunnaista kysymystä.
- Jokaisen kierroksen pitää tarkentaa edellistä.
- Kirjoita lopuksi, mikä kierros tuotti hyödyllisimmän vastauksen ja miksi.

**Aika-arvio:** 15–20 minuuttia

---

### TT-D: Pilko suuri tehtävä

**Tavoite:** Opiskelija osaa jakaa suuren tehtävän pienempiin tekoälylle annettaviin osiin.

**Tehtävä:** Opiskelija valitsee suuren tehtävän, kuten raportin kirjoittamisen, tenttiin valmistautumisen tai dokumentaation laatimisen, ja pilkkoo sen vaiheiksi.

| Osa | Mitä tekoälyltä pyydetään? | Mitä kontekstia annetaan? |
| --- | --- | --- |
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |

**Aika-arvio:** 15–20 minuuttia

---

## Arviointikriteerit

### Taso 1: Muistaminen ja ymmärtäminen

Opiskelija:

- nimeää kontekstin perusosat
- ymmärtää, että parempi konteksti tuottaa paremman vastauksen
- tietää pilkkomisen, iteraation ja lähdeaineiston perusidean

**Mitä opettaja etsii:** Opiskelija osaa sanoa esimerkiksi: ”Konteksti kertoo tekoälylle, kuka olen, mitä haluan ja mihin käytän vastausta.”

### Taso 2: Soveltaminen ja analysoiminen

Opiskelija:

- rakentaa parempaa kontekstia vähintään kahdessa vaiheessa
- näkee, miten konteksti parantaa vastausta
- osaa antaa lähdeaineistoa tekoälylle
- osaa tehdä yksinkertaisen pilkkomisen

**Mitä opettaja etsii:** Opiskelija muuttaa heikon pyynnön, kuten ”Auta esseen kanssa”, täsmällisemmäksi pyynnöksi, jossa näkyvät aihe, tavoite, pituus, rakenne ja käyttötarkoitus.

### Taso 3: Arvioiminen ja luominen

Opiskelija:

- rakentaa kontekstia systemaattisesti useassa vaiheessa
- perustelee, miksi jokainen tarkennus parantaa vastausta
- osaa pilkkoa monimutkaisen tehtävän osiin
- käyttää lähdeaineistoa ja iteraatiota tarkoituksenmukaisesti
- kirjoittaa tarkan pyynnön, jossa on riittävä konteksti ja selkeä tavoite

**Mitä opettaja etsii:** Opiskelija ei ainoastaan lisää tietoa, vaan osaa selittää, miksi juuri tämä tieto on tekoälyn kannalta tarpeellinen.

---

## Tarkistustehtävät oppimisen varmistamiseen

### 1. Kontekstin rakentaminen

**Tehtävä:** Kirjoita kaksi erilaista pyyntöä tekoälylle aiheesta **verkot**. Ensimmäinen on heikko, toinen on parempi kontekstin avulla.

**Hyvä vastaus:** Heikko: ”Kerro verkoista.” Parempi: ”Olen 15-vuotias IT-opiskelija. Haluan oppia verkoista 30 minuutissa. Anna perustiedot, kolme esimerkkiä jokapäiväisestä elämästä ja viisi testikysymystä.”

**Heikko vastaus:** ”Kerro verkoista” ja ”Kerro enemmän verkoista.” Tässä toinen pyyntö ei lisää oikeaa kontekstia.

### 2. Pilkkomisen soveltaminen

**Tehtävä:** Sinulla on iso tehtävä: **”Kirjoita dokumentaatio verkkoturvallisuudesta.”** Pilko se pienempiin osiin, jotka voisit antaa tekoälylle.

**Hyvä vastaus:**

1. Mitä verkkoturvallisuus tarkoittaa?
2. Kolme yleistä riskiä ja niiden selitykset.
3. Käytännön esimerkit kotiverkon suojaamisesta.
4. Yleisimmät virheet, joita opiskelijat tekevät.
5. Testikysymykset opiskelijoille.

**Heikko vastaus:** ”Kysy tekoälyltä: kirjoita dokumentaatio verkkoturvallisuudesta.” Tämä ei ole pilkottu.

### 3. Lähdeaineiston käyttäminen

**Tehtävä:** Sinulla on opiskelijoiden kirjoittama raportti, joka tarvitsee parannusta. Miten annat sen tekoälylle?

**Hyvä vastaus:** Opiskelija antaa raportin tai olennaisen osan siitä tekoälylle ja kirjoittaa selkeän pyynnön: ”Tässä on raporttimme. Anna palautetta erityisesti johdannosta, johtopäätöksistä ja lähdeviitteistä. Älä kirjoita koko raporttia uudelleen, vaan anna parannusehdotukset.”

**Heikko vastaus:** ”Miten parannan raporttia?” ilman, että raporttia annetaan tekoälylle nähtäväksi.

### 4. Iteraation soveltaminen

**Tehtävä:** Valitse oppimisaihe ja kirjoita neljä erilaista pyyntöä, joista jokainen rakentuu edellisen päälle.

**Hyvä vastaus:**

1. Kerro Python-funktioista.
2. Lisää kolme konkreettista esimerkkiä.
3. Lisää kolme yleistä virhettä, joita opiskelijat tekevät.
4. Tee kolme testikysymystä, joissa virheelliset vastaukset ovat todennäköisiä.

**Heikko vastaus:** Vain yksi kysymys, esimerkiksi ”Kerro Python-funktioista.” Tällöin iteraatiota ei synny.

---

## Lisäresurssit opettajalle

### Harjoitustehtävät opiskelijoille

#### Helppo

Valitse IT-aihe, esimerkiksi palvelimet, tietoturva tai tietokoneverkot. Kysy tekoälyltä ensin ilman kontekstia: **”Kerro aiheesta.”** Kysy sitten uudelleen kontekstilla: **”Olen 15-vuotias opiskelija. Kerro aiheesta yksinkertaisesti ja anna kolme arjen esimerkkiä.”** Vertaa vastauksia.

#### Keskivaikea

Valitse opiskelun aihe. Kirjoita neljä pyyntöä: ensimmäinen on heikko ja neljäs on paras. Näytä, miten konteksti parantaa vastausta kierros kierrokselta.

#### Vaikea

Valitse suuri tehtävä, kuten raportin kirjoittaminen, tenttiin valmistautuminen tai dokumentaation laatiminen. Pilko tehtävä pienempiin osiin ja kirjoita jokaiselle osalle oma, täsmällinen prompti.

---

## Jatkuva integraatio seuraavalle tunnille

Seuraavalla tunnilla opiskelijat harjoittelevat kontekstin rakentamista omissa projekteissaan. He käyttävät pilkkomista, iteraatiota ja lähdeaineistoa käytännössä ja näkevät, kuinka konteksti vaikuttaa heidän omiin lopputuloksiinsa.

**Opettajan muistutus:** Kontekstin rakentaminen erottaa satunnaisen tekoälyn käyttäjän vastuullisesta käyttäjästä. Vastuullinen käyttäjä ei vain kysy, vaan määrittää tilanteen, tavoitteen ja rajat.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että tekoälyn vastaus riippuu voimakkaasti siitä, mitä käyttäjä sille kertoo. Hyvä konteksti tekee vastauksesta täsmällisemmän, käyttökelpoisemman ja paremmin opiskelijan tilanteeseen sopivan. Pilkkominen, lähdeaineiston antaminen ja iteraatio ovat asiallisia tekoälyn käyttötaitoja.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Mitä tekoälyn pitäisi tietää sinusta, tavoitteestasi ja tehtävästäsi, jotta se voisi antaa oikeasti hyödyllisen vastauksen?

> **Lopetuslause opettajalle:** Tekoäly ei lue ajatuksia. Vastuullinen käyttäjä osaa antaa sille oikean tilanteen.

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **promptipankin yksi testattu kortti versioineen**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–10 min | Virittäytyminen | Kytke ydinkysymys tuttuun tilanteeseen ja tarkista lähtötaso. |
| 10–25 min | Ydinkäsite | Mallinna tunnin keskeinen ero yhdellä vastaesimerkillä. |
| 25–65 min | Perustuotos | Oppija rakentaa konteksti–lähde–vaiheet–muoto-kortin, testaa sen ja tallentaa kaksi versiota. Tämä 40 minuutin jakso on itsenäistä tai parin kanssa tehtävää työskentelyä. |
| 65–80 min | Testaus ja purku | Testauta tuotos annetulla tapauksella ja pura yksi onnistuminen sekä yksi korjaus. |
| 80–90 min | Tallennus ja exit ticket | Varmista tiedoston nimi, tallennuspaikka ja yhden lauseen johtopäätös. |

### Tukireitti

Oppija täyttää annetun promptikorttipohjan. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis, oppija soveltaa testattua korttia toiseen käyttötapaan. Syventävä työ ei kasvata pakollista ydintuotosta.
