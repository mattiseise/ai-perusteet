# Opettajan materiaalit: Turvallinen käyttö ja Teoria-osion arviointi

## Oppimisen tavoitteet (Bloom: arvioi)

Tämän lohkon jälkeen opiskelija:

1. Ymmärtää tekoälyn turvallisuusriskit: prompt injection, tietovuoto, data hygiene.
2. Osaa soveltaa Teoria-osion käsitteitä (epädeterminismi, hallusinaatiot, harha, etiikka) todellisiin skenaarioihin.
3. Osaa kirjoittaa rakenteisen, ammatillisesti vastuullisen analyysin.
4. Osaa arvioida omaa tekoälyn käyttöään turvallisuuden ja eettisen näkökulman perusteella.

---

## Arviointistrategia

### Tekoälyn käyttö tehtävässä

Opiskelijoita kehotetaan käyttämään tekoälyä analyysin kirjoittamisessa. Tämä on tarkoituksellista: tehtävä testaa opiskelijan kykyä **ohjata** tekoälyä tuottamaan analyyttistä tekstiä, ei kykyä kirjoittaa 1000 sanaa itse. Opiskelijalle ei kerrota alla olevasta faktataulukosta.

### Faktataulukko arvioinnin tueksi (opettajan työkalu)

Jokaisen opiskelijan raportin liitteenä tulee olla faktataulukko, jossa opiskelija osoittaa hallitsevansa Teoria-osion keskeiset käsitteet. Taulukko on opettajan arvioinnin apuväline — se paljastaa nopeasti, onko opiskelija ymmärtänyt käsitteet vai tuottanut tekoälyllä pintapuolista tekstiä.

**Pyydä opiskelijaa liittämään raportin loppuun taulukko seuraavassa muodossa:**

| Käsite | Selitys omin sanoin | Miten näkyy skenaariossani |
|---|---|---|
| Epädeterminismi | | |
| Hallusinaatio | | |
| Konteksti-ikkuna | | |
| Prompt injection | | |
| Algoritminen harha | | |
| Datahygienia | | |
| Tekijänoikeudet | | |
| Ammatillinen vastuu | | |

Opiskelijan ei tarvitse täyttää jokaista riviä — vain ne käsitteet, jotka ovat relevantteja hänen valitsemassaan skenaariossa. Taulukko kertoo nopeasti, ymmärtääkö opiskelija käsitteet vai onko hän vain antanut tekoälyn kirjoittaa ne.

### Miksi summatiivinen arviointi?

Teoria-osio (oppitunnit 1–9) on teoriaosuus. Arviointi testaa, kuinka syvällisesti opiskelijat ymmärtävät tekoälyä ja osaavat soveltaa tietoa.

Arviointitehtävä valitaan skenaarioista, koska se on realistinen (opiskelijat kohtaavat näitä ongelmia ammattilaisina), se vaatii syvää ajattelua (ei vain muistamista), se testaa kykyä soveltaa käsitteitä ja se mittaa ammatillista vastuullisuutta.

### Arviointikauden pituus

- **Oppitunnit 1–8:** Iteratiivinen oppiminen, harjoitukset, formatiivinen palaute.
- **Oppitunti 9:** Summatiivinen arviointi (skenaarion analyysi).
- **Arviointitehtävän pituus:** 1000–1200 sanaa (noin 3–4 tuntia työtä, riippuen kirjoituskyvystä).
- **Deadline:** Aika harkinnan mukaan (esim. 2 viikkoa oppitunnin 9 jälkeen).

---

## 5-tasoasteikon ymmärtäminen

| Taso | Prosentti | Merkitys | Opettajan näkökulma |
|---|---|---|---|
| **5 – Erinomainen** | 90–100% | Syvä ymmärrys käsitteistä, kyky soveltaa niitä ammatillisesti, rakentava analyysi | "Tämä opiskelija ymmärtää tekoälyä syvällisesti ja ajattelee ammatillisesti." |
| **4 – Hyvä** | 75–89% | Selvä ymmärrys useimmista käsitteistä, järkevä soveltaminen, jonkin verran puutteellinen analyysi | "Tämä opiskelija ymmärtää pääkäsitteet ja osaa soveltaa niitä." |
| **3 – Tyydyttävä** | 60–74% | Perusymmärrys pääkäsitteistä, mutta analyysi on pinnallinen tai osittainen | "Tämä opiskelija ymmärtää perusteet, mutta ei syvällisesti." |
| **2 – Välttävä** | 45–59% | Osittainen ymmärrys käsitteistä, huomattavia aukkoja, analyysi on sekava | "Tämä opiskelija tarvitsee lisäkoulutusta." |
| **1 – Hylätty** | alle 45% | Vähäinen ymmärrys käsitteistä, ei kykyä soveltaa niitä | "Tämä opiskelija ei ole saavuttanut oppimisen tavoitteita." |

---

## Arviointikriteerit yksityiskohtaisesti

### Ongelman ymmärrys (20 pistettä)

**Erinomainen (5 pistettä):**
- Opiskelija ymmärtää skenaarion moniulotteisesti.
- Tunnistaa kaikki merkitykselliset ongelmat.
- Liittää ongelmat Teoria-osion käsitteisiin.
- Esim. Skenaario 1 -opiskelijasta: "Riski on kolmijakoinen: GDPR, prompt injection ja organisaation vastuu."

**Hyvä (4 pistettä):**
- Ymmärtää skenaarion ja suurimman osan ongelmista.
- Liittää ongelmat Teoria-osion käsitteisiin, mutta jokin puuttuu.
- Esim.: "Riski on tietovuoto ja GDPR, mutta ei pohdita prompt injectionia."

**Tyydyttävä (3 pistettä):**
- Ymmärtää skenaarion pinnallisesti.
- Tunnistaa pääongelman, mutta muita puuttuu.
- Esim.: "Ongelma on, että asiakastiedot voivat vuotaa."

**Välttävä (2 pistettä):**
- Ymmärtää osan skenaariosta.
- Analyysi on sekava tai vähäinen.

**Hylätty (1 pistettä tai alle):**
- Ei ymmärrä skenaariota merkittävästi.

---

### Tekninen analyysi (25 pistettä)

**Erinomainen (5 pistettä):**
- Soveltaa Teoria-osion teknisiä käsitteitä syvällisesti.
- Yhdistää epädeterminismiä, hallusinaatioita, harhaa ja turvallisuutta skenaarion kontekstissa.
- Esittää käytännöllisiä ratkaisuja.
- Esim. Skenaario 2: "Algoritmin harha johtuu koulutusdatasta. Testaisin: vertaisin hyväksynnän prosentteja nais- ja miespuolisten hakijoiden joukossa. Erojen ollessa merkittäviä (esim. 85 % vs. 65 %), harha on todellinen. Korjatakseni tilanteen: perustaisin uuden koulutusdatajoukon tai poistaisin vinoutuneet piirteet."

**Hyvä (4 pistettä):**
- Soveltaa useimpia teknisiä käsitteitä.
- Analyysi on lähes syvällistä, mutta jokin puuttuu.
- Ratkaisut ovat järkeviä, mutta niissä voi olla epäselvyyksiä.

**Tyydyttävä (3 pistettä):**
- Soveltaa joitakin teknisiä käsitteitä.
- Analyysi on pinnallinen, ratkaisut ovat perustasoisia.
- Esim.: "Algoritmi on väärä. Korjaa se."

**Välttävä (2 pistettä):**
- Soveltaa vain yhtä teknistä käsitettä tai ei sovella sitäkään.

**Hylätty (1 pistettä tai alle):**
- Ei teknistä analyysia.

---

### Eettinen analyysi (20 pistettä)

**Erinomainen (5 pistettä):**
- Ajattelee syvällisesti tekijänoikeuksia, vastuullisuutta ja globaalia vaikutusta.
- Tunnistaa ammatillisen vastuun.
- Tekee eettisiä valintoja, joita osaa perustella.
- Esim. Skenaario 3: "Tekoälyn tuotanto sisältää eettisiä ongelmia: tekijöille ei makseta, merkitsijät työskentelevät matalapalkkaisesti. Minä sitoudun siihen, että informoin asiakkaita näistä ongelmista ja ehdotan läpinäkyvyyttä. En voi kuitenkaan yksinkertaisesti boikotoida tekoälyä — se on ammatillisesti ongelmallista; sitä pitää käyttää harkiten."

**Hyvä (4 pistettä):**
- Ajattelee eettisesti, mutta jokin osa-alue puuttuu.
- Tunnistaa vastuullisuuden, vaikka analyysi ei ole syvällinen.

**Tyydyttävä (3 pistettä):**
- Tunnistaa eettisen ongelman, mutta analyysi on yksinkertainen.
- Esim.: "Tekijänoikeudet ovat ongelma, koska tekijöille ei makseta."

**Välttävä (2 pistettä):**
- Mainitsee eettisen näkökulman, mutta analyysi on hyvin vähäinen.

**Hylätty (1 pistettä tai alle):**
- Ei eettistä analyysia.

---

### Ratkaisut ja suositukset (25 pistettä)

**Erinomainen (5 pistettä):**
- Ehdotukset ovat konkreettisia, käytännöllisiä ja ammatillisesti järkeviä.
- Ottavat huomioon kompleksisuuden (ei "yksinkertaista ratkaisua" asioihin, jotka eivät ole yksinkertaisia).
- Ehdotukset on perusteltu Teoria-osion käsitteillä.
- Esim. Skenaario 1: "Käytäntö 1: Asiakaspalvelijoille koulutus, jossa määritellään, mitä dataa saa antaa (ei henkilötietoja). Käytäntö 2: Dokumentointi — jokainen kysely merkitään. Käytäntö 3: Auditointi — kuukausittain tarkistetaan lokeja harhan varalta."

**Hyvä (4 pistettä):**
- Ehdotukset ovat konkreettisia ja järkeviä, mutta jokin osa puuttuu.
- Perustelut ovat selviä, mutta voisivat olla syvempiä.

**Tyydyttävä (3 pistettä):**
- Ehdotukset ovat perustasoisia ja pinnallisia.
- Esim.: "Kirjoita politiikka."

**Välttävä (2 pistettä):**
- Ehdotukset ovat epäselviä tai epäkäytännöllisiä.

**Hylätty (1 pistettä tai alle):**
- Ei ratkaisuja.

---

### Kirjoituksen laatu (10 pistettä)

**Erinomainen (5 pistettä):**
- Teksti on selkeä, hyvin organisoitu ja ammatillisesti kirjoitettu.
- Lähdeviitteet ovat oikein.
- Pituus: 1000–1200 sanaa.

**Hyvä (4 pistettä):**
- Teksti on pääosin selkeä ja organisoitu, mutta siinä on jokin pienempi epäselvyys.
- Lähdeviitteet ovat suurimmaksi osaksi oikein.
- Pituus on lähellä vaatimusta.

**Tyydyttävä (3 pistettä):**
- Teksti on ymmärrettävä, mutta sen organisointi tai selkeys on vain kohtuullinen.
- Lähdeviitteet ovat olemassa, mutta voivat olla epätäydellisiä.

**Välttävä (2 pistettä):**
- Teksti on vaikeasti ymmärrettävä tai huonosti organisoitu.

**Hylätty (1 pistettä tai alle):**
- Teksti on epäselvä tai epäorganisoitu.

---

## Arviointiprosessi

### Ennen arviointia (oppitunti 9)

1. **Fasilitoi harjoittelua** — älä anna vastauksia, mutta auta opiskelijoita harjoittelemaan.
2. **Selvennä vaatimukset** — varmista, että opiskelijat ymmärtävät, mitä odotetaan.
3. **Kerää kysymykset** — vastaa niihin ennen arviointia.

### Arviointiprosessin aikana (deadlinen jälkeen)

1. **Lue huolellisesti** — ymmärrä, mitä opiskelija analysoi.
2. **Käytä kriteerejä johdonmukaisesti** — ole tasapuolinen kaikille.
3. **Kirjoita palaute** — rakentavaa, ei tuomitsevaa.

### Jälkiarviointi

1. **Anna palaute** — missä he onnistuivat ja missä voivat parantaa.
2. **Keskustele tuloksista** — jos haluat, voit tehdä lyhyen palautekeskustelun.
3. **Dokumentoi pisteytys** — oppilaitoksen sääntöjen mukaan.

---

## Opettajan vinkkejä

**Arviointistandardin ylläpitäminen:**
- Lue kaikki raportit samalla myötätunnolla ja samalla standardilla.
- Jos epäilet pisteytyksen tasapuolisuutta, ota kaksi raporttia ja arvioi ne uudelleen.
- Monimutkaisissa tapauksissa (esim. opiskelija on sairas tai hänellä on vaikeuksia), harkitse joustomahdollisuutta.

**Opiskelijoiden tukeminen:**
- Jos opiskelija kokee arvioinnin liian raskaaksi, tarjoa mahdollisuus tehdä väliarviointia tai neuvotella deadlinesta.
- Jotkut opiskelijat saattavat tarvita enemmän harjoittelua — tarjoa sitä ennen arviointia.

**Omasta hyvinvoinnista:**
- Arviointisessio voi olla rasittava. Varaa aikaa, pidä taukoja, älä arvioi liian monta työtä kerralla.

---

## Seuraava askel (Tekoälyn käyttö -osio ja käytäntö)

Oppitunnit 10+ käsittelevät **käytäntöä** — miten tekoälyä käytetään hyvin ammatillisesti:
- Prompting-tekniikka
- Tekoälyn integrointi työnkulkuihin
- Ammatillisen kehittymisen jatkaminen

Teoria-osio (oppitunnit 1–9) antaa teorian pohjan. Tekoälyn käyttö -osio antaa käytännöllisiä taitoja.

**Opettajan huomio:** Arviointitehtävä on suunniteltu siten, että opiskelijat voivat osoittaa ymmärtävänsä teoriaa ja osaavansa soveltaa sitä. Se testaa ammatillista vastuullisuutta — mikä on tärkein oppi.

---

## Eriyttäminen ja tuen tarpeet — arviointitehtävä

### Vaihtoehtoinen suoritustapa
Kokonaisuuden 1 arviointitehtävässä opiskelija voi valita visuaalisen suoritustavan (tilannekartta + päätöspuu + suullinen perustelu) kirjallisen analyysin sijaan. Molemmat vaativat saman syvyyden — vaihtoehtoinen ei ole helpompi.

### Miksi vaihtoehtoinen suoritustapa on tärkeä
- Opiskelijat, joilla on kirjoittamisen vaikeuksia, voivat osoittaa saman osaamisen visuaalisesti ja suullisesti.
- Visuaalinen analyysi on itse asiassa **vaikeampi kopioida tekoälyllä** kuin kirjallinen essee. Tilannekartan piirtäminen ja suullinen perustelu ovat luonnostaan LLM-resistenttejä.
- Suullinen perustelu paljastaa heti, onko opiskelija ymmärtänyt vai kopioinut.

### Tuen kohdat kokonaisuudessa 1
Tunnista opiskelijat, jotka tarvitsevat tukea, näissä kohdissa:

| Tunti | Kriittinen kohta | Merkki siitä, että opiskelija tarvitsee tukea | Mitä tehdä |
|-------|-----------------|----------------------------------------------|-----------|
| 3 | Tokenisaatio ja parametrit | Opiskelija ei ymmärrä, miksi sanat pilkotaan osiin | Käytä konkreettista esimerkkiä: "Kokeile itse OpenAI:n tokenizeria" |
| 5 | Konteksti-ikkuna | Opiskelija ei hahmota FIFO-periaatetta | Piirrä taululle muistilaatikko, jossa uusi asia työntää vanhan ulos |
| 7 | Epädeterminismi | Opiskelija ajattelee, että tekoäly "valitsee" vastauksen | Muistuta: se ei valitse, se ennustaa todennäköisyyksiä |
| 9 | Arviointitehtävä | Opiskelija ei osaa aloittaa analyysia | Ohjaa "Jos olet jumissa" -osion pariin. Se antaa konkreettiset askeleet. |

### LLM-resistenssin varmistaminen
- Kirjallinen analyysi: pyydä opiskelijaa viittaamaan kurssin OMIIN esimerkkeihin ja oppituntien materiaaleihin, ei yleisiin lähteisiin.
- Visuaalinen analyysi: tilannekartta ja päätöspuu ovat luonnostaan henkilökohtaisia — niitä ei voi generoida tekstillä.
- Suullinen perustelu: opiskelijan on selitettävä omin sanoin, mikä paljastaa todellisen ymmärryksen tason.