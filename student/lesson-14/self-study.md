# Oma botti I — suunnittelu, ohjeet ja persoona

## Johdanto: Kun ChatGPT ei enää riitä

Olet nyt opiskellut, miten valita oikea työkalu tehtävään. Olet oppinut rakenteisen outputin käyttämisestä, tekoälyn käytöstä työparina ja dokumentoinnin perusteista. Seuraava askel on luonnollinen: tehdä **oma botti**, joka sopii juuri sinun tarpeisiisi.

Monella on virheellinen käsitys omasta botista. He kuvittelevat, että "oma ChatGPT" on vain ChatGPT, jolle on annettu nimi ja pari ohjeistusta. Väärä. Hyvin suunniteltu botti on jotain paljon enemmän. Sillä on selkeä tarkoitus, syvä osaaminen ja johdonmukainen tapa vastata. Nyt opit **miten suunnitella botti, joka on todella hyödyllinen**.

Pysähdy hetkeksi: Mitä bottia haluaisit tehdä? Kenen kanssa se kommunikoi — ammattilaiset, asiakkaat, opiskelijat? Mitä sen pitäisi tehdä paremmin kuin tavallinen ChatGPT?

## Esimerkki alusta loppuun: IT-helpdesk-botti

Ennen kuin suunnittelet omaa bottiasi, katsotaan yksi valmis esimerkki kokonaisuudessaan. Tämä näyttää, miltä suunnitteluprosessi näyttää alusta loppuun.

**Tarve:** IT-tukiosasto saa 40 samaa kysymystä päivässä: "Miten vaihdan salasanan?", "Miten yhdistän tulostimeen?", "VPN ei toimi." Ihmisten aika kuluu rutiineihin.

**Tarkoitus:** "Vastata 10 yleisimpään IT-tukikysymykseen ja ohjata monimutkaiset ongelmat ihmiselle."

**Rooli:** "Olet ystävällinen IT-tukihenkilö, joka puhuu selkeää suomea ilman teknistä termistöä. Sinulla on viiden vuoden kokemus käyttäjätuesta."

**Ohjeet:**
1. Kysy ensin, mikä laite on kyseessä (Windows/Mac/puhelin).
2. Anna ohjeet vaihe vaiheelta, yksi askel kerrallaan.
3. Kysy jokaisen vaiheen jälkeen: "Toimiko? Voimmeko jatkaa?"

**Rajaukset:**
- Ei koskaan pyydä käyttäjän salasanaa.
- Ei tee muutoksia järjestelmiin — vain ohjeistaa.
- Jos ongelma ei ratkea 3 yrityksellä, ohjaa ihmiselle: "Tämä vaatii tarkempaa tutkimista. Lähetän tiketin IT-tiimille."

**Esimerkkivuorovaikutus:**
```
Käyttäjä: VPN ei toimi
Botti: Hei! Selvitetään. Mikä laite sinulla on — Windows, Mac vai puhelin?
Käyttäjä: Windows
Botti: Hyvä. Kokeillaan ensin: avaa VPN-sovellus ja klikkaa "Disconnect", odota 10 sekuntia ja klikkaa "Connect" uudelleen. Toimiko?
Käyttäjä: Ei
Botti: Kokeillaan seuraavaksi: avaa Windows-asetukset → Verkko → VPN → poista yhteys ja lisää se uudelleen. Tarvitsetko tarkemmat ohjeet?
```

**Testaus (esikatselu):**
- Positiivinen testi: "Miten vaihdan salasanan?" → Botti kysyy laitteen ja ohjeistaa vaiheittain ✓
- Negatiivinen testi: "Mikä on ylläpitäjän salasana?" → Botti kieltäytyy ja selittää miksi ✓
- Rajatapaus: "Kone ei käynnisty ollenkaan" → Botti ohjaa ihmiselle ✓

Tämä esimerkki näyttää koko prosessin: tarve → tarkoitus → rooli → ohjeet → rajaukset → esimerkkivuorovaikutus → testaus. Seuraavaksi opit jokaisen vaiheen yksityiskohdat ja suunnittelet omaa bottiasi.

## Kolme rakennuspalikkaa: tarkoitus, rooli, ohjeet

Kun aloitat botin suunnittelun, sinun täytyy vastata kolmeen perustavaan kysymykseen. Nämä kolme asiaa erottavat hyödyllisen botin pelkästään leikiksi tehdystä lelusta.

**Ensimmäinen on tarkoitus.** Botilla täytyy olla selvä, konkreettinen tarkoitus, jonka voit mitata ja tarkistaa. "Olla älykäs" ei ole tarkoitus — se on liian epämääräinen eikä voi väittää, että botti täytti sen. Hyvä tarkoitus kuulostaa tältä: "Auttaa opiskelijoita ymmärtämään Python-loopeita interaktiivisten esimerkkien avulla", "Vastata asiakkaiden IT-ongelmiin 24 tuntia vuorokaudessa ja ohjata heidät oikeille tiimeille, jos asia on monimutkainen", tai "Neuvoa nuoria yrittäjiä, miten liiketoimintasuunnitelma rakennetaan, kysymysten kautta". Jokainen näistä on konkreettinen. Jokainen on mitattavissa. Kun olet valmis, voit sanoa: "Kyllä, tämä botti täytti tarkoituksensa", tai "Ei, se epäonnistui tässä kohdassa".

**Toinen rakennuspalikka on rooli.** Botilla täytyy olla uskottava rooli — se antaa sille persoonallisuuden ja asiantuntemuksen. Se voisi olla kokenut Python-tutori, jolla on 10 vuoden opetuskokemus ja joka tietää, miten nuoret oppivat. Se voisi olla ystävällinen IT-tukihenkilö, joka puhuu sujuvasti suomea ja joka kuuntelee asiakkaan huolia ennen kuin ryhtyy toimiin. Se voisi olla mentori, joka opastaa startup-perustajaa, koska sillä on oikea kokemus rahoituksesta, markkinoinnista ja tiimin johtamisesta. Rooli kirjoitetaan osaksi **järjestelmäpromptia** (system prompt) — sitä ohjeistusta, jonka annat botille ennen ensimmäistä keskustelua. Hyvin kirjoitettu rooli tekee botista uskottavan ja johdonmukaisen.

**Kolmas rakennuspalikka on ohjeet.** Ohjeet ovat käytännön säännöt, jotka kertovat botille, **miten** se tekee työtään päivästä toiseen. Esimerkiksi: "Aloita aina yksinkertaisilla esimerkeillä, siirry vasta sitten monimutkaisempiin asioihin." "Kun asiakas kuulostaa ärsyyntyneeltä, pahoittele ensin, ennen kuin vastaat." "Anna aina vähintään kaksi konkreettista esimerkkiä jokaisen käsitteen jälkeen." Ohjeet varmistavat, että botti käyttäytyy johdonmukaisesti ja tavalla, joka palvelee käyttäjää.

Pysähdy hetkeksi: Kirjoita muistiin kolme asiaa, jotka sinun pitäisi määritellä omalle botillesi juuri nyt. Mitkä ovat sen tarkoitus, rooli ja kolme tärkeintä ohjeistusta?

## Rajaukset — mitä botti EI saa tehdä

Yhtä tärkeää kuin se, mitä botti tekee, on se, mitä se **ei koskaan tee**. Rajaukset ovat turvallisuus- ja tarkkuusmekanismi. Ne suojaavat käyttäjää virheelliseltä tiedolta ja bottia tekemästä vaarallisia tai sopimattomia asioita.

Hyvät rajaukset ovat selkeät ja perusteltavissa. Botti voisi sanoa: "En vastaa lääketieteellisiin kysymyksiin, koska en ole lääkäri — suosittelen sinulle terveyspalveluja." Tai: "En kirjoita sinulle valmiita koululäksyjä, koska sinun pitää oppia tekemällä. Sen sijaan teen yhteenvetoja ja kysyn sinulta johdattavia kysymyksiä, jotka opastavat sinut ratkaisuun." Tai: "En käsittele maksutietoja tai luottokortteja turvallisuussyistä." Nämä rajaukset ovat vastuullisia, ja ne antavat käyttäjälle tietoa siitä, miten botti auttaa ja missä sen vastuu päättyy.

Huonot rajaukset ovat epämääräisiä tai puuttuvat kokonaan. "En tiedä" -vastaus on liian väljä. Jos botissa ei ole rajauksia lainkaan, se voi tehdä mitä tahansa — antaa vaarallisia neuvoja, tehdä harhaanjohtavia väitteitä tai yksinkertaisesti pitää käyttäjää kiinni päivän mittaa. Rajaukset kirjoitetaan osaksi järjestelmäpromptia, ja ne ovat yhtä kriittisiä kuin botin positiiviset ohjeet.

## Järjestelmäprompti — botin sydän

Kun luot oman GPT:n tai mukauttavat bottia ChatGPT:ssä tai Claude-projektissa, pääset määrittelemään **järjestelmäpromptin** (system prompt). Tämä on pitkä, yksityiskohtainen ohjeistus, joka kertoo kielimallille, **kuka** botti on, **mitä** se tekee ja **miten** sen pitäisi käyttäytyä.

Hyvä järjestelmäprompti sisältää neljä osaa. **Ensimmäinen osa on identiteetti:** "Olet kokenut Python-ohjelmointitutori. Sinulla on 10 vuoden kokemus opettamisesta aloittelijoille." **Toinen osa on tarkoitus:** "Tarkoituksesi on auttaa opiskelijoita ymmärtämään Python-ohjelmointia interaktiivisten esimerkkien ja kysymysten avulla." **Kolmas osa on ohjeet:** "Aloita aina peruskäsitteistä. Anna konkreettisia, ajettavia esimerkkejä. Kysy opiskelijalta, ymmärsikö hän." **Neljäs osa on rajaukset:** "En kirjoita valmiita projekteja opiskelijoille. En vastaa aiheisiin, jotka eivät liity Pythoniin."

Tässä on täydellinen esimerkki Python-tutoribotin järjestelmäpromptista:

> Olet kokenut Python-ohjelmointitutori. Sinulla on 10 vuoden kokemus opettamisesta aloittelijoille.
>
> Tarkoituksesi: Auttaa opiskelijoita ymmärtämään Python-ohjelmointia interaktiivisten esimerkkien ja kysymysten avulla.
>
> Ohjeet:
> 1. Aloita aina peruskäsitteistä. Älä hyppää heti monimutkaisiin asioihin.
> 2. Anna konkreettisia, ajettavia esimerkkejä jokaisesta käsitteestä.
> 3. Kysy opiskelijalta, ymmärsikö hän. Anna hänelle aikaa vastata.
> 4. Jos oppilas tekee virheen, auta häntä löytämään virhe itse. Älä vain kerro ratkaisua.
>
> Rajaukset:
> - En kirjoita valmiita projekteja opiskelijoille. He oppivat tekemällä.
> - En vastaa kysymyksiin, jotka eivät liity Pythoniin.
> - Jos oppilas kysyy muista aiheista, kehoita häntä ottamaan yhteyttä opettajaan.

Näetkö eron? Tämä ei ole yksinkertainen "Python-tutori". Tämä on **yksityiskohtainen ohjeistus**, joka ohjaa jokaisen vastauksen.

Pysähdy hetkeksi: Kirjoita lyhyt järjestelmäprompti omalle botillesi. Mitä se on? Kuka se on? Mitä se tekee? Mitä se ei saa tehdä?

## Esimerkkivuorovaikutukset: näytä, miten botti käyttäytyy

Kun suunnittelet bottia, kirjoita **esimerkkivuorovaikutuksia**. Ne ovat kuin näytelmäharjoituksia — näyttävät, miten botti todellisuudessa käyttäytyy eri tilanteissa. Nämä esimerkit auttavat sekä sinua ymmärtämään, onko ohjeistus riittävän selkeä, että kielimallia oppimaan, mitä sinä haluat.

Katso Python-tutoribotin esimerkkivuorovaikutus:

> **Käyttäjä:** Mitä on muuttuja?
>
> **Botti:** Hyvä kysymys! Ajattele muuttujaa kuin säiliötä. Liitteri voi sisältää nauloja, ruuveja tai vasareita. Se on **säiliö**, joka pitää sisällään jotain.
>
> Ohjelmoinnissa muuttuja toimii samalla tavalla. Se on **nimetty paikka**, jossa voit säilyttää tietoja. Esimerkiksi:
> ```python
> nimi = "Liisa"
> ```
> Tässä muuttuja on `nimi` ja se sisältää tekstin "Liisa".
>
> Ymmärsikö tämän? Halusitko nähdä lisää esimerkkejä vai mennään seuraavaan asiaan?

Ja IT-helpdesk-botin esimerkkivuorovaikutus:

> **Käyttäjä:** Laskuni ei ole saapunut. Mikä on vialla?
>
> **Botti:** Pahoittelut siitä, että tämä aiheuttaa sinulle vaivaa. Ymmärrän, että laskun puuttuminen on ärsyttävää. Autan sinua selvittämään, mitä tapahtui:
> 1. Saatko laskut normaalisti sähköpostiin vai paperisena postissa?
> 2. Mikä on laskunumerosi, jos tiedät sen?
>
> Näiden tietojen perusteella voin tutkia tilannetta paremmin.

Nämä esimerkit antavat käyttäjille realistisen kuvan siitä, mitä odottaa. Ne myös auttavat kielimallia oppimaan juuri siihen käyttäytymiseen, jonka haluat.

## Persoonallisuus vs. ammattilaisuus

Monet opiskelijat sekoittavat "roolin antamisen botille" ja "persoonallisuuden lisäämisen". Ne eivät ole sama asia.

**Ammattilaisuus** tarkoittaa, että botti tietää, mitä tekee, ja tekee sen hyvin. Se vastaa tarkkuudella, käyttää oikeaa termistöä ja antaa luotettavaa tietoa. Ammattilaisuus on silmälläpito — se ei ole mukava juttu, se on **pätevyys**.

**Persoonallisuus** on tapa, jolla botti välittää ammattilaisuuttaan. Se voi olla ystävällinen ja lämminhenkinen tai suora ja asiallinen. Se riippuu roolista ja käyttäjäryhmästä. Opiskelija-botti voi olla kannustava ja kärsivällinen. IT-helpdesk-botti voi olla ripeä ja tehokas. Mentoribotti voi olla rohkaiseva ja kuuntelevainen.

Hyvä botti on aina ammattilaismainen. Persoonallisuus on makuasia.

## Kohti omaa projektia

Tällä tunnilla opit, miten botille annetaan selkeä tarkoitus, rooli ja ohjeet — ja miten järjestelmäprompti on botin sydän. Tehtävissä suunnittelit oman bottisi persoonallisuuden ja kirjoitit sille ensimmäisen järjestelmäpromptin (**Botin rakennuspala 3**). Tämä on iso askel: botillasi on nyt alusta, kontekstistrategia ja persoonallisuus. Seuraavaksi opit, miten varmistat, että botti toimii vastuullisesti — miten lisäät sille tietopohjan, rajaukset ja testauksen.

## Yhteenveto

Hyvin suunniteltu oma botti ei ole vain nimetty ChatGPT — se on AI-järjestelmä, jonka luot selkeällä tarkoituksella, vakuuttavalla roolilla ja yksityiskohtaisilla ohjeilla. Järjestelmäprompti on botin sydän. Se sisältää identiteetin, tarkoituksen, ohjeet ja rajaukset. Esimerkkivuorovaikutukset auttavat sinua testaamaan, onko ohjeistus riittävä. Kun valmistelet omaa bottia, muista: ammattilaisuus ensin, persoonallisuus toiseksi. Seuraavaksi opit, miten lisäät botille tietokannan, jotta se voi vastata tarkasti ja ajankohtaisesti.
