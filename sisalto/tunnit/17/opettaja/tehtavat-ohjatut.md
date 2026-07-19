# Opettajavetoiset tehtävät — Oppitunti 17

## Johdanto oppituntiin (5 min)

Aloita ottamalla yhteys opiskelijoiden kokemukseen. Kysy: "Kuinka moni teistä on koskaan yrittänyt opetella jotain uutta ilman, että kukaan ohjasi tai kysyi oikeita kysymyksiä? Mitä tapahtui?" Anna muutaman opiskelijan kertoa. Korosta, että hyvä ohjaava kysyminen vie eteenpäin paljon nopeammin kuin yksin pähkäily.

Kerro, että tänään he rakentavat oman apuri-botin, joka auttaa jossakin heille tutussa arjen aiheessa — opiskelussa, harrastuksessa, tutussa pienessä palvelussa tai vaikka pelin tai sisällön ideoinnissa. Botti kysyy oikeita kysymyksiä ja ohjaa käyttäjää eteenpäin. Se on kuin henkilökohtainen apuri.

## Tehtävä 1: Apuri-botin käytön havainnollistaminen (15 min)

### Tavoite

Näyttää käytännössä, miltä toimiva botti näyttää ja mitä se tekee.

### Vaiheet

1. **Valmistelu:** Avaa ChatGPT, Claude tai Copilot, johon olet jo kirjoittanut apuri-botin järjestelmäpromptin. Kirjoita se etukäteen tai käytä teoria-aineiston esimerkkiä.

2. **Havainnollistaminen:** Kirjoita opiskelijoiden nähtäville käyttötilanne. Esimerkiksi:
   > "Aloitan salitreenin enkä tiedä, miten koota itselleni järkevä viikko-ohjelma. Pääsen salille kolmena päivänä viikossa."

3. **Seuraa botin vuorovaikutusta:** Kerro ääneen, mitä botti tekee:
   - "Botti kysyi ensin käyttäjän tavoitetta. Hyvä — se alkaa yksinkertaisesta."
   - "Nyt se kysyy lähtötasoa. Se on tärkeä — jos et tiedä, kenelle ohjaat, et ohjaa oikein."
   - "Huomaa, kuinka botti muistaa, mitä sanoimme aiemmin — se ei kysy samaa uudelleen."

4. **Lopputulos**: Kun botti on kerännyt tarpeeksi tietoa, anna sen koota lopputulos. Näytä, miltä valmis lopputulos näyttää.

5. **Pohdinta:** Kysy opiskelijoilta:
   - "Olivatko botin kysymykset hyödyllisiä?"
   - "Oliko jotain, jonka botti olisi pitänyt kysyä?"
   - "Mikä tekee botin järjestelmäpromptista hyvän?"

### Opettajan huomiot

Näytä, että botti ei ole täydellinen — se on vain työväline, joka auttaa, mutta käyttäjä tekee päätökset. Korosta, että järjestelmäprompti on kriittinen. Ilman sitä botti olisi vain yleinen ChatGPT, ei ohjaava apuri. Jos jotain menee pieleen (botti unohtaa jotain, kysyy huonon kysymyksen), käytä sitä opetusvälineenä: "Näetkö, miten tämä näyttää, kun järjestelmäprompti ei ole riittävän selkeä?"

---

## Tehtävä 2: Ryhmätyö — Ideoikaa botin kysymyksiä (20 min)

### Tavoite

Saada opiskelijat ajattelemaan, mitä kysymyksiä hyvä apuri-botti pitäisi esittää.

### Vaiheet

1. **Jakautuminen**: Jaa opiskelijat 3–4 henkilön ryhmiin.

2. **Anna käyttötilanne:** Jokainen ryhmä saa saman tai oman käyttötilanteen:
   > "Rakennamme apuri-botin, joka auttaa uutta jäsentä pääsemään alkuun urheiluseuran harrastuksessa."

3. **Tehtävä**: "Te olette apuri-botin suunnittelijat. Mitä 5–7 kysymystä botin pitäisi esittää, jotta se saisi riittävästi tietoa käyttäjän auttamiseksi?"

4. **Ryhmät kirjoittavat:** Anna ryhmille 10 minuuttia kysymysten kirjoittamiseen. Ohjaa heitä pohtimaan:
   - Mitä?
   - Kenelle?
   - Miksi?
   - Milloin?
   - Miten?

5. **Esittely:** Jokainen ryhmä esittelee 2–3 parasta kysymystään. Varaa ryhmälle kolme minuuttia.

6. **Yhteenveto**: Kerää kaikki kysymykset liitutaululle tai dialle. Mitkä olivat yleisimpiä? Mitkä olivat loistavia, ja mitkä kaikki muut unohtivat?

### Opettajan huomiot

Hyviä kysymyksiä ovat: "Kuka käyttää bottia?", "Mitä käyttäjä haluaa saada selville?", "Mikä käyttäjälle on uutta tai vaikeaa?" Heikot kysymykset ovat: "Mikä on lempivärisi?", "Montako vuotta olet ollut mukana?" (eivät vaikuta lopputulokseen). Käytä tätä opettaaksesi: "Kysymykset, jotka auttavat tekemään parempia päätöksiä, ovat hyviä. Kysymykset, jotka ovat yksityiskohtaisia mutta eivät vaikuta lopputulokseen, ovat huonoja."

---

## Tehtävä 3: Koko luokka — Arvioikaa, mitä tekee hyvän apuri-botin (10 min)

### Tavoite

Rakentaa yhteinen ymmärrys siitä, mitä hyväksi apuri-botiksi katsotaan.

### Vaiheet

1. **Kysymys**: "Olette nyt nähneet, mitä botti tekee ja mitä kysymyksiä se pitäisi esittää. Mitä vaatimuksia hyvällä apuri-botilla on?"

2. **Opiskelijoiden ajatukset**: Kuuntele heidän ehdotuksia. Kirjoita ylös:
   - Selkeä kuvaus, missä botti auttaa
   - Tieto, kenelle se on
   - Ymmärrys, miksi siitä on hyötyä
   - Looginen kysymysten järjestys
   - Selkeät rajat: mitä botti ei tee

3. **Kalibrointi**: Kysy seuraavia:
   - "Oliko demobotti riittävän hyödyllinen?"
   - "Oliko jokin kysymys liian yksityiskohtainen?"
   - "Oliko jokin kohta liian pinnallinen?"

4. **Säännöt**: Kerro, että seuraavassa harjoituksessa (tehtävät 17.1–17.4) he käyttävät näitä oivalluksia rakentaakseen oman botin.

### Opettajan huomiot

Hyväksi botiksi lasketaan selkeä, perusteltu, käyttäjäkeskeinen ja rajoiltaan harkittu botti. Huonoksi botiksi lasketaan epäselvä, liian yleinen tai rajoja huomioimaton botti. Kerro, että arviointi seuraavalla kerralla perustuu näihin kriteereihin.

---

## Sulkeminen (5 min)

Kertaa tunnin opit. Apuri-botti kysyy tarkoituksenmukaisia kysymyksiä ja ohjaa käyttäjää eteenpäin. Järjestelmäprompti määrittää botin toiminnan. Hyvä suunnitelma vastaa viiteen peruskysymykseen: kenelle, mitä, miksi, missä järjestyksessä ja millä rajoilla.

Kerro, että seuraavalla kerralla he:
1. Suunnittelevat oman botin kysymykset (tehtävä 17.1)
2. Kirjoittavat järjestelmäpromptin (tehtävä 17.2)
3. Testaavat bottia (tehtävä 17.3)
4. Iteroivat ja parantavat (tehtävä 17.4)

Huomenna oppitunnilla 18 he viimeistelevät ja esittelevät. Tämä on Tekoälyjen käyttö -osion arvioinnin ensimmäinen osa kahdesta.

---

## Ajatuksia ongelmien varalta

**Ongelma:** Opiskelija sanoo: "Entä jos botilla ei ole selkeää käyttäjää?"

**Vastaus:** "Hyvä kysymys! Joskus käyttäjä on opiskelija itse tai kaveri. Botti palvelee silti jotakuta: kenelle tämä on? Miksi botti on hyödyllinen hänelle? Jos et voi vastata, botin tarkoitus ei ole riittävän selkeä."

**Ongelma:** Ryhmä tuottaa liian yksityiskohtaisia kysymyksiä ("Mikä on lempivärisi?")

**Vastaus:** "Nämä ovat hyviä yksityiskohtia joskus, mutta ensin meidän pitää ymmärtää, MITÄ käyttäjä haluaa saavuttaa ja MITEN botti auttaa siinä. Pikkuasiat tulevat myöhemmin, kun tiedämme mitä botti tekee."

**Ongelma:** Opiskelija on epävarma, onko heidän botinsa "hyvä"

**Vastaus:** "Hyvyys mitataan, toimiiko se. Testaa sitä. Jos botti kysyy oikeita kysymyksiä ja kokoaa vastaukset järkeviksi, se on hyvä. Ei tarvitse olla täydellinen."
