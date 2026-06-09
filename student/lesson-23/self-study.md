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

<figure class="ai-demo"><span class="ai-demo__tag">// ReAct: ajattele → toimi → havaitse</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;padding:0 22px">
  <svg viewBox="0 0 320 200" style="width:100%;max-width:360px;height:190px">
    <circle cx="160" cy="100" r="68" fill="none" stroke="#232C44" stroke-width="1.5" stroke-dasharray="4 7"/>
    <g class="l23-orbit"><circle cx="160" cy="32" r="6" fill="oklch(0.66 0.15 305)"/></g>
    <g font-family="var(--font-mono)">
      <text x="160" y="26" text-anchor="middle" font-size="10" fill="#E6EAF5" class="n1">AJATTELE</text>
      <text x="160" y="40" text-anchor="middle" font-size="8.5" fill="#9aa3bd" class="n1">"tarvitsen hinnan"</text>
      <text x="248" y="150" text-anchor="middle" font-size="10" fill="#E6EAF5" class="n2">TOIMI</text>
      <text x="248" y="163" text-anchor="middle" font-size="8.5" fill="#9aa3bd" class="n2">"hae hinta"</text>
      <text x="72" y="150" text-anchor="middle" font-size="10" fill="#E6EAF5" class="n3">HAVAITSE</text>
      <text x="72" y="163" text-anchor="middle" font-size="8.5" fill="#9aa3bd" class="n3">"29 €"</text>
      <text x="160" y="104" text-anchor="middle" font-size="9" fill="#69728F">toistuu kunnes</text>
      <text x="160" y="116" text-anchor="middle" font-size="9" fill="#69728F">tavoite valmis</text>
    </g>
  </svg>
</div>
<figcaption class="ai-demo__cap">ReAct vuorottelee ajattelua ja toimintaa: agentti päättelee mitä tarvitsee, toimii työkalulla ja havaitsee tuloksen — ja päättelee taas. Toiminta ei ole sokeaa eikä pelkkää puhetta.</figcaption></figure>
<style>
.l23-orbit{transform-box:view-box;transform-origin:160px 100px;animation:l23spin 15s ease-in-out infinite}
@keyframes l23spin{0%,18%{transform:rotate(0deg)}28%,46%{transform:rotate(120deg)}56%,74%{transform:rotate(240deg)}84%,100%{transform:rotate(360deg)}}
.n1{animation:l23n1 15s steps(1) infinite}
.n2{animation:l23n2 15s steps(1) infinite}
.n3{animation:l23n3 15s steps(1) infinite}
@keyframes l23n1{0%,27%{opacity:1}28%,92%{opacity:.35}100%{opacity:1}}
@keyframes l23n2{0%,27%{opacity:.35}28%,55%{opacity:1}56%,100%{opacity:.35}}
@keyframes l23n3{0%,55%{opacity:.35}56%,83%{opacity:1}84%,100%{opacity:.35}}
@media (prefers-reduced-motion:reduce){.l23-orbit,.n1,.n2,.n3{animation:none}.n1,.n2,.n3{opacity:1}}
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
