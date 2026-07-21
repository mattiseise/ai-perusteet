# Agentin muisti ja konteksti — miten kone pysyy kartalla?

## Johdanto

Kun rakennat omaa agenttia n8n:llä, suunnittelet samalla, mitä tietoa kielimallille annetaan juuri nyt ja mitä tietoa järjestelmä säilyttää myöhempää käyttöä varten. Kielimalli ei itsessään kanna asiakashistoriaa suorituksesta toiseen. Agentin ohjauskehys voi valita kontekstiin keskusteluhistoriaa, hakea rakenteista tietoa, ylläpitää prosessin tilaa tai tuoda mukaan tietopohjasta löytyviä tekstikatkelmia.

Tässä oppitunnissa erotat toisistaan **konteksti-ikkunan, keskusteluhistorian, prosessin tilan, rakenteisen pitkäkestoisen tiedon, semanttisen vektorihaun sekä tietopohjan ja RAGin**. Niillä on eri tehtävät, eikä niitä pidä niputtaa yhdeksi muistiksi.

> **Ohjauskehys-kytkentä:** Agentin ohjauskehys valitsee, mitä mallille annetaan juuri nyt, tallentaa sovitut tiedot ja prosessin tilan sekä hakee tehtävän kannalta olennaisen tiedon. Samalla se toimeenpanee käyttöoikeudet ja rajaa, mitä ei saa tallentaa tai näyttää mallille.

## Konteksti-ikkuna: mitä agentti näkee juuri nyt?

Kuvittele asiakaspalveluagenttia, joka vastaa pitkän keskustelun jälkeen kysymykseen: ”Entä mitä ehdotat nyt?” Järjestelmän täytyy valita mukaan ongelman kuvaus, olennaiset aiemmat kokeilut ja uusimmat viestit. Kaiken keskusteluhistorian siirtäminen mallille ei ole aina tarpeellista eikä turvallista.

**Konteksti-ikkuna** tarkoittaa rajattua määrää tokeneita eli tekstin osia ja muuta aineistoa, jonka malli voi käsitellä yhdessä suorituksessa. Se ei ole sama asia kuin keskusteluhistoria. Sovellus voi valita historiasta osan, tiivistää aiempia tapahtumia tai jättää tarpeettoman sisällön pois ennen kuin konteksti annetaan mallille.

Käytännössä konteksti-ikkunan koko on kompromissi. Mitä suurempi ikkuna on, sitä enemmän agentti näkee aiempaa keskustelua ja sitä paremmin se voi ymmärtää tilanteen. Suurempi ikkuna tarkoittaa kuitenkin myös **enemmän käsiteltävää dataa**, mikä tekee agentista hitaamman ja kalliimman. Jokainen sana, jonka agentti käsittelee, voi maksaa rahaa, jos käytössä on kaupallinen kielimallipalvelu.

> **Pysähdy hetkeksi:** Mitkä kolme asiaa pitkästä tukikeskustelusta mallin täytyy nähdä seuraavaa päätöstä varten? Mitkä tiedot voidaan tiivistää, ja mitkä pitää jättää kokonaan pois?

Vastuullinen suunnittelija ei valitse kontekstia viestimäärän perusteella vaan kysyy, mikä tieto on tehtävän ratkaisemiseksi tarpeellista, ajantasaista ja sallittua. Kontekstissa olevan tiedon lähde ja ajankohta pitää voida tarkistaa.

<figure class="ai-demo"><span class="ai-demo__tag" id="l21-t"><i aria-hidden="true">// </i>konteksti, pitkäkestoinen muisti ja tila — eri tehtävät, yksi asiakaspyyntö</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:480px">
  <div class="l21-wrap" data-once role="img" aria-labelledby="l21-t" aria-describedby="l21-d">
    <span class="sr-only" id="l21-d">Konteksti rajaa sen, mitä malli näkee nyt: vanhin viesti putoaa ikkunasta pois. Pitkäkestoinen muisti tuo aiempaa tietoa nykyiseen kontekstiin — haku osuu merkityksen perusteella, ja osuvuus tarkistetaan: samankaltainen mutta eri laitetta koskeva tulos hylätään. Tila kertoo, missä vaiheessa prosessi on: konteksti rajaa nykyhetken, tila kertoo vaiheen. Muistiin talletetaan vain tarpeellinen, ja säilytysaika ja poistoehto kirjataan. Pysyvät periaatteet ovat sääntöjä, eivät muistia.</span>
    <span class="l21-hd">ASIAKASPALVELUAGENTTI · YKSI PYYNTÖ</span>
    <span class="l21-fz f1">vaihe 1/3 · asiakas kertoo</span>
    <span class="l21-fz f2">vaihe 2/3 · haku muistista</span>
    <span class="l21-fz f3">vaihe 3/3 · päätös</span>
    <div class="l21-p pw"><i class="l21-ph">KONTEKSTI</i>
      <em class="l21-pt">mitä malli näkee nyt</em>
      <span class="l21-c c1">laite ei toimi</span>
      <span class="l21-c c2">kokeilin ohjetta A</span>
      <span class="l21-c c3">ei auttanut</span>
      <span class="l21-c c4">mitä nyt?</span>
      <span class="l21-c c5">tilausnro 1414</span>
      <span class="l21-c ok c6">muistista: B-ohje</span>
      <span class="l21-ov o1">vanhin putoaa ulos ↓</span>
      <em class="l21-pd">ikkuna on pieni</em></div>
    <div class="l21-p pm"><i class="l21-ph phm">PITKÄKESTOINEN MUISTI</i>
      <em class="l21-pt">tuo aiempaa tietoa kontekstiin</em>
      <span class="l21-k k1">muistilaiteongelma · B auttoi</span>
      <span class="l21-k k2">näppäimistövika · eri laite</span>
      <span class="l21-gate">osuvuus: sama laite ja ongelma?<b class="gk1">✓ B-ohje osuu</b><b class="gk2">✗ eri laite: hylätty</b></span>
      <span class="l21-sem">eri sanat — sama merkitys</span></div>
    <div class="l21-p pt"><i class="l21-ph pht">TILA</i>
      <em class="l21-pt">missä vaiheessa prosessi on</em>
      <span class="l21-r">vaihe: <u class="l21-vv"><b class="l21-va">kartoitus</b><b class="l21-vb">ratkaisu käynnissä</b></u></span>
      <span class="l21-r">yritys: <u class="l21-vv"><b class="l21-ya">1/3</b><b class="l21-yb">2/3</b></u></span>
      <span class="l21-r">eskalointi: <b>ei</b></span></div>
    <span class="l21-q">se muistijuttu taas?</span>
    <span class="l21-ct">konteksti rajaa nykyhetken — tila kertoo prosessin vaiheen</span>
    <span class="l21-min">minimimuisti: talleta vain tarpeellinen · peruste ja säilytysaika kirjataan · poisto pyynnöstä tai vanhentuessa</span>
    <i class="l21-cv v1"></i><i class="l21-cv v2"></i><i class="l21-cv v3"></i>
    <span class="l21-dec">ehdota ratkaisua B<em>jos ei auta → ihmiselle</em></span>
    <span class="l21-pr">PYSYVÄT PERIAATTEET — sääntöjä, eivät muistia · esim. ”ei salasanoja muistiin”</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Konteksti rajaa sen, mitä malli näkee nyt. Pitkäkestoinen muisti tuo aiempaa tietoa nykyiseen kontekstiin — ja haun osuvuus tarkistetaan ennen käyttöä: samankaltainen mutta eri laitetta koskeva tulos hylätään. Tila kertoo, missä vaiheessa prosessi on. Nämä ovat eri tehtäviä, eivät kolme samanlaista muistia. Muistiin talletetaan vain tarpeellinen perustein, säilytysajoin ja poistoehdoin — ja pysyvät periaatteet ovat sääntöjä, eivät muistia.</figcaption></figure>
<style>
.l21-wrap{position:relative;width:560px;height:464px;font-family:var(--font-mono);animation:l21w 21s 1 forwards}
.l21-hd{position:absolute;left:0;top:4px;font-size:12px;font-weight:700;letter-spacing:.04em;color:#EAEEF8}
.l21-fz{position:absolute;right:0;top:0;font-size:12px;font-weight:700;color:#06212A;background:#46C7CF;border-radius:999px;padding:4px 10px;opacity:0}
.l21-fz.f1{animation:l21f1 21s 1 forwards}
.l21-fz.f2{animation:l21f2 21s 1 forwards}
.l21-fz.f3{animation:l21f3 21s 1 forwards}
.l21-p{position:absolute;top:30px;height:254px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:8px 9px}
.l21-p.pw{left:0;width:178px;animation:l21dimw 21s 1 forwards}
.l21-p.pm{left:190px;width:178px}
.l21-p.pt{left:380px;width:180px;animation:l21dimw 21s 1 forwards}
.l21-ph{display:block;font-style:normal;font-size:12px;font-weight:700;letter-spacing:.03em;color:#B9C2DA}
.l21-ph.phm{color:#C9B7F1}.l21-ph.pht{color:#FFD79A}
.l21-pt{display:block;font-style:normal;font-size:12px;line-height:1.2;color:#8B94B3;margin-top:2px}
.l21-pd{position:absolute;left:9px;bottom:6px;font-style:normal;font-size:12px;color:#8B94B3}
.l21-c{position:absolute;left:9px;width:160px;box-sizing:border-box;font-size:12px;line-height:1.2;color:#06212A;background:#9BD8DC;border-radius:6px;padding:5px 8px;opacity:0}
.l21-c.ok{background:#7FD0A8;font-weight:700}
.l21-c.c1{top:56px;animation:l21c1 21s 1 forwards}
.l21-c.c2{top:88px;animation:l21c2 21s 1 forwards}
.l21-c.c3{top:120px;animation:l21c3 21s 1 forwards}
.l21-c.c4{top:152px;animation:l21c4 21s 1 forwards}
.l21-c.c5{top:152px;animation:l21c5 21s 1 forwards}
.l21-c.c6{top:152px;animation:l21c6 21s 1 forwards}
.l21-ov{position:absolute;left:9px;bottom:24px;font-size:12px;font-weight:700;color:#FFD79A;opacity:0;animation:l21o1 21s 1 forwards}
.l21-k{position:absolute;left:9px;width:160px;box-sizing:border-box;font-size:12px;line-height:1.25;color:#EAEEF8;background:#0E1524;border:1px solid #2B3552;border-radius:8px;padding:6px 8px}
.l21-k.k1{top:54px;animation:l21k1 21s 1 forwards}
.l21-k.k2{top:130px;animation:l21k2 21s 1 forwards}
.l21-gate{position:absolute;left:9px;top:172px;width:160px;box-sizing:border-box;font-size:12px;line-height:1.25;color:#B9C2DA;border:1px dashed #4A5677;border-radius:8px;padding:5px 5px;opacity:0;animation:l21gt 21s 1 forwards}
.l21-gate b{display:block;font-weight:700;opacity:0}
.l21-gate .gk1{color:#7FD0A8;animation:l21gk1 21s 1 forwards}
.l21-gate .gk2{color:#FFD79A;animation:l21gk2 21s 1 forwards}
.l21-sem{position:absolute;left:9px;top:100px;width:160px;line-height:1.2;font-size:12px;font-weight:700;color:#C9B7F1;opacity:0;animation:l21sem 21s 1 forwards}
.l21-r{display:block;margin-top:11px;font-size:12px;color:#B9C2DA}
.l21-vv{position:relative;display:inline-block;min-width:118px;text-decoration:none}
.l21-r b{position:relative;font-weight:700;color:#FFD79A}
.l21-r .l21-va{animation:l21va 21s 1 forwards}
.l21-r .l21-vb{position:absolute;left:0;top:0;white-space:nowrap;opacity:0;animation:l21vb 21s 1 forwards}
.l21-r .l21-ya{animation:l21ya 21s 1 forwards;display:inline-block}
.l21-r .l21-yb{position:absolute;left:0;top:0;opacity:0;animation:l21yb 21s 1 forwards;display:inline-block}
.l21-ct{position:absolute;left:0;top:290px;width:560px;text-align:center;font-size:12.5px;font-weight:700;color:#FFD79A;opacity:0;animation:l21ct 21s 1 forwards}
.l21-min{position:absolute;left:0;top:310px;width:560px;text-align:center;font-size:12px;color:#8B94B3}
.l21-q{position:absolute;left:120px;top:126px;font-size:12px;color:#0B0F1A;background:#46C7CF;border-radius:999px;padding:4px 9px;opacity:0;animation:l21q 21s 1 forwards;white-space:nowrap}
.l21-cv{position:absolute;top:348px;width:0;height:14px;border-left:2px solid #7E88A8;transform:scaleY(0);transform-origin:top}
.l21-cv.v1{left:88px;animation:l21v1 21s 1 forwards}
.l21-cv.v2{left:278px;animation:l21v2 21s 1 forwards}
.l21-cv.v3{left:468px;animation:l21v3 21s 1 forwards}
.l21-dec{position:absolute;left:160px;top:366px;width:240px;box-sizing:border-box;text-align:center;font-size:12.5px;font-weight:700;color:#7FD0A8;border:1.5px solid #7FD0A8;border-radius:9px;padding:6px 8px 7px;background:rgba(127,208,168,.07);opacity:0;animation:l21dec 21s 1 forwards}
.l21-dec em{display:block;font-style:normal;font-size:12px;font-weight:400;color:#B9C2DA;margin-top:2px}
.l21-pr{position:absolute;left:0;top:426px;width:560px;box-sizing:border-box;text-align:center;font-size:12px;line-height:1.3;color:#8B94B3;border:1.5px dashed #4A5677;border-radius:9px;padding:8px 8px}
@keyframes l21w{0%{opacity:0}3%{opacity:1}100%{opacity:1}}
@keyframes l21f1{0%,2%{opacity:0}4%{opacity:1}31%{opacity:1}33%,100%{opacity:0}}
@keyframes l21f2{0%,33%{opacity:0}35%{opacity:1}64%{opacity:1}66%,100%{opacity:0}}
@keyframes l21f3{0%,66%{opacity:0}68%,100%{opacity:1}}
@keyframes l21c1{0%,2%{opacity:0;transform:none}5%{opacity:1}22%{opacity:1;transform:none}27%,100%{opacity:0;transform:translateY(110px)}}
@keyframes l21c2{0%,6%{opacity:0;transform:none}9%{opacity:1}23%{transform:none}27%{transform:translateY(-32px)}54%{opacity:1;transform:translateY(-32px)}59%,100%{opacity:0;transform:translateY(70px)}}
@keyframes l21c3{0%,10%{opacity:0;transform:none}13%{opacity:1}23%{transform:none}27%{transform:translateY(-32px)}55%{transform:translateY(-32px)}59%{transform:translateY(-64px)}85%{transform:translateY(-64px)}90%,100%{opacity:0;transform:translateY(40px)}}
@keyframes l21c4{0%,14%{opacity:0;transform:none}17%{opacity:1}23%{transform:none}27%{transform:translateY(-32px)}55%{transform:translateY(-32px)}59%{transform:translateY(-64px)}86%{transform:translateY(-64px)}90%,100%{opacity:1;transform:translateY(-96px)}}
@keyframes l21c5{0%,23%{opacity:0;transform:translateY(8px)}27%{opacity:1;transform:none}55%{transform:none}59%{transform:translateY(-32px)}86%{transform:translateY(-32px)}90%,100%{opacity:1;transform:translateY(-64px)}}
@keyframes l21c6{0%,58%{opacity:0;transform:translate(190px,-50px) scale(.85)}65%{opacity:1;transform:none}86%{transform:none}90%,100%{opacity:1;transform:translateY(-32px)}}
@keyframes l21o1{0%,23%{opacity:0}26%{opacity:1}33%{opacity:1}36%{opacity:0}86%{opacity:0}89%,100%{opacity:1}}
@keyframes l21q{0%,34%{opacity:0;transform:none}37%{opacity:1;transform:none}40%{transform:none}47%{opacity:1;transform:translate(115px,-45px) scale(.9)}51%,100%{opacity:0;transform:translate(115px,-45px)}}
@keyframes l21k1{0%,46%{border-color:#2B3552;box-shadow:none}51%{border-color:#C9B7F1;box-shadow:0 0 10px rgba(201,183,241,.6)}100%{border-color:#C9B7F1;box-shadow:0 0 4px rgba(201,183,241,.3)}}
@keyframes l21k2{0%,46%{border-color:#2B3552;opacity:1}50%{border-color:#C9B7F1}56%{border-color:#2B3552}60%,100%{opacity:.75;border-color:#4A5677}}
@keyframes l21gt{0%,50%{opacity:0;transform:translateY(5px)}53%,100%{opacity:1;transform:none}}
@keyframes l21gk1{0%,53%{opacity:0}56%,100%{opacity:1}}
@keyframes l21gk2{0%,56%{opacity:0}59%,100%{opacity:1}}
@keyframes l21sem{0%,48%{opacity:0}52%,100%{opacity:1}}
@keyframes l21dimw{0%,38%{opacity:1}42%{opacity:.75}50%{opacity:.75}54%,100%{opacity:1}}
@keyframes l21va{0%,76%{opacity:1}80%,100%{opacity:0}}
@keyframes l21vb{0%,76%{opacity:0}80%,100%{opacity:1}}
@keyframes l21ya{0%,12%{opacity:0}16%{opacity:1}76%{opacity:1}80%,100%{opacity:0}}
@keyframes l21yb{0%,76%{opacity:0}80%{opacity:1}81.5%{transform:scale(1.25)}83%,100%{opacity:1;transform:scale(1)}}
@keyframes l21ct{0%,88%{opacity:0}92%,100%{opacity:1}}
@keyframes l21v1{0%,67%{transform:scaleY(0)}69%,100%{transform:scaleY(1)}}
@keyframes l21v2{0%,68.5%{transform:scaleY(0)}70.5%,100%{transform:scaleY(1)}}
@keyframes l21v3{0%,70%{transform:scaleY(0)}72%,100%{transform:scaleY(1)}}
@keyframes l21dec{0%,72%{opacity:0;transform:scale(.8)}75%,100%{opacity:1;transform:scale(1)}}
@media (prefers-reduced-motion:reduce){
  .l21-wrap,.l21-wrap *{animation:none!important}
  .l21-wrap,.l21-sem,.l21-ct,.l21-dec,.l21-fz.f3,.l21-gate,.l21-gate b,.l21-ov{opacity:1}
  .l21-r .l21-vb,.l21-r .l21-yb{opacity:1}
  .l21-c.c4{opacity:1;transform:translateY(-96px)}
  .l21-c.c5{opacity:1;transform:translateY(-64px)}
  .l21-c.c6{opacity:1;transform:translateY(-32px)}
  .l21-c.c1,.l21-c.c2,.l21-c.c3,.l21-q,.l21-fz.f1,.l21-fz.f2{opacity:0}
  .l21-r .l21-va,.l21-r .l21-ya{opacity:0}
  .l21-cv{transform:scaleY(1)}
  .l21-k.k1{border-color:#C9B7F1}
  .l21-k.k2{opacity:.75;border-color:#4A5677}
}
</style>


## Pitkäkestoinen tieto, tietopohja ja semanttinen haku

Konteksti-ikkuna kertoo agentille, mitä tapahtuu **nyt**. Mutta entä jos asiakkaan kanssa on työskennelty kuusi kuukautta? Entä jos hän palaa uuden ongelman kanssa ja haluat, että agentti muistaa, mitä viimeksi opittiin?

**Rakenteinen pitkäkestoinen tieto** tallennetaan tavallisesti järjestelmään, jossa sillä on määritellyt kentät. Asiakkaan tunniste, sopimuksen tila, tilausnumero ja hyväksynnän ajankohta kuuluvat esimerkiksi asiakas- tai tilaustietokantaan. Täsmällistä tietoa ei pidä päätellä samankaltaisuuden perusteella.

**Tietopohja** on hyväksytty aineistokokoelma, kuten käyttöohjeet, menettelyohjeet tai kurssimateriaali. Se ei ole käyttäjästä kerättävää muistia. Tunnilla 15 opittu **RAG** tarkoittaa, että järjestelmä hakee tietopohjasta tehtävään liittyviä katkelmia ja antaa ne mallille vastauksen tueksi.

**Semanttinen vektorihaku** auttaa löytämään merkitykseltään samankaltaisia tekstikatkelmia, vaikka niissä käytetään eri sanoja. Se sopii esimerkiksi ohjeen etsimiseen tietopohjasta. Samankaltaisuus ei kuitenkaan todista, että katkelma koskee oikeaa tuotetta, versiota, käyttäjää tai ajankohtaa. Haun osuvuus ja lähde pitää tarkistaa ennen käyttöä.

Tämä merkitysperusteinen haku on vektoritietokannan vahvuus. Se ei vaadi täsmällistä sanavastaavuutta, vaan se auttaa löytämään olennaista tietoa myös silloin, kun asiakas muotoilee asian eri tavalla kuin aiemmin.

Asiakaskohtaista tietoa saa hakea vain käyttäjä- tai organisaatiorajauksen ja käyttöoikeuksien perusteella. Asiakkaan tunnisteella tehtävä tarkka haku kuuluu rakenteiseen järjestelmään, ei semanttiseen vektorihakuun. Ohjauskehyksen pitää estää toisen käyttäjän tai organisaation tietojen päätyminen kontekstiin.

Vektoritietokanta toimii näin:

Voit ajatella vektoritietokantaa kirjaston hakujärjestelmänä. Kun haet kirjastosta aihetta ”koiran koulutus”, hyvä hakujärjestelmä ei etsi vain kirjoja, joissa lukee täsmälleen ”koiran koulutus”. Se voi löytää myös kirjoja, joiden nimi on esimerkiksi ”Pentujen kasvatus” tai ”Lemmikkien kouluttaminen”, koska ne käsittelevät samaa aihetta eri sanoin. Vektoritietokanta toimii samalla periaatteella: se etsii **merkityksiä**, ei pelkkiä sanoja.

> **Pysähdy hetkeksi:** Asiakas kysyy sopimuksensa erityisehdosta. Mitkä tiedot haet rakenteisesta sopimusjärjestelmästä ja mitkä yleiset tulkintaohjeet tietopohjasta? Miten varmistat, että molemmat kuuluvat juuri tälle käyttäjälle ja ovat voimassa?

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

**Konteksti-ikkuna** sisältää tähän päätökseen valitut uusimmat viestit, tiivistelmän aiemmista kokeiluista ja vain tarpeelliset tunnistetiedot.

**Rakenteinen historia** kertoo käyttöoikeuden sallimissa rajoissa, mitä laitetta tapaus koskee ja mitä toimenpiteitä juuri tässä asiakkuudessa on jo tehty. **Tietopohjan semanttinen haku** löytää hyväksytystä ohjeesta mahdollisen ratkaisun B. Järjestelmä tarkistaa tuotteen, version ja lähteen ennen kuin katkelma annetaan mallille.

**Tila** kertoo, että kyseessä on toinen ratkaisuyritys kolmesta, asiakas on aktiivinen eikä ihmisen tekemää eskalointia ole vielä pyydetty. Nämä muuttujat ohjaavat agentin seuraavaa päätöstä.

Tässä esimerkkitoteutuksessa agentin ohjauskehys kokoaa päätöstä varten nykyisen tilanteen, tähän asiakkuuteen rajatun historian ja prosessin tilan. Näiden perusteella kielimalli voi valita sallitun etenemisen: ”Kokeillaan ratkaisua B, koska se auttoi aiemmin. Jos se ei auta, siirrän asian ihmiselle.” Ratkaisu B voidaan valita tässä tapauksessa, koska ohjauskehys välittää mallille juuri tähän päätökseen tarvittavat tiedot. Toisenlaisessa tehtävässä pitkäkestoista muistia ei välttämättä tarvita lainkaan.

> **Pysähdy hetkeksi:** Ajattele omaa työtäsi tai opintojasi. Mitä tietoa pidät mielessä lyhytaikaisesti? Mitä tietoa säilytät pidempään? Miten seuraat, missä vaiheessa olet jossakin prosessissa? Agentin muisti ja tila toimivat samankaltaisella tavalla.

## Pysyvät toimintaperiaatteet eivät ole muistia

Konteksti-ikkuna, pitkäkestoinen muisti ja tila kertovat, mitä tietoa agentilla on käytettävissään. Niistä pitää erottaa **pysyvät toimintaperiaatteet**: järjestelmäohjeet ja agentin ohjauskehyksen säännöt, jotka määrittävät, miten agentin pitää toimia tilanteesta toiseen.

Toimintaperiaatteet vastaavat kolmeen kysymykseen:

**Ensimmäinen kysymys: Mikä on agentin tehtävä ja toimintatapa?** Esimerkiksi: ”Toimi kärsivällisenä neuvojana. Anna ensin lyhyt toimintaohje ja pyydä lisätietoa vain, jos se on ratkaisun kannalta tarpeen.” Ohje kuvaa havaittavaa toimintaa, ei koneen sisäistä luonnetta.

**Toinen kysymys: Mitkä rajat ovat voimassa aina?** Esimerkiksi: agentti ei palauta salasanaa, jaa toisen asiakkaan tietoja eikä esitä puuttuvaa tietoa varmana. Osa rajoista kirjoitetaan järjestelmäohjeisiin, mutta kriittiset rajat toteutetaan myös agentin ohjauskehyksessä oikeuksina, tarkistuksina ja hyväksyntäportteina.

**Kolmas kysymys: Miten epäselvä tilanne käsitellään?** Esimerkiksi: jos tietoa ei ole tarpeeksi, agentti pyytää tarkennusta; jos toimintaan liittyy korkea riski, agentin ohjauskehys pysäyttää vaiheen ja pyytää ihmisen hyväksynnän.

Käytännössä toimintaperiaatteet voidaan dokumentoida erikseen ja muuntaa järjestelmäohjeiksi, käyttöoikeuksiksi ja valvontasäännöiksi. Ne eivät ole agentin muistoja eivätkä todiste tietoisuudesta tai arvoista. Ne ovat ihmisen suunnittelema osa agentin ohjauskehystä.

## Muistin turvallisuus ja hallinta

Kun agentti muistaa paljon, täytyy puhua myös turvallisuudesta. Pitkäkestoinen muisti voi sisältää arkaluontoisia tietoja, kuten asiakkaiden henkilötietoja, maksutietoja tai liikesalaisuuksia.

Vastuullisena käyttäjänä sinun täytyy asettaa selkeät rajat sille, **mitä agentti saa muistaa ja mitä se ei saa muistaa**. Asiakkaan nimi ja ostohistoria voivat olla perusteltuja tietoja, jos niitä käsitellään turvallisesti ja lain mukaisesti. Luottokortin neljä viimeistä numeroa voidaan joissain tilanteissa tallentaa tunnistamista varten, jos tieto on suojattu asianmukaisesti. Asiakkaan salasanaa ei kuitenkaan pidä koskaan tallentaa agentin muistiin. Myös terveystiedot ja muut erityisen arkaluontoiset tiedot vaativat erityistä varovaisuutta ja lainmukaisen käsittelyperusteen.

Muistin hallinta vaatii myös **säännöllistä puhdistamista**. Vanhentuneet tiedot kannattaa poistaa. Jos asiakas poistaa tilinsä, myös häneen liittyvä historia pitäisi poistaa pitkäkestoisesta muistista silloin, kun se on sääntöjen ja lainsäädännön mukaan tarpeen. Tämä on sekä turvallisuus- että yksityisyyskysymys.

## Kohti omaa projektia

Nyt kun ymmärrät konteksti-ikkunan, pitkäkestoisen muistin ja tilan, mieti omaa agenttiprojektiasi. Mitä tietoa agenttisi tarvitsee yksittäisen suorituksen aikana? Mitä sen täytyy säilyttää suoritusten välillä? Mitä tiloja prosessilla on? Kirjaa toimintaperiaatteet erikseen, jotta muistitieto ja järjestelmää ohjaavat säännöt eivät sekoitu toisiinsa.

> **Lopuksi pohdittavaksi:** Mitä tietoa agentin ohjauskehys antaa mallille nyt, mitä se säilyttää myöhemmäksi ja mitä sen pitää jättää tallentamatta?

## Yhteenveto

Agentin ohjauskehys kokoaa mallille **konteksti-ikkunan**. Keskusteluhistoria on yksi mahdollinen lähde, mutta sitä voidaan valita ja tiivistää. Täsmälliset pitkäkestoiset tiedot kuuluvat rakenteiseen järjestelmään. **Semanttinen vektorihaku** etsii tietopohjasta merkitykseltään samankaltaisia tekstikatkelmia, ja RAG tuo tarkistetut katkelmat vastauksen tueksi. **Prosessin tila** kertoo, missä vaiheessa tehtävä on.

Pidä erillään **mitä malli näkee nyt**, **mitä järjestelmä säilyttää rakenteisesti**, **mitä tietopohjasta haetaan**, **missä vaiheessa prosessi on** ja **mitkä säännöt rajaavat toimintaa**. RAG voi epäonnistua joko hakuvaiheessa, jos väärä tai puutteellinen katkelma valitaan, tai vastauksen muodostamisessa, jos malli käyttää oikeaakin lähdettä väärin. Siksi lähde, käyttäjärajaus ja lopputulos tarkistetaan.

---

## Lähteet ja tarkistuspäivä

- [Anthropic: Building Effective AI Agents](https://resources.anthropic.com/building-effective-ai-agents)
- [Yao ym.: ReAct](https://arxiv.org/abs/2210.03629)

Tarkistettu 15.7.2026.
