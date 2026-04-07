# Opettajan materiaalit – Lesson 27: n8n-projektipaja, osa 2

## Osaamistavoitteet (Bloom)

**Muistaa / Ymmärtää:**
- Opiskelija ymmärtää, kuinka testata agenttia systemaattisesti.
- Opiskelija tunnistaa normaalit tapaukset, reunatapaukset ja turvallisuustestit.
- Opiskelija ymmärtää dokumentaation tärkeyden ja sen kolme ydinmuotoa (README, ARCHITECTURE, SAFETY).

**Soveltaa / Analysoida:**
- Opiskelija rakentaa toimivan n8n-agentin.
- Opiskelija testaa agenttia kattavasti ja dokumentoi tulokset.
- Opiskelija arvioi kriittisesti omaa työtään ja toisen projektia.

**Luoda / Arvioida:**
- Opiskelija kirjoittaa selkeää, ammatillista dokumentaatiota.
- Opiskelija esittelee projektinsa demona ja perustaa valintojaan.
- Opiskelija tunnistaa agentin kuusi komponenttia omassa projektissaan.

---

## Pedagoginen lähestymistapa

### Ydinviesti: ammattilaisuus

Lesson 27 on kokonaan ammatillisen ohjelmiston kehittämisen prosessista.

**"Amatööri rakentaa ja toivoo, että se toimii. Ammattilainen rakentaa, testaa ja dokumentoi."**

Painota opiskelijoille:
- Testaaminen ei ole valinnaista — se on pakollista
- Dokumentaatio tekee projektista ammatillisen
- Itsekritiikki osoittaa syvää ajattelua paremmin kuin täydellisyys

### Iteratiivinen kehitys, ei "big bang"

Monet opiskelijat yrittävät rakentaa koko projektin kerralla ja sitten korjata. Tämä johtaa:
- Vaikeisiin debuggaustilanteisiin
- Turhauttaviin virheisiin
- Epämotivaatioon

**Opetuskäytäntö:** Pakota opiskelijat rakentamaan pienissä askelissa.

"Rakenna ensin Trigger + yksi solmu. Testaa sitä. Kunhan se toimii, lisää seuraava. Näin jos jotain menee pieleen, tiedät mikä."

### Testaamisen filosofia

Testaaminen on kolmiosainen:

1. **Normaalit tapaukset** — Agentti on suunniteltu näihin. Pitää toimia.
2. **Reunatapaukset** — Epätavallisia, mutta mahdollisia. Agentti pitää käsitellä nämä rakentavasti.
3. **Turvallisuus** — Aktiivisia hyökkäysyrityksiä. Agentti pitää torjua ne.

Ilman turvallisuustesteja et tiedä, onko agentissasi haavoittuvuuksia.

### Dokumentaation kolme tasoa

**README** — ei-tekniset ihmiset
- Yksinkertainen, selkeä, esimerkkejä

**ARCHITECTURE** — tekijät ja ylläpitäjät
- Tekninen, yksityiskohtainen, kaavioita

**SAFETY** — riskinarvioint
- Riskit, ratkaisut, testtulokset

Jokainen dokumentti palvelee eri yleisöä.

---

## Yleisiä väärinkäsityksiä

### 1. "Jos testaus menee pieleen, projekti epäonnistui"

**Todellisuus:** Jos testaus menee pieleen JA korjaat sen, projekti onnistui. Epäonnistuminen on, jos testaus menee pieleen ja et huomaa.

**Opetuskäytäntö:** Kerro: "Epäonnistuneet testit ovat hyviä. Ne osoittavat, että testit toimivat. Kun löydät ongelman ja korjaat sen, olet parempi insinööri."

### 2. "Dokumentaatio on turhaa — koodi on tarpeeksi"

**Todellisuus:** Koodi kertoo mitä agentti tekee. Dokumentaatio selittää miksi. Dokumentaation puuttuminen on kriittinen ongelma tuotannossa.

**Esimerkki:** "Kuka muu voi ylläpitää projektia, jos sinulla menee poissa ja et ole jättänyt dokumentaatiota?"

### 3. "Turvallisuustestit ovat äärimmäisiä — oikeat käyttäjät eivät tekisi näin"

**Todellisuus:** Oikeat hyökkääjät tekevät näin. Turvallisuustestit ovat realistista harjoittelua.

"Prompt injection ei ole teoreettinen. Se tapahtuu oikeassa maailmassa. Sinun agenttisi pitää torjua se."

### 4. "Oma projektini on liian pieni dokumentoinnista"

**Todellisuus:** Jopa pienillä projekteilla on dokumentaatio. Se auttaa sinua muistamaan, mitä teit kuukauden päästä.

---

## Luokkatehtävän ohjeistus

### TT-A: Testaaminen

**Tavoite:** Opiskelija testaa agenttia systemaattisesti ja dokumentoi tulokset.

**Yleisiä ongelmia:**

- Opiskelija testaa vain muutaman kerran ja väittää "valmis"
  - Ratkaisu: vaadi 15 testiä (5 normaalia + 5 reuna + 5 turva)

- Testaus on satunnaista, ei dokumentoitua
  - Ratkaisu: vaadi testausraportin muotoa — kirjaa jokainen testi

- Turvallisuustestit puuttuvat tai liian pehmeitä
  - Ratkaisu: näytä konkreettisia hyökkäysyrityksiä (prompt injection, piilotut ohjeet)

- Opiskelija ei korjaa epäonnistuneita testeja
  - Ratkaisu: sano: "Epäonnistuneet testit ovat merkintöjä siitä, mitä pitää korjata. Korjaa ne."

**Aikaarvio:** 30-45 min

### TT-B: Dokumentaatio

**Tavoite:** Opiskelija kirjoittaa ammatillista dokumentaatiota.

**Yleisiä ongelmia:**

- README on liian tekninen
  - Ratkaisu: sano: "README on ihmisille, jotka eivät ymmärrä tekniikkaa. Yksinkertaista sitä."

- ARCHITECTURE puuttuu kokonaan tai on liian yksinkertainen
  - Ratkaisu: vaadi taulukkoa: jokainen solmu, sen tehtävä, input/output

- SAFETY on pelkkä lista, ei analyysia
  - Ratkaisu: vaadi "Mitä tapahtuu jos...?" -taulukkoa ja ratkaisuja jokaiselle riskille

- Dokumentaatiossa ei ole kuuden komponentin linkitystä
  - Ratkaisu: vaadi eksplisiittisesti: "Kirjoita, mikä solmu on syötekäsittelijä, mikä päättelijä, jne."

**Aikaarvio:** 45-60 min

### TT-C: Punainen tiimi

**Tavoite:** Opiskelija testaa ja arvioi toisen projektia kriittisesti.

**Yleisiä ongelmia:**

- Palaute on liian pehmeää ("Tämä on hyvää!")
  - Ratkaisu: sano: "Konkreetit. Mikä tarkalleen on hyvää? Miksi?"

- Palaute on liian ankara ("Tämä on huono!")
  - Ratkaisu: muistuta: "Tavoite on auttaa, ei vahingoittaa. Ole rakentava."

- Turvallisuustestit puuttuvat kokonaan
  - Ratkaisu: vaadi konkreettisia testeja: "Entä prompt injection? Entä piilotut ohjeet?"

- Punainen tiimi ei testaa tarpeeksi
  - Ratkaisu: anna tarkistuslista: "Testattiin nämä 15 asiaa?"

**Aikaarvio:** 30-40 min

### TT-D: Demo ja itsekritiikki

**Tavoite:** Opiskelija esittelee projektinsa ja arvioi sitä kriittisesti.

**Yleisiä ongelmia:**

- Demo on liian pitkä tai liian lyhyt
  - Ratkaisu: vaadi 3-5 minuuttia — ei enempää, ei vähempää

- Itsekritiikki puuttuu ("Se toimii täydellisesti!")
  - Ratkaisu: sano: "Mikään ei ole täydellinen. Mitä epäonnistui? Mitä oppit?"

- Kuuden komponentin linkitys puuttuu demosta
  - Ratkaisu: vaadi selityksessä: "Näytä, mikä solmu on päättelijä ja miksi."

- Opiskelija ei kuuntele punaisen tiimin palautetta
  - Ratkaisu: sano: "Punainen tiimi löysi ongelmia. Miten vastaat niihin?"

**Aikaarvio:** 20-30 min

---

## Arviointikaavio (projektiviikko)

| Kriteeri | Paino | Mitä se tarkoittaa |
|----------|-------|---------------------|
| **Toiminnallisuus** | 30 % | Tekeekö agentti sen, mitä lupasit? Toimiiko se ilman kriittisiä virheitä? |
| **Dokumentaatio** | 20 % | Voidaanko projektia ymmärtää ilman sinun selitystäsi? README + ARCHITECTURE + SAFETY olemassa? |
| **Testaaminen** | 20 % | Testattiinko normaalia, reunatapauksia ja turvallisuutta? Dokumentoitiko tulokset? |
| **Demo** | 15 % | Osaatko esitellä selkeästi? Voitko puolustaa valintojasi? |
| **Kriittinen ajattelu** | 15 % | Tunnistitko kuuden komponentin? Linkkivätkö ne solmuihisi? Ymmärrät heikkoudet? |

---

## Tuntiesityksen rakenne (45 minuuttia)

1. **Kertaus: iteratiivinen kehitys** (3 min)
   - "Rakentakaa pienissä askelissa. Testatkaa jokaisen askeleen jälkeen."

2. **Rakentamisen demo** (5 min)
   - Näytä, miten rakennetaan prototyyppistä valmistuotteeseen

3. **Testaamisen koulutus** (7 min)
   - Näytä normaalia, reunatapausta ja turvallisuustestiä live

4. **Dokumentaation selitys** (5 min)
   - Näytä README + ARCHITECTURE + SAFETY -esimerkkejä

5. **Opiskelijat rakentavat ja testaavat** (20 min)
   - Kierrä luokassa, anna palautetta, auta ongelmissa

6. **Yhteenveto ja seuraavat askeleet** (5 min)
   - "Seuraavalla tunnilla esitätte demot. Valmistautukaa."

---

## Materiaalit, jotka opettajalla pitää olla valmiina

- **N8n-instanssi** (testattavaksi)
- **Malliagentit:**
  - Yksinkertainen (Trigger + HTTP + IF + Discord)
  - Keskivertainen (Webhook + Validointi + OpenAI + Tarkistus + Discord)
  - Haastava (kaikki yllä + Memory + Logging)
- **Testausraportin malli** (printattava)
- **Dokumentaation mallit** (README, ARCHITECTURE, SAFETY)
- **Punaisen tiimin palautelomake** (printattava)
- **Arviointikaavio** (printattava)

---

## Opettajan vihjeet

1. **Opiskelijat haluavat rakentaa liian nopeasti**
   - Pakota heitä pysähtymään ja suunnittelemaan ennen rakentamista

2. **Testaaminen jää tekemättä**
   - Aseta testaaminen pakolliseksi välivaiheeksi — ei demoa ilman testiraporttia

3. **Dokumentaatio unohdetaan**
   - Sano selkeästi: "Ilman dokumentaatiota projekti ei ole valmis."

4. **Kriittinen ajattelu puuttuu**
   - Kysy: "Miksi valitsit tämän? Mitä olisit voinut tehdä toisin? Mitä puuttuu?"

5. **Aikapaineista huolimatta laatu sijoiksi**
   - "Pienempi, hyvin testattu ja dokumentoitu projekti on aina parempi kuin suurempi puolivalmis työ."

## Eriyttäminen ja tuen tarpeet — arviointitehtävä Agentit-osiossa

### Suorituspolut
Opiskelijat voivat valita ohjatun (Polku A) tai tutkivan (Polku B) testauksen. Polku A seuraa valmista suunnitelmaa, Polku B vaatii opiskelijan itse keksimiä testejä. Molemmat arvioidaan samoilla kriteereillä.

### Tuen kohdat Agentit-osiossa

| Tunti | Kriittinen kohta | Merkki siitä, että opiskelija tarvitsee tukea | Mitä tehdä |
|-------|-----------------|----------------------------------------------|-----------|
| 19 | Agentin käsite | Opiskelija sekoittaa agentin ja chatbotin | Palaa konkreettiseen esimerkkiin: "Chatbot vastaa. Agentti tekee." |
| 21 | Vektoritietokanta | Opiskelija ei ymmärrä, miksi se on tärkeää | "Ajattele Google-hakua, joka ymmärtää mitä tarkoitat, ei vain mitä kirjoitat" |
| 23 | ReAct ja suunnittelumallit | Opiskelija kadottaa punaisen langan | Piirrä yksinkertainen kaavio: "Ajattele → Tee → Tarkista → Toista" |
| 26 | n8n:n aloittaminen | Opiskelija jähmettyy tyhjän työtilan edessä | Ohjaa Taso 1 -projektiin (FAQ-botti) ja "Jos olet jumissa" -osion pariin |
| 27 | Dokumentaatio | Opiskelija ei tiedä mitä kirjoittaa | Näytä ARCHITECTURE.md -pohja ja sano: "Täytä tämä solmu kerrallaan" |

### LLM-resistenssin varmistaminen arviointitehtävässä
- n8n-projekti on luonnostaan LLM-resistentti: opiskelija rakentaa visuaalisen työnkulun, testaa sitä ja dokumentoi arkkitehtuurin.
- Vertaisarviointi (punainen tiimi) ja suullinen demo paljastavat, onko opiskelija todella ymmärtänyt rakentamansa agentin.
- Itsekritiikki-dokumentti vaatii henkilökohtaista pohdintaa, jota ei voi generoida.

