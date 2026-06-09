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

<figure class="ai-demo"><span class="ai-demo__tag">// konteksti-ikkuna on täynnä — vanhin putoaa</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center">
  <div class="l05-scene">
    <span class="l05-side">uusi sisään →</span>
    <div class="l05-win">
      <div class="l05-track">
        <span class="l05-tk">alku</span><span class="l05-tk">tausta</span><span class="l05-tk">ohje</span><span class="l05-tk">kysymys</span><span class="l05-tk">vastaus</span><span class="l05-tk l05-new">uusin</span>
      </div>
    </div>
    <div class="l05-fallen">alku ↓ ei enää näkyvissä</div>
    <span class="l05-cap">ikkuna: 5 muistipaikkaa · TÄYNNÄ</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Konteksti-ikkuna on kiinteän kokoinen. Kun uusi tieto työntyy sisään oikealta, vanhin putoaa ulos vasemmalta — eikä malli kerro sinulle siitä.</figcaption></figure>
<style>
.l05-scene{position:relative;width:330px;display:flex;flex-direction:column;align-items:center;gap:10px;animation:l05scene 13s ease-in-out infinite}
@keyframes l05scene{0%,4%{opacity:0}8%,94%{opacity:1}100%{opacity:0}}
.l05-side{font-family:var(--font-mono);font-size:10px;color:oklch(0.66 0.13 208);align-self:flex-end;margin-right:6px}
.l05-win{position:relative;width:284px;height:46px;border:1px solid #2A3450;border-radius:8px;overflow:hidden;background:#11182A;-webkit-mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent)}
.l05-track{position:absolute;top:8px;left:8px;display:flex;gap:8px;animation:l05push 13s ease-in-out infinite}
.l05-tk{flex:none;width:46px;text-align:center;font-family:var(--font-mono);font-size:9.5px;color:#C7CEE6;background:#1A2236;border:1px solid #2A3450;border-radius:6px;padding:7px 0}
.l05-new{color:#0B0F1A;background:oklch(0.66 0.13 208);border-color:transparent;opacity:0;animation:l05newin 13s ease-in-out infinite}
@keyframes l05push{0%,30%{transform:translateX(0)}48%,92%{transform:translateX(-54px)}100%{transform:translateX(-54px)}}
@keyframes l05newin{0%,30%{opacity:0}48%,92%{opacity:1}100%{opacity:1}}
.l05-fallen{font-family:var(--font-mono);font-size:9.5px;color:#69728F;border:1px dashed #3A445F;border-radius:6px;padding:4px 9px;align-self:flex-start;margin-left:6px;opacity:0;animation:l05fall 13s ease-in-out infinite}
@keyframes l05fall{0%,30%{opacity:0;transform:translateY(-14px)}44%{opacity:1;transform:translateY(0)}92%{opacity:1;transform:translateY(0)}100%{opacity:0}}
.l05-cap{font-family:var(--font-mono);font-size:10px;color:#8B94B3;letter-spacing:.06em}
@media (prefers-reduced-motion:reduce){.l05-scene,.l05-track,.l05-new,.l05-fallen{animation:none}.l05-track{transform:translateX(-54px)}.l05-new,.l05-fallen{opacity:1}.l05-scene{opacity:1}}
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
