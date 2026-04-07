# Opettajavetoiset tehtävät

## Tehtävä 6.1: Multimodaalinen vs. pelkkä teksti — live-demonstraatio

### Tavoite
Näyttää opiskelijoille konkreettisesti, kuinka kuvakaappaus + teksti antaa tekoälylle paremmat mahdollisuudet auttaa IT-ongelmassa kuin pelkkä teksti.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**
- Valitse IT-ongelma, jolla on selvä visuaalinen komponentti: virheilmoitus, käyttöliittymävika, verkkosivun ongelma, konfiguraationäkymä, väreillä erotellut lokit jne.
- Ota kuvakaappaus ongelmasta.
- Kirjoita tekstikuvaus samasta ongelmasta (noin 150 sanaa).

**Oppitunnilla (20 min):**

1. **Johdanto (2 min):**
   - Kerro: "Tekoäly voi nyt nähdä kuvia. Entä jos näytämme kuvan kirjoittamisen sijaan? Muuttuuko vastaus? Tätä on multimodaalisuus — useita tietomuotoja."

2. **Ensimmäinen testi: vain teksti (5 min):**
   - Näytä tekstikuvaus ongelmasta ruudulla.
   - Lähetä se tekoälylle (ChatGPT-4V, Claude 3 jne.) samalla kysymyksellä: "Mikä on tämän ongelman syy ja miten korjaan sen?"
   - Dokumentoi vastaus.
   - Kysy opiskelijoilta: "Kuinka hyödyllinen tämä vastaus on? Antaako se tarkan ratkaisun?"

3. **Toinen testi: teksti + kuvakaappaus (5 min):**
   - Näytä sama tekstikuvaus sekä kuvakaappaus.
   - Lähetä molemmat tekoälylle (sama kysymys).
   - Dokumentoi vastaus.
   - Kysy: "Entä tämä vastaus? Onko se parempi? Miksi?"

4. **Vertailu (5 min):**
   - Piirrä taululle:
     ```
     | Vastaus | Spesifisyys | Käytännöllisyys | Visuaalisen tiedon käyttö |
     |---------|-------------|-----------------|---------|
     | Vain teksti | | | |
     | Teksti + kuva | | | |
     ```
   - Analyysi: "Näet, kuinka multimodaalisuus muuttaa vastausta. Tekoäly näki kuvan ja ymmärsi ongelman paremmin."

5. **Johtopäätös (3 min):**
   - Kerro: "Tämä on IT-ammattilaiselle tärkeä taito. Tiedät, milloin käyttää tekstiä, milloin kuvakaappauksia ja milloin molempia."

### Odotettu oppimistulos
- Opiskelijat näkevät konkreettisesti, kuinka multimodaalisuus parantaa vastauksia.
- He ymmärtävät, että kuvakaappaukset eivät ole vain "kauniita" — ne ovat toiminnallinen konteksti-informaatiotyökalu.

---

## Tehtävä 6.2: Multimodaalisen kontekstin suunnittelu — ohjattu harjoitus

### Tavoite
Opettaa opiskelijoille, kuinka rakentaa tehokas multimodaalinen konteksti — milloin käyttää tekstiä, milloin kuvakaappauksia, milloin lokitietoja tai koodia.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**
- Valitse IT-projekti, jonka opiskelijat tunnistavat (esim. verkkopalvelun debugging, tietokantaongelma jne.).

**Oppitunnilla (25 min):**

1. **Asetelman muutos (2 min):**
   - Kerro: "Nyt suunnittelemme multimodaalisen kontekstin. Se ei ole vain yksi kuvakaappaus — se on strateginen yhdistelmä eri tietomuotoja."

2. **Vaihe 1: Mitä materiaalia sinulla on? (5 min):**
   - Piirrä taululle:
     ```
     Materiaali | Esimerkki | Hyödyt | Haitat
     -----------|----------|--------|-------
     Teksti | Kuvaus... | Nopea, selkeä | Voi olla epäselvä
     Kuvakaappaus | Virheviesti | Näyttää tarkalleen | Iso token-kustannus
     Lokit | Error lines | Yksityiskohtainen | Voi olla sekainen
     Koodi | Funktio... | Rakenne näkyy | Pitkä
     ```
   - Kysy: "Mitä näistä sinulla on käytettävissä?"

3. **Vaihe 2: Miten valitset? (8 min):**
   - Käy läpi jokaisen valinnan logiikka:
     - **Teksti:** Jos ongelma on helppo kuvailla ja konteksti-ikkuna on pieni.
     - **Kuvakaappaus:** Jos visuaalinen tieto on kriittistä — väri, asettelu, kuvakkeet.
     - **Lokit:** Jos virhe näkyy yksityiskohtaisesti lokissa.
     - **Koodi:** Jos ongelma on koodissa — näytä relevantti osa.
   - Esimerkki: "Tässä on verkkopalvelun ongelma. Mitä tarvitaan?"
     - Teksti: "Sivulla näkyy error 500. Lisätty sähköpostiosoite."
     - Kuvakaappaus: Näyttää virheen sivulla näkyvissä väreissä.
     - Lokit: Palvelimen virheilmoitus.
     - Koodi: Kontrollerin funktio, joka aiheuttaa virheen.

4. **Vaihe 3: Yhdistäminen (7 min):**
   - Kirjoita taululle lopullinen "multimodaalinen konteksti":
     ```
     1. Teksti: "Käyttäjä raportoi error 500 -sivun näkyvän, kun he lähettävät lomakkeen X."
     2. Kuvakaappaus: [näyttää punaisen virheilmoituksen]
     3. Lokit: [viimeiset 5 virhettä palvelimen lokista]
     4. Koodi: [kontrollerin funktio, joka aiheuttaa virheen]
     ```
   - Selitä: "Tämä on tehokas. Tekoäly näkee ongelman monella tavalla. Se voi antaa paremman ratkaisun."

5. **Strategia ja rajoitukset (3 min):**
   - Korosta: "Mutta huomio: kuvakaappaukset ovat suuria. Jokainen kuva = 10 000 tokenia. Joten käytä 1–2, ei kymmentä."
   - "Jos konteksti-ikkuna täyttyy, poista kuvakaappaus — pidä teksti ja lokit."

### Odotettu oppimistulos
- Opiskelijat näkevät, että multimodaalinen konteksti on strategista valintaa, ei kaiken heittämistä kerralla.
- He ymmärtävät token-kustannukset ja osaavat tehdä älykkäitä valintoja.