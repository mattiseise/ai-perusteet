# Lesson 24: Opettajavetoiset tehtävät

## Tehtävä 1: Live-demo — Agentin työkalut näkyvästi

**Aika:** 25 min
**Materiaali:** Esimerkki-agentti, jonka voi näyttää olevan toiminta vaiheitta

**Kulku:**
1. **Johdanto (3 min):** "Näytämme agentin, joka tekee analyysiraportin. Näette, miten se käyttää eri työkaluja."
2. **Vaihe 1: Tiedostot (5 min):** Näytä agentti lukemassa tiedostoa
   - "Agentti avaa myyntitiedot.csv"
   - Näytä, mitä se näkee
   - Kysy: "Mitä oikeuksia agentilla pitäisi olla?" (Lukea, ei kirjoittaa)
3. **Vaihe 2: CLI (5 min):** Näytä agentti ajamassa komentoa
   - "Nyt agentti ajaa Python-analyysin"
   - Näytä komennon tulos
   - Kysy: "Mitä pahaa voisi tapahtua, jos agentti voisi ajaa mitä tahansa komentoja?" (Poistaa tiedostoja, sammuttaa palvelimen)
4. **Vaihe 3: Verkkohaku (5 min):** Näytä agentti hakemassa tietoa
   - "Nyt agentti hakee kilpailijoiden hinnat"
   - Näytä hakutulokset
   - Kysy: "Mitä vaaraa on, jos agentti hakee herkkiä tietoja?" (Yksityisyyden loukkaus)
5. **Vaihe 4: Raportti (5 min):** Näytä agentti kirjoittamassa raporttia
   - Näytä lopullinen raportti
   - "Näette: agentti kutsui neljää eri työkalua järjestyksessä"
6. **Analyysi (2 min):** "Kuka näistä vaiheista voisi mennä pieleen?"

**Facilitoinnin vinkkejä:**
- Tehdä demosta interaktiivinen — kysy opiskelijoilta joka vaiheessa
- Jos agentin työkalu ei toimi, käytä sitä opetuksena: "Entä nyt? Mikä meni pieleen?"
- Osoita: "Agentti ei ole yksi iso neuroverkko — se on orkesteri!"

**Solo-vaihtoehto:** Dokumentoi yksinkertainen agentti-prosessi (esim. "Lähettää sähköpostin") ja merkitse jokaisen vaiheen, mitä työkaluja se käyttää.

---

## Tehtävä 2: Ryhmätyö — Turvallisuussuunnittelu

**Aika:** 20 min
**Skenario:** "Agentti analysoib palvelimen lokeja ja etsii häiriöitä. Mitä turvallisuusrajoituksia pitäisi asettaa?"

**Kulku:**
1. **Jaetaan ryhmiin (1 min):**
   - Ryhmä 1: Tiedostojen turvallisuus
   - Ryhmä 2: CLI:n turvallisuus
   - Ryhmä 3: Verkkohakujen turvallisuus
2. **Analyysi (8 min):** "Mitä pahaa voisi tapahtua? Miten voisit suojata?"
   - Ryhmä 1: "Mitkä tiedostot agentilla saa lukea? Voiko se poistaa?"
   - Ryhmä 2: "Mitä komentoja se voi ajaa? Whitelist vai blacklist?"
   - Ryhmä 3: "Mitä sitä voi hakea? Onko joitain kiellettyjä hakuja?"
3. **Esitykset (8 min):** Jokainen ryhmä esittelee:
   - Riskif sen alueella
   - Ehdotettu rajoitus
   - Perustelut
4. **Kokonaissuunnitelma (3 min):** "Yhdessä muodostamme täydellisen turvallisuussuunnitelman"

**Facilitoinnin vinkkejä:**
- Auta ryhmiä ajattelemaan "entä jos" -skenaarioita
- "Entä jos agentti on hakkeroitu? Mitä se voi tehdä?"
- Korostaa: "Turvallisuus ei ole mikään lisä — se on ydin"

**Solo-vaihtoehto:** Kirjoita turvallisuussuunnitelma yhdelle työkalulle (esim. "Miten rajoittaa agentin CLI-oikeuksia?")
**Skenario:** "Teidän pitäisi päättää: mitkä prosessit automatisoituu täysin agentin tekemiksi, ja mitkä vaativat ihmisen hyväksyntää?"

**Kulku:**
1. **Prosessit (3 min):** Opettaja listaa 4-5 prosessia:
   - Tilauksien vastaanottaminen
   - Maksujen käsittely
   - Asiakastukitikettien vastaaminen
   - Henkilöstön rekrytointi
   - Varastojen päivitys
2. **Pienryhmät (10 min):** Kukin ryhmä valitsee yhden prosessin ja päättää:
   - Mitkä vaiheet automatisoituu?
   - Mitkä vaativat hyväksyntää?
   - Miksi?
3. **Esitykset ja väittely (10 min):** Ryhmät puolustavat valintojaan. Muut voivat haastaa.
4. **Yhteenveto (2 min):** "Harvoin on oikea vastaus — se on aina kompromissi riskin ja tehokkuuden välillä."

**Facilitoinnin vinkkejä:**
- "Mitä jos hyväksyjä on poissa?"
- "Kuinka nopeasti ihminen pystyy hyväksymään?"
- "Mitkä prosessit ovat riskillisempiä kuin muut?"

**Solo-vaihtoehto:** Valitse yksi prosessi ja kirjoita: "Missä vaiheissa tarvitsen hyväksyntää ja miksi?"

---

## Tehtävä 2: Skenaariopohjainen päätös — Vaarallinen tilanne

**Aika:** 20 min
**Skenario:** "Agentti ehdottaa päätöstä, mutta se kuulostaa vaaralliselta. Hyväksyjä oli kiiruhtaa ja hyväksyi. Mitä nyt?"

**Kulku:**
1. **Asetus (3 min):** Opettaja kertoo skenaarion: "Agentti ehdottaa: 'Korottaa kaikille asiakkaille hintaa 20%. Johtaja kiiruhtaa ja hyväksyy ilman tarkempaa katsantoa. Seuraavana päivänä 500 asiakasta puolittaa tilauksensa.'"
2. **Analyysi (10 min):** Ryhmät pohdinnan:
   - Kuka on vastuussa?
   - Olisiko tämä voitu estää?
   - Mitä paremmin huomioitu hyväksyntäprosessissa?
3. **Ehdotukset (5 min):** Ryhmät ehdottavat parannuksia
4. **Pohdi:** "Tämä on todellinen — hyväksyntäportti on vain niin hyvä kuin ihminen, joka päättää."

**Mahdollisia parannuksia (joita voit ohjata):**
- Pakollinen "nukkumispäivä" ennen toteutusta
- Enemmän tietoa hyväksyjälle
- Automaattinen tarkistus liian radikaleille muutoksille
- Porrastettu täyttöönotto (testi pienessä joukossa ensin)

**Solo-vaihtoehto:** Kirjoita: "Mitä hyväksyntäprosessi olisi pitänyt sisältää, jotta tämä ei tapahtuisi?"
