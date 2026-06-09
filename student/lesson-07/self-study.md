# Miksi tekoäly valehtelee? — hallusinaatiot ja satunnaisuus

## Johdanto

Olet juuri antanut ChatGPT:lle saman kysymyksen kaksi kertaa. Huomaat kuitenkin jotain outoa: vastaukset ovat erilaiset. Ensimmäisellä kerralla sait selkeän ja hyvin jäsennellyn koodinpätkän. Toisella kerralla sama pyyntö tuotti lähes oikean koodin, mutta funktio kutsuikin API:a, jota ei ole olemassa. Mistä tämä johtuu? Eikö tekoälyn pitäisi olla **deterministinen**, kuten perinteinen ohjelma, joka tuottaa aina samalla syötteellä saman tuloksen?

Vastaus on: ei. **Generatiiviset kielimallit** eivät ole samalla tavalla deterministisiä kuin perinteiset ohjelmat. Ne ovat **todennäköisyyspohjaisia järjestelmiä**, jotka toimivat eri tavalla kuin klassinen ohjelmointi. Tämän ymmärtäminen on tärkeää, kun työskentelet tekoälyn kanssa ammatillisesti.

Tämän tunnin jälkeen sinulla on seitsemäs todistusaineisto omaan arviointipöytääsi: tekoäly voi olla yhtä aikaa vahva ja epäluotettava. Se voi tuottaa hyödyllisiä vastauksia, mutta se voi myös väittää itsevarmasti asioita, jotka eivät pidä paikkaansa, koska se ei ymmärrä totuutta samalla tavalla kuin ihminen.

## Miksi tulokset vaihtelevat: epädeterminismi

Kun ChatGPT tai Claude vastaa kysymykseesi, se ei muodosta vastausta samalla tavalla kuin ihminen, joka pohtii asiaa tietoisesti. Sen sijaan malli tekee sarjan valintoja yksi sana tai tekstin osa kerrallaan. Jokaisessa vaiheessa malli arvioi, mikä seuraava sana tai merkkiyhdistelmä on todennäköisin aiemman tekstin perusteella.

Malli voi esimerkiksi arvioida: ”Mikä on todennäköisyys, että seuraava sana on *koodi*? Entä *lohko*? Entä *silmukka*?” Näiden todennäköisyyksien perusteella se valitsee seuraavan osan vastauksesta.

Tähän liittyy usein parametri nimeltä **lämpötila** eli *temperature*. Se vaikuttaa siihen, kuinka ennustettava tai vaihteleva vastaus on. **Matala lämpötila**, esimerkiksi 0,3, ohjaa mallia valitsemaan todennäköisimpiä vaihtoehtoja. Tällöin vastaukset ovat yleensä johdonmukaisempia ja ennustettavampia. **Korkea lämpötila**, esimerkiksi 1,5, sallii epätodennäköisempien vaihtoehtojen valitsemisen. Tällöin vastaukset voivat olla luovempia, mutta myös vaihtelevampia ja epävarmempia.

Tämä ei ole ohjelmointivirhe, vaan mallin rakenteellinen ominaisuus. Korkea lämpötila mahdollistaa luovuuden ja monimuotoisuuden. Matala lämpötila taas lisää johdonmukaisuutta ja ennustettavuutta. Ammattilaiselle tämä tarkoittaa, että esimerkiksi API-dokumentaatiota kirjoittaessa kannattaa suosia johdonmukaisuutta. Ideointivaiheessa, kuten markkinointikampanjan vaihtoehtoja suunniteltaessa, vaihtelevuus voi puolestaan olla hyödyllistä.

> **Pysähdy hetkeksi:** Missä oman työsi tilanteissa tarvitsisit matalaa lämpötilaa eli johdonmukaisuutta? Entä missä tilanteissa korkeampi lämpötila eli luovempi ja vaihtelevampi vastaus voisi olla hyödyllinen?

## Miksi malli hallusinoi: teksti ei ole sama asia kuin fakta

**Hallusinaatio** tarkoittaa tilannetta, jossa tekoäly väittää jotain, mikä ei pidä paikkaansa. Saatat esimerkiksi kysyä: ”Mikä on Pythonin urllib3-kirjaston oikea syntaksi HTTP-kutsulle?” Malli voi vastata uskottavalla koodiesimerkillä, joka näyttää oikealta mutta käyttää funktiota, jota ei todellisuudessa ole olemassa.

Toinen esimerkki: kysyt ”Kuka oli Suomen toinen pääministeri?” ja saat vastauksen, joka kuulostaa varmalta mutta on väärä. Hallusinaatio voi siis olla täysin itsevarmalta vaikuttava virheellinen väite.

Miksi näin tapahtuu? Koska kielimallit ovat **todennäköisyyspohjaisia ennustajia**, eivät faktakoneita. Ne oppivat, millaiset sanat, rakenteet ja sisällöt tyypillisesti seuraavat toisiaan. Kun mallilta kysytään esimerkiksi urllib3-kirjaston HTTP-kutsusta, se on oppinut, että tällaisissa yhteyksissä seuraa usein koodiesimerkkejä. Siksi se tuottaa koodia, joka näyttää uskottavalta.

Ongelma on siinä, että malli ei välttämättä ole tarkistanut vastausta oikeaa dokumentaatiota vasten. Se ennustaa, millainen oikealta näyttävä vastaus sopisi tilanteeseen. Se ei automaattisesti tiedä, ovatko kaikki yksityiskohdat oikein. **Hallusinaatio** syntyy, kun todennäköinen ja uskottavalta kuulostava vastaus onkin virheellinen.

Tämä on erityisen vaarallista tekniikan parissa. IT-ammattilaisella voi olla hyvä ”kuulostaa oikealta” -tuntuma, mutta se ei aina riitä. Kriittiset tiedot täytyy aina **verifioida** eli tarkistaa luotettavasta lähteestä ennen käyttöä.

> **Pysähdy hetkeksi:** Missä IT:n käyttötapauksissa hallusinaatiot olisivat vaarallisimpia? Ajattele esimerkiksi tuotantokoodia, tietoturvaa ja asiakastietoja.

## Miksi tekoäly ei ole totuuskone?

Seuraavaa asiaa ei voi korostaa liikaa: **generatiiviset kielimallit eivät ole faktakoneita, vaan sanojen ja tekstirakenteiden ennustajia.**

Tämä tarkoittaa kolmea tärkeää asiaa:

1. **Itsevarmuus ei tarkoita oikeellisuutta.** Hallusinaatio voi kuulostaa täysin varmalta. Malli voi antaa väärän tiedon täsmällisin yksityiskohdin eikä välttämättä varoita epävarmuudesta. Tämä tekee virheistä erityisen vaarallisia.
2. **Konteksti antaa mallille kuvion, ei varmaa tietoa.** Jos kysyt: ”Mitä Windowsin tasklist-komento tekee?”, malli hyödyntää koulutusdatassa oppimiaan malleja ja esimerkkejä. Se osaa ennustaa, mitä tällainen vastaus yleensä sisältää, mutta vastaus on silti tarkistettava, jos sitä käytetään kriittisessä työssä.
3. **Mallilla voi olla ajallinen raja.** Malli on opetettu aineistolla, joka ulottuu vain tiettyyn ajankohtaan asti. Uudet tapahtumat, API-päivitykset, kirjastoversiot ja dokumentaatiomuutokset voivat siksi olla erityisen alttiita virheille.

Ammattilaisena sinun ei pidä koskaan luottaa tekoälyn vastaukseen ilman itsenäistä tarkistusta kriittisissä asioissa. Käytä mallia ideointiin, koodin rungon luomiseen, vaihtoehtojen vertailuun ja dokumentaation luonnosteluun. Sen jälkeen **tarkista, testaa ja validoi**.

> **Pysähdy hetkeksi:** Jos annat asiakkaalle raportin, jonka olet luonut tekoälyn avulla, kenen vastuulla datan oikeellisuus on: sinun vai mallin?

## Epäluotettavuuden merkkejä käytännössä

Seuraavat merkit voivat kertoa, että tekoälyn vastaus saattaa sisältää hallusinaatioita:

- **Vastaus on liian näyttävä:** se on hyvin muotoiltu ja yksityiskohtainen, mutta väitteet ovat hyvin tarkkoja eikä niiden paikkansapitävyyttä ole helppo tarkistaa.
- **Vastaus ei sovi ajankohtaan:** kysyt uusimmasta tekniikasta, mutta mallilla voi olla vanhentunutta tietoa.
- **Logiikka ei kestä tarkastelua:** vastaus vaikuttaa aluksi johdonmukaiselta, mutta tarkempi pohdinta paljastaa ristiriidan.
- **Kokonaisuus sisältää heikkouksia:** yksittäiset lauseet kuulostavat oikeilta, mutta vastaus kokonaisuutena on ristiriitainen tai epäselvä.

**Paras puolustus on terve skeptisyys, erityisesti teknisissä ja kriittisissä asioissa.**

## Yhteenveto

**Generatiiviset kielimallit** ovat epädeterministisiä ja todennäköisyyspohjaisia. Tämä mahdollistaa luovuuden ja monipuoliset vastaukset, mutta tarkoittaa myös sitä, että mallit voivat **hallusinoida**: ne voivat tuottaa itsevarmasti väitteitä, jotka eivät pidä paikkaansa.

Malli ei ole totuuskone, vaan tekstin ennustaja. Ammattilaisena sinun vastuullasi on ymmärtää nämä rajat, tarkistaa kriittiset tiedot ja käyttää tekoälyä oikealla tavalla: apuvälineenä, ei erehtymättömänä auktoriteettina.

Seuraavalla tunnilla siirryt eettisiin kysymyksiin: kenen datalla tekoäly on opetettu, ja mitä se maksaa?

---
