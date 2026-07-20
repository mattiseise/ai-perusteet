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

Kolmas väline on **agentti**. Asiakaspalvelun agentti voi lukea sähköposteja, analysoida niiden sävyä, etsiä vastaavia aiempia tapauksia tietokannasta ja **päättää**, onko se riittävän varma lähettämään automaattisen vastauksen vai pitäisikö viesti ohjata ihmiselle. Agentti ei siis vain seuraa sääntöjä, vaan tekee tilanteesta oman arvionsa. Jos asiakas on vihainen, agentti voi käyttää tavallista varovaisempaa sävyä. Jos sama asiakastapaus tulee vastaan toisen kerran, agentti voi muistaa aiemman tapauksen ja hyödyntää oppimaansa.

Agentin kustannus on suuri. Kehittäminen on monimutkaisempaa, koska logiikka on dynaamista. Testaus vie paljon aikaa, koska agentti voi tuottaa odottamattomia tuloksia. Ylläpito on jatkuvaa, koska sinun täytyy valvoa, mitä agentti tekee ja millaisia päätöksiä se tekee. Agentin hyöty on siinä, että se pystyy käsittelemään monimutkaisia ja poikkeavia tapauksia, joita työnkulku ei osaa ratkaista. Rajoitus on korkea hinta: agentista täytyy saada merkittävä hyöty suhteessa siihen, mitä sen rakentaminen ja ylläpito maksavat.

> **Pysähdy hetkeksi:** Miksi olisit valmis maksamaan enemmän agentin rakentamisesta? Mitä sellaista etua agentti antaa, jota ei voi saavuttaa pelkällä työnkululla?

## Kuusi kysymystä päätöksenteon tueksi

Kun tarkastelet automatisoitavaa tehtävää, kysy seuraavat kuusi kysymystä **järjestyksessä**. Ne auttavat sinua valitsemaan oikean välineen.

**Ensimmäinen kysymys: Toistuuko tehtävä?** Jos tehtävä on kertaluontoinen tai sitä tehdään hyvin harvoin, sitä ei yleensä kannata automatisoida. Automatisoinnin rakentamiseen kuluu todennäköisesti enemmän aikaa kuin itse tehtävän tekemiseen. Jos tehtävä taas toistuu joka päivä, joka tunti tai jopa useita kertoja minuutissa, automatisointi alkaa kannattaa. Jopa yksinkertainen työnkulku voi säästää merkittävästi aikaa, kun sitä käytetään tuhansia kertoja vuodessa.

**Toinen kysymys: Onko tehtävä yksinkertainen vai monimutkainen?** Yksinkertaiset tehtävät, joissa on yksi tai kaksi vaihetta ja selkeät säännöt, ratkeavat usein työnkululla. Esimerkiksi ohje ”kun laskua ei ole vastaanotettu, siirrä asia kansioon Odottaa” on niin suoraviivainen, että työnkulku riittää. Monimutkaisissa tehtävissä tilanne on toinen. Jos tehtävä sisältää useita vaiheita, ehdollisia päätöksiä, oppimista ja mukautumista, työnkulun jäykät säännöt eivät välttämättä enää riitä. Tämä on merkki siitä, että **päättely** eli agentin keskeinen ominaisuus voisi tuoda lisäarvoa.

**Kolmas kysymys: Ovatko säännöt staattisia vai muuttuvia?** Jos säännöt ovat staattisia eli sama asia tehdään joka kerta täsmälleen samalla tavalla, työnkulku on yleensä täysin riittävä. Jokainen tapaus käsitellään samalla tavalla, eikä uusia poikkeamia juuri ilmene. Jos säännöt ovat muuttuvia, agentti voi olla parempi valinta. Muuttuvissa tilanteissa jokainen asiakas voi olla erilainen, uusia toimintamalleja syntyy ja tilanteet muuttuvat. Agentti voi hyödyntää aiempia havaintoja ja soveltaa oppimaansa seuraaviin tilanteisiin. Työnkulku ei voi tehdä tätä, vaan se toimii aina ennalta kirjoitettujen sääntöjen mukaan.

**Neljäs kysymys: Kuka maksaa hinnan?** Jos käyttäjä maksaa pienen summan, kuten tekoälypalvelun tilauksen, kokeileminen on helppoa ja riski on pieni. Jos taas organisaatio maksaa tuhansia tai kymmeniä tuhansia euroja agentin rakentamisesta, päätös on paljon suurempi. Silloin tarvitaan vahvat perusteet ja realistinen arvio siitä, että investointi maksaa itsensä takaisin.

**Viides kysymys: Mitkä ovat epäonnistumisen kustannukset?** Jos agentti tekee virheen eikä mitään vakavaa tapahdu, riski voi olla hyväksyttävä. Esimerkiksi sähköposti voi mennä väärään kansioon, mutta ihminen huomaa sen ja korjaa virheen. Jos epäonnistumisen seuraukset ovat suuret, tilanne muuttuu. Rahaa voidaan menettää, asiakkaita voidaan menettää tai ihminen voi joutua vaaraan. Tällöin agenttia täytyy valvoa hyvin huolellisesti, ja valvonta nostaa ylläpitokustannuksia merkittävästi. Joissain tapauksissa korkeat epäonnistumisen kustannukset tekevät agentin rakentamisesta kannattamatonta.

**Kuudes kysymys: Onko ihmisen valvonta mahdollista?** Jos ihminen voi valvoa agentin päätöksiä ja puuttua toimintaan, kun jokin menee pieleen, riski on hallittavampi. Agentti voi pyytää ihmisen apua vaikeissa tilanteissa, jolloin riskien hallinta on mahdollista. Jos valvonta on mahdotonta, agentin täytyy toimia lähes täydellisesti. Tämä on harvinaisen kallista rakentaa ja ylläpitää.

## Käytännön päätöspuu kolmessa tarinassa

Katsotaan seuraavaksi kolmea käytännön tilannetta ja sitä, mitä kuusi kysymystä niissä ohjaavat tekemään.

<figure class="ai-demo"><span class="ai-demo__tag">// automaatio toistaa saman polun — agentti valitsee tilanteen mukaan</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:300px">
  <div class="l20-wrap">
    <div class="l20-lane l20-top"><span class="l20-lh">AUTOMAATIO</span><div class="l20-rail"></div><span class="l20-stn" style="left:96px">A</span><span class="l20-stn" style="left:240px">B</span><span class="l20-stn" style="left:384px">C</span><i class="l20-pk"></i><span class="l20-ll">sama polku joka kerta — tilanteesta riippumatta</span></div>
    <div class="l20-lane l20-bot"><span class="l20-lh">AGENTTI</span>
      <div class="l20-case"><span class="l20-c cc1">rutiinikysymys</span><span class="l20-c cc2">epäselvä tapaus</span><span class="l20-c cc3">kriittinen poikkeama!</span></div>
      <span class="l20-eval">tilannearvio…</span>
      <div class="l20-br b1"><span>vastaa heti</span></div>
      <div class="l20-br b2"><span>hae lisätietoa</span></div>
      <div class="l20-br b3"><span>ohjaa ihmiselle</span></div>
    </div>
  </div>
</div>
<figcaption class="ai-demo__cap">Automaatio seuraa aina samaa ennalta määrättyä polkua. Agentti on autonominen: se arvioi tilanteen ensin ja valitsee polun itse — rutiini hoituu heti, epäselvä vaatii lisätietoa ja kriittinen siirtyy ihmiselle.</figcaption></figure>
<style>
.l20-wrap{position:relative;width:560px;height:268px;font-family:var(--font-mono)}
.l20-lane{position:absolute;left:0;right:0;background:#11182A;border:1.5px solid #2B3552;border-radius:13px}
.l20-top{top:0;height:96px}
.l20-bot{top:108px;height:160px;border-color:oklch(0.66 0.13 208)}
.l20-lh{position:absolute;left:13px;top:9px;font-size:10.5px;letter-spacing:.12em;color:#B9C2DA}
.l20-rail{position:absolute;left:84px;right:60px;top:46px;height:3px;background:#3A4560}
.l20-stn{position:absolute;top:33px;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#EAEEF8;background:#1E2740;border:2px solid #44517A;border-radius:50%}
.l20-pk{position:absolute;left:78px;top:42px;width:11px;height:11px;border-radius:50%;background:#46c7cf;box-shadow:0 0 10px rgba(70,199,207,.8);animation:l20pk 4.66s linear infinite}
@keyframes l20pk{0%{transform:translateX(0)}12%{transform:translateX(0)}88%{transform:translateX(330px)}100%{transform:translateX(330px)}}
.l20-ll{position:absolute;left:84px;bottom:8px;font-size:10.5px;color:#8B94B3}
.l20-case{position:absolute;left:13px;top:34px;width:158px;height:56px}
.l20-c{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;font-size:11px;font-weight:500;line-height:1.35;color:#06212A;background:#46c7cf;border-radius:10px;padding:4px 8px;opacity:0}
.l20-c.cc1{animation:l20c1 14s infinite}
.l20-c.cc2{animation:l20c2 14s infinite}
.l20-c.cc3{animation:l20c3 14s infinite;background:#F0A38C;color:#3A1408}
@keyframes l20c1{0%,2%{opacity:0}5%,28%{opacity:1}32%,100%{opacity:0}}
@keyframes l20c2{0%,35%{opacity:0}38%,61%{opacity:1}65%,100%{opacity:0}}
@keyframes l20c3{0%,68%{opacity:0}71%,94%{opacity:1}98%,100%{opacity:0}}
.l20-eval{position:absolute;left:188px;top:56px;font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:oklch(0.75 0.12 208);animation:l20ev 4.66s ease-in-out infinite}
@keyframes l20ev{0%,8%{opacity:0}18%,40%{opacity:1}52%,100%{opacity:0}}
.l20-br{position:absolute;left:300px;width:236px;height:34px;border:1.5px solid #2B3552;border-radius:10px;background:#0E1422}
.l20-br span{position:absolute;left:12px;top:50%;transform:translateY(-50%);font-size:11.5px;color:#B9C2DA}
.l20-br.b1{top:22px;animation:l20b1 14s infinite}
.l20-br.b2{top:64px;animation:l20b2 14s infinite}
.l20-br.b3{top:106px;animation:l20b3 14s infinite}
@keyframes l20b1{0%,9%{border-color:#2B3552;box-shadow:none}13%,28%{border-color:#7FD0A8;box-shadow:0 0 12px rgba(127,208,168,.4)}33%,100%{border-color:#2B3552;box-shadow:none}}
@keyframes l20b2{0%,42%{border-color:#2B3552;box-shadow:none}46%,61%{border-color:#46c7cf;box-shadow:0 0 12px rgba(70,199,207,.4)}66%,100%{border-color:#2B3552;box-shadow:none}}
@keyframes l20b3{0%,75%{border-color:#2B3552;box-shadow:none}79%,94%{border-color:#F0A38C;box-shadow:0 0 12px rgba(240,163,140,.45)}99%,100%{border-color:#2B3552;box-shadow:none}}
@media (prefers-reduced-motion:reduce){
.l20-pk,.l20-c,.l20-eval,.l20-br{animation:none}
.l20-pk{transform:translateX(330px)}
.l20-c.cc3,.l20-eval{opacity:1}
.l20-br.b3{border-color:#F0A38C}}
</style>


**Tilanne 1: Laskujen käsittely.** Yritys käsittelee 100 laskua päivässä. Lasku saapuu, sen summa täytyy vahvistaa ja tiedot pitää kirjata järjestelmään. Säännöt muuttuvat jonkin verran: uusia laskuttajia tulee ja hinnat muuttuvat, mutta perusprosessi pysyy samana. Epäonnistumisen hinta on korkea, koska väärä summa voi aiheuttaa organisaatiolle taloudellista vahinkoa. Ihmisen valvonta on kuitenkin mahdollista: valvoja voi tarkistaa, että laskut on käsitelty oikein.

Kuuden kysymyksen perusteella tehtävä toistuu, on melko monimutkainen, sisältää jonkin verran muuttuvia sääntöjä, aiheuttaa organisaatiotason kustannuksia, sisältää korkean epäonnistumisen hinnan ja mahdollistaa ihmisen valvonnan. Paras ratkaisu on **työnkulku yhdessä ihmisen valvonnan kanssa**. Agentti olisi todennäköisesti ylimitoitettu, ellei laskumäärä kasva huomattavasti tai tapausten monimutkaisuus lisäänny merkittävästi.

**Tilanne 2: Sähköpostien lajittelu.** Sähköposteja tulee satoja päivässä, mutta tehtävä on yksinkertainen: viestit luokitellaan sisällön perusteella. Hakusanat pysyvät samoina vuodesta toiseen. Epäonnistumisen hinta on matala. Jos sähköposti menee väärään kansioon, käyttäjä huomaa sen ja siirtää sen itse. Tilanne ei aiheuta kriisiä, eikä jatkuvaa valvontaa tarvita.

Kuuden kysymyksen perusteella tehtävä toistuu, on yksinkertainen, perustuu staattisiin sääntöihin, aiheuttaa pienet kustannukset, sisältää matalan epäonnistumisen hinnan eikä vaadi kriittistä valvontaa. Paras ratkaisu on **yksinkertainen työnkulku**. Agentti olisi tähän tehtävään täysin ylimitoitettu ja turhan kallis.

**Tilanne 3: Asiakaspalvelupyyntöjen reitittäminen.** Organisaatio saa yli 50 yhteydenottoa päivässä. Reititykseen vaikuttavat monet tekijät, kuten asian prioriteetti, työntekijöiden osaaminen, asian kiireellisyys ja asiakassuhteen arvo. Säännöt muuttuvat jatkuvasti, koska työntekijät, käsiteltävät aihealueet ja prioriteetit muuttuvat. Epäonnistumisen hinta on keskikorkea: väärä reititys voi heikentää asiakastyytyväisyyttä. Valvonta on mahdollista, koska esihenkilö voi tarkistaa päätöksiä.

Kuuden kysymyksen perusteella tehtävä toistuu, on monimutkainen, sisältää muuttuvia sääntöjä, aiheuttaa merkittäviä kustannuksia, sisältää keskikorkean epäonnistumisen hinnan ja mahdollistaa valvonnan. Paras ratkaisu on **aloittaa työnkululla ja valmistautua agenttiin**. Jos yritys kasvaa ja tiketit monimutkaistuvat, agenttiin voidaan siirtyä myöhemmin. Aluksi ei kuitenkaan kannata rakentaa liian raskasta ratkaisua.

> **Pysähdy hetkeksi:** Käy läpi nämä kolme tilannetta ja ajattele omaa mahdollista tehtävääsi. Mitä kuusi kysymystä vastaavat sen kohdalla?

<figure class="ai-demo"><span class="ai-demo__tag">// testi: mikä väline riittää tähän tilanteeseen?</span>
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
    <span class="l20q-cta">▶ KOKEILE ITSE — valitse väline klikkaamalla</span>
    <span class="l20q-prog p1">tilanne 1/3</span><span class="l20q-prog p2">tilanne 2/3</span><span class="l20q-prog p3">tilanne 3/3</span>
    <div class="l20q-round r1"><span class="l20q-sc">Tarvitset kerran tiivistelmän yhdestä 40-sivuisesta raportista.</span><div class="l20q-opts"><label for="l20q-1a" class="l20q-opt o1a corr">PROMPTAUS</label><label for="l20q-1b" class="l20q-opt o1b">TYÖNKULKU</label><label for="l20q-1c" class="l20q-opt o1c">AGENTTI</label></div><span class="l20q-fb f1a">✓ Kertaluonteinen tehtävä — promptaus riittää, eikä mitään jää ylläpidettäväksi.</span><span class="l20q-fb f1b">✗ Työnkulku kannattaa vasta, kun sama toistuu — tämä tehdään vain kerran.</span><span class="l20q-fb f1c">✗ Agentti on raskain väline: kertatehtävään se on ylimitoitettu.</span><label for="l20q-s2" class="l20q-next">seuraava tilanne →</label></div>
    <div class="l20q-round r2"><span class="l20q-sc">Joka aamu: siirrä ”lasku”-viestit kansioon ja kuittaa lähettäjälle.</span><div class="l20q-opts"><label for="l20q-2a" class="l20q-opt o2a">PROMPTAUS</label><label for="l20q-2b" class="l20q-opt o2b corr">TYÖNKULKU</label><label for="l20q-2c" class="l20q-opt o2c">AGENTTI</label></div><span class="l20q-fb f2a">✗ Promptaus vaatisi sinut joka aamu mukaan — tämä toistuu päivittäin.</span><span class="l20q-fb f2b">✓ Toistuva tehtävä + selkeä sääntö = työnkulku. Halpa, nopea ja luotettava.</span><span class="l20q-fb f2c">✗ Säännöt eivät muutu — agentin päättelylle ei ole tässä tarvetta.</span><label for="l20q-s3" class="l20q-next">seuraava tilanne →</label></div>
    <div class="l20q-round r3"><span class="l20q-sc">Palautteita tulee jatkuvasti: kiireellisyys vaihtelee, säännöt elävät ja epäselvät pitää ohjata ihmiselle.</span><div class="l20q-opts"><label for="l20q-3a" class="l20q-opt o3a">PROMPTAUS</label><label for="l20q-3b" class="l20q-opt o3b">TYÖNKULKU</label><label for="l20q-3c" class="l20q-opt o3c corr">AGENTTI</label></div><span class="l20q-fb f3a">✗ Promptaus ei skaalaudu jatkuvaan virtaan — joku istuisi koneella koko ajan.</span><span class="l20q-fb f3b">✗ Kiinteät avainsanasäännöt eivät riitä, kun tapaukset vaihtelevat.</span><span class="l20q-fb f3c">✓ Muuttuvat säännöt + harkinta = agentti, ihmisen valvonnassa. — Muista silti: valitse aina yksinkertaisin riittävä väline.</span><label for="l20q-s1" class="l20q-next">↺ alusta</label></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Päätöspuu käytännössä: toistuuko tehtävä, muuttuvatko säännöt, tarvitaanko harkintaa? Kertaluonteiseen riittää promptaus, toistuvaan selkeäsääntöiseen työnkulku — agentti kannattaa vasta, kun säännöt elävät ja päätökset vaativat tilannearviota.</figcaption></figure>
<style>
.l20q-wrap{position:relative;width:560px;height:290px;font-family:var(--font-mono)}
.l20q-in{position:absolute;opacity:0;pointer-events:none}
.l20q-cta{position:absolute;left:50%;transform:translateX(-50%);top:0;white-space:nowrap;font-size:11.5px;font-weight:700;letter-spacing:.07em;color:#0B1A14;background:#7FD0A8;border-radius:999px;padding:6px 16px;animation:l20qcta 2.2s ease-out infinite}
@keyframes l20qcta{0%{box-shadow:0 0 0 0 rgba(127,208,168,.5)}70%{box-shadow:0 0 0 12px rgba(127,208,168,0)}100%{box-shadow:0 0 0 0 rgba(127,208,168,0)}}
.l20q-prog{position:absolute;right:0;top:6px;font-size:10.5px;color:#8B94B3;opacity:0}
.l20q-round{position:absolute;left:0;right:0;top:48px;bottom:0;opacity:0;pointer-events:none;transition:opacity .35s}
.l20q-sc{display:block;font-size:12.5px;line-height:1.5;font-weight:500;color:#06212A;background:#46c7cf;border-radius:11px;padding:10px 13px}
.l20q-opts{display:flex;gap:12px;margin-top:14px}
.l20q-opt{flex:1;text-align:center;font-size:12px;font-weight:600;letter-spacing:.08em;color:#EAEEF8;background:#11182A;border:2px solid #2B3552;border-radius:11px;padding:13px 6px;cursor:pointer;transition:border-color .25s,transform .2s;animation:l20qinv 2.6s ease-in-out infinite}
.l20q-opt:nth-child(2){animation-delay:.85s}
.l20q-opt:nth-child(3){animation-delay:1.7s}
@keyframes l20qinv{0%,100%{border-color:#2B3552}50%{border-color:oklch(0.66 0.13 208)}}
.l20q-opt:hover{border-color:oklch(0.72 0.13 208);transform:translateY(-2px)}
.l20q-fb{position:absolute;left:0;right:0;top:148px;font-size:11.5px;line-height:1.5;color:#B9C2DA;text-align:center;opacity:0;transition:opacity .35s}
.l20q-next{position:absolute;right:0;bottom:0;min-height:44px;display:flex;align-items:center;font-size:11px;letter-spacing:.05em;color:#0B1A14;background:#7FD0A8;font-weight:600;border-radius:999px;padding:5px 13px;cursor:pointer;opacity:0;pointer-events:none;transition:opacity .3s}
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

Työnkulun kehitysaika mitataan usein tunneissa tai päivissä. Agentin kehitysaika mitataan usein viikoissa tai kuukausissa, koska dynaaminen logiikka vaatii paljon enemmän suunnittelua. Työnkulkua testaa yleensä tekijä, joka ymmärtää säännöt. Agenttia täytyy testata laajemmin, koska sen dynaamisuus voi tuottaa odottamattomia tuloksia. Agentti vaatii myös jatkuvaa valvontaa. Jos agentti oppii virheistä, sinun täytyy seurata, mitä se on oppinut ja ovatko opitut asiat oikeanlaisia. Jos agentti alkaa tehdä systemaattisesti virheellisiä johtopäätöksiä, sinun täytyy puuttua sen toimintaan ja muuttaa sen ohjeistusta.

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

Kun olet valinnut oppitunnilla 19 oman agenttiongelmasi, tämän oppitunnin kuusi kysymystä auttavat sinua tarkistamaan, onko agentti todella oikea ratkaisu. Palaa päätöspuuhun ja käy ongelmasi läpi: toistuuko tehtävä, onko se riittävän monimutkainen ja muuttuvatko säännöt tilanteen mukaan? Jos päätöspuu osoittaa, että yksinkertaisempi ratkaisu riittäisi, harkitse ongelman tarkentamista sellaiseksi, jossa agentin autonomisuus tuottaa aidosti lisäarvoa.

> **Lopuksi pohdittavaksi:** Mitä kielimallin ympärillä pitää olla, jotta ratkaisua voi perustellusti kutsua agentiksi — ja tarvitaanko sitä tässä ongelmassa?

## Yhteenveto

Automatisointi on jatkumo, ei joko–tai-valinta. Älä valitse agenttia automaattisesti. Kysy ensin nämä kuusi kysymystä: **Toistuuko tehtävä?** **Onko tehtävä monimutkainen?** **Muuttuvatko säännöt?** **Kuka maksaa?** **Mitkä ovat epäonnistumisen kustannukset?** **Onko valvonta mahdollista?**

Päätöspuu ohjaa sinut oikean välineen luo. Yksinkertainen työnkulku ratkaisee usein ongelman riittävän hyvin ja paljon pienemmillä kustannuksilla kuin agentti. Valitse aina yksinkertaisin ratkaisu, joka todella toimii.

---

## Lähteet ja tarkistuspäivä

- [Anthropic: Building Effective AI Agents](https://resources.anthropic.com/building-effective-ai-agents)
- [Yao ym.: ReAct](https://arxiv.org/abs/2210.03629)
- [Model Context Protocol: server primitives](https://modelcontextprotocol.io/specification/2025-06-18/server/index)

Tarkistettu 15.7.2026.
