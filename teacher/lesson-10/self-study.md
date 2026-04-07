# Työkalupaletti — ChatGPT, Claude ja Copilot käytännössä

## Johdanto

Olet nyt saavuttanut kurssin kohdan, jossa teoria muuttuu käytännöksi. Olet oppinut, mitä tekoäly on, miten se toimii ja mitä rajoituksia sillä on. Nyt on aika tarttua itse työkaluihin.

Huomaa, että tekoälymallit kehittyvät erittäin nopeasti. Tämän materiaalin tiedot vastaavat maaliskuun 2026 tilannetta. On hyvin todennäköistä, että kun luet tätä, mallit ovat jo kehittyneet merkittävästi. Tärkeintä ei ole muistaa yksittäisiä mallinimiä tai versionumeroita, vaan ymmärtää erot työkalujen välillä ja osata valita tilanteeseen sopiva.

Kolme suurta kielimallipohjista palvelua hallitsevat tällä hetkellä markkinaa: ChatGPT, Claude ja Microsoft Copilot. Nämä eivät ole sama työkalu eri nimillä — ne on rakennettu eri lähtökohdista, eri tavoitteilla ja eri vahvuuksilla. Yksi painottaa monipuolisuutta ja laajaa ekosysteemiä, toinen turvallisuutta ja tarkkuutta, kolmas yrityskäyttöä ja Office-integraatiota.

Tämän opintojakson tarkoitus on yksinkertainen: opit tunnistamaan, mikä työkalu sopii mihinkin tilanteeseen. Ammattilaisena et valitse työkalua siksi, että se on suosituin tai tutuin. Valitset sen, joka sopii parhaiten siihen tehtävään, jonka juuri nyt teet.

---

## ChatGPT — suosituin ja monipuolisin

ChatGPT on OpenAI:n kehittämä palvelu, ja se on tällä hetkellä maailman tunnetuin tekoälytyökalu. Sen suosio perustuu helppokäyttöisyyteen ja monipuolisuuteen: se osaa kirjoittaa, analysoida, koodata, luoda kuvia ja selata verkkoa — kaikki saman keskusteluikkunassa.

ChatGPT:stä on useita versioita. Ilmainen versio käyttää kevyempää mallia ja siinä on rajoituksia. Plus-versio (noin 20 euroa kuussa) avaa käyttöön tehokkaimman mallin (GPT-5.4), Go-versio (8 euroa kuussa) tarjoaa nopeamman ja kevyemmän vaihtoehdon, ja Pro-versio (200 euroa kuussa) on entusiastikoille ja ammattilaisille. Organisaatioille on oma Team-versio, jossa on jaettu työtila ja hallintaominaisuudet.

### Mikä tekee ChatGPT:stä erityisen?

ChatGPT:n suurin vahvuus on sen laajuus. GPT-5.4 ymmärtää tekstiä, kuvia, ääntä ja videoita, joten sille voi antaa hyvin erilaisia tehtäviä. Se on erityisen hyvä luovissa tehtävissä, kuten mainostekstien kirjoittamisessa tai ideoinnissa, mutta pärjää hyvin myös analyyttisissä tehtävissä, kuten datan käsittelyssä ja raportoinnissa.

Yksi ChatGPT:n merkittävimmistä ominaisuuksista on Custom GPT eli räätälöity botti. Voit luoda ChatGPT:stä erikoisversion, joka on konfiguroitu tiettyyn tarkoitukseen. Esimerkiksi yritys voi rakentaa markkinointiassistenttia, joka tuntee yrityksen brändin ja osaa kirjoittaa oikealla tyylillä. Koulutuksessa voi tehdä koulutuskaveria, joka kysyy testikysymyksiä tietystä aiheesta. Tätä ominaisuutta hyödynnät myöhemmin kurssilla, kun rakennat oman Custom GPT:n.

ChatGPT osaa myös kirjoittaa ja suorittaa Python-koodia suoraan keskusteluikkunassa. Käytännössä tämä tarkoittaa, että voit ladata esimerkiksi CSV-tiedoston, pyytää analyysiä ja saada kaavioita automaattisesti — ilman, että sinun tarvitsee avata erillistä ohjelmaa. Lisäksi ChatGPT Plus pystyy selaamaan internetiä reaaliajassa, joten se voi hakea tuoretta tietoa eikä vain nojaa koulutusaikaiseen tietoonsa.

### Missä ChatGPT ei ole paras?

ChatGPT:n konteksti-ikkuna on 272 000 tokenia, ja sitä voidaan laajentaa jopa 1 miljoonaan tokeniin. Se kuulostaa suurelta, mutta se on silti pienempi kuin Clauden vakioarvoinen konteksti-ikkuna. Pitkien dokumenttien käsittelyssä tämä ero näkyy. ChatGPT:n turvallisuuslähestymistapa on myös vapaampi kuin Clauden — se antaa enemmän vapautta, mutta samalla valvontaa on vähemmän. Ilmainen versio on saatavilla, mutta Plus-, Go- ja Pro-versiot tarjoavat paremmat ominaisuudet ja suuremmat rajat.

> **Pysähdy hetkeksi:** Oletko käyttänyt ChatGPT:tä aiemmin? Mihin tehtäviin käytit sitä? Mietitkö koskaan, olisiko jokin toinen työkalu voinut olla parempi vaihtoehto?

---

## Claude — turvallisuus ja tarkkuus edellä

Claude on Anthropicin kehittämä kielimalli, ja se edustaa erilaista filosofiaa kuin ChatGPT. Siinä missä ChatGPT painottaa monipuolisuutta, Claude painottaa turvallisuutta, tarkkuutta ja rehellisyyttä. Tämä näkyy käytännössä: Claude sanoo useammin "en tiedä" sen sijaan että keksisi vastauksen. Se on rakennettu perusperiaatteella "turvallisuus ensin".

Claudesta on ilmainen versio (Sonnet 4.6 -malli) ja Pro-versio (noin 20 euroa kuussa), joka avaa käyttöön tehokkaimman mallin (Opus 4.6) ja suuremmat käyttörajat. Kehittäjille on myös API-versio, jossa maksetaan käytön mukaan.

### Mikä tekee Claudesta erityisen?

Clauden selkein tekninen etu on sen pitkä konteksti-ikkuna: 1 000 000 tokenia nyt vakiohinnalla. Käytännössä tämä tarkoittaa, että Claude pystyy lukemaan ja analysoimaan erittäin pitkiä dokumentteja kerralla — kokonaisia romaaneja, suuria koodilataajoja tai tuntien mittaisia transkriptioita. Siinä missä muut mallit joutuvat pilkkomaan pitkiä dokumentteja osiin, Claude käsittelee ne kokonaisuutena ja säilyttää kokonaiskuvan.

Claude tarjoaa Artifacts-ominaisuuden, jossa koodi, teksti ja verkkosivut näkyvät erillisessä paneelissa. Kun Claude kirjoittaa vaikkapa HTML-sivun, se renderöityy suoraan näkyviin — työskentelystä tulee sujuvampaa kuin pitkissä chat-virroissa. Projects-ominaisuus puolestaan antaa sinun järjestää keskustelut ja tiedostot projektikohtaisesti, jolloin Claude muistaa kontekstin paremmin.

Koodauksessa Claude on erityisen vahva. Se pystyy käsittelemään monimutkaisia koodiprojekteja ja antaa tarkkoja, johdonmukaisia ratkaisuja. Claude on myös hyvä kuvien ymmärtämisessä: kaavioiden, graafien ja taulukoiden tulkinnassa se suoriutuu erityisen hyvin.

### Missä Claude ei ole paras?

Claude ei pysty selaamaan internetiä, joten kaikki tieto täytyy tulla käyttäjältä. Sen ekosysteemi ja integrointimahdollisuudet ovat pienemmät kuin ChatGPT:llä, vaikka ne kasvavat nopeasti. Joissakin luovissa tehtävissä, joissa tarvitaan vapaampaa ideointia, ChatGPT voi olla monipuolisempi.

> **Pysähdy hetkeksi:** Kuvittele, että sinulla on 80-sivuinen tutkimusraportti, jonka sisällön haluat ymmärtää nopeasti. Kumpi työkalu sopisi paremmin — ChatGPT vai Claude? Miksi?

---

## Microsoft Copilot — yritysmaailman valinta

Microsoft Copilot edustaa kolmatta lähestymistapaa. Se ei yritä olla paras yleiskäyttöinen tekoäly vaan paras *integroitu* tekoäly. Copilotin arvo syntyy siitä, miten syvästi se on kytketty Microsoftin tuotteisiin: Wordiin, Exceliin, PowerPointiin ja Outlookiin.

Copilotilla on ilmainen web-versio, jossa on perusominaisuudet ja Bing-integraatio. Pro-versio (noin 20 euroa kuussa) tarjoaa paremman suorituskyvyn. Yrityksille on oma Microsoft 365 Copilot, joka tuo tekoälyn suoraan kaikkiin Office-sovelluksiin.

### Mikä tekee Copilotista erityisen?

Copilotin selkein vahvuus on sen Bing-integraatio ja Microsoft 365 -integraatio. Bing-integraatio tarkoittaa, että Copilot pystyy hakemaan tietoa verkosta reaaliajassa ja viittaamaan lähteisiin. Se ei vain kerro asioita — se näyttää, mistä tieto tulee. Tämä on tärkeää silloin, kun tarvitset luotettavaa ja ajantasaista tietoa.

Microsoft 365 -integraatio on kuitenkin se, mikä tekee Copilotista ainutlaatuisen. Kun työskentelet Wordissa, Copilot voi auttaa suoraan dokumentissa: kirjoittaa, muokata ja luoda sisältöä. Excelissä se analysoi dataa, luo kaavioita ja tekee pivot-taulukoita. PowerPointissa se auttaa esitysten suunnittelussa. Outlookissa se kirjoittaa sähköpostivastauksia ja auttaa viestien priorisoinnissa. Tällaista syvää integraatiota muilla työkaluilla ei ole.

Yritysmaailmassa Copilotin turvallisuusominaisuudet ovat merkittävät. Microsoft 365 Copilotissa data pysyy organisaation sisällä, kertakirjautuminen (SSO) toimii ja vaatimustenmukaisuussertifikaatit (kuten GDPR ja SOC 2) ovat kunnossa. Jos organisaatiosi käyttää jo Microsoftin tuotteita, Copilot on luonnollinen valinta.

### Missä Copilot ei ole paras?

Teknisesti Copilot ei ole yhtä tehokas kuin ChatGPT:n GPT-5.4 tai Clauden Opus 4.6 -malli. Se ei ole paras valinta monimutkaisiin koodaustehtäviin tai syvälliseen dokumenttianalyysiin. Copilotin arvo syntyy nimenomaan integraatiosta — jos et käytä Microsoftin tuotteita, hyöty jää pienemmäksi. Enterprise-tason Copilot on myös kallis organisaatioille.

> **Pysähdy hetkeksi:** Monet yritykset käyttävät jo Microsoft 365:tä. Millä tavalla Copilot voisi auttaa tavallisessa toimistopäivässä? Entä milloin se ei riittäisi?

---

## Käytännön vertailu: sama tehtävä, kolme vastausta

Paras tapa ymmärtää työkalujen erot on antaa niille sama tehtävä ja katsoa, mitä tapahtuu.

Kuvittele, että sinulla on 40-sivuinen tutkimusraportti PDF-muodossa ja haluat ymmärtää sen nopeasti. ChatGPT lataa PDF:n, analysoi sen nopeasti ja antaa hyvän yhteenvedon. Jos käytät Code Interpreter -ominaisuutta, se voi luoda visualisointeja datasta. Lisäksi se voi hakea verkosta taustatietoa, jos raportin aihe liittyy ajankohtaisiin tapahtumiin.

Claude puolestaan pystyy lukemaan koko dokumentin kerralla pitkän konteksti-ikkunansa ansiosta. Se antaa tyypillisesti perusteellisemman analyysin ja tarkempia viittauksia itse dokumenttiin — ei pelkkiä yleistyksiä. Jos raportissa on kaavioita tai taulukoita, Claude osaa analysoida ne visuaalisesti erityisen hyvin.

Copilot lähestyy tehtävää eri kulmasta. Jos raportti on SharePointissa, Copilot osaa löytää siihen liittyviä verkkoresursseja ja viitteitä. Se on parhaimmillaan, kun haluat yhdistää raportin tiedot muihin Office-dokumentteihin tai kun tarvitset lähdeviittauksia.

Yksinkertaistettuna: Claude on paras syvälliseen analyysiin, ChatGPT on monipuolisin ja Copilot on paras yritysintegraatioihin. Mutta oikea vastaus riippuu aina kontekstista.

---

## Hinnoittelu ja tietosuoja

Kaikki kolme palvelua tarjoavat ilmaisen version, ja kaikkien maksullinen versio on suurin piirtein samassa hintaluokassa — noin 20 euroa kuukaudessa. Ilmaisversioissa on eri rajoituksia: ChatGPT:n ilmaisversio käyttää kevyempää mallia, Clauden ilmaisversiossa on viestirajoitus ja Copilotin ilmaisversio on sidottu Bing-hakuun.

API-hinnoittelu on kehittäjille merkittävämpi. Sekä OpenAI että Anthropic laskuttavat miljoonaa input-tokenia kohti, ja hinnat vaihtelevat mallista riippuen. Microsoftin enterprise-hinnoittelu on tapauskohtainen.

### Tietosuoja — mihin datasi menee?

Tietosuoja on ammatillisesti kriittinen kysymys. Kun kirjoitat jotain ChatGPT:lle, keskustelu tallentuu OpenAI:n palvelimille. Oletusarvoisesti OpenAI käyttää keskusteluja mallin parantamiseen, ellei käyttäjä itse poista tätä asetusta. Business-asiakkailla on tiukempi kontrolli.

Clauden lähestymistapa on erilainen. Anthropic ei käytä käyttäjien keskusteluja mallin harjoittamiseen. Tämä on perustavanlaatuinen periaate, joka tekee Claudesta houkuttelevan vaihtoehdon silloin, kun käsitellään luottamuksellista tietoa.

Copilot M365 -versiossa data pysyy organisaation sisällä eikä lähde Microsoftin ulkopuolelle ilman lupaa. Web-versiossa Bing saa hakutiedot, mutta ne eivät jää henkilöön liitettyinä.

Kaikki kolme noudattavat GDPR-asetusta, mutta toteutus vaihtelee. OpenAI:lla on ollut kitkaa eurooppalaisten tietosuojaviranomaisten kanssa, Anthropic noudattaa tiukkaa linjaa ja Microsoftilla on laajimmat vaatimustenmukaisuussertifikaatit.

> **Pysähdy hetkeksi:** Jos yrityksesi käsittelee arkaluontoista asiakastietoa, millä perusteella valitsisit työkalun? Mitä tietosuojakysymyksiä ottaisit huomioon?

---

## Milloin mikäkin — valintaperusteet käytännössä

Ammattilaisena et kysy "mikä on paras tekoäly?" vaan "mikä on paras tekoäly *tähän tehtävään*?" Valinta riippuu siitä, mitä teet, missä ympäristössä työskentelet, kuka maksaa ja mitä vaatimuksia organisaatiollasi on.

ChatGPT on vahvin valinta silloin, kun tarvitset monipuolisuutta: luovaa kirjoittamista, kuvien generointia, nopeita prototyyppejä tai verkkotiedon hakemista. Sen ekosysteemi on laajin ja lisäosavalikoimaa on eniten.

Claude on paras valinta silloin, kun käsittelet pitkiä dokumentteja, tarvitset tarkkuutta ja johdonmukaisuutta tai kun turvallisuus ja yksityisyys ovat prioriteetteja. Koodauksessa se on erityisen vahva monimutkaisissa projekteissa.

Copilot on oikea valinta silloin, kun työskentelet Microsoft 365 -ympäristössä ja haluat tekoälyn auttavan suoraan dokumenteissa, taulukoissa ja esityksissä. Yritysturvallisuus ja lähdeviittaukset ovat sen vahvuuksia.

### Vertailutaulukko

| Kriteeri | ChatGPT | Claude | Copilot |
|---------|---------|--------|---------|
| **Kontekstikoko** | 272K tokenia (jopa 1M) | 1M tokenia | 32K tokenia |
| **Hinta/kk** | ~20 € (Plus), ~8 € (Go), ~200 € (Pro) | ~20 € (Pro) | ~20 € (Pro) |
| **Web-selaus** | Kyllä | Ei | Kyllä |
| **Office-integraatio** | Ei | Ei | Erinomainen |
| **Turvallisuuden painotus** | Perus | Korkea | Enterprise |
| **Datan käyttö malliin** | Kyllä (opt-out) | Ei | Ei |

---

## Käytännön kokeilu

Paras tapa oppia on kokeilla itse. Valitse tehtävä, joka on riittävän monimutkainen, jotta erot näkyvät: vaikkapa 500 sanan artikkeli, CSV-datan analysointi tai Python-funktion kirjoittaminen. Anna sama tehtävä kaikille kolmelle työkalulle ja vertaa tuloksia. Mikä oli nopein? Kuka antoi tarkkaimman vastauksen? Kenen tulos oli käytännöllisin omaan tarpeeseesi?

Dokumentoi havaintosi. Tämän tutkimuksen jälkeen sinulla on todellinen, omakohtainen käsitys siitä, mitkä ovat kunkin työkalun vahvuudet ja heikkoudet juuri sinun käyttötilanteissasi.

---

## Yhteenveto

Kolmesta suuresta kielimallista jokainen on rakennettu erilaiseen tarpeeseen. ChatGPT on monipuolisin ja sen ekosysteemi on laajin. Claude on turvallisin, tarkin ja parhaimmillaan pitkien dokumenttien ja monimutkaisen koodin kanssa. Copilot on yritysmaailman integraatiotyökalu, joka tuo tekoälyn suoraan Office-sovelluksiin.

Ammattilaisena sinun ei tarvitse valita yhtä — tarvitset ymmärryksen kaikista kolmesta. Kun tiedät, mihin kukin on hyvä, osaat valita oikean työkalun oikeaan tilanteeseen. Se on ammattitaitoa.
