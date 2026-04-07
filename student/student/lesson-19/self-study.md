# Boteista agentteihin — mikä muuttuu kun AI toimii itsenäisesti

## Johdanto

Kun puhutaan tekoälystä ja automatisoinnista, sanaa “agentti” käytetään nykyään hyvin usein. Sitä esiintyy teknologiauutisissa, yritysviestinnässä ja opetuksessa, mutta käsitteen merkitys jää usein epäselväksi. Agentti ei kuitenkaan ole sama asia kuin chatbot. Se ei myöskään tarkoita mitä tahansa automaattista lajittelijaa tai yksinkertaista ohjelmaa.

Tämä on ensimmäinen askel kohti omaa agenttiasi, jonka rakennat n8n:llä tämän osion lopussa. Oppitunneilla 26–27 toteutat tässä oppimaasi konkreettisesti. Ymmärrä nyt agentin logiikka — myöhemmin rakentaminen on paljon helpompaa.

Tarkastellaan esimerkkiä. Tehtävänä on avata sähköpostisovellus, etsiä kaikki viestit, joissa esiintyy sana ”lasku”, siirtää ne kansioon ”Laskut” ja lähettää lähettäjälle automaattinen vastaus, jossa ilmoitetaan laskun vastaanottamisesta. Yksittäisenä suorituksena tehtävä on melko yksinkertainen. Jos sama toiminto täytyy kuitenkin tehdä toistuvasti, esimerkiksi joka päivä tai jatkuvasti pitkän ajan kuluessa, siitä tulee työläs ja aikaa vievä.

Tällaisessa tilanteessa agentti voisi hoitaa tehtävän itsenäisesti käyttäjän puolesta. Tämä herättää kuitenkin tärkeän kysymyksen: miten agentti eroaa tavallisesta automaatiosta, ja mikä tekee järjestelmästä juuri agentin?

Ennen kuin asiaa tarkastellaan tarkemmin, on hyödyllistä pohtia omaa arkea. 


> **Pysähdy hetkeksi:**  Millaisia toistuvia tehtäviä teet säännöllisesti? Mitkä niistä ovat yksinkertaisia, mutta vievät silti aikaa ja kuormittavat turhaan?


## Agentti on järjestelmä, joka päättää itse

Ensimmäinen ja keskeisin asia on tämä: agentti on automatisoitu järjestelmä, joka **suorittaa useita vaiheita itsenäisesti** jonkin tavoitteen saavuttamiseksi. Se ei siis vain toteuta yhtä yksittäistä käskyä. Se ei myöskään seuraa ohjeita täysin mekaanisesti tilanteesta riippumatta, vaan tekee päätelmiä tilanteen perusteella.

Jos sähköpostisovellus käy joka aamu läpi uudet viestit ja siirtää laskut automaattisesti tiettyyn kansioon, kyse ei vielä välttämättä ole agentista. Usein kyse on skriptistä eli yksinkertaisesta ohjelmasta, joka tekee aina saman toiminnon samalla tavalla. Tällainen ratkaisu toimii hyvin niin kauan kuin tilanne vastaa ennalta määriteltyä mallia. Jos viestin muoto poikkeaa odotetusta, skripti voi epäonnistua.

Agentti toimii toisin. Se voi vastaanottaa uuden sähköpostin, analysoida sen sisältöä ja arvioida, onko kyseessä lasku. Sen jälkeen se voi päätellä, mihin kansioon viesti kannattaa siirtää. Se voi myös tarkistaa lähettäjään liittyviä tietoja muista järjestelmistä, hyödyntää aiempia havaintoja ja päättää, voidaanko lähettäjälle lähettää automaattinen vastaus. Lopuksi se voi kirjata tekemänsä toimenpiteet. Jos jokin vaihe epäonnistuu, esimerkiksi vastaanottajan osoite on virheellinen, agentti voi tunnistaa ongelman, ilmoittaa siitä ja pyytää jatko-ohjeita.

> **Pysähdy hetkeksi:**  Mitä eroa on siinä, että ohjelma tekee aina samaa, ja siinä, että se ajattelee ja muuttaa toimintaansa tilanteen perusteella?

## Agentin kuusi rakennusosaa

Nyt kun tiedät, mitä agentti on, voidaan siirtyä tarkastelemaan sen sisäistä rakennetta. Jokainen agentti, olipa se yksinkertainen tai monimutkainen, rakentuu kuudesta peruskomponentista. Kun nämä komponentit toimivat yhdessä, agentti pystyy käsittelemään tietoa, tekemään päätelmiä ja toteuttamaan tehtäviään mielekkäällä tavalla.

**Ensimmäinen komponentti: syötekäsittelijä.** Syötekäsittelijä toimii agentin aisteina. Se havaitsee, kun uusi sähköposti saapuu, palvelin lähettää hälytyksen tai käyttäjä painaa painiketta. Sen tehtävänä on vastaanottaa nämä herätteet ja käyttäjän syötteet sekä muuntaa ne sellaiseen muotoon, jota agentti pystyy käsittelemään.

Ilman syötekäsittelijää agentti ei tietäisi, että mitään on tapahtunut. Se ei voisi reagoida ympäristöönsä eikä käynnistää toimintaansa oikealla hetkellä

Voit ajatella asiaa myös näin: vaikka IT-tukihenkilö olisi kuinka taitava, hän ei voi ratkaista ongelmia, jos hän ei saa niistä mitään tietoa. Jos hän ei kuule puheluita eikä lue sähköposteja, hän ei edes tiedä, että apua tarvitaan.

**Toinen komponentti: päättelijä ja suunnittelija.** Päättelijä on agentin aivot. Kun tietoa on vastaanotettu, sen tehtävä on analysoida tilanne ja arvioida, mikä toimenpide on tarkoituksenmukaisin. Tässä se voi hyödyntää esimerkiksi kielimallia, joka auttaa tulkitsemaan tekstiä ja valitsemaan seuraavan vaiheen. Se voi esimerkiksi päätellä, onko viesti kiireellinen, löytyykö vastaus tietokannasta vai pitääkö asia ohjata ihmiselle.

Ilman päättelijää agentti ei tekisi päätöksiä tilanteen perusteella, vaan toimisi aina samalla tavalla. Tällöin se olisi enemmän skripti kuin varsinainen agentti.

**Kolmas komponentti: työkalujen suorittaja.** Kun päättelijä on arvioinut tilanteen ja valinnut toimintatavan, työkalujen suorittaja toteuttaa päätöksen käytännössä. Se voi kutsua rajapintoja, tehdä tietokantahakuja, lähettää sähköposteja tai muokata tiedostoja. Työkalujen suorittaja on siis se osa agenttia, joka muuttaa päätökset toiminnaksi.

Ilman tätä osaa agentti ei pystyisi vaikuttamaan ympäristöönsä. Päättelijä voisi kyllä muodostaa tarkoituksenmukaisen ratkaisun, mutta mitään ei tapahtuisi käytännössä. Tällöin agentti olisi kuin johtaja, jolla ei ole mahdollisuutta toteuttaa tekemiään päätöksiä.

**Neljäs komponentti: muisti ja konteksti.** Agentti tarvitsee myös muistia. Lyhytkestoinen muisti tarkoittaa sitä tietoa, jota agentti pitää aktiivisesti mukana tehtävän aikana. Tähän voi kuulua esimerkiksi viimeisimmät työvaiheet, käsiteltävän tapauksen sisältö ja tieto siitä, ketä agentti on juuri auttanut. Pitkäkestoinen muisti taas viittaa tietoon, joka on tallennettu pysyvämmin esimerkiksi tietokantaan tai lokiin. Sen avulla agentti voi hyödyntää aiempia kokemuksiaan myöhemmissä tilanteissa.

Muistin ansiosta agentti voi ottaa huomioon, mitä se on tehnyt aiemmin ja millaisiin tuloksiin eri toimintatavat ovat johtaneet. Ilman muistia se käsittelisi jokaisen tilanteen ikään kuin ensimmäistä kertaa. Tällöin se voisi toistaa samoja virheitä yhä uudelleen eikä pystyisi kehittämään toimintaansa.

**Viides komponentti: turvakerros.** Ennen kuin agentti suorittaa mitään toimintoa, sen on tarkistettava, onko toiminta sallittua. Tästä vastaa turvakerros. Sen tehtävänä on estää agenttia tekemästä vaarallisia, virheellisiä tai luvattomia toimenpiteitä. Turvakerros tarkistaa esimerkiksi, saako agentti poistaa tietokannan rivejä, siirtää rahaa tietylle tilille tai käsitellä tietyn käyttäjän tietoja.

Turvakerros toimii yleensä kolmella tasolla. Se voi tarkistaa toiminnan etukäteen ennen sen suorittamista, valvoa toimintaa sen aikana ja arvioida jälkikäteen, tapahtuiko kaikki sääntöjen mukaisesti. Näin se vähentää riskiä, että agentti toimisi tavalla, joka aiheuttaisi vahinkoa tai rikkoisi annettuja rajoja.

Ilman turvakerrosta agentti voisi tehdä vakavia virheitä tai aiheuttaa vahinkoa ympäristölleen. Turvakerros on siis se osa järjestelmää, joka pysäyttää toiminnan silloin, kun sitä ei pitäisi sallia.

**Kuudes komponentti: seuranta ja palautesilmukka.** Kun agentti suorittaa toiminnon, on tärkeää pystyä seuraamaan, mitä tapahtui. Onko tehtävä onnistunut, vastasiko tulos odotuksia ja kuinka kauan suoritus kesti? Tästä vastaa seurantakomponentti, joka kirjaa agentin toiminnan ja sen tulokset.

Kerättyä tietoa hyödynnetään palautesilmukassa. Sen avulla agentin toimintaa voidaan arvioida ja kehittää. Jos jokin toimintatapa on aiemmin johtanut epäonnistumiseen, järjestelmä voi käyttää tätä tietoa myöhemmissä tilanteissa ja ohjata toimintaa toiseen suuntaan.

Ilman palautesilmukkaa agentti ei pystyisi tunnistamaan omia virheitään eikä parantamaan toimintaansa. Tällöin se voisi toistaa samoja virheitä yhä uudelleen ilman mahdollisuutta oppia niistä.

> **Pysähdy hetkeksi:** mitkä kuudesta komponentista näet omassa elämässäsi, kun teet omia päätöksiäsi? Kuinka moni niistä puuttuu skriptiltä tai yksinkertaiselta työnkululta?

Seuraavissa oppitunneissa avaamme jokaisen näistä komponenteista tarkemmin. Kun kohtaat uuden aiheen, mieti aina: mihin agentin osaan tämä liittyy?

## Chatbot ei ole agentti

Chatbot on ohjelma, joka vastaa käyttäjän kirjoittamiin viesteihin. Se voi vaikuttaa hyvinkin älykkäältä, ja erityisesti nykyaikaiset chatbotit, kuten ChatGPT, osaavat käydä sujuvaa keskustelua. Chatbotin toiminta on kuitenkin pääosin reaktiivista: se odottaa käyttäjän viestiä, vastaa siihen ja jää sitten odottamaan seuraavaa viestiä.

Agentti toimii eri tavalla. Se ei ainoastaan reagoi käyttäjän pyyntöihin, vaan voi myös tarkkailla tilannetta taustalla ja käynnistää toimintoja itsenäisesti ilman erillistä käskyä.

Ero näkyy hyvin esimerkin avulla. Jos kirjoitat ChatGPT:lle: ”Anna minulle ohje pizzan tekemiseen”, saat vastauksen. Tällöin kyse on chatbotista. Jos taas järjestelmä huomaa esimerkiksi, että tietyt jääkaapissa olevat ruoka-aineet ovat vanhenemassa, ja lähettää sinulle oma-aloitteisesti reseptejä niiden hyödyntämiseksi, kyse on agentista.

## Skripti, työnkulku, agentti — kolme eri tasoa

Yritysmaailmassa käytettävät järjestelmät voidaan jakaa kolmeen pääkategoriaan. Näiden erojen ymmärtäminen on tärkeää, koska skripti, työnkulku ja agentti eivät tarkoita samaa asiaa.

**Skripti** on yksinkertainen ohjelma, joka suorittaa täsmälleen ennalta määritellyt komennot. Se ei arvioi tilannetta eikä huomioi seurauksia, vaan tekee sen, mitä sille on määrätty. Esimerkiksi komento ”poista kaikki tiedostot, joiden nimi alkaa sanalla temp_” on skriptille tyypillinen tehtävä. Skripti ei tee päätelmiä, vaan toteuttaa ohjeen sellaisenaan.

**Työnkulku** on useasta vaiheesta koostuva prosessi, jossa toiminta etenee ennalta kirjoitettujen sääntöjen mukaan. Esimerkiksi sähköpostien käsittelyssä työnkulku voi toimia näin: jos viesti sisältää sanan ”lasku”, se siirretään kansioon A, jos se sisältää sanan ”raportti”, se siirretään kansioon B, ja muissa tapauksissa se jätetään saapuneisiin. Työnkulku on skriptiä joustavampi, koska siihen sisältyy päätöslogiikkaa. Se perustuu kuitenkin edelleen valmiiksi määriteltyihin sääntöihin, eikä se muuta toimintaansa itsenäisesti.

**Agentti** on tätä kehittyneempi järjestelmä. Se vastaanottaa tietoa, analysoi tilannetta, tekee päätöksiä, toteuttaa toimintoja ja seuraa niiden tuloksia. Jos lopputulos ei vastaa tavoitetta, agentti voi hyödyntää tätä tietoa seuraavissa tilanteissa ja muuttaa toimintaansa. Se voi myös arvioida, mitä tehtäviä tai tavoitteita kannattaa kulloinkin painottaa.

Ero näkyy hyvin käytännön esimerkissä. Skripti voi lajitella tiedostot pelkän koon perusteella. Työnkulku voi lajitella ne koon ja tiedostotyypin mukaan ennalta määriteltyjen sääntöjen perusteella. Agentti taas voi tehdä lajittelua sen mukaan, mitä tiedostoja käyttäjä todennäköisesti tarvitsee myöhemmin ja miten ne olisi järkevintä järjestää tulevaa käyttöä varten.

## Miten kaikki toimii yhdessä: agentin suoritusputki

Nyt tiedät, mistä osista agentti koostuu ja miten se eroaa skriptistä ja työnkulusta. Pelkät osat eivät kuitenkaan vielä riitä, vaan on myös ymmärrettävä, miten ne toimivat yhdessä. Kuusi komponenttia voidaan ajatella järjestelmän osina, mutta suoritusputki määrittää, missä järjestyksessä ja millä tavalla ne osallistuvat tehtävän suorittamiseen.

Seuraavaksi tarkastellaan, mitä agentin sisällä tapahtuu silloin, kun se saa tehtävän. Esimerkkinä käytetään IT-tukiagenttia.

**Käynnistyminen** (initialization): Prosessi alkaa aina siitä, että jokin tapahtuma käynnistää agentin toiminnan. Käyttäjä voi esimerkiksi lähettää tukipyynnön viestillä: ”Tulostimeni ei toimi.” Syötekäsittelijä vastaanottaa viestin ja muuntaa sen sellaiseen muotoon, jota agentti pystyy käsittelemään. Käytännössä tämä voi tarkoittaa esimerkiksi jäsenneltyä tietuetta, johon tallennetaan viestin sisältö, lähettäjän tiedot ja aikaleima.

**Päättelijä arvioi tilanteen.** Tässä vaiheessa agentti ei vielä suorita varsinaisia toimenpiteitä, vaan arvioi tilannetta. Päättelijä lukee syötteen ja tekee kaksi keskeistä asiaa. Ensin se arvioi, mitä tehtävä edellyttää. Sen jälkeen se suunnittelee, mitä vaiheita tehtävän ratkaiseminen vaatii. Tätä vaihetta kutsutaan reititykseksi: agentti valitsee, mitä toimintapolkua tilanteessa kannattaa seurata. Tulostinongelman kohdalla agentti voi esimerkiksi päätyä siihen, että se hakee ensin ratkaisua tietokannasta, vastaa sitten käyttäjälle ja ohjaa asian ihmiselle, jos ratkaisu ei toimi.

Reitityspäätös ei synny sattumalta. Agentti hyödyntää kielimallia, joka analysoi tilanteen ja arvioi, mikä toimintatapa on tarkoituksenmukaisin. Myös muistilla on tässä vaiheessa merkitystä. Jos agentti on käsitellyt aiemmin useita tulostinongelmia ja havainnut, että ne liittyvät usein verkkoyhteyteen, se voi painottaa tätä vaihtoehtoa uuden tapauksen käsittelyssä.

**Muisti tuo kontekstin.** Agentti ei aloita jokaista tehtävää täysin alusta, vaan se hyödyntää muistiaan. Sillä on yleensä kahdenlaista muistia. Lyhytkestoinen muisti sisältää tiedon, jota tarvitaan juuri käsillä olevan tehtävän aikana. Siihen kuuluu esimerkiksi nykyinen keskustelu, käyttäjän viimeisimmät viestit ja agentin omat edelliset vaiheet. Pitkäkestoinen muisti taas sisältää pysyvämmin tallennettua tietoa, kuten aiempien tehtävien tuloksia, havaittuja toimintamalleja ja tietokantahakujen vastauksia.

Lyhytkestoinen muisti auttaa agenttia pysymään selvillä siitä, mitä parhaillaan tapahtuu. Pitkäkestoinen muisti puolestaan auttaa sitä hyödyntämään aiempia kokemuksia uusissa tilanteissa. Tämän ansiosta agentti ei joudu käsittelemään jokaista tapausta täysin uutena.

Käytännössä tämä voi tarkoittaa esimerkiksi sitä, että agentti tunnistaa saman käyttäjän aiemman ongelman ja hyödyntää sitä uuden tapauksen käsittelyssä: viimeksi tulostinongelman syynä oli se, että tulostin ei ollut samassa verkossa, joten tämä tarkistetaan ensin.

**Työkalut tekevät työn.** Kun suunnitelma on valmis, agentti alkaa toimia. Se kutsuu työkaluja: hakee tietokannasta ratkaisuehdotuksen, tarkistaa tulostimen tilan verkon­hallinta­järjestelmästä, kirjoittaa vastausviestin käyttäjälle. Jokainen työkalu on kuin erikoistunut käsipari — yksi osaa lukea tietokantoja, toinen lähettää sähköposteja, kolmas muokkaa tiedostoja. Agentti valitsee oikean työkalun kuhunkin tilanteeseen. Tätä valintaa kutsutaan työkalureititykseksi, ja se on yksi tärkeimmistä päätöksistä, joita agentti tekee.

**Turvakerros valvoo joka askeleella.** Turvakerros on mukana agentin toiminnassa koko ajan, ei vain prosessin lopussa. Ennen kuin agentti esimerkiksi hakee tietoa, turvakerros tarkistaa, onko sillä oikeus käyttää kyseistä tietokantaa. Ennen viestin lähettämistä se voi arvioida, sisältääkö viesti sellaista arkaluontoista tietoa, jota ei saa jakaa. Toiminnon jälkeen turvakerros voi vielä varmistaa, että kaikki tapahtui sääntöjen ja oikeuksien mukaisesti.

Turvakerros toimii siis kolmessa vaiheessa: ennen toimintoa, sen aikana ja sen jälkeen. Sen tehtävänä on valvoa agentin toimintaa jatkuvasti ja estää virheelliset, vaaralliset tai luvattomat toimenpiteet. Jos jokin näyttää poikkeavalta tai epäilyttävältä, turvakerros voi keskeyttää toiminnan missä vaiheessa tahansa.

**Palautesilmukka sulkee kehän.** Kun agentti on suorittanut toiminnon, se ei vain siirry automaattisesti seuraavaan vaiheeseen, vaan arvioi ensin, mitä tapahtui. Onnistuiko viestin lähetys? Ratkesiko ongelma? Saatiinko käyttäjältä vahvistus siitä, että toimenpide auttoi? Tämän arvioinnin perusteella agentti päättää, miten se jatkaa.

Jos kaikki on sujunut odotetusti, agentti kirjaa onnistumisen ja voi tallentaa ratkaisun pitkäkestoiseen muistiin. Näin samaa tai samankaltaista tapausta voidaan käsitellä tulevaisuudessa tehokkaammin. Jos taas jokin meni pieleen, agentti voi kokeilla toista toimintatapaa, käyttää eri työkalua tai siirtää asian ihmiselle.

Tätä kutsutaan palautesilmukaksi. Sen perusajatus on, että agentin toiminnan tulokset vaikuttavat sen seuraaviin päätöksiin ja myöhempään toimintaan.

**Koko kierto kokonaisuutena.** Kun käyttäjä lähettää tukipyynnön, agentin toiminta etenee vaiheittain. Ensin syötekäsittelijä vastaanottaa viestin ja muuntaa sen käsiteltävään muotoon. Sen jälkeen päättelijä arvioi tilanteen ja suunnittelee sopivan toimintapolun. Muisti tuo mukaan aiempien tapausten tarjoaman kontekstin. Tämän jälkeen päättelijä ohjaa tehtävän oikeille työkaluille, jotka toteuttavat tarvittavat käytännön toimenpiteet. Turvakerros valvoo toimintaa koko prosessin ajan, ja lopuksi palautesilmukka arvioi tuloksen sekä tallentaa hyödylliset havainnot myöhempää käyttöä varten. Kun tämä on tehty, agentti on valmis aloittamaan saman kierron uudelleen seuraavan tehtävän kohdalla.

Juuri tämä jatkuva toimintakierto erottaa agentin muista ratkaisuista. Skripti suorittaa ennalta määrätyn toiminnon ilman tilanteen arviointia. Työnkulku etenee valmiiksi määriteltyä polkua pitkin. Agentti sen sijaan käy läpi toistuvia toimintakierroksia, arvioi niiden tuloksia ja voi muuttaa toimintaansa saamansa palautteen perusteella.

> **Pysähdy hetkeksi:** Valitse omasta työstäsi tai arjestasi jokin toistuva tehtävä. Kuvittele, että suunnittelet agentin hoitamaan sen. Mitkä agentin kuudesta peruskomponentista olisivat tässä tehtävässä keskeisimmät, ja missä suoritusputken vaiheessa ihmisen valvonta olisi tärkeintä?

## Kohti omaa projektia

Agentit-osion aikana rakennat oman n8n-agenttityönkulun. Ensimmäinen askel on valita ongelma, jonka haluat ratkaista. Kun mietit aihetta, palaa tämän oppitunnin käsitteisiin: tarvitseeko ongelmasi autonomista päätöksentekoa vai riittäisikö yksinkertaisempi ratkaisu? Mitkä kuudesta komponentista ovat ongelmassasi kriittisimpiä? Hyvä agenttiongelma on sellainen, jossa pelkkä chatbot tai skripti ei riitä — tarvitaan järjestelmä, joka arvioi tilannetta, tekee päätöksiä ja käyttää työkaluja tavoitteen saavuttamiseksi.

## Yhteenveto

Agentti on automatisoitu järjestelmä, joka toteuttaa useita vaiheita itsenäisesti tavoitteen saavuttamiseksi. Se eroaa chatbotista, skriptistä ja työnkulusta siinä, että se ei vain reagoi, toista samaa toimintoa tai seuraa valmiita sääntöjä, vaan arvioi tilannetta ja ohjaa toimintaansa sen perusteella.

Agentti koostuu kuudesta peruskomponentista: syötekäsittelijästä, päättelijästä, työkaluista, muistista, turvakerroksesta ja palautesilmukasta. Yhdessä nämä muodostavat suoritusputken, jossa jokainen vaihe vaikuttaa seuraavaan. Kun tämän kokonaisuuden ymmärtää, on helpompi nähdä sekä agenttien voima että se, miksi niiden rakentaminen edellyttää tarkkaa suunnittelua, valvontaa ja turvallisuusrajoja.