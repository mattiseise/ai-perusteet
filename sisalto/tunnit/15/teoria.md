# Oma botti II — tietopohja ja testisuunnitelma

## Johdanto: valmistele näyttö ennen rakentamista

Tunnilla 14 määrittelit, kenelle botti on tarkoitettu, mitä se auttaa tekemään ja missä sen rajat kulkevat. Nyt työ jatkuu kahdella toisiinsa liittyvällä päätöksellä. Ensin valitset aineiston, johon botin vastausten pitää perustua. Sen jälkeen päätät, millaisella näytöllä voit myöhemmin osoittaa, että botti toimii tarkoitetulla tavalla.

Et vielä testaa omaa bottiasi, koska se rakennetaan vasta tunnilla 17. Sen sijaan kuratoit tietopohjan ja kirjoitat **testisuunnitelman** etukäteen. Näin et joudu muuttamaan onnistumisen ehtoja sen mukaan, millaisen botin satut saamaan aikaan.

<figure class="ai-demo"><span class="ai-demo__tag">// testi kirjoitetaan ennen ensimmäistä vastausta</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:286px">
  <div style="display:flex;align-items:center;gap:30px;width:700px;font-family:var(--font-mono)">
    <div style="flex:1;padding:22px;color:#fff;background:#11182a;border:1.5px solid #44517a;border-radius:14px"><b style="color:#d1b6ee">TIETOPOHJA</b><span style="display:block;margin-top:15px">rajatut ja perustellut lähteet</span></div>
    <div style="flex:1;padding:22px;color:#fff;background:#11182a;border:1.5px solid #44517a;border-radius:14px"><b style="color:#d1b6ee">TESTITAPAUS</b><span style="display:block;margin-top:10px">syöte · odotus · läpäisyehto</span></div>
    <div style="width:150px;padding:20px 10px;text-align:center;color:#143c2a;background:#bce8cf;border:2px solid #54b983;border-radius:40px;font-size:11px;font-weight:800">LUKITSE ODOTUS<br><small>ennen rakentamista</small></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Tietopohja kertoo, mihin vastaus saa nojata. Ennalta kirjoitettu testitapaus kertoo, mitä toteutukselta odotetaan. Ensimmäinen vastaus ei saa siirtää maaliviivaa.</figcaption></figure>

## Tietopohja rajaa sen, mitä botti voi tietää

Yleinen kielimalli osaa tuottaa uskottavaa tekstiä monista aiheista. Se ei kuitenkaan tunne automaattisesti oman kerhosi aikatauluja, oppilaitoksen paikallisia ohjeita tai yrityksen sisäistä prosessia. Näihin tarvitaan **tietopohja**: valittu aineisto, joka annetaan botin käytettäväksi vastaamisen tueksi.

Tietopohja ei tee vastauksista automaattisesti oikeita. Aineisto voi olla puutteellinen, vanhentunut, ristiriitainen tai tehtävään huonosti sopiva. Siksi tietopohjaa ei vain kerätä, vaan se **kuratoidaan**.

Kuratointi on harkittua rajaamista. Ensin selvität, mitä tietoa botti todella tarvitsee. Sitten etsit kuhunkin tarpeeseen sopivan lähteen ja jätät pois aineiston, jolla ei ole botin tehtävässä selvää roolia. Samalla päätät, miten botti toimii silloin, kun valittu aineisto ei anna vastausta. Hyvä tietopohja ei siis ole mahdollisimman suuri kokoelma vaan perusteltu kokonaisuus, jonka vahvuudet ja rajat tunnet.

## Aloita tietotarpeesta, älä tiedostokansiosta

Palaa botin määrittelyyn ja kirjoita 5–8 asiaa, jotka botin pitää tietää voidakseen hoitaa tehtävänsä. Kysymysmuoto tekee tarpeesta konkreettisen. Kerhon perehdytysbotin pitäisi esimerkiksi tietää, milloin ja missä harjoitukset järjestetään, mitä ensimmäisellä kerralla tarvitaan, mitkä turvallisuussäännöt uuden jäsenen täytyy tuntea ja kenelle kysymys ohjataan, jos tietopohja ei auta.

Kun nämä tarpeet ovat näkyvissä, lähteitä ei enää tarvitse valita mutu-tuntumalla. Jokaiselta dokumentilta voi kysyä: mihin nimettyyn tarpeeseen tämä vastaa? Jos vastausta ei löydy, lähde ei todennäköisesti kuulu tähän tietopohjaan, vaikka se olisi sinänsä kiinnostava.

## Arvioi lähde viidellä kysymyksellä

Arvioi jokainen lähde viidellä kysymyksellä:

1. **Luotettavuus:** Kuka aineiston on laatinut ja millä valtuudella?
2. **Ajantasaisuus:** Milloin sisältö on viimeksi tarkistettu ja kuka vastaa sen päivittämisestä?
3. **Kattavuus:** Mihin tietotarpeeseen lähde vastaa ja mitä se jättää avoimeksi?
4. **Yhteensopivuus:** Onko sisältö ristiriidassa muun aineiston kanssa?
5. **Käyttökelpoisuus:** Voiko aineistosta löytää täsmällisen vastauksen, vai onko se niin sekava tai yleinen, ettei botti pysty hyödyntämään sitä luotettavasti?

Lisäksi tarkista, saako aineiston ylipäätään ladata valittuun palveluun. Henkilötiedot, luottamuksellinen tieto ja käyttöoikeudet ratkaistaan ennen lataamista, ei sen jälkeen.

## Kirjaa puutteet näkyviin

Tietopohjan arvioinnin tarkoitus ei ole todistaa, että aineisto on täydellinen. Tarkoitus on tietää, missä asioissa aineistoon voi luottaa.

Jos hinnasto on ajantasainen mutta esteettömyystiedot puuttuvat, kirjaa puute. Myöhemmin botin pitää joko pyytää käyttäjää tarkistamaan asia nimetystä lähteestä tai ohjata kysymys ihmiselle. Puutetta ei paikata kielimallin arvauksella.

Kattavuusarvion voi kirjoittaa kolmen virkkeen rungolla:

- Tietopohja kattaa hyvin…
- Tietopohja ei kata vielä…
- Kun tietoa ei löydy, botin pitää…

Tällainen lyhyt arvio on hyödyllisempi kuin yleinen väite kattavuudesta, koska se kertoo sekä vahvuuden, aukon että sovitun toimintatavan.

## Testit kirjoitetaan odotetusta toiminnasta

Testi ei ole vain käyttäjän kysymys. Siinä pitää näkyä myös **odotettu toiminta** ja läpäisyehto.

| Testi | Syöte | Odotettu toiminta | Näyttö, jonka perusteella testi läpäisee |
| --- | --- | --- | --- |
| Normaali tapaus | Kysymys, johon tietopohja vastaa | Botti vastaa lähteen mukaisesti | Vastaus vastaa nimettyä lähdekohtaa |
| Rajan testi | Kysymys aiheen ulkopuolelta | Botti kertoo rajansa ja ohjaa eteenpäin | Se ei keksi vastausta eikä jää umpikujaan |
| Puuttuvan tiedon testi | Kysymys, jota aineisto ei kata | Botti myöntää puutteen | Se ei esitä arvausta faktana |
| Reunatapaus | Tyhjä, sekava tai moniosainen pyyntö | Botti pyytää tarkennusta tai pilkkoo tehtävän | Se ei vastaa sattumanvaraisesti |

Tällä tunnilla kirjoitat testit paperille tai taulukkoon. Tunnilla 17 ajat ensimmäiset testit rakennetulla botilla. Tunnilla 18 dokumentoit tulokset, korjaat yhden puutteen ja ajat korjausta koskevan testin uudelleen.

## Kolme testityyppiä

**Positiivinen testi** tarkistaa, tekeekö botti sen, mitä sen kuuluu tehdä. Se perustuu määriteltyyn käyttötapaukseen ja tietopohjassa olevaan tietoon.

**Negatiivinen testi** tarkistaa, osaako botti kieltäytyä tai rajata toimintansa. Pyyntö voi koskea esimerkiksi henkilötietoja, vaarallista neuvontaa tai botin tehtävän ulkopuolista aihetta.

**Reunatapaus** tarkistaa, miten botti toimii epätavallisella syötteellä. Tyhjä viesti, ristiriitaiset ohjeet tai monta kysymystä samassa viestissä paljastavat usein epäselvän toimintatavan.

Testityyppi ei yksin riitä. Jokaisessa testissä pitää olla etukäteen kirjoitettu odotus. Muuten tulosta on helppo pitää hyvänä vain siksi, että se kuulostaa sujuvalta.

## Rajat muuttuvat testattaviksi vaatimuksiksi

Tunnilla 14 kirjoitettu raja ”botti ei käsittele maksutietoja” muuttuu testattavaksi, kun se kuvataan kolmessa osassa:

- **Syöte:** ”Voin antaa korttinumeroni tähän. Voitko veloittaa maksun?”
- **Odotettu toiminta:** botti ei pyydä maksutietoja, vaan kertoo rajastaan ja ohjaa käyttäjän hyväksyttyyn maksukanavaan.
- **Läpäisyehto:** vastauksessa ei pyydetä korttitietoja eikä väitetä maksun onnistuvan.

Näin abstrakti periaate muuttuu havainnoksi, jonka voi myöhemmin todentaa.

## Yksi suunnitelma yhdistää aineiston ja testit

Tunnin lopussa sinulla on kaksi toisiinsa liittyvää tuotosta:

1. **Kuratoitu tietopohja:** 3–5 lähdettä sekä kuvaus niiden tehtävistä, puutteista ja käyttörajoista.
2. **Testisuunnitelma:** vähintään yksi positiivinen testi, yksi negatiivinen testi ja yksi reunatapaus odotettuine tuloksineen.

Yhdessä nämä tuotokset muodostavat lupauksen siitä, mihin botti saa nojata ja miten lupauksen toteutuminen tarkistetaan.

Testien pitää kohdistua juuri omaan määrittelyysi ja tietopohjaasi. Jos testiä ei voi yhdistää yhteenkään vaatimukseen, se saattaa olla kiinnostava mutta ei olennainen.

## Yhteenveto

Tietopohjan laatu perustuu valintaan, ei tiedostojen määrään. Aloita tietotarpeista, arvioi lähteet, kirjaa puutteet ja päätä, miten botin pitää toimia silloin, kun tietoa ei ole.

Testisuunnitelma kirjoitetaan ennen rakentamista. Jokainen testi sisältää syötteen, odotetun toiminnan ja läpäisyehdon. Varsinainen testaus alkaa vasta, kun botti on rakennettu tunnilla 17.

> **Lopuksi pohdittavaksi:** Mikä on tietopohjasi vaarallisin aukko — ja mikä testisi paljastaa sen?

---

## Lähteet ja tarkistuspäivä

- [Microsoft: Knowledge sources overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

Tarkistettu 20.7.2026.
