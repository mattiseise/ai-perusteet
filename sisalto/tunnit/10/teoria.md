# Kilpailuta tekoälyt — vertaa ennen kuin valitset

## Johdanto: vertailu on koe, ei mielipidekysymys

Tekoälypalvelut muuttuvat nopeasti. Yksittäinen malli, ominaisuus tai hinta voi vaihtua, mutta hyvän vertailun periaate säilyy. Siksi tällä tunnilla ei opetella ulkoa, mikä tuote on ”paras”. Opit rakentamaan pienen vertailukokeen, jonka perusteella voit valita tehtävään sopivan työkalun.

Vertailun lähtökohta on aina tehtävä. Sama palvelu voi onnistua hyvin yhdessä työssä ja heikosti toisessa. Työkalun maine, tuttuus tai sujuva vastaustyyli eivät vielä osoita, että se täyttää käyttötarkoituksen.

> **Tunnin ydinkysymys:** Millä samalla aineistolla, samoilla ehdoilla ja ennalta päätetyillä kriteereillä osoitat työkalun sopivuuden?

<figure class="ai-demo"><span class="ai-demo__tag" id="l10-t"><i aria-hidden="true">// </i>sokkovertailu: portti → lukitse → pisteytä → paljasta vasta lopuksi</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:346px">
  <div class="l10-wrap" data-once role="img" aria-labelledby="l10-t" aria-describedby="l10-d">
    <span class="sr-only" id="l10-d">Sokkovertailun neljä askelta. Ensin tarkistetaan porttiehdot: saako aineistoa käyttää palvelussa ja täyttyvätkö pakolliset ehdot — muuten työkalua ei pisteytetä. Sitten kriteerit lukitaan, vastaukset pisteytetään sokkona havaintoineen, ja merkit paljastetaan vasta lopuksi: A eli uusi työkalu voitti tutun — näyttö ratkaisi.</span>
    <span class="l10-hd">SOKKOVERTAILU</span>
    <span class="l10-step s0"><b class="l10-sa a0"></b><b class="l10-sd d0"></b>0 · PORTTI</span>
    <span class="l10-step s1"><b class="l10-sa a1"></b><b class="l10-sd d1"></b>1 · LUKITSE</span>
    <span class="l10-step s2"><b class="l10-sa a2"></b><b class="l10-sd d2"></b>2 · PISTEYTÄ</span>
    <span class="l10-step s3"><b class="l10-sa a3"></b><b class="l10-sd d3"></b>3 · PALJASTA</span>
    <span class="l10-gate">portti: aineisto sallittu <b class="g1">✓</b> · pakolliset ehdot <b class="g2">✓</b> — muuten ei pisteytetä</span>
    <div class="l10-kp"><i class="l10-ph">KRITEERIT</i><svg class="l10-lock" aria-hidden="true" width="14" height="14" viewBox="0 0 24 24"><path fill="#7FD0A8" d="M12 2a5 5 0 0 0-5 5v3H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2h-1V7a5 5 0 0 0-5-5zm-3 8V7a3 3 0 1 1 6 0v3H9z"/></svg>
      <span class="l10-kw k1">sisältö</span><span class="l10-kw k2">rakenne</span><span class="l10-kw k3">kieli</span>
      <em class="l10-kn">lukittu ennen katselua</em></div>
    <div class="l10-card cA"><i class="l10-ph pha">VASTAUS A</i><span class="l10-id"><b class="q">?</b><b class="nm nma">UUSI</b></span>
      <span class="l10-cr"><b class="l10-m mA1">✓</b> sisältö</span>
      <span class="l10-cr"><b class="l10-m mA2">✓</b> rakenne</span>
      <span class="l10-cr"><b class="l10-m mA3">✓</b> kieli</span>
      <span class="l10-sc scA">3/3</span></div>
    <div class="l10-card cB"><i class="l10-ph pha">VASTAUS B</i><span class="l10-id"><b class="q">?</b><b class="nm nmb">TUTTU</b></span>
      <span class="l10-cr"><b class="l10-m mB1">✓</b> sisältö</span>
      <span class="l10-cr"><b class="l10-m x mB2">✗</b> rakenne</span>
      <span class="l10-cr"><b class="l10-m x mB3">✗</b> kieli</span>
      <em class="l10-note">✗ rakenne: välivaiheet puuttuvat</em>
      <span class="l10-sc x scB">1/3</span>
      <em class="l10-mic">tuttu ≠ voittaja</em></div>
    <span class="l10-res">Tässä tehtävässä: A — näyttö ratkaisi, ei merkki</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Reilu vertailu on järjestys: porttiehdot ensin — jos aineistoa ei saa käyttää palvelussa tai pakollinen ehto ei täyty, työkalua ei pisteytetä lainkaan. Sitten kriteerit lukitaan, pisteytys tehdään merkkiä näkemättä havaintoineen ja alkuperä paljastetaan vasta lopuksi. Tulos pätee tähän tehtävään, ei kaikkeen.</figcaption></figure>
<style>
.l10-wrap{position:relative;width:560px;height:330px;font-family:var(--font-mono);animation:l10w 21s 1 forwards}
.l10-hd{position:absolute;left:0;top:5px;font-size:12px;font-weight:700;letter-spacing:.08em;color:#EAEEF8}
.l10-step{position:absolute;top:0;height:26px;box-sizing:border-box;font-size:12px;font-weight:700;color:#B9C2DA;border:1px solid #2B3552;border-radius:999px;display:flex;align-items:center;justify-content:center;background:#0E1524;overflow:hidden;padding:0 4px}
.l10-step.s0{left:148px;width:92px}.l10-step.s1{left:246px;width:100px}.l10-step.s2{left:352px;width:102px}.l10-step.s3{left:460px;width:100px}
.l10-sa,.l10-sd{position:absolute;inset:-1px;border-radius:999px;opacity:0}
.l10-sa{border:1.5px solid #46C7CF}
.l10-sd{border:1.5px solid #7FD0A8;background:rgba(127,208,168,.1)}
.l10-sa.a0{animation:l10a0 21s 1 forwards}.l10-sd.d0{animation:l10d0 21s 1 forwards}
.l10-sa.a1{animation:l10a1 21s 1 forwards}.l10-sd.d1{animation:l10d1 21s 1 forwards}
.l10-sa.a2{animation:l10a2 21s 1 forwards}.l10-sd.d2{animation:l10d2 21s 1 forwards}
.l10-sa.a3{animation:l10a3 21s 1 forwards}.l10-sd.d3{animation:l10d3 21s 1 forwards}
.l10-gate{position:absolute;left:0;top:34px;width:560px;box-sizing:border-box;text-align:center;font-size:12px;color:#B9C2DA;border:1px dashed #4A5677;border-radius:9px;padding:5px 8px;opacity:0;animation:l10gate 21s 1 forwards}
.l10-gate b{color:#7FD0A8;opacity:0}
.l10-gate .g1{animation:l10g1 21s 1 forwards}
.l10-gate .g2{animation:l10g2 21s 1 forwards}
.l10-kp{position:absolute;left:0;top:70px;width:150px;height:210px;box-sizing:border-box;background:#11182A;border:1.5px solid #2B3552;border-radius:12px;padding:9px 12px;animation:l10kp 21s 1 forwards}
.l10-ph{display:block;font-style:normal;font-size:12px;font-weight:700;letter-spacing:.06em;color:#C9B7F1}
.l10-ph.pha{color:#EAEEF8}
.l10-lock{position:absolute;right:10px;top:9px;animation:l10lock 21s 1 forwards}
.l10-kw{display:block;margin-top:12px;font-size:12px;line-height:1.2;color:#EAEEF8;opacity:0}
.l10-kw.k1{animation:l10k1 21s 1 forwards}.l10-kw.k2{animation:l10k2 21s 1 forwards}.l10-kw.k3{animation:l10k3 21s 1 forwards}
.l10-kn{position:absolute;left:12px;bottom:9px;width:126px;font-style:normal;font-size:12px;line-height:1.25;color:#7FD0A8;opacity:0;animation:l10kn 21s 1 forwards}
.l10-card{position:absolute;top:70px;width:190px;height:210px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:9px 12px}
.l10-card.cA{left:162px}.l10-card.cB{left:364px}
.l10-id{position:absolute;right:9px;top:7px;width:48px;height:22px}
.l10-id b{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;border-radius:6px}
.l10-id .q{color:#C9B7F1;border:1.5px dashed #C9B7F1;animation:l10q 21s 1 forwards}
.l10-id .nm{color:#0B0F1A;opacity:0}
.l10-id .nma{background:#46C7CF;animation:l10nm 21s 1 forwards}
.l10-id .nmb{background:#C9B7F1;animation:l10nm 21s 1 forwards}
.l10-cr{display:block;margin-top:12px;font-size:12px;line-height:1.2;color:#B9C2DA}
.l10-m{display:inline-block;width:16px;font-style:normal;font-weight:700;color:#7FD0A8;opacity:0;transform:scale(.4)}
.l10-m.x{color:#FFD79A;font-size:13px}
.l10-m.mA1{animation:l10mA1 21s 1 forwards}.l10-m.mA2{animation:l10mA2 21s 1 forwards}.l10-m.mA3{animation:l10mA3 21s 1 forwards}
.l10-m.mB1{animation:l10mB1 21s 1 forwards}.l10-m.mB2{animation:l10mB2 21s 1 forwards}.l10-m.mB3{animation:l10mB3 21s 1 forwards}
.l10-note{position:absolute;left:12px;top:128px;width:164px;font-style:normal;font-size:12px;line-height:1.25;color:#FFD79A;opacity:0;animation:l10note 21s 1 forwards}
.l10-sc{position:absolute;left:12px;bottom:9px;font-size:14px;font-weight:700;color:#7FD0A8;opacity:0;animation:l10sc 21s 1 forwards}
.l10-sc.x{color:#FFD79A}
.l10-mic{position:absolute;right:12px;bottom:11px;font-style:normal;font-size:12px;color:#C9B7F1;opacity:0;animation:l10mic 21s 1 forwards}
.l10-res{position:absolute;left:0;top:296px;width:560px;text-align:center;font-size:12.5px;font-weight:600;color:#FFD79A;opacity:0;animation:l10res 21s 1 forwards}
@keyframes l10w{0%{opacity:0}3%{opacity:1}100%{opacity:1}}
@keyframes l10a0{0%,3%{opacity:0}4.5%{opacity:1}12%{opacity:1}14%,100%{opacity:0}}
@keyframes l10d0{0%,12%{opacity:0}14%,100%{opacity:1}}
@keyframes l10gate{0%,3.5%{opacity:0;transform:translateY(-5px)}6.5%,100%{opacity:1;transform:none}}
@keyframes l10g1{0%,7%{opacity:0}9.5%,100%{opacity:1}}
@keyframes l10g2{0%,10%{opacity:0}12.5%,100%{opacity:1}}
@keyframes l10a1{0%,14%{opacity:0}15.5%{opacity:1}32%{opacity:1}34%,100%{opacity:0}}
@keyframes l10d1{0%,32%{opacity:0}34%,100%{opacity:1}}
@keyframes l10a2{0%,34%{opacity:0}36%{opacity:1}69%{opacity:1}71%,100%{opacity:0}}
@keyframes l10d2{0%,69%{opacity:0}71%,100%{opacity:1}}
@keyframes l10a3{0%,71%{opacity:0}73%{opacity:1}93%{opacity:1}95%,100%{opacity:0}}
@keyframes l10d3{0%,93%{opacity:0}95%,100%{opacity:1}}
@keyframes l10kp{0%,29%{border-color:#2B3552}32%,100%{border-color:#7FD0A8}}
@keyframes l10lock{0%,28%{transform:scale(1)}30%{transform:scale(1.35)}32%,100%{transform:scale(1)}}
@keyframes l10k1{0%,16%{opacity:0;transform:translateX(-8px)}19.5%,100%{opacity:1;transform:none}}
@keyframes l10k2{0%,20%{opacity:0;transform:translateX(-8px)}23.5%,100%{opacity:1;transform:none}}
@keyframes l10k3{0%,24%{opacity:0;transform:translateX(-8px)}27.5%,100%{opacity:1;transform:none}}
@keyframes l10kn{0%,31%{opacity:0}34%,100%{opacity:1}}
@keyframes l10mA1{0%,37%{opacity:0;transform:scale(.4)}39%,100%{opacity:1;transform:scale(1)}}
@keyframes l10mB1{0%,39%{opacity:0;transform:scale(.4)}41%,100%{opacity:1;transform:scale(1)}}
@keyframes l10mA2{0%,45%{opacity:0;transform:scale(.4)}47%,100%{opacity:1;transform:scale(1)}}
@keyframes l10mB2{0%,47%{opacity:0;transform:scale(.4)}49%,100%{opacity:1;transform:scale(1)}}
@keyframes l10note{0%,50%{opacity:0}53%,100%{opacity:1}}
@keyframes l10mA3{0%,55%{opacity:0;transform:scale(.4)}57%,100%{opacity:1;transform:scale(1)}}
@keyframes l10mB3{0%,57%{opacity:0;transform:scale(.4)}59%,100%{opacity:1;transform:scale(1)}}
@keyframes l10sc{0%,63%{opacity:0}66%{opacity:1}89%{transform:scale(1)}91%{transform:scale(1.08)}93%,100%{opacity:1;transform:scale(1)}}
@keyframes l10q{0%,73%{opacity:1}78%,100%{opacity:0}}
@keyframes l10nm{0%,73%{opacity:0;transform:scale(.6)}78%,100%{opacity:1;transform:scale(1)}}
@keyframes l10mic{0%,79%{opacity:0}83%,100%{opacity:1}}
@keyframes l10res{0%,83%{opacity:0}87%,100%{opacity:1}}
@media (prefers-reduced-motion:reduce){
  .l10-wrap,.l10-wrap *{animation:none!important}
  .l10-wrap,.l10-kw,.l10-kn,.l10-sc,.l10-mic,.l10-res,.l10-sd,.l10-id .nm,.l10-gate,.l10-gate b,.l10-note{opacity:1}
  .l10-m{opacity:1;transform:scale(1)}
  .l10-sa,.l10-id .q{opacity:0}
  .l10-kp{border-color:#7FD0A8}
}
</style>

## Määritä ensin päätös

Ennen testiä kirjoita, mitä olet valitsemassa ja mihin käyttöön. ”Vertailen tekoälyjä” on liian väljä tavoite, sillä sen perusteella et vielä tiedä, millaista vastausta olet arvioimassa. Parempi muoto on:

> Valitsen työkalun, jolla muokataan 500 sanan ohje aloittelijalle sopivaksi. Tärkeintä ovat sisällön säilyminen, selkeys ja tarkistettavuus.

Hyvä päätös sisältää:

- todellisen tehtävän
- käyttäjän tai yleisön
- käytettävän aineiston
- hyväksyttävän lopputuloksen
- ehdot, joiden pitää täyttyä ennen laadun vertailua.

Kun nämä asiat on kirjoitettu näkyviin, työkalun ominaisuudet eivät pääse huomaamatta muuttamaan itse tehtävää.

## Erota porttiehdot ja laatukriteerit

Kaikkia työkaluja ei pidä edes ottaa mukaan laadulliseen vertailuun. **Porttiehto** ratkaisee, saako työkalua käyttää tehtävään.

Porttiehtoja voivat olla:

- organisaatio on hyväksynyt palvelun kyseiselle aineistolle
- aineisto mahtuu palvelun käsiteltäväksi
- tarvittava tiedostomuoto tai toiminto on käytettävissä
- käyttäjällä on tarvittava lisenssi ja käyttöoikeus
- palvelun käyttö täyttää saavutettavuuden tai muun pakollisen vaatimuksen

Jos porttiehto ei täyty, työkalu hylätään ennen vastausten pisteytystä. Kaunis vastaus ei korjaa sitä, ettei palveluun saanut syöttää aineistoa.

**Laatukriteeri** kertoo, kuinka hyvin hyväksytty työkalu hoitaa tehtävän. Ohjeen muokkaamisessa voit esimerkiksi tarkastella, säilyvätkö faktat, noudattaako vastaus annettua rakennetta ja sopiiko kieli kohderyhmälle. Tärkeää voi olla myös se, erottuvatko lähteestä saadut tiedot mallin omista päätelmistä ja kuinka paljon jälkikorjausta vastaus vaatii. Valitse kokeeseen 3–5 kriteeriä. Liian pitkä lista hajottaa huomion ja tekee valinnasta helposti mekaanisen pistekilpailun.

## Kirjoita kriteereille havaittavat kuvaukset

Pelkkä numero 1–5 ei kerro, mitä arvioija näki. Kuvaa etukäteen, mitä asteikon päät tarkoittavat.

| Kriteeri | Heikko tulos | Hyvä tulos |
| --- | --- | --- |
| Sisällön säilyminen | Olennaisia asioita puuttuu tai uusia väitteitä ilmestyy | Keskeinen sisältö säilyy eikä uusia faktoja keksitä |
| Kohderyhmälle sopivuus | Sanasto ja oletukset ovat liian vaikeita | Aloittelija ymmärtää tekstin ilman selittämätöntä erikoissanastoa |
| Rakenteen noudattaminen | Pyydetty muoto puuttuu | Vastaus noudattaa sovittua rakennetta |
| Jälkikorjauksen määrä | Tuotos vaatii olennaisen uudelleenkirjoituksen | Tarvitaan vain pieniä tyylikorjauksia |

Näin arvio perustuu näyttöön eikä siihen, mikä vastaus ”tuntuu parhaalta”.

## Hallitse vertailun muuttujat

Reilussa vertailussa pidät olennaiset olosuhteet samoina:

- sama prompti
- sama lähdeaineisto
- sama tavoiteltu vastausmuoto
- uusi keskustelu jokaiselle testille
- kirjattu palvelu, malli tai käyttöympäristö siltä osin kuin tieto on saatavilla
- sama arviointitaulukko.

Näin et vahingossa anna toiselle työkalulle helpompaa tehtävää.

Täydellistä laboratoriokoetta ei tavallisessa käytössä synny. Ilmais- ja maksulliset versiot voivat erota, palvelut voivat käyttää eri oletusasetuksia ja mallit voivat muuttua testien välillä. Nämä erot pitää kirjata rajoituksiksi, ei unohtaa.

Jos vertailet vain yhden kerran, satunnaisuus voi vaikuttaa tulokseen. Tärkeässä valinnassa aja sama koe useammalla edustavalla aineistolla. Tämän tunnin pieni koe opettaa menetelmän; se ei todista työkalun yleistä paremmuutta.

## Arvioi vastaukset sokkona, jos mahdollista

Tuotemerkki synnyttää ennakko-odotuksia. Jos mahdollista, kopioi vastaukset dokumenttiin nimillä **A** ja **B** ennen pisteytystä. Arvioi ensin sisältö ja paljasta palvelut vasta sen jälkeen.

Sokkoutus ei poista kaikkia vinoumia, mutta se vähentää tutun brändin ja käyttöliittymän vaikutusta. Vielä parempi on pyytää toista ihmistä arvioimaan samat vastaukset samoilla kriteereillä ja vertailla havaintoja.

## Älä pyydä yhtä kilpailijaa tuomariksi

Tekoälyä voi käyttää kysymysten esittämiseen tai arviointitaulukon puutteiden etsimiseen. Sille ei kuitenkaan kannata antaa yksin päätösvaltaa siitä, mikä vastaus voitti. Mallin arvio voi suosia tiettyä kirjoitustapaa, olla epäjohdonmukainen tai muuttua promptin mukana.

Ihminen tekee lopullisen päätöksen ja vastaa siitä. Tekoäly voi auttaa haastamaan perustelun:

> ”Mikä havainto taulukostani ei vielä tue johtopäätöstäni?”

Tämä kysymys ohjaa arvioimaan omaa näyttöä sen sijaan, että malli valitsisi työkalun puolestasi.

## Kirjaa myös käytännön työ

Paras tekstivastaus ei aina tarkoita parasta työkalua. Kuvittele, että toinen palvelu tuottaa hieman paremman luonnoksen mutta vaatii aineiston hankalaa kopiointia, erillisiä käyttöoikeuksia ja paljon käsin tehtävää jälkityötä. Silloin pieni laatuero ei ehkä ratkaise valintaa.

Kirjaa siksi myös käytännön työ:

- kuinka helposti aineisto saadaan palveluun ja tulos takaisin
- voiko työn tehdä ilman tarpeetonta kopiointia
- miten käyttöoikeudet ja tiedot hallitaan
- paljonko tuloksen tarkistamiseen ja korjaamiseen kuluu aikaa
- mitä käyttö maksaa todellisella työmäärällä
- pystyykö toinen ihminen dokumentoinnin perusteella toistamaan kokeen.

Nämä eivät ole pysyviä tuotekohtaisia totuuksia. Ne tarkistetaan siinä käyttöympäristössä ja sillä käyttäjätilillä, jota päätös koskee.

## Tee rajattu johtopäätös

Hyvä johtopäätös ei kuulu: ”Työkalu A on paras tekoäly.” Se kuuluu:

> Tässä kokeessa työkalu A sopi paremmin aloittelijan ohjeen muokkaamiseen, koska se säilytti kaikki viisi sisältökohtaa ja noudatti rakennetta. Työkalu B vaati kahden puuttuneen kohdan palauttamisen. Koe ei osoita, kumpi on parempi muissa tehtävissä.

Johtopäätös kertoo:

- mihin tehtävään valinta koskee
- mikä havainto ratkaisi valinnan
- mitkä porttiehdot täyttyivät
- mitä kokeesta ei voi päätellä
- milloin nopeasti muuttuvassa käyttöympäristössä testi on syytä uusia.

## Yhteenveto

Työkalun valinta on pieni tutkimusprosessi:

1. määritä tehtävä ja päätös
2. tarkista porttiehdot
3. päätä laatukriteerit ennen vastausten näkemistä
4. käytä samaa promptia ja aineistoa
5. arvioi havaittava näyttö, mielellään sokkona
6. kirjaa käytännön työ ja rajoitukset
7. tee tehtäväkohtainen, rajattu johtopäätös

Tällä menetelmällä vertailu kestää paremmin myös sen, että palvelut ja mallit muuttuvat.

> **Lopuksi pohdittavaksi:** Mikä omassa vertailussasi voisi näyttää työkalujen erolta, vaikka se johtuisi todellisuudessa erilaisesta tilistä, asetuksesta tai satunnaisuudesta?

---

## Lähteet ja tarkistuspäivä

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST: Towards a Standard for Identifying and Managing Bias in Artificial Intelligence](https://www.nist.gov/publications/towards-standard-identifying-and-managing-bias-artificial-intelligence)

Tarkistettu 20.7.2026.
