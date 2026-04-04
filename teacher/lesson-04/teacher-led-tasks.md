# Opettajavetoiset tehtävät

## Tehtävä 4.1: "Sama kysymys, kaksi kontekstia" — Käytännön vertailu luokassa

### Tavoite
Rakentaa konkreettisesti ymmärrys siitä, kuinka dramaattisesti konteksti vaikuttaa tekoälyn vastauksen hyödyllisyyteen. Osoittaa opiskelijoille, että "parempi vastaus" ei tule paremmalta promptilta, vaan paremmalta kontekstilta.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu (5 min ennen oppituntia):**
- Valitse IT-aihe, jonka tiedät ja jonka opiskelijanpoikasi ymmärtävät. Esim. "Tietokannan optimointi", "Python-debuggaus", "Verkkokytkimen konfigurointi"
- Kirjoita kaksi kyselyä valmiiksi:
  1. Huono kysymys: Vain yksittäinen lause ilman kontekstia. Esim. "Kuinka optimoin tietokantaa?"
  2. Hyvä kysymys: Sisältää roolin, taustan, tavoitteen, rajaukset ja esimerkin.

**Oppitunnilla (20 min):**

1. **Johdanto (3 min):**
   - Näytä opiskelijoille molempat kysymykset rinnakkain ruudulla.
   - Kerro: "Käytetään samaa tekoälyä kahteen kertaan. Ensimmäinen kerta ilman kontekstia, toinen kerta hyvällä kontekstilla. Vertaamme vastauksia."

2. **Kysely 1 — Ilman kontekstia (5 min):**
   - Lähetä huono kysymys tekoälylle ruudulla oikeiden opiskelijoiden katselessa.
   - Lue vastaus ääneen tai näytä se.
   - Kysy luokalta:
     - "Kuinka hyödyllinen tämä vastaus on sinulle IT-opiskelijana?"
     - "Mitä tietoa puuttuu?"
     - "Kuinka kauan on vastaus?" (lasketaan sanaväli tai rivit)

3. **Kysely 2 — Hyvällä kontekstilla (5 min):**
   - Lähetä hyvä kysymys samaiselle tekoälylle.
   - Lue vastaus ääneen.
   - Kysy luokalta:
     - "Kuinka paljon parempi tämä on?"
     - "Mitkä osat kontekstista auttoi tekoälyä?"
     - "Voitko käyttää tätä vastusta suoraan omassa projektissa?"

4. **Analyysi ja pohdinni (7 min):**
   - Kirjoita liitutaululle:
     | Aspekti | Vastaus 1 | Vastaus 2 |
     |---------|-----------|-----------|
     | Pituus | | |
     | Spesifisyys | | |
     | Soveltuvuus | | |
   - Keskustele yhdessä:
     - "Muuttuiko tekoäly vai konteksti?"
     - "Mitä kontekstin osia käytimme?"

**Fasilitointikysymykset:**
- Jos opiskelija sanoo "vastaus 1 oli hyvin yleinen": "Niin, miksi? Koska tekoäly ei tiennyt, mitä tarvitsit."
- Jos opiskelija sanoo "vastaus 2 oli pidempi": "Entä jos se oli tarkempi? Oliko pituus ongelma vai etu?"

### Odotettu oppimistulos
- Opiskelijat ymmärtävät, että konteksti, ei prompti, määrittää vastauksen laatua.
- He näkevät konkreettisesti, että konteksti säästää aikaa ja antaa hyödyllisempiä vastauksia.
- He tunnistavat kontekstin viisi osaa käytännössä.

---

## Tehtävä 4.2: "Kontekstin rakentaminen yhdessä" — Ohjattu kirjoitus ryhmässä

### Tavoite
Oppia rakentamaan konteksti vaihe vaiheelta opettajan ohjuksella, niin että jokainen opiskelija näkee prosessin.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
- Valitse todellinen IT-ongelma, jota opiskelijat tunnustavat. Esim. "Linux-palvelimen SSH-ongelma" tai "SQL-tietokannan hidas haku"
- Kirjoita taulu- tai diaksi viiden komponentin malli.

**Oppitunnilla (25 min):**

1. **Asetusmuutos (2 min):**
   - Kerro: "Nyt rakennamme kontekstin yhdessä vaihe vaiheelta. Jokainen vaihe lisää tarkuutta."

2. **Vaihe 1: Rooli (3 min):**
   - Kirjoita tauluun: "Rooli: ___?"
   - Kysy opiskelijoilta: "Ketkä te olette tässä ongelmassa?"
   - Täytä yhdessä esim. "Olen IT-opiskelija, neljän viikon Linux-kurssilla"
   - Selitä: "Rooli auttaa tekoälyä valitsemaan sopivan tason — opiskelijalle vai ammattilaiselle?"

3. **Vaihe 2: Taustatieto (4 min):**
   - Kirjoita tauluun: "Taustatieto: ___?"
   - Kysy: "Mitä olemme jo yrittäneet? Mitä jo tiedämme?"
   - Täytä esim. "Palvelin on Ubuntu 20.04. SSH-avain on generoitu. Kelpuutus epäonnistuu, virheviesti on 'Permission denied (publickey)'"
   - Selitä: "Taustatieto auttaa tekoälyä olemaan arvailematta — se tietää, mitä olet jo yrittänyt."

4. **Vaihe 3: Tavoite (3 min):**
   - Kirjoita: "Tavoite: ___?"
   - Kysy: "Mitä haluat saavuttaa? Entä miksi?"
   - Täytä esim. "Haluan ottaa SSH-yhteyttä tuotantopalvelimelle ja siellä olevan web-sovelluksen debuggaus."
   - Selitä: "Tavoite fokusoi vastauksen — tekoäly tietää, mihin vastaus pitää kohdistaa."

5. **Vaihe 4: Rajaukset (3 min):**
   - Kirjoita: "Rajaukset: ___?"
   - Kysy: "Mitä et halua? Mitä lähestymistavasavoitko välttää?"
   - Täytä esim. "En halua muuttaa palvelimen SSH-asetuksia. Haluan oppia, miksi avain ei toimi."
   - Selitä: "Rajaukset elimioivat turhaa vastauspalaa — ei turhia vaihtoehtoja."

6. **Vaihe 5: Esimerkki (3 min):**
   - Kirjoita: "Esimerkki: ___?"
   - Kysy: "Voimme antaa virheilmoituksen? Koodin näytteen?"
   - Näytä esim.: "Komento: `ssh -v user@192.168.1.100`. Virheilmoitus alkaa: `debug1: Offering public key: /home/student/.ssh/id_rsa`..."
   - Selitä: "Esimerkki auttaa tekoälyä näkemään tarkalleen, mitä tapahtuu."

7. **Lopullinen konteksti (5 min):**
   - Kirjoita kaikki osat yhteen logiikaksi: "Olen IT-opiskelija (neljän viikon Linux-kurssilla). Yritän SSH-yhteyttä Ubuntu 20.04 -palvelimelle. SSH-avain on generoitu, mutta autentikikointi epäonnistuu: Permission denied (publickey). Tavoite: löytää ongelma ja oppia oikea ratkaisu — en halua muuttaa palvelimen SSH-asetuksia. Tässä virheilmoitus..."
   - Näytä: "Tämä konteksti on valmis tekoälylle!"

**Fasilitointikysymykset:**
- "Entä jos jättäisimme rooli-osan pois? Miksi se vaikuttaa?"
- "Kuinka paljon erilaisempi vastaus olisi ilman taustatieto-osaa?"

### Odotettu oppimistulos
- Opiskelijat näkevät jokaisen komponentin roolin ja hyödyn.
- He ymmärtävät, että konteksti on rakentamisen prosessi, ei vain "kirjoita paljon tekstiä".
- He pystyvät tunnistamaan, mitkä osat kontekstista puuttuvat omasta kysymyksestään.
