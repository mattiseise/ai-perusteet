# Opettajavetoiset tehtävät — oppitunti 26: n8n-projektipaja, osa 1

## Tehtävä 1: n8n-rajapinnan perustutoriaali noin 15 minuuttia

### Tavoite

Tehtävän tavoitteena on, että opiskelijat näkevät käytännössä, miten **n8n-työnkulku** rakentuu. Opiskelijat oppivat tunnistamaan **triggerin**, **solmut**, **yhteydet** ja **datan kulun** solmusta toiseen.

**Opettajan painotus:** Tässä tehtävässä tärkeintä ei ole tehdä vielä valmista agenttia, vaan ymmärtää n8n:n peruslogiikka: työnkulku alkaa triggeristä, etenee solmusta toiseen ja jokainen solmu käsittelee dataa jollakin tavalla.

### Valmistelu

- Avaa **n8n** projektorille tai näytölle niin, että kaikki opiskelijat näkevät sen.
- Voit käyttää n8n:n pilvipalvelua tai paikallista asennusta.
- Varmista etukäteen, että kirjautuminen, uuden työnkulun luominen ja testiajo toimivat.

### Opettajan ohjeistus

#### Vaihe 1: Näytä triggeri

1. Luo uusi työnkulku.
2. Lisää **Manual Trigger** -solmu.
3. Selitä opiskelijoille:

> Tämä on työnkulun aloituskohta. Trigger kertoo, milloin työnkulku käynnistyy. Ilman triggeriä työnkulku ei tiedä, mistä sen pitäisi alkaa.

4. Klikkaa **Execute** ja näytä, mitä tapahtuu.
5. Näytä opiskelijoille, että trigger tuottaa työnkululle aloitusdatan.

#### Vaihe 2: Näytä HTTP Request -solmu

1. Lisää **HTTP Request** -solmu Manual Trigger -solmun jälkeen.
2. Aseta pyynnöksi **GET**.
3. Käytä esimerkkiosoitteena: `https://api.github.com/zen`
4. Klikkaa **Execute** ja näytä vastaus.

Selitä opiskelijoille:

> HTTP Request -solmu kutsuu ulkoista palvelua eli API:a. Se lähettää pyynnön ja saa vastauksen takaisin. Tämä on esimerkki siitä, miten agentti voi käyttää ulkoista työkalua.

Näytä samalla, miten data kulkee solmusta toiseen viivaa pitkin.

#### Vaihe 3: Näytä IF-solmu päätöksentekoa varten

1. Lisää **IF**-solmu HTTP Request -solmun jälkeen.
2. Aseta ehdoksi esimerkiksi: vastaus sisältää sanan `code`.
3. Selitä opiskelijoille:

> IF-solmu tekee päätöksen ehdon perusteella. Se voi ohjata työnkulun eri suuntaan sen mukaan, täyttyykö ehto vai ei.

4. Näytä opiskelijoille **true**- ja **false**-haarat.
5. Kysy: “Mitä voisi tapahtua true-haarassa? Entä false-haarassa?”

#### Vaihe 4: Näytä tekstinkäsittely

1. Lisää seuraavaksi tekstin muokkaamiseen sopiva solmu, esimerkiksi **Set**- tai muu tekstinkäsittelysolmu käytössä olevan n8n-version mukaan.
2. Näytä, miten dataa voidaan muokata. Esimerkiksi vastauksen eteen voidaan lisätä selite:

GitHub Zen -vastaus: [API:n palauttama teksti]

Selitä opiskelijoille:

> Jokainen solmu voi muuttaa dataa. Data virtaa putkessa solmusta seuraavaan, ja jokainen vaihe lisää, tarkistaa, muokkaa tai käyttää sitä.

**Esimerkki opetukseen**

Pyydä opiskelijoita seuraamaan jokaisen solmun kohdalla kahta asiaa: mitä dataa solmu saa sisään ja mitä dataa se antaa ulos. Tämä auttaa ymmärtämään työnkulun logiikkaa.

### Opiskelijoiden osallistuminen

- Pyydä opiskelijoita avaamaan omat tietokoneensa ja rakentamaan työnkulku vaihe vaiheelta mukana.
- Pysähdy jokaisen uuden solmun jälkeen ja anna opiskelijoille aikaa testata oma työnkulkunsa.
- Vastaa kysymyksiin livenä ja näytä ratkaisut näytöllä.
- Pyydä opiskelijoita avaamaan jokaisen solmun **Output**-näkymä ja kertomaan, mitä dataa he näkevät.

### Yhteenveto noin 1 minuutti

Kokoa tehtävän lopuksi kolme keskeistä käsitettä:

1. **Trigger** kertoo, mistä työnkulku alkaa.
2. **Solmut** tekevät työnkulun yksittäiset vaiheet.
3. **Data virtaa** solmusta seuraavaan yhteyksiä pitkin.

### Odotettu oppimistulos

- Opiskelijat osaavat luoda yksinkertaisen n8n-työnkulun.
- Opiskelijat ymmärtävät triggerin, solmun ja yhteyden merkityksen.
- Opiskelijat näkevät, miten data muuttuu työnkulun aikana.

---

## Tehtävä 2: Agentin arkkitehtuurin tunnistaminen noin 15 minuuttia

### Tavoite

Tehtävän tavoitteena on yhdistää aiemmilla oppitunneilla opittu **agentin arkkitehtuuri** n8n:n konkreettiseen toteutukseen. Opiskelijat erottavat kielimallin ja harnessin vastuut ja tarkistavat kuuden rakennusosan avulla, ettei suunnitelmasta puutu olennaista.

### Valmistelu

Näytä n8n:ssä yksinkertainen työnkulku, jossa on vähintään 4–5 solmua. Voit käyttää esimerkiksi seuraavaa rakennetta:

Webhook → Validointi IF-solmulla → OpenAI → Tarkistus IF-solmulla → Discord

Vaihtoehtoisesti voit käyttää oppitunnin 26 aineistossa olevaa projektimallia.

### Opettajan ohjeet

Käy ensin läpi, mikä esimerkissä on kielimallin vastuulla ja mikä harnessin vastuulla. Käytä sen jälkeen kuutta rakennusosaa kattavuuden tarkistamiseen. Korosta, että taulukon n8n-vastineet ovat esimerkkejä: yksi solmu, sääntö tai palvelu voi kattaa useita vastuita, ja yksi vastuu voi jakautua useaan vaiheeseen.

| Tarkistuslistan kohta | Mahdollinen n8n-vastine | Miten vastuu voi toteutua? |
| --- | --- | --- |
| **Syötekäsittelijä** | Webhook ja Validointi-IF | Vastaanottaa viestin ulkomaailmasta ja tarkistaa, että syöte on järkevä. |
| **Päättelijä** | OpenAI-solmu | Analysoi viestin, hyödyntää ohjeistusta ja tuottaa päätöksen tai vastauksen. |
| **Työkalujen suorittaja** | Discord, sähköposti tai muu lähetyssolmu | Tekee konkreettisen toiminnon, kuten lähettää viestin. |
| **Muisti** | Google Sheets, tietokanta tai Memory-solmu | Tallentaa tai hakee historiaa, asiakastietoja tai aiempia tapahtumia. |
| **Turvakerros** | IF-solmu päättelyn jälkeen | Tarkistaa ennen toimintaa, onko vastaus turvallinen ja sallittu. |
| **Palautesilmukka** | Lokitus Google Sheetsiin tai muuhun tallennuspaikkaan | Kirjaa tapahtumat, jotta toimintaa voidaan arvioida ja parantaa myöhemmin. |

### Käsittely vastuu kerrallaan

1. **Syötekäsittelijä:** Osoita Webhook-solmua ja ensimmäistä IF-ehtoa.

   Selitä: “Jotain tapahtuu ulkomaailmassa, esimerkiksi viesti saapuu. Syötekäsittelijä vastaanottaa sen ja tarkistaa, että viesti on käsiteltävissä.”
2. **Päättelijä:** Osoita OpenAI-solmua ja sen ohjeistusta.

   Selitä: “Tässä agentti tekee päättelyä. Se analysoi viestin, hyödyntää järjestelmäpromptia ja muodostaa vastauksen tai päätösehdotuksen.”
3. **Työkalujen suorittaja:** Osoita Discord-, sähköposti- tai muuta lähetyssolmua.

   Selitä: “Tässä agentti toimii. Se ei vain ajattele, vaan tekee konkreettisen toimenpiteen.”
4. **Muisti:** Näytä Google Sheets-, tietokanta- tai muu tallennusratkaisu.

   Selitä: “Jos agentin pitää muistaa aiempia tapauksia tai hakea historiaa, se tarvitsee muistia.”
5. **Turvakerros:** Osoita päättelyn jälkeistä IF-solmua.

   Selitä: “Ennen kuin agentti toimii, sen pitää tarkistaa, onko vastaus turvallinen. Sisältääkö se arkaluonteisia tietoja? Tarvitaanko ihmisen hyväksyntä?”
6. **Palautesilmukka:** Näytä lokitusvaihe.

   Selitä: “Jokainen tärkeä toimenpide kannattaa kirjata. Näin voidaan myöhemmin arvioida, mitä agentti teki ja miksi.”

**Opettajan huomio:** Älä anna opiskelijoiden ajatella, että kaikki n8n-työnkulut ovat automaattisesti agentteja tai että jokainen rakennusosa vaatii oman solmun. Agentti syntyy kielimallin ja harnessin kokonaisuudesta. Harness vastaanottaa ja rajaa syötteen, tarjoaa työkalut, ylläpitää tarvittavaa tilaa ja toimeenpanee turvarajat; kielimalli tekee sille annetun tehtävän sisällä tarvittavan arvion.

### Keskustelu

- Mitä kielimalli tekee ja mistä harness vastaa?
- Miten kaikki kuusi rakennusosaa toteutuvat kokonaisuutena, vaikka solmuja olisi vähemmän tai enemmän kuin kuusi?
- Mitä tapahtuisi, jos **turvakerros** puuttuisi?
- Miten agentti eroaa tavallisesta n8n-skriptistä?
- Missä vaiheessa ihminen pitäisi ottaa mukaan?

### Odotettu oppimistulos

- Opiskelijat osaavat erottaa kielimallin ja harnessin vastuut ja käyttää kuutta rakennusosaa kattavuuden tarkistuslistana.
- Opiskelijat ymmärtävät, että agentti ei ole vain solmujen ketju, vaan päätöksiä tekevä ja rajatusti toimiva järjestelmä.
- Opiskelijat osaavat selittää, miksi turvakerros ja palautesilmukka ovat tärkeitä.

---

## Tehtävä 3: Suunnittelutyöpaja — projekti-ideoiden arviointi noin 20 minuuttia

### Tavoite

Tehtävän tavoitteena on, että opiskelijat suunnittelevat realistisen n8n-agentin ennen rakentamista. Opiskelijat arvioivat projektinsa laajuutta, riskejä, hyväksyntäportteja ja solmukaaviota.

**Vinkki arviointiin:** Hyvä suunnitelma on toteutettavissa. Se ei ole vain idea, vaan siinä näkyvät vaiheet, triggeri, solmut, rajaukset, riskit ja hyväksyntäportit.

### Valmistelu

- Jaa opiskelijat pareihin tai 2–3 henkilön pienryhmiin.
- Anna ryhmille kolme projektivaihtoehtoa tai anna heidän valita oma idea.

**Projektivaihtoehdot:**

1. **Taso 1: FAQ-botti** — vastaa usein kysyttyihin kysymyksiin rajatun tietopohjan perusteella.
2. **Taso 2: Sähköpostin yhteenveto** — lukee sähköpostin tai tekstin ja tekee siitä tiiviin yhteenvedon.
3. **Taso 3: Asiakaspalvelun tikettijärjestelmä** — luokittelee tikettejä, ehdottaa vastauksia ja ohjaa riskitapaukset ihmiselle.

### Ohjeet pareille

#### Vaihe 1: Valitkaa projektityyppi noin 10 minuuttia

Valitkaa yksi projektityyppi tai oma idea. Kirjoittakaa suunnitelma seuraavan rakenteen mukaan:

| Suunnittelukohta | Ryhmän vastaus |
| --- | --- |
| **Käyttötapaus** | Mihin ongelmaan agentti auttaa? |
| **Mitä agentti tekee?** | Kirjoittakaa 3–4 vaihetta. |
| **Mitä agentti ei tee?** | Kirjoittakaa rajaukset. |
| **Hyväksyntäportit** | Missä kohdassa tarvitaan ihmisen hyväksyntä? |
| **Riskit** | Mitä voi mennä pieleen? |
| **Solmukaavio** | Piirtäkää työnkulku solmuina ja nuolina. |

#### Vaihe 2: Näyttäkää suunnitelma toiselle parille tai opettajalle noin 5 minuuttia

Toinen pari tai opettaja tarkistaa suunnitelman ja antaa palautetta.

**Tarkistuskysymykset palautteen antajalle:**

- Onko työnkulun aloituskohta eli triggeri selkeä?
- Onko työnkulku realistinen toteuttaa?
- Näkyykö suunnitelmassa turvakerros?
- Onko ihmisen hyväksyntä mukana oikeassa kohdassa?
- Onko jokin vaihe liian epäselvä tai liian laaja?

### Opettajan rooli

Kiertele luokassa ja kysy ryhmiltä:

- Mistä työnkulku alkaa? Mikä on triggeri?
- Kuka tai mikä tekee päätöksiä: agentti, sääntö vai ihminen?
- Onko kyseessä agentti vai chatbot?
- Missä vaiheessa ihminen päättää?
- Mitä riskejä olette tunnistaneet?
- Miten virhe huomataan ja korjataan?

Ohjaa opiskelijoita tarkentamaan suunnitelmiaan. Seuraavalla oppitunnilla he rakentavat työnkulkuja näiden suunnitelmien pohjalta.

### Yhteenveto noin 1 minuutti

Kerro opiskelijoille:

> Hyvä suunnitelma säästää aikaa rakentamisessa. Nyt tiedätte, mitä olette rakentamassa, mistä työnkulku alkaa, mitä solmuja tarvitaan ja missä kohtaa tarvitaan turvakerros tai ihmisen hyväksyntä.

### Odotettu oppimistulos

- Opiskelijat osaavat suunnitella yksinkertaisen n8n-agentin.
- Opiskelijat osaavat määritellä käyttötapauksen, rajaukset, riskit ja hyväksyntäportit.
- Opiskelijat ymmärtävät, että hyvä rakentaminen alkaa suunnittelusta.

---

## Arviointi

Opettaja arvioi opiskelijoiden työskentelyä seuraavien kriteerien perusteella:

| Arviointikohde | Mitä arvioidaan? |
| --- | --- |
| **Solmujen ymmärtäminen** | Osaavatko opiskelijat selittää, mitä kukin solmu tekee? |
| **Arkkitehtuurin pohdinta** | Erottavatko opiskelijat kielimallin ja harnessin vastuut ja perustelevatko he kuuden rakennusosan kattavuuden? |
| **Suunnittelun laatu** | Onko suunnitelma selkeä, rajattu ja realistinen? |
| **Kriittinen ajattelu** | Tunnistavatko opiskelijat riskejä, turvakerroksia ja hyväksyntäportteja? |

**Esimerkki arviointipalautteesta**

“Suunnitelmassanne on selkeä triggeri ja hyvä käyttötapaus. Seuraavaksi tarkentakaa, missä kohdassa agentti saa toimia itse ja missä kohdassa tarvitaan ihmisen hyväksyntä.”

---
