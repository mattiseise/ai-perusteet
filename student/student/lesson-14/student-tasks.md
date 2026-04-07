# Lesson 14: Opiskelijan tehtävät — Oman botin suunnittelu

## Tehtävä 14.1: Määrittele oma botti — tarkoitus, rooli ja ohjeet (TT-B)

**Tavoite:** Suunnitella oman botin kolme perusrakennuspalikkaa — tarkoitus, rooli ja ohjeet.

Valitse yksi seuraavista botin tyypeistä tai ehdota oma:
- Python-tutori-botti, joka opettaa aloittelijoille
- IT-helpdesk-botti, joka auttaa ongelmissa
- Asiakaspalvelu-botti verkkokaupalle
- Liiketoimintamentorin rooli nuorille yrittäjille

**Suunnittelulomake:**

```
OMAN BOTIN SUUNNITTELU

Botin tyyppi: [mitä botti tekee]

=== RAKENNUSPALIKKA 1: TARKOITUS ===

Mikä on selkeä, konkreettinen tarkoitus?
[kirjoita niin, että voit mitata onnistumisen]

Esimerkki:
- Huono: "Olla hyödyllinen"
- Hyvä: "Auttaa opiskelijoita ymmärtämään Python-loopeita interaktiivisten esimerkkien kautta"

Oma tarkoitukseni:
[vastaus]

Kuinka voin mitata onnistumisen?
[miten tiedät, että botti täytti tarkoituksensa?]

=== RAKENNUSPALIKKA 2: ROOLI ===

Kuka botti on? Mikä on sen asiantuntemus?
[kirjoita 2–3 lausetta: uskottava rooli]

Esimerkki:
"Olet kokenut Python-tutori, jolla on 10 vuoden opetuskokemus aloittelijoille."

Oma rooli:
[vastaus]

Miksi tämä rooli on uskottava tehtävääni varten?
[perustelu]

=== RAKENNUSPALIKKA 3: OHJEET ===

Mitkä ovat kolme tärkeintä ohjetta, jotka botille tulee antaa?
[kirjoita 3 konkreettista ohjeistusta]

Esimerkki:
1. Aloita aina peruskäsitteistä
2. Anna konkreettisia, ajettavia esimerkkejä
3. Kysy opiskelijalta, ymmärsikö hän

Omat ohjeet:
1. [ohje 1]
2. [ohje 2]
3. [ohje 3]

=== LISÄOSA: RAJAUKSET ===

Mitä botti EI saa tehdä? (Kirjoita vähintään 2)
[rajaukset suojaavat käyttäjää ja bottia]

Esimerkki:
- "En kirjoita valmiita projekteja — opiskelijat oppivat tekemällä"
- "En vastaa aiheisiin, jotka eivät liity Pythoniin"

Omat rajaukset:
1. [rajausta 1]
2. [rajausta 2]
```

**Arvioinnin kriteerit:**
- Tarkoitus on konkreettinen ja mitattavissa
- Rooli on uskottava ja perusteltu
- Ohjeet ovat selkeät ja johdattavat johdonmukaista käyttäytymistä
- Rajaukset suojaavat käyttäjää ja bottia

---

## Tehtävä 14.2: Kirjoita järjestelmäprompti (TT-B)

**Tavoite:** Kirjoittaa yksityiskohtainen järjestelmäprompti, joka ohjaa botin käyttäytymistä.

Käytä tehtävässä 14.1 suunnittelemaasi bottia. Nyt kirjoitat sen **järjestelmäpromptin**.

Järjestelmäprompti sisältää neljä osaa:
1. **Identiteetti:** Kuka botti on?
2. **Tarkoitus:** Mitä botti tekee?
3. **Ohjeet:** Miten botti käyttäytyy?
4. **Rajaukset:** Mitä botti ei saa tehdä?

**Kirjoitusohje:**

```markdown
JÄRJESTELMÄPROMPTI — OMAN BOTIN SYDÄN

[Identiteetti: 1–2 lausetta. Kuka olet? Mikä on taustasi?]

Esimerkki:
"Olet kokenut Python-ohjelmointitutori, jolla on 10 vuoden kokemus
opettamisesta aloittelijoille. Ymmärrät, miten nuoret oppivat."

Sinun identiteettisi:
[vastaus]

---

[Tarkoitus: 1–2 lausetta. Miksi olet olemassa?]

Esimerkki:
"Tarkoituksesi on auttaa opiskelijoita ymmärtämään Python-ohjelmointia
interaktiivisten esimerkkien ja kysymysten kautta."

Sinun tarkoituksesi:
[vastaus]

---

[Ohjeet: Neljä konkreettista sääntöä. Miten toimit?]

Esimerkki:
1. Aloita aina peruskäsitteistä. Älä hyppää heti monimutkaisiin asioihin.
2. Anna konkreettisia, ajettavia esimerkkejä jokaisesta käsitteestä.
3. Kysy opiskelijalta, ymmärsikö hän.
4. Jos oppilas tekee virheen, auta häntä löytämään virhe itse.

Sinun ohjeet:
1. [ohje 1]
2. [ohje 2]
3. [ohje 3]
4. [ohje 4]

---

[Rajaukset: Vähintään kaksi asiaa, joita et saa tehdä]

Esimerkki:
- En kirjoita valmiita projekteja. Opiskelijat oppivat tekemällä.
- En vastaa kysymyksiin, jotka eivät liity Pythoniin.

Sinun rajaukset:
- [rajausta 1]
- [rajausta 2]

```

**Lopullinen järjestelmäprompti (kopio):**

[Liitä tähän koko, lopullinen järjestelmäprompti, joka on valmis käyttöön]

**Arvioinnin kriteerit:**
- Järjestelmäprompti on yksityiskohtainen ja selkeä
- Identiteetti, tarkoitus, ohjeet ja rajaukset ovat kaikki läsnä
- Teksti on ammattilaismainen
- Botti-ohjaaja ymmärtää, miten botin pitäisi käyttäytyä

---

## Tehtävä 14.3: Esimerkki-interaktiot — näytä, miten botti käyttäytyy (TT-A)

**Tavoite:** Kirjoittaa 2–3 esimerkki-interaktiota, jotka näyttävät, miten botti vastaa eri tilanteissa.

Käytä tehtävistä 14.1 ja 16.2 luomaasi bottia. Kirjoita nyt konkreettisia esimerkkejä.

**Esimerkkien rakenne:**

Jokainen esimerkki on dialogi:
- Käyttäjä: [mitä käyttäjä kysyy tai sanoo]
- Botti: [miten botti vastaa — omat sanoin, ei yleinen]

**Esimerkki: Python-tutori-botti**

```
Käyttäjä: Mitä on muuttuja?

Botti: Hyvä kysymys! Ajattele muuttujaa kuin säiliötä. Liiteri voi sisältää
nauloja, ruuveja tai vasareita. Se on säiliö, joka pitää sisällään jotain.

Ohjelmoinnissa muuttuja toimii samalla tavalla. Se on nimetty paikka,
jossa voit säilyttää tietoja.

```python
nimi = "Liisa"
```

Tässä muuttuja on `nimi` ja se sisältää tekstin "Liisa".

Ymmärsikö tämän? Halusitko nähdä lisää esimerkkejä vai mennään seuraavaan asiaan?
```

**Kirjoita nyt kolme esimerki-interaktiota omalle bottillesi:**

**Esimerkki 1: Normaali tilanne**
```
Käyttäjä: [tavallinen kysymys]

Botti: [vastaus, joka näyttää botin rollia ja ohjeiden mukaista käyttäytymistä]
```

**Esimerkki 2: Vaikea tilanne — botti kieltäytyy tai ohjaa**
```
Käyttäjä: [kysymys, joka on botin rajauksien ulkopuolella]

Botti: [kuinka botti vastuullisesti kieltäytyy tai ohjaa]
```

**Esimerkki 3: Sekava tai epäselvä tilanne**
```
Käyttäjä: [epäselvä tai hajanainen kysymys]

Botti: [kuinka botti pyytää tarkennusta tai yksinkertaistaa]
```

**Arvioinnin kriteerit:**
- Esimerkit näyttävät botin persoonallisuutta ja ohjeiden mukaista käyttäytymistä
- Vaikea tilanne näyttää rajaukset käytännössä
- Botti kuulostaa yhdenmukaiselta ja uskottavalta jokaisessa esimerkissä

---

## Kotitehtävä

Valitse tehtävät 14.1 ja 14.2. Tee ne perusteellisesti.

**Palautus:**
- Tehtävä 14.1 (suunnittelulomake)
- Tehtävä 14.2 (järjestelmäprompti)
- Tehtävä 14.3 (kolme esimerkki-interaktiota)

Palauta seuraavalla tunnilla. Valmistaudu esittelemään oma botti.

**Bonus:** Jos olet kiinnostunut, kokeile järjestelmäpromptia todellisella AI:lla (ChatGPT, Claude jne.) ja dokumentoi, kuinka hyvin se toimi.

---

## Jos olet jumissa

Jos botin suunnittelu tuntuu vaikealta etkä tiedä mistä aloittaa, seuraa näitä viittä askelta:

**Askel 1:** Mieti yhtä asiaa, jota teet toistuvasti ja joka on tylsää. Se voi olla työ, koulu tai arki. Kirjoita se yhteen lauseeseen: "Minua ärsyttää, että joudun aina..."

**Askel 2:** Muuta se botin tarkoitukseksi: "Botti, joka auttaa [tekemään sen tylsän asian]."

**Askel 3:** Kirjoita kolme ohjetta, jotka antaisit ihmiselle, joka tekee sen asian puolestasi. Nämä ovat botin ohjeet.

**Askel 4:** Kirjoita yksi asia, jota botti ei saa tehdä. Mieti: mikä voisi mennä pieleen?

**Askel 5:** Kirjoita yksi esimerkkikeskustelu — mitä käyttäjä kysyisi ja mitä botti vastaisi. Jos tämä tuntuu luontevalta, suunnitelmasi on hyvä.
