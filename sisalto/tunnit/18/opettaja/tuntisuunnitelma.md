# Opettajan materiaalit — oppitunti 18: viimeistele ja esittele botti

## Oppitunnin tarkoitus

Tunti 18 on Tekoälyjen käyttö -osion arviointitunti. Oppija käyttää tunnilla 15 ennakkoon kirjoitettuja testejä ja tunnilla 17 saatuja kolmea ensitulosta, tekee yhden nimetyn korjauksen ja toistaa sitä koskevan testin.

Arvioinnin kohde ei ole vain valmis botti. Arvioitavaa näyttöä ovat määrittely, tietopohja, järjestelmäprompti, testit, korjaus, uudelleentestaus ja perusteltu reflektio. Tekninen toteutuspolku ja dokumentoitu suunnittelupolku ovat samanarvoisia, mutta niiden ensimmäinen arviointikriteeri on polkukohtainen.

Tunnin keskeinen kertomus on ennen–jälkeen-muutos. Oppijan ei tarvitse väittää bottiaan valmiiksi tai virheettömäksi. Hänen pitää pystyä osoittamaan, mitä testi paljasti, minkä rajatun muutoksen hän teki ja muuttuiko tulos odotetulla tavalla. Näin arviointi kohdistuu ajatteluun ja kehittämiseen, ei pelkkään esittelytilanteessa näkyvään pintaan.

## Osaamistavoitteet

Oppija:

- hyödyntää tunnilla 17 ajettua tai simuloitua normaalia, kielteistä ja reunatapausta
- vertaa yhden uudelleentestin tulosta samaan etukäteen kirjoitettuun odotukseen
- nimeää yhden korjauksen ja sen kohteen
- ajaa korjausta koskevan testin uudelleen
- esittelee 2–3 minuutissa botin tarkoituksen, rajat ja näytön korjauksen vaikutuksesta tässä testissä
- arvioi, mihin bottia voi ja ei voi käyttää

## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **summatiivinen bottipaketti: botin määrittely, järjestelmäprompti, tietopohja ja testisuunnitelma, tunnin 17 kolme ensitulosta, yksi korjaus ja uudelleentesti, reflektio sekä 2–3 minuutin esittely**.

| Aika | Vaihe | Opettajan tehtävä |
| --- | --- | --- |
| 0–10 min | Tavoite ja aineistot | Varmista, että ennakkoon kirjoitetut testit ja tunnin 17 tulokset ovat käytössä. |
| 10–25 min | Yksi korjaus | Oppija valitsee ensituloksista yhden puutteen, muuttaa yhtä ohjetta, lähdettä tai rajausta ja perustelee valinnan. |
| 25–35 min | Uudelleentestaus | Juuri korjausta koskeva testi ajetaan tai simuloidaan uudelleen muuttamatta odotusta. |
| 35–50 min | Dokumentointi | Oppija kokoaa ennen–jälkeen-näytön ja rajaa päätelmän tähän testiin. |
| 50–70 min | Reflektio | Oppija kirjoittaa 200–300 sanaa tai tekee saavutettavan 2–3 minuutin äänitteen tai selostetun kuvakoosteen. |
| 70–85 min | Esittely tai puolustus | 2–3 minuutin esittely pienryhmässä, tallenteena tai opettajan valitsemana otoksena. Koko luokan kierrosta ei tehdä. |
| 85–90 min | Palautus | Tarkista tiedostot, linkit ja saavutettava vaihtoehto toimimattomalle demolle. |

Pidä testin odotus muuttumattomana korjauksen aikana. Muuten oppija voi tiedostamattaan siirtää tavoitetta sen mukaan, millaisen vastauksen botti sattui tuottamaan. Jos korjaus ei auta, tulos ei ole epäonnistuminen: myös vaikutuksettomaksi osoittautunut muutos on käyttökelpoista näyttöä, kun se on dokumentoitu rehellisesti.

## Arviointikriteerit — 100 pistettä

| Kriteeri | Pisteet | Näyttö |
| --- | --- | --- |
| Polkukohtainen toteutus tai suunnittelu | 25 p | Tekninen polku: todellinen toiminta, tietopohjan kytkentä ja pääsy. Suunnittelupolku: arkkitehtuuri, simuloitu suoritusjälki ja toteuttamatta jääneet ominaisuudet. |
| Järjestelmäprompti | 20 p | Tehtävä, työnkulku, rajat ja testien perusteella tehty korjaus. |
| Tietopohja | 20 p | Perustellut lähteet, haun tai suunnitellun haun kuvaus sekä käyttöoikeusraja. |
| Testaus ja korjaus | 20 p | Tunnin 17 normaali, kielteinen ja reunatapaus sekä tunnin 18 yksi korjaus ja uudelleentesti. |
| Reflektio ja puolustus | 15 p | Valintojen perustelu, rajojen tunnistaminen ja näytön rehellinen tulkinta. |

## Arvioinnin periaatteet

- Älä palkitse pelkkää tuotoksen näyttävyyttä.
- Arvioi prosessista jäävää näyttöä ja oppijan päätöksiä.
- Testissä löytynyt virhe on arvokas havainto, jos se dokumentoidaan ja käsitellään.
- Toimimaton live-demo ei yksin kaada suoritusta, jos kuvakaappaukset, suoritusjälki ja analyysi osoittavat osaamisen.
- Tiettyä maksullista alustaa ei saa vaatia hyväksytyn suorituksen ehdoksi.

Arviointikeskustelussa kannattaa kysyä ensin, millä näytöllä oppija perustelee väitteensä. Jos hän sanoo botin olevan turvallinen, pyydä näyttämään negatiivinen testi. Jos hän kertoo vastauksen parantuneen, pyydä ennen–jälkeen-pari. Tämä ohjaa pois yleisistä laatulauseista kohti havaittavaa osaamista.

## Eriyttäminen

**Tuettu työskentely:** oppija käyttää valmista esittelyrunkoa ja tarvittaessa dokumentoitua suunnittelupolkua. Samat kolme testityyppiä, korjaus ja perustelu säilyvät. Arvioi suunnittelun arkkitehtuuria ja simuloitua suoritusjälkeä, älä teknisiä integraatioita.

**Syventävä reitti:** oppija pyytää vertaisarvioijaa toistamaan yhden testin ja vertaa tuloksia. Pakollinen ydintuotos ei kasva.

## Siirtymä Agentit-osioon

Päätä kysymykseen:

> Botti vastaa käyttäjän viestiin. Mitä uutta tarvitaan, jos järjestelmän pitää seuraavaksi valita työkalu ja toimia käyttäjän puolesta?
