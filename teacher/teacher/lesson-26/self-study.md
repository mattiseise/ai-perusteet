# Kädet saveen — n8n-agenttipaja alkaa

## Johdanto: Teoriasta tekemiseen

Olet oppinut, mitä agentit ovat, miten ne päättelevät, miten niitä turvataan ja miten ne eroavat tavallisista ohjelmista. Nyt on aika tehdä oma. Seuraavat kaksi oppituntia ovat projektipaja, jossa rakennat toimivan agentin tai automaation n8n-alustalla.

n8n (lausutaan "n-eight-n") on avoimen lähdekoodin automaatioalusta, jossa rakennat työnkulkuja visuaalisesti vetämällä ja pudottamalla solmuja (nodes) kankaalle. Jokainen solmu tekee yhden asian: vastaanottaa viestin, kutsuu tekoälyä, lukee tiedoston, lähettää sähköpostin. Solmujen välille vedät viivan, ja data virtaa automaattisesti solmusta toiseen. Se on kuin rakentaisit putkirakennelman, jossa jokainen mutka tekee jotain hyödyllistä.

Miksi juuri n8n? Koska se poistaa suurimman esteen agentin rakentamisesta: sinun ei tarvitse osata ohjelmoida. Kaikki, mitä olet oppinut agentin rakenteesta — syötekäsittely, päättely, työkalut, turvakerrokset — toteutuu n8n:ssä visuaalisesti. Näet agentin arkkitehtuurin konkreettisesti edessäsi, solmuina ja viivoina.

Pysähdy hetkeksi: mieti jotain toistuvaa tehtävää arjessasi tai koulussa. Voisiko kone hoitaa sen puolestasi, jos sillä olisi pääsy oikeisiin työkaluihin?

## n8n:n perusteet — solmut, yhteydet ja triggerit

Kun avaat n8n:n ensimmäistä kertaa, näet tyhjän kankaan. Kaikki alkaa triggeristä (trigger) — solmusta, joka käynnistää työnkulun. Triggeri voi olla ajastin ("joka maanantai klo 8"), webhook ("kun joku lähettää viestin") tai manuaalinen nappi ("kun painan käynnistä"). Ilman triggeriä mikään ei tapahdukaan.

Triggerin jälkeen lisäät toimintasolmuja. Jokainen solmu saa dataa edelliseltä solmulta ja antaa dataa eteenpäin. Esimerkiksi: triggeri vastaanottaa Discord-viestin → HTTP Request -solmu lähettää viestin tekoäly-API:lle → toinen solmu muotoilee vastauksen → viimeinen solmu lähettää vastauksen takaisin Discordiin. Tämä on yksinkertainen agentti: se ottaa syötteen, käsittelee sen tekoälyllä ja toimii tuloksen perusteella.

n8n:ssä on satoja valmiita integraatioita: Google Sheets, Slack, Discord, sähköposti, tiedostot, tietokannat, HTTP-kutsut ja tietenkin tekoälypalvelut kuten OpenAI ja Claude. Sinun ei tarvitse tietää, miten mikään näistä toimii teknisesti — n8n hoitaa yhteydet puolestasi. Sinun tehtäväsi on päättää, mitä solmuja käytät ja missä järjestyksessä.

Pysähdy hetkeksi: miten n8n:n solmut vastaavat agentin kuutta komponenttia, jotka opit lesson 19:ssä? Mieti, mikä solmu olisi syötekäsittelijä, mikä päättelijä ja mikä työkalujen suorittaja.

## Agentin kuusi komponenttia n8n:ssä

Palataan hetkeksi lesson 19:n arkkitehtuuriin ja katsotaan, miten se toteutuu n8n:ssä konkreettisesti.

**Syötekäsittelijä** on triggersolmu ja mahdolliset validointisolmut sen jälkeen. Jos rakennat chatbotin, triggeri on webhook, joka vastaanottaa käyttäjän viestin. Heti sen jälkeen voit lisätä IF-solmun, joka tarkistaa: onko viesti liian pitkä? Onko se tyhjä? Tämä on sama syötevalidointi, josta puhuimme teoriassa — nyt se on konkreettinen laatikko kankaalla.

**Päättelijä** on tekoälysolmu — esimerkiksi OpenAI-solmu, johon kirjoitat system promptin. Tässä solmussa agentti "ajattelee": se saa käyttäjän viestin, mahdollisesti kontekstitietoa edellisistä solmuista ja ohjeet siitä, miten vastata. System prompt on agentin aivot, aivan kuten lesson 21:ssä opittiin.

**Työkalujen suorittaja** on kaikki muu. Google Sheets -solmu lukee tai kirjoittaa tietoja. HTTP Request -solmu kutsuu ulkoisia palveluita. Slack-solmu lähettää viestejä. Nämä ovat agentin "kädet" — ne tekevät konkreettisia toimintoja maailmassa.

**Muisti ja konteksti** voidaan toteuttaa usealla tavalla. Yksinkertaisimmillaan voit tallentaa keskusteluhistorian Google Sheetsiin ja ladata sen jokaisen uuden viestin yhteydessä. n8n:ssä on myös sisäänrakennettu muistisolmu (Memory), joka pitää kirjaa keskustelun kontekstista automaattisesti.

**Turvakerros** toteutuu IF-solmuilla ja ehtologiikalla. Voit lisätä ehdon: "Jos vastaus sisältää henkilötietoja, älä lähetä sitä eteenpäin." Tai: "Jos käyttäjä pyytää jotain, mikä ei kuulu agentin tehtävään, vastaa kohteliaasti kieltäytymällä." Nämä ovat n8n:ssä konkreettisia haarautumia työnkulussa.

**Seuranta ja palautesilmukka** tarkoittaa lokitusta. Lisää työnkulkuun solmu, joka tallentaa jokaisen toiminnon Google Sheetsiin tai tiedostoon: mitä käyttäjä kysyi, mitä agentti vastasi, kauanko se kesti. Näin näet jälkikäteen, miten agentti toimii, ja voit parantaa sitä.

## Projektin suunnittelu

Ennen kuin avaat n8n:n, sinun pitää tietää, mitä rakennat. Hyvä projekti alkaa selkeästä käyttötapauksesta: kuka käyttää tätä, mitä ongelmaa se ratkaisee ja mitä se EI tee.

Tässä kolme esimerkkiprojektia eri vaikeustasoille:

**Taso 1 — FAQ-botti Discordiin.** Pelaajayhteisö saa kymmeniä samoja kysymyksiä päivässä. Rakennat botin, joka vastaa yleisimpiin kysymyksiin automaattisesti. Triggeri: Discord-viesti. Toiminta: lähetä viesti OpenAI:lle, jolla on system prompt ja FAQ-tietokanta kontekstina. Vastaus takaisin Discordiin.

**Taso 2 — Sähköpostiyhteenvetoagentti.** Joka aamu klo 8 agentti lukee viimeiset 24 tunnin sähköpostit, tekee niistä yhteenvedon tekoälyllä ja lähettää sen Slackiin. Triggeri: ajastin. Toiminta: hae sähköpostit → kokoa yhteenveto → lähetä Slackiin.

**Taso 3 — Asiakastuen tikettijärjestelmä.** Asiakas lähettää viestin lomakkeella. Agentti luokittelee viestin (tekninen ongelma, laskutus, palaute), luo tiketin Google Sheetsiin, vastaa asiakkaalle automaattisesti ja ilmoittaa oikealle tiimille Slackissa. Jos viesti on kriittinen, se menee ihmiselle hyväksyttäväksi ennen vastausta — tämä on human-in-the-loop, josta puhuimme Lesson 25:ssä.

Valitse yksi näistä tai keksi oma. Tärkeintä on, että tiedät ennen rakentamista: mitä agentti tekee, mitä se ei tee, missä kohdissa ihminen päättää ja mitkä ovat riskit.

## Suunnitteludokumentti

Ennen kuin rakennat mitään, kirjoita suunnitelma. Se ei tarvitse olla pitkä — puoli sivua riittää. Mutta siinä pitää olla nämä asiat:

```
PROJEKTI: [Nimi]

KÄYTTÖTAPAUS: Mitä ongelmaa tämä ratkaisee? Kuka käyttää tätä?

MITÄ SE TEKEE:
1. [Ensimmäinen vaihe]
2. [Toinen vaihe]
3. [Kolmas vaihe]

MITÄ SE EI TEE:
- [Raja 1]
- [Raja 2]

HYVÄKSYNTÄPORTIT:
- [Missä kohtaa ihminen päättää?]

RISKIT:
- [Mitä voi mennä pieleen?]

SOLMUT (n8n):
Trigger → [Solmu 1] → [Solmu 2] → ... → [Viimeinen solmu]
```

Kun suunnitelma on valmis, näytä se opettajalle tai vertaisopiskelijalle. Toisen silmä huomaa aukot, jotka itse ohittaa.

## Yhteenveto

Tämä oppitunti antoi sinulle työkalut n8n-projektipajan aloittamiseen. Ymmärrät nyt, miten n8n:n solmut, yhteydet ja triggerit toimivat ja miten agentin kuusi komponenttia toteutuvat visuaalisessa automaatioalustassa. Olet valinnut projektin ja kirjoittanut suunnitelman. Seuraavassa tunnissa rakennat, testaat ja dokumentoit agentin — ja valmistat sen esittelyä varten.
