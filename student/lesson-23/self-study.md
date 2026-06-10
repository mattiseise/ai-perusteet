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

<figure class="ai-demo"><span class="ai-demo__tag">// ajattele → toimi → havainnoi — silmukka pyörii, kunnes tehtävä on valmis</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:310px">
  <div class="l23-wrap">
    <div class="l23-ring"><span class="l23-mid">ReAct</span></div>
    <span class="l23-node n-think">AJATTELE</span>
    <span class="l23-node n-act">TOIMI</span>
    <span class="l23-node n-obs">HAVAINNOI</span>
    <span class="l23-exit">✓ VALMIS</span>
    <div class="l23-log"><span class="l23-lh">LOKI — jokainen vaihe jää näkyviin</span>
      <span class="l23-l t1"><b>[AJATTELU]</b> Tarvitsen ensin säätiedon.</span>
      <span class="l23-l a1"><b>[TOIMINTA]</b> hae_saa("Turku")</span>
      <span class="l23-l o1"><b>[HAVAINTO]</b> +2 °C, sadetta 80 %</span>
      <span class="l23-l t2"><b>[AJATTELU]</b> Vielä vapaa aika kalenterista.</span>
      <span class="l23-l a2"><b>[TOIMINTA]</b> hae_kalenteri(huomenna)</span>
      <span class="l23-l o2"><b>[HAVAINTO]</b> klo 14 vapaa</span>
      <span class="l23-l done"><b>[VALMIS ✓]</b> Ehdotan: huomenna klo 14 sisällä.</span>
    </div>
  </div>
</div>
<figcaption class="ai-demo__cap">ReAct-agentti ei toimi sokkona: se perustelee ensin, toimii sitten ja arvioi tuloksen — ja toistaa silmukkaa, kunnes tieto riittää. Loki näyttää jokaisen vaiheen, joten virheen syntykohta on aina jäljitettävissä.</figcaption></figure>
<style>
.l23-wrap{position:relative;width:560px;height:272px;font-family:var(--font-mono)}
.l23-ring{position:absolute;left:28px;top:62px;width:128px;height:128px;border:2.5px dashed #44517A;border-radius:50%;animation:l23spin 14s linear infinite}
@keyframes l23spin{from{transform:rotate(0)}to{transform:rotate(360deg)}}
.l23-mid{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-size:12.5px;font-weight:700;letter-spacing:.08em;color:#EAEEF8;animation:l23unspin 14s linear infinite}
@keyframes l23unspin{from{transform:translate(-50%,-50%) rotate(0)}to{transform:translate(-50%,-50%) rotate(-360deg)}}
.l23-node{position:absolute;font-size:10.5px;letter-spacing:.09em;color:#B9C2DA;background:#11182A;border:2px solid #2B3552;border-radius:999px;padding:5px 11px;z-index:2}
.l23-node.n-think{left:54px;top:42px;animation:l23think 14s infinite}
.l23-node.n-act{left:128px;top:158px;animation:l23act 14s infinite}
.l23-node.n-obs{left:-6px;top:158px;animation:l23obs 14s infinite}
@keyframes l23think{0%,2%,14%,38%,50%,100%{color:#B9C2DA;background:#11182A;border-color:#2B3552;box-shadow:none}4%,12%,40%,48%{color:#0B0F1A;background:#46c7cf;border-color:#46c7cf;box-shadow:0 0 14px rgba(70,199,207,.6)}}
@keyframes l23act{0%,14%,26%,50%,62%,100%{color:#B9C2DA;background:#11182A;border-color:#2B3552;box-shadow:none}16%,24%,52%,60%{color:#1d1230;background:#c9b7f1;border-color:#c9b7f1;box-shadow:0 0 14px rgba(201,183,241,.6)}}
@keyframes l23obs{0%,26%,38%,62%,74%,100%{color:#B9C2DA;background:#11182A;border-color:#2B3552;box-shadow:none}28%,36%,64%,72%{color:#0B0F1A;background:#F7C873;border-color:#F7C873;box-shadow:0 0 14px rgba(247,200,115,.6)}}
.l23-exit{position:absolute;left:48px;top:228px;font-size:11px;letter-spacing:.08em;color:#06241f;background:#7FD0A8;border-radius:999px;padding:4px 12px;opacity:0;animation:l23exit 14s infinite}
@keyframes l23exit{0%,76%{opacity:0;transform:scale(1.25)}81%,97%{opacity:1;transform:scale(1)}100%{opacity:0}}
.l23-log{position:absolute;right:0;top:6px;width:330px;min-height:258px;background:#0E1422;border:1.5px solid #232C44;border-radius:13px;padding:11px 13px}
.l23-lh{display:block;font-size:9.5px;letter-spacing:.1em;color:#7E88A8;margin-bottom:8px;text-transform:uppercase}
.l23-l{display:block;font-size:11px;line-height:1.4;color:#EAEEF8;background:#141B2D;border-left:3px solid #44517A;border-radius:6px;padding:5px 8px;margin-bottom:6px;opacity:0}
.l23-l b{font-weight:700}
.l23-l.t1 b,.l23-l.t2 b{color:#46c7cf}
.l23-l.a1 b,.l23-l.a2 b{color:#c9b7f1}
.l23-l.o1 b,.l23-l.o2 b{color:#F7C873}
.l23-l.done{border-left-color:#7FD0A8}
.l23-l.done b{color:#7FD0A8}
.l23-l.t1{animation:l23l1 14s infinite}
.l23-l.a1{animation:l23l2 14s infinite}
.l23-l.o1{animation:l23l3 14s infinite}
.l23-l.t2{animation:l23l4 14s infinite}
.l23-l.a2{animation:l23l5 14s infinite}
.l23-l.o2{animation:l23l6 14s infinite}
.l23-l.done{animation:l23l7 14s infinite}
@keyframes l23l1{0%,3%{opacity:0;transform:translateX(6px)}6%,96%{opacity:1;transform:translateX(0)}100%{opacity:0}}
@keyframes l23l2{0%,15%{opacity:0;transform:translateX(6px)}18%,96%{opacity:1;transform:translateX(0)}100%{opacity:0}}
@keyframes l23l3{0%,27%{opacity:0;transform:translateX(6px)}30%,96%{opacity:1;transform:translateX(0)}100%{opacity:0}}
@keyframes l23l4{0%,39%{opacity:0;transform:translateX(6px)}42%,96%{opacity:1;transform:translateX(0)}100%{opacity:0}}
@keyframes l23l5{0%,51%{opacity:0;transform:translateX(6px)}54%,96%{opacity:1;transform:translateX(0)}100%{opacity:0}}
@keyframes l23l6{0%,63%{opacity:0;transform:translateX(6px)}66%,96%{opacity:1;transform:translateX(0)}100%{opacity:0}}
@keyframes l23l7{0%,76%{opacity:0;transform:translateX(6px)}81%,96%{opacity:1;transform:translateX(0)}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l23-ring,.l23-mid,.l23-node,.l23-exit,.l23-l{animation:none}
.l23-l,.l23-exit{opacity:1}}
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
