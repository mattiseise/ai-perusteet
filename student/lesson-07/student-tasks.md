# Opiskelutehtävät: Gen AI:n luonne

## Tehtävä 1: Testaa epädeterminismi ja lämpötila

### Tavoite
Ymmärtää käytännössä, miten epädeterminismi ja lämpötila vaikuttavat AI:n vastauksiin.

### Ohjeet

1. **Valitse AI-palvelu** (ChatGPT, Claude, tai muu, jonka käyttöliittymässä voit säätää lämpötilaa tai "creativity"-tasoa).

2. **Kirjoita sama promt neljä kertaa, eri säädöillä:**
   - Alin lämpötila/creativity-asetus (esim. "precise" tai 0,1)
   - Matala asetus (esim. 0,5)
   - Korkea asetus (esim. 1,0)
   - Alin asetus uudelleen (tarkista, onko vastaus sama kuin ensimmäinen)

3. **Prompt voi olla esim.:**
   - "Kirjoita lyhyt, tekninen kuvaus siitä, mitä Python-funktio tekee"
   - "Ideoida kolme nimen ominaisuutta uudelle sovellukselle"

4. **Täytä taulukko:**

| Asetus | Vastaus (lyhenne) | Johdonmukaisuus | Luovuus | Selkeä ero edellisestä |
|---|---|---|---|---|
| Alin (1. yritys) | | | | |
| Matala | | | | |
| Korkea | | | | |
| Alin (2. yritys) | Sama kuin 1:n vai eri? | | | |

5. **Kirjoita pohdinnat (2–3 lausetta):**
   - Huomasitko, että vastaukset vaihtelivat? Missä eniten?
   - Oliko alin asetus todella deterministinen (sama vastaus kahdesti)?
   - Minkä säädön olisit valinnut, jos kirjoittaisit API-dokumentaatiota? Entä markkinointitekstejä?

---

## Tehtävä 2: Etsi hallusinaatiot

### Tavoite
Oppia tunnistamaan hallusinaatioita ja ymmärtämään, miksi niitä syntyy.

### Ohjeet

1. **Kysy AI:lta jokin tekninen kysymys, johon vastaus on helppo verifioidä:**
   - "Mikä on Pythonin urllib3-kirjaston oikea funktio tekemään HTTP GET -pyynnölle?"
   - "Mitkä ovat JavaScript-funktion `Array.map()` ensimmäiset kolme parametriä?"
   - "Mikä on Microsoftin Windows-komentoriville komento näyttämään tiedostojen koot?"

2. **Kopioi vastaus taulukkoon.**

3. **Tarkista vastaus kolmesta lähteestä:**
   - Virallinen dokumentaatio (docs.python.org, developer.mozilla.org, jne.)
   - Kokeile koodi käyttämällä (jos mahdollista)
   - Googlen haku

4. **Täytä taulukko:**

| Kysymys | AI:n vastaus | Dokumentaation vastaus | Oikein vai väärin | Hallusinaation merkkejä |
|---|---|---|---|---|
| [Esim. urllib3 GET] | | | | |

5. **Kirjoita analyysi (3–4 lausetta):**
   - Oliko vastaus hallusinaatio? Mitä merkkejä huomasit?
   - Oliko vastaus "näyttävä" mutta väärä, vai selvästi epävarma?
   - Miksi malli halusinoi tämä?

---

## Tehtävä 3: Suunnittele verifiointiprosessi

### Tavoite
Oppia, miten integroida AI-apua työhön ilman, että hallusinaatiot pääsevät virheiksi.

### Ohjeet

**Skenaario:** Työskentelit kehittäjänä ja käytät ChatGPT:tä kirjoittamaan koodia, joka luettelee kaikki tietokantaan tallennetut käyttäjät. Haluat varmistaa, että koodi on turvallinen ja toimii.

**Tehtävä:** Suunnittele 5-vaiheinen verifiointiprosessi.

**Täytä lista:**

1. **Ennen kuin kysy ChatGPT:tä:**
   - Mitä sinulla täytyy jo tietää? (Esim. tietokannan schema)

2. **Kun kysyt ChatGPT:tä:**
   - Miten kirjoitat promptin, jotta saat järkevät vastaukset?
   - Mitä yksityiskohtia pyydät?

3. **Kun saat vastauksen:**
   - Mihin asioihin kiinnität huomiota? (Syntaksi, logiikka, turvallisuus...)
   - Mistä merkeistä epäilet hallusinaatiota?

4. **Testaus ja validointi:**
   - Mitä testejä ajet ennen kuin käytät koodia tuotannossa?
   - Miten tarkistat, että se ei julkaise tietokantaa turvattomasti?

5. **Dokumentointi:**
   - Mitä kirjoitat muistiinpanoihin, jotta muut kääntävät sen, mitä ChatGPT:lle pyysit ja miksi?

---

## Ohjeet tehtäviin

- **Tehtävät 1 ja 2** voidaan tehdä yksin tai pareittain.
- **Tehtävä 3** kannattaa tehdä pareittain tai pienryhmässä, jotta voit keskustella valintaisista verifiointikeinoista.
- **Kirjaa vastaukset taulukkoihin ja analyyseiksi**, joita voit näyttää opettajalle.

---

## Odotettu tuotos

**Tehtävä 1:**
- Täytetty taulukko neljällä eri säädöllä
- Pohdinnat, jotka näyttävät ymmärryksen epädeterminismistä

**Tehtävä 2:**
- Vähintään yksi hallusinaatio tunnistettu
- Vertailu viralliseen dokumentaatioon
- Analyysi hallusinaation syystä

**Tehtävä 3:**
- Viiden vaiheen verifiointiprosessi
- Konkreettiset testit ja dokumentointikäytännöt
