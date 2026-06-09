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

<figure class="ai-demo"><span class="ai-demo__tag">// sama tapaus, kaksi tapaa päättää</span>
<div class="ai-demo__stage" style="display:flex;gap:18px;align-items:stretch;justify-content:center;padding:16px 22px">
  <div class="l01-col">
    <div class="l01-h">SÄÄNTÖ</div>
    <div class="l01-rule">jos summa &gt; 10 000 € → hälytä</div>
    <div class="l01-in">tapahtuma: 9 990 €</div>
    <div class="l01-out l01-ok">→ ei hälytystä</div>
    <div class="l01-miss">petos jäi huomaamatta</div>
  </div>
  <div class="l01-col">
    <div class="l01-h" style="color:oklch(0.66 0.15 264)">TEKOÄLY</div>
    <div class="l01-sigs"><span class="l01-sig s1">summa</span><span class="l01-sig s2">sijainti</span><span class="l01-sig s3">kellonaika</span><span class="l01-sig s4">historia</span></div>
    <div class="l01-meter"><span class="l01-mfill"></span><span class="l01-mlbl">97 % epäilyttävä</span></div>
    <div class="l01-out l01-flag">⚠ hälytä</div>
  </div>
</div>
<figcaption class="ai-demo__cap">Kiinteä sääntö katsoo yhtä rajaa ja päästää poikkeuksen läpi. Tekoäly punnitsee monta signaalia yhtä aikaa ja antaa todennäköisyyden — siksi se huomaa epätavallisen kuvion.</figcaption></figure>
<style>
.l01-col{flex:1;max-width:240px;border:1px solid #232C44;border-radius:10px;background:#11182A;padding:14px;display:flex;flex-direction:column;gap:9px}
.l01-h{font-family:var(--font-mono);font-size:11px;letter-spacing:.18em;color:#8B94B3}
.l01-rule{font-family:var(--font-mono);font-size:10.5px;color:#8B94B3;line-height:1.4}
.l01-in{font-family:var(--font-mono);font-size:11px;color:#C7CEE6;background:#1A2236;border:1px solid #2A3450;border-radius:6px;padding:5px 9px}
.l01-out{font-family:var(--font-mono);font-size:12px;font-weight:500;margin-top:auto}
.l01-ok{color:#6FBF9B}
.l01-miss{font-family:var(--font-mono);font-size:10px;color:#E0796B;opacity:0;animation:l01miss 11s ease-in-out infinite}
@keyframes l01miss{0%,40%{opacity:0}52%,94%{opacity:1}100%{opacity:0}}
.l01-sigs{display:flex;flex-wrap:wrap;gap:5px}
.l01-sig{font-family:var(--font-mono);font-size:9px;color:#69728F;border:1px solid #2A3450;border-radius:999px;padding:2px 8px;opacity:.3}
.l01-sig.s1{animation:l01sig 11s ease-in-out infinite}
.l01-sig.s2{animation:l01sig 11s ease-in-out infinite;animation-delay:.6s}
.l01-sig.s3{animation:l01sig 11s ease-in-out infinite;animation-delay:1.2s}
.l01-sig.s4{animation:l01sig 11s ease-in-out infinite;animation-delay:1.8s}
@keyframes l01sig{0%{opacity:.3}18%,94%{opacity:1;color:oklch(0.66 0.15 264);border-color:oklch(0.66 0.15 264)}100%{opacity:.3}}
.l01-meter{position:relative;height:18px;border:1px solid #2A3450;border-radius:5px;overflow:hidden;background:#0E1320}
.l01-mfill{position:absolute;inset:0;width:0;background:linear-gradient(90deg,oklch(0.66 0.15 264),oklch(0.66 0.15 305));animation:l01fill 11s ease-in-out infinite}
.l01-mlbl{position:absolute;right:7px;top:2px;font-family:var(--font-mono);font-size:10px;color:#E6EAF5}
@keyframes l01fill{0%,28%{width:4%}52%{width:97%}94%{width:97%}100%{width:4%}}
.l01-flag{color:oklch(0.66 0.15 305)}
@media (prefers-reduced-motion:reduce){.l01-miss,.l01-sig,.l01-mfill{animation:none}.l01-miss{opacity:1}.l01-sig{opacity:1;color:oklch(0.66 0.15 264);border-color:oklch(0.66 0.15 264)}.l01-mfill{width:97%}}
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
