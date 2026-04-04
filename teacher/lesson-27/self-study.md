# OSP3 Arviointi: Agentit ja automaatio — Demo ja dokumentaatio

## Johdanto: Agenteista oppilas ammattilaiseen

Neljässä viikossa olet oppinut agenteista pienestä käsitteestä — "miten AI voi automatisoida asioita" — täydelliseen arkkitehtuuriin. Olet tutustunut agenttien päättelyyn, hallintoon, turvallisuuteen ja käytännön rakentamiseen. Tämä oppitunti on **OSP3:n kokonaisarviointi**, jossa näytät, mitä opit.

Arviointi perustuu projektiin, jonka rakensit lesson 26:ssa. Esittelyt pohjaavat näihin arviointikohteihin:
1. **Toiminnallisuus** — Tekee se mitä lupasit?
2. **Dokumentaatio** — Ymmärretään se ilman sinua?
3. **Kontekstintaju** — Ymmärrät käyttötapauksen ja rajat?
4. **Turvallisuusajattelu** — Tunnistat ja mitigation riskit?
5. **Demo-laatu** — Osaat esitellä selkeästi?

## Arvioinnin rakenne

### Osa 1: Dokumentaatio (arvioitu ennen demoa)

Ennen demopäivää jäätät näyttöä opettajalle:
- **README.md** — Mitä agentti tekee? Kuinka käyttää?
- **ARCHITECTURE.md** — Miten se on rakennettu?
- **SAFETY.md** — Mitkä riskit? Miten mitigated?
- **TESTING.md** — Mitä testejä ajoit? Tulokset?

Dokumentaation on oltava sellainen, että toinen oppilas voi lukea sen ja ymmärtää projektin **ilman sinun selitystä**.

### Osa 2: Live-demo (arvioitu demopäivässä)

Esittelet projektia luokalla:
1. **Live-esitys** (3-4 min) — Näytät agentin/botin toiminnassa
2. **Kontekstintaju** (2 min) — Selität käyttötapauksen ja rajat
3. **Arkkitehtuuri** (2 min) — Kerrot lyhyesti, miten se toimii
4. **Turvallisuus** (2 min) — Selität riskit ja niiden mitigaation
5. **Reflektio** (1 min) — Opit ja parannukset

Demossa **näytät, et lue diaa**. Diaa voi käyttää tukena, mutta demolla on oltava live-elementti.

### Osa 3: Kysymykset ja keskustelu (arvioitu demopäivässä)

Opettaja ja vertaisopiskelijat voivat esittää kysymyksiä:
- "Miksi valitsit tämän lähestymistavan?"
- "Entä jos käyttäjä tekee X:ää?"
- "Mitä riskejä näet?"
- "Mitä tekisit toisin?"

Vastauksesi näyttävät, oletko ajatellut projektia kriittisesti.

## Arviointikriteerit (5-portainen asteikko)

| Taso | Pisteet | Kuvaus |
|------|---------|--------|
| **Erinomainen (5)** | 90–100 % | Projekti on täysin toimiva, hyvin dokumentoitu ja esitelty. Turvallisuusajattelu on näkyvissä. Vastaukset ovat kriittisiä ja reflektoivia. |
| **Hyvä (4)** | 75–89 % | Projekti toimii pääasiassa hyvin. Dokumentaatio on selvä. Turvallisuusriskit on tunnistettu. Esitys on selkeä. |
| **Tyydyttävä (3)** | 60–74 % | Projekti toimii, mutta voi olla puutteita. Dokumentaatio on perusvaatimukset täyttävä. Turvallisuusajattelu on alkeellinen. |
| **Välttävä (2)** | 45–59 % | Projekti toimii osittain tai dokumentaatio puutteellinen. Turvallisuusajattelu heikko. Esitys epäselvä. |
| **Hylätty (1)** | alle 45 % | Projekti ei toimi tai dokumentaatio puuttuu. Ei näyttöä ymmärryksestä. |

## Arviointikohteet yksityiskohtaisesti

### 1. Toiminnallisuus (30 %)

**Erinomainen (27–30):**
- Agentti tekee kaikki arvanneet askeleet
- Edge casea käsitellään hyvin
- Virheitä ei tule ilmi
- Live-demo toimii ilman ongelmia

**Hyvä (22–26):**
- Agentti tekee pääosassa askelista
- Joitain edge casea käsitellään
- Yksittäisiä virheitä, mutta ne eivät riko käyttöä
- Demo toimii pääosin

**Tyydyttävä (18–21):**
- Agentti tekee perusaskeleet
- Joitain edge casea ei käsitellä
- Virheiden käsittely heikkoa
- Demo toimii, mutta häiriöt mahdollisia

**Välttävä (13–17):**
- Agentti tekee joitain askelista
- Paljon edge casea käsittelemättä
- Virheet häiritsevät käyttöä
- Demo epävarma

**Hylätty (< 13):**
- Agentti ei toimi tai tekee vain osaa tehtävästään

### 2. Dokumentaatio (20 %)

**Erinomainen (18–20):**
- README on selkeä ja täydellinen
- ARCHITECTURE selittää rakennetta kirkkäasti
- SAFETY tunnistaa ja mitigoi riskit
- TESTING näyttää perusteellisen testaamisen
- Dokumentaatio on niin selvä, että joku muu voi käyttää sitä

**Hyvä (15–17):**
- README ja ARCHITECTURE selvät
- SAFETY tunnistaa riskit, mitigaatio osittainen
- TESTING näyttää testeja
- Dokumentaatio riittävä

**Tyydyttävä (12–14):**
- Perusdokumentaatio on olemassa
- README tai ARCHITECTURE puutteellinen
- SAFETY alkeellinen
- TESTING vähäinen

**Välttävä (9–11):**
- Dokumentaatio niukka
- Osista puuttuu sisältö
- Vaikeasti ymmärrettävää

**Hylätty (< 9):**
- Dokumentaatio puuttuu tai merkityksetön

### 3. Turvallisuus & Riskinarvio (20 %)

**Erinomainen (18–20):**
- Prompt injection -riskit tunnistettu
- Minimioikeus-periaate sovellettu
- Lokitus/audit trail suunniteltu
- Hyväksyntäportit tai pysäytysehdot määritelty
- Konkreettisia suojaustoimia toteutettu

**Hyvä (15–17):**
- Suurimmat riskit tunnistettu
- Minimioikeus osittain sovellettu
- Lokitus tai hyväksyntäportit olemassa
- Jotain suojaustoimia

**Tyydyttävä (12–14):**
- Joitain riskejä tunnistettu
- Turvallisuusajattelu alkeellinen
- Joitain toimia, mutta epätäydellisiä

**Välttävä (9–11):**
- Riskit tunnistettu heikosti
- Suojaus minimaalista
- Turvallisuusajattelu puuttuu

**Hylätty (< 9):**
- Ei näyttöä turvallisuusajattelusta

### 4. Demo-laatu ja Esittelytaito (15 %)

**Erinomainen (13–15):**
- Demo live ja toimiva
- Selkeä narratiivi (mikä → miksi → miten)
- Puhe selkeä ja vakuuttava
- Vastaukset kysymyksiin kriittiset

**Hyvä (11–12):**
- Demo toimii
- Narratiivi selvä
- Puhe ymmärrettävä
- Vastaukset asiallisia

**Tyydyttävä (9–10):**
- Demo toimii, mutta häiriöitä
- Narratiivi puutteellinen
- Puhe selkeä
- Vastaukset perustasoa

**Välttävä (7–8):**
- Demo epävarma
- Narratiivi epäselvä
- Vastauksissa häilyntää

**Hylätty (< 7):**
- Demo ei toimi tai esitys häiritsevä

### 5. Kriittinen Ajattelu & Reflektio (15 %)

**Erinomainen (13–15):**
- Osaa perustella valintoja ("miksi tämä lähestymistapa?")
- Tunnistaa projektin heikkoudet
- Osaa ajatella riskejä syvällisesti
- Näkee, mitä voisi parantaa

**Hyvä (11–12):**
- Perustelee joitain valintoja
- Näkee joitain heikkoja kohtia
- Ymmärtää riskejä
- Antaa parannusideoita

**Tyydyttävä (9–10):**
- Perustelu osittainen
- Tunnistaa joitain heikkoja kohtia
- Riskiymmärrys alkeellinen

**Välttävä (7–8):**
- Perustelu niukkaa
- Heikko riskiymmärrys

**Hylätty (< 7):**
- Ei ole ajatellut kriittisesti

## Valmistautuminen demoon

### Ennen demopäivää
1. Lue dokumentaatiosi ääneen — voisiko joku muu ymmärtää sen?
2. Testaa demoa useita kertoja — varmista, että se toimii
3. Harjoittele esitystä — mitä sanot? Kuinka kauan kestää?
4. Ajattele kysymyksiä — mitä opettaja tai vertaisopiskelijat kysyisivät?

### Demopäivänä
1. Saapuu ajoissa
2. Testaa tekniikkaa (järjestelmä, näytön jakaminen, jne.)
3. Näytä projektia, älä lukea diaa
4. Vastaa rehellisesti kysymyksiin
5. Kuuntele muiden demoja — asiallisesti, ilman häiriöistä

## Yhteenveto

OSP3-arviointi on muista poikkeava: se ei ole testi, vaan projektin esittely. Sinulla on koko kolme-neljä viikkoa rakentaa jotain oikeaa, dokumentoida se hyvin ja esitellä se selkeästi. Arvioinnissa näkyy, oletko oppinut agenttien teoriasta, rakentamisesta ja turvallisuudesta. Onnistuminen on se, että olet rakentanut jotain, josta olet ylpeä, ja pystyt selittämään sen muille.
