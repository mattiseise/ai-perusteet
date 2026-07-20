# Opettajan materiaalit — oppitunti 14: käyttäjä, tehtävä ja rajat

## Oppitunnin tarkoitus

Oppija laatii botista määrittelydokumentin ennen järjestelmäpromptin kirjoittamista tai rakentamista. Tunnin ydin on erottaa toisistaan **tarve**, **määrittely** ja **toteutus**.

Tällä tunnilla ei rakenneta bottia, kirjoiteta valmista järjestelmäpromptia eikä ajeta botin testejä. Tämä rajaus on tärkeä: oppijan pitää ensin osata perustella, mitä ollaan rakentamassa.

Oppijalle suunnittelun arvo voi jäädä abstraktiksi, jos tunti näyttäytyy vain lomakkeen täyttämisenä. Mallinna siksi määrittely päätösketjuna: käyttäjän tilanteesta seuraa tehtävä, tehtävästä havaittava onnistuminen ja onnistumisesta tarvittava eteneminen. Rajat kertovat, missä kohdassa botti ei enää pysty jatkamaan turvallisesti ja kenelle vastuu silloin siirtyy.

## Osaamistavoitteet

Oppija:

- rajaa käyttäjän ja käyttötilanteen
- kuvaa yhden konkreettisen tehtävän ja havaittavan onnistumisen
- jäsentää keskustelun 4–6 vaiheeksi
- erottaa asiallisen roolin viestinnällisestä persoonasta
- kirjoittaa käyttötapaukseen liittyvät rajat ja toiminnan rajan tullessa vastaan
- muokkaa määrittelyä saadun palautteen perusteella

## Ydinviesti

Hyvä botti ei ala alustasta tai järjestelmäpromptista. Se alkaa käyttäjän tehtävästä. Määrittely kertoo, mitä myöhemmän toteutuksen pitää tehdä ja millä näytöllä onnistuminen voidaan osoittaa.

Käytä yhtenä esimerkkinä kerhon uutta jäsentä, joka tarvitsee oikean harjoitusajan, varustetiedon ja seuraavan askeleen. Kun idea rajataan tähän tilanteeseen, myös tarpeettomat ominaisuudet tulevat näkyviksi. Botti ei tarvitse yleistä harrastusneuvontaa, vaan ajantasaiset lähteet ja turvallisen tavan ohjata käyttäjä ihmiselle, jos tieto puuttuu.

## Tyypilliset väärinkäsitykset

| Väärinkäsitys | Korjaava kysymys |
| --- | --- |
| ”Teen botin, joka auttaa kaikessa.” | Kuka käyttää bottia, missä tilanteessa ja mihin yhteen lopputulokseen? |
| ”Persoona on sama asia kuin rooli.” | Mitä botti tietää ja tekee — ja millä tavalla se viestii? |
| ”Rajat ovat vain kieltoja.” | Mitä botti tekee käyttäjän hyväksi silloin, kun raja tulee vastaan? |
| ”Kirjoitan ensin promptin ja päätän tarkoituksen myöhemmin.” | Miten arvioit promptia, jos onnistumista ei ole määritelty? |

Taulukon kysymyksiä ei käytetä tietovisailuna. Niillä avataan oppijan omaa määrittelyä. Kun vastaus jää yleiseksi, jatka kysymällä, mitä käyttäjä konkreettisesti tekee seuraavaksi ja mistä toinen ihminen voisi nähdä onnistumisen.

## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **rakennuspalikka 2: viimeistelty botin määrittelydokumentti ja yksi palautteen perusteella tehty muutos**.

Pidä koko tunnin ajan näkyvissä ero suunnitelman ja toteutuksen välillä. Jos oppija alkaa kirjoittaa järjestelmäpromptia, kysy ensin, mihin määrittelyn päätökseen kyseinen ohje perustuu. Jos vastausta ei löydy, ohje on ennenaikainen tai määrittelystä puuttuu olennainen päätös.

| Aika | Vaihe | Opettajan tehtävä |
| --- | --- | --- |
| 0–10 min | Rajaus | Näytä liian laaja botti-idea ja rajaa se yhdessä ryhmän kanssa käyttäjä–tehtävä–lopputulos-muotoon. |
| 10–25 min | Mallinnus | Erota käyttäjä, tehtävä, onnistuminen, eteneminen, rooli, sävy ja rajat yhdellä esimerkillä. |
| 25–60 min | Määrittely | Oppijat täyttävät oman määrittelydokumenttinsa. Ohjaa konkretisoivilla kysymyksillä. |
| 60–75 min | Haastaminen | Pari tai tekoäly esittää 2–3 kysymystä suunnitelman aukoista. Vastausta ei kirjoiteta oppijan puolesta. |
| 75–85 min | Korjaus | Oppija tekee vähintään yhden nimetyn muutoksen määrittelyyn. |
| 85–90 min | Tallennus | Tarkista tiedoston nimi, sijainti ja yhteys tuntien 15 ja 17 tuotoksiin. |

Aikataulun siirtymät ovat pedagogisesti tärkeitä. Mallinnuksen jälkeen oppija siirtyy omaan tapaukseensa, haastamisen jälkeen takaisin omaan päätösvaltaansa ja tunnin lopuksi kohti tietopohjaa. Tee nämä yhteydet ääneen, jotta määrittely ei jää erilliseksi harjoituslomakkeeksi.

## Arvioitava näyttö

Arvioi kokonaisuuden johdonmukaisuutta, älä yksittäisten kenttien pituutta. Lyhyt määrittely voi olla vahva, jos käyttäjä, tehtävä, eteneminen ja rajat tukevat toisiaan. Pitkä teksti voi puolestaan peittää sen, ettei onnistumista ole määritelty havaittavasti.

Hyväksyttävä tuotos:

- nimeää yhden käyttäjän tai käyttäjäryhmän
- kuvaa yhden tehtävän ja havaittavan onnistumisen
- sisältää loogisen keskustelun etenemisen
- erottaa roolin ja äänensävyn
- sisältää vähintään kolme käyttötapaukseen liittyvää rajaa
- kertoo, miten botti toimii rajan tullessa vastaan
- nimeää yhden palautteen perusteella tehdyn muutoksen

Hyvästä tuotoksesta voi seurata käyttäjän polkua alusta loppuun ja osoittaa kohdan, jossa botti pysähtyy tai vastuu siirtyy. Palautteen perusteella tehty muutos osoittaa, että oppija osasi arvioida määrittelyään eikä vain täyttää pohjaa.

## Eriyttäminen

**Tukireitti:** anna valmis käyttötapaus ja lauseenalut. Tuki vähentää valintoja, mutta säilyttää saman ydintuotoksen.

**Syventävä reitti:** oppija lisää kaksi keskenään ristiriitaista käyttäjätarvetta ja perustelee, kumpi asetetaan etusijalle. Syventävä työ ei kasvata pakollista ydintuotosta.

Tukireitillä valmis tapaus vapauttaa työmuistia päätösten yhteyksien hahmottamiseen. Syventävällä reitillä ristiriita pakottaa tekemään priorisoinnin näkyväksi. Kummassakin reitissä arvioidaan samaa ydintaitoa: osaako oppija perustella, mitä botti auttaa tekemään ja mitä se rajaa pois.

## Siirtymä seuraavaan tuntiin

Päätä tunti kysymykseen:

> Mitä tietoa bottisi tarvitsee voidakseen toteuttaa juuri tämän määrittelyn — ja miten myöhemmin testaat, ettei se arvaa puuttuvaa tietoa?

Kysymys toimii siltana tuntiin 15. Sen avulla oppija huomaa, että tietopohjaa ei kerätä aiheen ympäriltä yleisesti, vaan määrittelyssä luvattua käyttäjän tehtävää varten.
