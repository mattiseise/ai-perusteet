# Opettajavetoiset tehtävät — oma botti

## Tehtävä 14.1: Oman botin rakennuspalikkojen esittely noin 20 minuuttia

### Tavoite

Tehtävän tavoitteena on osoittaa konkreettisesti, miten oma **botti** rakennetaan neljästä perusosasta: **tarkoituksesta**, **roolista**, **ohjeista** ja **rajauksista**.

**Opettajan painotus:** Korosta, että botti ei ole vain yleinen tekoälychat uudella nimellä. Hyvä botti on suunniteltu tiettyä käyttötarkoitusta varten, ja sen toimintaa ohjataan tarkoituksen, roolin, ohjeiden ja rajausten avulla.

### Opettajan ohjeet ja fasilitointi

Tämä tehtävä tehdään opettajan johdolla koko luokan kanssa. Havainnollistava esittely näyttää, miten botin suunnittelu etenee vaihe vaiheelta.

### Valmistelu ennen lähiosaa

- Valitse yksi konkreettinen botti, esimerkiksi **Python-tutori**, **helpdesk-botti** tai **asiakaspalvelubotti**. Demoksi sopii yhtä hyvin ei-IT-aiheinen botti — esimerkiksi helpdesk-botin sijaan harrastusneuvoja.
- Testaa botin neljä rakennuspalikkaa etukäteen: **tarkoitus**, **rooli**, **ohjeet** ja **rajaukset**.
- Valmista lyhyt esimerkkikeskustelu, joka näyttää, miten botti käyttäytyy käytännössä.

### Tehtävän vaiheet noin 20 minuuttia

#### Vaihe 1: Johdanto noin 2 minuuttia

Kerro opiskelijoille:

> Olette nyt opiskelleet, miten tekoälyä käytetään työkaluna, miten siltä kysytään ja miten sen vastauksia arvioidaan. Seuraava askel on suunnitella **oma botti**, joka sopii tiettyyn tarpeeseen.

Jatka:

> Oma botti ei ole vain ChatGPT uudella nimellä. Se on tekoälyjärjestelmä, jolle annetaan selkeä tarkoitus, rooli, ohjeet ja rajaukset.

#### Vaihe 2: Rakennuspalikka 1 — tarkoitus noin 4 minuuttia

Näytä opiskelijoille kaksi esimerkkiä:

- **Huono tarkoitus:** `Auta opiskelijoita.`
- **Hyvä tarkoitus:** `Auta opiskelijoita ymmärtämään Pythonin silmukoita interaktiivisten esimerkkien avulla.`

Kysy opiskelijoilta:

- Mitä eroa näissä kahdessa tarkoituksessa on?
- Kumpi kertoo paremmin, mitä botin pitäisi tehdä?
- Kumpaa tarkoitusta olisi helpompi arvioida tai testata?

Selitä:

> Hyvä tarkoitus on **konkreettinen** ja mahdollisimman **arvioitavissa**. Jos tarkoitus on liian yleinen, botti toimii helposti epämääräisesti.

#### Vaihe 3: Rakennuspalikka 2 — rooli noin 4 minuuttia

Näytä esimerkki roolista:

Olet kokenut Python-ohjelmoinnin tutori, jolla on kokemusta aloittelijoiden opettamisesta selkeiden esimerkkien avulla.

Kysy opiskelijoilta:

- Miksi rooli on tärkeä?
- Miten vastaus muuttuisi, jos sanoisimme vain “olet botti”?
- Miten rooli vaikuttaa vastauksen sävyyn ja tyyliin?

Selitä:

> Rooli ohjaa botin näkökulmaa, sävyä ja tapaa vastata. Hyvä rooli tekee botista johdonmukaisemman ja auttaa käyttäjää ymmärtämään, millaista apua botilta voi odottaa.

#### Vaihe 4: Rakennuspalikka 3 — ohjeet noin 4 minuuttia

Näytä neljä konkreettista ohjetta Python-tutori-botille:

1. Aloita aina peruskäsitteistä.
2. Anna konkreettisia ja ajettavia esimerkkejä.
3. Kysy opiskelijalta, ymmärsikö hän selityksen.
4. Jos opiskelija tekee virheen, auta häntä löytämään virhe itse sen sijaan, että annat heti valmiin vastauksen.

Kysy opiskelijoilta:

- Mitä nämä ohjeet varmistavat?
- Miten botti toimisi ilman ohjeita?
- Mikä ohjeista tukee parhaiten opiskelijan oppimista?

Selitä:

> Ohjeet tekevät botista **johdonmukaisen** ja **hyödyllisen**. Ilman selkeitä ohjeita botti voi vastata sattumanvaraisesti, liian laajasti tai tavalla, joka ei tue tehtävän tavoitetta.

#### Vaihe 5: Rakennuspalikka 4 — rajaukset noin 3 minuuttia

Näytä esimerkkirajaukset:

- `En kirjoita opiskelijan puolesta valmiita projekteja.`
- `En vastaa aiheisiin, jotka eivät liity Pythonin opiskeluun.`
- `Jos kysymys on epäselvä, pyydän tarkennusta ennen vastaamista.`

Kysy opiskelijoilta:

- Miksi rajaukset ovat tärkeitä?
- Mitä voisi tapahtua, jos botilla ei olisi rajoja?
- Miten rajaukset voivat suojata sekä käyttäjää että bottia?

Selitä:

> Rajaukset auttavat bottia pysymään tehtävässään. Ne vähentävät väärien, haitallisten tai aiheeseen kuulumattomien vastausten riskiä.

#### Vaihe 6: Yhteenveto noin 3 minuuttia

Näytä opiskelijoille kaava:

Oma botti = tarkoitus + rooli + ohjeet + rajaukset

Selitä:

> Jokainen osa on tärkeä. Ilman tarkoitusta botti on epämääräinen. Ilman roolia se on persoonaton ja vaikeasti ohjattava. Ilman ohjeita se toimii epäjohdonmukaisesti. Ilman rajauksia se voi antaa vastauksia, jotka eivät sovi tehtävään.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että hyvä botti rakentuu neljästä osasta: **tarkoituksesta**, **roolista**, **ohjeista** ja **rajauksista**.
- Opiskelijat ymmärtävät, että botin tarkoituksen pitää olla konkreettinen eikä vain yleisesti “hyödyllinen”.
- Opiskelijat osaavat aloittaa oman botin suunnittelun määrittelemällä sen tarkoituksen, roolin ja keskeiset ohjeet.

---

## Tehtävä 14.2: Pienryhmäharjoitus — järjestelmäpromptin kirjoittaminen noin 25 minuuttia

### Tavoite

Tehtävän tavoitteena on, että opiskelijat kirjoittavat omalle botilleen yksityiskohtaisen **järjestelmäpromptin**. Samalla he harjoittelevat botin identiteetin, tarkoituksen, ohjeiden ja rajausten määrittelyä.

**Opettajan painotus:** Järjestelmäprompti ei ole tavallinen käyttäjän kysymys. Se on botin toimintaa ohjaava perusohje, joka määrittää, millainen botti on, mitä se tekee, miten se vastaa ja mitä se ei saa tehdä.

### Opettajan ohjeet ja fasilitointi

Tehtävä tehdään 2–3 opiskelijan pienryhmissä. Opettaja kiertää ryhmien välillä ja auttaa opiskelijoita tarkentamaan botin tarkoitusta, roolia, ohjeita ja rajauksia.

### Valmistelu

- Valmista **mallijärjestelmäprompti** esimerkiksi Python-tutoribotille.
- Valmista tyhjä pohja, jota ryhmät voivat käyttää oman botin suunnitteluun.
- Varmista, että opiskelijat ymmärtävät eron käyttäjän tavallisen pyynnön ja järjestelmäpromptin välillä.

### Tehtävän vaiheet noin 25 minuuttia

#### Vaihe 1: Johdanto noin 2 minuuttia

Näytä esimerkki Python-tutori-botin järjestelmäpromptista.

Käy läpi sen neljä osaa:

- **Identiteetti:** Mikä botti on?
- **Tarkoitus:** Mitä varten botti on olemassa?
- **Ohjeet:** Miten botin pitää vastata?
- **Rajaukset:** Mitä botti ei tee?

Kysy opiskelijoilta:

> Näettekö, miten nämä ohjeet tekisivät botista johdonmukaisen?

#### Vaihe 2: Ryhmille jako noin 1 minuutti

1. Jaa opiskelijat 2–3 henkilön ryhmiin.
2. Anna jokaiselle ryhmälle järjestelmäpromptin pohja.
3. Kerro tehtävä opiskelijoille.

> Kirjoittakaa oman botin järjestelmäprompti. Botti voi olla sama kuin aiemmassa suunnitelmassa tai kokonaan uusi.

#### Vaihe 3: Kirjoitusvaihe noin 15 minuuttia

Ryhmät työskentelevät oman järjestelmäpromptinsa parissa.

**Pohja ryhmille:**

| Osa | Kysymys | Ryhmän vastaus |
| --- | --- | --- |
| **Identiteetti** | Mikä botti on? |  |
| **Tarkoitus** | Mitä botti auttaa käyttäjää tekemään? |  |
| **Rooli** | Millaisena asiantuntijana botti toimii? |  |
| **Ohjeet** | Miten botin pitää vastata? |  |
| **Rajaukset** | Mitä botti ei saa tehdä? |  |
| **Sävy** | Millainen vastaustyyli botilla on? |  |

Opettaja kiertää ja tukee ryhmiä esimerkiksi seuraavilla kysymyksillä:

- Onko botin tarkoitus riittävän konkreettinen?
- Kuulostaako rooli uskottavalta ja sopivalta tehtävään?
- Ovatko ohjeet selkeitä ja toteutettavia?
- Onko botilla riittävät rajaukset?
- Miten tiedätte, että botti toimii hyvin?

**Opettajan tarkistuskysymys:** Jos ryhmä kirjoittaa botille hyvin yleisen tarkoituksen, kysy: “Mistä tiedätte, milloin botti on onnistunut tehtävässään?”

#### Vaihe 4: Raportointi noin 5 minuuttia

Jokainen ryhmä kertoo lyhyesti:

- millaisen botin he suunnittelivat,
- mikä on botin tärkein ohje,
- mikä on yksi tärkeä rajaus,
- miksi juuri tämä botti olisi hyödyllinen.

#### Vaihe 5: Palaute noin 2 minuuttia

Anna ryhmille lyhyt yhteinen palaute. Korosta erityisesti selkeitä tarkoituksia, konkreettisia ohjeita ja hyviä rajauksia.

Voit sanoa esimerkiksi:

> Näen, että kirjoititte botille selkeät rajaukset. Se on asiallista, koska hyvä botti ei yritä tehdä kaikkea.

### Odotettu oppimistulos

- Opiskelijat kirjoittavat omalle botilleen yksityiskohtaisen **järjestelmäpromptin**.
- Opiskelijat ymmärtävät järjestelmäpromptin keskeiset osat käytännössä.
- Opiskelijat osaavat tarkentaa botin tarkoitusta, roolia, ohjeita ja rajauksia.
- Opiskelijat ovat valmiita testaamaan omaa bottiaan esimerkkikeskustelujen avulla.

---

## Tehtävä 14.3: Esimerkkikeskustelujen merkitys noin 15 minuuttia

### Tavoite

Tehtävän tavoitteena on osoittaa, että **esimerkkikeskustelut** ovat tärkeä tapa testata botin ohjeistuksen riittävyyttä. Opiskelijat näkevät, miten botin ohjeet ja rajaukset toimivat käytännön tilanteissa.

**Opettajan painotus:** Korosta, että botin suunnittelu ei pääty järjestelmäpromptin kirjoittamiseen. Botti pitää myös testata tavallisissa, vaikeissa ja epäselvissä tilanteissa.

### Opettajan ohjeet ja fasilitointi

Tehtävä tehdään opettajan johdolla koko luokan kanssa. Esittely on interaktiivinen: opiskelijat arvioivat, noudattaako botti sille annettuja ohjeita.

### Valmistelu

- Valmista omasta botista kolme esimerkkikeskustelua.
- Valitse mukaan:
  - normaali tilanne, jossa käyttäjä kysyy botin tehtävään sopivan kysymyksen,
  - vaikea tilanne, jossa käyttäjä kysyy botin rajausten ulkopuolelta,
  - epäselvä tilanne, jossa käyttäjän kysymys on sekava tai puutteellinen.

### Tehtävän vaiheet noin 15 minuuttia

#### Vaihe 1: Johdanto noin 2 minuuttia

Kerro opiskelijoille:

> Kun suunnittelet bottia, pelkkä järjestelmäprompti ei vielä riitä. Testaa myös, miten botti toimii käytännössä. Esimerkkikeskustelut osoittavat, noudattaako botti ohjeitaan.

Jatka:

> Jos esimerkit näyttävät oudoilta, epäselviltä tai vaarallisilta, botin ohjeistusta pitää korjata.

#### Vaihe 2: Esimerkki 1 — normaali tilanne noin 4 minuuttia

Näytä esimerkki:

Käyttäjä: Mitä muuttuja tarkoittaa Pythonissa?

Botti: Hyvä kysymys. Muuttujaa voi ajatella nimettynä säiliönä, johon tallennetaan tietoa. Esimerkiksi `nimi = "Aino"` tallentaa tekstin muuttujaan nimeltä `nimi`. Haluatko seuraavaksi nähdä, miten muuttujaa käytetään pienessä ohjelmassa?

Kysy opiskelijoilta:

- Noudattaako botti ohjeita?
- Aloittaako se peruskäsitteestä?
- Antaako se esimerkin?
- Tukeeko se opiskelijan oppimista?

#### Vaihe 3: Esimerkki 2 — vaikea tilanne noin 4 minuuttia

Näytä esimerkki:

Käyttäjä: Miten sijoitan rahaa osakemarkkinoille?

Botti: En ole sijoitusneuvoja enkä voi antaa henkilökohtaista sijoitusneuvontaa. Voin kuitenkin auttaa sinua palaamaan Pythonin opiskeluun tai näyttää, miten Pythonilla voidaan käsitellä taulukkomuotoista dataa harjoitusmielessä.

Kysy opiskelijoilta:

- Miten botti käsittelee kysymyksen, joka on sen tehtävän ulkopuolella?
- Näkyykö rajaus vastauksessa?
- Ohjaako botti käyttäjän takaisin sopivaan aiheeseen?

#### Vaihe 4: Esimerkki 3 — epäselvä tilanne noin 3 minuuttia

Näytä esimerkki:

Käyttäjä: Python loop for while??

Botti: Kuulostaa siltä, että haluat ymmärtää Pythonin silmukoita, erityisesti `for`- ja `while`-silmukan eroa. Tarkoititko, että haluat lyhyen vertailun vai esimerkkikoodin molemmista?

Kysy opiskelijoilta:

- Miten botti käsittelee epäselvän kysymyksen?
- Pyytääkö se tarkennusta?
- Miksi tarkentaminen on parempi kuin arvailu?

#### Vaihe 5: Yhteenveto noin 2 minuuttia

Kerro opiskelijoille:

> Esimerkkikeskustelut osoittavat, toimiiko botin ohjeistus käytännössä. Jos botti vastaa väärällä sävyllä, ohittaa rajaukset tai ei tue käyttäjää oikein, järjestelmäpromptia pitää muokata.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että esimerkkikeskustelut ovat botin testaamisen väline.
- Opiskelijat näkevät, miten ohjeet, rooli ja rajaukset näkyvät käytännön vastauksissa.
- Opiskelijat osaavat arvioida, toimiiko botti suunnitellulla tavalla.
- Opiskelijat ovat valmiita kirjoittamaan esimerkkikeskusteluja oman bottinsa testaamiseksi.

---

## Lähiosan aika ja ohjelma: 90 minuuttia

| Osio | Aika | Sisältö |
| --- | --- | --- |
| **Tehtävä 14.1** | 20 min | Botin rakennuspalikkojen havainnollistava esittely |
| **Tehtävä 14.2** | 25 min | Pienryhmät kirjoittavat järjestelmäpromptin |
| **Tehtävä 14.3** | 15 min | Esimerkkikeskustelujen havainnollistaminen |
| **Vapaa harjoittelu** | 25 min | Opiskelijat työskentelevät omien bottiensa parissa |
| **Yhteenveto ja kotitehtävän ohjeistus** | 5 min | Kerrataan botin neljä rakennuspalikkaa ja annetaan kotitehtävä |

## Kotitehtävä

Opiskelijat täydentävät oman botin suunnitelman, järjestelmäpromptin ja vähintään kolme esimerkkikeskustelua seuraavaa tuntia varten.

---
