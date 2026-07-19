# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

Tämän lohkon tavoitteena on, että opiskelija ymmärtää, miten **kielimalli** toimii perusperiaatteeltaan ja miksi se voi tuottaa sekä hyödyllisiä että virheellisiä vastauksia. Oppitunnin ydin on **next-token prediction**: kielimalli ennustaa seuraavaa tokenia todennäköisyyksien perusteella.

### Muistaa ja ymmärtää

- Opiskelija osaa selittää, että kielimalli toimii ennustamalla seuraavaa tokenia.
- Opiskelija ymmärtää, että **parametrit** ovat mallin oppimia numeerisia painoja, eivät käsin kirjoitettuja sääntöjä.
- Opiskelija ymmärtää, että kielimalli ei hae vastausta suoraan tietokannasta, vaan muodostaa vastauksen opittujen todennäköisyyksien perusteella.
- Opiskelija tunnistaa **hallusinaation** tilanteena, jossa malli tuottaa vakuuttavan mutta virheellisen vastauksen.

### Soveltaa ja analysoida

- Opiskelija osaa selittää, miksi hallusinaatiot ovat mahdollisia kielimallin toimintaperiaatteen vuoksi.
- Opiskelija osaa arvioida, millaisissa tilanteissa kielimallin vastaukset pitää tarkistaa erityisen huolellisesti.
- Opiskelija osaa kuvata yhteyden **koulutusdatan**, parametrien ja mallin käyttäytymisen välillä.

### Luoda ja arvioida

- Opiskelija osaa arvioida kielimallin vastausta kriittisesti eikä oleta sen olevan automaattisesti totta.
- Opiskelija osaa ehdottaa keinoja hallusinaatioiden vähentämiseen, kuten vastausten tarkistamista, lähteiden käyttöä ja matalampaa lämpötilaa kriittisissä tehtävissä.
- Opiskelija osaa liittää kielimallien toimintaperiaatteen omaan tulevaan ammattialaansa ja sen riskeihin.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että kielimalli ei “tiedä” samalla tavalla kuin ihminen. Se ennustaa seuraavaa tokenia opittujen todennäköisyyksien perusteella. Juuri tämä tekee siitä hyödyllisen mutta myös epäluotettavan tilanteissa, joissa faktatarkkuus on kriittistä.

---

## Pedagoginen lähestymistapa

### Ydinviesti: kielimalli ennustaa seuraavaa tokenia

Kielimallin toimintaa kannattaa havainnollistaa ensin käytännön esimerkillä. Pyydä opiskelijoita jatkamaan lauseita, kuten ”Kissa istui...” tai ”Salasana pitää vaihtaa, jos...”. Opiskelijat huomaavat nopeasti, että he ennustavat seuraavia sanoja aiemman kielenkäytön ja tilanteen perusteella. Kielimalli tekee jotakin samankaltaista, mutta matemaattisesti ja valtavan datamäärän pohjalta.

> **Kielimalli ei hae valmista vastausta. Se muodostaa todennäköisen jatkon.**

Korosta opiskelijoille:

- **Token** voi olla sana, sanan osa, merkki tai merkkijono.
- **Next-token prediction** tarkoittaa seuraavan tokenin ennustamista aiemman tekstin perusteella.
- **Parametrit** ovat mallin oppimia numeroita, jotka vaikuttavat siihen, mikä jatko näyttää todennäköiseltä.
- Malli voi kuulostaa ymmärtävältä, koska sen koulutusdata on sisältänyt paljon ihmisten kirjoittamaa järkevää tekstiä.

### Parametrit eivät ole sääntöjä

Opiskelijoille voi olla vaikeaa ymmärtää, että parametrit eivät ole yksittäisiä sääntöjä, kuten ”jos käyttäjä kysyy X, vastaa Y”. Parametrit ovat numeerisia painoja, jotka yhdessä ohjaavat mallin käyttäytymistä.

| Käsite | Mitä se ei ole? | Mitä se on? |
| --- | --- | --- |
| **Sääntö** | Ei sama asia kuin mallin parametri. | Ihmisen kirjoittama ehto, esimerkiksi ”jos viestissä lukee lasku, siirrä se kansioon Laskut”. |
| **Parametri** | Ei yksittäinen luettava ohje tai sääntö. | Mallin oppima numeroarvo, joka vaikuttaa todennäköisyyksiin yhdessä muiden parametrien kanssa. |

**Opettajan huomio:** Hyvä vertaus on mikseri tai äänipöytä: yksi säädin ei yksin “sisällä” kappaletta, mutta tuhansien säätimien yhdistelmä vaikuttaa lopputulokseen. Parametrit toimivat samantyyppisesti: ne eivät ole lauseita vaan painoja.

### Hallusinaatiot syntyvät uskottavasta ennustamisesta

**Hallusinaatio** tarkoittaa, että malli tuottaa vastauksen, joka kuulostaa uskottavalta mutta on väärä, keksitty tai tarkistamaton. Tämä ei ole tahallista valehtelua. Malli ei tiedä, mikä on totta samalla tavalla kuin ihminen. Se jatkaa tekstiä tavalla, joka näyttää tilastollisesti sopivalta.

Hallusinaatio on erityisen vaarallinen, koska se voi näyttää oikealta. Kielimalli voi antaa väärän lähteen, keksiä henkilön, muistaa lakipykälän väärin tai antaa ohjelmointiohjeen, joka näyttää järkevältä mutta ei toimi.

> **Hallusinaatio ei välttämättä näytä virheeltä. Siksi se pitää tarkistaa.**

Hallusinaatioita voi vähentää, mutta niitä ei voi poistaa täysin. Keinoja ovat esimerkiksi:

- vastausten tarkistaminen luotettavista lähteistä
- kielimallin ankkurointi annettuun tietopohjaan
- matalamman lämpötilan käyttäminen kriittisissä tehtävissä
- ihmisen tarkistus ennen riskialttiita päätöksiä
- työkalujen käyttö, kuten haku, tietokanta tai laskin, kun tarvitaan tarkkaa tietoa

### Lämpötila ei ole mielentila

**Lämpötila** on matemaattinen asetus, joka vaikuttaa siihen, kuinka paljon satunnaisuutta mallin vastauksessa on. Matala lämpötila tekee vastauksesta yleensä ennakoitavamman. Korkeampi lämpötila voi tehdä vastauksesta vaihtelevamman ja luovemman, mutta myös riskialttiimman faktatehtävissä.

| Lämpötila | Mitä se tekee? | Milloin hyödyllinen? |
| --- | --- | --- |
| **Matala** | Vähentää vaihtelua ja tekee vastauksista ennakoitavampia. | Faktapainotteiset, tekniset ja kriittiset tehtävät. |
| **Korkea** | Lisää vaihtelua, luovuutta ja yllätyksellisyyttä. | Ideointi, luova kirjoittaminen ja vaihtoehtoisten näkökulmien tuottaminen. |

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”Kielimalli ymmärtää tekstiä.”

**Korjaava näkökulma:** Kielimalli ennustaa seuraavaa tokenia todennäköisyyksien perusteella. Se voi näyttää ymmärtävän, koska se on oppinut valtavasti kielen ja tekstien rakenteita koulutusdatasta. Tämä ei kuitenkaan tarkoita ihmisen kaltaista ymmärrystä.

> Malli näyttää ymmärtävän, koska se osaa tuottaa ymmärtävältä näyttävää tekstiä.

### Väärinkäsitys 2: ”Parametrit ovat sääntöjä, jotka malli oppi.”

**Korjaava näkökulma:** Parametrit ovat numeroita eli painoja. Ne eivät ole erillisiä luettavia sääntöjä. Miljardit parametrit yhdessä vaikuttavat siihen, millainen vastaus mallista syntyy.

### Väärinkäsitys 3: ”Jos malli hallusinoi, se valehtelee tarkoituksella.”

**Korjaava näkökulma:** Malli ei valehtele tarkoituksella, koska sillä ei ole tietoisuutta tai aikomusta. Se tuottaa väärän vastauksen, koska se ennustaa uskottavan jatkon väärin.

### Väärinkäsitys 4: ”Suurempi malli on aina parempi.”

**Korjaava näkökulma:** Suurempi malli voi olla kyvykkäämpi, mutta koko ei yksin ratkaise laatua. Koulutusdata, hienosäätö, käyttötapa, tehtävän rajaus ja turvallisuusratkaisut vaikuttavat paljon.

### Väärinkäsitys 5: ”Lämpötila kuvaa mallin mielentilaa.”

**Korjaava näkökulma:** Lämpötila ei ole mielentila vaan matemaattinen asetus. Se ohjaa satunnaisuutta siinä, miten seuraava token valitaan mahdollisten vaihtoehtojen joukosta.

---

## Opettajan fasilitointiohjeet

### Ennen luokkaa

- Testaa etukäteen yksinkertainen live-demo, jossa opiskelijat jatkavat lauseita ja vertaavat omaa arvaamistaan kielimallin vastaukseen.
- Valmistele yksi turvallinen hallusinaatioesimerkki, jonka voi tarkistaa nopeasti luotettavasta lähteestä.
- Varmista, että osaat selittää **next-token prediction** -periaatteen yksinkertaisesti ilman liian teknistä matematiikkaa.
- Tutustu yleisellä tasolla transformerien ja attention-mekanismin ideaan, mutta pidä oppitunnin pääpaino ennustamisessa, parametreissa ja hallusinaatioissa.

### Luokan aikana

- **Aloita käytännöstä.** Anna opiskelijoiden ennustaa seuraava sana ennen teoriaa.
- **Näytä hallusinaatio konkreettisesti.** Keskustelkaa siitä, miksi virhe näyttää uskottavalta.
- **Yhdistä asialliseen käyttöön.** Kysy: ”Mitä tapahtuu, jos tällainen virhe päätyy asiakasviestiin, koodiin tai tietoturvaohjeeseen?”
- **Pidä ero selkeänä:** malli ei tiedä, vaan ennustaa. Tämä ero on tärkeä myöhemmissä tekoälyn turvallisuutta ja agentteja käsittelevissä osioissa.

### Yleisten opiskelijakysymysten vastaukset

**Kysymys: ”Jos malli vain arvaa sanoja, miten se osaa vastata monimutkaisiin kysymyksiin?”**
Vastaus: Se on hyvä kysymys. Malli on nähnyt koulutusdatassa valtavasti monimutkaisia kysymyksiä, vastauksia, selityksiä ja ongelmanratkaisun esimerkkejä. Se oppii näistä kuvioita. Siksi se voi tuottaa hyvin monimutkaiselta näyttävän vastauksen, vaikka perusmekanismi on seuraavan tokenin ennustaminen.

**Kysymys: ”Voiko hallusinaatiot poistaa?”**
Vastaus: Ei täysin. Niitä voi kuitenkin vähentää tarkistamalla vastauksia, käyttämällä luotettavia lähteitä, ankkuroimalla mallin tietopohjaan, käyttämällä matalampaa lämpötilaa ja lisäämällä ihmisen tarkistus kriittisiin tehtäviin.

**Kysymys: ”Kuinka monta parametria ihmisen aivoissa on?”**
Vastaus: Tätä ei voi verrata suoraan. Ihmisen aivot eivät ole kielimallin kaltainen parametrijoukko, vaan biologinen, dynaaminen ja kehon kanssa yhteydessä oleva järjestelmä. Mallin parametrit ja aivojen toiminta ovat eri asioita.

---

## Luokkatehtävien ohjeistus

### TT-A: Seuraavan tokenin ennustaminen

**Tavoite:** Opiskelija ymmärtää seuraavan tokenin ennustamisen periaatteen käytännön esimerkin avulla.

**Tehtävä:** Kirjoita taululle lauseen alkuja ja pyydä opiskelijoita ehdottamaan seuraavaa sanaa. Keskustelkaa, miksi tietyt sanat tuntuvat todennäköisiltä.

| Lauseen alku | Todennäköisiä jatkoja | Miksi? |
| --- | --- | --- |
| ”Kissa istui...” | matolla, tuolilla, ikkunalla | Nämä ovat tuttuja ja kielellisesti todennäköisiä jatkoja. |
| ”Salasana pitää vaihtaa, jos...” | se on vuotanut, epäilet väärinkäyttöä, se on liian heikko | Tietoturvakonteksti ohjaa todennäköisiä jatkoja. |

**Aika-arvio:** 10–15 minuuttia

---

### TT-B: Hallusinaation tunnistaminen

**Tavoite:** Opiskelija oppii tarkistamaan kielimallin väitteitä eikä luota pelkkään vakuuttavaan muotoon.

**Tehtävä:** Näytä opiskelijoille tekoälyn tuottama lyhyt vastaus, jossa on yksi keksitty tai virheellinen fakta. Pyydä opiskelijoita tunnistamaan, mikä väite pitää tarkistaa ja miten se tarkistettaisiin.

**Ohje opiskelijalle:**

1. Mikä väite kuulostaa faktalta?
2. Mistä sen voisi tarkistaa?
3. Mitä tapahtuu, jos väite hyväksytään ilman tarkistusta?
4. Miten voisit muotoilla vastauksen turvallisemmin?

**Aika-arvio:** 15–20 minuuttia

---

### TT-C: Lämpötila ja käyttötarkoitus

**Tavoite:** Opiskelija ymmärtää, että lämpötila vaikuttaa vastausten vaihteluun eikä mallin “mielentilaan”.

**Tehtävä:** Anna opiskelijoille kolme käyttötapausta ja pyydä heitä valitsemaan, olisiko matalampi vai korkeampi lämpötila järkevämpi.

| Käyttötapaus | Sopiva lämpötila | Perustelu |
| --- | --- | --- |
| Tietoturvaohjeen tarkka tiivistelmä | Matala | Tarvitaan ennakoitava ja tarkka vastaus. |
| Ideoita pelihahmon nimeksi | Korkeampi | Luovuus ja vaihtelu ovat hyödyllisiä. |
| Asiakkaalle lähetettävä laskutustieto | Matala | Virheellinen tieto voi aiheuttaa taloudellista haittaa. |

**Aika-arvio:** 10–15 minuuttia

---

## Formatiivinen tarkistuspiste — todistusaineisto 1

### Tavoite

Opiskelija prosessoi oppitunnin ydinkäsitteet omin sanoin. Todistusaineisto toimii sekä **formatiivisena arviointina** että rakennuspalikkana Teoria-osion arviointitehtävälle.

### Tehtävänanto opiskelijalle

Kirjoita lyhyt vastaus, jossa selität omin sanoin:

1. Miten kielimalli tuottaa vastauksen?
2. Mitä tarkoittaa **next-token prediction**?
3. Miksi kielimalli voi hallusinoida?
4. Miksi mallin vastausta ei pidä aina hyväksyä ilman tarkistusta?

**Valmis vastaus:** noin 150–250 sanaa.

### Mitä etsiä palautuksesta?

- **Ydinajatus ymmärretty:** opiskelija selittää, että malli ennustaa seuraavaa tokenia todennäköisyyksien perusteella eikä “ymmärrä” tai “tiedä” samalla tavalla kuin ihminen.
- **Yleinen väärinymmärrys:** opiskelija kirjoittaa, että malli hakee vastauksen tietokannasta tai tietää faktat. Ohjaa tällöin takaisin tilastolliseen ennustamiseen.
- **Luotettavuuskysymys mukana:** opiskelija yhdistää ennustamisen epäluotettavuuteen: koska malli ei tiedä, onko vastaus totta, sen vastaus täytyy tarkistaa kriittisissä tilanteissa.

### Palautteen antaminen

Anna lyhyt 2–3 lauseen palaute ennen seuraavaa oppituntia. Keskity yhteen tärkeimpään asiaan.

- **Jos ydinajatus on oikein:** ”Hyvä — ymmärrät, että kielimalli ennustaa eikä hae valmista vastausta. Muista tämä, kun myöhemmin arvioimme tekoälyn luotettavuutta.”
- **Jos väärinymmärrys näkyy:** ”Tarkista vielä: hakeeko malli vastauksen tietokannasta vai ennustaako se todennäköisen jatkon? Tämä ero on tärkeä myöhemmin.”
- **Jos hallusinaatio jää epäselväksi:** ”Lisää vielä selitys siitä, miksi vakuuttava vastaus voi silti olla väärä.”

---

## Arviointivinkit

### Perusymmärryksen tarkistaminen

- Kysy: ”Miten kielimalli ennustaa seuraavan sanan tai tokenin?” Hyvä vastaus: se käyttää opittuja parametreja ja todennäköisyyksiä aiemman tekstin perusteella.
- Kysy: ”Mitä hallusinaatio tarkoittaa?” Hyvä vastaus: malli tuottaa vakuuttavan mutta virheellisen tai keksityn vastauksen.

### Kriittinen ajattelu

- Näytä hallusinaatio ja kysy: ”Mistä tiesit, että se voi olla väärä?” Hyvä vastaus: väite pitää tarkistaa luotettavasta lähteestä, koska uskottava muoto ei takaa totuutta.
- Kysy: ”Missä ammateissa hallusinaatiot ovat vaarallisimpia?” Hyviä vastauksia ovat esimerkiksi lääketiede, oikeus, IT-tietoturva, taloushallinto ja asiakaspalvelu.

### Itsearviointi

Voit antaa tunnin lopuksi lyhyen itsearvioinnin:

- Ymmärrän, kuinka next-token prediction toimii: täysin samaa mieltä / jokseenkin samaa mieltä / tarvitsen vielä harjoitusta.
- Ymmärrän, miksi hallusinaatiot ovat vaarallisia: täysin samaa mieltä / jokseenkin samaa mieltä / tarvitsen vielä harjoitusta.
- Osaan selittää, miksi kielimallin vastaus pitää tarkistaa kriittisissä tilanteissa: täysin samaa mieltä / jokseenkin samaa mieltä / tarvitsen vielä harjoitusta.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että kielimalli on tehokas tekstin tuottaja mutta ei erehtymätön tietolähde. Sen toiminta perustuu seuraavan tokenin ennustamiseen, opittuihin parametreihin ja koulutusdatan kuvioihin. Tämä selittää sekä mallin vaikuttavat kyvyt että sen virheet.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Millaisessa tilanteessa kielimallin vakuuttava mutta väärä vastaus voisi aiheuttaa todellista vahinkoa?

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **syöte–kolme tulosta–mekanismiselitys**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–10 min | Virittäytyminen | Kytke ydinkysymys tuttuun tilanteeseen ja tarkista lähtötaso. |
| 10–25 min | Ydinkäsite | Mallinna tunnin keskeinen ero yhdellä vastaesimerkillä. |
| 25–65 min | Perustuotos | Oppija ajaa saman promptin kolme kertaa ja selittää tulosten vaihtelua tokenien ennustamisella. Tämä 40 minuutin jakso on itsenäistä tai parin kanssa tehtävää työskentelyä. |
| 65–80 min | Testaus ja purku | Testauta tuotos annetulla tapauksella ja pura yksi onnistuminen sekä yksi korjaus. |
| 80–90 min | Tallennus ja lopputehtävä | Varmista tiedoston nimi, tallennuspaikka ja yhden lauseen johtopäätös. |

### Tukireitti

Oppija analysoi opettajan antamia kolmea tulosta ilman omaa tiliä. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis, oppija vertailee vaihtelua kahdella eri syötteellä. Syventävä työ ei kasvata pakollista ydintuotosta.
