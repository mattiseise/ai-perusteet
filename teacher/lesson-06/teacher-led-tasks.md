# Opettajavetoiset tehtävät

## Tehtävä 6.1: Multimodaalinen vs. pelkkä teksti — Live-demonstraatio

### Tavoite
Näyttää opiskelijoille konkreettisesti, kuinka kuvakaappaus + teksti antaa tekoälylle paremmat mahdollisuudet auttaa IT-ongelmassa kuin vain teksti.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
- Valitse IT-ongelma, jolla on selvä visuaalinen komponentti: virheilmoitus, UI-vika, verkkosivun ongelma, konfiguraatio-näyttö, lokit väreillä jne.
- Ota kuvakaappaus ongelmasta.
- Kirjoita tekstikuvaus samasta ongelmasta (noin 150 sanaa).

**Oppitunnilla (20 min):**

1. **Johdanto (2 min):**
   - Kerro: "Tekoäly voi nyt nähdä kuvia. Entä muuttuu vastaus, jos näytämme kuvan sijaan kirjoitamme?" Tämä on multimodaalisuus — useampi tietomuoto."

2. **Ensimmäinen testi: Vain teksti (5 min):**
   - Näytä tekstikuvaus ongelmaista ruudulla.
   - Lähetä se tekoälylle (ChatGPT-4V, Claude 3, jne.) samalla kysymyksellä: "Mikä on tämän ongelman syy ja miten korjaan sen?"
   - Dokumentoi vastaus.
   - Kysy opiskelijoilta: "Kuinka hyödyllinen tämä vastaus on? Antaako se tarkkaa ratkaisua?"

3. **Toinen testi: Teksti + kuvakaappaus (5 min):**
   - Näytä sama teksti-kuvaus PLUS kuvakaappaus.
   - Lähetä molempaa tekoälylle (sama kysymys).
   - Dokumentoi vastaus.
   - Kysy: "Entä tämä vastaus? Onko se parempi? Miksi?"

4. **Vertailu (5 min):**
   - Piirä tauluun:
     ```
     | Vastaus | Spesifisyys | Käytännöllisyys | Visuaalisen tiedon käyttö |
     |---------|-------------|-----------------|---------|
     | Vain teksti | | | |
     | Teksti + kuva | | | |
     ```
   - Analyysi: "Näet, kuinka multimodaalisuus muuttaa vastauksen. Tekoäly näki kuvan ja ymmärsi ongelman paremmin."

5. **Johtopäätös (3 min):**
   - Kerro: "Tämä on IT-ammattilaiselle tärkeä taito. Tiedät, milloin käyttää tekstiä, milloin kuvakaappauksia, milloin molempia."

### Odotettu oppimistulos
- Opiskelijat näkevät konkreettisesti, kuinka multimodaalisuus parantaa vastauksia.
- He ymmärtävät, että kuvakaappaukset eivät ole vain "kauniita" — ne ovat funktionaalinen konteksti-työkalu.

---

## Tehtävä 6.2: Multimodaalisen kontekstin suunnittelu — Ohjattu harjoitus

### Tavoite
Opettaa opiskelijoille, kuinka rakentaa tehokas multimodaalinen konteksti — milloin käyttää tekstiä, milloin kuvakaappauksia, milloin lokkeja tai koodia.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu:**
- Valitse IT-projekti, jota opiskelijat tunnistavat (esim. verkkopalvelun debugging, tietokanta-ongelma, jne.).

**Oppitunnilla (25 min):**

1. **Asetusmuutos (2 min):**
   - Kerro: "Nyt suunnittelemme multimodaalisen kontekstin. Se ei ole vain yksi kuvakaappaus — se on strateginen yhdistelmä eri muodoista."

2. **Vaihe 1: Mitä materiaalia sinulla on? (5 min):**
   - Piirä tauluun:
     ```
     Materiaali | Esimerkki | Hyödyt | Haitat
     -----------|----------|--------|-------
     Teksti | Kuvaus... | Nopea, selkeä | Voi olla epäselvä
     Kuvakaappaus | Virheviesti | Näyttää tarkalleen | Iso token-kustannus
     Lokit | Error lines | Yksityiskohtainen | Voi olla sekainen
     Koodi | Funktio... | Rakentuu näkyy | Pitkä
     ```
   - Kysy: "Mitä näistä sinulla on käytettävissä?"

3. **Vaihe 2: Miten valitset? (8 min):**
   - Käy läpi jokaisen valinnan looginen:
     - **Teksti:** Jos ongelma on helppo kuvailla ja konteksti-ikkuna on pieni.
     - **Kuvakaappaus:** Jos visuaalinen tieto on kriittiinen — väri, asettelu, kuvakkeet.
     - **Lokit:** Jos virhe näkyy yksityiskohtaisesti logissa — monitoroidaan ja tallenloge.
     - **Koodi:** Jos ongelma on koodissa — näytä relevantti osa.
   - Esimerkki: "Tässä on verkkopalvelun ongelma. Mitä tarvitaan?"
     - Teksti: "Sivulla näkyy error 500. Lisätty sähköpostia."
     - Kuvakaappaus: Näyttää virheen sivulla näyttävissä väreissä.
     - Lokit: Palvelimen virheilmoitus.
     - Koodi: Kontrollerin funktio, joka heittää virheen.

4. **Vaihe 3: Yhdistäminen (7 min):**
   - Kirjoita tauluun lopullinen "multimodaalinen konteksti":
     ```
     1. Teksti: "Käyttäjä raportoi error 500 -sivun näkyvän, kun lähettävät lomakkeen X."
     2. Kuvakaappaus: [näyttö näyttää red error-viestin]
     3. Lokit: [viimeiset 5 virhettä palvelimen logista]
     4. Koodi: [kontrollerin funktio, joka aiheutti virheen]
     ```
   - Selitä: "Tämä on tehokas. Tekoäly näkee ongelman monella tavalla. Se voi antaa paremman ratkaisun."

5. **Strategia ja rajoitukset (3 min):**
   - Korostaa: "Mutta huomio: kuvakaappaukset ovat suuria. Jokainen kuva = 10 000 tokenia. Joten käytä 1-2, ei 10."
   - "Jos konteksti-ikkuna täyttyy, poista kuvakaappaus — pidä teksti ja lokit."

### Odotettu oppimistulos
- Opiskelijat näkevät, että multimodaalinen konteksti on strategista valintaa, ei kaiken heittämistä kerralla.
- He ymmärtävät token-kustannukset ja tekevät älykkäitä valintoja.
