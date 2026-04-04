# Lesson 23: Opettajavetoiset tehtävät

## Tehtävä 1: Live-muistin testaus — Chatbotti muistin rajoilla

**Aika:** 25 min
**Materiaali:** Chat-agentti (opettaja valitsee), merkitsevästi pitkä keskustelu-script

**Kulku:**
1. **Johdanto (2 min):** "Testaamme agentin muistia. Näetään, kuinka kauan se muistaa asioita."
2. **Keskustelu (12 min):**
   - Opettaja tai opiskelija käy chattia agentin kanssa
   - 1. viesti: Kerro koko identiteettisi (nimi, ammatti, harrastus)
   - Viestit 2-15: Puhu erilaisista asioista
   - Viesti 16: Kysy: "Mikä on nimeni?" "Mikä oli ammattini?"
   - Näytä vastaukset luokalle
3. **Uusi istunto (5 min):**
   - Sulkea chat, avata uusi istunto
   - Kysy agentilta: "Muistaatko minusta mitään?"
   - Dokumentoi: muistaako vai ei?
4. **Analyysi (6 min):** "Mikä ero on konteksti-ikkunalla ja pitkäaikaisella muistilla?"

**Facilitoinnin vinkkejä:**
- Näytä, milloin agentti "unohtaa" vanhat asiat
- Kysy: "Mitä se unohtaa ensin?"
- Pohdi: "Mitä tapahtuisi, jos tätä olisi asiakaspalvelubotti?"

**Solo-vaihtoehto:** Testaa opettajan antamaa bottia 15-20 viestin sarjalla ja dokumentoi, mitä muistaa.

---

## Tehtävä 2: Tilakoneen suunnittelu — Ryhmätyö prosessin kanssa

**Aika:** 20 min
**Skenario:** Asiakastuki-tiketti. Tila vaihtuu vaiheesta toiseen.

**Kulku:**
1. **Jaetaan ryhmiin (1 min):** Jokainen ryhmä saa tiketin eri vaiheesta
2. **Analyysi (8 min):** "Mitä tietoja meidän täytyy muistaa tässä vaiheessa?"
   - Ryhmä 1: UUSI-vaihe
   - Ryhmä 2: RATKAISUSSA-vaihe
   - Ryhmä 3: RATKAISTU-vaihe
3. **Esitys (8 min):** Jokainen ryhmä näyttää:
   - Missä vaiheessa we ollaan?
   - Mitä tietoja tarvitaan?
   - Mihin vaiheeseen siirrytään seuraavaksi?
4. **Koostetaan tilakaavio (3 min):** "Yhdessä piirrämme koko tilakoneen"

**Facilitoinnin vinkkejä:**
- Piirtää jokainen tila ympyränä taululle
- Kysy jokaisesta: "Mitä data meidän täytyy tallentaa?"
- Osoita: "Kun tila vaihtuu, agentti tekee eri asioita"

**Solo-vaihtoehto:** Piirrä tilakone yksinkertaiselle prosessille (esim. pizzan tilaus) ja merkitse kaikki tilat ja siirtymät.
   - Mitä teet ensimmäiseksi?
   - Ketkä osallistuvat?
   - Mitä tietoa tarvitset?
   - Miten palaudut?
3. **Esitykset ja pohdinnat (8 min):** "Miten olisit voinut valmistautua tähän etukäteen?"
4. **Yhteenveto (2 min):** "Tämä on riskienhallintaa — ennakoiminen ja palautuminen."

**Facilitoinnin vinkkejä:**
- Lisää paineita: "CEO on liukastaa, mitä sanot?"
- Johdatele: "Mitä lokit kertoivat?"
- Kysy: "Miten testaisit korjauksen ennen käynnistämistä uudelleen?"

**Solo-vaihtoehto:** Kirjoita kriisinhallintosuunnitelma: "Jos agentti kaatuu, mitä tehdään ensimmäiset 15 minuuttia?"

---

## Tehtävä 2: Red Team — Agenttihyökkäys

**Aika:** 15 min
**Tehtävä:** "Olette hyökkääjät. Kuinka voisitte hyödyntää tätä agenttikirjaa vahingon aiheuttamiseksi?"

**Kulku:**
1. **Asetus (2 min):** Opettaja kertoo agenttijärjestelmän (esim. verkkokaupan tilausjärjestelmä)
2. **Red Team -työ (8 min):** Opiskelijat keksivät hyökkäystapoja:
   - Mitä voisit antaa syötteeksi, joka lamauttaa agentin?
   - Mitä integraatiota voisit ohittaa?
   - Miten voisit tehdä agenttia tekemään vahingollisia asioita?
3. **Esitykset (3 min):** Kukin ryhmä esittelee yhden hyökkäyksen
4. **Puolustus (2 min):** "Miten vertaisit näitä hyökkäyksiä?"

**Mahdollisia hyökkäyksiä (joita voit ohjata jos opiskelijat juuttuvat):**
- Antaa väärä/pahantahtoisesti muokattu syöte
- Ylikuormittaa agentin samalla triggerillä
- Katkaista integraatio kesken
- Antaa agenttille liian paljon oikeuksia tietokantaan

**Solo-vaihtoehto:** Keksi yksi hyökkäystapa ja kuvaa se: "Jos hyökkääjä tekisi tämän, mitä tapahtuisi?"
