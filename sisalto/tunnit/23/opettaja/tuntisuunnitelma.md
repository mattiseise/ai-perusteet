# Opettajan materiaalit — oppitunti 23

## Osaamistavoitteet

Tämän oppitunnin tavoitteena on, että opiskelija ymmärtää, miten **suunnittelumallit** ohjaavat agentin päättelyä ja toimintaa. Oppitunnin ydin on ReActin ja eksplisiittisen työnkulun ero. Moniagenttijärjestelmät ovat valinnainen syvennys. Mallin sisäistä päättelyä ei pyydetä eikä tallenneta.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, mitä **ReAct** tarkoittaa: agentti vuorottelee päättelyn ja toiminnan välillä.
- Opiskelija ymmärtää, mitä **eksplisiittinen työnkulku** tarkoittaa: agentti etenee vaihe vaiheelta järjestyksessä.
- Opiskelija tunnistaa, että ReAct ja eksplisiittinen työnkulku sopivat erilaisiin tehtäviin.
- Opiskelija ymmärtää, että ReAct-kierros ja eksplisiittinen työnkulku ovat agentin ohjauskehyksen ohjaamia rakenteita, eivät vain mallin sisäistä toimintaa.

### Soveltaa ja analysoida

- Opiskelija osaa valita, sopiiko tiettyyn tehtävään paremmin ReAct vai eksplisiittinen työnkulku.
- Opiskelija osaa kuvata havaittavan työnkulun ja lokin: lyhyt päätösperustelu, rakenteinen työkalukutsu, tulos tai virhe ja toiminto.
- Opiskelija osaa tunnistaa tilanteita, joissa ReAct voi jäädä kiertämään silmukkaa tai eksplisiittinen työnkulku voi olla liian jäykkä.

### Luoda ja arvioida

- Opiskelija osaa suunnitella oman agenttinsa **päättelymallin**.
- Opiskelija osaa perustella, miksi valittu malli sopii omaan agenttiongelmaan.
- Opiskelija osaa nimetä eksplisiittisestä työnkulusta vaiheen, jossa kielimalli tekee aidon rajatun valinnan vähintään kahdesta sallitusta vaihtoehdosta.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että agentin päättelyä täytyy ohjata. Hyvä agentti ei hypi sattumanvaraisesti työkalusta toiseen, vaan noudattaa tehtävään sopivaa päättelymallia.

---

## Pedagoginen lähestymistapa

### Ydinviesti: suunnittelumallit opettavat agentille, miten toimia

Suunnittelumallit auttavat opiskelijaa muuttamaan agentin toiminnan näkyväksi ja testattavaksi. Havaittavat työkalukutsut, tulokset, virheet ja toiminnot voidaan jäsentää toimintamalleiksi ilman mallin piilotetun ajatusketjun tallentamista.

Tunnin kaksi keskeistä mallia ovat:

- **ReAct:** joustava ja iteratiivinen malli, jossa agentti kutsuu työkalua, havainnoi tuloksen tai virheen ja valitsee seuraavan toiminnon.
- **Eksplisiittinen työnkulku:** systemaattinen malli, jossa agentti jakaa tehtävän vaiheisiin ja etenee järjestyksessä.

> **Hyvä päättelymalli tekee agentin toiminnasta ennakoitavampaa, jäljitettävämpää ja helpommin korjattavaa.**

### ReAct — kutsu työkalua, tarkista tulos ja jatka

**ReAct** tarkoittaa päättelyn ja toiminnan vuorottelua. Agentti ei tee kaikkea yhdellä kertaa, vaan etenee rajatussa silmukassa: se valitsee työkalun, saa tuloksen tai virheen ja päättää seuraavan toiminnon. Valinnasta voidaan tallentaa lyhyt päätösperustelu, mutta ei mallin sisäistä päättelyä.

ReAct-toteutuksen havaittava kierros:

1. **Lyhyt päätösperustelu:** Mitä tietoa tai toimintoa tarvitaan seuraavaksi?
2. **Rakenteinen työkalukutsu:** Työkalun nimi ja vain tarvittavat parametrit.
3. **Tulos tai virhe:** Mitä työkalu palautti?
4. **Seuraava toiminto:** Jatka, vastaa, keskeytä tai eskaloi.

**Esimerkki opetukseen**

Anna opiskelijoille tehtävä: ”Asiakas kysyy, onko tuotetta varastossa.” Pyydä heitä kirjoittamaan havaittava loki: lyhyt päätösperustelu, rakenteinen varastohaku, palautettu tulos tai virhe ja lähetetty vastaus. Sano ääneen, ettei tehtävässä kirjoiteta mallin sisäistä ajatusketjua.

ReAct on hyödyllinen silloin, kun agentti ei tiedä etukäteen kaikkia vaiheita. Se voi edetä havaintojen perusteella ja muuttaa suuntaa, jos ensimmäinen toimenpide ei auta.

| ReAct-vaihe | Mitä agentti tekee? | Esimerkki |
| --- | --- | --- |
| **Päätösperustelu** | Kertoo lyhyesti, miksi kutsu tarvitaan. | ”Ajantasainen saldo vaatii varastohaun.” |
| **Työkalukutsu** | Kirjaa työkalun ja rakenteiset parametrit. | `hae_varastosaldo({"tuote_id":"123"})` |
| **Tulos tai virhe** | Tallentaa työkalun palauttaman havainnon. | `{"saldo":5}` |
| **Toiminto** | Kirjaa, vastataanko, jatketaanko vai eskaloidaanko. | ”Lähetä asiakkaalle saldo 5.” |

### Eksplisiittinen työnkulku — vaihe vaiheelta etenevä malli

**Eksplisiittisessä työnkulussa** agentti jakaa ongelman selkeisiin vaiheisiin ja käsittelee ne järjestyksessä. Tämä sopii tilanteisiin, joissa prosessi on melko ennakoitava ja jokainen vaihe riippuu edellisestä.

**1. Ongelma:** Mitä asiakas kysyy?

**2. Rajoitteet:** Mitä sääntöjä tai ehtoja pitää noudattaa?

**3. Valinnat:** Mitä vaihtoehtoja on?

**4. Päätös:** Mikä vaihtoehto valitaan ja miksi?

Eksplisiittinen työnkulku on hyödyllinen esimerkiksi palautuspyynnön käsittelyssä. Agentti tarkistaa ensin palautusajan, sitten palautuskäytännön, sitten asiakkaan oikeuden palautukseen ja vasta lopuksi muodostaa vastauksen.

> **Tärkeää:** Eksplisiittisessä työnkulussa ei hypitä vaiheiden yli. Jokainen vaihe rakentuu edellisen päälle.

### Valinnainen syvennys: moniagenttijärjestelmät — jaettu vastuu

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

### Väärinkäsitys 2: ”Eksplisiittinen työnkulku on huono, koska se on jäykkä.”

**Korjaava näkökulma:** Eksplisiittisen työnkulun jäykkyys on sen vahvuus silloin, kun prosessin pitää olla ennakoitava. Esimerkiksi palautuksen, laskun tarkistuksen tai hyväksyntäprosessin pitää usein edetä tietyssä järjestyksessä.

### Väärinkäsitys 3: ”Suunnittelumalli on vain tekninen toteutustapa.”

**Korjaava näkökulma:** Suunnittelumalli on myös pedagoginen ja arkkitehtoninen valinta. Se vaikuttaa siihen, miten agenttia testataan, miten sitä selitetään ja miten sen virheitä korjataan.

### Väärinkäsitys 4: ”ReAct tapahtuu pelkästään promptissa tai kielimallissa.”

**Korjaava näkökulma:** Malli voi valita seuraavan toiminnon, mutta agentin ohjauskehys ylläpitää kierrosta, välittää ja tarkistaa työkalukutsut, palauttaa havainnot, asettaa iteraatiorajan, käsittelee virheet ja lokittaa tapahtumat. Ilman tätä ohjausta ReAct ei ole hallittu työnkulku.

---

## Luokkatehtävien ohjeistus

### TT-A: havaittavan ReAct-lokin kirjoittaminen

**Tavoite:** Opiskelija ymmärtää ReAct-toteutuksen työkalukutsu–tulos–toiminto-silmukan.

**Tehtävä:** Anna opiskelijoille lyhyt asiakastilanne ja pyydä heitä kirjoittamaan havaittava ReAct-loki. Lokissa näkyvät lyhyt päätösperustelu, työkalun nimi ja tarvittava tieto, tulos tai virhe sekä seuraava toiminto. Mallin sisäistä päättelyä ei kirjoiteta.

| Vaihe | Opiskelijan vastaus |
| --- | --- |
| **Lyhyt päätösperustelu** | Miksi tietoa tai toimintoa tarvitaan? |
| **Rakenteinen työkalukutsu** | Mitä työkalua käytetään ja millä parametreilla? |
| **Tulos tai virhe** | Mitä työkalu palauttaa? |
| **Toiminto** | Vastataanko, jatketaanko, keskeytetäänkö vai eskaloidaanko? |

**Aika-arvio:** 15–20 minuuttia

---

### TT-B: Eksplisiittisen työnkulun vaiheistus

**Tavoite:** Opiskelija osaa purkaa monimutkaisen tehtävän selkeiksi vaiheiksi.

**Tehtävä:** Anna opiskelijoille tehtävä, esimerkiksi palautuspyynnön käsittely, laskun tarkistaminen tai tukipyynnön luokittelu. Opiskelijat kirjoittavat tehtävän 4–6 vaiheeksi.

**Ohje opiskelijalle:**

1. Mikä ongelma pitää ratkaista?
2. Mitä tietoa tarvitaan ensin?
3. Mitä sääntöjä tai rajoitteita pitää tarkistaa?
4. Mitä vaihtoehtoja on?
5. Mikä päätös tehdään?
6. Mitä agentti tekee päätöksen jälkeen?

Lisäksi opiskelija nimeää yhden vaiheen, jossa kielimalli tekee aidon rajatun valinnan vähintään kahdesta sallitusta vaihtoehdosta. Lokinäytössä pitää näkyä syöte, sallitut vaihtoehdot, mallin valinta ja sitä seuraava ennalta määritelty haara. Pelkkä kiinteä jos–niin-ehto ei täytä tätä kohtaa.

**Aika-arvio:** 15–20 minuuttia

---

### TT-C: Suunnittelumallin valinta

**Tavoite:** Opiskelija osaa valita tehtävään sopivan päättelymallin ja perustella valintansa.

**Tehtävä:** Anna opiskelijoille 3–4 eri tilannetta. He valitsevat jokaiseen ReActin tai eksplisiittisen työnkulun ja perustelevat valintansa.

| Tilanne | Sopiva malli | Perustelu |
| --- | --- | --- |
| Agentti tutkii, miksi tilauksia katoaa satunnaisesti matkalla. | ReAct | Agentti tarvitsee havaintoihin perustuvaa etenemistä ja voi vaihtaa suuntaa tulosten mukaan. |
| Agentti käsittelee palautuspyynnön. | Eksplisiittinen työnkulku | Prosessi etenee selkeissä vaiheissa: tarkista aika, tarkista ehdot, tee päätös ja vastaa. |

**Aika-arvio:** 20–25 minuuttia

---

### Valinnainen TT-D: Moniagenttikaavion piirtäminen

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

## Oppimisen tarkistuskysymykset

1. **ReAct:** Miksi ReAct-mallissa agentti ei tee kaikkia toimintoja heti kerralla?
2. **Eksplisiittinen työnkulku:** Millaisiin tehtäviin vaiheittainen eteneminen sopii parhaiten?
3. **Valinta:** Mistä tiedät, että tehtävä tarvitsee ReActin eikä pelkkää eksplisiittistä työnkulkua?
4. **Rajattu mallivalinta:** Missä eksplisiittisen työnkulun vaiheessa kielimalli valitsee vähintään kahdesta sallitusta vaihtoehdosta?
5. **Rajoitukset:** Miksi ReAct-agentille kannattaa asettaa enimmäismäärä iteraatioita?

---

## Opettajan vihjeet

### Jos opiskelija sekoittaa ReActin ja eksplisiittisen työnkulun

Käytä seuraavaa erottelua:

- **ReAct:** agentti päättää seuraavan askeleen havaintojen perusteella.
- **Eksplisiittinen työnkulku:** agentti etenee ennalta määriteltyjen vaiheiden mukaan.

> ReAct sopii tutkimiseen. Eksplisiittinen työnkulku sopii prosessiin.

### Valinnaisen syvennyksen tuki: jos opiskelija haluaa tehdä heti moniagenttijärjestelmän

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

### Jos eksplisiittisen työnkulun vaiheet jäävät liian epämääräisiksi

Pyydä opiskelijaa kirjoittamaan jokainen vaihe verbinä:

- Tunnista ongelma.
- Tarkista sääntö.
- Hae tarvittava tieto.
- Valitse vaihtoehto.
- Lähetä vastaus.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että agentin päättelymalli on arkkitehtuuripäätös. ReAct tukee havaintojen perusteella muuttuvaa etenemistä, kun taas eksplisiittinen työnkulku tekee ennalta tunnetusta prosessista järjestelmällisen. Kumpikaan ei ole aina paras, vaan malli valitaan tehtävän mukaan.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Tarvitseeko oma agenttisi joustavaa tutkimista vai ennalta rajattua vaiheittaista prosessia?

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **työnkulkujälki: kutsut, tulokset, toiminnot, virheet ja lyhyet perustelut**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–10 min | Virittäytyminen | Kytke ydinkysymys tuttuun tilanteeseen ja tarkista lähtötaso. |
| 10–25 min | Ydinkäsite | Mallinna tunnin keskeinen ero yhdellä vastaesimerkillä. |
| 25–65 min | Perustuotos | Oppija rakentaa nelivaiheisen suoritusjäljen työkalukutsuineen, tuloksineen ja lyhyine perusteluineen. Tämä 40 minuutin jakso on itsenäistä tai parin kanssa tehtävää työskentelyä. |
| 65–80 min | Testaus ja purku | Testauta tuotos annetulla tapauksella ja pura yksi onnistuminen sekä yksi korjaus. |
| 80–90 min | Tallennus ja lopputehtävä | Varmista tiedoston nimi, tallennuspaikka ja yhden lauseen johtopäätös. |

### Tukireitti

Oppija järjestää annetut vaihe- ja lokikortit. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis ja aikaa jää, oppija voi tarkastella moniagenttirakennetta erillisenä valinnaisena sivupolkuna. Syventävää työtä ei arvioida osana pakollista ydintuotosta.
