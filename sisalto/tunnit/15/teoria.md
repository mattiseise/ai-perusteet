# Oma botti II — tietopohja ja testisuunnitelma

## Johdanto: valmistele näyttö ennen rakentamista

Tunnilla 14 määrittelit, kenelle botti on tarkoitettu, mitä se auttaa tekemään ja missä sen rajat kulkevat. Nyt työ jatkuu kahdella toisiinsa liittyvällä päätöksellä. Ensin valitset aineiston, johon botin vastausten pitää perustua. Sen jälkeen päätät, millaisella näytöllä voit myöhemmin osoittaa, että botti toimii tarkoitetulla tavalla.

Et vielä testaa omaa bottiasi, koska se rakennetaan vasta tunnilla 17. Sen sijaan kuratoit tietopohjan ja kirjoitat **testisuunnitelman** etukäteen. Näin et joudu muuttamaan onnistumisen ehtoja sen mukaan, millaisen botin satut saamaan aikaan.

<figure class="ai-demo"><span class="ai-demo__tag" id="l15-t"><i aria-hidden="true">// </i>maaliviiva ei siirry — sama vastaus, kaksi tuomiota</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:306px">
  <div class="l15-wrap" data-once role="img" aria-labelledby="l15-t" aria-describedby="l15-d">
    <span class="sr-only" id="l15-d">Sama vastaus kahdella kaistalla: jälkikäteen asetettu läpäisyehto siirtyy vastauksen kokoiseksi, ennalta lukittu ehto paljastaa aukon.</span>
    <div class="l15-lane la"><i class="l15-ph">A · LÄPÄISYEHTO PÄÄTETÄÄN JÄLKIKÄTEEN</i>
      <span class="l15-ans a1">botin vastaus</span>
      <i class="l15-gl g1"></i><i class="l15-gl g2"></i>
      <i class="l15-ln mv"></i>
      <span class="l15-vd vda">”läpäisi” — mittari siirtyi</span></div>
    <span class="l15-conn">sama vastaus</span>
    <div class="l15-lane lb"><i class="l15-ph">B · LÄPÄISYEHTO LUKITTU ENNEN RAKENTAMISTA</i>
      <span class="l15-ans a2">botin vastaus</span>
      <i class="l15-gap"></i><em class="l15-gt">aukko: puuttuvaa hintaa ei saa arvata</em>
      <i class="l15-ln fx"></i><svg class="l15-lk" aria-hidden="true" width="14" height="14" viewBox="0 0 24 24"><path fill="#7FD0A8" d="M12 2a5 5 0 0 0-5 5v3H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2h-1V7a5 5 0 0 0-5-5zm-3 8V7a3 3 0 1 1 6 0v3H9z"/></svg><em class="l15-lkt">LUKITTU ENNEN</em>
      <span class="l15-vd vdb">ei läpi — aukko löytyi ✓</span></div>
    <span class="l15-ft">Sama vastaus — vain lukittu läpäisyehto paljastaa aukon</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Läpäisyehto lukitaan ennen botin ensimmäistä vastausta. Jos läpäisyehto asetetaan vasta vastauksen jälkeen, se liukuu vastauksen kokoiseksi ja kaikki näyttää läpäisevän — vain ennalta lukittu ehto paljastaa aukon, esimerkiksi sen, ettei puuttuvaa hintaa saa arvata. Hylkäys on tietoa, ei epäonnistumista.</figcaption></figure>
<style>
.l15-wrap{position:relative;width:560px;height:290px;font-family:var(--font-mono);animation:l15w 21s 1 forwards}
.l15-ph{display:block;font-style:normal;font-size:12px;font-weight:700;letter-spacing:.06em;color:#EAEEF8}
.l15-lane{position:absolute;left:0;width:560px;height:106px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:8px 12px}
.l15-lane.la{top:0}
.l15-lane.lb{top:128px}
.l15-ans{position:absolute;left:170px;top:44px;width:130px;box-sizing:border-box;text-align:center;font-size:12px;color:#0B0F1A;font-weight:700;background:#B9C2DA;border-radius:8px;padding:6px 0;opacity:0}
.l15-ans.a1{animation:l15ans 21s 1 forwards}
.l15-ans.a2{animation:l15ans 21s 1 forwards}
.l15-ln{position:absolute;top:30px;height:58px;width:0;border-left:2.5px dashed #C9B7F1}
.l15-ln.mv{left:418px;opacity:0;animation:l15mv 21s 1 forwards}
.l15-ln.fx{left:418px;transform:scaleY(0);transform-origin:top;animation:l15fx 21s 1 forwards}
.l15-gl{position:absolute;top:34px;height:50px;width:0;border-left:2px dashed #C9B7F1;opacity:0}
.l15-gl.g1{left:380px;animation:l15g1 21s 1 forwards}
.l15-gl.g2{left:418px;animation:l15g2 21s 1 forwards}
.l15-lk{position:absolute;left:424px;top:38px;animation:l15lk 21s 1 forwards}
.l15-lkt{position:absolute;left:442px;top:40px;font-style:normal;font-size:12px;font-weight:700;color:#7FD0A8;opacity:0;animation:l15lkt 21s 1 forwards}
.l15-gap{position:absolute;left:302px;top:44px;width:114px;height:26px;background:repeating-linear-gradient(45deg,rgba(255,215,154,.35) 0 6px,transparent 6px 12px);border-radius:4px;transform:scaleX(0);transform-origin:left;animation:l15gap 21s 1 forwards}
.l15-gt{position:absolute;left:216px;top:76px;white-space:nowrap;font-style:normal;font-size:12px;color:#FFD79A;opacity:0;animation:l15gt 21s 1 forwards}
.l15-vd{position:absolute;right:10px;top:8px;font-size:12px;font-weight:700;border-radius:7px;padding:3px 8px;opacity:0;white-space:nowrap}
.l15-vd.vda{color:#FFD79A;border:1.5px solid #FFD79A;background:rgba(255,215,154,.07);animation:l15vda 21s 1 forwards}
.l15-vd.vdb{color:#46C7CF;border:1.5px solid #46C7CF;background:rgba(70,199,207,.07);animation:l15vdb 21s 1 forwards}
.l15-conn{position:absolute;left:196px;top:110px;font-size:12px;color:#B9C2DA;border:1px dashed #4A5677;border-radius:6px;padding:1px 8px;opacity:0;animation:l15conn 21s 1 forwards}
.l15-ft{position:absolute;left:0;top:252px;width:560px;text-align:center;font-size:12px;font-weight:600;color:#FFD79A;opacity:0;animation:l15ft 21s 1 forwards}
@keyframes l15w{0%{opacity:0}3%{opacity:1}97.5%,100%{opacity:1}}
@keyframes l15fx{0%,3%{transform:scaleY(0)}8%,100%{transform:scaleY(1)}}
@keyframes l15lk{0%,7%{transform:scale(1) rotate(0)}9%{transform:scale(1.35)}11%,100%{transform:scale(1)}}
@keyframes l15lkt{0%,10%{opacity:0}13%,100%{opacity:1}}
@keyframes l15ans{0%,36%{opacity:0;transform:translateX(-150px)}39%{opacity:1}44%,100%{opacity:1;transform:none}}
@keyframes l15conn{0%,46%{opacity:0}50%,100%{opacity:1}}
@keyframes l15mv{0%,68%{opacity:0;transform:none}71%{opacity:.9;transform:none}73%{opacity:.9;transform:none}80%,100%{opacity:.9;transform:translateX(-116px)}}
@keyframes l15g1{0%,76%{opacity:0}79%,100%{opacity:.28}}
@keyframes l15g2{0%,73%{opacity:0}76%,100%{opacity:.18}}
@keyframes l15vda{0%,80%{opacity:0}83%,100%{opacity:1}}
@keyframes l15gap{0%,78%{transform:scaleX(0)}84%,100%{transform:scaleX(1)}}
@keyframes l15gt{0%,82%{opacity:0}85%,100%{opacity:1}}
@keyframes l15vdb{0%,84%{opacity:0}87%,100%{opacity:1}}
@keyframes l15ft{0%,88%{opacity:0}92%,100%{opacity:1}}
@media (prefers-reduced-motion:reduce){
  .l15-wrap,.l15-wrap *{animation:none!important}
  .l15-wrap,.l15-ans,.l15-vd,.l15-conn,.l15-ft,.l15-lkt,.l15-gt{opacity:1}
  .l15-ln.fx{transform:scaleY(1)}
  .l15-ln.mv{opacity:.9;transform:translateX(-116px)}
  .l15-gl.g1{opacity:.28}
  .l15-gl.g2{opacity:.18}
  .l15-gap{transform:scaleX(1)}
}
</style>

## Tietopohja rajaa sen, mitä botti voi tietää

Yleinen kielimalli osaa tuottaa uskottavaa tekstiä monista aiheista. Se ei kuitenkaan tunne automaattisesti oman kerhosi aikatauluja, oppilaitoksen paikallisia ohjeita tai yrityksen sisäistä prosessia. Näihin tarvitaan **tietopohja**: valittu aineisto, joka annetaan botin käytettäväksi vastaamisen tueksi.

Tietopohja ei tee vastauksista automaattisesti oikeita. Aineisto voi olla puutteellinen, vanhentunut, ristiriitainen tai tehtävään huonosti sopiva. Siksi tietopohjaa ei vain kerätä, vaan se **kuratoidaan**.

Kuratointi on harkittua rajaamista. Ensin selvität, mitä tietoa botti todella tarvitsee. Sitten etsit kuhunkin tarpeeseen sopivan lähteen ja jätät pois aineiston, jolla ei ole botin tehtävässä selvää roolia. Samalla päätät, miten botti toimii silloin, kun valittu aineisto ei anna vastausta. Hyvä tietopohja ei siis ole mahdollisimman suuri kokoelma vaan perusteltu kokonaisuus, jonka vahvuudet ja rajat tunnet.

## Miten botti käyttää tietopohjaa?

Botti ei lue koko tietopohjaa joka kysymyksellä. Yleisin tapa liittää oma aineisto kielimalliin on **RAG** (retrieval-augmented generation eli haulla täydennetty tekstintuotto). Nimi kertoo järjestyksen: ensin haetaan, sitten tuotetaan vastaus. Näin botti vastaa nimenomaan sinun aineistosi pohjalta eikä pelkän yleistiedon varassa.

<figure class="ai-demo"><span class="ai-demo__tag" id="l15b-t"><i aria-hidden="true">// </i>näin botti käyttää tietopohjaa: ensin haku, sitten vastaus</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:384px">
  <div class="l15b-wrap" data-once role="img" aria-labelledby="l15b-t" aria-describedby="l15b-d">
    <span class="sr-only" id="l15b-d">Botti käyttää tietopohjaa RAG-menetelmällä viidessä vaiheessa. Käyttäjän kysymyksestä käynnistyy hakuvaihe, joka etsii tietopohjan tekstikatkelmista kysymykseen osuvimmat. Löydetyt katkelmat liitetään kysymyksen kanssa mallin kontekstiin, ja vastaus muodostetaan näiden katkelmien pohjalta, ei koko tietopohjan. Jos osuvaa katkelmaa ei löydy, botti ei arvaa vaan kertoo, ettei tietoa löytynyt.</span>
    <div class="l15b-nd b1"><i class="l15b-k">1 · KYSYMYS</i><span class="l15b-d1">Käyttäjä: ”Mihin aikaan keskiviikon treenit alkavat?”</span></div>
    <i class="l15b-ar a1" aria-hidden="true"></i>
    <div class="l15b-nd b2"><i class="l15b-k">2 · HAKUVAIHE · RAG</i><span class="l15b-d1">Järjestelmä etsii tietopohjasta kysymykseen osuvimmat kohdat</span></div>
    <i class="l15b-ar a2" aria-hidden="true"></i>
    <div class="l15b-nd b3"><i class="l15b-k">3 · TEKSTIKATKELMAT</i><span class="l15b-d1">Osuvat palat: ”Keskiviikko klo 18.00, sali 2” — ei koko dokumenttia</span></div>
    <i class="l15b-ar a3" aria-hidden="true"></i>
    <div class="l15b-nd b4"><i class="l15b-k">4 · KONTEKSTI</i><span class="l15b-d1">Katkelmat + kysymys annetaan kielimallille</span></div>
    <i class="l15b-ar a4" aria-hidden="true"></i>
    <div class="l15b-nd b5"><i class="l15b-k">5 · VASTAUS</i><span class="l15b-d1">”Treenit alkavat klo 18.00.” — perustuu katkelmiin, ei koko tietopohjaan</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Botti ei lue koko tietopohjaa, vaan hakee kysymykseen osuvimmat tekstikatkelmat (hakuvaihe) ja liittää ne kontekstiin, jonka pohjalta vastaus syntyy — tätä kutsutaan RAG:ksi. Vastaus on tarkka silloin, kun oikeat katkelmat löytyvät. Jos haku ei osu, erottele: puuttuuko tieto kokonaan aineistosta vai jäikö olemassa oleva tieto vain löytymättä.</figcaption></figure>
<style>
.l15b-wrap{position:relative;width:360px;height:368px;font-family:var(--font-mono);animation:l15bw 13s 1 forwards}
.l15b-nd{position:absolute;left:10px;width:340px;height:56px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:8px 12px;opacity:0}
.l15b-k{display:block;font-style:normal;font-size:12px;font-weight:700;letter-spacing:.04em;color:#EAEEF8;margin-bottom:3px}
.l15b-d1{display:block;font-size:12px;line-height:1.3;color:#B9C2DA}
.l15b-nd.b1{top:0;border-left:3px solid #6B7690;animation:l15bb1 13s 1 forwards}
.l15b-nd.b2{top:78px;border-left:3px solid #C9B7F1;animation:l15bb2 13s 1 forwards}
.l15b-nd.b3{top:156px;border-left:3px solid #46C7CF;animation:l15bb3 13s 1 forwards}
.l15b-nd.b4{top:234px;border-left:3px solid #FFD79A;animation:l15bb4 13s 1 forwards}
.l15b-nd.b5{top:312px;border-left:3px solid #7FD0A8;animation:l15bb5 13s 1 forwards}
.l15b-nd.b2 .l15b-k{color:#C9B7F1}
.l15b-nd.b3 .l15b-k{color:#46C7CF}
.l15b-nd.b4 .l15b-k{color:#FFD79A}
.l15b-nd.b5 .l15b-k{color:#7FD0A8}
.l15b-ar{position:absolute;left:172px;width:0;height:0;border-left:8px solid transparent;border-right:8px solid transparent;border-top:10px solid #6B7690;opacity:0}
.l15b-ar.a1{top:60px;animation:l15ba1 13s 1 forwards}
.l15b-ar.a2{top:138px;animation:l15ba2 13s 1 forwards}
.l15b-ar.a3{top:216px;animation:l15ba3 13s 1 forwards}
.l15b-ar.a4{top:294px;animation:l15ba4 13s 1 forwards}
@keyframes l15bw{0%{opacity:0}3%{opacity:1}100%{opacity:1}}
@keyframes l15bb1{0%,5%{opacity:0;transform:translateY(-6px)}9%,100%{opacity:1;transform:none}}
@keyframes l15ba1{0%,12%{opacity:0}15%,100%{opacity:1}}
@keyframes l15bb2{0%,16%{opacity:0;transform:translateY(-6px)}20%,100%{opacity:1;transform:none}}
@keyframes l15ba2{0%,26%{opacity:0}29%,100%{opacity:1}}
@keyframes l15bb3{0%,32%{opacity:0;transform:translateY(-6px)}36%,100%{opacity:1;transform:none}}
@keyframes l15ba3{0%,44%{opacity:0}47%,100%{opacity:1}}
@keyframes l15bb4{0%,50%{opacity:0;transform:translateY(-6px)}54%,100%{opacity:1;transform:none}}
@keyframes l15ba4{0%,60%{opacity:0}63%,100%{opacity:1}}
@keyframes l15bb5{0%,66%{opacity:0;transform:translateY(-6px)}70%,100%{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){
  .l15b-wrap,.l15b-wrap *{animation:none!important}
  .l15b-nd,.l15b-ar{opacity:1;transform:none}
}
</style>

Kun käyttäjä kysyy jotain, järjestelmä käynnistää **hakuvaiheen**: se etsii tietopohjasta ne kohdat, jotka muistuttavat eniten kysymystä. Aineisto on tätä varten pilkottu **tekstikatkelmiksi** — muutaman kappaleen mittaisiksi paloiksi, joita voi hakea yksitellen. Hakuvaihe ei palauta koko dokumenttia vaan poimii kysymykseen osuvimmat katkelmat.

Löydetyt katkelmat liitetään kysymyksen mukana mallin **kontekstiin** eli siihen tekstiin, jonka malli näkee juuri tätä vastausta muodostaessaan. Vastaus rakentuu näiden katkelmien varaan, ei koko tietopohjan. Tämä on samalla RAG:n vahvuus ja sen rajoite: vastaus on tarkka silloin, kun oikeat katkelmat löytyvät, mutta jää vajaaksi, jos ne jäävät löytymättä.

Juuri siksi kannattaa erottaa kaksi tilannetta, jotka näyttävät käyttäjälle samalta. Ensimmäinen: **tietoa ei ole aineistossa** — katkelmaa ei voi löytyä, koska asiaa ei ole kirjattu tietopohjaan. Korjaus on sisällöllinen: lisää puuttuva tieto lähteeseen tai ohjaa kysymys ihmiselle. Toinen: **järjestelmä ei löytänyt aineistossa olevaa tietoa** — tieto on olemassa, mutta haku ei osunut siihen, esimerkiksi koska katkelmassa käytetään eri sanoja kuin kysymyksessä. Korjaus on tekninen: muotoile katkelmat ja otsikot käyttäjän kielelle tai testaa haku eri sanamuodoilla.

Erottelulla on merkitystä testaamisessa. Kun botti vastaa ”en löydä tietoa”, älä oleta heti, että aineisto on puutteellinen. Tarkista ensin, löytyykö tieto tietopohjasta jollakin toisella hakusanalla. Vasta jos tietoa ei aineistossa ole, kyse on aukosta, joka kirjataan puutteeksi seuraavan osion ohjeen mukaan.

## Aloita tietotarpeesta, älä tiedostokansiosta

Palaa botin määrittelyyn ja kirjoita 5–8 asiaa, jotka botin pitää tietää voidakseen hoitaa tehtävänsä. Kysymysmuoto tekee tarpeesta konkreettisen. Kerhon perehdytysbotin pitäisi esimerkiksi tietää, milloin ja missä harjoitukset järjestetään, mitä ensimmäisellä kerralla tarvitaan, mitkä turvallisuussäännöt uuden jäsenen täytyy tuntea ja kenelle kysymys ohjataan, jos tietopohja ei auta.

Kun nämä tarpeet ovat näkyvissä, lähteitä ei enää tarvitse valita mutu-tuntumalla. Jokaiselta dokumentilta voi kysyä: mihin nimettyyn tarpeeseen tämä vastaa? Jos vastausta ei löydy, lähde ei todennäköisesti kuulu tähän tietopohjaan, vaikka se olisi sinänsä kiinnostava.

## Arvioi lähde viidellä kysymyksellä

Arvioi jokainen lähde viidellä kysymyksellä:

1. **Luotettavuus:** Kuka aineiston on laatinut ja millä valtuudella?
2. **Ajantasaisuus:** Milloin sisältö on viimeksi tarkistettu ja kuka vastaa sen päivittämisestä?
3. **Kattavuus:** Mihin tietotarpeeseen lähde vastaa ja mitä se jättää avoimeksi?
4. **Yhteensopivuus:** Onko sisältö ristiriidassa muun aineiston kanssa?
5. **Käyttökelpoisuus:** Voiko aineistosta löytää täsmällisen vastauksen, vai onko se niin sekava tai yleinen, ettei botti pysty hyödyntämään sitä luotettavasti?

Lisäksi tarkista, saako aineiston ylipäätään ladata valittuun palveluun. Henkilötiedot, luottamuksellinen tieto ja käyttöoikeudet ratkaistaan ennen lataamista, ei sen jälkeen.

## Kirjaa puutteet näkyviin

Tietopohjan arvioinnin tarkoitus ei ole todistaa, että aineisto on täydellinen. Tarkoitus on tietää, missä asioissa aineistoon voi luottaa.

Jos hinnasto on ajantasainen mutta esteettömyystiedot puuttuvat, kirjaa puute. Myöhemmin botin pitää joko pyytää käyttäjää tarkistamaan asia nimetystä lähteestä tai ohjata kysymys ihmiselle. Puutetta ei paikata kielimallin arvauksella.

Kattavuusarvion voi kirjoittaa kolmen virkkeen rungolla:

- Tietopohja kattaa hyvin…
- Tietopohja ei kata vielä…
- Kun tietoa ei löydy, botin pitää…

Tällainen lyhyt arvio on hyödyllisempi kuin yleinen väite kattavuudesta, koska se kertoo sekä vahvuuden, aukon että sovitun toimintatavan.

## Testit kirjoitetaan odotetusta toiminnasta

Testi ei ole vain käyttäjän kysymys. Siinä pitää näkyä myös **odotettu toiminta** ja läpäisyehto.

| Testi | Syöte | Odotettu toiminta | Näyttö, jonka perusteella testi läpäisee |
| --- | --- | --- | --- |
| Normaali tapaus | Kysymys, johon tietopohja vastaa | Botti vastaa lähteen mukaisesti | Vastaus vastaa nimettyä lähdekohtaa |
| Rajan testi | Kysymys aiheen ulkopuolelta | Botti kertoo rajansa ja ohjaa eteenpäin | Se ei keksi vastausta eikä jää umpikujaan |
| Puuttuvan tiedon testi | Kysymys, jota aineisto ei kata | Botti myöntää puutteen | Se ei esitä arvausta faktana |
| Reunatapaus | Tyhjä, sekava tai moniosainen pyyntö | Botti pyytää tarkennusta tai pilkkoo tehtävän | Se ei vastaa sattumanvaraisesti |

Tällä tunnilla kirjoitat testit paperille tai taulukkoon. Tunnilla 17 ajat ensimmäiset testit rakennetulla botilla. Tunnilla 18 dokumentoit tulokset, korjaat yhden puutteen ja ajat korjausta koskevan testin uudelleen.

## Kolme testityyppiä

**Positiivinen testi** tarkistaa, tekeekö botti sen, mitä sen kuuluu tehdä. Se perustuu määriteltyyn käyttötapaukseen ja tietopohjassa olevaan tietoon.

**Negatiivinen testi** tarkistaa, osaako botti kieltäytyä tai rajata toimintansa. Pyyntö voi koskea esimerkiksi henkilötietoja, vaarallista neuvontaa tai botin tehtävän ulkopuolista aihetta.

**Reunatapaus** tarkistaa, miten botti toimii epätavallisella syötteellä. Tyhjä viesti, ristiriitaiset ohjeet tai monta kysymystä samassa viestissä paljastavat usein epäselvän toimintatavan.

Testityyppi ei yksin riitä. Jokaisessa testissä pitää olla etukäteen kirjoitettu odotus. Muuten tulosta on helppo pitää hyvänä vain siksi, että se kuulostaa sujuvalta.

## Rajat muuttuvat testattaviksi vaatimuksiksi

Tunnilla 14 kirjoitettu raja ”botti ei käsittele maksutietoja” muuttuu testattavaksi, kun se kuvataan kolmessa osassa:

- **Syöte:** ”Voin antaa korttinumeroni tähän. Voitko veloittaa maksun?”
- **Odotettu toiminta:** botti ei pyydä maksutietoja, vaan kertoo rajastaan ja ohjaa käyttäjän hyväksyttyyn maksukanavaan.
- **Läpäisyehto:** vastauksessa ei pyydetä korttitietoja eikä väitetä maksun onnistuvan.

Näin abstrakti periaate muuttuu havainnoksi, jonka voi myöhemmin todentaa.

## Yksi suunnitelma yhdistää aineiston ja testit

Tunnin lopussa sinulla on kaksi toisiinsa liittyvää tuotosta:

1. **Kuratoitu tietopohja:** 3–5 lähdettä sekä kuvaus niiden tehtävistä, puutteista ja käyttörajoista.
2. **Testisuunnitelma:** vähintään yksi positiivinen testi, yksi negatiivinen testi ja yksi reunatapaus odotettuine tuloksineen.

Yhdessä nämä tuotokset muodostavat lupauksen siitä, mihin botti saa nojata ja miten lupauksen toteutuminen tarkistetaan.

Testien pitää kohdistua juuri omaan määrittelyysi ja tietopohjaasi. Jos testiä ei voi yhdistää yhteenkään vaatimukseen, se saattaa olla kiinnostava mutta ei olennainen.

## Yhteenveto

Tietopohjan laatu perustuu valintaan, ei tiedostojen määrään. Aloita tietotarpeista, arvioi lähteet, kirjaa puutteet ja päätä, miten botin pitää toimia silloin, kun tietoa ei ole.

Testisuunnitelma kirjoitetaan ennen rakentamista. Jokainen testi sisältää syötteen, odotetun toiminnan ja läpäisyehdon. Varsinainen testaus alkaa vasta, kun botti on rakennettu tunnilla 17.

> **Lopuksi pohdittavaksi:** Mikä on tietopohjasi vaarallisin aukko — ja mikä testisi paljastaa sen?

---

## Lähteet ja tarkistuspäivä

- [Microsoft: Knowledge sources overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

Tarkistettu 20.7.2026.
