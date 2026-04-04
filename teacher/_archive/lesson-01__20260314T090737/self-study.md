# Mitä tekoäly on — ja mitä se ei ole

## Johdanto: Miksi tämä aihe kuuluu ITT-ammattilaisille

Tekoälytyökalut ovat jo osa jokapäiväistä TVT-työtä. Saatat käyttää niitä koodin kirjoittamiseen, dokumentaation luomiseen tai ongelmien ratkaisuun. Mutta jos ymmärrät vain sen, miten käyttää näitä työkaluja, et osaa arvioida niiden rajoja, riskeejä tai sitä, milloin niiden käyttö on sopivaa ja milloin ei. Ammattilaisena sinun on osattava nähdä, mikä tekoälyä näyttävän järjestelmän takaa on oikeasti tapahtumassa — ja mitä se ei osaa tehdä, vaikka näyttäisikin osaavansa.

Tämä oppitunti käsittelee tekoälyn perusluonteen siten, että voit tehdä tietoisia päätöksiä ammattilaisina. Se ei opeta sinua käyttämään tekoälyä paremmin — sillä ei ole väliä, koska väärä ymmärrys voi johtaa seurauksiin, joita et ole odottanut. Tämä oppi on pohja, jolle kaikki seuraava rakentuu.

## Tekoälyn ja koneoppimisen ero — ja miksi se merkitsee

Monet käyttävät sanoja "tekoäly" ja "koneoppiminen" ikään kuin ne olisivat sama asia. Ne eivät ole. Tekoäly on laajempi käsite — se tarkoittaa mitä tahansa järjestelmää, joka näyttää tekevän älykkäitä päätöksiä ilman että ihminen on eksplisiittisesti ohjelmoinneet jokaista päätöstä. Koneoppiminen puolestaan on yksi tapa rakentaa tekoälyjärjestelmiä: järjestelmä oppii datasta automaattisesti eikä ihminen kirjoita sääntöjä käsin.

Mutta tekoäly voi rakentua muilla tavoillakin. Esimerkiksi yksinkertainen sääntöpohjainen järjestelmä — "jos asiakkaalla on yli 20 vuotta historiaa ja hänen maksutietuensa on puhdas, hyväksy laina automaattisesti" — on tekoälyä eksplisiittisen sääntöjärjestelmän mielessä, mutta ei ole koneoppimista. Samoin pelikentän strategia, jonka ohjelmoija on kirjoittanut käsin (jos pelaaja lähestyy, puolusta; jos pelaaja on kaukana, hyökkää), on tekoälyä ainakin jonkin verran, mutta täysin deterministinen ja sääntöjen varassa.

Tämä ero on tärkeä ammattilaiselle, koska se vaikuttaa siihen, miten voit luottaa järjestelmään. Koneoppimisen varassa oleva tekoäly on **probabilistinen** — se tuottaa tilastollisen arvion, ei varmuutta. Sääntöpohjainen tekoäly on tavallisesti **deterministinen** — samat syötöt tuottavat aina samat tulokset. Deterministiset järjestelmät ovat helpompia testata, virheenkorjaukselle ja validoinnille. Probabilistiset järjestelmät vaativat erilaista ajattelutapaa.

**Pysähdy hetkeksi: Ajattele tietokoneista, joita käytät. Mikä niistä on deterministinen (saman tuloksen antava), ja mikä ei? Kuinka tämä vaikuttaa siihen, mihin tarkoituksiin voit niitä luottaa?**

Käytännön esimerkkinä: olet kehittäjä, joka integroi koneoppimismalleja kulujen ennustamiseen. Malli sanoo, että kulujen summa tulee olemaan 4500 euroa plus miinus 300 euroa. Mutta talouspäällikkö haluaa tarkat luvut budjetoinnille. Tämä on ristiriita. Malli voi oppia datasta hyvin — se voi olla 95-prosenttisesti oikein — mutta se ei voi koskaan olla deterministinen. Jos talous tarvitsee täsmällistä, takuuta saamatonta lukua, sinun täytyy rakentaa järjestelmän ympärille kontrollit, jotka ovat deterministisiä: ihmisen hyväksyntä, riskien hallinnan mekanismit, variointiensa rajat. Malli antaa tietoa, mutta päätöstä ei voi delegoida täysin sille.

## Probabilistinen laskenta — miksi tekoäly tuottaa eri vastauksia

Perinteinen ohjelma — esimerkiksi pankkisovellus, joka laskee korkoa tai validoi tilinumeroita — on deterministinen. Kirjoitat säännön: "jos tilinumeron pituus on 14, hyväksy se". Sama tilinumero tuottaa aina saman vastauksen. Järjestelmä ei tee mitään arvioita. Se noudattaa logiikkaa, joka on ihminen kirjoittanut.

Koneoppimismalli on eri asia. Sen sijaan että logiikka olisi kirjoitettu, logiikka on opittu **tilastollisista kuvioista datasta**. Kun malli näkee tuhansia esimerkkejä, se oppii: "Kun näen nämä merkit, seuraava merkki on usein tämä." Se ei tiedä miksi — se on oppinut pelkästään datasta. Se on kuin jos oppinut pelkkää dataparikkorreja tekemään arvauksia, ei todellisen, syvän ymmärryksen perusteella.

Tämän seurauksena malli tuottaa **todennäköisyyksiä**, ei varmuuksia. Kun annat esikäsiteltyä dataa chatbot-mallille ja kysyt sille kysymyksen, malli ei hakee vastausta tietokannasta — se valitsee seuraavan todennäköisimmän merkin. Sitten seuraavan. Ja seuraavan. Kunnes se pääättää lopettaa. Jokainen valinta on paras arvio sen opittujen kuvioiden perusteella, mutta se ei ole logiikkaketju, joka johtuu matemaattisista säännöistä. Se on tilastollinen prosessi.

Tämä selittää monia tekoälyn omituisuuksia, joita näet käytännössä. Miksi saman kysymyksen esittäminen kahdesti antaa hieman erilaisen vastauksen? Koska jokainen mallin "päätös" merkeittäin on probabilistinen. Miksi malli joskus kirjoittaa jotain, joka näyttää älykkäältä, mutta on täysin väärää? Koska se arvaa seuraavaa merkkiä perustuen dataan, jossa se näkyi usein, vaikka konteksti olisi erilainen. Se ei ymmärrine asiaa. Se ennustaa merkkejä tilastollisten kuvioiden perusteella.

**Pysähdy hetkeksi: Jos tekoäly tuottaa todennäköisyyksiä eikä varmuuksia, missä ammattilaiset TVT-tehtävissä käyttävät malleja siten, että epävarmuus on ongelmallinen? Missä se ei olisi ongelma?**

## Tekoälyn rajat — mitä se ei voi tehdä

Tekoäly näyttää tekevän asioita, joita ei voi tehdä. Se näyttää neuvottelevan, tekevän päätöksiä ja ratkovan ongelmia omalla "älykkyydelleen" perustuen. Mutta nämä näkökulmat ovat harhaanjohtavia.

Ensinnäkin tekoäly ei ole yleisäly. Se on valmistettu tiettyyn tehtävään, tietyllä datalla, tietyssä kontekstissa. Kuva-analyysin malli, joka tunnistaa koirat ja kissat, ei osaa lukea teksiä tai kuulla musiikkia. Tekstitaakse opittu malli, joka tuottaa hyviä tarinoita, ei voi diagnoosoida sairauksia tekstin perusteella. Nämä ovat eri "älylliset" osaamisen alueita. Mitä enemmän tietty malli on opittu, sitä parempi se on kyseisessä tehtävässä — mutta mitä kapeampi sen osaamisen alue.

Toiseksi tekoäly ei toimi kausaliteetin perusteella. Se ei ymmärrä syy-seuraussuhteita. Se vain näkee kuvioita. Jos tietokanta osoittaa, että "ihmiset, joiden nimi alkaa J:llä, ostavat usein kirjoja", malli voi oppia tämän kuvion ja ennustaa, että seuraava J:llä alkavalla nimellä oleva ihminen ostaa kirjan. Mutta se ei ymmärrä, että nimen alkukirjain ei ole nimessä mitään erityisesti, joka edistäisi kirjojen ostamista. Se on ollut pelkkä tilastollinen sattuma datassa. Tämä tekee tekoälystä vaarallisen tiettyissä konteksteissa: se voi vahvistaa olemassa olevia harhoja ja tunnistaa väärän syyt-seuraus-linkkejä.

Kolmanneksi tekoäly ei osaa neuvotella tai tehdä todellisia arvopäätöksiä. Se ei ymmärrä oikeutta, etiikkaa tai ihmisen arvoa. Se voi tuottaa tekstiä, joka näyttää neuvottelevalta tai arvokkaalta, koska se on oppinut merkkikuvioita joissa neuvottelu näyttää sille. Mutta kun tekemme päätöksiä, jotka koskevat ihmisen elämää — kuka saa lainaa, kuka värvätään, kenen asuinluvat hyväksytään — emme voi delegoida näitä päätöksiä järjestelmälle, joka näkee vain kuvioita datassa. Nämä päätökset vaativat inhimillistä harkintaa ja vastuunottoa.

Käytännön esimerkkinä: terveydenhuollon yritys käyttää mallia diagnoosien auttamiseen. Malli tuottaa todennäköisyyksiä tiettyjen sairauksien olemassaolosta potilastiedoista. Mutta se ei voi verrata näitä todennäköisyyksiä potilaan elämää säästävien hoitojen riskeihin. Se ei voi päättää, onko "80 prosentin varmuus keuhkosyövästä" tarpeeksi syy invasiiviselle toimenpiteelle. Lääkäri tekee nämä päätökset. Malli on ammattilaiselle työkalu — informaatio — mutta ammattilaisuus on siinä, että ihminen ymmärtää mallin rajat ja pitää vastuun.

## Käsitteen yhteenveto

Tekoäly on järjestelmä, joka tekee päätöksiä ilman eksplisiittisiä ihmisen kirjoittamia sääntöjä. Kun tekoäly rakentuu koneoppimisen varaan, se tuottaa **todennäköisyyksiä tilastollisen datan perusteella**, ei varmuuksia. Tämä tekee siitä ammattilaiselle sopeutetun, kuten muutenkin, mutta vaatii muistaa kolme ratkaisevaa rajaa: tekoäly on kapea-alaista (ei yleisäly), ei ymmärrä syy-seuraus-suhteita (vain kuvioita) ja ei voi kantaa arvopäätösten vastuuta (se on ihmisen tehtävä). ITT-ammattilaisena sinun on ymmärrettävä nämä rajat, jotta tietäisit, mistä kohtaa tarvitaan inhimillistä älyä, kontrolleja ja vastuunottoa.

---

## Seuraavaksi

Oppitunnin lähiosassa käytämme tätä perustietämystä konkreettisiin tapauksiin: analysoidaan todellisia järjestelmiä, jaetaan väärinkäsitykset ja harjoitellaan ammattilaisesti kriittistä ajattelua tekoälyyn liittyen.
