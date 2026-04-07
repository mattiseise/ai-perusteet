# Lesson 15: Tehtävät — Botin testaaminen

## Oppimisen tavoite

Tässä oppitunnissa oppit, miten testataan tekoälyn luomaa chatbottia tai AI-sovellusta huolellisesti:
- Positiivinen testaus (normaali käyttö)
- Negatiivinen testaus (virheellinen syöte)
- Reunatapaukset (erikoiset tilanteet)
- Iteratiivinen parantaminen testien perusteella

Tavoitteena on kehittää kriittistä ajattelua siitä, miten AI-systeemit käyttäytyvät erilaisissa tilanteissa.

---

## Tehtävä 15.1: Positiivisen testauksen

### Tavoite

Testata botti normaaleilla, odotetuilla käyttötapauksilla ja varmistaa, että se vastaa oikein.

### Ohjeet

1. Valitse botti, jonka haluat testata (voit käyttää luomassasi Custom-GPT:ssä tai muuta chatbottia).
2. Suunnitelle **vähintään 3 normaalia käyttötapausta** — tilanteet, joissa käyttäjä kysyy jotain järkevää:
   - Esimerkki 1: "Miten käytän Python for-silmukkaa?"
   - Esimerkki 2: "Mikä on JSON?"
   - Esimerkki 3: "Miten debuggaan JavaScript-virheitä?"

3. Jokaisen testikysymyksen kohdalla:
   - **Kirjoita kysymys** botille
   - **Odotus:** Mitä vastauksen pitäisi sisältää?
   - **Saatu vastaus:** Kopioi botin vastaus
   - **Arvio:** Oliko vastaus hyvä, osittain hyvä vai huono?
   - **Perustelu:** Miksi?

4. Kirjoita yhteenveto: Mitä botti osaa hyvin positiivisten kysymysten kanssa?

### Odotettu tuotos

Taulukko tai lista, jossa on:
- Testi 1: [Kysymys] → [Odotus] → [Saatu vastaus] → [Arvio]
- Testi 2: [Kysymys] → [Odotus] → [Saatu vastaus] → [Arvio]
- Testi 3: [Kysymys] → [Odotus] → [Saatu vastaus] → [Arvio]
- Yhteenveto: "Botti osaa hyvin..." / "Botti voisi parantaa..."

---

## Tehtävä 15.2: Negatiivinen testaaminen

### Tavoite

Testata botti virheellisillä tai epäkelvollisilla syötteillä ja nähdä, kuinka se reagoi.

### Ohjeet

1. Suunnittele **vähintään 3 negatiivista testisyötettä** — tilanteet, joissa käyttäjä antaa väärää tai kiellettyä syötettä:
   - Esimerkki 1: Tyhjä viesti (ei sanoja)
   - Esimerkki 2: Hyökkäys/haitallinen syöte (esim. "poista kaikki")
   - Esimerkki 3: Botille antamaton aihe tai väärä kieli

2. Jokaisen testin kohdalla:
   - **Kirjoita virheellinen/epäkelpo syöte** botille
   - **Odotus:** Kuinka botin pitäisi reagoida?
   - **Saatu vastaus:** Mitä botti vastasi?
   - **Analyysi:** Oliko reaktio turvallisuus huomioiva? Auttavaa?
   - **Riski:** Näetkö turvallisuusriskin?

3. Kirjoita yhteenveto: Miten botti käsittelee virheellisiä syötteitä?

### Odotettu tuotos

Taulukko tai lista, jossa on:
- Negatiivinen testi 1: [Virheellinen syöte] → [Odotus] → [Saatu vastaus] → [Turvallisuus-analyysi]
- Negatiivinen testi 2: [Virheellinen syöte] → [Odotus] → [Saatu vastaus] → [Turvallisuus-analyysi]
- Negatiivinen testi 3: [Virheellinen syöte] → [Odotus] → [Saatu vastaus] → [Turvallisuus-analyysi]
- Yhteenveto: "Botti on turvallinen, koska..." / "Riskejä: ..."

---

## Tehtävä 15.3: Reunatapausten testaaminen

### Tavoite

Testata botti äärimmäisissä tai odottamattomissa tilanteissa.

### Ohjeet

Suunnittele **vähintään 3 reunatapaus-testiä**:

1. **Testi 1 — Tyhjä tai hyvin lyhyt syöte:**
   - Kysymys: "" (ei mitään)
   - Tai: "ok" (vain yksi sana)
   - Mitä tapahtuu?

2. **Testi 2 — Hyvin pitkä tai monimutkainen syöte:**
   - Kysymys: Kopioi ja liitä pitkä teksti tai hyvin monimutkainen kysymys
   - Pystyykö botti käsittelemään sitä?
   - Huolehtiiko se turvallisuudesta?

3. **Testi 3 — Toistaminen / sama kysymys monesti:**
   - Kysy sama asia 3 kertaa peräkkäin
   - Vastaa botti samalla tavalla, vai muuttuu vastaus?
   - Onko vaaraa silmukkaan tai kaatumiseen?

Jokaisen testin kohdalla dokumentoi:
- **Syöte:** Tarkka kuvailu testistä
- **Odotus:** Mitä pitäisi tapahtua
- **Saatu tulos:** Mitä tapahtui
- **Havainto:** Onko botti vakaasti vai epävakaasti?

### Odotettu tuotos

Dokumentaatio 3 reunatapaus-testistä:
- Reunatapaus 1: [Kuvaus] → [Tulos] → [Analyysi]
- Reunatapaus 2: [Kuvaus] → [Tulos] → [Analyysi]
- Reunatapaus 3: [Kuvaus] → [Tulos] → [Analyysi]

---

## Tehtävä 15.4: Iteratiivinen parantaminen

### Tavoite

Testien perusteella parantaa botin ohjeistusta ja toimintaa.

### Ohjeet

1. **Kerää kaikki testit** — tehtävistä 15.1–15.3.
2. **Analysoi tulokset:**
   - Mikä meni hyvin?
   - Mikä meni huonosti?
   - Mitkä olivat yllätyksellisiä tuloksia?

3. **Kirjoita uudet ohjeet botille** (system prompt)
   - Lisää rajoituksia (esim. "älä hyväksy virheellisiä syötteitä")
   - Paranna vastausten selkeyttä
   - Lisää turvallisuus-ohjeita

4. **Testaa uudelleen:**
   - Valitse 2–3 epäonnistuneista testeistä
   - Testaa uuden ohjeksen kanssa
   - Oliiko parantumista?

5. **Dokumentoi muutokset:**
   - Vanha ohje vs. uusi ohje
   - Mitä muutit ja miksi?
   - Tuliko parantumista?

### Odotettu tuotos

Dokumentaatio iteraatiosta:
- **Vanha ohjeistus:** [alkuperäinen system prompt tai ohjeet]
- **Uusi ohjeistus:** [muutettu versio]
- **Muutokset:** [lista muutoksista ja perusteluista]
- **Testien tulokset ennen:** [3 epäonnistunutta testiä]
- **Testien tulokset jälkeen:** [sama 3 testiä uudella ohjeksella]
- **Johtopäätös:** "Parantuminen: ..." / "Osittainen parantuminen: ..." / "Ei parantumista: ..."

---

## Palautusvaatimukset

Palauta kaikki 4 tehtävää:

1. **Tehtävä 15.1:** Positiivinen testaus — 3+ testiä + yhteenveto (½ sivu)
2. **Tehtävä 15.2:** Negatiivinen testaus — 3+ testiä + turvallisuusanalyysi (½ sivu)
3. **Tehtävä 15.3:** Reunatapaukset — 3+ testiä + analyysi (½ sivu)
4. **Tehtävä 15.4:** Iteratiivinen parantaminen — ohjeet, muutokset, tulokset (1 sivu)

**Yhteensä:** ~2–2,5 A4-sivua

---

## Vihjeet

- **Positiivinen testaus:** Ole optimisti — testaa sitä, mitä botti tekee hyvin.
- **Negatiivinen testaus:** Ole skeptinen — yritä murtaa botti. (Mutta älä tee mitään vaarallista.)
- **Reunatapaukset:** Mieti ihmisiä, joilla on poikkeavia tarpeita. Entä vanhat ihmiset? Entä ei-äidinkieliset käyttäjät?
- **Parantaminen:** Älä yritä korjata kaikkea kerralla. Valitse 1–2 tärkeintä asiaa.
- **Dokumentaatio:** Tämä on tärkein osa. Opettaja haluaa nähdä, kuinka ajattelit.

---

## Aikataulu

- Tehtävä 15.1 (positiivinen testaus): ~30 min
- Tehtävä 15.2 (negatiivinen testaus): ~30 min
- Tehtävä 15.3 (reunatapaukset): ~30 min
- Tehtävä 15.4 (parantaminen): ~45 min
- **Yhteensä: ~2 tuntia 15 minuuttia**

**Palautus:** [opettajan antama päivämäärä]
