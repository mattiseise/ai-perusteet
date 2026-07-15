# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

Tämän lohkon tavoitteena on, että opiskelija ymmärtää **konteksti-ikkunan** teknisen rajoituksen ja osaa hallita sitä pitkillä tekoälykeskusteluilla ja monivaiheisissa IT-projekteissa. Oppitunnin ydin on, että tekoäly ei muista kaikkea rajattomasti. Kun keskustelu, lokit, koodi tai dokumentaatio kasvavat liian pitkiksi, vanha tieto voi pudota pois mallin näkyvistä.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, että **konteksti-ikkuna** määrittää, kuinka paljon tietoa tekoäly näkee kerralla.
- Opiskelija ymmärtää, että pitkä keskustelu, suuri lokitiedosto, laaja dokumentaatio tai suuri koodipohja voi ylittää konteksti-ikkunan rajat.
- Opiskelija ymmärtää, että mallin unohtaminen ei ole välttämättä virhe, vaan tekninen rajoitus.
- Opiskelija tunnistaa **FIFO-periaatteen**: kun ikkuna täyttyy, vanhinta tietoa putoaa ensin pois.

### Soveltaa ja analysoida

- Opiskelija tunnistaa kolme keskeistä konteksti-ikkunan hallintastrategiaa: **tiivistys**, **pilkkominen** ja **ankkurointi**.
- Opiskelija osaa arvioida, milloin keskustelu tai projekti täytyy jakaa pienempiin osiin.
- Opiskelija osaa tunnistaa tilanteita, joissa tekoälyn vastaus voi heiketä, koska aiempi tieto on pudonnut pois kontekstista.

### Luoda ja arvioida

- Opiskelija osaa suunnitella monivaiheisen IT-projektin tekoälyn kanssa niin, että keskeinen tieto ei katoa.
- Opiskelija osaa laatia **ankkurikontekstin**, jota voidaan käyttää keskustelun jatkamiseen uudessa ikkunassa.
- Opiskelija ymmärtää, että dokumentointi ei ole ylimääräistä työtä, vaan tapa tehdä tekoälystä luotettavampi yhteistyökumppani.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että konteksti-ikkunan hallinta on vastuullisen käyttäjän taito. Tekoäly ei aina kerro, milloin se on unohtanut jotakin. Siksi käyttäjän pitää suunnitella, tiivistää, dokumentoida ja ankkuroida tieto itse.

---

## Pedagoginen lähestymistapa

### Ydinviesti: tekoälyn muisti on rajallinen työtila

Opiskelijoille kannattaa selittää konteksti-ikkuna rajallisena työtilana. Tekoälyllä on käytössään vain se tieto, joka mahtuu sen hetkiseen konteksti-ikkunaan. Jos keskustelu jatkuu pitkään tai mukaan lisätään paljon koodia, lokeja ja dokumentaatiota, osa vanhemmasta tiedosta voi pudota pois.

> **Tekoälyn konteksti-ikkuna on kuin rajallinen muistikirja. Kun sivut täyttyvät, vanhimmat merkinnät eivät enää ole mallin näkyvissä.**

Korosta opiskelijoille:

- **Konteksti-ikkuna** ei ole sama asia kuin pysyvä muisti.
- Suuri konteksti-ikkuna auttaa, mutta se ei poista hallinnan tarvetta.
- Pitkissä projekteissa pitää päättää, mikä tieto on olennaista ja mikä voidaan tiivistää.
- Jos tieto katoaa kontekstista, malli voi vastata väärin mutta silti kuulostaa varmalta.

### Kolme hallintastrategiaa

Tällä oppitunnilla kannattaa opettaa kolme käytännön strategiaa, joiden avulla opiskelija voi hallita pitkiä keskusteluja ja laajoja projekteja tekoälyn kanssa.

| Strategia | Mitä se tarkoittaa? | IT-esimerkki |
| --- | --- | --- |
| **Tiivistys** | Pitkä keskustelu, dokumentti tai loki tiivistetään olennaisiin havaintoihin. | ”Tiivistä nämä 500 lokiriviä 10 tärkeimpään havaintoon.” |
| **Pilkkominen** | Laaja tehtävä jaetaan pienempiin osiin, jotka käsitellään erikseen. | Sovelluksen virheenkorjaus jaetaan käyttöliittymään, tietokantaan ja palvelinlogiikkaan. |
| **Ankkurointi** | Keskeinen tieto kirjataan ankkurikontekstiksi, joka tuodaan mukaan uuteen keskusteluun. | Projektin tavoite, päätökset, rajoitukset ja nykyinen tilanne tallennetaan yhteenvetoon. |

**Opettajan huomio:** Korosta, että nämä strategiat eivät ole toisensa poissulkevia. Pitkässä projektissa opiskelija käyttää usein kaikkia kolmea: hän pilkkoo työn osiin, tiivistää jokaisen osan tulokset ja ylläpitää ankkurikontekstia projektin jatkuvuutta varten.

### Dokumentointi on kontekstinhallintaa

Opiskelijat saattavat ajatella, että dokumentointi on erillinen työvaihe. Tällä oppitunnilla dokumentointi kannattaa esittää osana konteksti-ikkunan hallintaa. Kun tekoäly ei voi muistaa kaikkea, ihmisen täytyy pitää yllä projektin ulkoista muistia.

Hyvä dokumentaatio vastaa ainakin näihin kysymyksiin:

- **Mikä on projektin tavoite?**
- **Mitä on jo päätetty?**
- **Mitä on jo kokeiltu?**
- **Mikä toimii ja mikä ei toimi?**
- **Mitä rajoituksia pitää muistaa?**
- **Mikä on seuraava tehtävä?**

> **Dokumentointi ei ole tekoälytyön hidaste. Se on tapa varmistaa, että työ voi jatkua oikein myös silloin, kun keskusteluikkuna vaihtuu.**

### Ankkurikontekstin malli

Ankkurikonteksti on lyhyt, jäsennelty yhteenveto, jonka opiskelija voi liittää uuden tekoälykeskustelun alkuun. Se säilyttää projektin jatkuvuuden, vaikka alkuperäinen keskustelu ei enää olisi mallin näkyvissä.

**PROJEKTIN TAVOITE:** Rakennan Python-sovellusta, joka lukee CSV-tiedoston ja tuottaa raportin.

**NYKYTILANNE:** CSV-tiedosto luetaan onnistuneesti, mutta raportin summat ovat väärin.

**JO KOKEILTU:** Tarkistin tiedoston polun, sarakkeiden nimet ja desimaalierottimen.

**TÄRKEÄ RAJAUS:** Älä ehdota koko sovelluksen uudelleenkirjoittamista.

**SEURAAVA TEHTÄVÄ:** Auta selvittämään, miksi laskettu summa poikkeaa odotetusta.

Tätä mallia voi käyttää myös tulevilla oppitunneilla, kun opiskelijat rakentavat laajempia projekteja tai agentteja.

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”Konteksti-ikkuna on niin suuri, ettei minun tarvitse huolehtia siitä.”

**Korjaava näkökulma:** Vaikka konteksti-ikkuna voi olla suuri, IT-projektit täyttävät sen nopeasti. Pitkät lokit, kooditiedostot, keskustelut ja dokumentaatio voivat yhdessä ylittää rajan. Suuri ikkuna auttaa, mutta se ei korvaa suunnittelua.

> Iso työpöytä ei poista järjestyksen tarvetta.

### Väärinkäsitys 2: ”Jos malli unohtaa, se on mallin huonoutta.”

**Korjaava näkökulma:** Konteksti-ikkuna on tekninen ominaisuus, ei pelkkä mallin huonous. Vastuullinen käyttäjä ymmärtää rajoituksen ja suunnittelee työn sen mukaan. Hyvä käyttäjä ei oleta, että malli muistaa kaiken ikuisesti.

### Väärinkäsitys 3: ”Dokumentointi on ylimääräistä, koska malli muistaa kaiken.”

**Korjaava näkökulma:** Malli ei muista kaikkea. Dokumentointi on ulkoinen muisti, jonka avulla tärkeät päätökset, rajoitukset ja tulokset voidaan tuoda takaisin kontekstiin. Ilman dokumentaatiota tieto voi kadota keskustelun mukana.

### Väärinkäsitys 4: ”Pilkkominen tekee projektista hitaamman.”

**Korjaava näkökulma:** Pilkkominen voi tuntua aluksi hitaammalta, mutta se säästää aikaa kokonaisuudessa. Pienemmät osat ovat helpompia ymmärtää, testata ja korjata. Ilman pilkkomista tekoäly voi antaa yleisiä, sekavia tai virheellisiä vastauksia.

### Väärinkäsitys 5: ”Malli kertoo kyllä, jos se ei muista.”

**Korjaava näkökulma:** Malli ei välttämättä ilmoita, että tieto on pudonnut pois kontekstista. Se voi vastata puuttuvan tiedon perusteella arvaamalla. Tämä tekee kontekstin katoamisesta erityisen vaarallista: vastaus voi näyttää itsevarmalta mutta perustua puutteelliseen tietoon.

---

## Opettajan fasilitointiohjeet

### Ennen oppituntia

- Testaa etukäteen esimerkki, jossa pitkä keskustelu tai suuri tietomäärä saa mallin menettämään olennaista kontekstia.
- Valitse opiskelijoille konkreettiset IT-esimerkit. Jos kurssi painottuu tietokantoihin, käytä SQL- tai tietokantaesimerkkejä. Jos painotus on ohjelmoinnissa, käytä koodiin ja virheilmoituksiin liittyviä esimerkkejä.
- Tutustu tokeneihin yleisellä tasolla. Opiskelijoille ei tarvitse opettaa tarkkaa tokenlaskentaa, mutta opettajan on hyvä ymmärtää, että sanat, merkit ja koodinpätkät vievät tilaa konteksti-ikkunasta.
- Valmistele ankkurikontekstin malli, jota opiskelijat voivat käyttää omissa tehtävissään.

### Oppitunnin aikana

- **Avaa konkreettisella kysymyksellä:** ”IT-projektit voivat olla pitkiä. Miten hallitsemme niitä tekoälyn kanssa niin, ettei tärkeä tieto katoa?”
- **Käytä analogiaa:** tekoälyn muistikirjassa on rajallinen määrä sivuja. Kun muistikirja täyttyy, vanhimmat sivut eivät enää ole käytössä.
- **Näytä elävä esimerkki:** jos mahdollista, tee lyhyt demo, jossa mallin vastaus heikkenee, kun keskustelu pitkittyy tai olennaista tietoa ei enää anneta mukaan.
- **Korosta kolmea strategiaa:** tiivistys, pilkkominen ja ankkurointi. Kirjoita ne näkyville ja palaa niihin harjoitusten aikana.
- **Tee dokumentoinnista vastuullisen käyttäjän taito:** älä esitä dokumentointia ylimääräisenä koulutehtävänä, vaan työelämätaitona.

### Yleisiä haasteita ja ratkaisuja

**Haaste: Opiskelijat kysyvät, voiko malli vain muistaa kaiken.**
**Ratkaisu:** Selitä, että kyseessä ei ole käyttäjän valinta vaan tekninen raja. Vastuullinen käyttäjä ei kiellä rajaa, vaan suunnittelee sen ympärille.

**Haaste: Dokumentointi tuntuu opiskelijoista raskaalta.**
**Ratkaisu:** Näytä, miten tekoälyä voi käyttää myös dokumentoinnin tukena. Esimerkiksi: ”Tiivistä tämä keskustelu 200 sanaan ja säilytä päätökset, rajoitukset ja seuraavat tehtävät.”

**Haaste: Opiskelijat eivät ymmärrä pilkkomisen hyötyä ennen kuin ongelma osuu kohdalle.**
**Ratkaisu:** Käytä tehtävää, jossa sama projekti käsitellään ensin yhtenä suurena kokonaisuutena ja sen jälkeen pilkottuna. Anna opiskelijoiden vertailla vastausten laatua.

---

## Luokkatehtävien ohjeistus

### TT-A: Konteksti-ikkunan täyttyminen

**Tavoite:** Opiskelija näkee, että konteksti-ikkuna ei ole rajaton ja että pitkä keskustelu voi vaikuttaa vastauksen laatuun.

**Tehtävä:** Anna opiskelijoille pitkä tekninen keskustelu, loki tai dokumentti. Pyydä heitä lisäämään siihen vaiheittain uutta tietoa ja tarkkailemaan, milloin tekoälyn vastaus alkaa menettää aiempaa kontekstia.

**Ohje opiskelijalle:**

1. Anna tekoälylle projektin alkuperäinen tavoite ja tärkeät rajoitukset.
2. Lisää keskusteluun vaiheittain uutta tietoa, kuten lokirivejä, virheilmoituksia tai koodia.
3. Kysy lopuksi alkuperäiseen tavoitteeseen liittyvä kysymys.
4. Arvioi, muistiko tekoäly olennaisen tiedon vai unohtuiko jotakin.

**Aika-arvio:** 20–25 minuuttia

---

### TT-B: Projektin pilkkominen

**Tavoite:** Opiskelija osaa jakaa laajan IT-tehtävän hallittaviin osiin.

**Tehtävä:** Opiskelija valitsee laajan projektin, kuten verkkosovelluksen virheenkorjauksen, tietokantaprojektin tai palvelinasennuksen. Hän pilkkoo sen pienempiin osiin ja määrittää, mitä tietoa kuhunkin osaan tarvitaan.

| Projektin osa | Mitä tietoa tarvitaan? | Mikä on osan tavoite? |
| --- | --- | --- |
| Käyttöliittymä | Käyttäjän näkymä, virheilmoitus, selainkonsolin virheet. | Selvittää, johtuuko ongelma käyttöliittymästä. |
| Palvelinlogiikka | API-kutsut, palvelimen lokit, virhekoodit. | Tarkistaa, käsitelläänkö pyyntö oikein palvelimella. |
| Tietokanta | Tietokantakyselyt, taulurakenne, testidata. | Varmistaa, että data tallentuu ja palautuu oikein. |

**Aika-arvio:** 20–25 minuuttia

---

### TT-C: Ankkurikontekstin kirjoittaminen

**Tavoite:** Opiskelija osaa luoda lyhyen yhteenvedon, jonka avulla projekti voi jatkua uudessa tekoälykeskustelussa.

**Tehtävä:** Opiskelija kirjoittaa oman projektinsa tai annetun esimerkkiprojektin perusteella ankkurikontekstin. Sen pitää sisältää tavoite, nykytilanne, tehdyt päätökset, rajoitukset ja seuraava tehtävä.

| Ankkurikontekstin osa | Kirjoita tähän |
| --- | --- |
| **Projektin tavoite** | Mitä ollaan rakentamassa tai ratkaisemassa? |
| **Nykytilanne** | Mikä toimii ja mikä ei vielä toimi? |
| **Tehdyt päätökset** | Mitä on jo päätetty tai rajattu? |
| **Rajoitukset** | Mitä ei saa tehdä tai mitä pitää huomioida? |
| **Seuraava tehtävä** | Mihin tekoälyn pitää auttaa seuraavaksi? |

**Aika-arvio:** 15–20 minuuttia

---

## Epäonnistumisen pedagogiikka — Tehtävä 5.3

### Miksi tämä tehtävä on tärkeä?

Tehtävät 5.1 ja 5.2 opettavat hallintastrategioita. Tehtävä 5.3 opettaa vielä syvemmän oivalluksen: **malli ei välttämättä kerro, kun se on unohtanut**. Tämä on kriittinen havainto, koska opiskelija voi muuten luottaa mallin vastaukseen liikaa.

Tavoitteena on, että opiskelija kokee itse tilanteen, jossa malli antaa vastauksen puutteellisella kontekstilla. Kokemus tekee kontekstinhallinnasta konkreettista.

### Fasilitointiohje

- Älä varoita opiskelijoita etukäteen tarkasti siitä, mitä tulee tapahtumaan. Anna heidän havaita ongelma itse.
- Kun ryhmät raportoivat tuloksiaan, kysy: ”Mistä huomasitte, että vastaus oli väärä tai puutteellinen?”
- Korosta, että vastuulliselle käyttäjälle tärkeintä ei ole se, ettei virheitä koskaan tapahdu. Tärkeää on osata tunnistaa virhe, arvioida sen syy ja korjata toimintatapa.
- Jos malli muistaa liian pitkään, pidennä keskustelua, lisää lokia tai käytä tehtävässä pienemmän konteksti-ikkunan mallia.

### Yleisiä väärinkäsityksiä tehtävässä 5.3

**”Malli oli huono, koska se unohti.”**
**Korjaus:** Malli toimi teknisten rajojensa sisällä. Konteksti-ikkuna on rakenteellinen rajoitus, ei pelkkä laatuvirhe. Vastuullinen käyttäjä suunnittelee työn tämän rajan mukaan.

**”Huomasin heti, että vastaus oli väärä.”**
**Jatkokysymys:** Entä jos et olisi tiennyt oikeaa vastausta itse? Miten vastuullisena käyttäjänä varmistaisit vastauksen oikeellisuuden?

### Arviointivinkit tehtävään 5.3

- Etsi opiskelijan dokumentaatiosta konkreettinen kohta, jossa virhe tapahtui.
- Hyvä vastaus sisältää tarkan kohdan keskustelussa, analyysin siitä, miksi malli unohti, ja ehdotuksen korjaukseksi.
- Erinomainen vastaus lisää pohdinnan: ”Oikeassa projektissa tämä olisi voinut johtaa siihen, että...”

---

## Formatiivinen tarkistuspiste — todistusaineisto 2

### Tavoite

Opiskelija soveltaa kontekstin katoamisen teoriaa konkreettiseen työtilanteeseen. Todistusaineisto toimii rakennuspalikkana myöhemmälle arviointitehtävälle.

### Tehtävänanto opiskelijalle

Kirjoita lyhyt analyysi tilanteesta, jossa tekoälyn konteksti voisi kadota kesken IT-projektin. Kuvaa:

1. Mikä projekti tai työtilanne on kyseessä?
2. Mikä tärkeä tieto voisi pudota pois konteksti-ikkunasta?
3. Miksi juuri alkupään tieto katoaa ensin?
4. Mitä haittaa unohtamisesta voisi seurata?
5. Miten estäisit ongelman? Käytä vähintään yhtä strategiaa: **tiivistys**, **pilkkominen**, **ankkurointi** tai **dokumentointi**.

**Valmis vastaus:** noin 150–250 sanaa.

### Mitä etsiä palautuksesta?

- **Konkreettinen tilanne:** opiskelija kuvaa todellisen tai uskottavan tilanteen eikä vain toista oppimateriaalin esimerkkiä.
- **FIFO-periaate ymmärretty:** opiskelija selittää, miksi juuri alkupään tieto katoaa ensin.
- **Seuraukset tunnistettu:** opiskelija yhdistää unohtamisen konkreettiseen haittaan, kuten virheeseen, turvallisuusriskiin tai tehokkuushäviöön.
- **Ratkaisu ehdotettu:** opiskelija ehdottaa vähintään yhtä hallintatekniikkaa, kuten ankkurointia, pilkkomista, tiivistämistä tai dokumentointia.

### Yleinen väärinymmärrys

**”Malli unohtaa, koska se on tyhmä.”**
Ohjaa opiskelijaa kohti FIFO-periaatetta: malli ei unohda tahallaan. Vanhimmat tokenit putoavat pois, kun konteksti-ikkuna täyttyy.

### Palautteen antaminen

Anna lyhyt palaute. Kiinnitä erityistä huomiota siihen, onko tapausesimerkki konkreettinen ja uskottava. Opiskelijan täytyy analysoida nimenomaan konkreettista skenaariota, ei vain selittää teoriaa yleisellä tasolla.

- **Jos vastaus on hyvä:** ”Hyvä — kuvaat konkreettisen tilanteen ja yhdistät kontekstin katoamisen todelliseen haittaan. Ratkaisusi sopii tilanteeseen.”
- **Jos tilanne jää yleiseksi:** ”Tarkenna vielä: missä työtilanteessa tämä tapahtuisi ja mikä tieto tarkalleen katoaisi?”
- **Jos FIFO jää epäselväksi:** ”Lisää selitys siitä, miksi vanhin tieto putoaa pois ensin, kun ikkuna täyttyy.”

---

## Arviointivinkit

### Tehtävän TT-A jälkeen

- Tarkista, huomasivatko opiskelijat, että mallin vastaus voi heiketä ilman selvää varoitusta.
- Kysy: ”Mistä päättelitte, että malli ei enää käyttänyt alkuperäistä tietoa?”
- Ohjaa opiskelijoita erottamaan mallin tekninen raja ja käyttäjän vastuu kontekstinhallinnasta.

### Tehtävän TT-B jälkeen

- Katso opiskelijoiden pilkkomistaulukkoa. Ovatko osat loogisia ja tehtävän kannalta hallittavia?
- Kysy: ”Miksi valitsit juuri nämä osat?”
- Hyvä vastaus osoittaa, että jokainen osa voidaan käsitellä omassa kontekstissaan ilman, että koko projekti täytyy antaa kerralla.

### Tehtävän TT-C jälkeen

- Tarkista, että ankkurikonteksti sisältää projektin tavoitteen, nykytilanteen, tehdyt päätökset, rajoitukset ja seuraavan tehtävän.
- Kysy: ”Voisiko toinen ihminen jatkaa projektia tämän yhteenvedon perusteella?” Jos vastaus on kyllä, myös tekoälyn on helpompi jatkaa oikeasta kohdasta.

---

## Jatkuva integraatio tulevilla oppitunneilla

### Multimodaalisuus

Myöhemmillä oppitunneilla opiskelijat näkevät, että kuvia, koodia, taulukoita ja lokitiedostoja voidaan käyttää kontekstina. Konteksti-ikkunan hallinta laajenee tällöin: opiskelijan pitää arvioida, mikä osa kuvasta, lokista tai datasta on olennaista ja mikä kannattaa tiivistää.

### Jatkuvat projektit

Jokaisessa pidemmässä tekoälyavusteisessa projektissa opiskelijoiden tulisi käyttää tämän oppitunnin strategioita. Tiivistys, pilkkominen ja ankkurointi ovat erityisen tärkeitä, kun projekti jatkuu useamman päivän tai useamman keskustelun ajan.

### Myöhemmät agenttioppitunnit

Kontekstin katoamisen kokemus rakentaa pohjaa myöhemmille agenttioppitunneille. Kun opiskelijat oppivat agenteista, muistista ja tilasta, he ymmärtävät paremmin, miksi agentille täytyy suunnitella erillinen muisti, tilanhallinta ja lokitus.

**Opettajan muistutus:** Tämä oppitunti yhdistää teorian ja käytännön. Opiskelijat näkevät, että tekoälystä tulee luotettava yhteistyökumppani vain, jos sen rajoitukset ymmärretään ja työskentely suunnitellaan niiden ympärille.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että pitkä tekoälykeskustelu ei automaattisesti tarkoita parempaa ymmärrystä. Kun konteksti-ikkuna täyttyy, osa tiedosta voi pudota pois, ja malli voi jatkaa vastaamista itsevarmasti puutteellisella tiedolla.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Jos jatkaisit samaa IT-projektia tekoälyn kanssa viikon ajan, mitä tietoa sinun pitäisi dokumentoida, jotta työ ei alkaisi ajautua väärään suuntaan?

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **katoamis- ja palautusloki**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–10 min | Virittäytyminen | Kytke ydinkysymys tuttuun tilanteeseen ja tarkista lähtötaso. |
| 10–25 min | Ydinkäsite | Mallinna tunnin keskeinen ero yhdellä vastaesimerkillä. |
| 25–65 min | Perustuotos | Oppija dokumentoi keskustelun tiedon katoamisen ja palauttaa olennaisen tiedon tiivistämällä. Tämä 40 minuutin jakso on itsenäistä tai parin kanssa tehtävää työskentelyä. |
| 65–80 min | Testaus ja purku | Testauta tuotos annetulla tapauksella ja pura yksi onnistuminen sekä yksi korjaus. |
| 80–90 min | Tallennus ja exit ticket | Varmista tiedoston nimi, tallennuspaikka ja yhden lauseen johtopäätös. |

### Tukireitti

Oppija järjestää annetun keskustelukatkelman tiedot ikkunan sisä- ja ulkopuolelle. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis, oppija vertailee kahta tiivistysstrategiaa. Syventävä työ ei kasvata pakollista ydintuotosta.
