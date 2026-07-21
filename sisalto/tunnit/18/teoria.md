# Oppitunti 18 — Viimeistele ja esittele bottisi ★

## Mitä tällä tunnilla tapahtuu?

Tähän mennessä olet kerännyt kolme **rakennuspalikkaa**, tehnyt toteutuspäätöksen ja tuottanut ensimmäisen version. Nyt viimeistelet apuri-botin teknisen toteutuksen tai dokumentoidun suunnittelupaketin. Polut ovat samanarvoisia, mutta niitä arvioidaan osittain eri näytöillä: tekninen polku osoittaa todellista toimintaa, kun taas suunnittelupolku osoittaa arkkitehtuuria, simuloitua suoritusjälkeä, testejä ja tunnistettuja rajoituksia.

Suunnittelupolku ei ole vähemmän vaativa teknisen polun luonnos. Sen pitää olla niin täsmällinen, että toinen ihminen ymmärtää, miten ratkaisu voitaisiin toteuttaa ja testata. Samalla siinä sanotaan rehellisesti, mitä ei ole toteutettu. Simuloitu suoritusjälki ei todista integraation, käyttöoikeuden, tilan säilymisen tai lokituksen toimivan oikeassa järjestelmässä.

Tällä tunnilla et opiskele enää uusia teoreettisia käsitteitä botin rakentamisesta. Sen sijaan opit **yhdistämään** sen, mitä jo osaat. Tämä materiaali auttaa sinua siinä. Se ei kerro lisää tekoälyn teoriasta, vaan ohjaa viimeistelemään teknisen botin tai toteutuskelpoisen suunnittelupaketin, jossa näkyy huolellisen tekijän kädenjälki.

## Mikä on hyvä apuri-botti?

Hyvä botti on **ohjaava, ei tekevä**. Se ei tee asiaa käyttäjän puolesta, vaan auttaa käyttäjää onnistumaan paremmin kuin yksin. Käyttäjän osaaminen ja vastuu kasvavat, eivät katoa.

Hyvä apuri-botti eroaa yleisestä keskustelupalvelusta kolmella tavalla:

1. **Se tietää kontekstin.** Käyttäjän ei tarvitse joka kerta selittää, mistä aiheesta on kyse — esimerkiksi mistä lajista, kerhosta tai oppiaineesta. Botti tietää sen automaattisesti.
2. **Se ohjaa työnkulkua.** Botti tietää, missä järjestyksessä tehtävän vaiheet kannattaa käydä läpi. Käyttäjän ei tarvitse muistaa rakennetta itse.
3. **Sillä on rajat.** Botti tietää, milloin sen pitää sanoa: ”Tämä ei kuulu minulle, kysy oikealta ihmiseltä.” Tämä on huolellisuutta, ei heikkoutta.

## Kolme rakennuspalikkaa ja toteutusohje

Bottiprojekti perustuu kolmeen aiemmin tehtyyn rakennuspalikkaan: **Promptikorttiin**, **botin määrittelyyn** sekä **tietopohjaan ja testisuunnitelmaan**. Järjestelmäprompti ei ole neljäs rakennuspalikka, vaan näistä päätöksistä koottu toteutusohje botille.

Promptikortti antaa aiemmin testatun tavan muotoilla ohje. Botin määrittely kertoo käyttäjän, tehtävän, onnistumisen ehdot ja rajat. Tietopohja ja testisuunnitelma sisältävät 2–4 huolella valittua lähdettä sekä kolme testiä, joiden odotukset kirjoitettiin ennen ensimmäistä ajoa.

## Järjestelmäpromptin kieli

Botin **järjestelmäprompti** on tärkein yksittäinen tekstipätkä, jonka kirjoitat tässä projektissa. Se määrittelee botin persoonan, työnkulun ja rajat. Alla on esimerkki kahdesta tasosta.

### Heikko järjestelmäprompti

> Olet ystävällinen tekoälyavustaja, joka auttaa käyttäjiä opiskelussa. Vastaa asiantuntevasti ja kohteliaasti.

**Mikä tekstissä on ongelmana:** Ohje on liian yleinen. Se ei kerro aihetta, työnkulkua eikä rajoja. Botti voi yhtä hyvin auttaa CV:n kirjoittamisessa kuin matematiikan kertaamisessa. Se ei siis erikoistu mihinkään.

### Vahva järjestelmäprompti

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

Aloita siitä, mitä botin pitää tietää voidakseen auttaa. Useimmiten se tarkoittaa kolmea asiaa: miltä hyvä lopputulos aiheessasi näyttää, mitä virheitä siinä tyypillisesti tehdään ja mitä termejä alalla käytetään. Näillä botti pystyy sekä ohjaamaan oikeaan suuntaan että tunnistamaan, milloin käyttäjä on menossa metsään.

Materiaalin luotettavuus ratkaisee lopputuloksen laadun. Oppikirjat, kurssin omat materiaalit, lajin viralliset säännöt ja oman oppilaitoksen tai seuran ohjeet ovat hyviä lähteitä, koska joku on vastuussa niiden sisällöstä. Satunnaiselle blogikirjoitukselle ei ole tällaista vastuuta, eikä botti osaa erottaa hyvää blogia huonosta.

Määrä kannattaa pitää kurissa. Kahdesta neljään huolella valittua dokumenttia on parempi kuin kaksikymmentä keskinkertaista: mitä enemmän aineistoa on, sitä todennäköisemmin botti löytää sieltä osumia, jotka eivät liity kysymykseen — ja sitä sekavampia vastauksista tulee.

**Hyvä tietopohja oman aiheesi botille voi sisältää esimerkiksi:**

- yhden malliesimerkin onnistuneesta lopputuloksesta omasta aiheestasi
- tarkistuslistan tai rakennepohjan, jonka botti voi opettaa käyttäjälle
- listan aiheesi yleisistä virheistä tai sudenkuopista
- termistön ja sanaston, jotta botti käyttää oikeaa kieltä

## Testaus: kolme testityyppiä, korjaus ja uudelleentesti

Tunnilla 17 ajoit tai simuloit kaikki kolme ennalta kirjoitettua testiä ensimmäisen kerran. Tällä tunnilla valitset korjauslistalta yhden puutteen, teet siihen yhden nimetyn korjauksen ja toistat juuri sitä koskevan testin. Teknisen botin toiminta näkyy oikean toteutuksen ajossa. Suunnittelupolulla sama ketju kuvataan simuloituna suoritusjälkenä, mutta simulaatio ei todista teknisen yhteyden toimivuutta.

Arvioitava testimatriisi sisältää vähintään kolme tapausta ja odotetun tuloksen jokaiselle:

**1. Normaali käyttötapaus.** Anna botille aiheelle tyypillinen tilanne. Käy keskustelu loppuun ja vertaa tulosta etukäteen kirjoittamaasi odotukseen.

**2. Kielteinen testi.** Pyydä jotakin, mitä botti ei saa tehdä, kuten alueen ulkopuolinen tai liian riskialtis tehtävä. Tarkista, noudattaako se rajausta ja eskaloiko oikein.

**3. Reunatapaus.** Anna epäselvä, puutteellinen tai ristiriitainen syöte. Tarkista, kysyykö botti tarpeellisen tarkennuksen eikä arvaa.

Säilytä tunnin 17 kolmesta testistä syöte, odotus, toteutunut tai simuloitu tulos ja johtopäätös. Dokumentoi tunnilla 18 yhden valitun puutteen korjaus ja sitä koskeva uudelleentesti. Ennen–jälkeen-vertailu **antaa näyttöä korjauksen vaikutuksesta tässä testissä**. Se ei osoita ratkaisun toimivan kaikissa tilanteissa.

Valitse tämän tunnin korjaukseksi vain yksi olennainen puute. Toista juuri siihen liittyvä testi samalla odotuksella. Kirjaa muut epäonnistumiset tunnistetuiksi jatkokehityskohteiksi, mutta älä yritä korjata niitä kaikkia tämän tunnin aikana.

## Yleisimmät sudenkuopat

**1. Liian kiltti botti.**

Jos botti vain vastaa ”hyvä kysymys” ja toistaa käyttäjän sanat, se ei ohjaa. Lisää järjestelmäpromptiin velvoite kysyä tarkentavia kysymyksiä, antaa konkreettista palautetta ja ohjata käyttäjää seuraavaan vaiheeseen.

**2. Liian yleinen botti.**

Jos botti kuulostaa samalta riippumatta siitä, onko aiheena salitreeni vai kerhon säännöt, järjestelmäpromptissa ja tietopohjassa ei ole tarpeeksi aiheesi erikoispiirteitä. Lisää termistöä ja konkreettisia esimerkkejä.

**3. Liian innokas botti.**

Jos botti tekee koko tehtävän käyttäjän puolesta heti ensimmäisellä viestillä, työnkulun ohjaus on jäänyt vajaaksi. Lisää järjestelmäpromptiin vaihe vaiheelta etenevä toimintatapa ja kielto tehdä koko tehtävä käyttäjän puolesta.

::: luokka
## Tarkistuslista ennen palautusta

Käy nämä kohdat läpi ennen kuin palautat työn:

- ☐ Botin järjestelmäpromptissa on selkeä rooli, työnkulku ja rajat.
- ☐ Botti puhuu oman aiheesi kieltä eikä käytä vain yleisiä fraaseja.
- ☐ Tietopohjassa on 2–4 hyvää ja perusteltua dokumenttia.
- ☐ Olen ajanut tai simuloinut normaalin, kielteisen ja reunatapauksen sekä kirjannut odotukset ja tulokset.
- ☐ Ratkaisu tunnistaa rajansa eikä mene oman alueensa ulkopuolelle.
- ☐ Olen tehnyt yhden nimetyn korjauksen ja toistanut sitä koskevan testin.
- ☐ Reflektioni kuvaa, mitä opin, ei vain sitä, mitä tein.
- ☐ Teknisen botin linkki tai dokumentoidun suunnittelupolun arkkitehtuuri ja simuloitu suoritusjälki ovat mukana.
- ☐ Olen ylpeä tästä botista. Se on minun käsialaani.
:::

::: verkko
## Tarkistuslista ennen kuin työ on valmis

Käy nämä kohdat läpi ennen kuin toteat työsi valmiiksi:

- ☐ Botin järjestelmäpromptissa on selkeä rooli, työnkulku ja rajat.
- ☐ Botti puhuu oman aiheesi kieltä eikä käytä vain yleisiä fraaseja.
- ☐ Tietopohjassa on 2–4 hyvää ja perusteltua dokumenttia.
- ☐ Olen ajanut tai simuloinut normaalin, kielteisen ja reunatapauksen sekä kirjannut odotukset ja tulokset.
- ☐ Ratkaisu tunnistaa rajansa eikä mene oman alueensa ulkopuolelle.
- ☐ Olen tehnyt yhden nimetyn korjauksen ja toistanut sitä koskevan testin.
- ☐ Reflektioni kuvaa, mitä opin, ei vain sitä, mitä tein.
- ☐ Valitsemani polun näyttö on mukana, ja simuloidut ominaisuudet on merkitty.
- ☐ Olen ylpeä tästä botista. Se on minun käsialaani.
:::

## Lopuksi

Apuri-botti on **näyttö osaamisestasi**: osaat rajata tehtävän, suunnitella aineiston käytön, testata ennen–jälkeen-muutoksen ja perustella toteutuksen rajat. Tekninen polku tuottaa käytettävän botin. Dokumentoitu suunnittelupolku tuottaa toteuttamiskelpoisen ja rehellisesti rajatun suunnitelman. Kumpikaan ei ole valmis ilman testejä, uudelleentestausta ja oman ratkaisun puolustamista.

Tämä on iso askel käyttäjästä rakentajaksi. Pidä siitä kiinni.

Et opettele vain käyttämään tekoälyä. Opit rakentamaan sillä.

---

## Lähteet ja tarkistuspäivä

- [NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [UNESCO: Recommendation on the Ethics of Artificial Intelligence](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence)
- [European Commission: GDPR principles](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr/overview-principles/what-data-can-we-process-and-under-which-conditions_en)

Tarkistettu 15.7.2026.
