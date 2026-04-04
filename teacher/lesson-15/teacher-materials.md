# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

Tämän lohkon jälkeen opiskelija:
1. Ymmärtää, että AI:ta käytetään koko IT-uralla — ei vain koodaukseen.
2. Osaa käyttää AI:ta dokumentaation kirjoittamiseen, lokin analyysiin ja CLI-komennon ymmärtämiseen.
3. Osaa lukea ja ymmärtää lokeja — ja käyttää AI:ta apuna.
4. Osaa kirjoittaa ja hyväksyä CLI-komentoja **turvallisesti** — ymmärtämällä ensin, ajamalla testilla.
5. Ymmärtää, että turvallisuus on ammattilaisesti pakollista — ei salasanoja, API-avaimia, eikä sokea kopioi-liitä.

---

## Yleisiä väärinkäsityksiä

### 1. "AI on vain ohjelmoijille — se ei auta IT-tukihenkilöitä tai järjestelmänvalvojia."

**Todellisuus:** AI auttaa kaikkea IT-työtä: dokumentaatiota, lokien analyysia, skriptejä, asetuksia, ratkaisujen dokumentointia.

### 2. "Lokit ovat vain kehittäjille — en tarvitse niitä."

**Todellisuus:** Jokainen IT-ammattilainen käyttää lokeja. Ne kertovat, mitä järjestelmällä tapahtui. Ammattilaisesti lokit ovat ensimmäinen paikka, mihin katsot.

### 3. "Dokumentaatio voidaan kirjoittaa myöhemmin — nyt on tärkein koodi."

**Todellisuus:** Dokumentaatio on yhtä tärkeää kuin koodi. Ilman dokumentaatiota uudet käyttäjät, tiimiläiset ja asiakkaat menettävät aikaa.

### 4. "CLI-komennot ovat vaarallisia — en uskalla käyttää komentoriviä."

**Todellisuus:** Komentorivi on ammattilaiselle päivittäinen työkalu. Vaarassa ei ole komentorivia — on tietämättömyyttä. Ymmärretään komennot ensin.

### 5. "Kopioin AI:n komentoja — miksi se merkitsee, jos ymmärrän ne vai en?"

**Todellisuus:** Jos kopioivat sokean koodin, voisit vahingossa poistaa kriittisiä tiedostoja, hakata järjestelmää tai vastaavaa. Turvallisuus ensin.

---

## Opettajan fasilitointiohjeet

### Ennen lähiosaa

- Valmista 2-3 todellista dokumentaatiota: hyvä ja huono esimerkki
- Testaa AI:n kanssa: README-pohja, lokin analyysi, CLI-komennot
- Valmista 2-3 todellista lokeista näytettä
- Näytä, mitkä CLI-komennot voivat olla vaarallisia ja miksi

### Lähiosassa (90 minuuttia)

- Aloita dokumentaation kirjoittamisella (Tehtävä 15.3) — live-esittely
- Liitä lokin analyysi — näytä, kuinka AI auttaa
- Näytä CLI-komennot ja turvallisuus — elävä varoitus
- Vahvista: AI on apulainen, sinä olet vastuussa

### Yleinen neuvo

- Monelta puuttuu näkemys, että dokumentaatio on ammattilaisuutta. Se ei ole kuollutta työtä — se on hyödyllista.
- Näytä todellisia esimerkkejä: "Ilman dokumentaatiota uusi tiimiläinen menettää 8 tuntia asennusyrityksissä."
- Lokit voivat tuntua abstrakteilta opiskelijoille. Näytä niiden käytännön arvo: "Tämän lokin mukaan minulla on muistin vuoto — näet kuka pikaisesti?"
- CLI-turvallisuus: opiskelijoilla on oikea huoli. Selvitä se: "Turvallisuus = ymmärrys. Ymmärrä ensin, aja sitten."

---

## Tarkistustehtävät (Checking-for-Understanding)

### 1. Dokumentaation tärkeys
**"Miksi README-tiedosto on tärkeä projektille?"**
- *Mitä etsit:* Opiskelija ymmärtää, että uudet käyttäjät/tiimiläiset alkavat README:sta. Se on ensimmäinen asia.

### 2. Lokin lukeminen
**"Tässä on logi virheilmoituksella. Mitä sinä katso ensin?"**
- *Mitä etsit:* Opiskelija osaa tunnistaa ERROR/CRITICAL -rivit ja ymmärtää kontekstin (mitä tapahtui ennen ja jälkeen).

### 3. AI:n käyttö dokumentaatioon
**"Miten käytät AI:ta README-tiedoston kirjoittamiseen?"**
- *Mitä etsit:* Opiskelija osaa pyytää pohja, mutta ymmärtää, että sinun täytyy muokata sitä.

### 4. CLI-turvallisuus
**"AI antaa sinulle komennon: `find . -name "*.backup" -delete`. Mitä teet?"**
- *Mitä etsit:* Opiskelija sanoo: ymmärrän ensin mitä se tekee, testaan `find` ilman `-delete`, sitten ajon.

### 5. Vastuullisuus
**"Kuka on vastuussa, jos AI:n antama komento vahingoittaa järjestelmää?"**
- *Mitä etsit:* Opiskelija ymmärtää, että **sinä** olet vastuussa — AI antaa ehdotuksen, mutta sinä päätät ja ajat.

---

## Yleisiä vaikeuksia ja niihin vastaamisen strategiat

### Vaikeus 1: Opiskelijat ajattelevat, että dokumentaatio on kuollutta työtä

**Mitä kuuluu:** "Dokumentaatiota ei kooda — miksi se merkitsee?"

**Vastaus:** "Ilman dokumentaatiota uudet ihmiset menettävät aikaa. Se on kuin lukea ohjeita ilman ohjeiden kirja — vain koodilla. Dokumentaatio = ammattilaisuus."

**Strategia:** Näytä todellinen esimerkki. "Kuvittele, että uusi tiimiläinen tulee. Hänellä on 3 tuntia osata asentaa ja käynnistää projekti. Ilman dokumentaatiota se vie 8 tuntia. Millä erolla?"

### Vaikeus 2: Opiskelijat eivät ymmärrä lokeja

**Mitä kuuluu:** "Loki on vain tekstiä — miten se auttaa?"

**Vastaus:** "Lokit ovat tarina. Aika, mitä tapahtui, virhe. Lue ne tarinana: mitä tapahtui ensin, sitten?"

**Strategia:** Yhdessä lukeminen. Ota yksinkertainen loki, lue rivi riviltä. "Näe se tarinana, ei vain tekstinä."

### Vaikeus 3: Opiskelijat pelkäävät CLI:tä

**Mitä kuuluu:** "Komentorivi on pelottava — voisin rikkoa kaiken!"

**Vastaus:** "Oikea! Jotkut komennot ovat vaarallisia. Mutta ymmärrys ja testi tekevät siitä turvallisen. Turvallisuus = tieto, ei pelko."

**Strategia:** Live-esittely turvallisista ja vaarallisista komennoista. Näytä testi-vaihe, joka tekee siitä turvallisen.

### Vaikeus 4: Opiskelijat kopioivat komentoja sokeasti

**Mitä kuuluu:** "AI antoi komennon, joten kopioin sen."

**Vastaus:** "Älä. Ymmärrä ensin. Koska vääränä komentohan voi vahingoittaa."

**Strategia:** Näytä vaarallinen komento. Pyydä opiskelijaa ajamaan se (turvallisessa ympäristössä). Näytä vahingon. Opeta ymmärtäminen.

### Vaikeus 5: Opiskelijat ei näe yhteyttä IT-uraansa

**Mitä kuuluu:** "Okei, dokumentaatio ja lokit — mutta mitä sillä on tekemistä siihen, mitä minä teen?"

**Vastaus:** "Joka päivä sinulla on dokumentaation kirjoittamisen, lokin lukemisen, komentojen ajamisen tehtävä. Ammattilaisesti."

**Strategia:** Kysy: "Milloin sinulla on viimeeksi kuvattu ongelmaa muille? Milloin olet lukenut lokeista? Milloin ajanut komentoriviä?" Linkitä oppituntiin.

---

## Oppimisresurssit, joihin opettaja voi viitata

1. **Builder-materiaali (content/lessons/lesson-15.md):** Kaikki perusideat ovat siellä.

2. **Dokumentaation esimerkit:**
   - GitHub: etsi hyviä README-tiedostoja (esim. torvalds/linux)
   - API-dokumentaatio: esim. OpenAPI-spesifikaatiot
   - Asennusohjeet: distributions, Docker, software

3. **Lokeista oppiminen:**
   - Linux-lokit: `/var/log/syslog`, `/var/log/auth.log`
   - Sovellus-lokit: application-specific
   - Cloud-lokit: AWS CloudWatch, GCP Logs

4. **CLI-turvallisuus:**
   - Näytä vaarallisia komentoja (turvallisissa ympäristöissä)
   - Näytä `man`-sivut komennoista
   - Opeta `--dry-run` vaihtoehdoista

5. **Opiskelijoiden omat esimerkit:** Pyydä opiskelijoita tuomaan todellisia lokeja (anonymisoidut), dokumentaatiota, komentoja. Analysoi yhdessä.

