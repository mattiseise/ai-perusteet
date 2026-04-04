# Gen AI:n luonne: epädeterminismi, hallusinaatiot ja rajat

## Johdanto

Olet juuri antanut ChatGPT:lle saman kysymyksen kaksi kertaa. Kumma — vastaukset olivat eri. Ensimmäisellä kerralla sait selvän, hyvin organisoidun koodinpätkän. Toisella kerralla sama pyyntö tuotti lähes oikean koodin, mutta funktio kutsuu API:a, jota ei ole olemassa. Mikä homma? Eikö tekoäly olisi deterministinen — kuten perinteinen ohjelma, joka tekee aina saman asian samalla syötteellä?

Vastaus on: Ei. Generatiiviset kielimallit eivät ole deterministisiä. Ne ovat todennäköisyyspohjaisia järjestelmiä, jotka toimivat aivan eri tavalla kuin klassinen ohjelmointi. Ymmärtäminen tämän asiasta on kriittistä, kun työskentelet AI:n kanssa ammatillisesti.

## Miksi tulokset vaihtelevat: epädeterminismi

Kun ChatGPT tai Claude vastaa kysymykseesi, se ei päätä vastaustaan jotenkin "ajattelemalla". Sen sijaan malli tekee valintasarjan: seuraava sana kerrallaan. Joka askeleella malli sanoo: "Mikä on todennäköisyys, että seuraava sana on 'koodi'? Mikä on todennäköisyys 'lohkon' sanalle? Mikä on todennäköisyys 'silmukalle'?"

Sitten malliin sisäänrakennettu mekanismi — parametri, jota kutsutaan lämpötilaksi (temperature) — päättää, kuinka "seikkailu" vastaus on. Matala lämpötila (esim. 0,3) tarkoittaa, että malli valitsee lähes aina todennäköisimmän seuraavan sanan. Korkea lämpötila (esim. 1,5) tarkoittaa, että malli on valmis valitsemaan epätodennäköisiäkin sanoja — tulokset vaihtelevat enemmän.

Tämä ei ole ohjelmointivirhe. Se on rakentava piirre. Korkea lämpötila mahdollistaa luovuutta ja monimuotoisuutta. Matala lämpötila tekee vastauksista johdonmukaisia ja ennustettavia. Ammattilaiselle: kun kirjoitat API-dokumentaatiota, haluat alhaisempaa lämpötilaa (johdonmukaisuus). Kun ideoit markkinointikampanjoita, korkeampi lämpötila tuottaa rikkaampia vaihtoehtoja.

> **Pysähdy hetkeksi:** Mitkä ammattityösi tilanteet vaatisivat matalan lämpötilan (johdonmukaisuus) ja mitkä korkeampaa (luovuus)?

## Miksi malli hallusinoi: teksti ei ole fakta

Hallusinaatio (hallucination) on hetki, kun AI väittää jotain, mikä ei pidä paikkaansa. Ehkä kysyit: "Mikä on Pythonin urllib3-kirjaston oikea syntaksi HTTP-kutsulle?" Malli vastasi näyttävällä esimerkillä — joka käyttää funktiota, jota ei ole olemassa.

Tai: "Kuka oli Suomen toinen pääministeri?" ja vastaus oli väärä. Hallusinaatio on täydellisen itsevarmaa valestelua.

Miksi näin tapahtuu? Koska kielimallit ovat *todennäköisyyspohjaiset ennustajat, eivät faktakoneita*. Ne oppivat sanasta sanaan: mikä tyypillisesti seuraa jotakin muuta. Kun mallia kysytään "urllib3 HTTP-kutsu — koodi?", se on oppinut, että tällaisissa konteksteissa seuraa usein koodiesimerkkejä. Joten se *tuottaa* koodia, joka *näyttää oikealta* — syntaksi kohtuullinen, logiikka kohta.

Mutta malli ei ole *verifioinut* koodia oikeaa dokumentaatiota vasten. Se vain ennustaa "mitä näyttävät koodit näyttävät tämänkaltaisilla aiheilla." Hallusinaatio syntyy, kun todennäköisyydet johtavat vastaukseen, joka kuulostaa oikealta mutta on väärä.

Tämä on vaarallisinta tekniikan kanssa. IT-ammattilaisella on sisäinen "kuulostaa oikealta" -anturi, mutta *se ei aina toimi*. Sinun vastuulla on aina verifioidaan kriittiset tiedot itsenäisesti.

> **Pysähdy hetkeksi:** Missä IT-käyttötapauksissa hallusinaatiot olisivat vaarallisimpia? (Ajattele tuotantokoodia, tietoturvaa, asiakastietoja.)

## Miksi AI ei ole totuuskone

Seuraavaa ei voi painottaa liikaa: **generatiiviset kielimallit eivät ole faktakoneita. Ne ovat sanojen ennustajia.**

Tämä merkitsee kolme asiaa:

1. **Itsevarmuus ei tarkoita oikeellisuutta.** Hallusinaatio voi kuulostaa täydellisen luottavaiselta. Malli voi antaa väärän tiedon täsmällisin yksityiskohdin, ilman varoitusta epävarmuudesta. Tämä on vaarallista.

2. **Konteksti antaa kuvion, ei faktoja.** Jos kysyt "Mitä Windowsin taskkilleri-komento tekee?", mallia opetettiin miljoonista koodista. Se osaa ennustaa, mitä tämänkaltainen vastaus tyypillisesti sisältää — mutta se ei *tiedä* komponentin tosiasiallista toimintaa.

3. **Ajallinen raja.** Malli on opetettu datalla tiettyyn pisteeseen asti. Viimeaikaiset tapahtumat, API:n päivitykset, uudet kirjastoversiot — kaikki voi olla hallusinaation alttis.

Ammattilaisena **älä koskaan luota AI:n vastaukseen ilman itsenäistä verifiointia kriittisillä alueilla**. Käytä mallia ideointiin, koodin rungon luomiseen, dokumentaation vedokseen. Sitten *tarkista, testiä, validoi.*

> **Pysähdy hetkeksi:** Jos annat asiakkaalle raportin, jonka olet luonut AI:n avulla, kenen vastuulla on datan oikeellisuus? Sinä vai malli?

## Epäluotettavuuden merkkejä käytännössä

Neljä opastetta siitä, että AI-vastaus saattaa olla hallusinaatio:

- **Liian näyttävä:** Vastaus on hyvin muodostettu, mutta sisältää erityisen yksityiskohtaisia väittämiä, joita et voi nopeasti kääntää lähdelähteiksi.
- **Sopeutumaton aika:** Olet kysynyt uusimmasta tekniikasta, mutta mallissa on käytössään vanha tieto.
- **Logiikka ei mene yhteen:** Vastaus on johdonmukainen, mutta looginen seuranta johtaa ristiriitaan.
- **Kasvu-heikkoudet:** Kun analysoit osissa, yksittäiset lauseet kuulostaa oikealta, mutta kokonaisuus ei.

**Paras puolustus: skeptisyys varsinkin tekniikoissa.**

## Yhteenveto

Generatiiviset kielimallit ovat epädeterminisiä ja todennäköisyyspohjaisia. Tämä mahdollistaa luovuutta, mutta merkitsee myös, että ne voivat hallusinoida: tuottaa itsevarmuudella faktoja, jotka eivät pidä paikkaansa. Malli ei ole totuuskone, vaan sanojen ennustaja. Ammattilaisena sinun vastuulla on ymmärtää nämä rajat, verifioinaa kriittinen tieto ja käyttää AI:tä sopivasti — apuvälineenä, ei oraakkelina.
