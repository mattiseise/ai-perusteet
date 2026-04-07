# Opettajan materiaalit – Lesson 19

## Osaamistavoitteet (Bloom)

**Muistaa / Ymmärtää:**
- Opiskelija osaa selittää, mikä agentti on ja miten se eroaa chatbotista, skriptistä ja työnkulusta.
- Opiskelija tunnistaa agentin kuusi rakennusosaa: syötekäsittelijä, päättelijä, työkalut, muisti, turvakerros ja palautesilmukka.
- Opiskelija ymmärtää autonomisuuden käsitteen ja sen rajat.
- Opiskelija ymmärtää suoritusputken käsitteen ja osaa kuvata, miten komponentit toimivat yhdessä.

---

## Pedagoginen lähestymistapa

### Avaus

Aloita **tutulla esimerkillä**: sähköpostin käsittely. Näytä, miten sama tehtävä voidaan automatisoida kolmella eri tavalla:
1. Skriptillä (yksinkertainen, ei ajattele)
2. Työnkululla (sääntöihin perustuva)
3. Agentilla (autonominen päätöksenteko)

Tämä antaa opiskelijoille konkreettisen viitekehyksen.

### Keskeinen käsite: hype vs. todellisuus

**Virheellinen ajatus:** "Agentti on vain fancy chatbot" tai "kaikki AI-automatisointi on agenttia."

**Oikea ajatus:** Agentilla on spesifinen rakenne ja itsenäisyys. Se ei ole sama asia kuin muu automaatio.

Vahvista tätä painokkaasti. Monet opiskelijat suhtautuvat agentteihin varauksella, kunnes ymmärtävät, että niissä on konkreettinen ero.

### Suoritusputki (pipeline) – keskeinen opetuskäsite

Agentin voimakkuus piilee siinä, että sen kuusi komponentti **toimivat yhdessä muodostaen suoritusputken**. Tämä ei ole vain lista osista, vaan **dynaaminen sykli**, jossa jokaisen vaiheen tulos vaikuttaa seuraavaan.

**Opetuskäytäntö:** Piirrä kuuden komponentin sykli taululle:
1. Sähköposti saapuu → **Syötekäsittelijä** (tekee datasta ymmärrettävää)
2. Tiedot käsitellään → **Päättelijä** (analysoi ja päättää)
3. Päätökset → **Työkalut** (suorittavat toiminnot)
4. Tulokset tallennetaan → **Muisti** (oppii ja muistaa)
5. Jokainen vaihe → **Turvakerros** (validoi ja suojaa)
6. Silmukka sulkeutuu → **Palautesilmukka** (parantaa seuraavalla kierroksella)

Tämän visuaalisen esityksen avulla opiskelijat näkevät, että agentti ei ole staattinen rakenne, vaan **elävä prosessi**.

### Opiskelijoiden kokemusten hyödyntäminen

Kysy opiskelijoilta:
- "Montako kertaa päivässä käytät chatbottia?"
- "Oletko nähnyt automatisoitua järjestelmää, joka tekee jotakin ilman sinun osallistumistasi?"

Nämä kysymykset kiinnittävät oppimisen heidän omiin kokemuksiinsa.

---

## Yleisiä väärinkäsityksiä

### 1. "Agentti on aina parempi kuin chatbot"

**Todellisuus:** Agentti on monimutkaisempi ja kalliimpi. Se on järkevä vain silloin, kun tehtävä on toistuva, monivaiheinen ja vaatii itsenäisiä päätöksiä.

### 2. "Agentti voi tehdä mitä tahansa"

**Todellisuus:** Agentti on rajallinen suhteessa tavoitteihinsa, työkaluihinsa ja muistiinsa. Se ei voi rikkoa rajoituksiaan, ellei sitä ole siihen suunniteltu.

### 3. "Autonomisuus tarkoittaa, että agentti toimii ilman valvontaa"

**Todellisuus:** Autonomisuus tarkoittaa, että agentti tekee päätöksiä oman logiikkansa pohjalta, mutta silti ihmisten asettamissa rajoissa. Valvonta on silti tarpeen, erityisesti kriittisissä sovelluksissa.

### 4. "Agentti on sama kuin työnkulku"

**Todellisuus:** Työnkulku seuraa etukäteen määriteltyjä sääntöjä. Agentti oppii ja muuttaa käyttäytymistään. Agentti on älykkäämpi, mutta myös monimutkaisempi.

### 5. "Agentin komponentit toimivat erikseen"

**Todellisuus:** Ne muodostavat suoritusputken, jossa jokaisen vaiheen tulos vaikuttaa seuraavaan. Yhden komponentin poistaminen tai heikentäminen (esim. muistin tai turvakerroksen) heikentää koko järjestelmää.

---

## Luokkatehtävä — ohjeistus

### Tehtävä 1: Luokittelu

Kun opiskelijat tekevät luokittelutehtävää, he saattavat epäonnistua seuraavissa kohdissa:

**Tavallinen virhe:** "Tämä on agentti, koska se on automaattinen."

**Oikea päätös:** Kysy: "Tekeekö se päätöksiä itsenäisesti vai seuraako se vain sääntöjä? Oppiiko se virheistään? Käyttääkö se muistia ja turvakerroksia?"

### Tehtävä 2: Suoritusputken jäljittäminen

Kun käyt läpi kuuden komponentin mallia, käytä **visuaalista kaaviota**. Piirrä silmukka taululle ja näytä, miten jokainen osa yhdistyy. Valitse konkreettinen esimerkki (esim. asiakaspalveluagentti) ja jäljitä, miten se etenee:
- **Syötekäsittelijä:** sähköposti tai chat-viesti saapuu
- **Päättelijä:** analysoi asiakkaan ongelman ja kiireellisyyden
- **Työkalut:** haku tietokannoista, ticket-järjestelmän päivitys, vastauksen lähettäminen
- **Muisti:** oppii asiakkaan historian ja hänen tyypilliset ongelmansa
- **Turvakerros:** varmistaa, että vastaus on asianmukainen eikä sisällä arkaluonteisia tietoja
- **Palautesilmukka:** asiakkaan vastaus parantaa seuraavan käsittelyn tarkkuutta

Tämä konkreettinen jäljitys auttaa opiskelijoita ymmärtämään, että kukin komponentti on **välttämätön** ja **riippuvainen muista**.

### Tehtävä 3: Riskianalyysi

Kun keskustelette autonomisuuden vaaroista, käytä **oikeaa esimerkkiä**: esimerkiksi äskettäin ilmoitettua tapausta tekoälyn tekemästä virheestä tai varoittavia tarinoita.

Keskustelkaa erityisesti siitä, mitä tapahtuu, jos turvakerros heikkenee, muisti katoaa tai palautesilmukka ei toimi.

---

## Arviointivihjeet

### Hyvä vastaus:

"Tämä on agentti, koska se käsittelee syötteet (syötekäsittelijä), analysoi tilanteen (päättelijä), tekee päätöksiä ja toimii itsenäisesti (työkalut), muistaa tapahtumat ja asiakkaiden historiaa (muisti), noudattaa turvallisuusperiaatteita (turvakerros) ja parantaa itseään jokaisen tapahtuman perusteella (palautesilmukka). Nämä kuusi komponenttia muodostavat suoritusputken, joka erottaa agentin chatbotista."

### Riittävä vastaus:

"Tämä on agentti, koska se tekee päätöksiä autonomisesti ja oppii kokemuksistaan."

### Heikko vastaus:

"Tämä on agentti, koska se on tekoäly" tai "koska se on nopea."

---

## Tuntiesityksen rakenne (45 minuuttia)

1. **Avaava keskustelu** (5 min) — Esimerkki sähköpostin käsittelystä
2. **Suoritusputken opetus** (10 min) — Kuuden komponentin sykli taululle, visuaalinen opetus
3. **Itsenäinen lukeminen** (10 min) — Opiskelijat lukevat aineistoa
4. **Ryhmätehtävä: suoritusputken jäljitys** (15 min) — Järjestelmien komponenttien tunnistaminen
5. **Yhteenveto ja riskianalyysi** (5 min) — Autonomisuuden rajat ja turvallisuuden merkitys

---

## Jatkoyhteys Lesson 20:een

Lesson 20 käsittelee sitä, **milloin agentti on oikea ratkaisu**. Tämä oppitunti luo pohjan: opiskelijat ymmärtävät, mikä agentti on ja miten sen komponentit toimivat yhdessä suoritusputkessa. Seuraavaksi he oppivat, mitä kustannuksia ja hyötyjä siihen liittyy.