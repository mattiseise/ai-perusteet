# Lesson 22: Opettajavetoiset tehtävät

## Tehtävä 1: Live-testaus — Ryhmissä botinketjun testaaminen

**Aika:** 25 min
**Materiaali:** Opettajan valitsema botti (FAQ, asiakaspalvelu, IT-tuki)

**Kulku:**
1. **Johdanto (3 min):** "Nyt testaamme oikeaa bottia. Jakaudutaan kolmeen ryhmään: positiiviset testit, negatiiviset testit, reunatapaukset."
2. **Ryhmätyö (15 min):**
   - **Ryhmä A (Positiiviset):** Testaa 3-4 normaalia kysymystä. Dokumentoi vastaukset.
   - **Ryhmä B (Negatiiviset):** Testaa asioita, joissa botissa pitäisi sanoa "en osaa". Dokumentoi kieltäytymisen.
   - **Ryhmä C (Reunatapaukset):** Testaa outoja tilanteita (tyhjät, sekavat, liian pitkät kysymykset). Dokumentoi, kaadutaanko vai ei.
3. **Esitykset (5 min):** Jokainen ryhmä esittelee yhden tuloksen. Mitä löydettiin?
4. **Analyysi (2 min):** "Mikä testi paljasti buggin? Miten korjaisimme?"

**Facilitoinnin vinkkejä:**
- Anna jokaiselle ryhmälle print-out testausmallista
- Kerro, että "ei onnistumiset" ovat yhtä arvokkaita kuin onnistumiset
- Selvitä: "Miksi tämä testi epäonnistui?"

**Solo-vaihtoehto:** Testaa opettajan antamaa bottia yksin kaikkien kolmen tyypin perusteella (positiiviset, negatiiviset, reunatapaukset). Dokumentoi tulokset.

---

## Tehtävä 2: Iteraatio-simulaatio — Botti 1.0 → 2.0

**Aika:** 20 min
**Skenario:** "Ensimmäisen testin jälkeen botti epäonnistuu kolmessa asiassa. Yhdessä korjaamme yhden ongelman."

**Kulku:**
1. **Näytä vika (2 min):** Opettaja näyttää botti-simulaation, jossa testi epäonnistuu. Esim. "Botti ei osaa vastata turvallisuusongelmaan."
2. **Ryhmä analysoi (5 min):** "Miksi botti epäonnistuu? Onko tietopohja vai ohjeistus ongelma?"
3. **Ryhmä ehdottaa korjausta (5 min):** "Miten korjaisimme? Mitä kirjoittaisimme ohjeistukseen?"
4. **Testaus uudelleen (5 min):** Näytä, miten korjattu botti vastaa paremmin. "Katso: iteraatio toimi!"
5. **Pohdi:** "Mitä muita ongelmia olisi korjattava seuraavalla kierroksella?"

**Mahdollisia virheitä näytettäviksi:**
- Botti antaa virheellistä tietoa
- Botti ei ymmärrä tavallista kysymystä
- Botti ei osaa kieltäytyä asiassa, joissa pitäisi

**Solo-vaihtoehto:** Ota edelliseltä oppitunnilta oma botti. Testaa se (3 kysymystä), löydä yksi vika, korjaa ohjeistusta, testaa uudelleen. Dokumentoi prosessi.
