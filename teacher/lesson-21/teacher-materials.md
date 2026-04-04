# Opettajan materiaalit – Lesson 21

## Osaamistavoitteet (Bloom)

**Ymmärtää / Soveltaa:**
- Opiskelija osaa suunnitella oman botin määrittelemällä tarkoitus, rooli ja ohjeet.
- Opiskelija ymmärtää järjestelmäpromptin merkityksen botin käyttäytymiselle.
- Opiskelija osaa erottaa omien bottien vahvuudet ja rajoitukset agenteihin verrattuna.

## Pedagoginen lähestymistapa

### Avaus

Aloita kysymyksellä: "Kuka haluaisi tehdä oman AI-botin? Mitä se tekisi?" Tämä herättää kiinnostusta.

Varoitus: "Monet tekevät vain nimetyn ChatGPT:n. Halun näyttää, miten tehdä botti, joka on **todella hyödyllinen**."

### Keskiössä

Ohjeistus on avain. Hyvä järjestelmäpromti tekee eron hyvän ja huonon botin välille.

Näytä esimerkki huonosta järjestelmäprompista: "Olet Python-tutori." vs. hyvästä: pitkä, yksityiskohtainen prompi, joka sisältää roolin, ohjeet ja rajaukset.

### Rajoitukset

Tärkeä viesti: Omat botit eivät ole agenteja. Ne eivät voi oppia, integroitua laajasti tai tehdä autonomisia päätöksiä. Mutta niillä on paikkansa.

## Virheellinen ajattelu

- **"Kaikki botit ovat samanlaisia"** → Ei. Ohjeistus tekee suuren eron.
- **"Oma botti = agentti"** → Ei. Agentti on paljon autonomisempi.
- **"Rajaukset ovat turhia"** → Ei. Ne ovat kriittisiä turvallisuuden ja tarkkuuden kannalta.

## Tuntiesityksen rakenne (45 min)

1. **Avaus**: Mikä on oma botti? (5 min)
2. **Itsenäinen lukeminen**: Opiskelijat lukevat self-study-materiaalin (15 min)
3. **Suunnittelu-työpaja**: Opiskelijat suunnittelevat oman botin paperilla (15 min)
4. **Jakaminen**: Jokainen esittelee bottiensa (5 min)
5. **Yhteenveto**: Mitä opimme? (5 min)

## Suunnittelu-työpajalla
1. Rakentaa tehtäväjonon monimutkaista prosessia analysoimalla
2. Tunnistaa agenttijärjestelmän syötteet, askeleet ja tuotteet (inputs, steps, outputs)
3. Arvioida, milloin omaksi koodattu agentti riittää ja milloin tarvitaan kehys
4. Tunnistaa virheenkäsittelyn ja integraatioiden merkityksen agenttijärjestelmässä

## Yleisimmät väärinkäsitykset

1. **"Agentti tekee kaiken automaattisesti, ei tarvita mitään tekemistä"** → Agentti vaatii huolellista suunnittelua, testaamista ja jatkuvaa valvontaa

2. **"Agenttikehys on aina parempi kuin oma koodi"** → Riippuu vaatimuksista; yksinkertainen agentti voi olla parempi omalla koodilla

3. **"Integraatiot ovat helppoja"** → Integraatiot vaativat huolellista turvallisuussuunnittelua ja testausta

4. **"Virheenkäsittely on vain tekniikka"** → Se on kriittistä liiketoiminnalle, koska virheet voivat aiheuttaa rahallista vahinkoa

5. **"Arkkitehtuuri on vain piirtämistä"** → Arkkitehtuuri määrittää riskejä, vaatimuksia ja vastuita

## Tarkistustehtävät / CFU (Checking-for-Understanding)

1. Mikä on tehtäväjonon tehtävä agenttijärjestelmässä?
2. Mitä eroa on omaksi koodatulla agentilla ja agenttikehyksellä?
3. Nimeä kolme erilaista virheenkäsittelystrateigiaa.
4. Miksi arkkitehtuurin ymmärtäminen on tärkeää riskienhallinnan kannalta?
5. Mitä dataa agentti voi tarvita syötteenä, kun se käsittelee tilauksia?
6. Mitä tarkoittaa "integraatio" agenttijärjestelmässä?
7. Jos agentti epäonnistuu, kuka on vastuussa — agentti, kehittäjä vai käyttäjä?
8. Mikä on "single point of failure" tehtäväjonossa?

## Tyypilliset vaikeudet

### 1. Arkkitehtuurin abstraktio
Opiskelijat voivat vaikeutua näkemään, kuinka abstrakteja käsitteitä sovelletaan todelliseen ongelmaan. 
**Apua:** Käytä konkreettisia kaavioita ja oikean maailman esimerkkejä.

### 2. Riskin tunnistaminen
Opiskelijat eivät välttämättä näe, missä askelissa voi mennä pieleen. 
**Apua:** Kysy "mitä voisi mennä pieleen" jokaiselle askeleelle erikseen.

### 3. Vaatimuksista ratkaisuun
Opiskelijat voivat vaikeutua valitsemaan sopivaa ratkaisua (oma koodi vs. kehys). 
**Apua:** Tee vertailutaulukko, johon ne voivat merkitä plussat ja miinukset.

### 4. Tekniikan ja liiketoiminnan yhteys
Opiskelijat eivät näe, miksi arkkitehtuuri on liiketoiminnallisesti tärkeä. 
**Apua:** Kysy "mikä tapahtuu, jos tämä menee pieleen?" dollarimäärinä.
