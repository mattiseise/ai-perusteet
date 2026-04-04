# Opiskelutehtävät

## Tehtävä 12.1: Monimutkainen ongelma pilkkoon osiin — Kontekstin rakentaminen

### Tavoite
Oppia pilkkoon monimutkainen IT-ongelma osiin ja ratkaista jokainen osa tekoälyn kanssa iteratiivisesti, dokumentoimalla kaikki vaiheet.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

**Annettu monimutkainen ongelma:**
"Rakenna käyttäjän kirjautumis-järjestelmä, joka tarkistaa salasanan voimakkuuden, tallentaa käyttäjän tietokantaan ja lähettää vahvistus-sähköpostilla."

**Vaihe 1 — Pilkkaa ongelma osiin (10 min)**
Kirjoita taululle tai dokumentissa kuusi osaa:
1. Salasanan voimakkuuden validointi (regex, pituus, merkit)
2. Käyttäjän tietojen tallentaminen tietokantaan (SQL)
3. Sähköpostin lähettäminen (email-API)
4. Virheenkäsittely (mitä jos salasana heikko? Mitä jos tietokanta kaatuu?)
5. Testaaminen (millä tapauksilla testaa?)
6. Integraatio (kuinka kytkeä nämä osassa yhteen)

**Vaihe 2 — Kierros 1: Salasanan voimakkuus**
- Prompt: "Kirjoita regex-pattern, joka validoi salasanan. Vaatimukset: vähintään 8 merkkiä, yksi iso kirjain, yksi numero, yksi erikoismerkki."
- Dokumentoi: Mitä sait? Toimiiko se?

**Vaihe 3 — Kierros 2: Lisää tietokantaa**
- Konteksti: "Käytän SQLite:a. Taulussa 'users' on sarakkeet: id, email, password_hash, created_date."
- Prompt: "Kirjoita SQL-käsky ja Python-koodi, joka tallentaa käyttäjän tietokantaan. Älä tallenna salasanaa suorana — käytä hash-funktiota."
- Dokumentoi: Miten tietokanta integroitu?

**Vaihe 4 — Kierros 3: Email-lähettäminen**
- Prompt: "Lisää koodi, joka lähettää vahvistus-sähköpostia uudelle käyttäjälle. Sisällytä myös vahvistus-linkki."
- Dokumentoi: Kuinka sähköposti integroituu järjestelmään?

**Vaihe 5 — Kierros 4: Virheenkäsittely**
- Prompt: "Lisää error-käsittely. Mitä tapahtuu, jos: (1) salasana on heikko, (2) email on jo käytössä, (3) tietokanta-yhteys epäonnistuu, (4) email-palvelu on poissa käytöstä?"
- Dokumentoi: Kuinka virheet käsitellään?

**Vaihe 6 — Kierros 5: Testit**
- Prompt: "Kirjoita testit näille tapauksille: validi käyttäjä, heikko salasana, duplikaatti-email, tietokanta-virhe. Käytä pytest."
- Dokumentoi: Kuinka järjestelmä testataan?

**Vaihe 7 — Kierros 6: Lopullinen integraatio**
- Prompt: "Yhdistä kaikki osat: validointi, tallennus, email, error-käsittely, testit. Miten käyttäjä kutsuu tätä järjestelmää?"
- Dokumentoi: Lopullinen ratkaisu.

**Dokumentointi-taulukko:**

| Kierros | Fokus | Prompt | Saatu vastaus (yks. rivissä) | Mitä parannettiin |
|---------|-------|--------|------------------------------|------------------|
| 1 | Validointi | Regex-pattern... | [yhteenveto] | Perusta |
| 2 | Tietokanta | SQLite+hash... | | |
| 3 | Email | Vahvistus-linkki... | | |
| 4 | Virheet | Error-caset... | | |
| 5 | Testit | Pytest-testit... | | |
| 6 | Integraatio | Lopullinen ratkaisu... | | |

### Odotettu tuotos

- Täytetty kierros-taulukko, joka näyttää kontekstin rakentamisen vaihe vaiheelta
- Dokumentaatio jokaisesta promtista ja vastauksesta (tai kuvakaappaukset testaus-istunnoista)
- Johtopäätös (2-3 lausetta): "Pilkkoon ja iteroimalla saavutin käyttökelpoisen ratkaisun, koska..."

**Jos teet tehtävän yksin:**
Voit toteuttaa neljä kierrosta kuuden sijaan ja dokumentoida ne samalla tavalla.

---

## Tehtävä 12.2: Oikeasta koodista parantaminen — Lähdeaineiston liittäminen

### Tavoite
Oppia antamaan tekoälylle olemassa olevaa koodia, jota parannetaan iteratiivisesti.

### Ohjeet (ryhmä tai yksin)

**Annettu koodi, joka täytyy parantaa:**
```python
def check_password(password):
    if len(password) > 8:
        return True
    return False
```

Tämä on huono ratkaisu — liian yksinkertainen.

**Kierros 1 — Analyysi:**
- Prompt: "Tässä on Python-funktio: [liitä koodi]. Mikä on väärin tässä funktiossa? Mitä sinä parantaisit?"
- Dokumentoi: Mitä analyysi paljasti?

**Kierros 2 — Parannus 1: Vaatimukset:**
- Prompt: "Paranna funktiota lisäämällä vaatimukset: vähintään 8 merkkiä, yksi iso kirjain, yksi numero. Palauta True/False."
- Dokumentoi: Miten parantunut koodi näyttää?

**Kierros 3 — Parannus 2: Error-käsittely:**
- Prompt: "Lisää error-käsittely. Jos syöte ei ole merkkijono, palauta arvo None ja virhesanoma."
- Dokumentoi: Miten virheet käsitellään?

**Kierros 4 — Parannus 3: Testit:**
- Prompt: "Kirjoita testit tälle funktiolle. Sisällytä vähintään 5 tapausta: validi salasana, liian lyhyt, ei numeroa, ei isoa kirjainta, ei merkkijono."
- Dokumentoi: Miten testataan?

**Dokumentointi-taulukko:**

| Kierros | Tarkoitus | Saamiasi kehitystä |
|---------|-----------|-------------------|
| 0 | Alkuperäinen koodi | [nykytila] |
| 1 | Analyysi | [mitä paljastui] |
| 2 | Vaatimukset | [parannettu versio] |
| 3 | Error-käsittely | [virheenkäsittely] |
| 4 | Testit | [test-suite] |

### Odotettu tuotos

- Dokumentaatio alkuperäisestä ja parannetusta koodista (tai kuvakaappaukset)
- Täytetty parannus-taulukko
- Johtopäätös: "Olemassa olevan koodin parantaminen iteratiivisesti oli hyödyllistä, koska..."

---

## Tehtävä 12.3: Tiimityö monimutkaisen ongelman ratkaisemisessa — Realistinen casetutkimus

### Tavoite
Työskennellä ryhmässä ratkaistaksenne realistisen IT-ongelman käyttämällä tekoälyä ammattilaisesti — pilkkomalla, iteroimalla, dokumentoimalla.

### Ohjeet (ryhmätehtävä, 3-4 henkilöä)

**Annettu tiimi-tehtävä (valitse yksi):**
1. **E-kauppa:** Rakenna tuotteen hakujärjestelmä, joka etsii tuotteita nimellä, hinnalla, kategorialla. Sisällytä taulukko tulosten näyttämiseksi.
2. **Sosiaaliset media:** Rakenna kommenttien moderointijärjestelmä, joka estää roskapostia ja sopimattomia kommentteja.
3. **Oppilashallinto:** Rakenna opiskelijoiden arvo-järjestelmä, joka laskee keskiarvon, antaa arvosanan ja lähettää raportin.

**Prosessi:**

1. **Vaihe 1: Ryhmän roolien jako**
   - Projektipäällikkö: ohjaa prosessia
   - Prompt-insinööri: kirjoittaa prompteja
   - Dokumentoija: tallentaa vaiheet
   - Testaa: testaa tuloksia

2. **Vaihe 2: Pilkkoa tehtävä osiin** (15 min)
   - Ryhmä listaa 4-6 osaa, joihin ongelma jakautuu
   - Kirjoita ne selkeästi.

3. **Vaihe 3: Iteratiivinen rakentaminen** (30 min)
   - Jokainen osa ratkaistaan yksitellen
   - Prompt-insinööri kirjoittaa promptin
   - Testaa validoi tuloksia
   - Dokumentoija kirjoittaa muistiin

4. **Vaihe 4: Integraatio** (10 min)
   - Yhdistä osät
   - Testaa kokonaisuus

5. **Vaihe 5: Esittely** (5 min)
   - Ryhmä esittää prosessia ja lopputulosta

### Odotettu tuotos

- Dokumentaatio kokonaisesta prosessista (pilkkoon vaiheet, kierros kierrokselta)
- Lopullinen ratkaisu tai sen dokumentaatio
- Ryhmän johtopäätös: "Ammattilaisesti rakensimme ratkaisua iteratiivisesti, koska..."
- Esittely muille opiskelijoille (5 min)

**Jos teet tehtävän yksin:**
Teet yhden tehtävistä yksin ja dokumentoit prosessia samalla tavalla.
