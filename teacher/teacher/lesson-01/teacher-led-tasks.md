# Opettajavetoiset tehtävät

## Tehtävä 1.1: Luokitteluharjoitus — AI vai ei AI — luokkakeskustelu

### Tavoite
Haastaa opiskelijoiden "kaikki älykäs = AI" -ajattelua ja vahvistaa AI:n määritelmää käytännön esimerkkien kautta.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu (5 minuuttia ennen tuntia):**
Kirjoita liitutaululle tai projisoi nämä 6 järjestelmää:
1. Älypuhelimen auto-correct
2. Netflix-suositukset
3. Pankin ATM-automaatti
4. Sähköpostin spämmi-suodatin (vanha versio, sääntöpohjainen)
5. Google Maps -reititys reaaliaikaisella liikennetiedolla
6. Älykoti, joka säätää lämmitystä kellonajan perusteella

**Luokkakeskustelu (20 minuuttia):**

1. **Avaus (2 min):** "Näytän teille 6 järjestelmää. Jokaisen kohdalla: käyttääkö se tekoälyä vai ei? Äänestyksen sijaan haluaisin kuulla perusteluja."

2. **Käy yksi kerrallaan läpi (3 min per järjestelmä):**
   - Kysy: "Mitä mieltä olette? Miksi?"
   - Jos vastaus on "se oppii", kysy: "Mistä se oppii? Miltä se näyttää silloin?"
   - Jos vastaus on "se on älykäs", kysy: "Mitä älykäs tarkoittaa? Eroaako se siitä, mitä tarkoitamme tekoälyllä?"

3. **Käänteinen hallusinaatio (5 min):** Näytä tämä sääntö: "Jos käyttäjä ei ole kovin aktiivinen, älä näytä kalliita mainoksia." Kysy: "Voiko tämän tehdä tekoäly vai voiko tämän tehdä tavallinen ohjelma?" (Vastaus: voi tehdä molemmat — tämä on liian epämääräinen esimerkki.)

**Vastaukset, joita haet:**
- ATM: Ei AI. Se seuraa sääntöjä: PIN oikein → anna raha.
- Auto-correct (yksinkertainen): Voi olla AI, mutta usein se on sääntöpohjainen sanakirja.
- Netflix: AI. Oppii miljoonista käyttäjäprofiileista.
- Google Maps + liikenne: AI. Oppii reaaliaikaisesta liikennetiedosta ja historiasta.
- Spämmi-suodatin (vanha): Ei AI, vaan sääntöjä. (Uusissa Gmail-versioissa AI.)
- Älykoti: Riippuu. Yksinkertainen aikaväli = ei. Oppii käyttäjän käyttäytymisestä = AI.

**Virheet, joita selvittää:**
- "AI = automaatio" — Ei. Automaatio tekee saman, tekoäly oppii.
- "AI = monimutkainen" — Ei. Yksinkertainenkin ohjelmisto voi olla todella monimutkainen.
- "AI = tulokset ovat aina oikein" — Ei. AI antaa todennäköisyyksiä ja tekee virheitä.

### Odotettu oppimistulos

Opiskelijat ymmärtävät:
- Tekoäly vaatii *oppimista* ja *dataa*, ei pelkästään automaatiota.
- Sama tehtävä voidaan tehdä sekä tekoälyllä että säännöillä, mutta eri tavoin.
- "Älykäs" ja "tekoäly" eivät ole synonyymeja.

---

## Tehtävä 1.2: Tapaustutkimus — sääntö vs. tekoäly petoksentunnistuksessa — ryhmäharjoitus

### Tavoite
Näyttää, miksi tekoäly pärjää paremmin monimutkaisissa päätöksentekotilanteissa kuin säännöt.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu (10 minuuttia):**
Jaa luokka kolmeen ryhmään. Anna jokaiselle ensin sama 10 transaktion taulukko (katso opiskelijatehtävästä). Ryhmien tehtävä:
- Ryhmä A: Kehitä 5 sääntöä petoksentunnistukseen
- Ryhmä B: Kehitä 5 *erilaista* sääntöä samaan ongelmaan
- Ryhmä C: Ajattele, mitä tekoäly voisi tehdä, mihin A ja B eivät pysty

**Toteutus (30 minuuttia):**

1. Ryhmät työskentelevät itsenäisesti (15 min).

2. Ryhmä A ja B esittelevät sääntönsä (3 min per ryhmä).
   - Kirjoita säännöt taululle.
   - Kysy: "Kuinka monta petosta huomaisitte oikein?"
   - Testaa säännöt käytännössä (esim. Transaktio #7 = 10 000 €, tuntematon maa. A sanoo petos, B sanoo laillinen.)

3. Ryhmä C esittelee AI-ajatuksensa (3 min).
   - Kysy: "Mitä dataa tekoäly tarvitsisi?"
   - Kysy: "Mitä parametreja tai kuvioita se voisi oppia?"

4. **Johtopäätös (5 min):** Kirjoita taululle:
   ```
   Säännöt: Nopea, ennustettava, mutta jäykkä
   Tekoäly: Oppii kuvioita, parempi monimutkaisissa tilanteissa, mutta vaatii dataa
   ```

**Mahdollisia vastauksia/väärinkäsityksiä:**
- Väärä: "Säännöt ovat aina parempia, koska ne ovat nopeampia." Oikea: Ne ovat nopeampia, mutta tarkkuudeltaan huonompia.
- Väärä: "Tekoäly tuntee petoksen." Oikea: Se havaitsee kuvioita, joita ihminen ei näkisi.

### Odotettu oppimistulos

Opiskelijat ymmärtävät:
- Sääntöjen kehittäminen on vaikeaa, kun muuttujia on monta.
- Tekoäly voi "nähdä" kuvioita, joita ihmisen laatimat säännöt missaavat.
- Kummallakaan ei ole selvää voittajaa — konteksti ratkaisee.

---

## Tehtävä 1.3: Omat sovellukset — pohdinnan fasilitaatio — luokkakeskustelu

### Tavoite
Yhdistää teoria opiskelijoiden omaan digitaaliseen elämään ja tehdä tekoälystä konkreettista.

### Opettajan ohjeet ja fasilitaatio

**Valmistelu (0 minuuttia, improvisoidaan):**
Pyydä 3–4 opiskelijaa jakamaan yksi sovellus, jota he käyttävät päivittäin. Esimerkiksi:
- Instagram
- Snapchat
- Fortnite
- Spotify
- Discord

**Keskustelu (15 minuuttia):**

Jokaisesta sovelluksesta:
1. Kysy: "Missä näet tekoälyä tässä?" (Suositukset, sisällön suodatus, haku jne.)
2. Kysy: "Miten sovellus voisi tietää, mitä sinä haluat?"
3. Kysy: "Millaista dataa se kerää sinusta?" (Ei yksityisyyden loukkausta, vaan opetusta: data = tekoälyn polttoaine)

**Esimerkkejä:**
- **Instagram:** Suositukset (FYP) käyttävät tekoälyä. Sovellus näkee, mitä selailet, mistä tykkäät ja kuinka kauan pysyt postauksessa. Parametrit: "Tämä tuntuu samankaltaiselta kuin postaukset, joiden parissa hän viettää pitkään aikaa."
- **Spotify:** Sekoitus sääntöjä ja tekoälyä. Säännöt: "Jos kuuntelit tätä, saatat tykätä tästä samankaltaisesta." Tekoäly: Oppii miljoonista kuuntelijaprofiileista.
- **Fortnite:** Matchmaking voi käyttää tekoälyä. Säännöt: "Pelaajat samoilla taidoilla." Tekoäly: "Optimoi tasapainoa erittäin suuresta datajoukosta."

**Johtopäätös (3 min):**
- Tekoäly ei ole tulevaisuutta — se on jo täällä.
- Se toimii taustalla, eivätkä opiskelijat näe sitä.
- Tämä on hyvä ja huono asia (turvallisuus, yksityisyys).

### Odotettu oppimistulos

Opiskelijat ymmärtävät:
- Tekoäly on lähellä heidän päivittäistä elämäänsä.
- Sovellukset käyttävät sekä sääntöjä että tekoälyä, eivät vain toista.
- Data on tekoälyn polttoaine, ja he tuottavat sitä päivittäin.