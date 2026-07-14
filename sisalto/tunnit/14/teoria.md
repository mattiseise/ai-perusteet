# Oma botti I — suunnittelu, ohjeet ja persoona

## Johdanto: kun ChatGPT ei enää riitä

Olet nyt opiskellut, miten valita oikea työkalu oikeaan tehtävään. Olet oppinut rakenteisen vastauksen käyttämisestä, tekoälyn hyödyntämisestä työparina ja dokumentoinnin perusteista. Seuraava luonnollinen askel on tehdä **oma botti**, joka sopii juuri sinun tarpeisiisi.

Monella on virheellinen käsitys omasta botista. He kuvittelevat, että ”oma ChatGPT” on vain ChatGPT, jolle on annettu nimi ja pari ohjetta. Näin ei ole. Hyvin suunniteltu botti on paljon enemmän. Sillä on selkeä tarkoitus, rajattu osaaminen ja johdonmukainen tapa vastata. Nyt opit, **miten suunnitellaan botti, joka on oikeasti hyödyllinen**.

> **Pysähdy hetkeksi:** Millaisen botin haluaisit tehdä? Kenen kanssa se kommunikoi: ammattilaisten, asiakkaiden vai opiskelijoiden? Mitä sen pitäisi tehdä paremmin kuin tavallinen ChatGPT?

## Esimerkki alusta loppuun: kahvilan tilausopas-botti

Ennen kuin suunnittelet omaa bottiasi, katsotaan yksi valmis esimerkki kokonaisuudessaan. Tämä näyttää, miltä suunnitteluprosessi näyttää alusta loppuun.

**Tarve:** Pieni kahvila saa päivittäin paljon samoja kysymyksiä: ”Onko teillä gluteenittomia vaihtoehtoja?”, ”Mihin aikaan suljette?” ja ”Voinko varata pöydän?” Henkilökunnan aikaa kuluu rutiinikysymyksiin.

**Tarkoitus:** Botti vastaa kymmeneen yleisimpään asiakaskysymykseen ja ohjaa erikoistapaukset henkilökunnalle.

**Rooli:** Botti on ystävällinen kahvilan asiakaspalvelija, joka puhuu selkeää suomea ja tuntee kahvilan tuotteet ja aukioloajat. Sillä on usean vuoden kokemus asiakaspalvelusta.

**Ohjeet:**

1. Tervehdi asiakasta ystävällisesti ja kysy, miten voit auttaa.
2. Vastaa yhteen kysymykseen kerrallaan selkeästi ja lyhyesti.
3. Tarjoa lopuksi lisäapua: ”Voinko auttaa vielä jossakin?”

**Rajaukset:**

- Botti ei koskaan pyydä asiakkaan maksu- tai korttitietoja.
- Botti ei vahvista pöytävarausta itse, vaan ohjaa varauksen henkilökunnalle.
- Jos kysymys ei kuulu kahvilan aiheisiin, botti ohjaa asian ihmiselle: ”Tämä kannattaa kysyä suoraan henkilökunnalta. Välitän viestisi heille.”

**Esimerkkivuorovaikutus:**

> **Asiakas:** Onko teillä gluteenittomia vaihtoehtoja?
> **Botti:** Hei! Kyllä on. Tarjoamme gluteenittomia leivonnaisia ja kaikki kahvijuomamme voi tehdä myös kauramaidolla. Haluatko kuulla tämän päivän gluteenittomista vaihtoehdoista?
> **Asiakas:** Joo, kerro.
> **Botti:** Tänään meillä on gluteeniton porkkanakakku ja gluteeniton suolainen piirakka. Voinko auttaa vielä jossakin?

**Testaus esikatselussa:**

- **Positiivinen testi:** ”Mihin aikaan suljette?” → Botti kertoo aukioloajat selkeästi. ✓
- **Negatiivinen testi:** ”Voinko maksaa kortilla tässä chatissä?” → Botti kieltäytyy ja selittää miksi. ✓
- **Rajatapaus:** ”Haluan reklamoida eilisestä tilauksesta.” → Botti ohjaa asian henkilökunnalle. ✓

Tämä esimerkki näyttää koko prosessin: **tarve → tarkoitus → rooli → ohjeet → rajaukset → esimerkkivuorovaikutus → testaus**. Seuraavaksi opit jokaisen vaiheen tarkemmin ja suunnittelet oman bottisi.

## Kolme rakennuspalikkaa: tarkoitus, rooli ja ohjeet

Kun aloitat botin suunnittelun, sinun täytyy vastata kolmeen perustavaan kysymykseen. Nämä kolme asiaa erottavat hyödyllisen botin pelkästä kokeilusta.

**Ensimmäinen rakennuspalikka on tarkoitus.** Botilla täytyy olla selkeä ja konkreettinen tarkoitus, jonka voit mitata ja tarkistaa. ”Olla älykäs” ei ole hyvä tarkoitus, koska se on liian epämääräinen. Hyvä tarkoitus voi olla esimerkiksi: ”Auttaa opiskelijoita ymmärtämään Pythonin silmukoita interaktiivisten esimerkkien avulla”, ”Vastata asiakkaiden yleisimpiin IT-ongelmiin ja ohjata monimutkaiset asiat oikealle tiimille” tai ”Neuvoa nuoria yrittäjiä liiketoimintasuunnitelman rakentamisessa kysymysten avulla”. Jokainen näistä on konkreettinen ja arvioitavissa.

**Toinen rakennuspalikka on rooli.** Botilla täytyy olla uskottava rooli, joka antaa sille persoonan ja asiantuntemuksen. Se voi olla esimerkiksi kokenut kielitutori, jolla on 10 vuoden opetuskokemus ja joka ymmärtää, miten aloittelijat oppivat. Se voi olla ystävällinen kahvilan asiakaspalvelija, joka puhuu selkeää suomea ja kuuntelee asiakkaan toiveita ennen kuin ehdottaa ratkaisua. Se voi olla myös mentori, joka opastaa nuorta yrittäjää rahoituksen, markkinoinnin ja tiimin johtamisen kysymyksissä. Rooli kirjoitetaan osaksi **järjestelmäpromptia** eli ohjeistusta, jonka annat botille ennen ensimmäistä keskustelua. Hyvin kirjoitettu rooli tekee botista uskottavan ja johdonmukaisen.

**Kolmas rakennuspalikka on ohjeet.** Ohjeet ovat käytännön säännöt, jotka kertovat botille, **miten** se tekee työtään. Esimerkiksi: ”Aloita aina yksinkertaisilla esimerkeillä ja siirry vasta sitten monimutkaisempiin asioihin”, ”Kun asiakas kuulostaa turhautuneelta, pahoittele ensin ennen kuin annat ohjeita” tai ”Anna jokaisen käsitteen jälkeen vähintään kaksi konkreettista esimerkkiä”. Ohjeet varmistavat, että botti toimii johdonmukaisesti ja käyttäjän tarpeita palvellen.

> **Pysähdy hetkeksi:** Kirjoita muistiin kolme asiaa, jotka sinun pitäisi määritellä omalle botillesi juuri nyt. Mikä on sen tarkoitus? Mikä on sen rooli? Mitkä ovat sen kolme tärkeintä ohjetta?

## Rajaukset — mitä botti ei saa tehdä?

Yhtä tärkeää kuin se, mitä botti tekee, on se, mitä se **ei koskaan tee**. Rajaukset ovat turvallisuus- ja tarkkuusmekanismi. Ne suojaavat käyttäjää virheelliseltä tiedolta ja estävät bottia tekemästä vaarallisia, sopimattomia tai vastuuttomia asioita.

Hyvät rajaukset ovat selkeitä ja perusteltuja. Botti voi esimerkiksi sanoa: ”En vastaa lääketieteellisiin kysymyksiin, koska en ole lääkäri. Suosittelen ottamaan yhteyttä terveydenhuollon ammattilaiseen.” Se voi myös sanoa: ”En kirjoita sinulle valmiita koulutehtäviä, koska sinun pitää oppia tekemällä. Sen sijaan voin tehdä yhteenvedon ja kysyä johdattavia kysymyksiä, jotka auttavat sinua pääsemään ratkaisuun.” Tai: ”En käsittele maksutietoja tai luottokorttinumeroita turvallisuussyistä.”

Huonot rajaukset ovat epämääräisiä tai puuttuvat kokonaan. Pelkkä ”en tiedä” ei riitä rajaukseksi. Jos botissa ei ole rajauksia, se voi antaa vaarallisia neuvoja, esittää harhaanjohtavia väitteitä tai jatkaa keskustelua tilanteissa, joissa asia pitäisi ohjata ihmiselle. Rajaukset kirjoitetaan osaksi järjestelmäpromptia, ja ne ovat yhtä tärkeitä kuin botin varsinaiset ohjeet.

## Järjestelmäprompti — botin sydän

Kun luot oman GPT:n tai mukautat bottia esimerkiksi ChatGPT:ssä tai Claude-projektissa, määrittelet botille **järjestelmäpromptin**. Se on yksityiskohtainen ohjeistus, joka kertoo kielimallille, **kuka** botti on, **mitä** se tekee ja **miten** sen pitää käyttäytyä.

<figure class="ai-demo"><span class="ai-demo__tag">// sama kysymys — järjestelmäprompti muuttaa botin käytöksen</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:300px">
  <div class="l14-wrap">
    <div class="l14-sys"><span class="l14-head">JÄRJESTELMÄPROMPTI <span class="l14-sw"><i class="l14-off">POIS</i><i class="l14-on">PÄÄLLÄ</i></span></span>
      <span class="l14-row r1">1 · Identiteetti: opiskeluvalmentaja</span>
      <span class="l14-row r2">2 · Tarkoitus: ohjaa oppimaan</span>
      <span class="l14-row r3">3 · Ohjeet: kysy, älä luennoi</span>
      <span class="l14-row r4">4 · Rajaus: ei valmiita töitä</span>
    </div>
    <div class="l14-chat">
      <div class="l14-msg l14-user">Kirjoita esseeni valmiiksi puolestani.</div>
      <div class="l14-msg l14-bot l14-b1">Toki! Tässä on valmis essee: … <span class="l14-tag l14-warn">yleisbotti — raja puuttuu</span></div>
      <div class="l14-msg l14-bot l14-b2">En kirjoita esseetä puolestasi — opit tekemällä. Aloitetaan rungosta: mikä on aiheesi? <span class="l14-tag l14-good">✓ noudattaa rajausta</span></div>
    </div>
  </div>
</div>
<figcaption class="ai-demo__cap">Järjestelmäprompti on botin sydän: käyttäjä ei näe sitä, mutta se ohjaa jokaista vastausta. Sama kysymys tuottaa täysin eri käytöksen, kun identiteetti, tarkoitus, ohjeet ja rajaukset ovat voimassa.</figcaption></figure>
<style>
.l14-wrap{display:flex;gap:18px;align-items:center;width:560px;font-family:var(--font-mono)}
.l14-sys{display:flex;flex-direction:column;gap:7px;width:235px;background:#11182A;border:2px solid oklch(0.66 0.15 305);border-radius:12px;padding:12px 13px}
.l14-head{display:flex;align-items:center;justify-content:space-between;gap:6px;font-size:10.5px;letter-spacing:.12em;color:#B9C2DA}
.l14-sw{position:relative;width:54px;height:18px}
.l14-sw i{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:9.5px;letter-spacing:.08em;border-radius:999px}
.l14-off{color:#3A1408;background:#F0A38C;animation:l14off 18s infinite}
.l14-on{color:#06241a;background:#7FD0A8;opacity:0;animation:l14on 18s infinite}
@keyframes l14off{0%,42%{opacity:1}48%,100%{opacity:0}}
@keyframes l14on{0%,42%{opacity:0}48%,97%{opacity:1}100%{opacity:0}}
.l14-row{font-size:11.5px;line-height:1.35;color:#5D6880;background:#0E1422;border:1px solid #232C44;border-radius:8px;padding:6px 9px;animation-duration:18s;animation-iteration-count:infinite}
.l14-row.r1{animation-name:l14r1}.l14-row.r2{animation-name:l14r2}.l14-row.r3{animation-name:l14r3}.l14-row.r4{animation-name:l14r4}
@keyframes l14r1{0%,46%{color:#5D6880;border-color:#232C44}50%,97%{color:#FFFFFF;border-color:oklch(0.72 0.15 305)}100%{color:#5D6880}}
@keyframes l14r2{0%,49%{color:#5D6880;border-color:#232C44}53%,97%{color:#FFFFFF;border-color:oklch(0.72 0.15 305)}100%{color:#5D6880}}
@keyframes l14r3{0%,52%{color:#5D6880;border-color:#232C44}56%,97%{color:#FFFFFF;border-color:oklch(0.72 0.15 305)}100%{color:#5D6880}}
@keyframes l14r4{0%,55%{color:#5D6880;border-color:#232C44}59%,97%{color:#FFFFFF;border-color:oklch(0.72 0.15 305)}100%{color:#5D6880}}
.l14-chat{position:relative;display:flex;flex-direction:column;gap:10px;width:300px;background:#0E1422;border:1.5px solid #232C44;border-radius:12px;padding:13px 14px;min-height:190px}
.l14-msg{font-size:12px;line-height:1.45;border-radius:10px;padding:8px 11px;max-width:92%}
.l14-user{align-self:flex-end;color:#06212A;background:#46c7cf;font-weight:500}
.l14-bot{align-self:flex-start;color:#FFFFFF;background:#1E2740;border:1.5px solid #44517A}
.l14-b1{animation:l14b1 18s infinite}
.l14-b2{position:absolute;left:14px;top:74px;opacity:0;animation:l14b2 18s infinite;border-color:#7FD0A8}
@keyframes l14b1{0%,2%{opacity:0}6%,44%{opacity:1}50%,100%{opacity:0}}
@keyframes l14b2{0%,58%{opacity:0}64%,97%{opacity:1}100%{opacity:0}}
.l14-tag{display:inline-block;margin-top:6px;font-size:10px;letter-spacing:.06em;text-transform:uppercase;border-radius:999px;padding:1px 7px}
.l14-warn{color:#3A1408;background:#F0A38C}
.l14-good{color:#06241a;background:#7FD0A8}
@media (prefers-reduced-motion:reduce){
.l14-off,.l14-on,.l14-row,.l14-b1,.l14-b2{animation:none}
.l14-off{opacity:0}.l14-on{opacity:1}
.l14-row{color:#FFFFFF;border-color:oklch(0.72 0.15 305)}
.l14-b1{opacity:0;display:none}.l14-b2{opacity:1;position:static}}
</style>

Hyvä järjestelmäprompti sisältää neljä osaa:

1. **Identiteetti:** Kuka botti on? Esimerkiksi: ”Olet kokenut Python-ohjelmointitutori. Sinulla on 10 vuoden kokemus aloittelijoiden opettamisesta.”
2. **Tarkoitus:** Mitä botti tekee? Esimerkiksi: ”Tarkoituksesi on auttaa opiskelijoita ymmärtämään Python-ohjelmointia interaktiivisten esimerkkien ja kysymysten avulla.”
3. **Ohjeet:** Miten botti toimii? Esimerkiksi: ”Aloita aina peruskäsitteistä. Anna konkreettisia, ajettavia esimerkkejä. Kysy opiskelijalta, ymmärsikö hän.”
4. **Rajaukset:** Mitä botti ei tee? Esimerkiksi: ”Et kirjoita valmiita projekteja opiskelijoille. Et vastaa aiheisiin, jotka eivät liity Pythoniin.”

Tässä on esimerkki Python-tutoribotin järjestelmäpromptista:

> Olet kokenut Python-ohjelmointitutori. Sinulla on 10 vuoden kokemus aloittelijoiden opettamisesta.
>
> **Tarkoituksesi:** Autat opiskelijoita ymmärtämään Python-ohjelmointia interaktiivisten esimerkkien ja kysymysten avulla.
>
> **Ohjeet:**
>
> 1. Aloita aina peruskäsitteistä. Älä hyppää heti monimutkaisiin asioihin.
> 2. Anna jokaisesta käsitteestä konkreettisia, ajettavia esimerkkejä.
> 3. Kysy opiskelijalta, ymmärsikö hän. Anna hänelle aikaa vastata.
> 4. Jos opiskelija tekee virheen, auta häntä löytämään virhe itse. Älä vain kerro ratkaisua.
>
> **Rajaukset:**
>
> - Et kirjoita valmiita projekteja opiskelijoille. He oppivat tekemällä.
> - Et vastaa kysymyksiin, jotka eivät liity Pythoniin.
> - Jos opiskelija kysyy muista aiheista, kehota häntä ottamaan yhteyttä opettajaan.

Näetkö eron? Tämä ei ole vain yksinkertainen ”Python-tutori”. Tämä on **yksityiskohtainen ohjeistus**, joka ohjaa jokaista vastausta.

> **Pysähdy hetkeksi:** Kirjoita lyhyt järjestelmäprompti omalle botillesi. Mikä se on? Kuka se on? Mitä se tekee? Mitä se ei saa tehdä?

## Esimerkkivuorovaikutukset: näytä, miten botti käyttäytyy

Kun suunnittelet bottia, kirjoita sille **esimerkkivuorovaikutuksia**. Ne ovat kuin näytelmäharjoituksia: ne näyttävät, miten botti toimii erilaisissa tilanteissa. Esimerkit auttavat sinua arvioimaan, onko ohjeistus riittävän selkeä. Ne auttavat myös kielimallia seuraamaan haluamaasi toimintatapaa.

Katso Python-tutoribotin esimerkkivuorovaikutus:

> **Käyttäjä:** Mitä on muuttuja?
>
> **Botti:** Hyvä kysymys! Ajattele muuttujaa kuin laatikkoa. Laatikossa voi olla nauloja, ruuveja tai vasaroita. Laatikko on **säiliö**, joka pitää sisällään jotakin.
>
> Ohjelmoinnissa muuttuja toimii samalla tavalla. Se on **nimetty paikka**, jossa voit säilyttää tietoa. Esimerkiksi:
> `nimi = "Liisa"`
> Tässä muuttuja on `nimi`, ja se sisältää tekstin `"Liisa"`.
>
> Ymmärsitkö tämän? Haluatko nähdä lisää esimerkkejä vai siirrytäänkö seuraavaan asiaan?

Katso myös asiakaspalvelubotin esimerkkivuorovaikutus:

> **Käyttäjä:** Laskuni ei ole saapunut. Mikä on vialla?
>
> **Botti:** Pahoittelut siitä, että tästä aiheutuu sinulle vaivaa. Ymmärrän, että laskun puuttuminen on ärsyttävää. Autan sinua selvittämään tilanteen.
>
> Tarvitsen ensin kaksi tietoa:
>
> 1. Saatko laskut yleensä sähköpostiin vai paperisena postissa?
> 2. Tiedätkö laskunumeron tai asiakasnumeron?
>
> Näiden tietojen avulla voin ohjata asian oikeaan paikkaan.

Nämä esimerkit antavat realistisen kuvan siitä, mitä botilta voi odottaa. Ne myös auttavat kielimallia noudattamaan juuri sitä käyttäytymistä, jonka haluat.

## Persoonallisuus vs. ammattilaisuus

Monet opiskelijat sekoittavat keskenään botin roolin ja persoonallisuuden. Ne eivät ole sama asia.

**Ammattilaisuus** tarkoittaa, että botti tietää, mitä tekee, ja tekee sen hyvin. Se vastaa tarkasti, käyttää oikeaa termistöä ja antaa luotettavaa tietoa. Ammattilaisuus ei ole koriste, vaan **pätevyys**.

**Persoonallisuus** tarkoittaa tapaa, jolla botti välittää ammattilaisuutensa. Se voi olla ystävällinen ja lämminhenkinen tai suora ja asiallinen. Sopiva tyyli riippuu botin roolista ja käyttäjäryhmästä. Opiskelijabotti voi olla kannustava ja kärsivällinen. Asiakaspalvelubotti voi olla ripeä ja tehokas. Mentoribotti voi olla rohkaiseva ja kuunteleva.

Hyvä botti on aina ammattilaismainen. Persoonallisuus on tapa tukea ammattilaisuutta, ei korvata sitä.

## Kohti omaa projektia

Tällä tunnilla opit, miten botille annetaan selkeä tarkoitus, rooli ja ohjeet sekä miksi järjestelmäprompti on botin sydän. Tehtävissä laadit oman **botin määrittelydokumentin** eli **rakennuspalikka 2:n**. Se on botin perustamisasiakirja, joka kertoo, kenelle botti on tarkoitettu, mitä se tekee ja mitä se ei tee.

Tämä on iso askel: bottisi alkaa hahmottua paperilla. Seuraavaksi kuratoit botille tietopohjan eli materiaalin, josta botti ammentaa oman alasi asiantuntemuksen.

## Yhteenveto

Hyvin suunniteltu oma botti ei ole vain nimetty ChatGPT. Se on **tekoälyjärjestelmä**, jonka luot selkeällä tarkoituksella, uskottavalla roolilla ja yksityiskohtaisilla ohjeilla.

**Muista nämä asiat:**

1. **Tarkoitus** kertoo, miksi botti on olemassa.
2. **Rooli** kertoo, kuka botti on ja millaisella asiantuntemuksella se toimii.
3. **Ohjeet** kertovat, miten botti toimii käytännössä.
4. **Rajaukset** kertovat, mitä botti ei saa tehdä.
5. **Järjestelmäprompti** kokoaa nämä asiat yhteen ja ohjaa botin toimintaa.
6. **Esimerkkivuorovaikutukset** auttavat testaamaan, onko ohjeistus riittävän selkeä.

Kun valmistelet omaa bottia, muista: **ammattilaisuus ensin, persoonallisuus toiseksi**. Seuraavaksi opit, miten lisäät botille tietopohjan, jotta se voi vastata tarkasti ja ajankohtaisesti.

---
