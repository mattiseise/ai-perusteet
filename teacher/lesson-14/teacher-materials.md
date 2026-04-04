# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

Tämän lohkon jälkeen opiskelija:
1. Ymmärtää, että konteksti (kuvakaappaukset, lokit, koodi) on oleellinen ongelmanratkaisussa.
2. Osaa ottaa kuvakaappauksia ja analysoida lokeja ammattilaisesti.
3. Osaa yhdistää teksti, kuva ja koodi tehokkaaksi multimodaaliseksi pyynnöksi.
4. Ymmärtää turvallisuusriskit — mitä ei saa koskaan näyttää (salasanat, API-avaimet).

---

## Yleisiä väärinkäsityksiä

### 1. "Voin kuvata ongelman sanoilla — kuvakaappauksia ei tarvita."

**Todellisuus:** Kuvakaappaus on tarkempi ja nopeampi kuin kuvaus. Se näyttää täsmälleen mitä näet, kontekstia myöten.

### 2. "Kaikki lokit ovat hyödyllisiä — katso vain kaiken."

**Todellisuus:** Lokeissa voi olla tuhansia rivejä. Ammattilaiset etaavat oleellisen osan: virheilmoitukset, varoitukset ja tapahtumien sarja.

### 3. "Lokit ovat vain kehittäjille — IT-tukihenkilö ei tarvitse sitä."

**Todellisuus:** Lokit ovat jokaiselle. Kun asiakkaan ongelma ratkaistaan, lokit auttavat ymmärtämään, mitä tapahtui.

### 4. "Salasanakenttä näkyy lokissa — se on normaalia."

**Todellisuus:** Salasanat lokeissa ovat vakava turvallisuusriski. Ne pitää poistaa tai muokata, ennen kuin jaat lokit.

### 5. "Multimodaalinen = kaikki kuvat ja lokit kerralla."

**Todellisuus:** Multimodaalinen tarkoittaa monipuolisten lähteiden käyttöä — mutta vain oleellisia. Vähemmän on usein enemmän.

---

## Opettajan fasilitointiohjeet

### Ennen lähiosaa

- Testaa kuvakaappausten ottaminen eri ohjelmista — Windows, Mac, Linux
- Valmista 2–3 todellista ongelmaa, joilla on kuvakaappaukset ja lokit
- Tutustu lokien muotoon eri järjestelmissä (application, system, apache, nginx, app-specific)
- Testaa AI:n kanssa: näytä sekä huono että hyvä pyyntö, näytä ero

### Lähiosassa (90 minuuttia)

- Aloita live-esittelyllä (Tehtävä 14.3) — näytä ero
- Liitä siihen pienryhmä-harjoitukset (Tehtävä 14.4)
- Vahvista turvallisuuden tärkeys — ei salasanoja, ei API-avaimia
- Praktisoi lokiravintoa: yhdessä lukeminen ja tulkinta

### Yleinen neuvo

- Monet opiskelijat ajattelevat, että kaikki on joko koodi tai sanat. Selvitä, että konteksti on kolmannen: lokit, kuvakaappaukset, virheilmoitukset.
- Näytä, että ammattilaiset tekevät tämän päivittäin. Se ei ole valinnaista — se on ammattilaisuus.
- Palaa aina: "Näytä, älä kerro." Se on mantra.

---

## Tarkistustehtävät (Checking-for-Understanding)

### 1. Lokin tulkinta
**"Luki tämä logi-rivi: '2024-03-14 10:23:45 ERROR: Database connection failed'. Mitä se kertoo?"**
- *Mitä etsit:* Opiskelija näkee ajan, vakavuuden (ERROR), viestin. Voi sanoa: "Tietokanta-yhteys epäonnistui tämän aikaisen.

### 2. Konteksti
**"Miksi on tärkeää kertoa AI:lle, mitä yritit tehdä, ennen kuin näytät kuvakaappauksen?"**
- *Mitä etsit:* Opiskelija ymmärtää, että sama virheilmoitus voi tarkoittaa eri asioita eri konteksteissa.

### 3. Turvallisuus
**"Näytössäsi on salasana lokissa. Mitä teet?"**
- *Mitä etsit:* Opiskelija sanoo, että poistaa tai muokkaa sen pois ennen jakamista.

### 4. Multimodaalisuus
**"Mistä lähteistä voit saada kontekstia ongelmaan? Listaa vähintään kolme."**
- *Mitä etsit:* Opiskelija nimeää: kuvakaappaukset, lokit, koodi, virheilmoitukset, console-tuloste, debugger.

### 5. Prioriteetti
**"Sinulla on 500 rivistä lokit. Millä tavalla valitset, mitä näytät AI:lle?"**
- *Mitä etsit:* Opiskelija ymmärtää, että oleellinen on: virherivit, varoitusrivit, ennen virhettä ja sen jälkeen.

---

## Yleisiä vaikeuksia ja niihin vastaamisen strategiat

### Vaikeus 1: Opiskelijat eivät osaa lukea lokeja

**Mitä kuuluu:** "En ymmärrä, mitä tämä loki sanoo. Siinä on vain numeroita ja tekstiä."

**Vastaus:** "Lokit ovat säännölliset. Joka rivi on: aika | taso (INFO/WARNING/ERROR) | viesti. Etsimme ERROR ja WARNING -rivejä."

**Strategia:** Yhdessä lukeminen. Ota yksinkertainen logi, lue rivi riviltä. "Tämä rivi sanoo 'aika on 10:23, taso on ERROR, viesti on Connection failed'."

### Vaikeus 2: Opiskelijat näyttävät liikaa tai liian vähän

**Mitä kuuluu:** "Näytin kaikki 1000 riviä lokit" tai "Näytin vain virheen, mutta AI sanoo, että tarvitsee lisää kontekstia."

**Vastaus:** "Oikea määrä on yleensä: 10 riviä ennen virhettä, virherivit, 10 riviä jälkeen. Se on usein tarpeeksi."

**Strategia:** Opeta "konteksti-ikkuna" -käsite. Näytä esimerkki.

### Vaikeus 3: Opiskelijat ottavat kuvakaappauksia väärillä tavalla

**Mitä kuuluu:** "Otin kuvakaappauksen, mutta se näyttää liian pieneltä" tai "Unohdin näyttää virhetekstin."

**Vastaus:** "Kuvakaappauksen pitäisi näyttää ne alueet, joissa virhe on. Lisää kontekstia: mitä sovellusta, mitä vaiheessa?"

**Strategia:** Näytä hyvät ja huonot kuvakaappaukset. Näytä, miksi hyvä auttaa, huono ei.

### Vaikeus 4: Opiskelijat eivät ajattele turvallisuutta

**Mitä kuuluu:** "Eikö tämä ole vain lokit? Eikö ole vaaraa jakaa niitä?"

**Vastaus:** "Lokit voivat sisältää salasanoja, API-avaimia, käyttäjätietoja. Jos annat ne muille, järjestelmä voi olla vaarassa."

**Strategia:** Näytä todellinen esimerkki: lokit, jotka sisältävät salasanan. Näytä, miten hacker voisi käyttää sitä. Opeta muokkaamisen.

### Vaikeus 5: Opiskelijat eivät linkitä tätä omaan työhönsä

**Mitä kuuluu:** "Okei, ymmärrän lokit. Mutta mitä sillä on tekemistä siihen, mitä minä teen?"

**Vastaus:** "Joka päivä jotain menee pieleen. Tietokanta ei vasta, ohjelma kaatuu, verkkopyyntö epäonnistuu. Lokit ja kuvakaappaukset ovat ensimmäinen asia, jonka näet."

**Strategia:** Kysy: "Milloin sinulla oli ongelma, jonka ei löytänyt? Entä jos olisit antanut lokit ammattilaisen nähtäväksi?"

---

## Oppimisresurssit, joihin opettaja voi viitata

1. **Builder-materiaali (content/lessons/lesson-14.md):** Kaikki käsitteet ovat siellä.

2. **Esimerkit:** Etsi todellisia lokeja:
   - Apache/Nginx: `/var/log/apache2/`, `/var/log/nginx/`
   - Sovellus-lokit: variaatio sovelluksittain
   - Järjestelmä-lokit: `syslog`, Windows Event Viewer

3. **Kuvakaappausten ottaminen:** Näytä eri tavat:
   - Windows: PrintScreen, Snipping Tool
   - Mac: Cmd+Shift+4
   - Linux: Screenshot-sovellus

4. **AI-työkalut:** Näytä, miten jakaa kuvia AI:lle (ChatGPT, Claude, Copilot).

5. **Opiskelijoiden omat esimerkit:** Pyydä opiskelijoita tuomaan todellisia lokeja (anonymisoidut). Analysoi yhdessä.

