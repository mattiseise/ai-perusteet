# Opettajavetoiset tehtävät — oppitunti 25

## Aktiviteetti 1: Kolme sääntöä hyväksynnän tarpeelle noin 20 minuuttia

### Tavoite

Aktiviteetin tavoitteena on auttaa opiskelijoita ymmärtämään, milloin agentin päätös voidaan automatisoida ja milloin tarvitaan **ihmisen hyväksyntä**. Opiskelijat oppivat käyttämään kolmea sääntöä päätöksenteon riskin arvioimiseen.

**Opettajan painotus:** Korosta opiskelijoille, että kaikkia päätöksiä ei tarvitse hyväksyttää ihmisellä. Jos hyväksyntää vaaditaan joka vaiheessa, agentti hidastaa työtä. Jos hyväksyntää ei vaadita riskitilanteissa, agentti voi aiheuttaa vahinkoa. Ammattilaisen tehtävä on löytää oikea tasapaino.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Kerro opiskelijoille:

“Human-in-the-loop tarkoittaa sitä, että ihminen osallistuu agentin päätöksentekoon silloin, kun päätös on riskialtis, epävarma tai poikkeuksellinen. Kaikkea ei tarvitse hyväksyttää ihmisellä, mutta tärkeät ja vaaralliset päätökset pitää.”

Kirjoita taululle kolme hyväksynnän sääntöä:

1. **Rahaa tai rakenteita koskeva päätös:** alennukset, hyvitykset, sopimukset, asiakastiedot tai pysyvät tietokantamuutokset vaativat hyväksynnän.
2. **Epävarmuus:** jos agentin varmuus on alle sovitun rajan, esimerkiksi alle 70 %, päätös siirretään ihmiselle.
3. **Poikkeama:** jos tilanne on epätavallinen, tunnepitoinen, riskialtis tai poikkeaa normaalista prosessista, tarvitaan hyväksyntä.

**Esimerkki opetukseen**

Näytä opiskelijoille, että päätöksen tekninen helppous ei tarkoita, että agentti saa tehdä sen itsenäisesti. Esimerkiksi hyvityksen lähettäminen voi olla teknisesti yksinkertaista, mutta taloudellisesti ja asiakassuhteen kannalta merkittävää.

### Esittely: kolme sääntöä käytännössä

| Sääntö | Esimerkki | Miksi hyväksyntä tarvitaan? |
| --- | --- | --- |
| **Rahaa tai rakenteita** | Agentti ehdottaa 40 % alennusta asiakkaalle. | Päätös vaikuttaa yrityksen rahaan ja hinnoitteluun. |
| **Epävarmuus** | Agentti on vain 62 % varma siitä, että asiakas on oikeutettu hyvitykseen. | Matala varmuus lisää virheellisen päätöksen riskiä. |
| **Poikkeama** | Asiakas on erittäin vihainen ja uhkaa lopettaa sopimuksen. | Tilanne vaatii harkintaa, empatiaa ja mahdollisesti poikkeusmenettelyä. |

### Ryhmätyö

Jaa opiskelijat pienryhmiin. Anna ryhmille kahdeksan päätöstä. Ryhmän tehtävänä on päättää, vaatiiko päätös ihmisen hyväksynnän vai voiko agentti tehdä sen itsenäisesti.

**Esimerkkipäätökset:**

1. Agentti lähettää asiakkaalle linkin käyttöohjeeseen.
2. Agentti antaa asiakkaalle 10 % alennuskoodin.
3. Agentti ehdottaa 50 % hyvitystä myöhästyneestä toimituksesta.
4. Agentti muuttaa asiakkaan toimitusosoitetta.
5. Agentti vastaa usein kysyttyyn kysymykseen palautusajasta.
6. Agentti poistaa vanhan tukitiketin.
7. Agentti lähettää viestin asiakkaalle, jonka viesti on vihainen ja uhkaava.
8. Agentti tekee päätöksen, vaikka se on vain 58 % varma oikeasta ratkaisusta.

**Ryhmän tehtävä:**

| Päätös | Vaatiiko hyväksynnän? | Mikä sääntö vaikuttaa? | Perustelu |
| --- | --- | --- | --- |
| [Päätös] | Kyllä / ei | Raha / epävarmuus / poikkeama | [Perustelu] |

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, ettei jokainen agentin päätös tarvitse ihmisen hyväksyntää.
- Opiskelijat osaavat tunnistaa tilanteet, joissa hyväksyntä on tarpeellinen.
- Opiskelijat osaavat käyttää kolmea sääntöä: raha tai rakenne, epävarmuus ja poikkeama.

---

## Aktiviteetti 2: Hyväksyntäportti käyttöliittymänä noin 20 minuuttia

### Tavoite

Aktiviteetin tavoitteena on opettaa opiskelijoille, millainen on hyvä **hyväksyntäportti**. Hyvä hyväksyntäportti antaa ihmiselle riittävästi tietoa päätöksen tekemiseen, mutta ei kuormita häntä turhalla tiedolla.

**Opettajan huomio:** Hyväksyntäportin tarkoitus ei ole vain kysyä “hyväksytäänkö?”. Sen pitää näyttää päätöksen kannalta olennaiset tiedot: mitä agentti aikoo tehdä, miksi se ehdottaa sitä, mitä riskejä päätökseen liittyy ja mitä vaihtoehtoja hyväksyjällä on.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Kerro opiskelijoille:

“Hyväksyntäportin pitää olla **selkeä**, **nopea** ja **päätöstä tukeva**. Ihmisen ei pidä joutua arvaamaan, mitä agentti aikoo tehdä tai mihin tietoihin ehdotus perustuu.”

### Esittely: hyväksyntäportti alennukselle

**HYVÄKSYNTÄPYYNTÖ**

**Asiakas:** Jane Smith, 3 aiempaa ostoa

**Pyyntö:** 50 % alennus, 100 € → 50 €

**Agentin perustelu:** Asiakas on lojaali ja kertoo kilpailijan tarjonneen halvempaa hintaa.

**Päätöksen tekee:** Myyntipäällikkö

**Vaihtoehto, jos hylätään:** Tarjoa ilmainen toimitus.

**Toiminnot:** [HYVÄKSY] [HYLKÄÄ] [KYSY LISÄÄ]

Kysy opiskelijoilta:

- Mikä tässä hyväksyntäportissa on selkeää?
- Mitä tietoa päätöksentekijä tarvitsee lisää?
- Onko vaihtoehtoinen ratkaisu hyödyllinen?
- Mitä tapahtuisi, jos hyväksyntäportissa näkyisi vain painike “Hyväksy”?

### Ryhmätyö

Opiskelijat muotoilevat hyväksyntäportin valitsemalleen tilanteelle.

**Mahdollisia tilanteita:**

- asiakkaalle myönnettävä hyvitys,
- tilauksen peruminen,
- asiakkaan osoitetiedon muuttaminen,
- tukitiketin siirtäminen kiireelliseksi,
- laskun hyväksyminen,
- käyttäjätunnuksen lukitseminen.

**Hyväksyntäportissa pitää näkyä:**

| Kohta | Mitä siihen kirjoitetaan? |
| --- | --- |
| **Päätöksen kohde** | Mitä ollaan hyväksymässä? |
| **Taustatiedot** | Mihin tietoihin agentin ehdotus perustuu? |
| **Agentin perustelu** | Miksi agentti ehdottaa tätä päätöstä? |
| **Riski** | Mitä voi mennä pieleen? |
| **Vaihtoehdot** | Hyväksy, hylkää, kysy lisää tai siirrä eteenpäin. |

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että hyväksyntäportin pitää tukea ihmisen päätöksentekoa.
- Opiskelijat osaavat suunnitella selkeän hyväksyntäpyynnön.
- Opiskelijat osaavat erottaa olennaisen päätöstiedon turhasta taustatiedosta.

---

## Aktiviteetti 3: Human-in-the-loop-työnkulku noin 25 minuuttia

### Tavoite

Aktiviteetin tavoitteena on auttaa opiskelijoita suunnittelemaan kokonainen **human-in-the-loop-työnkulku**, jossa agentti ja ihminen tekevät yhteistyötä. Opiskelijat ymmärtävät, missä vaiheissa agentti voi toimia itsenäisesti ja missä vaiheissa ihmisen pitää tarkistaa, hyväksyä tai korjata päätös.

**Vinkki arviointiin:** Hyvä työnkulku ei vain lisää ihmistä loppuun tarkistajaksi. Ihmisen rooli sijoitetaan niihin kohtiin, joissa riski, epävarmuus tai vaikutus on suurin.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Kerro opiskelijoille:

“Human-in-the-loop ei tarkoita sitä, että ihminen tekee kaiken. Se tarkoittaa, että agentti tekee rutiinityötä ja ihminen osallistuu niissä kohdissa, joissa tarvitaan harkintaa, vastuuta tai hyväksyntää.”

### Esittely: palautuspyynnön käsittely

1. Agentti lukee asiakkaan viestin.

2. Hyväksyntäportti 1: Onko palautusaika voimassa?

3. Agentti lähettää palautusohjeet.

4. Hyväksyntäportti 2: Tarjotaanko alennusta seuraavaan ostokseen?

5. Agentti lähettää jatkoviestin asiakkaalle.

Keskustelkaa:

- Mitä agentti voi tehdä itse?
- Missä kohdassa tarvitaan ihmisen hyväksyntä?
- Voisiko jokin hyväksyntäportti olla automaattinen matalan riskin tapauksissa?
- Miten asiakas huomaa, että prosessi toimii luotettavasti?

### Ryhmätyö

Opiskelijat suunnittelevat human-in-the-loop-työnkulun yhdelle prosessille.

**Mahdollisia prosesseja:**

- tilauksen käsittely,
- ajanvaraus,
- asiakaspalvelupyyntö,
- asiakaspalautteen käsittely,
- hyvityksen myöntäminen,
- jäsenyyden uusiminen.

**Ryhmän tehtävä:**

1. Kirjoittakaa prosessin vaiheet oikeassa järjestyksessä.
2. Merkitkää, missä vaiheessa agentti toimii itsenäisesti.
3. Merkitkää, missä vaiheessa ihminen hyväksyy tai tarkistaa päätöksen.
4. Merkitkää, mitä tietoa hyväksyjä tarvitsee.
5. Merkitkää, mitä tapahtuu, jos hyväksyjä hylkää päätöksen.

**Human-in-the-loop-työnkulun malli**

|  |
| --- |
| **1. Agentti lukee syötteen** Asiakasviesti, lomake, tiketti tai tilaus. |
| ↓ |
| **2. Agentti tekee alustavan arvion** Luokittelu, riskitaso ja ehdotus. |
| ↓ |
| **3. Hyväksyntäportti** Ihminen hyväksyy, hylkää tai pyytää lisätietoa. |
| ↓ |
| **4. Agentti suorittaa turvallisen toiminnon** Viesti, päivitys, raportti tai ohje. |

### Odotettu oppimistulos

- Opiskelijat ymmärtävät human-in-the-loop-työnkulun periaatteen.
- Opiskelijat osaavat sijoittaa ihmisen hyväksynnän prosessin riskikohtiin.
- Opiskelijat osaavat kuvata, miten agentti ja ihminen toimivat yhdessä.

---

## Aktiviteetti 4: Oppiminen palautteesta noin 15 minuuttia

### Tavoite

Aktiviteetin tavoitteena on näyttää opiskelijoille, miten agentti voi hyödyntää ihmisen palautetta ja hyväksyntäpäätöksiä tulevien ehdotusten parantamiseen. Samalla opiskelijat tunnistavat **väärän oppimisen** riskin.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Kerro opiskelijoille:

“Kun ihminen hyväksyy, hylkää tai muokkaa agentin ehdotusta, siitä syntyy arvokasta palautedataa. Agentti voi käyttää tätä tietoa myöhemmin parempien ehdotusten tekemiseen. Tämä pitää kuitenkin suunnitella huolellisesti, koska agentti voi myös oppia vääristä tai epäjohdonmukaisista päätöksistä.”

### Esittely: alennusehdotuksista oppiminen

Anna opiskelijoille esimerkki:

- Hyväksyjä A hyväksyy usein suuret alennukset, jos asiakas on pitkäaikainen.
- Hyväksyjä B hyväksyy vain pienet alennukset ja suosii vaihtoehtoisia etuja, kuten ilmaista toimitusta.
- Agentti huomaa eron ja alkaa ehdottaa eri hyväksyjille erilaisia ratkaisuja.

Kysy opiskelijoilta:

- Onko tämä hyödyllistä vai vaarallista?
- Voiko agentti oppia liikaa yhden henkilön tyylistä?
- Miten varmistetaan, että agentti oppii organisaation säännöistä eikä yksittäisen hyväksyjän mieltymyksistä?

**Opettajan tarkistuskysymys:** Jos opiskelijat sanovat “agentti oppii hyväksyjien päätöksistä”, pyydä heitä tarkentamaan, mitä se saa oppia. Oppiiko se säännön, päätösmallin vai yksittäisen ihmisen tavan toimia? Näissä on suuri ero.

### Ryhmätyö

Opiskelijat suunnittelevat, miten agentti oppii hyväksyntäpäätöksistä turvallisesti.

**Ryhmän tehtävä:**

1. **Mitä dataa tallennetaan?** Esimerkiksi päätös, perustelu, hyväksyjä, riskitaso, lopputulos ja asiakaspalaute.
2. **Miten agentti oppii?** Esimerkiksi tunnistamalla, millaiset ehdotukset hyväksytään usein ja millaiset hylätään.
3. **Miten ehdotuksia mukautetaan?** Esimerkiksi agentti ehdottaa jatkossa pienempiä alennuksia, jos suuret alennukset hylätään usein.
4. **Mitä riskejä syntyy?** Esimerkiksi agentti voi oppia väärän käytännön, vahvistaa epäoikeudenmukaisia päätöksiä tai ylisovittaa yhden hyväksyjän tyyliin.

| Kysymys | Ryhmän suunnitelma |
| --- | --- |
| **Mitä dataa tallennetaan?** |  |
| **Miten agentti oppii?** |  |
| **Miten ehdotuksia mukautetaan?** |  |
| **Mitä riskejä syntyy?** |  |
| **Miten väärä oppiminen estetään?** |  |

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että hyväksyntäpäätöksistä voi syntyä hyödyllistä palautedataa.
- Opiskelijat osaavat kuvata, mitä tietoa agentin kannattaa tallentaa oppimista varten.
- Opiskelijat ymmärtävät, että agentti voi oppia myös vääriä malleja, jos palaute on puutteellista tai vinoutunutta.

---

## Herättävät keskustelukysymykset

- **Entä jos hyväksyjä ei vastaa 24 tunnissa?**
- **Voiko agentti oppia vääriä asioita ihmisten päätöksistä?**
- **Mitä tapahtuu, jos agentti tulkitsee palautteen väärin?**
- **Kenen vastuulla päätös on, jos ihminen hyväksyy agentin ehdotuksen lukematta sitä kunnolla?**
- **Milloin automaattinen päätös on parempi kuin ihmisen hyväksyntä?**

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- selittää, mitä **human-in-the-loop** tarkoittaa agenttijärjestelmässä,
- tunnistaa, mitkä päätökset vaativat ihmisen hyväksynnän,
- soveltaa kolmea sääntöä: **raha tai rakenne**, **epävarmuus** ja **poikkeama**,
- suunnitella selkeän **hyväksyntäportin**,
- piirtää työnkulun, jossa agentin ja ihmisen roolit näkyvät,
- kuvata, miten agentti voi oppia hyväksyntäpäätöksistä turvallisesti,
- tunnistaa väärän oppimisen ja palautteen väärintulkinnan riskit.

---
