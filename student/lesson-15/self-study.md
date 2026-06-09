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

Esimerkiksi kahvilan asiakaspalvelubotti hyötyy siitä, että sen tietopohjassa on tuotelista, aukioloajat ja yleisimmät kysymykset vastauksineen. Tietopohja voi sisältää myös rakenteista tietoa, kuten tietokantoja, CSV-tiedostoja tai taulukoita. Joissakin tapauksissa botti voi hyödyntää myös ulkoisia lähteitä, kuten verkkohakua tai API-kutsuja. Esimerkiksi verkkokaupan botti voi tarkistaa varastotilanteen ennen kuin se kertoo asiakkaalle, onko tuotetta saatavilla.

Kun asiakas kysyy: ”Onko teillä laktoosittomia vaihtoehtoja?”, hyvin varustettu asiakaspalvelubotti osaa vastata, koska tietopohja sisältää ajantasaisen tuotelistan. Ilman tietopohjaa botti antaisi yleisen arvauksen, joka voisi olla täysin väärä kyseisessä kahvilassa.

Tietopohjaa täytyy myös päivittää säännöllisesti. Jos ohjeistus muuttuu, prosessit vaihtuvat tai tuotteeseen lisätään uusia ominaisuuksia, tietopohja täytyy päivittää. Muuten botti voi antaa vanhentunutta tietoa, jonka perusteella käyttäjät tekevät virheellisiä päätöksiä.

Vanhentuneet tiedot voivat aiheuttaa myös ongelmia. Jos esimerkiksi kahvila vaihtaa aukioloaikojaan, mutta botti kertoo edelleen vanhat ajat, asiakkaat voivat tulla turhaan suljetulle ovelle.

> **Pysähdy hetkeksi:** Kuvittele FAQ-botti, joka antaa kuusi kuukautta vanhentunutta tietoa. Mitä seurauksia sillä voisi olla asiakkaalle tai organisaatiolle?

## Rajaukset: mitä botti ei saa tehdä?

Hyvä botti ei vain osaa vastata. Se myös **tietää, mitä se ei osaa**. Rajaukset ovat botin kriittisiä ”en osaa” tai ”en saa tehdä tätä” -kohtia. Ne suojaavat sekä käyttäjää että bottia.

Rajauksia voi asettaa usealla tavalla sen mukaan, mitä haluat suojata.

- **Aihealueiden rajaus:** Kerro botille, mihin aiheisiin se vastaa ja mihin ei. Kahvilan asiakaspalvelubotti vastaa tuote- ja aukiolokysymyksiin, mutta ei esimerkiksi rekrytointiin tai laskutukseen.
- **Varmuuskynnys:** Jos botti ei ole riittävän varma vastauksestaan, sen pitää sanoa, ettei se tiedä, eikä yrittää arvata.
- **Herkkien tietojen kieltäminen:** Määritä selvästi, ettei botti koskaan kysy, tallenna tai paljasta salasanoja, luottokorttinumeroita tai muita arkaluontoisia tietoja.
- **Sallittujen toimintojen rajaus:** Botti voi esimerkiksi lukea tietokantaa, mutta ei muuttaa sitä. Se voi neuvoa käyttäjää, mutta ei tehdä käyttäjän puolesta järjestelmämuutoksia.

Käytännön esimerkki auttaa hahmottamaan asiaa. Kahvilan FAQ-botti osaa vastata tuotekysymyksiin hyvin. Kun käyttäjä kysyy: ”Kuinka sijoittaisin rahaa osakemarkkinoille?”, botin ei pidä yrittää vastata. Sen kannattaa sanoa esimerkiksi: ”En osaa antaa sijoitusneuvoja, koska se ei kuulu kahvilan palveluihin. Tällaisessa asiassa kannattaa kääntyä pankin tai rahoitusneuvojan puoleen.”

Tämä on vastuullinen rajaus. Botti ohjaa käyttäjän oikeaan paikkaan sen sijaan, että antaisi mahdollisesti haitallisen neuvon.

Rajaukset asetetaan **ohjeistuksella**. Kirjoita botille selvästi ja yksityiskohtaisesti, missä sen toiminta-alue kulkee. Esimerkiksi ”Vastaa vain IT-aiheisiin” on liian epämääräinen. Parempi rajaus on:

> Vastaa vain seuraaviin aiheisiin: tuotevalikoima, hinnat, aukioloajat ja allergeenitiedot. Jos käyttäjä kysyy muista aiheista, kerro, ettei aihe kuulu toiminta-alueeseesi, ja ohjaa hänet henkilökunnalle.

> **Pysähdy hetkeksi:** Kuvittele agentti, jolla on oikeus muuttaa asiakkaiden tilejä tai varaston tietoja. Mitkä rajaukset olisivat kriittisiä sen turvallisuuden kannalta?

## Testaus: varmista, että botti tekee, mitä pitää

**Testaaminen** ei tarkoita satunnaisten kysymysten esittämistä. Se on systemaattista ja järjestelmällistä työtä. Testaat bottia kolmella tavalla, ja jokainen testaustapa kertoo botin toiminnasta eri näkökulmasta.

### 1. Positiiviset testit

Positiivisissa testeissä testaat asioita, joiden pitäisi toimia. Nämä ovat kysymyksiä ja tilanteita, joihin botti on suunniteltu vastaamaan.

Jos kysyt kahvilan FAQ-botilta ”Mihin aikaan avaatte aamulla?”, sen pitäisi antaa selkeä ja oikea vastaus. Jos kysyt asiakaspalvelubotilta ”Kuinka näen laskuhistoriani?”, sen pitäisi antaa linkki laskuihin tai ohjeet niiden löytämiseen.

Dokumentoi jokainen testi esimerkiksi näin:

| Testi | Odotettu vastaus | Todellinen vastaus | Tulos |
| --- | --- | --- | --- |
| Mihin aikaan avaatte aamulla? | Selkeä vastaus aukioloajasta. | Botti kertoo aukioloajan. | ✓ Onnistui |
| Onko teillä kasvisvaihtoehtoja? | Lista kasvisvaihtoehdoista. | Botti luettelee päivän kasvisvaihtoehdot. | ✓ Onnistui |

Tee useita positiivisia testejä. Sopiva määrä riippuu botin laajuudesta, mutta tärkeintä on, että testaat kaikki keskeiset käyttötapaukset.

### 2. Negatiiviset testit

Negatiivisissa testeissä testaat asioita, joiden **ei pitäisi toimia**. Näissä tilanteissa botin pitää osata kieltäytyä, rajata vastaustaan tai ohjata käyttäjä oikeaan paikkaan.

Jos botti on kahvilan asiakaspalvelubotti ja käyttäjä kysyy: ”Kuinka sijoitan rahaa?”, botin ei pidä antaa sijoitusneuvoja. Jos käyttäjä kysyy: ”Mikä on toisen asiakkaan tilaus?”, botin pitää kieltäytyä yksityisyyssyistä.

| Testi | Odotettu vastaus | Todellinen vastaus | Tulos |
| --- | --- | --- | --- |
| Kuinka sijoitan rahaa osakemarkkinoille? | Botti kieltäytyy ja ohjaa oikealle osastolle. | Botti kertoo, ettei se anna sijoitusneuvoja, ja ohjaa rahoituspalveluihin. | ✓ Onnistui |
| Mikä on toisen asiakkaan tilaus? | Botti kieltäytyy. | Botti ei kerro muiden asiakkaiden tietoja yksityisyyssyistä. | ✓ Onnistui |

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

- **Ohjeistus:** ”Vastaa kahvilan tuotekysymyksiin.”
- **Positiivinen testi:** ”Mitä kahveja teillä on?” → Botti luettelee vaihtoehdot. ✓
- **Negatiivinen testi:** ”Voinko varata pöydän kymmenelle?” → Botti ei tunnista aihetta oikein. ✗
- **Korjaus:** Lisää ohjeistukseen, että botti osaa myös ohjata pöytävaraukset henkilökunnalle.

**Kierros 2:**

- **Ohjeistus:** ”Vastaa kahvilan tuotekysymyksiin ja ohjaa varaukset henkilökunnalle.”
- **Positiivinen testi:** ”Voinko varata pöydän?” → Botti ohjaa varauksen henkilökunnalle. ✓
- **Positiivinen testi:** ”Onko teillä gluteenitonta?” → Botti antaa oikean vastauksen. ✓
- **Reunatapaus:** Tyhjä kysymys → Botti pyytää tarkennusta. ✓
- **Tulos:** Botti toimii paremmin kuin ensimmäisessä versiossa.

Iterointi on täysin normaalia. Ensimmäinen versio on harvoin täydellinen. Hyvät botit syntyvät testaamalla, parantamalla ja testaamalla uudelleen.

## Todellinen esimerkki: asiakaspalvelubotti käytännössä

Kuvittele, että rakennat asiakaspalvelubottia oman alasi organisaatioon, esimerkiksi kahvilaan, kirjastoon tai liikuntakeskukseen.

**Tietopohja** sisältää 50 yleisintä asiakaskysymystä ja niiden vastaukset. Mukana ovat esimerkiksi tuotevalikoima, hinnat, aukioloajat, allergeenitiedot ja varausohjeet. Lisäksi tietopohjassa on yhteystiedot eskalointia varten, koska joskus botti ei osaa vastata kysymykseen ja asia täytyy ohjata ihmiselle.

**Rajaukset** ovat selkeät. Botti vastaa vain oman alueensa kysymyksiin, ei esimerkiksi rekrytointiin, laskutukseen tai talousasioihin. Jos botti ei ole riittävän varma vastauksestaan, se sanoo, ettei osaa vastata, eikä yritä arvata. Botti voi lukea tietopohjaa ja hakea tietoja, mutta se ei saa käsitellä asiakkaiden maksutietoja tai muuttaa varauksia.

**Testaus** on systemaattista. Testaat esimerkiksi 15 yleisintä asiakaskysymystä, joihin botin pitäisi osata vastata. Testaat myös viisi negatiivista tapausta, joissa botin pitää kieltäytyä tai ohjata käyttäjä muualle. Lisäksi testaat viisi reunatapausta, kuten tyhjät kysymykset, sekavat kysymykset ja pitkät kysymykset. Dokumentoit jokaisen testin ja varmistat, että botti käyttäytyy oikein.

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
