# Opettajavetoiset tehtävät

## Tehtävä 1.1: Luokitteluharjoitus — tekoälyä vai ei? — luokkakeskustelu

### Tavoite

Tehtävän tavoitteena on haastaa opiskelijoiden ajattelua siitä, että kaikki älykkäältä vaikuttava olisi automaattisesti **tekoälyä**. Samalla vahvistetaan tekoälyn määritelmää käytännön esimerkkien avulla.

**Opettajan painotus:** Korosta opiskelijoille, että **automaatio**, **älykäs vaikutelma** ja **tekoäly** eivät tarkoita samaa asiaa. Keskeistä on pohtia, käyttääkö järjestelmä dataa, oppiiko se malleja ja mukautuuko se tilanteisiin.

### Opettajan ohjeet ja fasilitointi

**Valmistelu ennen tuntia noin 5 minuuttia:**

Kirjoita taululle tai projisoi näkyviin seuraavat kuusi järjestelmää:

1. Älypuhelimen automaattinen tekstinkorjaus
2. Netflixin suositukset
3. Pankkiautomaatti
4. Sähköpostin roskapostisuodatin, vanha sääntöpohjainen versio
5. Google Mapsin reititys reaaliaikaisen liikennetiedon perusteella
6. Älykoti, joka säätää lämmitystä kellonajan perusteella

### Luokkakeskustelu noin 20 minuuttia

1. **Avaus noin 2 minuuttia:**


   Kerro opiskelijoille:

   > Näytän teille kuusi järjestelmää. Pohtikaa jokaisen kohdalla, käyttääkö järjestelmä tekoälyä vai ei. Pelkän äänestyksen sijaan keskitymme perusteluihin.
2. **Käy järjestelmät läpi yksi kerrallaan noin 3 minuuttia järjestelmää kohti.**

   Kysy jokaisen esimerkin kohdalla:

   - Mitä mieltä olette: onko tämä tekoälyä vai ei?
   - Miksi ajattelette näin?
   - Jos opiskelija perustelee vastaustaan sanomalla, että järjestelmä “oppii”, kysy: **Mistä se oppii? Miltä oppiminen tässä tilanteessa näyttäisi?**
   - Jos opiskelija perustelee vastaustaan sanomalla, että järjestelmä on “älykäs”, kysy: **Mitä älykäs tässä tarkoittaa? Onko se sama asia kuin tekoäly?**
3. **Käänteinen esimerkki noin 5 minuuttia:**

   Näytä opiskelijoille seuraava sääntö:

   Jos käyttäjä ei ole kovin aktiivinen, älä näytä hänelle kalliita mainoksia.

   Kysy opiskelijoilta:

   > Voiko tämän toteuttaa tekoälyllä, vai voiko sen tehdä tavallisella ohjelmalla?

   **Keskeinen havainto:** Tämän voi toteuttaa molemmilla tavoilla. Esimerkki on tarkoituksella epämääräinen, joten se ei yksin riitä todistamaan, että kyseessä olisi tekoäly.

**Esimerkki opetukseen**

Kirjoita taululle kaksi kysymystä: “Onko tämä vain sääntö?” ja “Oppiiko järjestelmä datasta?” Näihin palaaminen auttaa opiskelijoita perustelemaan vastauksensa täsmällisemmin.

### Vastaukset ja perustelut, joita opettaja voi tavoitella

| Järjestelmä | Tekoälyä vai ei? | Perustelu |
| --- | --- | --- |
| **Pankkiautomaatti** | Ei yleensä tekoälyä | Se toimii ennalta määriteltyjen sääntöjen mukaan: jos PIN-koodi on oikein, automaatti antaa rahaa. |
| **Automaattinen tekstinkorjaus** | Riippuu toteutuksesta | Voi käyttää tekoälyä, mutta yksinkertainen versio voi perustua sääntöpohjaiseen sanakirjaan. |
| **Suoratoistopalvelun suositukset** | Kyllä | Koneoppimismalli koulutetaan käyttäjäprofiileilla ja katseluhistorialla. |
| **Google Maps ja reaaliaikainen liikennetieto** | Usein kyllä | Järjestelmä hyödyntää reaaliaikaista liikennetietoa ja aiempaa liikennedatahistoriaa reittien arvioinnissa. |
| **Vanha sääntöpohjainen roskapostisuodatin** | Ei, jos se on vain sääntöpohjainen | Jos suodatin perustuu vain ennalta kirjoitettuihin sääntöihin, se ei varsinaisesti opi datasta. Uudemmat sähköpostisuodattimet voivat kuitenkin käyttää tekoälyä. |
| **Älykoti** | Riippuu toteutuksesta | Jos järjestelmä toimii vain kellonajan perusteella, kyse on automaatiosta. Jos se oppii käyttäjän käyttäytymisestä, se voi käyttää tekoälyä. |

### Väärinkäsitykset, joita kannattaa käsitellä

- **“Tekoäly on sama asia kuin automaatio.”**
  Ei aivan. Automaatio toistaa ennalta määriteltyjä toimintoja, kun taas tekoäly hyödyntää dataa ja voi oppia siitä säännönmukaisuuksia.
- **“Tekoäly tarkoittaa, että järjestelmä on monimutkainen.”**
  Ei välttämättä. Monimutkainen ohjelmisto ei automaattisesti ole tekoälyä.
- **“Tekoälyn tulokset ovat aina oikein.”**
  Ei. Tekoäly tekee päätelmiä todennäköisyyksien perusteella ja voi tehdä virheitä.

### Odotettu oppimistulos

Tehtävän jälkeen opiskelijat ymmärtävät, että:

- **tekoäly** vaatii yleensä **dataa** ja jonkinlaista **oppimista**, ei pelkkää automaatiota,
- sama tehtävä voidaan joskus toteuttaa sekä tekoälyllä että sääntöpohjaisella ohjelmalla, mutta toteutustapa on erilainen,
- **älykäs järjestelmä** ja **tekoäly** eivät tarkoita automaattisesti samaa asiaa.

---

## Tehtävä 1.2: Tapaustutkimus — sääntö vai tekoäly petoksentunnistuksessa? — ryhmäharjoitus

### Tavoite

Tehtävän tavoitteena on havainnollistaa, miksi **tekoäly** voi toimia sääntöjä paremmin monimutkaisissa päätöksentekotilanteissa, joissa muuttujia on paljon.

**Opettajan painotus:** Tavoitteena ei ole todistaa, että tekoäly on aina sääntöjä parempi. Tavoitteena on näyttää, että monimutkaisissa tilanteissa pelkät käsin kirjoitetut säännöt voivat olla liian jäykkiä.

### Opettajan ohjeet ja fasilitointi

**Valmistelu noin 10 minuuttia:**

1. Jaa luokka kolmeen ryhmään.
2. Anna jokaiselle ryhmälle sama kymmenen transaktion taulukko opiskelijatehtävästä.
3. Kerro ryhmille heidän tehtävänsä:

- **Ryhmä A:** Kehittäkää viisi sääntöä petoksentunnistukseen.
- **Ryhmä B:** Kehittäkää viisi erilaista sääntöä samaan ongelmaan.
- **Ryhmä C:** Pohtikaa, mitä tekoäly voisi tehdä sellaisessa tilanteessa, johon ryhmien A ja B säännöt eivät välttämättä riitä.

### Toteutus noin 30 minuuttia

1. Ryhmät työskentelevät itsenäisesti noin 15 minuuttia.
2. Ryhmät A ja B esittelevät sääntönsä. Varaa esittelyyn noin 3 minuuttia ryhmää kohti.
3. Kirjoita ryhmien säännöt taululle, jotta niitä voidaan vertailla.
4. Kysy luokalta: **Kuinka monta petosta näillä säännöillä huomattaisiin oikein?**
5. Testaa sääntöjä käytännössä valituilla transaktioilla. Esimerkiksi: “Transaktio 7 on 10 000 euroa ja tehty tuntemattomassa maassa. Luokitteleeko ryhmä A sen petokseksi? Entä ryhmä B?”
6. Ryhmä C esittelee ajatuksensa siitä, miten tekoäly voisi lähestyä ongelmaa. Varaa esittelyyn noin 3 minuuttia.
7. Kysy luokalta:

   - Mitä dataa tekoäly tarvitsisi petosten tunnistamiseen?
   - Mitä kuvioita, yhteyksiä tai poikkeamia tekoäly voisi oppia datasta?
   - Milloin sääntöpohjainen ratkaisu voisi silti olla parempi?
8. **Johtopäätös noin 5 minuuttia:**

   Kirjoita taululle seuraava yhteenveto:

   Säännöt: nopeita ja ennustettavia, mutta usein jäykkiä.

   Koneoppimismalli: koulutetaan datalla tunnistamaan kuvioita, ja se toimii usein kiinteää sääntöä paremmin monimutkaisissa tilanteissa.

### Mahdollisia vastauksia ja väärinkäsityksiä

- **Väärinkäsitys:** “Säännöt ovat aina parempia, koska ne ovat nopeampia.”
  **Täsmennys:** Säännöt voivat olla nopeita ja selkeitä, mutta ne eivät aina tunnista monimutkaisia tai uusia petoskuvioita.
- **Väärinkäsitys:** “Tekoäly tietää, mikä on petos.”
  **Täsmennys:** Tekoäly ei “tiedä” samalla tavalla kuin ihminen. Se havaitsee datasta kuvioita ja poikkeamia, joiden perusteella se tekee todennäköisyysarvioita.

**Opettajan tarkistuskysymys:** Jos opiskelijat ehdottavat yksittäistä sääntöä, kysy: “Toimiiko tämä myös silloin, kun petos näyttää tavalliselta ostokselta tai tavallinen ostos näyttää epäilyttävältä?”

### Odotettu oppimistulos

Tehtävän jälkeen opiskelijat ymmärtävät, että:

- **sääntöjen** laatiminen on vaikeaa, kun päätökseen vaikuttavia muuttujia on paljon,
- **tekoäly** voi havaita datasta kuvioita, joita ihmisen laatimat säännöt eivät välttämättä huomaa,
- sääntöpohjaisella ratkaisulla ja tekoälyllä on molemmilla vahvuuksia ja rajoituksia,
- paras ratkaisu riippuu tilanteesta, tavoitteesta ja käytettävissä olevasta datasta.

---

## Tehtävä 1.3: Omat sovellukset — tekoäly opiskelijoiden arjessa — luokkakeskustelu

### Tavoite

Tehtävän tavoitteena on yhdistää tekoälyyn liittyvä teoria opiskelijoiden omaan digitaaliseen arkeen ja tehdä **tekoälystä** konkreettista.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**

Erillistä valmistelua ei tarvita. Pyydä tunnilla 3–4 opiskelijaa nimeämään yksi sovellus, peli tai digitaalinen palvelu, jota he käyttävät usein.

**Esimerkkejä:**

- YouTube
- Instagram
- Spotify
- WhatsApp
- Fortnite
- Verkkokaupan tuotesuositukset

### Keskustelu noin 15 minuuttia

Käykää jokainen opiskelijoiden mainitsema sovellus läpi samojen kysymysten avulla:

1. **Missä kohtaa tässä sovelluksessa voisi olla tekoälyä?**
   Esimerkiksi suosituksissa, sisällön suodatuksessa, haussa, mainonnassa tai käyttäjien yhdistämisessä.
2. **Miten sovellus voisi päätellä, mitä käyttäjä haluaa nähdä, kuunnella tai tehdä seuraavaksi?**
3. **Millaista dataa sovellus voi kerätä käyttäjän toiminnasta?**
   Korosta, että keskustelun tarkoitus ei ole syyllistää käyttäjiä vaan ymmärtää, että **data** on tekoälyn keskeinen raaka-aine.

### Esimerkkejä keskustelun tueksi

| Sovellus tai palvelu | Missä tekoäly voi näkyä? | Millaista dataa se voi hyödyntää? |
| --- | --- | --- |
| **Instagram** | Suosituksissa, mainonnassa, sisällön järjestämisessä ja sisällön moderoinnissa. | Mitä käyttäjä katsoo, mistä hän tykkää, mitä hän kommentoi ja kuinka pitkään hän pysyy tietyn julkaisun kohdalla. |
| **Spotify** | Suosituksissa, soittolistoissa ja samankaltaisen musiikin ehdottamisessa. | Kuunteluhistoria, ohitetut kappaleet, suosikit, kuunteluajat ja muiden käyttäjien samankaltaiset valinnat. |
| **Fortnite** | Pelaajien yhdistämisessä otteluihin, tasapainottamisessa tai pelidatan analysoinnissa. | Pelaajan taitotaso, otteluhistoria, pelityyli ja suoriutuminen eri tilanteissa. |

### Johtopäätös noin 3 minuuttia

- Tekoäly ei ole vain tulevaisuuden teknologiaa, vaan se näkyy jo monissa opiskelijoiden käyttämissä palveluissa.
- Tekoäly toimii usein taustalla, eikä käyttäjä aina huomaa sitä suoraan.
- Tekoälyn käyttöön liittyy sekä hyötyjä että riskejä, kuten turvallisuus, yksityisyys ja se, miten käyttäjän dataa hyödynnetään.

**Vinkki arviointiin:** Hyvä opiskelijavastaus ei vain nimeä sovellusta, vaan kertoo, mitä dataa sovellus voisi käyttää ja millainen päätös tai suositus datan perusteella tehdään.

### Odotettu oppimistulos

Tehtävän jälkeen opiskelijat ymmärtävät, että:

- **tekoäly** on osa monia arjessa käytettäviä sovelluksia ja palveluita,
- sovellukset voivat käyttää sekä sääntöpohjaisia ratkaisuja että tekoälyä,
- **data** on tekoälyn keskeinen raaka-aine, ja käyttäjät tuottavat sitä päivittäin omalla toiminnallaan.

---

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- erottaa **tekoäly**, **automaatio** ja sääntöpohjainen ohjelmisto toisistaan,
- perustella, miksi jokin järjestelmä käyttää tai ei käytä tekoälyä,
- selittää, miksi tekoäly tarvitsee dataa ja oppimista,
- tunnistaa sääntöpohjaisen ratkaisun ja tekoälyn vahvuuksia sekä rajoituksia,
- yhdistää tekoälyn käsitteet opiskelijoiden omiin digitaalisiin arjen sovelluksiin.

---
