# Projektidokumenttibotti — viimeistele ja esittele

## Johdanto: pelaat kovaa nyt

Edellisellä oppitunnilla aloitit rakentaa omaa bottiasi — Custom GPT:tä, joka kyselee sinulta projektista ja luo siitä struktuoidun projektisuunnitelman. Se oli haastava tehtävä, koska täytyi ajatella, mitä kysymyksiä botti pitäisi esittää, miten niiden avulla kerätä oleelliset tiedot, ja miten koota vastaukset järkeväksi dokumentiksi. Nyt tulee vielä hauskempi ja tärkeämpi osa: varmistaa, että botti oikeasti toimii, ja esitellä se.

Tässä vaiheessa et ole enää rakentaja, joka miettii teorioita. Olet testaja, iteroija ja esittelijä. Teet bottista toimivan, virheettömän ja vakuuttavan. Ja sitten näytät sen muille.

## Viimeistelyvaihe: rajaukset, reunatapaukset ja parantaminen

Projektidokumenttibotti on valmis, mutta se ei ole täydellinen. Mikään ei ole. Viimeistelyvaiheessa tehtävä on käydä läpi kolme asiaa, joita olet jo kohdannut Botin testaaminen -oppitunnilla, mutta nyt omaa bottia varten.

Ensimmäinen on rajausten tarkistus. Botti on suunniteltu tekemään tietyt asiat: kysyä projektista, kuulla vastaukset ja luoda suunnitelma. Sen ei pitäisi tehdä muuta. Jos joku pyytää sitä kirjoittamaan runoa tai antamaan sijoitusneuvoja, sen pitäisi sanoa "en osaa" eikä yrittää. Selkeät rajat tekevät botista käytettävän ja turvallisen. Lue system prompt uudelleen ja varmista, että rajaukset ovat selkeät. Kirjoita lisää ohjeita, jos tarvitaan.

Toinen on reunatapausten käsittely. Mitä tapahtuu, kun käyttäjä kirjoittaa vain "no" tai "en tiedä"? Mitä tapahtuu, jos projektista ei ole olemassa yhtään dokumentaatiota? Entä jos käyttäjä kysyy, kuinka saada apua muista tiimin jäsenistä? Nämä ovat reunatapaukset — outoja, epätavallisia tilanteita, joissa botti voi kaatua tai vastata tyhmästi. Testaa niitä. Monta.

Kolmas on vastausten laadun parantaminen. Kun botti luo suunnitelmadokumentin, pitäiskö sen sisältää kuvia, taulukoita, väriä? Pitäiskö projektille olla nimeä, kuvaa, budjetin arviota? Testaa ja paranna. Tee dokumentista niin hyvä, että se näyttää oikeasti hyödylliseltä.

Viimeistelyssä käytetään samoja testaustyökaluja kuin Botin testaaminen -oppitunnilla: positiiviset testit (normaali käyttö), negatiiviset testit (kieltäytyminen), reunatapaukset (odottamattomat tilanteet). Dokumentoi jokainen testi ja merkitse, meniko se läpi vai ei. Jos testi epäonnistuu, korjaa system promptia ja testaa uudelleen.

## Esittelyn valmistelu: kuinka esitellään botti vakuuttavasti

Esittely ei ole PowerPoint-kalvojen selittämistä. Se on live-demo. Istut tietokoneen ääressä, avaat botin ja osoitat, miten se toimii. Yleisö näkee sen reaaliajassa.

Esittelyn valmistelu alkaa käsikirjoituksella, mutta se ei ole word-dokumentti. Mieti, mitä tarinaa haluat kertoa. Mitkä ovat botin tärkeimmät ominaisuudet? Mitä ongelmaa se ratkaisee? Kenelle se on hyödyllinen? Yksinkertainen tarina on parempi kuin pitkä luettelo ominaisuuksista. Esimerkiksi: "Projektien dokumentointi on usein väsyttävää ja aikaa vievää. Tämä botti tekee siitä mukavampaa kysymällä sinulta projektista, kuuntelun tavalla, ja kootessaan sitten kaikki automaattisesti yhtenäiseksi suunnitelmaksi. Näytetään, miten se toimii."

Seuraavaksi valmistele tietyt käyttöskenaariot, jotka näytät livedemoissa. Valitse projekti, jonka tunnet hyvin — jopa kuvitteellinen, mutta realistinen. Esimerkiksi: "Rakennamme verkkosivuston pienelle e-kaupalle." Tiedät, mitä kysymyksiä botti esittää, ja pystyt vastaamaan luonnollisesti. Harjoittele, että se näyttää sujuvalta eikä pysähdytä sekuntien ajaksi miettimään, mitä sanoa.

Live-demossa oikean tekemisen pitää näkyä. Avaa botti. Näytä, miten se alkaa kysymään. Kuuntele kysymykset ääneen: "Entä projektin aikajanaksi — kuinka pitkä aika on käytettävissä?" Vastaa selkeästi ja luontevasti. Kun botti kokoaa suunnitelmaa, näytä prosessi. Anna muille nähdä, miten se etsii tietoa, jäsentää sitä ja rakentaa dokumenttia. Kun lopulta dokumentti on valmis, näytä koko tulos. Anna ihmisille hetki lukea ja ymmärtää, mitä he näkivät.

Harjoituksen jälkeen testaa teknologia. Varmista, että internet toimii, botti vastaa nopeasti, ja näytöllä näkyy se, mitä haluat näyttää. Ei mitään kuitenkaan kulje näin pieleen kuin yllätykset teknologian kanssa.

## Vertaisarviointi: miten arvioit toisen botin

Kun muut esittelevät omansa, sinulla on rooli. Olet arvioija, mutta ystävällinen arvioija. Vertaisarvioinnin tavoite ei ole saada mahdollisimman monta pistettä toiselle — se on antaa rakentavaa palautetta, joka auttaa kehittämään bottia.

Rakentavassa palautteessa on kolme osaa. Ensimmäinen on positiivinen havainto: mitä botti tekee hyvin? Onko system prompt selkeä? Ovatko kysymykset hyviä? Onko luotu dokumentti helppolukuinen? Kirjoita se alas. Toiseksi merkitse, mikä voisi olla paremmin. Ovatko rajaukset selkeät vai olisiko niitä parannettava? Oliko reunatapausten käsittely robustia vai kaatui botti joihinkin tilanteisiin? Kolmanneksi anna ehdotus: "Tähän voisi lisätä..." tai "Seuraavalla kerralla koittaisit...". Ehdotus on parannusidea, ei kritiikki.

Kirjoita arviointi muutamaan lauseeseen tai kappaleeseen, ei yhteen sanaan. "Hyvä" ei ole arviointi. "System prompti on selkeä ja ohjaa bottia hyvin tehtäväänsä. Kysymykset ovat asiaankuuluvia ja rakentavat realistisen kuvan projektista. Reunatapauksissa botti voisi kertoa paremmin, kun käyttäjä vastaa epäselvästi — nyt se yritsi ajoittain arvata. Seuraavalla kerralla lisäisit ehkä mahdollisuuden käyttäjälle pyytää selitystä kysymykseen." Nyt toinen opiskelija saa palautetta, josta voi oppia.

## Katsaus eteenpäin: tämä botti on seuraavan jakson pohja

Nyt valmistamasi projektidokumenttibotti ei ole lopullinen tuote. Se on muutakin varten. Seuraavassa osiossa, joka alkaa oppitunnilla 19, tutustut agenteihin. Agentti on kuin botti, mutta paljon älykkäämpi ja itsenäisempi. Se voi tehdä asioita ilman, että sinä käsket. Se voi lukea tiedostoja, ajaa komentoja, hakea tietoa ja tehdä päätöksiä yksin.

Projektidokumenttibotistasi tulee agentti seuraavassa osiossa. Ajattele sitä näin: nyt botti istuu ja kuuntelee sinua. Agentti nousee seisomaan, kävelee kantoilla ja tekee asioita. Se saattaa ottaa projektin tiedot, lähettää sähköpostiin, luoda kansion, ladata tarvittavat resurssit, ja tehdä kaiken ilman, että sinulla on vielä aikaa sanoa sana. Sekä botti että agentti rakentuvat samalle pohjalle — sille, mitä olet oppinut promptauksesta, kontekstista ja testaamisesta — mutta agentti tekee enemmän ja itsenäisemmin.

Tämän vuoksi on tärkeä, että viimeistelet botin perusteellisesti nyt. Kun siitä tulee agentti, sen täytyy olla vahva pohja. Jos system prompt on epäselvä tai botti ei osaa käsitellä odottamattomia tilanteita, agentti periyttää tuon pohjan heikkouden. Testaaminen nyt = terveempi agentti myöhemmin.

## OSP2:n yhteenveto: mitä olet oppinut koko osiossa

Nyt, kun olet lähes OSP2:n lopussa, on aika katsoa taaksepäin. Mitä olet oppinut "Tekoälyjen käyttö" -osiosta?

Alusta lähtien olet kohdannut peruskäsitteet. Mitä on tekoäly? Millä se toimii? Miten syötät sille kysymyksen? Opit, että tekoäly on työkalu — ei taikaa, vaan matematiikka ja tekniikka, joka voidaan oppia ja hallita.

Sitten opit promptauksesta. "Anna minulle koodi" ei toimi. "Kirjoita Python-funktio, joka ottaa syötteeksi merkkijonon ja palauttaa sen päinvastoin" toimii. Opit, että mitä tarkempi on pyyntö, sitä parempi on vastaus. Opit myös, että voit iteraatioida — jos vastaus ei ole täydellinen, voit pyytää uudelleen tarkentaen vaatimusta.

Sitten tulivat kontrolli ja rajaukset. Ymmärsit, että bottia pitää hallita — antaa sille selkeät ohjeet, mitä se voi tehdä ja mitä ei. Rajaukset tekevät botista turvallisemman ja käyttäjäystävällisemmän. Ymmärsit myös, että testaus on olennainen osa — botti ei ole valmis, kunnes sen tietää toimivan eri tilanteissa.

Dokumentaation merkitys tuli selväksi. Et vain rakenna bottia — dokumentoit, mitä teet, miksi ja miten se toimii. Dokumentaatio auttaa sinua itse muistamaan, ja se auttaa muita ymmärtämään ja käyttämään bottia.

Ja viimeisenä — viimeistelynä ja esittelynä — opit, että tekeminen on vain puoli tarinasta. Pitää myös osata kertoa muille, mitä teit ja miksi se on tärkeää. Esittely on taito, ja se kehittyy harjoituksella.

Koko Tekoälyjen käyttö -osio rakennetaan sille, että opiskelet käyttämään tekoälyä **vastuullisesti**, **itsenäisesti** ja **dokumentoidusti**. Nämä kolme sanaa tiivistävät koko osion. Vastuullisesti — älä käytä sitä vain siksi, että se on kivaa, vaan koska se ratkaisee ongelman. Itsenäisesti — älä odota, että opettaja neuvoo jokaista askelta, vaan ota omaa vastuuta oppimisestasi. Dokumentoidusti — näytä ja selitä, mitä teet, jotta muut voivat oppia sinusta ja sinä voit oppia itsestäsi.

Seuraavassa osiossa, Agentit-osiossa, nämä taidot syvenevät ja laajenevat. Agenteista oppiminen vaatii samaa vastuullisuutta, itsenäisyyttä ja dokumentointia — mutta isommassa mittakaavassa. Ja pohja, jolla seisot, rakennetaan siitä, mitä olet oppinut täällä.
