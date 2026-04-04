# Käyttö-OSP:n arvioitava tehtävä: tekoälyn käyttö IT-työssä

## Johdanto

Oppitunnit 10–17 ovat käsitelleet tekoälyn käyttöä IT-ammatissa. Olet oppinut, miten käyttää chat-pohjaisia assistentteja, generatiivisia malleja, koodin tuottamista ja kehittämistä. Nyt on aika soveltaa kaikkea mitä olet oppinut yhteen kokonaisuuteen: **käytännön IT-tapaukseen, jossa käytät tekoälyä näkyvästi ja perustellusti.**

Tämä arvioitava tehtävä on OSP2:n kokonaisarviointi. Se mittaa, ovatko ymmärtänyt, kuinka tekoäly toimii IT-ammateissa, kuinka sitä käytetään vastuullisesti, ja kuinka dokumentoit prosessisi.

## Arviointitehtävä: Asiakasmyönnytys-järjestelmän kehittäminen

Sinulle annetaan seuraava tapaus:

**Konteksti:** Kuvittele, että työskentelet IT-konsulttiyrityksen kehitystiimissä. Asiakasyritys tarvitsee pikaisesti "Asiakasmyönnytys-palvelun" (feature flag system), joka antaa järjestelmän ylläpitäjille mahdollisuuden ottaa osia sovellusta pois päältä ilman uudelleenkäynnistystä. Esimerkiksi: "Ota maksujärjestelmä pois käytöstä maanantaiaamuina ylläpidon vuoksi" tai "Testi uusia ominaisuuksia 10%:lle käyttäjistä."

**Tehtävä:** Sinun pitää:
1. Suunnitella yksinkertainen feature flag -logiikka
2. Pyytää tekoälyltä koodia (Python tai Bash — valitse yksi)
3. Testata koodi paikallisesti
4. Dokumentoida prosessisi: mitä kysyit, mitä sait, mitä testasit, mitä löysit
5. Jos virheitä, korjata ne ja dokumentoida korjaus

## Arviointikriteerit

| Taso | Pisteet | Kuvaus |
|------|---------|--------|
| **Erinomainen (5)** | 90–100 % | Prosessi on perusteellinen ja dokumentoitu. Tekoälyä käytetään strategisesti (ei vain "anna minulle koodi"). Koodi on testattu pienin ja reunatapauksilla. Löydetyt ongelmat on korjattu ja dokumentoitu. Opiskelija näyttää ymmärryksen siitä, mitä koodi tekee ja miksi. |
| **Hyvä (4)** | 75–89 % | Tekoälyä käytetään hyvin. Koodi on pyydetty selkeästi. Testaus on kattava (normaalit ja osa edge casesia). Dokumentaatio on hyvä, mutta ehkä hieman puutteellinen. Ymmärrys on lähes täydellinen. |
| **Tyydyttävä (3)** | 60–74 % | Tekoälyä käytetään, mutta prosessi on hieman satunnaista. Koodi on testattu, mutta testaus voisi olla kattavampi. Dokumentaatio on olemassa, mutta selkeyden puutetta. Ymmärrys on riittävä, mutta ei syvä. |
| **Välttävä (2)** | 45–59 % | Tekoälyä käytetään, mutta prosessi on vähäinen. Testaus on minimaalista. Dokumentaatio on puutteellinen. Ymmärrys on pinta-puolinen. |
| **Hylätty (1)** | alle 45 % | Tekoälyä ei ole käytetty merkittävästi, koodi ei ole testattu, dokumentaatio puuttuu tai on virheellinen. |

## Arviointikohteet (pisteytetään asteikolla 0–20)

### 1. Tekoälyn käyttö — strategia ja pyyntöjen laatu (4 piste)
- Oletko kysyttävä selkeitä, spesifisiä pyyntöjä tekoälyltä?
- Kertoitko ohjelmointikielen, version, syötteet, odotukset?
- Oletko iteroinut (pyytänyt uudelleen, muokannut pyyntöä)?

**Esimerkki hyvästä:**
> "Kirjoita Python 3.10 -funktio, joka ottaa syötteeksi sanakirjan, jonka avaimet ovat feature-nimiä ja arvot boolean-arvoja (True = feature on käytössä). Funktio palauttaa False, jos mitään 'database_migration' -featureita on käytössä. Käytä lambda-funktiota."

**Esimerkki huonosta:**
> "Kirjoita koodi joka tekee jotain"

### 2. Koodin testaus ja verifiointi (4 piste)
- Oletko testannut koodia paikallisesti?
- Oletko testannut normaaleita tapauksia ja reunatapauksia?
- Oletko dokumentoinut testitulokset (tulosteet, mitä testasit)?

**Dokumentaatioesimerkki:**
```
TESTAUS:
Test 1 — Normal case:
  Input: {'payment': True, 'analytics': False}
  Expected: Payment ON, Analytics OFF
  Result: PASS ✓

Test 2 — Edge case (tyhjä sanakirja):
  Input: {}
  Expected: ???  (KORJAUS TARVITAAN)
  Result: FAIL
```

### 3. Ongelmat ja korjaukset (4 piste)
- Oletko löytänyt ongelmia koodissa?
- Oletko korjannut ne (joko itse tai pyytämällä tekoälyltä)?
- Oletko dokumentoinut korjaukset?

**Esimerkki:**
> "Alkuperäinen koodi ei käsitellyt tyhjää sanakirjaa. Pyysin tekoälyltä: 'Lisää tarkistus, jos sanakirja on tyhjä, palauta True (kaikki featuret ovat käytössä oletuksena).' Koodi korjattiin."

### 4. Ymmärrys ja dokumentaatio (4 piste)
- Oletko selittänyt, mitä koodi tekee?
- Oletko näyttänyt, että ymmärrät logiikan?
- Oletko kirjoittanut kommentit koodiin?

**Esimerkki:**
```python
# Funktio tarkistaa, onko feature_flag käytössä
# Ottaa syötteeksi sanakirjan {feature_name: bool}
# Palauttaa True, jos feature on käytössä, False jos ei

def is_feature_enabled(flags, feature_name):
    # Oletuksena feature on pois päältä (False), jos sitä ei löydy
    return flags.get(feature_name, False)
```

### 5. Koko prosessin dokumentaatio (4 piste)
- Oletko luonut lyhyen raportin, joka kertoo koko prosessista?
  - Mitä tehtävä oli?
  - Mitä pyysit tekoälyltä (näytä alkuperäinen pyyntö)?
  - Mitä sait?
  - Mitä testasit?
  - Mitä löysit?
  - Mitkä olivat viimeiset korjaukset?

Raportissa pitäisi näkyä: **kokonaisuus** siitä, miten käytit tekoälyä ratkaista ongelmaa.

## Palautusvaatimukset

Palauta seuraavat dokumentit (tekstitiedostot tai PDF):

1. **Raportti** (1–2 sivua)
   - Tehtävän kuvaus
   - Tekoälyn pyyntö (alkuperäinen versio)
   - Mitä sait
   - Testauksen tulokset
   - Löydetyt ongelmat ja korjaukset
   - Johtopäätökset

2. **Koodi** (kommentoinut)
   - Alkuperäinen tekoälyn tuottama koodi
   - Lopullinen (korjattu) koodi
   - Jokainen rivi kommentoitu

3. **Testidokumentti**
   - Mitä testasit
   - Mitkä olivat syötteet
   - Mitkä olivat odotukset
   - Mitkä olivat tulokset

## Vinkkejä onnistumiseen

1. **Ei suuri projekti** — Pidä se yksinkertaisena. 50–100 rivaa koodia riittää.
2. **Dokumentoi jokainen askel** — Näytä, mitä teit. Opettaja haluaa nähdä prosessin, ei vain lopputulosta.
3. **Ole rehellinen virheistään** — Jos tekoäly antoi väärää koodia, se on OK. Dokumentoi se ja korjaa.
4. **Tarkista perusteita** — Ymmärrä koodi. Jos et ymmärrä, kysy opettajalta.
5. **Tarkista tietoturva** — Mitä turvattomuusriskejä näet? Dokumentoi ne.

## Esimerkki (pidempi dokumentaatio)

**RAPORTTI:**

**Tehtävä:** Kehitä yksinkertainen feature flag -järjestelmä, jonka avulla järjestelmän ylläpitäjät voivat ottaa sovelluksen ominaisuuksia pois käytöstä.

**Tekoälyn pyyntö (versio 1):**
> Kirjoita Python-funktio, joka tarkistaa feature flag -asetukset. Saatetaan sanakirja, jossa avaimet ovat feature-nimiä ja arvot boolean-arvoja.

**Saatu koodi:**
```python
def check_flag(flags, name):
    return flags[name]
```

**Testaus:**
- Test 1: `check_flag({'payment': True}, 'payment')` → True ✓
- Test 2: `check_flag({'payment': True}, 'unknown')` → KeyError ✗

**Ongelma löydetty:** Funktio kaatuu, jos feature-nimea ei löydy.

**Tekoälyn pyyntö (versio 2):**
> Muokkaa funktiota. Jos feature-nimea ei löydy, palauta False (feature on oletuksena pois).

**Lopullinen koodi:**
```python
def check_flag(flags, name):
    return flags.get(name, False)
```

**Testaus uudelleen:**
- Test 1: `check_flag({'payment': True}, 'payment')` → True ✓
- Test 2: `check_flag({'payment': True}, 'unknown')` → False ✓

**Johtopäätös:** Tekoäly auttoi, mutta testaus paljasti ongelman. Iteraation jälkeen koodi on nyt toimivaa ja turvallista.

---

**Aloita nyt.** Valitse yksi yksinkertainen feature (esim. feature flagit, käyttäjän validointi, log-parseri), käytä tekoälyä, testaa ja dokumentoi. Prosessi on tärkeämpi kuin lopputulos.
