# Oppitunti 18 — summatiivisen arvioinnin ohje

Tämä on Tekoälyjen käyttö -osion summatiivinen arviointi. Arvioi prosessista syntyvää näyttöä, älä tiettyä palvelua tai pelkän lopputuloksen viimeisteltyä pintaa. Oppija valitsee teknisen toteutuspolun tai dokumentoidun suunnittelupolun. Polut ovat samanarvoisia, mutta niiden polkukohtainen näyttö arvioidaan eri kuvauksilla.

## Pakollinen näyttö ennen pisteytystä

Työpaketissa pitää näkyä:

- botin tarkoitus, käyttäjä, rajaus ja järjestelmäprompti,
- tietopohjan 2–4 lähdettä, hakutavan kuvaus ja käyttöoikeusraja perusteluineen,
- normaali testi, kielteinen testi ja reunatapaus,
- jokaisesta testistä syöte, odotus, toteutunut tai simuloitu tulos ja johtopäätös,
- yksi nimetty korjaus ja sitä koskeva uudelleentesti,
- 200–300 sanan reflektio tai saavutettava vaihtoehto sekä 2–3 minuutin esittely tai puolustus.

Teknisellä polulla työpaketissa on lisäksi pääsy bottiin tai muu todennettava näyttö todellisesta toiminnasta. Suunnittelupolulla työpaketissa on arkkitehtuuri, simuloitu suoritusjälki, tietolähteiden tai työkalujen kuvaukset ja luettelo toteuttamatta jääneistä ominaisuuksista. Älä hyväksy simulaatiota näytöksi integraation, käyttöoikeuden, tilan säilymisen tai lokituksen teknisestä toiminnasta.

## Arviointitasot

Pisteytä viisi kriteeriä niiden painoarvoilla. Valitse taulukon kahdesta ensimmäisestä rivistä vain oppijan suorituspolkua vastaava 25 pisteen rivi. Sen lisäksi pisteytetään neljä yhteistä kriteeriä. Valitse kullekin kriteerille lähin tasokuvaus ja perustele palaute työpaketin näytöllä.

| Kriteeri | Erinomainen | Hyvä | Tyydyttävä | Välttävä | Ei vielä hyväksyttävä |
|---|---|---|---|---|---|
| **Tekninen toteutuspolku — 25 p** | Rajattu ydintehtävä toimii johdonmukaisesti; todellinen tietopohjan kytkentä, jakaminen tai käyttöoikeus ja testitulokset ovat todennettavissa. | Ydintehtävä toimii ja keskeisestä kytkennästä sekä pääsystä on näyttö. | Ydintehtävä toimii useimmissa testeissä, mutta yksi olennainen tekninen kohta jää epävarmaksi. | Osa toiminnasta näkyy, mutta ydintehtävä tai tekninen näyttö on puutteellinen. | Toimivaa toteutusta tai todennettavaa teknistä näyttöä ei ole. |
| **Dokumentoitu suunnittelupolku — 25 p** | Arkkitehtuuri, simuloitu suoritusjälki, tietolähteiden tai työkalujen kuvaukset ja rajoitukset muodostavat toteuttamiskelpoisen kokonaisuuden. | Rakenne ja suoritusjälki ovat johdonmukaisia, ja toteuttamatta jääneet ominaisuudet on nimetty. | Suunnitelma kattaa ydintehtävän, mutta yksi olennainen rajapinta tai rajoitus jää epäselväksi. | Osa työnkulusta näkyy, mutta arkkitehtuuri tai suoritusjälki on vaikeasti toteutettava. | Suunnittelun ydinnäyttö puuttuu tai simulaatio esitetään teknisenä toteutuksena. |
| **Järjestelmäprompti — 20 p** | Tarkoitus, rooli, ohjeet, rajat ja epävarmuuden käsittely ovat täsmällisiä ja testien perusteella parannettuja. | Prompti määrittää tarkoituksen, ohjeet ja rajat selkeästi. | Prompti ohjaa ydintehtävää, mutta rajat tai poikkeustilanteet ovat osittaisia. | Prompti on yleinen tai ristiriitainen. | Järjestelmäprompti puuttuu tai ei ohjaa tehtävää. |
| **Tietopohja — 20 p** | Lähteet ovat tarkoituksenmukaisia, jäljitettäviä ja rajattuja; ajantasaisuus ja käyttöoikeus arvioidaan. | Aineisto tukee tehtävää ja lähteet on nimetty sekä perusteltu. | Aineisto on käyttökelpoinen, mutta lähde- tai ajantasaisuustieto on osittainen. | Aineiston sopivuutta ei perustella tai siinä on selviä aukkoja. | Tietopohja tai sitä korvaava annettu aineisto puuttuu. |
| **Testaus ja korjaus — 20 p** | Tunnin 17 normaali, kielteinen ja reunatapaus on dokumentoitu; tunnin 18 yksi korjaus ja uudelleentesti antavat näyttöä korjauksen vaikutuksesta tässä testissä, ja päätelmän rajat kerrotaan. | Kaikki kolme testityyppiä, yksi korjaus ja uudelleentesti näkyvät. | Testit kattavat ydintoiminnan, mutta korjausketju jää osittaiseksi. | Testejä on vähän tai tuloksia ei verrata odotukseen. | Testaus ja korjaus puuttuvat. |
| **Reflektio ja puolustus — 15 p** | Oppija perustelee valinnat, tunnistaa rajat ja vastaa demossa täsmällisesti jatkokysymykseen. | Valinnat ja rajat perustellaan, ja demo osoittaa oman ymmärryksen. | Reflektio kuvaa työtä, mutta perustelut tai demo jäävät yleisiksi. | Reflektio on luettelomainen tai oma ymmärrys jää epäselväksi. | Reflektio ja demo tai puolustus puuttuvat. |

## Pisteytys

Muunna taso kriteerin pisteiksi suhteessa painoarvoon:

- **Erinomainen:** 100 % kriteerin pisteistä
- **Hyvä:** 80 %
- **Tyydyttävä:** 60 %
- **Välttävä:** 40 %
- **Ei vielä hyväksyttävä:** 0–20 % sen mukaan, onko osittaista näyttöä

Pyöristä kokonaispisteet lähimpään kokonaislukuun. Käytä oppilaitoksen omaa hyväksymisrajaa, jos sellainen on päätetty.

## Prosessinäytön aitous

Älä yritä päätellä vilppiä tekstin tyylistä. Tarkista sen sijaan todennettavat yhteydet:

- vastaavatko promptin versiot kuvattua korjausta,
- onko ennen–jälkeen-tuloksissa korjauksen mukainen muutos,
- pystyykö oppija selittämään yhden rajauksen ja yhden epäonnistuneen testin omin sanoin,
- ovatko lähteet olemassa ja liittyvätkö ne botin tehtävään.

Jos yhteys ei selviä, pyydä oppijaa täydentämään suoritusjälkeä tai näyttämään yksi testi. Epäonnistunut testi ei laske arviota, jos oppija tunnistaa syyn, korjaa toteutusta ja testaa uudelleen.

## Palautteen rakenne

Anna palaute viidellä lyhyellä kohdalla, yksi kutakin kriteeriä kohti. Nimeä lopuksi:

1. vahvin prosessinäyttö,
2. yksi täsmällinen seuraava korjaus,
3. kokonaispisteet ja käytetty hyväksymisraja.
