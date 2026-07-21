# Opettajan materiaalit — oppitunti 15: tietopohja ja testisuunnitelma

## Oppitunnin tarkoitus

Oppija kuratoi oman bottinsa tietopohjan ja kirjoittaa testit ennen botin rakentamista. Tunnilla ei siis vielä tavoitella toimivaa bottia. Työn arvo on siinä, että oppija päättää etukäteen, mihin vastaukset saavat perustua ja millainen toiminta myöhemmin hyväksytään. Testit ajetaan ensimmäisen kerran tunnilla 17, minkä jälkeen tulokset dokumentoidaan ja korjattu toteutus testataan uudelleen tunnilla 18.

## Osaamistavoitteet

Oppija:

- johtaa botin määrittelystä 5–8 tietotarvetta
- valitsee 2–4 lähdettä tehtävän, ei määrän, perusteella
- arvioi lähteiden luotettavuutta, ajantasaisuutta, kattavuutta ja käyttöoikeutta
- erottaa tietopohjan RAG-toteutuksesta sekä hakuvaiheen virheen vastauksen muodostamisen virheestä
- suunnittelee käyttäjä- tai roolikohtaisen käyttöoikeusrajauksen
- kirjaa tietopohjan aukot ja toiminnan puuttuvan tiedon tilanteessa
- kirjoittaa positiivisen, negatiivisen ja reunatapaustestin
- määrittää jokaiselle testille odotetun toiminnan ja läpäisyehdon

## Ydinviesti

Tietopohja ei tee botista automaattisesti luotettavaa. Luotettavuus alkaa siitä, että oppija tuntee aineiston alkuperän, tehtävän ja rajat. Kun tietopohjan aukko on nimetty ja sen varalle on kirjoitettu testi, puuttuva tieto ei jää epämääräiseksi riskiksi vaan muuttuu havaittavaksi osaksi suunnitelmaa.

Pidä tunnilla erillään kolme asiaa. Tietopohja on hallittu aineisto. RAG on mahdollinen toteutustapa, jossa järjestelmä hakee aineistosta katkelmia kielimallille. Käyttöoikeusrajaus puolestaan ratkaisee jo ennen hakua, mitä aineistoa kyseinen käyttäjä saa saada mallin kontekstiin. Näiden sekoittaminen johtaa helposti siihen, että tietopohjan laatua pidetään todisteena sekä haun että vastauksen luotettavuudesta.

## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **rakennuspalikka 3: kuratoitu tietopohjataulukko, kattavuusarvio ja kolmen testin suunnitelma**. Tunnin rytmi kannattaa pitää rauhallisena: lähteiden etsimiseen on helppo käyttää kaikki aika, vaikka varsinainen oppimistavoite on valintojen perusteleminen ja testattavien odotusten kirjoittaminen.

| Aika | Vaihe | Opettajan tehtävä |
| --- | --- | --- |
| 0–10 min | Silta määrittelyyn | Näytä, miten yksi käyttötapaus muuttuu tietotarpeiksi. |
| 10–25 min | Lähteiden arviointi | Mallinna hyvä, puutteellinen ja tehtävään tarpeeton lähde. |
| 25–55 min | Kuratointi | Oppijat valitsevat 2–4 lähdettä ja täyttävät perustelutaulukon. |
| 55–70 min | Aukot | Oppijat kirjoittavat, mitä tietopohja kattaa, mitä ei ja miten botin pitää toimia tiedon puuttuessa. |
| 70–85 min | Testisuunnitelma | Kirjoita positiivinen, negatiivinen ja reunatapaus sekä nimeä, testataanko haun osuvuutta vai muodostetun vastauksen tukea. |
| 85–90 min | Tallennus | Varmista aineiston sallittu käyttö ja yhteys tunnin 17 rakentamiseen. |

## Tyypilliset väärinkäsitykset

Oppija saattaa ajatella, että suuri tiedostomäärä tekee botista paremman. Palauta keskustelu silloin tietotarpeisiin: jokaisella mukaan otetulla lähteellä pitää olla nimetty tehtävä, ja tarpeeton aineisto voi vaikeuttaa oikean tiedon löytämistä.

Myös luotettavan lähteen käsite kaipaa usein tarkennusta. Maineikas tai virallinen lähde voi olla vanhentunut, liian yleinen tai väärä juuri tähän käyttötapaukseen. Pyydä oppijaa kertomaan lähteen nimen lisäksi, mihin tarpeeseen se vastaa ja milloin sen sisältö on tarkistettu.

Testi sekoittuu helposti tavalliseen kysymykseen. Konkreettinen syöte on vasta testin alku; lisäksi tarvitaan etukäteen kirjoitettu odotettu toiminta ja havaittava läpäisyehto. Juuri ennakkoon lukittu odotus estää selittämästä mitä tahansa sujuvaa vastausta jälkikäteen onnistumiseksi.

RAG-testissä kaksi epäonnistumista voivat näyttää käyttäjälle samalta. Jos vastaus puuttuu, selvitä ensin löytyikö oikea lähde. Jos löytyi, tarkista tukeeko lähde muodostettua vastausta. Käyttöoikeustestissä onnistuminen tarkoittaa, ettei luvaton lähde päädy hakuun tai vastaukseen — ei vain sitä, että botti lupaa olla kertomatta siitä.

## Arvioitava näyttö

Hyväksyttävässä tuotoksessa seuraavat kohdat muodostavat toisiinsa liittyvän näytön. Käytä listaa arvioinnin tukena, mutta pyydä oppijaa tarvittaessa avaamaan valintojensa välinen yhteys:

- tietotarpeet, jotka perustuvat tunnin 14 määrittelyyn
- 2–4 lähdettä ja perustelun niiden käytölle
- maininnan lähteen ajantasaisuudesta ja käyttörajoista
- yhden nimetyn kattavuusaukon
- toimintaohjeen tilanteeseen, jossa tietoa ei löydy
- positiivisen, negatiivisen ja reunatapaustestin
- jokaiselle testille odotetun toiminnan ja läpäisyehdon

## Eriyttäminen

**Tuetussa työskentelyssä** oppija käyttää opettajan antamaa kahden lähteen pakettia ja valmista testitaulukkoa. Tuki kohdistuu aineiston löytämiseen ja työn jäsentämiseen; oppija perustelee silti itse lähteiden tehtävät ja testien odotukset.

**Syventävällä reitillä** tietopohjaan tuodaan tarkoituksella ristiriitainen tai vanhentunut lähde. Oppija suunnittelee testin, joka paljastaa ongelman, ja perustelee, miten ristiriita pitäisi ratkaista. Syventävä työ ei kasvata pakollista ydintuotosta.

## Siirtymä tuntiin 17

> Tunnilla 17 rakennat ensimmäisen version. Aja silloin nämä samat testit muuttamatta odotuksia sen mukaan, mitä botti vastaa. Jos ensimmäinen versio ei läpäise testiä, testi on tehnyt tehtävänsä: se on näyttänyt, mitä pitää korjata.
