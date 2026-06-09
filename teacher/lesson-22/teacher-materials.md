# Opettajan materiaalit — oppitunti 22

## Osaamistavoitteet

Tämän oppitunnin tavoitteena on, että opiskelija ymmärtää, miten agentti käyttää **työkaluja** ja miksi työkalujen käyttö tekee agentista tavallista chatbotia voimakkaamman mutta myös riskialttiimman. Oppitunnin ydin on, että agentti ei vain vastaa, vaan voi **tehdä todellisia asioita**: lukea tiedostoja, hakea tietoa verkosta ja suorittaa komentoja.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, että agentin voima syntyy sen kyvystä käyttää **työkaluja**.
- Opiskelija tunnistaa kolme perustyökalua: **tiedostot**, **verkkohaku** ja **CLI-komennot**.
- Opiskelija ymmärtää, että jokainen työkalu tuo mukanaan turvallisuusriskejä.
- Opiskelija ymmärtää **orkestroinnin** merkityksen: agentin pitää käyttää työkaluja oikeassa järjestyksessä.

### Soveltaa ja analysoida

- Opiskelija osaa arvioida, mitä työkaluja agentti tarvitsee tiettyyn tehtävään.
- Opiskelija osaa suunnitella työkaluille **rajoituksia**, kuten luku- ja kirjoitusoikeuksia tai komentojen whitelistejä.
- Opiskelija osaa tunnistaa tilanteita, joissa verkkohaku, tiedostojen käsittely tai CLI-komennot voivat aiheuttaa vahinkoa.

### Luoda ja arvioida

- Opiskelija osaa suunnitella agentille työkalukokonaisuuden, jossa pääsy on rajattu tehtävän kannalta välttämättömään.
- Opiskelija osaa kuvata agentin työkalujen käyttöjärjestyksen työnkulkuna.
- Opiskelija osaa arvioida, millaisia validointi-, rajoitus-, seuranta- ja palautumiskerroksia työkalujen käyttö vaatii.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että työkalut tekevät agentista hyödyllisen mutta myös vaarallisen. Agentti, jolla on pääsy tiedostoihin, verkkoon tai komentoriville, voi tehdä oikeita asioita oikeassa ympäristössä. Siksi jokainen työkalu täytyy rajata, valvoa ja testata.

---

## Pedagoginen lähestymistapa

### Ydinviesti: agentti toimii maailmassa työkalujen avulla

Oppitunnin alussa kannattaa korostaa eroa chatbotin ja agentin välillä. Chatbot voi vastata kysymykseen. Agentti voi hakea tietoa, muokata tiedostoa, lähettää viestin tai ajaa komennon. Tämä tekee agentista käytännöllisen, mutta samalla jokainen toiminto kasvattaa vastuuta.

> **Chatbot sanoo. Agentti tekee.** Siksi agentin työkalut täytyy suunnitella turvallisesti.

Kolme perustyökalua kannattaa esitellä opiskelijoille näin:

1. **Tiedostot:** agentti voi lukea ja kirjoittaa tietoa.
2. **Verkkohaku:** agentti voi noutaa ajankohtaista tietoa ulkoisista lähteistä.
3. **CLI:** agentti voi suorittaa komentorivikomentoja ja vaikuttaa palvelimeen tai tiedostojärjestelmään.

### Tiedostotyökalu — hyödyllinen mutta rajattava

**Tiedostotyökalu** on usein ensimmäinen konkreettinen työkalu, jonka opiskelija ymmärtää. Agentti voi lukea raportteja, CSV-tiedostoja, lokeja ja asetustiedostoja. Se voi myös kirjoittaa raportteja, lokitiedostoja tai analyysituloksia.

Tiedostojen käsittelyssä tärkeintä on erottaa **lukuoikeus**, **kirjoitusoikeus** ja **poistooikeus**.

| Oikeus | Mitä se tarkoittaa? | Opettajan painotus |
| --- | --- | --- |
| **Lukuoikeus** | Agentti voi avata ja lukea tiedostoja. | Anna pääsy vain välttämättömiin tiedostoihin ja kansioihin. |
| **Kirjoitusoikeus** | Agentti voi luoda tai muokata tiedostoja. | Rajoita kirjoitus vain erillisiin kansioihin, kuten `/reports/` tai `/temp/`. |
| **Poistooikeus** | Agentti voi poistaa tiedostoja. | Älä anna poistooikeutta, ellei se ole tehtävän kannalta ehdottoman välttämätöntä. |

**Esimerkki opetukseen**

- **Agentti saa lukea:** `/data/` ja `/customer_info/`
- **Agentti saa kirjoittaa:** `/reports/` ja `/temp/`
- **Agentti ei saa poistaa:** mitään tiedostoja

### Verkkohakutyökalu — ajankohtainen tieto ei ole aina luotettavaa

**Verkkohaku** antaa agentille pääsyn ajankohtaiseen tietoon. Tämä on hyödyllistä, jos tieto muuttuu nopeasti: hinnat, uutiset, aikataulut, ohjelmistoversiot tai ohjeet. Samalla verkkohaku tuo kolme keskeistä riskiä.

| Riski | Mitä voi tapahtua? | Miten riskiä vähennetään? |
| --- | --- | --- |
| **Väärä tieto** | Agentti löytää epäluotettavan blogin, vanhentuneen ohjeen tai virheellisen lähteen. | Käytä lähteiden whitelistiä: viralliset sivustot, dokumentaatio ja luotettavat lähteet. |
| **Kustannukset** | Agentti tekee liikaa hakuja ja aiheuttaa tarpeettomia kustannuksia. | Rajoita hakujen määrää käyttäjää, tehtävää tai päivää kohden. |
| **Yksityisyys** | Agentti hakee tai lähettää verkkoon henkilötietoja, tunnisteita tai arkaluontoista tietoa. | Estä henkilötietojen ja salaisten tietojen hakeminen tai välittäminen ulkoisiin palveluihin. |

**Opettajan huomio:** Korosta, että verkkohaku ei tee agentista automaattisesti oikeassa olevaa. Se antaa pääsyn lisätietoon, mutta lähteiden laatu, ajantasaisuus ja turvallisuus täytyy silti arvioida.

### CLI-työkalu — tehokkain ja vaarallisin

**CLI** eli komentorivi on usein riskialttein työkalu. Sen avulla agentti voi luoda kansioita, ajaa skriptejä, käynnistää palveluita tai käsitellä tiedostoja. Samalla se voi virheellisesti käytettynä poistaa tiedostoja, sammuttaa palvelimen tai muuttaa käyttöoikeuksia.

CLI-työkalua kannattaa käsitellä opetuksessa erityisen varovaisesti. Hyvä lähtökohta on, että agentti ei saa ajaa mitä tahansa komentoa. Sen sijaan käytetään **whitelist-mallia**.

| Sallittu tai kielletty | Komento | Perustelu |
| --- | --- | --- |
| **Sallittu** | `ls` | Näyttää tiedostot eikä muuta järjestelmää. |
| **Sallittu rajatusti** | `mkdir`, `cp` | Voi olla hyödyllinen, jos se rajataan turvalliseen kansioon. |
| **Kielletty** | `rm`, `rm -rf`, `sudo`, `shutdown` | Voi poistaa tiedostoja, ohittaa rajoituksia tai sammuttaa järjestelmän. |

CLI-työkalun turvallisuutta voi vahvistaa kolmella keinolla:

1. **Whitelist:** agentti saa ajaa vain ennalta sallittuja komentoja.
2. **Hiekkalaatikko:** komennot ajetaan erillisessä ympäristössä, eivät oikeassa tuotantojärjestelmässä.
3. **Hyväksyntä:** kriittiset komennot vaativat ihmisen hyväksynnän ennen suorittamista.

> **CLI:n kanssa perussääntö on:** jos et antaisi komentoa opiskelijan ajaa vapaasti oikealla palvelimella, älä anna agentinkaan ajaa sitä vapaasti.

### Orkestrointi — oikea työkalu oikeassa järjestyksessä

**Orkestrointi** tarkoittaa sitä, että agentti käyttää työkaluja oikeassa järjestyksessä. Agentti ei käytä kaikkia työkaluja sattumanvaraisesti, vaan suunnittelee, mitä tarvitaan ensin, mitä seuraavaksi ja mikä on lopputuotos.

Esimerkiksi analytiikka-agentin työkaluketju voi olla:

1. **Tiedostot:** lue perustiedot CSV-tiedostosta.
2. **Verkkohaku:** hae ajankohtainen markkinakonteksti.
3. **CLI:** aja analyysiskripti.
4. **Tiedostot:** kirjoita valmis raportti.

**Esimerkki opetukseen:** Pyydä opiskelijoita vaihtamaan työkalujen järjestystä ja arvioimaan, mikä menee pieleen. Jos raportti kirjoitetaan ennen analyysiä, raportista puuttuu sisältö. Jos verkkohaku tehdään ennen kuin tiedetään, mitä dataa analysoidaan, haku voi olla väärä tai turha.

---

## Neljä turvakerrosta työkalujen käytössä

Työkalujen käyttöön kannattaa liittää sama neljän kerroksen turvallisuusmalli, jota hyödynnetään myöhemmillä turvallisuusoppitunneilla. Tämä auttaa opiskelijaa näkemään, että turvallisuus ei ole erillinen aihe, vaan osa jokaista työkalua.

| Turvakerros | Mitä se tarkoittaa työkalujen kohdalla? | Esimerkki |
| --- | --- | --- |
| **Validointi** | Tarkista syöte ennen työkalun käyttöä. | Tiedostonimen pitää olla sallittu eikä se saa sisältää polkua `../`. |
| **Rajoitus** | Anna vain välttämätön pääsy ja käytä whitelistejä. | Agentti saa kirjoittaa vain `/reports/`-kansioon. |
| **Seuranta** | Kirjaa jokainen tärkeä työkalukutsu lokiin. | Lokitetaan, mitä komentoa ajettiin ja millä parametreilla. |
| **Palautuminen** | Suunnittele, miten virhe korjataan tai kumotaan. | Jos raportti kirjoitetaan väärin, vanha versio säilytetään varmuuskopiona. |

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”Isompi whitelist on parempi.”

**Korjaava näkökulma:** Whitelist on turvallinen vain silloin, kun se on rajattu. Mitä enemmän komentoja, kansioita tai lähteitä sallitaan, sitä enemmän vahinkoa agentti voi tehdä virhetilanteessa.

> Hyvä whitelist ei ole pitkä lista. Hyvä whitelist on juuri niin lyhyt kuin tehtävä sallii.

### Väärinkäsitys 2: ”Verkkohaku on turvallista, koska agentti vain lukee tietoa.”

**Korjaava näkökulma:** Verkkohaku voi tuoda agentille virheellistä, vanhentunutta tai manipuloitua tietoa. Jos agentti toimii löydetyn tiedon perusteella, väärä tieto voi muuttua vääräksi toiminnaksi.

### Väärinkäsitys 3: ”CLI on tehokas, joten sitä kannattaa käyttää paljon.”

**Korjaava näkökulma:** CLI on tehokas juuri siksi, että se on vaarallinen. Sitä kannattaa käyttää vain, kun se on oikeasti tarpeen, ja silloinkin hiekkalaatikossa, whitelistillä ja tarvittaessa ihmisen hyväksynnällä.

### Väärinkäsitys 4: ”Orkestrointi ei ole tärkeää.”

**Korjaava näkökulma:** Väärä työkalujen järjestys voi tuottaa virheellisen lopputuloksen. Oikea järjestys on osa agentin päättelyä ja arkkitehtuuria.

---

## Luokkatehtävien ohjeistus

### TT-A: Whitelist eri agenteille

**Tavoite:** Opiskelija suunnittelee työkalujen käyttöoikeudet turvallisesti.

**Tehtävä:** Anna opiskelijoille 2–3 agenttiesimerkkiä. Opiskelijat määrittävät, mitä tiedostoja, verkkolähteitä tai komentoja agentti saa käyttää ja mitä ei.

| Agentti | Sallitut työkalut | Kielletyt työkalut | Perustelu |
| --- | --- | --- | --- |
| Raporttiagentti | `/data/`, `/reports/`, viralliset tilastosivut | `rm`, henkilötietokansiot, satunnaiset blogit | Agentti tarvitsee dataa ja raportin kirjoitusta, mutta ei poisto-oikeuksia tai henkilötietoja. |
| Asiakastukiagentti | FAQ-tietokanta, tikettien lukeminen, vastauskanava | Palkkatiedot, sopimusten muokkaus, poistokomennot | Agentti tarvitsee asiakastuen tietoja, mutta ei organisaation sisäisiä tai kriittisiä järjestelmiä. |

**Aika-arvio:** 15–20 minuuttia

---

### TT-B: Orkestrointikaavio

**Tavoite:** Opiskelija ymmärtää työkalujen käyttöjärjestyksen merkityksen.

**Tehtävä:** Opiskelijat piirtävät työnkulkukaavion agentille, joka käyttää vähintään kahta työkalua. Kaaviossa pitää näkyä, missä vaiheessa agentti käyttää mitäkin työkalua ja mitä dataa siirtyy seuraavaan vaiheeseen.

**Ohje opiskelijalle:**

1. Mikä on agentin tehtävä?
2. Mikä tieto tarvitaan ensin?
3. Mitä työkalua käytetään ensimmäisenä?
4. Mitä seuraava työkalu tarvitsee edelliseltä?
5. Mikä on lopputulos?

**Aika-arvio:** 20–25 minuuttia

---

### TT-C: Riskit ja seuraukset

**Tavoite:** Opiskelija tunnistaa, mitä voi mennä pieleen, jos työkalut on rajattu huonosti.

**Tehtävä:** Anna opiskelijoille riskitilanteita ja pyydä heitä kuvaamaan:

1. Mitä voi tapahtua?
2. Miksi tilanne on vaarallinen?
3. Mikä rajoitus tai turvakerros vähentäisi riskiä?

| Tilanne | Mitä voi mennä pieleen? | Mikä suojaa? |
| --- | --- | --- |
| Agentti saa ajaa `rm`-komennon. | Se voi poistaa tärkeitä tiedostoja. | Komentojen whitelist ja hiekkalaatikko. |
| Agentti saa hakea tietoa mistä tahansa verkosta. | Se voi käyttää virheellistä tai manipuloitua lähdettä. | Lähteiden whitelist ja lähteiden tarkistus. |
| Agentti saa kirjoittaa mihin tahansa kansioon. | Se voi ylikirjoittaa tärkeitä tiedostoja. | Kirjoitusoikeus vain rajattuun kansioon. |

**Aika-arvio:** 15–20 minuuttia

---

### TT-D: Oikea työkalu tehtävän mukaan

**Tavoite:** Opiskelija valitsee tehtävään sopivan työkalun ja perustelee valintansa.

**Tehtävä:** Anna opiskelijoille tehtäviä ja pyydä heitä valitsemaan, tarvitaanko tiedostotyökalua, verkkohakua, CLI:tä vai jotakin muuta työkalua.

| Tehtävä | Sopiva työkalu | Perustelu |
| --- | --- | --- |
| Agentti lukee myyntiraportin ja tiivistää sen. | Tiedostotyökalu | Tieto on olemassa tiedostossa, joten agentin pitää lukea se. |
| Agentti tarkistaa uusimman ohjelmistoversion. | Verkkohaku tai HTTP Request | Tieto muuttuu ajan mukana ja pitää hakea ajantasaisesta lähteestä. |
| Agentti ajaa valmiin analyysiskriptin. | CLI tai Execute Command | Tehtävä vaatii komentoriviltä ajettavaa skriptiä. |

**Aika-arvio:** 15–20 minuuttia

---

## n8n-tutustumisharjoitus — opettajan ohje

### Tavoite

Opiskelijat näkevät ensimmäistä kertaa, miltä tekoälyagentti näyttää n8n:ssä. He eivät vielä rakenna omaa agenttia, vaan **tunnistavat osat** ja **jäljittävät tiedon kulun**. Harjoitus toimii siltana oppituntien 19–22 teorian ja oppitunnin 26 rakentamisen välillä.

### Valmistelu

1. Jaa opiskelijoille tiedosto `esimerkki-agentti.json` kurssin materiaalikansiosta.
2. Varmista, että opiskelijoilla on pääsy n8n:ään joko paikallisesti tai pilvipalvelussa.
3. Varaa harjoitukseen 15–20 minuuttia.

### Odotetut vastaukset

| Solmu | Agentin osa | Selitys |
| --- | --- | --- |
| **Chat Trigger** | Syötekäsittelijä | Ottaa vastaan käyttäjän viestin. |
| **AI Agent** | Päättelijä | Päättää, mitä viestin perusteella tehdään. |
| **Calculator** | Työkalu | Tekee laskutoimituksia agentin puolesta. |
| **HTTP Request** | Työkalu | Hakee tietoa verkosta tai ulkoisesta palvelusta. |
| **Respond to Chat** | Tulosteen muotoilija | Lähettää vastauksen käyttäjälle. |

### Jos opiskelija ei tunnista osia

Ohjaa opiskelijaa katsomaan solmun nimeä, ikonia ja paikkaa työnkulussa. Voit kysyä:

- **Chat Trigger:** Mikä käynnistää keskustelun?
- **AI Agent:** Missä kohdassa päätös tehdään?
- **Calculator:** Mikä osa tekee laskun?
- **HTTP Request:** Mikä osa hakee tietoa ulkoa?
- **Respond to Chat:** Missä vastaus palautetaan käyttäjälle?

### Yhteys teoriaan

Tämä harjoitus yhdistää oppituntien 19–22 teorian konkreettiseen n8n-käyttöliittymään. Opiskelijat palaavat tähän kokemukseen oppitunnilla 26, kun he rakentavat oman agenttinsa.

---

## CFU-kysymykset

1. **Työkalut:** Miksi agentti tarvitsee työkaluja eikä pelkkä tekstivastaus riitä?
2. **Tiedostot:** Miksi agentille ei kannata antaa poistooikeutta tiedostoihin?
3. **Verkkohaku:** Miksi verkkohaku voi olla turvallisuusriski?
4. **CLI:** Miksi komentorivityökalu on erityisen vaarallinen?
5. **Orkestrointi:** Mitä voi tapahtua, jos agentti käyttää oikeita työkaluja väärässä järjestyksessä?

---

## Opettajan vihjeet

### Jos opiskelija haluaa antaa agentille kaikki oikeudet

Kysy:

- Mitä agentti todella tarvitsee tehtävän suorittamiseen?
- Mikä on pahin asia, jonka agentti voisi tehdä vahingossa?
- Miten vahinko rajataan, jos agentti toimii väärin?

### Jos opiskelija ajattelee verkkohakua neutraalina työkaluna

Korosta, että verkkohaku tuo agentille ulkoista tietoa, jonka luotettavuus vaihtelee. Pyydä opiskelijaa määrittelemään sallitut lähteet.

### Jos opiskelija innostuu CLI-työkalusta liikaa

Palauta keskustelu riskiin. Kysy, mitä tapahtuisi, jos agentti ajaisi väärän komennon oikeassa ympäristössä.

> Tehokas työkalu tarvitsee vahvat rajat.

### Jos orkestrointi jää epäselväksi

Pyydä opiskelijaa kirjoittamaan työnkulku vaiheina:

1. Mitä tietoa tarvitaan ensin?
2. Mistä tieto haetaan?
3. Mitä työkalua käytetään seuraavaksi?
4. Mitä syntyy lopputuloksena?

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että agentin työkalut ovat sekä sen vahvuus että sen suurin riski. Tiedostot, verkkohaku ja CLI-komennot tekevät agentista toimijan, joka voi vaikuttaa ympäristöönsä. Siksi työkalut pitää valita, rajata, orkestroida ja lokittaa huolellisesti.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Mitä työkaluja oma agenttisi todella tarvitsee, ja mikä olisi vaarallisin oikeus, jonka voisit sille vahingossa antaa?

---
