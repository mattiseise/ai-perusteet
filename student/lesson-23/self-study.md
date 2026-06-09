# Suunnittelumallit — ReAct, ketjuajattelu ja orkestrointi

## Johdanto

Nyt tiedät, mistä agentti koostuu: muistista, työkaluista ja identiteetistä. Seuraava kysymys on, miten saat agentin **ajattelemaan ja toimimaan järkevästi**. Miten varmistat, että se etenee oikeassa järjestyksessä eikä hyppää sattumanvaraisesti vääriin johtopäätöksiin?

Vastaus on **suunnittelumallit** eli design patterns. Ne ovat testattuja tapoja ohjata sitä, miten agentti päättelee ja toimii. Suunnittelumallit perustuvat siihen, **miten ihmiset ratkaisevat monimutkaisia ongelmia**: he perustelevat päätöksiään, jakavat ongelman osiin ja koordinoivat eri työvaiheita.

Seuraavassa projektissa käytät näitä malleja. Sinä päätät, käyttääkö agenttisi **ReAct-mallia** vai **ketjuajattelua** ja rakennatko sen yksittäiseksi agentiksi vai moniagenttijärjestelmäksi. Nämä päätökset vaikuttavat siihen, onko agentti tehokas, hidas, selkeä vai vaikeasti hallittava.

## ReAct: ajattele, toimi ja ajattele uudelleen

**ReAct** tarkoittaa sanoja **Reasoning + Acting** eli päättely ja toiminta. ReAct-mallissa agentti vuorottelee ajattelun ja toiminnan välillä. Se ei hyppää suoraan toimintaan, vaan ajattelee ensin, toimii sen jälkeen ja arvioi sitten toiminnan tuloksen.

Käytännössä se voi näyttää tältä. Agentti saa tehtävän: ”Asiakas kysyy, onko tuotetta saatavilla.” Agentti ei heti kutsu varasto-API:a, vaan aloittaa **ajattelulla**: ”Asiakkaan kysymys on selkeä. Minun täytyy tarkistaa varastotilanne. Kutsun varasto-API:a.” Tämä ajattelu voidaan kirjata lokiin, jotta nähdään, mitä agentti on päätellyt.

Seuraavaksi tulee **toiminta**: agentti kutsuu varasto-API:a ja saa vastauksen: ”Tuotetta on 5 kappaletta.”

Sitten agentti **ajattelee uudelleen**: ”Varasto kertoo, että tuotetta on 5 kappaletta. Asiakas voi siis ostaa tuotteen. Minulla on nyt riittävä tieto vastaukseen.” Agentti perustelee, mikä seuraava askel on.

Lopuksi agentti tekee **toisen toiminnon** ja kirjoittaa asiakkaalle vastauksen: ”Kyllä, tuotetta on 5 kappaletta varastossa. Voit tehdä tilauksen nyt.” Ajattelu ja toiminta vuorottelevat, kunnes tehtävä on valmis.

ReAct on tehokas malli, koska agentti perustelee jokaisen askeleensa ennen toimintaa. Se ei toimi sokkona, vaan kertoo ensin, miksi se tekee seuraavan toimenpiteen. Tämä tekee agentin päätöksistä **ymmärrettävämpiä** ja vähentää virheiden todennäköisyyttä.

**ReAct-mallin eteneminen**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tehtävä saapuu** | → | **Ajattele** Mitä tiedän? Mitä tarvitsen? | → | **Toimi** Kutsu työkalua tai hae tietoa. |
| ↓ | | | | |
| **Vastaa käyttäjälle** | ← | **Riittääkö tieto?** Kyllä: vastaa. Ei: ajattele uudelleen. | ← | **Havainnoi** Mitä sain? Oliko tulos hyödyllinen? |

Kun ReAct-mallin toimintaa lokitetaan, agentin ajattelu ja toiminta näkyvät selvästi:

**[AJATTELU]** Asiakkaan kysymys koskee tuotteen hintaa. Minun täytyy hakea se tietokannasta.

**[TOIMINTA]** GET /api/product?id=12345 → Hinta: 45 €

**[AJATTELU]** Tietokanta antoi hinnan. Minulla on nyt vastaus.

**[TOIMINTA]** Lähetä vastaus: ”Tuotteen hinta on 45 €.”

Näet jokaisen vaiheen ja voit ymmärtää, mitä agentti päätteli. Jos jokin menee pieleen, lokista voi nähdä tarkasti, missä ajattelun tai toiminnan vaiheessa virhe tapahtui.

> **Pysähdy hetkeksi:** Ajattele omaa ratkaisuprosessiasi. Kun ratkaiset ongelmaa, ajatteletko ensin, toimitko sen jälkeen ja arvioitko sitten tuloksen perusteella? Vai hyppäätkö suoraan toimintaan? Miten ReAct-malli voisi auttaa sinua tekemään parempia päätöksiä?

<figure class="ai-demo"><span class="ai-demo__tag">// tekoälyagentin toiminta — ReAct, ketjuajattelu ja orkestrointi</span>
<div class="ai-demo__stage" style="display:flex;flex-direction:column;align-items:center;justify-content:flex-start;gap:8px;padding:14px 18px;height:430px">
  <div class="ag-scn"><span class="ag-scn-k">Käyttäjä:</span> "Voinko pyöräillä töihin huomenna?"</div>
  <div class="ag-stage">
    <svg class="ag-svg" viewBox="0 0 460 330" aria-hidden="true">
      <defs><radialGradient id="agGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="oklch(0.72 0.16 264)"/><stop offset="60%" stop-color="oklch(0.5 0.18 285)"/><stop offset="100%" stop-color="#0B0F1A" stop-opacity="0"/></radialGradient></defs>
      <!-- ReAct-kehä -->
      <circle class="ag-ring" cx="230" cy="165" r="100" fill="none" stroke="oklch(0.66 0.15 264)" stroke-width="1.5" stroke-dasharray="3 9" opacity=".55"/>
      <!-- aktiivinen valokaari kiertää kehää -->
      <circle class="ag-arc" cx="230" cy="165" r="100" fill="none" stroke="oklch(0.72 0.16 200)" stroke-width="3" stroke-linecap="round" stroke-dasharray="52 576" pathLength="628"/>
      <circle cx="230" cy="165" r="55" fill="url(#agGlow)" class="ag-core-glow"/>
      <!-- orkestrointipulssit agentista oikean reunan työkaluille -->
      <path class="ag-pulse ag-pulse-saa" d="M230 165 L405 53" stroke="oklch(0.72 0.16 200)" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-dasharray="22 760"/>
      <path class="ag-pulse ag-pulse-kal" d="M230 165 L405 165" stroke="oklch(0.7 0.16 305)" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-dasharray="22 760"/>
    </svg>
    <div class="ag-core"><span class="ag-core-dot"></span><span class="ag-core-l">AI&nbsp;Agent</span></div>
    <div class="ag-think">
      <span class="th t1">"Tarvitsen sääennusteen"</span><span class="th t2">"Käytän sää-APIa"</span><span class="th t3">"Sää: +16 °C, sade 80 %"</span><span class="th t4">"Tarkistan kalenterin"</span><span class="th t5">"Tapaaminen klo 9"</span><span class="th t6">"Muodostan vastauksen"</span>
    </div>
    <!-- ReAct-vaiheet kehällä (keskialue, x 32-68%) -->
    <div class="ag-ph ph-aj">AJATTELE</div>
    <div class="ag-ph ph-to">TOIMI</div>
    <div class="ag-ph ph-ha">HAVAINNOI</div>
    <!-- 6 työkalua kahdessa sivupylväässä (eivät mene vaiheiden päälle) -->
    <div class="ag-tool tl-saa"><span class="ag-ico">🌦️</span>Sää-API</div>
    <div class="ag-tool tl-kal"><span class="ag-ico">📅</span>Kalenteri</div>
    <div class="ag-tool tl-sah"><span class="ag-ico">📧</span>Sähköposti</div>
    <div class="ag-tool tl-doc"><span class="ag-ico">📄</span>Dokumentit</div>
    <div class="ag-tool tl-net"><span class="ag-ico">🌐</span>Verkkohaku</div>
    <div class="ag-tool tl-db"><span class="ag-ico">🗄️</span>Tietokanta</div>
  </div>
  <div class="ag-out"><span class="ag-out-k">Vastaus:</span> "Kyllä, mutta ota sadevarusteet mukaan."</div>
</div>
<figcaption class="ai-demo__cap">Tekoälyagentti ratkaisee tehtävän silmukassa: se ajattelee ja suunnittelee, käyttää työkalua, havainnoi tuloksen ja päättää seuraavan toimen — ja toistaa, kunnes vastaus on valmis. Tässä se hakee sään ja kalenterin ennen vastausta.</figcaption></figure>
<style>
.ag-scn,.ag-out{font-family:var(--font-mono);font-size:12.5px;color:#EAEEF8;background:#11182A;border:1.5px solid #2A3656;border-radius:9px;padding:8px 13px;max-width:94%;text-align:center}
.ag-scn-k{color:oklch(0.72 0.16 200)}.ag-out{border-color:oklch(0.55 0.14 200)}.ag-out-k{color:#7FD0A8}
.ag-out{opacity:0;animation:agOut 12s ease-out infinite}
@keyframes agOut{0%,82%{opacity:.25}90%,100%{opacity:1}}
.ag-stage{position:relative;width:100%;max-width:460px;height:330px;flex:none}
.ag-svg{position:absolute;inset:0;width:100%;height:100%}
.ag-ring{transform-box:view-box;transform-origin:230px 165px;animation:agSpin 26s linear infinite}
@keyframes agSpin{to{transform:rotate(360deg)}}
.ag-arc{transform-box:view-box;transform-origin:230px 165px;animation:agSpin 12s linear infinite;filter:drop-shadow(0 0 4px oklch(0.72 0.16 200))}
.ag-core-glow{animation:agPulse 3s ease-in-out infinite}
@keyframes agPulse{0%,100%{opacity:.5}50%{opacity:.9}}
.ag-pulse{opacity:0}
.ag-pulse-saa{animation:agPulseSaa 12s linear infinite}.ag-pulse-kal{animation:agPulseKal 12s linear infinite}
@keyframes agPulseSaa{0%,16%{opacity:0;stroke-dashoffset:22}18%{opacity:1}30%{opacity:1;stroke-dashoffset:-400}33%,100%{opacity:0;stroke-dashoffset:-400}}
@keyframes agPulseKal{0%,50%{opacity:0;stroke-dashoffset:22}52%{opacity:1}64%{opacity:1;stroke-dashoffset:-400}67%,100%{opacity:0;stroke-dashoffset:-400}}
.ag-core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:92px;height:92px;border-radius:50%;background:radial-gradient(circle at 50% 38%,oklch(0.42 0.13 275),oklch(0.28 0.1 270));border:1.5px solid oklch(0.66 0.16 270);box-shadow:0 0 22px oklch(0.55 0.16 270 / .55),inset 0 0 18px oklch(0.7 0.16 264 / .35);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px}
.ag-core-dot{width:13px;height:13px;border-radius:50%;background:oklch(0.82 0.15 200);box-shadow:0 0 12px oklch(0.8 0.16 200);animation:agCore 2.4s ease-in-out infinite}
@keyframes agCore{0%,100%{transform:scale(1);opacity:.85}50%{transform:scale(1.25);opacity:1}}
.ag-core-l{font-family:var(--font-mono);font-size:11px;letter-spacing:.06em;color:#EAF2FF;text-shadow:0 0 6px oklch(0.7 0.16 264)}
.ag-think{position:absolute;left:50%;top:30%;transform:translateX(-50%);width:230px;text-align:center}
.ag-think .th{position:absolute;left:50%;top:0;transform:translateX(-50%);white-space:nowrap;font-family:var(--font-mono);font-size:12px;color:#CFE3FF;background:rgba(20,28,48,.9);border:1px solid oklch(0.6 0.14 270);border-radius:999px;padding:4px 11px;opacity:0}
.t1{animation:agTh 12s ease-in-out infinite}.t2{animation:agTh 12s ease-in-out infinite;animation-delay:2s}.t3{animation:agTh 12s ease-in-out infinite;animation-delay:4s}.t4{animation:agTh 12s ease-in-out infinite;animation-delay:6s}.t5{animation:agTh 12s ease-in-out infinite;animation-delay:8s}.t6{animation:agTh 12s ease-in-out infinite;animation-delay:10s}
@keyframes agTh{0%{opacity:0}3%{opacity:1}14%{opacity:1}17%{opacity:0}100%{opacity:0}}
.ag-ph{position:absolute;transform:translate(-50%,-50%);font-family:var(--font-mono);font-size:11px;letter-spacing:.1em;color:#8FA0C8;background:#0E1626;border:1.5px solid #2A3656;border-radius:7px;padding:5px 9px;white-space:nowrap}
.ph-aj{left:50%;top:13%}.ph-to{left:68%;top:77%}.ph-ha{left:32%;top:77%}
.ph-aj{animation:agAj 12s ease-in-out infinite}.ph-to{animation:agTo 12s ease-in-out infinite}.ph-ha{animation:agHa 12s ease-in-out infinite}
@keyframes agAj{0%,16%,50%,66%,90%,100%{color:oklch(0.82 0.14 264);border-color:oklch(0.7 0.15 264);box-shadow:0 0 12px oklch(0.6 0.15 264 / .5)}17%,49%,67%,89%{color:#8FA0C8;border-color:#2A3656;box-shadow:none}}
@keyframes agTo{16%,33%,50%,64%{color:oklch(0.82 0.14 305);border-color:oklch(0.7 0.15 305);box-shadow:0 0 12px oklch(0.6 0.15 305 / .5)}0%,15%,34%,49%,65%,100%{color:#8FA0C8;border-color:#2A3656;box-shadow:none}}
@keyframes agHa{30%,49%,64%,82%{color:oklch(0.82 0.13 200);border-color:oklch(0.7 0.14 200);box-shadow:0 0 12px oklch(0.6 0.14 200 / .5)}0%,29%,50%,63%,83%,100%{color:#8FA0C8;border-color:#2A3656;box-shadow:none}}
.ag-tool{position:absolute;transform:translate(-50%,-50%);display:flex;align-items:center;gap:5px;font-family:var(--font-mono);font-size:10.5px;color:#B9C2DA;background:#11182A;border:1.5px solid #2A3656;border-radius:999px;padding:4px 9px;white-space:nowrap}
.ag-ico{font-size:13px;line-height:1}
.tl-saa{left:87%;top:14%}.tl-kal{left:87%;top:50%}.tl-sah{left:87%;top:86%}
.tl-doc{left:13%;top:14%}.tl-net{left:13%;top:50%}.tl-db{left:13%;top:86%}
.tl-saa{animation:agTSaa 12s ease-in-out infinite}.tl-kal{animation:agTKal 12s ease-in-out infinite}
@keyframes agTSaa{0%,17%{color:#B9C2DA;border-color:#2A3656}20%,32%{color:#06212A;background:oklch(0.78 0.14 200);border-color:transparent;box-shadow:0 0 14px oklch(0.7 0.15 200 / .7)}36%,100%{color:#B9C2DA;background:#11182A;border-color:#2A3656;box-shadow:none}}
@keyframes agTKal{0%,51%{color:#B9C2DA;border-color:#2A3656}54%,66%{color:#06212A;background:oklch(0.76 0.15 305);border-color:transparent;box-shadow:0 0 14px oklch(0.7 0.16 305 / .7)}70%,100%{color:#B9C2DA;background:#11182A;border-color:#2A3656;box-shadow:none}}
@media (prefers-reduced-motion:reduce){.ag-ring,.ag-arc,.ag-core-glow,.ag-core-dot,.ag-pulse,.th,.ag-ph,.ag-tool,.ag-out{animation:none}.t1{opacity:1}.ag-out{opacity:1}}
</style>

## Ketjuajattelu: jaa ongelma osiin

**Ketjuajattelussa** eli chain-of-thought-mallissa agentti purkaa monimutkaisen ongelman pienempiin osiin ja käsittelee ne järjestyksessä. Se etenee vaiheittain: ensin tämä, sitten tuo ja lopuksi seuraava askel.

Esimerkiksi agentti saa tehtävän: ”Käsittele palautuspyyntö.” Agentti ei yritä ratkaista kaikkea yhdellä kertaa, vaan purkaa ongelman vaiheisiin:

1. **Mikä on asiakkaan ongelma?** Tilauksesta puuttuu kolme tuotetta.
2. **Onko palautusaika voimassa?** Tilaus tehtiin 5 päivää sitten, ja palautusaika on 14 päivää. Palautusaika on siis voimassa.
3. **Mitä palautus vaatii?** Asiakkaalle täytyy toimittaa palautuslomake ja kuljetusohjeet.
4. **Onko asiakas oikeutettu hyvitykseen vai korvaavaan tuotteeseen?** Yrityksen palautuskäytännön mukaan ensimmäisestä palautuksesta voidaan antaa hyvitys.
5. **Mitä asiakkaalle lähetetään?** Asiakkaalle lähetetään viesti, jossa selitetään prosessi ja annetaan linkit palautuslomakkeeseen sekä kuljetusohjeisiin.

Ketjuajattelu auttaa agenttia **välttämään virheitä**, koska se pakottaa käsittelemään yhden asian kerrallaan. Agentti ei yritä ratkaista kaikkea yhdellä hypyllä, vaan etenee systemaattisesti. Tämä tekee päätöksenteosta myös **jäljitettävämpää**: ihminen voi nähdä jokaisen vaiheen ja ymmärtää, miksi agentti toimi niin kuin toimi.

Vertaa seuraavia kahta tapaa toimia:

**Ilman ketjuajattelua:** Agentti näkee palautuspyynnön ja hyppää suoraan vastaukseen: ”Lähetän hyvityksen.” Mutta mitä jos palautusaika on jo kulunut? Entä jos käytäntö sanoo, että asiakkaalle pitää lähettää korvaava tuote hyvityksen sijaan? Agentti voi tehdä väärän päätöksen, koska se ei tarkistanut asiaa vaihe vaiheelta.

**Ketjuajattelun kanssa:** Agentti tarkistaa palautusajan, palautuskäytännön ja tuotteet ennen päätöksen tekemistä. Vasta tämän jälkeen se laatii vastauksen. Näin virheiden määrä vähenee.

## Moniagenttijärjestelmät: kun yksi agentti ei riitä

Tähän asti olemme puhuneet yksittäisestä agentista. Monimutkaisissa tehtävissä yksi agentti ei kuitenkaan aina riitä. Silloin voidaan rakentaa **moniagenttijärjestelmä**, jossa useat erikoistuneet agentit tekevät yhteistyötä.

Ajattele yritystä. Yksi ihminen ei yleensä hoida kaikkea. On myyjä, joka ymmärtää asiakkaat, kirjanpitäjä, joka hallitsee rahaa, varastotyöntekijä, joka hoitaa logistiikkaa, ja johtaja, joka koordinoi kokonaisuutta. Jokainen on erikoistunut omaan alueeseensa. Moniagenttijärjestelmä toimii samalla periaatteella: jokaisella agentilla on oma erikoisalansa.

Kuvittele asiakaspalvelun moniagenttijärjestelmä:

- **Analyysiagentti** lukee asiakkaan viestin ja päättelee: ”Asiakas on tyytymätön kuljetuspalveluun.”
- **Tiedonhakuagentti** hakee asiakkaan historian: ”Tämä asiakas on ostanut meiltä viisi kertaa. Hän on lojaali asiakas ja ollut aiemmin tyytymätön kuljetuspalveluihin.”
- **Kirjoitusagentti** laatii vastauksen: ”Pahoittelemme kuljetusongelmaa. Tarjoamme sinulle maksuttoman kotiinkuljetuksen seuraavaan tilaukseen.”
- **Validointiagentti** tarkistaa vastauksen: ”Vastaus on turvallinen. Se ei sisällä salassa pidettäviä tietoja.”

Moniagenttijärjestelmässä on kaksi perusrakennetta.

**Hierarkkinen malli:** Yksi agentti toimii johtajana ja jakaa tehtäviä muille. Johtaja-agentti näkee kokonaistehtävän ja päättää: ”Tämä tehtävä vaatii tietokantahaun, joten lähetän sen hakuagentille. Kun hakuagentti on valmis, lähetän tuloksen kirjoittaja-agentille.” Johtaja toimii kuin orkesterin kapellimestari: se koordinoi kokonaisuutta, ja muut agentit tekevät erikoistuneet osatehtävänsä.

**Hierarkkinen moniagenttijärjestelmä**

|  |  |  |
| --- | --- | --- |
| **Orkestroija** jakaa tehtävät ja kokoaa tulokset | | |
| ↓ | | |
| **Tutkija-agentti** hakee tietoa | **Kirjoittaja-agentti** tuottaa tekstin | **Tarkistaja-agentti** validioi tulokset |
| ↓ | | |
| **Tulokset palaavat orkestroijalle** | | |

**Yhteistyömalli:** Agentit keskustelevat keskenään ilman yhtä johtajaa. Ensimmäinen agentti aloittaa, toinen vastaanottaa tiedon ja tekee seuraavan vaiheen, kolmas tarkistaa ja neljäs antaa palautetta. Agentit vaihtavat tietoa keskenään ja tekevät päätöksiä yhdessä.

Moniagenttijärjestelmät ovat voimakkaita, koska niiden avulla monimutkainen työ voidaan jakaa osiin. Jokainen agentti tekee sitä, mitä se osaa parhaiten. Ne ovat kuitenkin myös monimutkaisia. Mitä enemmän agentteja on, sitä vaikeampaa on ymmärtää, mitä järjestelmässä tapahtuu. Agentti A kertoo jotain agentille B, agentti B tekee päätöksen ja lähettää tiedon agentille C, ja agentin C toiminta voi vaikuttaa agentti A:n seuraaviin päätöksiin. Siksi **lokitus ja seuranta** ovat erityisen tärkeitä, kun agentteja on useita.

> **Pysähdy hetkeksi:** Ajattele todellista, monimutkaista tehtävää, kuten asiakkaan uuden tilauksen käsittelyä. Siihen voi kuulua validointi, maksu, varasto, kuljetus ja asiakaspalvelu. Miten jakaisit tehtävän useamman erikoistuneen agentin kesken? Mikä agentti olisi johtaja? Mitä tietoa agentit vaihtaisivat keskenään?

## Suunnittelumallien valinta: milloin käytät mitä?

Sinulla on nyt kolme välinettä: **ReAct**, **ketjuajattelu** ja **moniagenttijärjestelmät**. Seuraavaksi pitää ymmärtää, milloin mitäkin kannattaa käyttää.

**ReActia käytetään**, kun agentti tarvitsee joustavuutta. Agentti voi ajatella, toimia, nähdä tuloksen ja muuttaa suuntaansa, jos tulos on odottamaton. ReAct sopii hyvin **tutkivaan ajatteluun**: tilanteisiin, joissa agentti ei tiedä tarkasti, mitä seuraavaksi tapahtuu, vaan sen täytyy edetä vaihe kerrallaan havaintojen perusteella.

**Ketjuajattelua käytetään**, kun ongelma voidaan **jakaa selkeisiin vaiheisiin**. Palautuspyynnön käsittely on hyvä esimerkki. Vaiheet ovat usein samat: tarkista palautusaika, tarkista palautuskäytäntö ja laadi vastaus. Ketjuajattelu pakottaa agentin käymään läpi jokaisen vaiheen, mikä vähentää virheitä.

**Moniagenttijärjestelmiä käytetään**, kun tehtävä on **niin monimutkainen, että se vaatii eri erikoisaloja**. Asiakaspalvelupyynnön käsittely voi vaatia analyysiä, tiedonhakua, kirjoittamista ja validointia. Tällöin jokainen osatehtävä voidaan antaa siihen erikoistuneelle agentille.

Käytännössä käytät usein **yhdistelmää**. Esimerkiksi moniagenttijärjestelmässä jokainen erikoistunut agentti voi käyttää ReAct-mallia omalla alueellaan, ja johtaja-agentti voi käyttää ketjuajattelua koko prosessin koordinoimiseen. Mallit eivät siis sulje toisiaan pois, vaan ne täydentävät toisiaan.

## Esimerkki käytännössä: tapahtumatiimi moniagenttijärjestelmänä

Kuvittele tapahtuman suunnittelutiimin työtä ja sitä, miten se muistuttaa moniagenttijärjestelmää.

**Tiimin jäsen 1 eli suunnittelija** lukee vaatimukset: ”Tilaisuuteen tarvitaan ohjelma, tarjoilu ja tila 80 hengelle.”

**Tiimin jäsen 2 eli toteuttaja** tekee ehdotuksen: ”Varaan salin, tilaan pitopalvelun ja kokoan kahden tunnin ohjelman.”

**Tiimin jäsen 3 eli tarkistaja** käy ehdotuksen läpi: ”Kävin läpi 10 yksityiskohtaa, ja 9 on kunnossa — tarjoilun erityisruokavaliot puuttuvat.”

**Tiimin jäsen 4 eli vastuuhenkilö** näkee tilanteen: ”Tarkistus löysi puutteen. Lähetän tehtävän takaisin toteuttajalle.”

**Toteuttaja** täydentää suunnitelman.

**Tarkistaja** käy sen läpi uudelleen: ”Nyt kaikki 10 yksityiskohtaa ovat kunnossa.”

**Vastuuhenkilö** tekee päätöksen: ”Valmis. Julkaistaan kutsu.”

Tämä on moniagenttijärjestelmä käytännössä. Jokainen osa tekee oman erikoistuneen tehtävänsä, vastuuhenkilö koordinoi kokonaisuutta ja lopputulos on parempi kuin yhden toimijan yksin tekemänä.

## Suunnittelumallit n8n:ssä — miltä ne näyttävät käytännössä?

Kun rakennat agenttia n8n:ssä, on hyödyllistä ymmärtää, miten nämä abstraktit mallit muuttuvat konkreettisiksi työnkuluiksi.

**ReAct n8n:ssä:** AI Agent -solmu, jolla on pääsy useisiin työkaluihin. n8n:n AI Agent -solmu toimii usein ReAct-periaatteen mukaisesti: se päättelee, valitsee työkalun, saa tuloksen, päättelee uudelleen ja valitsee tarvittaessa seuraavan työkalun. Sinun ei tarvitse rakentaa koko silmukkaa käsin, koska suuri osa tästä toiminnasta on sisäänrakennettu AI Agent -solmuun.

**ReAct n8n:ssä**

|  |  |  |
| --- | --- | --- |
| **Trigger** | → | **AI Agent** ReAct-silmukka sisäänrakennettuna |
| ↓ | | |
| **Hakutyökalu** | **Tietokanta** | **Sähköposti** |
| ↓ | | |
| **Vastaus käyttäjälle** | | |

**Ketjuajattelu n8n:ssä:** sarja erillisiä solmuja, joista jokainen tekee yhden vaiheen. Edellisen solmun tulos siirtyy seuraavalle solmulle. Tämä on n8n:n luonnollinen rakenne: solmut muodostavat ketjun.

**Ketjuajattelu n8n:ssä**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Pyyntö** | → | **Vaihe 1** Analysoi pyyntö | → | **Vaihe 2** Tarkista käytäntö | → | **Vaihe 3** Laadi vastaus | → | **Lähetä** |

**Moniagentti n8n:ssä:** useita erillisiä työnkulkuja, jotka kutsuvat toisiaan. Johtaja-työnkulku voi lähettää webhookin tutkija-työnkululle, saada tuloksen takaisin ja lähettää sen edelleen kirjoittaja-työnkululle. Tämä on monimutkaisin rakenne, mutta se voi olla tehokas monimutkaisissa tehtävissä.

Kun avaat n8n:n ensimmäistä kertaa, palaa tähän kappaleeseen. Se auttaa sinua valitsemaan projektiisi sopivan rakenteen.

## Kohti omaa projektia

Nyt kun tunnet ReAct-mallin, ketjuajattelun ja moniagenttijärjestelmät, valitse omalle agentillesi sopivin päättelymalli. Mieti ongelmasi luonnetta: tarvitseeko agenttisi reagoida reaaliaikaisesti työkalujen palautteeseen eli käyttää ReAct-mallia, vai voiko ongelman jakaa selkeisiin vaiheisiin eli käyttää ketjuajattelua? Tämä valinta muodostaa **Agentti: Päättely** -pohjapiirroksen, jonka kirjoitat opiskelutehtävissä.

## Yhteenveto

Agentti toimii paremmin, kun se ajattelee **järjestelmällisesti**. **ReAct-malli** auttaa agenttia ajattelemaan, toimimaan ja ajattelemaan uudelleen joustavasti. **Ketjuajattelu** auttaa sitä purkamaan ongelman vaiheisiin ja käsittelemään ne järjestyksessä. **Moniagenttijärjestelmät** antavat mahdollisuuden jakaa työn useille erikoistuneille agenteille.

Nämä mallit perustuvat siihen, miten ihmiset ajattelevat ja työskentelevät monimutkaisissa tilanteissa. Kun rakennat agenttia n8n:llä, sinä valitset, mitä mallia agentti noudattaa. Valinta vaikuttaa siihen, onko agentti tehokas vai tehoton, ymmärrettävä vai sekava. Valitse aina malli, joka sopii tehtävän luonteeseen.

---
