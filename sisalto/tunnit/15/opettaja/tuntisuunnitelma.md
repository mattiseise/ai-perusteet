# Opettajan materiaalit — oppitunti 15: tietopohja ja testisuunnitelma

## Oppitunnin tarkoitus

Oppija kuratoi oman bottinsa tietopohjan ja kirjoittaa testit ennen botin rakentamista. Tunnilla ei vielä testata omaa toteutusta. Testit ajetaan ensimmäisen kerran tunnilla 17 ja dokumentoidaan sekä uusitaan tunnilla 18.

## Osaamistavoitteet

Oppija:

- johtaa botin määrittelystä 5–8 tietotarvetta
- valitsee 3–5 lähdettä tehtävän, ei määrän, perusteella
- arvioi lähteiden luotettavuutta, ajantasaisuutta, kattavuutta ja käyttöoikeutta
- kirjaa tietopohjan aukot ja toiminnan puuttuvan tiedon tilanteessa
- kirjoittaa positiivisen, negatiivisen ja reunatapaustestin
- määrittää jokaiselle testille odotetun toiminnan ja läpäisyehdon

## Ydinviesti

Tietopohja ei tee botista automaattisesti luotettavaa. Luotettavuus syntyy siitä, että tiedät, mitä aineisto kattaa, mitä se ei kata ja millä testillä ero voidaan myöhemmin osoittaa.

## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **rakennuspalikka 3: kuratoitu tietopohjataulukko, kattavuusarvio ja kolmen testin suunnitelma**.

| Aika | Vaihe | Opettajan tehtävä |
| --- | --- | --- |
| 0–10 min | Silta määrittelyyn | Näytä, miten yksi käyttötapaus muuttuu tietotarpeiksi. |
| 10–25 min | Lähteiden arviointi | Mallinna hyvä, puutteellinen ja tehtävään tarpeeton lähde. |
| 25–55 min | Kuratointi | Oppijat valitsevat 3–5 lähdettä ja täyttävät perustelutaulukon. |
| 55–70 min | Aukot | Oppijat kirjoittavat, mitä tietopohja kattaa, mitä ei ja miten botin pitää toimia tiedon puuttuessa. |
| 70–85 min | Testisuunnitelma | Kirjoita yksi positiivinen, yksi negatiivinen ja yksi reunatapaus odotuksineen. |
| 85–90 min | Tallennus | Varmista aineiston sallittu käyttö ja yhteys tunnin 17 rakentamiseen. |

## Tyypilliset väärinkäsitykset

| Väärinkäsitys | Korjaava näkökulma |
| --- | --- |
| ”Mitä enemmän tiedostoja, sitä parempi botti.” | Jokaisella lähteellä pitää olla nimetty tietotarve. |
| ”Luotettava lähde riittää.” | Myös luotettava lähde voi olla vanhentunut tai väärä juuri tähän tehtävään. |
| ”Testi on sama asia kuin kysymys.” | Testissä on syöte, odotettu toiminta ja läpäisyehto. |
| ”Testit kirjoitetaan, kun botti on valmis.” | Ennalta kirjoitettu odotus estää tuloksen selittämisen jälkikäteen onnistumiseksi. |

## Arvioitava näyttö

Hyväksyttävä tuotos sisältää:

- tietotarpeet, jotka perustuvat tunnin 14 määrittelyyn
- 3–5 lähdettä ja perustelun niiden käytölle
- maininnan lähteen ajantasaisuudesta ja käyttörajoista
- yhden nimetyn kattavuusaukon
- toimintaohjeen tilanteeseen, jossa tietoa ei löydy
- positiivisen, negatiivisen ja reunatapaustestin
- jokaiselle testille odotetun toiminnan ja läpäisyehdon

## Eriyttäminen

**Tukireitti:** käytä opettajan antamaa kolmen lähteen pakettia ja valmista testitaulukkoa.

**Syventävä reitti:** lisää ristiriitainen tai vanhentunut lähde ja määritä testi, joka paljastaa ongelman. Syventävä työ ei kasvata pakollista ydintuotosta.

## Siirtymä tuntiin 17

> Tunnilla 17 rakennat ensimmäisen version. Aja silloin nämä samat testit muuttamatta odotuksia sen mukaan, mitä botti vastaa.
