
# Mitä tekoäly on – ja mitä se ei ole?

## Johdanto

Olet varmasti käyttänyt sovellusta, joka suosittelee sinulle musiikkia, elokuvia tai tuotteita. Joskus ajattelet: "Miten tämä tietää, mistä minä pidän?" Tai olet nähnyt uutisen tekoälystä, joka voitti maailman parhaan pelaajan shakkipelissä. Monet ajattelevat, että kaikki "älykäs" ohjelmisto on tekoälyä. Todellisuus on monimutkaisempi — ja paljon kiinnostavampi.

Tekoäly (artificial intelligence, AI) ei ole yksi asia. Se ei ole yksi ohjelmointilogiikka, joka tekee kaiken. Eron ymmärtäminen tekoälyn ja tavallisen ohjelmoinnin välillä auttaa sinua näkemään, miksi jotkut ongelmat vaativat tekoälyä ja jotkut eivät.

## Mitä tekoäly oikeasti on?

Tekoäly on ohjelma, joka oppii datan perusteella eikä vain seuraa ennalta kirjoitettuja sääntöjä. Se tekee päätöksiä tai ennustaa asioita muuttuvissa tilanteissa — ilman, että sinun täytyy ohjelmoida jokainen mahdollinen tapaus käsin.

Kuvitellaan pankin petoksentunnistus. Vanha sääntöpohjainen järjestelmä (rule-based system) voisi sanoa: "Jos tapahtuma on yli 10 000 euroa, hälytä operaattorille." Yksinkertainen, nopea, mutta rajoittunut. Oikea petos saattaa olla paljon pienempi summa, tai se saattaa näyttää normaalilta, kunnes katsot suurempaa kuvaa — tavallisen asiakkaan käyttäytymisen historiaa.

Tekoäly sen sijaan voi oppia miljoonista todellisista transaktioista ja havaita kuvioita, joita ihminen ei näkisi. Se kysyy itseltään: "Näyttääkö tämä transaktio samankaltaiselta kuin petolliset tapaukset, joista minulla on dataa?" Sen sijaan, että sääntö sanoisi "jos X, niin Y", tekoäly vastaa: "Datan kuvioiden perusteella tämä tapahtuma on 97 % todennäköisesti laillinen."

> **Pysähdy hetkeksi:** Kuinka moni päivittäin käyttämäsi sovellus käyttää tekoälyä päätösten tekemiseen? Poikkeavatko ne niistä, joissa on vain kiinteät säännöt?

## Ero automaatioon ja tavalliseen ohjelmointiin

Monet ihmiset sekoittavat tekoälyn automaatioon. "Tämä ohjelmisto teki työtä automaattisesti — sen täytyy olla AI!" Ei. Automaatio tarkoittaa vain sitä, että tietokone tekee työtä ilman, että käyttäjän tarvitsee painaa nappia.

Esimerkiksi sähköpostisovelluksessasi on todennäköisesti sääntöjä, jotka lajittelevat viestit automaattisesti kansioihin. Jos sähköposti sisältää sanat "laskut" ja "lomauttaminen", se menee kansioon "Juridinen". Nämä ovat kiinteitä sääntöjä — ne eivät opi eivätkä muutu. Se on automaatiota, ei tekoälyä.

Monissa IT-alan järjestelmissä on robottisia prosesseja (RPA, Robotic Process Automation). Robotti avaa asiakaspalvelujärjestelmän, lukee lipun, täyttää lomakkeen, lähettää vastauksen — kaikki automaattisesti ja ympäri vuorokauden. Nopeaa ja tehokasta, mutta silti vain rutiineja. Robotti ei opi asiakkaista eikä paranna omaa suoritustaan ajan myötä.

Tekoäly *oppii* datasta. Se muuttuu, paranee, sopeutuu. Kun petoksentunnistus näkee uudenlaisen petoskuvion, se oppii sen. Se ei vaadi uusia sääntöjä; sääntöjä ei ole.

> **Pysähdy hetkeksi:** Jos järjestelmä tekee samat asiat samalla tavalla ilman, että se oppii, onko se tekoälyä?

## Probabilistinen vs. deterministinen ajattelu

Yksi syvällinen ero tekoälyn ja perinteisen ohjelmoinnin välillä liittyy epävarmuuteen.

Tavallisessa ohjelmassa logiikka on deterministinen: if-then-else. Jos x = 5, tee A. Jos x = 10, tee B. Tulokset ovat ennustettavia.

Tekoäly on probabilistinen. Se vastaa: "Tämä on 85 % todennäköisyydellä A ja 15 % todennäköisyydellä B." Se antaa todennäköisyyksiä, ei varmuutta. Tämä on ominaista koneoppimiselle (machine learning): mallin on opittava epätäydellisestä datasta epävarmassa maailmassa.

Esimerkiksi sähköpostiin tulee viesti. Perinteinen roskapostisuodatin käyttää sääntöjä: "Jos otsikko sisältää isoja kirjaimia ja viisi huutomerkkiä, merkitse roskapostiksi." Yksinkertaista. Mutta uusi roskaposti peittelee itseään aina paremmin.

Tekoäly sen sijaan on nähnyt miljoonia todellisia roskaposti- ja laillisia viestejä. Se sanoo: "Tämä viesti muistuttaa 92 % roskaposteista, jotka olen nähnyt." Se ei vaadi sääntöjä. Sääntöjen sijaan sillä on *parametreja* — numeroita, jotka se on oppinut datasta ja jotka määrittävät sen käyttäytymisen.

> **Pysähdy hetkeksi:** Miksi epävarmuus on itse asiassa hyvä asia tekoälylle, mutta huono asia tavalliselle ohjelmalle?

## Konkreettisia esimerkkejä IT-alalta

Pankkisektori käyttää tekoälyä laajasti — mutta ei kaikkialla. Asiakkaan verkkopankissa näkemät sallitut vaihtoehdot ("Maksa lasku", "Siirry tilille") ovat ohjelmoituja sääntöjä. Mutta petoksentunnistus, kuten sanoimme, käyttää tekoälyä. Samoin lainahakemuksen automaattinen hyväksyminen tai hylkääminen voi perustua koneoppimismalliin, joka on oppinut historiallisista hakemuksista ja niiden tuloksista.

Tikettijärjestelmä (ticket system), jota IT-tuki käyttää, saattaa ohjata tikettejä automaattisesti. "Varmenneongelmaan liittyvät sanomat menevät ryhmälle A." Tämä on automaatiota ja perustuu kiinteisiin sääntöihin. Mutta älykkäämpi versio voi käyttää tekoälyyn perustuvia malleja, jotka voivat ennustaa, kuinka kauan tiketin ratkaiseminen kestää tai kuka on paras henkilö siihen — oppien yleisistä malleista.

Sovellusten suositukset (Netflix, Spotify, verkkokauppa) ovat tekoälyä. Ne eivät noudata sääntöä "kuka katsoi tämän elokuvan, katsoi myös tuota". Ne oppivat miljoonista käyttäjien käyttäytymiskuvioista ja ennustavat, mitä sinä haluat seuraavaksi.

## Yhteenveto

Tekoäly ei ole "mikä tahansa älykäs ohjelmisto" eikä "automaatiota". Se on ohjelma, joka oppii datasta ja tekee päätöksiä todennäköisyyksien perusteella ilman eksplisiittisiä sääntöjä. Automaatio ja säännöt ovat terävämpiä, nopeampia ja ennustettavampia — mutta tekoäly on joustavampaa ja oppii. Eron ymmärtäminen auttaa sinua näkemään, miksi jotkut IT-haasteet vaativat tekoälyä ja jotkut pärjäävät hyvin tavallisella ohjelmointilogiikalla.

Thought for a couple of seconds
# Mitä tekoäly on – ja mitä se ei ole?

## Johdanto

Olet varmasti käyttänyt sovellusta, joka suosittelee sinulle musiikkia, elokuvia tai tuotteita. Ehkä olet joskus ajatellut: "Miten tämä tietää, mistä minä pidän?" Tai olet nähnyt uutisen tekoälystä, joka voitti maailman parhaan pelaajan shakkipelissä. Monet ajattelevat, että kaikki "älykäs" ohjelmisto on tekoälyä. Todellisuus on monimutkaisempi — ja paljon kiinnostavampi.

Tekoäly (artificial intelligence, AI) ei ole yksi asia. Se ei ole yksi ohjelmointitapa, joka tekee kaiken. Kun ymmärrät eron tekoälyn ja tavallisen ohjelmoinnin välillä, näet paremmin, miksi jotkin ongelmat vaativat tekoälyä ja jotkin eivät.

## Mitä tekoäly oikeasti on?

Tekoäly on ohjelma, joka oppii datasta eikä vain noudata ennalta kirjoitettuja sääntöjä. Se tekee päätöksiä tai ennustaa asioita muuttuvissa tilanteissa — ilman, että jokaista mahdollista tapausta täytyy ohjelmoida käsin.

Kuvitellaan pankin petoksentunnistus. Vanha sääntöpohjainen järjestelmä (rule-based system) voisi sanoa: "Jos tapahtuma on yli 10 000 euroa, hälytä operaattorille." Se on yksinkertainen ja nopea, mutta myös rajoittunut. Todellinen petos voi olla paljon pienempi summa, tai se voi näyttää normaalilta, kunnes tarkastelet laajempaa kokonaisuutta — esimerkiksi asiakkaan aiempaa käyttäytymistä.

Tekoäly sen sijaan voi oppia miljoonista todellisista transaktioista ja havaita kuvioita, joita ihminen ei huomaisi. Se kysyy ikään kuin itseltään: "Näyttääkö tämä transaktio samanlaiselta kuin petolliset tapaukset, joista minulla on dataa?" Sen sijaan, että sääntö sanoisi "jos X, niin Y", tekoäly vastaa: "Datan kuvioiden perusteella tämä tapahtuma on 97 % todennäköisyydellä laillinen."

> **Pysähdy hetkeksi:** Kuinka moni päivittäin käyttämäsi sovellus käyttää tekoälyä päätösten tekemiseen? Miten ne eroavat niistä, joissa on vain kiinteät säännöt?

## Ero automaatioon ja tavalliseen ohjelmointiin

Monet ihmiset sekoittavat tekoälyn automaatioon. "Tämä ohjelmisto teki työn automaattisesti — sen täytyy olla AI!" Ei välttämättä. Automaatio tarkoittaa vain sitä, että tietokone tekee työn ilman, että käyttäjän tarvitsee painaa nappia.

Esimerkiksi sähköpostisovelluksessasi on todennäköisesti sääntöjä, jotka lajittelevat viestit automaattisesti kansioihin. Jos sähköposti sisältää sanat "laskut" ja "lomauttaminen", se siirtyy kansioon "Juridinen". Nämä ovat kiinteitä sääntöjä — ne eivät opi eivätkä muutu. Se on automaatiota, ei tekoälyä.

Monissa IT-alan järjestelmissä käytetään robottista prosessiautomaatiota (RPA, Robotic Process Automation). Robotti avaa asiakaspalvelujärjestelmän, lukee tiketin, täyttää lomakkeen ja lähettää vastauksen — kaikki automaattisesti ja ympäri vuorokauden. Se on nopeaa ja tehokasta, mutta silti vain rutiinien suorittamista. Robotti ei opi asiakkaista eikä paranna omaa toimintaansa ajan myötä.

Tekoäly *oppii* datasta. Se muuttuu, paranee ja sopeutuu. Kun petoksentunnistus kohtaa uudenlaisen petoskuvion, se voi oppia tunnistamaan sen. Se ei vaadi uusia sääntöjä, koska toiminta ei perustu yksittäisiin käsin kirjoitettuihin sääntöihin.

> **Pysähdy hetkeksi:** Jos järjestelmä tekee samat asiat samalla tavalla ilman, että se oppii, onko se tekoälyä?

## Probabilistinen vs. deterministinen ajattelu

Yksi syvällinen ero tekoälyn ja perinteisen ohjelmoinnin välillä liittyy epävarmuuteen.

Tavallisessa ohjelmassa logiikka on deterministinen: if-then-else. Jos x = 5, tee A. Jos x = 10, tee B. Tulokset ovat ennustettavia.

Tekoäly on probabilistinen. Se vastaa: "Tämä on 85 % todennäköisyydellä A ja 15 % todennäköisyydellä B." Se antaa todennäköisyyksiä, ei varmuutta. Tämä on koneoppimiselle (machine learning) ominaista: mallin täytyy oppia epätäydellisestä datasta epävarmassa maailmassa.

Esimerkiksi sähköpostiin tulee viesti. Perinteinen roskapostisuodatin käyttää sääntöjä: "Jos otsikko sisältää isoja kirjaimia ja viisi huutomerkkiä, merkitse roskapostiksi." Se on yksinkertaista. Mutta uusi roskaposti osaa peitellä itseään yhä paremmin.

Tekoäly sen sijaan on nähnyt miljoonia todellisia roskaposti- ja laillisia viestejä. Se sanoo: "Tämä viesti muistuttaa 92 % niistä roskaposteista, jotka olen nähnyt." Se ei tarvitse erikseen kirjoitettuja sääntöjä. Sääntöjen sijaan sillä on *parametreja* — numeroita, jotka se on oppinut datasta ja jotka ohjaavat sen toimintaa.

> **Pysähdy hetkeksi:** Miksi epävarmuus on itse asiassa hyvä asia tekoälylle, mutta huono asia tavalliselle ohjelmalle?

## Konkreettisia esimerkkejä IT-alalta

Pankkisektori käyttää tekoälyä laajasti — mutta ei kaikkialla. Asiakkaan verkkopankissa näkemät sallitut vaihtoehdot ("Maksa lasku", "Siirry tilille") ovat ohjelmoituja sääntöjä. Mutta petoksentunnistus, kuten edellä todettiin, käyttää tekoälyä. Samoin lainahakemuksen automaattinen hyväksyminen tai hylkääminen voi perustua koneoppimismalliin, joka on oppinut historiallisista hakemuksista ja niiden tuloksista.

Tikettijärjestelmä (ticket system), jota IT-tuki käyttää, saattaa ohjata tikettejä automaattisesti. "Varmenneongelmaan liittyvät viestit menevät ryhmälle A." Tämä on automaatiota ja perustuu kiinteisiin sääntöihin. Älykkäämpi versio voi kuitenkin käyttää tekoälyyn perustuvia malleja, jotka ennustavat, kuinka kauan tiketin ratkaiseminen kestää tai kuka on paras henkilö hoitamaan sen — oppien yleisistä toimintamalleista.

Sovellusten suositukset (Netflix, Spotify, verkkokauppa) ovat tekoälyä. Ne eivät noudata vain sääntöä "kuka katsoi tämän elokuvan, katsoi myös tuota". Ne oppivat miljoonista käyttäjien käyttäytymismalleista ja ennustavat, mitä sinä haluat seuraavaksi.

## Yhteenveto

Tekoäly ei ole "mikä tahansa älykäs ohjelmisto" eikä sama asia kuin "automaatio". Se on ohjelma, joka oppii datasta ja tekee päätöksiä todennäköisyyksien perusteella ilman eksplisiittisiä sääntöjä. Automaatio ja säännöt ovat tarkempia, nopeampia ja ennustettavampia — mutta tekoäly on joustavampaa ja oppivaa. Kun ymmärrät tämän eron, näet paremmin, miksi jotkin IT-haasteet vaativat tekoälyä ja jotkin pärjäävät hyvin tavallisella ohjelmointilogiikalla.



