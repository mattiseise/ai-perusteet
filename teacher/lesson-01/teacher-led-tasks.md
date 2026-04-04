# Opettajavetoiset tehtävät

## Tehtävä 1.1: Luokitteluharjoitus — AI vai ei AI — Luokkakeskustelu

### Tavoite
Haastaa opiskelijoiden "kaikki älykäs = AI" -ajattelu ja vahvistaa AI:n määritelmä käytännön esimerkkien kautta.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu (5 minuuttia ennen tuntia):**
Kirjoita liitutaululle tai projisele nämä 6 järjestelmää:
1. Älypuhelimen auto-correct
2. Netflix-suositukset
3. Pankin ATM-automaatti
4. Sähköpostin spämmi-suodatin (vanha versio, sääntöpohjainen)
5. Google Maps -reititys reaaliaikaisella liikennetiedolla
6. Älykoti, joka säätää lämmitystä kellonajan perusteella

**Luokkakeskustelu (20 minuuttia):**

1. **Avaus (2 min):** "Näytän teille 6 järjestelmää. Jokaisen kohdalla: käyttyykö se tekoälyä vai ei? Äänestyksen sijasta halusimme kuulla perustelut."

2. **Käy yksi kerrallaan (3 min per järjestelmä):**
   - Kysy: "Mitä mieltä? Miksi?"
   - Jos vastaus on "se oppii", kysy: "Mistä se oppii? Miltä se näyttää silloin?"
   - Jos vastaus on "se on älykäs", kysy: "Mitä tarkoittaa älykäs? Eroaa siitä, mitä tarkoitamme tekoälyllä?"

3. **Käänteinen hallusinaatio (5 min):** Näytä tämä sääntö: "Jos käyttäjä ei ole kovin aktiivinen, älä näytä kalliita mainoksia." Kysy: "Voiko tämä tekoäly tehdä sen, vai voiko tavallinen ohjelma?" (Vastaus: voi tehdä molemmat — tämä on liian epämääräinen esimerkki.)

**Vastaukset joita haet:**
- ATM: Ei AI. Se seuraa sääntöjä: PIN oikein → anna raha.
- Auto-correct (yksinkertainen): Voisi olla AI, mutta usein se on sääntöpohjainen sanakirja.
- Netflix: AI. Oppii miljoonista käyttäjäprofiileista.
- Google Maps + liikenne: AI. Oppii reaaliaikaisesta liikennetiedosta ja historiasta.
- Spämmi-suodatin (vanha): Ei AI, säännöt. (Uusissa Gmail-versioissa AI.)
- Älykoti: Riippuu. Yksinkertainen aikavälys = ei. Oppii käyttäjän käyttäytymisestä = AI.

**Virheet jotka selvitä:**
- "AI = automaatio" — Ei. Automaatio tekee saman, tekoäly oppii.
- "AI = monimutkainen" — Ei. Yksinkertainenkin ohjelmisto voi olla todella monimutkaista.
- "AI = tulokset ovat aina oikein" — Ei. AI antaa todennäköisyyksiä ja tekee virheitä.

### Odotettu oppimistulos

Opiskelijat ymmärtävät:
- Tekoäly vaatii *oppimisen* ja *datan*, ei vain automatisointi.
- Sama tehtävä voi tehdä sekä AI:lla että säännöillä, mutta eri tavoin.
- "Älykäs" ja "tekoäly" eivät ole synonyymeja.

---

## Tehtävä 1.2: Tapaustutkimus — Sääntö vs. Tekoäly Petoksentunnistuksessa — Ryhmäharjoitus

### Tavoite
Näyttää, miksi tekoäly pärjää paremmin monimutkaisissa päätöksentekotilanteissa, kuin säännöt.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu (10 minuuttia):**
Jaa luokka kolmeen ryhmään. Anna jokaiselle ensin sama 10 transaktioiden taulukko (katso opiskelija-tehtävästä). Ryhmien tehtävä:
- Ryhmä A: Kehitä 5 sääntöä petoksentunnistukseen
- Ryhmä B: Kehitä 5 *erilaista* sääntöä samaan ongelmaan
- Ryhmä C: Ajattele, mitä tekoäly voisi tehdä, mitä A ja B ei pysty

**Toteutus (30 minuuttia):**

1. Ryhmät työskenttelevät itsenäisesti (15 min).

2. Ryhmä A ja B esittelevät sääntönsä (3 min per ryhmä).
   - Kirjoita säännöt lautaan.
   - Kysy: "Kuinka monta petosta huomaisitte oikein?"
   - Testaa säännöt auki (esim. Transaktio #7 = 10 000 €, tuntematon maa. A sanoo petos, B sanoo laillinen.)

3. Ryhmä C esittelee AI-ajatuksensa (3 min).
   - Kysy: "Mitä dataa tekoäly tarvitsisi?"
   - Kysy: "Mitä parametreja tai kuvioita se voisi oppia?"

4. **Johtopäätös (5 min):** Kirjoita lautaan:
   ```
   Säännöt: Nopea, ennustettava, mutta jäykkä
   Tekoäly: Oppii kuvioita, parempi monimutkaisten tilanteen kanssa, mutta vaatii dataa
   ```

**Mahdollisia vastauksia/väärinkäsityksiä:**
- Väärä: "Säännöt ovat aina parempia, koska ne ovat nopeampia." Oikea: Nopeampia, mutta huonompia tarkkuudella.
- Väärä: "Tekoäly tunne petoksesta." Oikea: Se havaitsee kuvioita, joita ihminen ei näkisi.

### Odotettu oppimistulos

Opiskelijat ymmärtävät:
- Sääntöjen kehittäminen on vaikeaa, kun muuttujia on monta.
- Tekoäly voi "nähdä" kuvioita, joita ihmisen säännöt missaa.
- Kummallakaan ei ole selvää voittajaa — konteksti ratkaisee.

---

## Tehtävä 1.3: Omat sovellukset — Pohdinnan Fasilitaatio — Luokkakeskustelu

### Tavoite
Yhdistää teoria opiskelijoiden omaan digitaaliseen elämään ja tehdä tekoälystä konkreettista.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu (0 minuuttia, improvisoidaan):**
Pyydä 3–4 opiskelijaa jakaa yksi sovellus, jota he käyttävät päivittäin. Esimerkiksi:
- Instagram
- Snapchat
- Fortnite
- Spotify
- Discord

**Keskustelu (15 minuuttia):**

Jokaisesta sovelluksesta:
1. Kysy: "Missä näet tekoälyä täällä?" (Suositukset, sisällön suodatus, haku, jne.)
2. Kysy: "Miten sovellus voisi tietää, mitä sinä haluat?"
3. Kysy: "Millaista dataa se kerää sinusta?" (Ei yksityisyyden loukkaus, vaan opetus: data = tekoälyn polttoaine)

**Esimerkkiä:**
- **Instagram:** Suositukset (FYP) käyttävät tekoälyä. Sovellus näkee, mitä selailla, mitä tykkää, kuinka kauan pysyt postissa. Parametrit: "Tämä tuntuu samankaltaiselta kuin posit, joissa hän viettää aikaa kauan."
- **Spotify:** Sekoitus sääntöjä ja tekoälyä. Säännöt: "Jos lauloit tätä, saatat tykkää tästä samankaltaista." Tekoäly: Oppii miljoonista kuuntelijaprofiileista.
- **Fortnite:** Matchmaking voi käyttää tekoälyä. Säännöt: "Pelaajat samoilla taidoilla." Tekoäly: "Optimoi tasapainoa todella suuresta otantatiedosta."

**Johtopäätös (3 min):**
- Tekoäly ei ole tulevaisuutta — se on jo täällä.
- Se toimii taustalla ja opiskelijat eivät näe sitä.
- Tämä on hyvä ja huono asia (turvallisuus, yksityisyys).

### Odotettu oppimistulos

Opiskelijat ymmärtävät:
- Tekoäly on lähellä heidän päivittäistä elämää.
- Sovellukset käyttävät sekä sääntöjä että tekoälyä, ei vain yhtä.
- Data on tekoälyn polttoaine, ja he tuottavat sitä päivittäin.
