# Kädet saveen — n8n-agenttipaja alkaa

## Johdanto: Teoriasta tekemiseen

Olet oppinut, mitä agentit ovat, miten ne päättelevät, miten niitä turvataan ja miten ne eroavat tavallisista ohjelmista. Olet myös kerännyt matkan varrella viisi pohjapiirrosta — yksi tunneilta 19, 21, 23, 24 ja 25 — jotka muodostavat suunnitelman omasta agentistasi. Tällä tunnilla kasaat pohjapiirrokset yhteen, tutustut n8n:ään ja rakennat agenttisi ensimmäisen toimivan version.

n8n (lausutaan "n-eight-n") on avoimen lähdekoodin automaatioalusta, jossa rakennat työnkulkuja visuaalisesti vetämällä ja pudottamalla solmuja (nodes) kankaalle. Jokainen solmu tekee yhden asian: vastaanottaa viestin, kutsuu tekoälyä, lukee tiedoston, lähettää sähköpostin. Solmujen välille vedät viivan, ja data virtaa automaattisesti solmusta toiseen. Se on kuin rakentaisit putkirakennelman, jossa jokainen mutka tekee jotain hyödyllistä.

Miksi juuri n8n? Koska se poistaa suurimman esteen agentin rakentamisesta: sinun ei tarvitse osata ohjelmoida. Kaikki, mitä olet oppinut agentin rakenteesta — syötekäsittely, päättely, työkalut, turvakerrokset — toteutuu n8n:ssä visuaalisesti. Näet agentin arkkitehtuurin konkreettisesti edessäsi, solmuina ja viivoina.

> **Pysähdy hetkeksi:** mieti jotain toistuvaa tehtävää arjessasi tai koulussa. Voisiko kone hoitaa sen puolestasi, jos sillä olisi pääsy oikeisiin työkaluihin?

## n8n:n perusteet — solmut, yhteydet ja triggerit

Kun avaat n8n:n ensimmäistä kertaa, näet tyhjän kankaan. Kaikki alkaa **triggeristä** (trigger) — solmusta, joka käynnistää työnkulun. Triggeri voi olla ajastin ("joka maanantai klo 8"), webhook ("kun joku lähettää viestin") tai manuaalinen nappi ("kun painan käynnistä"). Ilman triggeriä mikään ei tapahdu.

Triggerin jälkeen lisäät **toimintasolmuja**. Jokainen solmu saa dataa edelliseltä solmulta ja antaa dataa eteenpäin. Esimerkiksi: triggeri vastaanottaa Discord-viestin → HTTP Request -solmu lähettää viestin tekoäly-API:lle → toinen solmu muotoilee vastauksen → viimeinen solmu lähettää vastauksen takaisin Discordiin. Tämä on yksinkertainen agentti: se ottaa syötteen, käsittelee sen tekoälyllä ja toimii tuloksen perusteella.

n8n:ssä on satoja valmiita integraatioita: Google Sheets, Slack, Discord, sähköposti, tiedostot, tietokannat, HTTP-kutsut ja tekoälypalvelut kuten OpenAI ja Claude. Sinun ei tarvitse tietää, miten mikään näistä toimii teknisesti — n8n hoitaa yhteydet puolestasi. Sinun tehtäväsi on päättää, mitä solmuja käytät ja missä järjestyksessä.

> **Pysähdy hetkeksi:** miten n8n:n solmut vastaavat agentin kuutta komponenttia, jotka opit tunnilla 19? Mieti, mikä solmu olisi syötekäsittelijä, mikä päättelijä ja mikä työkalujen suorittaja.

## Agentin kuusi komponenttia n8n:ssä

Palataan hetkeksi tunnin 19 arkkitehtuuriin ja katsotaan, miten se toteutuu n8n:ssä konkreettisesti. Tämä on tärkeää, koska tunnilla 27 dokumentoit agenttisi ja linkität jokaisen solmusi yhteen näistä kuudesta komponentista.

**Syötekäsittelijä** on triggersolmu ja mahdolliset validointisolmut sen jälkeen. Jos rakennat chatbotin, triggeri on webhook, joka vastaanottaa käyttäjän viestin. Heti sen jälkeen voit lisätä IF-solmun, joka tarkistaa: onko viesti liian pitkä? Onko se tyhjä? Tämä on sama syötevalidointi, josta puhuimme teoriassa — nyt se on konkreettinen laatikko kankaalla.

**Päättelijä** on tekoälysolmu — esimerkiksi OpenAI-solmu tai vastaava, johon kirjoitat system promptin. Tässä solmussa agentti "ajattelee": se saa käyttäjän viestin, mahdollisesti kontekstitietoa edellisistä solmuista ja ohjeet siitä, miten vastata. System prompt on agentin aivot, aivan kuten tunnilla 21 opittiin.

**Työkalujen suorittaja** on kaikki muu. Google Sheets -solmu lukee tai kirjoittaa tietoja. HTTP Request -solmu kutsuu ulkoisia palveluita. Slack-solmu lähettää viestejä. Nämä ovat agentin "kädet" — ne tekevät konkreettisia toimintoja maailmassa.

**Muisti ja konteksti** voidaan toteuttaa usealla tavalla. Yksinkertaisimmillaan voit tallentaa keskusteluhistorian Google Sheetsiin ja ladata sen jokaisen uuden viestin yhteydessä. n8n:ssä on myös sisäänrakennettu muistisolmu (Memory), joka pitää kirjaa keskustelun kontekstista automaattisesti.

**Turvakerros** toteutuu IF-solmuilla ja ehtologiikalla. Voit lisätä ehdon: "Jos vastaus sisältää henkilötietoja, älä lähetä sitä eteenpäin." Tai: "Jos käyttäjä pyytää jotain, mikä ei kuulu agentin tehtävään, vastaa kohteliaasti kieltäytymällä." Nämä ovat n8n:ssä konkreettisia haarautumia työnkulussa.

**Seuranta ja palautesilmukka** tarkoittaa lokitusta. Lisää työnkulkuun solmu, joka tallentaa jokaisen toiminnon Google Sheetsiin tai tiedostoon: mitä käyttäjä kysyi, mitä agentti vastasi, kauanko se kesti. Näin näet jälkikäteen, miten agentti toimii, ja voit parantaa sitä.

## Iteratiivinen kehitys — rakenna pienestä isoon

Tärkein periaate tähän tuntiin on: **aloita pienestä**. Rakenna ensin yksinkertaisin mahdollinen versio, joka tekee yhden asian oikein. Testaa se. Vasta sitten lisää seuraava ominaisuus. Tämä on ammattilaisten tapa rakentaa ohjelmistoja — sitä kutsutaan iteratiiviseksi kehitykseksi. Kukaan ei rakenna valmista tuotetta kerralla.

Käytännössä se tarkoittaa, että tunnin 26 tavoite on **toimiva minimiversio** — kolmesta solmusta koostuva agentti, joka tekee ydintehtävänsä. Turvakerros, monimutkaisemmat haarat ja viimeistelyt rakennat tunnilla 27. Jos yrität tehdä kaiken kerralla, et saa mitään toimivaksi.

Esimerkki iteratiivisesta rakentamisesta:

1. **Vaihe 1 — Yksinkertainen trigger + toiminta:** Manual Trigger → HTTP Request. Testaa.
2. **Vaihe 2 — Lisää päättely:** Manual Trigger → HTTP Request → AI-solmu. Testaa.
3. **Vaihe 3 — Lisää toiminta:** Manual Trigger → HTTP Request → AI-solmu → Discord/sähköposti. Testaa.

Jokaisen lisäyksen jälkeen testaa, että kaikki toimii. Jos jokin menee rikki, tiedät tarkalleen, mikä muutos sen aiheutti. Tämä on paljon helpompaa kuin yrittää rakentaa koko työnkulku kerralla ja sitten etsiä vikaa kymmenestä solmusta.

> **Pysähdy hetkeksi:** kun lisäät uuden solmun työnkulkuusi, mieti aina — mikä agentin komponentti tämä on? Onko tämä syötekäsittelyä, päättelyä, työkalu vai turvakerros?

## Pohjapiirroksesta toteutukseen

Tunnilla et aloita tyhjältä pöydältä. Sinulla on viisi pohjapiirrosta, jotka olet kerännyt edellisillä tunneilla. Niiden pohjalta tiedät jo:

- Mitä ongelmaa agenttisi ratkaisee ja kenelle (pohjapiirros 1)
- Mitä se muistaa ja millainen sen identiteetti on (pohjapiirros 2)
- Miten se ajattelee — ReAct vai ketjuajattelu (pohjapiirros 3)
- Mitä riskejä on ja miten ne torjutaan (pohjapiirros 4)
- Missä ihminen on mukana (pohjapiirros 5)

Tunnin alussa kokoat nämä viisi pohjapiirrosta yhdeksi suunnitelmaksi ja tarkistat, että ne sopivat yhteen. Sen jälkeen rakennat minimiversion: triggeri + tekoälysolmu + yksi toimintasolmu. Pohjapiirrokset 4 (turvakerros) ja 5 (ihmisen rooli) toteutuvat vasta tunnilla 27, kun viimeistelet agentin.

Jos olet epävarma omasta projektistasi, mieti vaikeustasoasi näiden esimerkkien avulla:

**Taso 1 — FAQ-botti.** Yhteisö saa kymmeniä samoja kysymyksiä päivässä. Bot vastaa yleisimpiin automaattisesti. Triggeri: viesti chat-kanavasta. Toiminta: lähetä viesti AI-solmulle, jolla on system prompt ja FAQ-tietokanta kontekstina. Vastaus takaisin chattiin.

**Taso 2 — Sähköpostiyhteenvetoagentti.** Joka aamu klo 8 agentti lukee viimeiset 24 tunnin sähköpostit, tekee niistä yhteenvedon tekoälyllä ja lähettää sen Slackiin tai Teamsiin. Triggeri: ajastin. Toiminta: hae sähköpostit → kokoa yhteenveto → lähetä.

**Taso 3 — Tikettiagentti.** Asiakas lähettää viestin lomakkeella. Agentti luokittelee viestin (tekninen, laskutus, palaute), luo tiketin Google Sheetsiin, vastaa asiakkaalle automaattisesti ja ilmoittaa oikealle tiimille. Jos viesti on kriittinen, se menee ihmiselle hyväksyttäväksi — tämä on human-in-the-loop.

## Yhteenveto

Tämä tunti vie sinut suunnittelusta rakentamiseen. Tunnin alussa kasaat viisi pohjapiirrostasi yhdeksi suunnitelmaksi, tutustut n8n:ään ja rakennat agenttisi minimiversion iteratiivisesti — solmu kerrallaan, testaten jokaisen lisäyksen jälkeen. Tunnin lopussa sinulla on toimiva perusversio, jonka päälle viimeistelet, testaat ja dokumentoit valmiin agentin tunnilla 27.
