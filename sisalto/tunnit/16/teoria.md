# Erikoistuneet tekoälytyökalut — kuva, ääni, video ja koodi

## Johdanto: eri tuotokset, sama työskentelytaito

Tekstiä tuottava chat on vain yksi tapa käyttää generatiivista tekoälyä. Erikoistunut työkalu voi tuottaa kuvan, ääntä, videota tai koodia. Välineet ja tuotokset eroavat, mutta vastuullinen työskentely etenee samalla tavalla:

1. määritä todellinen käyttötarve
2. päätä onnistumisen kriteerit
3. tee ensimmäinen versio
4. nimeä yksi havaittava puute
5. muuta yhtä asiaa
6. vertaa toista versiota ensimmäiseen
7. tee oikeuksiin, turvallisuuteen ja laatuun perustuva julkaisu- tai käyttöpäätös.

Järjestys on olennainen: kriteerit päätetään ennen ensimmäistä versiota, jotta niitä ei madalleta jälkikäteen sopimaan syntyneeseen tuotokseen.

Tällä tunnilla valitset yhden neljästä reitistä. Kaikkien ei tarvitse tehdä kuvaa, eikä yhden kategorian työkalu ole toista kehittyneempi. Ydintaito on osata ohjata, arvioida ja dokumentoida valitsemasi tuotantoprosessi.

Tunnin läpi kulkee yksi esimerkki. Kirjasto tarvitsee verkkosivulleen 20 sekunnin äänettömän opastusvideon, joka näyttää kirjan palauttamisen kolmessa vaiheessa. Ennen videon tekemistä sovitaan, että vaiheiden pitää näkyä oikeassa järjestyksessä, tekstitykset pitää ehtiä lukea rauhassa, esineiden ja tilan pitää säilyä johdonmukaisina eikä kuvassa saa olla tunnistettavia asiakkaita. Nämä kriteerit eivät muutu sen mukaan, millainen ensimmäisestä versiosta tulee.

<figure class="ai-demo"><span class="ai-demo__tag">// väline vaihtuu — sykli ei: tavoite → versio → arvio → yksi muutos</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:322px">
  <div class="l16-wrap" role="img" aria-label="Sama arviointisykli toistuu kolmella eri välineellä. Kuva: kohde hukkui taustaan, joten sommittelu tarkennettiin. Ääni: puhe peittyi musiikkiin, joten voimakkuussuhde muutettiin. Koodi: tyhjä syöte kaatoi ohjelman, joten virhetesti lisättiin. Joka kierroksella tehdään täsmälleen yksi muutos, ja laboratorioloki kerää havainnon ja muutoksen — väline vaihtuu, sykli ei.">
    <span class="l16-md md1">KUVA</span><span class="l16-md md2">ÄÄNI</span><span class="l16-md md3">VIDEO</span><span class="l16-md md4">KOODI</span>
    <div class="l16-cy"><i class="l16-ph">SYKLI</i>
      <span class="l16-st s1">TAVOITE</span><i class="l16-ar aa1">→</i><span class="l16-st s2">VERSIO 1</span><i class="l16-ar aa2">→</i><span class="l16-st s3">ARVIO</span><i class="l16-ar aa3">→</i><span class="l16-st s4">1 MUUTOS</span><i class="l16-ar aa4">→</i><span class="l16-st s5">VERSIO 2</span>
      <i class="l16-tok"></i>
      <span class="l16-sl slh"><b class="v1">kohde hukkui taustaan</b><b class="v2">puhe peittyi musiikkiin</b><b class="v3">tyhjä syöte kaataa ohjelman</b></span>
      <span class="l16-sl slm"><b class="v1">sommittelu tarkennettu</b><b class="v2">voimakkuussuhde muutettu</b><b class="v3">virhetesti lisätty</b></span>
      <span class="l16-dl">Δ muutoksia: 1</span></div>
    <div class="l16-lg"><i class="l16-ph">LABORATORIOLOKI</i>
      <span class="l16-hr"><b>väline</b><b>havainto</b><b>yksi muutos</b></span>
      <span class="l16-row r1"><b class="tg t1">KUVA</b><b>kohde hukkui taustaan</b><b>sommittelu tarkennettu</b></span>
      <span class="l16-row r2"><b class="tg t2">ÄÄNI</b><b>puhe peittyi musiikkiin</b><b>voimakkuussuhde muutettu</b></span>
      <span class="l16-row r3"><b class="tg t3">KOODI</b><b>tyhjä syöte kaataa ohjelman</b><b>virhetesti lisätty</b></span></div>
    <span class="l16-ft">Väline vaihtuu — sykli ei</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Erikoistuneet työkalut eroavat tuotoksissa, mutta työtapa on sama: tavoite, versio, arvio, täsmälleen yksi nimetty muutos ja uusi versio. Tärkein tuotos on loki, johon havainto ja muutos kirjataan joka kierrokselta. Vie hiiri kuvan päälle pysäyttääksesi.</figcaption></figure>
<style>
.l16-wrap{position:relative;width:560px;height:306px;font-family:var(--font-mono);animation:l16w 21s infinite}
.l16-wrap:hover,.l16-wrap:hover *{animation-play-state:paused}
.l16-ph{display:block;font-style:normal;font-size:10.5px;font-weight:700;letter-spacing:.08em;color:#EAEEF8}
.l16-md{position:absolute;top:0;width:92px;height:24px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;font-size:10.5px;font-weight:700;color:#B9C2DA;border:1px solid #2B3552;border-radius:999px;background:#0E1524;opacity:.45}
.l16-md.md1{left:78px;animation:l16md1 21s infinite}
.l16-md.md2{left:180px;animation:l16md2 21s infinite}
.l16-md.md3{left:282px}
.l16-md.md4{left:384px;animation:l16md3 21s infinite}
.l16-cy{position:absolute;left:0;top:36px;width:560px;height:118px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:8px 10px}
.l16-st{position:absolute;top:32px;width:92px;height:30px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;color:#EAEEF8;border:1px solid #4A5677;border-radius:8px;background:#0E1524}
.l16-st.s1{left:12px}.l16-st.s2{left:120px}.l16-st.s3{left:228px}.l16-st.s4{left:336px}.l16-st.s5{left:444px}
.l16-ar{position:absolute;top:38px;font-style:normal;font-size:12px;color:#7E88A8}
.l16-ar.aa1{left:106px}
.l16-ar.aa2{left:214px}
.l16-ar.aa3{left:322px}
.l16-ar.aa4{left:430px}
.l16-tok{position:absolute;left:52px;top:16px;width:12px;height:12px;border-radius:50%;background:#46C7CF;opacity:0;animation:l16tok 21s infinite}
.l16-sl{position:absolute;top:68px;height:30px}
.l16-sl.slh{left:196px;width:156px}
.l16-sl.slm{left:326px;width:130px;text-align:right}
.l16-sl b{position:absolute;left:0;top:0;width:100%;font-size:9.5px;line-height:1.25;font-weight:400;color:#B9C2DA;opacity:0}
.l16-sl.slh b{color:#FFD79A}
.l16-sl.slm b{color:#7FD0A8}
.l16-sl .v1{animation:l16v1 21s infinite}
.l16-sl .v2{animation:l16v2 21s infinite}
.l16-sl .v3{animation:l16v3 21s infinite}
.l16-dl{position:absolute;right:10px;top:8px;font-size:10px;font-weight:700;color:#C9B7F1;border:1px solid #C9B7F1;border-radius:999px;padding:2px 8px;opacity:0;animation:l16dl 21s infinite}
.l16-lg{position:absolute;left:0;top:166px;width:560px;height:112px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:8px 12px}
.l16-hr,.l16-row{display:flex;gap:10px;margin-top:6px;font-size:9.5px;line-height:1.3}
.l16-hr b,.l16-row b{font-weight:400}
.l16-hr b:nth-child(1),.l16-row b:nth-child(1){width:56px;flex:none}
.l16-hr b:nth-child(2),.l16-row b:nth-child(2){width:230px;flex:none}
.l16-hr b{color:#7E88A8;letter-spacing:.06em}
.l16-row{color:#EAEEF8;opacity:0}
.l16-row .tg{font-weight:700}
.l16-row .tg.t1{color:#46C7CF}.l16-row .tg.t2{color:#FFD79A}.l16-row .tg.t3{color:#7FD0A8}
.l16-row.r1{animation:l16r1 21s infinite}
.l16-row.r2{animation:l16r2 21s infinite}
.l16-row.r3{animation:l16r3 21s infinite}
.l16-ft{position:absolute;left:0;top:288px;width:560px;text-align:center;font-size:12px;font-weight:600;color:#FFD79A}
@keyframes l16w{0%{opacity:0}3%{opacity:1}97.5%{opacity:1}100%{opacity:0}}
@keyframes l16md1{0%{opacity:.45}1.5%{opacity:1}31%{opacity:1}33.3%,100%{opacity:.45}}
@keyframes l16md2{0%,33.3%{opacity:.45}35%{opacity:1}64.5%{opacity:1}66.7%,100%{opacity:.45}}
@keyframes l16md3{0%,66.7%{opacity:.45}68.3%{opacity:1}96%{opacity:1}97.5%,100%{opacity:.45}}
@keyframes l16tok{
  0%,1%{opacity:0;transform:translateX(0);background:#46C7CF}
  2.5%{opacity:1}
  4.5%{transform:translateX(108px)}
  7%{transform:translateX(216px)}
  9.5%{transform:translateX(324px)}
  12%{transform:translateX(432px);background:#46C7CF}
  14.5%{opacity:1}16%{opacity:0;transform:translateX(432px)}
  33.3%{opacity:0;transform:translateX(0);background:#FFD79A}
  34.5%{opacity:1}
  37.8%{transform:translateX(108px)}
  40.3%{transform:translateX(216px)}
  42.8%{transform:translateX(324px)}
  45.3%{transform:translateX(432px);background:#FFD79A}
  47.8%{opacity:1}49.3%{opacity:0;transform:translateX(432px)}
  66.7%{opacity:0;transform:translateX(0);background:#7FD0A8}
  67.9%{opacity:1}
  71.2%{transform:translateX(108px)}
  73.7%{transform:translateX(216px)}
  76.2%{transform:translateX(324px)}
  78.7%{transform:translateX(432px);background:#7FD0A8}
  81.2%{opacity:1}82.7%,100%{opacity:0;transform:translateX(432px)}
}
@keyframes l16v1{0%,7%{opacity:0}9.5%{opacity:1}30%{opacity:1}33.3%,100%{opacity:0}}
@keyframes l16v2{0%,40.3%{opacity:0}42.8%{opacity:1}63.4%{opacity:1}66.7%,100%{opacity:0}}
@keyframes l16v3{0%,73.7%{opacity:0}76.2%,100%{opacity:1}}
@keyframes l16dl{0%,12%{opacity:0;transform:scale(.7)}14%,100%{opacity:1;transform:scale(1)}}
@keyframes l16r1{0%,14%{opacity:0;transform:translateY(6px)}17%,100%{opacity:1;transform:none}}
@keyframes l16r2{0%,47.3%{opacity:0;transform:translateY(6px)}50.3%,100%{opacity:1;transform:none}}
@keyframes l16r3{0%,80.7%{opacity:0;transform:translateY(6px)}83.7%,100%{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){
  .l16-wrap,.l16-wrap *{animation:none!important}
  .l16-wrap,.l16-row,.l16-dl{opacity:1}
  .l16-sl .v3{opacity:1}
  .l16-md.md4{opacity:1}
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

## Yhteenveto

Kuva, ääni, video ja koodi tarvitsevat erilaiset syötteet ja laatukriteerit. Niitä yhdistää sama työskentelytapa: käyttötarve johtaa ennalta päätettyihin kriteereihin, ensimmäisen version puute johtaa yhteen perusteltuun muutokseen ja versioiden vertailu johtaa julkaisu- tai hylkäyspäätökseen.

Tunnin tärkein tuotos ei ole näyttävin kuva, pisin kappale, sulavin video tai suurin koodimäärä. Se on **laboratorioloki**, josta toinen ihminen näkee, miten tuotosta ohjattiin, arvioitiin ja korjattiin.

> **Lopuksi pohdittavaksi:** Mikä valitsemassasi tuotoksessa näyttää onnistumiselta ensi silmäyksellä mutta voi tarkemmassa tarkistuksessa osoittautua virheeksi?

---

## Lähteet ja tarkistuspäivä

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [W3C Web Accessibility Initiative](https://www.w3.org/WAI/)
- [OWASP: AI Security and Privacy Guide](https://owasp.org/www-project-ai-security-and-privacy-guide/)

Tarkistettu 20.7.2026.
