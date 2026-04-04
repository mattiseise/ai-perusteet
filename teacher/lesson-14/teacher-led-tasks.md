# Opettajavetoiset tehtävät

## Tehtävä 14.3: Live-ongelmanratkaisu — kuvakaappaus ja lokit

### Tavoite

Osoittaa konkreettisesti, kuinka kuvakaappaukset ja lokit tekevät ongelmanratkaisusta nopeampaa ja tarkempaa.

### Opettajan ohjeet ja fasilitaatio

Tämä tehtävä tehdään opettajan johdolla koko luokalle. Live-esittely on paras tapa näyttää, kuinka multimodaalinen lähestyminen toimii.

**Valmistelu (ennen lähiosaa):**
- Valmista kolme tekniikan ongelmaa, joista sinulla on kuvakaappaukset ja lokit
- Valitse ongelmat, jotka ovat opiskelijoille relevantteja (esim. tietokanta-yhteys, verkkopyyntö, skripti)
- Testaa AI:n kanssa etukäteen — näytä sekä huono että hyvä pyyntö
- Valmista lokit tai virheilmoitukset

**Tehtävän vaiheet (25 min):**

1. **Johdanto (1 min):** "Kun sinulla on ongelma, ensimmäinen asia on näyttää se, ei kuvata sitä."

2. **Esimerkki 1: Vain teksti vs. kuvakaappaus + lokit (10 min)**
   - Näytä huono pyyntö: "Tietokantaan ei saa yhteyttä. Voitko auttaa?"
   - Kerro, mitä AI:ltä kysytään: "Ehkä puuttuva asennus? Porttin ongelma? Salasana?"
   - Näytä hyvä pyyntö: "Tässä on kuvakaappaus virheilmoituksesta ja lokit. Näen 'Connection timeout' ja portti on oikein konfiguroitu (5432)."
   - Näytä AI:n vastaus: Paljon parempi, koska AI näkee todellisen virheellä.
   - Kysy luokalta: "Miksi toinen oli parempi?"

3. **Esimerkki 2: Lokin tulkinta (8 min)**
   - Näytä loki, jossa muisti loppuu
   - Kysy: "Mitä näet tässä logissa? Mihin jokainen rivi kertoo?"
   - Näytä, miten lokin rivejä luetaan: Aika, taso (WARNING, ERROR), viesti
   - Näytä AI:lle: "Lokin mukaan muisti kasvaa 10MB:n välein. Neljän minuutin kuluttua se on lopussa. Mitä ohjelma tekee?"
   - Näytä AI:n vastaus: Se tunnistaa muistin vuodon

4. **Esimerkki 3: Turvallisuus — mitä ei näytä (5 min)**
   - Näytä lokit, jotka sisältävät salasanan tai API-avaimen
   - Opeta, mitä muokata pois: `password: "***"`, `api_key: "sk-***xyz"`
   - Näytä esimerkki: Lokin ennen ja jälkeen

5. **Yhteenveto (1 min):** Kolme tärkeää asiaa:
   - Kuvakaappaukset tekevät kontekstista selväksi
   - Lokit kertovat, mitä tapahtui
   - Turvallisuus on kriittinen — ei koskaan salasanoja tai avaimia

### Odotettu oppimistulos

- Opiskelijat näkevät, että näyttäminen on tehokkain
- Opiskelijat ymmärtävät lokin rakennetta: aika, taso, viesti
- Opiskelijat osaa ajatella turvallisuudesta

---

## Tehtävä 14.4: Pienryhmä-harjoitus: Konteksti rakentaminen

### Tavoite

Opiskelija oppii keräämään oikean kontekstin ennen AI:lle kysymistä.

### Opettajan ohjeet ja fasilitaatio

Pienryhmät (2–3 henkilöä), opettaja valvoo ja auttaa.

**Valmistelu:**
- Jaa ryhmille neljä erilaista teknisten ongelmien skenaariota
- Varmista, että ryhmillä on pääsy lokeille tai kuvakaappausten esimerkkeihin

**Tehtävän vaiheet (20 min):**

1. **Skenaarion jakelu (1 min)**

2. **Konteksti rakentaminen (10 min):** Ryhmä miettii ja dokumentoi:
   - Mitä ohjelmaa / järjestelmää? (versio?)
   - Milloin virhe tapahtui?
   - Mitä sinä yritit tehdä?
   - Mitä virheilmoitus sanoi?
   - Mitä logit sanovat (jos saatavilla)?
   - Onko kuvakaappaus saatavilla?

3. **Pyyntö kirjoittaminen (8 min):** Ryhmä kirjoittaa **täsmällisen** pyynnön AI:lle.

4. **Raportointi (1 min per ryhmä):** Ryhmä sanoo:
   - Ongelma lyhyesti
   - Yksi kontekstin paremmin tekijä (kuvakaappaus, lokit, jne.)

### Skenaariot

**Skenaario A:** Python-skripti kaatuu satunnaisesti. Sinulla on kuvakaappaus virheilmoituksesta. Mitä muuta tarvitset?

**Skenaario B:** Docker-kontti ei käynnisty. Sinulla on `docker logs` -tuloste. Kuinka muodostat siihen pyynnön AI:lle?

**Skenaario C:** Verkkosivulla on virhe joskus, mutta et voi genneroida sitä omin päin. Sinulla on selaimesi console-lokit. Mitkä lokit ovat oleellisia?

**Skenaario D:** Node.js-sovellus vastaa hitaasti. Sinulla on performance-lokit 100 riviltä. Mitkä rivit ovat oleellisia AI:lle?

### Odotettu oppimistulos

- Opiskelijat näkevät, että konteksti rakentuu kertakerralta: lokit, kuvakaappaukset, koodi
- Opiskelijat osaa priorisioida mitä näyttää (mitä on oleellista?)
- Opiskelijat on valmiita tekemään todellisia ongelmanratkaisuja

