# Agentin muisti ja konteksti — miten kone pysyy kartalla?

## Johdanto

Kun rakennat omaa agenttia n8n:llä, yksi suurimmista eroista aiempiin oppitunteihin verrattuna on tämä: agentti ei unohda kaikkea heti. Se voi muistaa, mitä tapahtui viime viikolla. Se tietää, missä vaiheessa prosessi on. Se näkee asiakkaan historian ja osaa käyttää sitä uuden ongelman ratkaisemisessa. Tämä **muisti** ja **konteksti** ovat agentin toiminnan kannalta keskeisiä. Ilman niitä agentti olisi helposti toistava, epäjohdonmukainen ja lähes käyttökelvoton.

Yksinkertaisissa boteissa muisti päättyy usein siihen, kun keskustelu loppuu. Agentissa muisti voi kuitenkin jatkua keskustelujen välillä. Tässä oppitunnissa opit, **miten agentti näkee nykyisen tilanteen konteksti-ikkunan avulla, miten se muistaa menneisyyttä pitkäaikaisen muistin avulla ja miten se seuraa prosessin vaiheita tilan avulla**. Nämä kolme tekijää tekevät agentista näennäisesti älykkään. Kun rakennat agenttia n8n:llä, ne ovat myös niitä rakennuspalikoita, joista agentin logiikka syntyy.

## Konteksti-ikkuna: mitä agentti näkee juuri nyt?

Kuvittele asiakaspalveluagenttia, joka vastaa asiakkaalle neljänkymmenen aiemman viestin jälkeen kysymykseen: ”Entä mitä ehdotat nyt?” Agentti lukee 40 viestiä ja yrittää muistaa, mistä ongelma alun perin alkoi. Se muistuttaa tilannetta, jossa lukisit 40 sivua kirjaa yhdellä kertaa ja sinulta kysyttäisiin sen jälkeen jotain ensimmäiseltä sivulta. Ihmisen keskittyminen kuormittuu. Samalla tavalla myös agentin käsittelykyky on rajallinen.

**Konteksti-ikkuna** tarkoittaa sitä osaa keskustelusta tai datasta, jonka agentti näkee kerralla. Voit ajatella sitä muistilaatikkona, johon mahtuu vain rajattu määrä viimeisimpiä viestejä. Jos ikkuna sisältää 50 viestiä ja keskusteluun tulee 51. viesti, vanhin viesti voi poistua agentin näkyvistä. Tämä rajaaminen on **tarkoituksellista suunnittelua**, ei pelkkä puute. Kaikilla järjestelmillä on rajat prosessointikyvyssä, nopeudessa ja kustannuksissa.

Käytännössä konteksti-ikkunan koko on kompromissi. Mitä suurempi ikkuna on, sitä enemmän agentti näkee aiempaa keskustelua ja sitä paremmin se voi ymmärtää tilanteen. Suurempi ikkuna tarkoittaa kuitenkin myös **enemmän käsiteltävää dataa**, mikä tekee agentista hitaamman ja kalliimman. Jokainen sana, jonka agentti käsittelee, voi maksaa rahaa, jos käytössä on kaupallinen kielimallipalvelu, kuten OpenAI:n API.

> **Pysähdy hetkeksi:** Kuvittele asiakaspalveluagentti, joka käsittelee pitkää tukiprosessia. Asiakas kuvailee ongelmaa pitkään ja kysyy 30 viestin jälkeen: ”Nyt kun olet kuullut kaiken, mitä ehdotat?” Jos konteksti-ikkuna sisältää vain 20 viestiä, agentti näkee enää viimeiset 20 viestiä. Alkuperäinen ongelma on poissa näkyvistä. Mitä tästä voi seurata?

Ammattilaisena sinun täytyy ymmärtää konteksti-ikkunan merkitys omissa agenteissasi. Neuvonta-agentissa, joka käsittelee pitkiä keskusteluketjuja, saatat tarvita 100–200 viestin ikkunan, jotta riittävä historia säilyy mukana. Transaktioagentissa, joka ratkaisee nopeita kysymyksiä, kuten ”Mikä on hinta?”, 20–30 viestiä voi riittää. Järkevä valinta riippuu siitä, **mitä agentin täytyy muistaa tehtävän ratkaisemiseksi**.

<figure class="ai-demo"><span class="ai-demo__tag">// agentti hakee kulloinkin tarvitsemansa</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;gap:24px;padding:16px 22px">
  <div class="l21-store"><div class="l21-h">PITKÄKESTOINEN MUISTI</div>
    <div class="l21-grid"><span>tilaus #12</span><span class="l21-r1">asiakkaan toive</span><span class="l21-r2">hinnasto</span><span>aiempi chat</span><span>ohje</span><span>palaute</span></div></div>
  <div class="l21-arr">haku →</div>
  <div class="l21-work"><div class="l21-h">TYÖMUISTI</div>
    <div class="l21-slots"><span class="l21-old">nykyinen tehtävä</span><span class="l21-in"><span class="l21-i1">asiakkaan toive</span><span class="l21-i2">hinnasto</span></span></div>
    <div class="l21-cap">rajallinen tila</div></div>
</div>
<figcaption class="ai-demo__cap">Agentin työmuisti on pieni eikä pidä kaikkea mielessä. Se hakee pitkäkestoisesta muistista kulloinkin sen tiedon, jota tehtävä juuri nyt vaatii — eri vaiheessa eri palasen.</figcaption></figure>
<style>
.l21-store,.l21-work{border:1.5px solid #3A4560;border-radius:9px;background:#11182A;padding:12px}
.l21-h{font-family:var(--font-mono);font-size:11px;letter-spacing:.08em;color:#B9C2DA;margin-bottom:9px}
.l21-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:6px;width:212px}
.l21-grid span{font-family:var(--font-mono);font-size:11px;color:#B9C2DA;background:#1E2740;border:1.5px solid #3A4560;border-radius:6px;padding:6px;text-align:center}
.l21-r1{animation:l21r1 10s ease-out infinite}
.l21-r2{animation:l21r2 10s ease-out infinite}
@keyframes l21r1{0%,6%{color:#B9C2DA;border-color:#3A4560}16%,46%{color:#FFFFFF;border-color:oklch(0.66 0.15 264);background:#1b2a4d}56%,100%{color:#B9C2DA;border-color:#3A4560}}
@keyframes l21r2{0%,52%{color:#B9C2DA;border-color:#3A4560}62%,92%{color:#FFFFFF;border-color:oklch(0.66 0.15 305);background:#241b4d}100%{color:#B9C2DA}}
.l21-arr{font-family:var(--font-mono);font-size:12px;color:oklch(0.66 0.15 264);animation:l21arr 10s ease-out infinite}
@keyframes l21arr{0%,8%{opacity:.25}20%,44%{opacity:1}50%{opacity:.25}62%,90%{opacity:1}100%{opacity:.25}}
.l21-slots{display:flex;flex-direction:column;gap:6px;width:130px}
.l21-slots>span{font-family:var(--font-mono);font-size:11px;border-radius:6px;padding:7px;text-align:center}
.l21-old{color:#EAEEF8;background:#1E2740;border:1.5px solid #3A4560}
.l21-in{position:relative;height:30px;border-radius:6px}
.l21-i1,.l21-i2{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:6px;color:#0B0F1A;opacity:0}
.l21-i1{background:oklch(0.66 0.15 264);animation:l21i1 10s ease-out infinite}
.l21-i2{background:oklch(0.66 0.15 305);animation:l21i2 10s ease-out infinite}
@keyframes l21i1{0%,16%{opacity:0;transform:translateX(-10px)}24%,46%{opacity:1;transform:translateX(0)}52%,100%{opacity:0}}
@keyframes l21i2{0%,58%{opacity:0;transform:translateX(-10px)}66%,92%{opacity:1;transform:translateX(0)}100%{opacity:0}}
.l21-cap{font-family:var(--font-mono);font-size:11px;color:#B9C2DA;margin-top:8px;text-align:center}
@media (prefers-reduced-motion:reduce){.l21-r1,.l21-r2,.l21-arr,.l21-i1,.l21-i2{animation:none}.l21-r1{color:#FFFFFF;border-color:oklch(0.66 0.15 264)}.l21-i1{opacity:1}}
</style>


## Pitkäaikainen muisti: vektoritietokanta merkityksen etsijänä

Konteksti-ikkuna kertoo agentille, mitä tapahtuu **nyt**. Mutta entä jos asiakkaan kanssa on työskennelty kuusi kuukautta? Entä jos hän palaa uuden ongelman kanssa ja haluat, että agentti muistaa, mitä viimeksi opittiin?

Tätä varten agentilla voi olla **pitkäaikainen muisti**, joka tallennetaan esimerkiksi **vektoritietokantaan**. Vektoritietokanta on erikoistunut tietokanta, joka etsii samankaltaisuuksia merkityksen, ei vain täsmällisten sanojen perusteella. Tämä ero on tärkeä.

Tavallisessa tietokannassa haetaan usein täsmällisillä termeillä. Sana ”muistikortti” löytyy varmasti, jos hakusanana on ”muistikortti”. Vektoritietokannassa tieto tallennetaan kuitenkin merkityksen perusteella. Kun asiakas sanoo: ”Minulla oli ongelma muistilaitteen kanssa viime kuussa”, lause voidaan muuntaa **matemaattiseksi esitykseksi** eli vektoriksi. Tämä vektori kuvaa lauseen merkitystä: kyse on muistista, laitteesta, ongelmasta ja menneestä ajankohdasta.

Myöhemmin sama asiakas voi sanoa: ”Se muistiin liittyvä juttu oli vaikea.” Vaikka sanat ovat eri, lauseen merkitys voi olla samankaltainen kuin aiemmassa tapauksessa. Vektoritietokanta voi löytää tämän samankaltaisuuden ja auttaa agenttia päättelemään, että kyse voi olla samasta tai samantyyppisestä ongelmasta.

Tämä merkitysperusteinen haku on vektoritietokannan vahvuus. Se ei vaadi täsmällistä sanavastaavuutta, vaan se auttaa löytämään olennaista tietoa myös silloin, kun asiakas muotoilee asian eri tavalla kuin aiemmin.

Käytännössä tämä tarkoittaa, että kun agentti näkee asiakkaan nimen tai tunnisteen, se voi hakea vektoritietokannasta asiakkaaseen liittyvää aiempaa tietoa. Agentti ei välttämättä tarvitse kaikkia yksityiskohtia, vaan usein tiivistelmä riittää: ”Tämä asiakas on ostanut meiltä viisi kertaa. Hänellä on ollut aiemmin ongelmia toimituksissa. Viime kuussa ostettu tuote oli samaa sarjaa kuin nyt kysytty tuote.” Nämä tiedot auttavat agenttia ymmärtämään asiakkaan tilanteen ja tekemään parempia päätöksiä.

Vektoritietokanta toimii näin:

Voit ajatella vektoritietokantaa kirjaston hakujärjestelmänä. Kun haet kirjastosta aihetta ”koiran koulutus”, hyvä hakujärjestelmä ei etsi vain kirjoja, joissa lukee täsmälleen ”koiran koulutus”. Se voi löytää myös kirjoja, joiden nimi on esimerkiksi ”Pentujen kasvatus” tai ”Lemmikkien kouluttaminen”, koska ne käsittelevät samaa aihetta eri sanoin. Vektoritietokanta toimii samalla periaatteella: se etsii **merkityksiä**, ei pelkkiä sanoja.

> **Pysähdy hetkeksi:** Ajattele yrityssopimusta, jonka asiakas allekirjoitti kolme kuukautta sitten. Sopimuksessa oli erityisiä ehtoja ja myöhempi maksu. Kun asiakas ottaa nyt yhteyttä, agentti hakee sopimuksen vektoritietokannasta ja huomaa: ”Tämän asiakkaan sopimuksessa on erityisehtoja.” Mitä agentti voi tehdä toisin kuin tavallisten asiakkaiden kohdalla?

## Tila: prosessin vaihe ja muuttujat

Konteksti-ikkuna kertoo, mitä tapahtuu *nyt*. Pitkäaikainen muisti kertoo, mitä on tapahtunut *aiemmin*. Mutta mistä agentti tietää, *missä vaiheessa* prosessia ollaan? Tätä varten tarvitaan **tila** eli state.

Kuvittele tilauksen käsittelyä. Kun asiakas tekee tilauksen, tila on ”tilaus luotu”. Kun agentti lähettää vahvistuksen, tila muuttuu muotoon ”vahvistus lähetetty”. Kun varasto pakkaa tuotteen, tila muuttuu muotoon ”pakattavana”. Kun kuljetus lähtee, tila on ”lähetetty”. Kun asiakas vastaanottaa tuotteen, tila on ”toimitettu”. Jokainen vaihe on eri tila, ja agentti seuraa, missä vaiheessa prosessi on.

Tila sisältää myös **muuttujia** eli prosessin aikana tarvittavia tietoja. Esimerkiksi:

- **Yritykset: 2/3** — kaksi yritystä on käytetty, yksi on jäljellä.
- **Viimeinen hinta: 45 €** — tämä hinta tarjottiin asiakkaalle viimeksi.
- **Ihmisen hyväksyntä: saatu** — vastuuhenkilö on hyväksynyt alennuksen.
- **Virheet: 0** — prosessin aikana ei ole havaittu virheitä.

Ilman tilamuuttujia agentin toiminta menisi helposti sekaisin. Se ei tietäisi, missä vaiheessa tehtävä on tai mitä se oli tekemässä. Se voisi lähettää vahvistussähköpostin kahteen kertaan, koska se ei muistaisi lähettäneensä sitä jo aiemmin. Se voisi yrittää veloittaa asiakasta uudelleen, koska se ei tietäisi, että maksu on jo suoritettu.

Kun rakennat agenttia n8n:llä, **tilan hallinta on kriittistä**. Sinun täytyy suunnitella, mitä mahdollisia tiloja prosessilla voi olla ja mitä muuttujia kussakin tilassa tarvitaan. Nämä tilat ja muuttujat ohjaavat agentin seuraavaa vaihetta. Esimerkiksi jos tila on ”maksu maksettu” ja muuttuja ”varastosaatavuus” on ”ei saatavilla”, agentin seuraava askel voi olla ilmoittaa asiakkaalle arvioitu toimitusaika.

## Käytännön esimerkki: asiakaspalveluagentti kokonaisuutena

Laitetaan nyt nämä kolme komponenttia yhteen. Kuvittele asiakaspalveluagentti, joka käsittelee asiakkaita reaaliajassa.

**Konteksti-ikkuna** näyttää viimeisimmät kymmenen viestiä, jotka asiakkaan kanssa on vaihdettu. Asiakas on voinut kuvailla ongelmaa pitkään, mutta agentti näkee vain viimeisimmät 10 viestiä. Niiden perusteella agentti ymmärtää esimerkiksi tämän: ”Asiakas kokeili ratkaisua A. Se ei auttanut. Nyt hän kysyy, mitä tehdä seuraavaksi.”

**Pitkäaikainen muisti** paljastaa, että tämä asiakas on ollut asiakkaana kolme vuotta, hänellä on samankaltainen ongelma noin kolmen kuukauden välein ja edellisellä kerralla ratkaisu B auttoi. Vektoritietokanta löytää tämän yhteyden, koska se tunnistaa samankaltaisuuden nykyisen ja aiemman ongelman välillä.

**Tila** kertoo, että kyseessä on toinen ratkaisuyritys kolmesta, asiakas on aktiivinen eikä ihmisen tekemää eskalointia ole vielä pyydetty. Nämä muuttujat ohjaavat agentin seuraavaa päätöstä.

Agentti yhdistää nämä kolme tekijää: se näkee nykyisen tilanteen konteksti-ikkunan kautta, tietää pitkäaikaisen muistin avulla, mikä on aiemmin auttanut, ja ymmärtää tilan perusteella, missä vaiheessa prosessi on. Näiden perusteella se voi päätellä: ”Kokeillaan ratkaisua B, koska se auttoi aiemmin. Jos se ei auta, siirrän asian ihmiselle.” Tällainen päätös on mahdollinen vain siksi, että agentilla on käytössään konteksti, pitkäaikainen muisti ja tila.

> **Pysähdy hetkeksi:** Ajattele omaa työtäsi tai opintojasi. Mitä tietoa pidät mielessä lyhytaikaisesti? Mitä tietoa säilytät pidempään? Miten seuraat, missä vaiheessa olet jossakin prosessissa? Agentin muisti ja tila toimivat samankaltaisella tavalla.

## Soul — agentin pysyvä identiteetti ja arvot

Konteksti-ikkuna, pitkäaikainen muisti ja tila muodostavat agentin **toiminnallisen muistin**. Ne auttavat agenttia tekemään päätöksiä. Lisäksi tarvitaan kuitenkin jotain pysyvämpää: **soul** eli agentin pysyvä identiteetti ja arvot.

Soul on kuin agentin moraalikompassi. Se vastaa kolmeen kysymykseen, jotka agentti pitää mielessään tilanteesta toiseen:

**Ensimmäinen kysymys: Kuka minä pohjimmiltani olen?** Soul määrittää agentin identiteetin. Se ei kerro vain sitä, mitä agentti tekee, vaan myös sen, millainen toimija se on. Esimerkiksi: ”Olen kärsivällinen neuvoja, joka arvostaa asiakkaan aikaa ja yrittää auttaa ensin selkeästi ennen kuin pyytää asiakkaalta lisätietoja.” Tämä identiteetti ei muutu tehtävästä toiseen.

**Toinen kysymys: Mitä arvoja minulla on, ja mitä en koskaan tee?** Soul sisältää ehdottomat rajat. Esimerkiksi: ”En koskaan palauta asiakkaan salasanaa, vaan kerron, miten hän voi nollata sen itse.” ”En koskaan jaa yhden asiakkaan tietoja toiselle asiakkaalle.” ”Jos minulla ei ole vastausta, kerron sen suoraan enkä arvaa.” Nämä ovat agentin pysyviä arvoja. Ne ohjaavat toimintaa erityisesti silloin, kun tilanne on epäselvä eikä yksittäinen sääntö riitä.

**Kolmas kysymys: Miten päätän epäselvissä tilanteissa?** Soul antaa agentille perustan päätöksentekoon. Esimerkiksi: ”Jos olen epävarma, suosin asiakkaan turvallisuutta.” ”Jos asiakkaan pyyntö on ristiriidassa turvasääntöjen kanssa, turvasäännöt voittavat.” ”Jos minulla ei ole tarpeeksi tietoa, pyydän apua ennen kuin toimin.”

Käytännössä soul voidaan kirjoittaa **erilliseksi dokumentiksi**, johon agentti viittaa päätöksissään. Se toimii agentin sisäisenä ohjeena, jonka periaatteet näkyvät kaikissa tilanteissa: asiakkaiden kanssa, kollegoiden kanssa ja myös kriisitilanteissa.

## Muistin turvallisuus ja hallinta

Kun agentti muistaa paljon, täytyy puhua myös turvallisuudesta. Pitkäaikainen muisti voi sisältää arkaluontoisia tietoja, kuten asiakkaiden henkilötietoja, maksutietoja tai liikesalaisuuksia.

Ammattilaisena sinun täytyy asettaa selkeät rajat sille, **mitä agentti saa muistaa ja mitä se ei saa muistaa**. Asiakkaan nimi ja ostohistoria voivat olla perusteltuja tietoja, jos niitä käsitellään turvallisesti ja lain mukaisesti. Luottokortin neljä viimeistä numeroa voidaan joissain tilanteissa tallentaa tunnistamista varten, jos tieto on suojattu asianmukaisesti. Asiakkaan salasanaa ei kuitenkaan pidä koskaan tallentaa agentin muistiin. Myös terveystiedot ja muut erityisen arkaluontoiset tiedot vaativat erityistä varovaisuutta ja lainmukaisen käsittelyperusteen.

Muistin hallinta vaatii myös **säännöllistä puhdistamista**. Vanhentuneet tiedot kannattaa poistaa. Jos asiakas poistaa tilinsä, myös häneen liittyvä historia pitäisi poistaa pitkäaikaisesta muistista silloin, kun se on sääntöjen ja lainsäädännön mukaan tarpeen. Tämä on sekä turvallisuus- että yksityisyyskysymys.

## Kohti omaa projektia

Nyt kun ymmärrät muistin kolme tasoa ja soulin käsitteen, mieti omaa agenttiprojektiasi. Mitä tietoa agenttisi tarvitsee yksittäisen keskustelun aikana? Mitä sen täytyy muistaa keskustelujen välillä? Mitä tiloja prosessillasi on? Nämä päätökset muodostavat **Agentti: Muisti** -pohjapiirroksen, jonka kirjoitat opiskelutehtävissä.

## Yhteenveto

Agentti hahmottaa nykyhetkeä **konteksti-ikkunan** avulla. Konteksti-ikkuna voi sisältää esimerkiksi 20–200 viimeistä viestiä sen mukaan, millaista tehtävää agentti hoitaa. Agentilla voi olla myös **pitkäaikainen muisti**, joka tallentuu esimerkiksi vektoritietokantaan ja auttaa löytämään samankaltaisia merkityksiä, ei vain täsmällisiä sanoja. Lisäksi agentilla on **tila**, joka kertoo, missä vaiheessa prosessi on ja mitä muuttujia siihen liittyy.

Nämä kolme tekijää antavat agentille kyvyn toimia johdonmukaisesti: se näkee nykyisen tilanteen, muistaa aiempia asioita ja ymmärtää prosessin vaiheen. Lisäksi agentilla voi olla **soul** eli pysyvä identiteetti ja arvot, jotka ohjaavat sen toimintaa kaikissa tilanteissa. Kun rakennat agenttia n8n:llä seuraavilla oppitunneilla, konteksti, pitkäaikainen muisti, tila ja soul auttavat sinua suunnittelemaan agentista johdonmukaisemman, turvallisemman ja luotettavamman.

---
