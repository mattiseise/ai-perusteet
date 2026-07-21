# Tekoälyjen käyttö -osion lopputyö: Rakenna oma apuri-botti

Tämä on Tekoälyjen käyttö -osion arvioitava lopputyö. Suunnittelet rajatun **apuri-botin** ja valitset sille jommankumman kahdesta samanarvoisesta suorituspolusta. Teknisellä toteutuspolulla rakennat botin saatavilla olevalle alustalle ja testaat sen todellista toimintaa. Dokumentoidulla suunnittelupolulla tuotat toteuttamiskelpoisen arkkitehtuurin, simuloidun suoritusjäljen, tietolähteiden kuvaukset, testit ja tunnistetut rajoitukset. Et tee koko työtä yhdellä istumalla — keräät matkan varrella kolme rakennuspalikkaa, teet toteutuspäätöksen tunnilla 16 ja viimeistelet työn tunnilla 18.

> **Miksi näin?** Hyvää bottia ei rakenneta yhdellä tunnilla. Sen pohjana ovat kolme rakennuspalikkaa, jotka kerätään koko osion aikana — testattu promptikortti (tunti 12), botin määrittely (tunti 14) sekä kuratoitu tietopohja ja testisuunnitelma (tunti 15). Tunnilla 17 rakennat teknisen version tai dokumentoidun suunnittelupaketin ja ajat tai simuloit ennalta suunnitellut testit. Tunnilla 18 korjaat, testaat uudelleen ja arvioit lopputuloksen.

## Mitä rakennat?

**Apuri-botin tekninen toteutus tai dokumentoitu suunnitelma**, joka auttaa rajatussa arjen, opiskelun, harrastuksen tai muun itse valitun tilanteen tehtävässä. Botti on *ohjaava, ei käyttäjän puolesta tekevä* — se auttaa käyttäjää etenemään hallitusti.

Valitse polku käytettävissä olevien välineiden ja oppimistavoitteesi perusteella. Polut arvioidaan samoilla enimmäispisteillä, mutta niiden teknistä näyttöä ei teeskennellä samaksi. Suunnittelupolun simuloitu suoritusjälki ei todista integraatioiden, käyttöoikeuksien, tilan säilymisen tai lokituksen toimivan käytännössä.

Valitset itseäsi kiinnostavan, omasta arjestasi tutun aiheen, esimerkiksi:

- **Opiskelu** — selittää käsitteitä, auttaa jäsentämään tehtäviä, toimii harjoittelukaverina kokeisiin
- **Harrastus tai kerho** — säännöt, aikataulut, vinkit ja FAQ jäsenille
- **Tuttu pieni palvelu** — kahvilan, kirjaston tai urheiluseuran FAQ-botti
- **Pelit, musiikki tai sisältö** — auttaa ideoimaan pelin, biisin tai videon
- **Arjen apuri** — auttaa suunnittelemaan vaikka treenirutiinin tai viikkoaikataulun

Valitse aihe, jonka tunnet hyvin omasta arjestasi. Bottisi tuntee juuri sinun aiheesi termit ja tilanteet — se ei ole yleinen avustaja, vaan erikoistunut juuri sinun valitsemaasi tehtävään.

## Polku alusta loppuun

Lopputyö rakentuu kolmesta rakennuspalikasta, jotka kerätään matkan varrella ja kootaan botiksi tunnilla 17.

| Tunti | Mitä teet | Tuotos |
|---|---|---|
| 10–11 | Kilpailutat tekoälyt ja opit tietosuojan | (perusta, ei palautusta) |
| **12** | Rakennat ja testaat yhden uudelleen käytettävän promptikortin | **Rakennuspalikka 1: Promptikortti** |
| 13 | Harjoittelet AI:tä työparina | (tarkennus, ei palautusta) |
| **14** | Suunnittelet botin määrittelyn | **Rakennuspalikka 2: Botin määrittely** |
| **15** | Kuratoit tietopohjan ja kirjoitat testit ennen toteutusta | **Rakennuspalikka 3: Tietopohja ja testisuunnitelma** |
| **16** | Vertaat toteutustapoja, kokeilet yhtä erikoistyökalureittiä ja teet käyttöönottoa koskevat valinnat | **Bottiprojektin valintakortti** |
| **17** | **Kasaat rakennuspalikat ja ajat tai simuloit kolme ennalta kirjoitettua testiä ensimmäisen kerran** | **Ensimmäinen versio, kolme ensitulosta ja korjauslista** |
| **18** | **Teet yhden korjauksen, toistat sitä koskevan testin, reflektoit ja esittelet** | **Lopputyö valmis** |

> **Vinkki:** Tee oma muistiinpanodokumentti, johon kokoat kolme rakennuspalikkaa omiksi alaotsikoikseen. Tunnilla 17 tarvitset silloin vain yhden tiedoston.

## Kolmen rakennuspalikan yleiskuvaus

Yksityiskohtaiset ohjeet kunkin rakennuspalikan tekemiseen saat kyseisellä tunnilla. Tässä lyhyt yleiskuvaus, jotta näet kokonaisuuden.

**Rakennuspalikka 1: Promptikortti (tunti 12)**
Yksi kahdella versiolla testattu prompti, sen käyttötilanne, laatukriteerit ja tunnettu raja. Kortin toimiva rakenne antaa pohjan botin järjestelmäpromptille.

**Rakennuspalikka 2: Botin määrittely (tunti 14)**
Botin "perustamisasiakirja": kenelle botti on, mitä se osaa, mitä se ei tee, mitkä ovat sen rajat. Ilman tätä botti kasvaa hallitsemattomasti.

**Rakennuspalikka 3: Tietopohja ja testisuunnitelma (tunti 15)**
2–4 huolella valittua dokumenttia sekä positiivinen testi, negatiivinen testi ja reunatapaus odotettuine tuloksineen. Kuratointi on tärkeämpää kuin määrä, ja testien odotukset päätetään ennen ensimmäistä ajoa.

## Lopputuotoksen vaatimukset

::: luokka
Tunti 18:n päätteeksi palautat ja esittelet seuraavat:
:::

::: verkko
Lopputyön tuotokset:
:::

**1. Polkukohtainen ydintuotos**

Teknisellä toteutuspolulla annat linkin tai muun pääsyn bottiin sekä tallennetun suoritusjäljen, josta näkyvät todelliset syötteet, vastaukset, tietopohjan käyttö ja toteutukseen kuuluvat jakamis- tai käyttöoikeusasetukset.

Dokumentoidulla suunnittelupolulla annat arkkitehtuurin, simuloidun suoritusjäljen, tietolähteiden tai mahdollisten työkalujen kuvaukset ja luettelon teknisistä ominaisuuksista, joita ei ole toteutettu. Merkitse simuloidut vaiheet näkyvästi.

**2. Botin määrittely**
Tunnin 14 botin määrittely (rakennuspalikka 2), päivitettynä lopputyösi botin mukaisesti.

**3. Järjestelmäprompti kokonaisuudessaan**
Kopioi järjestelmäprompti tiedostoon kokonaisuudessaan. Se on kolmesta rakennuspalikasta koottu toteutusohje, ei neljäs rakennuspalikka.

**4. Lista tietopohjan dokumenteista**
2–4 dokumenttia ja perustelu, miksi valitsit juuri nämä.

**5. Testimatriisi ja korjausketju**
Tunnilla 17 ajetut tai simuloidut normaali tapaus, kielteinen testi ja reunatapaus. Kirjaa jokaisesta syöte, odotus, tulos ja johtopäätös. Tunnilla 18 tee yksi nimetty korjaus ja aja tai simuloi juuri sitä koskeva testi uudelleen samalla odotuksella.

**6. Reflektio (200–300 sanaa)**
Mitä opit botin rakentamisesta, mikä havainto johti korjaukseen ja mitä tekisit seuraavaksi? Saavutettavana vaihtoehtona voit palauttaa 2–3 minuutin äänitteen tai selostetun 3–5 dian kuvakoosteen, joka vastaa samoihin kysymyksiin.

## Lyhyt esittely ja puolustus

Pidä 2–3 minuutin esittely: kerro, kenelle botti on rakennettu, näytä yksi ennen–jälkeen-korjaus ja perustele yksi rajaus. Esitys tehdään pienryhmässä, tallenteena tai opettajan valitsemana otoksena, ei koko luokan peräkkäisenä kierroksena. Vastaa lopuksi yhteen jatkokysymykseen omista valinnoistasi.

> **Vinkki esimerkkikäyttäjästä:** Valitse testaamista ja esittelyä varten yksi tyypillinen käyttäjä. Hän voi olla esimerkiksi harrastuksen aloittava luokkakaveri tai kerhon usein kysyttyjä kysymyksiä selvittävä uusi jäsen. Varmista, että botti toimii juuri hänen tarpeessaan.

## Työkalut ja työskentelytapa

**Alusta tai suunnitteluväline:** valitse tekniselle polulle saatavilla oleva bottialusta. Suunnittelupolulla voit käyttää tavallista tekstinkäsittely-, kaavio- tai esitysvälinettä sekä kielimallia suunnitelman kriittiseen arviointiin.

::: luokka
Opettaja kertoo käytettävissä olevat alustat tunnilla 17. Tunnuksen puuttuminen ei estä työn tekemistä.
:::
::: verkko
Et tarvitse tietyn palvelun tiliä. Jos tekninen alusta ei ole käytettävissä, valitse dokumentoitu suunnittelupolku ja merkitse toteuttamatta jäävät tekniset ominaisuudet.
:::

**Tekoälytyökalu botin rakentamiseen:** Voit käyttää saatavilla olevaa ja aineistollesi hyväksyttyä palvelua. Tarkoitus ei ole keksiä kaikkea itse, vaan käyttää tekoälyä suunnittelun, testauksen ja viimeistelyn tukena. Sinun vastuullasi on, että tekninen botti toimii tarkoituksenmukaisesti tai suunnittelupaketti on toteutuskelpoinen ja että ymmärrät ratkaisun rakenteen kokonaan.

**Yksin tai pareittain:** Lopputyö tehdään yksin, koska bottisi on juuri sinun valitsemasi aiheen näköinen. Voit kuitenkin sparrata luokkakavereiden kanssa rakennuspalikoiden kokoamisessa.

::: luokka
## Arviointi

Lopputyö arvioidaan viiden kriteerin pohjalta. Yhteensä 100 pistettä. Valitse kahdesta ensimmäisestä rivistä vain omaa suorituspolkuasi vastaava 25 pisteen kriteeri; muut neljä kriteeriä ovat yhteisiä.

| Kriteeri | Pisteet | Mitä arvioidaan |
|---|---|---|
| **Tekninen toteutuspolku** | 25 p | Toimiiko rajattu ydintehtävä oikealla alustalla? Ovatko tietopohjan kytkentä, pääsy ja testitulokset todennettavissa? |
| **Dokumentoitu suunnittelupolku** | 25 p | Ovatko arkkitehtuuri, simuloitu suoritusjälki, tietolähteiden kuvaukset ja rajoitukset johdonmukaisia ja toteuttamiskelpoisia? |
| **Järjestelmäprompti** | 20 p | Onko järjestelmäpromptissa selkeä rooli, työnkulku ja rajat? Käyttääkö se oman aiheesi termejä? |
| **Tietopohja** | 20 p | Onko tietopohjassa 2–4 hyvää, perusteltua dokumenttia? Tukevatko ne botin tehtävää? |
| **Testaaminen ja korjaus** | 20 p | Kattavatko tunnin 17 ensitestit normaalin, kielteisen ja reunatapauksen? Näkyvätkö tunnin 18 yksi korjaus ja uudelleentesti? |
| **Reflektio ja puolustus** | 15 p | Perustellaanko valinnat, rajat ja ennen–jälkeen-korjaus lyhyessä esittelyssä? |
:::

::: verkko
## Itsearviointi

Opiskelet omaan tahtiin ilman oppilaitosta, joten arvioit bottisi itse. Valitse kahdesta ensimmäisestä rivistä vain oma polkusi ja käy sen lisäksi neljä yhteistä kriteeriä läpi. Painoarvo kertoo, mihin kannattaa panostaa eniten.

| Kriteeri | Painoarvo | Kysy itseltäsi |
|---|---|---|
| **Tekninen toteutuspolku** | 25 % | Toimiiko bottini oikealla alustalla, ja onko todellisesta tietopohjan käytöstä sekä pääsystä näyttöä? |
| **Dokumentoitu suunnittelupolku** | 25 % | Onko suunnitelmani toteuttamiskelpoinen, onko suoritusjälki merkitty simuloiduksi ja onko tekniset rajoitukset nimetty? |
| **Järjestelmäprompti** | 20 % | Onko järjestelmäpromptissani selkeä rooli, työnkulku ja rajat? Käyttääkö se oman aiheeni termejä? |
| **Tietopohja** | 20 % | Onko tietopohjassani 2–4 hyvää, perusteltua dokumenttia? Tukevatko ne botin tehtävää? |
| **Testaaminen ja korjaus** | 20 % | Olenko ajanut tai simuloinut tunnilla 17 kolme ensitestiä ja dokumentoinut tunnilla 18 yhden korjauksen ja uudelleentestin? |
| **Reflektio ja puolustus** | 15 % | Perustelenko valintani ja rajani sekä näytänkö ymmärrykseni lyhyessä esittelyssä? |
:::

## Aikabudjetti

Lopputyö hajautuu yhdeksälle oppitunnille. Tässä karkea aika-arvio, joka auttaa sinua suunnittelemaan omaa työtäsi.

| Vaihe | Aika-arvio |
|---|---|
| Yksi rakennuspalikka (tunnit 12, 14, 15) | ~25–30 min / palikka |
| Valintakortti ja yhden työkalureitin kokeilu (tunti 16) | ~90 min (koko tunti) |
| Tekninen rakentaminen tai dokumentoidun suunnittelupaketin laatiminen (tunti 17) | ~75 min (koko tunti) |
| Yksi korjaus ja uudelleentesti, reflektio sekä esittely (tunti 18) | ~90 min (koko tunti) |
| **Yhteensä työaikaa kurssin oppitunneilla** | **~5,5–5,75 tuntia** |

> **Vinkki ajankäyttöön:** Rakennuspalikat tehdään niille varatuilla oppitunneilla. Tunnin 18 reflektiota tai esittelyä ei siirretä pakolliseksi kotityöksi.

::: luokka
## Palautus

Palautat tunnilla 18 yhden tiedoston (esim. PDF tai Word), joka sisältää:

- Botin määrittely (päivitettynä)
- Järjestelmäprompti kokonaisuudessaan
- Tietopohjan dokumenttien lista perusteluineen
- Testimatriisi sekä korjauksen ennen–jälkeen-näyttö
- Reflektio (200–300 sanaa tai saavutettava äänite/selostettu kuvakooste)
- Teknisen botin linkki ja suoritusjälki tai suunnittelupolun arkkitehtuuri ja simuloitu suoritusjälki
:::

::: verkko
## Kokoa tuotoksesi

Kokoa työsi yhdeksi tiedostoksi (esim. PDF tai Word) omaan portfolioosi. Näin koko botti dokumentteineen on tallessa yhdessä paikassa:

- Botin määrittely (päivitettynä)
- Järjestelmäprompti kokonaisuudessaan
- Tietopohjan dokumenttien lista perusteluineen
- Testimatriisi sekä korjauksen ennen–jälkeen-näyttö
- Reflektio (200–300 sanaa tai saavutettava äänite/selostettu kuvakooste)
- Teknisen botin linkki ja suoritusjälki tai suunnittelupolun arkkitehtuuri ja simuloitu suoritusjälki

Käy lopuksi läpi yllä oleva itsearviointilista. Halutessasi jaa bottisi tai paketti — mitään ei palauteta minnekään.
:::

---

**Et opettele käyttämään tekoälyä — opit rakentamaan sillä.**


## Arviointitasot

| Kriteeri | Erinomainen | Hyvä | Tyydyttävä | Välttävä | Ei vielä hyväksyttävä |
|---|---|---|---|---|---|
| Tekninen toteutuspolku (25 p) | Botti ratkaisee rajatun tehtävän johdonmukaisesti; todellinen tietopohjan kytkentä, pääsy ja testitulokset ovat todennettavissa. | Ydintehtävä toimii ja keskeisestä kytkennästä sekä pääsystä on näyttö. | Ydintehtävä toimii useimmissa testeissä, mutta yksi olennainen tekninen kohta on epävarma. | Osa toiminnasta näkyy, mutta ydintehtävä tai tekninen näyttö on puutteellinen. | Toimivaa toteutusta tai todennettavaa teknistä näyttöä ei ole. |
| Dokumentoitu suunnittelupolku (25 p) | Arkkitehtuuri, simuloitu suoritusjälki, tietolähteiden kuvaukset ja rajoitukset muodostavat toteuttamiskelpoisen kokonaisuuden. | Rakenne ja suoritusjälki ovat johdonmukaisia, ja toteuttamatta jääneet ominaisuudet on nimetty. | Suunnitelma kattaa ydintehtävän, mutta yksi olennainen rajapinta tai rajoitus jää epäselväksi. | Osa työnkulusta näkyy, mutta arkkitehtuuri tai suoritusjälki on vaikeasti toteutettava. | Suunnittelun ydinnäyttö puuttuu tai simulaatio esitetään teknisenä toteutuksena. |
| Järjestelmäprompti (20 p) | Tarkoitus, rooli, ohjeet, rajat ja epävarmuuden käsittely ovat täsmällisiä ja testien perusteella parannettuja. | Prompti määrittää tarkoituksen, ohjeet ja rajat selkeästi. | Prompti ohjaa ydintehtävää, mutta rajat tai poikkeustilanteet ovat osittaisia. | Prompti on yleinen tai ristiriitainen. | Järjestelmäprompti puuttuu tai ei ohjaa tehtävää. |
| Tietopohja (20 p) | Lähteet ovat tarkoituksenmukaisia, jäljitettäviä, rajattuja ja ajantasaisuus arvioidaan. | Tietopohja tukee tehtävää ja lähteet on nimetty. | Tietopohja on käyttökelpoinen, mutta lähde- tai ajantasaisuustieto on osittainen. | Aineiston sopivuutta ei perustella tai siinä on selviä aukkoja. | Tietopohja tai sitä korvaava annettu aineisto puuttuu. |
| Testaus ja korjaus (20 p) | Kolme ensitestiä kattavat normaalin, kielteisen ja reunatapauksen; yksi korjaus ja uudelleentesti antavat näyttöä korjauksen vaikutuksesta tässä testissä ja päätelmän rajat kerrotaan. | Kaikki kolme testityyppiä, yksi korjaus ja uudelleentesti on dokumentoitu. | Testit kattavat ydintoiminnan, mutta korjausketju jää osittaiseksi. | Testejä on vähän tai tuloksia ei verrata odotukseen. | Testaus ja korjaus puuttuvat. |
| Reflektio ja puolustus (15 p) | Oppija perustelee valinnat, tunnistaa rajat ja vastaa demossa täsmällisesti jatkokysymyksiin. | Valinnat ja rajat perustellaan, ja demo osoittaa oman ymmärryksen. | Reflektio kuvaa työtä, mutta perustelut tai demo jäävät yleisiksi. | Reflektio on luettelomainen tai oma ymmärrys jää epäselväksi. | Reflektio ja demo tai puolustus puuttuvat. |
