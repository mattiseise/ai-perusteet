# Konteksti ja promptaus — miten puhut tekoälylle

## Johdanto

**Tämän tunnin rajaus:** Opit erottamaan kontekstin ja promptin sekä parantamaan yhden pyynnön sisältöä. Tunnilla 12 käytät tätä perustaa uudelleen käytettävän promptipankin, lähdeaineiston, pilkkomisen ja testatun iteroinnin rakentamiseen.

Kuvittele, että ystäväsi lähettää sinulle viestin: "Auta, en saa tätä toimimaan." Se on maininta, mutta mitä se tarkoittaa? Onko kyse pelistä, ruoanlaitosta vai koulutehtävästä? Mikä tarkalleen ei toimi? Sama koskee tekoälyä. Jos sanot vain "auta minua", saat yleisen, ehkä hyödyttömän vastauksen. Mutta jos kerrot "olen lukiolainen, valmistelen 5 minuutin esitelmää ilmastonmuutoksesta historian tunnille, ja tarvitsen selkeän rakenteen kolmesta pääkohdasta" — silloin tekoäly ymmärtää, mikä on todellinen tarve, ja voi antaa konkreettista apua. Tämä ero on *konteksti ja promptaus* — ja se on kaiken tekoälyviestinnän ydin.

## Osa 1: Mitä konteksti on

Konteksti on kokonaisuus kaikkea sitä tietoa, jota tekoäly tarvitsee ymmärtääkseen, mitä sinä todella kysyt ja mitä haluat. Se ei ole vain yksittäinen kysymys tai käsky. Konteksti koostuu useista osista: kuka olet (roolisi), mitä taustaa sinulla on, mitä haluamme saavuttaa (tavoite), mitkä ovat rajat ja rajoitukset sekä konkreettiset esimerkit siitä, millaista vastausta odotat.

Kun opettaja neuvoo sinua matematiikan ongelmassa, hän ei vain kuule kysymystä — hän tietää, että olet 15-vuotias opiskelija, että olet oppinut derivaatat, että analysoit nyt funktion nollakohtia ja että hän haluaa sinun oppivan prosessin, ei vain saavasi vastausta. Kaikki tämä konteksti auttaa opettajaa antamaan juuri oikeanlaisen selityksen. Tekoäly tarvitsee saman.

> **Pysähdy hetkeksi:** Muista viimeksi, kun kysyit jotain internetistä tai ChatGPT:ltä ja sait täysin väärän tai hyödyttömän vastauksen. Mikä tieto puuttui? Mitkä tiedot olisivat auttaneet?

<figure class="ai-demo"><span class="ai-demo__tag">// sama pyyntö — konteksti karsii väärät tulkinnat</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;gap:16px;padding:10px 20px;height:280px">
  <div class="l04-left">
    <div class="l04-prompt">Tee minulle treeniohjelma.</div>
    <div class="l04-chips">
      <span class="l04-chip l04-c1">+ rooli: vasta-alkaja</span>
      <span class="l04-chip l04-c2">+ tavoite: 5 km juoksu</span>
      <span class="l04-chip l04-c3">+ rajaus: 3 krt/vko, ei salia</span>
    </div>
  </div>
  <div class="l04-arrow">→</div>
  <div class="l04-right">
    <span class="l04-note l04-n1">malli arvaa — monta tulkintaa</span>
    <span class="l04-note l04-n2">konteksti karsii — yksi osuu</span>
    <div class="l04-g l04-g1">Kuntosaliohjelma, 5 × viikossa, painot…</div>
    <div class="l04-g l04-g2">Juoksuohjelma aloittelijalle: 3 krt/vko, tavoite 5 km <span class="l04-ok">✓ osuva</span></div>
    <div class="l04-g l04-g3">Kehonpainotreeni kotiin, 20 min…</div>
  </div>
</div>
<figcaption class="ai-demo__cap">Ilman kontekstia malli joutuu arvaamaan, mitä tarkoitat. Jokainen kontekstin pala — rooli, tavoite, rajaus — karsii vääriä tulkintoja, kunnes jäljelle jää juuri sinun tarpeeseesi osuva vastaus.</figcaption></figure>
<style>
.l04-left{display:flex;flex-direction:column;gap:10px;width:225px}
.l04-prompt{font-family:var(--font-mono);font-size:13px;font-weight:500;color:#06212A;background:#46c7cf;border-radius:11px;padding:10px 12px}
.l04-chips{display:flex;flex-direction:column;gap:6px}
.l04-chip{font-family:var(--font-mono);font-size:11.5px;color:#EAEEF8;background:#1E2740;border:1.5px solid oklch(0.66 0.15 264);border-radius:999px;padding:4px 10px;align-self:flex-start;opacity:0}
.l04-c1{animation:l04chip 10s infinite}
.l04-c2{animation:l04chip2 10s infinite}
.l04-c3{animation:l04chip3 10s infinite}
@keyframes l04chip{0%,26%{opacity:0;transform:translateY(5px)}31%,94%{opacity:1;transform:translateY(0)}100%{opacity:0}}
@keyframes l04chip2{0%,34%{opacity:0;transform:translateY(5px)}39%,94%{opacity:1;transform:translateY(0)}100%{opacity:0}}
@keyframes l04chip3{0%,42%{opacity:0;transform:translateY(5px)}47%,94%{opacity:1;transform:translateY(0)}100%{opacity:0}}
.l04-arrow{font-size:22px;color:#7E88A8}
.l04-right{position:relative;display:flex;flex-direction:column;gap:9px;width:265px}
.l04-note{font-family:var(--font-mono);font-size:11px;letter-spacing:.04em}
.l04-n1{color:#F0A38C;animation:l04n1 10s infinite}
.l04-n2{position:absolute;top:0;left:0;color:#7FD0A8;opacity:0;animation:l04n2 10s infinite}
@keyframes l04n1{0%,4%{opacity:0}8%,46%{opacity:1}52%,100%{opacity:0}}
@keyframes l04n2{0%,50%{opacity:0}56%,94%{opacity:1}100%{opacity:0}}
.l04-g{font-family:var(--font-mono);font-size:12px;line-height:1.4;color:#B9C2DA;background:#141B2D;border:1.5px dashed #44517A;border-radius:11px;padding:9px 11px;opacity:0}
.l04-g1{animation:l04g1 10s infinite}
.l04-g3{animation:l04g3 10s infinite}
@keyframes l04g1{0%,4%{opacity:0}10%{opacity:.85}20%{opacity:.5}30%{opacity:.85}40%{opacity:.6}48%{opacity:.85;transform:scale(1)}58%,100%{opacity:0;transform:scale(.92)}}
@keyframes l04g3{0%,8%{opacity:0}14%{opacity:.8}24%{opacity:.55}34%{opacity:.8}44%{opacity:.55;transform:scale(1)}54%,100%{opacity:0;transform:scale(.92)}}
.l04-g2{animation:l04g2 10s infinite}
@keyframes l04g2{0%,6%{opacity:0}12%,54%{opacity:.85;color:#B9C2DA;background:#141B2D;border-color:#44517A;border-style:dashed}64%,94%{opacity:1;color:#FFFFFF;background:#15301F;border-color:#7FD0A8;border-style:solid}100%{opacity:0}}
.l04-ok{font-family:var(--font-mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:#06241a;background:#7FD0A8;border-radius:999px;padding:1px 7px;margin-left:5px;white-space:nowrap;opacity:0;animation:l04ok 10s infinite}
@keyframes l04ok{0%,62%{opacity:0}68%,94%{opacity:1}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l04-c1,.l04-c2,.l04-c3,.l04-n2,.l04-g2,.l04-ok{animation:none;opacity:1}
.l04-g2{color:#FFFFFF;background:#15301F;border:1.5px solid #7FD0A8}
.l04-g1,.l04-g3,.l04-n1{animation:none;opacity:0;display:none}}
</style>

### Kontekstin viisi komponenttia

Hyvä konteksti rakentuu viidestä pääosasta.

**1. Rooli** — Keitä olemme, mikä on osaamisemme ja näkökulmamme. Jos kerrot "olen kokenut kokki", tekoäly tietää, että se voi käyttää alan termejä ja olettaa tietyn osaamistason. Jos sanot "olen aloittelija keittiössä", vastaus voi olla perusteellisempi ja helpommin hyödynnettävä.

**2. Taustatieto** — Mitä on jo tehty, mitä olemme oppineet ja mitkä ovat lähtökohdat. Kun suunnittelet luokkaretkeä, jota olet jo alustavasti pohtinut, kerro mitä on jo päätetty. Kun pyydät apua treeniohjelmaan, mainitse, mitä olet jo kokeillut ja mikä toimi.

**3. Tavoite** — Miksi kysyt, mitä haluat tehdä ja mihin käytät vastausta. "Anna minulle reseptejä" on eri asia kuin "ehdota kolme edullista ja nopeaa illallista neljälle hengelle, joista yksi on kasvissyöjä". Tavoitteen selventäminen muuttaa vastausta merkittävästi.

**4. Rajaukset** — Mitä et halua, mikä ei ole olennaista ja mitkä asiat on jätettävä pois. "Ehdota illallisia, mutta älä mainitse kanaa, koska söimme sitä eilen." Tai "En halua filosofista vastausta, vain käytännön neuvoja."

**5. Esimerkit** — Näytä mallia siitä, mitä haluat. Jos haluat, että tekoäly kirjoittaa tekstin samalla tyylillä kuin sinä, anna näyte aiemmin kirjoittamastasi tekstistä. Jos haluat vastauksen, joka noudattaa tiettyä rakennetta, näytä esimerkki.

> **Pysähdy hetkeksi:** Ajattele tehtävää, jota teet usein — esimerkiksi tekstin kirjoittamista, harjoittelun suunnittelua tai tapahtuman järjestämistä. Mitkä viidestä kontekstin osasta olisivat tärkeimpiä tässä tapauksessa? Miksi?

## Osa 2: Promptaus — kuinka kysyt

Kun konteksti on valmis, sinun on osattava muotoilla *prompti* — tehtävänanto, joka esitetään kontekstin puitteissa. Suomeksi promptista käytetään myös sanaa *kehote*; tällä kurssilla käytämme termiä prompti. Prompti on kysymys, joka rakentuu kontekstin pohjalle. Konteksti on pohja, jonka päälle prompti rakentuu.

Monella on tästä väärinkäsitys: he ajattelevat, että "hyvä prompti" on sama asia kuin "hyvä konteksti". Se on kuin sanoisi, että reseptin otsikko ("Pastakeitto") olisi sama kuin koko resepti – ainesosat, valmistusohjeet, käsittelylämpötila ja kypsennysajat. Prompti on *kysymys* tai *tehtävänanto*, jonka esität nyt. Konteksti on *kaikki muu*, joka tekee kysymyksestä ymmärrettävän ja vastauksesta hyödyllisen.

Kuvittele, että istut opettajan kanssa hänen työhuoneessaan ja kysyt matematiikan kysymystä. Opettaja on jo nähnyt aiemmat työsi, tietää, mistä olet epävarma, tuntee tavoitteesi (läpäisy vai erinomainen arvosana) ja tietää, mitä olet jo oppinut. Kaikki tämä on *konteksti*. Sitten esität *promptin*: "Kuinka ratkaiset nollakohdan?" Prompti on kysymys, mutta konteksti on kaikki se muu, joka tekee kysymyksestä ymmärrettävän ja vastauksesta hyödyllisen.

### Hyvän promptin viisi elementtiä

Hyvä prompt rakentuu viidestä osasta. Et tarvitse niitä kaikkia joka promptiin, mutta tieto siitä, mitä osia voit käyttää, tekee sinusta paremman käyttäjän.

**1. Tavoite (goal)** — Mitä haluat? "Kirjoita tämä", "Selitä tämä", "Paranna tämä". Tavoite on selkeä lause, joka kertoo, mitä tekoäly tekee.

**2. Rooli (role)** — Kuka tekoäly on? "Olet kokenut opettaja", "Olet urheiluvalmentaja", "Olet ravitsemusneuvoja". Rooli auttaa mallia omaksumaan oikean näkökulman ja sopivan kielen. Huomaa kuitenkin: rooli vaikuttaa näkökulmaan, sävyyn ja kieleen — ei siihen, kuinka paljon malli oikeasti osaa. Pelkkä "olet huippuasiantuntija" ei tee vastauksesta asiantuntevampaa, jos tarvittava tieto puuttuu.

**3. Rajat (constraints)** — Mitä EI tehdä? "Älä käytä vaikeita termejä", "Kirjoita enintään 3 lausetta", "Älä mainitse hintoja". Rajat antavat mallille selkeän toiminta-alueen.

**4. Outputformaatti (format)** — Miten haluat vastauksen? "Vastaa JSON-muodossa", "Kirjoita taulukko", "Anna vaihekohtaiset ohjeet". Formaatti varmistaa, että saat käyttökelpoisen tuloksen.

**5. Esimerkit (examples)** — Näytä yksittäinen esimerkki siitä, mitä haluat. "Esimerkiksi: INPUT: 'terve', OUTPUT: 'Terve! Kuinka voin auttaa?'". Esimerkit tekevät vaatimuksista konkreettisempia.

Huolellisesti nämä viisi elementtiä ovat perustyökalusarjasi. Mitä enemmän tietoja annat, sitä parempia vastauksia saat.

> **Pysähdy hetkeksi:** Ajattele viimeistä kertaa, kun kysyit ChatGPT:ltä jotain. Mitkä viidestä elementistä annoit? Mitä puuttui? Olisiko parempi vastaus ollut mahdollinen, jos olisit antanut puuttuvat elementit?

## Osa 3: Konteksti ja promptaus yhteensä

Seuraavassa konkreettinen esimerkki, joka näyttää, kuinka konteksti ja promptaus toimivat yhdessä.

### Huono esimerkki: ilman kontekstia ja heikolla promptilla

**Prompt:** "Kirjoita esitelmä ilmastonmuutoksesta."

Miksi se on huono? Koska se ei sisällä:
- Roolia: Oletko lukiolainen? Opettaja?
- Taustaa: Mitä olet jo kirjoittanut tai oppinut?
- Tavoitetta: Mihin esitelmää käytetään ja kuinka pitkä sen pitää olla?
- Rajausta: Mihin näkökulmaan keskitytään? Mitä jätetään pois?
- Esimerkkejä: Millainen rakenne tai tyyli olisi hyvä?

Tekoäly tekee oletuksia joka kohdassa ja antaa sinulle jonkin version, joka *saattaa* sopia tarpeisiisi.

### Hyvä esimerkki: selkeä konteksti ja terävä prompti

**Konteksti:**
- Rooli: Olen lukion ensimmäisen vuoden opiskelija, ja pidän esitelmän pienelle ryhmälle.
- Taustatieto: Olen jo lukenut aiheesta oppikirjan luvun, mutta minulla ei ole vielä rakennetta.
- Tavoite: Haluan selkeän 5 minuutin esitelmän rungon ilmastonmuutoksen syistä ja seurauksista.
- Rajaukset: En halua liikaa numeroita ulkoa muistettavaksi, vaan helposti selitettäviä pääkohtia.
- Esimerkit: Haluan kolme pääotsikkoa, joista jokaisen alla on 2–3 ranskalaista viivaa.

**Prompti:**
"Tee 5 minuutin esitelmän runko ilmastonmuutoksen syistä ja seurauksista lukiolaiselle. Käytä kolmea pääotsikkoa, ja kirjoita jokaisen alle 2–3 ranskalaista viivaa selkeällä yleiskielellä. Vältä liikaa lukuja. Esimerkkimuoto: 'Otsikko: ... — Pääkohta 1: ... — Pääkohta 2: ...'."

Miksi se on hyvä?
- Rooli: lukiolainen — malli tietää kontekstin ja osaamistason.
- Tavoite: "tee esitelmän runko" — selkeä.
- Rajat: "vältä liikaa lukuja", "selkeä yleiskieli" — tarkka.
- Formaatti: "kolme pääotsikkoa, ranskalaiset viivat" — malli tietää muotoilun.
- Esimerkit: mallimuoto näyttää, millaista jäsentelyä halutaan.

Huolellisesti hyvä konteksti ja prompti säästävät aikaa. Joudut ehkä käyttämään enemmän aikaa kontekstin ja promptin muotoiluun, mutta saat parempia tuloksia ja tarvitset vähemmän kierroksia.

## Osa 4: Miksi huono konteksti ja prompti tuottaa huonoa jälkeä

Kun konteksti ja prompti ovat epäselviä, tekoäly joutuu arvailemaan. Se yrittää täydentää puuttuvat tiedot omilla oletuksillaan. Oletukset ovat usein vääriä.

**Esimerkki:** Jos kysyt "miten teen hyvän treeniohjelman", tekoäly voi ajatella, että olet kuntosaliharrastaja, juoksija tai vasta-alkaja — jokainen oletus johtaa eri vastaukseen. Jos kerrot tavoitteesi ilman kontekstia, tekoäly voi ehdottaa ratkaisuja, jotka eivät sovi sinun tilanteeseesi.

Huonon kontekstin ja promptin seurauksena saat usein myös liian pitkiä tai hajanaisia vastauksia. Tekoäly ei tiedä, mihin vastaus pitäisi kohdistaa, joten se kirjoittaa kaiken, mitä tietää. Jos kerrot selvästi "tarvitsen 5 minuutin opetusvideon käsikirjoituksen", saat ytimekkään vastauksen. Jos sanot vain "kirjoita video tekoälystä", saatat saada kahden tunnin esseen aiheesta.

Kontekstin ja promptin puuttuminen aiheuttaa myös turhauttavia väärinymmärryksiä. Opettaja tulkitsee "apua matikassa" eri tavoin riippuen siitä, oletko yläkoululainen vai yo-opiskelija. Tekoäly toimii samoin — ja ilman kontekstia ja selkeää promptia se valitsee usein aivan liian yleisen tai liian yksityiskohtaisen tason.

> **Pysähdy hetkeksi:** Mieti, millä tavoin antaisit itse kontekstia ja selkeän pyynnön ystävällesi, joka auttaa sinua jossakin ongelmassa kasvotusten. Mitä kerrot ensin, mitä viimeiseksi?

## Osa 5: Iteratiivinen kontekstin ja promptin rakentaminen

Huolellisesti et yritä kertoa kaikkea yhdessä suuressa tekstissä. Sen sijaan rakennat kontekstia ja promptia kierros kierrokselta — kokeneet käyttäjät kutsuvat tätä "prompt engineeringiksi".

**Kierros 1 — PerusPrompt:**
"Tee esitelmän runko ilmastonmuutoksesta."
- Saat: yleisen perusrungon

**Kierros 2 — Lisää kontekstia:**
"Esitelmä on lukiolaisille ja kestää 5 minuuttia. Lisää jokaiseen kohtaan yksi konkreettinen esimerkki."
- Saat: paremmin kohdistetun version

**Kierros 3 — Tarkenna tavoitetta:**
"Nyt lisää alkuun koukku, joka herättää kuulijan kiinnostuksen, ja loppuun yksi pohdintakysymys."
- Saat: viimeistellymmän rungon

**Kierros 4 — Muuta formaattia:**
"Muuta runko muistiinpanokorteiksi: jokaisen kortin yläosaan otsikko ja alle 2–3 avainsanaa, joiden varassa puhun vapaasti."
- Saat: valmiit esiintymiskortit

Jokainen kierros rakentaa edellisen päälle. Tekoäly "muistaa" kontekstin jokaisessa kierroksessa (riippuen siitä, mitä mallia käytät ja siitä, onko kyse samasta sessiosta vai eri sessioista).

Huolellisesti tämä on tehokasta. Et yritä ennustaa kaikkea etukäteen. Teet iteratiivisesti, näet tulokset ja parannat. Tämä on parempi strategia kuin kirjoittaa kerralla yksi täydellinen suurprompti, koska:
- Näet tulokset välillä ja voit korjata kurssia.
- Voit antaa kontekstia vähitellen kun ymmärrät, mitä tarvitset.
- Tekoäly pysyy paremmin "kartalla" lyhyemmillä kierroksilla.

> **Pysähdy hetkeksi:** Miksi iteratiivinen kontekstin ja promptin rakentaminen olisi parempi kuin "kaiken kerralla" -lähestyminen? Mitä voisi huolellisesti mennä pieleen, jos yrität kertoa kaiken kerralla?

## Osa 6: Kontekstin rakentaminen käytännössä

Käytännössä kontekstin ja promptin rakentaminen alkaa siitä, että ymmärrät, mitä itse tarvitset. Ennen kuin avaat tekoälyn, kirjoita itsellesi lyhyesti: kuka olen, mitä teen, mikä on ongelmani, mitä tiedän jo, mitä haluan saavuttaa.

Kerro sitten nämä asiat tekoälylle — ei välttämättä muodollisesti, mutta selvästi.

**Esimerkki 1 — Tapahtuman suunnittelu:**
- Huono: "Auta järjestämään juhlat."
- Hyvä: "Olen lukiolainen ja järjestän luokkamme kevätjuhlan noin 30 hengelle. Budjetti on 150 euroa, ja juhla pidetään koulun jälkeen kahdessa tunnissa. Olemme jo varanneet tilan, mutta tarjoilu ja ohjelma puuttuvat. Tarvitsen konkreettisia ehdotuksia, jotka mahtuvat budjettiin."

**Esimerkki 2 — Harjoittelun ongelma:**
- Huono: "Treenini ei toimi."
- Hyvä: "Olen aloittanut juoksun kuukausi sitten ja haluan parantaa kestävyyttäni. Juoksen kolmesti viikossa noin 3 km, mutta hengästyn nopeasti enkä jaksa juosta pidempään. Tavoitteeni on juosta 5 km yhtäjaksoisesti kahdessa kuukaudessa. Tarvitsen apua ohjelman rakentamiseen ilman, että loukkaan itseäni."

Nämä ovat silti lyhyitä, mutta ne sisältävät roolin, taustan, tavoitteen ja rajaukset. Ne tekevät tekoälyn vastauksesta hyödyllisemmän ja kohdennetumman.

## Yhteenveto

Konteksti ja promptaus ovat kaksi puolta samasta kolikosta. Konteksti on pohja — se rakentuu viidestä osasta: roolista, taustasta, tavoitteesta, rajauksista ja esimerkeistä. Promptaus on kysymys, joka esitetään kontekstin puitteissa, ja se rakentuu viidestä elementistä: tavoitteesta, roolista, rajauksista, outputformaatista ja esimerkeistä. Yhdessä ne muodostavat tehokkaan välineen, jolla saat tekoälystä juuri sellaista apua, jota tarvitset.

Huolellisesti et yritä antaa kaikkea yhdessä. Sen sijaan rakennat kontekstia ja promptia kierros kierrokselta. Joka kierros tarkentaa seuraavaa, ja lopputulos on moninkertaisesti parempi kuin yksi kerralla kirjoitettu täydellinen suurprompti.

Hyvä konteksti ja terävä prompti ovat investointi: ne vaativat hiukan enemmän aikaa ajatteluun ja kirjoittamiseen, mutta tuloksena on vastaus, joka on todella hyödyllinen eikä turha. Tämän kurssin ydinasia on, että konteksti ja prompti eivät ole pikkujuttu — ne ovat kaiken tekoälyviestinnän perusta. Konteksti- ja promptaustaidot ovat tärkeä työelämä- ja opiskelutaito alalla kuin alalla.

Seuraavalla tunnilla syvennämme kontekstin hallintaan: ymmärrät, että tekoälyn muisti on rajallinen, ja opit hallitsemaan sitä.

---

## Lähteet ja tarkistuspäivä

- [Vaswani ym.: Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [NIST: Generative AI Profile, NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

Tarkistettu 15.7.2026.
