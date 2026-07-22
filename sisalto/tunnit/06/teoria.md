# Kuvat, ääni ja teksti — kun sanat eivät riitä

## Johdanto: anna mallille se havainto, jota tehtävä vaatii

Jos pyydät tekoälyä selittämään kaaviota mutta kuvailet kaavion vain muistisi varassa, osa tiedosta katoaa jo ennen kuin työ alkaa. Jos taas haluat korjata yhden virkkeen ja lähetät siitä epätarkan kuvakaappauksen, valitset tehtävään hankalamman aineistomuodon kuin tarvitset.

Tämän tunnin ajatus on yksinkertainen: **valitse aineistomuoto sen perusteella, mitä tekoälyn pitää havaita**. Kuva ei ole aina tekstiä parempi. Ääni ei ole aina kuvaa rikkaampi. Useampi aineisto ei automaattisesti paranna vastausta. Hyvä käyttäjä tunnistaa, mikä tieto on tehtävän kannalta olennaista ja missä muodossa se säilyy parhaiten.

> **Tunnin ydinkysymys:** Mitä mallin pitää nähdä, kuulla tai lukea, jotta se voi auttaa — ja mitä aineistosta ei pidä lähettää lainkaan?

<figure class="ai-demo"><span class="ai-demo__tag" id="l06-t"><i aria-hidden="true">// </i>sama tieto kahdessa muodossa — tehtävä ratkaisee kumpi voittaa</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:310px">
  <div class="l06-wrap" data-once role="img" aria-labelledby="l06-t" aria-describedby="l06-d">
    <span class="sr-only" id="l06-d">Sama aineisto kaaviona ja taulukkona: tarkka muutos löytyy taulukosta, harhaanjohtava asteikko näkyy vain kaaviosta. Muoto valitaan tehtävän mukaan.</span>
    <span class="l06-title">MITÄ TEHTÄVÄN PITÄÄ HAVAITA?</span>
    <span class="l06-task ta">Tehtävä 1 · laske tarkka muutos</span>
    <span class="l06-task tb">Tehtävä 2 · onko asteikko harhaanjohtava?</span>
    <div class="l06-p pk"><i class="l06-ph">KUVA · KAAVIO</i>
      <span class="l06-ax">10┤</span>
      <i class="l06-bar b1"></i><i class="l06-bar b2"></i>
      <span class="l06-yr y1">2024</span><span class="l06-yr y2">2025</span>
      <span class="l06-chip ca1">≈ 40 %?</span>
      <span class="l06-chip cb1">✓ katkaistu akseli</span></div>
    <div class="l06-p pt"><i class="l06-ph pht">TAULUKKO</i>
      <span class="l06-row r1">2024&nbsp;&nbsp;12,4</span>
      <span class="l06-row r2">2025&nbsp;&nbsp;17,9</span>
      <span class="l06-chip ca2">✓ +44,4 %</span>
      <span class="l06-chip cb2">esitystapa ei näy —</span></div>
    <span class="l06-log lg1">✓ tarkat luvut → taulukko</span>
    <span class="l06-log lg2">✓ asteikko ja esitystapa → kuva</span>
    <span class="l06-syn">Kumpikin voitti kerran — muoto valitaan tehtävän mukaan</span>
    <span class="l06-chk">Tarkista havainto lopuksi alkuperäisestä aineistosta</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Aineistomuoto ei ole koriste. Kaaviosta hahmottaa suunnan ja esitystavan valinnat, taulukko säilyttää tarkat arvot laskentaan. Sama aineisto — kumpikin muoto voittaa oman tehtävänsä. Tarkista havainto lopuksi alkuperäisestä aineistosta.</figcaption></figure>
<style>
.l06-wrap{position:relative;width:560px;height:294px;font-family:var(--font-mono);animation:l06w 16s 1 forwards}
.l06-title{position:absolute;left:0;top:0;width:560px;text-align:center;font-size:13px;font-weight:700;letter-spacing:.08em;color:#EAEEF8}
.l06-task{position:absolute;left:130px;top:32px;width:300px;box-sizing:border-box;text-align:center;font-size:12px;line-height:1.2;color:#EAEEF8;background:#0E1524;border:1.5px solid #46C7CF;border-radius:999px;padding:5px 10px;opacity:0}
.l06-task.ta{animation:l06ta 16s 1 forwards}
.l06-task.tb{border-color:#C9B7F1;animation:l06tb 16s 1 forwards}
.l06-p{position:absolute;top:76px;width:252px;height:118px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:8px 10px}
.l06-p.pk{left:16px}.l06-p.pt{left:292px}
.l06-ph{display:block;font-style:normal;font-size:12px;font-weight:700;letter-spacing:.1em;color:#C9B7F1}
.l06-ph.pht{color:#46C7CF}
.l06-ax{position:absolute;left:12px;bottom:34px;font-size:12px;color:#B9C2DA}
.l06-bar{position:absolute;bottom:36px;width:24px;background:#46C7CF;border-radius:3px 3px 0 0}
.l06-bar.b1{left:30px;height:26px;opacity:.75}
.l06-bar.b2{left:68px;height:40px}
.l06-yr{position:absolute;bottom:22px;font-size:12px;color:#8B94B3}
.l06-yr.y1{left:24px}.l06-yr.y2{left:62px}
.l06-row{position:absolute;left:16px;font-size:12px;line-height:1.2;color:#EAEEF8}
.l06-row.r1{top:38px}.l06-row.r2{top:60px}
.l06-chip{position:absolute;font-size:12px;line-height:1.2;font-weight:700;border-radius:7px;padding:3px 7px;opacity:0;white-space:nowrap}
.l06-chip.ca1{right:10px;top:34px;color:#FFD79A;border:1px solid #FFD79A;background:rgba(255,215,154,.07);animation:l06ca1 16s 1 forwards}
.l06-chip.cb1{right:10px;bottom:10px;color:#7FD0A8;border:1px solid #7FD0A8;background:rgba(127,208,168,.08);animation:l06cb 16s 1 forwards}
.l06-chip.ca2{right:10px;top:34px;color:#7FD0A8;border:1px solid #7FD0A8;background:rgba(127,208,168,.08);animation:l06ca2 16s 1 forwards}
.l06-chip.cb2{right:10px;bottom:10px;color:#FFD79A;border:1px solid #FFD79A;background:rgba(255,215,154,.07);animation:l06cb 16s 1 forwards}
.l06-log{position:absolute;left:0;width:560px;text-align:center;font-size:12px;line-height:1.2;color:#7FD0A8;opacity:0}
.l06-log.lg1{top:204px;animation:l06lg1 16s 1 forwards}
.l06-log.lg2{top:226px;animation:l06lg2 16s 1 forwards}
.l06-chk{position:absolute;left:0;top:274px;width:560px;text-align:center;font-size:12px;color:#B9C2DA;opacity:0;animation:l06chk 16s 1 forwards}
.l06-syn{position:absolute;left:0;top:252px;width:560px;text-align:center;font-size:12px;font-weight:600;color:#FFD79A;opacity:0;animation:l06syn 16s 1 forwards}
@keyframes l06w{0%{opacity:0}4.4%{opacity:1}96.5%,100%{opacity:1}}
@keyframes l06ta{0%,4.4%{opacity:0;transform:translateY(6px)}8%{opacity:1;transform:none}45%{opacity:1}49%,100%{opacity:0}}
@keyframes l06tb{0%,45%{opacity:0;transform:translateY(6px)}49%{opacity:1;transform:none}100%{opacity:1}}
@keyframes l06ca1{0%,12%{opacity:0}16%{opacity:1;transform:rotate(0)}18%{transform:rotate(-2.5deg)}20%{transform:rotate(2.5deg)}22%{transform:rotate(0)}45%{opacity:1}49%,100%{opacity:.7}}
@keyframes l06ca2{0%,18%{opacity:0}22%{opacity:1}45%{opacity:1}49%,100%{opacity:.7}}
@keyframes l06cb{0%,55%{opacity:0}60%,100%{opacity:1}}
@keyframes l06lg1{0%,38%{opacity:0}42%{opacity:1}88%{transform:scale(1)}90%{transform:scale(1.05)}92%,100%{opacity:1;transform:scale(1)}}
@keyframes l06lg2{0%,78%{opacity:0}82%{opacity:1}89%{transform:scale(1)}91%{transform:scale(1.05)}93%,100%{opacity:1;transform:scale(1)}}
@keyframes l06syn{0%,86%{opacity:0}90%,100%{opacity:1}}
@keyframes l06chk{0%,90%{opacity:0}94%,100%{opacity:1}}
@media (prefers-reduced-motion:reduce){
  .l06-wrap,.l06-wrap *{animation:none!important}
  .l06-wrap,.l06-task.ta,.l06-task.tb,.l06-chip.cb1,.l06-chip.cb2,.l06-log,.l06-syn,.l06-chk{opacity:1}
  .l06-task.ta{left:6px;width:268px;transform:none}
  .l06-task.tb{left:286px;width:268px;transform:none}
  .l06-chip.ca1,.l06-chip.ca2{opacity:.7}
}
</style>

## Multimodaalisuus tarkoittaa useita tietomuotoja

**Modaliteetti** tarkoittaa tietomuotoa, kuten tekstiä, kuvaa tai ääntä. **Multimodaalinen malli** pystyy käsittelemään useampaa kuin yhtä tietomuotoa. Se voi esimerkiksi lukea käyttäjän kysymyksen ja tarkastella siihen liitettyä valokuvaa.

Käytännössä useimmat tunnetut keskustelupalvelut ovat nykyään multimodaalisia: ChatGPT, Claude, Microsoft Copilot ja Google Gemini pystyvät kaikki käsittelemään sekä tekstiä että kuvaa, ja osa myös ääntä. Se ei tarkoita, että ne olisivat yhtä hyviä kaikissa muodoissa — ja juuri sitä tämän tunnin vertailukoe selvittää.

Eri muodot säilyttävät eri asioita:

| Aineistomuoto | Mitä se säilyttää hyvin? | Mitä siitä voi kadota? |
| --- | --- | --- |
| Teksti | Tarkka sanamuoto, nimet, luvut ja muokattavuus | Ulkoasu, sijainti ja visuaaliset suhteet |
| Kuva | Sommittelu, sijainti, muodot, värit ja näkyvä kokonaisuus | Pienen tekstin tarkkuus ja kuvan ulkopuolinen tapahtuma |
| Taulukko | Rivien, sarakkeiden ja lukujen rakenne | Alkuperäisen tilanteen tai mittauksen tausta |
| Ääni | Puhe, tauot, ääntämys ja keskustelun ajallinen kulku | Puhujan tarkoitus ei selviä varmasti pelkästä äänensävystä |
| Dokumentti | Pitkä rakenne, otsikot, kappaleet ja lähdeyhteys | Skannatun tai huonosti jäsennetyn tiedoston sisältö voi tulkkiutua väärin |

Valinta alkaa kysymyksestä, ei tiedostosta. Jos haluat mallin arvioivan painikkeiden sijoittelua, kuva on olennainen. Jos haluat muokata painikkeen tekstiä, kopioitu teksti on tarkempi. Jos haluat tarkastella myynnin kehitystä, alkuperäinen taulukko on usein parempi kuin kuva pylväsdiagrammista.

## Teksti sopii tarkkaan sisältöön ja muokkaamiseen

Käytä tekstiä, kun sanamuodon, lukujen tai rakenteen pitää säilyä täsmällisenä. Tekstiä voi lainata, hakea, vertailla ja muokata suoraan.

Ajattele vaikka viestiä, jonka sävyä haluat muuttaa, tai ohjetta, josta tarvitset selkokielisen version. Kun annat alkuperäisen tekstin mallille tekstinä, jokainen sana säilyy tarkasteltavana. Sama koskee laskennassa tarvittavia taulukkoarvoja, virheilmoituksen täsmällistä sanamuotoa sekä koodia, jota pitää muokata rivi riviltä. Kuvakaappaus voi näyttää nämä asiat, mutta se lisää turhaan yhden tulkintavaiheen: mallin pitää ensin lukea kuvassa oleva teksti oikein.

Pelkkä aineisto ei kuitenkaan kerro tavoitetta. Lisää aina lyhyt tehtävänanto: mitä aineistosta tarkastellaan, kenelle tulos tehdään ja missä muodossa vastaus tarvitaan.

## Kuva sopii näkyvien suhteiden tarkasteluun

Kuva on hyödyllinen silloin, kun ongelma sijaitsee asioiden välisissä suhteissa: mikä on minkä vieressä, mikä puuttuu, miten kokonaisuus on jäsennelty tai mitä ympäristössä näkyy. Sovelluksen päällekkäiset painikkeet tai kaavion epäselvä selite on helpompi havaita kuvasta kuin pitkästä kuvauksesta. Samoin laitteen merkkivalot, pakkauksen kuvan ja tekstin yhteys tai käsin kirjoitetun muistiinpanon rakenne voivat olla juuri sitä tietoa, joka katoaisi pelkäksi tekstiksi muutettuna.

Hyvä kuvapyyntö kertoo kolme asiaa:

1. **Tilanne:** Mistä kuva on ja miksi se on otettu?
2. **Kohde:** Mitä kohtaa mallin pitää tarkastella?
3. **Tehtävä:** Mitä haluat mallin selittävän, vertaavan tai ehdottavan?

Esimerkiksi: ”Tämä on kuvakaappaus ilmoittautumissivusta puhelimella. Tarkastele vain lomakkeen rakennetta. Mitkä kaksi kohtaa vaikeuttavat käyttäjän etenemistä? Älä päättele kuvasta henkilön ominaisuuksia.”

## Taulukko on usein kuvaa parempi numeroille

Kaavio näyttää kehityksen nopeasti, mutta alkuperäinen taulukko kertoo arvot tarkemmin. Jos tehtävä vaatii laskemista, poikkeamien etsimistä tai rivien vertailua, anna taulukko mieluiten rakenteisessa muodossa.

Jos tehtävässä tarvitaan sekä yleiskuvaa että täsmällisiä lukuja, muodot voi yhdistää tarkoituksellisesti. Kaavion kuva näyttää esitystavan ja kehityssuunnan, alkuperäinen taulukko antaa tarkat arvot ja lyhyt teksti kertoo, mitä päätöstä varten analyysi tehdään. Tämä ei tarkoita, että mukaan lisätään kaikki mahdollinen aineisto. Jokaisella liitteellä pitää olla nimetty tehtävä.

## Ääni säilyttää ajallisen kulun

Ääntä kannattaa käyttää, kun kiinnostuksen kohde on puheessa tai tapahtumien järjestyksessä. Esimerkiksi ääntämisen harjoittelu, kokouksen puheenvuorojen jäsentäminen tai haastattelun litterointi perustuvat tietoon, jota pelkkä jälkikäteen kirjoitettu yhteenveto ei säilytä.

Ääni ei kuitenkaan ole varma ikkuna ihmisen tunteisiin tai tarkoituksiin. Malli voi tulkita tauon, painotuksen tai puhujan asenteen väärin. Siksi turvallinen tehtävä kohdistuu havaittavaan asiaan. Voit pyytää mallia kirjoittamaan puheen tekstiksi ja merkitsemään epäselvät kohdat, tunnistamaan aiheen vaihtumisen tai vertaamaan ääntämystä annettuun malliin.

Vältä perusteettomia päätelmiä puhujan terveydestä, luonteesta, rehellisyydestä tai tunnetilasta.

## Vertailukoe paljastaa, mitä aineisto lisää

Tämän tunnin tehtävässä annat saman ongelman kahdessa eri aineistomuodossa. Kokeen tarkoitus ei ole todistaa, että toinen muoto voittaa. Tarkoitus on tunnistaa, **mitä uutta havaittavaa tietoa aineistomuodon vaihtaminen toi**.

Jotta vertailu kertoisi aineistomuodon vaikutuksesta, pidä mahdollisimman samoina:

- tehtävä
- taustatieto
- tavoiteltu vastausmuoto
- malli ja keskustelun lähtötilanne.

Muuten et tiedä, johtuiko ero aineistosta vai jostakin muusta muutoksesta.

Vertaa vastauksia nimetyillä kriteereillä. Löysikö toinen muoto sellaisen suhteen, jota toinen ei sisältänyt? Lukiko malli pienen tekstin väärin tai hävisikö litteroinnissa jotakin olennaista? Keskittyikö se epäolennaiseen yksityiskohtaan? Hyvä johtopäätös voi olla myös se, että yksinkertaisempi aineistomuoto riitti paremmin.

## Enemmän aineistoa ei tarkoita parempaa vastausta

Ylimääräinen aineisto voi lisätä kohinaa, kuluttaa konteksti-ikkunaa ja ohjata huomion pois olennaisesta. Valitse siksi pienin aineistokokonaisuus, joka säilyttää tehtävässä tarvittavan tiedon.

Kysy jokaisesta liitteestä:

- Mitä uutta tämä tuo?
- Riittääkö tiedostosta rajattu kohta?
- Voiko tarkan sisällön antaa turvallisemmin tekstinä?
- Miten tarkistan mallin tekemän tulkinnan?

## Turvallisuus ratkaistaan ennen lähettämistä

Kuva voi sisältää nimiä, kasvoja, osoitteita, ilmoituksia ja avoimia välilehtiä. Äänite voi sisältää sivullisten puhetta. Dokumentin metatiedoissa tai taulukon piilotetuissa sarakkeissa voi olla tietoa, jota et huomaa ensisilmäyksellä.

Ennen lähettämistä:

1. varmista, että aineiston käyttö on sallittu
2. rajaa mukaan vain tehtävässä tarvittava osa
3. poista henkilötiedot, salaisuudet ja tarpeettomat tunnisteet
4. tarkista myös kuvan reunat, tiedoston muut välilehdet ja äänen taustapuhe
5. käytä organisaation hyväksymää palvelua

Pelkkä peittäminen ei aina riitä, jos alkuperäinen tieto jää tiedostoon palautettavaksi. Tee jaettavaan käyttöön erillinen kopio ja tarkista se ennen lähettämistä.

## Mallin havainto pitää edelleen tarkistaa

Multimodaalinen malli voi lukea tekstin väärin, sekoittaa kaavion sarjat, jättää osan kuvasta huomiotta tai litteroida nimen virheellisesti. Siksi vastaus ei ole todiste aineistosta.

Tarkista tärkeä havainto alkuperäisestä materiaalista. Pyydä mallia tarvittaessa osoittamaan, mihin kuvan kohtaan, taulukon riviin tai äänitteen aikaleimaan havainto perustuu. Jos perustetta ei löydy, älä käytä väitettä päätöksen pohjana.

## Yhteenveto

Valitse aineistomuoto sen mukaan, mitä tehtävässä pitää havaita:

- teksti säilyttää tarkan sisällön ja helpottaa muokkaamista
- kuva näyttää näkyvät suhteet ja kokonaisuuden
- taulukko pitää luvut rakenteisina
- ääni säilyttää puheen ajallisen kulun
- dokumentti pitää pidemmän lähdeaineiston rakenteen ja asiayhteyden koossa.

Yhdistä muotoja vain silloin, kun jokainen tuo tehtävään oman tarpeellisen havaintonsa. Rajaa aineisto, suojaa tiedot ja tarkista mallin tulkinta alkuperäisestä lähteestä. Näin multimodaalisuus ei tarkoita mahdollisimman monen liitteen lähettämistä, vaan harkittua tapaa antaa mallille juuri se tieto, jota työ vaatii.

> **Lopuksi pohdittavaksi:** Minkä tiedon menetät, jos muutat aineiston toiseen muotoon — ja onko juuri se tieto tehtäväsi kannalta olennainen?

---

## Lähteet ja tarkistuspäivä

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [W3C: Making Audio and Video Media Accessible](https://www.w3.org/WAI/media/av/)

Tarkistettu 20.7.2026.
