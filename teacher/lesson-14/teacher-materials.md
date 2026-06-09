# Opettajan materiaalit — oman botin suunnittelu

## Oppitunnin tavoitteet

Tämän tunnin tavoitteena on, että opiskelija ymmärtää, miten hyvin suunniteltu **oma botti** rakennetaan. Oppitunnin ydin on, että botti ei ole vain ChatGPT, jolle annetaan nimi. Hyvä botti on **räätälöity AI-järjestelmä**, jolla on selkeä tarkoitus, rooli, ohjeet ja rajaukset.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, että hyvin suunniteltu botti rakentuu neljästä rakennuspalikasta: **tarkoitus**, **rooli**, **ohjeet** ja **rajaukset**.
- Opiskelija ymmärtää, että **järjestelmäprompti** ohjaa botin toimintaa ja käyttäytymistä.
- Opiskelija ymmärtää, että **ammattilaisuus** ja **persoonallisuus** eivät ole sama asia.
- Opiskelija ymmärtää, että ammattilaisuus tulee botin suunnittelussa ennen persoonallisuutta.

### Soveltaa ja analysoida

- Opiskelija osaa määritellä botille konkreettisen ja rajatun tarkoituksen.
- Opiskelija osaa kirjoittaa botille roolin, joka tukee sen uskottavuutta ja käyttötarkoitusta.
- Opiskelija osaa erottaa botin toimintaohjeet ja rajaukset toisistaan.
- Opiskelija osaa kirjoittaa esimerkki-interaktioita, joilla testataan, toimiiko botin ohjeistus käytännössä.

### Luoda ja arvioida

- Opiskelija osaa kirjoittaa ensimmäisen version oman bottinsa **järjestelmäpromptista**.
- Opiskelija osaa arvioida, onko botin tarkoitus liian yleinen vai riittävän konkreettinen.
- Opiskelija osaa testata botin toimintaa normaalissa, vaikeassa ja epäselvässä tilanteessa.
- Opiskelija ymmärtää, että bottia kehitetään **iteraation** avulla: suunnitellaan, testataan, korjataan ja testataan uudelleen.

**Opettajan painotus:** Tämän tunnin tärkein viesti on, että hyvä botti ei synny sattumalta. Se suunnitellaan samalla tavalla kuin mikä tahansa ammatillinen työkalu: sillä on tarkoitus, käyttäjäryhmä, toimintatapa, osaamisalue ja selkeät rajat.

---

## Pedagoginen lähestymistapa

### Ydinviesti: oma botti on suunniteltu järjestelmä

Opiskelijat voivat ajatella, että oman botin tekeminen tarkoittaa vain sitä, että ChatGPT:lle annetaan nimi ja muutama ohje. Tämän tunnin tehtävä on muuttaa tämä ajattelu. Oma botti on **räätälöity AI-järjestelmä**, joka on suunniteltu tiettyä tarkoitusta, käyttäjää ja tilannetta varten.

> **Hyvä botti ei ole “tekoäly, joka auttaa kaikessa”. Hyvä botti on tarkasti suunniteltu apuri tiettyyn tehtävään.**

Korosta opiskelijoille:

- **Tarkoitus** kertoo, miksi botti on olemassa.
- **Rooli** kertoo, millaisena asiantuntijana botti toimii.
- **Ohjeet** kertovat, miten botti toimii eri tilanteissa.
- **Rajaukset** kertovat, mitä botti ei saa tehdä.
- **Esimerkki-interaktiot** näyttävät, toimiiko suunnitelma käytännössä.

### Neljä rakennuspalikkaa

| Rakennuspalikka | Mitä se tarkoittaa? | Esimerkki |
| --- | --- | --- |
| **Tarkoitus** | Miksi botti on olemassa ja mitä se auttaa käyttäjää tekemään? | ”Auttaa aloittelijoita ymmärtämään Pythonin silmukoita esimerkkien ja harjoitusten avulla.” |
| **Rooli** | Millaisena asiantuntijana tai tukihenkilönä botti toimii? | ”Toimit kärsivällisenä Python-tutorina, joka selittää asiat aloittelijalle selkeästi.” |
| **Ohjeet** | Miten botin pitää vastata ja edetä? | ”Aloita aina lyhyellä selityksellä, anna sitten esimerkki ja lopuksi kysy tarkistuskysymys.” |
| **Rajaukset** | Mitä botti ei saa tehdä? | ”Älä kirjoita opiskelijalle valmista palautettavaa projektia. Ohjaa vaiheittain.” |

**Opettajan huomio:** Alkuperäisessä materiaalissa mainitaan ajoittain kolme rakennuspalikkaa, mutta tunnin ydinsisällössä niitä on neljä: tarkoitus, rooli, ohjeet ja rajaukset. Käytä opetuksessa johdonmukaisesti neljän rakennuspalikan mallia.

---

## Tarkoitus, rooli, ohjeet ja rajaukset käytännössä

### Tarkoitus: liian yleisestä konkreettiseksi

Opiskelijoiden yleisin virhe on kirjoittaa botin tarkoitukseksi jotakin liian laajaa, kuten ”auttaa ihmisiä” tai ”olla hyödyllinen”. Tällainen tarkoitus ei ohjaa botin toimintaa, koska se ei kerro, keitä autetaan, missä asiassa tai milloin botti onnistuu.

| Heikko tarkoitus | Parempi tarkoitus | Miksi parempi? |
| --- | --- | --- |
| ”Botti auttaa opiskelijoita.” | ”Botti auttaa ensimmäisen vuoden IT-opiskelijoita ymmärtämään Pythonin silmukoita vaiheittaisten esimerkkien avulla.” | Käyttäjä, aihe ja toimintatapa ovat selkeitä. |
| ”Botti on IT-apuri.” | ”Botti auttaa käyttäjiä selvittämään yleisiä Windows- ja Wi-Fi-ongelmia turvallisten tarkistusvaiheiden avulla.” | Tarkoitus rajaa tehtävän ja kertoo, miten apu annetaan. |

> **Hyvä tarkoitus vastaa kolmeen kysymykseen:** kuka käyttää bottia, mihin asiaan botti auttaa ja miten onnistuminen näkyy?

### Rooli ja persoonallisuus eivät ole sama asia

Opiskelijat voivat ajatella, että rooli tarkoittaa lähinnä sitä, onko botti hauska, rento tai ystävällinen. Tämä ei riitä. **Rooli** kertoo botin ammatillisesta identiteetistä. **Persoonallisuus** kertoo, millä tavalla botti viestii.

| Käsite | Mitä se tarkoittaa? | Esimerkki |
| --- | --- | --- |
| **Rooli** | Botin osaaminen, näkökulma ja ammatillinen tehtävä. | ”Kokenut Python-tutori aloittelijoille.” |
| **Persoonallisuus** | Tapa, jolla botti viestii käyttäjälle. | ”Ystävällinen, rauhallinen ja kannustava.” |

Korosta opiskelijoille, että ammattilaisuus tulee ensin. Botti voi olla ystävällinen, suora, kannustava tai rauhallinen, mutta sen pitää ennen kaikkea olla pätevä, johdonmukainen ja turvallinen.

### Ohjeet ja rajaukset

Ohjeet ja rajaukset sekoittuvat helposti. Käytä yksinkertaista eroa:

- **Ohjeet** kertovat, mitä botti tekee.
- **Rajaukset** kertovat, mitä botti ei tee.

| Bottityyppi | Ohje | Rajaus |
| --- | --- | --- |
| **Python-tutori** | Aloita peruskäsitteestä ja etene esimerkin kautta harjoitukseen. | Älä kirjoita opiskelijalle valmista palautettavaa tehtävää. |
| **Kahvilan tilausbotti** | Kysy ensin, mitä asiakas haluaa tilata ja onko erityistoiveita. | Älä ota vastaan maksua äläkä lupaa toimitusaikoja, joita kahvila ei voi pitää. |
| **Asiakaspalvelubotti** | Vastaa kohteliaasti ja ohjaa asiakas oikeaan palvelukanavaan. | Älä anna lääketieteellisiä, juridisia tai taloudellisia neuvoja. |

**Opettajan muistutus:** Rajaukset eivät tee botista huonompaa. Ne tekevät siitä turvallisemman, luotettavamman ja ammatillisemman.

---

## Järjestelmäprompti

### Miksi järjestelmäprompti on tärkeä?

**Järjestelmäprompti** on botin toimintaa ohjaava ydinteksti. Se määrittää botin tarkoituksen, roolin, vastaustavan ja rajat. Ilman järjestelmäpromptia botti toimii helposti epätasaisesti: se voi vastata välillä liian laajasti, välillä liian suppeasti, välillä väärällä sävyllä ja välillä tehtävän ulkopuolelle.

> **Järjestelmäprompti on botin sydän. Se kertoo, millainen botti on, mitä se tekee ja missä sen rajat kulkevat.**

### Järjestelmäpromptin perusrakenne

**1. Identiteetti:** Kuka tai mikä botti on?

**2. Tarkoitus:** Mihin tehtävään botti on suunniteltu?

**3. Ohjeet:** Miten botin pitää toimia?

**4. Rajaukset:** Mitä botin ei pidä tehdä?

### Malliesimerkki: Python-tutori

Olet kärsivällinen ja selkeä Python-tutori ensimmäisen vuoden IT-opiskelijoille. Tarkoituksesi on auttaa opiskelijoita ymmärtämään Pythonin peruskäsitteitä, kuten muuttujia, ehtolauseita, silmukoita ja funktioita.

Selitä asiat aina aloittelijalle sopivalla kielellä. Aloita lyhyellä käsitteen selityksellä, anna konkreettinen esimerkki ja kysy lopuksi opiskelijalta tarkistuskysymys. Jos opiskelija tekee virheen, ohjaa häntä vihjeiden avulla äläkä anna heti valmista vastausta.

Älä kirjoita opiskelijalle kokonaisia palautettavia projekteja valmiiksi. Älä väitä olevasi varma asiasta, jos et ole. Jos tehtävä liittyy kurssin arvioitavaan työhön, auta opiskelijaa ymmärtämään periaate, mutta älä tee tehtävää hänen puolestaan.

---

## Esimerkki-interaktiot testausvälineenä

### Miksi esimerkki-interaktiot tarvitaan?

**Esimerkki-interaktio** on lyhyt mallikeskustelu käyttäjän ja botin välillä. Sen tarkoitus on testata, miten botti toimii erilaisissa tilanteissa. Ilman esimerkki-interaktioita opiskelija ei välttämättä huomaa, että botin ohjeistus on liian epämääräinen tai että botti toimii väärin vaikeassa tilanteessa.

Opeta opiskelijoita testaamaan vähintään kolme tilannetta:

- **Normaali tilanne:** käyttäjä kysyy jotakin, johon botin kuuluu vastata.
- **Vaikea tilanne:** käyttäjä pyytää jotakin, johon botin pitää kieltäytyä tai rajata vastaus.
- **Epäselvä tilanne:** käyttäjän pyyntö on niin epäselvä, että botin pitää pyytää tarkennusta.

| Tilanne | Käyttäjän viesti | Mitä botilta odotetaan? |
| --- | --- | --- |
| **Normaali** | ”En ymmärrä, miten for-silmukka toimii.” | Botti selittää käsitteen, antaa esimerkin ja kysyy tarkistuskysymyksen. |
| **Vaikea** | ”Tee koko palautettava Python-projektini valmiiksi.” | Botti kieltäytyy tekemästä tehtävää valmiiksi ja tarjoaa ohjaavaa apua. |
| **Epäselvä** | ”Koodi ei toimi.” | Botti pyytää tarkennusta: koodinpätkän, virheilmoituksen ja tavoitteen. |

> **Esimerkki-interaktiot eivät ole näytelmiä. Ne ovat botin laadunvarmistusta.**

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”Oma botti on vain ChatGPT, jolle annetaan nimi ja muutama ohje.”

**Korjaava näkökulma:** Hyvin suunniteltu botti on paljon enemmän. Sillä on selkeä tarkoitus, rajattu osaamisalue, johdonmukainen käyttäytyminen ja turvalliset rajaukset. Se on räätälöity järjestelmä, ei pelkkä uudelleennimetty ChatGPT.

### Väärinkäsitys 2: ”Rooli tarkoittaa persoonallisuutta, joten botista pitää tehdä hauska.”

**Korjaava näkökulma:** Rooli ja persoonallisuus eivät ole sama asia. Rooli kertoo osaamisen ja tehtävän. Persoonallisuus kertoo viestintätyylin. Hauskuus voi olla hyvä lisä, mutta se ei korvaa ammattitaitoa.

### Väärinkäsitys 3: ”Järjestelmäprompti on liian pitkä tekstisarja, jota en halua kirjoittaa.”

**Korjaava näkökulma:** Järjestelmäprompti on botin suunnitelma. Sen kirjoittamiseen käytetty aika säästää myöhemmin aikaa, koska botti toimii johdonmukaisemmin ja turvallisemmin. Se on sama kuin suunnitelma ennen rakentamista.

### Väärinkäsitys 4: ”Rajaukset ovat negatiivisia.”

**Korjaava näkökulma:** Rajaukset ovat turvallisuusmekanismi. Ne suojaavat käyttäjää vääriltä neuvoilta ja bottia sopimattomilta tehtäviltä. Hyvä rajaus tekee botista vastuullisen.

### Väärinkäsitys 5: ”Esimerkki-interaktiot ovat turhia.”

**Korjaava näkökulma:** Esimerkki-interaktiot näyttävät, toimiiko ohjeistus oikeasti. Niiden avulla huomataan, tarvitseeko järjestelmäpromptia korjata ennen kuin bottia käytetään oikeassa tilanteessa.

---

## Opettajan fasilitointiohjeet

### Ennen lähiosaa

- Valitse yksi konkreettinen bottiesimerkki, kuten **läksyvalmentaja**, **harrastusneuvoja** tai **asiakaspalvelubotti**.
- Testaa neljän rakennuspalikan malli etukäteen valitulla botilla.
- Kirjoita malliksi 3–4 kappaleen järjestelmäprompti.
- Valmistele 2–3 esimerkki-interaktiota: normaali tilanne, vaikea tilanne ja epäselvä tilanne.
- Valmista esimerkki huonosta järjestelmäpromptista ja paremmasta järjestelmäpromptista, jotta opiskelijat näkevät eron.

### Lähiosan rakenne, 90 minuuttia

| Vaihe | Aika | Tavoite |
| --- | --- | --- |
| **Johdanto** | 5 min | Avaa ajatus: oma botti on suunniteltu järjestelmä, ei vain nimetty ChatGPT. |
| **Tehtävä 14.1: rakennuspalikat** | 20 min | Näytä tarkoitus, rooli, ohjeet ja rajaukset live-esimerkin avulla. |
| **Tehtävä 14.2: järjestelmäprompti** | 25 min | Ryhmät kirjoittavat omille boteilleen ensimmäisen järjestelmäpromptin. |
| **Tehtävä 14.3: esimerkki-interaktiot** | 15 min | Opiskelijat testaavat, miten botti toimisi eri tilanteissa. |
| **Vapaa harjoittelu** | 25 min | Opiskelijat jatkavat omien bottien suunnittelua ja saavat ohjausta. |

**Kotitehtävä:** Täydennä oman botin suunnittelu ja järjestelmäprompti seuraavaa tuntia varten.

### Johdantolause opettajalle

> Tänään emme vain nimeä bottia. Suunnittelemme tekoälyjärjestelmän, jolla on tarkoitus, rooli, ohjeet ja rajat. Hyvä botti käyttäytyy johdonmukaisesti, koska joku on suunnitellut sen hyvin.

---

## Luokkatehtävien ohjeistus

### TT-A: Neljä rakennuspalikkaa

**Tavoite:** Opiskelija tunnistaa oman bottinsa tarkoituksen, roolin, ohjeet ja rajaukset.

**Tehtävä:** Opiskelija valitsee botti-idean ja täyttää neljän rakennuspalikan taulukon.

| Rakennuspalikka | Opiskelijan suunnitelma | Tarkistuskysymys |
| --- | --- | --- |
| **Tarkoitus** |  | Onko tarkoitus konkreettinen ja rajattu? |
| **Rooli** |  | Miksi käyttäjä luottaisi tähän bottiin? |
| **Ohjeet** |  | Miten botin pitää toimia toistuvasti? |
| **Rajaukset** |  | Mitä botin ei saa tehdä? |

**Aika-arvio:** 20 minuuttia

---

### TT-B: Järjestelmäpromptin kirjoittaminen

**Tavoite:** Opiskelija osaa muuttaa suunnitelman toimivaksi järjestelmäpromptiksi.

**Tehtävä:** Kirjoita oman bottisi järjestelmäprompti. Käytä pohjana neljää osaa: identiteetti, tarkoitus, ohjeet ja rajaukset.

**Tee näin:**

1. Kirjoita ensimmäinen kappale: kuka botti on ja kenelle se on tarkoitettu.
2. Kirjoita toinen kappale: mitä botti auttaa käyttäjää tekemään.
3. Kirjoita kolmas kappale: miten botin pitää vastata ja ohjata käyttäjää.
4. Kirjoita neljäs kappale: mitä botti ei saa tehdä ja missä tilanteissa sen pitää pyytää tarkennusta tai ohjata eteenpäin.

**Prompttipohja:**

Olet [rooli] käyttäjille, jotka [käyttäjäryhmä]. Tarkoituksesi on auttaa käyttäjiä [konkreettinen tehtävä].

Toimi aina näin: [ohjeet]. Käytä kieltä, joka on [sävy ja taso].

Älä [rajaukset]. Jos käyttäjän pyyntö on epäselvä, kysy tarkentavia kysymyksiä ennen vastaamista.

**Aika-arvio:** 25 minuuttia

---

### TT-C: Esimerkki-interaktioiden kirjoittaminen

**Tavoite:** Opiskelija testaa, miten oma botti käyttäytyisi käytännössä.

**Tehtävä:** Kirjoita kolme esimerkki-interaktiota omalle botillesi: normaali tilanne, vaikea tilanne ja epäselvä tilanne.

| Tilanne | Käyttäjän viesti | Miten botin pitäisi vastata? |
| --- | --- | --- |
| **Normaali** |  |  |
| **Vaikea** |  |  |
| **Epäselvä** |  |  |

**Aika-arvio:** 15 minuuttia

---

## Yleisiä vaikeuksia ja vastaamisen strategiat

| Vaikeus | Miten ohjaat? |
| --- | --- |
| Opiskelija kirjoittaa liian epämääräisen tarkoituksen: ”Botti auttaa ihmisiä.” | Kysy: kuka käyttää bottia, missä asiassa ja mistä tiedämme, että botti onnistui? |
| Opiskelija ei näe roolin arvoa. | Näytä kaksi vastausta: toinen ilman roolia ja toinen roolin kanssa. Kysy, kumpi tuntuu luotettavammalta. |
| Opiskelija sekoittaa ohjeet ja rajaukset. | Toista ero: ohje kertoo, mitä botti tekee. Rajaus kertoo, mitä botti ei tee. |
| Opiskelija ei näe esimerkki-interaktioiden arvoa. | Näytä tilanne, jossa botti toimii väärin, koska sitä ei ole testattu vaikealla käyttäjäviestillä. |
| Opiskelija kokee järjestelmäpromptin liian pitkäksi. | Vertaa sitä arkkitehtuurisuunnitelmaan: hyvin suunniteltu botti toimii paremmin kuin nopeasti kasattu botti. |

---

## Eriyttäminen ja tuki

### Jos opiskelija on jumissa tarkoituksen kirjoittamisessa

Ohjaa opiskelija täyttämään tämä lause:

Botti auttaa [käyttäjäryhmä] tekemään [konkreettinen tehtävä] tavalla [miten botti auttaa].

Esimerkki: ”Botti auttaa ensimmäisen vuoden IT-opiskelijoita ymmärtämään Linux-komentoja lyhyiden selitysten ja harjoitusten avulla.”

### Jos opiskelija ei osaa kirjoittaa ohjeita

Anna opiskelijalle valmiita ohjepohjia, joita hän voi mukauttaa omalle botilleen:

- Aloita aina kysymällä käyttäjän tavoite.
- Selitä asia ensin lyhyesti ja anna sitten esimerkki.
- Älä anna heti valmista vastausta, vaan ohjaa käyttäjää vaiheittain.
- Jos käyttäjän pyyntö on epäselvä, kysy tarkentava kysymys.
- Jos asia ei kuulu botin osaamisalueeseen, sano se selkeästi ja ohjaa oikeaan suuntaan.

### Jos opiskelija ei näe rajausten merkitystä

Käytä esimerkkiä turvallisuudesta. Treenineuvojabotti voi ehdottaa kevyitä alkulämmittelyliikkeitä, mutta sen ei pidä antaa lääketieteellisiä ohjeita kivun hoitoon tai kehottaa jatkamaan harjoittelua loukkaantuneena. Rajaukset suojaavat käyttäjää vääriltä toimilta.

### Jos opiskelija on edellä

- Pyydä häntä kirjoittamaan kaksi versiota järjestelmäpromptista: yksi aloittelijoille ja yksi edistyneille käyttäjille.
- Pyydä häntä lisäämään botille testitilanne, jossa botti joutuu kieltäytymään käyttäjän pyynnöstä.
- Pyydä häntä vertaamaan kahta erilaista roolia ja arvioimaan, miten ne muuttavat botin vastauksia.

---

## Tarkistustehtävät oppimisen varmistamiseen

### 1. Botin tarkoitus

**Kysymys:** Mikä on hyvä botin tarkoitus? Miksi ”olla hyödyllinen” ei ole hyvä vastaus?

**Mitä opettaja etsii:** Opiskelija ymmärtää, että hyvä tarkoitus on konkreettinen ja mitattava. Esimerkiksi ”auttaa opiskelijoita ymmärtämään Python-silmukoita interaktiivisten esimerkkien kautta” on parempi kuin ”olla hyödyllinen”.

### 2. Rooli ja persoonallisuus

**Kysymys:** Mitä eroa on roolilla ja persoonallisuudella?

**Mitä opettaja etsii:** Opiskelija ymmärtää, että rooli kertoo botin tehtävän ja osaamisen, kun taas persoonallisuus kertoo viestintätyylin. Ammattilaisuus tulee ensin, persoonallisuus vasta sen jälkeen.

### 3. Järjestelmäpromptin neljä osaa

**Kysymys:** Mitä järjestelmäpromptin tulee sisältää?

**Mitä opettaja etsii:** Opiskelija nimeää ainakin seuraavat osat: **identiteetti**, **tarkoitus**, **ohjeet** ja **rajaukset**.

### 4. Rajaukset käytännössä

**Kysymys:** Miksi rajaukset ovat tärkeitä? Anna esimerkki.

**Mitä opettaja etsii:** Opiskelija ymmärtää, että rajaukset suojaavat käyttäjää ja bottia. Esimerkki: harrastusneuvojabotti ei anna sijoitusneuvoja, koska se ei ole talousneuvoja.

### 5. Esimerkki-interaktiot

**Kysymys:** Mitä esimerkki-interaktiot näyttävät?

**Mitä opettaja etsii:** Opiskelija ymmärtää, että esimerkki-interaktiot testaavat, toimiiko ohjeistus todellisuudessa ja miten botti käyttäytyy eri tilanteissa.

---

## Oppimisresurssit

1. **Opiskelijan itseopiskelumateriaali:** käytä sitä peruskäsitteiden kertaamiseen ennen lähiosaa.
2. **Esimerkit omista boteista:** analysoikaa hyviä Custom GPT -ratkaisuja ja pohtikaa, mikä niiden tarkoitus, rooli, ohjeet ja rajaukset voisivat olla.
3. **Järjestelmäpromptin esimerkit:** käytä esimerkkeinä läksyvalmentajaa, harrastusneuvojaa ja asiakaspalvelubottia.
4. **Testaus ja iteraatio:** näytä, miten botin toiminta muuttuu, kun järjestelmäpromptia muokataan.
5. **Opiskelijoiden omat botit:** pyydä opiskelijoita esittelemään botti-ideansa ja saamaan vertaispalautetta.

---

## Arviointivinkit

### Mitä hyvässä suorituksessa näkyy?

- Botin tarkoitus on konkreettinen eikä liian yleinen.
- Rooli tukee botin uskottavuutta ja käyttötarkoitusta.
- Ohjeet kertovat selvästi, miten botin pitää toimia.
- Rajaukset suojaavat käyttäjää ja pitävät botin tehtävän rajattuna.
- Järjestelmäprompti on selkeä, johdonmukainen ja käytännössä testattava.
- Esimerkki-interaktiot sisältävät normaalin, vaikean ja epäselvän tilanteen.

### Heikon suorituksen merkkejä

- Botin tarkoitus on liian yleinen: ”auttaa ihmisiä” tai ”olla hyödyllinen”.
- Rooli on pelkkä persoonallisuus: ”hauska botti” ilman asiantuntijuutta.
- Ohjeet ovat epämääräisiä eivätkä ohjaa botin toimintaa.
- Rajaukset puuttuvat kokonaan.
- Järjestelmäprompti on niin lyhyt, ettei se ohjaa bottia johdonmukaisesti.
- Esimerkki-interaktioita ei ole tai ne testaavat vain helppoja tilanteita.

**Opettajan arviointikysymys:** Voisiko toinen opiskelija rakentaa botin tämän suunnitelman perusteella ja saada siitä samanlaisen lopputuloksen?

---

## Oppitunnin rakenne ja merkitys

Tämä oppitunti toimii siltana kohti omien räätälöityjen bottien rakentamista. Opiskelijat näkevät, että hyvä botti ei ole sattuma vaan harkitun suunnittelun tulos.

Oppitunnin lopussa opiskelijoiden pitäisi ymmärtää kolme asiaa:

1. **Hyvä botti alkaa tarkoituksesta.** Jos tarkoitus on epäselvä, koko botti jää epäselväksi.
2. **Järjestelmäprompti on botin sydän.** Se ohjaa botin käyttäytymistä ja rajoja.
3. **Ammattilaisuus vaatii yksityiskohtia.** Mitä tarkemmin botti suunnitellaan, sitä luotettavammin se toimii.

---

## Yhteydet muihin oppitunteihin

- **Olemme jo oppineet:** tekoälyn käyttämistä työparina, kontekstin antamista, promptausta ja tekoälyn vastausten tarkistamista.
- **Nyt opimme:** miten oma botti suunnitellaan tarkoituksen, roolin, ohjeiden ja rajausten avulla.
- **Seuraavaksi:** opiskelijat rakentavat ja testaavat omia bottejaan tämän suunnitelman pohjalta.

**Opettajan muistutus:** Tämän tunnin jälkeen opiskelijan pitäisi osata sanoa: ”Bottini ei vain vastaa kysymyksiin. Se on suunniteltu tiettyyn tarkoitukseen ja toimii selkeiden ohjeiden mukaan.”

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että oman botin rakentaminen alkaa suunnittelusta. Hyvä botti tarvitsee tarkoituksen, roolin, ohjeet ja rajaukset. Vasta niiden jälkeen bottia kannattaa testata ja kehittää eteenpäin.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Jos käyttäjä keskustelee bottisi kanssa ensimmäistä kertaa, mistä hän huomaa, että botti on suunniteltu hyvin eikä vain nimetty uudelleen?

> **Lopetuslause opettajalle:** Hyvä botti ei ole taikuutta. Se on tarkoitus, rooli, ohjeet ja rajat — kirjoitettuna niin selkeästi, että tekoäly osaa toimia niiden mukaan.

---
