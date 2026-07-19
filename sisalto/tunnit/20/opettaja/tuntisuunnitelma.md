# Opettajan materiaalit — oppitunti 20

## Osaamistavoitteet

Tämän oppitunnin tavoitteena on, että opiskelija ymmärtää, milloin **agentti** on järkevä ratkaisu ja milloin yksinkertaisempi automaatio riittää. Oppitunnin ydin ei ole rakentamisessa vaan **arkkitehtuuripäätöksissä**: opiskelija oppii arvioimaan, kannattaako käyttää promptausta, työnkulkua vai agenttia.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, että agentti ei ole aina parempi ratkaisu kuin yksinkertainen työnkulku.
- Opiskelija tunnistaa automatisoinnin kolme tasoa: **promptaus**, **työnkulku** ja **agentti**.
- Opiskelija ymmärtää, että monimutkaisuus, kustannukset ja riskit kasvavat, kun siirrytään työnkulusta agenttiin.

### Soveltaa ja analysoida

- Opiskelija osaa soveltaa **päätöspuumenetelmää** todellisiin automaatioon liittyviin valintatilanteisiin.
- Opiskelija osaa arvioida, toistuuko tehtävä, onko se monimutkainen ja muuttuvatko sen säännöt.
- Opiskelija osaa tunnistaa tekijät, jotka tekevät agentista järkevän tai kannattamattoman investoinnin.

### Luoda ja arvioida

- Opiskelija osaa perustella, miksi omaan projektiin tarvitaan agentti tai miksi yksinkertaisempi ratkaisu riittäisi.
- Opiskelija osaa tarkentaa omaa agenttiongelmaansa niin, että agentin autonomisuus tuottaa todellista lisäarvoa.
- Opiskelija osaa arvioida ratkaisun hyötyjä suhteessa sen kustannuksiin ja riskeihin.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on yksinkertaisuus. Opiskelijan ei pidä valita agenttia siksi, että se kuulostaa edistyneeltä, vaan siksi, että ongelma aidosti vaatii autonomista päättelyä, muuttuvien tilanteiden käsittelyä ja työkalujen käyttöä.

---

## Pedagoginen lähestymistapa

### Ydinviesti: valitse yksinkertaisin ratkaisu, joka todella toimii

Oppitunnin ydin on ajattelutavan muutos. Opiskelija saattaa helposti ajatella, että agentti on aina paras tai modernein ratkaisu. Tällä tunnilla tätä ajatusta puretaan. Agentti on tehokas vain silloin, kun tehtävä vaatii enemmän kuin sääntöpohjaista automaatiota.

> **Hyvä arkkitehtuuripäätös ei ole monimutkaisin ratkaisu. Hyvä arkkitehtuuripäätös on yksinkertaisin ratkaisu, joka ratkaisee ongelman luotettavasti.**

Korosta opiskelijoille:

- **Promptaus** riittää, jos ihminen voi käynnistää tehtävän itse ja arvioida vastauksen.
- **Työnkulku** riittää, jos prosessi on toistuva ja säännöt ovat selkeät.
- **Agentti** kannattaa, jos tehtävä on toistuva, monimutkainen, muuttuva ja vaatii päättelyä sekä työkalujen käyttöä.

### Monimutkaisuus on aina kustannus

Opiskelijoiden on tärkeää ymmärtää, että agentti ei ole vain ”parempi työnkulku”. Agentti on luonteeltaan erilainen järjestelmä. Se vaatii enemmän suunnittelua, testausta, turvallisuutta, ylläpitoa ja valvontaa.

**Opettajan huomio:** Palaa kustannus–hyöty-ajatteluun usein. Kysy opiskelijoilta: ”Mitä agentti tekee paremmin kuin työnkulku?” Jos vastaus on epäselvä, agentti ei ehkä ole vielä perusteltu ratkaisu.

### Päätöspuu oppimisen välineenä

Päätöspuu auttaa opiskelijaa tekemään valinnan systemaattisesti. Tärkeää ei ole vain vastata kysymyksiin, vaan perustella vastaukset. Oppitunnin aikana opiskelijan tulisi oppia kysymään:

1. **Toistuuko tehtävä?**
2. **Onko tehtävä yksinkertainen vai monimutkainen?**
3. **Ovatko säännöt staattisia vai muuttuvia?**
4. **Kuka maksaa ratkaisun rakentamisen ja ylläpidon?**
5. **Mitkä ovat epäonnistumisen kustannukset?**
6. **Onko ihmisen valvonta mahdollista?**

| Jos vastaus on... | Todennäköinen ratkaisu | Perustelu |
| --- | --- | --- |
| Tehtävä ei toistu tai tehdään hyvin harvoin. | **Ei automaatiota** tai yksinkertainen promptaus. | Automatisoinnin rakentamiseen kuluu enemmän aikaa kuin tehtävän tekemiseen käsin. |
| Tehtävä toistuu ja säännöt ovat selkeät. | **Työnkulku**. | Sääntöpohjainen ratkaisu on riittävä, halvempi ja helpompi ylläpitää. |
| Tehtävä toistuu, on monimutkainen ja säännöt muuttuvat. | **Agentti** voi olla perusteltu. | Tarvitaan tilanteen arviointia, päättelyä ja joustavaa työkalujen käyttöä. |
| Epäonnistumisen kustannukset ovat korkeat. | **Työnkulku + ihmisen valvonta** tai tarkasti rajattu agentti. | Autonomian hyöty ei saa ylittää turvallisuuden ja valvonnan tarvetta. |

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”Agentti on aina paras ratkaisu.”

**Korjaava näkökulma:** Agentti ei ole aina paras ratkaisu, koska se lisää monimutkaisuutta, kustannuksia ja riskejä. Jos yksinkertainen työnkulku ratkaisee ongelman riittävän hyvin, agentti on ylimitoitettu ratkaisu.

> Älä rakenna agenttia, jos työnkulku riittää.

### Väärinkäsitys 2: ”Jos tehtävässä on tekoälyä, se on agentti.”

**Korjaava näkökulma:** Tekoälysolmu ei tee järjestelmästä automaattisesti agenttia. Agentti tarvitsee tavoitteen, syötteen käsittelyn, päättelyä, työkalujen käyttöä ja usein palautesilmukan. Pelkkä tekoälyn vastaus käyttäjän kysymykseen on usein promptausta tai chatbot-toimintaa.

**Esimerkki opetukseen**

Kysy opiskelijoilta: ”Jos työnkulussa on yksi tekoälysolmu, joka vastaa viestiin, onko se agentti vai tekoälyä käyttävä työnkulku?”

### Väärinkäsitys 3: ”Säännöt ovat huonoja, koska agentti on joustavampi.”

**Korjaava näkökulma:** Säännöt ovat usein hyvä asia. Jos prosessi on selkeä ja ennakoitava, sääntöpohjainen työnkulku on luotettavampi, halvempi ja helpompi testata kuin agentti. Joustavuus on hyödyllistä vain silloin, kun sitä todella tarvitaan.

### Väärinkäsitys 4: ”Agentin rakentamisen kustannus on vain sen tekemiseen käytetty aika.”

**Korjaava näkökulma:** Agentin kustannuksiin kuuluvat myös testaus, valvonta, virheiden korjaus, ylläpito, käyttökustannukset, tietoturva ja dokumentointi. Nämä voivat olla suurempi osa kokonaiskustannusta kuin alkuperäinen rakentaminen.

---

## Luokkatehtävien ohjeistus

### TT-A: Päätöspuun soveltaminen

**Tavoite:** Opiskelija arvioi, mikä ratkaisutyyppi sopii annettuun tilanteeseen: promptaus, työnkulku vai agentti.

**Tehtävä:** Anna opiskelijoille 2–3 tapausta, esimerkiksi sähköpostien lajittelu, asiakaspalvelupyyntöjen reititys ja laskujen käsittely. Opiskelija käy jokaisen tapauksen läpi kuuden kysymyksen avulla ja perustelee valintansa.

| Päätöspuun kysymys | Opiskelijan vastaus | Mitä vastaus tarkoittaa? |
| --- | --- | --- |
| Toistuuko tehtävä? |  | Jos ei toistu, automaatio ei yleensä kannata. |
| Onko tehtävä yksinkertainen vai monimutkainen? |  | Yksinkertainen tehtävä sopii usein työnkuluksi. |
| Muuttuvatko säännöt? |  | Muuttuvat säännöt voivat perustella agentin. |
| Kuka maksaa? |  | Suuret kustannukset vaativat vahvemmat perusteet. |
| Mitkä ovat epäonnistumisen kustannukset? |  | Korkea riski vaatii valvontaa ja rajoituksia. |
| Onko ihmisen valvonta mahdollista? |  | Jos valvonta on mahdollista, riskiä voidaan hallita paremmin. |

**Aika-arvio:** 20–25 minuuttia

---

### TT-B: Oma agenttiongelma päätöspuun läpi

**Tavoite:** Opiskelija tarkistaa, onko oma lopputyön agenttiongelma aidosti agentin arvoinen.

**Tehtävä:** Opiskelija ottaa oman pohjapiirros 1:n ongelman ja käy sen läpi päätöspuun avulla. Lopuksi opiskelija kirjoittaa lyhyen johtopäätöksen: **tarvitseeko tämä agentin vai riittäisikö yksinkertaisempi ratkaisu?**

**Opettajan tarkistuskysymys:** Jos opiskelija vastaa ”agentti, koska se on siistimpi”, pyydä häntä perustelemaan, mitä agentti tekee paremmin kuin työnkulku. Ilman tätä perustelua ongelmaa pitää tarkentaa.

**Hyvä vastaus sisältää:**

- päätöspuun kuusi kysymystä ja vastaukset niihin
- selkeän valinnan: promptaus, työnkulku vai agentti
- perustelun, miksi valinta on järkevä
- mahdollisen tarkennuksen omaan agenttiongelmaan

**Aika-arvio:** 20–30 minuuttia

---

## CFU-kysymykset

1. **Automaatio vs. autonomia:** Miksi agentti ei ole automaattisesti parempi kuin työnkulku?
2. **Kustannukset:** Mitä kustannuksia agenttiin liittyy rakentamisen lisäksi?
3. **Riskit:** Miksi korkean riskin tehtävä ei välttämättä sovi täysin autonomiselle agentille?
4. **Päätöspuu:** Mikä kuudesta kysymyksestä vaikuttaa eniten siihen, valitsetko työnkulun vai agentin?

---

## Opettajan vihjeet

### Jos opiskelija valitsee agentin liian helposti

Kysy:

- Mitä agentti tekee, mitä työnkulku ei pystyisi tekemään?
- Miten säännöt muuttuvat tilanteesta toiseen?
- Mitä tietoa agentti tarvitsee päättelyyn?
- Mikä on pienin versio, jolla ongelmaa voisi kokeilla?

### Jos opiskelija päätyy siihen, että oma idea ei tarvitse agenttia

Tämä ei ole epäonnistuminen. Se on hyvä arkkitehtuuripäätös. Pyydä opiskelijaa tarkentamaan ongelmaa niin, että agentti tuo lisäarvoa, tai hyväksymään yksinkertaisempi ratkaisu osaksi suunnitelmaa.

> Hyvä suunnittelija ei rakenna agenttia väkisin. Hyvä suunnittelija valitsee oikean työkalun.

### Jos opiskelija ajattelee vain teknistä toteutusta

Palauta keskustelu ongelmaan ja käyttäjään:

- Kenen ongelmaa ratkaiset?
- Kuinka usein ongelma tapahtuu?
- Mitä tapahtuu, jos ratkaisu epäonnistuu?
- Miksi tämä on tärkeää?

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että agentti on valinta, ei oletus. Agentti kannattaa rakentaa vain silloin, kun tehtävä vaatii autonomista päättelyä, muuttuvien tilanteiden käsittelyä ja työkalujen käyttöä tavalla, johon tavallinen työnkulku ei riitä.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Mikä omassa projektissasi on se kohta, jossa työnkulku ei enää riitä ja agentin päättely tuo lisäarvoa?

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **perusteltu päätösmuistio**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–10 min | Virittäytyminen | Kytke ydinkysymys tuttuun tilanteeseen ja tarkista lähtötaso. |
| 10–25 min | Ydinkäsite | Mallinna tunnin keskeinen ero yhdellä vastaesimerkillä. |
| 25–65 min | Perustuotos | Oppija rakentaa yhdelle tehtävälle päätöspuun promptin, työnkulun ja agentin välille. Tämä 40 minuutin jakso on itsenäistä tai parin kanssa tehtävää työskentelyä. |
| 65–80 min | Testaus ja purku | Testauta tuotos annetulla tapauksella ja pura yksi onnistuminen sekä yksi korjaus. |
| 80–90 min | Tallennus ja lopputehtävä | Varmista tiedoston nimi, tallennuspaikka ja yhden lauseen johtopäätös. |

### Tukireitti

Oppija valitsee perustelut valmiista vaihtoehdoista. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis, oppija vertailee kustannusta, riskiä ja ylläpitoa. Syventävä työ ei kasvata pakollista ydintuotosta.
