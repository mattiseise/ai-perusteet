# Älykäs vai sääntöpohjainen? Mitä tekoäly oikeasti tekee?

## Johdanto

Olet varmasti käyttänyt sovellusta, joka suosittelee sinulle musiikkia, elokuvia tai tuotteita. Ehkä olet joskus ajatellut: ”Miten tämä tietää, mistä minä pidän?” Tai olet nähnyt uutisen tekoälystä, joka voitti maailman parhaan pelaajan shakissa.

Monet ajattelevat, että kaikki ”älykkäältä” vaikuttavat ohjelmistot ovat tekoälyä. Todellisuus on kuitenkin monimutkaisempi — ja paljon kiinnostavampi. **Tekoäly** (artificial intelligence, AI) ei ole yksi yksittäinen asia. Se ei myöskään ole yksi ohjelmointitapa, joka osaa tehdä tai ymmärtää kaiken.

Tämän osion jälkeen ymmärrät, miten **tekoäly** eroaa tavallisesta ohjelmoinnista. Osaat myös arvioida paremmin, millaiset ongelmat vaativat tekoälyä ja millaiset voidaan ratkaista ilman sitä.

Tämän tunnin jälkeen ymmärrät: *tietävätkö tekoälyt todella, mitä ne tekevät, vai ovatko ne vain edistyneitä sääntökoneita?*

## Mitä tekoäly oikeasti on?

**Tekoäly** on ohjelma tai järjestelmä, joka oppii datasta eikä ainoastaan noudata ennalta kirjoitettuja sääntöjä. Se voi tehdä päätöksiä tai ennustaa asioita muuttuvissa tilanteissa ilman, että jokainen mahdollinen tapaus täytyy ohjelmoida käsin.

Kuvitellaan pankin **petoksentunnistusjärjestelmä**. Perinteinen sääntöpohjainen järjestelmä voisi toimia esimerkiksi näin: ”Jos tapahtuma on yli 10 000 euroa, lähetä hälytys operaattorille.” Tällainen ratkaisu on yksinkertainen ja nopea, mutta samalla melko rajallinen.

Todellinen petos voi liittyä paljon pienempään summaan, ja yksittäinen rahansiirto voi näyttää täysin normaalilta. Tapaus muuttuu usein epäilyttäväksi vasta silloin, kun sitä tarkastellaan osana laajempaa kokonaisuutta, kuten asiakkaan aiempaa käyttäytymistä.

Tekoäly toimii eri tavalla. Se voi oppia miljoonista oikeista transaktioista ja löytää niistä yhteyksiä ja poikkeamia, joita ihminen tai yksinkertainen sääntöjärjestelmä ei välttämättä huomaisi. Tekoäly ei siis perustu vain yksittäisiin sääntöihin, kuten ”jos X, niin Y”, vaan muodostaa datan perusteella arvion siitä, kuinka todennäköisesti tapahtuma on laillinen tai petollinen.

Esimerkiksi tekoäly voi arvioida: ”Tämän tapahtuman todennäköisyys olla laillinen on 97 prosenttia.”

> **Pysähdy hetkeksi:** Kuinka moni päivittäin käyttämäsi sovellus hyödyntää tekoälyä päätösten tekemisessä? Miten ne eroavat sovelluksista, joissa käytetään vain kiinteitä sääntöjä?

## Ero automaatioon ja tavalliseen ohjelmointiin

Monet sekoittavat tekoälyn **automaatioon**. Ajatus voi olla esimerkiksi tällainen: ”Tämä ohjelmisto teki työn automaattisesti, joten sen täytyy olla tekoälyä.” Näin ei kuitenkaan välttämättä ole.

**Automaatio** tarkoittaa sitä, että tietokone tekee työn ilman, että käyttäjän tarvitsee suorittaa jokaista vaihetta itse. Automaatio ei kuitenkaan välttämättä opi mitään.

Esimerkiksi sähköpostisovelluksessa voi olla sääntöjä, jotka lajittelevat viestit automaattisesti kansioihin. Jos sähköposti sisältää sanat ”lasku” ja ”lomauttaminen”, se voidaan siirtää kansioon ”Juridinen”. Nämä ovat **kiinteitä sääntöjä**: ne eivät opi eivätkä muutu itsestään. Kyse on automaatiosta, ei tekoälystä.

Monissa IT-alan järjestelmissä käytetään **robottista prosessiautomaatiota** (RPA, Robotic Process Automation). RPA-robotti voi esimerkiksi avata asiakaspalvelujärjestelmän, lukea tiketin, täyttää lomakkeen ja lähettää vastauksen automaattisesti ympäri vuorokauden.

Tämä on nopeaa ja tehokasta, mutta kyse on silti rutiinien suorittamisesta. Robotti ei opi asiakkaista eikä paranna toimintaansa ajan myötä, ellei sitä erikseen muuteta.

**Tekoäly oppii datasta.** Se voi muuttua, parantua ja sopeutua uusiin tilanteisiin. Kun petoksentunnistusjärjestelmä kohtaa uudenlaisen petoskuvion, se voi oppia tunnistamaan sen. Tämä ei välttämättä vaadi uusien yksittäisten sääntöjen kirjoittamista, koska toiminta perustuu datasta opittuihin malleihin.

> **Pysähdy hetkeksi:** Jos järjestelmä tekee samat asiat aina samalla tavalla eikä opi kokemuksista, onko se tekoälyä?

## Probabilistinen ja deterministinen ajattelu

Yksi tärkeä ero tekoälyn ja perinteisen ohjelmoinnin välillä liittyy **epävarmuuteen**.

Tavallinen ohjelma toimii usein **deterministisesti**. Se noudattaa ennalta kirjoitettuja sääntöjä ja tuottaa samanlaisessa tilanteessa ennustettavan tuloksen. Tekoäly puolestaan toimii usein **todennäköisyyksien** varassa. Se ei välttämättä anna täysin varmaa vastausta, vaan arvion siitä, mikä lopputulos on datan perusteella todennäköisin.

Tämä on **koneoppimisen** ydin: päätöksiä tehdään epätäydellisen datan pohjalta epävarmassa maailmassa.

Kun sähköpostiin tulee viesti, perinteinen roskapostisuodatin voi tarkistaa ennalta määriteltyjä sääntöjä. Se voi esimerkiksi toimia näin: ”Jos otsikossa on paljon isoja kirjaimia ja useita huutomerkkejä, merkitse viesti roskapostiksi.” Tämä on yksinkertainen toimintatapa, mutta samalla rajallinen, koska uudet roskapostit osaavat yhä paremmin näyttää tavallisilta viesteiltä.

Tekoäly toimii toisin. Se on voinut nähdä miljoonia todellisia roskapostiviestejä ja tavallisia viestejä. Sen perusteella se voi arvioida: ”Tämä viesti muistuttaa 92-prosenttisesti aiemmin nähtyjä roskapostiviestejä.”

Tekoäly ei siis tarvitse jokaista sääntöä erikseen kirjoitettuna. Sääntöjen sijaan sillä on **parametreja** eli datasta opittuja numeroarvoja, jotka ohjaavat sen toimintaa.

> **Pysähdy hetkeksi:** Miksi epävarmuuden käsittely on tekoälylle hyödyllistä, mutta tavalliselle ohjelmalle usein ongelmallista?

<figure class="ai-demo"><span class="ai-demo__tag">// sääntö vai todennäköisyys</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:space-around;gap:18px;padding:0 24px">
  <svg viewBox="0 0 230 150" style="width:46%;height:90%" preserveAspectRatio="xMidYMid meet">
    <text x="115" y="20" text-anchor="middle" font-family="var(--font-mono)" font-size="10" fill="#7E88A8">SÄÄNTÖ</text>
    <g stroke="oklch(0.66 0.13 208)" stroke-width="2" fill="none">
      <line x1="40" y1="70" x2="100" y2="70"/><line x1="130" y1="70" x2="190" y2="70"/>
    </g>
    <rect x="100" y="56" width="30" height="28" rx="4" fill="none" stroke="oklch(0.66 0.13 208)" stroke-width="2"/>
    <circle class="l01rule-tick" cx="40" cy="70" r="5" fill="oklch(0.66 0.13 208)"/>
    <rect x="180" y="58" width="20" height="24" rx="4" fill="oklch(0.66 0.13 208)"/>
    <text x="115" y="110" text-anchor="middle" font-family="var(--font-mono)" font-size="9" fill="#8B94B3">jos X → niin Y</text>
  </svg>
  <svg viewBox="0 0 230 150" style="width:46%;height:90%" preserveAspectRatio="xMidYMid meet">
    <text x="115" y="20" text-anchor="middle" font-family="var(--font-mono)" font-size="10" fill="#7E88A8">TODENNÄKÖISYYS</text>
    <g stroke="oklch(0.66 0.15 264)" stroke-width="1" opacity=".25">
      <line x1="40" y1="55" x2="115" y2="78"/><line x1="40" y1="100" x2="115" y2="78"/>
      <line x1="115" y1="78" x2="190" y2="50"/><line x1="115" y1="78" x2="190" y2="105"/>
    </g>
    <g fill="oklch(0.66 0.15 264)">
      <circle class="l01rule-node" cx="40" cy="55" r="4"/>
      <circle class="l01rule-node" cx="40" cy="100" r="4" style="animation-delay:.5s"/>
      <circle class="l01rule-node" cx="115" cy="78" r="4" style="animation-delay:1s"/>
      <circle class="l01rule-node" cx="190" cy="50" r="4" style="animation-delay:1.5s"/>
      <circle class="l01rule-node" cx="190" cy="105" r="4" style="animation-delay:2s"/>
    </g>
    <text x="115" y="135" text-anchor="middle" font-family="var(--font-mono)" font-size="9" fill="#8B94B3">97 % laillinen</text>
  </svg>
</div>
<figcaption class="ai-demo__cap">Sääntöpohjainen järjestelmä seuraa kiinteää polkua (jos X → niin Y). Tekoäly punnitsee monta painotettua yhteyttä ja antaa todennäköisyyden.</figcaption></figure>

<style>
.l01rule-tick{animation:l01ruleTick 3.2s ease-in-out infinite}
@keyframes l01ruleTick{0%,100%{opacity:.35}50%{opacity:1}}
.l01rule-node{animation:l01ruleBlink 3.4s ease-in-out infinite}
@keyframes l01ruleBlink{0%,100%{opacity:.35;r:3}50%{opacity:1;r:4.6}}
@media (prefers-reduced-motion:reduce){.l01rule-tick,.l01rule-node{animation:none}.l01rule-node{opacity:.9}}
</style>

## Konkreettisia esimerkkejä arjesta

Pankkisektorilla tekoälyä käytetään laajasti, mutta ei kaikessa. Esimerkiksi verkkopankissa näkyvät toiminnot, kuten ”Maksa lasku” ja ”Siirry tilille”, perustuvat tavalliseen ohjelmointiin ja ennalta määriteltyihin sääntöihin.

Sen sijaan **petoksentunnistuksessa** voidaan hyödyntää tekoälyä. Myös lainahakemuksen automaattinen hyväksyminen tai hylkääminen voi perustua **koneoppimismalliin**, joka on oppinut historiallisista hakemuksista ja niiden lopputuloksista.

Sama ero näkyy esimerkiksi koulun tai kunnan palautejärjestelmissä. Yksinkertainen järjestelmä voi ohjata viestejä kiinteiden sääntöjen perusteella. Esimerkiksi sana ”ruokala” voi ohjata viestin suoraan keittiön henkilökunnalle. Tämä on automaatiota, mutta ei vielä tekoälyä.

Kehittyneempi järjestelmä voi hyödyntää tekoälymalleja, jotka ennustavat esimerkiksi sen, kuinka kiireellinen viesti on tai kenelle se kannattaisi ohjata. Tällöin järjestelmä ei perustu vain yksittäisiin sääntöihin, vaan oppii aiemmista tapauksista ja toimintamalleista.

Netflixin, Spotifyn ja verkkokauppojen **suositukset** ovat hyvä esimerkki tekoälyn käytöstä. Ne eivät toimi pelkkien yksinkertaisten sääntöjen varassa, vaan oppivat miljoonista käyttäjien valinnoista, mieltymyksistä ja käyttäytymismalleista. Tämän perusteella ne pyrkivät ennustamaan, mitä haluat nähdä, kuunnella tai ostaa seuraavaksi.

## Yhteenveto

**Tekoäly** ei tarkoita mitä tahansa älykkäältä vaikuttavaa ohjelmistoa, eikä se ole sama asia kuin automaatio. Tekoäly on järjestelmä, joka oppii datasta ja tekee arvioita tai päätöksiä todennäköisyyksien perusteella ilman, että kaikki säännöt on kirjoitettu sille valmiiksi.

**Automaatio** ja **sääntöpohjaiset järjestelmät** ovat usein tarkkoja, nopeita ja ennustettavia. Tekoälyn vahvuus taas on siinä, että se on joustavampi ja pystyy oppimaan monimutkaisista ilmiöistä.

Kun ymmärrät tämän eron, sinun on helpompi hahmottaa, miksi jotkin ongelmat vaativat tekoälyä ja toiset voidaan ratkaista hyvin tavallisella ohjelmointilogiikalla.

Seuraavalla tunnilla perehdyt siihen, millaisia tekoälyn eri tyyppejä on olemassa — ja miksi ”älykkyyttä” voi olla monessa muodossa.

---
