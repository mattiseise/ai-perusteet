# Oma botti III — toteutustapa, erikoistyökalut ja käyttöönotto

## Johdanto: valitse toteutus, jonka pystyt perustelemaan

Tunneilla 14 ja 15 määrittelit apuri-bottisi tehtävän, rajat, tietopohjan ja testit. Ennen rakentamista tarvitset vielä toteutuspäätöksen. Toteutustapa ei ole vain alustan nimi, vaan perusteltu kuvaus siitä, mitä ominaisuuksia tarvitset, mitä aineistoa ratkaisu käsittelee, kuka pääsee siihen ja millaisella näytöllä voit osoittaa sen toiminnan.

Tekstiä tuottava chat on vain yksi mahdollisuus. Botti voi hyödyntää kuvaa, ääntä tai musiikkia, videota tai rajattua kooditoimintoa, jos se palvelee käyttäjän tehtävää. Nämä erikoistyökalut säilyvät tunnin näkyvänä laboratoriona, mutta niiden tarkoitus on auttaa tekemään omaa bottiprojektia koskeva valinta. Välineet ja tuotokset eroavat, mutta vastuullinen työskentely etenee samalla tavalla:

1. määritä todellinen käyttötarve
2. päätä onnistumisen kriteerit
3. tee ensimmäinen versio
4. nimeä yksi havaittava puute
5. muuta yhtä asiaa
6. vertaa toista versiota ensimmäiseen
7. tee oikeuksiin, turvallisuuteen ja laatuun perustuva julkaisu- tai käyttöpäätös.

Järjestys on olennainen: kriteerit päätetään ennen ensimmäistä versiota, jotta niitä ei madalleta jälkikäteen sopimaan syntyneeseen tuotokseen.

Tällä tunnilla tutkit neljää näkyvää reittiä ja kokeilet niistä yhtä: kuvaa, ääntä tai musiikkia, videota tai koodia. Kaikkien ei tarvitse lisätä erikoistyökalua omaan bottiinsa. Ydintaito on osata päättää, tuoko työkalu käyttäjälle todellista hyötyä vai kasvattaako se vain toteutuksen riskiä ja työmäärää.

Tunnin läpi kulkee yksi esimerkki. Kirjasto tarvitsee verkkosivulleen 20 sekunnin äänettömän opastusvideon, joka näyttää kirjan palauttamisen kolmessa vaiheessa. Ennen videon tekemistä sovitaan, että vaiheiden pitää näkyä oikeassa järjestyksessä, tekstitykset pitää ehtiä lukea rauhassa, esineiden ja tilan pitää säilyä johdonmukaisina eikä kuvassa saa olla tunnistettavia asiakkaita. Nämä kriteerit eivät muutu sen mukaan, millainen ensimmäisestä versiosta tulee.

<figure class="ai-demo"><span class="ai-demo__tag" id="l16-t"><i aria-hidden="true">// </i>väline vaihtuu — sykli ei: tavoite → kriteerit → versio → havainto → yksi muutos → vastuullisuustarkistus → julkaisu</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:418px">
  <div class="l16-wrap" data-once role="img" aria-labelledby="l16-t" aria-describedby="l16-d">
    <span class="sr-only" id="l16-d">Sama arviointisykli toistuu neljällä välineellä: tavoite, kriteerit, versio 1, havainto, täsmälleen yksi muutos, versio 2, vastuullisuustarkistus ja julkaisu tai hylkäys. Kuva: kohde hukkui taustaan, sommittelu tarkennettiin. Ääni: puhe peittyi musiikkiin, voimakkuussuhde muutettiin. Video: tekstitys vaihtui liian nopeasti, kohtauksen kesto muutettiin seitsemään sekuntiin. Koodi: tyhjä syöte kaatoi ohjelman, virhetesti lisättiin. Laboratorioloki kerää havainnon ja muutoksen joka kierrokselta.</span>
    <span class="l16-md md1">KUVA</span><span class="l16-md md2">ÄÄNI</span><span class="l16-md md3">VIDEO</span><span class="l16-md md4">KOODI</span>
    <div class="l16-cy"><i class="l16-ph">SYKLI</i><span class="l16-dl">Δ muutoksia: 1</span>
      <span class="l16-st s1">TAVOITE</span><i class="l16-ar aa1">→</i><span class="l16-st s2">KRITEERIT</span><i class="l16-ar aa2">→</i><span class="l16-st s3">VERSIO 1</span><i class="l16-ar aa3">→</i><span class="l16-st s4">HAVAINTO</span>
      <i class="l16-ar dn">↓</i>
      <span class="l16-st r2 s8">JULKAISE / HYLKÄÄ</span><i class="l16-ar aa4">←</i><span class="l16-st r2 s7">VASTUULLISUUS-TARKISTUS</span><i class="l16-ar aa5">←</i><span class="l16-st r2 s6">VERSIO 2</span><i class="l16-ar aa6">←</i><span class="l16-st r2 s5">1 MUUTOS</span>
      <i class="l16-tok"></i>
      <span class="l16-sl"><b class="v1">kohde hukkui taustaan → sommittelu tarkennettu</b><b class="v2">puhe peittyi musiikkiin → voimakkuussuhde muutettu</b><b class="v3">tekstitys vaihtui liian nopeasti → kohtauksen kesto 7 sekuntiin</b><b class="v4">tyhjä syöte kaataa ohjelman → virhetesti lisätty</b></span></div>
    <div class="l16-lg"><i class="l16-ph">LABORATORIOLOKI</i>
      <span class="l16-hr"><b>väline</b><b>havainto</b><b>yksi muutos</b></span>
      <span class="l16-row r1"><b class="tg t1">KUVA</b><b>kohde hukkui taustaan</b><b>sommittelu tarkennettu</b></span>
      <span class="l16-row rw2"><b class="tg t2">ÄÄNI</b><b>puhe peittyi musiikkiin</b><b>voimakkuussuhde muutettu</b></span>
      <span class="l16-row rw3"><b class="tg t3">VIDEO</b><b>tekstitys vaihtui liian nopeasti</b><b>kohtauksen kesto 7 sekuntiin</b></span>
      <span class="l16-row rw4"><b class="tg t4">KOODI</b><b>tyhjä syöte kaataa ohjelman</b><b>virhetesti lisätty</b></span></div>
    <span class="l16-ft">Väline vaihtuu — sykli ei</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Erikoistuneet työkalut eroavat tuotoksissa, mutta työtapa on sama: tavoite ja kriteerit, versio, havainto, täsmälleen yksi nimetty muutos, uusi versio, vastuullisuustarkistus ja vasta sitten julkaisu tai hylkäys. Tärkein tuotos on loki, johon havainto ja muutos kirjataan joka kierrokselta.</figcaption></figure>
<style>
.l16-wrap{position:relative;width:560px;height:402px;font-family:var(--font-mono);animation:l16w 28s 1 forwards}
.l16-ph{display:block;font-style:normal;font-size:12px;font-weight:700;letter-spacing:.06em;color:#EAEEF8}
.l16-md{position:absolute;top:0;width:100px;height:26px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#EAEEF8;border:1px solid #2B3552;border-radius:999px;background:#0E1524;opacity:.55}
.l16-md.md1{left:60px;animation:l16md1 28s 1 forwards}
.l16-md.md2{left:172px;animation:l16md2 28s 1 forwards}
.l16-md.md3{left:284px;animation:l16md3 28s 1 forwards}
.l16-md.md4{left:396px;animation:l16md4 28s 1 forwards}
.l16-cy{position:absolute;left:0;top:34px;width:560px;height:168px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:8px 10px}
.l16-st{position:absolute;top:26px;width:118px;height:38px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;font-size:12px;font-weight:700;color:#EAEEF8;border:1px solid #4A5677;border-radius:8px;background:#0E1524}
.l16-st.s1{left:10px}.l16-st.s2{left:148px}.l16-st.s3{left:286px}.l16-st.s4{left:424px}
.l16-st.r2{top:78px}
.l16-st.s5{left:424px}.l16-st.s6{left:286px}.l16-st.s7{left:148px}.l16-st.s8{left:10px;font-size:12px}
.l16-ar{position:absolute;font-style:normal;font-size:13px;color:#7E88A8}
.l16-ar.aa1{left:131px;top:38px}.l16-ar.aa2{left:269px;top:38px}.l16-ar.aa3{left:407px;top:38px}
.l16-ar.dn{left:479px;top:63px}
.l16-ar.aa4{left:131px;top:90px}.l16-ar.aa5{left:269px;top:90px}.l16-ar.aa6{left:407px;top:90px}
.l16-tok{position:absolute;left:62px;top:18px;width:12px;height:12px;border-radius:50%;background:#46C7CF;opacity:0;animation:l16tok 28s 1 forwards}
.l16-sl{position:absolute;left:10px;top:124px;width:536px;height:30px}
.l16-sl b{position:absolute;left:0;top:0;width:100%;text-align:center;font-size:12px;line-height:1.25;font-weight:400;color:#FFD79A;opacity:0}
.l16-sl .v1{animation:l16v1 28s 1 forwards}
.l16-sl .v2{animation:l16v2 28s 1 forwards}
.l16-sl .v3{animation:l16v3 28s 1 forwards}
.l16-sl .v4{animation:l16v4 28s 1 forwards}
.l16-dl{position:absolute;right:10px;top:8px;font-size:12px;font-weight:700;color:#C9B7F1;border:1px solid #C9B7F1;border-radius:999px;padding:2px 9px;opacity:0;animation:l16dl 28s 1 forwards}
.l16-lg{position:absolute;left:0;top:212px;width:560px;height:158px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:8px 12px}
.l16-hr,.l16-row{display:flex;gap:10px;margin-top:7px;font-size:12px;line-height:1.25}
.l16-hr b,.l16-row b{font-weight:400}
.l16-hr b:nth-child(1),.l16-row b:nth-child(1){width:52px;flex:none}
.l16-hr b:nth-child(2),.l16-row b:nth-child(2){width:236px;flex:none}
.l16-hr b{color:#7E88A8;letter-spacing:.05em}
.l16-row{color:#EAEEF8;opacity:0}
.l16-row .tg{font-weight:700}
.l16-row .tg.t1{color:#46C7CF}.l16-row .tg.t2{color:#FFD79A}.l16-row .tg.t3{color:#C9B7F1}.l16-row .tg.t4{color:#7FD0A8}
.l16-row.r1{animation:l16r1 28s 1 forwards}
.l16-row.rw2{animation:l16r2 28s 1 forwards}
.l16-row.rw3{animation:l16r3 28s 1 forwards}
.l16-row.rw4{animation:l16r4 28s 1 forwards}
.l16-ft{position:absolute;left:0;top:382px;width:560px;text-align:center;font-size:12.5px;font-weight:600;color:#FFD79A}
@keyframes l16w{0%{opacity:0}2.5%{opacity:1}100%{opacity:1}}
@keyframes l16md1{0%{opacity:.55}1%{opacity:1}23%{opacity:1}25%,100%{opacity:.55}}
@keyframes l16md2{0%,25%{opacity:.55}26%{opacity:1}48%{opacity:1}50%,100%{opacity:.55}}
@keyframes l16md3{0%,50%{opacity:.55}51%{opacity:1}73%{opacity:1}75%,100%{opacity:.55}}
@keyframes l16md4{0%,75%{opacity:.55}76%,100%{opacity:1}}
@keyframes l16tok{
  0%,0.7%{opacity:0;transform:translate(0,0);background:#46C7CF}1.6%{opacity:1}
  3.4%{transform:translate(138px,0)}5.2%{transform:translate(276px,0)}7%{transform:translate(414px,0)}
  8.8%{transform:translate(414px,52px)}10.6%{transform:translate(276px,52px)}12.4%{transform:translate(138px,52px)}14.2%{transform:translate(0,52px)}
  16%{opacity:1;transform:translate(0,52px)}17.5%{opacity:0;transform:translate(0,52px)}
  25%{opacity:0;transform:translate(0,0);background:#FFD79A}25.9%{opacity:1}
  28.4%{transform:translate(138px,0)}30.2%{transform:translate(276px,0)}32%{transform:translate(414px,0)}
  33.8%{transform:translate(414px,52px)}35.6%{transform:translate(276px,52px)}37.4%{transform:translate(138px,52px)}39.2%{transform:translate(0,52px)}
  41%{opacity:1}42.5%{opacity:0;transform:translate(0,52px)}
  50%{opacity:0;transform:translate(0,0);background:#C9B7F1}50.9%{opacity:1}
  53.4%{transform:translate(138px,0)}55.2%{transform:translate(276px,0)}57%{transform:translate(414px,0)}
  58.8%{transform:translate(414px,52px)}60.6%{transform:translate(276px,52px)}62.4%{transform:translate(138px,52px)}64.2%{transform:translate(0,52px)}
  66%{opacity:1}67.5%{opacity:0;transform:translate(0,52px)}
  75%{opacity:0;transform:translate(0,0);background:#7FD0A8}75.9%{opacity:1}
  78.4%{transform:translate(138px,0)}80.2%{transform:translate(276px,0)}82%{transform:translate(414px,0)}
  83.8%{transform:translate(414px,52px)}85.6%{transform:translate(276px,52px)}87.4%{transform:translate(138px,52px)}89.2%{transform:translate(0,52px)}
  91.5%{opacity:1}93%,100%{opacity:0;transform:translate(0,52px)}
}
@keyframes l16v1{0%,7%{opacity:0}9%{opacity:1}23%{opacity:1}25%,100%{opacity:0}}
@keyframes l16v2{0%,32%{opacity:0}34%{opacity:1}48%{opacity:1}50%,100%{opacity:0}}
@keyframes l16v3{0%,57%{opacity:0}59%{opacity:1}73%{opacity:1}75%,100%{opacity:0}}
@keyframes l16v4{0%,82%{opacity:0}84%,100%{opacity:1}}
@keyframes l16dl{0%,10%{opacity:0;transform:scale(.7)}12%,100%{opacity:1;transform:scale(1)}}
@keyframes l16r1{0%,15%{opacity:0;transform:translateY(6px)}17.5%,100%{opacity:1;transform:none}}
@keyframes l16r2{0%,40%{opacity:0;transform:translateY(6px)}42.5%,100%{opacity:1;transform:none}}
@keyframes l16r3{0%,65%{opacity:0;transform:translateY(6px)}67.5%,100%{opacity:1;transform:none}}
@keyframes l16r4{0%,90%{opacity:0;transform:translateY(6px)}92.5%,100%{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){
  .l16-wrap,.l16-wrap *{animation:none!important}
  .l16-wrap,.l16-row,.l16-dl{opacity:1}
  .l16-sl .v4{opacity:1}
  .l16-md{opacity:.85}
  .l16-tok{opacity:0}
}
</style>

## Valitse väline vasta käyttötarkoituksen jälkeen

Älä aloita kysymyksestä ”mitä tällä työkalulla voi tehdä?”. Aloita tarpeesta:

- Mitä tuotosta tarvitaan?
- Kuka sitä käyttää?
- Missä muodossa se julkaistaan tai suoritetaan?
- Mikä on onnistumisen tärkein ehto?
- Mitä virhe voisi aiheuttaa?

Kun nämä asiat ovat selvillä, työkalua voi arvioida tehtävän eikä uutuudenviehätyksen perusteella.

Sama aihe voi vaatia eri välineen eri käyttötarkoituksissa. Tapahtuman tunnelmakuva, äänitunnus, lyhyt mainosvideo ja ilmoittautumislomakkeen koodi eivät ole keskenään vaihtoehtoisia vastauksia samaan tehtävään, vaan ne ratkaisevat eri ongelmia. Kirjaston esimerkissä video on perusteltu valinta, koska työvaihe pitää näyttää ajassa. Jos tarve olisi vain merkitä palautusautomaatin paikka karttaan, kuva olisi selkeämpi ja kevyempi ratkaisu.

## Yhteinen laboratorioloki

Laboratorioloki tekee työskentelystä näkyvää. Riippumatta reitistä tallenna seuraavat tiedot:

- käyttötarkoitus ja kohderyhmä
- palvelu tai työympäristö sekä käytettävissä oleva versio
- syöte tai prompti kokonaisena
- ensimmäinen tuotos
- 3–5 arviointikriteeriä
- yksi havaittu ongelma
- yksi nimetty muutos
- uusi tuotos ja vertailu
- vastuullisuustarkistus

Ilman lokia jäljelle jää vain lopputulos, eikä toinen ihminen voi tietää, syntyikö se harkitulla kokeella vai sattumalta. Lokin avulla pystyt selittämään, mitä teit, miksi valitsit juuri tämän muutoksen ja paransiko se tuotosta. Kirjaston videon lokiin kirjataan siksi myös alkuperäiset kriteerit ennen ensimmäisen version tuottamista.

## Reitti A — kuva

Kuvatyökalulle kirjoitettava syöte alkaa kuvan tehtävästä. Kerro sen jälkeen pääkohde ja toiminta, sommittelu tai kuvakulma, tavoiteltu visuaalinen ilme ja tarvittava kuvasuhde. Rajaa samalla pois sellaiset elementit, jotka tekisivät kuvasta väärän tai harhaanjohtavan. Kaikkea mahdollista ei tarvitse kuvailla; valitse yksityiskohdat sen mukaan, mitä käyttötarkoitus vaatii.

Kuvan laatua ei ratkaise pelkkä näyttävyys. Katso, ohjaako sommittelu huomion olennaiseen ja ovatko tärkeät kohteet, tekstit, symbolit ja mittasuhteet uskottavia. Mieti myös, voisiko katsoja päätellä kuvasta jotakin sellaista, mikä ei pidä paikkaansa. Jos kuva julkaistaan verkossa, sille tarvitaan yleensä vaihtoehtoinen teksti, joka välittää saman olennaisen tiedon kuvan näkemättä.

Todellista tapahtumaa, henkilöä tai tuotetta esittävä kuva vaatii erityistä tarkkuutta. Katsoja ei saa erehtyä pitämään keksittyä yksityiskohtaa dokumentaarisena faktana.

## Reitti B — ääni tai musiikki

Äänituotoksen syötteessä olennaisia ovat käyttötarkoitus, kesto ja rakenne. Kuvaa tempoa, soittimia tai äänimaailmaa sellaisina havaittavina ominaisuuksina, joita voit myöhemmin arvioida. Jos mukana on puhetta, määritä myös kieli, rytmi ja kohderyhmä. Kerro lisäksi, mitä tuotoksessa ei saa olla.

Kuuntele versiota siinä tilanteessa, johon se on tarkoitettu. Täyttyvätkö pyydetty kesto ja rakenne? Erottuuko puhe, ja sopivatko tempo sekä äänenvoimakkuuksien suhteet käyttöön? Häiriö, katkos tai odottamaton ääni voi olla pienessäkin tuotoksessa ratkaiseva puute. Teknisen laadun rinnalla on varmistettava, että käyttö- ja julkaisuoikeudet ovat selvät.

Vältä elävän tekijän äänen, tunnistettavan esiintyjän tai tietyn teoksen jäljittelyä ilman lupaa. Nimeä sen sijaan tarvitsemasi ominaisuudet, kuten rauhallinen tempo, niukka soitinnus, selkeä rakenne ja lämmin tunnelma.

## Reitti C — video

Videossa kuva, aika, liike ja ääni muodostavat kokonaisuuden. Siksi pitkä, yhdellä kertaa kirjoitettu prompti on usein vaikea hallita. Aloita lyhyestä käsikirjoituksesta tai kuvakäsikirjoituksesta, jossa näkyvät tarkoitus, kesto, kohtausten järjestys ja kunkin kohtauksen tapahtuma. Kuvaa vasta sen jälkeen kamera, liike, siirtymät, puhe tai muu ääni, tekstitys ja kuvasuhde. Lopputulokselle pitää voida sanoa yhdellä virkkeellä, mitä katsojan kuuluu ymmärtää.

Kirjaston opastusvideon ensimmäisessä versiossa kolme vaihetta ovat oikeassa järjestyksessä, esineet säilyvät samoina eikä kuvassa näy asiakkaita. Toinen tekstitys vilahtaa kuitenkin niin nopeasti, ettei vertaisarvioija ehdi lukea sitä. Versio 1 ei siis vielä täytä ennen tuottamista sovittua luettavuuskriteeriä, vaikka se näyttää ensi silmäyksellä valmiilta.

Videota arvioidessa tarkista jatkuvuus kohtauksesta toiseen: säilyvätkö henkilöt, esineet ja ympäristö samoina ja näyttääkö liike uskottavalta? Katso myös, tukeeko ääni kuvaa ja välittyykö ydinasia ilman ääntä. Saavutettavuus ei ole lopuksi lisättävä koriste, vaan osa käyttötarkoituksen täyttymistä.

## Reitti D — koodi

Koodityökalun syöte ei ala lauseesta ”tee minulle sovellus”. Kirjoita ensin vaatimus, joka kertoo, mitä ohjelman pitää tehdä, millaisen syötteen se saa ja millaisen tuloksen se palauttaa. Nimeä myös suoritusympäristö ja riippuvuudet sekä ne virhetilanteet ja testit, joilla toiminta osoitetaan. Selkeä vaatimus auttaa erottamaan varsinaisen tarpeen tekoälyn ehdottamasta toteutuksesta.

Koodin sujuva ulkoasu ei todista, että se toimii tai on turvallinen. Lue muutokset ja aja koodi eristetyssä ympäristössä. Tarkista ainakin:

- normaali tapaus
- tyhjä tai virheellinen syöte
- vähintään yksi raja-arvo
- tietoturvan kannalta epäilyttävä syöte
- se, ettei koodi tee pyytämättömiä verkkokutsuja tai tiedostomuutoksia.

Älä suorita tuntematonta koodia vain siksi, että tekoäly vakuuttaa sen olevan turvallista. Vastuu siirtyy sinulle siinä hetkessä, kun päätät ajaa koodin.

## Iteroi yhtä muutosta kerrallaan

Ensimmäinen tuotos on koe, ei valmis työ. Valitse arvioinnissa yksi ongelma ja muuta sitä koskevaa kohtaa syötteessä.

Muutos määräytyy havaitun puutteen perusteella:

- **kuva:** pääkohde hukkuu taustaan → tarkenna sommittelua
- **ääni:** puhe peittyy musiikkiin → muuta äänenvoimakkuuksien suhdetta
- **video:** kohtaus vaihtuu liian nopeasti → muuta kestoa tai leikkausta
- **koodi:** tyhjä syöte kaataa ohjelman → lisää vaatimus ja testi tälle virhetilanteelle.

Kirjaston videossa nimetty puute on toisen tekstityksen liian lyhyt lukuaika. Syötteeseen tehdään yksi muutos: toinen kohtaus kestää seitsemän sekuntia. Sisältöä, kuvakulmaa ja muita asetuksia ei vaihdeta. Versiossa 2 vertaisarvioija ehtii lukea tekstityksen, ja muut ennalta sovitut kriteerit täyttyvät edelleen. Vertailu antaa siten perusteen sanoa, että juuri pidempi kesto korjasi havaitun ongelman.

Kun muutat yhden asian, voit perustellummin arvioida muutoksen vaikutusta. Jos vaihdat samalla tyylin, rakenteen, keston ja työkalun, ennen–jälkeen-vertailu ei kerro, mikä auttoi.

## Tarkista vastuu ennen julkaisemista

Ennen julkaisua tai käyttöönottoa tee kaikilla reiteillä sama vastuullisuustarkistus:

- Onko syöte tai lähdeaineisto omaa tai luvallisesti käytettävää?
- Saako tuotoksen julkaista suunnitellussa käytössä?
- Voiko tuotos johtaa katsojaa, kuulijaa tai käyttäjää harhaan?
- Sisältääkö se henkilötietoja, tunnistettavan äänen tai luottamuksellista koodia?
- Miten tekoälyn osuus kerrotaan yleisölle tai tilaajalle?
- Kuka tarkistaa tuotoksen ennen käyttöä?

Palvelun käyttöehdot, lisenssit ja ominaisuudet voivat muuttua. Tarkista ne aina siitä palvelusta ja tilistä, jota käytät. Kurssin tarkoitus ei ole antaa pysyvää tuotesuositusta.

Kirjaston videon lähdeaineisto on kirjaston omaa, kuvassa ei ole tunnistettavia henkilöitä, tekstitys toimii ilman ääntä ja ihminen on tarkistanut vaiheiden oikeellisuuden. Koska myös version 2 luettavuus täyttää ennalta sovitun kriteerin, video voidaan julkaista. Jos tekstitys olisi yhä liian nopea tai jokin käyttöoikeus jäisi epäselväksi, oikea päätös olisi hylätä versio ja jatkaa korjaamista — ei madaltaa kriteeriä jälkikäteen.

## Vertaa bottisi toteutustapoja

Palaa nyt omaan apuri-bottiisi. Vertaa vähintään kahta toteutustapaa samoilla kysymyksillä. Ensimmäinen voi olla varsinainen bottialusta, jossa ohjeet ja tietopohja määritetään pysyvästi. Toinen voi olla dokumentoitu suunnittelupolku, jossa arkkitehtuuri ja suoritusjälki kuvataan ilman väitettä toimivasta integraatiosta. Jos harkitset kuva-, ääni-, video- tai koodityökalua, käsittele sitä yhtenä toteutuksen osana, ei koko projektin tarkoituksena.

Vertailussa tarkistat käytettävyyden lisäksi aineiston soveltuvuuden, käyttöoikeudet, kustannukset, saavutettavuuden, ylläpidon ja sen, millaista näyttöä ratkaisu voi tuottaa. Tekninen toteutus voi osoittaa alustan todellisen toiminnan, tietopohjan kytkennän ja jakamisen rajat. Dokumentoitu suunnittelupolku voi osoittaa arkkitehtuurin, simuloidun suoritusjäljen, testit ja tunnistetut rajoitukset, mutta se ei todista integraation, käyttöoikeuksien tai tallennuksen toimivan käytännössä.

## Tee kolme päätöstä ennen rakentamista

Kirjaa tunnin lopuksi kolme toisiinsa liittyvää päätöstä. **Toteutuspäätös** kertoo, minkä polun ja ympäristön valitset sekä miksi ne riittävät rajattuun tehtävään. **Riskipäätös** nimeää tärkeimmän aineisto-, käyttöoikeus-, harhaanjohtavuus- tai teknisen riskin ja keinon, jolla rajaat sitä. **Käyttöönottopäätös** kertoo, kuka saa käyttää bottia, kuka tarkistaa sen vastaukset, millä testillä käyttöönotto hyväksytään ja milloin käyttö keskeytetään.

Yksinkertaisin riittävä ratkaisu on usein paras. Jos tavallinen tekstibotti ratkaisee tehtävän, erillistä kuva-, ääni-, video- tai koodityökalua ei tarvita. Jos lisätyökalu on perusteltu, sen oma syöte, tuotos, oikeudet ja virhetilanne lisätään testisuunnitelmaan.

## Yhteenveto

Kuva, ääni, video ja koodi tarvitsevat erilaiset syötteet ja laatukriteerit. Niitä yhdistää sama työskentelytapa: käyttötarve johtaa ennalta päätettyihin kriteereihin, ensimmäisen version puute johtaa yhteen perusteltuun muutokseen ja versioiden vertailu johtaa julkaisu- tai hylkäyspäätökseen. Oman bottisi kannalta tärkein kysymys on, kuuluuko erikoistyökalu perustellusti toteutukseen vai rajataanko se pois.

Tunnin ainoa tallennettava tuotos on **bottiprojektin valintakortti**. Siinä vertailet kaikkia neljää työkalureittiä tiiviisti, dokumentoit yhden käytännön kokeilun ja teet toteutus-, riski- ja käyttöönottopäätöksen. Muista reiteistä ei tehdä erillisiä tuotoksia.

> **Lopuksi pohdittavaksi:** Mikä valitsemassasi tuotoksessa näyttää onnistumiselta ensi silmäyksellä mutta voi tarkemmassa tarkistuksessa osoittautua virheeksi?

---

## Lähteet ja tarkistuspäivä

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [W3C Web Accessibility Initiative](https://www.w3.org/WAI/)
- [OWASP: AI Security and Privacy Guide](https://owasp.org/www-project-ai-security-and-privacy-guide/)

Tarkistettu 20.7.2026.
