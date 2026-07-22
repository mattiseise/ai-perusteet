# AI työparina — pohja, muokkaus ja tarkistus

## Johdanto: työparuus ei tarkoita työn luovuttamista

Tämän tunnin sykli toimii millä tahansa keskustelevalla tekoälypalvelulla — ChatGPT:llä, Claudella, Microsoft Copilotilla tai Google Geminillä. Kannattaa kokeilla sitä, joka on sinulle käytettävissä; menetelmä ei ole työkalusidonnainen.

Tekoälystä on hyötyä, kun sille annetaan rajattu rooli työprosessissa. Se voi tehdä ensimmäisen luonnoksen, ehdottaa vaihtoehtoja tai toimia kriittisenä lukijana. Ihminen päättää tavoitteen, tunnistaa virheet, tekee olennaiset valinnat ja hyväksyy lopputuloksen.

Tämän tunnin työskentelymalli on:

> **Pohja → oma muokkaus → tarkistus → päätös**

Tavoite ei ole saada tekoälyltä mahdollisimman valmis vastaus. Tavoite on tehdä oma ajattelu ja korjaukset näkyviksi.

<figure class="ai-demo"><span class="ai-demo__tag" id="l13-t"><i aria-hidden="true">// </i>jäljet jäävät — ihminen rajaa ensin ja päättää viimeisenä</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:392px">
  <div class="l13-wrap" data-once role="img" aria-labelledby="l13-t" aria-describedby="l13-d">
    <span class="sr-only" id="l13-d">Palautusohje syntyy työparityönä: ihminen antaa tavoitteen ja lähdeaineiston, tekoäly luonnostelee, ihminen korjaa ja lisää lähteen perusteella, arvioi tekoälyn ehdotukset perustellen ja päättää viimeisenä. Työn jälki -loki näyttää jokaisen vaiheen tekijän.</span>
    <span class="l13-rail r1">POHJA</span><span class="l13-rail r2">MUOKKAUS</span><span class="l13-rail r3">TARKISTUS</span><span class="l13-rail r4">PÄÄTÖS</span>
    <i class="l13-ul"></i>
    <div class="l13-doc"><i class="l13-ph">PALAUTUSOHJE — LUONNOS → OMA VERSIO</i>
      <span class="l13-goal">tavoite + lähdeaineisto</span>
      <span class="l13-tr ai t1">ohjeen runko: neljä vaihetta</span>
      <span class="l13-tr ai t2">palautus asiakastilin painikkeella<i class="l13-x"></i></span>
      <span class="l13-tr hu t2b">palautus tilausvahvistuksen linkistä <i class="l13-tag">lähde</i></span>
      <span class="l13-tr ai t3">palautusaika: 14 päivää</span>
      <span class="l13-tr hu t4">+ tuotteen oltava käyttämätön <i class="l13-tag">lähde</i></span>
      <span class="l13-tr su sa">ehdotus: selvennys aloittelijalle <i class="l13-tag tn">käyttäjän tarve</i></span>
      <span class="l13-tr su sb">ehdotus: poista määräaika<i class="l13-x"></i></span>
      <em class="l13-rej">hylätty: määräaika on lähteessä</em></div>
    <div class="l13-log"><i class="l13-ph">TYÖN JÄLKI</i>
      <span class="l13-lr h l1">Sinä: tavoite ja aineisto</span>
      <span class="l13-lr a l2">AI: luonnos</span>
      <span class="l13-lr h l3">Sinä: 2 muutosta + perusteet</span>
      <span class="l13-lr a l4">AI: 2 ehdotusta</span>
      <span class="l13-lr h l5">Sinä: hyväksyit yhden, hylkäsit yhden</span>
      <span class="l13-lr h l6">Sinä: päätös</span>
      <span class="l13-st"><i>IHMINEN PÄÄTTÄÄ ✓</i></span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Lopputulos on eri teksti kuin tekoälyn luonnos, ja eron tekee ihminen: rajaus ensin, korjaukset ja lisäykset lähteen perusteella, ehdotusten arviointi tavoitteen, lähteen ja käyttäjän tarpeen perusteella sekä päätös viimeisenä. Teal = tekoälyn tuotos, vihreä = ihmisen panos — perusteet lukevat riveillä.</figcaption></figure>
<style>
.l13-wrap{position:relative;width:560px;height:376px;font-family:var(--font-mono);animation:l13w 21s 1 forwards}
.l13-rail{position:absolute;top:0;width:132px;height:26px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;letter-spacing:.05em;color:#B9C2DA;border:1px solid #2B3552;border-radius:999px;background:#0E1524}
.l13-rail.r1{left:2px}.l13-rail.r2{left:144px}.l13-rail.r3{left:286px}.l13-rail.r4{left:428px}
.l13-ul{position:absolute;left:2px;top:30px;width:132px;height:3px;border-radius:2px;background:#C9B7F1;animation:l13ul 21s 1 forwards}
.l13-ph{display:block;font-style:normal;font-size:12px;font-weight:700;letter-spacing:.04em;color:#EAEEF8}
.l13-doc{position:absolute;left:2px;top:44px;width:330px;height:332px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:9px 12px}
.l13-goal{display:inline-block;margin-top:7px;font-size:12px;color:#7FD0A8;border:1.5px solid #7FD0A8;border-radius:7px;padding:3px 8px;opacity:0;animation:l13goal 21s 1 forwards}
.l13-tr{position:relative;display:block;margin-top:9px;padding:3px 6px 3px 9px;font-size:12px;line-height:1.25;color:#EAEEF8;border-left:3px solid #46C7CF;opacity:0}
.l13-tr.hu{border-left-color:#7FD0A8}
.l13-tr.su{border-left-color:#46C7CF;border-left-style:dashed;color:#B9C2DA}
.l13-tag{display:inline-block;font-style:normal;font-size:12px;color:#FFD79A;border:1px solid #FFD79A;border-radius:6px;padding:0 5px;margin-left:5px;opacity:0}
.l13-tag.tn{color:#7FD0A8;border-color:#7FD0A8}
.l13-x{position:absolute;left:6px;top:50%;width:0;height:2px;background:#FFD79A;transform:scaleX(0);transform-origin:left}
.l13-tr.t1{animation:l13t1 21s 1 forwards}
.l13-tr.t2{animation:l13t2 21s 1 forwards}
.l13-tr.t2 .l13-x{width:96%;animation:l13x2 21s 1 forwards}
.l13-tr.t2b{animation:l13t2b 21s 1 forwards}
.l13-tr.t2b .l13-tag{animation:l13tag2 21s 1 forwards}
.l13-tr.t3{animation:l13t3 21s 1 forwards}
.l13-tr.t4{animation:l13t4 21s 1 forwards}
.l13-tr.t4 .l13-tag{animation:l13tag4 21s 1 forwards}
.l13-tr.sa{animation:l13sa 21s 1 forwards}
.l13-tr.sa .l13-tag{animation:l13taga 21s 1 forwards}
.l13-tr.sb{animation:l13sb 21s 1 forwards}
.l13-tr.sb .l13-x{width:60%;animation:l13xb 21s 1 forwards}
.l13-rej{display:block;margin-top:4px;margin-left:12px;font-style:normal;font-size:12px;color:#FFD79A;opacity:0;animation:l13rej 21s 1 forwards}
.l13-log{position:absolute;left:344px;top:44px;width:214px;height:332px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:9px 12px}
.l13-lr{position:relative;display:block;margin-top:10px;padding-left:15px;font-size:12px;line-height:1.25;color:#B9C2DA;opacity:0}
.l13-lr::before{content:'';position:absolute;left:0;top:4px;width:8px;height:8px;border-radius:50%}
.l13-lr.h::before{background:#7FD0A8}
.l13-lr.a::before{background:#46C7CF}
.l13-lr.l1{animation:l13l1 21s 1 forwards}.l13-lr.l2{animation:l13l2 21s 1 forwards}
.l13-lr.l3{animation:l13l3 21s 1 forwards}.l13-lr.l4{animation:l13l4 21s 1 forwards}
.l13-lr.l5{animation:l13l5 21s 1 forwards}.l13-lr.l6{animation:l13l6 21s 1 forwards}
.l13-st{position:absolute;left:0;bottom:14px;width:100%;text-align:center;opacity:0;animation:l13st 21s 1 forwards}
.l13-st i{display:inline-block;font-style:normal;font-size:12px;font-weight:700;color:#C9B7F1;border:1.5px solid #C9B7F1;border-radius:7px;padding:5px 10px;background:rgba(201,183,241,.08);transform:rotate(-5deg)}
@keyframes l13w{0%{opacity:0}3%{opacity:1}100%{opacity:1}}
@keyframes l13ul{0%,31%{transform:translateX(0)}35%{transform:translateX(142px)}65%{transform:translateX(142px)}68%{transform:translateX(284px)}87%{transform:translateX(284px)}89.5%,100%{transform:translateX(426px)}}
@keyframes l13goal{0%,3.5%{opacity:0;transform:translateY(-5px)}7.5%,100%{opacity:1;transform:none}}
@keyframes l13t1{0%,10%{opacity:0;transform:translateY(-6px)}13%,100%{opacity:1;transform:none}}
@keyframes l13t2{0%,13%{opacity:0;transform:translateY(-6px)}16%{opacity:1;transform:none}41%{opacity:1}44%,100%{opacity:.7;transform:none}}
@keyframes l13x2{0%,38%{transform:scaleX(0)}41%,100%{transform:scaleX(1)}}
@keyframes l13t2b{0%,41%{opacity:0;transform:translateX(-8px)}45%,100%{opacity:1;transform:none}}
@keyframes l13tag2{0%,44%{opacity:0}47%,100%{opacity:1}}
@keyframes l13t3{0%,16%{opacity:0;transform:translateY(-6px)}19%,100%{opacity:1;transform:none}}
@keyframes l13t4{0%,48%{opacity:0;transform:translateX(-8px)}52%,100%{opacity:1;transform:none}}
@keyframes l13tag4{0%,51%{opacity:0}54%,100%{opacity:1}}
@keyframes l13sa{0%,69%{opacity:0;transform:translateX(14px)}72%{opacity:1;transform:none;border-left-style:dashed;color:#B9C2DA}78%{border-left-style:dashed}81%,100%{opacity:1;border-left-style:solid;border-left-color:#7FD0A8;color:#EAEEF8}}
@keyframes l13taga{0%,80%{opacity:0}83%,100%{opacity:1}}
@keyframes l13sb{0%,71%{opacity:0;transform:translateX(14px)}74%,100%{opacity:1;transform:none}}
@keyframes l13xb{0%,83%{transform:scaleX(0)}86%,100%{transform:scaleX(1)}}
@keyframes l13rej{0%,84%{opacity:0}87%,100%{opacity:1}}
@keyframes l13l1{0%,6%{opacity:0;transform:translateY(5px)}9%,100%{opacity:1;transform:none}}
@keyframes l13l2{0%,24%{opacity:0;transform:translateY(5px)}27%,100%{opacity:1;transform:none}}
@keyframes l13l3{0%,57%{opacity:0;transform:translateY(5px)}61%,100%{opacity:1;transform:none}}
@keyframes l13l4{0%,74%{opacity:0;transform:translateY(5px)}77%,100%{opacity:1;transform:none}}
@keyframes l13l5{0%,87%{opacity:0;transform:translateY(5px)}89%,100%{opacity:1;transform:none}}
@keyframes l13l6{0%,92%{opacity:0;transform:translateY(5px)}94%,100%{opacity:1;transform:none}}
@keyframes l13st{0%,90%{opacity:0;transform:scale(.6)}93%,100%{opacity:1;transform:scale(1)}}
@media (prefers-reduced-motion:reduce){
  .l13-wrap,.l13-wrap *{animation:none!important}
  .l13-wrap,.l13-goal,.l13-lr,.l13-st,.l13-tr,.l13-rej,.l13-tag{opacity:1}
  .l13-tr.t2{opacity:.7}
  .l13-tr.t2 .l13-x,.l13-tr.sb .l13-x{transform:scaleX(1)}
  .l13-tr.sa{border-left-style:solid;border-left-color:#7FD0A8;color:#EAEEF8}
  .l13-ul{transform:translateX(426px)}
}
</style>

## Läpi kulkeva esimerkki: palautusohje luonnoksesta päätökseksi

Kuvittele, että kirjoitat verkkokaupan uudelle asiakkaalle lyhyen palautusohjeen. Hyväksytty lähde kertoo kolme asiaa: palautuksesta ilmoitetaan 14 päivän kuluessa, tuotteen pitää olla käyttämätön ja palautus aloitetaan tilausvahvistuksessa olevasta linkistä. Asiakaspalvelun yhteystieto on varareitti, jos linkki ei toimi.

Pyydät tekoälyltä enintään kuuden vaiheen luonnoksen. Luonnos alkaa selkeästi, mutta siinä lukee: ”Kirjaudu asiakastilillesi ja valitse Peruuta tilaus.” Lähteessä ei mainita asiakastiliä tai tämännimistä painiketta. Luonnoksesta puuttuu myös ehto, jonka mukaan tuotteen pitää olla käyttämätön. Teksti kuulostaa sujuvalta, mutta sitä ei voi julkaista sellaisenaan.

Luet luonnoksen lähteen rinnalla. Säilytät ymmärrettävän aloituksen, korvaat keksityn vaiheen ohjeella avata tilausvahvistuksen palautuslinkki ja lisäät käyttämättömyyttä koskevan ehdon. Kirjaat päätöslokiin, että ensimmäinen muutos perustuu todelliseen asiointipolkuun ja toinen palautusehtoihin. Näin oma työsi näkyy muuna kuin kieliasun silottamisena.

Seuraavaksi annat korjatun version tekoälylle testilukijan roolissa. Se huomauttaa, ettei aloittelija ehkä tiedä, mistä tilausvahvistus löytyy, ja ehdottaa samalla koko 14 päivän määräajan poistamista tekstin keventämiseksi. Hyväksyt ensimmäisen havainnon ja lisäät, että vahvistus löytyy sähköpostista. Hylkäät toisen ehdotuksen, koska määräaika on käyttäjän toiminnan kannalta olennainen lähdetieto.

Lopullinen ohje syntyy siis neljän erilaisen päätöksen kautta: tekoäly tuotti käyttökelpoisen pohjan, ihminen korjasi faktat, tekoäly auttoi löytämään yhden epäselvän kohdan ja ihminen arvioi myös palautteen. Työparuus ei näy siinä, kuinka monta virkettä tekoäly kirjoitti, vaan siinä, että jokaisen muutoksen peruste voidaan osoittaa.

## 1. Pyydä pohja, älä lopullista totuutta

Ensimmäinen versio voi olla rakenne, luonnos tai vaihtoehtojen lista. Kerro tekoälylle:

- mitä olet tekemässä
- kenelle lopputulos on tarkoitettu
- mitä lähdeaineistoa pitää käyttää
- missä muodossa pohja tarvitaan
- mitä asioita ei saa keksiä

Esimerkiksi käyttöohjeen ensimmäinen pohja voi sisältää otsikot ja työvaiheet. Se ei vielä ole julkaistava ohje. Sen tehtävä on antaa jotakin, jota voit arvioida ja muokata.

Palautusohjeen esimerkissä hyödyllinen pohja säästi rakenteen aloittamisen vaivan. Samalla keksitty painike osoitti, miksi luonnosta pitää käsitellä väitteenä, joka tarkistetaan, eikä valmiina tietona.

## 2. Lue kuin toimittaja

Älä aloita tekstin silottamisesta. Tarkista ensin sisältö:

1. Vastaako luonnos oikeaan tehtävään?
2. Säilyvätkö lähdeaineiston faktat?
3. Puuttuuko jokin olennainen vaihe?
4. Onko mukana perusteeton väite tai oletus?
5. Sopivatko rakenne ja vaikeustaso yleisölle?

Merkitse muutokset näkyviin. Voit käyttää kommentteja tai taulukkoa:

| Luonnoksen kohta | Ongelma | Oma korjaus | Peruste |
| --- | --- | --- | --- |
|  |  |  |  |

Tämä tekee ihmisen panoksen näkyväksi. Pelkkä lopullinen teksti ei kerro, ymmärsitkö, mitä piti korjata.

Päätösloki ei ole vain arviointia varten. Se auttaa myös myöhempää muokkaajaa näkemään, mikä kohta perustuu lähteeseen, mikä kohderyhmän tarpeeseen ja mikä on tietoinen rajaus. Ilman perustelua oikeakin muutos voi näyttää satunnaiselta tyylivalinnalta.

## 3. Tee itse olennaiset päätökset

Tekoäly voi ehdottaa, mutta se ei tunne tavoitettasi yhtä hyvin kuin sinä. Päätä itse ainakin:

- mitä sisältöä poistetaan tai lisätään
- mihin järjestykseen asiat asetetaan
- mikä sävy sopii tilanteeseen
- mitkä väitteet pitää tarkistaa lähteestä
- milloin luonnos hylätään kokonaan

Kaikkea ei tarvitse pelastaa. Jos luonnos perustuu väärään oletukseen, uusi rajattu prompti voi olla järkevämpi kuin pitkän tekstin paikkaaminen.

Ihmisen päätösvalta näkyy myös säilyttämisessä. Palautusohjeen selkeä aloitus kannatti pitää, vaikka seuraava vaihe oli väärä. Kriittinen lukeminen ei tarkoita kaiken tekoälyn tuottaman hylkäämistä, vaan jokaisen kohdan arvioimista tehtävän ja lähteen perusteella.

## 4. Käytä tekoälyä testilukijana

Kun olet tehnyt oman version, anna tekoälylle rajattu tarkistusrooli. Älä pyydä ”parantamaan kaikkea”, vaan etsi nimettyä ongelmaa:

- löydä kohta, jossa aloittelija voi eksyä
- osoita termi, jota ei ole selitetty
- etsi väite, jolle lähteessä ei ole tukea
- tarkista, etenevätkö vaiheet oikeassa järjestyksessä

Pyydä havainto ja kysymys, älä valmista uudelleenkirjoitusta. Näin sinä säilytät päätösvallan.

Testilukija ei tunne käyttäjää eikä todellista käyttötilannetta automaattisesti. Siksi sille annetaan kohderyhmä ja yksi tarkastelukulma. Palautusohjeessa kysymys ”Missä aloittelija voi jäädä jumiin?” toi esiin tilausvahvistuksen löytämisen, mutta ei antanut mallille oikeutta poistaa tärkeää määräaikaa.

## 5. Tarkista tarkistajan ehdotus

Tekoälyn palaute voi olla väärä, epäolennainen tai tyyliltään huono. Jokaisesta ehdotuksesta päätetään:

- hyväksyn
- muokkaan
- hylkään

Kirjaa ainakin yksi hylätty ehdotus ja sen peruste. Kriittinen työparuus näkyy myös siinä, mitä et ota mukaan.

Hyväksyminen, muokkaaminen ja hylkääminen eivät ole mielipideäänestyksiä. Ratkaisu sidotaan ennalta määriteltyyn tavoitteeseen, lähteeseen tai käyttäjän tarpeeseen. Silloin myös hylätty ehdotus osoittaa osaamista: tunnistit, miksi sujuvalta kuulostava muutos olisi heikentänyt lopputulosta.

## Sama sykli toimii eri tehtävissä

Mallia voi käyttää kirjoittamisessa, opiskelussa, suunnittelussa ja ongelmanratkaisussa. Tehtävä vaihtuu, mutta vastuunjako säilyy:

| Vaihe | Tekoälyn rooli | Ihmisen vastuu |
| --- | --- | --- |
| Pohja | tuottaa rajatun luonnoksen tai vaihtoehtoja | määrittää tehtävän ja aineiston |
| Muokkaus | voi vastata tarkentaviin kysymyksiin | korjaa sisällön, rakenteen ja sävyn |
| Tarkistus | etsii nimettyä ongelmaa | arvioi ehdotuksen ja tarkistaa lähteet |
| Päätös | ei tee lopullista hyväksyntää | hyväksyy, hylkää ja vastaa tuloksesta |

## Yhteenveto

Tekoäly on hyödyllinen työpari, kun sen rooli vaihtuu työvaiheen mukaan. Ensin se tekee pohjan. Sitten ihminen muokkaa ja perustelee muutokset. Lopuksi tekoäly voi toimia rajattuna testilukijana, mutta ihminen arvioi myös sen palautteen.

Tunnin tuotoksessa pitää näkyä ennen–jälkeen-ero, omat korjaukset ja niiden perusteet. Valmis teksti yksin ei osoita työparitaitoa.

> **Lopuksi pohdittavaksi:** Mikä lopputuloksessa on parempaa juuri sinun päätöksesi vuoksi — ja mistä toinen ihminen voi sen nähdä?

---

## Lähteet ja tarkistuspäivä

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

Tarkistettu 20.7.2026.
