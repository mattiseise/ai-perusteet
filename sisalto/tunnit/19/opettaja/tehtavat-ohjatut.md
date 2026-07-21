# Opettajavetoiset tehtävät — oppitunti 19

## Tehtävä 19.1: Järjestelmien luokittelu ryhmissä noin 25 minuuttia

### Tavoite

Tehtävän tavoitteena on, että opiskelijat oppivat erottamaan **chatbotin**, **agentin** ja muun automaattisen järjestelmän toisistaan konkreettisten esimerkkien avulla. Kurssilla rakennettava tekoälyagentti rajataan kielimallin ja agentin ohjauskehyksen muodostamaksi järjestelmäksi. Tämä ei ole yleispätevä agentin määritelmä. Kuusi kohtaa — **syötekäsittelijä**, **päättelijä ja suunnittelija**, **työkalujen suorittaja**, **muisti ja konteksti**, **turvakerros** sekä **seuranta ja palautesilmukka** — ovat suunnittelun tarkistuslista, eivät jokaisen agentin pakolliset osat.

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
3. Analysoikaa järjestelmää kuuden kohdan tarkistuslistalla. Merkitkää jokainen kohta muodossa **tarvitaan**, **ei tarvita** tai **ei selviä kuvauksesta**:
   - **Syötekäsittelijä:** Miten järjestelmä vastaanottaa ja tulkitsee tietoa?
   - **Päättelijä:** Tekeekö järjestelmä päätöksiä vai reagoiko se vain käyttäjän kysymyksiin?
   - **Työkalut:** Mitä toimintoja järjestelmällä on käytössään?
   - **Muisti:** Tarvitseeko myöhempi suoritus aikaisempia tapauksia tai historiaa?
   - **Turvakerros:** Onko järjestelmässä mekanismi, joka estää vaarallisia tai epävarmoja toimintoja?
   - **Palautesilmukka:** Miten tuloksia seurataan ja kehitetäänkö toteutusta ihmisen vai automaation avulla?
4. Kirjoittakaa vastauksenne paperille tai yhteiseen dokumenttiin:
   - valintanne: **chatbot**, **agentti** vai **muu automaattinen järjestelmä**,
   - 3–4 lauseen perustelu, jossa käytetään määritelmää kielimalli + agentin ohjauskehys ja perustellaan ainakin yhden tarkistuskohdan tarpeellisuus tai pois jättäminen.

**Opettajan tarkistuskysymys:** Jos ryhmä sanoo “tämä on agentti, koska se toimii automaattisesti”, kysy: “Missä kielimalli tulkitsee tilannetta ja mitä työkaluja, oikeuksia tai turvarajoja agentin ohjauskehys antaa sille?”

### Käsittely noin 10 minuuttia

Kunkin ryhmän edustaja esittelee ryhmän valinnan ja perustelut. Opettaja tarkentaa vastauksia ja korjaa mahdollisia väärinkäsityksiä.

**Oikeat vastaukset ja perustelut:**

| Skenaario | Luokittelu | Perustelu |
| --- | --- | --- |
| **A: Laskun käsittelyagentti** | **Agentti, jos kuvauksen analyysi tehdään kielimallilla** | Agentin ohjauskehys välittää laskun mallille, tarjoaa työkalun kirjanpitojärjestelmään ja rajaa korkean riskin päätökset ihmisen hyväksyttäviksi. Aiempien laskuttajatietojen muisti on tämän toteutuksen valinta, ei agenttiuden ehto. |
| **B: Muistutus-chatbot** | **Chatbot** | Järjestelmä vastaa kysymykseen kalenteritiedolla mutta ei kuvauksen perusteella käytä kielimallia työkalutoimintojen valintaan. Muistin tai palautesilmukan puuttuminen ei yksin ratkaise luokitusta. |
| **C: Kasvihuoneen automaattinen ilmastonsäätö** | **Työnkulku tai agentti — kuvaus ei vielä ratkaise** | Kiinteät raja-arvot ovat työnkulku. Jos kielimalli tulkitsee poikkeustilannetta ja agentin ohjauskehys antaa sille rajatut anturi- ja ohjaustyökalut, kokonaisuus voi olla agentti. Opiskelijan pitää nimetä tämä puuttuva tieto. |

### Odotettu oppimistulos

- Opiskelijat osaavat erottaa chatbotin ja agentin toisistaan konkreettisten esimerkkien avulla.
- Opiskelijat osaavat käyttää kuutta kohtaa suunnittelutarkistuslistana ja tunnistaa, ettei kaikkia tarvita aina.
- Opiskelijat ymmärtävät, että agentti ei vain vastaa kysymyksiin vaan voi myös tehdä päätöksiä ja käyttää työkaluja.

---

## Tehtävä 19.2: Toteutusanalyysi — kuuden kohdan tarkistuslista noin 20 minuuttia

### Tavoite

Tehtävän tavoitteena on auttaa opiskelijoita soveltamaan kuuden kohdan tarkistuslistaa yhteen toteutukseen. Opiskelijat seuraavat tiedon kulkua syötteestä kielimallille ja työkaluille sekä perustelevat, tarvitseeko esimerkki pitkäkestoista muistia tai palautekierrosta.

### Valmistelu

Valitse esimerkkijärjestelmäksi agentti. Voit käyttää esimerkiksi **asiakaspalvelupyyntöjen automaattista reitittäjää**.

**Esimerkkikuvaus:**

Organisaation asiakaspalvelupyyntöjä hallitaan järjestelmällä, joka:

- vastaanottaa asiakkaiden yhteydenottoja,
- analysoi pyynnön sisältöä ja luokittelee asian,
- lähettää pyynnön oikealle asiantuntijalle,
- luo tapauksen ja ilmoittaa asiakkaalle,
- seuraa ratkaisuaikoja,
- tuottaa lokin, jonka perusteella ihminen voi arvioida reitityksen onnistumista.

### Opettajan ohjeet

Piirrä taululle esimerkin tiedonkulku tai näytä se diaesityksessä. Merkitse erikseen pakollinen ydin, **kielimalli + agentin ohjauskehys**, ja valinnaiset toteutuspäätökset.

**Yksi mahdollinen toteutus asiakaspalvelupyyntöjen reitityksessä**

|  |
| --- |
| **1. Syötekäsittelijä** Vastaanottaa asiakkaan sähköpostiviestin tai tukipyynnön ja analysoi tekstin. |
| ↓ |
| **2. Päättelijä** Luokittelee ongelman ja valitsee sopivan asiantuntijan aiemman datan perusteella. |
| ↓ |
| **3. Työkalut** Luo tapauksen, lähettää sähköpostin ja käyttää tarvittaessa tietokantaa. |
| ↓ |
| **4. Muisti — valinnainen** Hyödyntää aiempia ratkaisuja vain, jos käyttötarkoitus, säilytysaika ja oikeudet on määritelty. Muuten nykyinen pyyntö ja tietohaku riittävät. |
| ↓ |
| **5. Turvakerros** Jos luokittelu on epävarma, agentti pyytää ihmiseltä apua eikä lähetä pyyntöä suoraan väärälle tiimille. |
| ↓ |
| **6. Seuranta — tässä toteutuksessa ihmisen palautekierros** Mittaa ratkaisuaikoja ja tuottaa lokin, jonka perusteella ihminen korjaa reitityssääntöjä tai promptia. Malli ei opi automaattisesti. |

Korosta opiskelijoille, että taulukko kuvaa yhtä mahdollista toteutusta. Sama tarkistuslista voi johtaa toiseen järjestykseen tai siihen, että pitkäkestoinen muisti ja automaattinen palautekierros jätetään pois.

> Kurssin rajauksessa rakennettava tekoälyagentti muodostuu kielimallista ja agentin ohjauskehyksestä. Kuusi kohtaa auttavat perustelemaan ohjauskehyksen suunnittelun, mutta eivät ole pakollinen kuuden vaiheen suoritusputki.

### Kysymyksiä ryhmälle

- Mitä tapahtuisi, jos **syötekäsittelijä** epäonnistuisi ja ymmärtäisi pyynnön väärin?
- Miten **turvakerros** suojaa sekä asiakasta että palvelutiimiä?
- Miten seuranta auttaa ihmistä parantamaan toteutusta ilman oletusta mallin automaattisesta oppimisesta?
- Missä vaiheessa ihmisen pitäisi ottaa tilanne haltuun ja miksi?
- Minkä tarkistuskohdan voisi jättää tästä toteutuksesta pois ja millä perusteella?

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, miten kielimalli ja agentin ohjauskehys muodostavat toimivan agentin.
- Opiskelijat osaavat kuvata, miten syöte muuttuu päätökseksi ja toiminnaksi.
- Opiskelijat osaavat perustella muistin ja palautekierroksen tarpeen tai pois jättämisen sekä tunnistavat turvarajojen merkityksen.

---

## Tehtävä 19.3: Vaara-analyysi — suunnittelukohdan epäonnistuminen noin 15 minuuttia

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

Tässä esimerkkitoteutuksessa syötekäsittelyn, päättelyn ja turvarajojen täytyy toimia yhdessä. Kaikkien kuuden tarkistuskohdan ei tarvitse näkyä jokaisessa agentissa, mutta jokainen mukaan valittu osa pitää testata.

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
- osaa selittää kurssin rajauksen eli kielimallin ja agentin ohjauskehyksen muodostaman järjestelmän,
- käyttää kuutta kohtaa suunnittelutarkistuslistana,
- perustella, mitä toteutus tarvitsee ja mitä siitä voi jättää pois,
- tunnistaa, mitä voi tapahtua, kun mukaan valittu osa epäonnistuu,
- ymmärtää autonomisuuden rajat ja turvakerroksen merkityksen ihmisten, asiakkaiden ja organisaation suojelemisessa.

---
