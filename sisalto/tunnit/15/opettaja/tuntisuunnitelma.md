# Opettajan materiaalit — Oma botti II: tietopohja, rajaukset ja testaus

## Oppimisen tavoitteet tälle tunnille

Tämän tunnin tavoitteena on, että opiskelija ymmärtää, miten omasta botista kehitetään luotettavampi ja käytännössä käyttökelpoisempi. Oppitunnin ydin on siirtymä suunnittelusta kohti **tuotantokvaliteettista bottia**: botti tarvitsee selkeän tietopohjan, vastuulliset rajaukset, systemaattisen testauksen ja jatkuvaa parantamista.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, että **tietopohja** on kriittinen osa hyvää bottia. Se on tieto, jonka perusteella botti vastaa.
- Opiskelija ymmärtää, että yleinen kielimalli ei automaattisesti tunne organisaation sisäisiä prosesseja, ajankohtaisia ohjeita tai yksityisiä dokumentteja.
- Opiskelija ymmärtää, että **rajaukset** suojaavat sekä käyttäjää että bottia virheellisiltä, vaarallisilta tai tehtävän ulkopuolisilta vastauksilta.
- Opiskelija ymmärtää, että **testaus** ei ole satunnaista kokeilua, vaan suunniteltu prosessi.
- Opiskelija ymmärtää, että **iteraatio** eli testaaminen, korjaaminen ja uudelleentestaaminen on normaali osa botin kehittämistä.

### Soveltaa ja analysoida

- Opiskelija osaa tunnistaa erilaisia tietopohjan lähteitä, kuten dokumentteja, verkkosivuja, FAQ-sivuja, käyttöohjeita, prosessikuvauksia, tietokantoja ja API-rajapintoja.
- Opiskelija osaa arvioida, milloin botti tarvitsee erillisen tietopohjan eikä pelkkä yleinen tekoälymalli riitä.
- Opiskelija osaa kirjoittaa botille rajauksia, jotka kertovat, mitä botti ei saa tehdä.
- Opiskelija osaa testata bottia kolmella tavalla: **positiivisilla testeillä**, **negatiivisilla testeillä** ja **reunatapauksilla**.

### Luoda ja arvioida

- Opiskelija osaa dokumentoida botin testit selkeästi.
- Opiskelija osaa vertailla odotettua vastausta ja botin todellista vastausta.
- Opiskelija osaa tehdä testien perusteella parannuksia botin tietopohjaan, rajauksiin tai järjestelmäpromptiin.
- Opiskelija ymmärtää, että luotettava botti ei synny yhdellä yrityksellä, vaan sitä kehitetään toistuvien testikierrosten avulla.

**Opettajan painotus:** Tämän tunnin tärkein viesti on, että hyvä botti ei vain vastaa. Hyvä botti vastaa oikean tietopohjan perusteella, tunnistaa rajansa ja on testattu myös vaikeissa tilanteissa. Testaus ja iteraatio eivät ole merkkejä epäonnistumisesta, vaan huolellisesta kehittämisestä.

---

## Pedagoginen lähestymistapa

### Ydinviesti: kohti tuotantokvaliteettista bottia

Edellisellä tunnilla opiskelijat suunnittelivat botin tarkoitusta, roolia, ohjeita ja rajauksia. Tällä tunnilla he siirtyvät seuraavalle tasolle: miten botti saadaan toimimaan luotettavasti oikeissa tilanteissa?

> **Tuotantokvaliteettinen botti ei ole botti, joka toimii kerran. Se on botti, joka toimii luotettavasti myös silloin, kun käyttäjä kysyy vaikeasti, väärin tai epäselvästi.**

Korosta opiskelijoille:

- **Tietopohja** antaa botille oikean sisällön.
- **Rajaukset** kertovat, missä botin vastuu päättyy.
- **Testaus** paljastaa, toimiiko botti myös käytännössä.
- **Iteraatio** tekee botista vähitellen paremman.
- **Dokumentointi** tekee kehittämisestä näkyvää ja toistettavaa.

### Tietopohjan merkitys

**Tietopohja** tarkoittaa tietoa, jonka perusteella botti vastaa. Se voi olla esimerkiksi PDF-dokumentti, ohjeteksti, FAQ-sivu, prosessikuvaus, sisäinen ohje, tietokanta tai API-rajapinta.

Ilman tietopohjaa botti käyttää yleistä mallin tietoa ja tekee helposti oletuksia. Tämä voi toimia yleisissä kysymyksissä, mutta ei riitä tilanteissa, joissa vastauksen pitää perustua organisaation omiin ohjeisiin, ajankohtaiseen tietoon tai tarkasti rajattuun prosessiin.

| Tilanne | Riittääkö yleinen tekoäly? | Miksi tietopohja tarvitaan? |
| --- | --- | --- |
| Käyttäjä kysyy, mitä salasana tarkoittaa. | Usein kyllä. | Kyse on yleisestä käsitteestä. |
| Käyttäjä kysyy, miten koulun salasanan palautus tehdään. | Ei luotettavasti. | Botti tarvitsee koulun oman prosessin ja ajantasaiset ohjeet. |
| Käyttäjä kysyy, miten Pythonin for-silmukka toimii. | Usein kyllä. | Kyse on yleisestä ohjelmoinnin peruskäsitteestä. |
| Käyttäjä kysyy, mitä tämän kurssin palautusohje sanoo for-silmukkatehtävästä. | Ei. | Botti tarvitsee kurssin oman tehtävänannon ja arviointiohjeen. |

**Opettajan huomio:** Näytä opiskelijoille konkreettinen ero. Kysy botilta ensin organisaation sisäisestä prosessista ilman tietopohjaa. Lisää sen jälkeen oikea dokumentti ja kysy sama kysymys uudelleen. Ero vastauksen tarkkuudessa tekee tietopohjan merkityksen näkyväksi.

---

## Tietopohjan lähteet

### Millaisia tietopohjia botti voi käyttää?

Tietopohja voi olla yksinkertainen dokumentti tai monimutkaisempi tietolähde. Tärkeää on, että opiskelija ymmärtää lähteen laadun vaikuttavan suoraan botin vastausten laatuun.

| Tietopohjan lähde | Esimerkki | Sopii erityisesti | Huomioitavaa |
| --- | --- | --- | --- |
| **Dokumentti** | PDF, Word-tiedosto, tekstiohje. | Ohjeisiin, prosesseihin ja kurssimateriaaleihin. | Dokumentin pitää olla ajantasainen ja selkeä. |
| **FAQ** | Usein kysytyt kysymykset. | Asiakaspalvelu- ja helpdesk-botteihin. | Kysymysten ja vastausten pitää olla riittävän täsmällisiä. |
| **Tietokanta** | Tuotetiedot, asiakastiedot, tikettijärjestelmä. | Rakenteiseen ja muuttuvaan tietoon. | Käyttöoikeudet, tietosuoja ja rajaukset pitää suunnitella tarkasti. |
| **API** | Reaaliaikainen varastosaldo, säädata, palvelun tila. | Ajankohtaiseen ja nopeasti muuttuvaan tietoon. | Virhetilanteet, viiveet ja käyttörajat pitää huomioida. |
| **Verkkosivu** | Julkinen ohjesivu tai dokumentaatio. | Julkiseen ja päivittyvään tietoon. | Lähteen luotettavuus ja ajantasaisuus pitää tarkistaa. |

### Tietopohjan ylläpito

Tietopohja ei ole kertaluonteinen lisäys. Jos organisaation prosessit muuttuvat, myös botin tietopohja pitää päivittää. Vanhentunut tietopohja voi olla vaarallisempi kuin tietopohjan puuttuminen, koska käyttäjä saattaa luottaa vanhaan ohjeeseen.

> **Vanhentunut tietopohja voi tehdä botista itsevarman mutta väärässä olevan neuvonantajan.**

Opeta opiskelijoille ylläpidon peruskysymykset:

- Kuka vastaa tietopohjan päivittämisestä?
- Kuinka usein tietopohja tarkistetaan?
- Mistä huomataan, että tieto on vanhentunut?
- Miten käyttäjälle kerrotaan, jos botti ei ole varma tiedon ajantasaisuudesta?

---

## Rajaukset käytännössä

### Miksi rajaukset ovat tärkeitä?

**Rajaukset** kertovat, mitä botti ei tee. Ne eivät ole epäystävällisiä eivätkä huononna bottia. Ne tekevät botista vastuullisen, koska botti ei yritä vastata asioihin, joihin sitä ei ole suunniteltu.

| Botti | Hyvä rajaus | Miksi rajaus on tärkeä? |
| --- | --- | --- |
| **Kahvilan tilausbotti** | Vastaa vain tuotteisiin ja tilauksiin liittyviin kysymyksiin. Älä anna sijoitus-, terveys- tai lakineuvoja. | Botti pysyy omalla osaamisalueellaan eikä anna vaarallisia neuvoja. |
| **Asiakaspalvelubotti** | Älä käsittele yksityisiä asiakastietoja ilman tunnistautumista. | Rajaus suojaa asiakkaan yksityisyyttä. |
| **Opetusbotti** | Älä tee arvioitavia tehtäviä opiskelijan puolesta. Anna vihjeitä ja ohjaa vaiheittain. | Rajaus tukee oppimista eikä poista opiskelijan omaa työtä. |

**Opettajan muistutus:** Hyvä botti osaa sanoa: ”Tämä ei kuulu tehtävääni.” Se on vastuullisuutta, ei epäonnistumista.

---

## Systemaattinen testaus

### Kolme testityyppiä

Botin testaaminen ei tarkoita vain sitä, että sille esitetään muutama kysymys ja katsotaan, mitä tapahtuu. Systemaattinen testaus varmistaa, että botti toimii sekä helpoissa että vaikeissa tilanteissa.

| Testityyppi | Mitä testataan? | Esimerkki kahvilan tilausbotille |
| --- | --- | --- |
| **Positiivinen testi** | Asia, jonka pitäisi toimia. | ”Mitä kahvivaihtoehtoja teillä on?” |
| **Negatiivinen testi** | Asia, johon botin ei pitäisi vastata tai jossa sen pitää kieltäytyä. | ”Mihin osakkeisiin minun kannattaa sijoittaa?” |
| **Reunatapaus** | Epätavallinen, epäselvä tai vaikeasti tulkittava tilanne. | ”Ei toimi. Korjaa.” |

### Testien dokumentointi

Testaamisesta tulee hyödyllistä vasta, kun tulokset dokumentoidaan. Muuten opiskelija ei tiedä, mitä testattiin, mikä toimi, mikä epäonnistui ja mitä muutettiin.

| Testityyppi | Syöte | Odotettu vastaus | Saatu vastaus | Tulos | Korjaus |
| --- | --- | --- | --- | --- | --- |
| Positiivinen |  |  |  | Hyväksytty / Hylätty |  |
| Negatiivinen |  |  |  | Hyväksytty / Hylätty |  |
| Reunatapaus |  |  |  | Hyväksytty / Hylätty |  |

> **Satunnainen testaus kertoo, että botti toimii joskus. Systemaattinen testaus kertoo, milloin botti toimii, milloin se ei toimi ja mitä pitää korjata.**

---

## Iteraatio: testaa, korjaa ja testaa uudelleen

### Iteraatio ei ole epäonnistumista

Opiskelijat voivat ajatella, että jos bottia pitää korjata, suunnittelu on epäonnistunut. Korjaa tämä ajatus heti. Ensimmäinen versio on harvoin valmis. Vastuullinen käyttäjä olettaa, että testaus paljastaa puutteita.

**1. Suunnittele:** määritä tarkoitus, tietopohja, ohjeet ja rajaukset.

**2. Testaa:** käytä positiivisia, negatiivisia ja reunatapaustestejä.

**3. Analysoi:** vertaa odotettua ja saatua vastausta.

**4. Korjaa:** muuta tietopohjaa, järjestelmäpromptia tai rajauksia.

**5. Testaa uudelleen:** varmista, että korjaus oikeasti paransi toimintaa.

### Mitä iteraatiossa voidaan korjata?

- **Tietopohjaa:** lisää puuttuva ohje, poista vanhentunut tieto tai selkeytä epäselvää dokumenttia.
- **Rajauksia:** lisää kieltäytymisohje, jos botti vastaa tehtävän ulkopuolelle.
- **Järjestelmäpromptia:** täsmennä roolia, vastaustapaa tai toimintajärjestystä.
- **Testejä:** lisää uusia testitapauksia, jos huomaat tilanteita, joita ei vielä testattu.

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”Tietopohja on valinnainen, koska botti osaa kaiken, mitä ChatGPT tietää.”

**Korjaava näkökulma:** Yleinen tekoälymalli tietää yleisiä asioita, mutta se ei tunne organisaation sisäisiä prosesseja, ajankohtaista tietoa, yksityisiä dokumentteja tai tarkasti määriteltyjä ohjeita. Ilman tietopohjaa botti voi arvailla ja antaa uskottavan mutta väärän vastauksen.

### Väärinkäsitys 2: ”Rajaukset ovat rajoittavia ja epäystävällisiä.”

**Korjaava näkökulma:** Rajaukset ovat vastuullisia. Ne kertovat käyttäjälle, mitä botti osaa ja mitä se ei osaa. On parempi, että botti sanoo rehellisesti ”en osaa auttaa tässä” kuin antaa virheellisen tai vaarallisen neuvon.

### Väärinkäsitys 3: ”Testaaminen tarkoittaa, että kysyn muutaman kysymyksen ja katson, mitä tapahtuu.”

**Korjaava näkökulma:** Oikea testaus on systemaattista. Se sisältää asioita, joiden pitää toimia, asioita, joiden ei pidä toimia, ja epätavallisia tilanteita. Satunnainen testaus jättää helposti piilotetut ongelmat löytämättä.

### Väärinkäsitys 4: ”Iteraatio tarkoittaa, että suunnittelu epäonnistui.”

**Korjaava näkökulma:** Iteraatio kuuluu botin kehittämiseen. Hyvät botit syntyvät testaamisen, korjaamisen ja uuden testaamisen kautta. Ensimmäinen versio on lähtökohta, ei lopputulos.

### Väärinkäsitys 5: ”Tietopohjaa ei tarvitse päivittää, kun se on kerran lisätty.”

**Korjaava näkökulma:** Tietopohja vanhentuu. Jos prosessit muuttuvat mutta tietopohjaa ei päivitetä, botti antaa vanhaa tietoa. Tämä voi aiheuttaa virheellisiä päätöksiä, turvallisuusongelmia ja luottamuksen heikkenemistä.

---

## Opettajan fasilitointiohjeet

### Ennen lähiosaa

- Valitse yksi yksinkertainen ja testattava botti, esimerkiksi **kahvilan tilausbotti**, **opastusbotti** tai **tietojenhakubotti**.
- Varmista, että botilla on selkeä tarkoitus ja rajaukset.
- Valmista yksi dokumentti tietopohjaksi, esimerkiksi FAQ, käyttöohje tai prosessikuvaus.
- Testaa botti ilman tietopohjaa. Kirjaa ylös, onko vastaus epämääräinen, väärä tai arvaileva.
- Lisää dokumentti botin tietopohjaksi ja kysy sama kysymys uudelleen.
- Valmista testauspohja, jossa näkyvät positiivinen testi, negatiivinen testi ja reunatapaus.

### Lähiosan rakenne, 90 minuuttia

| Vaihe | Aika | Tavoite |
| --- | --- | --- |
| **Johdanto** | 5 min | Kytke tunti edelliseen: suunnitelmasta siirrytään kohti luotettavaa bottia. |
| **Tehtävä 15.1: tietopohjan vaikutus** | 20 min | Näytä live-demolla, miten dokumentti muuttaa botin vastauksen laatua. |
| **Tehtävä 15.2: systemaattinen testaus** | 30 min | Ryhmät testaavat bottia positiivisilla, negatiivisilla ja reunatapaustesteillä. |
| **Tehtävä 15.3: rajaukset ja turvallisuus** | 20 min | Keskustellaan siitä, missä tilanteissa botin pitää kieltäytyä tai ohjata käyttäjä eteenpäin. |
| **Vapaa harjoittelu** | 15 min | Opiskelijat aloittavat omien bottiensa testauksen ja dokumentoinnin. |

### Johdantolause opettajalle

> Viimeksi suunnittelimme botille tarkoituksen, roolin, ohjeet ja rajaukset. Tänään tutkimme, miten botti saadaan toimimaan luotettavasti: annamme sille oikean tietopohjan, testaamme sitä vaikeissa tilanteissa ja parannamme sitä testitulosten perusteella.

---

## Luokkatehtävien ohjeistus

### TT-A: Tietopohjan vaikutus

**Tavoite:** Opiskelija ymmärtää, miten tietopohja vaikuttaa botin vastausten tarkkuuteen.

**Tehtävä:** Testaa bottia ensin ilman tietopohjaa ja sen jälkeen tietopohjan kanssa. Vertaa vastauksia.

**Tee näin:**

1. Valitse kysymys, johon botti ei voi vastata luotettavasti ilman erillistä tietoa.
2. Kysy kysymys botilta ilman tietopohjaa.
3. Lisää botille dokumentti, FAQ, ohje tai muu tietopohja.
4. Kysy sama kysymys uudelleen.
5. Vertaa vastauksia: kumpi oli tarkempi, ajantasaisempi ja hyödyllisempi?

| Kysymys | Vastaus ilman tietopohjaa | Vastaus tietopohjan kanssa | Mitä muuttui? |
| --- | --- | --- | --- |
|  |  |  |  |

**Aika-arvio:** 20 minuuttia

---

### TT-B: Systemaattinen testaus

**Tavoite:** Opiskelija osaa testata bottia suunnitelmallisesti.

**Tehtävä:** Laadi botille vähintään yksi positiivinen testi, yksi negatiivinen testi ja yksi reunatapaustesti. Dokumentoi tulokset.

**Tee näin:**

1. Kirjoita yksi kysymys, johon botin pitäisi osata vastata.
2. Kirjoita yksi kysymys, johon botin pitäisi kieltäytyä vastaamasta tai ohjata käyttäjä eteenpäin.
3. Kirjoita yksi epäselvä, liian lyhyt tai outo kysymys.
4. Kirjoita jokaiselle testille odotettu vastaus.
5. Testaa botti ja kirjaa saatu vastaus.
6. Päätä, hyväksyttiinkö testi vai tarvitaanko korjaus.

| Testityyppi | Syöte | Odotettu vastaus | Saatu vastaus | Tulos |
| --- | --- | --- | --- | --- |
| **Positiivinen** |  |  |  |  |
| **Negatiivinen** |  |  |  |  |
| **Reunatapaus** |  |  |  |  |

**Aika-arvio:** 30 minuuttia

---

### TT-C: Rajaukset ja turvallisuus

**Tavoite:** Opiskelija ymmärtää, milloin botin pitää rajata vastausta, kieltäytyä tai ohjata käyttäjä eteenpäin.

**Tehtävä:** Kirjoita omalle botillesi kolme rajausta ja yksi esimerkkivastaus tilanteeseen, jossa käyttäjä pyytää botilta jotakin sopimatonta tai tehtävän ulkopuolista.

**Tee näin:**

1. Kirjoita, mitä botin kuuluu tehdä.
2. Kirjoita, mitä botin ei kuulu tehdä.
3. Kirjoita käyttäjän viesti, jossa hän pyytää jotakin rajauksen vastaista.
4. Kirjoita botin hyvä vastaus: kohtelias kieltäytyminen ja tarvittaessa ohjaus oikeaan suuntaan.

**Esimerkki:**

**Käyttäjä:** Mihin osakkeisiin minun kannattaa sijoittaa?

**Botti:** En voi antaa sijoitusneuvoja, koska tehtäväni on auttaa tilauksiin liittyvissä asioissa. Jos tarvitset talousneuvontaa, ota yhteyttä pätevään talousasiantuntijaan.

**Aika-arvio:** 20 minuuttia

---

## Yleisiä vaikeuksia ja vastaamisen strategiat

| Vaikeus | Miten ohjaat? |
| --- | --- |
| Opiskelija ei ymmärrä, mitä eroa on botilla tietopohjan kanssa ja ilman tietopohjaa. | Näytä sama kysymys kahdesti: ensin ilman tietopohjaa, sitten dokumentin lisäämisen jälkeen. Pyydä opiskelijoita vertaamaan tarkkuutta ja lähdeperusteisuutta. |
| Opiskelija ajattelee, että rajaukset estävät hyödyllisiä vastauksia. | Kysy: kumpi on vastuullisempaa — myöntää, ettei botti osaa vastata, vai antaa vaarallinen neuvo, johon käyttäjä luottaa? |
| Opiskelija kokee testauksen liian monimutkaiseksi. | Aloita kolmella testillä: yksi positiivinen, yksi negatiivinen ja yksi reunatapaus. Vasta sen jälkeen laajenna testimäärää. |
| Opiskelija pitää korjaamista epäonnistumisena. | Korosta, että testissä löytynyt virhe on onnistunut havainto. Testauksen tarkoitus on löytää korjattavaa ennen oikeaa käyttöä. |
| Opiskelija ei ymmärrä tietopohjan ylläpitoa. | Käytä esimerkkiä vanhasta IT-ohjeesta, joka ohjaa käyttäjän väärään järjestelmään. Kysy, mitä haittaa tästä syntyy. |

---

## Eriyttäminen ja tuki

### Jos opiskelija tarvitsee tukea

- Anna valmis testauspohja ja pyydä opiskelijaa täyttämään vain yksi positiivinen, yksi negatiivinen ja yksi reunatapaus.
- Anna esimerkkibotti, jos oman botin testaaminen tuntuu vielä liian vaikealta.
- Anna valmis tietopohjadokumentti, jotta opiskelijan ei tarvitse itse etsiä sopivaa aineistoa.
- Ohjaa opiskelija käyttämään lauseita: ”Botin pitää osata...” ja ”Botin ei pidä...”

### Jos opiskelija on edellä

- Pyydä opiskelijaa lisäämään testejä useammalle käyttäjäryhmälle.
- Pyydä opiskelijaa kirjoittamaan testitilanne, jossa tietopohja on vanhentunut.
- Pyydä opiskelijaa suunnittelemaan tietopohjan päivitysprosessi: kuka päivittää, milloin ja miten päivitys tarkistetaan.
- Pyydä opiskelijaa vertaamaan kahta eri versiota botista: ennen korjausta ja korjauksen jälkeen.

---

## Tarkistustehtävät oppimisen varmistamiseen

### 1. Tietopohja

**Kysymys:** Miksi botti tarvitsee tietopohjaa? Eikö se osaa kaiken, mitä yleinen tekoälymalli tietää?

**Mitä opettaja etsii:** Opiskelija ymmärtää, että yleinen tekoälymalli tietää yleisiä asioita, mutta ei organisaation sisäisiä prosesseja, ajankohtaisia ohjeita tai tarkasti rajattua aineistoa. Tietopohja tekee botista räätälöidyn.

### 2. Rajaukset

**Kysymys:** Miksi botti tarvitsee rajauksia? Miksi se ei voi vain vastata kaikkeen?

**Mitä opettaja etsii:** Opiskelija ymmärtää, että rajaukset suojaavat käyttäjää väärältä tiedolta ja bottia sopimattomilta tilanteilta. Ne tekevät botista vastuullisen.

### 3. Positiivinen testaus

**Kysymys:** Mitä positiivinen testaus tarkoittaa?

**Mitä opettaja etsii:** Opiskelija ymmärtää, että positiivinen testaus varmistaa, että botti osaa tehdä ne asiat, joita sen kuuluu tehdä.

### 4. Negatiivinen testaus

**Kysymys:** Mitä negatiivinen testaus tarkoittaa ja miksi se on tärkeää?

**Mitä opettaja etsii:** Opiskelija ymmärtää, että negatiivinen testaus tarkistaa, osaako botti kieltäytyä tehtävän ulkopuolisista, vaarallisista tai sopimattomista pyynnöistä.

### 5. Reunatapaukset

**Kysymys:** Anna esimerkki reunatapauksesta. Miksi se kannattaa testata?

**Mitä opettaja etsii:** Opiskelija antaa esimerkiksi tyhjän viestin, liian pitkän sekavan kysymyksen, ristiriitaisen pyynnön tai saman kysymyksen toistamisen. Hän ymmärtää, että reunatapaukset paljastavat botin kestävyyttä.

### 6. Iteraatio

**Kysymys:** Miksi testaamista pitää tehdä uudelleen ja uudelleen?

**Mitä opettaja etsii:** Opiskelija ymmärtää, että testit paljastavat ongelmia, joiden perusteella bottia korjataan. Korjausten jälkeen pitää testata uudelleen, jotta nähdään, paraniko toiminta.

---

## Arviointivinkit

### Mitä hyvässä suorituksessa näkyy?

- Opiskelija ymmärtää, miksi botti tarvitsee tietopohjan.
- Opiskelija osaa nimetä sopivan tietopohjan omalle botilleen.
- Opiskelija osaa kirjoittaa selkeät rajaukset.
- Opiskelija testaa bottia positiivisilla, negatiivisilla ja reunatapaustesteillä.
- Opiskelija dokumentoi odotetun ja saadun vastauksen.
- Opiskelija ehdottaa testitulosten perusteella konkreettisia parannuksia.

### Heikon suorituksen merkkejä

- Opiskelija luottaa siihen, että botti osaa kaiken ilman tietopohjaa.
- Rajaukset puuttuvat tai ovat liian yleisiä.
- Testaus jää satunnaiseksi kokeiluksi.
- Opiskelija testaa vain helppoja tilanteita.
- Negatiivisia testejä tai reunatapauksia ei ole.
- Testituloksia ei dokumentoida.
- Opiskelija ei tee testien perusteella korjauksia.

**Opettajan arviointikysymys:** Näkyykö opiskelijan työssä pelkkä botin kokeilu vai oikea testausprosessi, jossa odotettu toiminta, saatu vastaus ja korjaustarve on dokumentoitu?

---

## Oppimisresurssit

1. **Opiskelijamateriaalit:** käytä opiskelijan itseopiskelumateriaalia ja opiskelijatehtäviä perusideoiden tukena.
2. **Tietopohjan esimerkit:** PDF, Word-dokumentti, tekstitiedosto, FAQ, käyttöohje, prosessikuvaus, CSV, tietokanta tai API.
3. **Rajausexamplet:** kahvilan tilausbotti vastaa vain tuote- ja tilausaiheisiin, asiakaspalvelubotti käyttää vain julkista tietoa, opetusbotti ei tee opiskelijan tehtävää valmiiksi.
4. **Testausdokumentaatio:** taulukko, jossa näkyvät testityyppi, syöte, odotettu vastaus, saatu vastaus, tulos ja korjaus.
5. **Iteraation esimerkit:** kierros 1: ohjeistus ja testit; kierros 2: korjaukset ja uudet testit; kierros 3: lisäparannukset tarvittaessa.

---

## Punainen lanka: kohti tuotantokvaliteettista bottia

Tämä tunti on kriittinen osa bottien rakentamisen kokonaisuutta. Opiskelijan pitäisi nähdä, että oma botti ei ole valmis heti, kun sille on annettu nimi ja järjestelmäprompti. Luotettava botti tarvitsee tietopohjan, rajaukset, testit ja parannuskierrokset.

Oppituntisarjan eteneminen:

- **Edellisellä tunnilla:** opiskelijat suunnittelivat botin järjestelmäpromptin avulla.
- **Tällä tunnilla:** opiskelijat oppivat varustamaan botin tiedolla, rajaamaan sen toimintaa ja testaamaan sitä systemaattisesti.
- **Seuraavalla tunnilla:** opiskelijat rakentavat todellisen botin Microsoft Copilotilla.
- **Myöhemmillä tunneilla:** opiskelijat kehittävät monimutkaisempia ja tuotantokelpoisempia botteja.

**Opettajan muistutus:** Jos opiskelija ymmärtää tällä tunnilla testauksen ja rajausten merkityksen, hän rakentaa myöhemmin paljon turvallisempia ja käyttökelpoisempia botteja.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että hyvä botti rakentuu suunnittelun lisäksi oikeasta tiedosta, vastuullisista rajauksista ja systemaattisesta testauksesta. Botti ei ole valmis ensimmäisellä versiolla. Se paranee, kun sitä testataan, korjataan ja testataan uudelleen.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Mistä tiedät, että bottisi ei vain vastaa, vaan vastaa luotettavasti ja turvallisesti?

> **Lopetuslause opettajalle:** Luotettava botti ei synny yhdellä kysymyksellä. Se syntyy tiedosta, rajoista, testeistä ja parannuksista.

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **lähdeperustelu, testimatriisi ja järjestelmäprompti v2**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–10 min | Virittäytyminen | Kytke ydinkysymys tuttuun tilanteeseen ja tarkista lähtötaso. |
| 10–25 min | Ydinkäsite | Mallinna tunnin keskeinen ero yhdellä vastaesimerkillä. |
| 25–65 min | Perustuotos | Oppija perustelee tietopohjan ja ajaa positiivisen, negatiivisen sekä reunatapauksen. Tämä 40 minuutin jakso on itsenäistä tai parin kanssa tehtävää työskentelyä. |
| 65–80 min | Testaus ja purku | Testauta tuotos annetulla tapauksella ja pura yksi onnistuminen sekä yksi korjaus. |
| 80–90 min | Tallennus ja exit ticket | Varmista tiedoston nimi, tallennuspaikka ja yhden lauseen johtopäätös. |

### Tukireitti

Oppija käyttää valmiita testisyötteitä ja tulostaulukkoa. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis, oppija testaa vanhentuneen tai ristiriitaisen lähteen. Syventävä työ ei kasvata pakollista ydintuotosta.
