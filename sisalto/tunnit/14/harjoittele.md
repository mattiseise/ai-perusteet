# Harjoittele — Määrittele botti ennen rakentamista

Harjoittelet tarvetta, käyttäjää, tehtävää ja rajoja. Et vielä kirjoita valmista järjestelmäpromptia tai testaa toteutusta.

## Tehtävä 1/5 — määrittelyn osat

```task
{"type":"match","title":"Mitä ollaan päättämässä?","intro":"Yhdistä määrittelyn osa sitä kuvaavaan kysymykseen.","pairs":[{"a":"Käyttäjä","b":"Kuka tarvitsee apua ja mikä on hänen lähtötilanteensa?","explain":"Kohderyhmä rajataan todelliseen käyttäjään, ei kaikkiin ihmisiin."},{"a":"Tehtävä","b":"Mitä käyttäjä yrittää saada aikaan?","explain":"Botti rakennetaan auttamaan yhdessä tunnistettavassa tehtävässä."},{"a":"Onnistuminen","b":"Mistä voidaan havaita, että käyttäjä pääsi hyödylliseen lopputulokseen?","explain":"Onnistuminen kuvataan näkyvänä tuloksena, ei vain hyvänä tunteena."},{"a":"Työnkulku","b":"Missä järjestyksessä käyttäjää ohjataan alusta lopputulokseen?","explain":"Vaiheet tekevät toiminnasta ennakoitavaa."},{"a":"Raja","b":"Milloin botin pitää pysähtyä, kieltäytyä tai ohjata ihminen muualle?","explain":"Raja kertoo myös, kuka kantaa vastuun poikkeustilanteessa."}],"summary":"Määrittely kuvaa käyttäjän tarpeen ja tulevan toteutuksen vaatimukset."}
```

## Tehtävä 2/5 — rajaa tehtävä

```task
{"type":"quiz","title":"Mikä on riittävän tarkka määrittely?","intro":"Valitse määrittely, jonka perusteella toteutusta voisi myöhemmin arvioida.","items":[{"q":"Mikä tarkoitus on parhaiten rajattu?","options":[{"text":"Botti auttaa kerhon uutta jäsentä löytämään hyväksytyistä ohjeista harjoitusajan ja liittymisen seuraavan vaiheen.","correct":true,"explain":"Käyttäjä, aineisto, tehtävä ja hyödyllinen lopputulos ovat havaittavissa."},{"text":"Botti auttaa kaikessa harrastukseen liittyvässä.","correct":false,"explain":"Tehtävä ja onnistuminen jäävät liian avoimiksi."},{"text":"Botti on ystävällinen ja moderni.","correct":false,"explain":"Sävy ei vielä kerro, mitä käyttäjä saa aikaan."}]},{"q":"Mikä raja on käyttökelpoisin?","options":[{"text":"Jos vastausta ei löydy hyväksytystä aineistosta, botti kertoo puutteen eikä arvaa sekä ohjaa nimetylle yhteyshenkilölle.","correct":true,"explain":"Raja kertoo ehdon, toiminnan ja vastuun siirtymisen."},{"text":"Botti ei koskaan tee virheitä.","correct":false,"explain":"Tämä ei ole toteutettava toimintasääntö."},{"text":"Botti toimii vastuullisesti.","correct":false,"explain":"Yleinen arvo pitää muuttaa havaittavaksi toiminnaksi."}]}],"summary":"Hyvä määrittely tekee myöhemmästä toteutuksesta ja arvioinnista mahdollisen."}
```

## Tehtävä 3/5 — suunnittelun järjestys

```task
{"type":"order","title":"Tarpeesta määrittelyksi","intro":"Järjestä suunnittelun vaiheet ennen toteutusta.","steps":["Nimeä käyttäjä ja hänen todellinen tilanteensa.","Rajaa yksi tehtävä, jossa apua tarvitaan.","Kuvaa havaittava onnistuminen.","Kirjoita käyttäjän eteneminen vaiheiksi.","Määritä rajat ja vastuun siirtyminen.","Tarkista, että määrittelyn perusteella toinen ihminen ymmärtäisi rakennettavan botin."],"missHint":"Aloita käyttäjän tarpeesta. Toteutuksen ohjeet kirjoitetaan vasta määrittelyn jälkeen.","summary":"Suunnittelu etenee tarpeesta arvioitavaan määrittelyyn."}
```

## Tehtävä 4/5 — määrittelyn ydin

```task
{"type":"reflect","title":"Mitä olet rakentamassa?","intro":"Muotoile yhden botin perustelu ennen toteutusta.","prompt":"Kirjoita neljä virkettä: kenelle botti on, missä tehtävässä se auttaa, mistä onnistuminen näkyy ja missä tilanteessa sen pitää pysähtyä.","placeholder":"Botti on tarkoitettu…","tips":["Nimeä todellinen käyttäjä.","Valitse yksi tehtävä.","Kuvaa raja toimintana, ei iskulauseena."],"summary":"Kun tarve ja rajat ovat selvät, järjestelmäpromptin kirjoittaminen on myöhemmin määrittelyn toteuttamista."}
```

## Tehtävä 5/5 — tunnista vielä avoin päätös

```task
{"type":"reflect","title":"Mitä et vielä tiedä?","intro":"Hyvä määrittely näyttää myös ratkaisemattoman kohdan.","prompt":"Nimeä yksi botin toteutukseen vaikuttava asia, jota et vielä tiedä. Kerro, miten selvität sen ennen rakentamista ja mitä päätös voi muuttaa.","placeholder":"Avoin kysymys…\nSelvitän sen…\nPäätös vaikuttaa…","tips":["Älä peitä epävarmuutta yleisellä lauseella.","Nimeä tiedon lähde.","Kerro, mihin määrittelyn kohtaan vastaus vaikuttaa."],"summary":"Avoin päätös on hallittavissa, kun se nimetään ja sille sovitaan selvitystapa."}
```
