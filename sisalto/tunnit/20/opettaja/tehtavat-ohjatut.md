# Opettajavetoiset tehtävät — oppitunti 20

## Tehtävä 20.1: Päätöspuuanalyysi tosielämän skenaarioissa noin 30 minuuttia

### Tavoite

Tehtävän tavoitteena on, että opiskelijat oppivat arvioimaan, milloin kannattaa käyttää **agenttia**, milloin riittää tavallinen **automaatio** ja milloin paras ratkaisu on jokin muu, esimerkiksi ihmisen tekemä työ tai yksinkertainen chatbot. Opiskelijat harjoittelevat päätöksentekoa kuuden kysymyksen päätöspuun avulla.

**Opettajan painotus:** Korosta, että agentti ei ole automaattisesti paras ratkaisu. Agentti on hyödyllinen silloin, kun tehtävä vaatii tulkintaa, päätöksentekoa, työkalujen käyttöä ja rajattua itsenäistä toimintaa. Yksinkertainen ongelma kannattaa usein ratkaista yksinkertaisella automaatiolla.

### Valmistelu

- Jaa opiskelijat 3–4 hengen ryhmiin.
- Anna jokaiselle ryhmälle yksi tosielämän skenaario.
- Näytä taululla tai jaa opiskelijoille kuuden kysymyksen päätöspuu.
- Varaa ryhmille paperia, yhteinen dokumentti tai muu paikka vastausten kirjaamiseen.

### Kuuden kysymyksen päätöspuu

Ryhmät arvioivat omaa skenaariotaan seuraavien kysymysten avulla:

1. **Onko tehtävä toistuva?**
   Jos tehtävä tapahtuu vain harvoin, automaatio tai agentti ei välttämättä ole vaivan arvoinen.
2. **Onko tehtävässä selkeä tavoite?**
   Agentti tarvitsee tavoitteen. Jos tavoite on epäselvä, järjestelmä ei tiedä, mitä sen pitäisi optimoida.
3. **Tarvitaanko tilanteen tulkintaa?**
   Jos tehtävä perustuu pelkkään yksinkertaiseen sääntöön, tavallinen automaatio voi riittää.
4. **Tarvitaanko työkaluja tai ulkoisia järjestelmiä?**
   Jos järjestelmän pitää hakea tietoa, kirjoittaa järjestelmään tai lähettää viestejä, agenttimainen ratkaisu voi olla perusteltu.
5. **Onko päätöksellä riskejä?**
   Jos päätös koskee rahaa, henkilötietoja, turvallisuutta tai asiakassuhdetta, tarvitaan turvakerroksia ja mahdollisesti ihmisen hyväksyntä.
6. **Onko hyöty suurempi kuin kustannus ja monimutkaisuus?**
   Agentti voi olla kallis ja vaatia ylläpitoa. Jos hyöty on pieni, yksinkertaisempi ratkaisu on parempi.

**Esimerkki opetukseen**

Jos opiskelijat valitsevat agentin liian nopeasti, kysy: “Mitä agentti tekee sellaista, mitä tavallinen automaatio ei pysty tekemään?” Tämä ohjaa heitä perustelemaan valinnan teknisesti eikä vain siksi, että agentti kuulostaa edistyneeltä.

### Skenaarioehdotuksia ryhmille

| Skenaario | Tilanne | Mahdollisia ratkaisuja |
| --- | --- | --- |
| **A: Asiakaspalautteiden käsittely** | Yritys saa päivittäin paljon asiakaspalautteita, jotka pitää luokitella kiireellisyyden ja aiheen mukaan. | Sääntöpohjainen automaatio, agentti tai ihminen. |
| **B: Tentin päivämäärän kysyminen** | Opiskelijat kysyvät usein, milloin seuraava koe on. | FAQ, chatbot tai kalenteriin yhdistetty automaatio. |
| **C: Asiakaspalvelupyyntöjen reititys** | Yhteydenottoja tulee paljon, ja ne pitää ohjata oikealle asiantuntijalle. | Työnkulku, agentti tai hybridiratkaisu. |
| **D: Alennuspyyntöjen käsittely** | Asiakkaat pyytävät alennuksia eri perusteilla. Päätös vaikuttaa yrityksen rahaan. | Agentti, hyväksyntäportti ja human-in-the-loop. |

### Ryhmän tehtävä

Jokainen ryhmä täyttää seuraavan analyysitaulukon:

| Päätöspuun kysymys | Ryhmän vastaus | Mitä tämä tarkoittaa ratkaisun kannalta? |
| --- | --- | --- |
| Onko tehtävä toistuva? |  |  |
| Onko tehtävässä selkeä tavoite? |  |  |
| Tarvitaanko tulkintaa? |  |  |
| Tarvitaanko työkaluja? |  |  |
| Onko päätöksellä riskejä? |  |  |
| Onko hyöty suurempi kuin kustannus? |  |  |

Lopuksi ryhmä tekee ratkaisuehdotuksen:

- **Paras ratkaisu:** chatbot, sääntöpohjainen automaatio, työnkulku, agentti, agentti + ihmisen hyväksyntä tai ihminen.
- **Perustelu:** miksi juuri tämä ratkaisu sopii tilanteeseen?
- **Riski:** mikä on suurin riski tässä ratkaisussa?
- **Turvakerros:** miten riskiä vähennetään?

### Käsittely

Jokainen ryhmä esittelee ratkaisunsa lyhyesti. Opettaja ohjaa keskustelua seuraavilla kysymyksillä:

- Miksi valitsitte agentin tai miksi ette valinneet agenttia?
- Mikä olisi yksinkertaisin toimiva ratkaisu?
- Mikä kohta vaatii ihmisen hyväksynnän?
- Mitä tapahtuisi, jos ratkaisu rakennettaisiin liian monimutkaiseksi?

### Odotettu oppimistulos

- Opiskelijat osaavat arvioida, milloin agentti on perusteltu ratkaisu.
- Opiskelijat ymmärtävät, että yksinkertaisempi automaatio voi olla parempi kuin agentti.
- Opiskelijat osaavat perustella valinnan päätöspuun avulla.

---

## Tehtävä 20.2: Kustannus-hyötysimulaatio noin 20 minuuttia

### Tavoite

Tehtävän tavoitteena on auttaa opiskelijoita ymmärtämään, että agentin rakentamista pitää arvioida myös **kustannusten**, **hyötyjen**, **riskien** ja **ylläpidon** näkökulmasta. Hyvä tekninen ratkaisu ei aina ole taloudellisesti tai organisatorisesti järkevä.

**Opettajan huomio:** Tämä tehtävä auttaa opiskelijoita ymmärtämään, että agentin rakentaminen ei ole vain tekninen päätös. Se on myös taloudellinen, eettinen ja organisatorinen päätös.

### Esimerkkitilanne

Yritys saa kuukaudessa 1 000 asiakaspalautetta. Tällä hetkellä työntekijät lukevat palautteet käsin, luokittelevat ne ja ohjaavat ne oikealle tiimille.

Yritys harkitsee kolmea vaihtoehtoa:

| Vaihtoehto | Kuvaus | Hyödyt | Kustannukset ja riskit |
| --- | --- | --- | --- |
| **A: Ihminen tekee kaiken** | Työntekijät lukevat ja luokittelevat kaikki palautteet käsin. | Laadukas harkinta, hyvä ymmärrys poikkeustilanteista. | Hidas, kallis ja kuormittava suurissa määrissä. |
| **B: Sääntöpohjainen automaatio** | Järjestelmä ohjaa viestit avainsanojen perusteella. | Halvempi ja yksinkertaisempi toteuttaa. | Ei ymmärrä sävyä, poikkeuksia tai monimutkaisia viestejä hyvin. |
| **C: Agentti** | Agentti tulkitsee palautteen, luokittelee sen, ehdottaa vastausta ja ohjaa riskitapaukset ihmiselle. | Joustavampi, nopeampi ja parempi monimutkaisissa tilanteissa. | Kalliimpi rakentaa ja ylläpitää. Vaatii turvakerroksia, testausta ja seurantaa. |

### Keskustelun ohjaus

Johdata keskustelua seuraavilla kysymyksillä:

- Mikä ratkaisu on halvin rakentaa?
- Mikä ratkaisu on helpoin ylläpitää?
- Mikä ratkaisu toimii parhaiten monimutkaisissa tilanteissa?
- Mikä ratkaisu aiheuttaa suurimman riskin, jos se tekee virheen?
- Miten paljon virheet maksavat?
- Missä kohdassa ihmisen pitää olla mukana?

### Ryhmätehtävä

Ryhmät täyttävät kustannus-hyötytaulukon:

| Arviointikohta | Ihminen | Sääntöpohjainen automaatio | Agentti |
| --- | --- | --- | --- |
| **Rakentamisen kustannus** |  |  |  |
| **Ylläpidon tarve** |  |  |  |
| **Virheen riski** |  |  |  |
| **Nopeus** |  |  |  |
| **Soveltuvuus poikkeustilanteisiin** |  |  |  |
| **Kokonaisarvio** |  |  |  |

### Johtopäätös

Kokoa keskustelu yhteen:

> Agentti kannattaa rakentaa silloin, kun sen tuoma hyöty on suurempi kuin sen kustannukset, riskit ja ylläpidon vaiva. Jos yksinkertainen automaatio riittää, se on usein parempi ratkaisu.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että agentin rakentaminen vaatii kustannus-hyötyarvion.
- Opiskelijat osaavat vertailla ihmistyötä, sääntöpohjaista automaatiota ja agenttia.
- Opiskelijat ymmärtävät, että teknisesti mahdollinen ratkaisu ei aina ole järkevin ratkaisu.

---

## Tehtävä 20.3: Suunnittelusilmukan valinta noin 20 minuuttia

### Tavoite

Tehtävän tavoitteena on auttaa opiskelijoita ymmärtämään, että agentin rakentaminen on **suunnittelusilmukka**: ensin määritellään tavoite, sitten rajataan tehtävä, valitaan työkalut, suunnitellaan turvakerrokset, testataan ja parannetaan.

### Opettajan ohjeet

Selitä opiskelijoille:

“Agenttia ei kannata suunnitella aloittamalla työkalusta. Ensin pitää tietää, mitä ongelmaa ratkaistaan ja millainen päätöksenteko on sallittua. Vasta sen jälkeen valitaan työkalut ja rakennetaan ratkaisu.”

**Agentin suunnittelusilmukka**

|  |
| --- |
| **1. Määrittele tavoite** Mitä ongelmaa agentti ratkaisee? |
| ↓ |
| **2. Rajaa tehtävä** Mitä agentti tekee ja mitä se ei tee? |
| ↓ |
| **3. Valitse työkalut** Mitä järjestelmiä tai toimintoja agentti tarvitsee? |
| ↓ |
| **4. Lisää turvakerros** Mitä pitää estää, tarkistaa tai hyväksyttää ihmisellä? |
| ↓ |
| **5. Testaa** Toimiiko agentti normaaleissa, poikkeavissa ja riskialttiissa tilanteissa? |
| ↓ |
| **6. Paranna** Mitä muutetaan testien ja palautteen perusteella? |

### Ryhmätyö

Ryhmät valitsevat yhden aiemmista skenaarioista ja soveltavat siihen suunnittelusilmukkaa.

**Ryhmän tehtävä:**

- **Tavoite:** mitä ongelmaa ratkaistaan?
- **Rajaus:** mitä agentti saa tehdä ja mitä se ei saa tehdä?
- **Työkalut:** mitä tietolähteitä, API-yhteyksiä tai viestintäkanavia tarvitaan?
- **Turvakerros:** mitä tarkistetaan ennen toimintaa?
- **Testit:** millä kolmella testillä varmistetaan, että ratkaisu toimii?
- **Parannus:** mitä tehdään, jos testi epäonnistuu?

**Vinkki arviointiin:** Hyvä suunnittelusilmukka sisältää myös sen, mitä agentti ei tee. Rajaukset ovat yhtä tärkeitä kuin ominaisuudet.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät agentin rakentamisen iteratiivisena suunnitteluna.
- Opiskelijat osaavat määritellä tavoitteen, rajauksen, työkalut, turvakerrokset ja testit.
- Opiskelijat ymmärtävät, että agenttia parannetaan testien ja palautteen perusteella.

---

## Tehtävä 20.4: Työkalun merkitys noin 15 minuuttia

### Tavoite

Tehtävän tavoitteena on auttaa opiskelijoita ymmärtämään, että agentti on vain niin kykenevä kuin sen käytössä olevat **työkalut**. Samalla opiskelijat pohtivat työkalujen vaikutusta **turvallisuuteen**, **vastuuseen** ja **rajoihin**.

### Opettajan ohjeet

Kerro opiskelijoille:

> Agentti ilman työkaluja voi lähinnä keskustella ja ehdottaa. Agentti, jolla on työkaluja, voi tehdä asioita. Siksi työkalut lisäävät sekä hyötyä että riskiä.

### Esittely

Näytä sama agentti kolmella eri työkalutasolla:

| Työkalutaso | Mitä agentti voi tehdä? | Riski |
| --- | --- | --- |
| **Ei työkaluja** | Vastaa yleisellä tasolla ja antaa ehdotuksia. | Voi hallusinoida tai antaa yleisiä vastauksia, mutta ei tee suoria järjestelmämuutoksia. |
| **Lukuoikeudet** | Voi hakea tietoa tietokannasta, kalenterista tai dokumenteista. | Voi paljastaa tietoa, jota käyttäjän ei pitäisi nähdä. |
| **Kirjoitus- ja toiminto-oikeudet** | Voi lähettää viestejä, muuttaa tietoja, hyväksyä pyyntöjä tai käynnistää prosesseja. | Voi tehdä virheellisiä tai haitallisia toimintoja, jos turvakerros puuttuu. |

### Ryhmätyö

Ryhmät valitsevat yhden agenttityypin ja päättävät, mitä työkaluja se tarvitsee.

**Agenttivaihtoehdot:**

- **FAQ-agentti:** vastaa opiskelijoiden kysymyksiin kurssista.
- **Neuvonta-agentti:** auttaa ratkaisemaan käyttäjien ongelmia.
- **Myyntiagentti:** auttaa asiakkaita löytämään sopivan tuotteen.
- **Hyvitysagentti:** käsittelee asiakkaiden hyvityspyyntöjä.

**Ryhmän tehtävä:**

| Työkalu | Miksi tarvitaan? | Mitä riskiä se tuo? | Miten riski rajataan? |
| --- | --- | --- | --- |
| Tietokanta |  |  |  |
| Sähköposti tai viestintäkanava |  |  |  |
| Kalenteri tai ajanvarausjärjestelmä |  |  |  |

### Johtopäätös

Kokoa keskustelu yhteen:

> **Pääpointti:** Agentti on vain niin kykenevä kuin sen työkalut. Mitä enemmän työkaluja agentille annetaan, sitä hyödyllisempi mutta myös riskialttiimpi siitä tulee. Siksi työkalujen valinta on turvallisuus- ja vastuukysymys.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät työkalujen merkityksen agentin kyvykkyydelle.
- Opiskelijat osaavat arvioida, mitä työkaluja agentti tarvitsee tehtäväänsä varten.
- Opiskelijat ymmärtävät, että työkalut lisäävät myös riskejä ja vaativat rajoituksia.

---

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- käyttää päätöspuuta automaatioratkaisun valintaan,
- erottaa tilanteet, joissa agentti on perusteltu ratkaisu,
- perustella, milloin yksinkertaisempi automaatio riittää,
- arvioida agentin kustannuksia, hyötyjä, riskejä ja ylläpitoa,
- suunnitella agentin tavoitteen, rajauksen, työkalut ja turvakerrokset,
- selittää, miksi agentin työkalut vaikuttavat suoraan sen kyvykkyyteen ja riskeihin.

---
