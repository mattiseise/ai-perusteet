# Opettajavetoiset harjoitukset: Etiikka, tekijänoikeudet ja ympäristövaikutukset

## Harjoitus 1: Oikeustapaus-keskustelu — tekijänoikeudet

### Tavoite
Opettaa opiskelijoille, että tekoälyn tekijänoikeus- ja eettinen kysymykset ovat todellisia, kiistanalaisia ja ammatillisesti relevantteja.

### Ohjeet ja vaiheet

**Kesto: 25 minuuttia**

1. **Johdanto (5 min):**
   Esitä lyhyt yhteenveto:
   - Kirjailijoiden yhdistys vs. OpenAI (2023)
   - Kuvataiteilijat vs. Stability AI (2023)
   - Journalistien vs. Google (käyttävät Google News artikkeleja ilman korvausta)

   Kysy: "Kuka on oikeassa?"

2. **Pienryhmä-analyysi (10 min):**
   Jaa opiskelijat 3 ryhmään (yksi per tapaus).
   Jokainen ryhmä saa:
   - Kantajan (kirjailijat/taiteilijat) näkökulma
   - Vastaajan (AI-yritys) näkökulma
   - Tehtävän: "Rakentakaa paras argumentti kummallekin puolelle"

   **Kantaja:n argumentti (esim. kirjailijat):**
   ```
   "Miljoonat kirjat on ladattu ilman lupaa. Meidät
   ei kysytty, meitä ei korvata. ChatGPT tuottaa
   tekstejä, joilla on liian paljon samankaltaisuutta
   meidän omaamme kanssa. Tämä on tekijänoikeusrikkomus."
   ```

   **Vastaajan argumentti (esim. OpenAI):**
   ```
   "Koulutus on transformatiivista — emme vain
   jäljennä tekstejä. Olemme rakentaneet mallin,
   jonka tuotokset ovat uusia. Tekijänoikeuslaissa
   on 'reilu käyttö', joka sallii tämän."
   ```

3. **Esitys (10 min):**
   - Jokainen ryhmä esittää argumenttinsa 2–3 minuuttia.
   - Opettaja esittää jokaiselle ryhmälle "vastaväitteen":
     * Kantajille: "Entä jos emme poista kirjoja datasta — onko se silti ok?"
     * Vastaajille: "Entä jos tekijöille maksetaan oikeudenmukainen osuus?"

4. **Johtopäätös (5 min):**
   - Opettaja korostaa: **"Tämä ei ole yksinkertainen asia."**
   - Tuomioistuimet ovat edelleen jakautuneet.
   - Ammattilaisesti: sinun pitää olla tietoinen tekijänoikeuskysymyksistä valitessaan ja käyttäessään tekoälypalveluja.

---

## Harjoitus 2: Harha-testiminat — simulaatio

### Tavoite
Näyttää, kuinka algoritminen harha syntyy ja miten sitä voi havaita.

### Ohjeet ja vaiheet

**Kesto: 20 minuuttia**

1. **Skenariointi (5 min):**
   Esitä skenarioita:

   **Skenaario A: Rekrytointialgoritmi**
   ```
   Organisaatiosi kehitti algoritmin, joka valitsee
   paarhaat IT-hakijat automaattisesti. Algoritmi on
   opetettu 5 vuoden palkkaamisdatalla.

   Tulokset: Algoritmi hyväksyi 90% miehiksi
   hakijoista ja 30% naisiksi hakijoista,
   vaikka kelpoisuus oli sama.
   ```

   **Skenaario B: Luottotarina-algoritmi**
   ```
   Pankkisi käyttää algoritmia lainanhyväksynnän
   tekemiseen. Se analysoisi kredittihistoriaa,
   tuloja, kodin arvoa.

   Tarkastus osoittaa: Algoritmi epäonnistuu
   korkeammalla kurssilla lainojen kieltämisestä
   tietyillä postinumeroilla (joissa asuu
   pääasiassa tiettyä etnistä ryhmää).
   ```

2. **Ryhmän tehtävä (8 min):**
   Jaa opiskelijat kahtia (puolet Skenaario A:lla, puolet B:llä).

   Jokainen ryhmä analysoi:
   - Missä harha näkyy?
   - Mistä harha johtuu? (Koulutus datasta? Parametreista?)
   - Kuka on vastuussa?
   - Miten tämä voitaisiin havaita testaamalla?

   **Testisuunnitelma (täytä):**
   ```
   1. Testaa algoritmi demografiselle joukolle
   2. Vertaa hyväksynnän prosentteja ryhmittäin
   3. Tutki, ovatko alhaisemmat prosentit "liian pienet" (harha)
   4. Analysoi: mikä koulutus datassa aiheutti tämän?
   5. Dokumentoi ja ilmoita johtajille
   ```

3. **Esitys (7 min):**
   - Molemmat ryhmät esittävät testisuunnitelmaansa.
   - Opettaja korostaa: **"Harha on usein piilossa — se vaatii aktiivista testaamista."**

---

## Harjoitus 3: Eettinen keskustelu — globaali työ ja vastuu

### Tavoite
Opettaa opiskelijoille, että tekoälyn "näkymätön" työ (datan merkitseminen) on ammatillinen ja eettinen kysymys.

### Ohjeet ja vaiheet

**Kesto: 20 minuuttia**

1. **Johdanto (5 min):**
   Näytä video tai kirjoita tarinaa:
   - Datan merkitsijät Bangladeshissa
   - He merkitsevät kuvia ChatGPT:n opetusta varten
   - He saavat $2–5 per tunti
   - Joskus kuva sisältävät väkivaltaa tai seksuaalisuutta — psyykkinen kuormitus

   **Kysymys opiskelijoille:** "Ajatelitko, että näiden ihmisten työ mahdollistaa ChatGPT:n?"

2. **Eettinen ympyrä (10 min):**
   Jaa opiskelijat 4 ryhmään. Jokainen ryhmä edustaa näkökulmaa:

   **Ryhmä 1 — Merkitsijän näkökulma:**
   - Mitä haluaisit?
   - Miten olet hyödytetty? Käytätty?

   **Ryhmä 2 — AI-yrityksen (esim. OpenAI) näkökulma:**
   - Miksi palkat ovat alhaiset?
   - Mitä velvoitteita sinulla on?

   **Ryhmä 3 — Organisaation näkökulma (käyttäjä, kuten sinun opiskelija):**
   - Mitä sinun vastuulla on käyttäjänä?
   - Tiedätkö merkitsijien oloista?

   **Ryhmä 4 — Hallituksen näkökulma:**
   - Pitäisikö lainsäädäntöä antaa merkitsijöiden suojaamiseksi?

3. **Ympyrän kanssa (5 min):**
   - Jokainen ryhmä esittää 1–2 minuutin kannan.
   - Opettaja koostaa: "Näette, että vastuut ovat hajallaan — mutta ammattilaisena SINULLA on ääni."

**Opettajan muistio:**
- Älä anna ryhmille ratkaisua ("Ja sitten kaikki maksoivat reilua palkkaa!").
- Tavoitteena on, että opiskelijat näkevät kompleksisuuden ja ymmärtävät, että ammattilaisena he voivat tehdä valintoja.

---

## Harjoitus 4: Ympäristöjalanjälki ja "harkittu käyttö"

### Tavoite
Konkreettistaa ympäristövaikutukset ja opettaa ammattilaisesti harkittua tekoälyn käyttöä.

### Ohjeet ja vaiheet

**Kesto: 15 minuuttia**

1. **Laskenta (5 min):**
   Opettaja näyttää taululla:

   ```
   1 ChatGPT-query = ~0,29 Wh sähköä
   200 miljoonaa kyselyä/kuukausi = ~58 miljoonaa kWh/vuosi
   = kuin 5,600 amerikkalaista kotia sähkönkulutus

   Data-keskuksen jäähdytys = 37 miljoonaa gallonaa vettä/vuosi
   = kuinka paljon vettä saisi 2,800 amerikkalaista perhettä
   ```

2. **Ryhmä harjoitus (5 min):**
   Ryhmät arvioivat: "Pitäisikö tekoälyä käyttää seuraaviin tehtäviin?"

   | Tehtävä | Arvo vs. Kost | Päätös |
   |---|---|---|
   | Asiakkaalle lähetetty henkilökohtainen viesti | Matala? Korkealle? | |
   | API-dokumentaation koodiesimerkki | | |
   | Jokainen asiakastuki-query | | |
   | Sähköpostit, joita ei ole vielä lähetetty | | |
   | Tieteellinen tutkimus kirjoittaminen | | |

   **Jokaisen kohdalla: "Voitaisiko tehdä muulla tavalla, joka kuluttaa vähemmän energiaa?"**

3. **Johtopäätös (5 min):**
   - Opettaja: "Harkittu käyttö ei tarkoita 'älä käytä tekoälyä'. Se tarkoittaa: käytä sitä silloin, kun arvo ylittää kustannukset."
   - Ammattilaisesti: tiedä vaikutukset, mieti vaihtoehto, dokumentoi valinta.

---

## Opettajan tärkeitä kohtia

**Avainviesti 1: Tekoäly ei ole neutraali.**
- Se on rakennettu tekijöillä, jotka eivät ole suostuneet.
- Se on harhainen historiallisen datan kautta.
- Se on energiaintensiiviä.
- Ammattilaisesti: tämä on AINA mielessä.

**Avainviesti 2: Vastuu on hajaantuneet, mutta sinulla on se.**
- OpenAI vastaa... no, jotenkin.
- Merkitsijät — he kärsivät.
- Sinä, joka käytät tekoälyä — sinulla on valinta.
- Ammattilaisesti: et voi vain sysätä vastuuta pois.

**Avainviesti 3: Ammattilaisuus tarkoittaa syvempää pohdintaa.**
- "Kaikki käyttävät sitä" ei ole riittävä perustelu.
- "Se on laillista" ei ole sama kuin "se on eettistä".
- Ammattilaiset ovat ne, jotka kyseenalaistavat ja tekevät tietoisia valintoja.

---

## Sisäänrakennetut keskustelun herättäjät

**Jos opiskelijat sanovat:** "Ei ole mitään, mitä voin tehdä — tekoäly on liian suuri järjestelmä."

**Vastaa:** "Totta, mutta sinulla on valinta siitä, käytätkö sitä vai et, miten käytät sitä, mitä palvelua valitset. Nämä kumuloituvat. Ja jos organisaatiosi käyttää tekoälyä, sinulla on ääni."

**Jos opiskelijat sanovat:** "Eikö tekijöille maksetaan jo?"

**Vastaa:** "Joissain tapauksissa — esim. kontrolloidut data-koulutus projekti, joissa tekijät saavat korvauksen. Mutta perinteisesti, ei. Tämä muuttuu hitaasti."

**Jos opiskelijat sanovat:** "Entä jos yritys sanoo 'käytä tekoälyä, se säästää kustannuksia'?"

**Vastaa:** "Sitten sinulla on ammatillinen ja eettinen vastuualue. Voit nostaa huolenaiheita. Et ole ollut pakko tehdä asiaa, joka on vastuutonta."

