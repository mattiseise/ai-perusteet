# Konteksti I: kurssin tärkein käsite

## Johdanto

Kuvittele, että olet IT-tukihenkilö ja saat sähköpostissa viestin: "Tietokone ei toimi." Se on maininta, mutta mitä se tarkoittaa? Onko kyseessä verkkovirhe? Käyttöjärjestelmä ei käynnisty? Ohjelma kaatuu? Näyttö ei sytty? Sama koskee tekoälyä. Jos kerrot vain "auta minua", saat yleisen, ehkä hyödyttömän vastauksen. Mutta jos kerrot "olen IT-opiskelija, tarvitsen apua Linux-palvelimen SSH-ongelmaan, virhe on 'connection refused', yritän ottaa yhteyttä 192.168.1.100:22:iin" — silloin tekoäly ymmärtää, mikä on todellinen ongelma ja voi antaa konkreettista apua. Tämä ero on *konteksti* — ja se on kaiken tekoälyviestinnän sydän.

## Mitä konteksti on

Konteksti on kokonaisuus kaikkea tietoa, jota tekoäly tarvitsee ymmärtääkseen, mitä sinä todella kysyt ja mitä haluat. Se ei ole vain yksittäinen kysymys tai käsky. Konteksti koostuu useista osista: kuka olet (roolisi), mitä taustaa sinulla on, mitä haluamme saavuttaa (tavoite), mitkä ovat rajat ja rajoitukset, sekä konkreettiset esimerkit siitä, millaista vastausta odotat.

Kun opettaja neuvoo sinua matematiikan ongelmaan, hän ei vain kuule kysymyksen — hän tietää, että olet 15-vuotias opiskelija, että olet oppinut derivaatiot, että olet nyt analysoimassa funktion nollakohtia, ja että hän haluaa sinun oppivan prosessia, ei vain saavan vastauksen. Kaikki tämä konteksti auttaa opettajaa antamaan juuri oikeanlaisen selityksen. Tekoäly tarvitsee saman.

> **Pysähdy hetkeksi:** Muista viimeksi, kun kysyit jotain internetistä tai ChatGPT:ltä ja sait täysin väärän tai hyödyttömän vastauksen. Mikä tieto oli puutteellinen? Mitkä olisivat auttaneet?

## Kontekstin osat

Hyvä konteksti rakentuu viidestä pääosasta. Ensimmäinen on *rooli*: ketkä olemme, mikä on ammattitaitomme ja näkökulmamme. Jos kerrot "olen ammattitaitoinen C++-ohjelmoija", tekoäly tietää, että voi käyttää tekniikkasuomea ja olettaa tietyä tasoa osaamista. Jos sanot "olen IT-aloittelija", vastaus voi olla perusteellisempi ja hyödynnettävissä olevampi.

Toinen osa on *taustatieto*: mitä on jo tehty, mitä olemme oppineet, mitkä ovat valmiit lähtökohdat. Kun yrität korjata ohjelmaa, johon sinulla oli virhe aiemmin, kerro siitä. Kun analysoit tietokantaa, jota olet jo käyttänyt kuukausiin, mainitse, mitä jo tiedät sen rakenteesta.

Kolmas osa on *tavoite*: miksi kysyt, mitä haluat tehdä, mihin käytät vastausta. "Anna minulle lista pilvipalveluista" on eri asia kuin "valitse parhaat pilvipalvelut startup-yritykselle, jolla on budjetti 500 euroa kuukaudessa ja tarvitsee SQL-tietokantaa." Tavoitteen selvittäminen muuttaa vastauksen merkittävästi.

Neljäs osa on *rajaukset*: mitä et halua, mitä ei ole relevanttia, mitkä asiat on jätettävä pois. "Selitä pilvipalvelut, mutta älä mainitse AWS:ää, koska tiedämme siitä jo." Tai "En halua filosofista vastausta, vain käytännön neuvoja."

Viides osa on *esimerkit*: näytä mallia siitä, mitä haluat. Jos haluat, että tekoäly kirjoittaa kodin dokumentaatiota samalla tyylillä kuin sinä, anna näyttö aiemmin kirjoittamastasi dokumentaatiosta. Jos haluat koodia, joka noudattaa tiettyä rakennetta tai koodisuunnittelua, näytä esimerkki.

> **Pysähdy hetkeksi:** Ajattele tehtävää, jota teet usein ohjelmoinneissa — esimerkiksi "kirjoita funktio, joka käsittelee käyttäjän syötteen". Mitkä viidestä kontekstin osasta olisivat tärkeimpiä tässä tapauksessa? Miksi?

## Prompting ≠ konteksti

Monella on väärä käsitys: ne ajattelevat, että "hyvä prompti" on sama kuin "hyvä konteksti". Se on kuin sanoa, että reseptin otsikko ("Pastakeitto") on sama kuin koko resepti (ainesosat, valmistusohjeet, käsittelylämpö, kylläisyysajat). Prompti on *kysymys*, joka esitetään kontekstin puitteissa. Konteksti on *pohja*, jonka päälle prompti rakentuu.

Kuvittele, että istut opettajan kanssa hänen konttorissaan ja kysyt matematiikan kysymystä. Opettaja on jo nähnyt sinun aiemmat työt, tietää, mistä olet epävarma, tuntee sinun tavoitteesi (läpäisy vai erinomainen arvosana), ja tietää, mitä olet jo oppinud. Kaikki tämä on *konteksti*. Sitten esität *promptin*: "Kuinka ratkaiset nolla-kohdan?" Prompts on kysymys, mutta konteksti on kaikki se muu, joka tekee kysymyksen ymmärrettäväksi ja vastauksesta hyödyllisen.

Tekoälyjärjestelmissä sama logiikka. Voit antaa saman promptin kahelle eri tekoälylle, mutta jos toisen konteksti on huono ja toisen hyvä, vastaukset ovat täysin erilaiset. Se, että "prompit" ovat samanlaiset, ei merkitse, että *konteksti* on samaa. Liian moni aloittelija luottaa siihen, että pliitelee "oikea" kysymys, mutta jättää kontekstin hutiloitujen tai tyhjäksi. Silloin tulos jää heikoksi.

## Miksi huono konteksti tuottaa huonoa jälkeä

Kun konteksti on epäselvä, tekoäly joutuu arvailemaan. Se yrittää täyttää puuttuvat tiedot omilla oletuksillaan. Oletukset ovat usein väärät. Jos kysyt "kuinka järjestelmöin palvelimen", tekoäly voi ajatella, että olet Windows-käyttäjä tai Linux-ekspertti tai nöyryy aloittelija — jokainen johtaa eri vastaukseen. Jos jaat koodikatkelman ilman kontekstia, tekoäly voi ehdottaa ratkaisuja, joita et pysty toteuttamaan ympäristössäsi.

Huonon kontekstin seurauksena saat myös usein liian pitkiä tai irrallisia vastauksia. Tekoäly ei tiedä, mihin vastaus pitäisi kohdistaa, joten se kirjoittaa kaiken mitä tietää. Jos kerrot selvästi "tarvitsen 5 minuutin opetusvideon skriptin", saat tiiviit rivit. Jos sanot vain "kirjoita video tekoälystä", saatat saada kahden tunnin täydennystä.

Kontekstin puuttuminen myös aiheuttaa turhauttavia väärinymmärryksiä. Opettaja tulkitsee "apua matikassa" eri tavoin riippuen siitä, yläkoululainen vai yo-opiskelija olet. Tekoäly toimii samoin — ja ilman kontekstia se valitsee usein reilusti liian yleisen tai liian spesifin tasoksi.

> **Pysähdy hetkeksi:** Mieti, millä tavoin sinä itse antaisit kontekstia ystävällesi, joka auttaa sinua IT-ongelmassa vastaan kuin face-to-face olisitte? Mitä kerrot ensin, mitä viimeksi?

## Kontekstin rakentaminen käytännössä

Käytännössä kontekstin rakentaminen alkaa siitä, että ymmärrät, mitä sinä itse tarvitset. Ennen kuin avaat tekoälyä, kirjoita itsellesi lyhyesti: kuka olen, mitä teen, mikä on ongelmani, mitä tiedän jo. Sitten kerro nämä asiat tekoälylle — ei välttämättä kovalla muodolla, mutta selvästi.

Esimerkiksi:
- Huono: "Kuin'en tietokanta on hidas."
- Hyvä: "Olen IT-opiskelijana ja yritetään nopeuttaa SQL-tietokantaa. Taulukko on noin 100 000 riviä, ja haku TOP-10:n avulla kestää nyt 3 sekuntia. Olemme jo lisänneet indeksin hakukenttään, mutta se ei auttanut. Tarvitaan konkreettisia neuvoja, joita voimme testata omassa laboratorioympäristössämme."

Toinen esimerkki:
- Huono: "Ohjelmani ei toimi."
- Hyvä: "Olen kirjoittanut C++ -ohjelman, joka lukee CSV-tiedostoa ja lajittelee tiedot. Kun tiedosto on pienempi kuin 1000 riviä, se toimii. Kun tiedosto on 10 000 riviä, ohjelma kaatuu segmentation faultilla. Olen käyttänyt vector-rakennetta tietojen tallentamiseen. Tarvitsen apua sen selvittämiseen, miksi muisti loppuu."

Nämä ovat silti lyhyitä, mutta ne sisältävät roolin, taustan, tavoitteen ja rajaukset. Ne tekevät tekoälyn vastauksen hyödyllisemmäksi ja kohdistetummaksi.

## Yhteenveto

Konteksti on yksittäisiä promptia paljon tärkeämpi tekoälyviestinnän logiikka. Se rakentuu viidestä osasta — roolista, taustasta, tavoitteesta, rajauksista ja esimerkeistä — ja se ohjaa tekoälyä antamaan sinulle tarkalleen sitä apua, jota tarvitset. Hyvä konteksti on investointi: se vaatii hiukan enemmän aikaa ajatteluun ja kirjoittamiseen, mutta tuotoksena on vastaus, joka on todella hyödyllinen eikä haaskausta. Tämän kurssin ydinasia on, että konteksti ei ole sama kuin prompti — se on pohja, jolle jokainen hyväksi lausuttu kysymys rakentuu. Konteksti-taidot ovat IT-ammattilaiselle yhtä tärkeitä kuin ohjelmointikielten hallinta tai verkko-osaaminen.
