# Opettajavetoiset tehtävät – Lesson 26: n8n-projektipaja, osa 1

## Tehtävä 1: n8n-rajapinnan perustutorial (15 min)

### Valmistelu

Avaa n8n projektori tai näytöllä niin, että kaikki näkevät. Voit käyttää n8n:n ilmaista pilvipalvelua (n8n.cloud) tai paikallista asennusta.

### Opettajan ohjeistus

1. **Näytä triggeri:**
   - Luo uusi työnkulku
   - Lisää Manual Trigger -solmu
   - Selitä: "Tämä on agentin sydän — se sanoo, milloin työnkulku käynnistyy."
   - Klikitse "Execute" ja näytä, mitä tapahtuu.

2. **Näytä HTTP Request -solmu:**
   - Lisää HTTP Request -solmu triggerin jälkeen
   - Aseta GET-pyynnöksi https://api.github.com/zen
   - Klikkaa "Execute" ja näytä vastaus
   - Selitä: "Tämä solmu kutsuu ulkoista palvelua (API:ta). Se lähettää pyynnön ja saa vastauksen takaisin."
   - Näytä, miten data kulkee solmusta toiseen (viiva yhdistää ne)

3. **Näytä IF-solmu (päätös):**
   - Lisää IF-solmu HTTP Requestin jälkeen
   - Aseta ehto: "Jos vastaus sisältää sanan 'code'"
   - Selitä: "IF-solmu tekee päätöksiä. Se voi ohjata datan eri suuntaan riippuen ehdosta."
   - Näytä true/false-haarauma

4. **Näytä tekstinkäsittely:**
   - Lisää Text-solmu jonka jälkeen
   - Näytä, miten voit muuttaa dataa (esim. lisää etuliite vastauksen eteen)
   - Selitä: "Jokainen solmu muuttaa dataa. Data virtaa putkessa solmusta seuraavaan."

### Opiskelijoiden osallistuminen

- Pyydä opiskelijoita ottamaan omat tietokoneensa ja rakentaa perässä.
- Pysähdy säännöllisesti ja anna heille aikaa testata.
- Vastaa kysymyksiin live ja näytä ratkaisut näytöllä.

### Yhteenveto (1 min)

"Näitte nyt kolme keskeistä n8n-käsitettä:
1. **Trigger** — mistä työnkulku alkaa
2. **Solmut** — mitä kukin solmu tekee
3. **Data virtaa** — miten data liikkuu solmusta seuraavaan viivaa pitkin"

---

## Tehtävä 2: Agentin arkkitehtuurin tunnistaminen (15 min)

### Valmistelu

Näytä n8n:ssä yksinkertainen työnkulku, joka sisältää ainakin 4-5 solmua. Esimerkiksi:

```
Webhook → Validointi (IF) → OpenAI → Tarkistus (IF) → Discord
```

Tai käytä projektin mallia Lesson 26:n aineistosta.

### Opettajan ohjeet

Käy ryhmän kanssa läpi, miten n8n-solmut vastaavat agentin kuuteen komponenttiin:

1. **Syötekäsittelijä** → Webhook + Validointi-IF
   - "Jotain tapahtuu ulkomaailmassa (esim. viesti saapuu). Syötekäsittelijä vastaanottaa sen ja tarkistaa, että se on järkevä."
   - Osoita työnkulussa Webhook-solmu ja ensimmäinen IF-ehto.

2. **Päättelijä** → tekoälysolmu
   - "Tässä agentti 'ajattelee'. Se analysoi viestin, konsultoi system promptia ja tekee päätöksen."
   - Osoita tekoälysolmu ja sen system prompt.

3. **Työkalujen suorittaja** → Discord (tai muu lähettämissolmu)
   - "Tässä agentti toimii. Se ottaa päätöksen ja tekee konkreettista asiaa — lähettää viestin."
   - Osoita Discord-solmu.

4. **Muisti** → Google Sheets tai Memory-solmu
   - "Jos agentti tarvitsee muistaa asiakkaita tai historiaa, se tallennetaan tässä."
   - Näytä, miten konteksti voidaan hakea hakemalla tiedot ennen päättelyä.

5. **Turvakerros** → IF-solmu päättelyjen jälkeen
   - "Ennen kuin agentti toimii, se tarkistaa: onko vastaus turvallinen? Sisältääkö se arkaluonteisia tietoja?"
   - Näytä, miten IF-solmu voi blokata vaarallisia vastauksia.

6. **Palautesilmukka** → Logging (Google Sheets tai muu)
   - "Jokainen toimenpide kirjataan. Näin agentti oppii ja kehittyy."

### Keskustelu

- "Miten nämä kuusi osaa työskentelevät yhdessä?"
- "Mitä tapahtuisi, jos turvakerros puuttuisi?"
- "Miten agentti eroaa tavallisesta skriptistä n8n:ssä?"

---

## Tehtävä 3: Suunnittelutyöpaja — projektinideoiden arviointi (20 min)

### Valmistelu

Jaettele opiskelijat pareittain (2-3 henkilöä paria kohti). Jaa heille kolme eri projekti-ideaa (Lesson 26:n student-tasks.md:stä):
- Taso 1: FAQ-botti
- Taso 2: Sähköpostin yhteenveto
- Taso 3: Asiakaspalvelun tikettijärjestelmä

Tai anna opiskelijoiden valita oman idean.

### Ohjeet pareille

1. **Valitse projektityyppi** (10 min)
2. **Kirjoita yksinkertainen suunnitelma** käyttäen lesson 26:n lomaketta:
   - Käyttötapaus
   - Mitä se tekee (3-4 vaihetta)
   - Mitä se EI tee (rajat)
   - Hyväksyntäportit
   - Riskit
   - Solmukaaavio

3. **Näytä suunnitelma toiselle parille tai opettajalle** (5 min)

### Opettajan rooli

Kiertele luokkaa ja kysy:
- "Mistä työnkulku alkaa? Mikä on triggeri?"
- "Kuka tai mikä tekee päätöksiä? Onko se agentti vai chatbot?"
- "Missä vaiheessa ihminen päättää?"
- "Mitä riskeistä olette ajatelleet?"

Ohjaa opiskelijoita tarkentamaan suunnitelmiaan. Seuraavassa tunnissa he rakentavat näiden pohjalta.

### Yhteenveto (1 min)

"Hyvä suunnitelma säästää aikaa rakentamisessa. Nyt tiedätte, mitä rakentaa. Seuraavassa tunnissa alamme rakentaa ja testata."

---

## Arviointi

Opettaja arvioi seuraavaa:

1. **Solmujen ymmärtäminen** — Osavatko opiskelijat selittää, mitä kukin solmu tekee?
2. **Arkkitehtuurin pohdinta** — Linkkivätkö he solmut agentin kuuteen komponenttiin?
3. **Suunnittelun laatu** — Onko suunnitelma selkeä ja realistinen?
4. **Kriittinen ajattelu** — Tunnistiko he riskejä ja hyväksyntäportteja?

