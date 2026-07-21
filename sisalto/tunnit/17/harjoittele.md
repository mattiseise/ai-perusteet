# Harjoittele — Rakennuspalikoista arvioitavaksi botiksi

Tällä välilehdellä varmistat, että rakennuspalikat ja valitsemasi suorituspolku ovat kirkkaina mielessä. Tekninen toteutuspolku ja dokumentoitu suunnittelupolku ovat samanarvoisia, mutta niiden näyttö ei ole sama.

## Tehtävä 1/4 — rakennuspalat

```task
{"type":"match","title":"Rakennuspalat paikoilleen","intro":"Yhdistä kukin osa sen tehtävään ensimmäisessä versiossa.","pairs":[{"a":"Järjestelmäprompti","b":"Määrittää botin tehtävän, työnkulun ja rajat.","explain":"Se muuttaa suunnittelupäätökset botin pääohjeeksi."},{"a":"Promptikortti","b":"Tuo pääohjeeseen aiemmin testatun rakenteen.","explain":"Käytä ratkaisuja, joiden vaikutusta olet jo arvioinut."},{"a":"Botin määrittely","b":"Antaa käyttäjän, tehtävän, onnistumisen ja rajat.","explain":"Määrittely kertoo, mitä toteutuksen pitää saada aikaan."},{"a":"Tietopohja ja testit","b":"Antaa hyväksytyn aineiston ja ennen toteutusta päätetyt odotukset.","explain":"Testejä ei mukauteta ensimmäisen tuloksen mukaan."},{"a":"Valintakortti","b":"Perustelee toteutustavan, riskirajauksen ja käyttöönottokriteerin.","explain":"Se yhdistää tunnin 16 päätökset ensimmäiseen versioon."}],"summary":"Ensimmäinen versio kokoaa aiemmat päätökset arvioitavaksi kokonaisuudeksi."}
```

## Tehtävä 2/4 — valitse näyttö oikein

```task
{"type":"quiz","title":"Mitä polkusi voi osoittaa?","intro":"Valitse väite, joka vastaa annettua näyttöä.","items":[{"q":"Suunnittelupolun kaaviossa käyttöoikeus estää väärää käyttäjää hakemasta henkilöstöohjetta. Mitä voit päätellä?","options":[{"text":"Olen suunnitellut käyttöoikeusrajan, mutta en vielä osoittanut sen teknistä toimintaa.","correct":true,"explain":"Kaavio osoittaa suunnittelun, ei oikean järjestelmän pääsynvalvontaa."},{"text":"Käyttöoikeus toimii varmasti tuotannossa.","correct":false,"explain":"Tämä vaatisi teknisen toteutuksen ja testin."}]},{"q":"Tekninen botti löytää oikean lähteen kolmella testillä. Mitä voit päätellä?","options":[{"text":"Haku toimi näillä testeillä tässä toteutuksessa; muita tilanteita pitää arvioida erikseen.","correct":true,"explain":"Johtopäätös rajataan tehtyyn näyttöön."},{"text":"Tietopohja toimii virheettömästi kaikilla kysymyksillä.","correct":false,"explain":"Kolme testiä ei osoita yleistä virheettömyyttä."}]}],"summary":"Tekninen näyttö osoittaa toteutettua toimintaa; suunnittelunäyttö osoittaa rakenteen ja perustelut."}
```

## Tehtävä 3/4 — ensimmäinen testi

```task
{"type":"spot","title":"Testaa ensimmäinen versio","intro":"Kahvila-apurin pitää edetä vaiheittain, käyttää hyväksyttyä ohjetta eikä tehdä valintoja käyttäjän puolesta. Napauta repliikit, jotka rikkovat näitä ehtoja.","segments":[{"text":"Aloitetaan tavoitteesta: mitä toivot ensimmäiseltä vuoroltasi?","flag":false,"explain":"Botti aloittaa sovitusta vaiheesta."},{"text":"Ohitetaan loput kysymykset ja hypätään suoraan lopputulokseen.","flag":true,"explain":"Työnkulun vaiheita ei noudateta."},{"text":"Tein jo puolestasi valmiin valmistautumislistan.","flag":true,"explain":"Botti tekee valinnan käyttäjän puolesta vastoin rajausta."},{"text":"Kahvilan hyväksytyn ohjeen mukaan aamuvuoro alkaa kassan ja kahvinkeittimen valmistelulla.","flag":false,"explain":"Vastaus nojaa nimettyyn tietopohjan lähteeseen."},{"text":"Yleensä hyvä työntekijä vain tietää, mitä tehdä.","flag":true,"explain":"Yleinen väite ei nojaa hyväksyttyyn lähteeseen eikä auta käyttäjää etenemään."}],"summary":"Ensimmäinen testi tuottaa korjauslistan: työnkulku, lähteeseen pitäytyminen ja käyttäjän päätösvalta tarkistetaan erikseen."}
```

## Tehtävä 4/4 — polkujen näytöt

```task
{"type":"classify","title":"Tekninen näyttö vai suunnittelunäyttö?","intro":"Luokittele väitteet sen mukaan, millä polulla ne voidaan osoittaa.","categories":["Tekninen toteutuspolku","Dokumentoitu suunnittelupolku","Molemmat polut"],"items":[{"text":"Botti avautuu ja vastaa oikealla alustalla kolmella testisyötteellä.","answer":0,"explain":"Todellinen toiminta edellyttää rakennettua toteutusta."},{"text":"Arkkitehtuuri kuvaa käyttäjän, järjestelmäpromptin, tietopohjan haun ja vastauksen välisen kulun.","answer":1,"explain":"Suunnittelupolku voi osoittaa rakenteen ilman toimivaa integraatiota."},{"text":"Järjestelmäprompti sisältää tehtävän, työnkulun ja rajat.","answer":2,"explain":"Prompti voidaan arvioida kummallakin polulla."},{"text":"Todellinen käyttöoikeus estää väärää käyttäjää avaamasta rajattua lähdettä.","answer":0,"explain":"Simuloitu käyttöoikeus ei todista teknisen rajan toimivuutta."},{"text":"Testitapauksilla on ennen toteutusta kirjoitetut odotukset.","answer":2,"explain":"Testisuunnitelma kuuluu molempiin polkuihin."}],"summary":"Polut ovat samanarvoisia, mutta suunnittelupolku ei todista teknisiä integraatioita tai käyttöoikeuksia toimiviksi."}
```
