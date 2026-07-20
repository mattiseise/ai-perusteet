# Millaista tekoälyä on nyt — ja mistä tulevaisuuspuheessa puhutaan?

## Johdanto

Roskapostisuodatin tunnistaa epäilyttävän viestin. Tekstitekoäly luonnostelee vastauksen asiakkaalle. Elokuvassa kone taas oppii hetkessä lähes minkä tahansa taidon. Kaikkia voidaan kutsua tekoälyksi, mutta ne eivät kuvaa samanlaista järjestelmää — eivätkä välttämättä edes nykyistä todellisuutta.

Tällä tunnilla opit viisi käsitettä, joiden avulla erotat nykyiset järjestelmät tulevaisuutta koskevista oletuksista. Tunnin jälkeen osaat selittää, miksi generatiivisuus tai sujuva keskustelu ei yksin osoita yleistä tekoälyä ja miten generatiivinen järjestelmä voi silti olla kyvyiltään rajattu.

## Viisi käsitettä, ei viisi tasoa

Sääntöpohjainen järjestelmä, kapea tekoäly, generatiivinen tekoäly, AGI ja ASI eivät muodosta portaita, joita pitkin teknologia väistämättä etenee. Ne kuvaavat eri asioita. Sääntöpohjaisuus kertoo toteutustavasta, kapeus kykyjen rajauksesta ja generatiivisuus siitä, mitä järjestelmä tekee. AGI ja ASI puolestaan ovat tulevaisuutta koskevia käsitteitä.

Ajattele niitä siis viitenä käsitteenä samalla kartalla — älä viitenä kehitysvaiheena.

## 1. Sääntöpohjainen järjestelmä — ihminen kirjoittaa toimintaohjeen

Sääntöpohjainen järjestelmä noudattaa ennalta kirjoitettuja ehtoja. Laskunkäsittely voi esimerkiksi lähettää yli 10 000 euron laskun tarkistettavaksi. Järjestelmä ei päättele rajaa itse, vaan toimii täsmälleen ihmisen määrittelemän säännön mukaan.

Sääntöpohjainen järjestelmä ei välttämättä ole tekoälyä. Se kuuluu silti tähän kokonaisuuteen, koska sen avulla voi erottaa ihmisen kirjoittamiin sääntöihin perustuvan toiminnan datasta opittuun malliin perustuvasta toiminnasta. Sama palvelu voi myös yhdistää sääntöjä ja tekoälyä.

> **Muista tunnilta 1:** sääntöpohjainen järjestelmä seuraa kirjoitettua ohjetta. Koneoppimismalli soveltaa datasta oppimiaan parametreja uuteen syötteeseen.

<figure class="ai-demo"><span class="ai-demo__tag">// kertaus tunnilta 1 — sääntö vai opittu arvio?</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:210px">
  <div class="l02r-wrap" role="img" aria-label="Vasemmalla sääntöpohjainen järjestelmä seuraa ihmisen kirjoittamaa ehtoa: kun uusi lasku ylittää rajan, se menee tarkistukseen. Oikealla koneoppimismalli opetetaan esimerkeillä, ja se antaa uudelle tapaukselle opitun arvion. Sääntöpohjainen järjestelmä ei välttämättä ole tekoälyä.">
    <div class="l02r-p pl"><span class="l02r-h">SÄÄNTÖPOHJAINEN — ihminen kirjoittaa ehdon</span>
      <code class="l02r-rule">jos summa &gt; 10 000 € → tarkistus</code>
      <span class="l02r-case">uusi lasku · 12 400 €</span>
      <span class="l02r-res">✓ ehto täyttyi → tarkistukseen</span></div>
    <div class="l02r-p pr"><span class="l02r-h hr">KONEOPPIMISMALLI — opetetaan esimerkeillä</span>
      <div class="l02r-flow"><span class="l02r-d d1"></span><span class="l02r-d d2"></span><span class="l02r-d d3"></span><span class="l02r-mdl">malli</span><span class="l02r-arr">→</span><span class="l02r-out">arvio uudelle: 0,91</span></div>
      <span class="l02r-sub">malli soveltaa datasta oppimaansa uuteen tapaukseen</span></div>
    <span class="l02r-ft">sääntöpohjainen järjestelmä ei välttämättä ole tekoälyä — sama palvelu voi yhdistää molempia</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Sääntö seuraa ihmisen kirjoittamaa ehtoa. Koneoppimismalli muodostaa datasta opitun arvion uudesta tapauksesta.</figcaption></figure>
<style>
.l02r-wrap{position:relative;width:560px;height:198px;font-family:var(--font-mono);animation:l02rw 7s infinite}
.l02r-wrap:hover,.l02r-wrap:hover *{animation-play-state:paused}
.l02r-p{position:absolute;top:4px;width:272px;height:148px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:10px 12px}
.l02r-p.pl{left:2px}.l02r-p.pr{left:286px}
.l02r-h{display:block;font-size:10.5px;font-weight:700;letter-spacing:.08em;color:#7FD0A8}
.l02r-h.hr{color:#C9B7F1}
.l02r-wrap code.l02r-rule{display:inline-block;margin-top:6px;font-size:11px;white-space:nowrap;color:#EAEEF8;background:#0B0F1A;border:1px solid #2B3552;border-radius:7px;padding:4px 8px}
.l02r-case{display:block;margin-top:7px;font-size:11px;color:#0B0F1A;background:#46C7CF;border-radius:999px;padding:3px 10px;width:fit-content;opacity:0;animation:l02rcase 7s infinite}
.l02r-res{display:block;margin-top:6px;font-size:11.5px;font-weight:700;color:#7FD0A8;opacity:0;animation:l02rres 7s infinite}
.l02r-flow{position:relative;display:flex;align-items:center;gap:4px;margin-top:12px;height:30px}
.l02r-d{width:8px;height:8px;border-radius:50%;background:#46C7CF;flex:none}
.l02r-d.d1{animation:l02rd1 7s infinite}.l02r-d.d2{animation:l02rd2 7s infinite}.l02r-d.d3{animation:l02rd3 7s infinite}
.l02r-mdl{margin-left:6px;font-size:11px;color:#EAEEF8;border:1.5px solid #C9B7F1;border-radius:8px;padding:4px 9px;animation:l02rmdl 7s infinite}
.l02r-arr{color:#7E88A8;font-size:12px}
.l02r-out{font-size:10.5px;font-weight:700;color:#FFD79A;white-space:nowrap;opacity:0;animation:l02rout 7s infinite}
.l02r-sub{display:block;margin-top:10px;font-size:10.5px;color:#8B94B3}
.l02r-ft{position:absolute;left:0;top:166px;width:560px;text-align:center;font-size:10.5px;color:#8B94B3}
@keyframes l02rw{0%{opacity:0}4%{opacity:1}96%{opacity:1}100%{opacity:0}}
@keyframes l02rcase{0%,11.4%{opacity:0;transform:translateY(-4px)}22.9%,100%{opacity:1;transform:none}}
@keyframes l02rres{0%,31.4%{opacity:0}42.9%,100%{opacity:1}}
@keyframes l02rd1{0%,11.4%{transform:none;opacity:1}22.9%,100%{transform:translateX(46px);opacity:0}}
@keyframes l02rd2{0%,14.3%{transform:none;opacity:1}25.7%,100%{transform:translateX(30px);opacity:0}}
@keyframes l02rd3{0%,17.1%{transform:none;opacity:1}28.6%,100%{transform:translateX(14px);opacity:0}}
@keyframes l02rmdl{0%,25.7%{box-shadow:0 0 0 rgba(201,183,241,0)}31.4%{box-shadow:0 0 12px rgba(201,183,241,.8)}40%,100%{box-shadow:0 0 0 rgba(201,183,241,0)}}
@keyframes l02rout{0%,48.6%{opacity:0}60%,100%{opacity:1}}
@media (prefers-reduced-motion:reduce){
  .l02r-wrap,.l02r-wrap *{animation:none!important}
  .l02r-case,.l02r-res,.l02r-out{opacity:1;transform:none}
  .l02r-d{opacity:.25}
}
</style>

## 2. Kapea tekoäly — rajattu tehtävä

Monet käytössä olevat tekoälyjärjestelmät ovat kapeita: ne on rakennettu tiettyä tehtävää tai rajattua tehtäväjoukkoa varten. Järjestelmä voi esimerkiksi tunnistaa kuvasta tuotteen, arvioida maksutapahtuman poikkeavuutta tai suositella seuraavaa kappaletta.

Kapea ei tarkoita vaatimatonta. Rajattu järjestelmä voi olla omassa tehtävässään erittäin tarkka ja ylittää ihmisen suorituksen. Se ei kuitenkaan siirrä osaamistaan vapaasti täysin uudenlaiseen tehtävään. Shakkiohjelma ei ala kirjoittaa työhakemuksia, vaikka se pelaisi paremmin kuin kukaan ihminen.

> **Pysähdy hetkeksi:** Mitä käyttämäsi järjestelmä osaa tehdä hyvin? Mitä täysin erilaista tehtävää se ei osaisi tehdä?

## 3. Generatiivinen tekoäly — tuottaa uutta sisältöä

Generatiivinen tekoäly tuottaa tekstiä, kuvaa, ääntä, videota tai koodia. Se muodostaa tuotoksen koulutusdatasta oppimiensa rakenteiden ja todennäköisyyksien perusteella. Siksi tulos voi olla hyödyllinen ja vakuuttava, mutta myös virheellinen.

Generatiivisuus kertoo tuotoksen lajista: järjestelmä tuottaa sisältöä. Kapeus puolestaan kertoo kykyjen rajauksesta. Monet generatiiviset järjestelmät ovat tehtävältään rajattuja. Osa nykyisistä yleiskäyttöisistä malleista pystyy kuitenkin hoitamaan laajaa tehtäväjoukkoa. Tehtäväkirjon laajuus tai generatiivisuus ei vielä tarkoita, että järjestelmä olisi AGI.

> **Tunnin tärkein yhteys:** sama järjestelmä voi olla sekä generatiivinen että kyvyiltään rajattu. Generatiivisuus tai sujuva teksti ei yksin ole osoitus yleisestä älykkyydestä.

Nykyisistä laajaa tehtäväjoukkoa hoitavista malleista käytetään myös nimitystä **yleiskäyttöinen tekoäly** (*general-purpose AI*). Se ei ole sama asia kuin AGI. Tällä tunnilla nimitys toimii täsmennyksenä, ei kuudentena opeteltavana pääkäsitteenä.

## Tässä kulkee nykyisyyden raja

Sääntöpohjaisia järjestelmiä, kapeaa tekoälyä ja generatiivista tekoälyä käytetään jo nyt. AGI:sta ja ASI:sta puhutaan sen sijaan tutkimuksen, tulevaisuuden ja spekulaation yhteydessä. Niitä ei pidä esitellä nykyisten tuotteiden tavallisina ominaisuuksina eikä kehityksen varmoina seuraavina vaiheina.

## 4. AGI — yleisen tekoälyn ajatus

**AGI** on lyhenne sanoista *artificial general intelligence*. Sillä tarkoitetaan yleensä tekoälyä, joka pystyisi oppimaan, soveltamaan osaamistaan ja toimimaan joustavasti hyvin erilaisissa tehtävissä ihmisen tavoin.

AGI:lle ei ole yhtä yleisesti hyväksyttyä määritelmää tai testiä. Eri tutkijat ja organisaatiot painottavat esimerkiksi oppimiskykyä, tehtävien laajuutta, itsenäistä toimintaa tai kykyä soveltaa opittua uusiin tilanteisiin. Siksi yksittäistä onnistumista, sujuvaa keskustelua tai yhden testin läpäisemistä ei pidä tulkita varmaksi osoitukseksi AGI:sta.

Yleisesti hyväksyttyä nykyistä AGI-esimerkkiä ei ole. Kyse on tutkimus- ja tulevaisuuskäsitteestä, jonka toteutumisesta tai aikataulusta ei ole varmuutta.

## 5. ASI — ihmisen laajasti ylittävä tekoäly

**ASI** on lyhenne sanoista *artificial superintelligence*. Sillä tarkoitetaan hypoteettista tekoälyä, joka ylittäisi ihmisen kyvyt laajasti esimerkiksi tieteellisessä päättelyssä, suunnittelussa ja ongelmanratkaisussa.

ASI on AGI:a spekulatiivisempi käsite. Tällaista järjestelmää ei ole, eikä tiedetä, voitaisiinko sellainen rakentaa tai millainen se olisi. ASI:sta voidaan keskustella mahdollisuutena tai riskinä, mutta siitä ei pidä puhua nykyteknologiana tai varmana tulevaisuutena.

## Käsitteet rinnakkain

| Käsite | Mitä se tarkoittaa? | Onko sitä käytössä nyt? | Keskeinen rajaus |
|---|---|---|---|
| Sääntöpohjainen järjestelmä | Noudattaa ihmisen kirjoittamia ehtoja | Kyllä | Ei välttämättä ole tekoälyä eikä opi sääntöjä itse |
| Kapea tekoäly | Tekee rajattua tehtävää tai tehtäväjoukkoa | Kyllä | Ei siirrä osaamistaan vapaasti mihin tahansa tehtävään |
| Generatiivinen tekoäly | Tuottaa uutta sisältöä | Kyllä | Ei yksin kerro kykyjen laajuutta tai osoita AGI:a |
| AGI | Toimisi joustavasti hyvin erilaisissa tehtävissä | Ei yleisesti hyväksyttyä esimerkkiä | Määritelmästä ja toteutumisesta ei ole yksimielisyyttä |
| ASI | Ylittäisi ihmisen kyvyt laajasti | Ei | Hypoteettinen ja spekulatiivinen käsite |

<figure class="ai-demo"><span class="ai-demo__tag">// viisi käsitettä tekoälyn kartalla — kolme käytössä nyt, kaksi tulevaisuuspuhetta</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:312px">
  <div class="l02m-wrap" role="img" aria-label="Viisi käsitettä lajittuu kahteen ryhmään ilman kehitysportaita. Käytössä nyt: sääntöpohjainen järjestelmä, kapea tekoäly ja generatiivinen tekoäly — kapea ja generatiivinen limittyvät, koska sama järjestelmä voi olla molempia. Tulevaisuuspuhetta: AGI ilman hyväksyttyä nykyesimerkkiä ja hypoteettinen ASI. Väite ”sujuva teksti = AGI?” kimpoaa nykyisyyden rajasta takaisin: näyttö ei riitä.">
    <span class="l02m-gh g1">KÄYTÖSSÄ NYT</span><span class="l02m-gh g2">TULEVAISUUSPUHE</span>
    <i class="l02m-pan p1"></i><i class="l02m-pan p2"></i>
    <i class="l02m-bnd"></i><i class="l02m-bfl"></i>
    <span class="l02m-bl">tässä kulkee nykyisyyden raja</span>
    <div class="l02m-card c1"><b>Sääntöpohjainen</b><span>ihminen kirjoittaa säännöt</span></div>
    <div class="l02m-card c2"><div class="l02m-in ika"><b>Kapea tekoäly</b><span>rajattu tehtävä</span></div></div>
    <div class="l02m-card c3"><div class="l02m-in ige"><b>Generatiivinen</b><span>tuottaa sisältöä</span></div></div>
    <div class="l02m-card c4"><b>AGI</b><span>toimisi joustavasti eri tehtävissä</span><em>ei nykyesimerkkiä</em></div>
    <div class="l02m-card c5"><b>ASI</b><span>ylittäisi ihmisen kyvyt laajasti</span><em>hypoteettinen käsite</em></div>
    <span class="l02m-ov">sama järjestelmä voi olla molempia</span>
    <span class="l02m-bub">sujuva teksti = AGI?</span>
    <span class="l02m-st"><i>näyttö ei riitä</i></span>
    <span class="l02m-syn">Ei kehitysaskelmia: kolme on käytössä nyt — AGI ja ASI ovat tulevaisuuspuhetta.</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Viisi käsitettä samalla kartalla: sääntöpohjainen, kapea ja generatiivinen kuvaavat nykyisiä järjestelmiä, AGI ja ASI ovat tulevaisuuskäsitteitä. Kapea ja generatiivinen limittyvät, koska sama järjestelmä voi olla molempia — mutta sujuva tuotos ei ylitä nykyisyyden rajaa. Vie hiiri kuvan päälle pysäyttääksesi.</figcaption></figure>
<style>
.l02m-wrap{position:relative;width:560px;height:300px;font-family:var(--font-mono);animation:l02mw 21s infinite}
.l02m-wrap:hover,.l02m-wrap:hover *{animation-play-state:paused}
.l02m-gh{position:absolute;top:0;font-size:11px;font-weight:700;letter-spacing:.14em;opacity:0;animation:l02mp 21s infinite}
.l02m-gh.g1{left:14px;color:#7FD0A8}.l02m-gh.g2{left:374px;color:#C9B7F1}
.l02m-pan{position:absolute;top:22px;height:218px;border-radius:12px;opacity:0;animation:l02mp 21s infinite}
.l02m-pan.p1{left:2px;width:334px;background:#11182A;border:1px solid #2B3552}
.l02m-pan.p2{left:360px;width:198px;background:rgba(126,136,168,.06);border:1.5px dashed #7E88A8}
.l02m-bnd{position:absolute;left:347px;top:22px;height:218px;width:0;border-left:2px dashed #7E88A8;transform:scaleY(0);transform-origin:top;animation:l02mb 21s infinite}
.l02m-bfl{position:absolute;left:342px;top:22px;height:218px;width:12px;background:radial-gradient(50% 50% at 50% 50%,rgba(255,215,154,.55),transparent);opacity:0;animation:l02mfl 21s infinite}
.l02m-bl{position:absolute;left:198px;top:244px;width:300px;text-align:center;font-size:10.5px;color:#7E88A8;opacity:0;animation:l02mbl 21s infinite}
.l02m-card{position:absolute;box-sizing:border-box;background:#171F33;border:1px solid #2B3552;border-radius:10px;padding:8px 10px;opacity:0}
.l02m-card b{display:block;font-size:12.5px;line-height:1.25;color:#EAEEF8}
.l02m-card span{display:block;font-size:10.5px;line-height:1.3;color:#B9C2DA;margin-top:2px}
.l02m-card em{display:block;font-style:normal;font-size:10px;line-height:1.25;color:#C9B7F1;margin-top:4px;opacity:0;animation:l02mtag 21s infinite}
.l02m-card.c1{left:14px;top:44px;width:150px;height:62px;animation:l02mc1 21s infinite}
.l02m-card.c2{left:14px;top:120px;width:150px;height:62px;animation:l02mc2 21s infinite}
.l02m-card.c3{left:172px;top:120px;width:150px;height:62px;animation:l02mc3 21s infinite}
.l02m-card.c4{left:374px;top:44px;width:172px;height:84px;border-style:dashed;border-color:#7E88A8;animation:l02mc4 21s infinite}
.l02m-card.c5{left:374px;top:142px;width:172px;height:84px;border-style:dashed;border-color:#7E88A8;animation:l02mc5 21s infinite}
.l02m-in{animation:none}
.l02m-in.ika{animation:l02mika 21s infinite}
.l02m-in.ige{animation:l02mige 21s infinite}
.l02m-ov{position:absolute;left:14px;top:188px;width:308px;text-align:center;font-size:10.5px;color:#7FD0A8;opacity:0;animation:l02mov 21s infinite}
.l02m-bub{position:absolute;left:168px;top:82px;padding:4px 10px;border-radius:999px;background:#0E2A31;border:1px solid #46C7CF;color:#46C7CF;font-size:11px;white-space:nowrap;opacity:0;animation:l02mbub 21s infinite}
.l02m-st{position:absolute;left:238px;top:28px;opacity:0;animation:l02mst 21s infinite}
.l02m-st i{display:inline-block;font-style:normal;font-size:11px;font-weight:700;color:#FFD79A;border:1.5px solid #FFD79A;border-radius:6px;padding:3px 8px;background:rgba(255,215,154,.08);transform:rotate(-6deg);animation:l02mps 21s infinite}
.l02m-syn{position:absolute;left:0;top:268px;width:560px;text-align:center;font-size:12px;font-weight:600;color:#FFD79A;opacity:0;animation:l02msyn 21s infinite}
@keyframes l02mw{0%{opacity:0}3.3%{opacity:1}96.7%{opacity:1}100%{opacity:0}}
@keyframes l02mc1{0%,3.33%{opacity:0;transform:translate(206px,20px)}5.24%{opacity:1;transform:translate(206px,20px)}5.71%{transform:translate(206px,20px)}11.43%,100%{opacity:1;transform:none}}
@keyframes l02mc2{0%,3.33%{opacity:0;transform:translate(376px,-70px)}5.24%{opacity:1;transform:translate(376px,-70px)}6.67%{transform:translate(376px,-70px)}12.38%,100%{opacity:1;transform:none}}
@keyframes l02mc3{0%,3.33%{opacity:0;transform:translate(-112px,-80px)}5.24%{opacity:1;transform:translate(-112px,-80px)}7.62%{transform:translate(-112px,-80px)}13.33%,100%{opacity:1;transform:none}}
@keyframes l02mc4{0%,3.33%{opacity:0;transform:translate(-134px,102px)}5.24%{opacity:1;transform:translate(-134px,102px)}8.57%{transform:translate(-134px,102px)}14.29%,100%{opacity:1;transform:none}}
@keyframes l02mc5{0%,3.33%{opacity:0;transform:translate(-334px,20px)}5.24%{opacity:1;transform:translate(-334px,20px)}9.52%{transform:translate(-334px,20px)}15.24%,100%{opacity:1;transform:none}}
@keyframes l02mp{0%,17.14%{opacity:0}20.95%,100%{opacity:1}}
@keyframes l02mb{0%,20.95%{transform:scaleY(0)}24.76%,100%{transform:scaleY(1)}}
@keyframes l02mbl{0%,24.76%{opacity:0}27.6%,100%{opacity:1}}
@keyframes l02mika{0%,28.57%{transform:none}33.33%,100%{transform:translateX(14px)}}
@keyframes l02mige{0%,28.57%{transform:none}33.33%,100%{transform:translateX(-14px)}}
@keyframes l02mov{0%,33.33%{opacity:0}38.1%,100%{opacity:1}}
@keyframes l02mbub{0%,45.24%{opacity:0;transform:none}46.43%{opacity:1;transform:none}47.62%{transform:none}54.76%{transform:translate(30px,-24px)}55.5%{transform:translate(26px,-24px)}56.2%{transform:translate(34px,-24px)}57.14%{transform:translate(30px,-24px)}60%{transform:translate(30px,-24px)}64.76%{opacity:1;transform:none}69.05%{opacity:1}71.43%,100%{opacity:0;transform:none}}
@keyframes l02mfl{0%,54%{opacity:0}55.5%{opacity:1}58.57%,100%{opacity:0}}
@keyframes l02mst{0%,56.19%{opacity:0}59.05%,100%{opacity:1}}
@keyframes l02mps{0%,78.57%{transform:rotate(-6deg) scale(1)}79.8%{transform:rotate(-6deg) scale(1.16)}81%,100%{transform:rotate(-6deg) scale(1)}}
@keyframes l02mtag{0%,64.76%{opacity:0}69.05%,100%{opacity:1}}
@keyframes l02msyn{0%,73.81%{opacity:0}77.14%,100%{opacity:1}}
@media (prefers-reduced-motion:reduce){
  .l02m-wrap,.l02m-wrap *{animation:none!important}
  .l02m-wrap,.l02m-gh,.l02m-pan,.l02m-bl,.l02m-card,.l02m-card em,.l02m-ov,.l02m-st,.l02m-syn{opacity:1}
  .l02m-bnd{transform:scaleY(1)}
  .l02m-in.ika{transform:translateX(14px)}
  .l02m-in.ige{transform:translateX(-14px)}
  .l02m-card{transform:none}
  .l02m-bub,.l02m-bfl{opacity:0}
}
</style>

<!--
INFOGRAFIIKAN SISÄLTÖBRIEFI
Otsikko: Viisi käsitettä tekoälyn kartalla
Rakenne: vasemmalla NYKYISET JÄRJESTELMÄT, oikealla TULEVAISUUSKÄSITTEET. Ryhmien välissä selvä raja.
Nykyiset järjestelmät: 1) sääntöpohjainen järjestelmä — ihminen kirjoittaa säännöt; 2) kapea tekoäly — rajattu tehtävä; 3) generatiivinen tekoäly — tuottaa sisältöä. Yhdistä kapea ja generatiivinen merkinnällä ”sama järjestelmä voi olla molempia”, mutta älä sijoita kaikkia generatiivisia järjestelmiä kokonaan kapean sisään.
Tulevaisuuskäsitteet: 4) AGI — joustava ja laaja-alainen; 5) ASI — ihmisen kyvyt laajasti ylittävä.
Pääviesti kuvan yhteyteen: Käsitteet eivät ole kehitysaskelmia. Generatiivisuus ei yksin kerro kykyjen laajuutta tai osoita AGI:a. AGI ja ASI eivät ole nykyisiä järjestelmiä.
Vältä portaikkoa, nousevaa nuolta ja muuta väistämätöntä kehitystä ilmaisevaa muotoa.

Alt-teksti: Infografiikka jakaa viisi käsitettä nykyisiin järjestelmiin ja tulevaisuuskäsitteisiin. Sääntöpohjainen järjestelmä, kapea tekoäly ja generatiivinen tekoäly ovat käytössä nyt. Kapea ja generatiivinen on yhdistetty merkinnällä, jonka mukaan sama järjestelmä voi olla molempia. AGI ja ASI on erotettu tulevaisuuskäsitteiksi ilman niitä yhdistävää kehitysnuolta.

PIENEN KERTAUSINFOGRAFIIKAN SISÄLTÖBRIEFI
Otsikko: Sääntö vai opittu arvio?
Vasen puoli: Sääntöpohjainen järjestelmä — ihminen kirjoittaa ehdon — JOS summa ylittää rajan, pyydä tarkistus.
Oikea puoli: Koneoppimismalli — malli opetetaan esimerkeillä — esimerkkidata, malli, arvio uudesta tapauksesta.
Alateksti: Kertaus tunnilta 1. Sääntöpohjainen järjestelmä ei välttämättä ole tekoälyä.
Alt-teksti: Vertailu näyttää, että sääntöpohjainen järjestelmä seuraa ihmisen kirjoittamaa ehtoa, kun taas koneoppimismalli muodostaa datasta opitun arvion uudesta tapauksesta.
-->

## Kun kohtaat tekoälyväitteen

Tekoälyä koskeva otsikko voi sanoa järjestelmän ”ymmärtävän”, ”ajattelevan” tai ”toimivan kuin ihminen”. Ennen johtopäätöstä pysähdy kolmen kysymyksen äärelle:

1. Mitä järjestelmä osoitetusti teki?
2. Oliko tehtävä rajattu vai väitetäänkö järjestelmän osaavan yleisesti?
3. Perustuuko väite havaittuun tulokseen, valmistajan lupaukseen vai tulevaisuuden oletukseen?

Jos järjestelmä tuottaa hyvän tekstin, havainto koskee tekstin tuottamista. Se ei vielä osoita, että järjestelmä osaisi itsenäisesti minkä tahansa ammatin, ymmärtäisi seuraukset ihmisen tavoin tai olisi AGI.

> **Pysähdy hetkeksi:** Miten selittäisit tutullesi yhdellä lauseella, miksi sujuvasti keskusteleva tekoäly ei ole automaattisesti yleinen tekoäly?

## Yhteenveto

Sääntöpohjainen järjestelmä seuraa ihmisen kirjoittamia ehtoja. Kapea tekoäly tekee rajattua tehtävää. Generatiivinen tekoäly tuottaa sisältöä, mutta generatiivisuus ei yksin kerro järjestelmän kykyjen laajuutta. Nämä ovat nykyisiä järjestelmiä.

AGI ja ASI ovat tulevaisuutta koskevia käsitteitä, eivät käytössä olevan tekoälyn varmoja seuraavia vaiheita. Kun luet tekoälyväitteen, tarkista ensin, mitä järjestelmä todella teki ja kuinka pitkälle näyttö kantaa.

## Lähteet ja tarkistuspäivä

- [OECD: Explanatory memorandum on the updated definition of an AI system](https://oecd.ai/en/ai-publications/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system)
- [OECD: Framework for the Classification of AI Systems](https://oecd.ai/en/ai-publications/framework-classification)
- [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)

Tarkistettu 20.7.2026.
