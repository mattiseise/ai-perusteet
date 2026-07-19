# Opettajan materiaalit — oppitunti 17: oman apuri-botin suunnittelu ja rakentamisen aloitus

## Oppitunnin tarkoitus ja konteksti

Tämä oppitunti on **Tekoälyjen käyttö** -osion arvioinnin ensimmäinen osa. Oppitunti 17 keskittyy **suunnitteluun** ja **rakentamisen aloittamiseen**. Oppitunnilla 18 opiskelijat viimeistelevät, parantavat ja esittelevät työnsä.

Oppitunnin tavoitteena on, että opiskelijat suunnittelevat ja rakentavat **Microsoft Copilotilla** uuden botin: oman **apuri-botin** itse valitsemaansa arjen aiheeseen — opiskeluun, harrastukseen, tuttuun pieneen palveluun tai vaikka pelin tai sisällön ideointiin. Botin tehtävänä on kysyä käyttäjältä oikeita kysymyksiä, ohjata häntä järjestelmällisesti eteenpäin ja toimia ohjaavan apurin tavoin.

Opiskelijat osoittavat osaamistaan suunnittelemalla botille tarkoituksen, roolin, ohjeet, rajaukset ja kysymyspatteriston. He kirjoittavat **järjestelmäpromptin**, testaavat bottia käytännön tilanteissa, parantavat sitä iteratiivisesti ja dokumentoivat prosessin selkeästi.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että arvioinnissa ei mitata vain lopullista bottia. Arvioinnissa mitataan erityisesti suunnittelua, testausta, iteraatiota ja dokumentoitua ajattelua. Hyvä työ näyttää, miten botti syntyi ja miksi sitä muutettiin.

---

## Oppimisen tavoitteet

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, mikä **apuri-botti** on ja mihin sitä käytetään.
- Opiskelija ymmärtää, että hyvä botti tarvitsee selkeän **tarkoituksen**, **roolin**, **ohjeet** ja **rajaukset**.
- Opiskelija ymmärtää, että **järjestelmäprompti** ohjaa botin käyttäytymistä ja kysymysten järjestystä.
- Opiskelija ymmärtää, että testaus ja korjaaminen kuuluvat botin rakentamiseen.

### Soveltaa ja analysoida

- Opiskelija osaa suunnitella järjestelmällisen **kysymysketjun** käyttäjän ohjaamista varten.
- Opiskelija osaa kirjoittaa järjestelmäpromptin, jossa näkyvät botin identiteetti, tarkoitus, toimintatapa ja rajaukset.
- Opiskelija osaa testata bottia vähintään kahdella erilaisella käyttöskenaariolla.
- Opiskelija osaa analysoida testituloksia: mikä toimi, mikä ei toiminut ja miksi.

### Luoda ja arvioida

- Opiskelija osaa rakentaa ensimmäisen toimivan version apuri-botista.
- Opiskelija osaa parantaa bottia testitulosten perusteella.
- Opiskelija osaa dokumentoida tehtävät 17.1–17.4 niin, että toinen henkilö ymmärtää rakentamisen vaiheet.
- Opiskelija osaa arvioida omaa botin kehitysprosessiaan kriittisesti.

---

## Arvioinnin kokonaisuus

Oppitunnit 17 ja 18 muodostavat yhdessä **Tekoälyjen käyttö** -osion arvioinnin. Oppitunnilla 17 arvioidaan erityisesti suunnittelua, järjestelmäpromptia, testausta, iteraatiota ja dokumentaatiota. Oppitunnilla 18 arviointi jatkuu viimeistelyllä, esittelyllä ja lopullisen tuotoksen laadulla.

Oppitunnin 17 osuus on noin **kaksi kolmasosaa** kokonaisuudesta (40 pistettä 60 pisteen kokonaisuudesta).

### Pisteytys

| Arvosana | Pistemäärä | Yleiskuvaus |
| --- | --- | --- |
| **5 — Erinomainen** | 36–40 p | Suunnittelu, testaus, iteraatio ja dokumentaatio ovat selkeitä, perusteltuja ja asiallisia. |
| **4 — Hyvä** | 32–35 p | Kokonaisuus toimii hyvin, mutta joissakin kohdissa analyysi tai dokumentointi voisi olla tarkempaa. |
| **3 — Tyydyttävä** | 28–31 p | Perusasiat ovat mukana, mutta suunnittelu, testaus tai parantaminen jää osittain pinnalliseksi. |
| **2 — Välttävä** | 20–27 p | Työssä on selviä puutteita, mutta joitakin arvioitavia osia on tehty. |
| **1 — Hylätty** | 0–19 p | Työ ei vielä osoita riittävää osaamista botin suunnittelusta, testaamisesta ja dokumentoinnista. |

---

## Arviointikohteet yksityiskohtaisesti

### 1. Botin suunnittelu ja rooli — 8 pistettä

**Mitä arvioidaan?**

- Onko botin tarkoitus selkeä: auttaa käyttäjää jossakin tutussa arjen tehtävässä?
- Onko botin rooli uskottava, esimerkiksi kertauskaveri, harrastuksen opastaja tai FAQ-apuri?
- Ovatko ohjeet selkeät: miten botti kysyy, kuuntelee, tarkentaa ja ohjaa eteenpäin?
- Ovatko rajaukset sopivat?
- Onko tehtävässä 17.1 laadittu **kysymyspatteristo** järjestelmällinen ja riittävän kattava?

| Taso | Kuvaus |
| --- | --- |
| **Erittäin hyvä, 8 p** | Tarkoitus on konkreettinen, rooli on uskottava, ohjeet ovat selkeitä, rajaukset ovat vastuullisia ja kysymyspatteristo sisältää noin 15–20 hyvin järjestettyä kysymystä esimerkiksi viidessä ryhmässä. |
| **Heikko, 1–2 p** | Tarkoitus on epämääräinen, rooli puuttuu tai on yleinen, ohjeet ovat tasolla ”kysy oikeita kysymyksiä”, rajaukset puuttuvat ja kysymyspatteristo on lyhyt tai satunnainen. |

**Esimerkki hyvästä tarkoituksesta:**

”Botti auttaa opiskelijaa kertaamaan kokeeseen järjestelmällisten kysymysten avulla.”

**Esimerkki hyvästä roolista:**

”Olet kärsivällinen kertauskaveri, jolla on kokemusta aiheen selittämisestä, oikeiden kysymysten esittämisestä ja käyttäjän ohjaamisesta vaihe vaiheelta.”

---

### 2. Järjestelmäpromptin kirjoittaminen — 8 pistettä

**Mitä arvioidaan?**

- Sisältääkö järjestelmäprompti **identiteetin**, **tarkoituksen**, **ohjeet** ja **rajaukset**?
- Ovatko ohjeet selkeitä kielimallille?
- Näkyykö promptista, miten botin pitää käyttäytyä käytännössä?
- Onko prompti riittävän laaja, esimerkiksi noin 300–500 sanaa?

| Taso | Kuvaus |
| --- | --- |
| **Erittäin hyvä, 8 p** | Prompt sisältää kaikki neljä osaa selkeästi. Ohjeet ovat konkreettisia, johdonmukaisia ja toiminnallisia. Promptista näkee, missä järjestyksessä botti kysyy ja miten se ohjaa käyttäjää kohti lopputulosta. |
| **Heikko, 1–2 p** | Prompt on vain muutama lause. Rajaukset puuttuvat, ohjeet ovat yleisiä, ja teksti näyttää tekoälyn tuottamalta ilman opiskelijan omaa muokkausta. |

> **Järjestelmäprompti on botin toimintasuunnitelma.** Jos se on epämääräinen, botti joutuu arvaamaan. Jos se on täsmällinen, botti toimii johdonmukaisemmin.

#### Järjestelmäpromptin suositeltu rakenne

**1. Identiteetti:** Kuka botti on?

**2. Tarkoitus:** Mitä botti auttaa käyttäjää tekemään?

**3. Toimintatapa:** Missä järjestyksessä botti kysyy ja miten se reagoi vastauksiin?

**4. Rajaukset:** Mitä botti ei saa tehdä?

---

### 3. Testaus ja validointi — 8 pistettä

**Mitä arvioidaan?**

- Kuinka monta testiskenaariota opiskelija on dokumentoinut?
- Ovatko testit erilaisia ja järkeviä?
- Onko mukana sekä onnistumisia että kehittämiskohteita?
- Onko testidokumentaatiossa näkyvissä **syöte**, **odotettu toiminta** ja **todellinen tulos**?

| Taso | Kuvaus |
| --- | --- |
| **Erittäin hyvä, 8 p** | Opiskelija dokumentoi kaksi erilaista testiskenaariota, esimerkiksi yksinkertaisen ja monimutkaisen käyttötilanteen. Testeissä näkyvät botin vastaukset, analyysi onnistumisista ja kehittämiskohteista. |
| **Heikko, 1–2 p** | Testejä on vain yksi tai ne ovat lähes samanlaisia. Testidokumentaatio on epäselvä tai analyysi puuttuu. |

#### Testauspohja opiskelijoille

| Testi | Käyttäjän syöte | Odotettu toiminta | Botin todellinen vastaus | Johtopäätös |
| --- | --- | --- | --- | --- |
| **Testi 1** | Yksinkertainen käyttötilanne | Botti kysyy peruskysymykset ja ohjaa käyttäjän alustavaan lopputulokseen. |  |  |
| **Testi 2** | Monimutkainen tai epäselvä käyttötilanne | Botti pyytää tarkennuksia eikä tee liian nopeita oletuksia. |  |  |

---

### 4. Iteraatio ja parantaminen — 8 pistettä

**Mitä arvioidaan?**

- Löysikö opiskelija testien perusteella ongelmia?
- Muuttiko opiskelija järjestelmäpromptia tai kysymyspatteristoa ongelmien perusteella?
- Onko muutokset dokumentoitu?
- Näkyykö työssä **kriittinen ajattelu**?

| Taso | Kuvaus |
| --- | --- |
| **Erittäin hyvä, 8 p** | Opiskelija löytää konkreettisen ongelman, muuttaa promptia tai kysymyksiä, testaa uudelleen ja dokumentoi, paraniko botin toiminta. |
| **Heikko, 1–2 p** | Opiskelija ei havaitse ongelmia, vaikka testaus paljastaisi niitä, tai havaitsee ongelmia mutta ei tee muutoksia. |

**Opettajan muistutus:** Testissä ilmennyt virhe on hyödyllinen havainto. Olennaista on, että opiskelija huomaa, dokumentoi ja korjaa sen.

#### Iteraation dokumentointipohja

| Havaittu ongelma | Mitä muutin? | Miksi muutin? | Miten testasin uudelleen? | Paraniko toiminta? |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

---

### 5. Dokumentaatio ja prosessin selkeys — 8 pistettä

**Mitä arvioidaan?**

- Onko tehtävät 17.1–17.4 dokumentoitu kokonaisuutena?
- Näkyykö prosessi alusta loppuun?
- Onko mukana kuvakaappauksia tai linkki bottiin?
- Näkyykö dokumentaatiossa opiskelijan oma ymmärrys ja ajattelu?

| Taso | Kuvaus |
| --- | --- |
| **Erittäin hyvä, 8 p** | Dokumentaatio on noin 3–4 A4-sivua. Tehtävät 17.1–17.4 ovat selkeästi mukana. Kuvakaappaukset, testit, muutokset ja opittu asia näkyvät. Teksti on opiskelijan omaa, ei pelkkä tekoälyltä kopioitu tuotos. |
| **Heikko, 1–2 p** | Dokumentaatio on alle yhden sivun, tehtävät puuttuvat tai ovat epäselviä, kuvakaappauksia ei ole eikä prosessin ajattelu näy. |

> **Dokumentaatio näyttää ajattelun.** Ilman dokumentaatiota opettaja näkee vain lopputuloksen, ei osaamista, testejä eikä parannuksia.

---

## Yleisiä väärinkäsityksiä ja korjausvinkkejä

### Väärinkäsitys 1: ”Järjestelmäprompti ei ole niin tärkeä.”

**Opiskelija ajattelee:** ”Voin vain kirjoittaa botille, että kysy käyttäjältä, ja se tekee oikein.”

**Korjaava näkökulma:** Kielimalli ei tunne kontekstia ilman ohjeita. Se tarvitsee tiedon siitä, kuka se on, mitä sen pitää tehdä, missä järjestyksessä sen pitää edetä ja mitä se ei saa tehdä. Ilman näitä botti arvaa.

**Opettajan toiminta:** Havainnollista asia kahdella eri promptilla: toinen on epämääräinen ja toinen täsmällinen. Pyydä opiskelijoita vertaamaan tuloksia.

---

### Väärinkäsitys 2: ”Yksi testi riittää.”

**Opiskelija ajattelee:** ”Testasin botin yhdellä käyttötilanteella ja se toimi. Valmista.”

**Korjaava näkökulma:** Yksi testi näyttää vain, että botti toimi yhdessä tilanteessa. Arvioinnissa tarvitaan vähintään kaksi erilaista testiä, jotta nähdään, toimiiko botti myös erilaisella käyttäjällä tai monimutkaisemmassa tilanteessa.

**Opettajan toiminta:** Ohjaa opiskelija tekemään kaksi selvästi erilaista testiskenaariota: yksi yksinkertainen käyttötilanne ja yksi monimutkainen, epäselvä tai puutteellisesti kuvattu tilanne.

---

### Väärinkäsitys 3: ”Jos botti epäonnistuu, työ on huono.”

**Opiskelija ajattelee:** ”Botti unohti käyttäjän vastauksen. Olen epäonnistunut.”

**Korjaava näkökulma:** Testissä löytynyt ongelma on hyödyllinen havainto. Se kertoo, mitä pitää parantaa. Hyvässä työssä ongelma dokumentoidaan, promptia korjataan ja bottia testataan uudelleen.

**Opettajan toiminta:** Sanoita selkeästi, että testauksessa löytynyt virhe voi parantaa arvosanaa, jos opiskelija osoittaa sen avulla kriittistä ajattelua ja iteraatiota.

---

### Väärinkäsitys 4: ”Dokumentaatio on turhaa.”

**Opiskelija ajattelee:** ”Botti toimii, miksi pitäisi kirjoittaa raporttia?”

**Korjaava näkökulma:** Dokumentaatio osoittaa, mitä opiskelija suunnitteli, testasi, huomasi ja muutti. Arvioinnissa prosessi on yhtä tärkeä kuin valmis botti.

**Opettajan toiminta:** Näytä opiskelijoille dokumentaation minimirakenne: tehtävä 17.1, järjestelmäprompti, testit, iteraatiot, kuvakaappaukset ja yhteenveto opitusta.

---

## Fasilitointiohjeet

### Oppitunnin rakenne

| Vaihe | Aika | Tavoite |
| --- | --- | --- |
| **Johdanto** | 5 min | Kytke aihe opiskelijoiden omaan kokemukseen: mitä tapahtuu, jos uutta asiaa yrittää opetella ilman ohjausta? |
| **Havainnollistava esimerkki** | 15 min | Näytä toimiva apuri-botti ja konkretisoi, mihin opiskelijat pyrkivät. |
| **Ryhmätyö: kysymykset** | 20 min | Ryhmät ideoivat botin ohjaavia kysymyksiä ja huomaavat, ettei ole vain yhtä oikeaa kysymyspatteristoa. |
| **Yhteinen analyysi** | 10 min | Käydään arviointikriteerit läpi ja varmistetaan, että opiskelijat ymmärtävät, mitä heiltä odotetaan. |
| **Itsenäinen työskentely** | 40+ min | Opiskelijat aloittavat tehtävät 17.1–17.4. Opettaja kiertää ja ohjaa. |

### Johdantolause opettajalle

> Kun uutta asiaa yrittää opetella ilman ohjausta, eteneminen on usein hidasta: ei tiedä mistä aloittaa, mitä kysyä tai missä järjestyksessä edetä. Tänään rakennamme botin, jonka tehtävä on auttaa käyttäjää pääsemään eteenpäin oikeiden kysymysten avulla.

---

## Luokkatehtävien ohjeistus

### TT-A: Kysymyspatteriston suunnittelu

**Tavoite:** Opiskelija osaa suunnitella järjestelmällisen kysymysketjun, jonka avulla botti kerää tarvittavat tiedot käyttäjän auttamiseksi.

**Tee näin:**

1. Kirjoita, missä tehtävässä botti auttaa käyttäjää.
2. Jaa kysymykset 4–6 aihealueeseen, esimerkiksi tavoite, lähtötilanne, käyttäjä, vaihtoehdot, rajat ja lopputulos.
3. Kirjoita jokaiseen aihealueeseen 2–4 kysymystä.
4. Valitse lopuksi 15–20 tärkeintä kysymystä.
5. Tarkista, että kysymykset etenevät loogisessa järjestyksessä.

| Aihealue | Kysymykset | Miksi nämä kysymykset ovat tärkeitä? |
| --- | --- | --- |
| **Tavoite** |  |  |
| **Käyttäjä ja lähtötilanne** |  |  |
| **Vaihtoehdot ja valinnat** |  |  |
| **Rajat ja rajaukset** |  |  |
| **Lopputulos ja seuranta** |  |  |

**Aika-arvio:** 20 minuuttia

---

### TT-B: Järjestelmäpromptin kirjoittaminen

**Tavoite:** Opiskelija osaa kirjoittaa apuri-botille järjestelmäpromptin, joka ohjaa botin toimintaa käytännössä.

**Tee näin:**

1. Kirjoita botin identiteetti: kuka botti on?
2. Kirjoita botin tarkoitus: mitä botti auttaa käyttäjää tekemään?
3. Kirjoita botin toimintatapa: mitä se kysyy ensin, miten se etenee ja miten se ohjaa käyttäjää eteenpäin?
4. Kirjoita botin rajaukset: mitä botti ei saa tehdä?
5. Tarkista, että prompti on riittävän tarkka ja käytännössä testattava.

**Prompttipohja:**

Olet [rooli]. Tarkoituksesi on auttaa käyttäjää [tehtävä] kysymällä järjestelmällisiä kysymyksiä.

Aloita kysymällä lyhyt kuvaus käyttäjän lähtötilanteesta. Sen jälkeen kysy tavoite, lähtötaso, vaihtoehdot, rajat ja lopputulos. Kysy yksi aihealue kerrallaan ja tarvittaessa tarkentavia kysymyksiä.

Älä tee tehtävää käyttäjän puolesta. Älä oleta puuttuvia tietoja, vaan kysy tarkennuksia. Ohjaa lopuksi käyttäjä selkeään lopputulokseen.

**Aika-arvio:** 25 minuuttia

---

### TT-C: Botin testaus

**Tavoite:** Opiskelija testaa bottia käytännössä ja huomaa, toimiiko järjestelmäprompti eri tilanteissa.

**Tee näin:**

1. Kirjoita ensimmäinen testiskenaario: yksinkertainen käyttötilanne.
2. Kirjoita toinen testiskenaario: monimutkainen, epäselvä tai laajempi käyttötilanne.
3. Anna molemmat botille ja tallenna vastaukset.
4. Kirjaa, mitä botti kysyi ja oliko kysymysten järjestys järkevä.
5. Kirjaa, mitä botti teki hyvin ja mitä pitää parantaa.

**Aika-arvio:** 20–30 minuuttia

---

### TT-D: Iteraatio ja korjaus

**Tavoite:** Opiskelija parantaa bottia testitulosten perusteella.

**Tee näin:**

1. Valitse testissä havaittu ongelma.
2. Kirjoita, miksi ongelma haittaa botin toimintaa.
3. Muuta järjestelmäpromptia tai kysymyspatteristoa.
4. Testaa botti uudelleen samalla tai samantyyppisellä skenaariolla.
5. Kirjoita, paraniko toiminta.

**Aika-arvio:** 15–20 minuuttia

---

## Yleisiä apukysymyksiä opiskelijoille

### Jos opiskelija ei osaa kirjoittaa järjestelmäpromptia

- Mitä haluat botin tekevän?
- Mikä botin rooli on: mentori, asiantuntija, assistentti vai jokin muu?
- Mitä botin pitää kysyä ensin?
- Mitä botin ei saa tehdä?
- Miten botti kokoaa lopputuloksen?

### Jos opiskelija kokee testauksen vaikeaksi

- Kuvittele kaksi erilaista käyttäjää.
- Ensimmäinen käyttäjä kuvaa hyvin yksinkertaisen tilanteen.
- Toinen käyttäjä kuvaa epäselvän tai monimutkaisen tilanteen.
- Kirjoita ylös, mitä botti kysyy ja tuntuuko se järkevältä.

### Jos opiskelija sanoo, että botti ei toiminut

- Löysit testissä kehittämiskohteen.
- Mikä tarkalleen meni pieleen?
- Mitä järjestelmäpromptista puuttui?
- Miten voisit kirjoittaa ohjeen niin, että botti toimii seuraavalla kerralla paremmin?

### Jos opiskelijalla on liikaa kysymyksiä

- Kaikkia kysymyksiä ei tarvitse kysyä heti.
- Valitse 15–20 tärkeintä kysymystä.
- Jaa kysymykset aihealueisiin.
- Anna botille ohje kysyä tarkentavia kysymyksiä vain tarvittaessa.

---

## Eriyttäminen

### Haastavampi versio opiskelijoille, jotka etenevät nopeasti

- Lisää kysymyksiä aiheen sudenkuopista, eri käyttäjäryhmistä, poikkeustilanteista ja tarkennuksista.
- Suunnittele bottiin eri syvyystasot: nopea ohjaus, tarkempi ohjaus ja erittäin yksityiskohtainen ohjaus.
- Lisää botille monikielinen tuki, esimerkiksi suomi ja englanti.
- Lisää testiskenaario, jossa käyttäjä antaa ristiriitaisia tietoja ja botin pitää pyytää tarkennusta.

### Yksinkertaistettu versio opiskelijoille, jotka tarvitsevat tukea

- Anna valmis 15 kysymyksen lista ja pyydä opiskelijaa valitsemaan niistä tärkeimmät.
- Anna puolivalmis järjestelmäprompti, jonka opiskelija täydentää.
- Anna valmiit testiskenaariot, jotka opiskelija ajaa botilla.
- Vähennä vaatimusta niin, että opiskelija tekee tehtävät 17.1–17.3 ja dokumentoi ne selkeästi.

**Opettajan huomio:** Yksinkertaistettu versio ei tarkoita, että opiskelija vapautetaan ajattelusta. Se tarkoittaa, että hän saa enemmän rakennetta, jotta hän voi osoittaa ydintaidon: botin tarkoituksen, kysymysten, promptin ja testauksen ymmärtämisen.

---

## Aika ja aikataulutus

Oppitunnilla 17 painopiste on johdannossa, demossa ja työn aloittamisessa. Suurin osa viimeistelystä voi tapahtua oppitunnin jälkeen ja jatkua oppitunnilla 18.

| Osuus | Aika | Huomio |
| --- | --- | --- |
| Johdanto ja demo | 20 min | Näytä tavoitetaso konkreettisesti. |
| Ryhmätyö ja analyysi | 30 min | Opiskelijat suunnittelevat kysymyksiä ja ymmärtävät arviointikriteerit. |
| Itsenäinen työ | 40+ min | Tehtävät 17.1–17.4 aloitetaan tunnilla ja viimeistellään tarvittaessa kotona. |

---

## Yhteys muihin oppitunteihin

- **Oppitunnit 14–15:** opiskelijat oppivat botin suunnittelusta, tietopohjasta, rajauksista ja testaamisesta.
- **Oppitunti 17:** opiskelijat soveltavat näitä taitoja arvioitavassa apuri-botissa.
- **Oppitunti 18:** opiskelijat viimeistelevät, parantavat ja esittelevät botin.
- **Oppitunnit 19–27:** Agentit-osio rakentuu tämän ajattelun päälle. Apuri-botti toimii pohjana ymmärrykselle siitä, miten agenttimaisempi järjestelmä suunnitellaan.

**Opettajan muistutus:** Tämä oppitunti on silta botin suunnittelusta agenttiajatteluun. Kun opiskelija osaa suunnitella botin tarkoituksen, ohjeet, testit ja iteraation, hänellä on pohja ymmärtää myöhemmin myös agentteja.

---

## Arviointivinkit opettajalle

### Mitä hyvässä työssä näkyy?

- Botin tarkoitus on selkeä ja rajattu.
- Rooli tukee käyttäjän ohjaamista eikä ole pelkkä persoonallisuus.
- Kysymyspatteristo etenee loogisesti.
- Järjestelmäprompti on konkreettinen ja käytännössä testattava.
- Testejä on vähintään kaksi ja ne ovat erilaisia.
- Testien perusteella on tehty muutoksia.
- Dokumentaatio näyttää prosessin, ei vain lopputulosta.

### Heikon työn merkkejä

- Botti on määritelty liian yleisesti: ”auttaa kaikessa”.
- Järjestelmäprompti on hyvin lyhyt tai epämääräinen.
- Kysymykset ovat satunnaisia eivätkä muodosta selkeää ohjaavaa polkua.
- Testaus on tehty vain yhdellä esimerkillä.
- Iteraatiota ei ole tehty.
- Dokumentaatio on liian lyhyt tai siinä ei näy opiskelijan oma ajattelu.

**Opettajan arviointikysymys:** Näkyykö työssä suunnittelijan ajattelu vai vain nopeasti tehty botti? Arvioinnissa painota sitä, miten opiskelija perustelee, testaa ja parantaa ratkaisuaan.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että apuri-botti ei ole vain kysymyslista. Se on suunniteltu työkalu, joka ohjaa käyttäjää kohti parempaa lopputulosta. Hyvä botti kysyy oikeassa järjestyksessä, pyytää tarkennuksia, ohjaa käyttäjää selkeästi ja tunnistaa omat rajansa.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Mistä tiedät, että bottisi todella auttaa käyttäjää pääsemään tavoitteeseensa paremmin eikä vain kysy satunnaisia kysymyksiä?

> **Lopetuslause opettajalle:** Hyvä apuri-botti ei vain keskustele. Se ohjaa käyttäjän ajattelemaan tehtävänsä läpi vaihe vaiheelta.

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **botin minimiversio tai kuivaharjoittelujälki sekä korjauslista**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–10 min | Virittäytyminen | Kytke ydinkysymys tuttuun tilanteeseen ja tarkista lähtötaso. |
| 10–25 min | Ydinkäsite | Mallinna tunnin keskeinen ero yhdellä vastaesimerkillä. |
| 25–65 min | Perustuotos | Oppija kokoaa botin minimiversion tai kuivaharjoittelujäljen ja ajaa yhden testin. Tämä 40 minuutin jakso on itsenäistä tai parin kanssa tehtävää työskentelyä. |
| 65–80 min | Testaus ja purku | Testauta tuotos annetulla tapauksella ja pura yksi onnistuminen sekä yksi korjaus. |
| 80–90 min | Tallennus ja lopputehtävä | Varmista tiedoston nimi, tallennuspaikka ja yhden lauseen johtopäätös. |

### Tukireitti

Oppija käyttää alustariippumatonta järjestelmäprompti–syöte–tulos-runkoa. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis, oppija antaa version toiselle testikäyttäjälle tai vaihtaa testikontekstia. Syventävä työ ei kasvata pakollista ydintuotosta.
