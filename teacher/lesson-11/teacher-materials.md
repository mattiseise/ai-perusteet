# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

Tämän lohkon jälkeen opiskelija:
1. Osaa rakentaa hyvän promptin, joka sisältää tavoitteen, roolin, rajat, formaatin ja esimerkkejä.
2. Ymmärtää eroa promptin ja kontekstin välillä.
3. Osaa rakentaa kontekstia iteratiivisesti jatkoprompteilla.
4. Osaa testata ja dokumentoida, kuinka iteraatio parantaa tuloksia.

---

## Yleisiä väärinkäsityksiä

### 1. "Hyvä prompt on pitkä ja sisältää kaiken kerralla."

**Todellisuus:** Hyvä prompt on selkeä ja strukturoitu, mutta ei välttämättä pitkä. Ammattilaisesti rakentaa kontekstia iteratiivisesti — ensimmäinen prompt on yksinkertainen, seuraavat tekevät sitä terävemmäksi.

### 2. "Prompt on sama kuin kysymys."

**Todellisuus:** Kysymys on epämuodollinen. Prompt on strukturoitu tehtävänanto, jossa on selkeä tavoite, rooli, rajat ja formaatti.

### 3. "Konteksti ja prompt ovat sama asia."

**Todellisuus:** Prompt on "mitä haluan tehdä nyt". Konteksti on "mikä on tausta-aine". Konteksti rakentaa vastauksen laadun.

### 4. "Iteraatio tarkoittaa, että en osaa kirjoittaa hyvää promptia ensimmäisellä yrityksellä."

**Todellisuus:** Iteraatio on ammattilaisella strategia — et osaa tietää kaikkea etukäteen, joten parannella vaihe vaiheelta.

### 5. "Jos tekoäly antaa huonon vastauksen, vika on tekoälyssä, ei promtissa."

**Todellisuus:** Vastaus on riippuvainen promtin laadusta. Ammattilaisesti parannat promptia ennen kuin sanot, että tekoäly ei osaa.

---

## Opettajan fasilitointiohjeet

### Ennen lähiosaa

- Testaa itse ChatGPT:n kanssa huonon ja hyvän promptin eroja.
- Dokumentoi kuvakaappaukset molemmista vastuksista.
- Valmistele kolme "jatkopromptin" esimerkkiä, joissa näet, kuinka konteksti rakentuu.
- Jos mahdollista, valitse todellinen ammattilaisella tapaus (esim. asiakaspalvelu­vastaus, IT-tukitiketin kirjoitus).

### Lähiosassa (90 minuuttia)

- Aloita live-demolla (Tehtävä 11.1). Opiskelijat näkevät, miksi hyvä prompt merkitsee.
- Jatka iteratiivisella harjoituksella (Tehtävä 11.2). Opiskelijat tekevät itse kierros kierrokselta.
- Pääty konteksti-keskusteluun (Tehtävä 11.3). Opiskelijat näkevät ammattilaisesta perspektiiviä.
- Korostaa: "Hyvä prompt-kirjoitus on taito, jonka opit. Ammattilaiset tekevät tämän päivittäin."

### Yleinen neuvo

- Monet opiskelijat ajattelevat, että "hyvä prompt" on jokin mystinen salaisuus. Korjaa tämä: se on strukturoitu ajattelu.
- Kannusta iteraatiota — älä sano "keksit oikean promptin", sano "parani promptia kierros kierrokselta".
- Linkitä ammattilaisiin tapauksiin: "Asiakaspalvelussa tarvitset kontekstia asiakkaan historiasta. Koodissa tarvitset kontekstia vaatimuksista."

---

## Tarkistustehtävät (Checking-for-Understanding)

### 1. Promptin rakenne
**"Kerro viisi elementtiä, joista hyvä prompt rakentuu. Anna esimerkki jokaisesta."**
- *Mitä etsit:* Opiskelija nimeää tavoitteen, roolin, rajat, formaatin, esimerkit; osaa antaa esimerkin kustakin.

### 2. Iteraatio
**"Kirjoitit promptin. Tekoäly antoi vastauksen, joka oli lähellä oikeaa, mutta puutteellinen. Mitä teet seuraavaksi?"**
- *Mitä etsit:* Opiskelija kirjoittaa jatkopromptia, joka rakentaa edellisen kontekstiin. Ei kirjoita täysin uutta promptia.

### 3. Konteksti
**"Mitä konteksti tarkoittaa promptyssa? Kuinka eroaa promptista?"**
- *Mitä etsit:* Opiskelija ymmärtää, että konteksti on ympäröivä tieto, joka määrää vastauksen laadun.

### 4. Ammattilaisesti soveltaminen
**"Sinulla on tehtävä: kirjoita dokumentaatio koodille. Mitä kontekstia tarvitset?"**
- *Mitä etsit:* Opiskelija nimeää: keille dokumentaatio on, mitä teknologioita käytetään, kuinka yksityiskohtainen.

### 5. Testaaminen
**"Testasit promptia ja sait huonon vastauksen. Kuinka osaat, ovatko vika promtissa vai tekoälyssä?"**
- *Mitä etsit:* Opiskelija osaa muuttaa promptia ja testata uudelleen. Osaa erotella, onko vika promtissa.

---

## Yleisiä vaikeuksia ja niihin vastaamisen strategiat

### Vaikeus 1: Opiskelijat luulevat, että he pitävät kirjoittaa pitkän, yksityiskohtaisen promptin ensi kerran

**Mitä kuuluu:** "Kuinka voin tietää, miten kirjoittaa hyvä prompt? On liian paljon elementtejä."

**Vastaus:** "Et tarvitse muistaa kaikkia kerralla. Aloita yksinkertainella promptilla. Näet vastauksen. Parannela seuraavalla promptilla. Iteraatio opettaa."

**Strategia:** Anna struktuuri, mutta korostaa, että opiskelijat oppivat tekemällä, ei muistamalla. Ensimmäinen prompt on yleensä huono — se on ok.

### Vaikeus 2: Opiskelijat sekoittavat kontekstin promptiin ja ajattelevat, että ne ovat samaa

**Mitä kuuluu:** "Eikö konteksti ole vain pitkä prompt?"

**Vastaus:** "Ei. Prompt on 'mitä haluan tehdä'. Konteksti on 'mikä tausta-aine'. Ne rakennetaan eri tavoilla. Prompt sinä kirjoitat joka kierroksella. Konteksti rakentuu kierros kierrokselta."

**Strategia:** Käytä konkreettista esimerkkiä: "Prompt: 'Kirjoita sähköposti.' Konteksti: 'Asiakas on ollut 5 vuotta, pettynyt, odottaa pahoittelua.'"

### Vaikeus 3: Opiskelijat ajattelevat, että iteraatio tarkoittaa heikon promptin kirjoittamista

**Mitä kuuluu:** "Jos en osaa kirjoittaa hyvää promptia heti, olen huono tässä."

**Vastaus:** "Ammattilaiset iteraavat aina. Ensimmäinen prompt on pohja, seuraavat testavat ja parannella. Se ei ole 'huono' — se on prosessi."

**Strategia:** Näytä oikea ammattilaiselle esimerkki: kehittäjä kirjoittaa promptin, testaa sen, parannela sitä. Tämä on normaalia.

### Vaikeus 4: Opiskelijat eivät näe, miksi konteksti on tärkeä

**Mitä kuuluu:** "Miksi voin kirjoittaa vain promptin ilman kontekstia?"

**Vastaus:** "Voit, mutta vastaus on yleinen. Ammattilaisesti haluat asiakkaalle sopivan, tilanteeseen sovitetun vastauksen. Konteksti tekee sen."

**Strategia:** Näytä vertailu: vastaus ilman kontekstia vs. vastaus kontekstin kanssa. Konkreettinen ero auttaa.

---

## Oppimisresurssit, joihin opettaja voi viitata

1. **Builder-materiaali (lesson-11.md):** Viisi elementtiä ja iteraation käsite ovat selkeästi selitetty. Varmista, että opiskelijat ovat tutustuneet.
2. **Live-testaus:** Testaa prompteja itse ChatGPT:n kanssa. Näytä kuvakaappauksia.
3. **Ammattilaiset esimerkit:** Etsi oikeita tapauksita, joissa huono prompt vs. hyvä prompt johtaa erilaisiin tuloksiin.
4. **Opiskelijoiden omat promptit:** Pyydä opiskelijoita jakamaan heidän parantamansa promptit ja analysoimaan niitä.

---

## Lisämateriaalia opettajalle

### Esimerkkejä promptin elementeistä

**Tavoite:**
- "Kirjoita..."
- "Selitä..."
- "Paranna..."
- "Muuta..."

**Rooli:**
- "Olet Python-kehittäjä"
- "Olet opettaja, joka opettaa 15-vuotiaita"
- "Olet tietoturva-asiantuntija"

**Rajat:**
- "Enintään 5 lausetta"
- "Älä käytä teknisiä termejä"
- "Hyväksy vain näitä muotoja"

**Formaatti:**
- "JSON-muodossa"
- "Numeroidut vaiheet"
- "Taulukko"
- "Python-koodi"

**Esimerkki:**
- "Esimerkiksi: INPUT: 'test@example.com', OUTPUT: 'Valid'"
- "Kuten tässä tapauksessa: asiakas valitti kolme kertaa, odottaa pahoittelua"

### Prompting-strategiat ammattilaisille

1. **"Expert"-rooli:** Esim. "Olet lääketieteen asiantuntija. Selitä..." — antaa asiantuntevamman näkökulman.
2. **"Few-shot learning":** Annaa useita esimerkkejä, mallia oppii niistä paremmin.
3. **"Chain of thought":** Pyydä mallia selittämään ajattelun prosessi: "Selitä vaihe vaiheelta".
4. **"Temperature"-käsite:** (aikuisille) Joissa malleissa voi säätää "luovuutta" — lämpötila 0 = deterministinen, 1.0 = luova.
