# Opettajan materiaalit: Turvallinen käyttö ja OSP1-arviointi

## Oppimisen tavoitteet (Bloom: Arvioi)

Tämän lohkon jälkeen opiskelija:

1. Ymmärtää tekoälyn turvallisuusriskit: prompt injection, tietovuoto, data hygiene.
2. Osaa soveltaa OSP1:n käsitteitä (epädeterminismi, hallusinaatiot, harha, etiikka) todellisiin skenarioihin.
3. Osaa kirjoittaa rakennetun, ammattilaisesti vastuullisen analyysin.
4. Osaa arvioida omaa tekoälyn käyttöään turvallisuus ja eettisestä näkökulmasta.

---

## Arviointistrategia

### Miksi summatiivinen arviointi?

OSP1 (oppitunnit 1–9) on teoria-osuus. Arviointi testaa, kuinka syvällisesti opiskelijat ymmärtävät tekoälyä ja osavat soveltaa tietoa.

**Arviointitehtävä valitaan skenaarioista,** koska:
- Se on realistinen (opiskelijat kohtaavat näitä ongelmia ammattilaisena)
- Se vaatii syvää ajattelua (ei vain muistamista)
- Se testaa kyvykkyyttä soveltaa käsitteitä
- Se mittaa ammattilaisesti vastuullisuutta

### Arviointikauden pituus

- **Oppitunnit 1–8:** Iteratiivinen oppiminen, harjoitukset, formatiivinen palaute.
- **Oppitunti 9:** Summatiivinen arviointi (skenaarion analyysi).
- **Arviointitehtävän pituus:** 1000–1200 sanaa (noin 3–4 tuntia työtä, riippuen kirjoituskyvystä).
- **Deadline:** Aika harkinnan jälkeen (esim. 2 viikkoa oppitunnin 9 jälkeen).

---

## 5-taso-asteikon ymmärtäminen

| Taso | Prosentti | Merkitys | Opettajan näkökulma |
|---|---|---|---|
| **5 – Erinomainen** | 90–100% | Syvä ymmärrys käsitteistä, kyky soveltaa ammattilaisesti, rakentava analyysi | "Tämä opiskelija ymmärtää tekoälyä syvällisesti ja ajattelee ammattilaisesti." |
| **4 – Hyvä** | 75–89% | Selvä ymmärrys useimmista käsitteistä, järkevä soveltaminen, jonkin verran puutteellista analyysi | "Tämä opiskelija ymmärtää pääkäsitteet ja osaa soveltaa niitä." |
| **3 – Tyydyttävä** | 60–74% | Perusymmärrys pääkäsitteistä, mutta analyysi on pinnallinen tai osittainen | "Tämä opiskelija ymmärtää perusteita, mutta ei syvästi." |
| **2 – Välttävä** | 45–59% | Osittainen ymmärrys käsitteistä, huomattavia aukkoja, analyysi on sekava | "Tämä opiskelija tarvitsee lisäkoulutusta." |
| **1 – Hylätty** | alle 45% | Vähäinen ymmärrys käsitteistä, ei kyvykkyyttä soveltaa | "Tämä opiskelija ei ole saavuttanut oppimisen tavoitteita." |

---

## Arviointikriteerit yksityiskohtaisesti

### Ongelman ymmärrys (20 pistettä)

**Erinomainen (5 pistettä):**
- Opiskelija ymmärtää skenaarion moniulotteisesti.
- Tunnistaa kaikki merkitykselliset ongelmat.
- Liittää ongelmat OSP1:n käsitteisiin.
- Esim. Skenaario 1 -opiskelijasta: "Riski on kolmijakoinen: GDPR, prompt injection ja organisaation vastuu."

**Hyvä (4 pistettä):**
- Ymmärtää skenaarion ja suurimman osan ongelmista.
- Liittää ongelmat OSP1:n käsitteisiin, mutta jokin puuttuu.
- Esim: "Riski on tietovuoto ja GDPR, mutta ei pohdita prompt injection:ia."

**Tyydyttävä (3 pistettä):**
- Ymmärtää skenaarion pinnal lisesti.
- Tunnistaa pääongelman, mutta muita puuttuu.
- Esim: "Ongelma on, että asiakastiedot voivat vuotaa."

**Välttävä (2 pistettä):**
- Ymmärtää osaa skenariosta.
- Analyysi on sekava tai vähäinen.

**Hylätty (1 pistettä tai alle):**
- Ei ymmärrä skenaariota merkittävästi.

---

### Tekninen analyysi (25 pistettä)

**Erinomainen (5 pistettä):**
- Soveltaa OSP1:n teknisiä käsitteitä syvällisesti.
- Sekoittaa epädeterminismiä, hallusinaatioita, harhaa, turvallisuutta skenaarion kontekstissa.
- Käytännölliset ratkaisut.
- Esim. Skenaario 2: "Algoritmin harha johtuu koulutus datasta. Testaisin: vertaisin hyväksynnän prosentteja nais- ja miespuolisten joukossa. Erojen ollessa merkittäviä (esim. 85% vs. 65%), on harha todella. Korjatakseni: perustasin uusi koulutus data tai poistin vinoutuneet piirteet."

**Hyvä (4 pistettä):**
- Soveltaa useimpia teknisiä käsitteitä.
- Analyysi on lähes syvällistä, jokin puuttuu.
- Ratkaisut ovat järkeviä, mutta voivat olla epäselvyyksiä.

**Tyydyttävä (3 pistettä):**
- Soveltaa jotain teknisiä käsitteitä.
- Analyysi on pinnallinen, ratkaisut ovat perus.
- Esim: "Algoritmi on väärä. Korjaa se."

**Välttävä (2 pistettä):**
- Soveltaa vain yhtä teknistä käsitettä tai ei sovella samankaan.

**Hylätty (1 pistettä tai alle):**
- Ei teknistä analyysia.

---

### Eettinen analyysi (20 pistettä)

**Erinomainen (5 pistettä):**
- Ajattelee syvällisesti tekijänoikeuksista, vastuullisuudesta, globaalista vaikutuksesta.
- Tunnistaa ammattilaisesti vastuullisuuden.
- Tekee eettisiä valintoja, joita voi perustella.
- Esim. Skenaario 3: "Tekoäly tuotanto sisältää eettisiä ongelmia: tekijöille ei makseta, merkitsijät työskentelevät matalapalkkaisesti. Minä sitoutun siihen, että informoin asiakkaita näistä ongelmista ja ehdotan läpinäkyvyyttä. En voi kuitenkaan yksinkertaisesti boikotoida tekoälyä — se on ammatilliset; pitää käyttää harkiten."

**Hyvä (4 pistettä):**
- Ajattelee eettisesti, mutta jokin osa-alue puuttuu.
- Tunnistaa vastuullisuuden, vaikka analyysi ei ole syvällinen.

**Tyydyttävä (3 pistettä):**
- Tunnistaa eettisen ongelman, mutta analyysi on yksinkertainen.
- Esim: "Tekijänoikeudet ovat ongelma, koska tekijöille ei makseta."

**Välttävä (2 pistettä):**
- Mainitsee eettisen näkökulman, mutta analyysi on hyvin vähäinen.

**Hylätty (1 pistettä tai alle):**
- Ei eettistä analyysia.

---

### Ratkaisut ja suositukset (25 pistettä)

**Erinomainen (5 pistettä):**
- Ehdotukset ovat konkreettisia, käytännöllisiä ja ammattilaisesti järkeviä.
- Ottavat huomioon kompleksisuuden (ei "yksinkertaista ratkaisua" asioille, jotka eivät ole).
- Ehdotukset on perusteltu OSP1:n käsitteillä.
- Esim. Skenaario 1: "Käytäntö 1: Asiakaspalvelijoille koulutus, jossa määritellään, mitä dataa saa antaa (ei henkilötietoja). Käytäntö 2: Dokumentointi — jokainen kysely merkitään. Käytäntö 3: Auditointi — kuukausittain tarkistetaan lokeja harhan varalta."

**Hyvä (4 pistettä):**
- Ehdotukset ovat konkreettisia ja järkeviä, mutta jokin osa puuttuu.
- Perustelut ovat selvät, mutta voivat olla syvempiä.

**Tyydyttävä (3 pistettä):**
- Ehdotukset ovat perus ja pinnallisia.
- Esim: "Kirjoita politiikka."

**Välttävä (2 pistettä):**
- Ehdotukset ovat epäselviä tai epäkäytännöllisiä.

**Hylätty (1 pistettä tai alle):**
- Ei ratkaisuja.

---

### Kirjoituksen laatu (10 pistettä)

**Erinomainen (5 pistettä):**
- Teksti on selkeä, hyvin organisoitu, ammatillisesti kirjoitettu.
- Lähdeviitteet ovat oikein.
- Pituus: 1000–1200 sanaa.

**Hyvä (4 pistettä):**
- Teksti on pääosin selkeä ja organisoitu, jokin pienempi epäselvyys.
- Lähdeviitteet ovat suurimman osan oikein.
- Pituus on lähellä vaatimusta.

**Tyydyttävä (3 pistettä):**
- Teksti on ymmärrettävä, mutta organisointi tai selvyys on kohtuullinen.
- Lähdeviitteet ovat olemassa, mutta voivat olla epätäydellisiä.

**Välttävä (2 pistettä):**
- Teksti on vaikeasti ymmärrettävä tai huonosti organisoitu.

**Hylätty (1 pistettä tai alle):**
- Teksti on epäselvä tai epäorganisoitu.

---

## Arviointiprosessi

### Ennen arviointia (oppitunti 9)

1. **Fasilitoi harjoittelua** — ei antaa vastauksia, mutta auta opiskelijoita harjoittelemaan.
2. **Clarify vaatimukset** — varmistu, että opiskelijat ymmärtävät, mitä odotetaan.
3. **Kerää kysymykset** — vastaa ennen arviointia.

### Arviointiprosessin aikana (deadline jälkeen)

1. **Lue huolellisesti** — ymmärrä, mitä opiskelija analysoi.
2. **Käytä kriteerejä johdonmukaisesti** — ole tasapuolinen kaikille.
3. **Kirjoita palaute** — rakentavaa, ei tuomitsevaa.

### Jälkiarviointia

1. **Anna palaute** — mihin he onnistuivat, mihin voivat parantaa.
2. **Keskustele tuloksista** — jos haluat, voit tehdä lyhyen palautekeskustelun.
3. **Dokumentoi pisteytys** — oppilaitoksen sääntöjen mukaan.

---

## Opettajan vinkkejä

**Arviointistandardin ylläpitäminen:**
- Lue kaikki raportit samalla myötätunnolla ja standardilla.
- Jos epäilet pisteytyksen tasapuolisuudesta, ota kaksi raportista ja arvioi uudelleen.
- Monimutkaisissa tapauksissa (esim. opiskelija on sairaus tai on vaikeudet), harkitse jouston mahdollisuutta.

**Opiskelijoiden tukeminen:**
- Jos opiskelija tuntee arviointia olevan liian raskas, tarjoa mahdollisuus tehdä väli-arviointia tai neuvotella deadline:ia.
- Joidenkin opiskelijoiden saattaa tarvita enemmän harjoittelua — tarjoa se ennen arviointia.

**Omasta hyvinvoinnista:**
- Arviointisesio voi olla rasittava. Varaa aikaa, ota taukoja, älä arvioivat liian monta kerralla.

---

## Seuraava askel (OSP2 ja käytäntö)

Oppitunnit 10+ käsittelevät **käytäntöä** — miten käyttää tekoälyä hyvin ammattilaisesti:
- Prompting-tekniikka
- Tekoälyn integrointi työnkulkuihin
- Ammatillisen kehittymisen jatkaminen

OSP1 (oppitunnit 1–9) antaa teorian pohjan. OSP2 antaa käytännöllisiä taitoja.

**Opettajan huomio:** Arviointitehtävä on loukkaavasti suunniteltu siihen, että opiskelijat voivat näyttää ymmärtävänsä teoriaa ja osaavanso soveltaa sitä. Se testaa ammattilaisesti vastuullisuutta — mikä on tärkein oppi.

