# Opettajavetoiset tehtävät – Lesson 19

## Tehtävä 1: Järjestelmien luokittelu ryhmissä (25 min)

### Valmistelu

Jaa opiskelijat 3–4 hengen ryhmiin. Anna jokaiselle ryhmälle yksi näistä kuvauksista.

### Kuvaelmat

**Scenario A: Laskun käsittelyagentti**
Yritys vastaanottaa joka päivä satoja sähköpostilaskuja. Agentti lukee jokaisen laskun automaattisesti, tunnistaa laskuttajan, tarkistaa laskun summan yrityksen budjetin mukaisesti ja, jos kaikki on kunnossa, tallentaa laskun kirjanpito­järjestelmään. Jos jokin on pielessä (summaa ei tunneta tai laskuttaja ei ole luotettava), agentti käyttää ihmisen hyväksyntää. Agentti myös seuraa, mitkä laskuttajat maksavat ajallaan, ja antaa sen perusteella heille paremmat ehdot.

**Scenario B: Muistutus-chatbot**
Oppilaat voivat kysyä chatissa: "Milloin on seuraava tentti?" Chatbot etsii tiedon sillä hetkellä käytössä olevasta opetuskalenterista ja vastaa: "Englannin tentti on 15. maaliskuuta." Chatbot odottaa, että oppilas kysyy seuraavan kysymyksen.

**Scenario C: Palvelimen automaattinen kuormantasaus**
Palvelinfarmi seuraa jokaisen palvelimen kuormaa reaaliajassa. Kun jokin palvelin nousee 85 %:n kuormaan viiden minuutin ajaksi peräkkäin, järjestelmä käynnistää automaattisesti uuden palvelimen ja alkaa reitittää uusia pyyntöjä sille. Se myös ilmoittaa IT-tiimille sähköpostilla ja auttaa selvittämään, onko kyseessä normaali kuormituspäivä vai ongelma.

### Ohjeet ryhmälle

1. Lukekaa teidän saamanne kuvaelma.
2. Keskustelkaa: onko tämä chatbot, agentti vai jotain muuta?
3. Analysoikaa seuraavat kuusi rakennusosaa:
   - **Syötekäsittelijä**: Kuinka järjestelmä vastaanottaa ja tulkitsee tietoja?
   - **Päättelijä**: Tekeekö järjestelmä omia päätöksiä vai vain reagoi?
   - **Työkalut**: Mitä toimintoja järjestelmällä on käytössään?
   - **Muisti**: Oppiiko järjestelmä aikaisemmista tapauksista?
   - **Turvakerros**: Onko mekanismia, joka estää vaarallisia toimintoja?
   - **Palautesilmukka**: Kuinka järjestelmä kerää tietoa ja parantaa itseään?
4. Kirjoittakaa paperille:
   - Valintanne (Chatbot / Agentti / Muu)
   - Perustelut 3–4 lauseessa, joissa nimetään vähintään 4 kuudesta komponentista

### Käsittely (10 min)

Kunkin ryhmän edustaja esittelee ryhmänsä valinnan ja perustelut. Opettaja tarkastelee vastauksia ja korjaa mahdollisia väärinkäsityksiä.

**Oikeat vastaukset:**
- A: Agentti (syötekäsittelijä analysoi laskuja, päättelijä tekee hyväksyntäpäätöksiä, turvakerros käyttää ihmisen hyväksyntää riskialueilla, palautesilmukka oppii maksajien käyttäytymisestä)
- B: Chatbot (passiivinen syötekäsittelijä odottaa kysymyksiä, päättelijä vain etsii dataa, ei omaa päätöksentekoa, ei palautesilmukkaa)
- C: Agentti (syötekäsittelijä seuraa kuormaa, päättelijä tekee päätöksen palvelimen käynnistämisestä, turvakerros rajoittaa toimintaa tiettyihin parametreihin, palautesilmukka ilmoittaa ihmiselle ja kerää dataa)

---

## Tehtävä 2: Suoritusputki-analyysi — kuusi komponenttia ja niiden yhteistyö (20 min)

### Valmistelu

Valitse esimerkiksi agentti (IT-tikettien automaattinen reitittäjä):

"Yrityksen IT-tukipyyntöjä hallitaan järjestelmällä, joka:
- Vastaanottaa asiakkaan tukipyynnöt
- Analysoi pyynnön sisältöä ja kategorisoi ongelman
- Lähettää pyynnön oikealle asiantuntijalle, luo tiketin ja ilmoittaa asiakkaalle
- Seuraa ratkaisu­aikoja ja oppii, mitkä asiantuntijat ovat nopeimpia kunkin ongelmakategorian kohdalla"

### Ohjeet

Piirrä taululle kuuden komponentin sykli tai näytä PowerPoint-dia. Käy ryhmän kanssa läpi suoritusputki-analyysin vaiheet:

1. **Syötekäsittelijä**: Asiakkaan sähköpostiviestin vastaanottaminen ja tekstin analysointi
2. **Päättelijä**: Viestin kategorisointi (esim. "verkkoyhteysvika", "ohjelmisto-ongelma", "laite") ja asiantuntijan valinta historiallisen datan perusteella
3. **Työkalut**: Tiketin luominen, sähköposti asiantuntijalle ja asiakkaalle, tietokantayhteys
4. **Muisti**: Aikaisempien ongelmien tietokanta, asiantuntijoiden nopeushistoria, asiakkaiden profiilit
5. **Turvakerros**: Jos agentti on epävarma kategorisoinnista, se kysyy asiantuntijalta; ei lähetä pyyntöä väärään tiimiin
6. **Palautesilmukka**: Ratkaisuajan mittaaminen, asiakkaan palautteen kerääminen, datan päivittäminen seuraavia päätöksiä varten

### Kysymyksiä ryhmälle

- "Mitä tapahtuisi, jos syötekäsittelijä epäonnistuisi ja väärinymmärtäisi pyynnön?"
- "Millä tavalla turvakerros suojelee sekä asiakkaita että IT-tiimiä?"
- "Miten palautesilmukka auttaa agenttia parantamaan nopeutta?"
- "Missä vaiheessa ihminen ottaa tilanteen haltuun ja miksi?"

---

## Tehtävä 3: Vaara-analyysi — kuuden komponentin epäonnistuminen (15 min)

### Tilanne

Näytä opiskelijoille tämä skenaario:

"Sähköpostin automaattinen vastausagentti saa komennon: 'Vastaa kaikille asiakkaille, jotka lähettävät sähköposteja, joissa on sana lasku.' Agentti toimii hyvin muutaman viikon ajan, mutta sitten asiakas lähettää sähköpostin: 'Miksi laskun kanssa on näin vaikea saada vastinetta teidän tuesta?' Agentti tulkitsee tämän automaattisesti laskua sisältäväksi viestiksi ja lähettää asiakkaalle robottimaisen vastauksen, vaikka asiakas oli loukkaantunut ja tarvitsi ihmisen vastauksen."

### Keskustelu

- Mikä meni pieleen? (Mikä komponentti?)
  - **Syötekäsittelijä**: Viestin konteksti tulkittiin väärin (sana "lasku" löydettiin, mutta sen merkitystä siinä yhteydessä ei ymmärretty)
  - **Päättelijä**: Päätös vastata automaattisesti oli liian yksinkertainen; siihen ei sisältynyt sävyn tai tunnetilan analyysiä
  - **Turvakerros**: Puuttui mekanismi, joka olisi tunnistanut negatiivisen sävyn ja estänyt automaattisen vastauksen

- Mikä olisi ollut ratkaisu?
  - Turvakerros olisi voinut estää vastauksen ja lähettää pyynnön ihmisen käsiteltäväksi, kun pyynnön sävy on negatiivinen tai loukkaava.
  - Muisti olisi voinut sisältää tietoa asiakkaiden tyytymättömyydestä ja merkitä korkean riskin tapaukset.

- Mikä on agentin autonomisuuden raja?
  - Agentti saa toimia autonomisesti rutiininomaisissa tapauksissa, mutta turvakerroksen on erotettava herkät, sensitiiviset tai poikkeukselliset tilanteet ihmiselle

**Johtopäätös:** Kaikkien kuuden komponentin täytyy toimia yhdessä. Jos turvakerros tai päättelijä epäonnistuu, seurauksena ovat virheet tai huono asiakaskokemus. Agentti on hyödyllinen, mutta sen täytyy tietää, milloin kutsua ihminen mukaan ja mistä turvatoimista ei saa luopua.

---

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:
- Erottaa agentti chatbotista konkreettisilla perusteluilla, jotka viittaavat kuuteen rakennusosaan
- Tunnistaa agentin kuusi rakennusosaa ja niiden roolit suoritusputkessa
- Nähdä, kuinka komponentit työskentelevät yhdessä ja mitä tapahtuu, kun yksi epäonnistuu
- Ymmärtää autonomisuuden rajat ja turvakerroksen tärkeyden ihmisten suojelun kannalta