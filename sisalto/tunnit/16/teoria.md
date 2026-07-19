# Tekoälytyökalut erikoisaloilla

## Valinnainen laboratorio: kuva, musiikki, video tai koodi

## Johdanto

Olet jo tutustunut **kielimalleihin** eli tekoälyihin, joiden kanssa voi keskustella tekstillä. Olet ehkä käyttänyt niitä tekstin kirjoittamiseen, selittämiseen, tiivistämiseen tai ideointiin.

Tekoäly ei kuitenkaan rajoitu tekstiin. Nykyään tekoälyä käytetään myös kuvien, musiikin, videoiden ja koodin tekemiseen. Nämä työkalut toimivat usein samalla perusidealla: käyttäjä antaa ohjeen eli **promptin**, ja tekoäly tuottaa sen perusteella jotakin uutta.

Tämä on valinnainen laboratorio. Valitse yksi tekoälytyökalujen alue, jota kokeilet tai analysoit annetun esimerkkituloksen avulla. Kaikkia neljää ei tarvitse kokeilla:

- **kuvageneraatioon** eli kuvien luomiseen tekoälyllä
- **musiikin luomiseen** tekoälyllä
- **videon luomiseen ja muokkaamiseen** tekoälyllä
- **koodausavustajiin**

Samalla käsittelemme **tekijänoikeuksia** ja **etiikkaa**. Ne eivät ole sivuasioita, vaan olennainen osa tekoälyn käyttöä. Kun tekoäly tuottaa kuvan, musiikkia tai videon, pitää miettiä ainakin kolmea asiaa: mistä tekoäly on oppinut, saako tuotosta käyttää ja onko reilua väittää tekoälyn tekemää työtä kokonaan omaksi.

**Huomio:** Tämän materiaalin tiedot on tarkistettu toukokuussa 2026. Tekoälytyökalut muuttuvat nopeasti, joten yksittäiset nimet, hinnat ja ominaisuudet voivat myöhemmin olla erilaisia.

<figure class="ai-demo"><span class="ai-demo__tag">// sama idea, neljä mediaa — kullakin oma erikoistunut työkalunsa</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:300px">
  <div class="l16-wrap">
    <div class="l16-prompt">”Rauhallinen aamu järvellä, sumua veden päällä.”</div>
    <div class="l16-card c1"><span class="l16-h">KUVA</span><div class="l16-pic"><svg viewBox="0 0 104 62" width="100%" height="62" preserveAspectRatio="none" aria-hidden="true" focusable="false"><defs><linearGradient id="l16sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F7C873"/><stop offset=".55" stop-color="#F0A38C"/><stop offset="1" stop-color="#8E6B9E"/></linearGradient><linearGradient id="l16lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C98E84"/><stop offset="1" stop-color="#3E4C7A"/></linearGradient></defs><rect width="104" height="34" fill="url(#l16sky)"/><circle class="l16-sun" cx="52" cy="26" r="7" fill="#FFE9B8"/><path d="M0 34 L20 24 L38 34 Z" fill="#5A4670"/><path d="M30 34 L52 20 L78 34 Z" fill="#473A5E"/><path d="M70 34 L88 26 L104 34 Z" fill="#5A4670"/><rect y="34" width="104" height="28" fill="url(#l16lake)"/><ellipse class="l16-mist" cx="52" cy="36" rx="46" ry="5" fill="#EAEEF8" opacity=".4"/><ellipse cx="52" cy="42" rx="20" ry="2.4" fill="#FFE9B8" opacity=".5"/></svg></div><span class="l16-t">kuvageneraattori</span></div>
    <div class="l16-card c2"><span class="l16-h">MUSIIKKI</span><div class="l16-eq"><i></i><i></i><i></i><i></i><i></i></div><span class="l16-t">musiikkigeneraattori</span></div>
    <div class="l16-card c3"><span class="l16-h">VIDEO</span><div class="l16-film"><i></i><i></i><i></i><b>▸</b></div><span class="l16-t">videogeneraattori</span></div>
    <div class="l16-card c4"><span class="l16-h">KOODI</span><div class="l16-code"><span class="cl ln1"><b>def</b> aamu():</span><span class="cl ln2">  piirra(<i>"järvi"</i>,</span><span class="cl ln3">  sumu=<b>True</b>)</span></div><span class="l16-t">koodiavustaja</span></div>
    <span class="l16-note">muista: kerro, kun sisältö on tekoälyn tuottamaa</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Generatiivisia työkaluja on eri medioille. Sama sanallinen idea syntyy kuvana, musiikkina, videona tai koodina — periaate on sama (kuvaus sisään, tuotos ulos), mutta työkalu on kullekin medialle oma.</figcaption></figure>
<style>
.l16-wrap{position:relative;width:560px;height:262px;font-family:var(--font-mono)}
.l16-prompt{position:absolute;left:50%;transform:translateX(-50%);top:0;white-space:nowrap;font-size:12px;font-weight:500;color:#06212A;background:#46c7cf;border-radius:10px;padding:8px 13px}
.l16-card{position:absolute;top:62px;width:130px;height:138px;background:#11182A;border:2px solid #2B3552;border-radius:12px;padding:9px 10px;text-align:center}
.l16-card.c1{left:0;animation:l16k1 13s infinite}
.l16-card.c2{left:143px;animation:l16k2 13s infinite}
.l16-card.c3{left:286px;animation:l16k3 13s infinite}
.l16-card.c4{left:429px;animation:l16k4 13s infinite}
@keyframes l16k1{0%,3%{border-color:#2B3552}7%,93%{border-color:oklch(0.66 0.15 305)}97%,100%{border-color:#2B3552}}
@keyframes l16k2{0%,24%{border-color:#2B3552}28%,93%{border-color:oklch(0.66 0.15 305)}97%,100%{border-color:#2B3552}}
@keyframes l16k3{0%,45%{border-color:#2B3552}49%,93%{border-color:oklch(0.66 0.15 305)}97%,100%{border-color:#2B3552}}
@keyframes l16k4{0%,66%{border-color:#2B3552}70%,93%{border-color:oklch(0.66 0.15 305)}97%,100%{border-color:#2B3552}}
.l16-h{display:block;font-size:10.5px;letter-spacing:.12em;color:#B9C2DA;margin-bottom:8px}
.l16-t{position:absolute;left:6px;right:6px;bottom:8px;font-size:9.5px;color:#8B94B3}
.l16-pic{height:62px;border-radius:8px;overflow:hidden;opacity:0;animation:l16pic 13s infinite}
@keyframes l16pic{0%,4%{opacity:0;filter:blur(6px)}10%,95%{opacity:1;filter:blur(0)}100%{opacity:0}}
.l16-sun{animation:l16sun 13s ease-in-out infinite}
@keyframes l16sun{0%,6%{transform:translateY(8px)}16%,95%{transform:translateY(0)}100%{transform:translateY(8px)}}
.l16-mist{animation:l16mist 5s ease-in-out infinite}
@keyframes l16mist{0%,100%{opacity:.42}50%{opacity:.2}}
.l16-eq{display:flex;align-items:flex-end;justify-content:center;gap:5px;height:62px;padding-bottom:4px}
.l16-eq i{width:9px;border-radius:3px 3px 0 0;background:oklch(0.7 0.14 305);height:18%;animation:l16eq 1s ease-in-out infinite}
.l16-eq i:nth-child(1){animation-delay:0s}.l16-eq i:nth-child(2){animation-delay:.18s}.l16-eq i:nth-child(3){animation-delay:.36s}.l16-eq i:nth-child(4){animation-delay:.1s}.l16-eq i:nth-child(5){animation-delay:.27s}
@keyframes l16eq{0%,100%{height:18%}50%{height:88%}}
.l16-film{position:relative;display:flex;gap:4px;align-items:center;height:62px;overflow:hidden;border-radius:8px;background:#0B0F1A;padding:0 5px}
.l16-film i{flex:0 0 34px;height:44px;border-radius:5px;background:#28324F;border:1px solid #44517A;animation:l16film 2.4s linear infinite}
@keyframes l16film{from{transform:translateX(0)}to{transform:translateX(-39px)}}
.l16-film b{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-size:19px;color:#FFFFFF;text-shadow:0 0 8px #000}
.l16-code{display:flex;flex-direction:column;gap:6px;justify-content:center;height:62px;padding:0 4px;text-align:left}
.l16-code .cl{display:block;font-size:9.5px;line-height:1.3;color:#EAEEF8;white-space:nowrap;overflow:hidden;width:0}
.l16-code .cl b{color:#c9b7f1;font-weight:600}
.l16-code .cl i{color:#7FD0A8;font-style:normal}
.l16-code .ln1{animation:l16c1 13s steps(12) infinite}
.l16-code .ln2{animation:l16c2 13s steps(16) infinite}
.l16-code .ln3{animation:l16c3 13s steps(12) infinite}
@keyframes l16c1{0%,68%{width:0}73%,100%{width:100%}}
@keyframes l16c2{0%,73%{width:0}78%,100%{width:100%}}
@keyframes l16c3{0%,78%{width:0}83%,100%{width:100%}}
.l16-note{position:absolute;left:0;right:0;top:218px;text-align:center;font-size:11px;letter-spacing:.04em;color:#F0A38C;opacity:0;animation:l16note 13s infinite}
@keyframes l16note{0%,82%{opacity:0}88%,96%{opacity:1}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l16-card,.l16-pic,.l16-sun,.l16-mist,.l16-eq i,.l16-film i,.l16-code .cl,.l16-note{animation:none}
.l16-card{border-color:oklch(0.66 0.15 305)}
.l16-pic,.l16-note{opacity:1}
.l16-eq i{height:55%}
.l16-code .cl{width:100%}}
</style>

## Kuvageneraatio — tekoälyllä kuvia tekstistä

**Kuvageneraatio** tarkoittaa sitä, että tekoäly luo kuvan käyttäjän tekstikuvauksen perusteella. Voit esimerkiksi kirjoittaa:

> "Luo kuva futuristisesta luokkahuoneesta, jossa opiskelijat käyttävät lisättyä todellisuutta. Tyyli on realistinen, valaistus lämmin ja kuva sopii esityksen kansikuvaksi."

Tekoäly yrittää tehdä kuvan tämän ohjeen perusteella.

Kuvagenerointityökalut ovat kehittyneet nopeasti. Nykyään ne osaavat tehdä valokuvamaisia kuvia, kuvituksia, logoideoita, konseptitaidetta ja myös kuvia, joissa on jonkin verran tekstiä. Tekstin tekeminen kuvaan on silti edelleen asia, jossa kannattaa olla tarkkana: kirjaimet, sanat ja erikoismerkit voivat mennä väärin, vaikka työkalu olisi muuten hyvä.

### ChatGPT:n kuvagenerointi

ChatGPT:ssä on sisäänrakennettu kuvien luonti. OpenAI toi kuvageneroinnin osaksi GPT-4o-mallia vuonna 2025. Ajatuksena on, että kuvan luonti ei ole erillinen lisäosa, vaan osa samaa keskustelevaa tekoälyä. OpenAI kuvaa tätä natiivisti multimodaaliseksi malliksi: sama järjestelmä ymmärtää sekä tekstiä että kuvia ja voi tuottaa kuvia käyttäjän ohjeiden perusteella.

Tämän vahvuus on helppous. Käyttäjän ei tarvitse opetella erillistä työkalua, vaan kuvan voi pyytää samalla tavalla kuin pyytäisi tekstiä tai ideaa. Tämä sopii hyvin aloittelijalle.

Hyviä käyttötapoja ovat esimerkiksi:

- esityksen kuvituskuva
- blogin tai raportin kansikuva
- idean nopea visualisointi
- opetusmateriaalin havainnollistava kuva
- kuvan muokkaaminen ohjeiden perusteella

ChatGPT:n kuvagenerointi sopii erityisesti tilanteisiin, joissa haluat selittää kuvan tavallisella kielellä. Voit myös jatkaa keskustelua kuvan jälkeen: *"tee tästä rauhallisempi"*, *"lisää mukaan tietokoneita"*, *"muuta tyyli sarjakuvamaiseksi"* tai *"tee tästä 16:9-kuva dioihin"*.

Hyvä kuvaprompti ei ole vain "tee hieno kuva". Parempi prompti kertoo, mitä kuvassa näkyy, mikä on tyyli, millainen tunnelma kuvassa on ja mihin kuvaa käytetään.

**Esimerkki hyvästä kuvapromptista:**

"Luo vaakasuuntainen 16:9-kuva esityksen alkuun. Kuvassa on ensimmäisen vuoden opiskelija, joka tutkii tekoälytyökaluja tietokoneella. Tyyli on moderni, selkeä ja hieman futuristinen, mutta ei liian scifi. Väreinä sininen ja violetti. Ei tekstiä kuvaan."

Huomaa lopun ohje "Ei tekstiä kuvaan". Se on usein järkevää, koska tekoälyn luoma teksti kuvassa voi sisältää virheitä.

### Midjourney

**Midjourney** on kuvagenerointityökalu, joka tunnetaan erityisesti näyttävistä ja taiteellisista kuvista. Se toimii nykyään sekä verkkosovelluksen että Discordin kautta. Midjourneyn virallisessa dokumentaatiossa eri maksullisia suunnitelmia vertaillaan GPU-ajan, käyttörajojen ja ominaisuuksien perusteella.

Midjourney sopii hyvin, kun tavoitteena on visuaalisesti vaikuttava kuva. Se on suosittu esimerkiksi konseptitaiteessa, pelimaailmojen ideoinnissa, mainoskuvissa ja tunnelmakuvissa.

Aloittelijalle Midjourney voi tuntua hieman erikoisemmalta kuin ChatGPT:n kuvagenerointi, koska siinä on oma käyttölogiikkansa. Toisaalta se palkitsee kokeilemisen. Sama prompti voi tuottaa useita erilaisia kuvia, joista valitaan paras ja kehitetään sitä eteenpäin.

**Esimerkki Midjourney-tyylisestä promptista:**

"futuristic classroom, students working with AI assistants on laptops, realistic lighting, clean modern design, cinematic composition, 16:9"

Midjourneyssä käytetään usein myös lisäasetuksia, kuten kuvasuhdetta. Esimerkiksi 16:9 sopii esitysdioihin.

### Stable Diffusion ja avoimet kuvamallit

**Stable Diffusion** ei ole vain yksi verkkopalvelu, vaan laajempi joukko avoimempia kuvamalleja ja niitä käyttäviä työkaluja. Stability AI:n virallinen mallikatalogi sisältää esimerkiksi Stable Diffusion XL- ja Turbo-malleja, joita voidaan käyttää eri palveluissa ja ohjelmissa.

Avoimien mallien idea on, että käyttäjällä tai kehittäjällä on enemmän mahdollisuuksia säätää ja rakentaa omia ratkaisuja. Tämä on kiinnostavaa, jos halutaan ymmärtää, miten tekoälytyökalut toimivat teknisesti, tai jos halutaan käyttää malleja omissa sovelluksissa.

Aloittelijalle tämä ei yleensä ole helpoin aloituspaikka. Stable Diffusion -tyyppiset työkalut voivat vaatia enemmän asetusten säätämistä, mallien valintaa ja joskus tehokkaan tietokoneen tai pilvipalvelun käyttöä.

**Hyvä tapa ajatella tätä:**

- ChatGPT:n kuvagenerointi on helppo yleiskäyttöinen työkalu.
- Midjourney on vahva taiteellisessa kuvassa.
- Stable Diffusion -tyyppiset mallit ovat joustavia ja teknisesti kiinnostavia, mutta vaativat enemmän opettelua.

### Adobe Firefly

**Adobe Firefly** on Adoben tekoälykuva- ja sisältömallien perhe. Se on integroitu Adoben ohjelmiin, kuten Photoshopiin, Illustratoriin ja Adobe Expressiin. Adobe käyttää Fireflyssä generatiivisia krediittejä, joiden määrä riippuu käytössä olevasta tilauksesta.

Fireflyn tärkein myyntivaltti on kaupallinen käyttö. Adobe markkinoi Fireflyä työkaluna, joka sopii turvallisemmin yritys- ja mainoskäyttöön kuin monet muut kuvageneraattorit. Tämä liittyy siihen, millaisella aineistolla mallit on koulutettu ja millaisia käyttöehtoja Adobe tarjoaa.

Firefly sopii erityisesti silloin, kun käyttäjä tekee materiaalia yritykselle, mainontaan tai brändikäyttöön. Photoshopissa Fireflyn kaltaisia toimintoja voi käyttää esimerkiksi kuvan laajentamiseen, taustan muuttamiseen tai yksityiskohtien lisäämiseen.

Aloittelijan näkökulmasta Firefly on hyvä esimerkki siitä, että tekoäly ei ole aina erillinen "tekoälysivusto". Se voi olla myös osa tavallista työohjelmaa.

### Hyvä kuvaprompti

Kuvatyökaluille kannattaa antaa selkeä ohje. Hyvässä kuvapromptissa on usein nämä osat:

- mitä kuvassa näkyy
- mihin kuvaa käytetään
- mikä on tyyli
- millainen tunnelma tai valaistus kuvassa on
- mikä on kuvasuhde
- mitä kuvassa ei saa olla

**Heikko prompti:**

"Tee kuva tekoälystä."

**✓ Parempi prompti:**

"Luo vaakasuuntainen 16:9-kuva oppitunnin diaan. Kuvassa on nuori opiskelija, joka käyttää kannettavaa tietokonetta ja tutkii tekoälytyökaluja. Tyyli on selkeä, moderni ja opetusmateriaaliin sopiva. Valaistus on lämmin. Kuvassa ei saa olla tekstiä, logoja tai tunnistettavia henkilöitä."

**Tärkeä käytännön vinkki:** jos kuva tulee diaan, pyydä usein 16:9-kuvasuhdetta. Jos kuva tulee someen, kuvasuhde voi olla esimerkiksi 1:1 tai 9:16.

## Musiikin luominen tekoälyllä

Tekoälyllä voi nykyään luoda myös musiikkia. Käyttäjä voi antaa tekstikuvauksen, sanoitukset tai tyylin, ja palvelu luo kappaleen. Se voi sisältää esimerkiksi laulua, rumpuja, bassoa, kitaraa, syntetisaattoreita ja muuta tuotantoa.

Tämä on monelle opiskelijalle yllättävää. Tekoäly ei siis tee vain tekstiä tai kuvia, vaan se voi tuottaa kokonaiselta kuulostavan kappaleen muutamassa minuutissa.

### Suno

**Suno** on yksi tunnetuimmista tekoälymusiikkipalveluista. Sen virallisen hinnoittelusivun mukaan ilmaisella tasolla voi luoda rajoitetun määrän kappaleita päivässä, ja maksullisilla tasoilla saa enemmän kappaleita, kehittyneempiä malleja ja kaupallisia käyttöoikeuksia. Sunon sivuilla mainitaan esimerkiksi mallit v4.5, v5 ja v5.5 maksullisissa suunnitelmissa.

**Esimerkki Suno-promptista:**

"Energetic pop rock song about learning programming for the first time. Finnish lyrics. Mood is hopeful and confident. Include drums, electric guitar and catchy chorus."

Palvelu voi tämän perusteella tuottaa kappaleen, jossa on sanoitukset, laulu ja tausta.

Suno sopii hyvin esimerkiksi:

- podcastin introon
- videon taustamusiikin ideointiin
- peliprojektin tunnelmamusiikin hahmotteluun
- oman biisi-idean kokeilemiseen
- opetuksessa luovaan kokeiluun

Tärkeää on ymmärtää, että tulos ei aina ole heti valmis. Joskus laulu kuulostaa keinotekoiselta, sanat ovat kömpelöitä tai tyyli ei osu kohdalleen. Tekoälyn kanssa työskennellään usein kokeilemalla: luodaan monta versiota, valitaan paras ja parannetaan sitä.

### Udio

**Udio** on toinen tunnettu tekoälymusiikin palvelu. Se toimii samalla yleisidealla kuin Suno: käyttäjä antaa tekstiohjeen tai musiikillisen suunnan, ja palvelu tuottaa musiikkia. Udiolla on virallinen hinnoittelusivu, jossa palvelu tarjoaa eri tasoja eri käyttötarpeisiin.

Käytännössä Sunoa ja Udiota kannattaa ajatella vaihtoehtoisina työkaluina. Jos toinen ei tuota hyvää tulosta, toinen voi onnistua paremmin. Tekoälymusiikissa erot näkyvät usein laulun luonnollisuudessa, genren ymmärtämisessä ja siinä, miten hyvin kappale pysyy kasassa.

### Hyvä musiikkiprompti

Musiikkipromptissa kannattaa kertoa ainakin seuraavat asiat:

- genre
- tunnelma
- tempo tai energia
- soittimet
- onko mukana laulua
- millä kielellä sanoitukset ovat
- mihin kappaletta käytetään

**Heikko prompti:**

"Tee iloinen biisi."

**✓ Parempi prompti:**

"Tee 30 sekunnin mittainen energinen pop rock -intro opiskelijaprojektin videoon. Tunnelma on innostunut ja positiivinen. Mukana rummut, basso, sähkökitara ja kevyt syntetisaattori. Ei laulua, jotta musiikki ei häiritse puhetta."

**✓ Toinen esimerkki:**

"Tee suomenkielinen kappale ensimmäisestä ohjelmointikurssista. Tyyli on kevyt pop, tempo keskinopea. Kertosäkeen pitää olla tarttuva ja rohkaiseva. Sanoitusten pitää olla yksinkertaisia ja ymmärrettäviä."

### Musiikki, tekijänoikeudet ja reilu käyttö

Tekoälymusiikki on myös kiistanalainen aihe. Monet muusikot ja levy-yhtiöt ovat olleet huolissaan siitä, että tekoälymalleja on koulutettu tekijänoikeudella suojatulla musiikilla ilman lupaa.

Suno ja Udio ovat olleet mukana musiikkialan oikeuskiistoissa. Vuonna 2025 ja 2026 osa suurista levy-yhtiöistä on myös tehnyt lisensointi- ja sovintosopimuksia tekoälymusiikkipalveluiden kanssa, mutta koko kenttä ei ole vielä täysin selvä. Esimerkiksi Warner teki sopimuksen Sunon kanssa, kun taas osa oikeusprosesseista ja vaatimuksista on jatkunut.

Opiskelijan käytännön sääntö on tämä: älä käytä tekoälymusiikkia niin, että väität sitä kokonaan itse säveltämäksesi, jos tekoäly teki pääosan työstä. Tarkista myös palvelun käyttöehdot, jos aiot julkaista musiikkia tai käyttää sitä kaupallisesti.

**💭 Pysähdy hetkeksi:**

Jos olisit muusikko, miltä tuntuisi, että tekoäly voi tehdä kappaleen tyylissäsi? Entä jos olet opiskelija, jolla ei ole musiikkitaustaa, mutta haluat tehdä taustamusiikin omaan videoon?

Molemmat näkökulmat ovat ymmärrettäviä. Tekoäly voi demokratisoida luomista eli antaa uusille ihmisille mahdollisuuden tehdä asioita. Samalla se voi uhata ihmisten työtä ja oikeuksia.

## Videon luominen tekoälyllä

Video on yksi vaikeimmista generatiivisen tekoälyn alueista. Yksittäinen kuva on jo haastava, mutta video on monta kuvaa peräkkäin. Lisäksi liikkeen, kasvojen, valaistuksen, kameran ja äänen pitäisi pysyä johdonmukaisina.

Nykyiset videotyökalut ovat jo vaikuttavia, mutta niissä on yhä rajoituksia. Ne sopivat usein lyhyisiin videoihin, ideointiin, mainosmaisiin pätkiin, somevideoihin, storyboardeihin ja taustamateriaaleihin. Pitkän elokuvamaisen tarinan tekeminen kokonaan tekoälyllä on edelleen vaikeaa.

### Runway

**Runway** on yksi tunnetuimmista tekoälyvideon työkaluista. Runwayn Gen-4-mallin esittelyssä korostetaan johdonmukaisuutta: sama hahmo, esine tai ympäristö voidaan yrittää säilyttää useissa otoksissa paremmin kuin aiemmin.

Tämä on videossa tärkeää. Jos hahmon kasvot muuttuvat jokaisessa otoksessa, videosta tulee helposti outo. Jos taas tyyli, ympäristö ja hahmot pysyvät samankaltaisina, video näyttää ammattimaisemmalta.

Runwayn virallinen hinnoittelusivu kertoo, että palvelu perustuu suunnitelmiin ja krediitteihin. Ilmainen taso on tarkoitettu kokeiluun, mutta laajempi käyttö vaatii yleensä maksullisen tilauksen.

Runway sopii esimerkiksi:

- lyhyiden videoklippien tekemiseen
- mainosidean visualisointiin
- storyboardin tai kohtauksen kokeiluun
- kuvasta videoksi -kokeiluihin
- taustavideoihin ja efekteihin

### Pika

**Pika** on toinen tunnettu tekoälyvideopalvelu. Sen virallisella hinnoittelusivulla palvelu tarjoaa useita suunnitelmia erilaisiin käyttötarpeisiin.

Pikaa pidetään usein työkaluna, jolla voi tehdä nopeasti lyhyitä, luovia ja someen sopivia videoita. Se voi sopia hyvin kokeiluun, jos tavoitteena ei ole tehdä pitkää tuotantoa vaan testata ideaa.

### Google Veo

**Google Veo** on Google DeepMindin videomallien perhe. Googlen omilla sivuilla Veo 3.1 kuvataan videomallina, jossa on parempaa kontrollia, johdonmukaisuutta ja myös ääneen liittyviä ominaisuuksia. Google AI Studiossa Veo 3.1:n yhteydessä mainitaan myös 4K-ulostulo sekä vaaka- ja pystykuvasuhteet.

Tämä kertoo siitä, mihin suuntaan tekoälyvideo on kehittymässä: ei pelkästään "tee video tekstistä", vaan enemmän kohti hallittua tuotantotyökalua. Käyttäjä haluaa päättää kuvasuhteen, kameran liikkeen, tyylin, äänen ja käyttötarkoituksen.

### Sora ja muuttuva työkalukenttä

OpenAI julkaisi Sora 2 -videomallin vuonna 2025, ja sen yhteydessä korostettiin realistisempaa liikettä, parempaa hallittavuutta sekä synkronoituja ääniä ja dialogia. OpenAI:n omalla sivulla todetaan kuitenkin myös, että Sora-tuote ei ole ollut saatavilla 26.4.2026 jälkeen.

Tämä on hyvä esimerkki siitä, miksi tekoälytyökaluista ei kannata opiskella vain yhtä nimeä. Palvelut voivat muuttua, yhdistyä, kadota tai vaihtaa käyttömallia nopeasti. Tärkeämpää on ymmärtää työkalutyyppi: tekoäly voi luoda lyhyttä videota tekstistä, kuvasta tai olemassa olevasta materiaalista.

### Hyvä videoprompti

Videopromptissa kannattaa kertoa:

- mitä videossa tapahtuu
- millainen kamera tai kuvakulma on
- mikä on tyyli
- millainen liike tapahtuu
- kuinka pitkä video on
- onko mukana ääntä tai puhetta
- mihin video tulee

**Heikko prompti:**

"Tee video koulusta."

**✓ Parempi prompti:**

"Tee 6 sekunnin vaakasuuntainen video modernista luokkahuoneesta. Kamera liikkuu hitaasti vasemmalta oikealle. Opiskelijat työskentelevät tietokoneilla rauhallisesti. Tyyli on realistinen, valoisa ja opetusmateriaaliin sopiva. Ei tekstiä, ei logoja, ei tunnistettavia oikeita henkilöitä."

**Tärkeä huomio:** jos tarvitset tarkkaa faktaa tai oikeaa tapahtumaa, älä luo sitä tekoälyvideona niin, että katsoja voisi luulla sitä oikeaksi tallenteeksi. Merkitse tekoälyllä luotu sisältö selvästi.

### Mitä videoteköäly osaa ja mitä se ei vielä osaa?

Tekoälyvideo osaa jo tehdä vaikuttavia lyhyitä kohtauksia. Se voi luoda maisemia, tunnelmia, animaatiomaisia klippejä ja lyhyitä mainosmaisia pätkiä.

Se ei kuitenkaan ole täydellinen. Ongelmia voi tulla esimerkiksi näissä asioissa:

- kädet, kasvot ja pienet yksityiskohdat voivat vääristyä
- hahmo voi muuttua eri otoksissa
- fysiikka voi näyttää oudolta
- teksti voi mennä väärin
- pitkä tarina ei pysy kasassa
- tarkka ohjaus voi olla vaikeaa

Tekoälyvideo on hyvä ideointiin ja lyhyisiin tuotoksiin. Ammattimaisessa käytössä sitä täytyy yleensä editoida, tarkistaa ja yhdistää muihin työkaluihin.

**💭 Pysähdy hetkeksi:**

Jos opettaja näyttää videon, jonka tekoäly on luonut, pitäisikö siitä kertoa opiskelijoille? Entä jos video näyttää aidolta uutisvideolta?

## Koodausavustajat — tekoäly ohjelmoinnin tukena

**Koodausavustaja** on tekoälytyökalu, joka auttaa kirjoittamaan, selittämään, korjaamaan tai muuttamaan koodia. Se voi ehdottaa seuraavaa riviä, selittää virheen, kirjoittaa funktion tai tehdä muutoksia useisiin tiedostoihin.

Aloittelijan kannattaa ajatella koodia näin: **koodi on ohje tietokoneelle**. Kun ohjelmoit, kirjoitat tietokoneelle tarkkoja ohjeita. Tekoäly voi auttaa näiden ohjeiden kirjoittamisessa, mutta sinun pitää silti ymmärtää, mitä olet tekemässä.

Tekoäly ei tee sinusta automaattisesti ohjelmoijaa. Se voi kuitenkin nopeuttaa oppimista, jos käytät sitä oikein.

### GitHub Copilot

**GitHub Copilot** on yksi tunnetuimmista koodausavustajista. Se toimii esimerkiksi Visual Studio Codessa ja muissa kehitysympäristöissä. Copilot voi ehdottaa koodia samalla kun kirjoitat, vastata kysymyksiin projektista ja auttaa virheiden korjaamisessa.

GitHubin virallinen dokumentaatio kertoo, että Copilotin hinnoittelu on siirtymässä 1.6.2026 käyttöperusteisempaan malliin, jossa käytetään GitHub AI Credits -krediittejä ja mallikohtaisia hintoja.

Tämä on hyvä esimerkki siitä, miksi tarkkoja hintoja ei kannata opetella ulkoa. Tärkeämpää on ymmärtää, mitä työkalu tekee.

Copilot sopii hyvin tilanteisiin, joissa käyttäjä kirjoittaa itse koodia mutta haluaa apua yksityiskohtiin. Se voi ehdottaa esimerkiksi funktion runkoa, testejä tai virheen korjausta.

### Cursor

**Cursor** on tekoälyyn vahvasti integroitu koodieditori. Se muistuttaa Visual Studio Codea, mutta tekoäly on siinä keskeisemmässä roolissa. Cursorin virallinen hinnoittelusivu tarjoaa eri suunnitelmia käyttäjille ja tiimeille.

Cursorin idea on, että tekoäly ymmärtää koko projektia paremmin kuin pelkkä yksittäinen chat-ikkuna. Voit pyytää sitä esimerkiksi muuttamaan useita tiedostoja, etsimään bugia tai selittämään projektin rakennetta.

Tämä sopii opiskelijalle silloin, kun projekti kasvaa yksittäistä tiedostoa suuremmaksi. Alussa kannattaa kuitenkin olla varovainen: jos tekoäly muuttaa liikaa koodia kerralla, opiskelijan voi olla vaikea ymmärtää, mitä tapahtui.

### Claude Code

**Claude Code** on Anthropic-yhtiön koodausagentti. Sen virallisessa kuvauksessa sanotaan, että se ymmärtää koodikantaa, muokkaa tiedostoja, ajaa komentoja ja auttaa ohjelmiston rakentamisessa.

Claude Code toimii enemmän agenttina kuin pelkkänä automaattisena täydennyksenä. Tämä tarkoittaa, että sille voi antaa isomman tehtävän, kuten:

- *"Lisää tähän projektiin kirjautumissivu."*
- *"Korjaa testit ja selitä, mikä oli rikki."*
- *"Etsi, missä käyttäjän tiedot tallennetaan."*

Tällainen työkalu on tehokas, mutta se vaatii käyttäjältä vastuuta. Agentti voi ajaa komentoja ja muuttaa tiedostoja, joten käyttäjän pitää tarkistaa muutokset.

### ChatGPT ja data-analyysi

ChatGPT:ssä on myös data-analyysiin ja koodin ajamiseen liittyviä toimintoja. OpenAI:n ohjeiden mukaan ChatGPT voi auttaa datan puhdistamisessa, yhdistämisessä, kaavioiden tekemisessä ja Python-koodin kirjoittamisessa. Samalla OpenAI huomauttaa, että analyysiympäristö ei voi tehdä ulkoisia verkkopyyntöjä, joten tarvittava data pitää tuoda mukaan tai yhdistää käytettävissä olevasta lähteestä.

Aloittelijalle tämä on hyvä tapa kokeilla ohjelmointia turvallisesti. Voit pyytää esimerkiksi:

- *"Kirjoita Python-ohjelma, joka laskee listan lukujen keskiarvon."*
- *"Selitä tämä koodi rivi riviltä."*
- *"Miksi tämä ohjelma antaa virheen?"*
- *"Keksi minulle harjoitus if-lauseesta ja tarkista vastaukseni."*

### Koodausavustajan käyttäminen oppimisessa

Tekoälyn käyttäminen ohjelmoinnissa ei ole automaattisesti huijaamista. Se riippuu siitä, miten sitä käytetään.

**✓ Hyvä käyttö:**

- pyydät selitystä
- pyydät vihjettä
- pyydät virheen etsimistä
- pyydät esimerkin ja muokkaat sitä itse
- pyydät tekoälyä kyselemään sinulta, jotta opit

**Huono käyttötapa:**

- kopioit vastauksen ymmärtämättä sitä
- palautat tekoälyn tekemän tehtävän omana työnäsi
- et osaa selittää, mitä koodi tekee
- annat tekoälyn tehdä koko projektin, mutta et tarkista mitään

**Hyvä sääntö opiskelijalle:** jos palautat koodia, sinun pitää pystyä selittämään se omin sanoin. Jos et osaa selittää koodia, et vielä osaa sitä.

**💭 Pysähdy hetkeksi:**

Onko laskimen käyttäminen matematiikassa huijaamista? Entä tekoälyn käyttäminen ohjelmoinnissa? Missä menee raja apuvälineen ja oman osaamisen korvaamisen välillä?

## Tekijänoikeudet ja etiikka

Kun käytät tekoälyä kuvan, musiikin, videon tai koodin tekemiseen, sinun pitää miettiä muutakin kuin sitä, onnistuuko lopputulos.

Tärkeimmät kysymykset ovat:

- Mistä tekoäly on oppinut?
- Saanko käyttää tuotosta?
- Pitääkö minun merkitä, että käytin tekoälyä?
- Voiko tuotos loukata jonkun oikeuksia?
- Voiko tuotos johtaa katsojaa harhaan?

### Mistä tekoäly on oppinut?

Tekoälymallit koulutetaan suurella määrällä esimerkkejä. Kuvamallit ovat oppineet kuvista, musiikkimallit musiikista, kielimallit tekstistä ja koodausmallit koodista.

Ongelma on se, että kaikki koulutusaineisto ei välttämättä ole sellaista, johon tekijät ovat antaneet luvan. Siksi monilla aloilla käydään keskustelua ja oikeusjuttuja tekoälystä.

Tämä ei tarkoita, että tekoälyä ei saisi käyttää. Se tarkoittaa, että käyttäjän pitää olla tietoinen asiasta ja käyttää työkaluja vastuullisesti.

### Kuka omistaa tekoälyn tuotoksen?

Tähän ei ole yhtä helppoa vastausta. Se riippuu palvelun käyttöehdoista, maasta, käyttötarkoituksesta ja siitä, millainen tuotos on.

Jos käytät työkalua vain koulutehtävän ideointiin, riski on yleensä pieni. Jos taas aiot myydä tekoälyllä tehtyä musiikkia, mainoskuvia tai videoita, pitää tarkistaa palvelun käyttöehdot ja mahdolliset tekijänoikeuskysymykset.

**Vältä tätä:**

"Luo kuva Disneyn Mikki Hiirestä uudessa seikkailussa, ja myyn sen t-paitana."

Tämä voi rikkoa tavaramerkkejä ja tekijänoikeuksia.

**✓ Parempi:**

"Luo alkuperäinen, iloinen sarjakuvamainen hiirihahmo, joka ei muistuta tunnettua hahmoa. Hahmo seikkailee metsässä."

### Tekoälysisällön merkitseminen

Monet alustat vaativat tai suosittelevat tekoälyllä luodun sisällön merkitsemistä. Meta on kertonut lisäävänsä "AI info" -merkintöjä laajempaan joukkoon kuva-, video- ja äänisisältöä, kun tekoälyn käyttö havaitaan tai käyttäjä ilmoittaa siitä.

Euroopan unionin tekoälysääntelyssä eli AI Actissa on myös läpinäkyvyyteen liittyviä velvoitteita. EU:n komission mukaan AI Act sisältää läpinäkyvyysvelvoitteita tietyille tekoälyjärjestelmille ja niiden käyttäjille.

**Käytännön sääntö opiskelijalle:**

Jos tekoäly teki merkittävän osan kuvasta, musiikista, videosta tai tekstistä, kerro siitä. Esimerkiksi:

- *"Kuva on luotu tekoälyllä."*
- *"Taustamusiikki on tehty Sunolla."*
- *"Videon taustakuva on tekoälyn generoima."*
- *"Koodin virheenkorjauksessa käytettiin ChatGPT:tä."*

Rehellisyys on tärkeää, koska katsojalla, opettajalla, asiakkaalla tai yleisöllä on oikeus tietää, miten sisältö on tehty.

## Työkalun valinta — mikä työkalu mihin?

Tekoälytyökalua ei kannata valita vain siksi, että se on suosittu. Valitse työkalu tehtävän mukaan.

- Jos tarvitset nopeasti kuvan diaan tai raporttiin, **ChatGPT:n kuvagenerointi** on helppo aloituspaikka.
- Jos haluat erittäin näyttävän ja taiteellisen kuvan, **Midjourney** voi olla hyvä vaihtoehto.
- Jos haluat ymmärtää kuvamalleja teknisemmin tai käyttää avoimempia ratkaisuja, **Stable Diffusion** -tyyppiset työkalut ovat kiinnostavia.
- Jos teet kaupallista visuaalista materiaalia Adoben ohjelmilla, **Firefly** on luonteva vaihtoehto.
- Jos tarvitset musiikki-idean, kokeile **Sunoa tai Udiota**.
- Jos tarvitset lyhyen videoklipin tai storyboardin, kokeile **Runwayta, Pikaa tai Googlen Veo-työkaluja**, jos ne ovat käytettävissäsi.
- Jos kirjoitat koodia editorissa, **GitHub Copilot tai Cursor** voi auttaa.
- Jos haluat agenttimaisempaa apua koko projektiin, **Claude Code** -tyyppiset työkalut ovat tehokkaita, mutta vaativat enemmän tarkistamista.
- Jos olet aloittelija ja haluat oppia ohjelmoinnin perusteita, **ChatGPT** voi selittää, kysellä ja antaa pieniä harjoituksia.

Yllä oleva lista kokoaa yhteen ne työkalut, jotka esiteltiin medioittain aiemmin tällä tunnilla. Kun valitset työkalua, mieti ensin, mihin mediaan ja käyttötarkoitukseen sitä tarvitset, ja käytä sitten näitä esimerkkejä lähtökohtana.

## Kohti omaa projektia

Tällä tunnilla olet tutustunut siihen, miten tekoälyä voidaan käyttää erikoistuneissa tehtävissä: kuvissa, musiikissa, videossa ja koodissa.

Tärkeintä ei ole opetella ulkoa yksittäisten työkalujen nimiä. Tärkeämpää on ymmärtää, millaisissa tehtävissä tekoäly voi auttaa ja missä sen rajat ovat.

Kun rakennat omaa bottia tunnilla 18, voit hyödyntää näitä ajatuksia osana **rakennuspalikka 2:n** eli botin määrittelydokumentin rajauksia:

- Milloin botti tarvitsee kuvia?
- Voisiko botti auttaa käyttäjää kirjoittamaan koodia?
- Tarvitaanko projektissa ääntä, musiikkia tai videota?
- Miten käyttäjälle kerrotaan, että sisältö on tekoälyn luomaa?
- Mitä botti ei saa tehdä?

Vastuullinen tekoälyn käyttö tarkoittaa sitä, että työkaluja käytetään avoimesti, tarkasti ja muita kunnioittaen.

## Yhteenveto

Tekoälytyökalut eivät ole enää vain tekstin kirjoittamista varten. Niillä voi luoda kuvia, musiikkia, videoita ja koodia.

**Kuvageneraatio** on jo melko käyttökelpoista. Se sopii hyvin ideointiin, esityksiin, kuvituksiin ja visuaaliseen suunnitteluun. Muista kuitenkin tarkistaa yksityiskohdat, etenkin tekstit, logot ja ihmisiä muistuttavat hahmot.

**Musiikkityökalut** voivat tehdä kokonaisia kappaleita. Ne ovat hyviä kokeiluun, taustamusiikkiin ja ideointiin. Tekijänoikeudet ovat tällä alueella erityisen tärkeitä.

**Videotyökalut** kehittyvät nopeasti. Ne osaavat tehdä vaikuttavia lyhyitä klippejä, mutta pitkät ja täysin johdonmukaiset videot ovat edelleen vaikeita.

**Koodausavustajat** voivat nopeuttaa ohjelmointia ja auttaa oppimisessa. Ne eivät kuitenkaan poista tarvetta ymmärtää koodia itse.

**Tekijänoikeudet, läpinäkyvyys ja etiikka** kuuluvat kaikkeen tekoälyn käyttöön. Jos tekoäly on tehnyt merkittävän osan tuotoksesta, kerro siitä. Älä käytä toisten tyyliä, ääntä, kasvoja, hahmoja tai teoksia tavalla, joka voi loukata heidän oikeuksiaan.

Paras tapa oppia näitä työkaluja on kokeilla niitä itse ja ajatella samalla kriittisesti: mitä työkalu teki hyvin, missä se epäonnistui ja mitä vastuullinen käyttö tässä tilanteessa tarkoittaa?

**Tärkeä huomautus ajantasaisuudesta**

Tämän materiaalin tiedot on tarkistettu 16.5.2026. Tekoälytyökalut muuttuvat poikkeuksellisen nopeasti. Hinnat, mallit, käyttöehdot, saatavuus ja ominaisuudet voivat muuttua jopa muutamassa kuukaudessa.

Kun käytät jotakin työkalua oikeassa projektissa, tarkista aina ajantasaiset tiedot työkalun omalta verkkosivulta. Tämä koskee erityisesti hintoja, kaupallisia käyttöoikeuksia, tekijänoikeuksia ja sitä, mitä mallia palvelu juuri sillä hetkellä käyttää.

Tärkeämpää kuin yksittäiset nimet on ymmärtää työkalutyypit ja niiden rajat.

---

## Lähteet ja tarkistuspäivä

- [NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [UNESCO: Recommendation on the Ethics of Artificial Intelligence](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence)
- [European Commission: GDPR principles](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr/overview-principles/what-data-can-we-process-and-under-which-conditions_en)

Tarkistettu 15.7.2026.
