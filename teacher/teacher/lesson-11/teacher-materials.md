# Opettajan materiaalit — muita tekoälymalleja

## Oppimisen tavoitteet

Tämän lohkon jälkeen opiskelija tuntee muut mallit kuin ChatGPT ja Claude (Gemini, DeepSeek, Llama, Mistral), ymmärtää jokaisen mallin edut ja haitat (hinta, nopeus, tietosuoja), osaa vertailla malleja käytännössä antamalla niille saman tehtävän ja näkemällä erot, tietää tietosuojasta (missä palvelimet ovat ja mitä GDPR on), osaa valita oikean mallin tilanteen mukaan (mihin sopii DeepSeek, mihin Claude, mihin paikallinen malli), ymmärtää paikallisen mallin ajamisesta (Llama ja Mistral omalla tietokoneella täydellisen yksityisyyteen) ja ajattelee kriittisesti eikä vain "ChatGPT on paras".

---

## Mitä opiskelijat epäymmärtävät

### 1. "ChatGPT on paras"

**Mitä kuulla:** Opiskelijat luulevat, että ChatGPT on ainoa valinta.

**Totta on:** ChatGPT on tunnetuin, mutta ei paras kaikelle, koska Claude on parempi ohjelmoinnissa, Gemini on halvempi ja DeepSeek on nopea. Valinta riippuu siitä, mitä haluat tehdä.

**Mitä sanoa:** "ChatGPT on kuin suosituin levy. Se on hyvä, mutta ei kaikille, ja Claude on toisille parempi. Gemini on halvempi ja jokaisella on paikkansa."

### 2. "DeepSeek on halpa, miksi en käytä sitä?"

**Mitä kuulla:** Opiskelijat näkevät hinnan ja haluavat käyttää sitä.

**Totta on:** DeepSeek on hyvä ja halpa, mutta tiedot menevät Kiinan palvelimille. EU:ssa tämä on ongelma, koska GDPR kieltää sen, eikä oppilaiden tiedot, potilastiedot ja yrityksen asiakastiedot voi mennä sinne.

**Mitä sanoa:** "DeepSeek on hyvä, mutta kun lähetät siihen oppilaiden nimiä tai koodia, se menee Kiinan palveluun ja Kiinan hallitus voi nähdä sen. EU:ssa tämä ei ole sallittua. Ymmärrät nyt, miksi ammattilaiset ovat varovaisia?"

### 3. "Paikallinen malli on liian vaikea"

**Mitä kuulla:** Opiskelijat luulevat, että omalla koneella ajaminen vaatii ohjelmointia.

**Totta on:** Ohjelmat, kuten Ollama ja LM Studio, tekevät siitä helpoksi, ja se on kuin sovelluksen asentaminen.

**Mitä sanoa:** "Ollama tekee siitä helppoa, asennit sen, valitset mallin, ja se toimii. Ei tarvitse koodia. Kokeile!"

### 4. "Paikallinen malli on hidas ja huono"

**Mitä kuulla:** Opiskelijat ajattelevat, että paikallinen malli on pienempi ja heikkompi.

**Totta on:** Paikallinen malli on pienempi, mutta jos haluat yksityisyyden ja ilmaisen käytön, se on täydellinen, koska tiedot pysyvät sinulla, etkä maksa per kysymys.

**Mitä sanoa:** "Kyllä, se on hitaampi, mutta kaikki pysyy sinulla, 100 prosenttia yksityinen ja ilmainen. Jos tarvitset nopeutta, käytä pilvipalvelua, jos tarvitset yksityisyyttä, käytä paikallista."

### 5. "Tietosuoja on vain yrityksille"

**Mitä kuulla:** Opiskelijat ajattelevat, että tietosuoja ei ole heille tärkeä.

**Totta on:** Henkilökohtaisesti se ei ole kriittistä, mutta ammatillisesti se on tärkeä, koska opettaja, lääkäri ja sosiaalityöntekijä käsittelevät herkkiä tietoja, joista sinun on tiedettävä säännöt.

**Mitä sanoa:** "Henkilökohtaisesti käytä mitä haluat, mutta kun työskentelet opettajana tai lääkärinä, sinun on tiedettävä, mihin tiedot menevät. Tämä on ammattilaisuutta."

---

## Valmistelu opettajalle

### Viikko ennen lähiosaa (30 minuuttia)

Testaa kaksi mallia samalla tehtävällä, esimerkiksi "Kirjoita lyhyt tarina tulevaisuudesta". Testaa Gemini (ilmainen Google AI Studio), DeepSeek tai Llama ja kopioi vastaukset muistiin.

Valmistele ryhmille 3-4 skenaariota (opettaja-tehtävät ovat valmiita).

### Päivää ennen lähiosaa (15 minuuttia)

Varmista, että sinulla on internetti ja se toimii, testaa Google AI Studio -pääsy, tee testit muille malleille jos käytät niitä ja varaa varasuunnitelma siltä varalta, että netti ei toimi (voit näyttää kuvakaappauksia).

### Lähiosassa (90 minuuttia)

**Alku (5 minuuttia):**

Kerro opiskelijoille: "Viime viikolla opimme ChatGPT:stä ja Claudesta, tänään näytämme, että muita malleja on olemassa ja ne tuottavat erilaisia vastauksia. Ammattilaisesti sinun pitää tietää, mikä valinta sopii mihinkin."

**Tehtävä 1: Mallivertailu (25 minuuttia)**

Näytä kolme eri vastausta samaan tehtävään, kysy opiskelijoilta, mitä eroja he näkevät, ja selitä, että mallit ovat erilaisia.

**Tehtävä 2: Tietosuoja-skenaariot pienryhmissä (30 minuuttia)**

Jaa opiskelijat 3-4 ryhmään, anna jokaiselle ryhmälle skenaario, jossa he pohtivat mitä mallia käyttää, ja he esittelevät johtopäätöksensä.

**Tehtävä 3: Malleja testataan (25 minuuttia)**

Opiskelijat avaavat mallin omalla tietokoneella, antavat sille saman tehtävän ja vertaavat vastauksia parin kanssa.

**Lopetus (5 minuuttia):**

"Näimme, että malleja on monia ja ne ovat erilaisia. Ammattilaisesti valinta riippuu hinnasta, nopeudesta ja tietosuojasta."

### Jos netti ei toimi

Näytä kuvakaappauksia vastauksista, opiskelijat voivat vertailla kuvia ja tehtävä 3 voidaan siirtää seuraavalle päivälle.

### Jos opiskelijat eivät halua oppia

Kerro: "Seuraavassa työpaikassa on säännöt, mitä malleja saa käyttää. Jos tiedät nämä asiat nyt, et häpeä siellä."

---

## Arviointikriteerit

### Taso 1: Perustaidot

Opiskelija:
- Nimeää 5+ mallia
- Sanoo, mitä eroa niillä on
- Tietää, että hinta ja tietosuoja eroavat

**Mitä etsit:** "Gemini on halpa. Claude on tarkka. DeepSeek on halpa, mutta Kiinassa. Llama on yksityinen."

### Taso 2: Vertailu

Opiskelija:
- Testaa kahta mallia samalla tehtävällä
- Näkee erot (nopeus, selkeys, tarkkuus)
- Ymmärtää, miksi ne eroavat

**Mitä etsit:** "Claude oli parempi koodissa, mutta Gemini oli nopeampi."

### Taso 3: Valinta ja päätöksenteko

Opiskelija valitsee mallin skenaarion mukaan, ottaa huomioon hinnan, tietosuojan ja tarpeet sekä selittää päätöksensä.

**Mitä etsit:** "Sairaalalle valitsisin Claudea, koska potilastiedot ovat herkkiä. DeepSeek ei sovi, koska se on Kiinassa."

### Testaus

**Kysymys 1:** Mitkä mallit sopivat mihinkin? Halvoille ratkaisuille DeepSeek (mutta vain yksityisille), korkealaatuisille Claude, halvoille ja turvallisille Gemini ja yksityisille Llama paikallisesti.

**Kysymys 2:** Miksi DeepSeek ei sovellu EU:ssa? Data menee Kiinan palvelimille, GDPR kieltää sen ja oppilaiden ja potilaiden tiedot on suojattava.

**Kysymys 3:** Mitä valitsisit pienelle yritykselle pienellä budjetilla? Gemini on halpa ja turvallinen vaihtoehto, tai paikallinen Llama joka on ilmainen.

---

## Vinkkejä opettajalle

### Verkkosivustot, joista testata malleja

Testaa malleja seuraavista sivustoista: Google AI Studio (Gemini) osoitteesta `ai.google.dev` (ilmainen, ei rekisteröintiä tarvita), DeepSeek osoitteesta `chat.deepseek.com` (ilmainen, rajat), Ollama (asennettava ohjelma paikallisesti) ja LM Studio (graafinen käyttöliittymä paikallisesti).

### Konkreettisia esimerkkejä opiskelijoille

Jos opiskelijat kysyvät "Mihin voisin käyttää DeepSeekia?":
- **Oma koodaus:** Kyllä.
- **Kreatiivinen kirjoitus:** Kyllä.
- **Oppilaiden esseiden arviointi:** Ei (oppilaiden tiedot on suojattava).
- **Potilastietojen analysointi:** Ei (GDPR).
- **Asiakastietojen käsittely:** Ei (tietosuoja).

### Jos opiskelijat haluavat kokeilla malleja

Auta opiskelijoita avaamaan Google AI Studio (Gemini on ilmainen), suosittele heille Ollama-ohjelmaa, jos he haluavat paikallista ratkaisua, ja tehokkain tapa on antaa heille samat ohjeet ja antaa heidän testata omalla koneella.

### Hankalia kysymyksiä

**"Onko DeepSeek kielletty?"**
Vastaus: "Ei kielletty yksityisesti, mutta jos käsittelee oppilaiden tai potilaiden tietoja, se on ongelma."

**"Miksi USA:n mallit ovat parempia?"**
Vastaus: "Ne eivät ole parempia, vain eri, ja USA:n mallit noudattavat EU:n sääntöjä, kun Kiina ei."

**"Voinko käyttää DeepSeekia koodiin?"**
Vastaus: "Kyllä, omaan koodiin, mutta jos koodissa on arkaluonteista tietoa, niin ei."

---

## Seuraavaksi

Seuraavalla tunilla opimme, kuinka antaa tekoälylle tarkkoja käskyjä. Kun tiedät, mitä malleja on olemassa, opimme tekemään niille hyviä ohjeita.

## Muistiinpanot opettajalle

Opiskelijat ajattelevat usein, että halvin on paras. DeepSeek on halvin, mutta tietosuoja rajoittaa sen käyttöä, ja tämä on tärkeä oppi: tekniikka ei ole laki, molemmat ovat tärkeitä.

Opiskelijat saattavat innostua DeepSeekista ja kysyä, miksi he eivät käyttäisi sitä. Selitä konkreettisesti, että jos käytetään sitä oppilaiden tietojen kanssa, rikkoutuu lakia.

Paikallinen malli on cool opiskelijoille. Ollama on kuin sovellus ja opiskelijat pitävät siitä, koska he saavat kontrollin. Kannusta heitä kokeilemaan.

Ammattilaisuus on valinta-taito. Tämän lohkon ydin on, että ammattilaiset tietävät mitä mallia käyttää mihinkin, eikä se ole "ChatGPT on paras", vaan "valitse oikea työkalu oikealle työlle".
