# Opettajavetoiset harjoitukset: generatiivisen tekoälyn luonne

## Harjoitus 1: Sama prompti, eri mallit — epädeterministisyyden demonstraatio

### Tavoite

Harjoituksen tavoitteena on näyttää käytännössä, miksi **generatiivisen tekoälyn** tuottamat vastaukset voivat vaihdella. Opiskelijat ymmärtävät, että vaihtelu johtuu mallien **todennäköisyyspohjaisesta toiminnasta**, ei välttämättä käyttäjän virheestä.

**Opettajan painotus:** Korosta, että epädeterministisyys ei tarkoita sattumanvaraista tai hyödytöntä toimintaa. Se tarkoittaa, että malli voi tuottaa useita mahdollisia vastauksia, joista moni voi olla järkevä mutta eri tavalla muotoiltu.

### Opettajan ohjeet ja fasilitointi

**Kesto:** noin 15 minuuttia

#### Valmistelu ennen oppituntia noin 5 minuuttia

- Avaa selaimeen useita tekoälymalleja, esimerkiksi ChatGPT, Claude ja Google Gemini.
- Valmistele sama tai mahdollisimman samanlainen prompti kaikille malleille.
- Varmista, että vastaukset voidaan näyttää opiskelijoille rinnakkain tai peräkkäin.

#### Esimerkkiprompti

Kirjoita lyhyt koodinpätkä, 5–10 riviä, joka lukee tiedoston nimeltä `data.txt`, laskee rivien lukumäärän ja tulostaa tuloksen.

#### Luokkaharjoitus noin 10 minuuttia

1. Näytä ensin yhden tekoälymallin vastaus opetusnäytöllä.
2. Kysy opiskelijoilta: **Voitteko ennustaa, millaisen vastauksen toinen malli antaa?**
3. Näytä toisen mallin vastaus.
4. Vertailkaa vastauksia seuraavien kysymysten avulla:

   ```
   - Onko käytetty ohjelmointikieli tai syntaksi sama?
   - Onko mukana kommentteja?
   - Onko vastauksissa virheitä tai puutteita?
   - Onko ratkaisun tyyli samanlainen vai erilainen?
   - Kumpi vastaus olisi helpompi testata käytännössä?
5. Näytä vielä kolmannen mallin vastaus ja tehkää sama vertailu.
```

#### Keskustelu

Kysy opiskelijoilta:

- Miksi vastaukset ovat erilaisia, vaikka prompti oli sama tai lähes sama?
- Miksi kaikki vastaukset voivat silti olla mahdollisesti järkeviä?
- Milloin vaihtelu on hyödyllistä?
- Milloin vaihtelu voi olla ongelma?
- Mitä käyttäjän pitää tehdä ennen kuin tekoälyn tuottamaa koodia käytetään oikeassa projektissa?

Johdattele opiskelijat ymmärtämään, että mallit eivät hae yhtä valmista oikeaa vastausta tietokannasta. Ne tekevät **todennäköisyyspohjaisia valintoja** seuraavien sanojen, merkkien tai rakenteiden välillä.

> **Lämpötila** vaikuttaa siihen, kuinka paljon malli valitsee vaihtelevia tai yllättäviä vaihtoehtoja. Jokainen malli voi kulkea hieman eri reittiä seuraavien sanojen joukossa.

#### Johtopäätös

- **Epädeterministisyys** on generatiivisen tekoälyn ominaisuus, ei pelkkä virhe.
- Vaihtelu mahdollistaa luovuuden ja vaihtoehtoiset ratkaisut.
- Sama prompti ei välttämättä tuota aina täsmälleen samaa vastausta.
- Teknisissä tehtävissä käyttäjän täytyy tarkistaa, että vastaus toimii oikeasti.

**Opettajan tarkistuskysymys:** Jos opiskelijat keskittyvät valitsemaan parasta mallia, kysy: “Mitä tämä vertailu kertoo generatiivisen tekoälyn toimintatavasta?”

### Opettajan muistiinpanot

- Ole valmis siihen, että jokin vastaus voi sisältää virheen tai hallusinaation, esimerkiksi väärän funktion tai puutteellisen virheenkäsittelyn. Käytä tilannetta opetuksessa.
- Jos vastaukset ovat hyvin samankaltaisia, selitä opiskelijoille: “Koska mallien koulutusdata ja tehtävän rakenne ovat samankaltaisia, samankaltaiset vastaukset voivat olla todennäköisimpiä.”
- Korosta, että mallien vertailun tarkoitus ei ole valita “voittajaa”, vaan ymmärtää generatiivisen tekoälyn toimintatapaa.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, mitä **epädeterministisyys** tarkoittaa generatiivisen tekoälyn yhteydessä.
- Opiskelijat osaavat selittää, miksi sama prompti voi tuottaa erilaisia vastauksia.
- Opiskelijat ymmärtävät, milloin vaihtelu voi olla hyödyllistä ja milloin se voi olla riski.
- Opiskelijat osaavat perustella, miksi tekoälyn tuottama koodi pitää tarkistaa ennen käyttöä.

---

## Harjoitus 2: Hallusinaatioiden metsästys — ryhmäanalyysi

### Tavoite

Harjoituksen tavoitteena on oppia tunnistamaan **hallusinaatioita** ja ymmärtää, miksi kielimalli voi tuottaa uskottavalta kuulostavia mutta virheellisiä vastauksia. Opiskelijat harjoittelevat myös tiedon tarkistamista luotettavista lähteistä.

**Opettajan painotus:** Hallusinaation tunnistaminen ei tarkoita vain virheen osoittamista. Ammattilaisen pitää osata kertoa, **miten** väite tarkistettiin ja **miksi** vastaus oli epäluotettava.

### Opettajan ohjeet ja fasilitointi

**Kesto:** noin 20 minuuttia

#### Ryhmien muodostaminen noin 2 minuuttia

- Jaa opiskelijat 3–4 henkilön ryhmiin.
- Anna jokaiselle ryhmälle yksi hallusinaatiotapaus tutkittavaksi.
- Kerro, että ryhmän tehtävänä ei ole vain sanoa, onko väite väärä, vaan myös perustella, miten asia tarkistettiin.

#### Case-tutkimukset

Valitse seuraavista 2–3 tapausta tai jaa eri ryhmille eri tapaukset.

##### Case 1: Tekniikka

AI-malli väittää:

Pythonissa funktiota `urllib3.get_json(url)` käytetään JSON-datan hakemiseen.

- Tarkistakaa, onko funktio olemassa.
- Selvittäkää, millä tavoin JSON-dataa oikeasti haetaan Pythonissa.
- Pohtikaa, miksi malli saattoi keksiä tällaisen funktion.

##### Case 2: Historia

AI-malli väittää:

Suomen ensimmäinen pääministeri oli Mikael Agricola.

- Tarkistakaa, kuka oli Suomen ensimmäinen pääministeri.
- Pohtikaa, miksi malli saattoi sekoittaa tunnetun historiallisen henkilön väärään rooliin.

##### Case 3: API-dokumentaatio

AI-malli dokumentoi API-päätepisteen näin:

`GET /users/{id}/profile` — palauttaa käyttäjän profiilin ja salasanan.

- Arvioikaa, pitäisikö API:n koskaan palauttaa käyttäjän salasanaa.
- Pohtikaa, miksi malli saattoi ehdottaa tietoturvan kannalta vaarallista toimintoa.
- Miettikää, miten dokumentaatio pitäisi korjata turvalliseksi.

#### Ryhmän tehtävä noin 10 minuuttia

Tutkikaa oma tapauksenne ja täyttäkää seuraava taulukko:

| AI:n väite | Oikein vai väärin? | Missä tarkistitte? | Hallusinaation merkkejä | Miksi malli saattoi hallusinoida? |
| --- | --- | --- | --- | --- |
| [Kirjoittakaa tähän AI:n väite.] | [Oikein / väärin / osittain oikein] | [Lähde, dokumentaatio tai muu tarkistuspaikka] | [Mikä teki väitteestä epäilyttävän?] | [Mitä sanoja, malleja tai yhteyksiä tekoäly saattoi yhdistellä väärin?] |

#### Esittäminen noin 8 minuuttia

- Jokainen ryhmä esittelee havaintonsa noin 2–3 minuutissa.
- Ryhmän tulee kertoa:

  ```
  - mikä väite oli,
  - oliko se oikein, väärin vai osittain oikein,
  - miten asia tarkistettiin,
  - mistä hallusinaation olisi voinut tunnistaa,
  - miten virheellinen vastaus olisi pitänyt korjata.
```
> Hallusinaatiot eivät aina näytä ilmiselviltä virheiltä. Malli voi esittää väärän vastauksen hyvin itsevarmasti.

### Opettajan muistiinpanot

- Valmistele tapaukset etukäteen ja tarkista oikeat vastaukset luotettavista lähteistä.
- Hallusinaatiot voivat vaihdella eri malleissa, joten eri mallien käyttäytymistä voi käyttää keskustelun pohjana.
- Jos ryhmällä on vaikeuksia löytää virhettä, anna vihje: “Onko väite liian yksityiskohtainen? Kuulostaako se uskottavalta, mutta ilman lähdettä? Sisältääkö se oudon funktion, henkilön tai turvattoman käytännön?”

**Opettajan tarkistuskysymys:** Jos opiskelija sanoo “vastaus kuulostaa oikealta”, kysy: “Mihin lähteeseen se perustuu?”

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, mitä **hallusinaatio** tarkoittaa generatiivisen tekoälyn yhteydessä.
- Opiskelijat osaavat tarkistaa tekoälyn väitteen luotettavasta lähteestä.
- Opiskelijat tunnistavat hallusinaation merkkejä, kuten olemattomia funktioita, väärin yhdistettyjä käsitteitä ja turvattomia oletuksia.
- Opiskelijat ymmärtävät, että itsevarma sävy ei tee vastauksesta oikeaa.

---

## Harjoitus 3: Verifiointiprosessin suunnittelu

### Tavoite

Harjoituksen tavoitteena on opettaa opiskelijoille, miten tekoälyä voidaan käyttää ammatillisessa työnkulussa niin, että **hallusinaatiot**, virheellinen koodi tai puutteelliset vastaukset eivät päädy suoraan käyttöön. Opiskelijat suunnittelevat vaiheittaisen **verifiointiprosessin**.

**Opettajan painotus:** Verifiointi ei ole tekoälyn käytön hidaste, vaan osa ammatillista laatua ja turvallisuutta. Nopea vastaus ei vielä tarkoita oikeaa tai turvallista ratkaisua.

### Opettajan ohjeet ja fasilitointi

**Kesto:** noin 25 minuuttia

#### Skenaario noin 5 minuuttia

Esitä opiskelijoille seuraava tilanne:

> Tehtäväsi on kirjoittaa SQL-kysely tietokantaan. Kyselyn pitää hakea kaikki asiakkaat, joiden maksu on erääntynyt yli 30 päivää. Käytät ChatGPT:tä koodin kirjoittamisen tukena.

Kysy opiskelijoilta:

- Mitä voi mennä pieleen, jos kopioit tekoälyn vastauksen suoraan tuotantokantaan ilman tarkistusta?
- Mitä tietoja tekoäly voi olettaa väärin?
- Miten virhe voisi vaikuttaa asiakkaisiin, dataan tai organisaatioon?

#### Ryhmäkeskustelu: verifiointivaiheet noin 10 minuuttia

Jaa opiskelijat pienryhmiin. Anna jokaiselle ryhmälle yksi tai useampi vaihe pohdittavaksi:

1. **Ennen tekoälyltä kysymistä:** Mitä sinun täytyy tietää jo valmiiksi? Esimerkiksi taulujen nimet, sarakkeet, päivämäärämuodot, tietokannan tyyppi ja liiketoimintasäännöt.
2. **Promptin kirjoittaminen:** Miten kirjoitat tarkan promptin? Mitä yksityiskohtia annat tekoälylle?
3. **Vastauksen analysointi:** Mistä merkeistä voit epäillä, että vastaus sisältää hallusinaation tai väärän oletuksen?
4. **Koodin testaaminen:** Miten testaat SQL-kyselyn ennen oikeaan dataan tai tuotantoympäristöön viemistä?
5. **Dokumentointi:** Miten kirjaat, mitä tekoäly ehdotti, mitä muutit ja miksi hyväksyit lopullisen ratkaisun?

#### Ryhmän vastauspohja

| Verifiointivaihe | Mitä tehdään? | Miksi tämä on tärkeää? | Mitä riskiä tämä vähentää? |
| --- | --- | --- | --- |
| **Ennen kysymistä** |  |  |  |
| **Promptin kirjoittaminen** |  |  |  |
| **Vastauksen analysointi** |  |  |  |
| **Testaaminen** |  |  |  |
| **Dokumentointi** |  |  |  |

#### Esittäminen noin 10 minuuttia

- Jokainen ryhmä esittelee oman vaiheensa noin 2–3 minuutissa.
- Opettaja kokoaa ryhmien vastauksista yhteisen **verifiointiprosessin** taululle.

#### Esimerkkiprosessi

1. **Ymmärrä tietokannan rakenne:** tarkista taulut, sarakkeet, tietotyypit ja suhteet dokumentaatiosta tai skeemasta.
2. **Kirjoita tarkka prompti:** sisällytä taulujen ja sarakkeiden nimet, tietokantatyyppi sekä haluttu lopputulos.
3. **Analysoi vastaus:** tarkista syntaksi, vertaa sitä dokumentaatioon ja etsi mallin tekemiä oletuksia.
4. **Testaa turvallisesti:** käytä testidataa tai kehitysympäristöä ennen oikeaa dataa.
5. **Dokumentoi päätökset:** kirjaa esimerkiksi: “ChatGPT ehdotti ratkaisua X. Hyväksyin osan Y, koska se vastasi skeemaa. Muutin kohdan Z, koska alkuperäinen ehdotus ei huomioinut päivämäärämuotoa.”

**Vinkki arviointiin:** Hyvä verifiointiprosessi ei pääty siihen, että “koodi näyttää oikealta”. Siinä näkyy, miten vastaus testataan, miten oletukset tarkistetaan ja miten lopullinen ratkaisu dokumentoidaan.

### Opettajan muistiinpanot

- Korosta, että **verifiointi** ei ole ylimääräinen vaihe vaan ammatillinen standardi.
- Jos opiskelijat kokevat prosessin liian monimutkaiseksi, voit vastata: “Juuri siksi tekoälyn käyttö vaatii ammattitaitoa. Nopea vastaus ei vielä tarkoita oikeaa tai turvallista ratkaisua.”
- Muistuta, että tekoälyn tuottamaa koodia ei pidä ajaa tuotannossa ilman tarkistusta ja testausta.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, miksi tekoälyn tuottamaa teknistä ratkaisua ei pidä käyttää ilman tarkistusta.
- Opiskelijat osaavat suunnitella vaiheittaisen **verifiointiprosessin**.
- Opiskelijat osaavat tunnistaa tekoälyn tekemiä oletuksia ja mahdollisia hallusinaatioita.
- Opiskelijat ymmärtävät, että ammattilainen kantaa vastuun lopullisesta ratkaisusta.

---

## Opettajan tärkeät huomiot

### Avainviesti 1: Epädeterministisyys on ominaisuus, ei vika

- Johdonmukaisuus ja luovuus ovat saman työkalun kaksi eri puolta.
- Teknisissä tehtävissä kannattaa suosia johdonmukaisuutta ja tarkistaa tulokset huolellisesti.
- Ideoinnissa ja luonnostelussa vaihtelu voi olla hyödyllistä.

### Avainviesti 2: Uskottava ei tarkoita oikeaa

- **Hallusinaatiot** voivat kuulostaa täysin itsevarmoilta.
- IT-ammattilaisella voi olla hyvä “kuulostaa oikealta” -tuntuma, mutta sekään ei aina riitä.
- **Verifiointia ei voi ohittaa.**

### Avainviesti 3: Vastuu on käyttäjällä

- Jos annat asiakkaalle tekoälyavusteisen raportin tai koodin, vastaat sen oikeellisuudesta.
- Malli ei kanna ammatillista vastuuta käyttäjän puolesta.
- Tämä ei ole pelottelua, vaan osa asiantuntijatyötä ja ammattimaista tekoälyn käyttöä.

---

## Sisäänrakennetut keskustelun herättäjät

### Jos opiskelijat sanovat: “Entä jos käytän tekoälyä sellaisenaan ilman verifiointia?”

> Silloin riskit kohdistuvat sinuun, asiakkaaseen ja organisaatioon. Teknisissä tehtävissä hallusinaatiot ovat erityisen vaarallisia, koska virheellinen koodi voi epäonnistua tuotannossa tai avata tietoturva-aukon.

### Jos opiskelijat sanovat: “Tämä tekee tekoälystä käyttökelvottoman.”

> Ei tee. Se tarkoittaa, että tekoälyä pitää käyttää oikeassa tehtävässä ja oikealla tavalla. Tekoäly on hyödyllinen työkalu, kun käyttäjä ymmärtää sen rajat ja tarkistaa lopputuloksen.

---

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- selittää, mitä **epädeterministisyys** tarkoittaa generatiivisen tekoälyn käytössä,
- vertailla saman promptin tuottamia erilaisia vastauksia eri malleissa,
- tunnistaa **hallusinaatioita** ja tarkistaa väitteitä luotettavista lähteistä,
- selittää, miksi itsevarma vastaus ei vielä tarkoita oikeaa vastausta,
- suunnitella ammatillinen **verifiointiprosessi** tekoälyn tuottamalle tekniselle ratkaisulle,
- perustella, miksi käyttäjä kantaa vastuun tekoälyn avulla tuotetun lopputuloksen oikeellisuudesta.

---
