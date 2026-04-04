# Lesson 26: Opettajavetoiset tehtävät

## Tehtävä 1: Projektin kickoff — Ideointi yhdessä

**Aika:** 30 min
**Skenario:** "Haluamme varmistaa, että jokainen opiskelija valitsee realistisen projektin."

**Kulku:**
1. **Esimerkkiprojektit (5 min):** Näytä 3-4 esimerkkiprojektia (eri tasoilla).
   - Taso 1: "FAQ-botti omasta aiheesta"
   - Taso 2: "Slack-integratio, joka hakee tietoja Google Sheetsin"
   - Taso 3: "RAG-agentti dokumentaatiolle"

2. **Ryhmäkeskustelu (10 min):** Opiskelija-parit ideoidaan.
   - "Mikä on ongelmanne, jonka agentti/botti voisi ratkaista?"
   - "Kuka käyttäjä siitä hyötyisi?"
   - "Mitä se tekisi?"

3. **Opettaja-feedback (10 min):** Jokainen pari esittelee ideansa. Opettaja:
   - Vahvistaa, että idea on realistinen (5-10 tuntia)
   - Ehdottaa yksinkertaistamisia, jos liian suurta
   - Ohjeistaa tekniikan valinnasta

4. **Dokumentointi (5 min):** Opiskelijat täyttävät projektisuunnitelmalomakkeen (Milestone 1).

**Facilitoinnin vinkkejä:**
- "Tämä on realistinen aikaväli? 1-2 viikkoa?"
- "Mitä voit tehdä MVP:n rajoissa?"
- "Mitkä ovat suurimmat riskit?"

---

## Tehtävä 2: Testaus ja dokumentointikatselmus

**Aika:** 30 min (tapahtuu projektityöskentelyn puolivälissä)
**Skenario:** "Opiskelijat ovat rakentaneet prototyypin ja testanneet sitä. Nyt katsomme yhdessä, onko dokumentaatio riittävä."

**Kulku:**
1. **Testitulosten katselmus (10 min):**
   - Opiskelijat näyttävät testauslomakkeen
   - Opettaja tarkistaa: Onko vähintään 4 testiä? Onko edge case -testit?
   - "Miten agentti reagoi hyökkäyspromptiin?"

2. **Dokumentaatiokatselmus (10 min):**
   - Opiskelijat näyttävät README:n ja ARCHITECTURE.md:n
   - Opettaja tarkistaa: Voisiko toinen oppilas käyttää tätä ilman apua?
   - "Onko arkkitehtuuri selkeä?"

3. **Turvallisuus-feedback (10 min):**
   - Opiskelijat näyttävät SAFETY.md:n
   - Opettaja kysyy: "Mitä riskit? Onko mitigoinut ne?"
   - Opettaja antaa ideoita puuttuvista turvallisuusasioista

**Facilitoinnin vinkkejä:**
- "Testit ovat turvallisuuden ensimmäinen linja."
- "Dokumentaatio pitäisi olla niin selvä, että joku muu voi käyttää sitä."
- "Riskit eivät ole heikkous — tunnistaminen on vahvuus."

---

## Tehtävä 3: Demo-harjoitus ja feedback

**Aika:** 45 min (juuri ennen demopäivää)
**Skenario:** "Opiskelijat harjoittelevat demoa ja saavat opettajalta palautetta."

**Kulku:**
1. **Demo-harjoitus (20 min):**
   - Jokainen opiskelija/pari esittelee projektinsa lyhyesti (3-4 minuuttia)
   - Muut oppilaat: Kysymykset ja palaute

2. **Opettaja-feedback (20 min):**
   - Opettaja antaa palautetta jokaiselle:
     * "Mitä oli hyvää? Näytin hyvin X:ää."
     * "Mitä parantaisit? Voisi selittää paremmin Y:tä."
     * "Yksityiskohtakysymykset: 'Mitä tekisit toisin?'"

3. **Tekniikan harjoitus (5 min):**
   - Varmista, että demo toimii: Agentti käynnistyy, live-demo toimii, no typos

**Facilitoinnin vinkkejä:**
- "Demo on narratiivi, ei koodiesitys."
- "Näytä, että agentti toimii, ei koodia."
- "Kysy: 'Mitä oprit, mitä tekisit toisin?'" — tämä näyttää kriittisen ajattelun

---

## Tehtävä 4: Demopäivä (summatiivinen arviointi)

**Aika:** 1,5-2 tuntia
**Skenario:** "Jokainen opiskelija esittelee projektinsa."

**Rakenne:**
- Jokainen opiskelija/pari: 10-15 minuuttia (5 min demo + 5-10 min Q&A)
- Muut oppilaat: Kuunnella, esittää kysymyksiä

**Arviointi (katso arviointikriteerit lesson 27:stä):**
- Toiminnallisuus (30%)
- Dokumentaatio (20%)
- Turvallisuus & riskit (20%)
- Demo laatu (15%)
- Koodi & arkkitehtuuri (15%)

**Opettajan rooli:**
- Kysyy syvällisiä kysymyksiä: "Miksi valitsit tämän lähestymistavan?"
- Kuuntelee turvallisuus-selityksiä: "Mitä riskit?"
- Antaa julkista palautetta (positiivista + rakentavaa)

