# Opiskelutehtävät

## Tehtävä 14.1: Tekstistä näyttöön — ongelman dokumentointi

### Tavoite

Oppia muuttamaan epämääräinen kuvailu konkreettiseksi näytöksi.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

**TT-A3 – Dokumentoi ongelma multimodaalisesti**

Sinulle annetaan neljä tekniikan ongelmaa tekstinä. Jokaiselle:

1. Avaa vastuullinen ohjelma tai simuloi tilannetta
2. Ota kuvakaappaus siitä, mitä näet
3. Kirjoita **hyvä kuvaus** AI:lle, joka sisältää:
   - Mitä yritit tehdä?
   - Mitä tapahtui (virheilmoitus, käyttäytyminen)?
   - Mitä haluaisit tapahtua?
   - Mitkä ovat olosuhteet (ohjelmaversio, käyttöjärjestelmä)?

### Ongelmat simuloitavaksi tai kuvailtavaksi

1. **"Sain komentorivissä virheen MySQL:stä."**
   - Simuloi: Yritä muodostaa yhteys väärään palvelimeen tai portiin
   - Ota kuvakaappaus virheilmoituksesta
   - Kirjoita kuvaus AI:lle (3–5 lausetta)

2. **"Verkkosivuni kaatuu, mutta en tiedä miksi."**
   - Avaa selain, mene satunnaisen sivun lähelle
   - Avaa kehitystyökalut (F12), näytä Console tai Network
   - Ota kuvakaappaus virheistä
   - Kirjoita kuvaus (3–5 lausetta)

3. **"Python-skripti ei toimi — se antaa outoja tuloksia."**
   - Avaa editori, kirjoita pieni Python-skripti, jossa on vika
   - Ota kuvakaappaus koodista ja tulosteesta
   - Kirjoita kuvaus (3–5 lausetta)

4. **"Docker-kontti ei käynnisty."**
   - Simuloi tai muistele virhettä: Yritä ajaa Docker-komentoa, joka epäonnistuu
   - Ota kuvakaappaus docker-virheestä
   - Kirjoita kuvaus (3–5 lausetta)

### Odotettu tuotos

- Neljä kuvakaappusta neljästä ongelmasta
- Neljä kunnollista kuvausta, joissa on konteksti, virhe ja mitä tapahtui

**Jos teet tehtävän yksin:**
Tee kaksi neljästä ongelmasta täydellisesti.

---

## Tehtävä 14.2: Loki-analyysit

### Tavoite

Oppia lukemaan lokeja ja ottamaan niistä oleellisen osan AI:lle.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

**TT-A2 – Loki-data ja konteksti**

Sinulle annetaan neljä erilaista lokia. Jokaiselle:

1. Lue lokin läpi ja etsi virhe tai varoitus
2. Merkitse oleelliset rivit
3. Kopioi ne ja muotoile **AI:lle** seuraavasti:
   - Konteksti (mitä ohjelmaa, mitä tapahtui)
   - Lokin relevantti osio (15–20 rivi)
   - Kysymys (mitä tämä tarkoittaa, mikä on vika?)

### Lokit analysoitavaksi

**Loki 1: Tietokanta-yhteys epäonnistuu**
```
2024-03-14 10:23:45 INFO: Starting application
2024-03-14 10:23:46 INFO: Connecting to database at localhost:5432
2024-03-14 10:23:48 ERROR: Failed to connect to database
2024-03-14 10:23:48 ERROR: Connection timeout after 2000ms
2024-03-14 10:23:49 WARNING: Retrying connection attempt 1 of 3
2024-03-14 10:23:51 ERROR: Failed to connect to database
2024-03-14 10:23:51 WARNING: Retrying connection attempt 2 of 3
2024-03-14 10:23:53 ERROR: Failed to connect to database
2024-03-14 10:23:53 ERROR: Max retry attempts exceeded. Giving up.
2024-03-14 10:23:53 FATAL: Application shutdown due to database error
```
Kirjoita kuvaus AI:lle.

**Loki 2: Muistin loppuminen**
```
2024-03-14 11:00:00 INFO: Process started with 256MB memory limit
2024-03-14 11:02:30 WARNING: Memory usage at 75% (192MB)
2024-03-14 11:02:45 WARNING: Memory usage at 85% (217MB)
2024-03-14 11:02:50 WARNING: Memory usage at 95% (243MB)
2024-03-14 11:02:52 ERROR: Out of memory - cannot allocate 50MB
2024-03-14 11:02:52 FATAL: Process killed due to memory exhaustion
```
Kirjoita kuvaus AI:lle.

**Loki 3: Verkko-timeout**
```
2024-03-14 12:15:00 INFO: API call to https://api.example.com/users
2024-03-14 12:15:05 WARNING: Request took 5 seconds (expected < 2 sec)
2024-03-14 12:15:10 ERROR: HTTP request timeout after 10 seconds
2024-03-14 12:15:10 INFO: Retrying request
2024-03-14 12:15:20 ERROR: HTTP request timeout after 10 seconds
2024-03-14 12:15:20 INFO: Retrying request
2024-03-14 12:15:30 ERROR: HTTP request timeout after 10 seconds
2024-03-14 12:15:30 ERROR: Max retries exceeded, giving up
2024-03-14 12:15:30 FATAL: API integration failed
```
Kirjoita kuvaus AI:lle.

**Loki 4: Oikeudennus-virhe**
```
2024-03-14 13:45:00 INFO: User login attempt from 192.168.1.100
2024-03-14 13:45:00 INFO: Checking credentials for user: admin
2024-03-14 13:45:01 ERROR: Authentication failed: Wrong password
2024-03-14 13:45:02 INFO: User login attempt from 192.168.1.100
2024-03-14 13:45:02 INFO: Checking credentials for user: admin
2024-03-14 13:45:03 ERROR: Authentication failed: Wrong password
2024-03-14 13:45:04 INFO: User login attempt from 192.168.1.100
2024-03-14 13:45:04 WARNING: Multiple failed login attempts detected (3 in 5 seconds)
2024-03-14 13:45:04 WARNING: Blocking IP 192.168.1.100 for 15 minutes
```
Kirjoita kuvaus AI:lle.

### Odotettu tuotos

- Neljä kuvausta neljästä logista
- Kussakin kuvauksessa: konteksti, oleellinen loki-osio, ja huolellinen kysymys AI:lle

**Jos teet tehtävän yksin:**
Tee kaksi neljästä lokeista täydellisesti.

