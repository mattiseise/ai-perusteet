# Opettajavetoiset tehtävät

## Tehtävä 4.1: "Sama kysymys, kaksi kontekstia" — Käytännön vertailu luokassa

### Tavoite
Rakentaa konkreettisesti ymmärrys siitä, kuinka dramaattisesti konteksti ja prompti vaikuttavat tekoälyn vastauksen hyödyllisyyteen. Osoittaa opiskelijoille, että parempi vastaus ei tule pelkästään paremmasta promptista, vaan paremmasta kontekstista ja sen pohjalle rakentuvasta terävästä promptista.

### Opettajan ohjeet ja fasilitointi

**Valmistelu (5 min ennen oppituntia):**
- Valitse IT-aihe, jonka tunnet ja jonka opiskelijasi ymmärtävät. Esim. "Tietokannan optimointi", "Python-debuggaus", "verkkokytkinten konfigurointi"
- Kirjoita kaksi kyselyä valmiiksi:
  1. Huono kysymys: vain yksittäinen lause ilman kontekstia. Esim. "Kuinka optimoin tietokantaa?"
  2. Hyvä kysymys: sisältää sekä vahvan kontekstin (rooli, tausta, tavoite, rajaukset, esimerkki) että terävän promptin (tavoite, rooli, rajat, formaatti, esimerkit).

**Oppitunnilla (20 min):**

1. **Johdanto (3 min):**
   - Näytä opiskelijoille molemmat kysymykset rinnakkain ruudulla.
   - Kerro: "Käytämme samaa tekoälyä kaksi kertaa. Ensimmäinen kerta ilman kontekstia ja heikolla promptilla, toinen kerta hyvällä kontekstilla ja terävällä promptilla. Vertaamme vastauksia."

2. **Kysely 1 — Ilman kontekstia ja heikolla promptilla (5 min):**
   - Lähetä huono kysymys tekoälylle ruudulla opiskelijoiden katsellessa.
   - Lue vastaus ääneen tai näytä se.
   - Kysy luokalta:
     - "Kuinka hyödyllinen tämä vastaus on sinulle IT-opiskelijana?"
     - "Mitä tietoa puuttuu? Mitkä kontekstin osat puuttuivat?"
     - "Kuinka pitkä vastaus on?" (lasketaan sanamäärä tai rivit)
     - "Millä osaamistasolla vastaus oli?"

3. **Kysely 2 — Hyvällä kontekstilla ja terävällä promptilla (5 min):**
   - Lähetä hyvä kysymys samalle tekoälylle.
   - Lue vastaus ääneen.
   - Kysy luokalta:
     - "Kuinka paljon parempi tämä on?"
     - "Mitkä osat kontekstista auttoivat tekoälyä?"
     - "Millä tavalla prompti teki pyynnöstä terävän?"
     - "Voisitko käyttää tätä vastausta suoraan omassa projektissa?"

4. **Analyysi ja pohdinta (7 min):**
   - Kirjoita liitutaululle:
     | Aspekti | Vastaus 1 | Vastaus 2 |
     |---------|-----------|-----------|
     | Pituus | | |
     | Spesifisyys | | |
     | Soveltuvuus | | |
     | Osaamistaso | | |
   - Keskustele yhdessä:
     - "Muuttuiko tekoäly vai konteksti ja prompti?"
     - "Mitä kontekstin osia käytimme?"
     - "Mitkä promptin elementit tekivät pyynnöstä selkeän?"

**Fasilitointikysymykset:**
- Jos opiskelija sanoo "vastaus 1 oli hyvin yleinen": "Niin, miksi? Koska tekoäly ei tiennyt, mitä tarvitsit — ei kontekstia, ei terävää promptia."
- Jos opiskelija sanoo "vastaus 2 oli pidempi": "Entä jos se oli tarkempi ja paremmin kohdistettu? Oliko pituus ongelma vai etu?"
- "Voimme erottaa kaksi asiaa: konteksti antaa pohjan, prompti esittää spesifin pyynnön. Kumpi oli tärkeämpi tässä esimerkissä?"

### Odotettu oppimistulos
- Opiskelijat ymmärtävät, että konteksti ja prompti yhdessä määrittävät vastauksen laatua.
- He näkevät konkreettisesti, että konteksti ja terävä prompti säästävät aikaa ja antavat hyödyllisempiä vastauksia.
- He tunnistavat kontekstin viisi osaa ja promptin viisi elementtiä käytännössä.
- He ymmärtävät eron "hyvän kontekstin" ja "hyvän promptin" välillä.

---

## Tehtävä 4.2: "Kontekstin ja promptin rakentaminen yhdessä" — Ohjattu kirjoittaminen ryhmässä

### Tavoite
Oppia rakentamaan sekä konteksti että prompti vaihe vaiheelta opettajan ohjauksella niin, että jokainen opiskelija näkee prosessin. Näyttää, kuinka viiden komponentin konteksti ja viiden elementin prompti toimivat yhdessä.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**
- Valitse todellinen IT-ongelma, jonka opiskelijasi tunnistavat. Esim. "Linux-palvelimen SSH-ongelma" tai "SQL-tietokannan hidas haku"
- Kirjoita taululle tai diaan sekä viiden komponentin kontekstin malli että viiden elementin promptin malli.

**Oppitunnilla (30 min):**

1. **Asetelman muutos (2 min):**
   - Kerro: "Nyt rakennamme sekä kontekstin että promptin yhdessä vaiheittain. Konteksti on pohja, prompti on kysymys sen päälle."

**Kontekstin rakentaminen (15 min):**

2. **Vaihe 1: Rooli (3 min):**
   - Kirjoita tauluun: "KONTEKSTI — Rooli: ___?"
   - Kysy opiskelijoilta: "Keitä te olette tässä ongelmassa?"
   - Täytä yhdessä esim. "Olen IT-opiskelija, neljän viikon Linux-kurssilla"
   - Selitä: "Rooli auttaa tekoälyä valitsemaan sopivan tason — opiskelijalle vai ammattilaiselle."

3. **Vaihe 2: Taustatieto (3 min):**
   - Kirjoita taululle: "Taustatieto: ___?"
   - Kysy: "Mitä olemme jo yrittäneet? Mitä jo tiedämme?"
   - Täytä esim. "Palvelin on Ubuntu 20.04. SSH-avain on generoitu. Kirjautuminen epäonnistuu, virheviesti on 'Permission denied (publickey)'"
   - Selitä: "Taustatieto auttaa tekoälyä välttämään arvailua — se tietää, mitä olet jo yrittänyt."

4. **Vaihe 3: Tavoite (3 min):**
   - Kirjoita taululle: "Tavoite: ___?"
   - Kysy: "Mitä haluat saavuttaa? Ja miksi?"
   - Täytä esim. "Haluan ottaa SSH-yhteyden tuotantopalvelimelle ja debugata siellä olevaa web-sovellusta."
   - Selitä: "Tavoite fokusoi vastauksen — tekoäly tietää, mihin vastaus pitää kohdistaa."

5. **Vaihe 4: Rajaukset (2 min):**
   - Kirjoita taululle: "Rajaukset: ___?"
   - Kysy: "Mitä et halua? Mitä lähestymistapoja haluat välttää?"
   - Täytä esim. "En halua muuttaa palvelimen SSH-asetuksia. Haluan oppia, miksi avain ei toimi."
   - Selitä: "Rajaukset eliminoivat turhaa sisältöä — ei turhia vaihtoehtoja."

6. **Vaihe 5: Esimerkki (2 min):**
   - Kirjoita taululle: "Esimerkki: ___?"
   - Kysy: "Voimmeko antaa virheilmoituksen? Koodinäytteen?"
   - Näytä esim.: "Komento: `ssh -v user@192.168.1.100`. Virheilmoitus alkaa: `debug1: Offering public key: /home/student/.ssh/id_rsa`..."
   - Selitä: "Esimerkki auttaa tekoälyä näkemään tarkalleen, mitä tapahtuu."

7. **Lopullinen konteksti (2 min):**
   - Kirjoita taululle kaikki osat yhteen: "Olen IT-opiskelija (neljän viikon Linux-kurssilla). Yritän muodostaa SSH-yhteyden Ubuntu 20.04 -palvelimelle. SSH-avain on generoitu, mutta autentikointi epäonnistuu: Permission denied (publickey). Tavoite: löytää ongelma ja oppia oikea ratkaisu — en halua muuttaa palvelimen SSH-asetuksia. Tässä virheilmoitus..."
   - Näytä: "Konteksti on valmis! Nyt rakennamme sen päälle promptin."

**Promptin rakentaminen (12 min):**

8. **Vaihe 6: Tavoite (promptissa) (2 min):**
   - Kirjoita tauluun: "PROMPTI — Tavoite (goal): ___?"
   - Kysy: "Mitä haluat tekoälyn tekevän nyt?"
   - Täytä esim. "Auta minua selvittämään, miksi SSH-autentikointi epäonnistuu."
   - Selitä: "Tavoite kertoo tekoälylle, mitä haluat sen tekevän juuri nyt."

9. **Vaihe 7: Rooli (promptissa) (2 min):**
   - Kirjoita taululle: "Rooli (promptissa): ___?"
   - Kysy: "Millä tasolla tekoäly pitää vastata?"
   - Täytä esim. "Vastaa kuin opettaisit aloittelijalle — älä käytä liian syvälle menevää tekniikkaa."
   - Selitä: "Rooli varmistaa, että vastaus on sopivalla tasolla."

10. **Vaihe 8: Rajat (promptissa) (2 min):**
    - Kirjoita taululle: "Rajat: ___?"
    - Kysy: "Mitä et halua vastauksessa?"
    - Täytä esim. "En halua SSH-palvelimen konfiguraation muuttamista — fokus pitää olla asiakkaalla."
    - Selitä: "Rajat pitävät vastauksen fokuksessa."

11. **Vaihe 9: Formaatti (2 min):**
    - Kirjoita taululle: "Formaatti: ___?"
    - Kysy: "Miten haluat vastauksen muotoilun?"
    - Täytä esim. "Numeroidut vaiheet, jokaisen vaiheen kohdalla selitys siitä, miksi se tarvitaan."
    - Selitä: "Formaatti varmistaa, että saat käyttökelpoisen tuloksen."

12. **Vaihe 10: Esimerkit (promptissa) (2 min):**
    - Kirjoita taululle: "Esimerkit: ___?"
    - Kysy: "Voisiko meillä olla esimerkki siitä, millainen vastaus olisi hyvä?"
    - Täytä esim. "Esimerkiksi: Vaihe 1: Tarkista avainten oikeudet (`ls -la ~/.ssh/`) — tämä kertoo, onko avain luettavissa."
    - Selitä: "Esimerkit tekevät vaatimuksista konkreettisempia."

13. **Lopullinen prompti (2 min):**
    - Kirjoita taululle lopullinen terävä prompti, joka yhdistää kontekstin ja promptin elementit:
    "Auta minua debugaamaan SSH-autentikointi-ongelma. Vastaa kuten opettaisit aloittelijalle — älä käytä liian monimutkaista tekniikkaa, ja fokus vain asiakkaan puolen ongelmaan, älä palvelimen konfiguraatioon. Vastaa numeroituina vaiheina. Jokaisen vaiheen kohdalla selitä, mitä teemme ja miksi. Esimerkiksi: Vaihe 1: Tarkista avainten oikeudet (`ls -la ~/.ssh/`) — tämä kertoo, onko avain luettavissa ja sopivilla oikeuksilla."
    - Näytä: "Tämä on terävä, kontekstiin perustuva prompti!"

**Fasilitointikysymykset:**
- "Entä jos jättäisimme roolin kontekstista pois? Miksi se vaikuttaa?"
- "Kuinka paljon erilaisempi vastaus olisi ilman taustatieto-osaa?"
- "Mitä eroa on kontekstin roolilla ja promptin roolilla?"
- "Voimmeko käyttää samaa promptia ilman kontekstia? Miksi tai miksi ei?"

### Odotettu oppimistulos
- Opiskelijat näkevät jokaisen komponentin ja elementin roolin ja hyödyn.
- He ymmärtävät, että konteksti on pohja ja prompti on kysymys sen päälle.
- He pystyvät tunnistamaan, mitkä osat kontekstista ja promptista puuttuvat omasta kysymyksestään.
- He näkevät, että konteksti ja prompti toimivat yhdessä — konteksti antaa pohjan, prompti esittää spesifin pyynnön.