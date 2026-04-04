# Opettajavetoiset tehtävät – Lesson 21

## Tehtävä 1: Botin suunnittelu-työpaja (30 min)

Opiskelijat suunnittelevat oman botin paperille. Heidän pitää määritellä:
1. **Tarkoitus** (Purpose)
2. **Rooli** (Role)
3. **Ohjeet** (Instructions)
4. **Rajaukset** (Constraints)
5. **Esimerkki-interaktio** (Example conversation)
**Materiaali:** Valokuva tai kaavio todellisen agenttijärjestelmän arkkitehtuurista (esim. verkkokaupan järjestelmä)

**Kulku:**
1. **Näytä arkkitehtuuri (5 min):** "Tämä on todellinen agentti, joka käsittelee tilauksia. Mitä näette?"
2. **Opiskelijat tunnistavat (10 min):**
   - Mistä syötteet tulevat?
   - Mitä askeleita agentti ottaa?
   - Mitkä ovat tulokset?
   - Mitä voisi mennä pieleen?
3. **Pohdi yhdessä (10 min):** "Kuka vastaa, jos agentti poistaa väärän tilauksesta? Miksi arkkitehtuuri on tärkeä?"

**Facilitoinnin vinkkejä:**
- Pyydä opiskelijoita osoittamaan kaaviossa kohdat, joissa ihminen voisi tehdä vahinkoa
- Jos opiskelijat vaikeutuvat, kysymys: "Jos tämä menee pieleen, mitä rahallista vahinkoa tulisi?"

**Solo-vaihtoehto:** Jos et ole ryhmässä, piirrä oman ideasi mukainen agenttijärjestelmän arkkitehtuuri (esim. asiakastuki) ja merkitse syötteet, askeleet ja tulokset.

---

## Tehtävä 2: Oikean maailman esimerkki — Vianmääritys

**Aika:** 20 min
**Skenario:** "Agentti oli määrä lähettää 50 vahvistussähköpostia asiakkaille, mutta lähetti vain 25. Mitä meni pieleen?"

**Kulku:**
1. **Kerro skenario (2 min)**
2. **Ryhmätyö (10 min):** "Mitä askeleita meni pieleen? Mistä tiedät? Miten tutkisit?"
3. **Ryhmien esitykset (5 min):** Kukin ryhmä ehdottaa yhden mahdollisuuden
4. **Pohdi:** "Miksi lokitus ja valvonta ovat tärkeitä?"

**Mahdollisia vastauksia joita voi ohjata:**
- API epäonnistui puolessa pyyynnöistä
- Trigger laukeaa vain puolelle asiakkaista
- Integraatio katkaistiin kesken prosessin

**Solo-vaihtoehto:** Kirjoita 3-4 lausetta: "Mikä meni pieleen ja miksi? Miten testaisit tämän prosessin ennen käyttöönottoa?"
