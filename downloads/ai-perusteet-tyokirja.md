# AI · Perusteet — työkirja

**Kokeet, havainnot ja lopputyöt**

Työkirja kulkee mukanasi koko kurssin ajan. Kirjaa promptit, kokeiden tulokset, lähteet ja tekemäsi korjaukset työkirjaan työskentelyn aikana. Kurssisivusto ei säilytä näitä tuotoksia puolestasi.

Työkirja ei korvaa oppituntien tehtävänantoja. Avaa aina myös kyseisen tunnin ohje. Tämä pohja auttaa sinua kokoamaan arvioinnissa tarvittavan näytön yhteen paikkaan. Voit täyttää koko työkirjan tai vain opiskelemasi osion.

> **Huolehdi tietosuojasta.** Älä kirjoita työkirjaan henkilötietoja, salaisuuksia tai organisaation luottamuksellista tietoa. Käytä harjoituksissa kuvitteellista tai anonymisoitua aineistoa.

## Omat tiedot ja opiskelutapa

**Nimi tai sovittu tunniste**

[Kirjoita tähän.]

**Opiskelen**

- [ ] itsenäisesti
- [ ] oppilaitoksen toteutuksessa

**Täytän seuraavat osat**

- [ ] Teoria
- [ ] Tekoälyjen käyttö
- [ ] Agentit

**Työkirjan tallennuspaikka**

[Kirjoita tähän.]

**Käyttämäni työkalut**

[Kirjoita tähän. Työkalu voi vaihtua tehtävästä toiseen.]

> **Kolme osaa — kolme mahdollista projektia.** Sinun ei tarvitse käyttää samaa aihetta kaikissa osissa. Valitse kuhunkin lopputyöhön tilanne, jonka avulla voit osoittaa kyseisen osion tavoitteiden mukaisen osaamisen.

## Työkirjan kartta

Työkirja on yksi kokonaisuus, mutta sinun ei tarvitse täyttää sitä kerralla. Valitse opiskelemasi osa ja etene oppituntien tahdissa.

- **Teoria:** kerää todistusaineistot tunneilla 3, 5 ja 7 ja viimeistele lopputyö tunnilla 9.
- **Tekoälyjen käyttö:** rakenna promptauspankki sekä botin määrittely ja tietopohja tunneilla 12, 14 ja 15. Viimeistele apuri-botti tunneilla 17–18.
- **Agentit:** tee pohjapiirrokset tunneilla 19, 21 ja 23–25. Rakenna, testaa ja viimeistele kokonaisuus tunneilla 26–27.

### Näin etenet

1. Avaa aina myös kyseisen oppitunnin tehtävänanto kurssisivustolta.
2. Täytä vain opiskelemasi osan ajankohtainen kohta. Lisää kuvat, kaaviot ja laajat tuotokset linkkeinä tai liitteinä.
3. Tallenna työ säännöllisesti omalle laitteellesi tai valitsemaasi pilvipalveluun.
4. Tee osion lopputarkistus ja vie valmis työ myös PDF-muotoon.

Wordissa voit liikkua otsikosta toiseen valitsemalla **Näytä → Siirtymisruutu**. Markdown-versio toimii siirrettävänä rinnakkaispohjana, jos et halua käyttää Wordia.

---

# Osa 1 · Teoria

## Todistusaineisto 1: Miten kielimalli tuottaa tekstiä

Tee kokeet tunnilla 3. Säilytä tarkat syötteet ja tulokset, jotta voit palata niihin Teoria-osion lopputyössä.

### Koe A: Seuraavan sanan ennustaminen

**Kirjoita tarkka syöte.**

[Kirjoita tähän.]

**Tulos 1**

[Kirjoita tähän.]

**Tulos 2**

[Kirjoita tähän.]

**Tulos 3**

[Kirjoita tähän.]

### Koe B: Sama kysymys, eri vastaus

**Kirjoita tarkka kysymys.**

[Kirjoita tähän.]

**Vastaus 1**

[Kirjoita tähän.]

**Vastaus 2**

[Kirjoita tähän.]

**Vertaa vastauksia. Mitä eroja huomasit?**

[Kirjoita tähän.]

### Koe C: Vakuuttava vai oikea?

**Kirjoita tarkistettava kysymys ja mallin vastaus.**

[Kirjoita tähän.]

**Nimeä luotettava lähde ja kirjoita tarkistettu vastaus.**

[Kirjoita tähän.]

**Mitä havainto kertoo kielimallin luotettavuudesta?**

[Kirjoita tähän.]

### Oma analyysi, noin 300 sanaa

Selitä, miten kielimalli tuottaa tekstiä. Kerro, mitä tarkoittaa, että malli ennustaa eikä tiedä, ja kuvaa tilanne, jossa tästä voi syntyä ongelma. Käytä käsitteitä *token*, *seuraavan tokenin ennustaminen*, *lämpötila tai epädeterminismi* ja *hallusinaatio*.

[Kirjoita tähän.]

## Todistusaineisto 2: Kun konteksti ei enää kanna

Tee koe tunnilla 5. Tavoitteena on osoittaa, miten rajaus voi kadota kontekstista ja miten käyttäjä palauttaa sen.

**Kirjoita alkuperäinen rajaus kokonaisuudessaan.**

[Kirjoita tähän.]

**Millä kysymyksellä testasit rajauksen muistamista?**

[Kirjoita tähän.]

**Kirjoita vastaus ennen rajauksen palauttamista.**

[Kirjoita tähän.]

**Kuvaa, milloin ja miten rajaus katosi.**

[Kirjoita tähän.]

**Kirjoita toistettu rajaus ja sen jälkeinen vastaus.**

[Kirjoita tähän.]

### Oma tapausesimerkki, noin 300 sanaa

Kuvaa tilanne, jossa olennainen tieto unohtui. Selitä, miksi näin kävi, mitä siitä seurasi ja miten käyttäjä voi ehkäistä ongelman. Käytä käsitteitä *konteksti-ikkuna*, *FIFO-periaate*, *ankkurointi*, *pilkkominen* ja *dokumentointi*.

[Kirjoita tähän.]

## Todistusaineisto 3: Luotettavuusarvio ja tarkistuskäytäntö

Arvioi tunnilla 7 sekä kielimallin väite että petoksia tunnistavan luokittelumallin tulokset. Näin osoitat, että eri tekoälyjärjestelmien luotettavuutta tarkistetaan eri näytöllä.

### Kielimallin väitteen tarkistus

**Kirjaa tarkistettava väite ja mallin vastaus.**

[Kirjoita tähän.]

**Nimeä riippumaton lähde ja kirjaa, mitä se osoittaa.**

[Kirjoita tähän.]

**Tee johtopäätös: vahvistuiko väite, kumoutuiko se vai jäikö se epävarmaksi?**

[Kirjoita tähän.]

### Luokittelumallin arvio

Petosmalli arvioi 1 000 maksua. Todellisia petoksia oli 10. Malli löysi niistä 8 ja pysäytti lisäksi 42 tavallista maksua.

**Kirjaa väärät positiiviset ja väärät negatiiviset sekä selitä niiden käytännön seuraukset.**

[Kirjoita tähän.]

**Laske tai tulkitse kokonaistarkkuus, osumatarkkuus ja kattavuus. Mitä kukin mittari kertoo — ja mitä se ei kerro?**

[Kirjoita tähän.]

### Oma tarkistuskäytäntö

**Kirjoita 6–8 vaihetta, joilla tarkistat tekoälytuloksen. Aloita jokainen vaihe toimintaverbillä.**

[Kirjoita tähän.]

## Teoria-osion lopputyö

Valitse kirjallinen tai visuaalis-suullinen suoritustapa. Käytä kaikkia kolmea todistusaineistoa.

**Valitse suoritustapa.**

- [ ] Kirjallinen asiantuntijalausunto, 500–700 sanaa
- [ ] Tilannekartta ja päätöspuu sekä 5–8 minuutin suullinen esitys

**Valitse skenaario.**

- [ ] Asiakaspalvelu ja tietovuoto
- [ ] Rekrytointialgoritmi ja syrjintä
- [ ] Markkinointisisältö ja tekijänoikeudet

Käytä tunnilla 8 arvioimiasi lähteitä. Jos jokin työn keskeinen väite ei selviä niistä, tee tunnilla 9 enintään yksi uusi lähdetarkistus.

**Kirjaa keskeiset riskit ja käsitteet.**

[Kirjoita tähän.]

**Nimeä käyttämäsi todistusaineistot ja tunnilla 8 arvioidut lähteet. Kirjaa, mitä väitettä kukin lähde tukee.**

[Kirjoita tähän.]

**Liitä tarkka prompti tai keskusteluloki.**

[Kirjoita tähän tai lisää linkki tai liite.]

### Työn neljä osaa

Jäsennä valitsemasi suoritustapa näiden neljän kysymyksen avulla.

**1. Mitä tapahtui? Kuvaa tilanne neutraalisti.**

[Kirjoita tähän.]

**2. Miksi se tapahtui? Selitä syyt kurssin käsitteillä.**

[Kirjoita tähän.]

**3. Miten tilanne pitäisi hoitaa? Ehdota konkreettiset toimenpiteet.**

[Kirjoita tähän.]

**4. Miten ammatillinen ja käytännön vastuu jakautuvat? Kerro, kuka vastaa mistä ja miksi.**

[Kirjoita tähän.]

### Kirjallinen suoritustapa

**Lisää luonnos ja valmis asiantuntijalausunto linkkeinä tai liitteinä.**

[Kirjoita tähän tai lisää linkki tai liite.]

### Visuaalis-suullinen suoritustapa

Tee yhden sivun tilannekartta, jossa on neljä kenttää: mitä tapahtui, miksi se tapahtui, miten tilanne hoidetaan ja miten vastuu jakautuu. Avainsanat ja lyhyet lauseet riittävät, koska avaat perustelut puheessa. Tee lisäksi kevyt päätöspuu, jossa on kolme päätöskohtaa, kaksi haaraa kussakin sekä päätepisteissä toiminta ja vastuurooli.

**Tallenna yhden sivun tilannekartta.**

[Lisää linkki tai liite.]

**Tallenna kevyt päätöspuu.**

[Lisää linkki tai liite.]

**Tallenna 5–8 minuutin esityksen muistiinpanot tai nauhoite.**

[Kirjoita tähän tai lisää linkki tai liite.]

### Korjausloki — kaksi korjausta

| Ennen | Jälkeen | Miksi korjasin? | Lähde tai käsite |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |

**Kirjoita kirjallisen suoritustavan 1–2 minuutin puolustuksen muistiinpanot.**

[Kirjoita tähän.]

### Lopputarkistus

- [ ] Käytän käsitteitä täsmällisesti ja sovellan niitä tilanteeseen.
- [ ] Hyödynnän kaikkia kolmea todistusaineistoa.
- [ ] Ehdotan konkreettisia toimenpiteitä: kuka tekee, mitä tekee ja milloin.
- [ ] Tuotos on selkeä ja asiallinen, ja sen väitteet ovat perusteltuja.
- [ ] Käsittelen vastuukysymyksen omana osanaan.

---

# Osa 2 · Tekoälyjen käyttö

## Rakennuspalikka 1: Testattu promptikortti

Laadi tunnilla 12 yksi uudelleen käytettävä promptikortti. Testaa kaksi versiota samalla aineistolla ja muuta niiden välissä vain yhtä nimettyä asiaa.

**Kortin nimi ja käyttötilanne**

[Kirjoita tähän.]

**Tavoite, käyttäjä tai yleisö sekä vaihtuvan syötteen paikka**

[Kirjoita tähän.]

**Laatukriteerit, jotka päätit ennen ensimmäistä ajoa**

[Kirjoita tähän.]

**Promptin versio 1, käytetty aineisto ja saatu vastaus**

[Kirjoita tähän.]

**Nimeä yksi havaittu puute ja sitä vastaava promptimuutos.**

[Kirjoita tähän.]

**Promptin versio 2 ja samalla aineistolla saatu vastaus**

[Kirjoita tähän.]

**Vertaa vastauksia laatukriteereillä. Mitä muutos osoitti tässä testissä?**

[Kirjoita tähän.]

**Kirjaa kortin tunnettu raja ja kerro, miten hyödynnät toimivaa rakennetta botin järjestelmäpromptissa.**

[Kirjoita tähän.]

## Rakennuspalikka 2: Botin määrittely

**Botin nimi**

[Kirjoita tähän.]

**Botin aihe**

[Kirjoita tähän.]

**Tyypillinen käyttötilanne: missä tilanteessa ja kenelle botti on hyödyllinen?**

[Kirjoita tähän.]

**Kohderyhmä**

[Kirjoita tähän.]

**Tarkoitus: mitä käyttäjän ongelmaa botti auttaa ratkaisemaan?**

[Kirjoita tähän.]

**Persoona ja äänensävy**

[Kirjoita tähän.]

**Kuvaa työnkulku 5–7 vaiheena.**

[Kirjoita tähän.]

**Kirjaa 3–5 rajaa sille, mitä botti ei tee.**

[Kirjoita tähän.]

**Mitä rakentavaa tai kriittistä palautetta sait tekoälyltä tai vertaiselta? Mitä muutit sen perusteella?**

[Kirjoita tähän.]

**Tiivistä botin ydin yhteen lauseeseen.**

[Kirjoita tähän.]

## Rakennuspalikka 3: Tietopohja ja testisuunnitelma

**Kirjaa 5–8 tietotarvetta, joihin botin pitää osata vastata.**

[Kirjoita tähän.]

| Dokumentti | Lähde tai linkki | Miksi mukana? | Mitä tietotarvetta se tukee? | Luotettavuus ja ajantasaisuus | Tietosuoja tai käyttöoikeus |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

**Mitä tietopohja kattaa hyvin? Mitä se ei vielä kata?**

[Kirjoita tähän.]

Kirjaa näkyviin myös puuttuva tieto: milloin botin pitää sanoa, ettei tietopohja riitä vastaukseen?

**Tietopohjan kansio tai tallennuspaikka**

[Kirjoita tähän.]

- [ ] Tietopohjan 2–4 varsinaista lähdedokumenttia on tallennettu samaan kansioon, ja niiden nimet vastaavat taulukkoa.

## Tunti 16: Bottiprojektin valintakortti

Kokeile käytännössä yhtä työkalureittiä. Jos sopivaa palvelua ei ole käytettävissä, arvioi opettajan antamia esimerkkituotoksia. Muut reitit vertailet lyhyesti ilman erillisiä tuotoksia.

**Valitse kokeiltu reitti.**

- [ ] Kuva
- [ ] Ääni tai musiikki
- [ ] Video
- [ ] Koodi

### Yhden välinekokeilun dokumentointi

**Käyttötarkoitus, käyttäjä ja tärkein onnistumisen ehto**

[Kirjoita tähän.]

**Käytetty väline, syöte ja mahdollinen lähdeaineisto**

[Kirjoita tähän.]

**Ennalta päätetyt arviointikriteerit ja version 1 havainnot**

[Kirjoita tähän.]

**Yksi nimetty muutos, version 2 tulos ja rajattu johtopäätös**

[Kirjoita tähän.]

### Valintakortti

| Työkalureitti | Sopisiko se bottisi käyttäjätarpeeseen? Miksi tai miksi ei? |
|---|---|
| Kuva |  |
| Ääni tai musiikki |  |
| Video |  |
| Koodi |  |

| Kysymys | Toteutustapa A | Toteutustapa B |
|---|---|---|
| Miten järjestelmäprompti ja tietopohja toteutetaan? |  |  |
| Tarvitaanko erikoistyökalua? Miksi? |  |  |
| Millä näytöllä osoitat toiminnan tai suunnittelun? |  |  |
| Mikä on suurin riski tai rajoitus? |  |  |

**Kirjoita toteutuspäätös, tärkein riskirajaus ja havaittava käyttöönottokriteeri. Nimeä suunnittelupolulla teknisesti todentamattomat ominaisuudet.**

[Kirjoita tähän.]

## Apuri-botin lopputyö

Valitse toimiva tekninen toteutus tai dokumentoitu suunnittelusuoritus. Polut ovat samanarvoisia, mutta niissä osoitetaan osaaminen eri tavalla.

**Valitse toteutustapa.**

- [ ] Toimiva tekninen toteutus
- [ ] Dokumentoitu suunnittelusuoritus

**Lisää polkusi mukainen ydintuotos.**

Teknisellä polulla lisää linkki bottiin ja tallennettu suoritusjälki. Suunnittelupolulla lisää arkkitehtuuri ja selvästi simuloiduksi merkitty suoritusjälki, jossa näkyvät järjestelmäprompti, käyttäjän syötteet, vastaukset ja suunnitellut työkaluvaiheet. Simulaatio osoittaa suunnitelman johdonmukaisuuden, mutta ei todista integraatioiden, käyttöoikeuksien, tilan säilymisen tai lokituksen toimivuutta.

[Kirjoita tähän.]

**Liitä päivitetty botin määrittely.**

[Kirjoita tähän tai lisää linkki tai liite.]

**Kirjoita järjestelmäprompti kokonaisuudessaan.**

[Kirjoita tähän.]

**Nimeä tietopohjan 2–4 dokumenttia ja perustele valinnat.**

[Kirjoita tähän.]

> **Tuntien aikajana:** Aja tai simuloi kaikki kolme ennalta kirjoitettua testiä ensimmäisen kerran tunnilla 17 ja kirjaa korjauslista. Tee tunnilla 18 yksi nimetty korjaus ja toista juuri sitä koskeva testi samalla odotuksella.

### Testimatriisi

| Testi | Syöte | Odotettu tulos | Todellinen tulos | Johtopäätös |
|---|---|---|---|---|
| Normaali tapaus |  |  |  |  |
| Kielteinen testi |  |  |  |  |
| Reunatapaus |  |  |  |  |

### Nimetty korjaus ja uudelleentesti

**Havaittu puute ja tehty muutos**

[Kirjoita tähän.]

**Vertaa tulosta ennen korjausta ja sen jälkeen. Mitä vertailu kertoo korjauksen vaikutuksesta tässä testissä, ja mitä se ei vielä osoita?**

[Kirjoita tähän.]

### Reflektio, 200–300 sanaa

Kerro, mitä opit, mikä havainto johti korjaukseen ja mitä tekisit seuraavaksi. Saavutettavana vaihtoehtona voit tehdä 2–3 minuutin äänitteen tai selostetun 3–5 dian kuvakoosteen, joka vastaa samoihin kysymyksiin.

[Kirjoita tähän.]

### Esittely, 2–3 minuuttia

Kirjaa muistiin käyttäjä ja ongelma, yksi ennen–jälkeen-korjaus, yksi perusteltu rajaus sekä vastauksesi mahdolliseen jatkokysymykseen.

Esittely tehdään pienryhmässä, tallenteena tai opettajan valitsemana otoksena, ei koko luokan peräkkäisenä kierroksena.

[Kirjoita tähän.]

### Lopputarkistus

- [ ] Tekninen botti toimii rajatussa tehtävässä tai suunnittelusuoritus kuvaa toteuttamiskelpoisen rakenteen ja rajaa teknisesti todentamattomat ominaisuudet.
- [ ] Järjestelmäpromptissa on selkeä rooli, työnkulku ja rajat.
- [ ] Tietopohjassa on 2–4 perusteltua dokumenttia.
- [ ] Normaali, kielteinen ja reunatapaus sekä korjaus ja uudelleentesti on dokumentoitu.
- [ ] Reflektio ja esittely osoittavat, että ymmärrän tekemäni valinnat.

---

# Osa 3 · Agentit

Tällä kurssilla rakennettavalla tekoälyagentilla tarkoitetaan kielimallin ja sitä ohjaavan agentin ohjauskehyksen (harness) muodostamaa järjestelmää. Suunnittelun tarkistuslistaan kuuluu kuusi rakennusosaa: syötekäsittelijä, päättelijä ja suunnittelija, työkalujen suorittaja, muisti ja konteksti, turvakerros sekä seuranta ja palautesilmukka. Kaikkia niistä ei tarvitse toteuttaa jokaisessa agentissa erillisinä teknisinä osina.

**Työskentelytapa**

- [ ] Teen työn yksin
- [ ] Teen työn parin kanssa

**Parin nimi ja työnjako**

[Täytä, jos teet työn parin kanssa.]

## Pohjapiirros 1: Ongelma

Kirjoita 150–200 sanaa. Kuvaa ongelma ja käyttäjä, perustele, miksi ratkaisu tarvitsee agentin eikä tavallista automaatiota tai chatbotia, ja arvioi kuuden rakennusosan tarvetta. Perustele myös, jos jätät jonkin niistä pois.

[Kirjoita tähän.]

## Pohjapiirros 2: Muisti

Kirjoita 150–200 sanaa. Kuvaa yhden suorituksen konteksti, mahdollinen pitkäkestoinen muisti sekä prosessin tilat ja tilasiirtymät. Perustele, mitä tallennetaan, kuinka pitkäksi aikaa ja miksi. Älä sijoita agentin roolia tai toimintaohjeita muistiin.

[Kirjoita tähän.]

### Järjestelmäohjeet — erillään muistista

Kirjaa agentin tehtävä, rooli, sallitut toimintatavat ja rajat järjestelmäohjeisiin. Järjestelmäohjeet ohjaavat toimintaa, mutta eivät ole keskusteluhistoriaa, prosessin tilaa tai pitkäkestoista muistia.

[Kirjoita tähän.]

## Pohjapiirros 3: Päättely

Kirjoita 150–200 sanaa. Valitse ReAct tai eksplisiittinen työnkulku ja perustele valintasi. Kuvaa, miten päättely näkyy työnkulun rakenteessa ja lokissa. Määritä kummassakin mallissa vähintään yksi aito rajattu kielimallivalinta vähintään kahdesta sallitusta vaihtoehdosta. Anna lokiesimerkki, jossa näkyvät syöte, sallitut vaihtoehdot, mallin valinta, tulos tai virhe ja seuraava toiminto. Älä tallenna kielimallin raakaa päättelyketjua.

[Kirjoita tähän.]

## Pohjapiirros 4: Turva

Kirjoita 150–200 sanaa. Määritä, mitä agentti saa ja ei saa tehdä. Tunnista 2–3 riskiä. Kuvaa, miten validoit ja rajaat toimintaa, seuraat tapahtumia, palaudut virheistä ja määrität lokiin tallennettavat tiedot.

[Kirjoita tähän.]

## Pohjapiirros 5: Ihminen

Kirjoita 150–200 sanaa. Tunnista hyväksyntää vaativat kohdat. Jos niitä ei ole, perustele ratkaisu riskien perusteella. Jos hyväksyntäportteja on, kerro, mitä tietoja kukin portti näyttää ja missä kanavassa hyväksyntää pyydetään. Tietojen pitää riittää päätökseen noin 30 sekunnissa. Valitse jokaiselle portille varapolku siltä varalta, ettei hyväksyntäpyyntöön vastata: oletushylkäys, vain matalan riskin tilanteeseen sopiva oletushyväksyntä tai eskalointi toiselle ihmiselle.

[Kirjoita tähän.]

## Koottu suunnitelma: johdonmukaisuustarkistus

Tarkista viisi pohjapiirrosta yhtenä kokonaisuutena ennen rakentamista.

- [ ] Ongelma ja työnkulku vastaavat toisiaan.
- [ ] Muistiratkaisu noudattaa tietosuojarajauksia.
- [ ] Päättelymalli ja lokitus tukevat toisiaan.
- [ ] Turvakerros vastaa työkalujen oikeuksia ja riskejä.
- [ ] Mahdolliset hyväksyntäportit ja varapolut ovat yksiselitteisiä.

**Mitkä valinnat toistuvat kaikissa viidessä pohjapiirroksessa?**

[Kirjoita tähän.]

**Missä havaitsit ristiriidan tai aukon?**

[Kirjoita tähän.]

**Mitä päivitit ennen rakentamista?**

[Kirjoita tähän.]

## Toteutuspolun näyttö

**Lisää työnkulun linkki, JSON-vientitiedosto tai alustariippumaton suoritusjälki.**

[Kirjoita tähän.]

**Piirrä rajattu työnkulku.**

[Lisää kaavio tähän.]

Käytä niin monta vaihetta kuin tehtävän, työkalujen, turvallisuuden, hyväksynnän, lokituksen ja virhepolun näkyvä kuvaaminen vaatii. Solmujen määrä ei ratkaise, onko järjestelmä agentti. Merkitse teknisessä polussa suoritusnäkymä ja dokumentoidussa polussa todellinen mallikutsu sekä simuloidut vaiheet.

| Solmu | Tehtävä | Syöte | Tulos | Yhteys kuuteen rakennusosaan |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## Kuuden rakennusosan tarkistus

Merkitse, missä **syötekäsittelijä**, **päättelijä ja suunnittelija**, **työkalujen suorittaja**, **muisti ja konteksti**, **turvakerros** sekä **seuranta ja palautesilmukka** näkyvät tai miksi niitä ei tarvita.

[Kirjoita tähän.]

## Aito rajattu mallivalinta

| Syöte | Sallitut vaihtoehdot | Mallin todellinen valinta | Seuraava vaihe |
|---|---|---|---|
|  |  |  |  |

## Kolme testiä

| Kategoria | Syöte | Odotettu tulos | Todellinen tulos | Johtopäätös |
|---|---|---|---|---|
| Normaali |  |  |  |  |
| Reunatapaus |  |  |  |  |
| Turvallisuus |  |  |  |  |

## Yksi korjaus ja uudelleentesti

**Kirjaa alkuperäinen tulos, tehty korjaus, saman testin uusi tulos ja johtopäätös.**

[Kirjoita tähän.]

## Turvallisuusraja ja rehellinen rajoitus

**Mikä oikeus, hyväksyntä tai havaittava eskalointiehto rajaa toimintaa? Mitä työsi ei vielä todista?**

[Kirjoita tähän.]

## Puolustus, 2–3 minuuttia

Kirjaa muistiin ongelma ja toteutuspolku, aito rajattu mallivalinta, testissä havaittu puute, korjaus ja uudelleentestin tulos sekä tärkein turvallisuusraja ja rajoitus. Puolustus tehdään tunnilla pienryhmässä, tallenteena tai opettajan valitsemana otoksena.

[Kirjoita tähän.]

### Lopputarkistus

- [ ] Työnkulussa on vähintään yksi aito, rajattu kielimallin tekemä valinta, ja valitun polun näyttö vastaa sitä, mitä todella toteutin tai simuloin.
- [ ] Kuusi rakennusosaa on käsitelty kanonisilla nimillä.
- [ ] Normaali, reuna- ja turvallisuustesti on dokumentoitu.
- [ ] Yksi korjaus ja sama uudelleentesti näkyvät ennen–jälkeen-vertailuna.
- [ ] Turvallisuusraja, rajoitus ja 2–3 minuutin puolustus osoittavat, että ymmärrän kokonaisuuden.

---

# Lähteet

| Lähde tai linkki | Mitä tarkistin? | Tarkistuspäivä |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

Lisenssi: CC BY-SA 4.0. Kurssimateriaali: https://aiperusteet.fi/
