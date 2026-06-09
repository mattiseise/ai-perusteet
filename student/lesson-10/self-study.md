# Kilpailuta tekoälyt — mikä työkalu mihinkin?

## Johdanto

Olet nyt saavuttanut kurssin kohdan, jossa teoria muuttuu käytännöksi. Olet oppinut, mitä tekoäly on, miten se toimii ja millaisia rajoituksia sillä on. Nyt on aika tarttua itse työkaluihin.

Huomaa, että **tekoälymallit** ja niihin perustuvat palvelut kehittyvät erittäin nopeasti. Tämän materiaalin tiedot on tarkistettu toukokuussa 2026, mutta yksittäiset mallinimet, hinnat, käyttörajat ja ominaisuudet voivat muuttua nopeasti. Tärkeintä ei ole muistaa yksittäisiä malliversioita, vaan ymmärtää työkalujen väliset erot ja osata valita tilanteeseen sopiva työkalu.

Kolme suurta kielimallipohjaista palvelua ovat **ChatGPT**, **Claude** ja **Microsoft Copilot**. Ne eivät ole sama työkalu eri nimillä, vaan ne on rakennettu eri lähtökohdista, eri tavoitteilla ja eri vahvuuksilla. Yksi painottaa monipuolisuutta ja laajaa ekosysteemiä, toinen pitkien aineistojen käsittelyä ja turvallisuusajattelua, kolmas yrityskäyttöä ja Microsoft 365 -integraatiota.

Tämän opintojakson tarkoitus on yksinkertainen: opit tunnistamaan, mikä työkalu sopii mihinkin tilanteeseen. Ammattilaisena et valitse työkalua siksi, että se on suosituin tai tutuin. Valitset sen, joka sopii parhaiten juuri siihen tehtävään, jota olet tekemässä.

---

## ChatGPT — monipuolinen yleiskäyttöinen tekoälytyökalu

ChatGPT on OpenAI:n kehittämä palvelu. Sen vahvuus on monipuolisuus: se osaa kirjoittaa, analysoida, koodata, käsitellä tiedostoja, tulkita kuvia, luoda kuvia ja käyttää verkkohakua silloin, kun ominaisuus on käytössä. Kaikki tämä tapahtuu samassa keskusteluikkunassa.

ChatGPT:stä on sekä ilmaisia että maksullisia versioita. Käytettävissä olevat mallit, viestirajat, tiedostojen käsittely, kuvien luonti, verkkohaku ja muut työkalut riippuvat siitä, mitä versiota tai organisaatiotilausta käytetään. Siksi mallin tarkka nimi tai yksittäinen käyttöraja ei ole ammattilaiselle tärkein tieto. Tärkeämpää on ymmärtää, millaiseen työskentelyyn ChatGPT soveltuu.

### Mikä tekee ChatGPT:stä erityisen?

ChatGPT:n suurin vahvuus on sen **laaja käyttöalue**. Sitä voi käyttää esimerkiksi ideointiin, tekstin muokkaamiseen, ohjelmointiin, tiedostojen analysointiin, kuvien tulkintaan, kuvien luomiseen ja verkkotiedon hakemiseen. OpenAI:n nykyiset mallit tukevat teksti- ja kuvasyötteitä, tekstivastauksia, monikielistä käyttöä ja näkökykyyn perustuvia tehtäviä.

Yksi ChatGPT:n merkittävimmistä ominaisuuksista on **Custom GPT** eli räätälöity botti. Voit luoda ChatGPT:stä erikoisversion, joka on määritetty tiettyyn tarkoitukseen. Esimerkiksi yritys voi rakentaa markkinointiassistentin, joka tuntee yrityksen brändin ja osaa kirjoittaa oikealla tyylillä. Koulutuksessa voi tehdä opiskelukaverin, joka kysyy testikysymyksiä tietystä aiheesta. Tätä ominaisuutta hyödynnät myöhemmin kurssilla, kun rakennat oman Custom GPT:n.

ChatGPT osaa myös kirjoittaa ja suorittaa Python-koodia suoraan keskusteluikkunassa, jos käytössä oleva versio sisältää siihen tarvittavat työkalut. Käytännössä tämä tarkoittaa, että voit ladata esimerkiksi CSV-tiedoston, pyytää analyysiä ja saada kaavioita automaattisesti ilman, että sinun tarvitsee avata erillistä ohjelmaa.

### Missä ChatGPT ei ole paras?

ChatGPT ei ole automaattisesti paras valinta jokaiseen tehtävään. Hyvin pitkien dokumenttien käsittelyssä kannattaa tarkistaa, mikä konteksti-ikkuna valitulla mallilla ja käyttöympäristöllä on käytettävissä. OpenAI:n API-dokumentaatiossa suurten mallien konteksti-ikkuna voi olla jopa **1 miljoona tokenia**, mutta kevyemmillä malleilla ja ChatGPT:n käyttöliittymässä rajat voivat olla erilaisia. Siksi yksittäistä pysyvää tokenimäärää ei kannata opetella ulkoa.

Tietosuojassa on tärkeää ymmärtää käytettävän tilauksen asetukset. OpenAI voi käyttää ChatGPT-keskusteluja palvelun ja mallien parantamiseen, ellei käyttäjä poista tätä asetusta käytöstä. Organisaatio- ja yrityskäytössä hallintaominaisuudet voivat olla tiukemmat kuin henkilökohtaisessa käytössä.

> **Pysähdy hetkeksi:** Oletko käyttänyt ChatGPT:tä aiemmin? Mihin tehtäviin käytit sitä? Mietitkö silloin, olisiko jokin toinen työkalu voinut olla parempi vaihtoehto?

---

## Claude — vahva pitkissä aineistoissa ja huolellisessa analyysissä

Claude on Anthropicin kehittämä kielimalli. Sen vahvuuksia ovat pitkien aineistojen käsittely, johdonmukainen tekstianalyysi, ohjelmointi ja turvallisuusajattelu. Claude on usein hyvä vaihtoehto silloin, kun käyttäjän pitää käsitellä laajoja dokumentteja, raportteja, transkriptioita tai koodikokonaisuuksia.

Claudesta on sekä ilmaisia että maksullisia versioita. Käytettävissä olevat mallit, käyttörajat, tiedostojen käsittely ja lisäominaisuudet riippuvat valitusta versiosta, organisaatiosta ja käyttöympäristöstä.

### Mikä tekee Claudesta erityisen?

Clauden tärkeä vahvuus on **pitkä konteksti-ikkuna**. Anthropicin API-dokumentaation mukaan uusimmat Claude-mallit voivat tukea jopa **1 miljoonan tokenin** konteksti-ikkunaa, kun taas osa malleista käyttää pienempää, esimerkiksi **200 000 tokenin** konteksti-ikkunaa. Tämä tarkoittaa käytännössä sitä, että Claude voi soveltua erittäin pitkien aineistojen käsittelyyn, mutta käytännön raja riippuu aina valitusta mallista ja käyttöympäristöstä.

Claude tarjoaa myös **Artifacts**-ominaisuuden, jossa koodi, teksti ja verkkosivut voivat näkyä erillisessä paneelissa. Kun Claude kirjoittaa esimerkiksi HTML-sivun, sitä voidaan tarkastella erillisenä tuotoksena keskustelun rinnalla. Tämä tekee työskentelystä sujuvampaa kuin tilanteessa, jossa kaikki sisältö on vain pitkänä chat-keskusteluna.

Koodauksessa Claude on vahva erityisesti silloin, kun tehtävä edellyttää laajan kokonaisuuden hahmottamista. Se pystyy käsittelemään monimutkaisia koodiprojekteja ja tuottamaan usein johdonmukaisia ratkaisuja. Claude on myös hyvä kuvien, kaavioiden ja taulukoiden tulkinnassa, jos käytössä oleva versio tukee kyseisiä ominaisuuksia.

### Missä Claude ei ole paras?

Claude ei ole aina paras valinta silloin, kun tarvitaan mahdollisimman laajaa ekosysteemiä, valmiita räätälöityjä botteja tai monipuolisia kuluttajakäyttöön suunnattuja lisätyökaluja. Verkkohaku on Claudessa tuettu tietyissä ympäristöissä, mutta sen saatavuus riippuu käyttöliittymästä, tilauksesta, alueesta ja organisaation asetuksista. Siksi ei kannata olettaa, että jokaisessa Claude-käytössä on automaattisesti reaaliaikainen verkkohaku.

Tietosuojan osalta Claude ei ole yksinkertaisesti ”aina turvallisin” eikä ”aina täysin koulutuksen ulkopuolella”. Kuluttajakäytössä käyttäjän asetukset ja valinnat vaikuttavat siihen, voidaanko keskusteluja käyttää mallien kehittämiseen. Yritys- ja API-käytössä ehdot voivat olla erilaiset. Ammattilaisen pitää siis tarkistaa organisaation oma sopimus ja asetukset ennen luottamuksellisen tiedon syöttämistä.

> **Pysähdy hetkeksi:** Kuvittele, että sinulla on 80-sivuinen tutkimusraportti, jonka sisällön haluat ymmärtää nopeasti. Kumpi työkalu sopisi paremmin: ChatGPT vai Claude? Miksi?

---

## Microsoft Copilot — yritysmaailman ja Microsoft 365 -ympäristön työkalu

Microsoft Copilot edustaa kolmatta lähestymistapaa. Se ei ole vain yksi chat-ikkuna, vaan Microsoftin tuotteisiin kytkeytyvä tekoälyratkaisu. Copilotin arvo syntyy erityisesti siitä, miten se liittyy Microsoft 365 -ympäristöön: Wordiin, Exceliin, PowerPointiin, Outlookiin, Teamsiin, SharePointiin ja Microsoft Graphiin.

Copilotista on erilaisia versioita kuluttajille, organisaatioille ja Microsoft 365 -ympäristöihin. Käytettävissä olevat ominaisuudet riippuvat lisenssistä, organisaation asetuksista ja siitä, käytetäänkö Copilotia selaimessa, Microsoft 365 -sovelluksissa vai Copilot Studio -ympäristössä.

### Mikä tekee Copilotista erityisen?

Copilotin selkein vahvuus on **Microsoft 365 -integraatio**. Kun työskentelet Wordissa, Copilot voi auttaa dokumentin kirjoittamisessa ja muokkaamisessa. Excelissä se voi auttaa datan tarkastelussa ja taulukoiden tulkinnassa. PowerPointissa se voi tukea esitysten suunnittelua. Outlookissa se voi auttaa viestien kirjoittamisessa ja tiivistämisessä. Teamsissa se voi auttaa kokousten ja keskustelujen käsittelyssä.

Microsoft 365 Copilot toimii Microsoft 365 -palvelurajojen sisällä ja käyttää Microsoft Graphia hakeakseen organisaation tietoja käyttäjän oikeuksien perusteella. Se ei siis saa automaattisesti pääsyä kaikkeen organisaation dataan, vaan sen pitäisi noudattaa samoja käyttöoikeuksia kuin käyttäjänkin. Tämä on tärkeä ero verrattuna yleiseen verkkopohjaiseen tekoälytyökaluun.

Yritysmaailmassa Copilotin vahvuuksia ovat hallinta, käyttöoikeudet, tietoturva ja vaatimustenmukaisuus. Microsoftin dokumentaation mukaan Microsoft 365 Copilotin promptteja, vastauksia ja Microsoft Graphin kautta käytettyä dataa ei käytetä Microsoftin perusmallien kouluttamiseen.

### Missä Copilot ei ole paras?

Copilot ei ole aina paras valinta monimutkaiseen koodaukseen, vapaaseen luovaan ideointiin tai hyvin syvälliseen yksittäisen pitkän dokumentin analyysiin. Sen vahvuus on ennen kaikkea Microsoft 365 -ympäristössä toimiminen. Jos et käytä Microsoftin tuotteita tai organisaatiosi data ei ole Microsoft 365 -ympäristössä, Copilotin hyöty voi jäädä pienemmäksi.

Microsoft ei ilmoita Microsoft 365 Copilotille yhtä pysyvää julkista tokenmäärää samalla tavalla kuin monet mallien API-dokumentaatiot ilmoittavat. Copilotin käytännön rajat riippuvat sovelluksesta, lisenssistä, valitusta mallista, organisaation asetuksista ja siitä, miten tietoa haetaan Microsoft Graphin kautta. Siksi aiempi väite yhdestä kiinteästä Copilotin konteksti-ikkunasta oli liian yksinkertainen.

> **Pysähdy hetkeksi:** Monet yritykset käyttävät jo Microsoft 365:tä. Millä tavalla Copilot voisi auttaa tavallisessa toimistopäivässä? Entä milloin se ei riittäisi?

---

## Käytännön vertailu: sama tehtävä, kolme vastausta

Paras tapa ymmärtää työkalujen erot on antaa niille sama tehtävä ja katsoa, mitä tapahtuu.

Kuvittele, että sinulla on 40-sivuinen tutkimusraportti PDF-muodossa ja haluat ymmärtää sen nopeasti. ChatGPT voi olla hyvä valinta, jos haluat yhdistää dokumenttianalyysin, verkkotiedon hakemisen, taulukoiden käsittelyn ja mahdollisen datan visualisoinnin. Sen vahvuus on monipuolinen työskentely samassa keskustelussa.

Claude voi olla hyvä valinta silloin, kun haluat käsitellä pitkää dokumenttia kokonaisuutena ja saada siitä huolellisen, tekstilähtöisen analyysin. Pitkä konteksti-ikkuna voi auttaa silloin, kun aineistoa on paljon ja kokonaiskuvan säilyminen on tärkeää.

Copilot voi olla hyvä valinta silloin, kun raportti on osa Microsoft 365 -ympäristöä, esimerkiksi SharePointissa, Teamsissa tai OneDrivessa, ja haluat yhdistää sen tiedot muihin organisaation dokumentteihin, sähköposteihin tai kokouksiin käyttöoikeuksiesi rajoissa.

Yksinkertaistettuna: **Claude** on usein vahva pitkien aineistojen analyysissä, **ChatGPT** on monipuolinen yleistyökalu ja **Copilot** on vahva Microsoft 365 -integraatioissa. Oikea vastaus riippuu kuitenkin aina tilanteesta.

---

## Hinnoittelu ja tietosuoja

Kaikista kolmesta palvelusta on erilaisia versioita eri käyttäjäryhmille. Hinnat, käyttörajat ja ominaisuudet muuttuvat usein, joten niitä ei kannata opetella pysyvinä faktoina. Ammattilaisen kannattaa tarkistaa ajantasainen hinta aina palvelun omalta hinnastosivulta ennen hankintapäätöstä.

Ilmaisversiot sopivat kokeiluun ja opiskeluun, mutta niissä on yleensä rajoituksia esimerkiksi viestimäärissä, mallien saatavuudessa, tiedostojen käsittelyssä tai lisäominaisuuksissa. Maksulliset kuluttajaversiot tarjoavat tavallisesti paremmat käyttörajat ja enemmän ominaisuuksia. Yritysversioissa korostuvat hallinta, tietoturva, käyttäjähallinta ja sopimusehdot.

### Tietosuoja — mihin datasi menee?

**Tietosuoja** on ammatillisesti kriittinen kysymys. Kun käytät tekoälypalvelua, sinun pitää tietää ainakin kolme asiaa: tallentuuko syöttämäsi tieto, käytetäänkö sitä mallien kehittämiseen ja kuka voi hallita tai poistaa sen.

ChatGPT:ssä käyttäjä voi hallita data-asetuksiaan. OpenAI kertoo, että käyttäjä voi valita, käytetäänkö keskusteluja mallien parantamiseen. Tämä tarkoittaa, että henkilökohtaisessa käytössä asetukset pitää tarkistaa itse ennen luottamuksellisen tiedon syöttämistä.

Clauden tietosuojakäytännöt riippuvat käyttäjätyypistä ja asetuksista. Anthropic on muuttanut kuluttajakäytön ehtoja niin, että käyttäjän valinnoilla on merkitystä siihen, voidaanko dataa käyttää mallien kehittämiseen. Yritys-, koulutus- ja API-käytössä ehdot voivat poiketa kuluttajakäytöstä.

Microsoft 365 Copilotissa keskeinen ero on, että palvelu toimii organisaation Microsoft 365 -ympäristössä ja noudattaa käyttäjän käyttöoikeuksia. Microsoftin dokumentaation mukaan Microsoft 365 Copilotin promptteja, vastauksia ja Microsoft Graphin kautta käytettyä dataa ei käytetä perusmallien kouluttamiseen.

Yleinen sääntö on yksinkertainen: älä syötä tekoälypalveluun asiakastietoja, henkilötietoja, salasanoja, liikesalaisuuksia tai muuta luottamuksellista tietoa, ellei organisaatiosi ole hyväksynyt työkalua kyseiseen käyttöön.

> **Pysähdy hetkeksi:** Jos yrityksesi käsittelee arkaluontoista asiakastietoa, millä perusteella valitsisit työkalun? Mitä tietosuojakysymyksiä ottaisit huomioon?

---

## Milloin mikäkin — valintaperusteet käytännössä

Ammattilaisena et kysy ”mikä on paras tekoäly?”, vaan ”mikä on paras tekoäly *tähän tehtävään*?”. Valinta riippuu siitä, mitä teet, missä ympäristössä työskentelet, kuka maksaa ja millaisia vaatimuksia organisaatiollasi on.

**ChatGPT** on vahva valinta silloin, kun tarvitset monipuolisuutta: luovaa kirjoittamista, ideointia, kuvien käsittelyä, nopeita prototyyppejä, koodiapua, tiedostojen analysointia tai verkkotiedon hakemista. Sen ekosysteemi on laaja, ja sitä voi käyttää hyvin monenlaisiin tehtäviin.

**Claude** on vahva valinta silloin, kun käsittelet pitkiä dokumentteja, tarvitset johdonmukaista analyysiä tai teet monimutkaista koodiin tai tekstiin liittyvää työtä. Sen pitkät konteksti-ikkunat voivat olla merkittävä etu laajoissa aineistoissa.

**Copilot** on vahva valinta silloin, kun työskentelet Microsoft 365 -ympäristössä ja haluat tekoälyn auttavan suoraan dokumenteissa, taulukoissa, esityksissä, sähköposteissa, kokouksissa ja organisaation tiedon hyödyntämisessä käyttöoikeuksiesi mukaisesti.

### Vertailutaulukko

| Kriteeri | ChatGPT | Claude | Copilot |
| --- | --- | --- | --- |
| **Konteksti-ikkuna** | Riippuu mallista ja käyttöympäristöstä; OpenAI:n API:ssa suuret mallit voivat tukea jopa 1M tokenia. | Riippuu mallista; Anthropic ilmoittaa osalle malleista 200K ja osalle jopa 1M tokenin konteksti-ikkunan. | Microsoft ei ilmoita yhtä pysyvää julkista tokenmäärää Microsoft 365 Copilotille; käytännön rajat riippuvat sovelluksesta, lisenssistä ja toteutuksesta. |
| **Hinnoittelu** | Ilmainen ja maksullisia versioita; hinnat ja rajat muuttuvat, joten tarkista ajantasainen hinnasto. | Ilmainen ja maksullisia versioita; hinnat ja rajat muuttuvat, joten tarkista ajantasainen hinnasto. | Kuluttaja-, organisaatio- ja Microsoft 365 -lisensseihin liittyviä versioita; hinta riippuu lisenssistä. |
| **Verkkohaku** | Kyllä, kun ominaisuus on käytössä. | Kyllä tietyissä tuetuissa ympäristöissä; saatavuus riippuu käyttöympäristöstä ja asetuksista. | Kyllä, erityisesti Copilot Chatissa ja verkkopohjaisissa käyttötapauksissa. |
| **Office- ja työympäristöintegraatio** | Rajoitettu verrattuna Copilotiin; tiedostoja voi käsitellä, mutta ei ole Microsoft 365:n natiivi osa. | Rajoitettu verrattuna Copilotiin; vahva erillisessä analyysissä ja tekstityössä. | Erittäin vahva Microsoft 365 -ympäristössä. |
| **Tyypillinen vahvuus** | Monipuolinen yleiskäyttö, ideointi, kirjoittaminen, koodaus, tiedostoanalyysi ja multimodaaliset tehtävät. | Pitkät aineistot, huolellinen analyysi, koodikokonaisuudet ja johdonmukainen tekstityö. | Microsoft 365 -dokumentit, organisaation data, kokoukset, sähköpostit ja yrityskäyttö. |
| **Datan käyttö mallien kehittämiseen** | Riippuu asetuksista ja tilauksesta; käyttäjä voi hallita data-asetuksia. | Riippuu käyttäjätyypistä, asetuksista ja sopimuksesta; kuluttajakäytössä käyttäjän valinnoilla on merkitystä. | Microsoft 365 Copilotin promptteja, vastauksia ja Graph-dataa ei käytetä perusmallien kouluttamiseen. |

---

## Käytännön kokeilu

Paras tapa oppia on kokeilla itse. Valitse tehtävä, joka on riittävän monimutkainen, jotta työkalujen erot tulevat näkyviin. Tehtävä voi olla esimerkiksi 500 sanan artikkelin kirjoittaminen, CSV-datan analysointi, pitkän tekstin tiivistäminen tai Python-funktion laatiminen. Anna sama tehtävä kaikille kolmelle työkalulle ja vertaa tuloksia.

Kiinnitä huomiota ainakin seuraaviin kysymyksiin:

- Mikä työkalu oli nopein?
- Mikä antoi tarkimman vastauksen?
- Minkä työkalun tulos oli käytännöllisin omaan tarpeeseesi?
- Mikä työkalu perusteli vastauksensa selkeimmin?
- Mikä työkalu kertoi parhaiten, mistä tieto oli peräisin?
- Mikä työkalu teki virheitä tai väitti asioita liian varmasti?

Dokumentoi havaintosi. Tämän kokeilun jälkeen sinulla on todellinen, omakohtainen käsitys siitä, mitkä ovat kunkin työkalun vahvuudet ja heikkoudet juuri sinun käyttötilanteissasi.

---

## Kohti omaa projektia

Tällä tunnilla vertailit ChatGPT:tä, Claudea ja Copilotia sekä tunnistit niiden vahvuuksia ja rajoituksia. Tehtävissä valitsit alustan ja käyttötapauksen omalle botillesi (**Botin rakennuspala 1**). Tämä valinta on perusta kaikelle, mitä rakennat seuraavilla tunneilla. Kun tiedät, missä alustassa bottisi toimii ja ketä se palvelee, voit seuraavaksi suunnitella, miten annat sille oikean kontekstin eli miten ohjeistat sen ymmärtämään käyttäjän tilanteen.

## Yhteenveto

Kolmesta suuresta kielimallipohjaisesta palvelusta jokainen on rakennettu hieman erilaiseen tarpeeseen. ChatGPT on monipuolinen yleiskäyttöinen työkalu, jonka vahvuus on laaja työkalupakki. Claude on vahva pitkissä aineistoissa, huolellisessa analyysissä ja koodikokonaisuuksissa. Copilot on Microsoft 365 -ympäristön työkalu, joka tuo tekoälyn suoraan organisaation dokumentteihin, viestintään ja työprosesseihin.

Ammattilaisena sinun ei tarvitse valita vain yhtä työkalua. Tärkeämpää on ymmärtää kaikkien kolmen vahvuudet ja rajoitukset. Kun tiedät, mihin kukin työkalu sopii, osaat valita oikean työkalun oikeaan tilanteeseen. Se on ammattitaitoa.

---
