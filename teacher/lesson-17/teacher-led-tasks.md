# Opettajavetoiset tehtävät — Oppitunti 17

## Johdanto oppituntiin (5 min)

Aloita ottamalla yhteys opiskelijoiden kokemukseen. Kysy: "Kuinka moni teistä on koskaan aloittanut projektin ilman selkeää suunnitelmaa? Mitä tapahtui?" Anna muutaman opiskelijan kertoa. Korosta, että ilman suunnitelmaa projektit usein menevät pieleen — tai maksavat enemmän aikaa ja rahaa kuin suunnittelu olisi maksanut.

Kerro, että tänään he rakentavat botin, joka auttaa muita tekemään hyvän projektisuunnitelman. Botti kysyy oikeita kysymyksiä ja kokoaa vastaukset suunnitelmaksi. Se on kuin henkilökohtainen mentor.

## Tehtävä 1: Live-demo projektidokumenttibotin käytöstä (15 min)

### Tavoite

Näyttää käytännössä, miltä toimiva botti näyttää ja mitä se tekee.

### Vaiheet

1. **Valmistelu**: Avaa ChatGPT, Claude tai Copilot, johon olet jo kirjoittanut system promptin projektidokumenttibotille. (Kirjoita se etukäteen tai käytä self-study-materiaalista saatua esimerkkiä.)

2. **Live-demo**: Kirjoita opiskelijoilta näkyvillä oleva projektikuvaus. Esimerkiksi:
   > "Rakennan web-sovellusta opiskelijoille, joka auttaa löytämään harjoittelupaikat. Haluamme tiimin, joka osaa web-kehitystä."

3. **Seurata botin vuorovaikutusta**: Kerro ääneen, mitä botti tekee:
   - "Botti kysyi ensin lyhyttä projektikuvausta. Hyvä — se alkaa yksinkertaisesta."
   - "Nyt se kysyy käyttäjistä. Se on tärkeä — jos et tiedä, kenelle rakennat, et rakenna oikein."
   - "Huomaa, kuinka botti muistaa, mitä sanoimme aiemmin — se ei kysy samaa uudelleen."

4. **Lopputulos**: Kun botti on kerännyt tarpeeksi tietoa, anna sen koota suunnitelma. Näytä, miltä valmis suunnitelma näyttää.

5. **Reflektio**: Kysymykset opiskelijoille:
   - "Olivatko botin kysymykset hyödyllisiä?"
   - "Oliko jotain, jonka botti olisi pitänyt kysyä?"
   - "Mitä tekee botin system promptista hyvän?"

### Opettajan huomiot

Näytä, että botti ei ole täydellinen — se on vain työväline, joka auttaa, mutta käyttäjä tekee päätökset. Korosta, että system prompt on kriittinen. Ilman sitä botti olisi vain yleinen ChatGPT, ei mentori. Jos jotain menee pieleen (botti unohtaa jotain, kysyy huonon kysymyksen), käytä sitä opetusvälineenä: "Näetkö, miten tämä näyttää, kun system prompt ei ole riittävän selkeä?"

---

## Tehtävä 2: Ryhmätyö — Ideoikaa botin kysymyksiä (20 min)

### Tavoite

Saada opiskelijat ajattelemaan, mitä kysymyksiä hyvä projektidokumenttibotti pitäisi esittää.

### Vaiheet

1. **Jakautuminen**: Jaa opiskelijat 3–4 henkilön ryhmiin.

2. **Annetaan projekti**: Jokainen ryhmä saa saman projektikuvauksen (tai vaihtelevia):
   > "Rakennamme mobiilisovellusta, joka auttaa nuoria budjetoinnissa."

3. **Tehtävä**: "Te olette projektidokumenttibotin suunnittelijat. Mitä 5–7 kysymystä botin pitäisi esittää, jotta saisi riittävästi tietoa projektin suunnittelemiseksi?"

4. **Ryhmät kirjoittavat**: Anna ryhmille 10 minuuttia kirjoittaa kysymykset. Kehoita heitä ajattelemaan:
   - Mitä?
   - Kenelle?
   - Miksi?
   - Milloin?
   - Miten?

5. **Esittely**: Jokainen ryhmä esittelee 2–3 parhaita kysymyksiään (3 minuuttia per ryhmä).

6. **Yhteenveto**: Kerää kaikki kysymykset liitutaululle tai dialle. Mitkä olivat yleisimpiä? Mitkä olivat loistavia, ja mitkä kaikki muut unohtivat?

### Opettajan huomiot

Hyviä kysymyksiä ovat: "Kuka käyttää sovellusta?", "Mistä saadaan rahat?", "Miten tämä eroaa kilpailijoista?" Heikot kysymykset ovat: "Mitä väriä on sovellus?", "Kuinka paljon koodia?" (liian epäselvä). Käytä tätä opettaaksesi: "Kysymykset, jotka auttavat tehdä parempia päätöksiä, ovat hyviä. Kysymykset, jotka ovat yksityiskohtaisia mutta eivät vaikuta lopputulokseen, ovat huonoja."

---

## Tehtävä 3: Koko luokka — Arvioikaa, mitä tekee hyvän projektisuunnitelman (10 min)

### Tavoite

Rakentaa yhteinen ymmärrys siitä, mitä hyväksi projektisuunnitelmaksi katsotaan.

### Vaiheet

1. **Kysymys**: "Olette nyt nähneet, mitä botti tekee ja mitä kysymyksiä se pitäisi esittää. Mitä vaatimuksia hyvällä projektisuunnitelmalla on?"

2. **Opiskelijoiden ajatukset**: Kuuntele heidän ehdotuksia. Kirjoita ylös:
   - Selkeä kuvaus, mitä rakennetaan
   - Tieto, kenelle se on
   - Ymmärrys, miksi se on tarpeellinen
   - Realistinen aikataulu
   - Tiedot resursseista (ihmiset, raha, teknologia)

3. **Kalibrointi**: Kysy seuraavia:
   - "Oliko demosuunnitelma riittävä?"
   - "Oliko jokin osa liian yksityiskohtainen?"
   - "Oliko jokin osa liian pinnallinen?"

4. **Säännöt**: Kerro, että seuraavassa harjoituksessa (tehtävät 17.1–17.4) he käyttävät näitä oivalluksia rakentaakseen oman botin.

### Opettajan huomiot

Hyväksi suunnitelmaksi lasketaan selkeä, perusteltu, käyttäjäkeskeinen ja realistinen suunnitelma. Huonoksi suunnitelmaksi lasketaan epäselkeä, liian epärealistinen tai riskejä huomioimaton suunnitelma. Kerro, että arviointi seuraavalla kerralla perustuu näihin kriteereihin.

---

## Sulkeminen (5 min)

Kertaa, mitä tänään opittiin. Projektidokumenttibotti kysyy oikeita kysymyksiä ja kokoaa ne suunnitelmaksi. System prompt on se, joka tekee botista hyödyllisen. Hyvä suunnitelma vastaa viiteen perusiosioon: mitä, kenelle, miksi, milloin, miten.

Kerro, että seuraavalla kerralla he:
1. Suunnittele oman botin kysymykset (tehtävä 17.1)
2. Kirjoittaa system promptin (tehtävä 17.2)
3. Testavat bottia (tehtävä 17.3)
4. Iteroidaan ja parannetaan (tehtävä 17.4)

Huomenna oppitunnilla 18 he viimeistelevät ja esittelevät. Tämä on Tekoälyjen käyttö -osion arvioinnin ensimmäinen osa kahdesta.

---

## Ajatuksia ongelmien varalta

**Ongelma:** Opiskelija sanoo: "Entä jos projektilla ei ole selkeää asiakasta?"

**Vastaus:** "Hyvä kysymys! Joskus asiakas on itsesi tai tiimi. Botti kysyy silti: kenelle tämä on? Miksi me haluamme tehdä tämän? Jos et voi vastata, projekti ei ole riittävän selkeä."

**Ongelma:** Ryhmä tuottaa liian yksityiskohtaisia kysymyksiä ("Minkä väristä loggot?")

**Vastaus:** "Nämä ovat hyviä yksityiskohtia myöhemmin, mutta suunnitteluvaiheessa meidän pitää ensin ymmärtää MIKSI ja MITEN. Värit tulevat myöhemmin, kun kerran osaamme mitä rakennetaan."

**Ongelma:** Opiskelija on epävarma, onko heidän botinsa "hyvä"

**Vastaus:** "Hyvyys mitataan, toimiiko se. Testaa sitä. Jos botti kysyy oikeita kysymyksiä ja kokoaa vastaukset järkeviksi, se on hyvä. Ei tarvitse olla täydellinen."
