# Projektidokumenttibotti — suunnittele ja aloita rakentaminen

## Johdanto: Miksi projektisuunnitelma on tärkeä (ja usein tylsä)

Olet varmaasti kuullut projektisuunnittelusta. Se kuulostaa tylsältä, koska usein onkin. Istuu kokouksissa, täyttää lomakkeita, kirjoittelee dokumentteja — se vie aikaa ja tuntuu hidastelulta siihen verrattuna, että voisi vain aloittaa tekemisen. Mutta tässä on salaisuus: projektin epäonnistuminen johtuu melkein aina huonosta suunnittelusta, ei huonosta tekemisestä. Kun aloitat ilman selvää suunnitelmaa, päädyt korjaamaan vääriä asioita, tekemään turhaa työtä, tai löydät loppusuoralla, että et ymmärtänyt, mitä asiakkaat halusivat. Se maksaa enemmän aikaa ja rahaa kuin suunnittelu koskaan maksaisi.

Siitä huolimatta suunnittelu on usein hankalaa tehdä käsin. Sinulla on idea projektista, mutta mitä kysymyksiä pitäisi kysyä? Mitä dokumentointiin pitäisi sisältyä? Kuinka saada oikeat tiedot oikeassa muodossa? Kun tekisit sen yksin, voisit unohtaa kriittisen kysymyksen tai jättää jonkin oleellisen asian huomiotta. Tässä tekoäly voi auttaa — ei tekemään päätöksiä puolestasi, vaan ohjaamaan sinua oikeihin kysymyksiin ja kokoamalla vastaukset järjestelmälliseksi suunnitelmaksi.

## Miten botti voi auttaa: aktiivinen suunnittelu

Kuvittele tätä: kirjoitat botille pelkän projektoidean — esimerkiksi "rakennan web-sovelluksen joka auttaa opiskelijoita löytämään lentoja halvemmalla". Botti ei kuitenkaan vain kuittaa sitä. Sen sijaan se alkaa esittää kysymyksiä, yksi kerrallaan, joita todella tarvitset vastattavaksi.

"Kuka on sinun käyttäjä? Miten sovellusta käytetään? Kuinka kauan projekti kestää? Kuka muut tekevät sen kanssa? Millä rahalla rakennetaan? Mitkä ovat suurimmat riskit?"

Kun vastaat näihin, botti kokoaa vastaukset yhtenäiseksi projektisuunnitelmaksi, joka on selkeä ja valmis käyttöön. Se on kuin henkilökohtainen projektin mentor, joka tietää, mitä kysyä.

Tämä botti on kaksitahoinen: se on vuorovaikutuksellinen ja systemaattinen. Se tekee suunnittelusta luonnollisempaa ja vähemmän byrokraattista.

## Mitä hyvä projektisuunnitelma sisältää

Ennen kuin suunnittelet bottia, sinun pitää tietää, mitä suunnitelma sisältää. Yksinkertaisella tasolla projektisuunnitelma vastaa viiteen avaisskysymykseen.

**Mitä** tehdään — projektin kuvaus, mitä tuotetta tai palvelua rakennetaan. Esimerkiksi: "Web-sovellus lentoja hakeville opiskelijoille."

**Kenelle** tehdään — keitä ovat käyttäjät tai asiakkaat. Esimerkiksi: "Opiskelijat, jotka matkustavat usein ja etsivät halvempia vaihtoehtoja."

**Miksi** tehdään — tarkoitus, miksi projekti on olemassa. Esimerkiksi: "Opiskelijat käyttävät liian paljon rahaa lentolippuihin, haluamme ratkaista ongelman."

**Milloin** tehdään — aikataulu ja vaiheet. Esimerkiksi: "Alustava versio 3 kuukaudessa, täysi versio 6 kuukaudessa."

**Miten** ja **millä** tehdään — resurssit, tiimi, tekniikka. Esimerkiksi: "3 kehittäjää, 1 designer, Python ja React, 50 000 euron budjetti."

Nämä viisi osaa muodostavat rungon. Yksinkertainen botti voi opastaa näiden kautta ja koota vastaukset dokumentiksi, jonka voit antaa tiimille tai asiakkaalle.

## System promptin suunnittelu: miten ohjeistat bottia kysyä

System prompti on botin sydän. Se kertoo, mitä botti on, mitä se tekee ja miten se käyttäytyy. Projektidokumenttibotille se näyttäisi suunnilleen tältä:

Botti on **projektin mentor**, joka tietää, miten rakentaa selkeitä suunnitelmia. Sen **tarkoitus** on kyselemällä kerätä tiedot projektista ja koota ne selkeäksi dokumentiksi. Sen **ohjeet** ovat: kysy yksi kysymys kerrallaan, kuuntele vastaus, pyydä tarkennusta jos tarpeellista, ja kun riittävästi tietoa on kerätty, koota se suunnitelmaksi.

Tässä on konkreettinen esimerkki:

> Olet projektin mentor. Sinulla on 10 vuoden kokemus projektinjohdosta, ja tiedät, miten rakentaa selkeitä projektisuunnitelmia.
>
> Tarkoituksesi: Auttaa käyttäjää luomaan projektisuunnitelman esittämällä järjestelmällisiä kysymyksiä, kuuntelemalla vastauksia ja kokoamalla ne selkeäksi dokumentiksi.
>
> Ohjeet:
> 1. Aloita pyytämällä lyhyt projektikuvaus (2-3 lausetta).
> 2. Kysy sitten seuraavaksi: mitä ovat käyttäjät/asiakkaat? Kuuntele huolellisesti.
> 3. Jatka samalla tavalla: miksi projekti on olemassa? Milloin se valmistuu? Mitkä ovat resurssit?
> 4. Kun olet kerännyt kaikki viisi osaa (mitä, kenelle, miksi, milloin, miten), koota ne selkeäksi dokumentiksi.
> 5. Kysy käyttäjältä, mitä muutetaan tai parannetaan ennen viimeistelyä.
>
> Rajaukset:
> - Vastaa vain projekteihin liittyviin kysymyksiin. Jos käyttäjä kysyy muusta, ohjaa hänet takaisin suunnitteluun.
> - Älä tee päätöksiä käyttäjän puolesta. Kysy aina, jos olet epävarma.
> - Jos käyttäjä haluaa lopettaa puolessa välissä, tallenna osittainen suunnitelma ja tarjoa jatkamista myöhemmin.

Näetkö eron? Tämä ei ole vain "kysy kysymyksiä". Tämä on **tarkka ohjeistus** siitä, missä järjestyksessä kysyä, miten kuunnella ja miten koota lopputulos.

## Vinkkejä: miten botti tunnistaa, milloin tietoa on tarpeeksi

Yksi haaste on se, että botti ei voi tietää etukäteen, kuinka yksityiskohtainen käyttäjä haluaa suunnitelmaa. Jotkut haluavat pikaisen yleiskatsauksen, toiset haluavat syvällisen 20 sivun dokumentin. Kuinka botti tietää, milloin lopettaa kysymään?

Hyvin kirjoitettu botti ei lopeta, heti kun saa vastaukset viiteen perusiosioon. Sen sijaan se kysyy: "Haluatko lisää yksityiskohtia? Onko jokin osa, joka vaatii syventämistä?" Käyttäjä voi sanoa kyllä tai ei. Jos käyttäjä sanoo "ei", botti tietää, että voi koota suunnitelman. Jos käyttäjä sanoo "kyllä", botti pyytää tarkennusta.

Toinen tärkeä vihje: botti tekee **muistiinpanoja** samalla kun kysyy. Se ei kysy samaa asiaa kahdesti. Se ei unohda, mitä käyttäjä oli aiemmin sanonut. Jos käyttäjä sanoi "meillä on 3 kehittäjää", botti muistaa sen ja ei kysy uudelleen. Se tekee keskustelusta tehokkaan, ei pitkästyttävää.

## Konkreettinen esimerkki: ajattelun kulku

Otetaan konkreettinen esimerkki. Käyttäjä aloittaa tällä:

"Rakennan sovelluksen, joka auttaa nuoria budjetoinnissa."

Botti vastaa:

"Kiinnostava idea! Apua nuorille budjetoinnissa on tarpeellista. Laitetaan rakenne päälle. Ensin: ketkä ovat nämä nuoret? Mitä ikää, sijainti, onko heillä omaa rahaa vai vanhempien rahaa? Kuka on oikeasti käyttäjä?"

Käyttäjä vastaa:

"Nuoret 16–25-vuotiaat, pääosin Suomessa, omat pienemmät tulot, harjoittelijat ja opiskelijat."

Botti muistaa tämän ja kysyy seuraavaksi:

"Hyvä. Nyt: miksi tämä projekti on sinulle tärkeä? Oletko kohdannut tämän ongelman itse? Vai ratkaiseeko tämä jonkin markkinapaikan?"

Ja niin se jatkuu. Lopuksi, kun botti on kerännyt kaikki viisi osaa, se kokoaa:

**Projektisuunnitelma:**
- **Tuote:** Budjettisovellus nuorille
- **Käyttäjät:** 16–25-vuotiaat opiskelijat ja harjoittelijat Suomessa
- **Tarkoitus:** Auttaa nuoria hallitsemaan rahaa paremmin
- **Aikataulu:** Alfa-versio 2 kuukaudessa, beeta 4 kuukaudessa
- **Resurssit:** 2 kehittäjää, 1 designer, 15 000 euron budjetti

Tämä on hyödyllinen dokumentti, jonka voi antaa investoijille, tiimille tai asiakkaalle.

## Miksi tämä botti on tärkeä

Saattat ihmetellä: miksi teemme tätä bottia juuri nyt? Vastaus on tulevaisuus. Seuraavalla lähiviikoilla (oppitunneissa 19–27) rakennamme paljon monimutkaisempaa agenttia, joka tekee itsenäisiä päätöksiä ja suorittaa tehtäviä. Agentti on yksinkertaisesti botti, joka voi tehdä enemmän. Mutta tämä botti — projektidokumenttibotti — on se pohja, jonka avulla se oppii kommunikoimaan tilanteissa. Se opettaa, miten esittää hyviä kysymyksiä, kuunnella vastauksia ja prosessoida informaatiota systemaattisesti. Kun agentti rakentaa tulevaisuudessa projekteja, se tietää jo, miten tehdä se oikein.

Tämä oppitunti on ensiaskel. Seuraavalla kerralla (oppitunti 18) viimeistelette botin ja esittelette sen. Mutta nyt rakennatte perustan ja testatte, että se toimii.

## Yhteenveto

Hyödyllinen projektidokumenttibotti kysyy oikeat kysymykset, muistaa vastaukset ja kokoaa ne suunnitelmaksi. Sen system prompti kertoo, mikä botti on, mitä se tekee ja miten se käyttäytyy. Kun suunnittelet bottia, mieti ensin: mitkä ovat ne viisi perusosiota (mitä, kenelle, miksi, milloin, miten)? Sitten kirjoita ohjeistus, joka ohjaa botin kysymään näistä järjestelmällisesti. Testaa, että se toimii. Korjaa, mitä ei toimi. Seuraavaksi: rakenna ja viimeistele.
