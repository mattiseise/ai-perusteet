# Mitä tekoäly on – ja mitä se ei ole?

## Johdanto

Olet varmasti käyttänyt sovellusta, joka esittelee sinulle musiikkia, elokuvia tai tuotteita. Joskus ajattelet: "Miten tämä tietää, mitä minä pidän?" Tai olet nähnyt uutisen tekoälystä, joka voitti maailman parhaan pelaajan shakkipelissä. Monet ajattelevat, että kaikki "älykäs" ohjelmisto on tekoälyä. Todellisuus on monimutkaisempi — ja paljon kiinnostavampi.

Tekoäly (artificial intelligence, AI) ei ole yksi asia. Se ei ole yhtä ohjelmointilogiikkaa, joka tekee kaiken. Ymmärtää ero tekoälyn ja tavallisen ohjelmoinnin välillä auttaa sinua näkemään, miksi jotkut ongelmat vaativat AI:ta ja jotkut ei.

## Mitä tekoäly oikeasti on?

Tekoäly on ohjelma, joka oppii datan perusteella eikä vain seuraa ennalta kirjoitettuja sääntöjä. Se tekee päätöksiä tai ennustaa asioita muuttuvissa tilanteissa — ilman, että sinun tarvitse ohjelmoida jokainen mahdollinen tapaus käsin.

Kuvitella pankin petoksentunnistus. Vanha sääntöpohjainen järjestelmä (rule-based system) voisi sanoa: "Jos tapahtuma on yli 10 000 euroa, hälyytä operaattorille." Yksinkertainen, nopea, mutta rajoitettu. Oikea petos saattaa olla paljon pienempi summa, tai se saattaa näyttää normaalilta kunnes katsot suurempaa kuvaa — tavallisen asiakkaan käyttäytymisen historiaa.

Tekoäly sen sijaan voi oppia miljoonista todellisista transaktioista ja havaita kuvioita, joita ihminen ei näkisi. Se kysyy itseltään: "Näyttääkö tämä transaktio samankaltaiselta kuin petolliset tapaukset, joita minulla on data?" Sen sijaan että sääntö sanoo "jos X, niin Y", tekoäly vastaa: "Perustuen datan kuvioihin, tämä tapahtuma on 97 % todennäköisesti laillinen."

> **Pysähdy hetkeksi:** Kuinka moni sovellus, jota käytät päivittäin, käyttää tekoälyä päätösten tekemiseen? Poikkeaa niistä, joissa on vain kiinteät säännöt?

## Ero automaatioon ja tavalliseen ohjelmointiin

Monet ihmiset sekoittavat tekoälyn automaatioon. "Tämä ohjelmisto teki työtä automaattisesti — pitää olla AI!" Ei. Automaatio tarkoittaa vain sitä, että tietokone tekee työtä ilman käyttäjän nappia painamista.

Esimerkiksi sähköpostisovelluksessasi on todennäköisesti säännöt, jotka lajittelevat viestit automaattisesti kansioihin. Jos sähköposti sisältää sanat "laskut" ja "lomauttaminen", se menee kansioon "Juridinen". Nämä ovat kiinteitä sääntöjä — ne eivät oppi tai muutu. Se on automaatio, ei tekoäly.

Monissa IT-alan järjestelmissä on roboottisia prosesseja (RPA, Robotic Process Automation). Robotti avaa asiakaspalvelujärjestelmän, lukee lippun, täyttää lomakkeen, lähettää vastauksen — kaikki automaattisesti ja 24/7. Nopea, tehokasta, mutta silti vain rutiineja. Robotti ei opi asiakkaista tai paranna omaa suoritustaan ajan myötä.

Tekoäly *oppii* datasta. Se muuttuu, paranee, sopeutuu. Kun petoksentunnistus näkee uuden tyyppisen petosten kuvion, se oppii sen. Se ei vaadi uusia sääntöjä; sääntöjä ei ole.

> **Pysähdy hetkeksi:** Jos järjestelmä tekee samat asiat samalla tavalla ilman, että se oppii, onko se tekoäly?

## Probabilistinen vs. deterministinen ajattelu

Yksi syvä ero tekoälyn ja perinteisen ohjelmoinnin välillä on epävarmuus.

Tavallisessa ohjelmassa logiikka on deterministinen: if-then-else. Jos x = 5, tee A. Jos x = 10, tee B. Tulokset ovat ennustettavia.

Tekoäly on probabilistinen. Se vastaa: "Tämä on 85 % todennäköisyydellä A, ja 15 % todennäköisyydellä B." Se antaa todennäköisyydet, ei varmuutta. Tämä on ominaista koneoppimiselle (machine learning): mallin on opittava epätäydellisestä datasta epävarmassa maailmassa.

Esimerkiksi sähköpostiin tulee viesti. Perinteinen spämmi-suodatin käyttää sääntöjä: "Jos otsikko sisältää CAPITAL LETTERS ja viisi huutomerkkiä, merkitse spämmeiksi." Yksinkertainen. Mutta uusi spämmi aina peittelee itseään paremmin.

Tekoäly sen sijaan on nähnyt miljooneja todellisia spämmi- ja laillisia viestejä. Se sanoo: "Tämä viesti muistuttaa 92 % spämmeistä, jotka olen nähnyt." Se ei tarvitse sääntöjä. Sääntöjen sijaan sillä on *parametrit* — numeroita, jotka se on oppinut datasta ja jotka määrittävät sen käyttäytymisen.

> **Pysähdy hetkeksi:** Miksi epävarmuus on itse asiassa hyvä asia tekoälylle, mutta huono asia tavalliselle ohjelmalle?

## Konkreettisia esimerkkejä IT-alalta

Pankkisektori käyttää tekoälyä laajasti — mutta ei kaikkialle. Asiakkaan verkkopankissa näkemät sallitut vaihtoehdot ("Maksa lasku", "Siirry tilille") ovat ohjelmoituja sääntöjä. Mutta petoksentunnistus, kuten sanoimme, käyttää tekoälyä. Samoin lainahakemuksen automaattinen hyväksyntä tai hylkääminen perustuu koneoppimismalliin, joka on oppinut historiallisista hakemuksista ja niiden tuloksista.

Tikettijärjestelmä (ticket system), jota IT-tuki käyttää, saattaa ohjata tikettejä automaattisesti. "Varmenneongelmaan liittyvät sanomat menevät ryhmälle A." Automaatio, kiinteät säännöt. Mutta älympi version tekoälymallit voivat ennustaa, kuinka kauan tiketin ratkaiseminen kestää tai kuka on paras henkilö siihen — opittuina yleisistä malleista.

Sovellusten suositukset (Netflix, Spotify, verkkokauppa) ovat tekoälyä. Ne eivät noudata sääntöä "kuka katso tämän elokuvan, katso myös tuota". Ne oppivat miljoonia käyttäjien käyttäytymiskuvioista ja ennustavat, mitä sinä haluat seuraavaksi.

## Yhteenveto

Tekoäly ei ole "mikä tahansa älykäs ohjelmisto" eikä "automaatio". Se on ohjelma, joka oppii datasta ja tekee päätöksiä todennäköisyyksien perusteella ilman eksplisiittisiä sääntöjä. Automaatio ja säännöt ovat terävämpiä, nopeampia, ennustettavampia — mutta tekoäly on joustavampi ja oppii. Ymmärtää ero auttaa sinua näkemään, miksi jotkut IT-haasteet vaativat tekoälyä ja jotkut pärjäävät hyvin tavallisella koodilla.
