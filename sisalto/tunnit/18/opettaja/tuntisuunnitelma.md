# Opettajan materiaalit — oppitunti 18: viimeistele ja esittele botti

## Oppitunnin tarkoitus

Tunti 18 on Tekoälyjen käyttö -osion arviointitunti. Oppija käyttää tunnilla 15 ennakkoon kirjoitettuja testejä ja tunnilla 17 saatua ensimmäistä testitulosta, tekee vähintään yhden korjauksen ja osoittaa uudelleentestillä, miten korjaus vaikutti.

Arvioinnin kohde ei ole vain valmis botti. Arvioitavaa näyttöä ovat määrittely, tietopohja, järjestelmäprompti, testit, korjaus, uudelleentestaus ja perusteltu reflektio.

Tunnin keskeinen kertomus on ennen–jälkeen-muutos. Oppijan ei tarvitse väittää bottiaan valmiiksi tai virheettömäksi. Hänen pitää pystyä osoittamaan, mitä testi paljasti, minkä rajatun muutoksen hän teki ja muuttuiko tulos odotetulla tavalla. Näin arviointi kohdistuu ajatteluun ja kehittämiseen, ei pelkkään esittelytilanteessa näkyvään pintaan.

## Osaamistavoitteet

Oppija:

- ajaa positiivisen, negatiivisen ja reunatapaustestin
- vertaa tulosta etukäteen kirjoitettuun odotukseen
- nimeää yhden korjauksen ja sen kohteen
- ajaa korjausta koskevan testin uudelleen
- esittelee botin tarkoituksen, rajat ja näytön parannuksesta
- arvioi, mihin bottia voi ja ei voi käyttää

## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **summatiivinen bottipaketti: määrittely, prompti, tietopohja, testit, yksi korjaus, uudelleentesti ja esittely**.

| Aika | Vaihe | Opettajan tehtävä |
| --- | --- | --- |
| 0–10 min | Tavoite ja aineistot | Varmista, että ennakkoon kirjoitetut testit ja tunnin 17 tulokset ovat käytössä. |
| 10–30 min | Testaus | Oppija ajaa tai täydentää positiivisen, negatiivisen ja reunatapauksen. |
| 30–45 min | Korjaus | Oppija nimeää ongelman, muuttaa yhtä ohjetta, lähdettä tai rajausta ja perustelee valinnan. |
| 45–55 min | Uudelleentestaus | Sama testi ajetaan uudelleen muuttamatta odotusta. |
| 55–70 min | Dokumentointi | Oppija kokoaa ennen–jälkeen-näytön ja käytön rajat. |
| 70–85 min | Esittely tai puolustus | Oppija esittelee tarkoituksen, yhden testin, korjauksen ja rajoituksen. |
| 85–90 min | Palautus | Tarkista tiedostot, linkit ja saavutettava vaihtoehto toimimattomalle demolle. |

Pidä testin odotus muuttumattomana korjauksen aikana. Muuten oppija voi tiedostamattaan siirtää tavoitetta sen mukaan, millaisen vastauksen botti sattui tuottamaan. Jos korjaus ei auta, tulos ei ole epäonnistuminen: myös vaikutuksettomaksi osoittautunut muutos on käyttökelpoista näyttöä, kun se on dokumentoitu rehellisesti.

## Arviointikriteerit — 20 pistettä

| Kriteeri | 1 p | 2 p | 3 p | 4 p |
| --- | --- | --- | --- | --- |
| Määrittely ja tarkoitus | epäselvä | osittain rajattu | selkeä ja käyttäjälähtöinen | selkeä, testattava ja johdonmukainen |
| Ohjeet ja tietopohja | puutteiset | perusosat mukana | tehtävään sopivat ja perustellut | rajat, lähteet ja puutteet näkyvät tarkasti |
| Testaus ja korjaus | vähäinen | testejä ilman selvää korjausta | kolme testityyppiä ja yksi korjaus | ennen–jälkeen-näyttö osoittaa korjauksen vaikutuksen |
| Esittely ja dokumentointi | vaikeasti seurattava | pääkohdat näkyvät | rakenne ja näyttö ovat selkeitä | päätökset, rajat ja toistettavuus perustellaan vakuuttavasti |
| Reflektio ja vastuu | yleinen | tunnistaa joitakin rajoja | arvioi käyttöä ja omaa vastuuta | yhdistää näytön, rajat ja jatkokehityksen kriittisesti |

## Arvioinnin periaatteet

- Älä palkitse pelkkää tuotoksen näyttävyyttä.
- Arvioi prosessista jäävää näyttöä ja oppijan päätöksiä.
- Testissä löytynyt virhe on arvokas havainto, jos se dokumentoidaan ja käsitellään.
- Toimimaton live-demo ei yksin kaada suoritusta, jos kuvakaappaukset, suoritusjälki ja analyysi osoittavat osaamisen.
- Tiettyä maksullista alustaa ei saa vaatia hyväksytyn suorituksen ehdoksi.

Arviointikeskustelussa kannattaa kysyä ensin, millä näytöllä oppija perustelee väitteensä. Jos hän sanoo botin olevan turvallinen, pyydä näyttämään negatiivinen testi. Jos hän kertoo vastauksen parantuneen, pyydä ennen–jälkeen-pari. Tämä ohjaa pois yleisistä laatulauseista kohti havaittavaa osaamista.

## Eriyttäminen

**Tukireitti:** oppija käyttää dokumentoitua kuivaharjoittelua ja valmista esittelyrunkoa. Samat kolme testityyppiä, korjaus ja perustelu säilyvät.

**Syventävä reitti:** oppija pyytää vertaisarvioijaa toistamaan yhden testin ja vertaa tuloksia. Pakollinen ydintuotos ei kasva.

## Siirtymä Agentit-osioon

Päätä kysymykseen:

> Botti vastaa käyttäjän viestiin. Mitä uutta tarvitaan, jos järjestelmän pitää seuraavaksi valita työkalu ja toimia käyttäjän puolesta?
