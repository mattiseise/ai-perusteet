### Kädet saveen — n8n-agenttipaja alkaa

# Kädet saveen — n8n-agenttipaja alkaa

## Johdanto: teoriasta tekemiseen

Olet oppinut, mitä agentit ovat, miten ne päättelevät, miten niitä turvataan ja miten ne eroavat tavallisista ohjelmista. Olet myös kerännyt matkan varrella **viisi pohjapiirrosta** tunneilta 19, 21, 23, 24 ja 25. Ne muodostavat suunnitelman omasta agentistasi. Tällä tunnilla kokoat pohjapiirrokset yhteen, tutustut n8n:ään ja rakennat agenttisi ensimmäisen toimivan version.

**n8n** lausutaan ”n-eight-n”. Se on avoimen lähdekoodin automaatioalusta, jossa rakennat työnkulkuja visuaalisesti vetämällä ja pudottamalla **solmuja** eli nodeja kankaalle. Jokainen solmu tekee yhden asian: vastaanottaa viestin, kutsuu tekoälyä, lukee tiedoston tai lähettää sähköpostin. Solmujen välille vedetään yhteys, ja data virtaa automaattisesti solmusta toiseen. Voit ajatella sitä putkirakennelmana, jossa jokainen mutka tekee jotakin hyödyllistä.

Miksi juuri n8n? Koska se poistaa yhden suurimmista esteistä agentin rakentamisessa: sinun ei tarvitse osata ohjelmoida kaikkea käsin. Kaikki, mitä olet oppinut agentin rakenteesta — **syötekäsittely**, **päättely**, **työkalut**, **muisti**, **turvakerrokset** ja **palautesilmukka** — voidaan toteuttaa n8n:ssä visuaalisesti. Näet agentin arkkitehtuurin konkreettisesti solmuina ja yhteyksinä.

**Pysähdy hetkeksi:** Mieti jotakin toistuvaa tehtävää arjessasi tai koulussa. Voisiko kone hoitaa sen puolestasi, jos sillä olisi pääsy oikeisiin työkaluihin?

## n8n:n perusteet — solmut, yhteydet ja triggerit

Kun avaat n8n:n ensimmäistä kertaa, näet tyhjän kankaan. Kaikki alkaa **triggeristä** eli solmusta, joka käynnistää työnkulun. Triggeri voi olla esimerkiksi ajastin, kuten ”joka maanantai klo 8”, webhook, kuten ”kun joku lähettää viestin”, tai manuaalinen käynnistys, kuten ”kun painan käynnistä”. Ilman triggeriä työnkulku ei lähde liikkeelle.

Triggerin jälkeen lisäät **toimintasolmuja**. Jokainen solmu saa dataa edelliseltä solmulta ja antaa dataa seuraavalle solmulle. Esimerkiksi työnkulku voi edetä näin: triggeri vastaanottaa Discord-viestin → HTTP Request -solmu lähettää viestin tekoäly-API:lle → seuraava solmu muotoilee vastauksen → viimeinen solmu lähettää vastauksen takaisin Discordiin. Tämä on yksinkertainen agentti: se ottaa vastaan syötteen, käsittelee sen tekoälyn avulla ja toimii tuloksen perusteella.

n8n:ssä on satoja valmiita integraatioita, kuten Google Sheets, Slack, Discord, sähköposti, tiedostot, tietokannat, HTTP-kutsut sekä tekoälypalvelut, kuten OpenAI ja Claude. Sinun ei tarvitse tietää kaikkien näiden palveluiden teknisiä yksityiskohtia. n8n hoitaa yhteydet puolestasi. Sinun tehtäväsi on päättää, mitä solmuja käytät ja missä järjestyksessä.

**Pysähdy hetkeksi:** Miten n8n:n solmut vastaavat agentin kuutta komponenttia, jotka opit tunnilla 19? Mieti, mikä solmu olisi syötekäsittelijä, mikä päättelijä ja mikä työkalujen suorittaja.

## Agentin kuusi komponenttia n8n:ssä

Palataan hetkeksi tunnin 19 arkkitehtuuriin ja katsotaan, miten se toteutuu n8n:ssä konkreettisesti. Tämä on tärkeää, koska tunnilla 27 dokumentoit agenttisi ja yhdistät jokaisen solmun johonkin agentin kuudesta komponentista.

**Syötekäsittelijä** on triggerisolmu ja mahdolliset validointisolmut sen jälkeen. Jos rakennat chatbotin, triggeri voi olla webhook, joka vastaanottaa käyttäjän viestin. Heti sen jälkeen voit lisätä IF-solmun, joka tarkistaa esimerkiksi, onko viesti liian pitkä tai tyhjä. Tämä on samaa syötevalidointia, josta puhuttiin teoriassa. n8n:ssä se näkyy konkreettisena solmuna kankaalla.

**Päättelijä** on tekoälysolmu, esimerkiksi OpenAI-solmu tai vastaava. Siihen kirjoitat **system promptin**, joka ohjaa agentin toimintaa. Tässä solmussa agentti ”ajattelee”: se saa käyttäjän viestin, mahdollisesti kontekstitietoa edellisistä solmuista sekä ohjeet siitä, miten sen pitää vastata tai toimia.

**Työkalujen suorittaja** tarkoittaa solmuja, joilla agentti tekee konkreettisia toimintoja. Google Sheets -solmu lukee tai kirjoittaa tietoja. HTTP Request -solmu kutsuu ulkoisia palveluita. Slack-solmu lähettää viestejä. Nämä ovat agentin ”kädet”, joiden avulla se toimii maailmassa.

**Muisti ja konteksti** voidaan toteuttaa usealla tavalla. Yksinkertaisimmillaan voit tallentaa keskusteluhistorian Google Sheetsiin ja hakea sen jokaisen uuden viestin yhteydessä. n8n:ssä voi olla myös muistisolmuja tai muita tapoja säilyttää keskustelun kontekstia ja prosessin tilaa.

**Turvakerros** toteutuu IF-solmuilla, ehdoilla, validoinneilla ja hyväksyntäkohdilla. Voit esimerkiksi lisätä ehdon: ”Jos vastaus sisältää henkilötietoja, älä lähetä sitä eteenpäin.” Tai: ”Jos käyttäjä pyytää jotakin, mikä ei kuulu agentin tehtävään, vastaa kohteliaasti kieltäytymällä.” n8n:ssä nämä ovat konkreettisia haarautumia työnkulussa.

**Seuranta ja palautesilmukka** tarkoittavat lokitusta ja palautteen keräämistä. Lisää työnkulkuun solmu, joka tallentaa jokaisen tärkeän toiminnon esimerkiksi Google Sheetsiin tai tiedostoon: mitä käyttäjä kysyi, mitä agentti vastasi, mitä työkaluja käytettiin ja kauanko suoritus kesti. Näin näet jälkikäteen, miten agentti toimii, ja voit parantaa sitä.

## Iteratiivinen kehitys — rakenna pienestä isoon

Tämän tunnin tärkein periaate on: **aloita pienestä**. Rakenna ensin yksinkertaisin mahdollinen versio, joka tekee yhden asian oikein. Testaa se. Lisää vasta sen jälkeen seuraava ominaisuus. Tätä kutsutaan **iteratiiviseksi kehitykseksi**. Ammattilaisetkaan eivät rakenna valmista tuotetta yhdellä kertaa.

Käytännössä tunnin 26 tavoite on **toimiva minimiversio**: kolmesta solmusta koostuva agentti, joka tekee ydintehtävänsä. Turvakerros, monimutkaisemmat haarat, hyväksyntäportit ja viimeistely tehdään tunnilla 27. Jos yrität tehdä kaiken kerralla, on suuri riski, että mikään ei toimi kunnolla.

Esimerkki iteratiivisesta rakentamisesta:

1. **Vaihe 1 — Yksinkertainen triggeri ja toiminta:** Manual Trigger → HTTP Request. Testaa, että työnkulku käynnistyy ja data liikkuu.
2. **Vaihe 2 — Lisää päättely:** Manual Trigger → HTTP Request → AI-solmu. Testaa, että tekoälysolmu saa oikean syötteen ja tuottaa vastauksen.
3. **Vaihe 3 — Lisää toimintasolmu:** Manual Trigger → HTTP Request → AI-solmu → Discord, sähköposti tai muu toimintasolmu. Testaa, että vastaus lähtee oikeaan paikkaan.

Testaa jokaisen lisäyksen jälkeen, että kaikki toimii. Jos jokin menee rikki, tiedät tarkalleen, mikä muutos aiheutti ongelman. Tämä on paljon helpompaa kuin rakentaa koko työnkulku kerralla ja etsiä sen jälkeen vikaa kymmenestä eri solmusta.

**Pysähdy hetkeksi:** Kun lisäät uuden solmun työnkulkuusi, mieti aina: mikä agentin komponentti tämä on? Onko kyse syötekäsittelystä, päättelystä, työkalusta, muistista, turvakerroksesta vai palautesilmukasta?

## Pohjapiirroksesta toteutukseen

Tällä tunnilla et aloita tyhjältä pöydältä. Sinulla on viisi pohjapiirrosta, jotka olet kerännyt edellisillä tunneilla. Niiden pohjalta tiedät jo:

- mitä ongelmaa agenttisi ratkaisee ja kenelle se on tarkoitettu — **pohjapiirros 1**
- mitä agentti muistaa ja millainen sen identiteetti on — **pohjapiirros 2**
- miten agentti päättelee: ReAct-mallilla vai ketjuajattelun avulla — **pohjapiirros 3**
- mitä riskejä agenttiin liittyy ja miten ne torjutaan — **pohjapiirros 4**
- missä kohdissa ihminen on mukana — **pohjapiirros 5**

Tunnin alussa kokoat nämä viisi pohjapiirrosta yhdeksi suunnitelmaksi ja tarkistat, että ne sopivat yhteen. Sen jälkeen rakennat minimiversion: **triggeri + tekoälysolmu + yksi toimintasolmu**. Pohjapiirrosten 4 ja 5 sisältämät turvakerros ja ihmisen rooli viimeistellään tunnilla 27, kun testaat ja dokumentoit agentin.

Jos olet epävarma omasta projektistasi, voit arvioida vaikeustasoa seuraavien esimerkkien avulla:

**Taso 1 — FAQ-botti**

Yhteisö saa samoja kysymyksiä kymmeniä kertoja päivässä. Botti vastaa yleisimpiin kysymyksiin automaattisesti. Triggeri on viesti chat-kanavasta. Työnkulku lähettää viestin AI-solmulle, jolla on system prompt ja FAQ-tietokanta kontekstina. Lopuksi vastaus lähetetään takaisin chattiin.

**Taso 2 — Sähköpostiyhteenvetoagentti**

Agentti lukee joka aamu klo 8 viimeisen 24 tunnin sähköpostit, tekee niistä yhteenvedon tekoälyllä ja lähettää yhteenvedon Slackiin tai Teamsiin. Triggeri on ajastin. Työnkulku etenee näin: hae sähköpostit → kokoa yhteenveto → lähetä yhteenveto.

**Taso 3 — Tikettiagentti**

Asiakas lähettää viestin lomakkeella. Agentti luokittelee viestin, esimerkiksi tekninen ongelma, laskutus tai palaute. Sen jälkeen agentti luo tiketin Google Sheetsiin, vastaa asiakkaalle automaattisesti ja ilmoittaa oikealle tiimille. Jos viesti on kriittinen, se ohjataan ihmiselle hyväksyttäväksi. Tämä on esimerkki **human-in-the-loop**-rakenteesta.

## Tunnin tavoite ja valmis lopputulos

Tunnin lopussa sinulla pitäisi olla **toimiva minimiversio** omasta n8n-agentistasi. Sen ei tarvitse vielä olla täydellinen, mutta sen pitää näyttää, että perusidea toimii.

Minimiversiossa tulee olla vähintään:

- **triggeri**, joka käynnistää työnkulun
- **tekoälysolmu**, joka tekee päättelyn tai tuottaa vastauksen
- **toimintasolmu**, joka tekee jotakin konkreettista, esimerkiksi lähettää viestin, tallentaa rivin tai kutsuu palvelua

Lisäksi sinun kannattaa tunnin aikana kirjata muistiin:

- mitkä solmut vastaavat agentin kuutta komponenttia
- mikä osa toimii jo
- mikä osa jäi kesken
- mitä pitää testata tai korjata tunnilla 27

**Tarkista lopuksi:** Käynnistyykö työnkulku? Kulkeeko data solmulta toiselle? Tuottaako tekoälysolmu järkevän vastauksen? Tekeekö toimintasolmu sen, mitä sen pitää tehdä? Tiedätkö, mitä korjaat tai lisäät seuraavalla tunnilla?

## Yhteenveto

Tämä tunti vie sinut suunnittelusta rakentamiseen. Tunnin alussa kokoat viisi pohjapiirrostasi yhdeksi suunnitelmaksi. Sen jälkeen tutustut n8n:ään ja rakennat agenttisi minimiversion iteratiivisesti: solmu kerrallaan ja jokaisen lisäyksen jälkeen testaten.

Tunnin lopussa sinulla on toimiva perusversio, jonka päälle lisäät turvakerroksen, hyväksyntäportit, testauksen ja dokumentaation tunnilla 27. Tärkeintä ei ole rakentaa kaikkea valmiiksi yhdellä kertaa. Tärkeintä on saada ensimmäinen versio toimimaan, ymmärtää sen rakenne ja tietää, miten jatkat siitä eteenpäin.

---
