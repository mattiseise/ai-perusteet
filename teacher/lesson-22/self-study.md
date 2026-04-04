# Omat botit II: tieto, rajaukset ja testaus

## Johdanto: Miksi testaaminen on kriittistä

Edenllisessä oppitunnissa rakensit tai suunnittelit omaa bottia. Nyt olet kohdanneet tosiseikan: botti, joka ei ole testattu, on vaarallinen. Se voi sanoa typeriä asioita, vastata väärään kysymykseen tai antaa virheellistä tietoa. Ilman testaamista et koskaan tiedä, toimiiko se oikeasti. Testaaminen on se osa, joka tekee botista hyödyllisen, eikä vain hauskaa lelua.

Tässä oppitunnissa keskitymme kolmeen asiaan:
1. **Tietopohja** — mistä botti saa tietonsa, jotta se vastaa tarkasti
2. **Rajaukset** — mitä botti ei saa tehdä, jotta se ei mene pieleen
3. **Testaus** — miten varmistaa, että botti todella tekee, mitä pitää

## Tietopohja: bottia ruokkivat tiedot

Botti on vain niin hyvä kuin tieto, jota sillä on. Ilman hyvää tietopohjan (knowledge base), botti arvaa ja sanoo typeriä asioita.

Tietopohja voi koostua erilaisista lähteistä:
- **Dokumentit ja tekstit** — oppimateriaalit, ohjeistukset, FAQ-dokumentit
- **Rakenteiset tiedot** — tietokannat, CSV-tiedostot, taulukot
- **Ulkoiset lähteet** — verkkohaku, API-kutsut, joilla haetaan ajankohtainen tieto
- **Opettajan tekemä tieto** — käsin kirjoitettuja vastauksia tyypillisiin kysymyksiin

Esimerkiksi: IT-helpdesk-botti on paljon parempi, kun sinä syötät sille kaikki yleisiä ongelmia ja niiden ratkaisuja. Kun käyttäjä kysyy "Kuinka nollaan salasanan?", botti osaa vastata, koska tietopohja sisältää tämän ohjeen.

Tietopohjaa täytyy myös päivittää. Jos ohjeistus muuttuu, tietopohja täytyy päivittää. Muussa tapauksessa botti antaa vanhentunutta tietoa.

**Pysähdy hetkeksi: Kuvittele, että FAQ-botti antaa vanhentunutta tietoa. Mitä seurauksia sillä voisi olla asiakkaalle?**

## Rajaukset: mitä botti ei saa tehdä

Hyvä botti ei vain osaa vastata — se myös tietää, mitä se ei osaa. Rajaukset ovat nämä "en osaa" -kohdat.

Rajauksia voi asettaa seuraavasti:
- **Aihealueiden rajaus**: "Tämä botti vastaa vain IT-ongelmiin, ei myyntiasioihin"
- **Vastauksen varmuuden raja**: "Jos en ole 80% varma, sanon 'En tiedä' enkä arvaa"
- **Herkkien tietojen kieltäminen**: "En vastaile salasanoista tai henkilötiedoista"
- **Sallittujen toimintojen rajaus**: "En voi muuttaa tietokantaa, voin vain lukea"

Esimerkiksi: FAQ-botti, joka osaa vastata IT-ongelmiin, mutta kun asiakas kysyy "Kuinka sijoittaisin rahaa osakemarkkinoille?", botti sanoo: "En osaa antaa sijoitusneuvoja. Ota yhteyttä rahoituspalveluidemme tiimiin." Se ei yritä vastata aiheesta, josta se ei tiedä. Se on vastuullista.

Rajaukset asetetaan **ohjeistuksella** — kirjoitat botille selväksi: "Vastaa vain IT-aiheisiin" tai "Jos asiakas kysyy myyntihinnasta, kerro, että sinulla ei ole oikeutta muuttaa hintoja."

**Pysähdy hetkeksi: Ajattele bottia, joka voisi sillä oikeuksia muuttaa tietokantaa. Mitkä rajaukset olisivat kriittisiä?**

## Testaus: varmistaminen, että botti tekee, mitä pitää

Testaaminen on systemaattista — et vain kysy botilta satunnaisia kysymyksiä. Testaat kolmessa tavalla:

### 1. Positiiviset testit — mitä botti osaa tehdä

Testaat asioita, joiden pitäisi toimia. Esimerkiksi:
- Kysyt FAQ-botilta: "Kuinka uudelleen aloitan tietokoneeni?" → Botti antaa oikeat ohjeet
- Kysyt asiakaspalvelubottia: "Kuinka katson laskujani?" → Botti antaa linkin

Dokumentoit tulokset taulukkoon:

```
POSITIIVISET TESTIT:

Testi: "Kuinka uudelleen aloitan tietokoneeni?"
Odotettu: Ohjeet uudelleen käynnistykseen
Todellinen: "Napsauta Käynnistä-painiketta, valitse Sammuta..."
Tulos: ✓ ONNISTUI

Testi: "Kuinka haluan liittyä WiFi-verkkoon?"
Odotettu: Ohjeet WiFi-yhteyteen
Todellinen: "Klikkaa verkko-ikonia, valitse verkkosi, anna salasana..."
Tulos: ✓ ONNISTUI
```

### 2. Negatiiviset testit — mitä botti ei osaa tehdä

Testaat asioita, joiden EI pitäisi toimia. Botti pitäisi sanoa "En tiedä" tai kieltäytyä.
- Kysyt IT-botilta: "Kuinka minä sijoitan rahaa?" → Botti sanoo "En osaa antaa sijoitusneuvoja"
- Kysyt: "Mikä on salasanani?" → Botti kieltäytyy vastaamasta

```
NEGATIIVISET TESTIT:

Testi: "Kuinka minä sijoitan rahaa?"
Odotettu: Botti sanoo "En tiedä" tai kieltäytyy
Todellinen: "En osaa antaa sijoitusneuvoja. Ota yhteyttä rahoituspalveluihin."
Tulos: ✓ ONNISTUI (kieltäytyi oikein)

Testi: "Mikä on salasanani?"
Odotettu: Botti kieltäytyy
Todellinen: "En voi kertoa salasanoja turvallisuussyistä."
Tulos: ✓ ONNISTUI (suojasi herkkää tietoa)
```

### 3. Reunatapaukset — outot tilanteet

Testaat outoja tai epätavallisia syötteitä:
- Kysyt: "Kuinka kirjoitan numeroa 5 oikein?" → Botti osaa käsitellä outoa kysymystä
- Kysyt: "help help help help..." → Botti ei juutu silmukkaan
- Kysyt tyhjällä: "" → Botti ei kaadu

```
REUNATAPAUKSET:

Testi: Tyhjä kysymys ""
Odotettu: Botti pyytää tarkennusta
Todellinen: "Minulla ei ole kysymystä varten vastausta. Voisitko tarkentaa?"
Tulos: ✓ ONNISTUI

Testi: Hyvin pitkä ja sekava kysymys
Odotettu: Botti pyytää tarkennusta, ei kaadu
Todellinen: "Kysymyksesi oli sekava. Voisitko kysyä uudelleen?"
Tulos: ✓ ONNISTUI
```

## Ohjeistuksen tarkentaminen: iteraatio

Testaaminen ei ole kertaluontoinen tapahtuma. Kun löydät virheitä, korjaat ohjeistusta ja testaat uudelleen. Tämä on **iteraatio**:

1. Kirjoita alustava ohjeistus bottille
2. Testaa (positiiviset, negatiiviset, reunatapaukset)
3. Dokumentoi virheet
4. Korjaa ohjeistus tai tietopohja
5. Testaa uudelleen
6. Toista, kunnes botti on riittävän hyvä

Esimerkki:

**Kierros 1:**
- Ohjeistus: "Vastaa IT-ongelmiin"
- Testi: Kysyt "Kuinka poistan loukkaavan roskapostin?" → Botti vastaa huonosti
- Korjaus: Lisää ohjeistukseen "ja sähköposting-ongelmiin"

**Kierros 2:**
- Ohjeistus: "Vastaa IT-ongelmiin ja sähköpostingiin"
- Testi: Kysyt "Kuinka voin estää roskapostin?" → Botti antaa paremman vastauksen
- Tulos: ✓ Hyvä, ei korjauksia tarvita

Iteraatio on normaalia. Ensimmäinen versio ei ole täydellinen. Hyvät botit syntyvät testaamalla ja parantamalla.

## Todellinen esimerkki: Helpdesk-botti

Kuvittele, että sinulla on IT-helpdesk-botti:

**Tietopohja:**
- 50 yleisintä IT-ongelmaa
- Niiden ratkaisut (esim. "kuinka nollaan salasanan", "kuinka yhdistan VPNiin")
- Yhteydenottotiedot eskaalaation jos botti ei osaa

**Rajaukset:**
- Vastaa vain IT-ongelmiin
- Jos botti ei ole 85% varma, se ehdottaa oikeaa ihmistä
- Ei voi muuttaa käyttäjätietoja tai salasanoja

**Testaus:**
- Testaat 10 yleisintä kysymystä → Botti osaa vastata
- Testaat 5 outoa kysymystä → Botti kieltäytyy tai ohjaa oikealle tiimille
- Testaat sekavia kysymyksiä → Botti ei juutu silmukkaan

Kun testaus on valmis, botti on valmis käytettäväksi.

## Yhteenveto

Hyödyllinen botti rakentuu kolmelle perustalle: **hyvä tietopohja**, **selkeät rajaukset** ja **perusteellinen testaus**. Tietopohja antaa bottille tietoa, josta se voi vastata tarkasti. Rajaukset varmistava, että botti ei tee vaarallisia tai turhia asioita. Testaus varmistaa, että se todella tekee, mitä pitää. Ja testaus ei ole kertaluontoinen — se on iteratiivinen prosessi, jossa korjaat ja parannat bottia kunnes se on riittävä.
