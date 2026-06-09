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

<figure class="ai-demo"><span class="ai-demo__tag">// ReAct: jos tieto ei riitä, agentti yrittää uudelleen</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;padding:14px 22px">
  <div class="l23-tbl">
    <div class="l23-head"><span class="h-aj">AJATTELE</span><span class="h-to">TOIMI</span><span class="h-ha">HAVAITSE</span></div>
    <div class="l23-row r1"><span class="c cA"><i>tarvitsen hinnan</i></span><span class="c cB">hae nimellä</span><span class="c cC miss">ei löytynyt ✗</span></div>
    <div class="l23-fb">↻ tieto ei riittänyt — tarvitaan lisää</div>
    <div class="l23-row r2"><span class="c cA"><i>kokeile tuotekoodilla</i></span><span class="c cB">hae koodilla</span><span class="c cC">hinta: 45 €</span></div>
    <div class="l23-row r3"><span class="c cA"><i>tieto riittää</i></span><span class="c cB">vastaa: 45 €</span><span class="c cC done">✓ valmis</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">ReAct on palautesilmukka: agentti ajattelee, toimii ja havaitsee tuloksen. Jos tieto ei riitä — esimerkiksi haku ei tuota tulosta — se päättelee uuden tavan ja yrittää uudelleen, kunnes tavoite täyttyy.</figcaption></figure>
<style>
.l23-tbl{display:flex;flex-direction:column;gap:7px;width:100%;max-width:500px}
.l23-head,.l23-row{display:grid;grid-template-columns:1fr 1fr 1fr;gap:9px}
.l23-head span{font-family:var(--font-mono);font-size:12px;letter-spacing:.08em;text-align:center;padding-bottom:4px;border-bottom:2px solid}
.h-aj{color:oklch(0.66 0.15 305);border-color:oklch(0.66 0.15 305)}
.h-to{color:oklch(0.66 0.15 264);border-color:oklch(0.66 0.15 264)}
.h-ha{color:oklch(0.66 0.13 208);border-color:oklch(0.66 0.13 208)}
.l23-row .c{font-family:var(--font-mono);font-size:12.5px;color:#EAEEF8;background:#1E2740;border:1.5px solid #3A4560;border-radius:8px;padding:9px 7px;text-align:center;opacity:0}
.l23-row .c i{color:#B9C2DA;font-style:italic}
.miss{color:#F08A78!important;border-color:#F08A78!important}
.done{color:#7FD0A8!important;border-color:#7FD0A8!important;font-weight:500}
.l23-fb{font-family:var(--font-mono);font-size:11px;color:#F08A78;text-align:center;opacity:0;animation:l23fb 10s ease-out infinite}
@keyframes l23fb{0%,30%{opacity:0}38%,92%{opacity:1}100%{opacity:0}}
.r1 .c{animation:l23r1 10s ease-out infinite}
.r2 .c{animation:l23r2 10s ease-out infinite}
.r3 .c{animation:l23r3 10s ease-out infinite}
.r1 .cA{animation-delay:.6s}.r1 .cB{animation-delay:.9s}.r1 .cC{animation-delay:1.2s}
.r2 .cA{animation-delay:4.0s}.r2 .cB{animation-delay:4.3s}.r2 .cC{animation-delay:4.6s}
.r3 .cA{animation-delay:6.2s}.r3 .cB{animation-delay:6.5s}.r3 .cC{animation-delay:6.8s}
@keyframes l23r1{0%{opacity:0;transform:translateY(6px)}10%,92%{opacity:1;transform:none}100%{opacity:0}}
@keyframes l23r2{0%{opacity:0;transform:translateY(6px)}14%,92%{opacity:1;transform:none}100%{opacity:0}}
@keyframes l23r3{0%{opacity:0;transform:translateY(6px)}18%,92%{opacity:1;transform:none}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){.r1 .c,.r2 .c,.r3 .c,.l23-fb{animation:none;opacity:1!important;transform:none}}
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
