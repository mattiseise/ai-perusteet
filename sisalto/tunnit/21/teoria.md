# Agentin muisti ja konteksti — miten kone pysyy kartalla?

## Johdanto

Kun rakennat omaa agenttia n8n:llä, voit rakentaa sille järjestelmän, joka säilyttää tehtävän kannalta olennaista tietoa. Kielimalli ei itsessään muista, mitä tapahtui viime viikolla. Agentin harness voi tallentaa tapahtumia, ylläpitää prosessin vaihetta ja hakea asiakkaan historian mallin käyttöön silloin, kun sitä tarvitaan. Tämä **muisti** ja **konteksti** ovat agentin toiminnan kannalta keskeisiä. Ilman niitä agentti olisi helposti toistava, epäjohdonmukainen ja lähes käyttökelvoton.

Yksinkertaisissa boteissa muisti päättyy usein siihen, kun keskustelu loppuu. Agentissa muisti voi kuitenkin jatkua keskustelujen välillä. Tässä oppitunnissa opit, **miten agentti näkee nykyisen tilanteen konteksti-ikkunan avulla, miten se muistaa menneisyyttä pitkäkestoisen muistin avulla ja miten se seuraa prosessin vaiheita tilan avulla**. Nämä kolme tekijää tekevät agentista näennäisesti älykkään. Kun rakennat agenttia n8n:llä, ne ovat myös niitä rakennuspalikoita, joista agentin logiikka syntyy.

> **Harness-kytkentä:** Kielimalli ei kanna muistia mukanaan itsestään. Harness valitsee, mitä mallille annetaan juuri nyt, tallentaa sovitut tiedot ja prosessin tilan sekä hakee pitkäkestoisesta muistista tehtävän kannalta olennaisen tiedon. Samalla sen pitää rajata, mitä ei saa tallentaa.

## Konteksti-ikkuna: mitä agentti näkee juuri nyt?

Kuvittele asiakaspalveluagenttia, joka vastaa asiakkaalle neljänkymmenen aiemman viestin jälkeen kysymykseen: ”Entä mitä ehdotat nyt?” Agentti lukee 40 viestiä ja yrittää muistaa, mistä ongelma alun perin alkoi. Se muistuttaa tilannetta, jossa lukisit 40 sivua kirjaa yhdellä kertaa ja sinulta kysyttäisiin sen jälkeen jotain ensimmäiseltä sivulta. Ihmisen keskittyminen kuormittuu. Samalla tavalla myös agentin käsittelykyky on rajallinen.

**Konteksti-ikkuna** tarkoittaa sitä osaa keskustelusta tai datasta, jonka agentti näkee kerralla. Voit ajatella sitä muistilaatikkona, johon mahtuu vain rajattu määrä viimeisimpiä viestejä. Jos ikkuna sisältää 50 viestiä ja keskusteluun tulee 51. viesti, vanhin viesti voi poistua agentin näkyvistä. Tämä rajaaminen on **tarkoituksellista suunnittelua**, ei pelkkä puute. Kaikilla järjestelmillä on rajat prosessointikyvyssä, nopeudessa ja kustannuksissa.

Käytännössä konteksti-ikkunan koko on kompromissi. Mitä suurempi ikkuna on, sitä enemmän agentti näkee aiempaa keskustelua ja sitä paremmin se voi ymmärtää tilanteen. Suurempi ikkuna tarkoittaa kuitenkin myös **enemmän käsiteltävää dataa**, mikä tekee agentista hitaamman ja kalliimman. Jokainen sana, jonka agentti käsittelee, voi maksaa rahaa, jos käytössä on kaupallinen kielimallipalvelu, kuten OpenAI:n API.

> **Pysähdy hetkeksi:** Kuvittele asiakaspalveluagentti, joka käsittelee pitkää tukiprosessia. Asiakas kuvailee ongelmaa pitkään ja kysyy 30 viestin jälkeen: ”Nyt kun olet kuullut kaiken, mitä ehdotat?” Jos konteksti-ikkuna sisältää vain 20 viestiä, agentti näkee enää viimeiset 20 viestiä. Alkuperäinen ongelma on poissa näkyvistä. Mitä tästä voi seurata?

Vastuullisena käyttäjänä sinun täytyy ymmärtää konteksti-ikkunan merkitys omissa agenteissasi. Neuvonta-agentissa, joka käsittelee pitkiä keskusteluketjuja, saatat tarvita 100–200 viestin ikkunan, jotta riittävä historia säilyy mukana. Transaktioagentissa, joka ratkaisee nopeita kysymyksiä, kuten ”Mikä on hinta?”, 20–30 viestiä voi riittää. Järkevä valinta riippuu siitä, **mitä agentin täytyy muistaa tehtävän ratkaisemiseksi**.

<figure class="ai-demo"><span class="ai-demo__tag">// työmuisti on pieni — agentti hakee vain sen, mitä vaihe vaatii</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:300px">
  <div class="l21-wrap">
    <div class="l21-phase"><span class="l21-pp p1">vaihe 1/3 · laadi tarjous → tarvitaan hinnasto</span><span class="l21-pp p2">vaihe 2/3 · sovi asennus → tarvitaan ohje</span><span class="l21-pp p3">vaihe 3/3 · jälkihoito → tarvitaan palaute</span></div>
    <div class="l21-shelf"><span class="l21-sh">PITKÄKESTOINEN MUISTI</span>
      <span class="l21-card k0">asiakkaan toive</span>
      <span class="l21-card k1">hinnasto</span>
      <span class="l21-card k2">asennusohje</span>
      <span class="l21-card k3">aiempi palaute</span>
    </div>
    <i class="l21-fly f1"></i><i class="l21-fly f2"></i><i class="l21-fly f3"></i>
    <div class="l21-agent">AGENTTI<div class="l21-slot"><span class="l21-sl">TYÖMUISTI · 1 paikka</span><span class="l21-in i1">hinnasto</span><span class="l21-in i2">asennusohje</span><span class="l21-in i3">aiempi palaute</span></div></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Agentin työmuisti ei pidä kaikkea mielessä — se on pieni ja kallis. Siksi agentti hakee pitkäkestoisesta muistista kulloinkin vain sen palasen, jota tehtävän vaihe vaatii: nyt hinnaston, kohta ohjeen, lopuksi palautteen.</figcaption></figure>
<style>
.l21-wrap{position:relative;width:560px;height:262px;font-family:var(--font-mono)}
.l21-phase{position:absolute;left:50%;transform:translateX(-50%);top:0;width:440px;height:32px}
.l21-pp{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:11.5px;font-weight:500;color:#06212A;background:#46c7cf;border-radius:10px;padding:2px 10px;opacity:0}
.l21-pp.p1{animation:l21p1 13.5s infinite}
.l21-pp.p2{animation:l21p2 13.5s infinite}
.l21-pp.p3{animation:l21p3 13.5s infinite}
@keyframes l21p1{0%,2%{opacity:0}5%,29%{opacity:1}33%,100%{opacity:0}}
@keyframes l21p2{0%,35%{opacity:0}38%,62%{opacity:1}66%,100%{opacity:0}}
@keyframes l21p3{0%,68%{opacity:0}71%,95%{opacity:1}99%,100%{opacity:0}}
.l21-shelf{position:absolute;left:0;top:54px;width:218px;background:#11182A;border:1.5px solid #2B3552;border-radius:13px;padding:11px 13px 9px}
.l21-sh{display:block;font-size:10px;letter-spacing:.11em;color:#B9C2DA;margin-bottom:9px}
.l21-card{display:block;font-size:11.5px;color:#B9C2DA;background:#0E1422;border:1.5px solid #2B3552;border-radius:8px;padding:7px 10px;margin-bottom:7px}
.l21-card.k1{animation:l21k1 13.5s infinite}
.l21-card.k2{animation:l21k2 13.5s infinite}
.l21-card.k3{animation:l21k3 13.5s infinite}
@keyframes l21k1{0%,5%,33%,100%{color:#B9C2DA;border-color:#2B3552}9%,29%{color:#FFFFFF;border-color:oklch(0.72 0.13 208)}}
@keyframes l21k2{0%,38%,66%,100%{color:#B9C2DA;border-color:#2B3552}42%,62%{color:#FFFFFF;border-color:oklch(0.72 0.13 208)}}
@keyframes l21k3{0%,71%,99%,100%{color:#B9C2DA;border-color:#2B3552}75%,95%{color:#FFFFFF;border-color:oklch(0.72 0.13 208)}}
.l21-fly{position:absolute;left:222px;width:10px;height:10px;border-radius:3px;background:oklch(0.72 0.13 208);opacity:0}
.l21-fly.f1{top:112px;animation:l21f1 13.5s infinite}
.l21-fly.f2{top:150px;animation:l21f2 13.5s infinite}
.l21-fly.f3{top:188px;animation:l21f3 13.5s infinite}
@keyframes l21f1{0%,9%{opacity:0;transform:translate(0,0)}11%{opacity:1}16%{opacity:1;transform:translate(118px,40px)}18%,100%{opacity:0;transform:translate(118px,40px)}}
@keyframes l21f2{0%,42%{opacity:0;transform:translate(0,0)}44%{opacity:1}49%{opacity:1;transform:translate(118px,2px)}51%,100%{opacity:0;transform:translate(118px,2px)}}
@keyframes l21f3{0%,75%{opacity:0;transform:translate(0,0)}77%{opacity:1}82%{opacity:1;transform:translate(118px,-36px)}84%,100%{opacity:0;transform:translate(118px,-36px)}}
.l21-agent{position:absolute;right:0;top:74px;width:200px;text-align:center;font-size:12.5px;letter-spacing:.13em;color:#EAEEF8;background:#11182A;border:2px solid oklch(0.66 0.13 208);border-radius:13px;padding:13px 12px 12px}
.l21-slot{position:relative;margin-top:11px;height:64px;border:1.5px dashed #44517A;border-radius:10px;background:#0B0F1A}
.l21-sl{position:absolute;left:0;right:0;top:7px;font-size:9px;letter-spacing:.08em;color:#7E88A8}
.l21-in{position:absolute;left:14px;right:14px;top:30px;font-size:11.5px;letter-spacing:.02em;color:#06241f;background:#7FD0A8;border-radius:8px;padding:5px 6px;font-weight:600;opacity:0}
.l21-in.i1{animation:l21i1 13.5s infinite}
.l21-in.i2{animation:l21i2 13.5s infinite}
.l21-in.i3{animation:l21i3 13.5s infinite}
@keyframes l21i1{0%,15%{opacity:0;transform:scale(.85)}19%,31%{opacity:1;transform:scale(1)}35%,100%{opacity:0}}
@keyframes l21i2{0%,48%{opacity:0;transform:scale(.85)}52%,64%{opacity:1;transform:scale(1)}68%,100%{opacity:0}}
@keyframes l21i3{0%,81%{opacity:0;transform:scale(.85)}85%,96%{opacity:1;transform:scale(1)}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l21-pp,.l21-card,.l21-fly,.l21-in{animation:none}
.l21-pp.p1,.l21-in.i1{opacity:1}
.l21-card.k1{color:#FFFFFF;border-color:oklch(0.72 0.13 208)}}
</style>


## Pitkäkestoinen muisti: vektoritietokanta merkityksen etsijänä

Konteksti-ikkuna kertoo agentille, mitä tapahtuu **nyt**. Mutta entä jos asiakkaan kanssa on työskennelty kuusi kuukautta? Entä jos hän palaa uuden ongelman kanssa ja haluat, että agentti muistaa, mitä viimeksi opittiin?

Tätä varten agentilla voi olla **pitkäkestoinen muisti**, joka tallennetaan esimerkiksi **vektoritietokantaan**. Vektoritietokanta on erikoistunut tietokanta, joka etsii samankaltaisuuksia merkityksen, ei vain täsmällisten sanojen perusteella. Tämä ero on tärkeä. Yksinkertaisesti sanottuna: vektoritietokanta toimii kuin hakukone, joka ymmärtää mitä tarkoitat — se löytää saman asian, vaikka sanoisit sen eri sanoin.

Tavallisessa tietokannassa haetaan usein täsmällisillä termeillä. Sana ”muistikortti” löytyy varmasti, jos hakusanana on ”muistikortti”. Vektoritietokannassa tieto tallennetaan kuitenkin merkityksen perusteella. Kun asiakas sanoo: ”Minulla oli ongelma muistilaitteen kanssa viime kuussa”, lause voidaan muuntaa **matemaattiseksi esitykseksi** eli vektoriksi. Tämä vektori kuvaa lauseen merkitystä: kyse on muistista, laitteesta, ongelmasta ja menneestä ajankohdasta.

Myöhemmin sama asiakas voi sanoa: ”Se muistiin liittyvä juttu oli vaikea.” Vaikka sanat ovat eri, lauseen merkitys voi olla samankaltainen kuin aiemmassa tapauksessa. Vektoritietokanta voi löytää tämän samankaltaisuuden ja auttaa agenttia päättelemään, että kyse voi olla samasta tai samantyyppisestä ongelmasta.

Tämä merkitysperusteinen haku on vektoritietokannan vahvuus. Se ei vaadi täsmällistä sanavastaavuutta, vaan se auttaa löytämään olennaista tietoa myös silloin, kun asiakas muotoilee asian eri tavalla kuin aiemmin.

Käytännössä tämä tarkoittaa, että kun agentti näkee asiakkaan nimen tai tunnisteen, se voi hakea vektoritietokannasta asiakkaaseen liittyvää aiempaa tietoa. Agentti ei välttämättä tarvitse kaikkia yksityiskohtia, vaan usein tiivistelmä riittää: ”Tämä asiakas on ostanut meiltä viisi kertaa. Hänellä on ollut aiemmin ongelmia toimituksissa. Viime kuussa ostettu tuote oli samaa sarjaa kuin nyt kysytty tuote.” Nämä tiedot auttavat agenttia ymmärtämään asiakkaan tilanteen ja tekemään parempia päätöksiä.

Vektoritietokanta toimii näin:

Voit ajatella vektoritietokantaa kirjaston hakujärjestelmänä. Kun haet kirjastosta aihetta ”koiran koulutus”, hyvä hakujärjestelmä ei etsi vain kirjoja, joissa lukee täsmälleen ”koiran koulutus”. Se voi löytää myös kirjoja, joiden nimi on esimerkiksi ”Pentujen kasvatus” tai ”Lemmikkien kouluttaminen”, koska ne käsittelevät samaa aihetta eri sanoin. Vektoritietokanta toimii samalla periaatteella: se etsii **merkityksiä**, ei pelkkiä sanoja.

> **Pysähdy hetkeksi:** Ajattele yrityssopimusta, jonka asiakas allekirjoitti kolme kuukautta sitten. Sopimuksessa oli erityisiä ehtoja ja myöhempi maksu. Kun asiakas ottaa nyt yhteyttä, agentti hakee sopimuksen vektoritietokannasta ja huomaa: ”Tämän asiakkaan sopimuksessa on erityisehtoja.” Mitä agentti voi tehdä toisin kuin tavallisten asiakkaiden kohdalla?

## Tila: prosessin vaihe ja muuttujat

Konteksti-ikkuna kertoo, mitä tapahtuu *nyt*. Pitkäkestoinen muisti kertoo, mitä on tapahtunut *aiemmin*. Mutta mistä agentti tietää, *missä vaiheessa* prosessia ollaan? Tätä varten tarvitaan **tila** eli state.

Kuvittele tilauksen käsittelyä. Kun asiakas tekee tilauksen, tila on ”tilaus luotu”. Kun agentti lähettää vahvistuksen, tila muuttuu muotoon ”vahvistus lähetetty”. Kun varasto pakkaa tuotteen, tila muuttuu muotoon ”pakattavana”. Kun kuljetus lähtee, tila on ”lähetetty”. Kun asiakas vastaanottaa tuotteen, tila on ”toimitettu”. Jokainen vaihe on eri tila, ja agentti seuraa, missä vaiheessa prosessi on.

Tila sisältää myös **muuttujia** eli prosessin aikana tarvittavia tietoja. Esimerkiksi:

- **Yritykset: 2/3** — kaksi yritystä on käytetty, yksi on jäljellä.
- **Viimeinen hinta: 45 €** — tämä hinta tarjottiin asiakkaalle viimeksi.
- **Ihmisen hyväksyntä: saatu** — vastuuhenkilö on hyväksynyt alennuksen.
- **Virheet: 0** — prosessin aikana ei ole havaittu virheitä.

Ilman tilamuuttujia agentin toiminta menisi helposti sekaisin. Se ei tietäisi, missä vaiheessa tehtävä on tai mitä se oli tekemässä. Se voisi lähettää vahvistussähköpostin kahteen kertaan, koska se ei muistaisi lähettäneensä sitä jo aiemmin. Se voisi yrittää veloittaa asiakasta uudelleen, koska se ei tietäisi, että maksu on jo suoritettu.

Kun rakennat agenttia n8n:llä, **tilan hallinta on kriittistä**. Sinun täytyy suunnitella, mitä mahdollisia tiloja prosessilla voi olla ja mitä muuttujia kussakin tilassa tarvitaan. Nämä tilat ja muuttujat ohjaavat agentin seuraavaa vaihetta. Esimerkiksi jos tila on ”maksu maksettu” ja muuttuja ”varastosaatavuus” on ”ei saatavilla”, agentin seuraava askel voi olla ilmoittaa asiakkaalle arvioitu toimitusaika.

## Käytännön esimerkki: asiakaspalveluagentti kokonaisuutena

Laitetaan nyt nämä kolme komponenttia yhteen. Kuvittele asiakaspalveluagentti, joka käsittelee asiakkaita reaaliajassa.

**Konteksti-ikkuna** näyttää viimeisimmät kymmenen viestiä, jotka asiakkaan kanssa on vaihdettu. Asiakas on voinut kuvailla ongelmaa pitkään, mutta agentti näkee vain viimeisimmät 10 viestiä. Niiden perusteella agentti ymmärtää esimerkiksi tämän: ”Asiakas kokeili ratkaisua A. Se ei auttanut. Nyt hän kysyy, mitä tehdä seuraavaksi.”

**Pitkäkestoinen muisti** paljastaa, että tämä asiakas on ollut asiakkaana kolme vuotta, hänellä on samankaltainen ongelma noin kolmen kuukauden välein ja edellisellä kerralla ratkaisu B auttoi. Vektoritietokanta löytää tämän yhteyden, koska se tunnistaa samankaltaisuuden nykyisen ja aiemman ongelman välillä.

**Tila** kertoo, että kyseessä on toinen ratkaisuyritys kolmesta, asiakas on aktiivinen eikä ihmisen tekemää eskalointia ole vielä pyydetty. Nämä muuttujat ohjaavat agentin seuraavaa päätöstä.

Agentti yhdistää nämä kolme tekijää: se näkee nykyisen tilanteen konteksti-ikkunan kautta, tietää pitkäkestoisen muistin avulla, mikä on aiemmin auttanut, ja ymmärtää tilan perusteella, missä vaiheessa prosessi on. Näiden perusteella se voi päätellä: ”Kokeillaan ratkaisua B, koska se auttoi aiemmin. Jos se ei auta, siirrän asian ihmiselle.” Tällainen päätös on mahdollinen vain siksi, että agentilla on käytössään konteksti, pitkäkestoinen muisti ja tila.

> **Pysähdy hetkeksi:** Ajattele omaa työtäsi tai opintojasi. Mitä tietoa pidät mielessä lyhytaikaisesti? Mitä tietoa säilytät pidempään? Miten seuraat, missä vaiheessa olet jossakin prosessissa? Agentin muisti ja tila toimivat samankaltaisella tavalla.

## Pysyvät toimintaperiaatteet eivät ole muistia

Konteksti-ikkuna, pitkäkestoinen muisti ja tila kertovat, mitä tietoa agentilla on käytettävissään. Niistä pitää erottaa **pysyvät toimintaperiaatteet**: järjestelmäohjeet ja harnessin säännöt, jotka määrittävät, miten agentin pitää toimia tilanteesta toiseen.

Toimintaperiaatteet vastaavat kolmeen kysymykseen:

**Ensimmäinen kysymys: Mikä on agentin tehtävä ja toimintatapa?** Esimerkiksi: ”Toimi kärsivällisenä neuvojana. Anna ensin lyhyt toimintaohje ja pyydä lisätietoa vain, jos se on ratkaisun kannalta tarpeen.” Ohje kuvaa havaittavaa toimintaa, ei koneen sisäistä luonnetta.

**Toinen kysymys: Mitkä rajat ovat voimassa aina?** Esimerkiksi: agentti ei palauta salasanaa, jaa toisen asiakkaan tietoja eikä esitä puuttuvaa tietoa varmana. Osa rajoista kirjoitetaan järjestelmäohjeisiin, mutta kriittiset rajat toteutetaan myös harnessissa oikeuksina, tarkistuksina ja hyväksyntäportteina.

**Kolmas kysymys: Miten epäselvä tilanne käsitellään?** Esimerkiksi: jos tietoa ei ole tarpeeksi, agentti pyytää tarkennusta; jos toimintaan liittyy korkea riski, harness pysäyttää vaiheen ja pyytää ihmisen hyväksynnän.

Käytännössä toimintaperiaatteet voidaan dokumentoida erikseen ja muuntaa järjestelmäohjeiksi, käyttöoikeuksiksi ja valvontasäännöiksi. Ne eivät ole agentin muistoja eivätkä todiste tietoisuudesta tai arvoista. Ne ovat ihmisen suunnittelema osa harnessia.

## Muistin turvallisuus ja hallinta

Kun agentti muistaa paljon, täytyy puhua myös turvallisuudesta. Pitkäkestoinen muisti voi sisältää arkaluontoisia tietoja, kuten asiakkaiden henkilötietoja, maksutietoja tai liikesalaisuuksia.

Vastuullisena käyttäjänä sinun täytyy asettaa selkeät rajat sille, **mitä agentti saa muistaa ja mitä se ei saa muistaa**. Asiakkaan nimi ja ostohistoria voivat olla perusteltuja tietoja, jos niitä käsitellään turvallisesti ja lain mukaisesti. Luottokortin neljä viimeistä numeroa voidaan joissain tilanteissa tallentaa tunnistamista varten, jos tieto on suojattu asianmukaisesti. Asiakkaan salasanaa ei kuitenkaan pidä koskaan tallentaa agentin muistiin. Myös terveystiedot ja muut erityisen arkaluontoiset tiedot vaativat erityistä varovaisuutta ja lainmukaisen käsittelyperusteen.

Muistin hallinta vaatii myös **säännöllistä puhdistamista**. Vanhentuneet tiedot kannattaa poistaa. Jos asiakas poistaa tilinsä, myös häneen liittyvä historia pitäisi poistaa pitkäkestoisesta muistista silloin, kun se on sääntöjen ja lainsäädännön mukaan tarpeen. Tämä on sekä turvallisuus- että yksityisyyskysymys.

## Kohti omaa projektia

Nyt kun ymmärrät konteksti-ikkunan, pitkäkestoisen muistin ja tilan, mieti omaa agenttiprojektiasi. Mitä tietoa agenttisi tarvitsee yksittäisen suorituksen aikana? Mitä sen täytyy säilyttää suoritusten välillä? Mitä tiloja prosessilla on? Kirjaa toimintaperiaatteet erikseen, jotta muistitieto ja järjestelmää ohjaavat säännöt eivät sekoitu toisiinsa.

> **Lopuksi pohdittavaksi:** Mitä tietoa harness antaa mallille nyt, mitä se säilyttää myöhemmäksi ja mitä sen pitää jättää tallentamatta?

## Yhteenveto

Agentti hahmottaa nykyhetkeä **konteksti-ikkunan** avulla. Konteksti-ikkuna voi sisältää esimerkiksi 20–200 viimeistä viestiä sen mukaan, millaista tehtävää agentti hoitaa. Agentilla voi olla myös **pitkäkestoinen muisti**, joka tallentuu esimerkiksi vektoritietokantaan ja auttaa löytämään samankaltaisia merkityksiä, ei vain täsmällisiä sanoja. Lisäksi agentilla on **tila**, joka kertoo, missä vaiheessa prosessi on ja mitä muuttujia siihen liittyy.

Nämä kolme tekijää auttavat agenttia käyttämään oikeaa tietoa oikeassa vaiheessa. Pysyvät toimintaperiaatteet ovat eri asia: ne kirjoitetaan järjestelmäohjeisiin ja toteutetaan tarvittaessa harnessin säännöillä. Kun rakennat agenttia n8n:llä, pidä erillään **mitä agentti tietää**, **missä vaiheessa tehtävä on** ja **mitkä säännöt rajaavat toimintaa**.

---

## Lähteet ja tarkistuspäivä

- [Anthropic: Building Effective AI Agents](https://resources.anthropic.com/building-effective-ai-agents)
- [Yao ym.: ReAct](https://arxiv.org/abs/2210.03629)
- [Model Context Protocol: server primitives](https://modelcontextprotocol.io/specification/2025-06-18/server/index)

Tarkistettu 15.7.2026.
