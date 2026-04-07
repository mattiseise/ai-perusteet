# Opettajan johtamat tehtävät – Lesson 23

## Aktiviteetti 1: ReAct-malli (20 min)

**Selitys**: ReAct = Reasoning + Acting. Ajatella → tehdä → ajatella → tehdä.

**Esittely**: Näytä esimerkki. Asiakas kysyy "Mikä on tuotteen hinta?" Näytä lokit:

```
[AJATTELU]: Asiakkaan kysymys koskee tuotteen hintaa. Minun täytyy hakea se tietokannasta.
[TOIMINTA]: GET /api/product?id=12345 -> Hinta: 45€
[AJATTELU]: Tietokanta antoi hinnan. Nyt tiedän vastauksen.
[TOIMINTA]: "Tuotteen hinta on 45€"
```

**Ryhmätyö**: Opiskelijat valitsevat tilanteen (esim. palautuspyyntö, tekniikkaongelma). He kirjoittavat ReAct-prosessin lokeissa näkyvillä.

**Esitys**: Ryhmät esittelevät prosessiaan. Keskustelu: "Miten jokainen ajatteluvaihe auttaa seuraavaa vaihetta?"

---

## Aktiviteetti 2: Ketjuajattelu (20 min)

**Selitys**: Chain-of-thought = numeroitu lista vaiheista. Yksi kerrallaan.

**Esittely**: Palautuspyynnön käsittely:
1. Mikä on pyyntö?
2. Onko palautusaika voimassa?
3. Mitä käytäntö sanoo?
4. Mitä päätös?

**Ryhmätyö**: Opiskelijat valitsevat prosessin (tilauksen käsittely, sairaalan ajanvaraus, jne.). He kirjoittavat kaikki vaiheet järjestyksessä.

**Tärkeä**: "Entä jos vaiheista puuttuu jokin? Mitä menee pieleen?"

---

## Aktiviteetti 3: Mallin valinta (15 min)

**Selitys**: ReAct = joustava, ketjuajattelu = vakaa. Milloin mitä?

**Esittely**: 
- ReAct, kun agentti ei tiedä tarkkaan, mitä seuraavaksi (tutkiva ajattelu)
- Ketjuajattelu, kun vaiheet ovat selvät ja sama joka kerta

**Ryhmätyö**: Opiskelijat saavat 4 tilanteen. He päättävät, kumpi malli sopii.

---

## Aktiviteetti 4: Moniagenttijärjestelmä (20 min)

**Selitys**: Useita agentteja, jotka tekevät yhteistyötä. Hierarkkinen tai yhteistyö.

**Esittely**: Asiakaspalvelupyynnön käsittely:
1. Analyysi-agentti lukee viestin
2. Haku-agentti hakee historian
3. Kirjoitus-agentti laatii vastauksen
4. Validointi-agentti tarkistaa

**Ryhmätyö**: Opiskelijat suunnittelevat moniagenttijärjestelmää jollekin tehtävälle. He päättävät:
- Kuinka monta agenttia?
- Mikä on johtaja?
- Kuinka tieto kulkee?

**Esitys**: Ryhmät piirtävät kaavion.

---

## Herättimet

- "Mitä tapahtuu, jos ReAct iteroi liian kauan?"
- "Voiko ketjuajattelu epäonnistua?"
- "Milloin moniagenttijärjestelmä on overkill?"
