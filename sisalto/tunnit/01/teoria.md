# Älykäs vai sääntöpohjainen? Mitä tekoäly oikeasti tekee?

## Johdanto

Olet varmasti käyttänyt sovellusta, joka suosittelee sinulle musiikkia, elokuvia tai tuotteita. Ehkä olet joskus ajatellut: ”Miten tämä tietää, mistä minä pidän?” Tai olet nähnyt uutisen tekoälystä, joka voitti maailman parhaan pelaajan shakissa.

Monet ajattelevat, että kaikki ”älykkäältä” vaikuttavat ohjelmistot ovat tekoälyä. Todellisuus on kuitenkin monimutkaisempi — ja paljon kiinnostavampi. **Tekoäly** (artificial intelligence, AI) ei ole yksi yksittäinen asia vaan kattotermi usealle erilaiselle teknologialle. Siksi on tärkeää ymmärtää, mitä tekoälyllä tarkoitetaan. Mikä erottaa tekoälyn tavallisesta automaatiosta? Miten tekoäly tekee päätöksiä, ja miksi se soveltuu joihinkin ongelmiin paremmin kuin toisiin?

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

<figure class="ai-demo"><span class="ai-demo__tag">// sama tapaus, kaksi tapaa päättää — yksi raja vai painotetut signaalit</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:332px">
  <div class="l01-wrap">
    <div class="l01-case"><span class="l01-cs c1">Siirto 12 500 € · klo 14 · tuttu laite</span><span class="l01-cs c2">Siirto 90 € · klo 03 · uusi laite · 5. kerta tänään</span></div>
    <div class="l01-judge l01-rule"><span class="l01-jh">SÄÄNTÖ</span><span class="l01-jr">jos summa &gt; 10 000 € → hälytä</span><span class="l01-jr2">muita signaaleja ei katsota</span><span class="l01-verd l01-v1a">✓ hälytys — raja ylittyi</span><span class="l01-verd l01-v1b">läpi — ei osu sääntöön</span></div>
    <div class="l01-judge l01-ai"><span class="l01-jh">TEKOÄLY — painottaa joka signaalin</span>
      <div class="l01-row"><span class="l01-rn">summa</span><div class="l01-rb"><i class="b1"></i></div><b class="l01-rv vA">+0,62</b><b class="l01-rv vB">+0,04</b></div>
      <div class="l01-row"><span class="l01-rn">kellonaika</span><div class="l01-rb"><i class="b2"></i></div><b class="l01-rv vA">+0,08</b><b class="l01-rv vB">+0,31</b></div>
      <div class="l01-row"><span class="l01-rn">laite</span><div class="l01-rb"><i class="b3"></i></div><b class="l01-rv vA">+0,05</b><b class="l01-rv vB">+0,27</b></div>
      <div class="l01-row"><span class="l01-rn">toisto</span><div class="l01-rb"><i class="b4"></i></div><b class="l01-rv vA">+0,18</b><b class="l01-rv vB">+0,29</b></div>
      <div class="l01-sum"><span class="l01-eqbox"><i class="l01-eq eA">0,62 + 0,08 + 0,05 + 0,18 = <b>0,93</b></i><i class="l01-eq eB">0,04 + 0,31 + 0,27 + 0,29 = <b>0,91</b></i></span><div class="l01-mb"><div class="l01-meter"></div></div><b class="l01-pct pA">93 %</b><b class="l01-pct pB">91 %</b></div>
      <span class="l01-verd l01-v2a">✓ hälytys — kynnys 80 % ylittyi</span><span class="l01-verd l01-v2b">✓ hälytys — kynnys 80 % ylittyi</span>
    </div>
    <span class="l01-miss">⚠ petos pääsi läpi</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Kiinteä sääntö katsoo yhtä rajaa: ison summan se nappaa, mutta oudon pienen tapauksen se päästää läpi. Opittu malli antaa jokaiselle signaalille painon ja laskee painot yhteen todennäköisyydeksi (palkkien pituudet = painot) — kun kynnys ylittyy, se hälyttää, vaikka mikään yksittäinen raja ei ylittyisi.</figcaption></figure>
<style>
.l01-wrap{position:relative;width:560px;height:296px;font-family:var(--font-mono)}
.l01-case{position:absolute;left:50%;transform:translateX(-50%);top:0;width:440px;height:34px}
.l01-cs{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;font-size:12px;font-weight:500;color:#06212A;background:#46c7cf;border-radius:10px;padding:2px 10px;opacity:0}
.l01-cs.c1{animation:l01c1 14s infinite}
.l01-cs.c2{animation:l01c2 14s infinite}
@keyframes l01c1{0%,2%{opacity:0}5%,44%{opacity:1}48%,100%{opacity:0}}
@keyframes l01c2{0%,50%{opacity:0}53%,96%{opacity:1}100%{opacity:0}}
.l01-judge{position:absolute;top:50px;min-height:220px;background:#11182A;border:2px solid #2B3552;border-radius:13px;padding:11px 13px}
.l01-rule{left:0;width:225px}
.l01-ai{right:0;width:318px;border-color:oklch(0.66 0.15 264)}
.l01-jh{display:block;font-size:10.5px;letter-spacing:.1em;color:#B9C2DA;margin-bottom:9px}
.l01-jr{display:block;font-size:11.5px;line-height:1.4;color:#EAEEF8;background:#0E1422;border:1px solid #232C44;border-radius:8px;padding:7px 9px}
.l01-jr2{display:block;margin-top:7px;font-size:10.5px;color:#5D6880}
.l01-row{display:flex;align-items:center;gap:8px;margin-bottom:7px;position:relative}
.l01-rn{width:78px;font-size:11px;color:#EAEEF8}
.l01-rb{flex:1;height:8px;border-radius:99px;background:#0B0F1A;border:1px solid #232C44;overflow:hidden}
.l01-rb i{display:block;height:100%;border-radius:99px;background:oklch(0.68 0.15 264)}
.l01-rb i.b1{animation:l01b1 14s infinite}
.l01-rb i.b2{animation:l01b2 14s infinite}
.l01-rb i.b3{animation:l01b3 14s infinite}
.l01-rb i.b4{animation:l01b4 14s infinite}
@keyframes l01b1{0%,8%{width:0}14%,46%{width:62%}56%,96%{width:4%}100%{width:0}}
@keyframes l01b2{0%,9%{width:0}15%,46%{width:8%}57%,96%{width:31%}100%{width:0}}
@keyframes l01b3{0%,10%{width:0}16%,46%{width:5%}58%,96%{width:27%}100%{width:0}}
@keyframes l01b4{0%,11%{width:0}17%,46%{width:18%}59%,96%{width:29%}100%{width:0}}
.l01-rv{position:absolute;right:0;width:44px;text-align:right;font-size:10.5px;font-weight:600;color:#B9C2DA;opacity:0}
.l01-row .l01-rv.vA{animation:l01vA 14s infinite}
.l01-row .l01-rv.vB{animation:l01vB 14s infinite}
@keyframes l01vA{0%,12%{opacity:0}16%,46%{opacity:1}50%,100%{opacity:0}}
@keyframes l01vB{0%,56%{opacity:0}60%,96%{opacity:1}100%{opacity:0}}
.l01-row{padding-right:48px}
.l01-sum{position:relative;margin-top:9px;padding-right:48px}
.l01-sum .l01-eqbox{display:block;position:relative;height:15px;margin-bottom:4px}
.l01-eq{position:absolute;left:0;font-style:normal;font-size:10.5px;letter-spacing:.04em;color:#8B94B3;opacity:0}
.l01-eq b{color:#EAEEF8;font-weight:700}
.l01-eq.eA{animation:l01vA 14s infinite}
.l01-eq.eB{animation:l01vB 14s infinite}
.l01-mb{height:9px;border-radius:99px;background:#0B0F1A;border:1px solid #232C44;overflow:hidden}
.l01-meter{height:100%;border-radius:99px;background:linear-gradient(90deg,oklch(0.66 0.15 264),#F0A38C);animation:l01meter 14s infinite}
@keyframes l01meter{0%,12%{width:6%}20%,46%{width:93%}56%,62%{width:6%}70%,96%{width:91%}100%{width:6%}}
.l01-pct{position:absolute;right:0;bottom:0;font-size:11.5px;font-weight:700;color:#F0A38C;opacity:0}
.l01-pct.pA{animation:l01vA 14s infinite}
.l01-pct.pB{animation:l01vB 14s infinite}
.l01-verd{position:absolute;left:13px;right:13px;bottom:11px;font-size:11px;letter-spacing:.03em;border-radius:8px;padding:6px 9px;opacity:0}
.l01-v1a{color:#06241a;background:#7FD0A8;animation:l01v1a 14s infinite}
.l01-v1b{color:#3A1408;background:#F0A38C;animation:l01v1b 14s infinite}
.l01-v2a{color:#06241a;background:#7FD0A8;animation:l01v2a 14s infinite}
.l01-v2b{color:#06241a;background:#7FD0A8;animation:l01v2b 14s infinite}
@keyframes l01v1a{0%,14%{opacity:0}18%,44%{opacity:1}48%,100%{opacity:0}}
@keyframes l01v1b{0%,60%{opacity:0}64%,93%{opacity:1}97%,100%{opacity:0}}
@keyframes l01v2a{0%,22%{opacity:0}26%,44%{opacity:1}48%,100%{opacity:0}}
@keyframes l01v2b{0%,72%{opacity:0}76%,93%{opacity:1}97%,100%{opacity:0}}
.l01-miss{position:absolute;left:36px;top:276px;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:#F0A38C;opacity:0;animation:l01miss 14s infinite}
@keyframes l01miss{0%,68%{opacity:0}72%,93%{opacity:1}97%,100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l01-cs,.l01-rb i,.l01-rv,.l01-meter,.l01-pct,.l01-verd,.l01-miss,.l01-eq{animation:none}
.l01-cs.c2,.l01-v1b,.l01-v2b,.l01-miss,.l01-rv.vB,.l01-pct.pB,.l01-eq.eB{opacity:1}
.l01-rb i.b1{width:6%}.l01-rb i.b2{width:42%}.l01-rb i.b3{width:37%}.l01-rb i.b4{width:40%}
.l01-meter{width:91%}}
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
