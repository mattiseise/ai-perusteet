# Konteksti ratkaisee — miksi sama kysymys antaa eri vastauksen

## Johdanto

Kuvittele, että olet IT-tukihenkilö ja saat sähköpostissa viestin: "Tietokone ei toimi." Se on maininta, mutta mitä se tarkoittaa? Onko kyse verkkovirheestä? Eikö käyttöjärjestelmä käynnisty? Kaatuuko ohjelma? Eikö näyttö syty? Sama koskee tekoälyä. Jos sanot vain "auta minua", saat yleisen, ehkä hyödyttömän vastauksen. Mutta jos kerrot "olen IT-opiskelija, tarvitsen apua Linux-palvelimen SSH-ongelmaan, virhe on 'connection refused', yritän ottaa yhteyttä osoitteeseen 192.168.1.100:22" — silloin tekoäly ymmärtää, mikä on todellinen ongelma, ja voi antaa konkreettista apua. Tämä ero on *konteksti* — ja se on kaiken tekoälyviestinnän ydin.

Tämän tunnin jälkeen sinulla on tuomaripöydällesi neljäs todistusaineisto: konteksti ei ole pieni asia — se on kaiken tekoälyviestinnän perusta.

## Mitä konteksti on

Konteksti on kokonaisuus kaikkea sitä tietoa, jota tekoäly tarvitsee ymmärtääkseen, mitä sinä todella kysyt ja mitä haluat. Se ei ole vain yksittäinen kysymys tai käsky. Konteksti koostuu useista osista: kuka olet (roolisi), mitä taustaa sinulla on, mitä haluamme saavuttaa (tavoite), mitkä ovat rajat ja rajoitukset sekä konkreettiset esimerkit siitä, millaista vastausta odotat.

Kun opettaja neuvoo sinua matematiikan ongelmassa, hän ei vain kuule kysymystä — hän tietää, että olet 15-vuotias opiskelija, että olet oppinut derivaatat, että analysoit nyt funktion nollakohtia ja että hän haluaa sinun oppivan prosessin, ei vain saavasi vastausta. Kaikki tämä konteksti auttaa opettajaa antamaan juuri oikeanlaisen selityksen. Tekoäly tarvitsee saman.

> **Pysähdy hetkeksi:** Muista viimeksi, kun kysyit jotain internetistä tai ChatGPT:ltä ja sait täysin väärän tai hyödyttömän vastauksen. Mikä tieto puuttui? Mitkä tiedot olisivat auttaneet?

## Kontekstin osat

Hyvä konteksti rakentuu viidestä pääosasta. Ensimmäinen on *rooli*: keitä olemme, mikä on ammattitaitomme ja näkökulmamme. Jos kerrot "olen ammattitaitoinen C++-ohjelmoija", tekoäly tietää, että se voi käyttää tekniikkasuomea ja olettaa tietyn osaamistason. Jos sanot "olen IT-aloittelija", vastaus voi olla perusteellisempi ja helpommin hyödynnettävä.

Toinen osa on *taustatieto*: mitä on jo tehty, mitä olemme oppineet ja mitkä ovat lähtökohdat. Kun yrität korjata ohjelmaa, jossa sinulla oli virhe aiemmin, kerro siitä. Kun analysoit tietokantaa, jota olet jo käyttänyt kuukausia, mainitse, mitä jo tiedät sen rakenteesta.

Kolmas osa on *tavoite*: miksi kysyt, mitä haluat tehdä ja mihin käytät vastausta. "Anna minulle lista pilvipalveluista" on eri asia kuin "valitse parhaat pilvipalvelut startup-yritykselle, jolla on budjetti 500 euroa kuukaudessa ja joka tarvitsee SQL-tietokannan." Tavoitteen selventäminen muuttaa vastausta merkittävästi.

Neljäs osa on *rajaukset*: mitä et halua, mikä ei ole olennaista ja mitkä asiat on jätettävä pois. "Selitä pilvipalvelut, mutta älä mainitse AWS:ää, koska tiedämme siitä jo." Tai "En halua filosofista vastausta, vain käytännön neuvoja."

Viides osa on *esimerkit*: näytä mallia siitä, mitä haluat. Jos haluat, että tekoäly kirjoittaa koodin dokumentaatiota samalla tyylillä kuin sinä, anna näyte aiemmin kirjoittamastasi dokumentaatiosta. Jos haluat koodia, joka noudattaa tiettyä rakennetta tai suunnittelutapaa, näytä esimerkki.

> **Pysähdy hetkeksi:** Ajattele tehtävää, jota teet usein ohjelmoinnissa — esimerkiksi "kirjoita funktio, joka käsittelee käyttäjän syötteen". Mitkä viidestä kontekstin osasta olisivat tärkeimpiä tässä tapauksessa? Miksi?

## Prompting ≠ konteksti

Monella on tästä väärinkäsitys: he ajattelevat, että "hyvä prompti" on sama asia kuin "hyvä konteksti". Se on kuin sanoisi, että reseptin otsikko ("Pastakeitto") olisi sama kuin koko resepti – ainesosat, valmistusohjeet, käsittelylämpötila ja kypsennysajat. Prompti on *kysymys*, joka esitetään kontekstin puitteissa. Konteksti on *pohja*, jonka päälle prompti rakentuu.

Kuvittele, että istut opettajan kanssa hänen työhuoneessaan ja kysyt matematiikan kysymystä. Opettaja on jo nähnyt aiemmat työsi, tietää, mistä olet epävarma, tuntee tavoitteesi (läpäisy vai erinomainen arvosana) ja tietää, mitä olet jo oppinut. Kaikki tämä on *konteksti*. Sitten esität *promptin*: "Kuinka ratkaiset nollakohdan?" Prompti on kysymys, mutta konteksti on kaikki se muu, joka tekee kysymyksestä ymmärrettävän ja vastauksesta hyödyllisen.

Tekoälyjärjestelmissä pätee sama periaate. Voit antaa saman promptin kahdelle eri tekoälylle, mutta jos toisen konteksti on huono ja toisen hyvä, vastaukset ovat täysin erilaiset. Se, että "promptit" ovat samanlaiset, ei tarkoita, että *konteksti* on sama. Liian moni aloittelija luottaa siihen, että kehittää "oikean" kysymyksen, mutta jättää kontekstin huolimattomaksi tai tyhjäksi. Silloin tulos jää heikoksi.

## Miksi huono konteksti tuottaa huonoa jälkeä

Kun konteksti on epäselvä, tekoäly joutuu arvailemaan. Se yrittää täydentää puuttuvat tiedot omilla oletuksillaan. Oletukset ovat usein vääriä. Jos kysyt "kuinka järjestelmöin palvelimen", tekoäly voi ajatella, että olet Windows-käyttäjä, Linux-asiantuntija tai aloittelija — jokainen oletus johtaa eri vastaukseen. Jos jaat koodikatkelman ilman kontekstia, tekoäly voi ehdottaa ratkaisuja, joita et pysty toteuttamaan omassa ympäristössäsi.

Huonon kontekstin seurauksena saat usein myös liian pitkiä tai hajanaisia vastauksia. Tekoäly ei tiedä, mihin vastaus pitäisi kohdistaa, joten se kirjoittaa kaiken, mitä tietää. Jos kerrot selvästi "tarvitsen 5 minuutin opetusvideon käsikirjoituksen", saat ytimekkään vastauksen. Jos sanot vain "kirjoita video tekoälystä", saatat saada kahden tunnin esseen aiheesta.

Kontekstin puuttuminen aiheuttaa myös turhauttavia väärinymmärryksiä. Opettaja tulkitsee "apua matikassa" eri tavoin riippuen siitä, oletko yläkoululainen vai yo-opiskelija. Tekoäly toimii samoin — ja ilman kontekstia se valitsee usein aivan liian yleisen tai liian yksityiskohtaisen tason.

> **Pysähdy hetkeksi:** Mieti, millä tavoin antaisit itse kontekstia ystävällesi, joka auttaa sinua IT-ongelmassa kasvotusten. Mitä kerrot ensin, mitä viimeiseksi?

## Kontekstin rakentaminen käytännössä

Käytännössä kontekstin rakentaminen alkaa siitä, että ymmärrät, mitä itse tarvitset. Ennen kuin avaat tekoälyn, kirjoita itsellesi lyhyesti: kuka olen, mitä teen, mikä on ongelmani, mitä tiedän jo. Kerro sitten nämä asiat tekoälylle – ei välttämättä muodollisesti, mutta selvästi.

Esimerkiksi:
- Huono: "Koska tietokanta on hidas."
- Hyvä: "Olen IT-opiskelija, ja yritämme nopeuttaa SQL-tietokantaa. Taulukossa on noin 100 000 riviä, ja TOP-10-haku kestää nyt 3 sekuntia. Olemme jo lisänneet indeksin hakukenttään, mutta se ei auttanut. Tarvitsemme konkreettisia neuvoja, joita voimme testata omassa laboratorioympäristössämme."

Toinen esimerkki:
- Huono: "Ohjelmani ei toimi."
- Hyvä: "Olen kirjoittanut C++-ohjelman, joka lukee CSV-tiedostoa ja lajittelee tiedot. Kun tiedosto on pienempi kuin 1000 riviä, se toimii. Kun tiedosto on 10 000 riviä, ohjelma kaatuu segmentation faultiin. Olen käyttänyt vector-rakennetta tietojen tallentamiseen. Tarvitsen apua sen selvittämiseen, miksi muisti loppuu."

Nämä ovat silti lyhyitä, mutta ne sisältävät roolin, taustan, tavoitteen ja rajaukset. Ne tekevät tekoälyn vastauksesta hyödyllisemmän ja kohdennetumman.

## Yhteenveto

Konteksti on yksittäistä promptia paljon tärkeämpi tekoälyviestinnän logiikassa. Se rakentuu viidestä osasta — roolista, taustasta, tavoitteesta, rajauksista ja esimerkeistä — ja ohjaa tekoälyä antamaan sinulle juuri sellaista apua, jota tarvitset. Hyvä konteksti on investointi: se vaatii hiukan enemmän aikaa ajatteluun ja kirjoittamiseen, mutta tuloksena on vastaus, joka on todella hyödyllinen eikä turha. Tämän kurssin ydinasia on, että konteksti ei ole sama kuin prompti — se on pohja, jolle jokainen hyvin muotoiltu kysymys rakentuu. Kontekstitaidot ovat IT-ammattilaiselle yhtä tärkeitä kuin ohjelmointikielten hallinta tai verkko-osaaminen.

Seuraavalla tunnilla syvennyt kontekstin hallintaan: ymmärrät, että tekoälyn muisti on rajallinen, ja opit hallitsemaan sitä.