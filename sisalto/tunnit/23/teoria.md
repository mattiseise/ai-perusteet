# Suunnittelumallit — ReAct ja eksplisiittinen työnkulku

## Johdanto

Nyt tiedät, mistä agentti koostuu: muistista, työkaluista ja identiteetistä. Seuraava kysymys on, miten suunnittelet agentin **havaittavan toiminnan järkeväksi ja testattavaksi**. Miten varmistat, että se etenee oikeassa järjestyksessä eikä hyppää sattumanvaraisesti vääriin toimintoihin?

Vastaus on **suunnittelumallit**. Ne ovat testattuja tapoja järjestää työkalujen käyttö, tulosten tarkistus, päätökset ja toiminnot. Mallin sisäistä päättelyä ei pyydetä eikä tallenneta. Sen sijaan näkyviin tehdään lyhyt päätösperustelu, työkalun käyttö, tulos tai virhe sekä toteutettu toiminto.

Projektissasi valitset kahdesta perusmallista: käyttääkö agenttisi **ReAct-mallia** vai **eksplisiittistä työnkulkua**. Moniagenttijärjestelmät käsitellään myöhemmin valinnaisena syvennyksenä, eikä niitä tarvita lopputyössä.

> **Kytkentä agentin ohjauskehykseen:** ReAct ja eksplisiittinen työnkulku ovat tapoja, joilla agentin ohjauskehys ohjaa agentin havaittavaa toimintaa. Agentin ohjauskehys hallitsee kierrosta, välittää työkalukutsut ja tulokset, asettaa iteraatiorajan, käsittelee virheet ja lokittaa tapahtumat. Kielimalli valitsee seuraavaa sisältöä tai toimintoa näiden rajojen sisällä.

## ReAct: valitse toiminto, havainnoi tulos ja jatka

**ReAct** tarkoittaa sanoja **Reasoning + Acting** eli päättely ja toiminta. Toteutuksessa agentti valitsee työkalun, saa havainnon ja valitsee sen perusteella seuraavan toiminnon. Valinnasta voidaan kirjata lyhyt päätösperustelu, mutta mallin piilotettua sisäistä päättelyä ei paljasteta lokiin.

Käytännössä agentti saa tehtävän: ”Asiakas kysyy, onko tuotetta saatavilla.” Toteutus kirjaa lyhyen päätösperustelun: ”Saatavuus vaatii ajantasaisen varastohaun.” Sen jälkeen agentti kutsuu varastorajapintaa. Lokissa ei tarvita mallin raakaa, piilotettua ajatusketjua.

Seuraavaksi tulee **toiminta**: agentti kutsuu varasto-API:a ja saa vastauksen: ”Tuotetta on 5 kappaletta.”

Sitten toteutus tarkistaa tuloksen ja kirjaa lyhyesti: ”Haku onnistui; vastaus voidaan muodostaa palautetusta määrästä.” Käyttäjä saa tarvittaessa tiiviin perustelun, mutta mallin sisäinen päättely jää piiloon.

Lopuksi agentti tekee **toisen toiminnon** ja kirjoittaa asiakkaalle vastauksen: ”Kyllä, tuotetta on 5 kappaletta varastossa. Voit tehdä tilauksen nyt.” Työkalukutsu, havainto ja seuraava toiminto vuorottelevat, kunnes tehtävä on valmis tai enimmäisraja täyttyy.

ReAct on hyödyllinen, kun seuraava toiminto riippuu työkalun palauttamasta tuloksesta. Jäljitettävyyttä ei rakenneta tallentamalla raakaa ajatusketjua, vaan kirjaamalla rakenteiset kutsut, tulokset, virheet, toiminnot ja lyhyet päätösperustelut.

**ReAct-mallin eteneminen**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tehtävä saapuu** | → | **Päätösperustelu** Mitä tietoa tarvitaan seuraavaksi? | → | **Työkalukutsu** Käytä rakenteista syötettä. |
| ↓ | | | | |
| **Vastaa käyttäjälle** | ← | **Seuraava toiminto** Vastaa, jatka tai eskaloi. | ← | **Tulos tai virhe** Mitä työkalu palautti? |

Kun ReAct-mallin toimintaa lokitetaan, havaittava työnkulku näkyy selvästi:

**[PÄÄTÖSPERUSTELU]** Ajantasainen hinta vaatii tuotehaun.

**[TOIMINTA]** GET /api/product?id=12345 → Hinta: 45 €

**[TULOS]** Tuotehaku onnistui; palautettu hinta on 45 euroa.

**[TOIMINTA]** Lähetä vastaus: ”Tuotteen hinta on 45 €.”

Lokista näkyvät työkalujen käytöt, niille annetut syötteet, tulokset, toiminnot, virheet ja lyhyet päätösperustelut. Se ei tallenna mallin sisäistä päättelyä eikä tarpeettomia salaisuuksia tai henkilötietoja.

> **Pysähdy hetkeksi:** Ajattele omaa ratkaisuprosessiasi. Kun ratkaiset ongelmaa, ajatteletko ensin, toimitko sen jälkeen ja arvioitko sitten tuloksen perusteella? Vai hyppäätkö suoraan toimintaan? Miten ReAct-malli voisi auttaa sinua tekemään parempia päätöksiä?

<figure class="ai-demo"><span class="ai-demo__tag">// päätösperustelu → työkalukutsu → tulos → seuraava toiminto</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:310px">
  <div class="l23-wrap" data-once>
    <div class="l23-ring"><span class="l23-mid">ReAct</span></div>
    <span class="l23-node n-think">PERUSTELE LYHYESTI</span>
    <span class="l23-node n-act">TOIMI</span>
    <span class="l23-node n-obs">HAVAINNOI</span>
    <span class="l23-exit">✓ VALMIS</span>
    <div class="l23-log"><span class="l23-lh">LOKI — jokainen vaihe jää näkyviin</span>
      <span class="l23-l t1"><b>[PÄÄTÖSPERUSTELU]</b> Tarvitsen ensin säätiedon.</span>
      <span class="l23-l a1"><b>[TOIMINTA]</b> hae_saa("Turku")</span>
      <span class="l23-l o1"><b>[HAVAINTO]</b> +2 °C, sadetta 80 %</span>
      <span class="l23-l t2"><b>[PÄÄTÖSPERUSTELU]</b> Vielä vapaa aika kalenterista.</span>
      <span class="l23-l a2"><b>[TOIMINTA]</b> hae_kalenteri(huomenna)</span>
      <span class="l23-l o2"><b>[HAVAINTO]</b> klo 14 vapaa</span>
      <span class="l23-l done"><b>[VALMIS ✓]</b> Ehdotan: huomenna klo 14 sisällä.</span>
    </div>
  </div>
</div>
<figcaption class="ai-demo__cap">ReAct-toteutus etenee havaintojen perusteella. Loki näyttää lyhyen päätösperustelun, rakenteisen työkalukutsun, tuloksen tai virheen ja seuraavan toiminnon — ei mallin piilotettua raakaa ajatusketjua.</figcaption></figure>
<style>
.l23-wrap{position:relative;width:560px;height:272px;font-family:var(--font-mono);animation:l23wrapw 21s 1 forwards}
.l23-ring{position:absolute;left:28px;top:62px;width:128px;height:128px;border:2.5px dashed #44517A;border-radius:50%;animation:l23spin 21s linear infinite}
@keyframes l23spin{from{transform:rotate(0)}to{transform:rotate(360deg)}}
.l23-mid{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-size:12.5px;font-weight:700;letter-spacing:.08em;color:#EAEEF8;animation:l23unspin 21s linear infinite}
@keyframes l23unspin{from{transform:translate(-50%,-50%) rotate(0)}to{transform:translate(-50%,-50%) rotate(-360deg)}}
.l23-node{position:absolute;font-size:10.5px;letter-spacing:.09em;color:#B9C2DA;background:#11182A;border:2px solid #2B3552;border-radius:999px;padding:5px 11px;z-index:2}
.l23-node.n-think{left:54px;top:42px;animation:l23think 21s infinite}
.l23-node.n-act{left:128px;top:158px;animation:l23act 21s infinite}
.l23-node.n-obs{left:-6px;top:158px;animation:l23obs 21s infinite}
@keyframes l23think{0%,2%,14%,38%,50%,100%{color:#B9C2DA;background:#11182A;border-color:#2B3552;box-shadow:none}4%,12%,40%,48%{color:#0B0F1A;background:#46c7cf;border-color:#46c7cf;box-shadow:0 0 14px rgba(70,199,207,.6)}}
@keyframes l23act{0%,14%,26%,50%,62%,100%{color:#B9C2DA;background:#11182A;border-color:#2B3552;box-shadow:none}16%,24%,52%,60%{color:#1d1230;background:#c9b7f1;border-color:#c9b7f1;box-shadow:0 0 14px rgba(201,183,241,.6)}}
@keyframes l23obs{0%,26%,38%,62%,74%,100%{color:#B9C2DA;background:#11182A;border-color:#2B3552;box-shadow:none}28%,36%,64%,72%{color:#0B0F1A;background:#F7C873;border-color:#F7C873;box-shadow:0 0 14px rgba(247,200,115,.6)}}
.l23-exit{position:absolute;left:48px;top:228px;font-size:11px;letter-spacing:.08em;color:#06241f;background:#7FD0A8;border-radius:999px;padding:4px 12px;opacity:0;animation:l23exit 21s infinite}
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
.l23-l.t1{animation:l23l1 21s infinite}
.l23-l.a1{animation:l23l2 21s infinite}
.l23-l.o1{animation:l23l3 21s infinite}
.l23-l.t2{animation:l23l4 21s infinite}
.l23-l.a2{animation:l23l5 21s infinite}
.l23-l.o2{animation:l23l6 21s infinite}
.l23-l.done{animation:l23l7 21s infinite}
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
@keyframes l23wrapw{0%,100%{opacity:1}}
</style>

## Eksplisiittinen työnkulku: jaa ongelma näkyviin vaiheisiin

**Eksplisiittisessä työnkulussa** toteuttaja purkaa ongelman näkyviin, testattaviin vaiheisiin. Tämä on eri asia kuin mallin piilotettu sisäinen päättely. Työnkulku voidaan tarkistaa ja lokittaa ilman, että raakaa ajatusketjua pyydetään tai tallennetaan. Kurssin agenttiprojektissa myös eksplisiittiseen työnkulkuun kuuluu vähintään yksi nimetty vaihe, jossa kielimalli tekee aidon rajatun valinnan vähintään kahdesta ohjauskehyksen sallimasta vaihtoehdosta. Vaiheet ja sallitut haarat ovat ennalta määriteltyjä, mutta mallin valitsema haara riippuu syötteestä.

Esimerkiksi agentti saa tehtävän: ”Käsittele palautuspyyntö.” Agentti ei yritä ratkaista kaikkea yhdellä kertaa, vaan purkaa ongelman vaiheisiin:

1. **Mikä on asiakkaan ongelma?** Tilauksesta puuttuu kolme tuotetta.
2. **Onko palautusaika voimassa?** Tilaus tehtiin 5 päivää sitten, ja palautusaika on 14 päivää. Palautusaika on siis voimassa.
3. **Mitä palautus vaatii?** Asiakkaalle täytyy toimittaa palautuslomake ja kuljetusohjeet.
4. **Onko asiakas oikeutettu hyvitykseen vai korvaavaan tuotteeseen?** Yrityksen palautuskäytännön mukaan ensimmäisestä palautuksesta voidaan antaa hyvitys.
5. **Mitä asiakkaalle lähetetään?** Asiakkaalle lähetetään viesti, jossa selitetään prosessi ja annetaan linkit palautuslomakkeeseen sekä kuljetusohjeisiin.

Eksplisiittinen työnkulku auttaa agenttia **välttämään virheitä**, koska se pakottaa käsittelemään yhden asian kerrallaan. Agentti ei yritä ratkaista kaikkea yhdellä hypyllä, vaan etenee systemaattisesti. Tämä tekee päätöksenteosta myös **jäljitettävämpää**: ihminen voi nähdä jokaisen vaiheen ja ymmärtää, miksi agentti toimi niin kuin toimi.

Vertaa seuraavia kahta tapaa toimia:

**Ilman eksplisiittistä työnkulkua:** Agentti näkee palautuspyynnön ja hyppää suoraan vastaukseen: ”Lähetän hyvityksen.” Mutta mitä jos palautusaika on jo kulunut? Entä jos käytäntö sanoo, että asiakkaalle pitää lähettää korvaava tuote hyvityksen sijaan? Agentti voi tehdä väärän päätöksen, koska se ei tarkistanut asiaa vaihe vaiheelta.

**Eksplisiittisen työnkulun kanssa:** Agentti tarkistaa palautusajan, palautuskäytännön ja tuotteet ennen päätöksen tekemistä. Vasta tämän jälkeen se laatii vastauksen. Näin virheiden määrä vähenee.

> **Valinnainen syvennys — moniagenttijärjestelmä:** Monimutkainen tehtävä voidaan joskus jakaa usealle erikoistuneelle agentille. Tällöin tarvitaan selkeä työnjako, tiedonkulku, lokitus ja vastuu kokonaisuuden kokoamisesta. Rakenne lisää kuitenkin monimutkaisuutta, joten tällä kurssilla aloitat yhdestä agentista. Moniagenttijärjestelmää ei tarvitse suunnitella eikä toteuttaa lopputyössä.

## Suunnittelumallien valinta: milloin käytät mitä?

Projektiasi varten vertaat kahta perusmallia: **ReActia** ja **eksplisiittistä työnkulkua**. Valinta tehdään tehtävän luonteen perusteella.

**ReActia käytetään**, kun agentti tarvitsee joustavuutta. Toteutus voi kutsua työkalua, nähdä tuloksen tai virheen ja muuttaa seuraavaa toimintoa, jos tulos on odottamaton. ReAct sopii tutkiviin tilanteisiin, joissa vaiheita ei tiedetä tarkasti etukäteen, vaan eteneminen määräytyy havaintojen perusteella.

**Eksplisiittistä työnkulkua käytetään**, kun ongelma voidaan **jakaa selkeisiin vaiheisiin**. Palautuspyynnön käsittely on hyvä esimerkki. Vaiheet ovat usein samat: tarkista palautusaika, tarkista palautuskäytäntö ja laadi vastaus. Eksplisiittinen työnkulku pakottaa agentin käymään läpi jokaisen vaiheen, mikä vähentää virheitä.

Lopputyössä valitset yhden näistä kahdesta päämallista, jotta toteutus pysyy ymmärrettävänä ja testattavana. Valintaan kuuluu myös aito rajattu mallivalinta: vähintään yhdessä kohdassa kielimalli valitsee syötteen perusteella vähintään kahdesta ohjauskehyksen sallimasta vaihtoehdosta.

## Suunnittelumallit n8n:ssä — miltä ne näyttävät käytännössä?

Kun rakennat agenttia n8n:ssä, on hyödyllistä ymmärtää, miten nämä abstraktit mallit muuttuvat konkreettisiksi työnkuluiksi.

**ReAct n8n:ssä:** AI Agent -solmu voi valita sille annetun työkalun, saada tuloksen tai virheen ja valita sen perusteella seuraavan toiminnon. Lokiin tallennetaan havaittavat kutsut, tulokset, virheet, toiminnot ja tarvittaessa lyhyt päätösperustelu — ei mallin sisäistä päättelyä. Sinun ei tarvitse ohjelmoida silmukkaa itse.

**ReAct n8n:ssä**

|  |  |  |
| --- | --- | --- |
| **Trigger** | → | **AI Agent** ReAct-silmukka sisäänrakennettuna |
| ↓ | | |
| **Hakutyökalu** | **Tietokanta** | **Sähköposti** |
| ↓ | | |
| **Vastaus käyttäjälle** | | |

**Eksplisiittinen työnkulku n8n:ssä:** sarja erillisiä solmuja, joista jokainen tekee yhden vaiheen. Edellisen solmun tulos siirtyy seuraavalle solmulle. Tämä on n8n:n luonnollinen rakenne: solmut muodostavat ketjun.

**Eksplisiittinen työnkulku n8n:ssä**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Pyyntö** | → | **Vaihe 1** Analysoi pyyntö | → | **Vaihe 2** Tarkista käytäntö | → | **Vaihe 3** Laadi vastaus | → | **Lähetä** |

Kun avaat n8n:n ensimmäistä kertaa, palaa tähän kappaleeseen. Se auttaa sinua valitsemaan projektiisi sopivan rakenteen.

## Kohti omaa projektia

Nyt kun tunnet ReAct-mallin ja eksplisiittisen työnkulun, valitse omalle agentillesi sopivin toimintamalli. Mieti ongelmasi luonnetta: tarvitseeko agenttisi reagoida työkalujen palautteeseen eli käyttää ReAct-mallia, vai voiko ongelman jakaa selkeisiin vaiheisiin eli käyttää eksplisiittistä työnkulkua? Tämä valinta muodostaa **Agentti: Päättely** -pohjapiirroksen, jonka kirjoitat opiskelutehtävissä.

> **Lopuksi pohdittavaksi:** Mikä osa päättelymallista on kielimallin valintaa ja mikä agentin ohjauskehyksen ohjaamaa rakennetta?

## Yhteenveto

Agentti toimii paremmin, kun sen työnkulku on **järjestelmällinen ja havaittava**. **ReAct-malli** etenee rakenteisesta työkalukutsusta tulokseen tai virheeseen ja siitä seuraavaan toimintoon. **Eksplisiittinen työnkulku** purkaa ongelman ennalta nimettyihin vaiheisiin. Kummassakin mallissa etenemisen pitää sisältää aito rajattu mallivalinta eikä pelkkää kiinteää automaatiota.

Kun rakennat agenttia n8n:llä, valitset ReActin tai eksplisiittisen työnkulun tehtävän luonteen perusteella. Tee etenemisestä havaittava kirjaamalla työkalun käyttö, tulos tai virhe, seuraava toiminto ja lyhyt päätösperustelu. Mallin sisäistä päättelyä ei pyydetä eikä tallenneta.

---

## Lähteet ja tarkistuspäivä

- [Anthropic: Building Effective AI Agents](https://resources.anthropic.com/building-effective-ai-agents)
- [Yao ym.: ReAct](https://arxiv.org/abs/2210.03629)

Tarkistettu 15.7.2026.
