# Harjoittele — Rakenna uudelleen käytettävä promptikortti

Tavoitteena on yksi perusteltu kortti, ei suuri määrä kokeilemattomia prompteja.

## Tehtävä 1/5 — promptikortin osat

```task
{"type":"match","title":"Mitä korttiin kuuluu?","intro":"Yhdistä promptikortin osa sen tehtävään.","pairs":[{"a":"Käyttötilanne","b":"Kertoo, mihin toistuvaan tehtävään prompti on tarkoitettu.","explain":"Sama prompti ei sovi automaattisesti kaikkiin tehtäviin."},{"a":"Syötteen paikka","b":"Näyttää, mihin vaihtuva aineisto lisätään.","explain":"Pysyvä ohje ja vaihtuva sisältö erotetaan toisistaan."},{"a":"Laatukriteerit","b":"Kertovat, millä havainnoilla vastausta arvioidaan.","explain":"Kriteerit päätetään ennen vertailua."},{"a":"Tunnettu raja","b":"Kuvaa tilanteen, jossa kortti voi toimia huonosti tai vaatii tarkistusta.","explain":"Kortti ei lupaa enempää kuin siitä on testattu."},{"a":"Versiohistoria","b":"Kirjaa nimetyn muutoksen ja sen havaitun vaikutuksen.","explain":"Näin myöhemmin tiedetään, miksi prompti on nykyisessä muodossaan."}],"summary":"Promptikortti yhdistää ohjeen, käyttötilanteen, arvioinnin ja tunnetut rajat."}
```

## Tehtävä 2/5 — hallittu muutos

```task
{"type":"quiz","title":"Miten osoitat muutoksen vaikutuksen?","intro":"Valitse paras tapa testata promptin uusi versio.","items":[{"q":"Haluat selvittää, parantaako lähteeseen pitäytymistä koskeva ohje vastausta. Miten vertaat?","options":[{"text":"Pidän syötteen ja muun promptin samoina, lisään yhden ohjeen ja arvioin molemmat vastaukset samoilla kriteereillä.","correct":true,"explain":"Kun vain yksi olennainen asia muuttuu, vaikutusta voi arvioida uskottavasti."},{"text":"Vaihdaan samalla syötteen, mallin ja vastausmuodon.","correct":false,"explain":"Usea samanaikainen muutos peittää vaikutuksen syyn."},{"text":"Arvioin vain uutta vastausta sen perusteella, kuulostaako se paremmalta.","correct":false,"explain":"Ilman vertailua ja havaintokriteereitä vaikutus jää mielikuvaksi."}]},{"q":"Ensimmäinen testi onnistuu. Mitä voit päätellä?","options":[{"text":"Kortti toimi tällä syötteellä; käyttökelpoisuus kannattaa vielä koetella erilaisella syötteellä.","correct":true,"explain":"Yksi onnistuminen ei osoita yleistä toimivuutta."},{"text":"Prompti toimii varmasti kaikissa saman aiheen tehtävissä.","correct":false,"explain":"Johtopäätös ylittää tehdyn kokeen näytön."},{"text":"Laatukriteereitä ei enää tarvita.","correct":false,"explain":"Kriteerit tekevät myöhemmästä testistä vertailukelpoisen."}]}],"summary":"Muuta yksi asia kerrallaan ja rajaa johtopäätös tehtyyn kokeeseen."}
```

## Tehtävä 3/5 — työjärjestys

```task
{"type":"order","title":"Promptikortin rakentaminen","intro":"Järjestä työvaiheet niin, että muutos voidaan perustella.","steps":["Rajaa toistuva tehtävä ja käyttäjä.","Päätä laatukriteerit ennen ajoa.","Aja versio 1 turvallisella syötteellä.","Nimeä yksi puute ja tee yksi promptimuutos.","Aja versio 2 samalla syötteellä uudessa keskustelussa.","Vertaa havaintoja ja kirjaa kortin tunnettu raja."],"missHint":"Kriteerit päätetään ennen ajoa, ja toinen versio testataan samalla syötteellä.","summary":"Kortin arvo syntyy dokumentoidusta kokeesta."}
```

## Tehtävä 4/5 — oma rajaus

```task
{"type":"reflect","title":"Missä korttisi raja kulkee?","intro":"Ajattele yhtä promptia, jota käytät tai voisit käyttää toistuvasti.","prompt":"Kirjoita käyttötarkoitus, kaksi laatukriteeriä ja yksi tilanne, jossa et käyttäisi samaa promptikorttia sellaisenaan.","placeholder":"Käyttötarkoitus…\nLaatukriteerit…\nTunnettu raja…","tips":["Rajaa tehtävä konkreettisesti.","Kirjoita kriteeri havaittavana ominaisuutena.","Älä lupaa toimivuutta tilanteessa, jota et ole testannut."],"summary":"Hyvä promptikortti kertoo myös, missä sen käyttökelpoisuus päättyy."}
```

## Tehtävä 5/5 — seuraava testi

```task
{"type":"reflect","title":"Koettele korttia uudella syötteellä","intro":"Yksi onnistunut syöte ei vielä osoita yleistä toimivuutta.","prompt":"Kuvaa syöte, joka eroaa ensimmäisestä testistä olennaisella tavalla. Kerro, mitä ominaisuutta tällä testillä koettelisit ja mikä olisi hyväksyttävä tulos.","placeholder":"Uusi syöte…\nKoeteltava ominaisuus…\nHyväksyttävä tulos…","tips":["Muuta syötettä, älä kortin tavoitetta.","Valitse havaittava ominaisuus.","Kirjaa odotus ennen ajoa."],"summary":"Toinen syöte paljastaa, kestääkö promptikortin rakenne vaihtelua."}
```
