# Opettajan materiaalit — oppitunti 23

## Osaamistavoitteet

Tämän oppitunnin tavoitteena on, että opiskelija ymmärtää, miten **suunnittelumallit** ohjaavat agentin päättelyä ja toimintaa. Oppitunnin ydin on, että agentti ei vain käytä tekoälyä, vaan sen toiminta täytyy suunnitella: miten se ajattelee, missä järjestyksessä se toimii ja milloin tehtävä kannattaa jakaa usealle erikoistuneelle agentille.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, mitä **ReAct** tarkoittaa: agentti vuorottelee päättelyn ja toiminnan välillä.
- Opiskelija ymmärtää, mitä **ketjuajattelu** tarkoittaa: agentti etenee vaihe vaiheelta järjestyksessä.
- Opiskelija ymmärtää, mitä **moniagenttijärjestelmä** tarkoittaa: tehtävä jaetaan useille erikoistuneille agenteille.
- Opiskelija tunnistaa, että eri suunnittelumallit sopivat erilaisiin tehtäviin.

### Soveltaa ja analysoida

- Opiskelija osaa valita, sopiiko tiettyyn tehtävään paremmin ReAct, ketjuajattelu vai moniagenttirakenne.
- Opiskelija osaa kuvata agentin päättelyn vaiheina tai lokina.
- Opiskelija osaa tunnistaa tilanteita, joissa ReAct voi jäädä kiertämään silmukkaa tai ketjuajattelu voi olla liian jäykkä.

### Luoda ja arvioida

- Opiskelija osaa suunnitella oman agenttinsa **päättelymallin**.
- Opiskelija osaa perustella, miksi valittu malli sopii omaan agenttiongelmaan.
- Opiskelija osaa arvioida, milloin yhden agentin sijaan kannattaisi käyttää useampaa erikoistunutta agenttia.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että agentin päättelyä täytyy ohjata. Hyvä agentti ei hypi sattumanvaraisesti työkalusta toiseen, vaan noudattaa tehtävään sopivaa päättelymallia.

---

## Pedagoginen lähestymistapa

### Ydinviesti: suunnittelumallit opettavat agentille, miten toimia

Suunnittelumallit auttavat opiskelijaa ymmärtämään, että agentin “ajattelu” ei ole taikuutta. Se voidaan jäsentää toimintamalleiksi, joita voi suunnitella, testata ja arvioida.

Kolme keskeistä mallia ovat:

- **ReAct:** joustava ja iteratiivinen malli, jossa agentti ajattelee, toimii, havainnoi ja ajattelee uudelleen.
- **Ketjuajattelu:** systemaattinen malli, jossa agentti jakaa tehtävän vaiheisiin ja etenee järjestyksessä.
- **Moniagenttijärjestelmät:** jaetun työn malli, jossa eri agentit erikoistuvat eri osatehtäviin.

> **Hyvä päättelymalli tekee agentin toiminnasta ennakoitavampaa, jäljitettävämpää ja helpommin korjattavaa.**

### ReAct — ajattele, toimi ja tarkista

**ReAct** tarkoittaa päättelyn ja toiminnan vuorottelua. Agentti ei tee kaikkea yhdellä kertaa, vaan etenee silmukassa: se ajattelee, toimii, havainnoi tuloksen ja päättää seuraavan askeleen.

ReAct-malli vastaa hyvin ihmisen ongelmanratkaisua:

1. **Ajattele:** Mitä tarvitsen tämän tehtävän ratkaisemiseen?
2. **Toimi:** Käytä työkalua, hae tietoa tai suorita seuraava vaihe.
3. **Havainnoi:** Mitä tapahtui? Sainko hyödyllisen tuloksen?
4. **Ajattele uudelleen:** Riittääkö tieto vai tarvitaanko uusi toimenpide?
5. **Toimi seuraavaksi:** Jatka tai vastaa käyttäjälle.

**Esimerkki opetukseen**

Anna opiskelijoille tehtävä: ”Asiakas kysyy, onko tuotetta varastossa.” Pyydä heitä kirjoittamaan ReAct-loki: mitä agentti ajattelee, mitä työkalua se käyttää, mitä se havaitsee ja miten se vastaa.

ReAct on hyödyllinen silloin, kun agentti ei tiedä etukäteen kaikkia vaiheita. Se voi edetä havaintojen perusteella ja muuttaa suuntaa, jos ensimmäinen toimenpide ei auta.

| ReAct-vaihe | Mitä agentti tekee? | Esimerkki |
| --- | --- | --- |
| **Ajattelu** | Päättelee, mitä tietoa tarvitaan. | ”Tarvitsen varastosaldon.” |
| **Toiminta** | Kutsuu työkalua tai hakee tietoa. | Agentti kutsuu varasto-API:a. |
| **Havainto** | Arvioi työkalun palauttaman tuloksen. | ”Tuotetta on 5 kappaletta.” |
| **Seuraava päätös** | Päättää, vastaako käyttäjälle vai jatkaako tutkimista. | ”Tieto riittää. Vastaan asiakkaalle.” |

### Ketjuajattelu — vaihe vaiheelta etenevä malli

**Ketjuajattelussa** agentti jakaa ongelman selkeisiin vaiheisiin ja käsittelee ne järjestyksessä. Tämä sopii tilanteisiin, joissa prosessi on melko ennakoitava ja jokainen vaihe riippuu edellisestä.

**1. Ongelma:** Mitä asiakas kysyy?

**2. Rajoitteet:** Mitä sääntöjä tai ehtoja pitää noudattaa?

**3. Valinnat:** Mitä vaihtoehtoja on?

**4. Päätös:** Mikä vaihtoehto valitaan ja miksi?

Ketjuajattelu on hyödyllinen esimerkiksi palautuspyynnön käsittelyssä. Agentti tarkistaa ensin palautusajan, sitten palautuskäytännön, sitten asiakkaan oikeuden palautukseen ja vasta lopuksi muodostaa vastauksen.

> **Tärkeää:** Ketjuajattelussa ei hypitä vaiheiden yli. Jokainen vaihe rakentuu edellisen päälle.

### Moniagenttijärjestelmät — jaettu vastuu

**Moniagenttijärjestelmässä** tehtävä jaetaan usealle erikoistuneelle agentille. Tämä sopii monimutkaisiin tehtäviin, joissa tarvitaan erilaisia osaamisalueita: analyysiä, tiedonhakua, kirjoittamista, tarkistusta tai päätöksentekoa.

Moniagenttijärjestelmissä on kaksi perusmallia:

| Malli | Miten se toimii? | Milloin sitä käytetään? |
| --- | --- | --- |
| **Hierarkkinen malli** | Johtaja-agentti näkee kokonaisuuden ja jakaa tehtävät erikoistuneille agenteille. | Kun tehtävä tarvitsee selkeän koordinoijan ja useita erikoistuneita vaiheita. |
| **Yhteistyömalli** | Agentit keskustelevat keskenään ja kehittävät ratkaisua yhdessä. | Kun ratkaisu vaatii eri näkökulmien vertailua tai yhteistä päätöksentekoa. |

Moniagenttijärjestelmät ovat tehokkaita, mutta ne lisäävät monimutkaisuutta. Mitä enemmän agentteja on, sitä vaikeampaa on seurata, kuka teki mitä, miksi ja millä tiedolla. Siksi lokitus, roolien rajaus ja selkeä orkestrointi ovat erityisen tärkeitä.

**Opettajan huomio:** Ohjaa opiskelijoita aloittamaan yhdestä agentista. Moniagenttirakennetta kannattaa käyttää vasta, jos tehtävä todella vaatii erikoistumista. Muuten se voi tehdä projektista tarpeettoman vaikean.

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”ReAct jatkaa, kunnes ratkaisu löytyy.”

**Korjaava näkökulma:** ReAct tarvitsee rajat. Jos agentille ei aseteta enimmäismäärää iteraatioille, se voi jäädä toistamaan samoja vaiheita. Aseta esimerkiksi enintään 3–5 työkalukutsua ennen kuin agentti pyytää ihmisen apua tai keskeyttää tehtävän.

> Joustava päättely tarvitsee rajat. Muuten joustavuus muuttuu hallitsemattomaksi silmukaksi.

### Väärinkäsitys 2: ”Ketjuajattelu on huono, koska se on jäykkä.”

**Korjaava näkökulma:** Ketjuajattelun jäykkyys on sen vahvuus silloin, kun prosessin pitää olla ennakoitava. Esimerkiksi palautuksen, laskun tarkistuksen tai hyväksyntäprosessin pitää usein edetä tietyssä järjestyksessä.

### Väärinkäsitys 3: ”Moniagenttijärjestelmä on aina parempi kuin yksi agentti.”

**Korjaava näkökulma:** Moniagenttijärjestelmä lisää rooleja, viestinvaihtoa, lokitusta ja virhemahdollisuuksia. Aloita yhdellä agentilla ja lisää muita vain, jos tehtävän monimutkaisuus todella vaatii sitä.

### Väärinkäsitys 4: ”Suunnittelumalli on vain tekninen toteutustapa.”

**Korjaava näkökulma:** Suunnittelumalli on myös pedagoginen ja arkkitehtoninen valinta. Se vaikuttaa siihen, miten agenttia testataan, miten sitä selitetään ja miten sen virheitä korjataan.

---

## Luokkatehtävien ohjeistus

### TT-A: ReAct-lokin kirjoittaminen

**Tavoite:** Opiskelija ymmärtää ReAct-mallin ajattelu–toiminta–havainto-silmukan.

**Tehtävä:** Anna opiskelijoille lyhyt asiakastilanne ja pyydä heitä kirjoittamaan agentin ReAct-loki. Lokissa pitää näkyä, mitä agentti ajattelee, mitä työkalua se käyttää, mitä se havaitsee ja miten se jatkaa.

| Vaihe | Opiskelijan vastaus |
| --- | --- |
| **Ajattelu** | Mitä agentti tarvitsee seuraavaksi? |
| **Toiminta** | Mitä työkalua agentti käyttää? |
| **Havainto** | Mitä työkalu palauttaa? |
| **Seuraava päätös** | Riittääkö tieto vai tarvitaanko uusi vaihe? |

**Aika-arvio:** 15–20 minuuttia

---

### TT-B: Ketjuajattelun vaiheistus

**Tavoite:** Opiskelija osaa purkaa monimutkaisen tehtävän selkeiksi vaiheiksi.

**Tehtävä:** Anna opiskelijoille tehtävä, esimerkiksi palautuspyynnön käsittely, laskun tarkistaminen tai tukipyynnön luokittelu. Opiskelijat kirjoittavat tehtävän 4–6 vaiheeksi.

**Ohje opiskelijalle:**

1. Mikä ongelma pitää ratkaista?
2. Mitä tietoa tarvitaan ensin?
3. Mitä sääntöjä tai rajoitteita pitää tarkistaa?
4. Mitä vaihtoehtoja on?
5. Mikä päätös tehdään?
6. Mitä agentti tekee päätöksen jälkeen?

**Aika-arvio:** 15–20 minuuttia

---

### TT-C: Suunnittelumallin valinta

**Tavoite:** Opiskelija osaa valita tehtävään sopivan päättelymallin ja perustella valintansa.

**Tehtävä:** Anna opiskelijoille 3–4 eri tilannetta. He valitsevat jokaiseen ReActin, ketjuajattelun tai moniagenttijärjestelmän ja perustelevat valintansa.

| Tilanne | Sopiva malli | Perustelu |
| --- | --- | --- |
| Agentti tutkii, miksi palvelin antaa virheen 502. | ReAct | Agentti tarvitsee havaintoihin perustuvaa etenemistä ja voi vaihtaa suuntaa tulosten mukaan. |
| Agentti käsittelee palautuspyynnön. | Ketjuajattelu | Prosessi etenee selkeissä vaiheissa: tarkista aika, tarkista ehdot, tee päätös ja vastaa. |
| Agentti tuottaa laajan markkinaraportin, jossa tarvitaan tiedonhakua, analyysiä, kirjoittamista ja tarkistusta. | Moniagenttijärjestelmä | Tehtävä voidaan jakaa erikoistuneille agenteille, kuten tutkijalle, analysoijalle, kirjoittajalle ja tarkistajalle. |

**Aika-arvio:** 20–25 minuuttia

---

### TT-D: Moniagenttikaavion piirtäminen

**Tavoite:** Opiskelija ymmärtää, miten vastuu voidaan jakaa usealle agentille.

**Tehtävä:** Opiskelijat valitsevat monimutkaisen tehtävän ja piirtävät siitä moniagenttikaavion. Kaaviossa pitää näkyä agenttien roolit, tiedonkulku ja mahdollinen johtaja-agentti.

**Ohje opiskelijalle:**

- Mikä agentti johtaa kokonaisuutta?
- Mitä erikoistuneita agentteja tarvitaan?
- Mitä tietoa kukin agentti saa?
- Mitä kukin agentti palauttaa?
- Miten lopullinen päätös syntyy?

**Aika-arvio:** 20–25 minuuttia

---

## CFU-kysymykset

1. **ReAct:** Miksi ReAct-mallissa agentti ei tee kaikkia toimintoja heti kerralla?
2. **Ketjuajattelu:** Millaisiin tehtäviin vaiheittainen eteneminen sopii parhaiten?
3. **Moniagentti:** Miksi moniagenttijärjestelmä voi olla tehokas mutta myös vaikeampi hallita?
4. **Valinta:** Mistä tiedät, että tehtävä tarvitsee ReActin eikä pelkkää ketjuajattelua?
5. **Rajoitukset:** Miksi ReAct-agentille kannattaa asettaa enimmäismäärä iteraatioita?

---

## Opettajan vihjeet

### Jos opiskelija sekoittaa ReActin ja ketjuajattelun

Käytä seuraavaa erottelua:

- **ReAct:** agentti päättää seuraavan askeleen havaintojen perusteella.
- **Ketjuajattelu:** agentti etenee ennalta määriteltyjen vaiheiden mukaan.

> ReAct sopii tutkimiseen. Ketjuajattelu sopii prosessiin.

### Jos opiskelija haluaa tehdä heti moniagenttijärjestelmän

Kysy:

- Miksi yksi agentti ei riitä?
- Mitä erikoisosaamista kukin agentti tuo?
- Miten agenttien välinen viestintä lokitetaan?
- Mitä tapahtuu, jos yksi agenteista tekee virheen?

### Jos ReAct-loki jää liian yleiseksi

Pyydä opiskelijaa nimeämään konkreettinen työkalu ja konkreettinen havainto.

- Mitä työkalua agentti kutsuu?
- Mitä dataa työkalu palauttaa?
- Miten tämä muuttaa agentin seuraavaa päätöstä?

### Jos ketjuajattelun vaiheet jäävät liian epämääräisiksi

Pyydä opiskelijaa kirjoittamaan jokainen vaihe verbinä:

- Tunnista ongelma.
- Tarkista sääntö.
- Hae tarvittava tieto.
- Valitse vaihtoehto.
- Lähetä vastaus.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että agentin päättelymalli on arkkitehtuuripäätös. ReAct tekee agentista joustavan, ketjuajattelu tekee siitä järjestelmällisen ja moniagenttirakenne mahdollistaa erikoistumisen. Mikään malli ei ole aina paras. Malli valitaan tehtävän mukaan.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Tarvitseeko oma agenttisi joustavaa tutkimista, vaiheittaista prosessia vai useamman erikoistuneen agentin yhteistyötä?

---
