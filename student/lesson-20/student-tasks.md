# Tehtävät

## Tehtävä 1: Täytä päätöstaulukko agentin rakenteesta (TT-B1)

Alla on taulukko, jossa kuvataan kolme erilaista agenttijärjestelmää. Sinun tehtäväsi on täyttää taulukko kuvaamalla kunkin agentin **suunnittelusilmukkaa**, **työkaluja** ja **muistia**.

### Kolme agenttijärjestelmää

**Agentti A: Sähköpostivastausten automatisoija**
- Tehtävä: Vastaa sisään tuleviin asiakassähköposteihin automaattisesti
- Tavoite: "Tunnista asiakkaan ongelma, etsi samankaltaisia tapauksia ja lähetä ratkaisu"

**Agentti B: Palvelimen valvonta-agentti**
- Tehtävä: Valvoo palvelimen tilaa ja tekee korjaavia toimintoja
- Tavoite: "Seuraa CPU-kuormaa, muistin käyttöä ja levytilaa. Jos nämä ylittävät kynnysarvot, käynnistä korjaavia toimintoja."

**Agentti C: Tietokannan optimointiagentti**
- Tehtävä: Analysoi tietokantakyselyjen tehokkuutta ja optimoi indeksit
- Tavoite: "Etsi hitaat kyselyt, analysoi ne ja lisää tai muokkaa indeksejä parantaakseen nopeutta."

### Täyttötaulukko

Täytä seuraava taulukko kunkin agentin osalta:

| Agentti | Suunnittelusilmukan vaiheet | Tarvittavat työkalut | Konteksti-ikkuna | Ulkoinen muisti | Huomiot |
|---------|-----------------------------|----------------------|------------------|-----------------|---------|
| **A: Sähköpostivastaukset** | 1. Havainnoi: Lue sähköposti 2. Suunnittele: ... 3. Toimi: ... 4. Tarkkaile: ... | Sähköpostin luku-API, tietokannanhaku-API, sähköpostin lähetys-API | Asiakkaan aiemmat sähköpostit (viimeiset 5 viestiä) | Ratkaisutietokanta: tunnetut ongelmat ja ratkaisut | [Täytä] |
| **B: Palvelimen valvonta** | [Täytä] | [Täytä] | [Täytä] | [Täytä] | [Täytä] |
| **C: Tietokannan optimointi** | [Täytä] | [Täytä] | [Täytä] | [Täytä] | [Täytä] |

### Ohjeita

- **Suunnittelusilmukan vaiheet**: Kuvaile, mitä agentti havaitsee, miten se suunnittelee, mitä se tekee ja miten se tarkkailee tuloksia.
- **Työkalut**: Listaa konkreettiset API:t tai keinot, joita agentti tarvitsee.
- **Konteksti-ikkuna**: Mitä lyhytaikaista tietoa agentti tarvitsee ymmärtääkseen tilanteen nyt?
- **Ulkoinen muisti**: Mitä pitkäaikaista tietoa agentti tarvitsee oppimista varten?
- **Huomiot**: Jos agentti voi vahingoittaa järjestelmää, mikä on riski? Mitä rajoituksia sille tulisi asettaa?

**Jos teet tehtävän yksin:** Voit olettaa, että jokainen näistä agenteista on todellinen järjestelmä, jota olet ohjannut työssä. Käytä tätä oletusta apuna taulukkoa täyttäessäsi.

---

## Tehtävä 2: Suunnittele kontrolli agentin rajoittamiseksi (TT-D1)

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
|-------|-----------|-------|
| Agentti lähettää väärän ratkaisun asiakkaalle | Agentti voi lähettää vain valmiiksi hyväksyttyjä mallivastauksia, ei vapaata tekstiä | Vähemmän joustavuutta, mutta parempi turvallisuus |
| Agentti sulkee tiketin liian aikaisin | Tiketti merkitään "ehdotettu ratkaisu" -tilaan, ja ihminen hyväksyy sulkemisen | Lisää ihmisen työtä, mutta estää tärkeiden tikettien sulkemisen |
| ... | ... | ... |

Kirjoita omat 3–4 riski–kontrolli-parisi.

**Jos teet tehtävän yksin:** Voit valita jonkin muun agentin, jota et pelkää, jos haluat. Tärkeintä on ymmärtää, miten kontrolleja suunnitellaan ja mitä ne maksavat.

---

## Pisteet ja arviointi

- **Tehtävä 1 (päätöstaulukko):** Taulukko on täytetty oikein, kuvailut ovat tarkkoja ja teknisesti oikeita.
- **Tehtävä 2 (kontrollisuunnitelma):** Riskit ovat realistisia, kontrollit ovat konkreettisia ja trade-offien pohdinta on syvällistä.

Molemmat tehtävät opettavat sinulle keskeistä osaamista: agenttien sisäisten mekanismien ymmärtämistä ja kykyä suunnitella turvallisia agenttijärjestelmiä.