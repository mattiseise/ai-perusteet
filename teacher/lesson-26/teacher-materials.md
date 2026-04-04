# Lesson 26: Opettajan materiaalit

## Oppimisen tavoitteet

Opiskelija osaa:
1. Suunnitella AI-agentin/botin käyttötapauksen ja rajoitukset
2. Rakentaa toimivan prototyypin (itsenäisesti tai pienryhmässä)
3. Testata agentin edge case -tapauksissa ja turvallisuustilanteissa
4. Dokumentoida projektin (README, arkkitehtuuri, turvallisuus)
5. Esitellä projektia selkeästi ja vastaanottaa palautetta
6. Arvioida omaa projektia kriittisesti (opitut asiat, parannukset)

## Projektin roolit ja tuen nivelet

**Opiskelijat voivat valita:**
1. **Solo-projekti** — yksi oppilas, 5-8 tuntia
2. **Pariprojekti** — kaksi oppilasta, 8-12 tuntia (enemmän sekä)

**Opettajan tuen nivelet:**
1. **Kickoff** — Ideointi yhdessä, realistisuuden vahvistaminen
2. **Milestone 1 tarkistus** — Projektisuunnitelma hyväksytään ennen rakentamista
3. **Puolivälin tarkistus** — Testit ja dokumentaatio kunnossa?
4. **Demoherra** — Opettaja harjoittelee palautteen antoa
5. **Demo-päivä** — Summatiivinen arviointi

## Milloin projekti on liian suuri tai liian pieni?

**Liian pieni:** "Chatbotti, joka vain kutsuu yhtä API:tä ilman logiikkaa."
→ Ohjeista: "Lisää jokin logiikka: suodatus, validaatio, tai useita lähteitä."

**Liian suuri:** "Täysin uusi startup, frontend, backend, tietokanta, mobiili."
→ Ohjeista: "Valitse yksi komponentti. Keskity MVP:hen."

**Oikea koko:** 
- Yksinkertainen idea, hyvin toteutettu
- 5-10 tuntia projektityötä
- Näyttää jotain oikeaa ja toimivaa

## Yleisimmät väärinkäsitykset

1. **"Projektin täytyy olla täydellinen"** → Se ei tarvitse olla. Prototyypin riittää, jos dokumentointi on selvä.

2. **"Koodi on tärkein osa"** → Dokumentaatio ja demo ovat yhtä tärkeitä. Koodi osoittaa tekniikkaa, demo osoittaa arvoa.

3. **"Turvallisuus on vain lisä"** → Turvallisuus on kriittinen. Jos agentti käsittelee dataa, sillä on riskit.

4. **"Testaus on merkityksetöntä jos se 'toimii enkulla'"** → Testaus näyttää, että olet ajatellut edge caseja ja hyökkäyksiä.

5. **"Voin tehdä projektia vain salin ulkopuolella"** → Kickoff, tarkistukset ja demo-harjoitus ovat tärkeitä.

## Tarkistustehtävät / CFU

**Projektinsuunnittelulle (Milestone 1):**
1. Mikä on käyttötapaus? (Miksi joku tarvitsee tätä?)
2. Kuka käyttäjä siitä hyötyy?
3. Mitä agentti tekee? (Listaa askeleet)
4. Mitä agentti TIDAK tekee?
5. Mitkä ovat pääriskit?

**Testukselle (Milestone 2):**
1. Oletko testannut normaalia tapausta?
2. Oletko testannut edge casea?
3. Oletko testannut hyökkäystä/prompt injectionia?
4. Onko kaikki dokumentoitu?

**Demol (Milestone 3):**
1. Näytetään se toiminnassa ilman virheitä?
2. Selitätkö käyttötapauksen?
3. Selitätkö arkkitehtuuria lyhyesti?
4. Tunnistetko riskit?
5. Oletko reflektoinut (opitut asiat)?

## Arviointikaava (30 pisteen skaalassa)

| Kriteeri | Pisteet | Kuvaus |
|----------|---------|--------|
| **Toiminnallisuus** | 0-9 | Toimii? Edge casea kunnossa? |
| **Dokumentaatio** | 0-6 | README/ARCHITECTURE/SAFETY selvä? |
| **Turvallisuus** | 0-6 | Riskit tunnistettu? Mitigated? |
| **Demo** | 0-5 | Selkeä? Live toimii? Narrative? |
| **Koodi** | 0-4 | Luettavaa? Järkevä rakenne? |

**Kokonaisarvio:**
- 27-30: Erinomainen (5)
- 24-26: Hyvä (4)
- 20-23: Tyydyttävä (3)
- 16-19: Välttävä (2)
- < 16: Hylätty (1)

## Tukimateriaaleja opiskelijoille

**Valmis projektisuunnitelmalomake:**
Järjestä jäljentää, jonka opiskelijat täyttävät ennen rakentamista.

**Valmis testauslomake:**
Järjestä jäljentää testaustehtäville.

**Demo-runkoslaidi:**
Järjestä mallidiaesitys, jota voi käyttää pohjana.

**Tekninen ohjeistus:**
Valmiit Python/n8n -pohjaesimerkit, joita opiskelijat voivat mukailla.

## Tyypilliset vaikeudet

1. **Opiskelija ei osaa aloittaa** — Auta projektisuunnitelmalomakkeella. Kysy: "Mikä ongelma haluat ratkaista?"

2. **Projekti kasvaa liian suureksi** — Apua MVP-fokuksella: "Mitä vähimmäisvision tarvitset?"

3. **Testaus unohtuu** — Muistuta: "Testaus on 20% arvosanasta."

4. **Dokumentaatio on huono** — Lue README ääneen: "Pystyisikö joku muu käyttää tätä?"

5. **Demo-ahdistus** — Demoherra harjoitus ennen virallista demoa auttaa.

6. **Turvallisuus unohdetaan** — Muistuta: "Entä jos agentti saa prompt injectionin?"

