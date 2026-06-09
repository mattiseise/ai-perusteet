# Automaatio vai autonomia? — milloin agentti kannattaa?

## Johdanto

Nyt kun tiedät, mikä **agentti** on, seuraava kysymys on ilmeinen: milloin agenttia kannattaa käyttää? Vastaus ei ole ”aina”. Agentti tuo mukanaan monimutkaisuutta, kustannuksia ja riskejä. Usein tavallinen **työnkulku** tai jopa yksinkertainen **promptaus** riittää.

Kun rakennat oppitunneilla omaa agenttiasi n8n:llä, tämän asian ymmärtäminen auttaa sinua tekemään parempia arkkitehtuuripäätöksiä. Kun tiedät, milloin agentti todella kannattaa, voit suunnitella projektisi järkevämmin.

Kuvittele, että vastaat asiakaspalvelusta. Joka päivä tulee 50 yhteydenottoa. Joku ehdottaa: ”Tehdään agentti, joka käsittelee nämä automaattisesti!” Ajatus kuulostaa hyvältä, kunnes huomaat todellisuuden: agentin rakentaminen, testaaminen ja ylläpito kestävät kuukauden ja maksavat 10 000 euroa. Ehkä yksinkertainen työnkulku, joka ohjaa yhteydenotot automaattisesti oikealle henkilölle, antaisi saman hyödyn murto-osalla kustannuksista.

Tässä oppitunnissa opit käyttämään **päätöspuuta** eli ajattelumallia, joka auttaa valitsemaan oikean ratkaisun. Milloin promptaus riittää? Milloin tarvitset työnkulun? Milloin agentti todella kannattaa rakentaa?

> **Pysähdy hetkeksi:** Ajattele omaa tulevaa työtäsi. Mitä toistuvia ja monivaiheisia tehtäviä siinä voi olla? Mitkä niistä voisivat toimia työnkulkuina, ja mitkä vaatisivat agentin?

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

<figure class="ai-demo"><span class="ai-demo__tag">// päätös haarautuu: promptaus, työnkulku vai agentti</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center">
  <svg viewBox="0 0 460 180" style="width:100%;height:100%" preserveAspectRatio="xMidYMid meet">
    <circle cx="50" cy="90" r="9" fill="oklch(0.66 0.15 264)"/>
    <text x="50" y="118" text-anchor="middle" font-family="var(--font-mono)" font-size="9" fill="#8B94B3">tehtävä</text>
    <g stroke="#2A3450" stroke-width="1.5" fill="none">
      <path d="M59 90 Q140 90 200 40"/><path d="M59 90 L200 90"/><path d="M59 90 Q140 90 200 140"/>
    </g>
    <path class="l20dec-p" d="M59 90 Q140 90 200 40" fill="none" stroke="oklch(0.66 0.15 305)" stroke-width="2.4" stroke-dasharray="5 150"/>
    <path class="l20dec-w" d="M59 90 L200 90" fill="none" stroke="oklch(0.66 0.15 305)" stroke-width="2.4" stroke-dasharray="5 150"/>
    <path class="l20dec-a" d="M59 90 Q140 90 200 140" fill="none" stroke="oklch(0.66 0.15 305)" stroke-width="2.4" stroke-dasharray="5 160"/>
    <g font-family="var(--font-mono)" font-size="10" fill="#C7CEE6">
      <rect x="206" y="28" width="120" height="26" rx="6" fill="#1A2236" stroke="#2A3450"/><text x="266" y="45" text-anchor="middle">promptaus</text>
      <rect x="206" y="77" width="120" height="26" rx="6" fill="#1A2236" stroke="#2A3450"/><text x="266" y="94" text-anchor="middle">työnkulku</text>
      <rect x="206" y="126" width="120" height="26" rx="6" fill="#1A2236" stroke="#2A3450"/><text x="266" y="143" text-anchor="middle">agentti</text>
    </g>
  </svg>
</div>
<figcaption class="ai-demo__cap">Kuusi kysymystä ohjaavat valinnan oikealle haaralle — yksinkertaisin riittävä ratkaisu voittaa.</figcaption></figure>
<style>
.l20dec-p,.l20dec-w,.l20dec-a{animation:l20decRun 6s ease-in-out infinite}
.l20dec-w{animation-delay:2s}.l20dec-a{animation-delay:4s}
@keyframes l20decRun{0%{stroke-dashoffset:155}30%{stroke-dashoffset:0}45%,100%{stroke-dashoffset:0;opacity:.25}}
@media (prefers-reduced-motion:reduce){.l20dec-p,.l20dec-w,.l20dec-a{animation:none;stroke-dashoffset:0}}
</style>


**Tilanne 1: Laskujen käsittely.** Yritys käsittelee 100 laskua päivässä. Lasku saapuu, sen summa täytyy vahvistaa ja tiedot pitää kirjata järjestelmään. Säännöt muuttuvat jonkin verran: uusia laskuttajia tulee ja hinnat muuttuvat, mutta perusprosessi pysyy samana. Epäonnistumisen hinta on korkea, koska väärä summa voi aiheuttaa organisaatiolle taloudellista vahinkoa. Ihmisen valvonta on kuitenkin mahdollista: valvoja voi tarkistaa, että laskut on käsitelty oikein.

Kuuden kysymyksen perusteella tehtävä toistuu, on melko monimutkainen, sisältää jonkin verran muuttuvia sääntöjä, aiheuttaa organisaatiotason kustannuksia, sisältää korkean epäonnistumisen hinnan ja mahdollistaa ihmisen valvonnan. Paras ratkaisu on **työnkulku yhdessä ihmisen valvonnan kanssa**. Agentti olisi todennäköisesti ylimitoitettu, ellei laskumäärä kasva huomattavasti tai tapausten monimutkaisuus lisäänny merkittävästi.

**Tilanne 2: Sähköpostien lajittelu.** Sähköposteja tulee satoja päivässä, mutta tehtävä on yksinkertainen: viestit luokitellaan sisällön perusteella. Hakusanat pysyvät samoina vuodesta toiseen. Epäonnistumisen hinta on matala. Jos sähköposti menee väärään kansioon, käyttäjä huomaa sen ja siirtää sen itse. Tilanne ei aiheuta kriisiä, eikä jatkuvaa valvontaa tarvita.

Kuuden kysymyksen perusteella tehtävä toistuu, on yksinkertainen, perustuu staattisiin sääntöihin, aiheuttaa pienet kustannukset, sisältää matalan epäonnistumisen hinnan eikä vaadi kriittistä valvontaa. Paras ratkaisu on **yksinkertainen työnkulku**. Agentti olisi tähän tehtävään täysin ylimitoitettu ja turhan kallis.

**Tilanne 3: Asiakaspalvelupyyntöjen reitittäminen.** Organisaatio saa yli 50 yhteydenottoa päivässä. Reititykseen vaikuttavat monet tekijät, kuten asian prioriteetti, työntekijöiden osaaminen, asian kiireellisyys ja asiakassuhteen arvo. Säännöt muuttuvat jatkuvasti, koska työntekijät, käsiteltävät aihealueet ja prioriteetit muuttuvat. Epäonnistumisen hinta on keskikorkea: väärä reititys voi heikentää asiakastyytyväisyyttä. Valvonta on mahdollista, koska esihenkilö voi tarkistaa päätöksiä.

Kuuden kysymyksen perusteella tehtävä toistuu, on monimutkainen, sisältää muuttuvia sääntöjä, aiheuttaa merkittäviä kustannuksia, sisältää keskikorkean epäonnistumisen hinnan ja mahdollistaa valvonnan. Paras ratkaisu on **aloittaa työnkululla ja valmistautua agenttiin**. Jos yritys kasvaa ja tiketit monimutkaistuvat, agenttiin voidaan siirtyä myöhemmin. Aluksi ei kuitenkaan kannata rakentaa liian raskasta ratkaisua.

> **Pysähdy hetkeksi:** Käy läpi nämä kolme tilannetta ja ajattele omaa mahdollista tehtävääsi. Mitä kuusi kysymystä vastaavat sen kohdalla?

## Monimutkaisuus on aina kustannus

Tässä on tärkeä ajatus, jonka monet unohtavat: agentti on monimutkainen. Se ei ole vain ”parempi työnkulku”. Se on luonteeltaan erilainen ratkaisu, ei pelkästään suurempi tai tehokkaampi versio työnkulusta.

Työnkulun kehitysaika mitataan usein tunneissa tai päivissä. Agentin kehitysaika mitataan usein viikoissa tai kuukausissa, koska dynaaminen logiikka vaatii paljon enemmän suunnittelua. Työnkulkua testaa yleensä tekijä, joka ymmärtää säännöt. Agenttia täytyy testata laajemmin, koska sen dynaamisuus voi tuottaa odottamattomia tuloksia. Agentti vaatii myös jatkuvaa valvontaa. Jos agentti oppii virheistä, sinun täytyy seurata, mitä se on oppinut ja ovatko opitut asiat oikeanlaisia. Jos agentti alkaa tehdä systemaattisesti virheellisiä johtopäätöksiä, sinun täytyy puuttua sen toimintaan ja muuttaa sen ohjeistusta.

Kysy siis aina: miksi rakennan agentin? Vastaus perustuu kustannusten ja hyötyjen vertailuun. Jos työnkulku ratkaisee ongelmasi 80 prosentissa tapauksista ja agentti ratkaisee sen 85 prosentissa tapauksista, oletko valmis maksamaan 10 kertaa suuremmat kehitys- ja ylläpitokustannukset viiden prosenttiyksikön parannuksesta? Usein vastaus on ei. Jos työnkulku ratkaisee vain 40 prosenttia tapauksista ja agentti 95 prosenttia tapauksista, hyöty voi olla selvästi kustannuksia suurempi. Silloin agentti voi olla järkevä ratkaisu.

## Miltä nämä päätökset näyttävät n8n:ssä?

Kun rakennat ratkaisua n8n:ssä, tässä oppitunnissa käsitellyt päätökset muuttuvat konkreettisiksi valinnoiksi n8n:n visuaalisessa editorissa.

**Yksinkertainen promptaus n8n:ssä:** yksi AI Agent -solmu saa viestin ja vastaa siihen. Muita solmuja ei tarvita. Tämä riittää, kun tehtävä on yksinkertainen.

**Työnkulku n8n:ssä:** sarja solmuja seuraa toisiaan. Esimerkiksi: Email Trigger → IF-solmu, joka tarkistaa avainsanan → Slack-solmu, joka lähettää viestin oikealle kanavalle. Logiikka on kiinteä: sama syöte tuottaa aina saman tuloksen.

**Agentti n8n:ssä:** AI Agent -solmulla on pääsy **työkaluihin**, kuten tietokantaan, verkkohakuun tai tiedostoihin. Agentti päättää itse, mitä työkalua se käyttää. Tämä on monimutkaisempaa mutta joustavampaa.

Tämän esikatselun tarkoitus on yksinkertainen: kun tulet oppitunnille 26 ja avaat n8n:n, tiedät jo, **mitä olet rakentamassa ja miksi**. Päätös promptauksen, työnkulun ja agentin välillä on **arkkitehtuuripäätös**, ei pelkkä työkalupäätös.

## Kohti omaa projektia

Kun olet valinnut oppitunnilla 19 oman agenttiongelmasi, tämän oppitunnin kuusi kysymystä auttavat sinua tarkistamaan, onko agentti todella oikea ratkaisu. Palaa päätöspuuhun ja käy ongelmasi läpi: toistuuko tehtävä, onko se riittävän monimutkainen ja muuttuvatko säännöt tilanteen mukaan? Jos päätöspuu osoittaa, että yksinkertaisempi ratkaisu riittäisi, harkitse ongelman tarkentamista sellaiseksi, jossa agentin autonomisuus tuottaa aidosti lisäarvoa.

## Yhteenveto

Automatisointi on jatkumo, ei joko–tai-valinta. Älä valitse agenttia automaattisesti. Kysy ensin nämä kuusi kysymystä: **Toistuuko tehtävä?** **Onko tehtävä monimutkainen?** **Muuttuvatko säännöt?** **Kuka maksaa?** **Mitkä ovat epäonnistumisen kustannukset?** **Onko valvonta mahdollista?**

Päätöspuu ohjaa sinut oikean välineen luo. Yksinkertainen työnkulku ratkaisee usein ongelman riittävän hyvin ja paljon pienemmillä kustannuksilla kuin agentti. Valitse aina yksinkertaisin ratkaisu, joka todella toimii.

---
