# Mitä nykytekoäly osaa — ja mitä AGI ja ASI tarkoittavat?

## Johdanto

Roskapostikansioon päätyy yleensä viestejä, joita et halua lukea. Joskus suodatin kuitenkin erehtyy: tärkeä viesti katoaa roskapostiin tai huijausviesti jää saapuneisiin. Tämän tutun esimerkin avulla voit seurata, miten tekoälymalli oppii ja miksi sen toimintaa pitää tarkistaa myös käyttöönoton jälkeen.

Tunnilla etsit vastauksen kolmeen kysymykseen:

1. Miten malli oppii esimerkeistä ja miten sen toiminta tarkistetaan?
2. Miksi mallia pitää seurata käytössä?
3. Miksi nykyisen järjestelmän onnistuminen ei vielä osoita AGI:a tai ASI:a?

## Sääntö vai esimerkeistä oppiva malli?

Roskapostia voi käsitellä yksinkertaisella säännöllä: jos lähettäjän osoite on estolistalla, siirrä viesti roskapostiin. Ihminen on kirjoittanut ehdon etukäteen, ja järjestelmä noudattaa sitä.

Koneoppimismalli toimii eri tavalla. Sille näytetään paljon viestejä, joista tiedetään, mitkä ovat roskapostia ja mitkä tavallisia viestejä. Malli etsii esimerkeistä yhteyksiä ja muodostaa niiden perusteella arvion uudesta viestistä. Todellinen sähköpostipalvelu voi käyttää sekä ihmisen kirjoittamia sääntöjä että koulutettua mallia.

Tässä esimerkissä malli ei opi samalla hetkellä, kun se arvioi sinun viestiäsi. Ensin se **koulutetaan** esimerkkiaineistolla. Sen jälkeen koulutettua mallia käytetään uusien viestien arviointiin.

<figure class="ai-demo"><span class="ai-demo__tag" id="l02a-t"><i aria-hidden="true">// </i>sääntö ja esimerkeistä oppiva malli</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:230px">
  <div class="l02a-wrap" data-once role="img" aria-labelledby="l02a-t" aria-describedby="l02a-d">
    <span class="sr-only" id="l02a-d">Sääntöpohjainen suodatin seuraa ihmisen kirjoittamaa ehtoa. Koulutettu malli muodostaa esimerkeistä oppimansa perusteella arvion uudesta viestistä.</span>
    <div class="l02a-c c1"><strong style="display:block;margin-bottom:12px;color:#7FD0A8">SÄÄNTÖ</strong><span>Ihminen kirjoittaa ehdon:<br>estolistalla → roskapostiin</span></div>
    <div class="l02a-c c2"><strong style="display:block;margin-bottom:12px;color:#C9B7F1">KOULUTETTU MALLI</strong><span>Merkityt esimerkit → arvio uudesta viestistä</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Sääntö noudattaa ihmisen kirjoittamaa ehtoa. Koulutettu malli muodostaa esimerkeistä oppimansa perusteella arvion uudesta viestistä.</figcaption></figure>
<style>
.l02a-wrap{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:560px;animation:l02aw 10s 1 forwards}
@keyframes l02aw{0%,100%{opacity:1}}
.l02a-c{padding:24px;border:1px solid #34415F;border-radius:14px;background:#172038;color:#EAEEF8;opacity:0;transform:translateY(10px)}
.l02a-c.c1{animation:l02a1 10s 1 forwards}
.l02a-c.c2{animation:l02a2 10s 1 forwards}
@keyframes l02a1{0%,5%{opacity:0;transform:translateY(10px)}18%,100%{opacity:1;transform:none}}
@keyframes l02a2{0%,34%{opacity:0;transform:translateY(10px)}
  48%{opacity:1;transform:none;border-color:#34415F}
  62%{opacity:1;transform:none;border-color:#C9B7F1}
  78%,100%{opacity:1;transform:none;border-color:#34415F}}
@media (max-width:680px){.l02a-wrap{width:100%;grid-template-columns:1fr}}
</style>

## Kolme aineistoa, kolme tehtävää

Mallille kerättyä aineistoa ei käytetä yhtenä suurena kasana. Se jaetaan tavallisesti kolmeen osaan.

**Koulutusaineisto** on harjoittelua varten. Roskapostimalli oppii siitä, millaisia yhteyksiä viestien ja oikeiden luokkien välillä on.

**Validointiaineisto** auttaa vertailemaan malliversioita rakentamisen aikana. Sen avulla valitaan toimivampi versio ja säädetään rakentamisen valintoja.

**Testiaineisto** pidetään erillään viimeistä tarkistusta varten. Sillä arvioidaan valittua mallia tapauksissa, joita ei käytetty kouluttamiseen tai malliversion valintaan.

Ajattele opiskelua. Harjoitustehtävien avulla opit, harjoituskokeen avulla huomaat korjattavaa ja lopullinen koe näyttää, miten selviydyt uusista kysymyksistä. Jos katsot lopullisen kokeen vastaukset jo harjoittelun aikana, koe ei enää kerro luotettavasti osaamisestasi. Samasta syystä testiaineistoa ei käytetä mallin säätämiseen.

## Yleistyminen ja ylioppiminen

Hyvä malli ei vain muista näkemiään viestejä. Sen pitää osata arvioida myös uusia samankaltaisia viestejä. Tätä kutsutaan **yleistymiseksi**.

**Ylioppiminen** tarkoittaa, että malli mukautuu koulutusaineiston yksityiskohtiin liian tarkasti. Se voi näyttää harjoittelussa erinomaiselta mutta epäonnistua uusissa viesteissä. Sama tapahtuu, jos opiskelija opettelee harjoituskokeen vastausrivin ulkoa ymmärtämättä asiaa: uudenlainen kysymys paljastaa ongelman.

Erillinen testiaineisto auttaa huomaamaan ylioppimista. Yksi hyvä testitulos ei silti takaa, että malli toimii aina, kaikkien käyttäjien viesteissä tai tulevaisuudessa.

## Käyttöönotto ei päätä työtä

Kun malli on testattu, se voidaan liittää sähköpostipalveluun. Samalla päätetään, mitä malli saa tehdä ja miten käyttäjä voi korjata virheen. Esimerkiksi viestin voi palauttaa roskapostikansiosta saapuneisiin.

Käytössä mallia **seurataan**. Seurannassa tarkastellaan esimerkiksi sitä, lisääntyvätkö väärin luokitellut viestit tai jääkö uudenlainen huijausviesti tunnistamatta. Maailma muuttuu: viestien aiheet, kirjoitustavat ja huijausten keinot eivät pysy samoina.

Jos toiminta heikkenee, syy selvitetään. Aineistoa voidaan täydentää, malli kouluttaa uudelleen ja uusi versio testata ennen käyttöönottoa. Käytössä oleva malli ei korjaa itseään automaattisesti vain siksi, että se näkee uusia viestejä.

> **Pysähdy hetkeksi:** Miksi viime vuoden hyvä testitulos ei yksin riitä osoittamaan, että roskapostimalli toimii hyvin tänään?

## Mitä nykyiset järjestelmät osaavat?

Mallin onnistumista kannattaa kuvata sen mukaan, mitä sen on osoitettu tekevän. Roskapostimalli tekee rajattua tunnistustehtävää. Tekstiä tuottava järjestelmä voi puolestaan kirjoittaa luonnoksen varoitusviestistä. Näitä toimintoja kuvaavat käsitteet **kapea tekoäly** ja **generatiivinen tekoäly**.

### Kapea tekoäly — rajattu tehtävä

Kapea tekoäly on rakennettu tiettyä tehtävää tai rajattua tehtäväjoukkoa varten. Roskapostimalli voi olla omassa tehtävässään erittäin hyvä, mutta se ei siksi osaa suunnitella matkaa, opettaa matematiikkaa tai hoitaa mitä tahansa muuta tehtävää.

Kapea ei siis tarkoita huonoa. Se tarkoittaa, että osaamisella on rajat.

### Generatiivinen tekoäly — tuottaa sisältöä

Generatiivinen tekoäly tuottaa esimerkiksi tekstiä, kuvia, ääntä tai videota. Sähköpostipalvelun tekstitekoäly voisi luonnostella vastauksen käyttäjän puolesta. Tuotos voi olla hyödyllinen, mutta se voi myös sisältää virheitä ja vaatii siksi tarkistamista.

Kapea ja generatiivinen eivät ole vastakohtia. **Sama järjestelmä voi olla molempia.** Järjestelmä voi tuottaa tekstiä ja silti toimia vain rajatussa tehtävässä tai rajatussa toimintaympäristössä. Generatiivisuus kertoo, että järjestelmä tuottaa sisältöä. Se ei yksin kerro, kuinka laajasti järjestelmä osaa oppia ja toimia.

## Tässä kulkee nykyisyyden raja

Kapeaa ja generatiivista tekoälyä käytetään jo nyt. **AGI** ja **ASI** ovat eri asia: ne ovat tulevaisuutta koskevia käsitteitä, eivät nykyisten tuotteiden tavallisia ominaisuuksia tai kehityksen varmoja seuraavia vaiheita.

### AGI — yleisen tekoälyn ajatus

**AGI** on lyhenne sanoista *artificial general intelligence*. Sillä tarkoitetaan yleensä tekoälyä, joka pystyisi oppimaan, soveltamaan osaamistaan ja toimimaan joustavasti hyvin erilaisissa tehtävissä ihmisen tavoin.

AGI:lle ei ole yhtä yleisesti hyväksyttyä määritelmää tai testiä. Yleisesti hyväksyttyä nykyistä AGI-esimerkkiä ei ole. Sujuva keskustelu, hyvä koetulos tai onnistuminen monessa tehtävässä voi olla vaikuttava suoritus, mutta se ei yksin osoita AGI:a.

### ASI — ihmisen kyvyt laajasti ylittävä tekoäly

**ASI** on lyhenne sanoista *artificial superintelligence*. Sillä tarkoitetaan hypoteettista tekoälyä, joka ylittäisi ihmisen kyvyt laajasti esimerkiksi päättelyssä, suunnittelussa ja ongelmanratkaisussa.

ASI on spekulatiivinen käsite. Tällaista järjestelmää ei ole, eikä tiedetä, voitaisiinko sellainen rakentaa. ASI:a ei pidä esitellä nykyteknologiana eikä AGI:n varmana seuraavana vaiheena.

## Neljä käsitettä rinnakkain

| Käsite | Perusajatus | Nykyinen vai tulevaisuutta koskeva? |
|---|---|---|
| Kapea tekoäly | Tekee rajattua tehtävää tai tehtäväjoukkoa | Käytössä nyt |
| Generatiivinen tekoäly | Tuottaa uutta sisältöä | Käytössä nyt |
| AGI | Toimisi joustavasti hyvin erilaisissa tehtävissä | Tulevaisuus- ja tutkimuskäsite; yleisesti hyväksyttyä nykyistä AGI-esimerkkiä ei ole |
| ASI | Ylittäisi ihmisen kyvyt laajasti | Hypoteettinen ja spekulatiivinen käsite |

Taulukko ei ole kehitysportaikko. Kapea ja generatiivinen kuvaavat eri asioita ja voivat toteutua samassa järjestelmässä. AGI ja ASI eivät ole mallin koulutuksen tai päivityksen seuraavia vaiheita.

<figure class="ai-demo"><span class="ai-demo__tag" id="l02b-t"><i aria-hidden="true">// </i>nykyiset järjestelmät ja tulevaisuuskäsitteet</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:250px">
  <div class="l02b-wrap" data-once role="img" aria-labelledby="l02b-t" aria-describedby="l02b-d">
    <span class="sr-only" id="l02b-d">Kapea ja generatiivinen tekoäly ovat käytössä nyt ja voivat kuvata samaa järjestelmää. AGI ja ASI ovat tulevaisuutta koskevia käsitteitä.</span>
    <div class="l02b-c c1"><strong style="display:block;margin-bottom:12px;color:#7FD0A8">KÄYTÖSSÄ NYT</strong><span>Kapea tekoäly<br>Generatiivinen tekoäly<br><small>Sama järjestelmä voi olla molempia.</small></span></div>
    <div class="l02b-c c2"><strong style="display:block;margin-bottom:12px;color:#C9B7F1">TULEVAISUUSKÄSITTEET</strong><span>AGI — yleisesti hyväksyttyä nykyistä AGI-esimerkkiä ei ole<br>ASI — hypoteettinen</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Nykyiset järjestelmät erotetaan AGI:sta ja ASI:sta. Kapea ja generatiivinen eivät ole kehitysportaita tai toisiaan poissulkevia luokkia.</figcaption></figure>
<style>
.l02b-wrap{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:560px;animation:l02bw 10s 1 forwards}
@keyframes l02bw{0%,100%{opacity:1}}
.l02b-c{padding:22px;border-radius:14px;background:#172038;color:#EAEEF8;opacity:0;transform:translateY(10px)}
.l02b-c.c1{border:1px solid #2F9E69;animation:l02b1 10s 1 forwards}
.l02b-c.c2{border:1px dashed #9AA6BD;animation:l02b2 10s 1 forwards}
@keyframes l02b1{0%,5%{opacity:0;transform:translateY(10px)}18%,100%{opacity:1;transform:none}}
/* Tulevaisuuskäsitteet tulevat myöhemmin ja häivähtäen: katkoviiva ja hidas
   ilmestyminen koodaavat sen, ettei näistä ole nykyistä esimerkkiä. */
@keyframes l02b2{0%,36%{opacity:0;transform:translateY(10px)}
  56%{opacity:.55;transform:none}
  74%,100%{opacity:1;transform:none}}
@media (max-width:680px){.l02b-wrap{width:100%;grid-template-columns:1fr}}
</style>

## Kun kohtaat suuren tekoälyväitteen

Jos uutinen kertoo tekoälyn olevan ihmisen veroinen tai ihmistä parempi, aloita näkyvästä näytöstä:

1. Mitä järjestelmä osoitetusti teki?
2. Missä tehtävässä ja millaisissa tilanteissa se onnistui?
3. Mitä tästä ei vielä voida päätellä?

Roskapostin onnistunut tunnistaminen kertoo rajatusta tunnistustehtävästä. Hyvän viestin tuottaminen kertoo sisällön tuottamisesta. Kumpikaan havainto ei yksin osoita, että järjestelmä oppisi minkä tahansa uuden tehtävän tai ylittäisi ihmisen kyvyt laajasti.

## Yhteenveto

Malli oppii koulutusaineistosta. Validointiaineisto auttaa vertailemaan versioita, ja erillinen testiaineisto auttaa tarkistamaan valitun mallin toimintaa uusissa tapauksissa. Hyvä malli yleistää sen sijaan, että se muistaisi koulutusesimerkit liian tarkasti.

Käyttöönoton jälkeen mallia seurataan, koska maailma ja käyttötilanteet muuttuvat. Heikentynyt malli tutkitaan, päivitetään ja testataan hallitusti — se ei opi automaattisesti jokaisesta uudesta viestistä.

Kapea ja generatiivinen tekoäly kuvaavat nykyisiä järjestelmiä, ja sama järjestelmä voi olla molempia. AGI ja ASI ovat tulevaisuutta koskevia käsitteitä. Arvioi aina ensin, mitä järjestelmän on todella osoitettu tekevän.

## Lähteet ja tarkistuspäivä

- [Google for Developers: Datasets, generalization, and overfitting](https://developers.google.com/machine-learning/crash-course/overfitting)
- [Google for Developers: Production ML systems](https://developers.google.com/machine-learning/crash-course/production-ml-systems)
- [OECD: Framework for the Classification of AI Systems](https://oecd.ai/en/ai-publications/framework-classification)
- [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)

Tarkistettu 21.7.2026.
