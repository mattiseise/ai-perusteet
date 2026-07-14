# Mitä tekoäly on — ja mitä se ei ole

## Johdanto: Miksi tämä aihe kuuluu ITT-ammattilaisille

Tekoälytyökalut ovat jo osa jokapäiväistä TVT-työtä. Saatat käyttää niitä koodin kirjoittamiseen, dokumentaation luomiseen tai ongelmien ratkaisuun. Mutta jos ymmärrät vain sen, miten käyttää näitä työkaluja, et osaa arvioida niiden rajoja, riskejä tai sitä, milloin niiden käyttö on sopivaa ja milloin ei. Ammattilaisena sinun on osattava nähdä, mitä tekoälyltä näyttävän järjestelmän taustalla oikeasti tapahtuu — ja mitä se ei osaa tehdä, vaikka näyttäisikin osaavansa.

Tämä oppitunti käsittelee tekoälyn perusluonnetta siten, että voit tehdä tietoisia päätöksiä ammattilaisena. Se ei opeta sinua käyttämään tekoälyä paremmin — eikä sillä ole väliä, jos ymmärrys on väärä, koska väärä ymmärrys voi johtaa seurauksiin, joita et ole odottanut. Tämä oppi on pohja, jolle kaikki seuraava rakentuu.

## Tekoälyn ja koneoppimisen ero — ja miksi se merkitsee

Monet käyttävät sanoja "tekoäly" ja "koneoppiminen" ikään kuin ne olisivat sama asia. Ne eivät ole. Tekoäly on laajempi käsite — se tarkoittaa mitä tahansa järjestelmää, joka näyttää tekevän älykkäitä päätöksiä ilman, että ihminen on eksplisiittisesti ohjelmoinut jokaista päätöstä. Koneoppiminen puolestaan on yksi tapa rakentaa tekoälyjärjestelmiä: järjestelmä oppii datasta automaattisesti, eikä ihminen kirjoita sääntöjä käsin.

Mutta tekoäly voi rakentua muillakin tavoilla. Esimerkiksi yksinkertainen sääntöpohjainen järjestelmä — "jos asiakkaalla on yli 20 vuotta historiaa ja hänen maksutietonsa on puhdas, hyväksy laina automaattisesti" — on tekoälyä eksplisiittisen sääntöjärjestelmän mielessä, mutta ei ole koneoppimista. Samoin pelikentän strategia, jonka ohjelmoija on kirjoittanut käsin (jos pelaaja lähestyy, puolusta; jos pelaaja on kaukana, hyökkää), on ainakin jossain määrin tekoälyä, mutta täysin deterministinen ja sääntöjen varassa.

Tämä ero on tärkeä ammattilaiselle, koska se vaikuttaa siihen, miten voit luottaa järjestelmään. Koneoppimisen varassa oleva tekoäly on **probabilistinen** — se tuottaa tilastollisen arvion, ei varmuutta. Sääntöpohjainen tekoäly on tavallisesti **deterministinen** — samat syötteet tuottavat aina samat tulokset. Deterministisiä järjestelmiä on helpompi testata, virheenkorjata ja validoida. Probabilistiset järjestelmät vaativat erilaista ajattelutapaa.

**Pysähdy hetkeksi: Ajattele tietokonejärjestelmiä, joita käytät. Mikä niistä on deterministinen (antaa saman tuloksen), ja mikä ei? Kuinka tämä vaikuttaa siihen, mihin tarkoituksiin voit niitä käyttää luotettavasti?**

Käytännön esimerkkinä: olet kehittäjä, joka integroi koneoppimismalleja kulujen ennustamiseen. Malli sanoo, että kulujen summa tulee olemaan 4500 euroa plus miinus 300 euroa. Mutta talouspäällikkö haluaa tarkat luvut budjetointia varten. Tämä on ristiriita. Malli voi oppia datasta hyvin — se voi olla 95-prosenttisesti oikein — mutta se ei voi koskaan olla deterministinen. Jos talous tarvitsee täsmällisen luvun, jolle ei ole takuuta, sinun täytyy rakentaa järjestelmän ympärille kontrollit, jotka ovat deterministisiä: ihmisen hyväksyntä, riskienhallinnan mekanismit, vaihtelun rajat. Malli antaa tietoa, mutta päätöstä ei voi delegoida täysin sille.

## Probabilistinen laskenta — miksi tekoäly tuottaa eri vastauksia

Perinteinen ohjelma — esimerkiksi pankkisovellus, joka laskee korkoa tai validoi tilinumeroita — on deterministinen. Kirjoitat säännön: "jos tilinumeron pituus on 14, hyväksy se". Sama tilinumero tuottaa aina saman vastauksen. Järjestelmä ei tee mitään arvioita. Se noudattaa logiikkaa, jonka ihminen on kirjoittanut.

Koneoppimismalli on eri asia. Sen sijaan, että logiikka olisi kirjoitettu, logiikka on opittu **tilastollisista kuvioista datasta**. Kun malli näkee tuhansia esimerkkejä, se oppii: "Kun näen nämä merkit, seuraava merkki on usein tämä." Se ei tiedä miksi — se on oppinut pelkästään datasta. Se on kuin olisi oppinut pelkkiä datakorrelaatioita tekemään arvauksia, ei todellisen, syvän ymmärryksen perusteella.

Tämän seurauksena malli tuottaa **todennäköisyyksiä**, ei varmuuksia. Kun annat esikäsiteltyä dataa chatbot-mallille ja kysyt sille kysymyksen, malli ei hae vastausta tietokannasta — se valitsee seuraavan todennäköisimmän merkin. Sitten seuraavan. Ja seuraavan. Kunnes se päättää lopettaa. Jokainen valinta on paras arvio sen opittujen kuvioiden perusteella, mutta se ei ole logiikkaketju, joka johtuisi matemaattisista säännöistä. Se on tilastollinen prosessi.

Tämä selittää monia tekoälyn omituisuuksia, joita näet käytännössä. Miksi saman kysymyksen esittäminen kahdesti antaa hieman erilaisen vastauksen? Koska jokainen mallin "päätös" merkeittäin on probabilistinen. Miksi malli joskus kirjoittaa jotain, joka näyttää älykkäältä, mutta on täysin väärää? Koska se arvaa seuraavaa merkkiä perustuen dataan, jossa se esiintyi usein, vaikka konteksti olisi erilainen. Se ei ymmärrä asiaa. Se ennustaa merkkejä tilastollisten kuvioiden perusteella.

**Pysähdy hetkeksi: Jos tekoäly tuottaa todennäköisyyksiä eikä varmuuksia, missä TVT-ammattilaisten tehtävissä malleja käytetään siten, että epävarmuus on ongelmallista? Missä se ei olisi ongelma?**

## Tekoälyn rajat — mitä se ei voi tehdä

Tekoäly näyttää tekevän asioita, joita se ei voi tehdä. Se näyttää neuvottelevan, tekevän päätöksiä ja ratkovan ongelmia oman "älykkyytensä" perusteella. Mutta nämä tulkinnat ovat harhaanjohtavia.

Ensinnäkin tekoäly ei ole yleisäly. Se on rakennettu tiettyyn tehtävään, tietyllä datalla, tietyssä kontekstissa. Kuva-analyysimalli, joka tunnistaa koirat ja kissat, ei osaa lukea tekstiä tai kuulla musiikkia. Tekstiaineistoon opetettu malli, joka tuottaa hyviä tarinoita, ei voi diagnosoida sairauksia tekstin perusteella. Nämä ovat eri "älyllisen" osaamisen alueita. Mitä enemmän tiettyä mallia on opetettu, sitä parempi se on kyseisessä tehtävässä — mutta sitä kapeampi on sen osaamisalue.

Toiseksi tekoäly ei toimi kausaliteetin perusteella. Se ei ymmärrä syy-seuraussuhteita. Se vain näkee kuvioita. Jos tietokanta osoittaa, että "ihmiset, joiden nimi alkaa J:llä, ostavat usein kirjoja", malli voi oppia tämän kuvion ja ennustaa, että seuraava J:llä alkavalla nimellä oleva ihminen ostaa kirjan. Mutta se ei ymmärrä, ettei nimen alkukirjaimessa ole mitään sellaista, mikä edistäisi kirjojen ostamista. Se on ollut pelkkä tilastollinen sattuma datassa. Tämä tekee tekoälystä vaarallisen tietyissä konteksteissa: se voi vahvistaa olemassa olevia harhoja ja tunnistaa virheellisiä syy-seurausyhteyksiä.

Kolmanneksi tekoäly ei osaa neuvotella tai tehdä todellisia arvopäätöksiä. Se ei ymmärrä oikeutta, etiikkaa tai ihmisen arvoa. Se voi tuottaa tekstiä, joka näyttää neuvottelevalta tai harkitulta, koska se on oppinut merkkikuvioita, joissa neuvottelu näyttää siltä. Mutta kun teemme päätöksiä, jotka koskevat ihmisen elämää — kuka saa lainaa, kuka värvätään, kenen oleskeluluvat hyväksytään — emme voi delegoida näitä päätöksiä järjestelmälle, joka näkee vain kuvioita datassa. Nämä päätökset vaativat inhimillistä harkintaa ja vastuunottoa.

Käytännön esimerkkinä: terveydenhuollon yritys käyttää mallia diagnoosien tukena. Malli tuottaa todennäköisyyksiä tiettyjen sairauksien esiintymisestä potilastietojen perusteella. Mutta se ei voi verrata näitä todennäköisyyksiä potilaan elämää säästävien hoitojen riskeihin. Se ei voi päättää, onko "80 prosentin varmuus keuhkosyövästä" tarpeeksi vahva peruste invasiiviselle toimenpiteelle. Lääkäri tekee nämä päätökset. Malli on ammattilaiselle työkalu — informaation lähde — mutta ammattilaisuus on siinä, että ihminen ymmärtää mallin rajat ja kantaa vastuun.

## Käsitteen yhteenveto

Tekoäly on järjestelmä, joka tekee päätöksiä ilman eksplisiittisiä ihmisen kirjoittamia sääntöjä. Kun tekoäly rakentuu koneoppimisen varaan, se tuottaa **todennäköisyyksiä tilastollisen datan perusteella**, ei varmuuksia. Tämä tekee siitä hyödyllisen ammattilaiselle, mutta vaatii muistamaan kolme ratkaisevaa rajaa: tekoäly on kapea-alaista (ei yleisälyä), se ei ymmärrä syy-seuraussuhteita (vain kuvioita) eikä voi kantaa arvopäätösten vastuuta (se on ihmisen tehtävä). ITT-ammattilaisena sinun on ymmärrettävä nämä rajat, jotta tiedät, missä kohdin tarvitaan inhimillistä älyä, kontrollia ja vastuunottoa.

---

## Seuraavaksi

Oppitunnin seuraavassa osassa käytämme tätä perustietämystä konkreettisiin tapauksiin: analysoimme todellisia järjestelmiä, jäsennämme väärinkäsityksiä ja harjoittelemme ammatillisesti kriittistä ajattelua tekoälyyn liittyen.