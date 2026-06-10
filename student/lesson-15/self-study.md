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

<figure class="ai-demo"><span class="ai-demo__tag">// kolme testityyppiä — botti on valmis vasta, kun kaikki menevät läpi</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:300px">
  <div class="l15-wrap">
    <div class="l15-bot">BOTTI<span class="l15-score"><i class="l15-sc s0">testit: 0/3</i><i class="l15-sc s1">testit: 1/3</i><i class="l15-sc s2">testit: 2/3</i><i class="l15-sc s3">testit: 3/3 ✓</i></span></div>
    <div class="l15-in l15-i1"><span class="l15-type tp">positiivinen</span>”Mihin aikaan avaatte?”</div>
    <div class="l15-in l15-i2"><span class="l15-type tn">negatiivinen</span>”Anna minulle sijoitusneuvo.”</div>
    <div class="l15-in l15-i3"><span class="l15-type te">reunatapaus</span>”      ” (tyhjä viesti)</div>
    <div class="l15-out l15-o1">”Avaamme klo 9.” <b class="l15-okk">✓ vastaa oikein</b></div>
    <div class="l15-out l15-o2">”En anna sijoitusneuvoja — ohjaan henkilökunnalle.” <b class="l15-okk">✓ kieltäytyy oikein</b></div>
    <div class="l15-out l15-o3">”Kirjoitathan kysymyksen, niin autan.” <b class="l15-okk">✓ ei kaadu</b></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Hyvä botti testataan kolmella tavalla: positiivinen testi varmistaa, että se osaa vastata; negatiivinen, että se osaa kieltäytyä; reunatapaus, että se kestää oudot syötteet. Jos yksikin pettää, korjaa ohjeistusta ja testaa uudelleen.</figcaption></figure>
<style>
.l15-wrap{position:relative;width:560px;height:258px;font-family:var(--font-mono)}
.l15-bot{position:absolute;left:218px;top:96px;width:124px;text-align:center;font-size:13px;letter-spacing:.14em;color:#EAEEF8;background:#11182A;border:2px solid oklch(0.66 0.15 305);border-radius:12px;padding:13px 8px 28px}
.l15-score{position:absolute;left:8px;right:8px;bottom:7px;height:16px}
.l15-sc{position:absolute;inset:0;font-style:normal;font-size:10px;letter-spacing:.04em;color:#B9C2DA;opacity:0}
.l15-sc.s0{animation:l15s0 13.5s infinite}.l15-sc.s1{animation:l15s1 13.5s infinite}.l15-sc.s2{animation:l15s2 13.5s infinite}.l15-sc.s3{animation:l15s3 13.5s infinite;color:#7FD0A8}
@keyframes l15s0{0%{opacity:1}13%{opacity:1}16%{opacity:0}97%{opacity:0}100%{opacity:1}}
@keyframes l15s1{0%,13%{opacity:0}16%,44%{opacity:1}47%,100%{opacity:0}}
@keyframes l15s2{0%,44%{opacity:0}47%,75%{opacity:1}78%,100%{opacity:0}}
@keyframes l15s3{0%,75%{opacity:0}78%,97%{opacity:1}100%{opacity:0}}
.l15-in{position:absolute;left:0;width:196px;font-size:11.5px;line-height:1.4;color:#06212A;background:#46c7cf;font-weight:500;border-radius:10px;padding:8px 10px;opacity:0}
.l15-i1{top:8px;animation:l15i1 13.5s infinite}
.l15-i2{top:96px;animation:l15i2 13.5s infinite}
.l15-i3{top:188px;animation:l15i3 13.5s infinite}
@keyframes l15i1{0%,1%{opacity:0;transform:translateX(-14px)}5%,26%{opacity:1;transform:translateX(0)}30%,100%{opacity:0}}
@keyframes l15i2{0%,32%{opacity:0;transform:translateX(-14px)}36%,57%{opacity:1;transform:translateX(0)}61%,100%{opacity:0}}
@keyframes l15i3{0%,63%{opacity:0;transform:translateX(-14px)}67%,88%{opacity:1;transform:translateX(0)}92%,100%{opacity:0}}
.l15-type{display:block;margin-bottom:4px;font-size:9.5px;letter-spacing:.09em;text-transform:uppercase;border-radius:999px;padding:1px 7px;width:fit-content}
.l15-type.tp{color:#06241a;background:#7FD0A8}
.l15-type.tn{color:#3A1408;background:#F0A38C}
.l15-type.te{color:#1d1230;background:#c9b7f1}
.l15-out{position:absolute;left:364px;width:196px;font-size:11.5px;line-height:1.45;color:#FFFFFF;background:#1E2740;border:1.5px solid #44517A;border-radius:10px;padding:8px 10px;opacity:0}
.l15-o1{top:8px;animation:l15o1 13.5s infinite}
.l15-o2{top:88px;animation:l15o2 13.5s infinite}
.l15-o3{top:188px;animation:l15o3 13.5s infinite}
@keyframes l15o1{0%,9%{opacity:0;transform:translateX(14px)}13%,26%{opacity:1;transform:translateX(0)}30%,100%{opacity:0}}
@keyframes l15o2{0%,40%{opacity:0;transform:translateX(14px)}44%,57%{opacity:1;transform:translateX(0)}61%,100%{opacity:0}}
@keyframes l15o3{0%,71%{opacity:0;transform:translateX(14px)}75%,88%{opacity:1;transform:translateX(0)}92%,100%{opacity:0}}
.l15-okk{display:block;margin-top:5px;font-weight:600;font-size:10.5px;letter-spacing:.04em;color:#7FD0A8}
@media (prefers-reduced-motion:reduce){
.l15-sc,.l15-in,.l15-out{animation:none}
.l15-sc.s0,.l15-sc.s1,.l15-sc.s2{opacity:0}.l15-sc.s3{opacity:1}
.l15-in,.l15-out{opacity:1}}
</style>

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
