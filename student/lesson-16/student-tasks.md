# Lesson 16: Opiskelijan tehtävät

## Tehtävä 1: Pyydä koodi — dokumentoi prosessi (C1-TT)

**Tavoite:** Käyttää tekoälyä koodin tuottamiseen ja dokumentoida prosessi selkeästi.

Valitse yksi alla olevista pienistä skriptitehtävistä tai anna opettajasi valita sinulle:

1. Python-skripti, joka lukee tekstitiedoston ja laskee, kuinka monta sanaa siinä on
2. Bash-skripti, joka listaa kansiossa olevat tiedostot ja niiden koot
3. Python-funktio, joka ottaa syötteeksi nimen ja palauttaa "Hello, [nimi]!"
4. Python-funktio, joka tarkistaa, onko luku parillinen vai pariton

**Dokumentointilomake:**

```
KOODIN TUOTTAMISEN PROSESSI

Tehtävä: [mitä sinua pyydettiin tekemään]

VAIHE 1: PYYNTÖ
Tekoäly-kehotus (järjestelmä, mallia, yksityiskohdat):
[kirjoita täsmällinen pyyntö, jonka lähetit tekoälylle]

Esimerkki hyvästä pyynnöstä:
[ovatko sisällyttänyt kielen, version, syötteen, tuloksen? Kyllä / Ei]

VAIHE 2: SAATU KOODI
Alkuperäinen koodi:
[liitä tulos tai kirjoita se tähän]

Koodi näyttää: [ ] Hyvälle [ ] Epäilyttävän [ ] Väärältä
Miksi: [lyhyt selitys]

VAIHE 3: TESTAUS
Testitapaus 1:
  Syöte: [mitä annoit]
  Odottu tulos: [mitä odotit]
  Todellinen tulos: [mitä sait]
  Toimiko? [ ] Kyllä [ ] Ei

Testitapaus 2:
  Syöte: [toinen syöte]
  Odottu tulos: [odotus]
  Todellinen tulos: [tulos]
  Toimiko? [ ] Kyllä [ ] Ei

[Vähintään 2 testitapausta]

VAIHE 4: YMMÄRRYS
Mitä koodi tekee? [Kirjoita 2-3 lauseella selitys, jonka ymmärrät]

Miksi tämä rivi on tärkeä:
[valitse yksi merkittävä koodirivi ja selitä, miksi se on tärkea]

VAIHE 5: JOHTOPÄÄTÖKSET
Kelpuuttiko koodi? [ ] Kyllä, käyttökelpoinen [ ] Kyllä, pienillä muutoksilla [ ] Ei, tarvitsee korjaus

Jos tarvitsee korjausta, mikä meni pieleen?
[selitys]
```

**Arvioinnin kriteerit:**
- Pyyntö on selkeä ja sisältää kaikki tarvittavat tiedot
- Testaus on dokumentoitu (vähintään 2 tapausta)
- Ymmärrys on näkyvissä (selitykset omilla sanoilla)
- Johtopäätös on perusteltu

---

## Tehtävä 2: Vertaile pyyntöjä — miksi laatu vaikuttaa (A1-TT)

**Tavoite:** Nähdä, kuinka pyyntöjen laatu vaikuttaa saatuun koodiin.

Valitse yksittävä tehtävä (esim. "lukea CSV-tiedosto"). Lähetä kolme eri pyyntöä samasta asiasta:

**Pyyntö A (huono):**
```
Kirjoita funktio, joka lukee dataa
```

**Pyyntö B (parempi):**
```
Kirjoita Python-funktio, joka lukee CSV-tiedoston
```

**Pyyntö C (hyvä):**
```
Kirjoita Python 3.10 -funktio nimeltä read_csv_data, joka:
- Ottaa parametriksi tiedoston nimen (merkkijono)
- Lukee CSV-tiedoston (pilkkuerotteluilla)
- Palauttaa listan sanakirjoja (jokainen rivi on sanakirja, sarakkeet ovat avaimet)
- Käsittelee virheet: jos tiedostoa ei löydy, palauttaa tyhjän listan
```

**Vertailulomake:**

```
PYYNTÖJEN VERTAILU

Tehtävä: [mikä tehtävä]

| Aspekti | Pyyntö A | Pyyntö B | Pyyntö C |
|---------|----------|----------|----------|
| Kieli määritelty? | [ ] Ei | [ ] Kyllä | [ ] Kyllä |
| Versio määritelty? | [ ] Ei | [ ] Ei | [ ] Kyllä |
| Syötteet selitetty? | [ ] Ei | [ ] Osittain | [ ] Kyllä |
| Palautus selitetty? | [ ] Ei | [ ] Osittain | [ ] Kyllä |
| Virheet käsitelty? | [ ] Ei | [ ] Ei | [ ] Kyllä |

Saadun koodin laatu:
- Pyyntö A: [ ] Hyvä [ ] OK [ ] Huono
  Miksi: [selitys]

- Pyyntö B: [ ] Hyvä [ ] OK [ ] Huono
  Miksi: [selitys]

- Pyyntö C: [ ] Hyvä [ ] OK [ ] Huono
  Miksi: [selitys]

Johtopäätös: Mitä oppisit pyyntöjen laadusta?
[vastaus]
```

**Arvioinnin kriteerit:**
- Kaikki kolme pyyntöä on lähetetty
- Vastaukset ovat dokumentoituja
- Vertailu näyttää, kuinka yksityiskohtaisuus vaikuttaa tulokseen

---

## Kotitehtävä

Valitse tehtävä 1 tai 2. Tee sitä vähintään 45 minuuttia. Palauta dokumentointilomake opettajallesi seuraavalla tunnilla.

**Bonus:** Jos haluat, tee molemmat tehtävät.
