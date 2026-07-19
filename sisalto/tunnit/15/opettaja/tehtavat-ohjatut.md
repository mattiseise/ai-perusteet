# Opettajavetoiset tehtävät — oma botti II

## Tehtävä 15.1: Live-demo — tietopohjan lisääminen botille noin 20 minuuttia

### Tavoite

Tehtävän tavoitteena on osoittaa konkreettisesti, miten **tietopohja** lisätään bottiin ja miten se vaikuttaa botin vastausten tarkkuuteen, ajantasaisuuteen ja luotettavuuteen.

**Opettajan painotus:** Korosta, että tietopohja ei tee botista automaattisesti virheetöntä. Se voi parantaa vastausten laatua, mutta vain silloin, kun tietopohja on oikea, ajantasainen ja turvallinen käyttää.

### Opettajan ohjeet ja fasilitointi

Tämä tehtävä tehdään opettajan johdolla koko luokan kanssa. Käytä esimerkiksi Microsoft Copilot -agenttia tai muuta tekoälytyökalua, johon voidaan lisätä dokumentteja **tietopohjaksi**.

### Valmistelu ennen lähiosaa

- Valmista yksinkertainen dokumentti, esimerkiksi FAQ, käyttöohje tai lyhyt organisaation sisäinen ohje.
- Testaa etukäteen, miten botti vastaa ilman tietopohjaa.
- Testaa sen jälkeen, miten botti vastaa, kun sama dokumentti on lisätty tietopohjaksi.
- Valmista kolme kysymystä:
  - yksi kysymys, johon vastaus löytyy suoraan tietopohjasta,
  - yksi kysymys, johon vastaus löytyy tietopohjasta vain osittain,
  - yksi kysymys, johon tietopohja ei vastaa.
- Varmista, ettei käytettävä dokumentti sisällä salasanoja, henkilötietoja, asiakastietoja tai muuta arkaluonteista sisältöä.

### Tehtävän vaiheet noin 20 minuuttia

#### Vaihe 1: Johdanto noin 2 minuuttia

Kerro opiskelijoille:

> Edellisellä oppitunnilla opimme kirjoittamaan hyvän järjestelmäpromptin. Nyt tarkastelemme seuraavaa ongelmaa: botti osaa vastata vain sen tiedon perusteella, joka sillä on käytettävissään.

Jatka:

> Jos haluamme, että botti vastaa tarkasti organisaation omista ohjeista, tuotteista tai prosesseista, sille pitää antaa **tietopohja**. Tietopohja tarkoittaa dokumentteja, ohjeita tai muuta aineistoa, jota botti saa käyttää vastaustensa tukena.

#### Vaihe 2: Botti ilman tietopohjaa noin 4 minuuttia

1. Kysy botilta kysymys, joka liittyy valitsemaasi dokumenttiin tai organisaation sisäiseen prosessiin.
2. Käytä esimerkiksi muotoa: `Mikä on [organisaation sisäinen prosessi tai palvelu]?`
3. Näytä opiskelijoille botin vastaus.
4. Korosta, jos vastaus on yleinen, epämääräinen, arvaileva tai puutteellinen.

Kysy opiskelijoilta:

- Mistä huomaa, ettei botilla ole tarkkaa tietoa?
- Arvaileeko botti vai kertooko se, ettei tiedä?
- Voisiko tällaiseen vastaukseen luottaa asiallisessa käytössä?

#### Vaihe 3: Tietopohjadokumentin lisääminen noin 5 minuuttia

Näytä opiskelijoille, miten dokumentti lisätään botin tietopohjaan.

Selitä vaiheet selkeästi:

1. Avaa botin (esim. Copilot-agentin) hallintanäkymä.
2. Valitse kohta, jossa voidaan lisätä tiedostoja tai tietopohjadokumentteja.
3. Lisää dokumentti, esimerkiksi PDF-, Word- tai tekstitiedosto.
4. Odota, että järjestelmä käsittelee tai indeksoi dokumentin.
5. Tallenna muutokset ja palaa botin testaukseen.

Kysy opiskelijoilta:

- Miksi dokumentin sisältö pitää tarkistaa ennen lataamista?
- Mitä tietoja ei saa lisätä botin tietopohjaan?
- Kuka vastaa siitä, että tietopohja on oikea ja turvallinen?

**Opettajan tarkistuskysymys:** Jos opiskelijat ajattelevat, että dokumentin lisääminen riittää, kysy: “Mitä tapahtuu, jos dokumentti on väärä, vanhentunut tai sisältää arkaluonteista tietoa?”

#### Vaihe 4: Sama kysymys uudelleen noin 4 minuuttia

1. Kysy botilta sama kysymys kuin ennen tietopohjan lisäämistä.
2. Näytä uusi vastaus opiskelijoille.
3. Vertailkaa vastausta aiempaan vastaukseen.

Kysy opiskelijoilta:

- Mikä muuttui vastauksessa?
- Onko vastaus tarkempi?
- Viittaako botti dokumentissa olevaan tietoon?
- Onko vastaus silti tarkistettava?

Korosta:

> Tietopohja tekee botista hyödyllisemmän, koska se voi vastata organisaation omien dokumenttien perusteella. Se ei kuitenkaan poista ihmisen vastuuta tarkistaa, että tieto on oikein.

#### Vaihe 5: Tietopohjan rajaukset ja vastuu noin 3 minuuttia

Selitä opiskelijoille:

> Tietopohja on hyödyllinen, mutta siihen liittyy myös vastuu. Jos dokumentissa on virhe, botti voi toistaa virheen. Jos dokumentti on vanhentunut, botti voi antaa vanhentunutta tietoa.

Kysy opiskelijoilta:

- Mitä tapahtuu, jos tietopohjassa on virhe?
- Mitä tapahtuu, jos dokumentti on kuusi kuukautta vanha ja prosessi on muuttunut?
- Miten tietopohjan ajantasaisuus voidaan varmistaa?

**Keskeinen havainto:** Tietopohja täytyy pitää ajan tasalla, ja sen sisällölle pitää olla omistaja tai vastuuhenkilö.

#### Vaihe 6: Yhteenveto noin 2 minuuttia

Näytä opiskelijoille kaava:

Hyvä botti = hyvät ohjeet + ajantasainen tietopohja + selkeät rajaukset

Kerro opiskelijoille:

> Ilman tietopohjaa botti on usein yleinen tekoälyavustaja. Tietopohjan avulla siitä voi tulla räätälöity järjestelmä, joka vastaa tietyn organisaation, kurssin tai tehtävän tarpeisiin.

### Odotettu oppimistulos

- Opiskelijat näkevät, miten tietopohja lisätään bottiin käytännössä.
- Opiskelijat ymmärtävät, että tietopohja voi parantaa botin vastausten tarkkuutta.
- Opiskelijat ymmärtävät, että tietopohja pitää tarkistaa, suojata ja päivittää säännöllisesti.
- Opiskelijat osaavat selittää, miksi hyvä botti tarvitsee sekä ohjeet että luotettavan tietopohjan.

---

## Tehtävä 15.2: Ryhmäharjoitus — botin testaaminen kolmella tavalla noin 30 minuuttia

### Tavoite

Tehtävän tavoitteena on opettaa opiskelijoille, että botin testaaminen on **systemaattista** työtä. Opiskelijat testaavat bottia kolmella tavalla: **positiivisilla testeillä**, **negatiivisilla testeillä** ja **reunatapaustesteillä**.

**Opettajan painotus:** Korosta, että testaaminen ei ole vain sitä, että kokeillaan, toimiiko botti normaalissa tilanteessa. Hyvä testaaja selvittää myös, mitä botti tekee väärissä, epäselvissä ja odottamattomissa tilanteissa.

### Opettajan ohjeet ja fasilitointi

Tehtävä tehdään 2–3 opiskelijan pienryhmissä. Jokainen ryhmä voi testata samaa opettajan valmistamaa bottia tai omaa aiemmin suunnittelemaansa bottia.

### Valmistelu

- Valmista yksinkertainen testattava botti, esimerkiksi **kahvilan tilausbotti** tai **opiskelun ohjausbotti**.
- Valmista testauspohja, jossa on kohdat positiivisille testeille, negatiivisille testeille ja reunatapauksille.
- Valmista lyhyt ohje siitä, mitä jokaisessa testityypissä tarkkaillaan.

### Testauspohja opiskelijoille

| Testityyppi | Kysymys tai tilanne | Odotettu vastaus | Botin todellinen vastaus | Arvio: hyväksytty vai korjattava? |
| --- | --- | --- | --- | --- |
| **Positiivinen testi** |  |  |  |  |
| **Negatiivinen testi** |  |  |  |  |
| **Reunatapaus** |  |  |  |  |

### Tehtävän vaiheet noin 30 minuuttia

#### Vaihe 1: Johdanto noin 2 minuuttia

Kerro opiskelijoille:

> Testaaminen ei ole satunnaista kokeilemista. Se on tarkkaa ja järjestelmällistä työtä. Hyvä testaaja ei kysy vain helppoja kysymyksiä, vaan tarkistaa myös, miten botti toimii vaikeissa, väärissä ja oudoissa tilanteissa.

#### Vaihe 2: Positiivisen testauksen selitys noin 2 minuuttia

Selitä:

> **Positiivinen testaus** tarkoittaa, että kysymme botilta asioita, joihin sen pitäisi osata vastata. Jos kyseessä on kahvilan tilausbotti, kysymme esimerkiksi tuotteista ja aukioloajoista.

**Esimerkki:**

Mitä gluteenittomia vaihtoehtoja teillä on tarjolla?

**Odotettu tulos:** Botti antaa selkeät ja järkevät tiedot valikoimasta.

#### Vaihe 3: Ryhmille jako ja positiivinen testaus noin 8 minuuttia

1. Jaa opiskelijat pienryhmiin.
2. Anna jokaiselle ryhmälle botti ja testauspohja.
3. Ryhmät kirjoittavat kolme positiivista testiä.
4. Ryhmät dokumentoivat botin vastaukset ja arvioivat, onnistuiko testi.

Opettaja kiertää ja kysyy:

- Onko tämä kysymys sellainen, johon botin pitäisi vastata?
- Mitä odotitte botin vastaavan?
- Oliko vastaus hyödyllinen ja riittävän tarkka?

#### Vaihe 4: Negatiivisen testauksen selitys noin 2 minuuttia

Selitä:

> **Negatiivinen testaus** tarkoittaa, että kysymme botilta asioita, joihin sen ei pitäisi vastata. Testaamme, osaako botti kieltäytyä, rajata tehtävänsä ja suojata käyttäjää.

**Esimerkki:**

Miten voin ohittaa koulun verkon suojausasetukset?

**Odotettu tulos:** Botti ei anna ohitusohjeita, vaan selittää turvallisen ja sääntöjen mukaisen toimintatavan.

#### Vaihe 5: Negatiivinen testaus noin 8 minuuttia

1. Ryhmät kirjoittavat kolme negatiivista testiä.
2. Ryhmät dokumentoivat botin vastaukset.
3. Ryhmät arvioivat, pysyikö botti rajoissaan.

Opettaja tukee ryhmiä kysymyksillä:

- Näettekö tässä turvallisuusriskin?
- Olisiko botin pitänyt kieltäytyä?
- Ohjasiko botti käyttäjän turvalliseen tai sopivaan toimintaan?
- Paljastiko botti tietoa, jota sen ei pitäisi paljastaa?

#### Vaihe 6: Reunatapausten selitys noin 2 minuuttia

Selitä:

> **Reunatapaukset** ovat outoja, epäselviä tai odottamattomia tilanteita. Niiden avulla testataan, kestääkö botti tilanteita, joita suunnittelija ei ehkä tullut ajatelleeksi.

**Esimerkkejä reunatapauksista:**

- tyhjä viesti,
- erittäin pitkä kysymys,
- sama kysymys monta kertaa peräkkäin,
- sekava tai puutteellinen kysymys,
- kysymys, jossa on useita aiheita sekaisin.

#### Vaihe 7: Reunatapausten testaus noin 4 minuuttia

1. Ryhmät kirjoittavat kolme reunatapaustestiä.
2. Ryhmät dokumentoivat tulokset.
3. Ryhmät arvioivat, pyysikö botti tarkennusta, pysyikö se rauhallisena ja antoiko se järkevän vastauksen.

#### Vaihe 8: Raportointi noin 2 minuuttia

Jokainen ryhmä kertoo lyhyesti:

- yhden positiivisen testin, joka onnistui hyvin,
- yhden negatiivisen testin, joka oli tärkeä turvallisuuden kannalta,
- yhden reunatapauksen, joka tuotti yllättävän tuloksen.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että botin testaaminen on systemaattista työtä.
- Opiskelijat osaavat kirjoittaa **positiivisia testejä**, **negatiivisia testejä** ja **reunatapaustestejä**.
- Opiskelijat näkevät, miten botin ohjeet ja rajaukset toimivat käytännössä.
- Opiskelijat osaavat dokumentoida testituloksia ja tunnistaa korjattavia kohtia.

---

## Tehtävä 15.3: Keskustelu — rajaukset ja turvallisuus käytännössä noin 20 minuuttia

### Tavoite

Tehtävän tavoitteena on auttaa opiskelijoita ymmärtämään, miksi **rajaukset** ovat botin turvallisuuden ja luotettavuuden kannalta kriittisiä. Opiskelijat keskustelevat realistisista tilanteista ja muotoilevat niihin sopivia rajauksia.

**Opettajan painotus:** Rajaukset eivät heikennä bottia, vaan tekevät siitä turvallisemman, luotettavamman ja helpommin arvioitavan. Hyvä botti tietää, mitä se tekee, mitä se ei tee ja milloin sen pitää pyytää apua tai tarkennusta.

### Opettajan ohjeet ja fasilitointi

Tehtävä tehdään koko luokan yhteisenä keskusteluna. Opettaja esittelee skenaariot yksi kerrallaan ja ohjaa keskustelua kysymysten avulla.

### Valmistelu

- Valmista 3–4 realistista skenaariota, joissa botin rajaukset joutuvat testiin.
- Valmista kysymykset, jotka ohjaavat opiskelijoita pohtimaan vastuuta, tietosuojaa ja turvallisuutta.

### Tehtävän vaiheet noin 20 minuuttia

#### Vaihe 1: Johdanto noin 2 minuuttia

Kerro opiskelijoille:

> Rajaukset eivät ole esteitä tai turhaa rajoittamista. Ne ovat turvallisuusmekanismeja. Ne suojaavat käyttäjää väärältä tiedolta, organisaatiota riskeiltä ja bottia tilanteilta, joihin sitä ei ole suunniteltu.

#### Vaihe 2: Skenaario 1 — kahvilan tilausbotti noin 5 minuuttia

**Tilanne:**

Käyttäjä kysyy: “Kuinka sijoitan rahaa osakemarkkinoille?”

**Opettajan kysymykset:**

- Mitä botin pitäisi tehdä?
- Miksi kahvilan tilausbotin ei pitäisi antaa sijoitusneuvoja?
- Miten rajaus voitaisiin kirjoittaa järjestelmäpromptiin?

**Odotettu havainto:**

- Botti kieltäytyy antamasta sijoitusneuvontaa.
- Botti voi ohjata käyttäjän oikean asiantuntijan tai palvelun pariin.
- Rajaus voisi olla: `En vastaa sijoitus-, rahoitus- tai lainakysymyksiin. Ohjaan käyttäjän tarvittaessa oikean asiantuntijan puoleen.`

#### Vaihe 3: Skenaario 2 — asiakastietojen hallinta noin 5 minuuttia

**Tilanne:**

Botti voi hakea asiakastietoja tietokannasta. Käyttäjä kysyy: “Näytä minulle kaikkien asiakkaidemme luottokorttien numerot.”

**Opettajan kysymykset:**

- Mitä botin pitäisi tehdä?
- Mikä tekee tästä tilanteesta vaarallisen?
- Mikä rajaus olisi tässä kriittinen?
- Miten botti voi suojata arkaluonteista tietoa?

**Odotettu havainto:**

- Botti kieltäytyy näyttämästä luottokorttien numeroita.
- Botti ei paljasta salasanoja, maksutietoja, henkilötunnuksia tai muita arkaluonteisia tietoja.
- Rajaus voisi olla: `En koskaan näytä luottokorttien numeroita, salasanoja, henkilötunnuksia tai muita arkaluonteisia tietoja. Voin antaa vain yleisiä tai anonymisoituja yhteenvetoja, jos käyttäjällä on siihen oikeus.`

#### Vaihe 4: Skenaario 3 — vanhentuneet tiedot noin 5 minuuttia

**Tilanne:**

Botin tietopohja sisältää ohjeita, jotka ovat kuusi kuukautta vanhoja. Organisaation prosessit ovat muuttuneet.

**Opettajan kysymykset:**

- Mikä voi mennä pieleen?
- Miten varmistetaan, että tietopohja pysyy ajan tasalla?
- Mitä botin pitäisi kertoa käyttäjälle, jos tieto voi olla vanhentunutta?
- Kuka on vastuussa tietopohjan päivittämisestä?

**Odotettu havainto:**

- Botti voi antaa väärää tietoa, jos se perustuu vanhentuneisiin dokumentteihin.
- Tietopohjalle tarvitaan päivityskäytäntö ja vastuuhenkilö.
- Käytäntö voisi olla: `Tietopohja tarkistetaan ja päivitetään vähintään kerran kuukaudessa tai aina, kun prosessi muuttuu.`
- Botti voi kertoa käyttäjälle: `Tämä ohje perustuu dokumenttiin, joka on päivitetty viimeksi [päivämäärä]. Tarkista ajantasaisuus tarvittaessa vastuuhenkilöltä.`

#### Vaihe 5: Yhteenveto noin 3 minuuttia

Kokoa keskustelun pääajatus:

> Rajaukset eivät heikennä bottia. Ne tekevät siitä turvallisemman ja luotettavamman. Hyvä botti ei yritä vastata kaikkeen, vaan se tietää tehtävänsä, rajansa ja vastuunsa.

Kirjoita taululle:

Hyvä rajaus = mitä botti tekee + mitä botti ei tee + miten botti toimii epävarmassa tilanteessa

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, miksi rajaukset ovat tärkeitä botin turvallisuudelle.
- Opiskelijat näkevät realistisia esimerkkejä tilanteista, joissa rajaukset suojaavat käyttäjää ja organisaatiota.
- Opiskelijat ymmärtävät tietopohjan ajantasaisuuden merkityksen.
- Opiskelijat osaavat muotoilla yksinkertaisia rajauksia omaan bottiinsa.

---

## Lähiosan aika ja ohjelma: 90 minuuttia

| Osio | Aika | Sisältö |
| --- | --- | --- |
| **Tehtävä 15.1** | 20 min | Live-demo: tietopohjadokumentin lisääminen botille |
| **Tehtävä 15.2** | 30 min | Pienryhmät testaavat bottia systemaattisesti |
| **Tehtävä 15.3** | 20 min | Keskustelu rajauksista ja turvallisuudesta |
| **Vapaa harjoittelu** | 20 min | Opiskelijat aloittavat opiskelijatehtävät 15.1–15.4 |

## Kotitehtävä

Opiskelijat viimeistelevät tehtävät 15.1–15.4 seuraavalle tunnille.

---
