# Tehtävät – Lesson 22: Agentin työkalut — haku, tiedostot, komennot

## Tehtävä 1: Työkalujen turvallisuus — whitelist-mallit

Rakennat agentin, jolla on pääsy kolmeen työkaluun: tiedostot (lukea/kirjoittaa), verkkohaku ja CLI-komennot. Jokaisen työkalun täytyy olla turvallinen.

### Tehtävä

Kutakin työkalua kohden suunnittele **whitelist** — luettelo, mitä agentti saa tehdä:

**Tiedostot**:
- Mitä kansiota agentti voi lukea?
- Mitä kansiota voi kirjoittaa?
- Mitä kansiota ei saa koskea?

**Verkkohaku**:
- Mitä sivustoja agentti voi hakea? (esim. vain Wikipedia, hallituksen sivustot)
- Mitä asiaa ei saa hakea? (henkilötiedot, salaisuudet)

**CLI**:
- Mitä komentoja agentti voi ajaa? (esim. `ls`, `mkdir`, mutta ei `rm`, `sudo`)

**Vastausmuoto**: Taulukko tai luetelma

---

## Tehtävä 2: Kolmen työkalun orkestrointi

Kuvittele analytiikka-agenttia, joka tekee myyntiraportin:

1. **Tiedosto**: Lukee `myyntitiedot_2026.csv`
2. **Verkkohaku**: Etsii markkinatrendejä ja kilpailijatietoja
3. **CLI**: Ajaa analyysiskriptin `python analyze_sales.py`

### Tehtävä

Kuvaile, kuinka nämä kolme työkalua toimivat **järjestyksessä**:
1. Mitä agentti tekee ensin?
2. Mitä tapahtuu toiseksi?
3. Mitä tapahtuu viimeksi?
4. Kuinka tulokset yhdistetään?

Kirjoita prosessia kuvaava lyhyt "skenaarion" (150–200 sanaa).

**Arviointikriteerit**: Näytät, että ymmärrät, kuinka työkalut syöttävät toisiinsa.

---

## Tehtävä 3: Riskianalyysi — entä jos menee pieleen?

Rakennat agentin, jolla on pääsy:
- Tiedostoihin: `/reports/` kansioon kirjoitus
- Verkkohakuun: Wikipedia ja hallituksen sivustot
- CLI-komentoihin: `ls`, `mkdir`, `cp`

### Tehtävä

Jokaiselle työkalulle: **Entä jos agentti tekee virheen?** Kuvaa kolme skenaariota:

**Tiedostot**: "Agentti kirjoittaa raportin väärään tiedostoon..."
**Verkkohaku**: "Agentti etsii salassa pitämiä tietoja..."
**CLI**: "Agentti kutsuu komentoa `rm -rf /reports/`..."

Kutakin kohden: mitä haittaa voi tulla? Miten sen olisit voinut estää?

**Vastausmuoto**: Kolme skenaariota, kunkin alla riski + ehkäisy

---

## Tehtävä 4: Agentin suunnittelu — oikea työkalu oikeaan tehtävään

Sinulla on kolme tehtävää:
- A: Asiakkaan laskun käsittely (tarvitaan tietoja tietokannasta)
- B: Päivittäisen kyberturvatilan raportti (internet + tiedostot)
- C: Palvelimen lokin analyysi (lokit ovat paikallisia tiedostoja)

### Tehtävä

Jokaiselle tehtävälle päätä:
1. Tarvitseeko **verkkohakua**? Miksi / miksi ei?
2. Tarvitseeko **CLI-komentoja**? Mitkä?
3. Tarvitseeko **tiedostojen kirjoitusoikeutta**? Minne?

Kirjoita **jokaisen tehtävän työkalulista** (mitä agentti tarvitsee).

---

---

## Tehtävä: Tutustu n8n-työnkulkuun — tunnista agentin osat

### Tavoite
Nähdä ensimmäistä kertaa, miltä tekoälyagentti näyttää oikeassa työkalussa. Et rakenna vielä mitään — tutkit valmiin esimerkin.

### Ohjeet

1. **Avaa n8n** selaimessa (opettaja antaa osoitteen).

2. **Tuo esimerkkityönkulku:**
   - Klikkaa ylävalikosta "Import from File"
   - Valitse tiedosto `esimerkki-agentti.json` (opettaja jakaa tämän)
   - Ruudullesi ilmestyy valmis työnkulku, jossa on 5 solmua (laatikkoa)

3. **Tunnista agentin osat.** Katso jokaista solmua ja vastaa:

   | Solmu (laatikko) | Mikä agentin osa tämä on? | Mitä se tekee? |
   |---|---|---|
   | Ensimmäinen (vasemmalla) | | |
   | Toinen | | |
   | Kolmas | | |
   | Neljäs | | |
   | Viimeinen (oikealla) | | |

   Käytä näitä vaihtoehtoja: **syötekäsittelijä**, **päättelijä**, **työkalu**, **turvakerros**, **tulosteen muotoilija**

4. **Jäljitä tiedon kulku.** Kirjoita omin sanoin (3–4 lausetta):
   - Mistä data tulee sisään?
   - Mitä sille tapahtuu matkalla?
   - Mitä tulee ulos?

5. **Yhdistä teoriaan.** Vastaa:
   - Mikä oppitunnin 22 työkalu (tiedostot, verkkohaku, komennot) on tässä työnkulussa käytössä?
   - Jos haluaisit lisätä toisen työkalun, minkä lisäisit ja miksi?

### Odotettu tuotos
- Täytetty taulukko (5 solmua tunnistettu)
- Lyhyt kuvaus tiedon kulusta
- Vastaus teoriakysymykseen

---

## Pisteet

- Tehtävä 1: Whitelistit ovat turvalliset ja perustelut selkeät
- Tehtävä 2: Työkalujen järjestys on looginen ja selitetty
- Tehtävä 3: Riskianalyysi on realistinen ja ehkäisyt käytännöllisiä
- Tehtävä 4: Työkalulistan valinnat perusteltuja tehtävän tarpeisiin
- n8n-tutustumis: Solmut tunnistettu oikein, tiedon kulku selitetty, teoriayhteys nähtävissä
