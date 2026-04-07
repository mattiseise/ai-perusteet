# Tekoälytyökalut erikoisaloilla — kuva, musiikki, video ja koodi

## Johdanto

Olet jo tutustunut kielimalleihin ja niiden peruskykyihin. Nyt on aika laajentaa työkaluvalikkoasi — tekoäly ei rajoitu tekstiin. Tällä oppitunnilla tutustumme neljään eri alaan erikoistuneisiin tekoälytyökaluihin: kuvageneraatioon, musiikin tuottamiseen, videon luomiseen ja koodausavustajiin. Jokainen näistä työkaluista tekee jotain erilaista, vaatii erilaisia ohjeita ja ajattelutapoja kuin tavallisen tekoälyn kanssa jutteleminen.

Tutustumme myös tekijänoikeuksiin ja etiikkaan — nämä ovat oikeastaan tärkeitä kysymyksiä, kun alat käyttämään näitä työkaluja.

## Kuvageneraatio: neljä lähestymistapaa

Kuvien luominen AI:lla on nopeasti kehittyvä alue. Eri työkaluilla on erilaiset vahvuudet, hintamallit ja integrointivaihtoehdot. Käytämme neljää päätyökalutyyppiä.

### DALL-E ja GPT-4o: Kuvageneraatio ChatGPT:n kautta

OpenAI on integoinut natiivit kuvangenerointiominaisuudet suoraan ChatGPT:hen ja GPT-4o malliin. **DALL-E 3 on poistumassa käytöstä toukokuussa 2026**, ja sen paikalle tulevat GPT-4o:n sisäänrakennetut kuvangenerointikyky. Näiden ominaisuuksien pääsy käy ChatGPT Plus -tilauksen (20 $/kk) kautta. Suurin vahvuus on **tekstin ymmärtäminen ja tulkinta** — voit kirjoittaa luonnollista kuvausta, ja malli ymmärtää nuansseja hyvin — esimerkiksi "1950-luvun tyyli" tai "impressionistinen maalaus aurinkosesta". Se on myös näistä neljästä turvallisin: integroitu kuvageneraattori hylkää provosoivat tai sopimattoman sisällön pyynnöt automaattisesti.

Huomaa, että erillinen DALL-E 4 -versio ei ole olemassa — kuvangenerointi on integroitu suoraan ChatGPT:hen.

**Käyttötapaus:** Liiketoimintaesitykset, blogi-artikkelien kuvat, konseptin visualisoiminen nopeasti. Kalliimpi yksittäistä kuvaa kohti, mutta sopii hyvin satunnaiseen käyttöön.

**Prompt-tekniikka:** Ole spesifinen väreistä, valaistuksesta ja tyylistä. "Upea sininen aamu, sumu, valokuvallinen tyyli, kaunis valaistus" tuottaa parempia tuloksia kuin "kaunis kuva sinisestä aamusta".

### Midjourney: Ammattilaistyökalu verkkosovelluksessa ja Discordissa

Midjourney on johtava kuvageneraatiotyökalu, joka tunnetaan korkeasta visuaalisesta laadusta ja erityisesti **taidetta muistuttavista kuvista**. Uusin versio on **V8 Alpha** (maaliskuu 2026), joka tuottaa 5x nopeampia tuloksia ja natiiveja 2K HD -kuvia. Midjourneyn vahvuus on epätavallisten, luovan näköisten kuvien tuottaminen. Se on suosittu luoville ammattilaisille, joilla on aikaa kokeilla ja parantaa.

Midjourney toimii sekä Discord-botina että täysin toimivana verkkosovelluksena (ei enää pelkästään Discordia). Jokainen kuvageneraatio maksaa pisteitä (credits), ja paketit myydään kuukausittain. Hinnat ovat: Basic 10 $/kk, Standard 30 $/kk, Pro 48 $/kk ja Mega 96 $/kk.

**Käyttötapaus:** Tuotemerkin kuvat, konsepti-visualisaatiot, digitaalinen taide, pelien konsepti-art. Nopeiden, pienillä budjeilla tehtävien projektien kannalta ei-optimaalinen.

**Prompt-tekniikka:** Käytä vertailuilla ja tarkilla taiteellisilla termeillä. "--ar 16:9 --niji 6" -flagit hallitsevat muotosuhteita ja tyyliä. Midjourney ymmärtää iteraatiota hyvin: voit pyytää "tekemään sen rajumpana" tai "lisää purppuraisia värejä".

### Stable Diffusion: avoin lähdekoodi (edistyneemmille)

Stable Diffusion on avoimen lähdekoodin malli, jonka voit ajaa pilvipalvelussa. Uusin versio on **Stable Diffusion 3.5**. Se on ilmainen tai halvempi kuin Midjourney (maksulliset tasot alkavat noin 7 $/kk). Tämä on hyvä vaihtoehto, jos haluat tutkia kuvageneraatiota, mutta et tarvitse Midjourneyn korkeinta laatua.

Stable Diffusionin vahvuus on se, että se on avoin — voit nähdä koodin ja sen toimintaperiaatteet. Sitä käytetään paljon tutkimuksessa ja kehityksessä. Merkittävä haastaja on **FLUX.2** (julkaistu marraskuussa 2025), joka on tuottanut huomattavaa kilpailua avoimen lähdekoodin kuvageneraatiotilassa.

**Käyttötapaus:** Käytännön projektit, joissa haluat ilmaista tai halvempaa työkalua. Ei välttämätöntä valinta aloittelijalle, mutta hyvä tuntea olemassaolo.

**Prompt-tekniikka:** Samoin kuin muissa — ole tarkka ja spesifinen kuvauksessasi. Lisää yksityiskohtia väreistä, tyylistä ja tunnelmasta.

### Adobe Firefly: kaupallisen käytön turvallisuus

Adobe on integroinut Firefly-mallansa (omalla mallissaan, harjoitettua omalla kuvadatalla) Creative Cloud -sovelluksiin. Se on tarkoitettu ammattilaisille, joilla on selkeät kaupallisen käytön oikeudet ja jotka haluavat lain mukaisen varmuuden.

Firefly:n pääetu on se, että se koulutettiin vain avoimesti lisensoitujen kuvien perusteella, joten siitä ei tule tekijänoikeus-ongelmia (tai ainakin Adoben mukaan ei). Se integroituu saumattomasti Photoshopiin ja Illustratoriin.

**Käyttötapaus:** Mainostoimistot, ammattilaiset muotoilijat, kaupallinen käyttö suurella budjetilla.

## Musiikin luominen: Suno ja Udio

Musiikin tekeminen AI:lla on vielä uudemmilla vesillä kuin kuvageneraatio, mutta se kehittyy nopeasti. Kaksi päätyökalutyyppiä hallitsee nyt markkinoita.

### Suno: tekstistä täysiin biiseihin

Suno (www.suno.ai) on palvelu, jossa annat tekstikuvauksen tai sanoitukset, ja se tuottaa kokonaisen musiikin — *rummut, basso, jousisoittimet, laulu*. Voit määritellä genren ("jazz"), tunnelman ("melankolis") ja vaiheittaa prosessia.

Suno on ilmainen (50 krediittiä päivässä, eli noin 10 kappaletta päivässä) tai maksullinen. Pro-taso maksaa noin 10 $/kk ja sisältää 500 kappaletta kuukaudessa. Suno:lla on myös kumppanuus Warner Music Groupin kanssa. Se on todella vaikuttava: voit luoda äkillisesti kokonaisia kappaleita muutamassa minuutissa. Silti laatu on epätasainen, ja tulokset tarvitsevat usein editointia tai uudelleengeneraatiota.

**Käyttötapaus:** Podcast-introt, taustamusiikki videoon, demot, luovan prosessin kiihdyttäminen. *Ei* ammattilaistuotanto ilman merkittävää jälkitöitä.

**Prompt-tekniikka:** Ole spesifinen genrestä ja tunnelmasta. Kirjoita alkusanoitukset tai edes kokonainen laulu sovellukselle tulkittavaksi. "Upbeat indie pop, kevyt akustinen kitara, vesi-teema" toimii paremmin kuin "iloinen biisi".

### Udio: kilpailija ja vaihtoehto

Udio (www.udio.com) on Sunon kilpailija samalla idealla — tekstistä musiikkiin. Se on vielä nuorempi, mutta sen luomat biisit voivat joissakin tapauksissa olla laadultaan parempia. Molemmilla on käytössä neuroverkot, jotka ovat harjoiteltu laajalla musiikkidatalla.

Udio on myös ilmainen (rajoituksin) tai maksullinen (hintamalli oli vielä kehitteillä kirjoitushetkellä).

**Vertailu:** Suno on kehittyneempi, mutta Udio kehittyy nopeasti. Paras käytäntö:
kokeile molempia ja valitse, mikä sopii projektille.

### Tekijänoikeus ja luovuus

Tässä tulee **merkittävä eettinen kysymys**. Monet musiikintuottajat ovat huolissaan siitä, että nämä mallit koulutettiin miljoonilla tekijänoikeuksilla suojatuilla biiseillä. Kun generoit biisin, onko se sinun? Voitko myydä sitä? Onko siinä oikeasti "sinun" luovuutta?

Palveluntarjoajat (Suno, Udio) väittävät, että voit käyttää generoitua musiikkia kaupallisesti (niiden käyttöoikeuksien riippuen). Mutta jos olet pieni indie-levy-yhtiö tai muusikko, kannattaa olla varovainen: nämä työkalut voivat korvata palkallisen säveltäjän, eikä generoitu musiikki ole sinun omaa luovaa työtäsi.

> **Pysähdy hetkeksi:** Pohdi, pitäisikö generatiivisten musiikkityökalujen koulutusta
> rajoittaa? Entä jos malli oppi laulusta, jonka kirjoitit itse? Kuka omistaa generoitua
> musiikkia?

## Video: tulossa, mutta rajoitukset vielä realistiset

Video on seuraava raja. Kolme työkalutyyppiä ovat nyt käytössä tai tulossa, joissa on erilaisia kykyjä ja rajoituksia.

### Runway Gen-4.5: video tekstistä ja kuvista

Runway (www.runwayml.com) on johtavien videotuotantotyökalujen tarjoaja. Uusin malli on **Gen-4.5**, joka voi luoda videoita tekstikuvauksesta tai olemassa olevan kuvan pohjalta.

Oikeasti vaikuttava: voit sanoa "kamera liikkuu vasemmalta oikealle, auringonlasku, ranta" ja saada sekunnin verran videota. Mutta rajoitukset ovat selkeät. Videot ovat lyhyitä (yleensä alle 10 sekuntia) ja epätarkkoja liikkeissä — ihmisten kasvot saattavat muuttua. Video ei vielä korvaa ammattilaistuotantoa.

Runway on maksullinen: ilmainen taso sisältää 125 krediittiä, Standard-taso maksaa 12 $/kk ja Pro-taso 28 $/kk. Runway on arvostettu 5,3 miljardiksi dollariksi.

### Pika ja muut palvelut

Pika (www.pika.art) on samanlainen videotyökalu, joka toimii hyvin mutta on samassa vaiheessa kehitystä. Myös OpenAI lupaa Soraa (jota ei vielä ole laajasti saatavilla), joka lupaa parempaa laatua ja hallintaa.

### Realistiset käyttötapaukset *nyt*

Video-tekoäly sopii hyvin storyboard-visualisointiin, jossa voit nopeasti visualisoida filmikäsikirjoituksen. Se toimii myös teksti-video-esityksissä, joissa haluat yksinkertaisen liikkeellisen sisällön, kuten selittävät videot. Voit myös käyttää sitä olemassa olevien videoiden täydentämiseen ja efekteihin.

Mitä video-tekoäly ei vielä pysty tekemään: Se ei osaa tehdä pitkiä, johdonmukaisia videoita yli minuutin pituisia. Se ei tuota realistisia ihmisiä johdonmukaisilla kasvoilla. Se ei hallitse monitasoista kerrontaa. Ammattilaistuotannot vaativat merkittävää jälkityötä, jos käytät näitä työkaluja.

> **Pysähdy hetkeksi:** Video kehittyy nopeasti. Mitkä käyttötapaukset voisivat muuttua
> mahdollisiksi seuraavien 12 kuukauden aikana? Entä ammattilaisasema, jos video
> automatisoituu täysin?

## Koodausavustajat: tekoäly auttaa sinua kirjoittamaan ohjetta tietokoneelle

Kun puhutaan "koodausavustajista", monet ajattelevat ohjelmista, jotka vaativat erityisiä taitoja. Mutta ajattele asiaa näin: koodaus on vain ohjeen kirjoittamista tietokoneelle. Tekoäly voi auttaa sinua kirjoittamaan sitä ohjetta samalla tavalla, kuin se auttaa sinua kirjoittamaan mitä tahansa muuta tekstiä.

### Miten koodausavustajat toimivat?

Yksinkertainen esimerkki: Sinun pitää kirjoittaa "ohjelma, joka laskee kaikkien parillisten lukujen summan listassa". Normaalisti sinun pitäisi osata kirjoittaa sitä itse tai opiskella, miten se tehdään. Koodausavustajalla voit sanoa suoraan: "Kirjoita funktio, joka laskee kaikkien parillisten lukujen summan listassa." Tekoäly kirjoittaa sen sinulle.

Tämä ei ole "huijaamista". Se on samaa kuin käyttää laskinta matemaatiikassa — se auttaa sinua tekemään työtä nopeammin, kunhan ymmärrät, mitä se tekee.

### Neljä päätyökalutyyppiä

Eri koodausavustajilla on erilaisia tapoja toimia. Tässä on päätyyppi:

**Yksinkertainen avustaja (GitHub Copilot):** Kun kirjoitat koodia, se ehdottaa seuraavia rivejä automaattisesti. Se on kuin kirjoitusvirhe-korjaimen kaltainen, mutta koodille. Se on hyvä, jos tiedät jo, mitä haluat tehdä, ja tarvitset vain apua yksityiskohtien kanssa. GitHub Copilot on saatavilla ilmaisena (rajoitetuilla ominaisuuksilla), Pro-versiona (10 $/kk) ja Pro+ -versiona (39 $/kk).

**Kokonaisuuden ymmärtävä avustaja (Cursor ja Copilot Workspace):** Nämä ovat kehittyneempiä. Voit sanoa sille: "Muokkaa tämä koodi siihen muotoon, että..." ja se muokkaa isompia osia kerralla. Ne lukevat koko projektin ja ymmärtävät, miten osat liittyvät toisiinsa. **Copilot Workspace** on agenttijärjestelmä, joka kykenee lukemaan ja ymmärtämään koko koodikannan. Nämä ovat kuin mentorit, jotka näkevät koko kuvan.

**Terminaalissa toimiva avustaja (Claude Code):** Jos käytät komentoriviä (se on teksti-pohjainen tapa puhua tietokoneesi kanssa), tämä auttaa siinä. Voit sanoa "lisää tämä ominaisuus sovellukseen" ja se tekee muutokset automaattisesti.

**Selain-pohjainen kokeilu (ChatGPT Code Interpreter):** OpenAI:n ChatGPT:ssä voi kirjoittaa pieniä ohjelmia ja ajaa niitä suoraan selaimessa. Se näyttää tuloksen heti. Kuten pienillä laboratorio-kokeilla oppiaksesi, miten ohjelmointi toimii.

### Mitä koodausavustajat tekevät (ja mitä ne eivät tee)?

Koodausavustajat ovat hyviä siihen, että ne kiihdyttävät tavallista, toistuvaa työtä. Jos pitää kirjoittaa kymmenen samantapaista funktiota, avustaja voi tehdä ne kaikki nopeasti. Jos sinulla on vanha koodi, joka pitää päivittää, avustaja voi auttaa.

Mutta ne eivät osaa ajatella puolestasi. Jos haluat löytää päätehtävän ratkaisun — "miten teen tämän ohjelman?" — sinun pitää silti miettiä sitä itse. Avustaja ei oivalla uusia ideita. Se auttaa sinua tekemään sen, mitä olet päättänyt tehdä.

Tämä on tärkeää ymmärtää: **avustaja on työkalu, ei korvike ajattelulle**.

> **Pysähdy hetkeksi:** Kun näet jonkun käyttävän koodausavustajaa, hän ei välttämättä ole "huijari", joka ei osaa ohjelmoida. Hän käyttää työkalua, aivan kuten sinä käytät laskintataulukko-ohjelmaa. Mitä ajatit ennen kuin luit tämän?

## Tekijänoikeudet ja etiikka: mikä on oikein?

Kun käytät näitä tekoälytyökaluja, on hyvä tietää kolme asiaa: mistä tekoäly oppi, kuka omistaa sen, mitä luot, ja miten se vaikuttaa ihmisiin.

### Mistä nämä mallit opittiin?

Tekoälymallit opitaan miljoonilla esimerkeillä. DALL-E opittiin miljoonilla kuvilla. Musiikki-tekoäly opittiin miljoonilla biiseillä. Nämä esimerkit otettiin Internetista. Nyt on iso ongelma: monet näistä kuvista ja biiseistä omistaa joku toinen. He eivät ole antaneet lupaa käyttää niitä tekoälyn opettamiseen.

Oikeusjuttuja käydään juuri nyt. Muusikoita, taiteilijoita ja valokuvaajia häiritsee se, että heidän työnsä opetti tekoälyä ilman heidän suostumustaansa.

### Mitä sinun pitää tietää käytöstä?

Kun luot kuvaa DALL-E:lla, kenen kuva se on? Sinun? OpenAI:n? Vai sen ihmisen, jonka kuvan kaltainen se on?

Vastaus on: **se on monimutkaista ja riippuu siitä, missä asut ja mitä sääntöjä noudatat**. Jotkut palvelut sanovat, että kuva on sinun. Toiset sanovat, että se on heidän. Paras keino on olla varovainen.

Tässä on konkreettinen esimerkki: Jos luot kuvaa "Mona Lisa, joka juoksee, moderni taide" ja myyt sen postereina, saattaa tulla ongelma. Miksi? Koska Mona Lisa on tunnettu teos, ja sen käyttäminen voi rikkoa oikeuksia. Et voi vain sanoa "tekoäly teki sen".

### Merkintä ja rehellisyys

Jos käytät tekoälyä jotain luomiseen, ole rehellinen siitä. Monet palvelut (kuten Instagram) vaativat "Made with AI" -merkinnän. Paikallisillakaan kilpailuilla voi olla säännöt. Akateemisissa papereissa sinun pitää mainita, jos käytit tekoälyä.

Miksi? Koska ihmiset haluavat tietää, kuinka jotain tehtiin. Se on rehellisyyttä.

### Millainen vaikutus tällä on muihin?

Jotkut ihmiset, kuten muusikot tai kuvataiteilijat, ovat huolissaan. He sanovat: "Jos tekoäly voi tehdä musiikkia, minulla ei ole enää työtä." Se on oikea huoli, mutta vastaus on monimutkaisempi.

Nämä työkalut automatisoivat tavallista, toistuvaa työtä. Ne eivät korvaa sitä, mitä ammattilaiset tekevät parhaaksi — luovaa työtä ja oivallusta. Mutta ne tekevät kilpailusta kovempaa aloittelijoille.

Paras keino on oppia käyttämään näitä työkaluja hyväksi. Ammattilaiset, jotka ymmärtävät tekoälyä, voivat käyttää sitä apunaan.

> **Pysähdy hetkeksi:** Jos olisit kuvataiteilija tai muusikko, mitä ajattelisit näistä työkaluista? Entä jos olet opiskelija ja haluat oppia? Mitkä ovat eri näkökulmat?

## Työkalun valinta: Mikä työkalu mihin?

Kun haluat tehdä jotain tekoälyillä, sinun pitää valita oikea työkalu. Se on kuten kysymys: mitä haluan tehdä ja mikä avusta minua parhaiten?

Tässä on yksinkertainen tapa ajatella. Kuvaa tarvitessa käytä ChatGPT:hen integroitua kuvangeneraattoria (GPT-4o:n kautta), jos haluat nopean ja yksinkertaisen ratkaisun. Midjourney on parempi valinta, jos sinulla on aikaa odottaa ja haluat korkealaatuisia tuloksia.

Musiikkia tarvitessa kokeile Sunoa tai Udiota. Ne tekevät musiikkia teksti-kuvauksesta. Videota tarvitessa Runway tai Pika voivat tehdä lyhyitä videoita tekstikuvauksesta. Muista kuitenkin, että nämä ovat vielä kehitysvaiheessa, eivätkä ammattilaisvalmiita.

Koodia tarvitessa harkitse seuraavasti: Jos olet aloittelija ja haluat apua, ChatGPT Code Interpreter on helppo aloittaa, koska se näyttää tulokset heti. Jos haluat ammattilaismaista apua ja olet tekemässä suurempaa projektia, Claude Code auttaa terminaalissa. Copilot Workspace on loistava valinta, jos haluat agenttijärjestelmää, joka ymmärtää koko koodikannan.

**Käytännön esimerkit:**
- **Blogi-artikkelin kuva:** ChatGPT + GPT-4o (nopea ja kohtuullinen hinta)
- **Podcast-intro-musiikki:** Suno (tekee kokonaisen biisin muutamassa minuutissa)
- **Idea-video storyboards:** Runway Gen-4.5 (visualisoi ideasi nopeasti)
- **Pienessä kooditehtävässä:** ChatGPT Code Interpreter (näet tulokset välittömästi)

## Yhteenveto

Tekoälytyökalut ovat hyviä moniin tehtäviin, mutta ne eivät ole vielä valmiita kaikkeen.

**Kuvageneraatio** toimii hyvin. ChatGPT:n sisäänrakennettu kuvangenerointi (GPT-4o:n kautta) on nopea ja helppo. Midjourney tekee kauniimpia kuvia, mutta kestää kauemmin. Voit käyttää näitä oikeasti omissa projekteissasi.

**Musiikki ja video** kehittyvät, mutta niillä on vielä rajansa. Voit tehdä lyhyitä, yksinkertaisia videoita, mutta pitkiä tai monimutkaisia ei vielä. Musiikki toimii paremmin — voit tehdä kokonaisia biisejä, mutta ammattilaiselle ehkä tarvitaan vielä editointia.

**Koodausavustajat** auttavat oikeasti, jos osaat jo ohjelmoida jonkin verran. Jos et osaa, ne voivat opettaa, mutta et pitäisi laskea täysin niiden varaan.

**Tekijänoikeudet ja etiikka** ovat tärkeitä. Muista, että kaikki nämä mallit opittiin todellisten ihmisten töistä. Ole rehellinen siitä, miten käytät näitä työkaluja. Merkitse "Made with AI", jos olet julkaisemassa jotain.

Nyt on aika kokeilla itse näitä työkaluja. Seuraavissa tehtävissä luot todellisia tuotoksia ja näet, miten ne toimivat.

## Tärkeä huomautus: Tietojen ajantasaisuudesta

Tämän materiaalin tiedot vastaavat maaliskuun 2026 tilannetta. Erikoisalojen tekoälytyökalut kehittyvät poikkeuksellisen nopeasti — uusia versioita ja kokonaan uusia työkaluja julkaistaan kuukausittain. Kun luet tätä materiaalia myöhemmin, tarkista aina kunkin työkalun viralliselta verkkosivulta ajankohtaiset hinnat, versiot ja ominaisuudet. Tekoälyn alue muuttuu niin nopeasti, että kuuden kuukauden vanha tieto voi olla jo vanhentunut.
