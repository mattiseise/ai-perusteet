# Lesson 18: Arviointitehtävä — OSP2 Portfolio

## OSP2 Arviointi: Tekoälyn käyttö IT-työssä

### Arviointitehtävä: Asiakasmyönnytys-järjestelmän kehittäminen

Sinulle annetaan seuraava IT-case:

**Konteksti:** Työskentelet IT-konsulttiyrityksen kehitystiimissä. Asiakas tarvitsee nopeasti "Feature Flag" -järjestelmän, joka antaa ylläpitäjille mahdollisuuden ottaa ominaisuuksia pois päältä ilman koodin uudelleenkäyttöönottoa. Esimerkiksi: "Ota maksujärjestelmä offline maanantaiaamuina ylläpidon vuoksi" tai "Testaa uusia ominaisuuksia 10%:lle käyttäjistä."

### Tehtävä

1. Suunnittele yksinkertainen feature flag -logiikka (esim. sanakirja, jossa avaimet ovat feature-nimiä, arvot boolean)
2. Pyydä tekoälyltä koodia — Python tai Bash (valitse yksi)
3. Testaa koodi paikallisesti vähintään 3 testisyötteellä
4. Dokumentoi koko prosessi: pyyntö, saatu koodi, testaus, löydetyt ongelmat, korjaukset
5. Korjaa löydetyt virheet

### Arviointikriteerit

| Taso | Pisteet | Kuvaus |
|------|---------|--------|
| **Erinomainen (5)** | 90–100 % | Prosessi on perusteellinen ja dokumentoitu. Tekoälyä käytetään strategisesti. Koodi on testattu normaalilla ja reunatapauksilla. Löydetyt ongelmat korjattu ja dokumentoitu. Ymmärrys on näkyvissä. |
| **Hyvä (4)** | 75–89 % | Tekoälyä käytetään hyvin. Koodi pyydetty selkeästi. Testaus kattava. Dokumentaatio hyvä. Ymmärrys lähes täydellinen. |
| **Tyydyttävä (3)** | 60–74 % | Tekoälyä käytetään, prosessi hieman satunnainen. Testaus olemassa, mutta voisi olla kattavampi. Dokumentaatio riittävä. Ymmärrys perus. |
| **Välttävä (2)** | 45–59 % | Tekoälyä käytetään vähän. Testaus minimaalinen. Dokumentaatio puutteellinen. Ymmärrys pinta-puolinen. |
| **Hylätty (1)** | alle 45 % | Tekoälyä ei käytty merkittävästi, koodi testaamaton, dokumentaatio puuttuu. |

### Arviointikohteet (20 pistettä yhteensä)

**1. Tekoälyn käyttö ja pyyntöjen laatu (4 p)**
- Pyyntö on selkeä ja sisältää kielen, version, syötteet, odotukset
- Olet iteroinut tai muokannut pyyntöä tarvittaessa
- Pyyntö näyttää, että ymmärrät, mitä haluat

**2. Koodin testaus (4 p)**
- Vähintään 3 testitapausta dokumentoitu
- Sekä normaaleja että edge case -testejä
- Dokumentoitu syöte, odotus ja todellinen tulos

**3. Virheiden löytäminen ja korjaus (4 p)**
- Oletko löytänyt ongelmia?
- Oletko korjannut ne?
- Korjaus on dokumentoitu ja testattu uudelleen

**4. Ymmärrys ja kommentit (4 p)**
- Koodi on kommentoitu
- Selitykset ovat omilla sanoilla (et vain kopioinut AI:n selitystä)
- Näytetään, että ymmärrät koodin logiikan

**5. Dokumentaatio (4 p)**
- Raportti kertoo koko prosessista
- Alkuperäinen pyyntö on näkyvissä
- Testitulokset dokumentoitu
- Johtopäätökset ovat perusteltuja

### Palautusvaatimukset

Palauta **kolme dokumentia**:

1. **Raportti** (1–2 A4-sivua)
   - Tehtävän kuvaus
   - Alkuperäinen tekoälyn pyyntö
   - Saatu koodi (lainaus)
   - Testauksen tulokset (taulukko tai lista)
   - Löydetyt ongelmat ja korjaukset
   - Johtopäätökset (mitä oppit?)

2. **Koodi** (silleen kommentoitu)
   - Lopullinen, toimiva versio
   - Jokainen rivi tai funktio on kommentoitu
   - Sisällytä sekä alkuperäinen että korjattu versio (selkeästi merkitty)

3. **Testidokumentti**
   ```
   TEST 1: [kuvaus]
   Input: [syöte]
   Expected: [odotus]
   Result: [saatu]
   Status: PASS / FAIL
   
   TEST 2: [seuraava]
   ...
   ```

### Vinkkejä onnistumiseen

1. **Pidä se yksinkertaisena** — 50–100 rivaa koodia riittää täysin
2. **Dokumentoi jokainen vaihe** — Opettaja haluaa nähdä prosessin
3. **Ole rehellinen virheiden kanssa** — Virheet ovat osa prosessia
4. **Testaa perusteellisesti** — Normaali + reunatapaukset
5. **Ymmärrä koodi** — Voit selittää sen ääneen kaverilasi

### Aikataulu

- Suunnittelu: 15 min
- Koodin pyytäminen ja testaaminen: 45 min
- Dokumentointi: 30 min
- **Yhteensä: ~90 minuuttia**

**Palautus:** [opettajan antama päivämäärä]
