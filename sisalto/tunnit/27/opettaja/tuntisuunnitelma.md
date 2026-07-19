# Opettajan materiaalit — oppitunti 27: n8n-projektipaja, osa 2

## Osaamistavoitteet

Tämän oppitunnin tavoitteena on viedä n8n-agenttiprojekti suunnitelmasta kohti toimivaa, testattua ja dokumentoitua kokonaisuutta. Oppitunnin painopiste on **asiallisessa työskentelyssä**: rakentamisessa, testaamisessa, dokumentoinnissa, arvioinnissa ja oman työn kriittisessä tarkastelussa.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, miten agenttia testataan **systemaattisesti**.
- Opiskelija tunnistaa kolme testityyppiä: **normaalit tapaukset**, **reunatapaukset** ja **turvallisuustestit**.
- Opiskelija ymmärtää dokumentaation merkityksen ja tunnistaa kolme ydindokumenttia: **README**, **ARCHITECTURE** ja **SAFETY**.

### Soveltaa ja analysoida

- Opiskelija rakentaa toimivan **n8n-agentin**.
- Opiskelija testaa agenttia kattavasti ja dokumentoi testitulokset.
- Opiskelija arvioi kriittisesti omaa työtään ja toisen ryhmän projektia.

### Luoda ja arvioida

- Opiskelija kirjoittaa selkeää ja asiallista dokumentaatiota.
- Opiskelija esittelee projektinsa demona ja perustelee tekemänsä ratkaisut.
- Opiskelija tunnistaa agentin kuusi komponenttia omassa projektissaan.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on vastuullisuus. Projekti ei ole valmis, kun se toimii kerran. Projekti on valmis vasta, kun se on rakennettu, testattu, dokumentoitu ja arvioitu kriittisesti.

---

## Pedagoginen lähestymistapa

### Ydinviesti: vastuullinen käyttäjä rakentaa, testaa ja dokumentoi

Oppitunti 27 käsittelee asiallisen ohjelmistokehityksen prosessia. Opiskelijoiden tulee ymmärtää, että teknisen ratkaisun rakentaminen on vain yksi osa kokonaisuutta.

> **Amatööri rakentaa ja toivoo, että se toimii. Vastuullinen käyttäjä rakentaa, testaa ja dokumentoi.**

Korosta opiskelijoille:

- **Testaaminen** ei ole valinnainen lisä, vaan pakollinen osa agentin rakentamista.
- **Dokumentaatio** tekee projektista ymmärrettävän, ylläpidettävän ja asiallisen.
- **Itsekritiikki** osoittaa syvää ymmärrystä paremmin kuin väite siitä, että kaikki toimii täydellisesti.

### Iteratiivinen kehitys, ei “kaikki kerralla” -rakentaminen

Moni opiskelija yrittää rakentaa koko projektin kerralla ja korjata virheet vasta lopussa. Tämä johtaa usein vaikeaan debuggaamiseen, turhautumiseen ja motivaation laskuun.

**Opettajan huomio:** Ohjaa opiskelijat rakentamaan työnkulku pienissä osissa. Jokainen uusi solmu testataan ennen seuraavan lisäämistä. Näin virheen lähde on helpompi löytää.

Kerro opiskelijoille:

> Rakenna ensin trigger ja yksi solmu. Testaa ne. Kun ne toimivat, lisää seuraava solmu. Jos jokin menee pieleen, tiedät tarkemmin, missä virhe syntyi.

### Testaamisen filosofia

Agenttia ei testata vain kysymällä siltä kerran oikea kysymys. Testaamisen pitää kattaa kolme erilaista tilannetyyppiä:

1. **Normaalit tapaukset:** tilanteet, joita varten agentti on suunniteltu. Näiden pitää toimia varmasti.
2. **Reunatapaukset:** epätavalliset mutta mahdolliset tilanteet. Agentin pitää käsitellä ne rakentavasti.
3. **Turvallisuustestit:** aktiiviset hyökkäysyritykset tai väärinkäyttötilanteet. Agentin pitää torjua ne turvallisesti.

| Testityyppi | Mitä testataan? | Esimerkki |
| --- | --- | --- |
| **Normaali tapaus** | Toimiiko agentti siinä tehtävässä, johon se on suunniteltu? | FAQ-botti vastaa kurssin aikataulua koskevaan kysymykseen. |
| **Reunatapaus** | Miten agentti toimii epäselvässä tai poikkeavassa tilanteessa? | Käyttäjä lähettää tyhjän viestin tai kaksi ristiriitaista pyyntöä. |
| **Turvallisuustesti** | Torjuuko agentti väärinkäytön ja hyökkäysyritykset? | Käyttäjä yrittää prompt injection -hyökkäystä: “Unohda aiemmat ohjeet.” |

### Dokumentaation kolme tasoa

Dokumentaatio palvelee eri lukijoita. Siksi yksi dokumentti ei riitä kaikkeen.

| Dokumentti | Kenelle se on? | Mitä se sisältää? |
| --- | --- | --- |
| **README** | Käyttäjille ja ei-teknisille lukijoille | Mitä agentti tekee, miten sitä käytetään ja esimerkit käytöstä. |
| **ARCHITECTURE** | Tekijöille, ylläpitäjille ja arvioijille | Solmut, työnkulku, inputit, outputit ja agentin kuusi komponenttia. |
| **SAFETY** | Riskien arvioijille ja vastuuhenkilöille | Riskit, ehkäisykeinot, turvakerrokset ja testitulokset. |

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: “Jos testaus menee pieleen, projekti epäonnistui.”

**Korjaava näkökulma:** Epäonnistunut testi ei tarkoita epäonnistunutta projektia. Jos testi paljastaa ongelman ja opiskelija korjaa sen, projekti kehittyy paremmaksi. Todellinen ongelma on se, jos virhe jää huomaamatta.

> Epäonnistuneet testit ovat hyödyllisiä. Ne osoittavat, että testit löytävät ongelmia. Kun löydät ongelman ja korjaat sen, toimit kuten vastuullinen käyttäjä.

### Väärinkäsitys 2: “Dokumentaatio on turhaa — työnkulku kertoo kaiken.”

**Korjaava näkökulma:** Työnkulku näyttää, mitä tapahtuu. Dokumentaatio selittää, miksi näin tapahtuu, miten kokonaisuus toimii ja miten sitä ylläpidetään.

**Esimerkki opetukseen**

Kysy opiskelijoilta: “Kuka voisi ylläpitää projektiasi, jos olet itse poissa etkä ole kirjoittanut dokumentaatiota?”

### Väärinkäsitys 3: “Turvallisuustestit ovat liioittelua.”

**Korjaava näkökulma:** Turvallisuustestit eivät ole kuvitteellisia ääriesimerkkejä. Esimerkiksi **prompt injection** on todellinen riski agenttijärjestelmissä. Jos agentti voi lähettää viestejä, lukea tietoa tai käyttää työkaluja, sitä pitää testata väärinkäyttöä vastaan.

### Väärinkäsitys 4: “Oma projektini on liian pieni dokumentointiin.”

**Korjaava näkökulma:** Myös pieni projekti tarvitsee dokumentaation. Dokumentaatio auttaa opiskelijaa itseään muistamaan myöhemmin, mitä hän teki ja miksi.

---

## Luokkatehtävien ohjeistus

### TT-A: Testaaminen

**Tavoite:** Opiskelija testaa agenttia systemaattisesti ja dokumentoi tulokset.

**Tehtävä:** Opiskelijan tulee tehdä vähintään 9 testiä:

- **3 normaalia testiä**
- **3 reunatapaustestiä**
- **3 turvallisuustestiä**

| Testi | Syöte | Odotettu tulos | Todellinen tulos | Hyväksytty vai korjattava? |
| --- | --- | --- | --- | --- |
| Normaali tapaus |  |  |  |  |
| Reunatapaus |  |  |  |  |
| Turvallisuustesti |  |  |  |  |

**Yleisiä ongelmia ja opettajan ratkaisuja:**

| Ongelma | Opettajan ohjaava ratkaisu |
| --- | --- |
| Opiskelija testaa vain muutaman kerran ja sanoo projektin olevan valmis. | Vaadi vähintään 9 dokumentoitua testiä ja 2 uudelleentestiä. |
| Testaus on satunnaista eikä sitä kirjata. | Vaadi testausraportti, johon jokainen testi kirjataan. |
| Turvallisuustestit puuttuvat tai ovat liian pehmeitä. | Näytä konkreettisia hyökkäysyrityksiä, kuten prompt injection ja piilotetut ohjeet. |
| Opiskelija ei korjaa epäonnistuneita testejä. | Muistuta: epäonnistunut testi kertoo, mitä pitää korjata ennen demoa. |

**Aika-arvio:** 30–45 minuuttia

---

### TT-B: Dokumentaatio

**Tavoite:** Opiskelija kirjoittaa asiallista dokumentaatiota.

Opiskelijan tulee tuottaa kolme dokumentaation osaa:

1. **README:** mitä agentti tekee ja miten sitä käytetään.
2. **ARCHITECTURE:** miten agentti on rakennettu ja mitä kukin solmu tekee.
3. **SAFETY:** mitä riskejä agentissa on ja miten ne on huomioitu.

#### README — käyttäjälle

- Mikä agentti on?
- Mihin ongelmaan se auttaa?
- Miten sitä käytetään?
- Mitä se ei tee?
- Anna 1–2 esimerkkikäyttötilannetta.

#### ARCHITECTURE — ylläpitäjälle

| Solmu | Tehtävä | Input | Output | Agentin komponentti |
| --- | --- | --- | --- | --- |
| [Solmun nimi] | [Mitä solmu tekee?] | [Mitä dataa solmu saa?] | [Mitä dataa solmu palauttaa?] | [Syötekäsittelijä / päättelijä / työkalu / muisti / turvakerros / palaute] |

#### SAFETY — riskien arviointiin

| Riski | Mitä voi tapahtua? | Miten riskiä vähennetään? | Miten testattiin? |
| --- | --- | --- | --- |
| Prompt injection | Agentti voi yrittää noudattaa käyttäjän haitallista ohjetta. | Syötteen validointi, rajaukset ja turvakerros. | Testattiin hyökkäysviesteillä. |

**Yleisiä ongelmia ja opettajan ratkaisuja:**

- **README on liian tekninen:** muistuta, että README on myös ei-tekniselle lukijalle. Pyydä yksinkertaistamaan kieltä.
- **ARCHITECTURE puuttuu tai on liian suppea:** vaadi taulukko, jossa jokaiselle solmulle on tehtävä, input, output ja agentin komponentti.
- **SAFETY on pelkkä lista:** pyydä lisäämään “Mitä tapahtuu, jos…” -analyysi ja jokaiselle riskille ehkäisykeino.
- **Kuuden komponentin linkitys puuttuu:** vaadi, että opiskelija nimeää, mikä solmu toimii syötekäsittelijänä, päättelijänä, työkaluna, muistina, turvakerroksena ja palautteena.

**Aika-arvio:** 45–60 minuuttia

---

### TT-C: Punainen tiimi

**Tavoite:** Opiskelija testaa ja arvioi toisen projektia kriittisesti mutta rakentavasti.

**Opettajan painotus:** Punainen tiimi ei arvostele ihmistä, vaan etsii järjestelmän heikkoja kohtia. Palautteen tarkoitus on tehdä projektista parempi ja turvallisempi.

**Punaisen tiimin tehtävä:**

1. Käyttäkää toisen ryhmän agenttia tai lukekaa sen dokumentaatio.
2. Testatkaa agenttia normaaleilla, poikkeavilla ja turvallisuutta haastavilla syötteillä.
3. Kirjatkaa vähintään kolme konkreettista havaintoa.
4. Antakaa jokaiselle havainnolle parannusehdotus.

**Tarkistuslista punaiselle tiimille:**

- Testattiinko vähintään yksi normaali käyttötapaus?
- Testattiinko vähintään yksi reunatapaus?
- Testattiinko vähintään yksi prompt injection -yritys?
- Tarkistettiinko, paljastaako agentti tietoja, joita sen ei pitäisi paljastaa?
- Tarkistettiinko, pysähtyykö agentti hyväksyntäporttiin riskitilanteessa?
- Tarkistettiinko, onko dokumentaatio riittävää?

**Aika-arvio:** 30–40 minuuttia

---

### TT-D: Demo ja itsekritiikki

**Tavoite:** Opiskelija esittelee projektinsa selkeästi ja arvioi sitä kriittisesti.

**Demon kesto:** 3–5 minuuttia.

**Demon tulee sisältää:**

1. Mitä agentti tekee?
2. Mikä on agentin käyttötapaus?
3. Miten työnkulku etenee n8n:ssä?
4. Missä näkyvät agentin kuusi komponenttia?
5. Miten agenttia testattiin?
6. Mikä ei vielä toimi täydellisesti?
7. Mitä opiskelija tekisi seuraavaksi, jos projekti jatkuisi?

**Opettajan tarkistuskysymys:** Jos opiskelija sanoo “kaikki toimii täydellisesti”, kysy: “Mikä oli vaikein kohta? Mitä riskiä et vielä ehtinyt ratkaista? Mitä parantaisit seuraavassa versiossa?”

**Aika-arvio:** 20–30 minuuttia

---

## Arviointikaavio projektiviikolle

| Kriteeri | Pisteet (yht. 100 p) | Mitä se tarkoittaa? |
| --- | --- | --- |
| **Toimiva n8n-työnkulku** | 25 p | Tekeekö agentti sen, mitä opiskelija lupasi? Toimiiko se ilman kriittisiä virheitä? |
| **Turvallisuus (turvakerros, lokitus, riskien tunnistaminen)** | 20 p | Onko turvakerros paikallaan, lokitetaanko toiminta ja tunnistaako opiskelija projektin riskit? |
| **Dokumentaatio** | 20 p | Voidaanko projektia ymmärtää ilman opiskelijan suullista selitystä? Ovatko README, ARCHITECTURE ja SAFETY mukana? |
| **Testaus** | 20 p | Onko testattu normaaleja tapauksia, reunatapauksia ja turvallisuutta? Onko tulokset dokumentoitu? |
| **Itsearviointi ja demo** | 15 p | Osaako opiskelija esitellä projektin selkeästi, arvioida omaa työtään ja perustella valintansa? |

---

## Tuntiesityksen rakenne: 45 minuuttia

1. **Kertaus: iteratiivinen kehitys noin 3 minuuttia**

   Muistuta opiskelijoita: “Rakentakaa pienissä askelissa. Testatkaa jokaisen askeleen jälkeen.”
2. **Rakentamisen demo noin 5 minuuttia**

   Näytä, miten yksinkertainen prototyyppi kehittyy kohti valmista työnkulkua.
3. **Testaamisen koulutus noin 7 minuuttia**

   Näytä yksi normaali testi, yksi reunatapaus ja yksi turvallisuustesti livenä.
4. **Dokumentaation selitys noin 5 minuuttia**

   Näytä lyhyet esimerkit README-, ARCHITECTURE- ja SAFETY-dokumenteista.
5. **Opiskelijat rakentavat ja testaavat noin 20 minuuttia**

   Kierrä luokassa, anna palautetta ja auta ongelmatilanteissa.
6. **Yhteenveto ja seuraavat askeleet noin 5 minuuttia**

   Kerro opiskelijoille: “Tunnin lopussa esitätte demot. Valmistautukaa näyttämään, miten agentti toimii, miten testasitte sen ja mitä parantaisitte seuraavaksi.”

---

## Materiaalit, jotka opettajalla pitää olla valmiina

- **n8n-instanssi** testikäyttöön
- **Malliagentit** eri tasoille:
  - yksinkertainen: Trigger + HTTP + IF + Discord
  - keskitaso: Webhook + Validointi + OpenAI + Tarkistus + Discord
  - haastava: edelliset sekä Memory ja Logging
- **Testausraportin malli** printattuna tai jaettuna digitaalisesti
- **Dokumentaation mallit**: README, ARCHITECTURE ja SAFETY
- **Punaisen tiimin palautelomake**
- **Arviointikaavio**

---

## Opettajan vihjeet

### Jos opiskelijat haluavat rakentaa liian nopeasti

Pysäytä eteneminen hetkeksi ja pyydä heitä tarkistamaan suunnitelma:

- Mikä on pienin toimiva versio?
- Mikä solmu lisätään seuraavaksi?
- Miten testaatte sen ennen seuraavaa solmua?

### Jos testaaminen jää tekemättä

Aseta testaus pakolliseksi välivaiheeksi.

> Ei demoa ilman testiraporttia.

### Jos dokumentaatio unohtuu

Muistuta opiskelijoita:

> Ilman dokumentaatiota projekti ei ole valmis.

### Jos kriittinen ajattelu puuttuu

Kysy opiskelijoilta:

- Miksi valitsit tämän ratkaisun?
- Mitä olisit voinut tehdä toisin?
- Mitä projektista vielä puuttuu?
- Mikä on suurin riski?

### Jos aika loppuu kesken

Korosta laatua määrän sijaan:

> Pienempi, hyvin testattu ja dokumentoitu projekti on parempi kuin suurempi puolivalmis työ.

---

## Eriyttäminen ja tuen tarpeet arviointitehtävässä

### Suorituspolut

Opiskelijat voivat valita kahdesta testauspolusta:

- **Polku A: ohjattu testaus** — opiskelija seuraa valmista testauspohjaa ja täyttää jokaisen kohdan.
- **Polku B: tutkiva testaus** — opiskelija suunnittelee itse testit ja perustelee, miksi ne ovat tärkeitä.

Molemmat polut arvioidaan samoilla kriteereillä. Polku A tukee opiskelijaa, joka tarvitsee selkeän rakenteen. Polku B sopii opiskelijalle, joka pystyy itsenäisempään analyysiin.

### Tuen kohdat agentit-osiossa

| Oppitunti | Kriittinen kohta | Merkki tuen tarpeesta | Mitä opettaja tekee? |
| --- | --- | --- | --- |
| 19 | Agentin käsite | Opiskelija sekoittaa agentin ja chatbotin. | Palaa konkreettiseen esimerkkiin: “Chatbot vastaa. Agentti tekee.” |
| 21 | Vektoritietokanta | Opiskelija ei ymmärrä, miksi se on tärkeä. | Käytä vertausta: “Se on kuin haku, joka ymmärtää mitä tarkoitat, ei vain mitä kirjoitat.” |
| 23 | ReAct ja suunnittelumallit | Opiskelija kadottaa punaisen langan. | Piirrä yksinkertainen kaavio: “Ajattele → Tee → Tarkista → Toista.” |
| 26 | n8n:n aloittaminen | Opiskelija jähmettyy tyhjän työtilan edessä. | Ohjaa Taso 1 -projektiin, esimerkiksi FAQ-bottiin, ja anna valmis aloitusrakenne. |
| 27 | Dokumentaatio | Opiskelija ei tiedä, mitä kirjoittaa. | Näytä ARCHITECTURE-pohja ja sano: “Täytä tämä solmu kerrallaan.” |

### LLM-resistenssin varmistaminen arviointitehtävässä

- n8n-projekti on luonnostaan osittain **LLM-resistentti**, koska opiskelija rakentaa visuaalisen työnkulun, testaa sen ja dokumentoi oman arkkitehtuurinsa.
- **Vertaisarviointi** eli punainen tiimi ja **suullinen demo** paljastavat, ymmärtääkö opiskelija todella rakentamansa agentin.
- **Itsekritiikki** vaatii henkilökohtaista pohdintaa: mitä opiskelija yritti, mikä epäonnistui, mitä hän oppi ja mitä hän tekisi seuraavaksi.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että toimiva agentti ei synny yhdellä onnistuneella ajolla. Asiallinen agenttiprojekti rakennetaan pienissä osissa, testataan monipuolisesti, dokumentoidaan selkeästi ja arvioidaan kriittisesti.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Mikä oman agenttisi tärkein riski on? Miten testasit sen, ja mitä dokumentaatiosi kertoo siitä?

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **agenttipaketti, 9 testiä, 2 uudelleentestiä, dokumentaatio ja demo tai puolustus**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–5 min | Aloitus | Tarkista, että agentin ydintehtävä, testitaulukko ja dokumenttipohja ovat auki. |
| 5–25 min | Viimeistely | Oppija viimeistelee rajatun työnkulun ja varmistaa, että testattava versio on tallennettu. |
| 25–45 min | Testit | Oppija ajaa 9 testiä: normaalit, reunatapaukset ja turvallisuustestit, kolme kutakin. |
| 45–60 min | Korjaus ja uudelleentesti | Oppija korjaa vähintään yhden testissä löytyneen puutteen ja ajaa vähintään kaksi siihen liittyvää uudelleentestiä. |
| 60–75 min | Dokumentointi | Oppija viimeistelee arkkitehtuurin, oikeudet, lokin, testitulokset ja ennen–jälkeen-korjaukset. |
| 75–85 min | Demo tai puolustus | Oppija näyttää ydintehtävän ja perustelee yhden suunnitteluvalinnan sekä yhden turvallisuusrajan. |
| 85–90 min | Paketointi | Oppija nimeää ja tallentaa palautuspaketin sekä tarkistaa, että kaikki vaadittu näyttö avautuu. |

### Tukireitti

Oppija käyttää testitaulukkoa ja dokumenttipohjia samoilla arviointikriteereillä. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis, oppija ajaa lisätestejä vasta ydinnäytön valmistuttua. Syventävä työ ei kasvata pakollista ydintuotosta.
