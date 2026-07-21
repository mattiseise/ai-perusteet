# Harjoittele — Työkalusta perustelluksi bottivalinnaksi

Kuva, ääni, video ja koodi ovat tällä tunnilla näkyviä, samanarvoisia reittejä. Kaikissa niissä tavoite, arviointi ja vastuu kuuluvat ihmiselle. Lopuksi ratkaiset, tarvitseeko oma apuri-bottisi valittua työkalua lainkaan.

## Tehtävä 1/5 — reittien erityispiirteet

```task
{"type":"match","title":"Mitä pitää määritellä?","intro":"Yhdistä tuotos sen suunnittelussa korostuvaan asiaan.","pairs":[{"a":"Kuva","b":"Kohde, sommittelu, visuaalinen ilme, kuvasuhde ja pois rajattavat asiat.","explain":"Kuvan arviointi kohdistuu näkyvään kokonaisuuteen ja käyttötarkoitukseen."},{"a":"Ääni tai musiikki","b":"Kesto, rakenne, tempo, tunnelma sekä puheen tai musiikin käyttötarkoitus.","explain":"Ääntä arvioidaan kuunneltavana ajallisena tuotoksena."},{"a":"Video","b":"Kohtaukset, jatkuvuus, liike, ääni ja saavutettavuus.","explain":"Video vaatii myös kohtausten välisen yhteyden tarkistamista."},{"a":"Koodi","b":"Syötteet, tulosteet, virhetilanteet, testit ja ymmärrettävyys.","explain":"Toimivuus osoitetaan ajamalla testit, ei silmäilemällä koodia."}],"summary":"Reitit eroavat tuotoksena, mutta jokainen vaatii ennalta päätetyt kriteerit."}
```

## Tehtävä 2/5 — yhteinen sykli

```task
{"type":"order","title":"Tuotoksesta näyttöön","intro":"Järjestä kaikille neljälle reitille yhteiset työvaiheet.","steps":["Rajaa käyttötarkoitus ja käyttäjä.","Päätä arviointikriteerit ennen ensimmäistä versiota.","Tuota versio 1 ja säilytä se.","Arvioi versio 1 kriteereillä ja nimeä yksi puute.","Muuta yhtä nimettyä asiaa ja tuota versio 2.","Vertaa versioita ja tee vastuullisuustarkistus."],"missHint":"Kriteerit päätetään ennen tuottamista, ja muutos nimetään ennen toista versiota.","summary":"Sama sykli tekee eri tuotostyyppien työstä perusteltavaa."}
```

## Tehtävä 3/5 — mikä on näyttöä?

```task
{"type":"classify","title":"Havainto vai vaikutelma?","intro":"Luokittele väitteet sen mukaan, perustuvatko ne havaittavaan kriteeriin.","categories":["Havaittava arvio","Pelkkä vaikutelma"],"items":[{"text":"Videon kaikissa kolmessa kohtauksessa sama esine säilyy samanvärisenä.","answer":0,"explain":"Väitteen voi tarkistaa kohtaus kohtaukselta."},{"text":"Kuva on hienompi.","answer":1,"explain":"Ilman kriteeriä ei tiedetä, mihin arvio perustuu."},{"text":"Koodi palauttaa odotetun tuloksen kolmella ennalta kirjoitetulla testisyötteellä.","answer":0,"explain":"Testitulokset ovat havaittavaa näyttöä."},{"text":"Äänite tuntuu ammattimaiselta.","answer":1,"explain":"Arvio pitää purkaa esimerkiksi puheen selkeydeksi, äänenvoimakkuudeksi ja kohinaksi."}],"summary":"Arviointi tarvitsee ominaisuuden, jonka toinenkin ihminen voi tarkistaa."}
```

## Tehtävä 4/5 — vastuullinen julkaisu

```task
{"type":"quiz","title":"Milloin tuotos on valmis?","intro":"Valitse perustelluin toimintatapa.","items":[{"q":"Toinen versio täyttää laatukriteerit. Mitä tarkistat vielä ennen käyttöä?","options":[{"text":"Käyttöoikeudet, mahdollisen harhaanjohtavuuden, yksityisyyden, saavutettavuuden ja sen, miten tekoälyn käyttö kerrotaan.","correct":true,"explain":"Tekninen tai esteettinen onnistuminen ei yksin ratkaise vastuullista käyttöä."},{"text":"En mitään, koska kriteerien täyttyminen tekee tuotoksesta automaattisesti turvallisen.","correct":false,"explain":"Laatu ja vastuullisuus ovat eri tarkistuksia."},{"text":"Vain sen, pitääkö itse tuotoksesta.","correct":false,"explain":"Henkilökohtainen mieltymys ei kata tuotoksen vaikutuksia ja käyttöehtoja."}]},{"q":"Koodireitin ohjelma toimii yhdellä esimerkillä. Mikä on oikea johtopäätös?","options":[{"text":"Se läpäisi yhden testin; tarvitaan myös tavallinen toinen syöte ja virhetilanne ennen laajempaa johtopäätöstä.","correct":true,"explain":"Yksi onnistunut ajo ei osoita toimintaa eri tilanteissa."},{"text":"Ohjelma on valmis kaikkeen käyttöön.","correct":false,"explain":"Väite ylittää testin näytön."},{"text":"Koodia ei tarvitse ymmärtää, jos tulos näyttää oikealta.","correct":false,"explain":"Käyttäjän pitää pystyä selittämään ja tarkistamaan käyttämänsä koodi."}]}],"summary":"Valmis tuotos täyttää nimetyt laatukriteerit ja läpäisee käyttötilanteen vastuullisuustarkistuksen."}
```

## Tehtävä 5/5 — tee bottiprojektin valinta

```task
{"type":"reflect","title":"Mitä bottisi oikeasti tarvitsee?","intro":"Hyvä toteutuspäätös voi tarkoittaa myös lisätyökalun rajaamista pois.","prompt":"Valitse omaan apuri-bottiisi toteutustapa. Kerro, tarvitsetko kuva-, ääni-, video- tai koodityökalua, mikä on tärkein riski ja millä ehdolla ratkaisu voidaan ottaa käyttöön. Jos valitset suunnittelupolun, nimeä myös se, mikä jää simuloiduksi.","placeholder":"Toteutustapa…\nErikoistyökalu tai perusteltu poisrajaus…\nTärkein riski…\nKäyttöönottoehto…\nSimuloiduksi jää…","tips":["Valitse yksinkertaisin riittävä ratkaisu.","Älä väitä simuloitua integraatiota toimivaksi.","Kytke päätös Oma botti II -tunnin testeihin."],"summary":"Toteutustapa, riskirajaus ja käyttöönottokriteeri valmistavat bottisi rakentamista."}
```
