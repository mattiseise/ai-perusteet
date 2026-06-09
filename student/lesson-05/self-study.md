# Muistin rajat — kuinka paljon tekoäly oikeasti muistaa

## Johdanto

Kuvittele, että työskentelet opettajan kanssa koko viikon ajan pitkän projektin parissa. Maanantaina opettaja muistaa hyvin, mistä keskustelitte edellisellä viikolla. Tiistaina hän muistaa sen edelleen. Mutta entä kahden kuukauden kuluttua? Hän on jo unohtanut.

Hänen muistinsa on rajallinen — ei siksi, että hän olisi laiska, vaan siksi, että ihmisen muisti pystyy säilyttämään vain tietyn määrän tietoa kerrallaan.

Kielimallit toimivat samalla periaatteella. Ne eivät voi säilyttää koko keskustelua rajattomasti muistissa. Sen sijaan ne käyttävät niin sanottua konteksti-ikkunaa (context window), joka on rajallinen "muisti-ikkuna", jossa säilyy vain osa keskustelusta.

Kun tämä ikkuna täyttyy, vanhimmat tiedot poistuvat ja uudet tulevat tilalle.

Tämän oppitunnin aiheena on ymmärtää tämä raja ja oppia hallitsemaan kontekstia niin, että tekoäly saa aina tarvitsemansa tiedon.

Tämän tunnin jälkeen sinulla on tuomaripöydälläsi todistusaineisto: tekoälyllä on samat muistin rajat kuin ihmisillä — ja joskus jopa pienempiä.

## Mitä konteksti-ikkuna on?

Konteksti-ikkuna on tekoälymalleille asetettu raja, joka määrittää, kuinka paljon tekstiä malli voi käsitellä yhdessä keskustelussa. Raja määritellään tokeneina, jotka ovat pieniä tekstin palasia. Esimerkiksi ChatGPT-4:llä on konteksti-ikkuna, jossa on noin 128 000 tokenia, ja Claude 3:lla vielä suurempi. Vaikka ikkuna olisi suuri, se ei ole ääretön.

Tokenit eivät ole sama asia kuin sanat. Englannin kielessä yksi tokeni on noin 4 merkkiä, joten 128 000 tokenia vastaa noin 512 000 merkkiä eli noin 85 000 sanaa. Se kuulostaa paljolta — ja onkin, pituudeltaan lähes painetun kirjan verran. Mutta laajassa projektissa, jossa on kymmeniä sivuja muistiinpanoja, pitkiä keskusteluja tai monta liitettä, se täyttyy nopeasti.

Kun malli käsittelee syötettä, se menettää keskustelun vanhimman osan ja säilyttää vain uudemman osan. Tämä on kuin puhelimen tekstiviestiketju, joka näyttää vain viimeiset 100 viestiä — vanhemmat viestit liukuvat pois näkyvistä. Malli ei enää näe vanhaa kontekstia. Jos sanoit aiemmin "Kirjoitan tekstin selkeällä yleiskielellä", mutta keskustelu on nyt 15 000 tokenia edemmällä, malli saattaa unohtaa sen.

> **Pysähdy hetkeksi:** Kuvittele, että neuvot ystävääsi ohjelmointiongelmassa tunnin ajan. Ystävä kysyy lopuksi: "Muistatko sen, mitä sanoin alussa?" Jos muistisi olisi silloin huono, mitä toivoisit hänen kertovan uudelleen?

<figure class="ai-demo"><span class="ai-demo__tag">// konteksti-ikkuna on täynnä — vanhin putoaa ulos</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;padding:18px 28px">
  <div class="l05-scene">
    <span class="l05-side">uusi sisään →</span>
    <div class="l05-win">
      <div class="l05-track">
        <span class="l05-tk l05-old">alku</span><span class="l05-tk">tausta</span><span class="l05-tk">ohje</span><span class="l05-tk">kysymys</span><span class="l05-tk">vastaus</span>
      </div>
      <span class="l05-tk l05-new">uusin</span>
      <span class="l05-drop">↓ unohtui</span>
    </div>
    <span class="l05-cap">ikkuna: 5 muistipaikkaa · <b>TÄYNNÄ</b></span>
  </div>
</div>
<figcaption class="ai-demo__cap">Konteksti-ikkuna on kiinteän kokoinen. Kun uusi tieto työntyy sisään oikealta, vanhin liukuu ulos vasemmalta ja putoaa pois — malli ei enää näe sitä, eikä kerro sinulle siitä.</figcaption></figure>
<style>
.l05-scene{position:relative;width:360px;display:flex;flex-direction:column;align-items:center;gap:30px;animation:l05scene 7s ease-out infinite}
@keyframes l05scene{0%{opacity:0}8%{opacity:1}90%{opacity:1}100%{opacity:0}}
.l05-side{font-family:var(--font-mono);font-size:12px;color:oklch(0.66 0.13 208);align-self:flex-end;margin-right:8px}
.l05-win{position:relative;width:336px;height:56px;border:2px solid oklch(0.66 0.13 208);border-radius:10px;background:#11182A;overflow:visible}
.l05-track{position:absolute;top:9px;left:8px;display:flex;gap:9px;animation:l05push 7s cubic-bezier(.45,0,.15,1) infinite}
.l05-tk{flex:none;width:56px;height:36px;display:flex;align-items:center;justify-content:center;font-family:var(--font-mono);font-size:13px;color:#EAEEF8;background:#1E2740;border:1.5px solid #3A4560;border-radius:8px}
.l05-new{position:absolute;top:9px;left:272px;color:#0B0F1A;background:oklch(0.66 0.13 208);border:none;opacity:0;animation:l05new 7s cubic-bezier(.45,0,.15,1) infinite}
.l05-old{animation:l05fall 7s cubic-bezier(.45,0,.15,1) infinite;z-index:3}
@keyframes l05push{0%,16%{transform:translateX(0)}40%,100%{transform:translateX(-65px)}}
@keyframes l05new{0%,16%{opacity:0;transform:translateX(70px)}40%,100%{opacity:1;transform:translateX(0)}}
@keyframes l05fall{0%,16%{opacity:1;color:#EAEEF8;background:#1E2740;transform:translate(0,0) rotate(0)}40%{opacity:.9;color:#B9C2DA;transform:translate(0,0) rotate(0)}54%{opacity:.9;transform:translate(0,2px) rotate(-3deg)}72%{opacity:.6;transform:translate(-20px,54px) rotate(-14deg)}74%,100%{opacity:.5;color:#9AA6C4;background:#161E33;transform:translate(-24px,58px) rotate(-15deg)}}
.l05-drop{position:absolute;left:-6px;top:70px;font-family:var(--font-mono);font-size:11px;color:#7A839E;opacity:0;animation:l05drop 7s ease-out infinite}
@keyframes l05drop{0%,66%{opacity:0}78%,90%{opacity:1}100%{opacity:0}}
.l05-cap{font-family:var(--font-mono);font-size:12px;color:#B9C2DA;letter-spacing:.04em}
.l05-cap b{color:oklch(0.66 0.13 208);font-weight:500}
@media (prefers-reduced-motion:reduce){.l05-scene,.l05-track,.l05-new,.l05-old,.l05-drop{animation:none}.l05-track{transform:translateX(-65px)}.l05-new{opacity:1;transform:none}.l05-old{opacity:.5;transform:translate(-24px,58px) rotate(-15deg)}.l05-drop{opacity:1}.l05-scene{opacity:1}}
</style>

## Miten tieto putoaa ulos ikkunasta

Konteksti-ikkunan täyttyminen noudattaa FIFO-periaatetta (First In, First Out) — ensimmäinen sisään, ensimmäinen ulos. Jos aloitat keskustelun antamalla paljon kontekstia ja sitten kysyt 20 kertaa peräkkäin, kunnes keskustelussa on 120 000 tokenia, alkuperäinen kontekstisi on jo kadonnut. Mallilla on käytössään vain viimeiset muutamat kysymys–vastaus-parit ja hieman muuta kontekstia.

Tämä voi johtaa häiritseviin tilanteisiin. Olet saattanut sanoa alussa: "Vastaa aina suomeksi, älä englanniksi", mutta 50 viestin jälkeen malli alkaa vastata englanniksi, koska se on unohtanut rajauksesi. Tai olet antanut tarkan tyyliesimerkin keskustelun alussa, mutta myöhemmin malli kirjoittaa eri tyylillä, koska se ei enää näe esimerkkiä.

Tiedon putoaminen voi myös muuttaa keskustelun sävyä. Jos olet aluksi "opiskelija, joka oppii", mutta 30 viestin jälkeen tämä rooli unohtuu, malli saattaa alkaa pitää sinua asiantuntijana ja antaa hyvin teknisiä vastauksia ilman selityksiä.

> **Pysähdy hetkeksi:** Ajattele pitkää projektin debuggaamista. Mitä tärkeää tietoa malli voisi unohtaa niin, että se alkaisi antaa vääriä neuvoja?

## Kuinka kontekstia tiivistetään, pilkotaan ja rakennetaan uudelleen

Ammattilaisena sinun täytyy hallita konteksti-ikkunaa. Kuten olemme jo aiemmin oppineet, on kolme päästrategiaa: tiivistys, pilkkominen ja ankkurointi. Nämä ovat perustyökaluja, joita tarvitset jokaisen projektin parissa työskennellessäsi.

Käytännön työssä näitä strategioita käytetään yhdessä. Jos sinulla on suuri projekti, joka kestää useita päiviä, ankkuroi olennainen tieto joka päivä, pilko tehtävät pienemmiksi ja tiivistä edellisten päivien tulokset.

Palaamme näihin strategioihin myöhemmin, kun opimme, kuinka agentit hallitsevat muistiaan.

> **Pysähdy hetkeksi:** Ajattele omaa projektia, joka kestää viikon tai pidempään. Miten jakaisit sen osiin, jotta konteksti-ikkuna ei koskaan täyttyisi?

## Kun konteksti katoaa — mitä todella tapahtuu

Tähän asti olemme puhuneet konteksti-ikkunasta teoreettisesti. Nyt katsotaan, mitä tapahtuu käytännössä, kun tärkeä tieto putoaa ikkunasta — ja malli ei kerro sinulle siitä.

Kuvittele seuraava tilanne. Aloitat keskustelun tekoälyn kanssa ja annat selkeän rajauksen: "Kirjoitamme yhdessä novellia. Päähenkilön nimi on Aino, tarina sijoittuu 1920-luvun Suomeen, ja tyyli on vakava. Älä lisää tarinaan nykyaikaisia laitteita."

Ensimmäiset 10 vastausta ovat erinomaisia. Malli muistaa rajaukset, pitää tyylin vakavana ja kirjoittaa ajan kuvaukseen sopivasti.

Mutta 25 viestin jälkeen kysyt: "Miten kohtaus jatkuu?" Malli kirjoittaa Ainon selailemaan puhelinta ja vaihtaa tyylin kepeäksi — koska se on unohtanut alkuperäisen rajauksesi. Se ei kerro, etteikö muista. Se ei sano "huomaa, etten enää muista alkuperäistä kontekstiasi". Se yksinkertaisesti vastaa parhaansa mukaan sillä tiedolla, joka sillä on jäljellä.

Tämä on konteksti-ikkunan vaarallisin piirre: **malli ei kerro, kun se unohtaa**. Se ei anna virheilmoitusta. Se ei sano "konteksti on kadonnut". Se vain alkaa antaa vastauksia, jotka eivät enää noudata alkuperäisiä rajauksia.

Käytännön työssä tämä voi johtaa vakaviin virheisiin. Esitelmän sävy lipsahtaa väärään suuntaan. Asiakkaalle lähetetty teksti rikkoo sovittua ohjeistusta. Käännös vaihtaa kieltä kesken kaiken. Ja koska vastaukset ovat yhtä sujuvia kuin aiemmin, saatat huomata virheen vasta liian myöhään.

Oikea ammattilainen ei luota siihen, että malli muistaa. Hän tarkistaa, huomaa poikkeaman ja korjaa tilanteen — joko toistamalla ankkurin tai aloittamalla uuden keskustelun.

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

## Yhteenveto

Konteksti-ikkuna on tekninen raja, joka määrittää, kuinka paljon tekstiä tekoäly voi käsitellä yhdessä keskustelussa. Vanha tieto putoaa ulos, kun ikkuna täyttyy. Ammattilaisena hallitset ikkunaa kolmella tavalla: tiivistämällä vanhoja tekstejä, pilkkomalla projektit pienempiin osiin ja ankkuroimalla olennaisen tiedon jokaiseen viestiin. Näillä menetelmillä voit johtaa pitkiä, monimutkaisia projekteja tekoälyn kanssa ilman, että mallin muisti pettää. Konteksti-ikkunan ymmärtäminen on avain siihen, että tekoälystä tulee luotettava työkaveri eikä epävakaa avustaja.

Seuraavalla tunnilla laajennat näkökulmaasi: tekoäly voi käsitellä enemmän kuin pelkkää tekstiä — kuvia, ääntä, videota.

---
