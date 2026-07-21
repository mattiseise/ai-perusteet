# Harjoittele — Sääntö, malli vai yhdistelmä?

Näissä neljässä lyhyessä tehtävässä harjoittelet tunnin ydinasioita. Tehtävät tarkistuvat itsestään, ja saat jokaisesta valinnasta selityksen. Väärä vastaus ei haittaa — voit lukea palautteen ja kokeilla uudelleen.

## Tehtävä 1/4 — viisi peruskäsitettä

Yhdistä käsite sitä kuvaavaan selitykseen.

```task
{"type":"match","title":"Peruskäsitteet paikoilleen","intro":"Yhdistä käsite sitä kuvaavaan selitykseen.","pairs":[{"a":"Tekoäly","b":"Kattotermi menetelmille, joilla järjestelmä voi esimerkiksi tunnistaa, ennustaa, suositella tai tuottaa sisältöä.","explain":"Koneoppiminen on yksi tapa toteuttaa tekoälyä. Kaikki automaatio ei ole tekoälyä."},{"a":"Sääntöpohjainen järjestelmä","b":"Ohjelma, joka seuraa ennalta kirjoitettuja jos–niin-ehtoja.","explain":"Valmis sääntö sopii selkeään tilanteeseen, jossa toiminnan pitää olla ennustettavaa."},{"a":"Automaatio","b":"Tietokone hoitaa työvaiheen ilman, että ihminen tekee jokaista kohtaa käsin.","explain":"Automaatio voi käyttää sääntöä, mallia tai molempia. Automaattisuus ei yksin tarkoita tekoälyä."},{"a":"Data","b":"Tietoa, kuten kaupan aiempien päivien myyntimäärät, viikonpäivät ja sää.","explain":"Koneoppimismalli muodostetaan esimerkkidatan avulla."},{"a":"Koneoppimismalli","b":"Esimerkkidatan avulla muodostettu malli, joka antaa uudesta tapauksesta arvion.","explain":"Koulutettu malli voi arvioida uutta tapausta, mutta se ei automaattisesti opi jokaisesta käyttökerrasta."}],"summary":"Valmis sääntö kertoo toiminnan etukäteen. Koneoppimismalli muodostetaan esimerkeistä. Automaatio voi käyttää kumpaa tahansa tai niiden yhdistelmää."}
```

## Tehtävä 2/4 — läpinäkyvät tapaukset

Jokainen kuvaus kertoo suoraan, mihin toiminta perustuu. Luokittele tapaus valmiiksi kirjoitetuksi säännöksi, koulutetuksi malliksi tai niiden yhdistelmäksi.

```task
{"type":"classify","title":"Sääntö, koulutettu malli vai yhdistelmä?","intro":"Lue, miten järjestelmä on toteutettu. Valitse sen perusteella oikea ryhmä.","categories":["Valmis sääntö","Koulutettu malli","Yhdistelmä"],"items":[{"text":"Kaupan kassa antaa aina 10 prosentin alennuksen, jos asiakas näyttää voimassa olevan opiskelijakortin.","answer":0,"explain":"Toiminta perustuu ennalta kirjoitettuun jos–niin-sääntöön."},{"text":"Kaupan menekkimalli on koulutettu kolmen vuoden myyntipäivillä. Se arvioi niiden perusteella, kuinka paljon sämpylöitä huomenna tarvitaan.","answer":1,"explain":"Arvio syntyy aiemmista esimerkeistä muodostetulla mallilla."},{"text":"Menekkimalli ehdottaa tilausmäärän, mutta yli 200 sämpylän tilaus siirretään valmiin säännön perusteella ihmisen tarkistettavaksi.","answer":2,"explain":"Järjestelmä käyttää sekä koulutettua mallia että valmista tarkistussääntöä."},{"text":"Varaston valo syttyy joka päivä kello kuusi ja sammuu kello kahdeksan.","answer":0,"explain":"Kellonaikaan perustuva toiminta on valmis sääntö, vaikka se suoritetaan automaattisesti."},{"text":"Ruokala käyttää aiempien päivien kävijämääriä, säätä ja ruokalistaa arvioidakseen seuraavan päivän annosmäärän.","answer":1,"explain":"Uuden päivän arvio perustuu aiemmista esimerkeistä muodostettuun malliin."}],"summary":"Ratkaisevaa ei ole se, näyttääkö järjestelmä älykkäältä. Ratkaisevaa on, perustuuko toiminta valmiiseen sääntöön, esimerkeistä koulutettuun malliin vai molempiin."}
```

## Tehtävä 3/4 — valitse työkalu ja tarkistus

Auta pientä kauppaa valitsemaan kuhunkin tilanteeseen sopiva ratkaisu.

```task
{"type":"quiz","title":"Mikä ratkaisu sopii tehtävään?","intro":"Valitse jokaiseen tilanteeseen sopivin ratkaisu.","items":[{"q":"Varaston oven pitää aueta, jos työntekijän kulkukortti löytyy sallittujen korttien listalta. Mikä sopii tehtävään?","options":[{"text":"Valmis sääntö: jos kortti on listalla, ovi aukeaa.","correct":true,"explain":"Ehto on selkeä, ja toiminnan pitää olla ennustettavaa."},{"text":"Myyntidatasta koulutettu menekkimalli.","correct":false,"explain":"Menekkimalli ei ratkaise kulkulupaa. Selkeä kyllä–ei-ehto kannattaa toteuttaa valmiilla säännöllä."}]},{"q":"Kauppa haluaa arvioida huomisen sämpylätarpeen. Sillä on kolmen vuoden tiedot viikonpäivistä, säästä, tapahtumista ja myydyistä määristä. Mikä sopii tehtävään?","options":[{"text":"Esimerkkidatasta koulutettu menekkimalli.","correct":true,"explain":"Kun arvioon vaikuttaa monta asiaa ja aiempia esimerkkejä on paljon, koulutettu malli voi olla hyödyllinen."},{"text":"Yksi sääntö: tilaa joka päivälle aina sama määrä.","correct":false,"explain":"Yksi vakio ei huomioi viikonpäivää, säätä tai tapahtumia."}]},{"q":"Malli ehdottaa tavallista suurempaa tilausta. Jos arvio menee väärin, paljon ruokaa voi jäädä myymättä. Mitä teet?","options":[{"text":"Tarkistan suuren tilauksen ihmisen kanssa ennen lähettämistä.","correct":true,"explain":"Mallin arvio voi auttaa, mutta tavallista suureen ja vaikeasti peruttavaan tilaukseen kannattaa lisätä ihmisen tarkistus."},{"text":"Lähetän tilauksen aina suoraan, koska malli on koulutettu datalla.","correct":false,"explain":"Koulutusdata ei tee arviosta varmaa. Kun virheellä on selvä seuraus, tarkistus auttaa hallitsemaan riskiä."}]}],"summary":"Työkalu valitaan tehtävän mukaan. Malli ei ole aina sääntöä parempi, ja arvio voi tarvita ihmisen tarkistuksen."}
```

## Tehtävä 4/4 — selitä omin sanoin

Kirjoita lyhyt selitys niin kuin kertoisit asian tutulle, joka ei tunne tekoälyä.

```task
{"type":"reflect","title":"Selitä tutulle omin sanoin","intro":"Käytä tavallista kieltä. Voit käyttää esimerkkinä kaupan sämpylätilausta, kulkukorttiovea tai jotakin omaa arjen tilannetta.","prompt":"Selitä, mitä eroa on valmiilla säännöllä ja esimerkeistä koulutetulla koneoppimismallilla. Kerro myös, miksi automaattinen toiminta ei yksin tarkoita tekoälyä ja miten oikea järjestelmä voi käyttää sekä sääntöä että mallia.","min_chars":80,"expert":"Valmis sääntö kertoo etukäteen, mitä tietyssä tilanteessa tehdään. Koneoppimismalli muodostetaan aiemmista esimerkeistä, ja se antaa uudesta tapauksesta arvion. Molemmat voidaan suorittaa automaattisesti, joten automaattisuus ei yksin kerro, että kyse on tekoälystä. Kaupan järjestelmä voi esimerkiksi käyttää koulutettua mallia menekin arviointiin ja valmista sääntöä suuren tilauksen siirtämiseen ihmisen tarkistettavaksi.","checklist":["Kerroin, että valmis sääntö kirjoitetaan etukäteen.","Kerroin, että koneoppimismalli muodostetaan aiemmista esimerkeistä.","Muistin, ettei automaattisuus yksin tarkoita tekoälyä.","Käytin esimerkkiä, jossa sääntö ja malli toimivat yhdessä."]}
```
