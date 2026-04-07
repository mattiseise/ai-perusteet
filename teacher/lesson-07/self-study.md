# Miksi tekoäly valehtelee? — hallusinaatiot ja satunnaisuus

## Johdanto

Olet juuri antanut ChatGPT:lle saman kysymyksen kaksi kertaa. Kumma juttu — vastaukset olivat erilaiset. Ensimmäisellä kerralla sait selkeän, hyvin organisoidun koodinpätkän. Toisella kerralla sama pyyntö tuotti lähes oikean koodin, mutta funktio kutsuu API:a, jota ei ole olemassa. Mikä homma? Eikö tekoäly olisi deterministinen — kuten perinteinen ohjelma, joka tekee aina saman asian samalla syötteellä?

Vastaus on: ei. Generatiiviset kielimallit eivät ole deterministisiä. Ne ovat todennäköisyyspohjaisia järjestelmiä, jotka toimivat aivan eri tavalla kuin klassinen ohjelmointi. Tämän ymmärtäminen on kriittistä, kun työskentelet AI:n kanssa ammatillisesti.

Tämän tunnin jälkeen sinulla on tuomaripöydällesi seitsemäs todistusaineisto: tekoäly on samanaikaisesti vahva ja epäluotettava — se voi halukkaasti valehdella, koska se ei ymmärrä totuutta.

## Miksi tulokset vaihtelevat: epädeterminismi

Kun ChatGPT tai Claude vastaa kysymykseesi, se ei päätä vastaustaan jotenkin "ajattelemalla". Sen sijaan malli tekee sarjan valintoja: yksi sana kerrallaan. Joka askeleella malli sanoo: "Mikä on todennäköisyys, että seuraava sana on 'koodi'? Mikä on todennäköisyys sanalle 'lohkon'? Mikä on todennäköisyys sanalle 'silmukalle'?"

Sitten malliin sisäänrakennettu mekanismi — parametri, jota kutsutaan lämpötilaksi (temperature) — päättää, kuinka seikkailunhaluinen tai rohkea vastaus on. Matala lämpötila (esim. 0,3) tarkoittaa, että malli valitsee lähes aina todennäköisimmän seuraavan sanan. Korkea lämpötila (esim. 1,5) tarkoittaa, että malli on valmis valitsemaan epätodennäköisiäkin sanoja — tulokset vaihtelevat enemmän.

Tämä ei ole ohjelmointivirhe. Se on rakenteellinen piirre. Korkea lämpötila mahdollistaa luovuuden ja monimuotoisuuden. Matala lämpötila tekee vastauksista johdonmukaisia ja ennustettavia. Ammattilaiselle tämä tarkoittaa sitä, että kun kirjoitat API-dokumentaatiota, haluat alhaisemman lämpötilan (johdonmukaisuus). Kun taas ideoit markkinointikampanjoita, korkeampi lämpötila tuottaa rikkaampia vaihtoehtoja.

> **Pysähdy hetkeksi:** Missä oman työsi tilanteissa tarvitsisit matalaa lämpötilaa (johdonmukaisuus) ja missä korkeampaa (luovuus)?

## Miksi malli hallusinoi: teksti ei ole fakta

Hallusinaatio (hallucination) on tilanne, jossa AI väittää jotain, mikä ei pidä paikkaansa. Ehkä kysyit: "Mikä on Pythonin urllib3-kirjaston oikea syntaksi HTTP-kutsulle?" Malli vastasi uskottavalla esimerkillä — joka käyttää funktiota, jota ei ole olemassa.

Tai kysyit: "Kuka oli Suomen toinen pääministeri?" ja vastaus oli väärä. Hallusinaatio on täydellisen itsevarmaa valestelua.

Miksi näin tapahtuu? Koska kielimallit ovat *todennäköisyyspohjaisia ennustajia, eivät faktakoneita*. Ne oppivat sanasta sanaan, mikä tyypillisesti seuraa jotakin muuta. Kun mallilta kysytään "urllib3 HTTP-kutsu — koodi?", se on oppinut, että tällaisissa konteksteissa seuraa usein koodiesimerkkejä. Siksi se *tuottaa* koodia, joka *näyttää oikealta* — syntaksi on kohtuullinen, logiikka melkein kohdallaan.

Mutta malli ei ole *verifioinut* koodia oikeaa dokumentaatiota vasten. Se vain ennustaa, "miltä oikealta näyttävä koodi näyttää tämänkaltaisissa aiheissa" — se ei tiedä, ovatko vastaukset oikeita. Hallusinaatio syntyy, kun todennäköisyydet johtavat vastaukseen, joka kuulostaa oikealta mutta on väärä.

Tämä on vaarallisinta tekniikan parissa. IT-ammattilaisella on sisäinen "kuulostaa oikealta" -anturi, mutta *se ei aina toimi*. Sinun vastuullasi on aina verifioida kriittiset tiedot itsenäisesti ennen kuin käytät niitä.

> **Pysähdy hetkeksi:** Missä IT:n käyttötapauksissa hallusinaatiot olisivat vaarallisimpia? (Ajattele tuotantokoodia, tietoturvaa, asiakastietoja.)

## Miksi AI ei ole totuuskone

Seuraavaa ei voi painottaa liikaa: **generatiiviset kielimallit eivät ole faktakoneita. Ne ovat sanojen ennustajia.**

Tämä merkitsee kolmea asiaa:

1. **Itsevarmuus ei tarkoita oikeellisuutta.** Hallusinaatio voi kuulostaa täysin luottavaiselta. Malli voi antaa väärän tiedon täsmällisin yksityiskohdin ilman varoitusta epävarmuudesta. Tämä on vaarallista.

2. **Konteksti antaa kuvion, ei faktoja.** Jos kysyt "Mitä Windowsin tasklist-komento tekee?", mallia on opetettu miljoonilla koodiesimerkeillä. Se osaa ennustaa, mitä tämänkaltainen vastaus tyypillisesti sisältää — mutta se ei *tiedä* komponentin tosiasiallista toimintaa.

3. **Ajallinen raja.** Malli on opetettu datalla tiettyyn pisteeseen asti. Viimeaikaiset tapahtumat, API-päivitykset ja uudet kirjastoversiot — kaikki voivat olla alttiita hallusinaatioille.

Ammattilaisena **älä koskaan luota AI:n vastaukseen ilman itsenäistä verifiointia kriittisillä alueilla**. Käytä mallia ideointiin, koodin rungon luomiseen ja dokumentaation vedokseen. Sitten *tarkista, testaa, validoi*.

> **Pysähdy hetkeksi:** Jos annat asiakkaalle raportin, jonka olet luonut AI:n avulla, kenen vastuulla on datan oikeellisuus? Sinun vai mallin?

## Epäluotettavuuden merkkejä käytännössä

Neljä merkkiä siitä, että AI-vastaus saattaa olla hallusinaatio:

- **Liian näyttävä:** Vastaus on hyvin muotoiltu ja yksityiskohtainen, mutta väitteet ovat liian spesifejä eikä niiden tarkistaminen ole nopeaa.
- **Aikaan sopimaton:** Olet kysynyt uusimmasta tekniikasta, mutta mallilla on käytössään vanhentunutta tietoa.
- **Logiikka ei mene yhteen:** Vastaus on johdonmukainen, mutta looginen jatkotarkastelu johtaa ristiriitaan.
- **Kokonaisuuden heikkoudet:** Kun analysoit vastausta osissa, yksittäiset lauseet kuulostavat oikeilta, mutta kokonaisuus sisältää ristiriitoja.

**Paras puolustus: skeptisyys, varsinkin teknisissä asioissa.**

## Yhteenveto

Generatiiviset kielimallit ovat epädeterministisiä ja todennäköisyyspohjaisia. Tämä mahdollistaa luovuuden, mutta merkitsee myös sitä, että ne voivat hallusinoida: tuottaa itsevarmasti väitteitä, jotka eivät pidä paikkaansa. Malli ei ole totuuskone, vaan sanojen ennustaja. Ammattilaisena sinun vastuullasi on ymmärtää nämä rajat, verifioida kriittiset tiedot ja käyttää AI:tä sopivasti — apuvälineenä, ei oraakkelina.

Seuraavalla tunnilla siirryt eettisiin kysymyksiin: kenen datalla tekoäly on opetettu, ja mitä se maksaa?