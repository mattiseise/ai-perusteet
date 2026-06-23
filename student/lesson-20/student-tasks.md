# Tehtävät

## Tehtävä 1: Täytä päätöstaulukko agentin rakenteesta

Alla on taulukko, jossa kuvataan kolme erilaista agenttijärjestelmää. Sinun tehtäväsi on täyttää taulukko kuvaamalla kunkin agentin **suunnittelusilmukkaa**, **työkaluja** ja **muistia**.

### Kolme agenttijärjestelmää

**Agentti A: Sähköpostivastausten automatisoija**
- Tehtävä: Vastaa sisään tuleviin asiakassähköposteihin automaattisesti
- Tavoite: "Tunnista asiakkaan ongelma, etsi samankaltaisia tapauksia ja lähetä ratkaisu"

**Agentti B: Varaston valvonta-agentti**
- Tehtävä: Valvoo varaston tilaa ja tekee tilauksia
- Tavoite: "Seuraa tuotteiden määriä, menekkiä ja viimeisiä käyttöpäiviä. Jos jokin tuote on loppumassa, tee uusi tilaus toimittajalle."

**Agentti C: Tapahtuman aikatauluagentti**
- Tehtävä: Suunnittelee ja optimoi tapahtuman ohjelman aikataulua
- Tavoite: "Etsi päällekkäisyydet ja ruuhka-ajat, analysoi ne ja siirrä ohjelmanumeroita niin, että aikataulu toimii sujuvasti."

### Täyttötaulukko

Täytä seuraava taulukko kunkin agentin osalta:

| Agentti | Suunnittelusilmukan vaiheet | Tarvittavat työkalut | Konteksti-ikkuna | Ulkoinen muisti | Huomiot |
| --- | --- | --- | --- | --- | --- |
| **A: Sähköpostivastaukset** | 1. Havainnoi: Lue sähköposti 2. Suunnittele: ... 3. Toimi: ... 4. Tarkkaile: ... | Sähköpostin luku-API, tietokannanhaku-API, sähköpostin lähetys-API | Asiakkaan aiemmat sähköpostit (viimeiset 5 viestiä) | Ratkaisutietokanta: tunnetut ongelmat ja ratkaisut | [Täytä] |
| **B: Varaston valvonta** | [Täytä] | [Täytä] | [Täytä] | [Täytä] | [Täytä] |
| **C: Tapahtuman aikataulu** | [Täytä] | [Täytä] | [Täytä] | [Täytä] | [Täytä] |

### Ohjeita

- **Suunnittelusilmukan vaiheet**: Kuvaile, mitä agentti havaitsee, miten se suunnittelee, mitä se tekee ja miten se tarkkailee tuloksia.
- **Työkalut**: Listaa konkreettiset API:t tai keinot, joita agentti tarvitsee. (**API** = rajapinta, jonka kautta ohjelmat puhuvat keskenään — esimerkiksi sähköpostin luku- tai lähetysrajapinta.)
- **Konteksti-ikkuna**: Mitä lyhytaikaista tietoa agentti tarvitsee ymmärtääkseen tilanteen nyt?
- **Ulkoinen muisti**: Mitä pitkäaikaista tietoa agentti tarvitsee oppimista varten?
- **Huomiot**: Jos agentti voi vahingoittaa järjestelmää, mikä on riski? Mitä rajoituksia sille tulisi asettaa?

**Jos teet tehtävän yksin:** Voit olettaa, että jokainen näistä agenteista on todellinen järjestelmä, jota olet ohjannut työssä. Käytä tätä oletusta apuna taulukkoa täyttäessäsi.

---

## Tehtävä 2: Suunnittele kontrolli agentin rajoittamiseksi

Agentit ovat tehokkaita, mutta niihin liittyy merkittäviä riskejä. Tämä tehtävä vaatii sinua **suunnittelemaan turvatoimenpiteet** agentin varalle.

### Tilanne

Sinulla on agentti, joka hoitaa asiakastukitikettejä. Agentti voi:
- Lukea asiakastukitietokantaa
- Etsiä ratkaisuja knowledge base -tietokannasta
- Lähettää sähköposteja asiakkaille
- Merkitä tikettejä "ratkaistuiksi" ja sulkea niitä

Tavoite kuulostaa hyvältä — automatisoida tuki. Mutta mitä pahaa voisi tapahtua?

### Ohjeet

Kirjoita agenttijärjestelmälle **kontrollisuunnitelma**, joka kuvailee:

1. **Riskit** — Mitä voisi mennä pieleen? Anna 3–4 konkreettista vaaratapausta.
2. **Kunkin riskin mukainen kontrolli** — Miten voisit estää sen? Vaihtoehdot:
   - Rajaa agentin työkalut (esim. agentti voi lähettää vain malleja, ei vapaata tekstiä)
   - Lisää ihminen silmukkaan (esim. tiketit merkitään ratkaistuiksi vasta, kun ihminen hyväksyy ne)
   - Lisää valvontaa (esim. kirjaa kaikki agentin tekemät sähköpostit)
   - Testaa agenttia (esim. testaa, että agentti ei lähetä sopimattomia tekstejä)
3. **Trade-offs** — Mikä on jokaisen kontrollin hinta? Vaikuttaako se automaation nopeuteen? Lisääkö se työtä ihmisille?

### Esimerkki

| Riski | Kontrolli | Hinta |
| --- | --- | --- |
| Agentti lähettää väärän ratkaisun asiakkaalle | Agentti voi lähettää vain valmiiksi hyväksyttyjä mallivastauksia, ei vapaata tekstiä | Vähemmän joustavuutta, mutta parempi turvallisuus |
| Agentti sulkee tiketin liian aikaisin | Tiketti merkitään "ehdotettu ratkaisu" -tilaan, ja ihminen hyväksyy sulkemisen | Lisää ihmisen työtä, mutta estää tärkeiden tikettien sulkemisen |
| ... | ... | ... |

Kirjoita omat 3–4 riski–kontrolli-parisi.

**Jos teet tehtävän yksin:** Voit valita jonkin muun agentin, jota et pelkää, jos haluat. Tärkeintä on ymmärtää, miten kontrolleja suunnitellaan ja mitä ne maksavat.

---

## Hyvän vastauksen tuntomerkit

- **Tehtävä 1 (päätöstaulukko):** taulukko on täytetty oikein, kuvailut ovat tarkkoja ja teknisesti oikeita.
- **Tehtävä 2 (kontrollisuunnitelma):** riskit ovat realistisia, kontrollit konkreettisia ja kompromissien pohdinta syvällistä.

Molemmat tehtävät opettavat sinulle keskeistä osaamista: agenttien sisäisten mekanismien ymmärtämistä ja kykyä suunnitella turvallisia agenttijärjestelmiä.

---
