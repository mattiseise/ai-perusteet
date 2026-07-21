# Opettajan materiaalit — oppitunti 17: ensimmäinen versio ja ensitestit

## Tunnin tarkoitus

Oppija kokoaa aiempien tuntien kolme rakennuspalikkaa ensimmäiseksi arvioitavaksi versioksi. Rakennuspalikat ovat **Promptikortti**, **botin määrittely** sekä **tietopohja ja testisuunnitelma**. Järjestelmäprompti ei ole neljäs rakennuspalikka, vaan näistä päätöksistä koottu toteutusohje botille.

Teknisellä toteutuspolulla oppija rakentaa botin saatavilla olevalle alustalle. Dokumentoidulla suunnittelupolulla hän laatii arkkitehtuurin ja simuloidut suoritusjäljet. Polut ovat samanarvoisia, mutta simulaatio ei todista integraation, käyttöoikeuksien, tilan säilymisen tai lokituksen toimivan teknisessä järjestelmässä.

## Osaamistavoitteet

Tunnin jälkeen oppija:

- kokoaa kolme rakennuspalikkaa johdonmukaiseksi järjestelmäpromptiksi ja toteutukseksi
- tuottaa teknisen minimiversion tai tarkistettavan suunnittelupaketin
- ajaa tai simuloi ensimmäisen kerran kaikki kolme ennalta kirjoitettua testiä: normaalin tapauksen, kielteisen testin ja reunatapauksen
- vertaa jokaista tulosta etukäteen kirjoitettuun odotukseen
- laatii havaintojen perusteella korjauslistan tunnille 18 muuttamatta testien odotuksia jälkikäteen.

## 90 minuutin toteutus ja eriyttäminen

| Aika | Vaihe | Oppijan työ | Opettajan tehtävä |
| --- | --- | --- | --- |
| 0–10 min | Lähtöaineisto | Avaa kolme rakennuspalikkaa ja tunnin 16 valintakortin. | Varmista, että rakennuspalikkojen nimet ja tehtävät ovat selvät. |
| 10–25 min | Järjestelmäprompti | Muuttaa määrittelyn, promptikortin ratkaisut sekä tietopohjan käyttöohjeet yhdeksi pääohjeeksi. | Rajaa pääohje rooliin, työnkulkuun, aineiston käyttöön ja rajoihin. |
| 25–55 min | Ensimmäinen versio | Rakentaa teknisen minimiversion tai dokumentoi arkkitehtuurin ja suoritusjäljen rungon. | Auta vain ydintoiminnon saamisessa testattavaan muotoon. |
| 55–78 min | Kolme ensitestiä | Ajaa tai simuloi normaalin, kielteisen ja reunatapauksen. Tallentaa syötteen, odotuksen, tuloksen ja johtopäätöksen. | Kysy, onko näyttö teknistä vai simuloitua ja pysyikö odotus muuttumattomana. |
| 78–87 min | Korjauslista | Nimeää havainnot ja valitsee ehdokkaan tunnin 18 korjaukseksi. | Estä arvioitavan korjausketjun kiirehtiminen tämän tunnin loppuun. |
| 87–90 min | Tallennus | Tallentaa version, kolme testitulosta ja korjauslistan. | Tarkista, että työ on löydettävissä seuraavalla tunnilla. |

## Arvioitava näyttö

Tunnin 17 hyväksyttävä tuotos sisältää järjestelmäpromptin ensimmäisen version, polkukohtaisen ydintuotoksen, kaikki kolme ensimmäistä testitulosta ja korjauslistan. Testissä löytynyt puute on käyttökelpoinen havainto, ei epäonnistuminen.

Teknisen polun näyttö voi osoittaa alustan todellisen vastauksen, tietopohjan kytkennän ja toteutukseen kuuluvat pääsyasetukset. Suunnittelupolun näyttö voi osoittaa arkkitehtuurin, simuloidun haun ja vastauksen sekä tunnistetut rajat. Älä hyväksy simuloitua jälkeä todisteeksi teknisen yhteyden toiminnasta.

## Tuen järjestäminen

Anna tarvittaessa valmis järjestelmäpromptin otsikkorunko ja testimatriisi. Oppija tekee silti itse botin tehtävää, rajoja ja tuloksia koskevat päätelmät. Jos tekninen alusta ei ole käytettävissä, oppija voi siirtyä dokumentoituun suunnittelupolkuun tasavertaisena vaihtoehtona ilman teknisen toteutuksen väitettä.

Nopeasti etenevä oppija voi pyytää toista käyttäjää ajamaan yhden samoista testeistä. Tämä ei lisää pakollisten testien määrää eikä siirrä tunnin 18 korjausta tunnille 17.

## Siirtymä tunnille 18

Tunnin lopussa sano:

> Tänään sait ensimmäisen version ja kolme ensitulosta näkyviin. Ensi tunnilla valitset korjauslistalta yhden puutteen, teet siihen nimetyn korjauksen ja toistat juuri sitä koskevan testin. Vertailu antaa näyttöä korjauksen vaikutuksesta tässä testissä.
