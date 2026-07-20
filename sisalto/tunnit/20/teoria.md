# Automaatio vai autonomia? — milloin agentti kannattaa?

## Johdanto

Nyt kun tiedät, mikä **agentti** on, seuraava kysymys on ilmeinen: milloin agenttia kannattaa käyttää? Vastaus ei ole ”aina”. Agentti tuo mukanaan monimutkaisuutta, kustannuksia ja riskejä. Usein tavallinen **työnkulku** tai jopa yksinkertainen **promptaus** riittää.

Kun rakennat oppitunneilla omaa agenttiasi n8n:llä, tämän asian ymmärtäminen auttaa sinua tekemään parempia arkkitehtuuripäätöksiä. Kun tiedät, milloin agentti todella kannattaa, voit suunnitella projektisi järkevämmin.

Kuvittele, että vastaat asiakaspalvelusta. Joka päivä tulee 50 yhteydenottoa. Joku ehdottaa: ”Tehdään agentti, joka käsittelee nämä automaattisesti!” Ajatus kuulostaa hyvältä, kunnes huomaat todellisuuden: agentin rakentaminen, testaaminen ja ylläpito kestävät kuukauden ja maksavat 10 000 euroa. Ehkä yksinkertainen työnkulku, joka ohjaa yhteydenotot automaattisesti oikealle henkilölle, antaisi saman hyödyn murto-osalla kustannuksista.

Tässä oppitunnissa opit käyttämään **päätöspuuta** eli ajattelumallia, joka auttaa valitsemaan oikean ratkaisun. Milloin promptaus riittää? Milloin tarvitset työnkulun? Milloin agentti todella kannattaa rakentaa?

> **Pysähdy hetkeksi:** Ajattele omaa tulevaa työtäsi. Mitä toistuvia ja monivaiheisia tehtäviä siinä voi olla? Mitkä niistä voisivat toimia työnkulkuina, ja mitkä vaatisivat agentin?

> **Harness-kytkentä:** Agentti ei ole pelkkä kyvykäs kielimalli, vaan kielimallin ja sitä ympäröivän harnessin muodostama järjestelmä. Harness antaa tavoitteelle rakenteen, hallitsee tilaa ja työkaluja, rajaa oikeudet sekä huolehtii seurannasta. Jos tehtävä ei tarvitse näitä vastuita, promptaus tai tavallinen työnkulku on yleensä agenttia järkevämpi.

## Kolmen tason kustannukset ja hyödyt

Automatisoinnissa on kolme perusvälinettä, ja jokaisella niistä on omat kustannuksensa ja hyötynsä. Kun päätät, mitä rakennat, sinun täytyy ymmärtää, mitä kukin väline käytännössä maksaa ja mitä hyötyä se tuottaa.

Ensimmäinen väline on **yksinkertainen promptaus**. Käyttäjä kirjoittaa esimerkiksi ChatGPT:lle kysymyksen, ja tekoäly vastaa. Käyttäjä omistaa prosessin alusta loppuun. Kustannus on pieni: lähinnä käyttäjän aika ja mahdollinen ChatGPT-tilaus. Hyötynä on nopeus, helppous ja se, ettei ratkaisua tarvitse ylläpitää. Rajoitus on kuitenkin selvä: käyttäjän täytyy aloittaa prosessi itse. Jos sähköpostiviesteistä tarvitaan yhteenvetoja, jonkun täytyy kopioida viestit manuaalisesti ChatGPT:hen ja odottaa vastausta.

Toinen väline on **työnkulku** eli workflow. Kun sähköposti saapuu asiakaspalveluun, automaattinen työnkulku tarkistaa, mitä avainsanoja viesti sisältää. Sisältääkö se sanan ”lasku”? Viesti ohjataan henkilölle A. Sisältääkö se sanan ”palautus”? Viesti ohjataan henkilölle B. Eikö se sisällä mitään näistä? Viesti jätetään saapuneisiin. Työnkulku tekee nämä päätökset **joka kerta** ilman ihmisen osallistumista. Kustannus on suurempi kuin promptauksessa: sinun täytyy suunnitella logiikka, testata se ja ylläpitää sitä, kun avainsanat tai säännöt muuttuvat. Hyöty on kuitenkin merkittävä: ihmiset säästävät aikaa päivittäin, ja prosessi toimii johdonmukaisesti. Rajoitus on se, että säännöt ovat jäykkiä. Jos uusi tilanne ei sovi etukäteen kirjoitettuihin sääntöihin, työnkulku voi jumittua.

Kolmas väline on **agentti**. Asiakaspalvelun agentti voi lukea sähköposteja, analysoida niiden sävyä, etsiä vastaavia aiempia tapauksia tietokannasta ja **päättää**, onko se riittävän varma lähettämään automaattisen vastauksen vai pitäisikö viesti ohjata ihmiselle. Agentti ei siis vain seuraa yhtä ennalta määrättyä polkua, vaan arvioi tilanteen sille asetetuissa rajoissa. Jos asiakas on vihainen, agentti voi valita varovaisemman toimintatavan. Jos harness hakee aiemman samankaltaisen tapauksen agentin kontekstiin, kielimalli voi ottaa sen huomioon. Tämä ei tarkoita, että malli olisi oppinut tapauksesta itsestään.

Agentin kustannus on suuri. Kehittäminen on monimutkaisempaa, koska logiikka on dynaamista. Testaus vie paljon aikaa, koska agentti voi tuottaa odottamattomia tuloksia. Ylläpito on jatkuvaa, koska sinun täytyy valvoa, mitä agentti tekee ja millaisia päätöksiä se tekee. Agentin hyöty on siinä, että se pystyy käsittelemään monimutkaisia ja poikkeavia tapauksia, joita työnkulku ei osaa ratkaista. Rajoitus on korkea hinta: agentista täytyy saada merkittävä hyöty suhteessa siihen, mitä sen rakentaminen ja ylläpito maksavat.

> **Pysähdy hetkeksi:** Miksi olisit valmis maksamaan enemmän agentin rakentamisesta? Mitä sellaista etua agentti antaa, jota ei voi saavuttaa pelkällä työnkululla?

## Kuusi kysymystä päätöksenteon tueksi

Kun tarkastelet automatisoitavaa tehtävää, kysy seuraavat kuusi kysymystä **järjestyksessä**. Ne auttavat sinua valitsemaan oikean välineen.

**Ensimmäinen kysymys: Toistuuko tehtävä?** Jos tehtävä on kertaluontoinen tai sitä tehdään hyvin harvoin, sitä ei yleensä kannata automatisoida. Automatisoinnin rakentamiseen kuluu todennäköisesti enemmän aikaa kuin itse tehtävän tekemiseen. Jos tehtävä taas toistuu joka päivä, joka tunti tai jopa useita kertoja minuutissa, automatisointi alkaa kannattaa. Jopa yksinkertainen työnkulku voi säästää merkittävästi aikaa, kun sitä käytetään tuhansia kertoja vuodessa.

**Toinen kysymys: Onko tehtävä yksinkertainen vai monimutkainen?** Yksinkertaiset tehtävät, joissa on yksi tai kaksi vaihetta ja selkeät säännöt, ratkeavat usein työnkululla. Esimerkiksi ohje ”kun laskua ei ole vastaanotettu, siirrä asia kansioon Odottaa” on niin suoraviivainen, että työnkulku riittää. Monimutkaisissa tehtävissä tilanne on toinen. Jos tehtävä sisältää useita vaiheita, ehdollisia päätöksiä, oppimista ja mukautumista, työnkulun jäykät säännöt eivät välttämättä enää riitä. Tämä on merkki siitä, että **päättely** eli agentin keskeinen ominaisuus voisi tuoda lisäarvoa.

**Kolmas kysymys: Onko eteneminen ennalta määrätty vai pitääkö seuraava toiminto valita tilanteen perusteella?** Jos sama asia tehdään joka kerta samalla tavalla, työnkulku on yleensä riittävä. Agentista voi olla hyötyä silloin, kun kielimallin pitää tulkita uusi tilanne, valita käytettävä työkalu, arvioida työkalun tulos ja päättää seuraava toiminto. Myös agentin toimintaa rajaavat säännöt, oikeudet ja hyväksyntäportit. Ero ei siis ole siinä, että työnkululla on sääntöjä ja agentilla ei, vaan siinä, kuka tai mikä valitsee etenemisen rajojen sisällä.

**Neljäs kysymys: Kuka maksaa hinnan?** Jos käyttäjä maksaa pienen summan, kuten tekoälypalvelun tilauksen, kokeileminen on helppoa ja riski on pieni. Jos taas organisaatio maksaa tuhansia tai kymmeniä tuhansia euroja agentin rakentamisesta, päätös on paljon suurempi. Silloin tarvitaan vahvat perusteet ja realistinen arvio siitä, että investointi maksaa itsensä takaisin.

**Viides kysymys: Mitkä ovat epäonnistumisen kustannukset?** Jos agentti tekee virheen eikä mitään vakavaa tapahdu, riski voi olla hyväksyttävä. Esimerkiksi sähköposti voi mennä väärään kansioon, mutta ihminen huomaa sen ja korjaa virheen. Jos epäonnistumisen seuraukset ovat suuret, tilanne muuttuu. Rahaa voidaan menettää, asiakkaita voidaan menettää tai ihminen voi joutua vaaraan. Tällöin agenttia täytyy valvoa hyvin huolellisesti, ja valvonta nostaa ylläpitokustannuksia merkittävästi. Joissain tapauksissa korkeat epäonnistumisen kustannukset tekevät agentin rakentamisesta kannattamatonta.

**Kuudes kysymys: Onko ihmisen valvonta mahdollista?** Jos ihminen voi valvoa agentin päätöksiä ja puuttua toimintaan, kun jokin menee pieleen, riski on hallittavampi. Agentti voi pyytää ihmisen apua vaikeissa tilanteissa, jolloin riskien hallinta on mahdollista. Jos valvonta on mahdotonta, agentin täytyy toimia lähes täydellisesti. Tämä on harvinaisen kallista rakentaa ja ylläpitää.

## Käytännön päätöspuu kolmessa tarinassa

Katsotaan seuraavaksi kolmea käytännön tilannetta ja sitä, mitä kuusi kysymystä niissä ohjaavat tekemään.

<figure class="ai-demo"><span class="ai-demo__tag" id="l20-t"><i aria-hidden="true">// </i>kolme toteutustapaa, sama tehtävävirta — vaihtelu ratkaisee valinnan</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:398px">
  <div class="l20-wrap" data-once role="img" aria-labelledby="l20-t" aria-describedby="l20-d">
    <span class="sr-only" id="l20-d">Kolme toteutustapaa samalle tehtävävirralle: rutiinissa työnkulku riittää; agenttia eli kielimallia harnessin kanssa kannattaa harkita, kun toistuva vaihtelu vaatii tilannepäättelyä, rajattuja työkaluja ja ihmisen valvontaa. Monimutkaisempi ei ole automaattisesti parempi.</span>
    <span class="l20-hd">KOLME TOTEUTUSTAPAA — SAMA TEHTÄVÄVIRTA</span>
    <span class="l20-in ia">saapuu: rutiiniviesti ×3</span>
    <span class="l20-in ib">saapuu: poikkeava tapaus</span>
    <div class="l20-ln p1"><b class="l20-nm">PROMPTAUS</b>
      <span class="l20-cost c1">rakentaminen ●○○</span><span class="l20-cost c2">ihmistyö/tapaus ●●●</span>
      <i class="l20-tok tp"></i><span class="l20-hand">SINÄ</span>
      <em class="l20-ds">sinä aloitat ja ohjaat joka kerran</em>
      <span class="l20-tl"><b class="l20-m pm1">✓</b><b class="l20-m pm2">✓</b><b class="l20-m pm3">✓</b><b class="l20-m pm4">✓</b></span></div>
    <div class="l20-ln p2"><b class="l20-nm">TYÖNKULKU</b>
      <span class="l20-cost c1">rakentaminen ●●○</span><span class="l20-cost c2">ihmistyö rutiinissa ●○○</span>
      <i class="l20-tok tw"></i><i class="l20-gate"></i>
      <em class="l20-ds">sama sääntö joka kerta — nopein</em>
      <span class="l20-wx">ei sääntöä → jumittuu</span>
      <span class="l20-tl"><b class="l20-m wm1">✓</b><b class="l20-m wm2">✓</b><b class="l20-m wm3">✓</b><b class="l20-m x wm4">✗</b></span></div>
    <div class="l20-ln p3"><b class="l20-nm">AGENTTI <i class="l20-df">= kielimalli + harness</i></b>
      <span class="l20-cost c1">rakennus + ylläpito ●●●</span><span class="l20-cost c2">valvonta ●●○</span>
      <i class="l20-tok ta"></i><span class="l20-th">arvioi…</span>
      <span class="l20-br">ratkaisee / ohjaa ihmiselle</span>
      <em class="l20-ds">arvioi tilanteen — kallein ylläpitää</em>
      <span class="l20-tl"><b class="l20-m am1">✓</b><b class="l20-m am2">✓</b><b class="l20-m am3">✓</b><b class="l20-m am4">✓</b></span></div>
    <span class="l20-vd va">rutiini → työnkulku riittää</span>
    <span class="l20-vd vb">vaihtelu → harkitse agenttia</span>
    <span class="l20-cnd">monimutkaisempi ≠ parempi — harkitse agenttia, kun toistuva vaihtelu vaatii tilannepäättelyä, rajattuja työkaluja ja ihmisen valvontaa</span>
    
  </div>
</div>
<figcaption class="ai-demo__cap">Sama tehtävävirta, kolme toteutustapaa. Kustannuksilla on kaksi ulottuvuutta: rakentaminen ja ylläpito sekä ihmistyö tapausta kohti. Rutiinissa työnkulku riittää; agenttia (kielimalli + harness) kannattaa harkita, kun toistuva vaihtelu vaatii tilannekohtaista päättelyä, rajattua työkalujen käyttöä ja ihmisen valvomaa toimintaa. Monimutkaisempi ei ole automaattisesti parempi.</figcaption></figure>
<style>
.l20-wrap{position:relative;width:560px;height:384px;font-family:var(--font-mono);animation:l20w 14s 1 forwards}
.l20-hd{position:absolute;left:0;top:2px;font-size:12px;font-weight:700;letter-spacing:.07em;color:#EAEEF8}
.l20-in{position:absolute;right:0;top:0;font-size:12px;font-weight:700;border-radius:999px;padding:3px 10px;opacity:0}
.l20-in.ia{color:#06212A;background:#46C7CF;animation:l20ia 14s 1 forwards}
.l20-in.ib{color:#0B0F1A;background:#FFD79A;animation:l20ib 14s 1 forwards}
.l20-cnd{position:absolute;left:30px;top:340px;width:500px;text-align:center;font-size:12px;line-height:1.35;color:#B9C2DA;opacity:0;animation:l20cnd 14s 1 forwards}
.l20-ln{position:absolute;left:0;width:560px;height:86px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:7px 10px}
.l20-ln.p1{top:30px}.l20-ln.p2{top:122px}.l20-ln.p3{top:214px;border-color:#3D6b6e}
.l20-nm{display:block;font-size:12.5px;color:#EAEEF8}
.l20-df{font-style:normal;font-weight:400;font-size:12px;color:#B9C2DA}
.l20-cost{position:absolute;left:10px;font-size:12px;color:#FFD79A;white-space:nowrap}
.l20-cost.c1{top:24px}
.l20-cost.c2{top:40px}
.l20-ds{position:absolute;left:10px;bottom:7px;font-style:normal;font-size:12px;color:#8B94B3}
.l20-tok{position:absolute;left:170px;top:30px;width:13px;height:13px;border-radius:50%;background:#46C7CF;opacity:0}
.l20-tok.tp{animation:l20tp 14s 1 forwards}
.l20-tok.tw{animation:l20tw 14s 1 forwards}
.l20-tok.ta{animation:l20ta 14s 1 forwards}
.l20-hand{position:absolute;left:236px;top:24px;font-size:12px;color:#EAEEF8;border:1px solid #4A5677;border-radius:7px;padding:3px 7px;background:#0E1524;animation:l20hand 14s 1 forwards}
.l20-gate{position:absolute;left:270px;top:20px;width:0;height:38px;border-left:3px double #7E88A8}
.l20-th{position:absolute;left:236px;top:26px;font-size:12px;color:#C9B7F1;opacity:0;animation:l20th 14s 1 forwards}
.l20-br{position:absolute;right:10px;top:58px;font-size:12px;color:#7FD0A8;opacity:0;animation:l20br 14s 1 forwards}
.l20-wx{position:absolute;left:304px;top:26px;font-size:12px;font-weight:700;color:#FFD79A;opacity:0;animation:l20wx 14s 1 forwards}
.l20-tl{position:absolute;right:10px;top:30px;display:flex;gap:7px}
.l20-m{width:16px;text-align:center;font-size:13px;font-weight:700;color:#7FD0A8;opacity:0;transform:scale(.5)}
.l20-m.x{color:#FFD79A}
.l20-m.pm1{animation:l20s1 14s 1 forwards}.l20-m.pm2{animation:l20s2 14s 1 forwards}.l20-m.pm3{animation:l20s3 14s 1 forwards}.l20-m.pm4{animation:l20p4 14s 1 forwards}
.l20-m.wm1{animation:l20s1 14s 1 forwards}.l20-m.wm2{animation:l20s2 14s 1 forwards}.l20-m.wm3{animation:l20s3 14s 1 forwards}.l20-m.wm4{animation:l20x4 14s 1 forwards}
.l20-m.am1{animation:l20s1 14s 1 forwards}.l20-m.am2{animation:l20s2 14s 1 forwards}.l20-m.am3{animation:l20s3 14s 1 forwards}.l20-m.am4{animation:l20a4 14s 1 forwards}
.l20-vd{position:absolute;top:308px;font-size:12px;font-weight:700;border-radius:7px;padding:3px 9px;opacity:0}
.l20-vd.va{left:0;color:#7FD0A8;border:1.5px solid #7FD0A8;background:rgba(127,208,168,.07);animation:l20va 14s 1 forwards}
.l20-vd.vb{left:216px;color:#C9B7F1;border:1.5px solid #C9B7F1;background:rgba(201,183,241,.07);animation:l20vb 14s 1 forwards}
@keyframes l20w{0%{opacity:0}3%{opacity:1}97%,100%{opacity:1}}
@keyframes l20ia{0%,3%{opacity:0}6%{opacity:1}48%{opacity:1}52%,100%{opacity:0}}
@keyframes l20ib{0%,48%{opacity:0}52%{opacity:1}100%{opacity:1}}
@keyframes l20tp{0%,7%{opacity:0;transform:translateX(0);background:#46C7CF}9%{opacity:1}12%{transform:translateX(60px)}15%{transform:translateX(60px)}20%{transform:translateX(240px)}22%{opacity:0}
  55%{opacity:0;transform:translateX(0);background:#FFD79A}57%{opacity:1}61%{transform:translateX(60px)}64%{transform:translateX(60px)}70%{transform:translateX(240px)}72%,100%{opacity:0;transform:translateX(240px);background:#FFD79A}}
@keyframes l20tw{0%,8%{opacity:0;transform:translateX(0);background:#46C7CF}10%{opacity:1}15%{transform:translateX(240px)}17%{opacity:0}
  56%{opacity:0;transform:translateX(0);background:#FFD79A}58%{opacity:1}62%{transform:translateX(88px)}63%{transform:translateX(85px)}64%{transform:translateX(91px)}65%{transform:translateX(88px)}73%{opacity:1;transform:translateX(88px)}76%,100%{opacity:0;transform:translateX(88px);background:#FFD79A}}
@keyframes l20ta{0%,10%{opacity:0;transform:translateX(0);background:#46C7CF}12%{opacity:1}15%{transform:translateX(60px)}19%{transform:translateX(60px)}24%{transform:translateX(240px)}26%{opacity:0}
  57%{opacity:0;transform:translateX(0);background:#FFD79A}59%{opacity:1}62%{transform:translateX(60px)}67%{transform:translateX(60px)}72%{transform:translateX(240px)}74%,100%{opacity:0;transform:translateX(240px);background:#FFD79A}}
@keyframes l20hand{0%,12%{transform:scale(1)}13.5%{transform:scale(1.12)}15%{transform:scale(1)}61%{transform:scale(1)}62.5%{transform:scale(1.12)}64%,100%{transform:scale(1)}}
@keyframes l20th{0%,15%{opacity:0}17%{opacity:1}24%{opacity:1}27%{opacity:0}62%{opacity:0}64%{opacity:1}71%{opacity:1}74%,100%{opacity:0}}
@keyframes l20br{0%,63%{opacity:0}66%,100%{opacity:1}}
@keyframes l20wx{0%,65%{opacity:0}68%,100%{opacity:1}}
@keyframes l20s1{0%,26%{opacity:0;transform:scale(.5)}28%,100%{opacity:1;transform:scale(1)}}
@keyframes l20s2{0%,30%{opacity:0;transform:scale(.5)}32%,100%{opacity:1;transform:scale(1)}}
@keyframes l20s3{0%,34%{opacity:0;transform:scale(.5)}36%,100%{opacity:1;transform:scale(1)}}
@keyframes l20p4{0%,70%{opacity:0;transform:scale(.5)}72%,100%{opacity:1;transform:scale(1)}}
@keyframes l20x4{0%,65%{opacity:0;transform:scale(.5)}67%,100%{opacity:1;transform:scale(1)}}
@keyframes l20a4{0%,72%{opacity:0;transform:scale(.5)}74%,100%{opacity:1;transform:scale(1)}}
@keyframes l20va{0%,39%{opacity:0;transform:translateY(5px)}43%,100%{opacity:1;transform:none}}
@keyframes l20vb{0%,80%{opacity:0;transform:translateY(5px)}84%,100%{opacity:1;transform:none}}
@keyframes l20cnd{0%,83%{opacity:0}87%,100%{opacity:1}}
@media (prefers-reduced-motion:reduce){
  .l20-wrap,.l20-wrap *{animation:none!important}
  .l20-wrap,.l20-vd,.l20-in.ib,.l20-wx,.l20-br,.l20-cnd{opacity:1}
  .l20-m{opacity:1;transform:scale(1)}
  .l20-m{transform:scale(1)}
  .l20-in.ia,.l20-tok,.l20-th{opacity:0}
}
</style>


**Tilanne 1: Laskujen käsittely.** Yritys käsittelee 100 laskua päivässä. Lasku saapuu, sen summa täytyy vahvistaa ja tiedot pitää kirjata järjestelmään. Säännöt muuttuvat jonkin verran: uusia laskuttajia tulee ja hinnat muuttuvat, mutta perusprosessi pysyy samana. Epäonnistumisen hinta on korkea, koska väärä summa voi aiheuttaa organisaatiolle taloudellista vahinkoa. Ihmisen valvonta on kuitenkin mahdollista: valvoja voi tarkistaa, että laskut on käsitelty oikein.

Kuuden kysymyksen perusteella tehtävä toistuu, on melko monimutkainen, sisältää jonkin verran muuttuvia sääntöjä, aiheuttaa organisaatiotason kustannuksia, sisältää korkean epäonnistumisen hinnan ja mahdollistaa ihmisen valvonnan. Paras ratkaisu on **työnkulku yhdessä ihmisen valvonnan kanssa**. Agentti olisi todennäköisesti ylimitoitettu, ellei laskumäärä kasva huomattavasti tai tapausten monimutkaisuus lisäänny merkittävästi.

**Tilanne 2: Sähköpostien lajittelu.** Sähköposteja tulee satoja päivässä, mutta tehtävä on yksinkertainen: viestit luokitellaan sisällön perusteella. Hakusanat pysyvät samoina vuodesta toiseen. Epäonnistumisen hinta on matala. Jos sähköposti menee väärään kansioon, käyttäjä huomaa sen ja siirtää sen itse. Tilanne ei aiheuta kriisiä, eikä jatkuvaa valvontaa tarvita.

Kuuden kysymyksen perusteella tehtävä toistuu, on yksinkertainen, perustuu staattisiin sääntöihin, aiheuttaa pienet kustannukset, sisältää matalan epäonnistumisen hinnan eikä vaadi kriittistä valvontaa. Paras ratkaisu on **yksinkertainen työnkulku**. Agentti olisi tähän tehtävään täysin ylimitoitettu ja turhan kallis.

**Tilanne 3: Asiakaspalvelupyyntöjen reitittäminen.** Organisaatio saa yli 50 yhteydenottoa päivässä. Reititykseen vaikuttavat monet tekijät, kuten asian prioriteetti, työntekijöiden osaaminen, asian kiireellisyys ja asiakassuhteen arvo. Säännöt muuttuvat jatkuvasti, koska työntekijät, käsiteltävät aihealueet ja prioriteetit muuttuvat. Epäonnistumisen hinta on keskikorkea: väärä reititys voi heikentää asiakastyytyväisyyttä. Valvonta on mahdollista, koska esihenkilö voi tarkistaa päätöksiä.

Kuuden kysymyksen perusteella tehtävä toistuu, on monimutkainen, sisältää muuttuvia sääntöjä, aiheuttaa merkittäviä kustannuksia, sisältää keskikorkean epäonnistumisen hinnan ja mahdollistaa valvonnan. Paras ratkaisu on **aloittaa työnkululla ja valmistautua agenttiin**. Jos yritys kasvaa ja tiketit monimutkaistuvat, agenttiin voidaan siirtyä myöhemmin. Aluksi ei kuitenkaan kannata rakentaa liian raskasta ratkaisua.

> **Pysähdy hetkeksi:** Käy läpi nämä kolme tilannetta ja ajattele omaa mahdollista tehtävääsi. Mitä kuusi kysymystä vastaavat sen kohdalla?

<figure class="ai-demo"><span class="ai-demo__tag" id="l20q-t"><i aria-hidden="true">// </i>testi: mikä toteutustapa riittää tähän tilanteeseen?</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:330px">
  <div class="l20q-wrap">
    <input type="radio" name="l20qs" id="l20q-s1" class="l20q-in l20q-s1" checked>
    <input type="radio" name="l20qs" id="l20q-s2" class="l20q-in l20q-s2">
    <input type="radio" name="l20qs" id="l20q-s3" class="l20q-in l20q-s3">
    <input type="radio" name="l20q1" id="l20q-1a" class="l20q-in l20q-1a">
    <input type="radio" name="l20q1" id="l20q-1b" class="l20q-in l20q-1b">
    <input type="radio" name="l20q1" id="l20q-1c" class="l20q-in l20q-1c">
    <input type="radio" name="l20q2" id="l20q-2a" class="l20q-in l20q-2a">
    <input type="radio" name="l20q2" id="l20q-2b" class="l20q-in l20q-2b">
    <input type="radio" name="l20q2" id="l20q-2c" class="l20q-in l20q-2c">
    <input type="radio" name="l20q3" id="l20q-3a" class="l20q-in l20q-3a">
    <input type="radio" name="l20q3" id="l20q-3b" class="l20q-in l20q-3b">
    <input type="radio" name="l20q3" id="l20q-3c" class="l20q-in l20q-3c">
    <span class="l20q-cta">Kokeile itse: valitse toteutustapa jokaisessa tilanteessa</span>
    <span class="l20q-prog p1">tilanne 1/3</span><span class="l20q-prog p2">tilanne 2/3</span><span class="l20q-prog p3">tilanne 3/3</span>
    <div class="l20q-round r1"><fieldset class="l20q-fs"><legend class="l20q-sc">Tarvitset kerran tiivistelmän yhdestä 40-sivuisesta raportista.</legend><div class="l20q-opts"><label for="l20q-1a" class="l20q-opt o1a corr">PROMPTAUS</label><label for="l20q-1b" class="l20q-opt o1b">TYÖNKULKU</label><label for="l20q-1c" class="l20q-opt o1c">AGENTTI</label></div></fieldset><span class="l20q-fb f1a">✓ Kertaluonteinen tehtävä — promptaus riittää, eikä mitään jää ylläpidettäväksi.</span><span class="l20q-fb f1b">✗ Työnkulku kannattaa vasta, kun sama toistuu — tämä tehdään vain kerran.</span><span class="l20q-fb f1c">✗ Agentti on raskain väline: kertatehtävään se on ylimitoitettu.</span><label for="l20q-s2" class="l20q-next">seuraava tilanne →</label></div>
    <div class="l20q-round r2"><fieldset class="l20q-fs"><legend class="l20q-sc">Joka aamu: siirrä ”lasku”-viestit kansioon ja kuittaa lähettäjälle.</legend><div class="l20q-opts"><label for="l20q-2a" class="l20q-opt o2a">PROMPTAUS</label><label for="l20q-2b" class="l20q-opt o2b corr">TYÖNKULKU</label><label for="l20q-2c" class="l20q-opt o2c">AGENTTI</label></div></fieldset><span class="l20q-fb f2a">✗ Promptaus vaatisi sinut joka aamu mukaan — tämä toistuu päivittäin.</span><span class="l20q-fb f2b">✓ Toistuva tehtävä + selkeä sääntö = työnkulku. Halpa, nopea ja luotettava.</span><span class="l20q-fb f2c">✗ Säännöt eivät muutu — agentin päättelylle ei ole tässä tarvetta.</span><label for="l20q-s3" class="l20q-next">seuraava tilanne →</label></div>
    <div class="l20q-round r3"><fieldset class="l20q-fs"><legend class="l20q-sc">Palautteita tulee jatkuvasti: kiireellisyys vaihtelee, säännöt elävät ja epäselvät pitää ohjata ihmiselle.</legend><div class="l20q-opts"><label for="l20q-3a" class="l20q-opt o3a">PROMPTAUS</label><label for="l20q-3b" class="l20q-opt o3b">TYÖNKULKU</label><label for="l20q-3c" class="l20q-opt o3c corr">AGENTTI</label></div></fieldset><span class="l20q-fb f3a">✗ Promptaus ei skaalaudu jatkuvaan virtaan — joku istuisi koneella koko ajan.</span><span class="l20q-fb f3b">✗ Kiinteät avainsanasäännöt eivät riitä, kun tapaukset vaihtelevat.</span><span class="l20q-fb f3c">✓ Muuttuvat säännöt + harkinta = agentti, ihmisen valvonnassa. — Muista silti: valitse aina yksinkertaisin riittävä väline.</span><label for="l20q-s1" class="l20q-next">↺ alusta</label></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Päätöspuu käytännössä: toistuuko tehtävä, muuttuvatko säännöt, tarvitaanko harkintaa? Kertaluonteiseen riittää promptaus, toistuvaan selkeäsääntöiseen työnkulku — agentti kannattaa vasta, kun säännöt elävät ja päätökset vaativat tilannearviota.</figcaption></figure>
<style>
.l20q-wrap{position:relative;width:560px;height:290px;font-family:var(--font-mono)}
.l20q-in{position:absolute;opacity:0;pointer-events:none}
.l20q-cta{position:absolute;left:50%;transform:translateX(-50%);top:0;white-space:nowrap;font-size:11.5px;font-weight:700;letter-spacing:.07em;color:#0B1A14;background:#7FD0A8;border-radius:999px;padding:6px 16px;animation:l20qcta 2.2s ease-out infinite}
@keyframes l20qcta{0%{box-shadow:0 0 0 0 rgba(127,208,168,.5)}70%{box-shadow:0 0 0 12px rgba(127,208,168,0)}100%{box-shadow:0 0 0 0 rgba(127,208,168,0)}}
.l20q-prog{position:absolute;right:0;top:6px;font-size:12px;color:#8B94B3;opacity:0}
.l20q-fs{border:0;margin:0;padding:0;min-width:0}
.l20q-fs legend{width:100%;padding:0}
.l20q-round{position:absolute;left:0;right:0;top:48px;bottom:0;opacity:0;pointer-events:none;transition:opacity .35s}
.l20q-sc{display:block;font-size:12.5px;line-height:1.5;font-weight:500;color:#06212A;background:#46c7cf;border-radius:11px;padding:10px 13px}
.l20q-opts{display:flex;gap:12px;margin-top:14px}
.l20q-opt{flex:1;text-align:center;font-size:12px;font-weight:600;letter-spacing:.08em;color:#EAEEF8;background:#11182A;border:2px solid #2B3552;border-radius:11px;padding:13px 6px;cursor:pointer;transition:border-color .25s,transform .2s;animation:l20qinv 2.6s ease-in-out infinite}
.l20q-opt:nth-child(2){animation-delay:.85s}
.l20q-opt:nth-child(3){animation-delay:1.7s}
@keyframes l20qinv{0%,100%{border-color:#2B3552}50%{border-color:oklch(0.66 0.13 208)}}
.l20q-opt:hover{border-color:oklch(0.72 0.13 208);transform:translateY(-2px)}
.l20q-fb{position:absolute;left:0;right:0;top:148px;font-size:11.5px;line-height:1.5;color:#B9C2DA;text-align:center;opacity:0;transition:opacity .35s}
.l20q-next{position:absolute;right:0;bottom:0;min-height:44px;display:flex;align-items:center;font-size:12px;letter-spacing:.05em;color:#0B1A14;background:#7FD0A8;font-weight:600;border-radius:999px;padding:5px 13px;cursor:pointer;opacity:0;pointer-events:none;transition:opacity .3s}
.l20q-s1:checked~.l20q-round.r1{opacity:1;pointer-events:auto}
.l20q-s1:checked~.l20q-prog.p1{opacity:1}
:is(.l20q-1a:checked,.l20q-1b:checked,.l20q-1c:checked)~.r1 .l20q-opt.corr{border-color:#7FD0A8;color:#FFFFFF;animation:none}
:is(.l20q-1a:checked,.l20q-1b:checked,.l20q-1c:checked)~.r1 .l20q-opt{animation:none}
:is(.l20q-1a:checked,.l20q-1b:checked,.l20q-1c:checked)~.r1 .l20q-next{opacity:1;pointer-events:auto}
.l20q-1a:checked~.r1 .l20q-fb.f1a{opacity:1}
.l20q-1b:checked~.r1 .l20q-fb.f1b{opacity:1}
.l20q-1b:checked~.r1 .l20q-opt.o1b{border-color:#F0A38C;color:#FFD9CD}
.l20q-1c:checked~.r1 .l20q-fb.f1c{opacity:1}
.l20q-1c:checked~.r1 .l20q-opt.o1c{border-color:#F0A38C;color:#FFD9CD}
.l20q-s2:checked~.l20q-round.r2{opacity:1;pointer-events:auto}
.l20q-s2:checked~.l20q-prog.p2{opacity:1}
:is(.l20q-2a:checked,.l20q-2b:checked,.l20q-2c:checked)~.r2 .l20q-opt.corr{border-color:#7FD0A8;color:#FFFFFF;animation:none}
:is(.l20q-2a:checked,.l20q-2b:checked,.l20q-2c:checked)~.r2 .l20q-opt{animation:none}
:is(.l20q-2a:checked,.l20q-2b:checked,.l20q-2c:checked)~.r2 .l20q-next{opacity:1;pointer-events:auto}
.l20q-2a:checked~.r2 .l20q-fb.f2a{opacity:1}
.l20q-2a:checked~.r2 .l20q-opt.o2a{border-color:#F0A38C;color:#FFD9CD}
.l20q-2b:checked~.r2 .l20q-fb.f2b{opacity:1}
.l20q-2c:checked~.r2 .l20q-fb.f2c{opacity:1}
.l20q-2c:checked~.r2 .l20q-opt.o2c{border-color:#F0A38C;color:#FFD9CD}
.l20q-s3:checked~.l20q-round.r3{opacity:1;pointer-events:auto}
.l20q-s3:checked~.l20q-prog.p3{opacity:1}
:is(.l20q-3a:checked,.l20q-3b:checked,.l20q-3c:checked)~.r3 .l20q-opt.corr{border-color:#7FD0A8;color:#FFFFFF;animation:none}
:is(.l20q-3a:checked,.l20q-3b:checked,.l20q-3c:checked)~.r3 .l20q-opt{animation:none}
:is(.l20q-3a:checked,.l20q-3b:checked,.l20q-3c:checked)~.r3 .l20q-next{opacity:1;pointer-events:auto}
.l20q-3a:checked~.r3 .l20q-fb.f3a{opacity:1}
.l20q-3a:checked~.r3 .l20q-opt.o3a{border-color:#F0A38C;color:#FFD9CD}
.l20q-3b:checked~.r3 .l20q-fb.f3b{opacity:1}
.l20q-3b:checked~.r3 .l20q-opt.o3b{border-color:#F0A38C;color:#FFD9CD}
.l20q-3c:checked~.r3 .l20q-fb.f3c{opacity:1}
@media (prefers-reduced-motion:reduce){.l20q-cta,.l20q-opt{animation:none}.l20q-round,.l20q-opt,.l20q-fb,.l20q-next{transition:none}}
@media (max-width:680px){
.ai-demo__interaction:has(.l20q-wrap){height:560px!important;padding:12px}
.l20q-wrap{width:100%;height:520px}
.l20q-cta{position:static;display:block;transform:none;white-space:normal;text-align:center;font-size:12px;line-height:1.4;min-height:44px;padding:10px 12px}
.l20q-prog{top:58px;right:0;font-size:12px}
.l20q-round{top:84px}
.l20q-sc{font-size:13px;line-height:1.45}
.l20q-opts{display:grid;grid-template-columns:1fr;gap:8px;margin-top:10px}
.l20q-opt{min-height:44px;padding:10px;font-size:13px}
.l20q-fb{top:252px;text-align:left;font-size:13px;line-height:1.45}
.l20q-next{bottom:0;min-height:44px;display:flex;align-items:center;padding:8px 14px;font-size:13px}
}
</style>

## Monimutkaisuus on aina kustannus

Tässä on tärkeä ajatus, jonka monet unohtavat: agentti on monimutkainen. Se ei ole vain ”parempi työnkulku”. Se on luonteeltaan erilainen ratkaisu, ei pelkästään suurempi tai tehokkaampi versio työnkulusta.

Työnkulun kehitysaika mitataan usein tunneissa tai päivissä. Agentin kehitysaika mitataan usein viikoissa tai kuukausissa, koska dynaaminen logiikka vaatii paljon enemmän suunnittelua. Työnkulkua testaa yleensä tekijä, joka ymmärtää säännöt. Agenttia täytyy testata laajemmin, koska sen dynaamisuus voi tuottaa odottamattomia tuloksia. Agentti vaatii myös jatkuvaa valvontaa. Virheet ja ihmisen palaute tallennetaan, jotta niitä voidaan arvioida. Niiden perusteella ihminen korjaa ohjeita, harnessin sääntöjä tai testejä ja varmistaa muutoksen vaikutuksen uudella testillä. Agentti ei siis opi yksittäisestä virheestä itsestään.

Kysy siis aina: miksi rakennan agentin? Vastaus perustuu kustannusten ja hyötyjen vertailuun. Jos työnkulku ratkaisee ongelmasi 80 prosentissa tapauksista ja agentti ratkaisee sen 85 prosentissa tapauksista, oletko valmis maksamaan 10 kertaa suuremmat kehitys- ja ylläpitokustannukset viiden prosenttiyksikön parannuksesta? Usein vastaus on ei. Jos työnkulku ratkaisee vain 40 prosenttia tapauksista ja agentti 95 prosenttia tapauksista, hyöty voi olla selvästi kustannuksia suurempi. Silloin agentti voi olla järkevä ratkaisu.

## Osta vai rakenna — riittääkö valmisagentti?

Kun kuusi kysymystä osoittaa, että tehtävä ansaitsee agentin, jäljellä on vielä yksi valinta: rakennatko oman vai käytätkö **valmisagenttia**, jollaisiin tutustuit tunnilla 19? Tämäkin on arkkitehtuuripäätös, ei tuotevalinta — ja se ratkeaa samalla logiikalla kuin muutkin tämän tunnin päätökset.

Nyrkkisääntö kuuluu näin. Toistuva ja tarkkaan määritelty prosessi puoltaa omaa työnkulkua tai omaa n8n-agenttia, koska silloin saat täsmälleen omat sääntösi, omat integraatiosi ja omat lokisi. Vaihteleva, kertaluonteinen tietotyö puoltaa valmisagenttia, koska rakentamisen ja ylläpidon kustannus jää silloin kokonaan pois. Huomaa samalla ero käyttämisen ja rakentamisen välillä: valmisagentin voi ottaa käyttöön myös silloin, kun oman rakentaminen ei kannata — rakentamiskustannus on nolla, joten päätöspuun ensimmäinen kysymys ei estä valmisagentin käyttöä.

Vertailussa auttaa kolme perustetta. **Kustannus:** valmisagentissa maksat tilausmaksun, omassa maksat kehityksen ja jatkuvan ylläpidon. **Kontrolli:** omassa agentissa päätät itse säännöt, työkalut ja rajat — valmiissa joku muu on päättänyt ne puolestasi. **Läpinäkyvyys:** omassa n8n-työnkulussa näet jokaisen solmun ja jokaisen suorituksen, valmisagentissa näet vain sen, minkä se näyttää.

Lopputyössä rakennat oman n8n-agentin joka tapauksessa — juuri siksi, että osaisit jatkossa tehdä tämän valinnan perustellusti. Kun olet kerran nähnyt, mitä oman agentin rakentaminen ja ylläpito vaativat, osaat myös arvioida, mistä valmisagentin tilausmaksussa oikeastaan maksetaan.

> **Pysähdy hetkeksi:** Ratkeaisiko sinun lopputyöongelmasi valmisagentilla? Jos ratkeaisi, mitä menettäisit — ja onko sillä menetyksellä sinun tapauksessasi väliä?

## Miltä nämä päätökset näyttävät n8n:ssä?

Kun rakennat ratkaisua n8n:ssä, tässä oppitunnissa käsitellyt päätökset muuttuvat konkreettisiksi valinnoiksi n8n:n visuaalisessa editorissa.

**Yksinkertainen promptaus n8n:ssä:** yksi AI Agent -solmu saa viestin ja vastaa siihen. Muita solmuja ei tarvita. Tämä riittää, kun tehtävä on yksinkertainen.

**Työnkulku n8n:ssä:** sarja solmuja seuraa toisiaan. Esimerkiksi: Email Trigger → IF-solmu, joka tarkistaa avainsanan → Slack-solmu, joka lähettää viestin oikealle kanavalle. Logiikka on kiinteä: sama syöte tuottaa aina saman tuloksen.

**Agentti n8n:ssä:** AI Agent -solmulla on pääsy **työkaluihin**, kuten tietokantaan, verkkohakuun tai tiedostoihin. Agentti päättää itse, mitä työkalua se käyttää. Tämä on monimutkaisempaa mutta joustavampaa.

Tämän esikatselun tarkoitus on yksinkertainen: kun tulet oppitunnille 26 ja avaat n8n:n, tiedät jo, **mitä olet rakentamassa ja miksi**. Päätös promptauksen, työnkulun ja agentin välillä on **arkkitehtuuripäätös**, ei pelkkä työkalupäätös.

## Kohti omaa projektia

Kun olet valinnut oppitunnilla 19 oman agenttiongelmasi, tämän oppitunnin kuusi kysymystä auttavat sinua tarkistamaan, onko agentti todella oikea ratkaisu. Palaa päätöspuuhun ja käy ongelmasi läpi: toistuuko tehtävä, onko eteneminen ennalta määrätty vai pitääkö kielimallin valita seuraava toiminto tilanteen perusteella? Jos tavallinen työnkulku riittää, havainto on onnistunut oppimistulos. Rajaa silloin projektiin yksi aito tilannekohtainen päätös tai valitse toinen ongelma.

> **Lopuksi pohdittavaksi:** Mitä kielimallin ympärillä pitää olla, jotta ratkaisua voi perustellusti kutsua agentiksi — ja tarvitaanko sitä tässä ongelmassa?

## Yhteenveto

Automatisointi on jatkumo, ei joko–tai-valinta. Älä valitse agenttia automaattisesti. Kysy ensin nämä kuusi kysymystä: **Toistuuko tehtävä?** **Onko tehtävä monimutkainen?** **Pitääkö seuraava toiminto valita tilanteen perusteella?** **Kuka maksaa?** **Mitkä ovat epäonnistumisen kustannukset?** **Onko valvonta mahdollista?**

Päätöspuu ohjaa sinut oikean välineen luo. Yksinkertainen työnkulku ratkaisee usein ongelman riittävän hyvin ja paljon pienemmillä kustannuksilla kuin agentti. Valitse aina yksinkertaisin ratkaisu, joka todella toimii.

---

## Lähteet ja tarkistuspäivä

- [Anthropic: Building Effective AI Agents](https://resources.anthropic.com/building-effective-ai-agents)
- [Yao ym.: ReAct](https://arxiv.org/abs/2210.03629)
- [Model Context Protocol: server primitives](https://modelcontextprotocol.io/specification/2025-06-18/server/index)

Tarkistettu 15.7.2026.
