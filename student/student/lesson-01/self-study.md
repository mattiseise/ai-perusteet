# Älykäs vai sääntö? — mitä tekoäly oikeasti tekee

## Johdanto

Olet varmasti käyttänyt sovellusta, joka suosittelee sinulle musiikkia, elokuvia tai tuotteita. Ehkä olet joskus ajatellut: "Miten tämä tietää, mistä minä pidän?" Tai olet nähnyt uutisen tekoälystä, joka voitti maailman parhaan pelaajan shakkipelissä. Monet ajattelevat, että kaikki "älykäs" ohjelmisto on tekoälyä. Todellisuus on monimutkaisempi — ja paljon kiinnostavampi. Tekoäly (artificial intelligence, AI) ei ole yksi asia. Se ei ole yksi ohjelmointitapa, joka tekee tai ymmärtää kaiken kaikesta. Tämän osion jälkeen ymmärrät, miten tekoäly eroaa tavallisesta ohjelmoinnista. Osaat myös paremmin arvioida, millaiset ongelmat vaativat tekoälyä ja millaiset eivät.

Tämän tunnin jälkeen sinulla on uusi todistusaineisto tuomaripöydällesi: tietävätkö tekoälyt todella mitä ne tekevät, vai ovat ne vain edistyneitä sääntökonekoneita?

## Mitä tekoäly oikeasti on?

Tekoäly on ohjelma, joka oppii datasta eikä vain noudata ennalta kirjoitettuja sääntöjä. Se tekee päätöksiä tai ennustaa asioita muuttuvissa tilanteissa — ilman, että jokaista mahdollista tapausta täytyy ohjelmoida käsin.

Kuvitellaan pankin petoksentunnistusjärjestelmä. Perinteinen sääntöpohjainen järjestelmä voisi toimia esimerkiksi näin: ”Jos tapahtuma on yli 10 000 euroa, lähetä hälytys operaattorille.” Tällainen ratkaisu on yksinkertainen ja nopea, mutta samalla melko rajallinen. Todellinen petos voi liittyä paljon pienempään summaan, ja yksittäinen rahansiirto voi näyttää täysin normaalilta. Epäilyttäväksi tapaus muuttuu usein vasta silloin, kun sitä tarkastellaan osana laajempaa kokonaisuutta, kuten asiakkaan aiempaa käyttäytymistä.

Tekoäly toimii eri tavalla. Se voi oppia miljoonista oikeista transaktioista ja löytää niistä sellaisia yhteyksiä ja poikkeamia, joita ihminen tai yksinkertainen sääntöjärjestelmä ei huomaisi. Siksi se ei perustu vain yksittäisiin sääntöihin, kuten ”jos X, niin Y”, vaan muodostaa datan perusteella arvion siitä, kuinka todennäköisesti tapahtuma on laillinen tai petollinen. Esimerkiksi se voi päätellä: ”Tämän tapahtuman todennäköisyys olla laillinen on 97 prosenttia.”

> **Pysähdy hetkeksi:** Kuinka moni päivittäin käyttämäsi sovellus käyttää tekoälyä päätösten tekemiseen? Miten ne eroavat niistä, joissa on vain kiinteät säännöt?

## Ero automaatioon ja tavalliseen ohjelmointiin

Monet ihmiset sekoittavat tekoälyn automaatioon. "Tämä ohjelmisto teki työn automaattisesti — sen täytyy olla AI!" Ei välttämättä. Automaatio tarkoittaa vain sitä, että tietokone tekee työn ilman, että käyttäjän tarvitsee painaa nappia.

Esimerkiksi sähköpostisovelluksessasi on todennäköisesti sääntöjä, jotka lajittelevat viestit automaattisesti kansioihin. Jos sähköposti sisältää sanat "laskut" ja "lomauttaminen", se siirtyy kansioon "Juridinen". Nämä ovat kiinteitä sääntöjä — ne eivät opi eivätkä muutu. Se on automaatiota, ei tekoälyä.

Monissa IT-alan järjestelmissä käytetään robottista prosessiautomaatiota (RPA, Robotic Process Automation). Robotti avaa asiakaspalvelujärjestelmän, lukee tiketin, täyttää lomakkeen ja lähettää vastauksen — kaikki automaattisesti ja ympäri vuorokauden. Se on nopeaa ja tehokasta, mutta silti vain rutiinien suorittamista. Robotti ei opi asiakkaista eikä paranna omaa toimintaansa ajan myötä.

Tekoäly *oppii* datasta. Se muuttuu, paranee ja sopeutuu. Kun petoksentunnistus kohtaa uudenlaisen petoskuvion, se voi oppia tunnistamaan sen. Se ei vaadi uusia sääntöjä, koska toiminta ei perustu yksittäisiin käsin kirjoitettuihin sääntöihin.

> **Pysähdy hetkeksi:** Jos järjestelmä tekee samat asiat samalla tavalla ilman, että se oppii, onko se tekoälyä?

## Probabilistinen vs. deterministinen ajattelu

Yksi syvällinen ero tekoälyn ja perinteisen ohjelmoinnin välillä liittyy epävarmuuteen.

Tavallinen ohjelma toimii deterministisesti: se noudattaa ennalta kirjoitettuja sääntöjä ja tuottaa ennustettavan tuloksen. Tekoäly puolestaan toimii todennäköisyyksien varassa. Se ei anna varmaa vastausta, vaan arvion siitä, mikä lopputulos on datan perusteella todennäköisin. Tämä on koneoppimisen ydin: päätöksiä tehdään epätäydellisen datan pohjalta epävarmassa maailmassa.

Kun sähköpostiin tulee viesti, perinteinen roskapostisuodatin tarkistaa ennalta määriteltyjä sääntöjä. Se voi esimerkiksi toimia näin: ”Jos otsikossa on paljon isoja kirjaimia ja useita huutomerkkejä, merkitse viesti roskapostiksi.” Tämä on yksinkertainen tapa toimia, mutta samalla rajallinen, koska uudet roskapostit osaavat yhä paremmin näyttää tavallisilta viesteiltä.

Tekoäly sen sijaan on nähnyt miljoonia todellisia roskaposti- ja laillisia viestejä. Se sanoo: "Tämä viesti muistuttaa 92 % niistä roskaposteista, jotka olen nähnyt." Se ei tarvitse erikseen kirjoitettuja sääntöjä. Sääntöjen sijaan sillä on *parametreja* — numeroita, jotka se on oppinut datasta ja jotka ohjaavat sen toimintaa.

> **Pysähdy hetkeksi:** Miksi epävarmuus on itse asiassa hyvä asia tekoälylle, mutta huono asia tavalliselle ohjelmalle?

## Konkreettisia esimerkkejä IT-alalta

Pankkisektorilla tekoälyä käytetään laajasti, mutta ei kaikessa. Esimerkiksi asiakkaan verkkopankissa näkyvät toiminnot, kuten ”Maksa lasku” ja ”Siirry tilille”, perustuvat tavalliseen ohjelmointiin ja ennalta määriteltyihin sääntöihin. Sen sijaan petoksentunnistuksessa voidaan hyödyntää tekoälyä, kuten edellä todettiin. Myös lainahakemuksen automaattinen hyväksyminen tai hylkääminen voi perustua koneoppimismalliin, joka on oppinut historiallisista hakemuksista ja niiden lopputuloksista.

Sama ero näkyy myös IT-tuen tikettijärjestelmissä. Yksinkertainen järjestelmä voi ohjata tikettejä kiinteiden sääntöjen perusteella, esimerkiksi näin: ”Varmenneongelmaan liittyvät viestit ohjataan ryhmälle A.” Tämä on automaatiota, mutta ei vielä tekoälyä. Kehittyneempi järjestelmä voi sen sijaan hyödyntää tekoälymalleja, jotka ennustavat esimerkiksi tiketin ratkaisuaikaa tai sitä, kenellä olisi parhaat valmiudet hoitaa se. Tällöin järjestelmä ei perustu vain yksittäisiin sääntöihin, vaan oppii aiemmista tapauksista ja yleisistä toimintamalleista.

Netflixin, Spotifyn ja verkkokauppojen suositukset ovat hyvä esimerkki tekoälyn käytöstä. Ne eivät toimi pelkkien yksinkertaisten sääntöjen varassa, vaan oppivat miljoonista käyttäjien valinnoista, mieltymyksistä ja käyttäytymismalleista. Tämän perusteella ne pyrkivät ennustamaan, mitä haluat nähdä, kuunnella tai ostaa seuraavaksi.

## Yhteenveto

Tekoäly ei tarkoita mitä tahansa älykästä ohjelmistoa, eikä se ole sama asia kuin automaatio. Tekoäly on ohjelma, joka oppii datasta ja tekee arvioita tai päätöksiä todennäköisyyksien perusteella ilman, että kaikkia sääntöjä on kirjoitettu sille valmiiksi. Automaatio ja sääntöpohjaiset järjestelmät ovat usein tarkempia, nopeampia ja ennustettavampia. Tekoälyn vahvuus taas on siinä, että se on joustavampi ja pystyy oppimaan monimutkaisista ilmiöistä. Kun tämän eron ymmärtää, on helpompi hahmottaa, miksi jotkin IT-haasteet vaativat tekoälyä ja toiset voidaan ratkaista hyvin tavallisella ohjelmointilogiikalla.

Seuraavalla tunnilla perehdyt siihen, kuinka montaa eri tyyppiä tekoälystä on olemassa — ja että "älykkyys" on monessa muodossa.