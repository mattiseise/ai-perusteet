# Oppitunti 18 — Viimeistele ja esittele bottisi ★

## Mitä tällä tunnilla tapahtuu?

Tähän mennessä olet kerännyt kahdeksan tunnin aikana taidot ja kolme **rakennusainetta**. Nyt avaat Microsoft Copilotin ja rakennat niistä toimivan, viimeistellyn botin: oman **apuri-bottisi** juuri sinun valitsemaasi arjen aiheeseen.

Tällä tunnilla et opiskele enää uusia teoreettisia käsitteitä botin rakentamisesta. Sen sijaan opit **yhdistämään** sen, mitä jo osaat. Tämä materiaali auttaa sinua siinä. Se ei kerro lisää tekoälyn teoriasta, vaan ohjaa rakentamaan botin, joka toimii oikeasti ja näyttää huolellisen tekijän kädenjäljen.

## Mikä on hyvä apuri-botti?

Hyvä botti on **ohjaava, ei tekevä**. Se ei tee asiaa käyttäjän puolesta, vaan auttaa käyttäjää onnistumaan paremmin kuin yksin. Käyttäjän osaaminen ja vastuu kasvavat, eivät katoa.

Hyvä botti eroaa yleisestä ChatGPT:stä kolmella tavalla:

1. **Se tietää kontekstin.** Käyttäjän ei tarvitse joka kerta selittää, mistä aiheesta on kyse — esimerkiksi mistä lajista, kerhosta tai oppiaineesta. Botti tietää sen automaattisesti.
2. **Se ohjaa työnkulkua.** Botti tietää, missä järjestyksessä tehtävän vaiheet kannattaa käydä läpi. Käyttäjän ei tarvitse muistaa rakennetta itse.
3. **Sillä on rajat.** Botti tietää, milloin sen pitää sanoa: ”Tämä ei kuulu minulle, kysy oikealta ihmiseltä.” Tämä on huolellisuutta, ei heikkoutta.

## Botin rakenne

Bottisi rakentuu neljästä komponentista. Käytä niitä työvaiheina:

**1. Botin määrittely eli rakennusaine 2.** Päätä, kenelle botti on tarkoitettu, mitä se osaa ja mitä se ei tee. Tämä on botin **perustamisasiakirja**. Ilman sitä botti kasvaa helposti hallitsemattomaksi.

**2. Järjestelmäkehote eli pääohje, rakennusaine 1.** Tämä on tekstipätkä, jonka annat Copilotille ja joka määrittää, miten botti käyttäytyy. Se on botin **DNA**.

**3. Tietopohja eli rakennusaine 3.** Valitse 3–5 dokumenttia, jotka annat botille luettavaksi. Tämä on botin **kirjasto**, josta se ammentaa oman alasi tietoa.

**4. Testaus.** Et tunne bottiasi ennen kuin olet käyttänyt sitä oikealla projekti-idealla. Ensimmäisen testikierroksen jälkeen botti paljastaa yleensä, mitä siinä pitää vielä korjata.

## Järjestelmäkehotteen kieli

Botin **järjestelmäkehote** on tärkein yksittäinen tekstipätkä, jonka kirjoitat tässä projektissa. Se määrittelee botin persoonan, työnkulun ja rajat. Alla on esimerkki kahdesta tasosta.

### Heikko järjestelmäkehote

> Olet ystävällinen tekoälyavustaja, joka auttaa käyttäjiä opiskelussa. Vastaa asiantuntevasti ja kohteliaasti.

**Mikä mättää:** Ohje on liian yleinen. Se ei kerro aihetta, työnkulkua eikä rajoja. Botti voi yhtä hyvin auttaa CV:n kirjoittamisessa kuin matematiikan kertaamisessa. Se ei siis erikoistu mihinkään.

### Vahva järjestelmäkehote

> Olet kärsivällinen kertauskaveri, joka auttaa opiskelijaa valmistautumaan biologian kokeeseen. Et anna valmiita vastauksia, vaan autat käyttäjää oppimaan itse.
>
> Työnkulkusi on aina sama: ohjaat käyttäjää järjestyksessä viiden vaiheen läpi — (1) mitä aihetta kerrataan, (2) mitä käyttäjä jo osaa, (3) käsitteen selittäminen omin sanoin, (4) harjoituskysymykset ja (5) yhteenveto ja seuraava askel. Et siirry seuraavaan vaiheeseen ennen kuin nykyinen on käsitelty riittävän tarkasti.
>
> Et tee tehtäviä käyttäjän puolesta. Kysyt aina tarkentavia kysymyksiä ja autat käyttäjää muotoilemaan vastauksensa omin sanoin. Käytät aiheen omia termejä, etkä vaikeaa jargonia.
>
> Et anna terveys- tai lääketieteellisiä neuvoja etkä arvioi käyttäjän arvosanoja. Jos käyttäjä kysyy näistä, ohjaat hänet opettajan tai oikean asiantuntijan puoleen.

**Mikä toimii:** Rooli on konkreettinen: **kertauskaveri biologian kokeeseen**. Työnkulku on jäsennetty: viisi vaihetta on nimetty. Toimintatapa on selkeä: botti ei tee tehtäviä käyttäjän puolesta. Rajat ovat näkyvissä: botti ei anna terveysneuvoja. Lisäksi botti käyttää aiheen omia termejä. Botti tietää nyt tarkasti, mitä sen pitää tehdä.

## Tietopohjan kuratointi

**Tietopohja** on kokoelma dokumentteja, jotka botti lukee ja joista se ammentaa tietoa. Tietopohjan kuratointi on käytännössä päättelyä: mitä botin pitää tietää, jotta se voi auttaa käyttäjää hyvin?

Kun valitset tietopohjaa, pohdi seuraavia kysymyksiä:

- **Mitä botin pitää tietää?** Esimerkiksi miltä hyvä lopputulos näyttää, mitä yleisiä virheitä aiheessa tehdään ja mitä termejä käytetään.
- **Mistä saat luotettavaa materiaalia?** Hyviä lähteitä ovat esimerkiksi oppikirjat, kurssin omat materiaalit, harrastuksen viralliset säännöt ja oman koulun tai seuran omat ohjeet. Älä perusta tietopohjaa satunnaisiin blogikirjoituksiin.
- **Mikä on liikaa?** 3–5 hyvää dokumenttia on parempi kuin 20 keskinkertaista. Liian suuri määrä materiaalia voi tehdä botin vastauksista sekavia.

**Hyvä tietopohja oman aiheesi botille voi sisältää esimerkiksi:**

- yhden malliesimerkin onnistuneesta lopputuloksesta omasta aiheestasi
- tarkistuslistan tai rakennepohjan, jonka botti voi opettaa käyttäjälle
- listan aiheesi yleisistä virheistä tai sudenkuopista
- termistön ja sanaston, jotta botti käyttää oikeaa kieltä

## Testaus: kun botti on melkein valmis

Et tunne bottiasi ennen kuin olet ajanut sen läpi oikealla käyttötilanteella. **Testivaihe** paljastaa puutteet, joita et huomannut suunnittelussa.

Hyvä testikeskustelu sisältää nämä neljä osaa:

**1. Normaali käyttötapaus.** Anna botille oikea, aiheellesi tyypillinen tilanne. Käy keskustelu loppuun. Pääsetkö lopputulokseen, jota botin on tarkoitus auttaa tekemään?

**2. Epävarma käyttäjä.** Kuvittele aloittelija, joka ei vielä tunne aihetta lainkaan. Auttaako botti silti pääsemään alkuun?

**3. Rajalla oleva kysymys.** Kysy botilta jotakin, mikä on sen alueen ulkopuolella, esimerkiksi: ”Voitko arvioida, mikä lääke minulle sopisi?” Tunnistaako botti rajan ja ohjaako oikein?

**4. Yritys saada botti tekemään työ puolesta.** Pyydä bottia tekemään koko homma suoraan käyttäjän puolesta. Noudattaako se ohjeitaan vai murtuuko rajaus?

Jos jokin näistä epäonnistuu, botti ei ole vielä valmis. Korjaa järjestelmäkehotetta, lisää tietopohjaa tai tarkenna rajauksia. Testaa sen jälkeen uudelleen.

## Yleisimmät sudenkuopat

**1. Liian kiltti botti.**

Jos botti vain vastaa ”hyvä kysymys” ja toistaa käyttäjän sanat, se ei ohjaa. Lisää järjestelmäkehotteeseen velvoite kysyä tarkentavia kysymyksiä, antaa konkreettista palautetta ja ohjata käyttäjää seuraavaan vaiheeseen.

**2. Liian yleinen botti.**

Jos botti kuulostaa samalta riippumatta siitä, onko aiheena salitreeni vai kerhon säännöt, järjestelmäkehotteessa ja tietopohjassa ei ole tarpeeksi aiheesi erikoispiirteitä. Lisää termistöä ja konkreettisia esimerkkejä.

**3. Liian innokas botti.**

Jos botti tekee koko homman käyttäjän puolesta heti ensimmäisellä viestillä, työnkulun ohjaus on jäänyt vajaaksi. Lisää järjestelmäkehotteeseen vaihe vaiheelta etenevä toimintatapa ja kielto tehdä koko tehtävä käyttäjän puolesta.

## Tarkistuslista ennen palautusta

Käy nämä kohdat läpi ennen kuin palautat työn:

- ☐ Botin järjestelmäkehotteessa on selkeä rooli, työnkulku ja rajat.
- ☐ Botti puhuu oman aiheesi kieltä eikä käytä vain yleisiä fraaseja.
- ☐ Tietopohjassa on 3–5 hyvää ja perusteltua dokumenttia.
- ☐ Olen testannut botin vähintään yhdellä oikealla käyttötilanteella loppuun saakka.
- ☐ Botti tunnistaa rajansa eikä mene oman alueensa ulkopuolelle.
- ☐ Olen iteroinut järjestelmäkehotteen vähintään kahdesti. Ensimmäinen versio ei ole vielä lopullinen.
- ☐ Reflektioni kuvaa, mitä opin, ei vain sitä, mitä tein.
- ☐ Bottiin pääsee linkillä, jotta arvioija voi testata sitä itse.
- ☐ Olen ylpeä tästä botista. Se on minun käsialaani.

## Lopuksi

Apuri-botti on **näyttö osaamisestasi**: sekä kurssin sisällöstä että siitä taidosta, jota osio 3 syventää eli tekoälyn rakentamisesta toimimaan itsenäisesti. Et osoita osaamistasi pelkästään sillä, että käytät tekoälyä. Osoitat sen sillä, että **rakennat tekoälyllä** jotain, mitä joku toinen voi käyttää.

Tämä on iso askel käyttäjästä rakentajaksi. Pidä siitä kiinni.

Et opettele vain käyttämään tekoälyä. Opit rakentamaan sillä.

---
