# Oma botti II — tietopohja, rajaukset ja testaus

## Johdanto: miksi testaaminen on kriittistä?

Edellisessä oppitunnissa rakensit tai suunnittelit omaa bottia. Nyt kohtaat tärkeän tosiasian: botti, jota ei ole testattu, voi olla riskialtis. Se voi vastata kysymykseen väärin, antaa virheellistä tietoa tai toimia epäjohdonmukaisesti haastavissa tilanteissa. Ilman testaamista et voi tietää, toimiiko botti oikeasti.

**Testaaminen** ei ole valinnainen lisäosa, vaan se tekee botista hyödyllisen työkalun pelkän hauskan kokeilun sijaan.

Tässä oppitunnissa käsittelemme kolmea asiaa, jotka muodostavat hyvän botin perustan:

- **Tietopohja:** mistä botti saa tiedon, jotta se voi vastata tarkasti.
- **Rajaukset:** mitä botti ei saa tehdä, jotta se ei toimi väärin tai vaarallisesti.
- **Testaus:** miten varmistat järjestelmällisesti, että botti tekee sen, mitä sen pitää tehdä.

## Tietopohja: bottia ohjaava tieto

Botti on vain niin hyvä kuin tieto, jota sillä on käytettävissään. Ilman hyvää **tietopohjaa** eli knowledge basea botti arvailee ja voi antaa virheellisiä vastauksia. Siksi tietopohjan suunnittelu ja ylläpito ovat ratkaisevan tärkeitä.

Tietopohja voi koostua monista eri lähteistä. Lähteiden valinta riippuu siitä, mitä botti tekee. Perinteinen tietopohja sisältää esimerkiksi dokumentteja ja tekstejä: oppimateriaaleja, oppaita, usein kysyttyjä kysymyksiä, käyttöohjeita ja prosessikuvauksia.

Esimerkiksi IT-helpdesk-botti hyötyy siitä, että sen tietopohjassa on yleisimmät ongelmat ja niiden ratkaisut. Tietopohja voi sisältää myös rakenteista tietoa, kuten tietokantoja, CSV-tiedostoja tai taulukoita. Joissakin tapauksissa botti voi hyödyntää myös ulkoisia lähteitä, kuten verkkohakua tai API-kutsuja. Esimerkiksi verkkokaupan botti voi tarkistaa varastotilanteen ennen kuin se kertoo asiakkaalle, onko tuotetta saatavilla.

Kun käyttäjä kysyy: ”Kuinka nollaan salasanan?”, hyvin varustettu IT-helpdesk-botti osaa vastata, koska tietopohja sisältää oikean ohjeen. Ilman tietopohjaa botti antaisi yleisen arvauksen, joka voisi olla täysin väärä kyseisessä organisaatiossa.

Tietopohjaa täytyy myös päivittää säännöllisesti. Jos ohjeistus muuttuu, prosessit vaihtuvat tai tuotteeseen lisätään uusia ominaisuuksia, tietopohja täytyy päivittää. Muuten botti voi antaa vanhentunutta tietoa, jonka perusteella käyttäjät tekevät virheellisiä päätöksiä.

Vanhentuneet ohjeet voivat aiheuttaa myös turvallisuusongelmia. Jos esimerkiksi salasanan nollausprosessiin lisätään uusi tunnistautumisvaihe, mutta botti neuvoo edelleen vanhan tavan, käyttäjät voivat toimia väärin tai ohittaa tärkeän suojauksen.

> **Pysähdy hetkeksi:** Kuvittele FAQ-botti, joka antaa kuusi kuukautta vanhentunutta tietoa. Mitä seurauksia sillä voisi olla asiakkaalle tai organisaatiolle?

## Rajaukset: mitä botti ei saa tehdä?

Hyvä botti ei vain osaa vastata. Se myös **tietää, mitä se ei osaa**. Rajaukset ovat botin kriittisiä ”en osaa” tai ”en saa tehdä tätä” -kohtia. Ne suojaavat sekä käyttäjää että bottia.

Rajauksia voi asettaa usealla tavalla sen mukaan, mitä haluat suojata.

- **Aihealueiden rajaus:** Kerro botille, mihin aiheisiin se vastaa ja mihin ei. IT-helpdesk-botti vastaa IT-ongelmiin, mutta ei myynti-, henkilöstö- tai talousasioihin.
- **Varmuuskynnys:** Jos botti ei ole riittävän varma vastauksestaan, sen pitää sanoa, ettei se tiedä, eikä yrittää arvata.
- **Herkkien tietojen kieltäminen:** Määritä selvästi, ettei botti koskaan kysy, tallenna tai paljasta salasanoja, luottokorttinumeroita tai muita arkaluontoisia tietoja.
- **Sallittujen toimintojen rajaus:** Botti voi esimerkiksi lukea tietokantaa, mutta ei muuttaa sitä. Se voi neuvoa käyttäjää, mutta ei tehdä käyttäjän puolesta järjestelmämuutoksia.

Käytännön esimerkki auttaa hahmottamaan asiaa. FAQ-botti osaa vastata IT-ongelmiin hyvin. Kun käyttäjä kysyy: ”Kuinka sijoittaisin rahaa osakemarkkinoille?”, botin ei pidä yrittää vastata. Sen kannattaa sanoa esimerkiksi: ”En osaa antaa sijoitusneuvoja, koska se vaatii rahoitusalan asiantuntemusta. Ota yhteyttä rahoituspalveluidemme tiimiin.”

Tämä on vastuullinen rajaus. Botti ohjaa käyttäjän oikeaan paikkaan sen sijaan, että antaisi mahdollisesti haitallisen neuvon.

Rajaukset asetetaan **ohjeistuksella**. Kirjoita botille selvästi ja yksityiskohtaisesti, missä sen toiminta-alue kulkee. Esimerkiksi ”Vastaa vain IT-aiheisiin” on liian epämääräinen. Parempi rajaus on:

> Vastaa vain seuraaviin aiheisiin: Windows-järjestelmä, verkkoyhteydet, salasanojen palautus ja ohjelmistojen asennus. Jos käyttäjä kysyy muista aiheista, kerro, ettei aihe kuulu toiminta-alueeseesi, ja ohjaa hänet oikealle tiimille.

> **Pysähdy hetkeksi:** Kuvittele agentti, jolla on oikeus muuttaa asiakkaiden tilejä tai varaston tietoja. Mitkä rajaukset olisivat kriittisiä sen turvallisuuden kannalta?

## Testaus: varmista, että botti tekee, mitä pitää

**Testaaminen** ei tarkoita satunnaisten kysymysten esittämistä. Se on systemaattista ja järjestelmällistä työtä. Testaat bottia kolmella tavalla, ja jokainen testaustapa kertoo botin toiminnasta eri näkökulmasta.

### 1. Positiiviset testit

Positiivisissa testeissä testaat asioita, joiden pitäisi toimia. Nämä ovat kysymyksiä ja tilanteita, joihin botti on suunniteltu vastaamaan.

Jos kysyt FAQ-botilta ”Kuinka käynnistän tietokoneeni uudelleen?”, sen pitäisi antaa selkeät ja oikeat vaiheet. Jos kysyt asiakaspalvelubotilta ”Kuinka näen laskuhistoriani?”, sen pitäisi antaa linkki laskuihin tai ohjeet niiden löytämiseen.

Dokumentoi jokainen testi esimerkiksi näin:

| Testi | Odotettu vastaus | Todellinen vastaus | Tulos |
| --- | --- | --- | --- |
| Kuinka käynnistän tietokoneeni uudelleen? | Selkeät vaiheet uudelleenkäynnistykseen. | Botti antaa vaiheittaisen ohjeen. | ✓ Onnistui |
| Kuinka muodostan WiFi-yhteyden? | Vaiheet WiFi-verkkoon liittymiseen. | Botti ohjaa valitsemaan verkon, syöttämään salasanan ja yhdistämään. | ✓ Onnistui |

Tee useita positiivisia testejä. Sopiva määrä riippuu botin laajuudesta, mutta tärkeintä on, että testaat kaikki keskeiset käyttötapaukset.

### 2. Negatiiviset testit

Negatiivisissa testeissä testaat asioita, joiden **ei pitäisi toimia**. Näissä tilanteissa botin pitää osata kieltäytyä, rajata vastaustaan tai ohjata käyttäjä oikeaan paikkaan.

Jos botti on IT-tukibotti ja käyttäjä kysyy: ”Kuinka sijoitan rahaa?”, botin ei pidä antaa sijoitusneuvoja. Jos käyttäjä kysyy: ”Mikä on salasanani?”, botin pitää kieltäytyä turvallisuussyistä.

| Testi | Odotettu vastaus | Todellinen vastaus | Tulos |
| --- | --- | --- | --- |
| Kuinka sijoitan rahaa osakemarkkinoille? | Botti kieltäytyy ja ohjaa oikealle osastolle. | Botti kertoo, ettei se anna sijoitusneuvoja, ja ohjaa rahoituspalveluihin. | ✓ Onnistui |
| Mikä on salasanani? | Botti kieltäytyy. | Botti ei kerro salasanoja, mutta voi ohjata salasanan nollaukseen. | ✓ Onnistui |

Negatiivisilla testeillä varmistat, että botti osaa sanoa ”ei” ja suojaa käyttäjää, organisaatiota ja itseään.

### 3. Reunatapaukset

Reunatapauksissa testaat outoja tai epätavallisia tilanteita. Ne eivät välttämättä ole yleisiä, mutta ne paljastavat, kuinka kestävä botti on.

Testaa esimerkiksi seuraavia tilanteita:

- Käyttäjä lähettää tyhjän kysymyksen.
- Kysymys on hyvin pitkä ja sekava.
- Käyttäjä kysyy saman asian monta kertaa peräkkäin.
- Käyttäjä kirjoittaa tahallaan väärällä kielellä tai hyvin epäselvästi.

| Testi | Odotettu vastaus | Tulos |
| --- | --- | --- |
| Tyhjä kysymys | Botti pyytää käyttäjää kirjoittamaan kysymyksen eikä kaadu. | ✓ Onnistui |
| Hyvin pitkä ja sekava kysymys | Botti pyytää tarkennusta tai ehdottaa kysymyksen pilkkomista osiin. | ✓ Onnistui |
| Sama kysymys kolme kertaa peräkkäin | Botti ei jää silmukkaan, vaan vastaa, pyytää tarkennusta tai ehdottaa yhteydenottoa ihmiseen. | ✓ Onnistui |

Reunatapaukset osoittavat, kuinka **kestävä** botti on. Hyvä botti ei kaadu outoihin tilanteisiin, vaan toimii hallitusti.

## Iterointi: testaa, korjaa ja testaa uudelleen

Testaaminen ei lopu siihen, että ajat testit kerran. Kun löydät ongelmia, korjaat ne ja testaat uudelleen. Tätä kutsutaan **iteroinniksi**, ja se on normaali osa botin kehittämistä.

Iterointi etenee näin:

1. Kirjoita botille alustava ohjeistus.
2. Testaa kaikki kolme testityyppiä: positiiviset testit, negatiiviset testit ja reunatapaukset.
3. Dokumentoi virheet ja ongelmat.
4. Korjaa ohjeistusta tai tietopohjaa.
5. Testaa uudelleen.
6. Toista, kunnes botti toimii riittävän hyvin.

**Konkreettinen esimerkki:**

**Kierros 1:**

- **Ohjeistus:** ”Vastaa IT-ongelmiin.”
- **Positiivinen testi:** ”Kuinka asennan ohjelmiston?” → Botti antaa ohjeet. ✓
- **Negatiivinen testi:** ”Kuinka poistan loukkaavan roskapostin?” → Botti ei tunnista aihetta oikein. ✗
- **Korjaus:** Lisää ohjeistukseen, että botti vastaa myös sähköpostiongelmiin, kuten roskapostiin ja suodatuksiin.

**Kierros 2:**

- **Ohjeistus:** ”Vastaa IT-ongelmiin ja sähköpostiongelmiin.”
- **Positiivinen testi:** ”Kuinka voin estää roskapostin?” → Botti antaa hyvät ohjeet roskapostin suodattamiseen. ✓
- **Positiivinen testi:** ”Kuinka vaihdan salasanan?” → Botti antaa oikeat ohjeet. ✓
- **Reunatapaus:** Tyhjä kysymys → Botti pyytää tarkennusta. ✓
- **Tulos:** Botti toimii paremmin kuin ensimmäisessä versiossa.

Iterointi on täysin normaalia. Ensimmäinen versio on harvoin täydellinen. Hyvät botit syntyvät testaamalla, parantamalla ja testaamalla uudelleen.

## Todellinen esimerkki: helpdesk-botti käytännössä

Kuvittele, että rakennat IT-helpdesk-bottia organisaatioosi.

**Tietopohja** sisältää 50 yleisintä IT-ongelmaa ja niiden ratkaisut. Mukana ovat esimerkiksi salasanan palauttaminen, VPN-yhteyden muodostaminen, ohjelmistojen asentaminen ja verkkoyhteysongelmien ratkaiseminen. Lisäksi tietopohjassa on yhteystiedot eskalointia varten, koska joskus botti ei osaa ratkaista ongelmaa ja asia täytyy ohjata ihmiselle.

**Rajaukset** ovat selkeät. Botti vastaa vain IT-ongelmiin, ei HR-, talous- tai myyntiaiheisiin. Jos botti ei ole riittävän varma vastauksestaan, se sanoo, ettei osaa vastata, eikä yritä arvata. Botti voi lukea tietopohjaa ja hakea ohjeita, mutta se ei saa muuttaa käyttäjätietoja, salasanoja tai järjestelmäasetuksia.

**Testaus** on systemaattista. Testaat esimerkiksi 15 yleisintä kysymystä, joihin botin pitäisi osata vastata. Testaat myös viisi negatiivista tapausta, joissa botin pitää kieltäytyä tai ohjata käyttäjä muualle. Lisäksi testaat viisi reunatapausta, kuten tyhjät kysymykset, sekavat kysymykset ja pitkät kysymykset. Dokumentoit jokaisen testin ja varmistat, että botti käyttäytyy oikein.

Kun testaus on valmis ja keskeiset testit menevät läpi, botti on valmis kokeiltavaksi oikeassa käytössä.

## Kohti omaa projektia

Tällä tunnilla opit **tietopohjan**, **rajausten** ja **testauksen** merkityksen. Nämä kolme perustaa erottavat hyvän botin huonosta.

Mieti omaa bottiasi seuraavien kysymysten avulla:

- Mitä tietoa botti tarvitsee, jotta se toimii hyvin?
- Mistä aiheista botin pitää kieltäytyä?
- Mitä botti saa tehdä ja mitä se ei saa tehdä?
- Miten testaat, että botti tekee sen, mitä lupaa?
- Miten dokumentoit testitulokset?

Nämä kysymykset ovat keskeisiä, kun rakennat bottisi valmiiksi arviointiprojektissa. Hyvä botti ei ole vain nimetty ChatGPT, vaan **testattu, rajattu ja tarkoituksenmukainen työkalu**.

## Yhteenveto

Hyödyllinen botti rakentuu kolmelle vahvalle perustalle:

1. **Tietopohja** antaa botille tiedon, jonka perusteella se voi vastata tarkasti ja ajankohtaisesti.
2. **Rajaukset** varmistavat, että botti ei tee vaarallisia tai sopimattomia asioita ja tietää, milloin sen pitää kieltäytyä.
3. **Testaus** varmistaa järjestelmällisesti, että botti toimii oikein positiivisissa tilanteissa, negatiivisissa tilanteissa ja epätavallisissa reunatapauksissa.

Testaus ei ole kertaluonteinen työ, vaan iteratiivinen prosessi. Korjaat ja parannat bottia, testaat uudelleen ja jatkat, kunnes botti on riittävän hyvä. Hyvällä botilla on laadukas tietopohja, selkeät rajat ja perusteellinen testaus.

---
