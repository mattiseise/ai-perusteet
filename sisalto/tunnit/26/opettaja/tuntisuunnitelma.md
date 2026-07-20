# Opettajan materiaalit — oppitunti 26: n8n-projektipaja, osa 1

## Osaamistavoitteet

Tämän oppitunnin tavoitteena on siirtyä agenttien teoriasta käytännön rakentamiseen. Opiskelijat tutustuvat **n8n**-työkaluun, ymmärtävät visuaalisen työnkulun perusidean ja suunnittelevat oman agenttinsa ennen varsinaista rakentamista.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, mitä **n8n** on ja miten se eroaa perinteisestä ohjelmoinnista.
- Opiskelija tunnistaa n8n:n keskeiset käsitteet: **solmu**, **trigger**, **webhook** ja **yhteys** eli viiva solmujen välillä.
- Opiskelija ymmärtää, että n8n on yksi ympäristö harnessin toteuttamiseen: tekoälysolmu kutsuu kielimallia, ja ympäröivät solmut, säännöt sekä palvelut huolehtivat muista vastuista.
- Opiskelija käyttää agentin kuutta rakennusosaa kattavuuden tarkistuslistana. Yksi solmu tai sääntö voi kattaa useita kohtia, eikä jokaiselle tarvita omaa solmua.

### Soveltaa

- Opiskelija pystyy rakentamaan yksinkertaisen n8n-työnkulun, jossa on trigger ja 2–3 muuta solmua.
- Opiskelija pystyy suunnittelemaan oman n8n-agenttinsa ja tekemään siitä yksityiskohtaisen suunnitelman.

**Opettajan painotus:** Korosta, että tämän oppitunnin tärkein tavoite ei ole rakentaa mahdollisimman monimutkaista työnkulkua, vaan ymmärtää, miten kielimallin ja harnessin vastuut muuttuvat konkreettisiksi solmuiksi, ehdoiksi ja tiedonkuluksi.

---

## Pedagoginen lähestymistapa

### Avaus: koodaamisen demokratisointi

Aloita oppitunti sanomalla opiskelijoille:

> Tähän mennessä olemme puhuneet agentin arkkitehtuurista teoriassa. Nyt rakennamme sitä käytännössä. n8n näyttää kielimallin ja harnessin vastuut konkreettisina solmuina, sääntöinä ja yhteyksinä. Kuusi rakennusosaa auttaa tarkistamaan kattavuuden, mutta ne eivät määrää solmujen määrää.

Tämä auttaa erityisesti niitä opiskelijoita, joille ohjelmointi tuntuu vaikealta tai pelottavalta. Samalla on tärkeää korostaa, että visuaalinen työkalu ei poista suunnittelun ja loogisen ajattelun tarvetta.

### Keskeinen käsite: visuaalinen ohjelmointi

**Vertaus:** Perinteinen ohjelmointi on kuin reseptin kirjoittamista tekstillä. n8n on kuin reseptin rakentamista näkyvistä osista: asetat ainekset eli solmut kankaalle, yhdistät ne viivoilla ja data virtaa niiden läpi vaiheesta toiseen.

**Perinteinen ohjelmointi:**

if (user.message) { ai.think(user.message); return response; }

**n8n:**

[Webhook] → [IF] → [OpenAI] → [Discord]

Näytä opiskelijoille molemmat esimerkit ja selitä, että ne voivat tehdä saman asian eri muodossa. Tekstikoodi ja visuaalinen työnkulku kuvaavat molemmat logiikkaa.

**Esimerkki opetukseen**

Pyydä opiskelijoita katsomaan n8n-työnkulkua kuin karttaa. Jokainen solmu vastaa kysymykseen: “Mitä tapahtuu seuraavaksi?” Jokainen viiva vastaa kysymykseen: “Mihin data kulkee tämän jälkeen?”

---

## n8n:n solmujen kolme pääkategoriaa

Opeta n8n:n solmujen pääkategoriat lyhyesti noin 10 minuutissa. Tavoitteena ei ole käydä läpi kaikkia mahdollisia solmuja, vaan antaa opiskelijoille käsitteellinen malli, jonka avulla he osaavat lukea työnkulkuja.

### 1. Triggerit — mistä työnkulku alkaa?

- **Manual trigger:** työnkulku käynnistetään käsin.
- **Schedule trigger:** työnkulku käynnistyy ajastetusti.
- **Webhook:** ulkoinen palvelu lähettää viestin tai datan, joka käynnistää työnkulun.

### 2. Päätössolmut — miten työnkulku haarautuu?

- **IF-solmu:** tarkistaa ehdon ja ohjaa työnkulun eri suuntaan sen perusteella.
- **Switch-solmu:** ohjaa työnkulun useampaan eri haaraan tilanteen mukaan.

### 3. Toimintasolmut — mitä työnkulku tekee?

- **HTTP Request:** kutsuu API:a tai ulkoista palvelua.
- **OpenAI-solmu:** käyttää tekoälyä tekstin, analyysin tai päätöksen tuottamiseen.
- **Discord, Slack tai Email:** lähettää viestin.
- **Google Sheets:** lukee tai kirjoittaa dataa taulukkoon.

| Solmutyyppi | Mitä se tekee? | Esimerkki |
| --- | --- | --- |
| **Trigger** | Käynnistää työnkulun. | Webhook vastaanottaa lomakevastauksen. |
| **Päätössolmu** | Valitsee suunnan ehdon perusteella. | IF-solmu tarkistaa, onko viesti kiireellinen. |
| **Toimintasolmu** | Tekee varsinaisen toiminnon. | OpenAI-solmu laatii vastausehdotuksen. |

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: “n8n on yksinkertainen, joten logiikkakin on yksinkertaista.”

**Korjaava näkökulma:** n8n on helppokäyttöinen käyttöliittymän tasolla, mutta sen taustalla on silti vaativia käsitteitä, kuten datanmuunnos, turvakerrokset, muistin hallinta, hyväksyntäportit ja virheiden käsittely.

Kerro opiskelijoille:

> Vaikka rajapinta näyttää yksinkertaiselta, logiikka voi olla vaativaa. Jokainen solmu tekee jotain merkityksellistä, ja jokaisen solmun paikka työnkulussa pitää perustella.

### Väärinkäsitys 2: “Suunnitelma on turha — aloitetaan vain rakentaminen.”

**Korjaava näkökulma:** Hyvä työnkulku suunnitellaan ennen rakentamista. Jos opiskelija aloittaa suoraan rakentamisen, hän päätyy helposti korjaamaan samaa ongelmaa monta kertaa.

**Opettajan huomio:** Pysäytä liian nopeasti rakentamaan lähtevät opiskelijat ystävällisesti mutta selkeästi. Pyydä heitä kirjoittamaan ensin työnkulun vaiheet numeroituna ja merkitsemään, missä kohtaa tarvitaan syöte, päätös, toiminto, turvakerros ja palaute.

Voit sanoa:

> Hyvä insinööri piirtää suunnitelman ennen rakentamista. Huono insinööri rakentaa ensin ja yrittää sitten selvittää, miksi kokonaisuus ei toimi.

### Väärinkäsitys 3: “n8n voi tehdä mitä tahansa.”

**Korjaava näkökulma:** n8n on integraatioalusta. Se voi tehdä sitä, mitä sen solmut, integraatiot ja API-yhteydet mahdollistavat. Jos tarvitaan hyvin erikoistunutta logiikkaa, voidaan tarvita **Code node** -solmua, joka vaatii ohjelmointitaitoa.

| n8n voi usein tehdä | n8n ei välttämättä voi tehdä ilman lisätyötä |
| --- | --- |
| HTTP-kutsut ja API-yhteydet | Hyvin erikoistuneet tai uudet palvelut ilman valmista integraatiota |
| Tekoälypalveluiden käyttö | Monimutkainen räätälöity logiikka ilman koodisolmua |
| Tietokantojen, viestien ja sähköpostien käsittely | Palvelut, joihin ei ole rajapintaa tai käyttöoikeutta |

### Väärinkäsitys 4: “Turvakerros on valinnainen.”

**Korjaava näkökulma:** Turvakerros on pakollinen osa agentin rakentamista. Jos agentti voi lähettää viestejä, muuttaa tietoja tai kutsua ulkoisia palveluita, sen toimintaa pitää rajoittaa ja valvoa.

**Esimerkki opetukseen**

Jos agentti voi lähettää sähköpostia ilman tarkistusta, se voi vahingossa lähettää arkaluonteisia tietoja väärälle vastaanottajalle. Turvakerros voi estää tämän esimerkiksi tarkistamalla vastaanottajan, sisällön ja riskitason ennen lähetystä.

### Väärinkäsitys 5: ”Kuusi rakennusosaa tarkoittaa kuutta erillistä solmua.”

**Korjaava näkökulma:** Kuusi rakennusosaa toimii suunnittelun tarkistuslistana, ei pakollisena teknisenä topologiana. Yksi solmu, sääntö tai ulkoinen palvelu voi hoitaa useita vastuita, ja jokin vastuu voi jakautua useaan vaiheeseen. Opiskelijan tehtävä on perustella vastuunjako.

---

## Luokkatehtävien ohjeistus

### TT-A: Kokeile ja dokumentoi

**Tavoite:** Opiskelija rakentaa yksinkertaisen työnkulun ja ymmärtää, miten data virtaa solmujen läpi.

**Ohje opiskelijalle:**

1. Rakenna yksinkertainen työnkulku, jossa on trigger ja 2–3 solmua.
2. Yhdistä solmut viivoilla oikeassa järjestyksessä.
3. Suorita työnkulku tai yksittäiset solmut testinä.
4. Avaa solmun **Output**-näkymä ja tarkastele, mitä dataa solmu palauttaa.
5. Kirjoita lyhyt dokumentaatio: mitä työnkulku tekee, mitä dataa liikkuu ja missä vaiheessa data muuttuu.

**Yleisiä ongelmia ja ratkaisuja:**

| Ongelma | Opettajan ohjaava ratkaisu |
| --- | --- |
| Opiskelija ei yhdistä solmuja oikein viivalla. | Näytä, miten viiva vedetään solmun outputista seuraavan solmun inputiin. |
| Opiskelija painaa Execute väärässä solmussa. | Selitä, että Execute testaa työnkulkua kyseiseen solmuun asti tai kyseisen solmun toimintaa. |
| Opiskelija ei näe, miten data muuttuu. | Avaa solmun Output-välilehti ja pyydä opiskelijaa vertaamaan syötettä ja tulosta. |

**Aika-arvio:** 15–20 minuuttia

---

### TT-B: Arkkitehti — suunnittele

**Tavoite:** Opiskelija tekee realistisen projektisuunnitelman, joka voidaan toteuttaa n8n:ssä.

**Ohje opiskelijalle:**

1. Valitse agenttisi käyttötarkoitus.
2. Kirjoita työnkulun vaiheet numeroituna järjestyksessä.
3. Merkitse jokaiseen vaiheeseen, mitä solmua tai solmutyyppiä siinä tarvitaan.
4. Merkitse, missä kohtaa tarvitaan turvakerros tai ihmisen hyväksyntä.
5. Tarkista, että työnkulku ei ole liian laaja ensimmäiseksi projektiksi.

**Vinkki arviointiin:** Hyvä suunnitelma on toteutettavissa. Se ei ole vain idea, vaan siinä näkyvät vaiheet, solmut, datan kulku, turvakerros ja palaute.

**Yleisiä ongelmia ja ratkaisuja:**

| Ongelma | Opettajan ohjaava ratkaisu |
| --- | --- |
| Suunnitelma on liian monimutkainen ensimmäiseksi projektiksi. | Suosittele Taso 1 -lähtökohtaa: yksi syöte, yksi päätös, yksi toiminto ja yksi palautevaihe. |
| Vaiheiden riippuvuudet ovat epäselvät. | Pyydä opiskelijaa kirjoittamaan vaiheet numeroituna ja tarkistamaan, syntyykö jokaisessa vaiheessa tieto, jota seuraava vaihe tarvitsee. |
| Hyväksyntäportit puuttuvat. | Kysy: “Missä kohtaa ihmisen pitää hyväksyä päätös ennen kuin agentti toimii?” |

**Aika-arvio:** 20–25 minuuttia

---

### TT-C: Punainen tiimi

**Tavoite:** Opiskelija oppii arvioimaan suunnitelmaa kriittisesti ja löytämään ongelmia ennen rakentamista.

**Opettajan rooli:** Varmista, että tiimityö on rakentavaa, ei henkilökohtaista tai loukkaavaa.

> Punainen tiimi etsii ongelmia suunnitelmasta, ei ihmisestä. Palautteen tarkoitus on parantaa projektia.

**Ohje opiskelijalle:**

1. Vaihtakaa suunnitelma toisen ryhmän kanssa.
2. Etsikää suunnitelmasta mahdollisia ongelmia.
3. Kirjoittakaa vähintään kolme konkreettista riskiä tai epäselvyyttä.
4. Ehdottakaa jokaiseen ongelmaan parannus.

**Punaisen tiimin tarkistuskysymyksiä:**

- Mitä voisi mennä pieleen tässä työnkulussa?
- Onko jokin solmu liian laajoilla oikeuksilla?
- Puuttuuko hyväksyntäportti?
- Onko datan kulku selkeä?
- Mitä tapahtuu, jos tekoäly antaa väärän vastauksen?
- Miten virhe huomataan ja korjataan?

**Aika-arvio:** 15–20 minuuttia

---

### TT-D: Keskustele ja perustele

**Tavoite:** Opiskelija erottaa kielimallin ja harnessin vastuut ja käyttää kuutta rakennusosaa työnkulun kattavuuden tarkistamiseen.

**Ohje opiskelijalle:**

1. Kuvaa, mikä vastuu kuuluu kielimallille ja mikä harnessille.
2. Tarkista kuuden rakennusosan avulla, että olennaiset vastuut näkyvät suunnitelmassa.
3. Perustele, jos yksi solmu, sääntö tai palvelu kattaa useita kohtia tai jokin kohta jätetään pois.

| Tarkistuslistan kohta | Mahdollinen n8n-vastine | Miten vastuu toteutuu? |
| --- | --- | --- |
| **Syötekäsittelijä** | Webhook tai lomakesolmu | Vastaanottaa käyttäjän viestin tai datan. |
| **Päättelijä** | OpenAI-solmu tai IF-solmu | Tulkitsee tilanteen tai tekee päätöksen. |
| **Työkalut** | HTTP Request, Email, Discord, Google Sheets | Tekee toiminnon tai kutsuu ulkoista palvelua. |
| **Muisti** | Tietokanta, Sheets tai aiempi loki | Säilyttää ja hakee aiempaa tietoa. |
| **Turvakerros** | IF-solmu, hyväksyntäportti tai validointivaihe | Estää vaaralliset tai epävarmat toiminnot. |
| **Palaute** | Lokitus, Sheets, palauteviesti tai seurantavaihe | Tallentaa tulokset ja mahdollistaa toiminnan parantamisen. |

**Aika-arvio:** 15–20 minuuttia

---

## Tuntiesityksen rakenne: 45 minuuttia

1. **Avaus ja motivaatio noin 3 minuuttia**

   Kerro opiskelijoille: “Olemme oppineet agentin teoriaa. Nyt rakennamme sen visuaalisesti n8n:ssä.”
2. **n8n-tutoriaali noin 12 minuuttia**

   - Avaa n8n.
   - Näytä trigger, HTTP Request, IF-solmu ja viestin lähetyssolmu.
   - Korosta: “Jokainen solmu tekee yhden asian. Data virtaa solmujen läpi.”
3. **Arkkitehtuurin selitys noin 10 minuuttia**

   - Näytä, miten kielimallin ja harnessin vastuut jakautuvat ja miten kaikki kuusi rakennusosaa tulevat kokonaisuutena katetuiksi.
   - Piirrä taululle työnkulku: `Trigger → Validointi → Päättely → Turva → Toiminta → Palaute`
4. **Opiskelijoiden työskentely noin 15 minuuttia**

   - TT-A: opiskelijat rakentavat yksinkertaisen työnkulun.
   - TT-B ja TT-D: opiskelijat suunnittelevat oman projektinsa ja perustelevat solmuvalinnat.
   - TT-C: opiskelijat arvioivat toisen ryhmän suunnitelmaa, jos aikaa jää.
5. **Yhteenveto ja seuraavan tunnin esittely noin 5 minuuttia**

   Kerro opiskelijoille: “Seuraavalla tunnilla rakennamme niitä projekteja, jotka suunnittelitte tänään.”

---

## Yhteys oppituntiin 27

Oppitunti 27 on rakentamisen, testaamisen ja dokumentoinnin tunti. Varmista, että opiskelijat palauttavat suunnitelmansa ennen seuraavaa oppituntia, jotta:

1. voit arvioida, onko suunnitelma realistinen,
2. voit antaa palautetta parannuksista,
3. opiskelijat voivat aloittaa rakentamisen ilman turhia viivästyksiä.

**Opettajan tarkistuskysymys:** Jos opiskelijan suunnitelma kuulostaa liian laajalta, kysy: “Mikä tästä olisi pienin toimiva versio?” Tämä auttaa rajaamaan projektin toteutettavaksi.

---

## Materiaalit, jotka opettajalla pitää olla valmiina

- n8n-instanssi, joko paikallinen tai pilvipalvelu
- valmis esittelyprojekti n8n:ssä, esimerkiksi yksinkertainen FAQ-botti
- projektimallit tasoille 1, 2 ja 3 tekstinä tai näytöllä
- taulukko, jossa kuvataan kielimallin ja harnessin vastuut sekä kuuden rakennusosan kattavuus ilman yksi yhteen -solmupakkoa
- punaisen tiimin palautelomake printattuna tai digitaalisesti jaettuna
- varasuunnitelma teknisten ongelmien varalle, esimerkiksi kuvakaappaukset työnkulusta

---

## Opettajan vihjeet

### Jos opiskelijat etenevät liian nopeasti

Anna heille lisähaaste:

- Rakenna työnkulku, joka integroituu kahteen ulkoiseen palveluun.
- Lisää turvakerros, joka estää tietynlaisia syötteitä.
- Lisää lokitus, joka tallentaa, mitä agentti teki ja milloin.
- Lisää hyväksyntäportti ennen riskialtista toimintoa.

### Jos opiskelijat etenevät liian hitaasti

Rajaa tehtävää:

- Anna valmis työnkulkupohja, jota opiskelijat muokkaavat.
- Anna TT-B suunnittelumallina, jossa osa kohdista on valmiiksi täytetty.
- Siirrä TT-C eli punaisen tiimin arviointi seuraavalle oppitunnille.
- Keskity yhteen toimivaan työnkulkuun monimutkaisen projektin sijaan.

### Jos n8n ei toimi

Käytä varasuunnitelmaa:

- Näytä valmiita kuvakaappauksia n8n-työnkulusta.
- Piirrä työnkulku taululle solmuina ja nuolina.
- Käy läpi, mitä dataa kukin solmu saisi ja palauttaisi.
- Käsittele tekninen ongelma oppimistilanteena: mitä kokeiltiin, mikä epäonnistui ja mitä tehtäisiin seuraavaksi?

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että n8n tekee agentin arkkitehtuurista näkyvän. Jokainen solmu on osa järjestelmää, ja jokaisella yhteydellä on merkitys. Hyvä työnkulku ei synny sattumalta, vaan se suunnitellaan, rajataan, testataan ja parannetaan.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Mikä oman agenttisi pienin toimiva versio olisi? Mitkä solmut siihen tarvitaan, ja missä kohdassa tarvitset turvakerroksen?

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **minimiagentti v1 tai alustariippumaton suoritusjälki**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–10 min | Virittäytyminen | Kytke ydinkysymys tuttuun tilanteeseen ja tarkista lähtötaso. |
| 10–25 min | Ydinkäsite | Mallinna tunnin keskeinen ero yhdellä vastaesimerkillä. |
| 25–65 min | Perustuotos | Oppija rakentaa 3–5 solmun minimiagentin tai alustariippumattoman suoritusjäljen. Tämä 40 minuutin jakso on itsenäistä tai parin kanssa tehtävää työskentelyä. |
| 65–80 min | Testaus ja purku | Testauta tuotos annetulla tapauksella ja pura yksi onnistuminen sekä yksi korjaus. |
| 80–90 min | Tallennus ja lopputehtävä | Varmista tiedoston nimi, tallennuspaikka ja yhden lauseen johtopäätös. |

### Tukireitti

Oppija käyttää valmista solmurunkoa ja annettuja syötteitä. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis, oppija lisää yhden hallitun virhepolun. Syventävä työ ei kasvata pakollista ydintuotosta.
