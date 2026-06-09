# Oma botti I — suunnittelu, ohjeet ja persoona

## Johdanto: kun ChatGPT ei enää riitä

Olet nyt opiskellut, miten valita oikea työkalu oikeaan tehtävään. Olet oppinut rakenteisen vastauksen käyttämisestä, tekoälyn hyödyntämisestä työparina ja dokumentoinnin perusteista. Seuraava luonnollinen askel on tehdä **oma botti**, joka sopii juuri sinun tarpeisiisi.

Monella on virheellinen käsitys omasta botista. He kuvittelevat, että ”oma ChatGPT” on vain ChatGPT, jolle on annettu nimi ja pari ohjetta. Näin ei ole. Hyvin suunniteltu botti on paljon enemmän. Sillä on selkeä tarkoitus, rajattu osaaminen ja johdonmukainen tapa vastata. Nyt opit, **miten suunnitellaan botti, joka on oikeasti hyödyllinen**.

> **Pysähdy hetkeksi:** Millaisen botin haluaisit tehdä? Kenen kanssa se kommunikoi: ammattilaisten, asiakkaiden vai opiskelijoiden? Mitä sen pitäisi tehdä paremmin kuin tavallinen ChatGPT?

## Esimerkki alusta loppuun: IT-helpdesk-botti

Ennen kuin suunnittelet omaa bottiasi, katsotaan yksi valmis esimerkki kokonaisuudessaan. Tämä näyttää, miltä suunnitteluprosessi näyttää alusta loppuun.

**Tarve:** IT-tukiosasto saa päivittäin paljon samoja kysymyksiä: ”Miten vaihdan salasanan?”, ”Miten yhdistän tulostimeen?” ja ”VPN ei toimi.” Ihmisten aikaa kuluu rutiinikysymyksiin.

**Tarkoitus:** Botti vastaa kymmeneen yleisimpään IT-tukikysymykseen ja ohjaa monimutkaiset ongelmat ihmiselle.

**Rooli:** Botti on ystävällinen IT-tukihenkilö, joka puhuu selkeää suomea ilman turhaa teknistä termistöä. Sillä on viiden vuoden kokemus käyttäjätuesta.

**Ohjeet:**

1. Kysy ensin, mikä laite on kyseessä: Windows-tietokone, Mac vai puhelin.
2. Anna ohjeet vaihe vaiheelta, yksi askel kerrallaan.
3. Kysy jokaisen vaiheen jälkeen: ”Toimiko? Voimmeko jatkaa?”

**Rajaukset:**

- Botti ei koskaan pyydä käyttäjän salasanaa.
- Botti ei tee muutoksia järjestelmiin, vaan ainoastaan ohjeistaa käyttäjää.
- Jos ongelma ei ratkea kolmen yrityksen jälkeen, botti ohjaa asian ihmiselle: ”Tämä vaatii tarkempaa tutkimista. Lähetän tiketin IT-tiimille.”

**Esimerkkivuorovaikutus:**

> **Käyttäjä:** VPN ei toimi.
> **Botti:** Hei! Selvitetään asia. Mikä laite sinulla on: Windows, Mac vai puhelin?
> **Käyttäjä:** Windows.
> **Botti:** Hyvä. Kokeillaan ensin tätä: avaa VPN-sovellus, klikkaa ”Disconnect”, odota 10 sekuntia ja klikkaa sitten ”Connect” uudelleen. Toimiko?
> **Käyttäjä:** Ei.
> **Botti:** Kokeillaan seuraavaksi: avaa Windowsin asetukset → Verkko → VPN. Poista yhteys ja lisää se uudelleen.
> **Botti:** Tarvitsetko tähän tarkemmat ohjeet?

**Testaus esikatselussa:**

- **Positiivinen testi:** ”Miten vaihdan salasanan?” → Botti kysyy laitteen ja ohjeistaa vaiheittain. ✓
- **Negatiivinen testi:** ”Mikä on ylläpitäjän salasana?” → Botti kieltäytyy ja selittää miksi. ✓
- **Rajatapaus:** ”Kone ei käynnisty ollenkaan.” → Botti ohjaa asian ihmiselle. ✓

Tämä esimerkki näyttää koko prosessin: **tarve → tarkoitus → rooli → ohjeet → rajaukset → esimerkkivuorovaikutus → testaus**. Seuraavaksi opit jokaisen vaiheen tarkemmin ja suunnittelet oman bottisi.

## Kolme rakennuspalikkaa: tarkoitus, rooli ja ohjeet

Kun aloitat botin suunnittelun, sinun täytyy vastata kolmeen perustavaan kysymykseen. Nämä kolme asiaa erottavat hyödyllisen botin pelkästä kokeilusta.

**Ensimmäinen rakennuspalikka on tarkoitus.** Botilla täytyy olla selkeä ja konkreettinen tarkoitus, jonka voit mitata ja tarkistaa. ”Olla älykäs” ei ole hyvä tarkoitus, koska se on liian epämääräinen. Hyvä tarkoitus voi olla esimerkiksi: ”Auttaa opiskelijoita ymmärtämään Pythonin silmukoita interaktiivisten esimerkkien avulla”, ”Vastata asiakkaiden yleisimpiin IT-ongelmiin ja ohjata monimutkaiset asiat oikealle tiimille” tai ”Neuvoa nuoria yrittäjiä liiketoimintasuunnitelman rakentamisessa kysymysten avulla”. Jokainen näistä on konkreettinen ja arvioitavissa.

**Toinen rakennuspalikka on rooli.** Botilla täytyy olla uskottava rooli, joka antaa sille persoonan ja asiantuntemuksen. Se voi olla esimerkiksi kokenut Python-tutori, jolla on 10 vuoden opetuskokemus ja joka ymmärtää, miten aloittelijat oppivat. Se voi olla ystävällinen IT-tukihenkilö, joka puhuu selkeää suomea ja kuuntelee asiakkaan huolia ennen kuin ehdottaa ratkaisua. Se voi olla myös mentori, joka opastaa startup-perustajaa rahoituksen, markkinoinnin ja tiimin johtamisen kysymyksissä. Rooli kirjoitetaan osaksi **järjestelmäpromptia** eli ohjeistusta, jonka annat botille ennen ensimmäistä keskustelua. Hyvin kirjoitettu rooli tekee botista uskottavan ja johdonmukaisen.

**Kolmas rakennuspalikka on ohjeet.** Ohjeet ovat käytännön säännöt, jotka kertovat botille, **miten** se tekee työtään. Esimerkiksi: ”Aloita aina yksinkertaisilla esimerkeillä ja siirry vasta sitten monimutkaisempiin asioihin”, ”Kun asiakas kuulostaa turhautuneelta, pahoittele ensin ennen kuin annat ohjeita” tai ”Anna jokaisen käsitteen jälkeen vähintään kaksi konkreettista esimerkkiä”. Ohjeet varmistavat, että botti toimii johdonmukaisesti ja käyttäjän tarpeita palvellen.

> **Pysähdy hetkeksi:** Kirjoita muistiin kolme asiaa, jotka sinun pitäisi määritellä omalle botillesi juuri nyt. Mikä on sen tarkoitus? Mikä on sen rooli? Mitkä ovat sen kolme tärkeintä ohjetta?

## Rajaukset — mitä botti ei saa tehdä?

Yhtä tärkeää kuin se, mitä botti tekee, on se, mitä se **ei koskaan tee**. Rajaukset ovat turvallisuus- ja tarkkuusmekanismi. Ne suojaavat käyttäjää virheelliseltä tiedolta ja estävät bottia tekemästä vaarallisia, sopimattomia tai vastuuttomia asioita.

Hyvät rajaukset ovat selkeitä ja perusteltuja. Botti voi esimerkiksi sanoa: ”En vastaa lääketieteellisiin kysymyksiin, koska en ole lääkäri. Suosittelen ottamaan yhteyttä terveydenhuollon ammattilaiseen.” Se voi myös sanoa: ”En kirjoita sinulle valmiita koulutehtäviä, koska sinun pitää oppia tekemällä. Sen sijaan voin tehdä yhteenvedon ja kysyä johdattavia kysymyksiä, jotka auttavat sinua pääsemään ratkaisuun.” Tai: ”En käsittele maksutietoja tai luottokorttinumeroita turvallisuussyistä.”

Huonot rajaukset ovat epämääräisiä tai puuttuvat kokonaan. Pelkkä ”en tiedä” ei riitä rajaukseksi. Jos botissa ei ole rajauksia, se voi antaa vaarallisia neuvoja, esittää harhaanjohtavia väitteitä tai jatkaa keskustelua tilanteissa, joissa asia pitäisi ohjata ihmiselle. Rajaukset kirjoitetaan osaksi järjestelmäpromptia, ja ne ovat yhtä tärkeitä kuin botin varsinaiset ohjeet.

## Järjestelmäprompti — botin sydän

Kun luot oman GPT:n tai mukautat bottia esimerkiksi ChatGPT:ssä tai Claude-projektissa, määrittelet botille **järjestelmäpromptin**. Se on yksityiskohtainen ohjeistus, joka kertoo kielimallille, **kuka** botti on, **mitä** se tekee ja **miten** sen pitää käyttäytyä.

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

Katso myös IT-helpdesk-botin esimerkkivuorovaikutus:

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

**Persoonallisuus** tarkoittaa tapaa, jolla botti välittää ammattilaisuutensa. Se voi olla ystävällinen ja lämminhenkinen tai suora ja asiallinen. Sopiva tyyli riippuu botin roolista ja käyttäjäryhmästä. Opiskelijabotti voi olla kannustava ja kärsivällinen. IT-helpdesk-botti voi olla ripeä ja tehokas. Mentoribotti voi olla rohkaiseva ja kuunteleva.

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
