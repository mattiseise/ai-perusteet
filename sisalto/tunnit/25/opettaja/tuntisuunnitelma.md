# Opettajan materiaalit — oppitunti 25: ihminen portinvartijana

## Oppitunnin tarkoitus

Oppija suunnittelee, missä kohdissa agentti saa toimia itse ja missä ihmisen pitää hyväksyä, muokata tai hylätä ehdotus. Samalla erotetaan palautedatan tallentaminen mallin oppimisesta.

Opetuksen punaisena lankana toimii päätöksen riski. Kun oppija tarkastelee virheen vaikutusta, peruttavuutta ja vastuunkantajaa, hyväksyntäportin paikka ei jää mielipiteeksi. Sama tarkastelu auttaa myös poistamaan turhia portteja: vähäriskinen ja helposti peruttava rutiini voidaan usein automatisoida ilman ihmisen hyväksyntää.

## Osaamistavoitteet

Oppija:

- tunnistaa päätökset, joihin liittyy raha, sitoumus, puuttuva tieto, työkalun virhe tai merkittävä vaikutus
- suunnittelee hyväksyntäportin, joka näyttää päätöksen kannalta tarpeellisen tiedon
- määrittää aikarajan, eskaloinnin ja turvallisen oletustoiminnon
- välttää hyväksyntäväsymystä rajaamalla portit riskikohtiin
- kuvaa, miten palaute tallennetaan ja miten siitä tehdään hallittu järjestelmämuutos

## Ydinviesti

Ihminen ei kuulu jokaiseen vaiheeseen varmuuden vuoksi. Hän kuuluu kohtaan, jossa päätös tarvitsee vastuuta tai harkintaa. Hyväksyntä tai hylkäys voi tuottaa kehitysaineistoa, mutta kielimalli ei opi siitä automaattisesti.

Tee ero näkyväksi yhdellä esimerkillä. Asiakkaalle lähetettävä vastaanottokuittaus voi olla automaattinen, mutta hinnanalennus muuttaa taloudellista sitoumusta ja tarvitsee nimetyn päätöksentekijän. Jos päätöksentekijä hylkää ehdotuksen, tieto tallennetaan lokiin. Järjestelmän sääntö muuttuu vasta, kun ihminen on arvioinut havaintoa ja hyväksynyt testatun muutoksen.

## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **Agentti: Ihminen -pohjapiirros**.

| Aika | Vaihe | Opettajan tehtävä |
| --- | --- | --- |
| 0–15 min | Riskikohta | Vertaa rutiinitoimintoa ja rahaa tai oikeuksia koskevaa päätöstä. |
| 15–30 min | Hyvä portti | Mallinna päätös, perustelu, näyttö, vaihtoehdot ja seuraukset. |
| 30–55 min | Oma pohjapiirros | Oppija sijoittaa hyväksyntäportit omaan agenttiinsa. |
| 55–68 min | Hiljaisuus | Oppija määrittää aikarajan, eskaloinnin ja oletustoiminnon. |
| 68–80 min | Palautedata | Oppija kuvaa lokin, arvioijan, muutoksen ja uudelleentestauksen. |
| 80–90 min | Haastaminen | Pari etsii yhden turhan portin ja yhden puuttuvan riskikohdan. |

Oman pohjapiirroksen aikana pyydä oppijaa kuvaamaan yhden portin koko elinkaari. Pelkkä sijainti prosessissa ei riitä: näkyviin tarvitaan päätösaineisto, päätöksentekijä, vastausaika ja toiminta hiljaisuudessa. Parityöskentelyn tehtävä ei ole lisätä portteja vaan löytää tasapaino sujuvuuden ja vastuun välille.

## Tyypilliset väärinkäsitykset

- Jokaisen toiminnon hyväksyttäminen voi tehdä järjestelmästä hitaamman ilman olennaista lisäturvaa.
- Pelkkä hyväksy/hylkää-painike ei anna ihmiselle päätöksen taustaa.
- Vastaamattomuus ei saa tarkoittaa kriittisen päätöksen automaattista hyväksyntää.
- Yksi poikkeuspäätös ei ole uusi organisaation sääntö.
- Lokimerkintä ei muuta mallia; muutos vaatii arvioinnin, toteutuksen ja testauksen.

Kun väärinkäsitys tulee esiin, palaa seuraukseen. Kysy esimerkiksi, mitä tapahtuu, jos hyväksyjä ei vastaa ennen määräaikaa tai jos kiireessä tehty poikkeuspäätös muuttuu vahingossa kaikkia tapauksia koskevaksi säännöksi. Tällainen tapaus tekee abstraktista varoituksesta konkreettisen suunnittelupäätöksen.

## Arvioitava näyttö

Hyväksyttävä pohjapiirros kertoo, missä portti on, mitä se näyttää, kuka päättää, kuinka kauan odotetaan, mitä tapahtuu hiljaisuudessa ja miten päätös tallennetaan kehitystä varten.
