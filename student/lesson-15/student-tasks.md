# Opiskelutehtävät

## Tehtävä 15.1: Kirjoita dokumentaatio AI:n avulla

### Tavoite

Oppia käyttämään AI:ta dokumentaation kirjoittamiseen ja nähdä, miten dokumentaation pohja voidaan luoda nopeasti.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

**TT-A3 – Luo README-tiedosto projektille**

1. Valitse yksi seuraavista projektityypeistä:
   - Python-skripti, joka analysoi CSV-tiedostoja
   - Node.js Express REST API
   - Django-verkkosovellus
   - Docker-palvelu

2. Pyydä AI:ta luomaan README-pohja projektille. Sisällytä:
   - Kuvaus: Mitä projekti tekee? (2-3 lausetta)
   - Vaatimukset: Mitä tarvitaan (Python 3.8+, Node 16 jne.)
   - Asennus: Vaiheittain (3-5 vaihetta)
   - Käyttö: Esimerkki (1-2 esimerkkiä)
   - Testit: Miten testeja ajetaan
   - Kontribuointi: Lyhyt ohjeistus

3. Säilö AI:n tuottama README (3-4 koko sitä ei pyydä muuttamaan)

4. **Muokkaa sitten README:a** ammattilaisemmaksi:
   - Lisää todelliset komennot (koodattavat komennot, ei vain yleiskuvaus)
   - Lisää linkkejä dokumentaatioon
   - Lisää esimerkkejä riveinä, joita voi kopioida

5. Kirjoita huomio siitä, miten AI auttoi:
   - Mitä oli hyvää? (rakenne, nopeus, ideat)
   - Mitä puuttui? (spesifikaatiot, esimerkit, yksityiskohdat)

### Odotettu tuotos

- AI:n tuottama README-pohja
- Muokattu, parempi versio
- Huomio: Mitä opitte

**Jos teet tehtävän yksin:**
Tee README yhteen projektityyppiin ja muokkaa se perusteellisesti.

---

## Tehtävä 15.2: Lokin analyysi ja vianseuranta

### Tavoite

Oppia analysoimaan lokeja ja käyttämään AI:ta apuna virheiden löytämisessä.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

**TT-A2 – Analysoi loki ja etsi virhe**

Sinulle annetaan kolme eri lokeista näytettä. Jokaiselle:

1. Lue loki läpi ja etsi ERROR tai CRITICAL -rivit
2. Merkitse:
   - Milloin virhe tapahtui? (aika)
   - Mikä virhe oli? (viesti)
   - Mitä tapahtui sen jälkeen? (seuraavat rivit)

3. Pyydä AI:ta: "Analysoi tämä loki. Etsi virherivit ja selitä: Mitä meni pieleen? Miksi se tapahtui? Mitä pitää korjata?"

4. Vertaa AI:n vastausta omaan analyysiin:
   - Näki AI virheet, joita sinä ei nähnyt?
   - Näit sinä asioita, joita AI ei nähnyt?
   - Mikä oli AI:n analyysi tarkempi vai väärä?

### Lokit analysoitavaksi

**Loki 1: Muistin ongelma**
```
2024-03-14 08:00:00 INFO: Service started
2024-03-14 08:05:15 INFO: Loaded 1000 records
2024-03-14 08:07:30 WARNING: Memory usage at 70%
2024-03-14 08:09:45 WARNING: Memory usage at 85%
2024-03-14 08:10:00 ERROR: Out of memory - cannot allocate 100MB
2024-03-14 08:10:01 FATAL: Service crashed
```

**Loki 2: Verkon timeout**
```
2024-03-14 10:00:00 INFO: Starting sync with remote server
2024-03-14 10:00:05 INFO: Connected to server at 192.168.1.50
2024-03-14 10:00:10 INFO: Sending 500 records
2024-03-14 10:01:00 WARNING: Transfer rate is slow (10KB/s)
2024-03-14 10:02:00 ERROR: Network timeout after 120 seconds
2024-03-14 10:02:01 INFO: Retrying connection
2024-03-14 10:02:30 ERROR: Network timeout after 120 seconds
2024-03-14 10:02:31 FATAL: Failed to sync after 2 attempts
```

**Loki 3: Tietokannan lukitus**
```
2024-03-14 12:00:00 INFO: Starting database operation
2024-03-14 12:00:05 INFO: User 'admin' connected to database
2024-03-14 12:00:10 WARNING: Table 'users' is locked by another process
2024-03-14 12:00:15 WARNING: Waiting for lock...
2024-03-14 12:00:30 WARNING: Lock still held, waiting...
2024-03-14 12:01:00 ERROR: Operation timeout - could not acquire lock
2024-03-14 12:01:01 FATAL: Database operation failed
```

### Odotettu tuotos

- Kolmen lokin analyysit (omat havainnot)
- AI:n analyysit kutakin lokeista
- Vertailu: Mitä näit sinä? Mitä näki AI?

**Jos teet tehtävän yksin:**
Analysoi kaksi lokeista itse ja AI:lla.

---

## Tehtävä 15.3: CLI-komennot ja shell-skriptit

### Tavoite

Oppia kirjoittamaan CLI-komentoja AI:n avulla — ja ennen kaikkea ymmärtämään niitä ennen kuin ajat.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

**TT-C2 – Komennon ymmärrys ja turvallisuus**

Sinulle annetaan neljä tehtävää. Jokaista:

1. Pyydä AI:ta generoimaan komento/skripti
2. **Analyysivaihe:** Jokaiselle osalle kirjoita:
   - Mitä tämä komento/vaihe tekee? (omin sanoin)
   - Mitkä ovat vaaralliset osat? (esim. `-delete`, `rm`)
   - Mitä sinun täytyy tarkistaa ennen ajamista?

3. Kirjoita **turvallisuusvaroitus:** Mitä voisi mennä pieleen?

### Tehtävät

**Tehtävä 1: Varmuuskopioi kaikki tiedostot paitsi lokit**
- Pyydä: "Kirjoita komento, joka kopioi kaikki tiedostot hakemistosta 'src/' hakemistoon 'backup/', paitsi tiedostot, joiden nimi päättyy '.log'"
- Analysoi AI:n komento (find? rsync? tar?)
- Kirjoita: Mitä jokainen vippu tekee?
- Turvallisuus: Mitä pitää tarkistaa?

**Tehtävä 2: Poista yli 30 päivää vanhat tiedostot**
- Pyydä: "Kirjoita shell-skripti, joka poistaa kaikki tiedostot 'temp/' -hakemistosta, jotka ovat yli 30 päivää vanhat. Skripti saa kirjaaa poistettujen tiedostojen määrän logiin."
- Analysoi AI:n skripti (how loops? find?)
- Kirjoita: Mitä tämä skripti tekee riviltä riviltä?
- Turvallisuus: Miten testataan ensin (ilman poistamista)?

**Tehtävä 3: Etsi kaikki Python-tiedostot, joissa ei ole testejä**
- Pyydä: "Kirjoita komento, joka etsi kaikki Python-tiedostot (.py) 'src/' hakemistosta, joihin TEKSTI 'import unittest' tai 'import pytest'. Listaa tiedostonimet."
- Analysoi AI:n komento (grep? find?)
- Kirjoita: Miten tämä komento toimii?
- Turvallisuus: Voiko tämä vahingoittaa tiedostoja?

**Tehtävä 4: Automatisoi päivittäisen kunnossapidon**
- Pyydä: "Kirjoita shell-skripti, joka päivittäin (ajettavaksi cron-jobilla): (1) Katsoo sovelluksen lokeja, (2) Etsi ERROR-rivejä, (3) Lähettää summaa sähköpostiin. Skripti saa kutsua: ./daily-maintenance.sh"
- Analysoi AI:n skripti (grep? mail? cron?)
- Kirjoita: Mitä jokainen osa tekee?
- Turvallisuus: Mitä pitää konfiguroida turvallisesti (sähköpostiosoitteet jne)?

### Odotettu tuotos

- Neljä AI-generoimaa komentoa/skriptiä
- Neljä analyysia: "Mitä tämä tekee?"
- Neljä turvallisuusvaroitusta: "Mitä voisi mennä pieleen?"
- Näyttö siitä, että ymmärrät ennen ajamista, etkä vain kopioi-liitä

**Jos teet tehtävän yksin:**
Tee kaksi tehtävää täydellisesti.

