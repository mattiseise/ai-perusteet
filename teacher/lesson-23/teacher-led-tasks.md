# Opettajavetoiset tehtävät — oppitunti 23

## Aktiviteetti 1: ReAct-malli noin 20 minuuttia

### Tavoite

Aktiviteetin tavoitteena on auttaa opiskelijoita ymmärtämään, miten **ReAct-malli** toimii agentin päätöksenteossa. ReAct tarkoittaa mallia, jossa agentti vuorottelee **päättelyn** ja **toiminnan** välillä: se arvioi tilanteen, tekee toiminnon, tarkastelee tulosta ja päättää seuraavan askeleen.

**Opettajan painotus:** Korosta, että ReAct ei tarkoita vain “ajattelua ääneen”. Sen ydin on, että agentti käyttää työkalua, havainnoi tuloksen ja muuttaa seuraavaa päätöstään havainnon perusteella.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> ReAct tulee sanoista **Reasoning** ja **Acting**. Suomeksi se tarkoittaa päättelyä ja toimintaa. Agentti ei vastaa heti arvaamalla, vaan se voi ensin päätellä, mitä tietoa tarvitaan, käyttää työkalua, tarkistaa tuloksen ja vasta sen jälkeen vastata käyttäjälle.

Kirjoita taululle:

Ajattele → toimi → havainnoi tulos → ajattele uudelleen → toimi uudelleen

### Esittely: tuotteen hinnan tarkistaminen

Näytä opiskelijoille yksinkertainen esimerkki. Asiakas kysyy:

`Mikä on tuotteen hinta?`

Näytä agentin eteneminen lokina:

```
[AJATTELU]: Asiakkaan kysymys koskee tuotteen hintaa. Minun täytyy hakea hinta tietokannasta.[TOIMINTA]: GET /api/product?id=12345[HAVAINTO]: Tietokanta palautti hinnan: 45 €.[AJATTELU]: Nyt tiedän tuotteen hinnan ja voin vastata asiakkaalle.[TOIMINTA]: Tuotteen hinta on 45 €.
```

Kysy opiskelijoilta:

- Miksi agentti ei vastannut heti?
- Mitä tietoa agentti tarvitsi ennen vastaamista?
- Miten työkalun käyttö teki vastauksesta luotettavamman?
- Mitä voisi mennä pieleen, jos agentti arvaa hinnan ilman tietokantaa?

**Esimerkki opetukseen**

Kysy opiskelijoilta, missä kohdassa agentti olisi voinut pysähtyä ja pyytää ihmiseltä apua. Hyvä vastaus on esimerkiksi tilanne, jossa tietokanta ei löydä tuotetta tai palauttaa ristiriitaisia hintoja.

### Ryhmätyö

Jaa opiskelijat pienryhmiin. Jokainen ryhmä valitsee yhden tilanteen ja kirjoittaa siihen **ReAct-prosessin** lokimuodossa.

**Mahdollisia tilanteita:**

- asiakas pyytää tuotteen palautusta,
- käyttäjä ilmoittaa teknisestä ongelmasta,
- opiskelija kysyy tehtävän palautuspäivää,
- asiakas kysyy, onko tilaus jo lähetetty,
- IT-tukipyyntö pitää ohjata oikealle asiantuntijalle.

**Ryhmän tehtävä:**

1. Kirjoittakaa käyttäjän kysymys tai ongelma.
2. Kirjoittakaa ensimmäinen **ajatteluvaihe**: mitä agentin pitää selvittää?
3. Kirjoittakaa ensimmäinen **toimintavaihe**: mitä työkalua agentti käyttää?
4. Kirjoittakaa **havainto**: mitä työkalu palauttaa tai mitä agentti saa selville?
5. Kirjoittakaa uusi **ajatteluvaihe**: mitä havainto tarkoittaa seuraavan päätöksen kannalta?
6. Kirjoittakaa lopullinen **toimintavaihe**: mitä agentti vastaa tai tekee?

| Vaihe | Ryhmän lokimerkintä |
| --- | --- |
| **[AJATTELU]** |  |
| **[TOIMINTA]** |  |
| **[HAVAINTO]** |  |
| **[AJATTELU]** |  |
| **[TOIMINTA]** |  |

**Esitys:**

Ryhmät esittelevät ReAct-prosessinsa lyhyesti. Keskustelkaa yhdessä:

- Miten jokainen ajatteluvaihe auttoi seuraavaa toimintaa?
- Missä kohdassa agentti tarvitsi ulkoista tietoa?
- Missä kohdassa agentin olisi pitänyt pyytää ihmiseltä apua?

**Opettajan tarkistuskysymys:** Jos ryhmä kirjoittaa vain lopullisen vastauksen, kysy: “Mistä agentti sai tiedon? Mitä se havaitsi ennen päätöstä?”

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että ReAct-mallissa agentti vuorottelee päättelyn, toiminnan ja havainnoinnin välillä.
- Opiskelijat osaavat kuvata yksinkertaisen ReAct-prosessin lokimuodossa.
- Opiskelijat ymmärtävät, miksi työkalujen käyttö tekee agentin vastauksesta luotettavamman kuin pelkkä arvaus.

---

## Aktiviteetti 2: Ketjuajattelu noin 20 minuuttia

### Tavoite

Aktiviteetin tavoitteena on auttaa opiskelijoita ymmärtämään, miten **ketjuajattelu** tukee järjestelmällistä ongelmanratkaisua. Ketjuajattelussa tehtävä jaetaan selkeisiin vaiheisiin, jotka suoritetaan oikeassa järjestyksessä.

**Opettajan painotus:** Ketjuajattelu sopii erityisesti prosesseihin, joissa vaiheet ovat tiedossa etukäteen. Se vähentää satunnaisuutta ja auttaa varmistamaan, ettei kriittisiä tarkistuksia ohiteta.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> Ketjuajattelu tarkoittaa sitä, että ongelma ratkaistaan vaihe vaiheelta. Sen sijaan, että agentti yrittäisi tehdä kaiken kerralla, se käy läpi ennalta määritellyn prosessin yksi kohta kerrallaan.

Kirjoita taululle:

Vaihe 1 → vaihe 2 → vaihe 3 → päätös → toiminto

### Esittely: palautuspyynnön käsittely

Näytä esimerkki palautuspyynnön käsittelystä:

1. **Mikä on pyyntö?** Asiakas haluaa palauttaa tuotteen.
2. **Onko palautusaika voimassa?** Tarkistetaan ostopäivä ja palautusehdot.
3. **Mitä käytäntö sanoo?** Tarkistetaan yrityksen palautuspolitiikka.
4. **Mikä on päätös?** Hyväksytään palautus, hylätään se tai pyydetään lisätietoja.

Kysy opiskelijoilta:

- Miksi vaiheet pitää tehdä tässä järjestyksessä?
- Mitä tapahtuisi, jos palautus hyväksyttäisiin ennen palautusajan tarkistamista?
- Mikä vaihe vaatii eniten tarkkuutta?

### Ryhmätyö

Opiskelijat valitsevat yhden prosessin ja kirjoittavat sen vaiheet oikeassa järjestyksessä.

**Mahdollisia prosesseja:**

- tilauksen käsittely,
- sairaalan ajanvaraus,
- IT-tukipyynnön käsittely,
- asiakaspalautteen käsittely,
- käyttäjätunnuksen luominen,
- laskun tarkistaminen.

**Ryhmän tehtävä:**

1. Valitkaa prosessi.
2. Kirjoittakaa kaikki vaiheet oikeassa järjestyksessä.
3. Merkitkää, missä vaiheessa tarvitaan tietoa järjestelmästä, käyttäjältä tai ihmisasiantuntijalta.
4. Merkitkää, mikä vaihe on turvallisuuden tai oikeellisuuden kannalta kriittisin.
5. Pohtikaa, mitä tapahtuu, jos jokin vaihe puuttuu.

| Vaihe | Mitä tarkistetaan? | Mistä tieto saadaan? | Mikä voi mennä pieleen? |
| --- | --- | --- | --- |
| 1. |  |  |  |
| 2. |  |  |  |
| 3. |  |  |  |

**Tärkeä keskustelukysymys:**

> Mitä menee pieleen, jos ketjusta puuttuu yksi vaihe?

**Mahdollisia vastauksia:**

- Asiakas saa väärän päätöksen.
- Agentti tekee toiminnon ilman lupaa.
- Tietoturvariski jää huomaamatta.
- Prosessi etenee väärään tilaan.
- Ihminen joutuu korjaamaan virheen myöhemmin.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että ketjuajattelu sopii prosesseihin, joissa vaiheet ovat selkeät ja toistuvat.
- Opiskelijat osaavat pilkkoa prosessin vaiheisiin.
- Opiskelijat ymmärtävät, että puuttuva tai väärässä järjestyksessä tehty vaihe voi johtaa virheisiin.

---

## Aktiviteetti 3: Mallin valinta noin 15 minuuttia

### Tavoite

Aktiviteetin tavoitteena on auttaa opiskelijoita valitsemaan, milloin kannattaa käyttää **ReAct-mallia** ja milloin **ketjuajattelua**. Opiskelijat ymmärtävät, että eri ongelmat tarvitsevat erilaisia päättelymalleja.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> ReAct on joustava malli tilanteisiin, joissa agentti ei vielä tiedä, mitä tietoa tarvitaan seuraavaksi. Ketjuajattelu taas sopii tilanteisiin, joissa prosessin vaiheet ovat selkeät ja toistuvat samalla tavalla.

| Malli | Sopii parhaiten | Esimerkki |
| --- | --- | --- |
| **ReAct** | Tutkiviin ja vaihteleviin tilanteisiin, joissa agentti käyttää työkaluja päätöksen aikana. | Teknisen ongelman selvittäminen lokien ja tietokannan avulla. |
| **Ketjuajattelu** | Selkeisiin prosesseihin, joissa vaiheet ovat tiedossa etukäteen. | Palautuspyynnön käsittely palautusehtojen mukaan. |

### Ryhmätyö

Anna opiskelijoille neljä tilannetta. Ryhmät päättävät, kumpi malli sopii paremmin: **ReAct** vai **ketjuajattelu**. Heidän pitää myös perustella valintansa.

| Tilanne | Sopiva malli | Perustelu |
| --- | --- | --- |
| Agentti selvittää, miksi palvelin kaatuu satunnaisesti. |  |  |
| Agentti käsittelee tuotteen palautuspyynnön yrityksen palautusehtojen mukaan. |  |  |
| Agentti etsii asiakkaan tilauksen tilan ja vastaa asiakkaalle. |  |  |
| Agentti tutkii tietoturvahälytystä, jonka syy ei ole vielä tiedossa. |  |  |

**Odotetut vastaukset:**

- **Palvelimen satunnainen kaatuminen:** ReAct, koska agentin täytyy tutkia, hakea lisätietoa ja muuttaa etenemistä löydösten perusteella.
- **Palautuspyyntö:** ketjuajattelu, koska vaiheistus on selkeä ja perustuu palautusehtoihin.
- **Tilauksen tilan tarkistus:** usein ReAct tai yksinkertainen työkalukutsu. Jos prosessi on täysin vakioitu, ketjuajattelu voi riittää.
- **Tietoturvahälytys:** ReAct, koska agentin pitää tutkia eri lähteitä ja tehdä päätöksiä havaintojen perusteella.

**Opettajan tarkistuskysymys:** Jos opiskelijat valitsevat aina ReActin, kysy: “Onko tässä oikeasti tarvetta iteroida, vai riittääkö vakioitu vaiheistus?”

**Keskustelu:**

- Voiko sama tehtävä joskus hyötyä molemmista malleista?
- Milloin ReAct on liian monimutkainen?
- Milloin ketjuajattelu on liian jäykkä?

### Odotettu oppimistulos

- Opiskelijat osaavat erottaa ReAct-mallin ja ketjuajattelun käyttötarkoitukset.
- Opiskelijat osaavat valita tehtävään sopivan päättelymallin.
- Opiskelijat ymmärtävät, että mallin valinta vaikuttaa agentin turvallisuuteen, joustavuuteen ja luotettavuuteen.

---

## Aktiviteetti 4: Moniagenttijärjestelmä noin 20 minuuttia

### Tavoite

Aktiviteetin tavoitteena on esitellä **moniagenttijärjestelmä**, jossa useat agentit tekevät yhteistyötä. Opiskelijat ymmärtävät, että eri agenteilla voi olla eri roolit ja että järjestelmä tarvitsee selkeän työnjaon, tiedonkulun ja vastuun.

**Opettajan painotus:** Moniagenttijärjestelmä ei ole automaattisesti parempi kuin yksi agentti. Se kannattaa vain silloin, kun työnjako tekee järjestelmästä selkeämmän, turvallisemman tai helpommin valvottavan.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> Moniagenttijärjestelmässä yksi agentti ei tee kaikkea. Sen sijaan useat agentit tekevät eri osia tehtävästä. Yksi voi analysoida viestin, toinen hakea tietoa, kolmas kirjoittaa vastauksen ja neljäs tarkistaa laadun tai turvallisuuden.

### Esittely: asiakaspalvelupyynnön käsittely moniagenttijärjestelmänä

**Moniagenttijärjestelmän esimerkkityönkulku**

|  |
| --- |
| **1. Analyysiagentti** Lukee asiakkaan viestin ja tunnistaa aiheen sekä kiireellisyyden. |
| ↓ |
| **2. Hakuagentti** Hakee asiakkaan historian, aiemmat tiketit ja asiaan liittyvät ohjeet. |
| ↓ |
| **3. Kirjoitusagentti** Laatii vastausehdotuksen asiakkaalle. |
| ↓ |
| **4. Validointiagentti** Tarkistaa, että vastaus on oikea, turvallinen, kohtelias ja organisaation ohjeiden mukainen. |

Kysy opiskelijoilta:

- Miksi yksi agentti ei välttämättä ole paras ratkaisu kaikkeen?
- Mikä agentti tekee tärkeimmän päätöksen?
- Mitä tapahtuu, jos validointiagentti puuttuu?
- Miten tieto kulkee agentilta toiselle?

### Ryhmätyö

Opiskelijat suunnittelevat moniagenttijärjestelmän valitsemalleen tehtävälle.

**Mahdollisia tehtäviä:**

- asiakaspalvelupyyntöjen käsittely,
- tietoturvahälytysten analysointi,
- opiskelijan projektisuunnitelman arviointi,
- verkkokaupan palautusten käsittely,
- IT-tikettien priorisointi.

**Ryhmän tehtävä:**

1. Päättäkää, kuinka monta agenttia järjestelmässä tarvitaan.
2. Nimetkää jokaisen agentin rooli.
3. Päättäkää, onko järjestelmässä **johtaja-agentti** vai toimivatko agentit tasavertaisesti.
4. Kuvatkaa, miten tieto kulkee agentilta toiselle.
5. Merkitkää, missä kohdassa ihminen tarkistaa tai hyväksyy päätöksen.

| Agentti | Rooli | Mitä tietoa se saa? | Mitä se tuottaa seuraavalle vaiheelle? |
| --- | --- | --- | --- |
| Agentti 1 |  |  |  |
| Agentti 2 |  |  |  |

**Esitys:**

Ryhmät piirtävät kaavion ja esittelevät sen luokalle.

Kaaviossa tulee näkyä:

- agenttien nimet ja roolit,
- tiedon kulkusuunta,
- päätöksentekokohta,
- ihmisen tarkistusvaihe,
- mahdollinen johtaja-agentti.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, mitä moniagenttijärjestelmä tarkoittaa.
- Opiskelijat osaavat jakaa laajan tehtävän usean agentin rooleihin.
- Opiskelijat ymmärtävät, että moniagenttijärjestelmä tarvitsee selkeän työnjaon, tiedonkulun ja valvonnan.

---

## Herättävät keskustelukysymykset

- **Mitä tapahtuu, jos ReAct-prosessi iteroi liian kauan?**
- **Voiko ketjuajattelu epäonnistua, vaikka kaikki vaiheet olisi kirjoitettu valmiiksi?**
- **Milloin moniagenttijärjestelmä on liian monimutkainen eli overkill?**
- **Mitä riskejä syntyy, jos useat agentit tekevät päätöksiä ilman yhteistä valvontaa?**
- **Milloin ihmisen pitää ottaa päätös haltuun?**

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- selittää, mitä **ReAct-malli** tarkoittaa ja miten se etenee,
- kuvata yksinkertainen ReAct-prosessi ajattelun, toiminnan ja havainnoinnin vaiheina,
- selittää, mitä **ketjuajattelu** tarkoittaa ja millaisiin prosesseihin se sopii,
- valita sopiva päättelymalli erilaisiin tilanteisiin,
- suunnitella yksinkertainen **moniagenttijärjestelmä**,
- perustella, miten agenttien työnjako, tiedonkulku ja ihmisen valvonta toteutuvat.

---
