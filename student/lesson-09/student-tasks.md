# OSP1 Arviointi: Tekoälyn teoria ja perusteet

## Arviointitehtävä: Skenaarion analyysi

### Tehtävän kuvaus

Valitse **yksi** seuraavista kolmesta skenariosta. Kirjoita rakennettu analyysi (1000–1200 sanaa), joka käyttää OSP1:n käsitteitä ja periaatteita ratkaisun kehittämiseen.

**Näytä ymmärrys seuraavista:**
- Tekoälyn luonne: epädeterminismi, hallusinaatiot, rajat
- Etiikka ja tekijänoikeudet
- Turvallisuus ja data hygiene
- Ammattilaisesti vastuullisuutta

---

## Skenaariot

### Skenaario 1: Asiakaspalvelu ja data hygiene

**Konteksti:**
Olet IT-johtaja pienessä e-commerce-yrityksessä. Toimitusjohtaja haluaa implementoida ChatGPT:n asiakaspalvelussa nopeuttamaan vastausaikoja. Asiakaspalvelijat voivat käyttää sitä seuraavasti:

```
Asiakas kirjoittaa: "Missä on tilaukseni #12345?"
Asiakaspalvelija copypaste ChatGPT:hen: "Asiakkaan nimi:
Jukka Mäkinen, sähköpostri jukka@email.com, tilaus #12345,
maksettu luottokortilla 1234-5678-9000-1234."

ChatGPT vastaa: "Tilauksessa voi olla viivästystä
postin kautta. Seuraavat toimet..."
```

**Tehtävä:**
1. Analysoi turvallisuus- ja yksityisyyriskit tässä skenaarissa.
2. Mitä käsitteitä OSP1:stä tarvitset ymmärtämään ongelman?
3. Kirjoita kirjallinen politiikka asiakaspalvelijoille:
   - Mitä tietoja saa antaa ChatGPT:lle?
   - Miten dokumentoida?
   - Mitä pitää tehdä, jos asiakas kysyy herkkää asiaa?
4. Miten ehkäistä tietovuotoja?
5. Miten kouluttaa henkilökunta?

**Arviointikriteeri:**
- Osoita ymmärrys GDPR:stä ja henkilötietojen suojauksesta
- Tunnista prompt injection -riskit
- Ehdota konkreettisia käytäntöjä
- Osoita ymmärrys siitä, että sinulla on ammattilaisesti vastuu

---

### Skenaario 2: Algoritminen harha ja palkkaus

**Konteksti:**
Organisaatiosi käyttää tekoälyä IT-alan rekrytointiin. Algoritmi analysoida hakija hakemusten ja ennustaa, kuka "menestyy" IT-alalla. Data, jolla algoritmi on opetettu, on 10 vuoden historiasta: kenen palkkasi on nousseet, kenet on ylennetty, kuka on jäänyt.

Tarkastus paljastaa: Algoritmi hylkää 85% naispuolisista hakijoista ja hyväksyy 65% miespuolisista — samalla kelpoisuudella.

**Tehtävä:**
1. Miksi algoritmi on puolueellinen? (Selitä algoritmisen harhan mekanismi.)
2. Kuka vastaa? (Sinä? Algoritmin kehittäjät? Johtajat?)
3. Miten tämä liittyy "epädeterminismiin" ja "koulutus dataan"?
4. Kuinka hoitaisit tilanteen?
   - Miten tutkia harhaa?
   - Miten korjata algoritmi?
   - Miten kommunikoida hakijoiden kanssa?
   - Miten estää toistumasta?
5. Mitä "vastuullinen AI" merkitsee tässä kontekstissa?

**Arviointikriteeri:**
- Ymmärrä algoritmisen harhan lähde
- Osoita ymmärrys siitä, että harha on testattavissa
- Tunnista ammattilaisesti vastuu (ei "se on algoritmin vika")
- Ehdota konkreettisia testaus- ja korjauskäytäntöjä

---

### Skenaario 3: Tekijänoikeudet ja vastuullisuus

**Konteksti:**
Sinulla on startup, joka käyttää generatiivista AI:ta luomaan markkinointisisältöä asiakkaille. Käytät ChatGPT:tä kirjoittamaan artikkeleita, sosiaalisen median postauksia ja mainoksia. Prosessi: asiakas antaa aiheen, sinä antaa ChatGPT:lle promptin, ChatGPT tuottaa tekstin, sinä muokkaat sitä, asiakas hyväksyy.

Kuukauden jälkeen asiakas huomaa: hänen kilpailijallaan on lähes identtinen artikkeli ChatGPT:n tuotoksena. Asiakas on huolissaan:
1. Voiko joku varastaa hänen sisältönsä?
2. Kuka omistaa sisällön — hän vai ChatGPT?
3. Onko tekoälyn käyttö eettistä?
4. Vastaavatko tekijät tekijänoikeuksista, kun olivat käyttäneet ChatGPT:tä opetukseen ilman lupaa?

**Tehtävä:**
1. Vastaa asiakkaan neljään kysymykseen käyttäen OSP1:n tietoja.
2. Miten selittäisit tekijänoikeus-ongelmia?
3. Mitä tekijänoikeus merkitsee, kun käytät generatiivista AI:ta?
4. Kuinka informoida asiakasta tekijänoikeusten ja eettisten näkökohtien riskeistä?
5. Ehdota muutettuja prosesseja, jotka ottavat tekijänoikeudet huomioon:
   - Kuinka ilmoittaa asiakkaalle?
   - Kuinka dokumentoida AI:n käyttö?
   - Kuinka varmistaa, ettei plagioida?

**Arviointikriteeri:**
- Ymmärrä tekijänoikeus-kysymykset ja niiden vaativuus
- Tunnista koulutus datan eettisiä ongelmia
- Osoita ymmärrys siitä, että sinulla on vastuu (et voi sanoa "OpenAI teki sen")
- Ehdota käytännöllisiä ratkaisuja asiakkaille

---

## Arviointikriteerit

### 5-taso-asteikko (Erinomainen – Hylätty)

| Taso | Prosentti | Kuvaus | Esimerkit |
|---|---|---|---|
| **Erinomainen (5)** | 90–100% | Syvä ymmärrys OSP1:n käsitteistä. Analyysi on strukturoitu, lähdepohjain ja käytännöllinen. Osoita ammattilaisesti vastuullisuutta. | "Algoritmin harha johtuu siitä, että koulutusdata heijastaa historiallista syrjintää. Kuin testata: vertaa hyväksynnän prosenttia nais- ja miespuolisten joukossa. Erojen ollessa merkittäviä, kaikki hakemusproses on käytävä uudelleen..." |
| **Hyvä (4)** | 75–89% | Selvä ymmärrys useimmista OSP1:n käsitteistä. Analyysi on järkevä mutta saattaa puuttua yksityiskohdista. Osoita ammattilaisesti vastuullisuutta. | "Harha voi johtua opetusdata. Pitäisi testata, mutta en täysin tiedä kuinka. Pitäisi kieltää algoritmi ja käyttää ihmisiä." |
| **Tyydyttävä (3)** | 60–74% | Perusymmärrys pääkäsitteistä (epädeterminismi, hallusinaatiot, harha, turvallisuus). Analyysi on oikeansuuntainen mutta pinnallinen. | "Algoritmi on väärä koska se hylkää naisia. Korjaa data. Tekijöille pitäisi maksaa koska ei he antaneet lupaa." |
| **Välttävä (2)** | 45–59% | Osittainen ymmärrys pääkäsitteistä, mutta huomattavia aukkoja. Analyysi on sekava tai epäyhdistynyt. | "Harha on huonoa. Sinulla pitäisi olla parempi algoritmi. Tekijänoikeudet ovat sekava asia." |
| **Hylätty (1)** | alle 45% | Vähäinen ymmärrys OSP1:n käsitteistä. Analyysi ei osoita kyvykkyyttä soveltaa tietoa. | "Ei tiedä, mitä tehdä. Käytä jotain muuta." |

---

## Arviointikohteet ja pisteet

**Kokonais 100 pistettä, jaettu:**

| Osa | Pisteet | Arviointi |
|---|---|---|
| **Ongelman ymmärrys** | 20 | Kuinka hyvin ymmärrät skenaarion ja siihen liittyvät OSP1-käsitteet? |
| **Tekninen analyysi** | 25 | Kuinka hyvin sovellat epädeterminismiä, hallusinaatioita, harhaa tai turvallisuutta? |
| **Eettinen analyysi** | 20 | Kuinka hyvin ajattelet tekijänoikeuksista, vastuullisuudesta ja globaalista vaikutuksesta? |
| **Ratkaisut ja suositukset** | 25 | Kuinka käytännöllisiä, ammattilaisesti järkeviä ja konkreettisia ehdotuksesi ovat? |
| **Kirjoituksen laatu** | 10 | Onko raportti selkeä, hyvin organisoitu ja ammatillisesti kirjoitettu? |

---

## Ohjeita vastaajalle

1. **Valitse yksi skenaario** — kolmesta.
2. **Lue tarkasti** — ymmärrä skenaarion ongelmat ja konteksti.
3. **Käytä OSP1:n käsitteitä** — epädeterminismi, hallusinaatiot, harha, tekijänoikeudet, ympäristövaikutukset, turvallisuus.
4. **Kirjoita ammatillisesti** — näytä, että ajattelet ammattilaisesti, et vain valikoitui asioita.
5. **Dokumentoi lähteensä** — jos viittaat oikeustapausiin, tutkimusraportteihin, linkit.
6. **Pituus:** 1000–1200 sanaa (ei enemmän, ei vähemmän).

---

## Osio 1 ja 2 arviointi

Seuraavat oppitunnit (10+) käsittelevät käytäntöä — miten käyttää tekoälyä hyvin. OSP1 (oppitunnit 1–9) ovat teoria. Tämä arviointi testaa teoria.

**OSP1:n pääkäsitteet, jotka sinun täytyy tuntea:**
1. Mikä on tekoäly? (oppitunti 1)
2. Miten se toimii? (oppitunnit 2–4)
3. Mitä ovat mallit ja hienosäätö? (oppitunnit 5–6)
4. Miksi se epädeterministinen ja hallusinoiva? (oppitunti 7)
5. Mitkä ovat eettiset näkökohdat? (oppitunti 8)
6. Miten käyttää turvallisesti? (oppitunti 9)

**Onneksi löysit tämän — arviointiä on aika.**
