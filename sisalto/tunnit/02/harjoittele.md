# Harjoittele — Roskapostimallin matka ja rajat

Tällä välilehdellä harjoittelet tunnin kolmea kysymystä: miten malli oppii ja tarkistetaan, miksi sitä seurataan käytössä ja miksi nykyinen suoritus ei osoita AGI:a tai ASI:a. Tehtävät tarkistuvat heti, eikä kukaan muu näe vastauksiasi.

## Tehtävä 1/5 — aineistot oikeaan järjestykseen

```task
{"type":"order","title":"Roskapostimallin matka käyttöön","intro":"Järjestä vaiheet niin, että viimeinen testi pysyy erillään harjoittelusta.","steps":["Jaa merkityt viestit koulutus-, validointi- ja testiaineistoon.","Kouluta malli koulutusaineistolla.","Vertaa malliversioita validointiaineiston avulla.","Arvioi valittu malli erillisellä testiaineistolla.","Ota malli käyttöön ja seuraa sen tekemiä virheitä."],"missHint":"Koulutus tulee ensin. Testi tehdään vasta sen jälkeen, kun malliversio on valittu.","summary":"Koulutus, validointi ja testi palvelevat eri tarkoituksia. Käytössä mallia seurataan edelleen."}
```

## Tehtävä 2/5 — mitä käsitteet tarkoittavat?

```task
{"type":"match","title":"Oppimisen ja tarkistamisen käsitteet","intro":"Yhdistä käsite sitä parhaiten kuvaavaan selitykseen.","pairs":[{"a":"Koulutusaineisto","b":"Esimerkit, joiden avulla malli oppii."},{"a":"Validointiaineisto","b":"Erilliset esimerkit, joiden avulla malliversioita verrataan."},{"a":"Testiaineisto","b":"Sivussa pidetyt esimerkit valitun mallin viimeistä arviota varten."},{"a":"Yleistyminen","b":"Malli toimii myös uusissa samankaltaisissa tapauksissa."},{"a":"Ylioppiminen","b":"Malli muistaa harjoitusten yksityiskohtia eikä toimi hyvin uusissa tapauksissa."}],"summary":"Hyvä malli ei vain muista koulutusesimerkkejä. Se osoittaa osaamisensa erillisissä, uusissa tapauksissa."}
```

## Tehtävä 3/5 — nykyinen järjestelmä vai tulevaisuusväite?

Tässä tehtävässä kapea ja generatiivinen tekoäly kuuluvat samaan nykyisten järjestelmien ryhmään. Sama järjestelmä voi olla molempia.

```task
{"type":"classify","title":"Missä nykyisyyden raja kulkee?","intro":"Luokittele kuvaus sen perusteella, mitä järjestelmä tekee tai mitä siitä väitetään.","categories":["Nykyinen järjestelmä tai toiminto","AGI-väite","ASI-väite"],"items":[{"text":"Roskapostimalli arvioi, kuuluuko uusi viesti roskapostiin.","answer":0,"explain":"Tämä on nykyinen rajattu tunnistustehtävä eli esimerkki kapeasta tekoälystä."},{"text":"Tekstitekoäly luonnostelee käyttäjälle vastauksen sähköpostiin.","answer":0,"explain":"Tekstin tuottaminen on generatiivista tekoälyä. Tehtävä voi samalla olla rajattu."},{"text":"Järjestelmän väitetään oppivan joustavasti minkä tahansa uuden ammatin ihmisen tavoin.","answer":1,"explain":"Väite kuvaa AGI:hin liitettyä laaja-alaista oppimista. Yleisesti hyväksyttyä nykyistä AGI-esimerkkiä ei ole."},{"text":"Tulevaisuuden järjestelmän ennustetaan ylittävän ihmisen kyvyt kaikilla tieteenaloilla.","answer":2,"explain":"Ihmisen kykyjen laaja ylittäminen kuvaa ASI:a. Kyse on spekulatiivisesta tulevaisuusväitteestä."}],"summary":"Kapea ja generatiivinen tekoäly ovat käytössä nyt. AGI ja ASI ovat tulevaisuutta koskevia käsitteitä, eivät nykyisten tuotteiden tavallisia ominaisuuksia."}
```

## Tehtävä 4/5 — tarkista tärkeät rajat

```task
{"type":"quiz","title":"Mikä päätelmä kestää tarkastelun?","intro":"Valitse täsmällisin vaihtoehto.","items":[{"q":"Roskapostimalli toimi hyvin viime vuoden testissä. Miksi sitä pitää silti seurata?","options":[{"text":"Uudet viestit ja huijausten keinot voivat muuttua, joten vanha tulos ei takaa nykyistä toimivuutta.","correct":true,"explain":"Seuranta näyttää, toimiiko malli edelleen todellisissa käyttötilanteissa."},{"text":"Koska malli unohtaa testituloksen joka yö.","correct":false,"explain":"Seurannan tarve ei johdu tällaisesta unohtamisesta vaan käyttötilanteiden ja aineiston muuttumisesta."},{"text":"Koska testiä pitää käyttää mallin jatkuvaan harjoittamiseen.","correct":false,"explain":"Testiaineisto pidetään erillään rakentamisen valinnoista."}]},{"q":"Miten kapea ja generatiivinen tekoäly liittyvät toisiinsa?","options":[{"text":"Sama järjestelmä voi tuottaa sisältöä ja silti toimia rajatussa tehtävässä.","correct":true,"explain":"Generatiivisuus kertoo sisällön tuottamisesta, kapeus kykyjen rajauksesta."},{"text":"Generatiivinen tekoäly on aina AGI.","correct":false,"explain":"Sisällön tuottaminen ei yksin osoita yleistä ja joustavaa oppimiskykyä."},{"text":"Kapea ja generatiivinen tarkoittavat samaa asiaa.","correct":false,"explain":"Ne kuvaavat eri ominaisuuksia, vaikka voivat toteutua samassa järjestelmässä."}]},{"q":"Tekstitekoäly kirjoittaa hyvän sähköpostin. Mitä tästä voidaan päätellä?","options":[{"text":"Se osoitti tekstin tuottamisen kykyä tässä tehtävässä, mutta tulos ei yksin osoita AGI:a.","correct":true,"explain":"Johtopäätös rajataan siihen, mitä järjestelmä todella teki."},{"text":"Se osaa nyt minkä tahansa työn.","correct":false,"explain":"Yksi onnistunut tehtävä ei ole näyttö kaikista muista tehtävistä."},{"text":"Se on ASI, koska teksti oli hyvä.","correct":false,"explain":"ASI tarkoittaisi ihmisen kykyjen laajaa ylittämistä, ei onnistumista yhdessä tekstitehtävässä."}]}],"summary":"Arvioi ensin näkyvä suoritus ja sen rajat. Älä tee yhdestä onnistumisesta AGI- tai ASI-päätelmää."}
```

## Tehtävä 5/5 — selitä omin sanoin

```task
{"type":"reflect","title":"Kolme kysymystä yhdellä esimerkillä","intro":"Kirjoita lyhyt selitys ihmiselle, joka ei tunne tekoälyn käsitteitä.","prompt":"Selitä roskapostimallin avulla, miten malli oppii ja tarkistetaan, miksi sitä seurataan käytössä ja miksi hyvä roskapostin tunnistus ei vielä osoita AGI:a tai ASI:a.","min_chars":120,"expert":"Roskapostimalli koulutetaan merkityillä viesteillä, malliversioita verrataan validointiaineistolla ja valittu malli tarkistetaan erillisellä testiaineistolla. Käytössä mallia seurataan, koska viestit ja huijausten keinot muuttuvat. Hyvä roskapostin tunnistus osoittaa rajattua osaamista, ei kykyä oppia mitä tahansa tehtävää tai ylittää ihmisen kykyjä laajasti.","checklist":["Mainitsin koulutuksen ja erillisen tarkistamisen.","Kerroin, miksi seurantaa tarvitaan.","Rajasin johtopäätöksen roskapostin tunnistamiseen.","Erotin nykyisen suorituksen AGI:sta ja ASI:sta."]}
```
