# Opettajavetoiset tehtävät — oppitunti 19

## Tehtävä 19.1: Järjestelmien luokittelu ryhmissä noin 25 minuuttia

### Tavoite

Tehtävän tavoitteena on, että opiskelijat oppivat erottamaan **chatbotin**, **agentin** ja muun automaattisen järjestelmän toisistaan konkreettisten esimerkkien avulla. Samalla opiskelijat harjoittelevat tunnistamaan agentin kuusi keskeistä rakennusosaa: **syötekäsittelijän**, **päättelijän**, **työkalut**, **muistin**, **turvakerroksen** ja **palautesilmukan**.

**Opettajan painotus:** Korosta, että kaikki automaattiset järjestelmät eivät ole agentteja. Agenttimaisuus syntyy siitä, että järjestelmä tulkitsee tilannetta, tekee päätöksiä, käyttää työkaluja ja toimii rajatusti itsenäisesti.

### Valmistelu

- Jaa opiskelijat 3–4 hengen ryhmiin.
- Anna jokaiselle ryhmälle yksi alla olevista skenaarioista.
- Varmista, että jokaisella ryhmällä on käytössään muistiinpanovälineet tai yhteinen dokumentti vastausten kirjaamista varten.

### Skenaariot

#### Skenaario A: Laskun käsittelyagentti

Yritys vastaanottaa joka päivä satoja sähköpostilaskuja. Agentti lukee jokaisen laskun automaattisesti, tunnistaa laskuttajan, tarkistaa laskun summan yrityksen budjetin mukaisesti ja tallentaa laskun kirjanpitojärjestelmään, jos kaikki on kunnossa.

Jos jokin on pielessä, esimerkiksi laskun summaa ei tunnisteta tai laskuttaja ei ole luotettava, agentti pyytää ihmiseltä hyväksynnän. Agentti seuraa myös laskuttajien aiempaa toimintaa ja voi hyödyntää tätä tietoa myöhemmissä päätöksissä.

#### Skenaario B: Muistutus-chatbot

Opiskelijat voivat kysyä chatissa: “Milloin on seuraava tentti?” Chatbot etsii tiedon käytössä olevasta opetuskalenterista ja vastaa esimerkiksi: “Englannin tentti on 15. maaliskuuta.” Tämän jälkeen chatbot odottaa, että opiskelija kysyy seuraavan kysymyksen.

#### Skenaario C: Kasvihuoneen automaattinen ilmastonsäätö

Järjestelmä seuraa kasvihuoneen lämpötilaa ja ilmankosteutta reaaliajassa. Kun lämpötila on yli 28 asteessa viiden minuutin ajan, järjestelmä avaa automaattisesti tuuletusluukut ja käynnistää kastelun.

Järjestelmä lähettää myös vastuuhenkilölle ilmoituksen ja auttaa selvittämään, onko kyseessä normaali lämpöpiikki vai poikkeustilanne.

### Ohjeet ryhmälle

1. Lukekaa ryhmällenne annettu skenaario huolellisesti.
2. Päättäkää, onko kyseessä **chatbot**, **agentti** vai **muu automaattinen järjestelmä**.
3. Analysoikaa järjestelmää kuuden rakennusosan avulla:
   - **Syötekäsittelijä:** Miten järjestelmä vastaanottaa ja tulkitsee tietoa?
   - **Päättelijä:** Tekeekö järjestelmä päätöksiä vai reagoiko se vain käyttäjän kysymyksiin?
   - **Työkalut:** Mitä toimintoja järjestelmällä on käytössään?
   - **Muisti:** Hyödyntääkö järjestelmä aikaisempia tapauksia tai historiaa?
   - **Turvakerros:** Onko järjestelmässä mekanismi, joka estää vaarallisia tai epävarmoja toimintoja?
   - **Palautesilmukka:** Kerääkö järjestelmä tietoa ja parantaako se toimintaansa sen perusteella?
4. Kirjoittakaa vastauksenne paperille tai yhteiseen dokumenttiin:
   - valintanne: **chatbot**, **agentti** vai **muu automaattinen järjestelmä**,
   - 3–4 lauseen perustelu, jossa mainitaan vähintään neljä kuudesta rakennusosasta.

**Opettajan tarkistuskysymys:** Jos ryhmä sanoo “tämä on agentti, koska se toimii automaattisesti”, kysy: “Tekeekö se itsenäisiä päätöksiä? Käyttääkö se työkaluja? Onko sillä muistia tai turvakerrosta?”

### Käsittely noin 10 minuuttia

Kunkin ryhmän edustaja esittelee ryhmän valinnan ja perustelut. Opettaja tarkentaa vastauksia ja korjaa mahdollisia väärinkäsityksiä.

**Oikeat vastaukset ja perustelut:**

| Skenaario | Luokittelu | Perustelu |
| --- | --- | --- |
| **A: Laskun käsittelyagentti** | **Agentti** | Syötekäsittelijä analysoi laskuja, päättelijä tekee hyväksyntään liittyviä päätöksiä, työkalut mahdollistavat laskun tallentamisen kirjanpitojärjestelmään, turvakerros pyytää ihmisen hyväksyntää riskitilanteissa ja palautesilmukka hyödyntää laskuttajien toimintaa. |
| **B: Muistutus-chatbot** | **Chatbot** | Chatbot odottaa käyttäjän kysymyksiä ja hakee vastauksen kalenterista. Se ei tee itsenäisiä päätöksiä, ei käynnistä toimenpiteitä eikä sillä ole selkeää palautesilmukkaa. |
| **C: Kasvihuoneen automaattinen ilmastonsäätö** | **Agentti tai agenttimainen automaatio** | Syötekäsittelijä seuraa lämpötilaa ja kosteutta, päättelijä tekee päätöksen tuuletuksen ja kastelun käynnistämisestä, työkalut mahdollistavat luukkujen avaamisen ja kastelun ohjaamisen, turvakerros rajoittaa toimintaa ennalta määriteltyihin raja-arvoihin ja palautesilmukka tuottaa tietoa vastuuhenkilölle. |

### Odotettu oppimistulos

- Opiskelijat osaavat erottaa chatbotin ja agentin toisistaan konkreettisten esimerkkien avulla.
- Opiskelijat osaavat nimetä agentin keskeisiä rakennusosia.
- Opiskelijat ymmärtävät, että agentti ei vain vastaa kysymyksiin vaan voi myös tehdä päätöksiä ja käyttää työkaluja.

---

## Tehtävä 19.2: Suoritusputki-analyysi — kuusi komponenttia ja niiden yhteistyö noin 20 minuuttia

### Tavoite

Tehtävän tavoitteena on auttaa opiskelijoita ymmärtämään, miten agentin kuusi komponenttia toimivat yhdessä **suoritusputkessa**. Opiskelijat näkevät, miten tieto kulkee järjestelmässä syötteestä päätökseen, toimintaan, muistiin ja palautteeseen.

### Valmistelu

Valitse esimerkkijärjestelmäksi agentti. Voit käyttää esimerkiksi **asiakaspalvelupyyntöjen automaattista reitittäjää**.

**Esimerkkikuvaus:**

Organisaation asiakaspalvelupyyntöjä hallitaan järjestelmällä, joka:

- vastaanottaa asiakkaiden yhteydenottoja,
- analysoi pyynnön sisältöä ja luokittelee asian,
- lähettää pyynnön oikealle asiantuntijalle,
- luo tapauksen ja ilmoittaa asiakkaalle,
- seuraa ratkaisuaikoja,
- oppii, mitkä asiantuntijat ratkaisevat nopeimmin eri tyyppisiä asioita.

### Opettajan ohjeet

Piirrä taululle kuuden komponentin sykli tai näytä se diaesityksessä. Käy opiskelijoiden kanssa läpi, miten asiakaspalvelupyyntöjen reititys etenee vaihe vaiheelta.

**Agentin suoritusputki asiakaspalvelupyyntöjen reitityksessä**

|  |
| --- |
| **1. Syötekäsittelijä** Vastaanottaa asiakkaan sähköpostiviestin tai tukipyynnön ja analysoi tekstin. |
| ↓ |
| **2. Päättelijä** Luokittelee ongelman ja valitsee sopivan asiantuntijan aiemman datan perusteella. |
| ↓ |
| **3. Työkalut** Luo tapauksen, lähettää sähköpostin ja käyttää tarvittaessa tietokantaa. |
| ↓ |
| **4. Muisti** Hyödyntää aiempien ongelmien tietokantaa, asiantuntijoiden ratkaisuhistoriaa ja asiakkaiden profiilitietoja. |
| ↓ |
| **5. Turvakerros** Jos luokittelu on epävarma, agentti pyytää ihmiseltä apua eikä lähetä pyyntöä suoraan väärälle tiimille. |
| ↓ |
| **6. Palautesilmukka** Mittaa ratkaisuaikoja, kerää asiakaspalautetta ja päivittää tietoja seuraavia päätöksiä varten. |

Korosta opiskelijoille, että komponentit eivät ole irrallisia osia. Ne muodostavat ketjun, jossa jokainen vaihe vaikuttaa seuraavaan.

> Agentti ei ole vain lista osia. Se on prosessi, jossa tieto liikkuu vaiheesta toiseen ja jokainen vaihe vaikuttaa seuraavaan päätökseen.

### Kysymyksiä ryhmälle

- Mitä tapahtuisi, jos **syötekäsittelijä** epäonnistuisi ja ymmärtäisi pyynnön väärin?
- Miten **turvakerros** suojaa sekä asiakasta että palvelutiimiä?
- Miten **palautesilmukka** auttaa agenttia parantamaan toimintaansa?
- Missä vaiheessa ihmisen pitäisi ottaa tilanne haltuun ja miksi?
- Mikä komponentti olisi vaarallisin jättää pois tästä järjestelmästä?

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, miten agentin komponentit muodostavat yhdessä toimivan prosessin.
- Opiskelijat osaavat kuvata, miten syöte muuttuu päätökseksi ja toiminnaksi.
- Opiskelijat ymmärtävät, miksi muisti, turvakerros ja palautesilmukka ovat tärkeitä agentin luotettavuuden kannalta.

---

## Tehtävä 19.3: Vaara-analyysi — kuuden komponentin epäonnistuminen noin 15 minuuttia

### Tavoite

Tehtävän tavoitteena on auttaa opiskelijoita ymmärtämään, mitä voi tapahtua, jos agentin jokin komponentti epäonnistuu. Erityisesti tarkastellaan **syötekäsittelijän**, **päättelijän** ja **turvakerroksen** merkitystä.

### Tilanne

Näytä opiskelijoille seuraava skenaario:

> Sähköpostin automaattinen vastausagentti saa komennon: “Vastaa kaikille asiakkaille, jotka lähettävät sähköposteja, joissa on sana lasku.”
>
> Agentti toimii hyvin muutaman viikon ajan. Sitten asiakas lähettää sähköpostin: “Miksi laskun kanssa on näin vaikea saada vastinetta teidän tuestanne?”
>
> Agentti tulkitsee viestin automaattisesti laskua koskevaksi rutiiniviestiksi ja lähettää asiakkaalle robottimaisen vastauksen, vaikka asiakas oli tyytymätön ja olisi tarvinnut ihmisen vastauksen.

### Keskustelu

**Kysymys 1: Mikä meni pieleen?**

- **Syötekäsittelijä:** Järjestelmä tunnisti sanan “lasku”, mutta ei ymmärtänyt viestin kokonaiskontekstia eikä asiakkaan tyytymätöntä sävyä.
- **Päättelijä:** Päätös vastata automaattisesti oli liian yksinkertainen. Päätöksessä ei huomioitu viestin tunnetilaa, sävyä tai asiakassuhteen riskiä.
- **Turvakerros:** Järjestelmästä puuttui mekanismi, joka olisi tunnistanut negatiivisen, turhautuneen tai poikkeuksellisen viestin ja siirtänyt tilanteen ihmiselle.

**Kysymys 2: Mikä olisi ollut parempi ratkaisu?**

- **Turvakerros** olisi voinut estää automaattisen vastauksen, jos viestin sävy on negatiivinen, turhautunut tai poikkeuksellinen.
- Agentti olisi voinut ohjata viestin asiakaspalvelijalle tai tiiminvetäjälle.
- **Muisti** olisi voinut sisältää tietoa aiemmasta asiakastyytymättömyydestä ja merkitä tapauksen korkean riskin tilanteeksi.
- **Päättelijän** olisi pitänyt huomioida pelkän avainsanan lisäksi viestin tarkoitus ja sävy.

**Kysymys 3: Missä kulkee agentin autonomisuuden raja?**

- Agentti voi toimia itsenäisesti rutiininomaisissa ja matalan riskin tilanteissa.
- Agentin pitää siirtää herkät, epäselvät, poikkeukselliset tai tunnepitoiset tilanteet ihmiselle.
- Agentti ei saa tehdä päätöksiä, joilla voi olla merkittävä haitta asiakkaalle, organisaatiolle tai luottamukselle ilman riittävää turvakerrosta.

**Esimerkki opetukseen**

Kysy opiskelijoilta, olisiko sama virhe tapahtunut, jos agentti olisi tarkistanut viestin sävyn, asiakashistorian ja riskitason ennen vastaamista. Näin opiskelijat näkevät, miksi yksi avainsana ei riitä turvalliseen päätökseen.

### Johtopäätös

Kaikkien kuuden komponentin täytyy toimia yhdessä. Jos **syötekäsittelijä**, **päättelijä** tai **turvakerros** epäonnistuu, seurauksena voi olla virheellinen toiminta, huono asiakaskokemus tai luottamuksen menetys.

Agentti voi olla hyödyllinen, mutta sen täytyy tietää, milloin se saa toimia itsenäisesti ja milloin sen pitää kutsua ihminen mukaan.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että agentin virheet voivat syntyä yksittäisen komponentin epäonnistumisesta.
- Opiskelijat osaavat tunnistaa, mikä komponentti on epäonnistunut tietyssä tilanteessa.
- Opiskelijat ymmärtävät, miksi turvakerros ja ihmisen mukanaolo ovat tärkeitä.
- Opiskelijat osaavat pohtia agentin autonomisuuden rajoja.

---

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- erottaa **agentti** ja **chatbot** toisistaan konkreettisilla perusteluilla,
- viitata perusteluissaan agentin kuuteen rakennusosaan,
- tunnistaa agentin kuusi rakennusosaa ja niiden roolit suoritusputkessa,
- selittää, miten komponentit toimivat yhdessä,
- tunnistaa, mitä voi tapahtua, kun yksi komponentti epäonnistuu,
- ymmärtää autonomisuuden rajat ja turvakerroksen merkityksen ihmisten, asiakkaiden ja organisaation suojelemisessa.

---
