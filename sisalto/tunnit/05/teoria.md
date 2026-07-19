# Muistin rajat — kuinka paljon tekoäly oikeasti muistaa

## Johdanto

Kuvittele, että työskentelet opettajan kanssa koko viikon ajan pitkän projektin parissa. Maanantaina opettaja muistaa hyvin, mistä keskustelitte edellisellä viikolla. Tiistaina hän muistaa sen edelleen. Mutta entä kahden kuukauden kuluttua? Hän on jo unohtanut.

Hänen muistinsa on rajallinen — ei siksi, että hän olisi laiska, vaan siksi, että ihmisen muisti pystyy säilyttämään vain tietyn määrän tietoa kerrallaan.

Kielimallit toimivat samalla periaatteella. Ne eivät voi säilyttää koko keskustelua rajattomasti muistissa. Sen sijaan ne käyttävät niin sanottua konteksti-ikkunaa (context window), joka on rajallinen "muisti-ikkuna", jossa säilyy vain osa keskustelusta.

Kun tämä ikkuna täyttyy, vanhimmat tiedot poistuvat ja uudet tulevat tilalle.

Tämän oppitunnin aiheena on ymmärtää tämä raja ja oppia hallitsemaan kontekstia niin, että tekoäly saa aina tarvitsemansa tiedon.

Tämän tunnin jälkeen sinulla on tuomaripöydälläsi todistusaineisto: tekoälyllä on samat muistin rajat kuin ihmisillä — ja joskus jopa pienempiä.

## Mitä konteksti-ikkuna on?

Konteksti-ikkuna on tekoälymalleille asetettu raja, joka määrittää, kuinka paljon tekstiä malli voi käsitellä yhdessä keskustelussa. Raja määritellään tokeneina, jotka ovat pieniä tekstin palasia. Esimerkiksi GPT-4-mallin konteksti-ikkuna oli noin 128 000 tokenia; uudemmissa malleissa ikkunat ovat usein vielä suurempia, jopa miljoona tokenia. Vaikka ikkuna olisi suuri, se ei ole ääretön.

Tokenit eivät ole sama asia kuin sanat. Englannin kielessä yksi tokeni on noin 4 merkkiä, joten 128 000 tokenia vastaa noin 512 000 merkkiä eli noin 85 000 sanaa. Se kuulostaa paljolta — ja onkin, pituudeltaan lähes painetun kirjan verran. Mutta laajassa projektissa, jossa on kymmeniä sivuja muistiinpanoja, pitkiä keskusteluja tai monta liitettä, se täyttyy nopeasti.

Kun malli käsittelee syötettä, se menettää keskustelun vanhimman osan ja säilyttää vain uudemman osan. Tämä on kuin puhelimen tekstiviestiketju, joka näyttää vain viimeiset 100 viestiä — vanhemmat viestit liukuvat pois näkyvistä. Malli ei enää näe vanhaa kontekstia. Jos sanoit aiemmin "Kirjoitan tekstin selkeällä yleiskielellä", mutta keskustelu on nyt 15 000 tokenia edemmällä, malli saattaa unohtaa sen.

> **Pysähdy hetkeksi:** Kuvittele, että neuvot ystävääsi ohjelmointiongelmassa tunnin ajan. Ystävä kysyy lopuksi: "Muistatko sen, mitä sanoin alussa?" Jos muistisi olisi silloin huono, mitä toivoisit hänen kertovan uudelleen?

<figure class="ai-demo"><span class="ai-demo__tag">// ikkuna liukuu keskustelun yli — vain sisällä oleva on muistissa</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:280px">
  <div class="l05-wrap">
    <span class="l05-hdr">vanhin putoaa ←</span><span class="l05-hdr2">→ uusin saapuu</span>
    <div class="l05-rail"><div class="l05-strip">
      <span class="l05-m l05-ohje">OHJE: vastaa aina suomeksi</span><span class="l05-m">Suunnitellaan kampanja.</span><span class="l05-m">Tavoite: vähemmän muovia.</span><span class="l05-m">Kohderyhmä: koko koulu.</span><span class="l05-m">Ehdota kolme julistetta.</span><span class="l05-m">Lisää aikataulu.</span><span class="l05-m">Entä budjetti?</span><span class="l05-m">Tee yhteenveto tähän asti.</span><span class="l05-m l05-ohje">OHJE: vastaa aina suomeksi</span><span class="l05-m">Suunnitellaan kampanja.</span><span class="l05-m">Tavoite: vähemmän muovia.</span><span class="l05-m">Kohderyhmä: koko koulu.</span><span class="l05-m">Ehdota kolme julistetta.</span><span class="l05-m">Lisää aikataulu.</span><span class="l05-m">Entä budjetti?</span><span class="l05-m">Tee yhteenveto tähän asti.</span>
    </div></div>
    <div class="l05-cur l05-cl"></div><div class="l05-cur l05-cr"></div>
    <div class="l05-win"><span class="l05-wl">KONTEKSTI-IKKUNA — mallin koko muisti</span></div>
    <span class="l05-x">✕</span>
    <span class="l05-warn">myös alun OHJE putoaa lopulta ulos — malli ei kerro unohtaneensa</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Konteksti-ikkuna on kiinteän kokoinen: keskustelun kasvaessa se liukuu eteenpäin, ja vanhimmat viestit — myös alussa antamasi pysyväisohjeet — putoavat ulos. Ikkunan ulkopuolella olevaa malli ei muista lainkaan.</figcaption></figure>
<style>
.l05-wrap{position:relative;width:560px;height:240px;font-family:var(--font-mono)}
.l05-hdr{position:absolute;left:6px;top:24px;font-size:10.5px;letter-spacing:.05em;color:#F0A38C}
.l05-hdr2{position:absolute;right:6px;top:24px;font-size:10.5px;letter-spacing:.05em;color:#7FD0A8}
.l05-rail{position:absolute;left:0;right:0;top:62px;height:64px;overflow:hidden}
.l05-strip{position:absolute;top:11px;display:flex;gap:10px;width:max-content;animation:l05slide 30s linear infinite}
@keyframes l05slide{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.l05-m{font-size:11.5px;white-space:nowrap;color:#EAEEF8;background:#1E2740;border:1.5px solid #44517A;border-radius:9px;padding:9px 11px}
.l05-ohje{color:#06212A;background:#46c7cf;border-color:transparent;font-weight:600}
.l05-cur{position:absolute;top:56px;height:76px;z-index:3;pointer-events:none}
.l05-cl{left:0;width:148px;background:linear-gradient(90deg,#0c1120 55%,rgba(12,17,32,0))}
.l05-cr{right:0;width:148px;background:linear-gradient(270deg,#0c1120 55%,rgba(12,17,32,0))}
.l05-win{position:absolute;left:150px;width:260px;top:48px;height:92px;border:2.5px solid oklch(0.66 0.15 264);border-radius:13px;z-index:4;box-shadow:0 0 18px oklch(0.66 0.15 264/.25)}
.l05-wl{position:absolute;left:50%;transform:translateX(-50%);top:-15px;font-size:10px;letter-spacing:.09em;text-transform:uppercase;white-space:nowrap;color:#0B0F1A;background:oklch(0.78 0.12 264);border-radius:999px;padding:2px 9px}
.l05-x{position:absolute;left:64px;top:84px;z-index:5;font-size:15px;font-weight:700;color:#F0A38C;animation:l05x 3.4s ease-out infinite}
@keyframes l05x{0%{opacity:0;transform:translateY(0) scale(.8)}30%{opacity:1}100%{opacity:0;transform:translateY(-20px) scale(1.25) rotate(18deg)}}
.l05-warn{position:absolute;left:0;right:0;top:170px;text-align:center;font-size:11.5px;line-height:1.4;color:#F0A38C;animation:l05warn 4s ease-in-out infinite}
@keyframes l05warn{0%,100%{opacity:.6}50%{opacity:1}}
@media (prefers-reduced-motion:reduce){
.l05-strip,.l05-x,.l05-warn{animation:none}
.l05-strip{transform:translateX(-25%)}
.l05-x{opacity:1}}
</style>

## Miten tieto putoaa ulos ikkunasta

Konteksti-ikkunan täyttyminen noudattaa FIFO-periaatetta (First In, First Out) — ensimmäinen sisään, ensimmäinen ulos. Jos aloitat keskustelun antamalla paljon kontekstia ja sitten kysyt 20 kertaa peräkkäin, kunnes keskustelussa on 120 000 tokenia, alkuperäinen kontekstisi on jo kadonnut. Mallilla on käytössään vain viimeiset muutamat kysymys–vastaus-parit ja hieman muuta kontekstia.

Tämä voi johtaa häiritseviin tilanteisiin. Olet saattanut sanoa alussa: "Vastaa aina suomeksi, älä englanniksi", mutta 50 viestin jälkeen malli alkaa vastata englanniksi, koska se on unohtanut rajauksesi. Tai olet antanut tarkan tyyliesimerkin keskustelun alussa, mutta myöhemmin malli kirjoittaa eri tyylillä, koska se ei enää näe esimerkkiä.

Tiedon putoaminen voi myös muuttaa keskustelun sävyä. Jos olet aluksi "opiskelija, joka oppii", mutta 30 viestin jälkeen tämä rooli unohtuu, malli saattaa alkaa pitää sinua asiantuntijana ja antaa hyvin teknisiä vastauksia ilman selityksiä.

> **Pysähdy hetkeksi:** Ajattele pitkää projektin virheiden selvittämistä. Mitä tärkeää tietoa malli voisi unohtaa niin, että se alkaisi antaa vääriä neuvoja?

## Kuinka kontekstia tiivistetään, pilkotaan ja rakennetaan uudelleen

Vastuullisena käyttäjänä sinun täytyy hallita konteksti-ikkunaa. Kuten olemme jo aiemmin oppineet, on kolme päästrategiaa: tiivistys, pilkkominen ja ankkurointi. Nämä ovat perustyökaluja, joita tarvitset jokaisen projektin parissa työskennellessäsi.

Käytännön työssä näitä strategioita käytetään yhdessä. Jos sinulla on suuri projekti, joka kestää useita päiviä, ankkuroi olennainen tieto joka päivä, pilko tehtävät pienemmiksi ja tiivistä edellisten päivien tulokset.

Palaamme näihin strategioihin myöhemmin, kun opimme, kuinka agentit hallitsevat muistiaan.

> **Pysähdy hetkeksi:** Ajattele omaa projektia, joka kestää viikon tai pidempään. Miten jakaisit sen osiin, jotta konteksti-ikkuna ei koskaan täyttyisi?

## Kun konteksti katoaa — mitä todella tapahtuu

Tähän asti olemme puhuneet konteksti-ikkunasta teoreettisesti. Nyt katsotaan, mitä tapahtuu käytännössä, kun tärkeä tieto putoaa ikkunasta — ja malli ei kerro sinulle siitä.

Kuvittele seuraava tilanne. Aloitat keskustelun tekoälyn kanssa ja annat selkeän rajauksen: "Kirjoitamme yhdessä novellia. Päähenkilön nimi on Aino, tarina sijoittuu 1920-luvun Suomeen, ja tyyli on vakava. Älä lisää tarinaan nykyaikaisia laitteita."

Ensimmäiset 10 vastausta ovat erinomaisia. Malli muistaa rajaukset, pitää tyylin vakavana ja kirjoittaa ajan kuvaukseen sopivasti.

Mutta 25 viestin jälkeen kysyt: ”Miten kohtaus jatkuu?” Malli kirjoittaa kohtauksen, jossa Aino selailee puhelinta, ja vaihtaa tyylin kepeäksi — koska se on unohtanut alkuperäisen rajauksesi. Se ei kerro, ettei enää muista. Se ei sano: ”Huomaa, etten enää muista alkuperäistä kontekstiasi.” Se vain vastaa parhaansa mukaan sillä tiedolla, joka sillä on jäljellä.

Tämä on konteksti-ikkunan vaarallisin piirre: **malli ei kerro, kun se unohtaa**. Se ei anna virheilmoitusta. Se ei sano "konteksti on kadonnut". Se vain alkaa antaa vastauksia, jotka eivät enää noudata alkuperäisiä rajauksia.

Käytännön työssä tämä voi johtaa vakaviin virheisiin. Esitelmän sävy lipsahtaa väärään suuntaan. Asiakkaalle lähetetty teksti rikkoo sovittua ohjeistusta. Käännös vaihtaa kieltä kesken kaiken. Ja koska vastaukset ovat yhtä sujuvia kuin aiemmin, saatat huomata virheen vasta liian myöhään.

Oikea vastuullinen käyttäjä ei luota siihen, että malli muistaa. Hän tarkistaa, huomaa poikkeaman ja korjaa tilanteen — joko toistamalla ankkurin tai aloittamalla uuden keskustelun.

> **Pysähdy hetkeksi:** Oletko koskaan ollut tilanteessa, jossa tekoäly antoi sinulle vastauksen, joka tuntui oikealta mutta ei sopinut tilanteeseesi? Mistä tiesit, että jokin oli vialla?

## Keskustelun hallinta käytännössä

Käytännössä konteksti-ikkunan hallinta alkaa siitä, että ymmärrät koko projektisi koon ja monimutkaisuuden. Pieni kysymys? Älä huolehdi ikkunasta — 1 000 tokenia ei ole ongelma. Suuri analyysi? Suunnittele etukäteen.

Kun aloitat keskustelun tekoälyn kanssa, pidä mielessäsi seuraavat asiat:

- **Jokainen vastaus kuluttaa ikkunaa.** Kun malli vastaa, se käyttää tokeneita. Pitkä vastaus = enemmän ikkunaa käytetty.
- **Historia kasvaa.** Jokainen uusi kysymys lisää sisältöä ikkunaan. Jos kysyt 100 kertaa, historia on paljon suurempi kuin jos kysyt kerran.
- **Vanha tieto menetetään ensin.** Jos aloitit kontekstilla "Kirjoita aina suomeksi, vakavalla sävyllä ja korkeintaan 200 sanaa kerrallaan", ja nyt olet 100 viestiä edemmällä, tämä tieto voi olla jo poissa ikkunasta.

Ratkaisuksi:

- Jaa pitkä projekti useiksi lyhyiksi keskusteluiksi. Jokainen keskustelu on uusi, puhdas ikkuna.
- Dokumentoi tulokset. Kun aloitat uuden keskustelun, kopioi oleelliset tulokset kontekstiin.
- Käytä "muista aina" -tekniikkaa: muistuta mallia jokaisen viestin alussa tärkeistä asioista.

Esimerkiksi:

- **Päivä 1:** Teet tutkielmaa. Aloita kontekstilla: "Aiheena on lukion liikuntatottumukset, lähteitä on 8, kohderyhmänä toisen asteen opiskelijat. Käsittelen nyt lähteet 1–3."
- **Päivä 2:** Aloitat uudelleen. Konteksti: "Edellispäivää jatkaen. Aiheena lukion liikuntatottumukset, lähteitä 8. Eilen lähteistä 1–3 nousi esiin: [yhteenveto]. Nyt käsittelen lähteet 4–6."

Näin malli ei koskaan unohda olennaista, vaikka ikkuna olisi täyttynyt.

## Konteksti-ikkuna ja pysyvä muisti — kaksi eri asiaa

Konteksti-ikkunan lisäksi monella tekoälytyökalulla, kuten ChatGPT:llä, on erillinen pysyvä muisti. Sinne voit tallentaa tietoja, jotka haluat mallin muistavan aina — myös uusissa keskusteluissa. Voit esimerkiksi pyytää: "Muista tämä: käytän Unity 6 -pelimoottoria", jolloin malli ei enää ehdota sinulle vanhentuneita versioita seuraavissakaan keskusteluissa. Ero on tärkeä: konteksti-ikkuna unohtaa keskustelun päättyessä, mutta pysyvä muisti säilyy keskustelusta toiseen. Pysyvä muisti on siis kuin muistilappu, jonka kiinnität jääkaapin oveen, kun taas konteksti-ikkuna on vain yhden keskustelun aikainen työpöytä, joka tyhjenee, kun suljet sen.

## Yhteenveto

Konteksti-ikkuna on tekninen raja, joka määrittää, kuinka paljon tekstiä tekoäly voi käsitellä yhdessä keskustelussa. Vanha tieto putoaa ulos, kun ikkuna täyttyy. Vastuullisena käyttäjänä hallitset ikkunaa kolmella tavalla: tiivistämällä vanhoja tekstejä, pilkkomalla projektit pienempiin osiin ja ankkuroimalla olennaisen tiedon jokaiseen viestiin. Näillä menetelmillä voit johtaa pitkiä, monimutkaisia projekteja tekoälyn kanssa ilman, että mallin muisti pettää. Konteksti-ikkunan ymmärtäminen on avain siihen, että tekoälystä tulee luotettava työkaveri eikä epävakaa avustaja.

Seuraavalla tunnilla laajennat näkökulmaasi: tekoäly voi käsitellä enemmän kuin pelkkää tekstiä — kuvia, ääntä, videota.

---

## Lähteet ja tarkistuspäivä

- [Vaswani ym.: Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [NIST: Generative AI Profile, NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

Tarkistettu 15.7.2026.
