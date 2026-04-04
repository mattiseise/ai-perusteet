# Lesson 25: Opettajan materiaalit

## Oppimisen tavoitteet

Opiskelija osaa:
1. Tunnistaa prompt injection -riskit agentin kontekstissa (erityisesti ulkoisista lähteistä)
2. Soveltaa minimioikeus-periaatetta agentin oikeuksiin
3. Suunnitella lokituksen vianetsintää ja audit trailaa varten
4. Analysoida agentin turvallisuutta neljän kerroksen viitekehyksellä
5. Arvioida kompromisseja turvallisuuden ja tehokkuuden välillä

## Yleisimmät väärinkäsitykset

1. **"Prompt injection on riskitön, jos käyttäjä ei ole pahantahtoinen"** → Kuka tahansa voi olla pahantahtoinen, ja injektio voi tulla monesta lähteestä (sähköpostit, API-vastaukset, tietokanta).

2. **"Jos annan agentille laajat oikeudet, se tekee paremmin tehtävänsä"** → Laajat oikeudet lisäävät vahinkopotentiaalia, eivät tehokkuutta.

3. **"Lokitus on vain byrokratiaa"** → Lokit ovat kriittinen turvallisuus- ja lakisääteinen vaatimus.

4. **"Neljä kerrosta on liikaa — yksi riittää"** → Jokainen kerros puolustaa eri tavalla. Yhden epäonnistuminen ei tarkoita, että agentti on turvaton, jos muut kerrokset toimivat.

5. **"Hyväksyntä on riittävä suojaus"** → Hyväksyntä on yksi kerros, mutta validointi, rajoitus ja seuranta ovat yhtä tärkeitä.

## Tarkistustehtävät / CFU

1. Mitä on prompt injection agentin kontekstissa?
2. Miksi agentin kontekstissa prompt injection on vaarallisempi kuin yksittäisessä chatissa?
3. Antaa esimerkkejä lähteistä, joista injektio voisi tulla.
4. Mitä on minimioikeus-periaate? Miksi se on tärkeä?
5. Antaa esimerkkejä: "Mitä oikeuksia agentti TODELLA tarvitsee?" vs. "Mitä se ei tarvitse?"
6. Mikä on lokituksen tarkoitus?
7. Mitä kuuluu lokiin ja mitä ei?
8. Mikä on neljän kerroksen malli turvallisuudelle?
9. Mitä tapahtuu, jos validointi epäonnistuu?
10. Mitä tapahtuu, jos minimioikeus on liian rajoittava?

## Tyypilliset vaikeudet

1. **Turvallisuus abstraktina** — Opiskelijat voivat ajatella, että turvallisuus on vain teoria.
   **Apua:** "Tämä on toistettavissa todellisessa maailmassa. Jos agentti käsittelee maksukortin numeroita ja menettää ne, se on miljoonien eurojen riski."

2. **Liikaa kerroksista** — Opiskelijat voivat ajatella, että neljä kerrosta on liikaa.
   **Apua:** "Jokaisella kerroksella on erilainen tarkoitus. Validointi, rajoitus, seuranta ja palautuminen puolustavat eri tavalla."

3. **Minimioikeuksien inventointivaikeus** — Opiskelijat voivat vaikeutua määrittelemään, mitä oikeuksia agentti tarvitsee.
   **Apua:** "Aloita siitä, mitä agentti TEKEE. Jokaista tekemistä varten tarvitaan yksi oikeus. Ei muita."

4. **Lokituksen yksityisyyden huoli** — Opiskelijat voivat ajatella, että lokitettavat tiedot ovat yksityisyyden loukkausta.
   **Apua:** "Lokit eivät saisi sisältää salaiseksi merkittyä tietoa. Logeista näkee PERUSTAsyyt, ei tietoja itse."

5. **Hyväksyntä vs. turvallisuus** — Opiskelijat voivat ajatella, että hyväksyntä ratkaisee kaiken.
   **Apua:** "Hyväksyntä on tärkeä, mutta se on YKSI kerros. Jos validointi epäonnistuu, injektio pääsee hyväksyjälle."

## Materiaaleja ja esimerkkejä

**Esimerkkiagentti analyysiin:**
```
Agentti: HR-chatbotti, joka vastaa palkka-kysymyksiin
- Lukee henkilöstön tiedot
- Kyselee, mistä kysymys on
- Ehdottaa vastausta
- Lähettää vastauksen sähköpostilla

Turvallisuusanalyysi:
1. Validointi: Tarkista, että kysymys on laillinen palkka-aiheinen kysymys (ei "löyhennä palkkoja kaikille")
2. Rajoitus: Agentti näkee vain yleisiä palkka-politiikkoja, ei yksittäisiä palkkoja
3. Seuranta: Lokeista näkee, mitä agentti ehdotti ja keille
4. Palautuminen: HR-henkilö voi perua väärän vastauksen ennen kuin se lähetetään
```

**Lokitusesimerkkejä:**
- Hyviä: `[2026-03-14 09:15:22] VALIDATION: Email format valid`
- Huonoja: `[2026-03-14 09:15:22] EMAIL: john.smith@company.com (sisältää yksityisen tiedon)`
- Hyviä: `[2026-03-14 09:15:30] FUNCTION_CALL: get_salary_policy(department_id=5)`
- Huonoja: `[2026-03-14 09:15:30] DATABASE: Retrieved salary for John Smith = 45000`

