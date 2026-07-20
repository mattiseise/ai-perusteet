# Oma botti I — käyttäjä, tehtävä ja rajat

## Johdanto: bottia ei aloiteta ohjetekstistä

Oman botin rakentaminen houkuttelee aloittamaan järjestelmäpromptista: kirjoitetaan botille rooli, muutama sääntö ja kokeillaan, mitä tapahtuu. Silloin tärkeimmät päätökset jäävät helposti tekemättä. Kenelle botti on tarkoitettu? Mitä käyttäjä yrittää saada aikaan? Missä tilanteessa botti auttaa — ja missä sen pitää lopettaa?

Tällä tunnilla et rakenna bottia etkä kirjoita valmista järjestelmäpromptia. Laadit **määrittelydokumentin**, jonka perusteella botin voisi myöhemmin rakentaa myös joku toinen. Suunnittelu erotetaan toteutuksesta tarkoituksella: ensin päätetään, millainen työkalu tarvitaan, vasta sitten kirjoitetaan ohjeet ja valitaan alusta.

Määrittely on lupaus tulevasta toiminnasta. Se kertoo, ketä autetaan, missä tehtävässä ja millä rajoilla. Kun nämä päätökset ovat näkyvissä, myöhempää bottia voidaan arvioida muullakin kuin kysymyksellä ”vaikuttaako tämä hyvältä?”. Ilman määrittelyä jokainen sujuva vastaus voi näyttää onnistumiselta, vaikka botti ratkaisisi väärää ongelmaa.

> **Tunnin ydinkysymys:** Mitä botin pitää auttaa tiettyä käyttäjää tekemään — ja mistä huomaat, että tehtävä onnistui?

<figure class="ai-demo"><span class="ai-demo__tag">// sumeasta ideasta arvioitavaksi määrittelyksi — prompti on viimeinen askel</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:322px">
  <div class="l14-wrap" role="img" aria-label="Botti-idea tarkentuu määrittelyksi. Sumea idea Opiskelubotti on liian laaja, joten se tiivistetään mittatikkuun: kerhon uusi jäsen tarvitsee apua sääntöjen ja aikojen löytämiseen, jotta on valmiina harjoituksiin. Onnistumiskriteeri auttaa hyvin hylätään, koska se ei ole havaittava, ja tilalle tulee: vastaus löytyy tietopohjasta. Rajakysymys ei törmää seinään vaan ohjataan yhteyshenkilölle. Määrittely valmistuu ennen promptia.">
    <span class="l14-mt"><b class="l14-slot s1"><i class="e">KÄYTTÄJÄ</i><i class="f f1">kerhon uusi jäsen</i></b><span class="l14-mw">tarvitsee apua:</span><b class="l14-slot s2"><i class="e">TEHTÄVÄ</i><i class="f f2">löytää säännöt ja ajat</i></b></span>
    <span class="l14-mt m2"><span class="l14-mw">jotta</span><b class="l14-slot s3"><i class="e">LOPPUTULOS</i><i class="f f3">valmiina harjoituksiin</i></b></span>
    <div class="l14-ws"><i class="l14-ph">TYÖTILA</i>
      <span class="l14-blob">Opiskelubotti?</span>
      <em class="l14-tag t1">liian laaja</em>
      <span class="l14-fz"><b class="l14-fzc">auttaa hyvin?<i class="l14-fzs"></i></b><em class="l14-tag t2">ei havaittava</em></span>
      <span class="l14-ok">✓ vastaus löytyy tietopohjasta</span>
      <i class="l14-line la"></i><i class="l14-line lb"></i>
      <span class="l14-test">kysymys aiheen ulkopuolelta</span>
      <span class="l14-step p1">rajaus yhdellä lauseella</span>
      <span class="l14-step p2">→ ohjaa yhteyshenkilölle</span></div>
    <div class="l14-def"><i class="l14-ph">MÄÄRITTELY</i>
      <span class="l14-dr d1"><b class="bx x1"></b>Käyttäjä</span>
      <span class="l14-dr d2"><b class="bx x2"></b>Tehtävä</span>
      <span class="l14-dr d3"><b class="bx x3"></b>Onnistuminen</span>
      <span class="l14-dr d4"><b class="bx x4"></b>Rajat</span>
      <span class="l14-fin"><i>VALMIS — EI VIELÄ PROMPTI</i></span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Määrittely on tarkentumista: laaja idea tiivistyy käyttäjäksi, tehtäväksi, havaittavaksi onnistumiskriteeriksi ja rajoiksi, joilla on ovi — ei seinää. Prompti kirjoitetaan vasta, kun määrittely on valmis. Vie hiiri kuvan päälle pysäyttääksesi.</figcaption></figure>
<style>
.l14-wrap{position:relative;width:560px;height:306px;font-family:var(--font-mono);animation:l14w 21s infinite}
.l14-wrap:hover,.l14-wrap:hover *{animation-play-state:paused}
.l14-ph{display:block;font-style:normal;font-size:10.5px;font-weight:700;letter-spacing:.08em;color:#EAEEF8}
.l14-mt{position:absolute;left:0;top:0;width:560px;display:flex;align-items:center;justify-content:center;gap:8px}
.l14-mt.m2{top:32px}
.l14-mw{font-size:10.5px;color:#B9C2DA}
.l14-slot{position:relative;width:184px;height:26px}
.l14-slot i{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:10.5px;border-radius:8px;box-sizing:border-box}
.l14-slot .e{color:#7E88A8;border:1.5px dashed #4A5677;letter-spacing:.08em}
.l14-slot .f{color:#0B0F1A;font-weight:700;opacity:0}
.l14-slot .f1{background:#C9B7F1;animation:l14f1 21s infinite}
.l14-slot .f2{background:#46C7CF;animation:l14f2 21s infinite}
.l14-slot .f3{background:#7FD0A8;animation:l14f3 21s infinite}
.l14-slot.s1 .e{animation:l14e1 21s infinite}
.l14-slot.s2 .e{animation:l14e2 21s infinite}
.l14-slot.s3 .e{animation:l14e3 21s infinite}
.l14-ws{position:absolute;left:2px;top:72px;width:330px;height:234px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:9px 12px}
.l14-blob{position:absolute;left:30px;top:52px;width:250px;height:44px;display:flex;align-items:center;justify-content:center;font-size:12.5px;color:#B9C2DA;border:2px dashed #4A5677;border-radius:22px;opacity:0;animation:l14blob 21s infinite}
.l14-tag{position:absolute;font-style:normal;font-size:10px;color:#FFD79A;border:1px solid #FFD79A;border-radius:6px;padding:2px 6px;opacity:0;background:rgba(255,215,154,.07)}
.l14-tag.t1{left:214px;top:32px;animation:l14t1 21s infinite}
.l14-fz{position:absolute;left:24px;top:56px;opacity:0;animation:l14fz 21s infinite}
.l14-fzc{position:relative;display:inline-block;font-size:11.5px;font-weight:400;color:#EAEEF8;border:1px solid #2B3552;border-radius:8px;padding:5px 10px;background:#0E1524}
.l14-fzs{position:absolute;left:6px;top:50%;width:86%;height:2px;background:#FFD79A;transform:scaleX(0);transform-origin:left;animation:l14fzs 21s infinite}
.l14-fz .l14-tag{position:static;margin-left:8px;opacity:0;animation:l14t2 21s infinite}
.l14-ok{position:absolute;left:24px;top:100px;font-size:11px;font-weight:700;color:#7FD0A8;border:1.5px solid #7FD0A8;border-radius:8px;padding:5px 10px;opacity:0;animation:l14ok 21s infinite}
.l14-line{position:absolute;left:216px;width:0;border-left:2px dashed #7E88A8;transform:scaleY(0)}
.l14-line.la{top:26px;height:92px;transform-origin:top;animation:l14la 21s infinite}
.l14-line.lb{top:158px;height:66px;transform-origin:bottom;animation:l14lb 21s infinite}
.l14-test{position:absolute;left:14px;top:150px;font-size:10.5px;color:#EAEEF8;border:1px solid #4A5677;border-radius:8px;padding:4px 8px;opacity:0;animation:l14test 21s infinite}
.l14-step{position:absolute;font-size:10px;line-height:1.25;color:#7FD0A8;border:1.5px solid #7FD0A8;border-radius:7px;padding:3px 7px;opacity:0;background:rgba(127,208,168,.07)}
.l14-step.p1{left:14px;top:188px;animation:l14p1 21s infinite}
.l14-step.p2{left:180px;top:188px;width:140px;box-sizing:border-box;animation:l14p2 21s infinite}
.l14-def{position:absolute;left:344px;top:72px;width:214px;height:234px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:9px 12px}
.l14-dr{position:relative;display:block;margin-top:13px;padding-left:22px;font-size:11px;line-height:1.3;color:#EAEEF8}
.l14-dr .bx{position:absolute;left:0;top:1px;width:12px;height:12px;border:1.5px solid #4A5677;border-radius:3px}
.l14-dr .bx::after{content:'✓';position:absolute;left:1px;top:-3px;font-size:11px;font-weight:700;color:#7FD0A8;opacity:0}
.l14-dr .bx.x1::after{animation:l14x1 21s infinite}
.l14-dr .bx.x2::after{animation:l14x2 21s infinite}
.l14-dr .bx.x3::after{animation:l14x3 21s infinite}
.l14-dr .bx.x4::after{animation:l14x4 21s infinite}
.l14-fin{position:absolute;left:0;bottom:14px;width:100%;text-align:center;opacity:0;animation:l14fin 21s infinite}
.l14-fin i{display:inline-block;font-style:normal;font-size:10.5px;font-weight:700;color:#FFD79A;border:1.5px solid #FFD79A;border-radius:7px;padding:4px 8px;transform:rotate(-4deg);background:rgba(255,215,154,.07)}
@keyframes l14w{0%{opacity:0}3%{opacity:1}97.5%{opacity:1}100%{opacity:0}}
@keyframes l14blob{0%,4%{opacity:0;transform:scale(1)}8%{opacity:1}17%{opacity:1;transform:scale(1)}24%{opacity:0;transform:scale(.42) translateY(-60px)}100%{opacity:0}}
@keyframes l14t1{0%,10%{opacity:0}14%{opacity:1}22%{opacity:1}26%,100%{opacity:0}}
@keyframes l14e1{0%,24%{opacity:1}27%,100%{opacity:0}}
@keyframes l14f1{0%,24%{opacity:0;transform:scale(.8)}27%,100%{opacity:1;transform:scale(1)}}
@keyframes l14x1{0%,25%{opacity:0}28%,100%{opacity:1}}
@keyframes l14e2{0%,29%{opacity:1}32%,100%{opacity:0}}
@keyframes l14f2{0%,29%{opacity:0;transform:scale(.8)}32%,100%{opacity:1;transform:scale(1)}}
@keyframes l14x2{0%,30%{opacity:0}33%,100%{opacity:1}}
@keyframes l14e3{0%,36%{opacity:1}39%,100%{opacity:0}}
@keyframes l14f3{0%,36%{opacity:0;transform:scale(.8)}39%,100%{opacity:1;transform:scale(1)}}
@keyframes l14fz{0%,40%{opacity:0;transform:translateY(6px)}44%,100%{opacity:1;transform:none}}
@keyframes l14fzs{0%,45%{transform:scaleX(0)}48%,100%{transform:scaleX(1)}}
@keyframes l14t2{0%,46%{opacity:0}49%,100%{opacity:1}}
@keyframes l14ok{0%,50%{opacity:0;transform:translateY(6px)}55%,100%{opacity:1;transform:none}}
@keyframes l14x3{0%,58%{opacity:0}61%,100%{opacity:1}}
@keyframes l14la{0%,67%{transform:scaleY(0)}69%,100%{transform:scaleY(1)}}
@keyframes l14lb{0%,67%{transform:scaleY(0)}69%,100%{transform:scaleY(1)}}
@keyframes l14test{0%,69%{opacity:0;transform:translateX(-30px)}72%{opacity:1;transform:translateX(0)}76%,100%{opacity:1;transform:translateX(120px)}}
@keyframes l14p1{0%,76%{opacity:0}80%,100%{opacity:1}}
@keyframes l14p2{0%,80%{opacity:0;transform:translateX(-8px)}84%,100%{opacity:1;transform:none}}
@keyframes l14x4{0%,86%{opacity:0}89%,100%{opacity:1}}
@keyframes l14fin{0%,90%{opacity:0;transform:scale(.6)}93%,100%{opacity:1;transform:scale(1)}}
@media (prefers-reduced-motion:reduce){
  .l14-wrap,.l14-wrap *{animation:none!important}
  .l14-wrap,.l14-slot .f,.l14-fz,.l14-ok,.l14-test,.l14-step,.l14-fin,.l14-dr .bx::after{opacity:1}
  .l14-slot .e,.l14-blob,.l14-tag.t1{opacity:0}
  .l14-fz .l14-tag{opacity:1}
  .l14-fzs{transform:scaleX(1)}
  .l14-line{transform:scaleY(1)}
  .l14-test{transform:translateX(120px)}
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

Kun onnistuminen on havaittava, tunnilla 15 voidaan kirjoittaa sitä koskevat testit ja tunneilla 17–18 voidaan tarkistaa, toteutuuko se oikeassa botissa.

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

Kirjaa määrittelyyn alustava luettelo tietotarpeista. Tunnilla 15 etsit niihin sopivat lähteet ja arvioit, mitä aineisto kattaa ja mitä ei.

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

Näiden päätösten jälkeen järjestelmäpromptin kirjoittaminen on myöhemmin muuntamista, ei arvailua. Tunnilla 17 kokoat määrittelyn, promptikortin toimivan rakenteen ja tietopohjan yhdeksi toteutukseksi.

Lue taulukkoa päätösketjuna, ei kuutena irrallisena kenttänä. Käyttäjän tilanne määrittää tehtävän, tehtävä määrittää onnistumisen, onnistuminen ohjaa keskustelun etenemistä ja rajat kertovat, milloin vastuu siirtyy botilta ihmiselle. Rooli ja sävy tukevat tätä kokonaisuutta, mutta eivät muuta sen tarkoitusta.

## Yhteenveto

Tällä tunnilla suunnittelet ennen rakentamista. Rajaat käyttäjän, tehtävän, havaittavan onnistumisen, keskustelun etenemisen, roolin, äänensävyn ja toiminnan rajat. Et vielä kirjoita valmista järjestelmäpromptia tai testaa omaa bottia.

Tunnin tuotoksena syntyy **rakennuspalikka 2: botin määrittelydokumentti**. Se kertoo, mitä tunnilla 17 rakennetaan ja millä perusteella toteutusta myöhemmin arvioidaan.

> **Lopuksi pohdittavaksi:** Voisiko toinen ihminen rakentaa määrittelysi perusteella saman botin kuin sinä? Jos ei, mikä päätös on vielä vain omassa päässäsi?

---

## Lähteet ja tarkistuspäivä

- [Microsoft: Plan your agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/plan-your-agent)
- [Nielsen Norman Group: Personas](https://www.nngroup.com/articles/persona/)

Tarkistettu 20.7.2026.
