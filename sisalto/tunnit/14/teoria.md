# Oma botti I — käyttäjä, tehtävä ja rajat

## Johdanto: bottia ei aloiteta ohjetekstistä

Oman botin rakentaminen houkuttelee aloittamaan järjestelmäpromptista: kirjoitetaan botille rooli, muutama sääntö ja kokeillaan, mitä tapahtuu. Silloin tärkeimmät päätökset jäävät helposti tekemättä. Kenelle botti on tarkoitettu? Mitä käyttäjä yrittää saada aikaan? Missä tilanteessa botti auttaa — ja missä sen pitää lopettaa?

Tällä tunnilla et rakenna bottia etkä kirjoita valmista järjestelmäpromptia. Laadit **määrittelydokumentin**, jonka perusteella botin voisi myöhemmin rakentaa myös joku toinen. Suunnittelu erotetaan toteutuksesta tarkoituksella: ensin päätetään, millainen työkalu tarvitaan, vasta sitten kirjoitetaan ohjeet ja valitaan alusta.

Määrittely on lupaus tulevasta toiminnasta. Se kertoo, ketä autetaan, missä tehtävässä ja millä rajoilla. Kun nämä päätökset ovat näkyvissä, myöhempää bottia voidaan arvioida muullakin kuin kysymyksellä ”vaikuttaako tämä hyvältä?”. Ilman määrittelyä jokainen sujuva vastaus voi näyttää onnistumiselta, vaikka botti ratkaisisi väärää ongelmaa.

> **Tunnin ydinkysymys:** Mitä botin pitää auttaa tiettyä käyttäjää tekemään — ja mistä huomaat, että tehtävä onnistui?

<figure class="ai-demo"><span class="ai-demo__tag" id="l14-t"><i aria-hidden="true">// </i>sumeasta ideasta arvioitavaksi määrittelyksi — prompti on viimeinen askel</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:368px">
  <div class="l14-wrap" data-once role="img" aria-labelledby="l14-t" aria-describedby="l14-d">
    <span class="sr-only" id="l14-d">Botti-idea tarkentuu kuusikohtaiseksi määrittelyksi: käyttäjä, tehtävä, havaittava onnistuminen, keskustelun eteneminen, rooli ja äänensävy sekä rajat, joilla on ovi. Tietotarpeet kirjataan erilliseen korttiin. Prompti kirjoitetaan vasta, kun kaikki kohdat ovat valmiit.</span>
    <span class="l14-mt"><b class="l14-slot s1"><i class="e">KÄYTTÄJÄ</i><i class="f f1">kerhon uusi jäsen</i></b><span class="l14-mw">tarvitsee apua:</span><b class="l14-slot s2"><i class="e">TEHTÄVÄ</i><i class="f f2">löytää säännöt ja ajat</i></b></span>
    <span class="l14-mt m2"><span class="l14-mw">jotta</span><b class="l14-slot s3"><i class="e">LOPPUTULOS</i><i class="f f3">valmiina harjoituksiin</i></b></span>
    <div class="l14-ws"><i class="l14-ph">TYÖTILA</i>
      <span class="l14-blob">Opiskelubotti?</span>
      <em class="l14-tag t1">liian laaja</em>
      <span class="l14-fz"><b class="l14-fzc">auttaa hyvin?<i class="l14-fzs"></i></b><em class="l14-tag t2">ei havaittava</em></span>
      <span class="l14-ok">✓ löytää hyväksytystä lähteestä ajan, varusteet ja seuraavan askeleen</span>
      <span class="l14-mini mA">eteneminen: kysy tarkennus, jos pyyntö on epäselvä</span>
      <span class="l14-mini mB">rooli ja sävy: asiallinen ohjaaja</span>
      <i class="l14-line la"></i><i class="l14-line lb"></i>
      <span class="l14-test">kysymys ohi aiheen</span>
      <span class="l14-step p1">rajaus yhdellä lauseella</span>
      <span class="l14-step p2">→ ohjaa yhteyshenkilölle</span></div>
    <div class="l14-def"><i class="l14-ph">MÄÄRITTELY</i>
      <span class="l14-dr d1"><b class="bx x1"></b>Käyttäjä</span>
      <span class="l14-dr d2"><b class="bx x2"></b>Tehtävä</span>
      <span class="l14-dr d3"><b class="bx x3"></b>Havaittava onnistuminen</span>
      <span class="l14-dr d4"><b class="bx x4"></b>Keskustelun eteneminen</span>
      <span class="l14-dr d5"><b class="bx x5"></b>Rooli ja äänensävy</span>
      <span class="l14-dr d6"><b class="bx x6"></b>Rajat ja seuraava askel</span>
      <span class="l14-fin"><i>VALMIS — EI VIELÄ PROMPTI</i></span></div>
    <span class="l14-info"><b>TIETOTARPEET · erillinen kortti:</b> säännöt ja varusteet · aikataulut · yhteyshenkilö — vain hyväksytyt lähteet</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Määrittely on tarkentumista: käyttäjä, tehtävä, havaittava onnistuminen, keskustelun eteneminen, rooli ja äänensävy sekä rajat, joilla on ovi — ei seinää. Tietotarpeet kirjataan erilliseen korttiin. Prompti kirjoitetaan vasta, kun määrittelyn kaikki kohdat ovat valmiit.</figcaption></figure>
<style>
.l14-wrap{position:relative;width:560px;height:352px;font-family:var(--font-mono);animation:l14w 21s 1 forwards}
.l14-ph{display:block;font-style:normal;font-size:12px;font-weight:700;letter-spacing:.06em;color:#EAEEF8}
.l14-mt{position:absolute;left:0;top:0;width:560px;display:flex;align-items:center;justify-content:center;gap:8px}
.l14-mt.m2{top:32px}
.l14-mw{font-size:12px;color:#B9C2DA}
.l14-slot{position:relative;width:188px;height:26px}
.l14-slot i{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:12px;border-radius:8px;box-sizing:border-box}
.l14-slot .e{color:#7E88A8;border:1.5px dashed #4A5677;letter-spacing:.06em}
.l14-slot .f{color:#0B0F1A;font-weight:700;opacity:0}
.l14-slot .f1{background:#C9B7F1;animation:l14f1 21s 1 forwards}
.l14-slot .f2{background:#46C7CF;animation:l14f2 21s 1 forwards}
.l14-slot .f3{background:#7FD0A8;animation:l14f3 21s 1 forwards}
.l14-slot.s1 .e{animation:l14e1 21s 1 forwards}
.l14-slot.s2 .e{animation:l14e2 21s 1 forwards}
.l14-slot.s3 .e{animation:l14e3 21s 1 forwards}
.l14-ws{position:absolute;left:2px;top:72px;width:320px;height:240px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:9px 12px}
.l14-blob{position:absolute;left:26px;top:52px;width:250px;height:44px;display:flex;align-items:center;justify-content:center;font-size:13px;color:#B9C2DA;border:2px dashed #4A5677;border-radius:22px;opacity:0;animation:l14blob 21s 1 forwards}
.l14-tag{position:absolute;font-style:normal;font-size:12px;color:#FFD79A;border:1px solid #FFD79A;border-radius:6px;padding:2px 6px;opacity:0;background:rgba(255,215,154,.07)}
.l14-tag.t1{left:206px;top:32px;animation:l14t1 21s 1 forwards}
.l14-fz{position:absolute;left:16px;top:34px;opacity:0;animation:l14fz 21s 1 forwards}
.l14-fzc{position:relative;display:inline-block;font-size:12px;font-weight:400;color:#EAEEF8;border:1px solid #2B3552;border-radius:8px;padding:5px 10px;background:#0E1524}
.l14-fzs{position:absolute;left:6px;top:50%;width:86%;height:2px;background:#FFD79A;transform:scaleX(0);transform-origin:left;animation:l14fzs 21s 1 forwards}
.l14-fz .l14-tag{position:static;margin-left:8px;opacity:0;animation:l14t2 21s 1 forwards}
.l14-ok{position:absolute;left:16px;top:72px;width:280px;box-sizing:border-box;font-size:12px;line-height:1.3;font-weight:700;color:#7FD0A8;border:1.5px solid #7FD0A8;border-radius:8px;padding:5px 9px;opacity:0;animation:l14ok 21s 1 forwards}
.l14-mini{position:absolute;left:16px;width:280px;box-sizing:border-box;font-size:12px;line-height:1.25;color:#B9C2DA;border:1px solid #2B3552;border-left:3px solid #7FD0A8;border-radius:7px;padding:4px 8px;opacity:0}
.l14-mini.mA{top:126px;animation:l14mA 21s 1 forwards}
.l14-mini.mB{top:162px;animation:l14mB 21s 1 forwards}
.l14-line{position:absolute;left:216px;width:0;border-left:2px dashed #7E88A8;transform:scaleY(0)}
.l14-line.la{top:70px;height:50px;transform-origin:top;animation:l14la 21s 1 forwards}
.l14-line.lb{top:170px;height:58px;transform-origin:bottom;animation:l14lb 21s 1 forwards}
.l14-test{position:absolute;left:14px;top:126px;font-size:12px;color:#EAEEF8;border:1px solid #4A5677;border-radius:8px;padding:4px 8px;opacity:0;animation:l14test 21s 1 forwards}
.l14-step{position:absolute;font-size:12px;line-height:1.25;color:#7FD0A8;border:1.5px solid #7FD0A8;border-radius:7px;padding:3px 7px;opacity:0;background:rgba(127,208,168,.07)}
.l14-step.p1{left:14px;top:196px;animation:l14p1 21s 1 forwards;opacity:0}
.l14-step.p2{left:222px;top:132px;width:96px;box-sizing:border-box;animation:l14p2 21s 1 forwards}
.l14-def{position:absolute;left:334px;top:72px;width:224px;height:240px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:9px 12px}
.l14-dr{position:relative;display:block;margin-top:9px;padding-left:22px;font-size:12px;line-height:1.25;color:#EAEEF8}
.l14-dr .bx{position:absolute;left:0;top:1px;width:12px;height:12px;border:1.5px solid #4A5677;border-radius:3px}
.l14-dr .bx::after{content:'✓';position:absolute;left:1px;top:-3px;font-size:11px;font-weight:700;color:#7FD0A8;opacity:0}
.l14-dr .bx.x1::after{animation:l14x1 21s 1 forwards}
.l14-dr .bx.x2::after{animation:l14x2 21s 1 forwards}
.l14-dr .bx.x3::after{animation:l14x3 21s 1 forwards}
.l14-dr .bx.x4::after{animation:l14x4 21s 1 forwards}
.l14-dr .bx.x5::after{animation:l14x5 21s 1 forwards}
.l14-dr .bx.x6::after{animation:l14x6 21s 1 forwards}
.l14-fin{position:absolute;left:0;bottom:12px;width:100%;text-align:center;opacity:0;animation:l14fin 21s 1 forwards}
.l14-fin i{display:inline-block;font-style:normal;font-size:12px;font-weight:700;color:#FFD79A;border:1.5px solid #FFD79A;border-radius:7px;padding:4px 8px;transform:rotate(-4deg);background:rgba(255,215,154,.07)}
.l14-info{position:absolute;left:0;top:322px;width:560px;box-sizing:border-box;font-size:12px;line-height:1.3;color:#B9C2DA;border:1px dashed #4A5677;border-radius:9px;padding:6px 10px;opacity:0;animation:l14info 21s 1 forwards}
.l14-info b{color:#46C7CF;font-weight:700}
@keyframes l14w{0%{opacity:0}3%{opacity:1}100%{opacity:1}}
@keyframes l14blob{0%,4%{opacity:0;transform:scale(1)}8%{opacity:1}17%{opacity:1;transform:scale(1)}24%{opacity:0;transform:scale(.42) translateY(-60px)}100%{opacity:0}}
@keyframes l14t1{0%,10%{opacity:0}14%{opacity:1}22%{opacity:1}26%,100%{opacity:0}}
@keyframes l14e1{0%,24%{opacity:1}27%,100%{opacity:0}}
@keyframes l14f1{0%,24%{opacity:0;transform:scale(.8)}27%,100%{opacity:1;transform:scale(1)}}
@keyframes l14x1{0%,25%{opacity:0}28%,100%{opacity:1}}
@keyframes l14e2{0%,29%{opacity:1}32%,100%{opacity:0}}
@keyframes l14f2{0%,29%{opacity:0;transform:scale(.8)}32%,100%{opacity:1;transform:scale(1)}}
@keyframes l14x2{0%,30%{opacity:0}33%,100%{opacity:1}}
@keyframes l14e3{0%,35%{opacity:1}38%,100%{opacity:0}}
@keyframes l14f3{0%,35%{opacity:0;transform:scale(.8)}38%,100%{opacity:1;transform:scale(1)}}
@keyframes l14fz{0%,39%{opacity:0;transform:translateY(6px)}42%{opacity:1;transform:none}63%{opacity:1}66%,100%{opacity:0}}
@keyframes l14fzs{0%,43%{transform:scaleX(0)}46%,100%{transform:scaleX(1)}}
@keyframes l14t2{0%,44%{opacity:0}47%,100%{opacity:1}}
@keyframes l14ok{0%,47%{opacity:0;transform:translateY(6px)}51%{opacity:1;transform:none}64%{transform:none}68%,100%{opacity:1;transform:translateY(-38px)}}
@keyframes l14x3{0%,52%{opacity:0}55%,100%{opacity:1}}
@keyframes l14mA{0%,56%{opacity:0;transform:translateY(6px)}59%{opacity:1;transform:none}63%{opacity:1}66%,100%{opacity:0}}
@keyframes l14x4{0%,59%{opacity:0}62%,100%{opacity:1}}
@keyframes l14mB{0%,60%{opacity:0;transform:translateY(6px)}63%{opacity:1;transform:none}64.5%{opacity:1}67%,100%{opacity:0}}
@keyframes l14x5{0%,63%{opacity:0}66%,100%{opacity:1}}
@keyframes l14la{0%,68%{transform:scaleY(0)}70%,100%{transform:scaleY(1)}}
@keyframes l14lb{0%,68%{transform:scaleY(0)}70%,100%{transform:scaleY(1)}}
@keyframes l14test{0%,70%{opacity:0;transform:translateX(-30px)}73%{opacity:1;transform:translateX(0)}77%,100%{opacity:1;transform:translateX(116px)}}
@keyframes l14p1{0%,77%{opacity:0}80%,100%{opacity:1}}
@keyframes l14p2{0%,80%{opacity:0;transform:translateX(-8px)}83%,100%{opacity:1;transform:none}}
@keyframes l14x6{0%,84%{opacity:0}86%,100%{opacity:1}}
@keyframes l14info{0%,86%{opacity:0;transform:translateY(5px)}89%,100%{opacity:1;transform:none}}
@keyframes l14fin{0%,92%{opacity:0;transform:scale(.6)}95%,100%{opacity:1;transform:scale(1)}}
@media (prefers-reduced-motion:reduce){
  .l14-wrap,.l14-wrap *{animation:none!important}
  .l14-wrap,.l14-ok,.l14-test,.l14-step,.l14-fin,.l14-info{opacity:1}
  .l14-fz,.l14-mini{opacity:0}
  .l14-ok{transform:translateY(-38px)}
  .l14-slot .f{opacity:1}
  .l14-dr .bx::after{opacity:1}
  .l14-slot .e,.l14-blob,.l14-tag.t1{opacity:0}
  .l14-fz .l14-tag{opacity:1}
  .l14-fzs{transform:scaleX(1)}
  .l14-line{transform:scaleY(1)}
  .l14-test{transform:translateX(116px)}
}
</style>

## Aloita käyttäjän tilanteesta

Hyvä botti ratkaisee rajatun ongelman rajatussa tilanteessa. ”Opiskelubotti” on liian laaja lähtökohta. ”Kertauskaveri, joka auttaa ensimmäisen vuoden opiskelijaa tunnistamaan tietoverkkojen keskeiset käsitteet ennen koetta” kertoo jo käyttäjän, tilanteen ja tavoitteen.

Kuvaa käyttötapaus yhdellä virkkeellä:

> **[Käyttäjä]** tarvitsee apua **[tehtävässä]**, jotta hän voi **[saavutettava lopputulos]**.

Esimerkiksi:

> Kerhon uusi jäsen tarvitsee apua sääntöjen ja harjoitusaikojen löytämisessä, jotta hän osaa tulla ensimmäisiin harjoituksiinsa valmistautuneena.

Tämä virke toimii koko suunnitelman mittatikkuna. Jos myöhempi ominaisuus ei auta käyttäjää tässä tehtävässä, sitä ei ehkä tarvita.

Kerhon perehdytysbotissa tämä rajaus sulkee pois esimerkiksi yleisen harjoitusohjelman laatimisen ja henkilökohtaisen terveysneuvonnan. Ne voivat liittyä harrastukseen, mutta eivät uuden jäsenen tehtävään löytää säännöt, harjoitusaika ja ensimmäisen kerran valmistautumisohjeet. Rajaus pitää botin tietopohjan, keskustelun ja vastuun hallittavina.

## Määritä onnistuminen havaittavasti

”Botti auttaa hyvin” ei ole vielä arvioitava tavoite. Onnistuminen pitää kuvata niin, että sen voi myöhemmin testata.

Havaittava onnistuminen voi tarkoittaa esimerkiksi sitä, että:

- käyttäjä löytää vastauksen nimetystä tietopohjasta
- botti kysyy puuttuvan lähtötiedon ennen ehdotusta
- vastaus etenee ennalta sovitussa rakenteessa
- botti myöntää, ettei tietopohja kata kysymystä
- käyttäjä saa seuraavan konkreettisen askeleen

Kun onnistuminen on havaittava, Oma botti II -tunnilla voidaan kirjoittaa sitä koskevat testit ja tunneilla 17–18 voidaan tarkistaa, toteutuuko se oikeassa botissa.

Havaittava tavoite muuttaa myös keskustelun suunnittelua. Jos onnistuminen tarkoittaa, että uusi jäsen löytää oikean harjoitusajan ja seuraavan askeleen, botin pitää joko antaa nämä tiedot hyväksytystä lähteestä tai kertoa avoimesti, ettei lähde kata kysymystä. Pelkkä ystävällinen keskustelu ei silloin vielä riitä onnistumiseksi.

## Kuvaa keskustelun eteneminen

Botin **työnkulku** tarkoittaa tässä keskustelun loogista etenemistä, ei vielä teknistä automaatiota. Kirjoita 4–6 vaihetta, jotka kuvaavat käyttäjän matkan alusta hyödylliseen lopputulokseen.

Kertauskaverin eteneminen voisi olla:

1. kysy aihe ja tavoite
2. selvitä käyttäjän lähtötaso yhdellä kysymyksellä
3. selitä yksi käsite kerrallaan
4. anna lyhyt harjoituskysymys
5. anna palaute käyttäjän vastauksesta
6. ehdota seuraavaa harjoiteltavaa asiaa

Vaiheet eivät vielä ole järjestelmäprompti. Ne ovat vaatimus sille, mitä myöhemmän järjestelmäpromptin ja käyttöliittymän pitää saada aikaan.

Järjestys kertoo myös, milloin botti ei vielä voi vastata. Kertauskaveri ei esimerkiksi voi valita sopivaa harjoituskysymystä ennen kuin aihe ja lähtötaso ovat selvillä. Työnkulun tehtävä ei siis ole vain järjestää tekstiä siistiksi, vaan tehdä tarvittavat päätökset näkyviksi ennen toteutusta.

## Rooli ei ole sama asia kuin persoona

**Rooli** kertoo, mistä näkökulmasta botti auttaa. **Persoona ja äänensävy** kertovat, miltä vuorovaikutus tuntuu.

”Olet ystävällinen apuri” kuvaa lähinnä sävyä. ”Olet uusien jäsenten perehdyttäjä, joka käyttää vain kerhon hyväksyttyjä sääntöjä ja harjoitusaikoja” kertoo tehtävän, tiedollisen perustan ja vastuun.

Valitse ensin asiallinen rooli. Lisää sen jälkeen tehtävään sopiva viestintätapa:

- kannustava mutta ei ylikehuva
- selkeä mutta ei alentuva
- rauhallinen riskitilanteissa
- tiivis silloin, kun käyttäjä tarvitsee toimintaohjeen

Persoona ei korvaa asiantuntemusta, lähteitä tai rajoja. Se auttaa tekemään botin toiminnasta johdonmukaista ja käyttäjälle sopivaa.

Kerhon botin rooli voi olla ”uuden jäsenen perehdyttäjä, joka käyttää hyväksyttyjä sääntöjä ja aikatauluja”. Sen sävy voi olla rauhallinen, lämmin ja tiivis. Jos sävy poistetaan, tehtävä säilyy. Jos rooli ja lähdepohja poistetaan, jäljelle jää vain miellyttävästi kirjoittava yleisbotti.

## Rajat tekevät botista käyttökelpoisen

Rajaus ei ole luettelo kaikesta pahasta. Hyvä rajaus liittyy käyttötapaukseen ja kertoo myös, mitä botti tekee rajan tullessa vastaan.

Kirjoita rajat kolmesta suunnasta:

1. **Aiheen raja:** Mihin kysymyksiin botti ei vastaa?
2. **Toiminnan raja:** Mitä botti ei tee käyttäjän puolesta?
3. **Tiedon raja:** Mitä tietoa botti ei pyydä, tallenna tai arvaa?

Pelkkä ”älä vastaa aiheen ulkopuolelle” jättää käyttäjän tyhjän päälle. Parempi ohje on: ”Jos kysymys ei koske kerhon toimintaa, kerro rajaus yhdellä lauseella ja ohjaa käyttäjä kerhon yhteyshenkilölle.”

Käyttäjän näkökulmasta raja on osa palvelua. Jos hän kysyy vamman hoitamisesta, botti ei vain vaikene tai toista kieltoa. Se kertoo, ettei anna terveysneuvontaa, ja ohjaa käyttäjän asianmukaiseen apuun. Hyvä raja siis yhdistää kolme asiaa: ehdon, botin toiminnan ja turvallisen seuraavan askeleen.

## Tee myös tietotarpeet näkyviksi

Määrittely paljastaa, mitä botin pitää tietää. Kerhon perehdytysbotti saattaa tarvita säännöt, harjoitusajat, varusteluettelon ja yhteystiedot. Se ei tarvitse koko kerhon vuosikertomusta vain siksi, että dokumentti liittyy samaan organisaatioon.

Kirjaa määrittelyyn alustava luettelo tietotarpeista. Oma botti II -tunnilla etsit niihin sopivat lähteet ja arvioit, mitä aineisto kattaa ja mitä ei.

Tietotarpeet seuraavat suoraan käyttäjän etenemisestä. Jos botin pitää kertoa harjoitusaika, varusteet ja yhteyshenkilö, jokaiselle tiedolle tarvitaan myöhemmin nimetty ja ajantasainen lähde. Jos määrittelyssä luvataan jotakin, jolle ei löydy luotettavaa tietopohjaa, lupausta pitää rajata ennen rakentamista.

## Määrittelydokumentti on päätösten ketju

Hyvä määrittely vastaa kuuteen kysymykseen:

| Päätös | Kysymys |
| --- | --- |
| Käyttäjä | Kuka tarvitsee apua ja missä tilanteessa? |
| Tehtävä | Mitä käyttäjä yrittää saada aikaan? |
| Onnistuminen | Mitä havaittavaa tapahtuu, kun botti auttaa oikein? |
| Eteneminen | Missä järjestyksessä botti ohjaa käyttäjää? |
| Rooli ja sävy | Millaisena asiantuntijana ja millä tavalla botti viestii? |
| Rajat | Mitä botti ei tee, ja miten se toimii rajan tullessa vastaan? |

Näiden päätösten jälkeen järjestelmäpromptin kirjoittaminen on myöhemmin muuntamista, ei arvailua. Apuri-botin rakennustunnilla kokoat määrittelyn, promptikortin toimivan rakenteen ja tietopohjan yhdeksi toteutukseksi.

Lue taulukkoa päätösketjuna, ei kuutena irrallisena kenttänä. Käyttäjän tilanne määrittää tehtävän, tehtävä määrittää onnistumisen, onnistuminen ohjaa keskustelun etenemistä ja rajat kertovat, milloin vastuu siirtyy botilta ihmiselle. Rooli ja sävy tukevat tätä kokonaisuutta, mutta eivät muuta sen tarkoitusta.

## Yhteenveto

Tällä tunnilla suunnittelet ennen rakentamista. Rajaat käyttäjän, tehtävän, havaittavan onnistumisen, keskustelun etenemisen, roolin, äänensävyn ja toiminnan rajat. Et vielä kirjoita valmista järjestelmäpromptia tai testaa omaa bottia.

Tunnin tuotoksena syntyy **rakennuspalikka 2: botin määrittelydokumentti**. Se kertoo, mitä Apuri-botin rakennustunnilla rakennetaan ja millä perusteella toteutusta myöhemmin arvioidaan.

> **Lopuksi pohdittavaksi:** Voisiko toinen ihminen rakentaa määrittelysi perusteella saman botin kuin sinä? Jos ei, mikä päätös on vielä vain omassa päässäsi?

---

## Lähteet ja tarkistuspäivä

- [Microsoft: Plan your Copilot Studio projects](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/plan-overview)
- [Nielsen Norman Group: Personas](https://www.nngroup.com/articles/persona/)

Tarkistettu 20.7.2026.
