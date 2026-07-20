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

## Todistusaineisto 3: Vastuullisen käyttäjän tarkistuslista

Tee kaksi hallusinaatiokoetta tunnilla 7. Tarkista kummankin vastaus luotettavasta lähteestä.

### Hallusinaatiokoe 1

**Kysymys ja mallin vastaus**

[Kirjoita tähän.]

**Tarkistuslähde ja oikea vastaus**

[Kirjoita tähän.]

**Mistä hallusinaation saattoi tunnistaa?**

[Kirjoita tähän.]

### Hallusinaatiokoe 2

**Kysymys ja mallin vastaus**

[Kirjoita tähän.]

**Tarkistuslähde ja oikea vastaus**

[Kirjoita tähän.]

**Mistä hallusinaation saattoi tunnistaa?**

[Kirjoita tähän.]

### Oma tarkistuslista, noin 250–300 sanaa

**Kirjaa 3–5 hallusinaation tuntomerkkiä.**

[Kirjoita tähän.]

**Selitä 2–3 lauseella, miksi kielimalli voi hallusinoida.**

[Kirjoita tähän.]

**Kirjoita 5–7 vaihetta, jotka käyt läpi ennen kuin luotat vastaukseen.**

[Kirjoita tähän.]

## Teoria-osion lopputyö

Valitse kirjallinen tai visuaalis-suullinen suoritustapa. Käytä vähintään kahta todistusaineistoa; kaikkien kolmen käyttäminen on suositeltavaa.

**Valitse suoritustapa.**

- [ ] Kirjallinen asiantuntijalausunto, 750–1000 sanaa
- [ ] Tilannekartta ja päätöspuu sekä 5–8 minuutin suullinen esitys

**Valitse skenaario.**

- [ ] Asiakaspalvelu ja tietovuoto
- [ ] Rekrytointialgoritmi ja syrjintä
- [ ] Markkinointisisältö ja tekijänoikeudet

**Kirjaa keskeiset riskit ja käsitteet.**

[Kirjoita tähän.]

**Nimeä käyttämäsi todistusaineistot ja lähteet.**

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

**4. Mikä on asiallinen vastuu? Kerro, kuka vastaa mistä ja miksi.**

[Kirjoita tähän.]

### Kirjallinen suoritustapa

**Lisää luonnos ja valmis asiantuntijalausunto linkkeinä tai liitteinä.**

[Kirjoita tähän tai lisää linkki tai liite.]

### Visuaalis-suullinen suoritustapa

**Tallenna tilannekartta.**

[Lisää linkki tai liite.]

**Tallenna päätöspuu.**

[Lisää linkki tai liite.]

**Tallenna 5–8 minuutin esityksen muistiinpanot tai nauhoite.**

[Kirjoita tähän tai lisää linkki tai liite.]

### Korjausloki — vähintään kolme korjausta

| Ennen | Jälkeen | Miksi korjasin? | Lähde tai käsite |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

**Kirjoita kirjallisen suoritustavan 2–3 minuutin puolustuksen muistiinpanot.**

[Kirjoita tähän.]

### Lopputarkistus

- [ ] Käytän käsitteitä täsmällisesti ja sovellan niitä tilanteeseen.
- [ ] Hyödynnän vähintään kahta todistusaineistoa.
- [ ] Ehdotan konkreettisia toimenpiteitä: kuka tekee, mitä tekee ja milloin.
- [ ] Tuotos on selkeä ja asiallinen, ja sen väitteet ovat perusteltuja.
- [ ] Käsittelen vastuukysymyksen omana osanaan.

---

# Osa 2 · Tekoälyjen käyttö

## Rakennuspalikka 1: Promptauspankki

Laadi tunnilla 12 yhteensä 5–7 promptikorttia. Tässä pohjassa on tilaa viidelle kortille. Kopioi korttipohja, jos tarvitset lisää.

### Promptikortti 1

**Nimeä prompti tai käyttötilanne.**

[Kirjoita tähän.]

**Kirjoita ensimmäinen versio kokonaisuudessaan.**

[Kirjoita tähän.]

**Mikä vastauksessa toimi? Mitä piti täsmentää?**

[Kirjoita tähän.]

**Kirjoita viimeistelty prompti kokonaisuudessaan.**

[Kirjoita tähän.]

**Mihin prompti sopii ja mihin se ei sovi?**

[Kirjoita tähän.]

### Promptikortti 2

**Nimeä prompti tai käyttötilanne.**

[Kirjoita tähän.]

**Kirjoita ensimmäinen versio kokonaisuudessaan.**

[Kirjoita tähän.]

**Mikä vastauksessa toimi? Mitä piti täsmentää?**

[Kirjoita tähän.]

**Kirjoita viimeistelty prompti kokonaisuudessaan.**

[Kirjoita tähän.]

**Mihin prompti sopii ja mihin se ei sovi?**

[Kirjoita tähän.]

### Promptikortti 3

**Nimeä prompti tai käyttötilanne.**

[Kirjoita tähän.]

**Kirjoita ensimmäinen versio kokonaisuudessaan.**

[Kirjoita tähän.]

**Mikä vastauksessa toimi? Mitä piti täsmentää?**

[Kirjoita tähän.]

**Kirjoita viimeistelty prompti kokonaisuudessaan.**

[Kirjoita tähän.]

**Mihin prompti sopii ja mihin se ei sovi?**

[Kirjoita tähän.]

### Promptikortti 4

**Nimeä prompti tai käyttötilanne.**

[Kirjoita tähän.]

**Kirjoita ensimmäinen versio kokonaisuudessaan.**

[Kirjoita tähän.]

**Mikä vastauksessa toimi? Mitä piti täsmentää?**

[Kirjoita tähän.]

**Kirjoita viimeistelty prompti kokonaisuudessaan.**

[Kirjoita tähän.]

**Mihin prompti sopii ja mihin se ei sovi?**

[Kirjoita tähän.]

### Promptikortti 5

**Nimeä prompti tai käyttötilanne.**

[Kirjoita tähän.]

**Kirjoita ensimmäinen versio kokonaisuudessaan.**

[Kirjoita tähän.]

**Mikä vastauksessa toimi? Mitä piti täsmentää?**

[Kirjoita tähän.]

**Kirjoita viimeistelty prompti kokonaisuudessaan.**

[Kirjoita tähän.]

**Mihin prompti sopii ja mihin se ei sovi?**

[Kirjoita tähän.]

### Promptauspankin yhteenveto

Kuvaa 3–5 lauseella rakenteet, jotka toimivat toistuvasti eri prompteissa.

[Kirjoita tähän.]

**Mikä promptikortti liittyy tulevan botin aiheeseen? Miten käytät sitä järjestelmäpromptin raaka-aineena?**

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

## Rakennuspalikka 3: Tietopohja

**Kirjaa 5–8 tietotarvetta, joihin botin pitää osata vastata.**

[Kirjoita tähän.]

| Dokumentti | Lähde tai linkki | Miksi mukana? | Mitä tietotarvetta se tukee? | Luotettavuus ja ajantasaisuus | Tietosuoja tai käyttöoikeus |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

**Mitä tietopohja kattaa hyvin? Mitä se ei vielä kata?**

[Kirjoita tähän.]

Kirjaa näkyviin myös puuttuva tieto: milloin botin pitää sanoa, ettei tietopohja riitä vastaukseen?

**Tietopohjan kansio tai tallennuspaikka**

[Kirjoita tähän.]

- [ ] Tietopohjan 3–5 varsinaista lähdedokumenttia on tallennettu samaan kansioon, ja niiden nimet vastaavat taulukkoa.

## Apuri-botin lopputyö

Voit käyttää valitsemaasi alustaa tai tehdä dokumentoidun kuivaharjoittelun.

**Valitse toteutustapa.**

- [ ] Toimiva botti
- [ ] Dokumentoitu kuivaharjoittelu

**Lisää linkki toteutukseen tai kuivaharjoittelun suoritusjälki.**

Kuivaharjoittelun suoritusjäljessä pitää näkyä järjestelmäprompti, käyttäjän syötteet, vastaukset ja odotetut työkaluvaiheet.

[Kirjoita tähän.]

**Liitä päivitetty botin määrittely.**

[Kirjoita tähän tai lisää linkki tai liite.]

**Kirjoita järjestelmäprompti kokonaisuudessaan.**

[Kirjoita tähän.]

**Nimeä tietopohjan 3–5 dokumenttia ja perustele valinnat.**

[Kirjoita tähän.]

> **Tarkista ennen testausta.** Varmista, että järjestelmäprompti, botin määrittely ja tietopohja ovat keskenään johdonmukaisia. Korjaa ristiriidat ennen testien ajamista.

### Testimatriisi

| Testi | Syöte | Odotettu tulos | Todellinen tulos | Johtopäätös |
|---|---|---|---|---|
| Normaali tapaus |  |  |  |  |
| Kielteinen testi |  |  |  |  |
| Reunatapaus |  |  |  |  |

### Nimetty korjaus ja uudelleentesti

**Havaittu puute ja tehty muutos**

[Kirjoita tähän.]

**Vertaa tulosta ennen korjausta ja sen jälkeen. Mitä päätät vertailun perusteella?**

[Kirjoita tähän.]

### Reflektio, 200–300 sanaa

Kerro, mitä opit, mikä toimi heti, mikä vaati useita yrityksiä ja mitä tekisit seuraavalla kerralla toisin.

[Kirjoita tähän.]

### Esittely, 2–3 minuuttia

Kirjaa muistiin käyttäjä ja ongelma, yksi ennen–jälkeen-korjaus, yksi perusteltu rajaus sekä vastauksesi mahdolliseen jatkokysymykseen.

[Kirjoita tähän.]

### Lopputarkistus

- [ ] Botti toimii rajatussa tehtävässä tai kuivaharjoittelu todentaa työnkulun.
- [ ] Järjestelmäpromptissa on selkeä rooli, työnkulku ja rajat.
- [ ] Tietopohjassa on 3–5 perusteltua dokumenttia.
- [ ] Normaali, kielteinen ja reunatapaus sekä korjaus ja uudelleentesti on dokumentoitu.
- [ ] Reflektio ja esittely osoittavat, että ymmärrän tekemäni valinnat.

---

# Osa 3 · Agentit

Tällä kurssilla agentti = kielimalli + harness. Suunnittelun tarkistuslistaan kuuluu kuusi rakennusosaa: syötekäsittelijä, päättelijä ja suunnittelija, työkalujen suorittaja, muisti ja konteksti, turvakerros sekä seuranta ja palautesilmukka. Kaikkia niistä ei tarvitse toteuttaa jokaisessa agentissa erillisinä teknisinä osina.

**Työskentelytapa**

- [ ] Teen työn yksin
- [ ] Teen työn parin kanssa

**Parin nimi ja työnjako**

[Täytä, jos teet työn parin kanssa.]

## Pohjapiirros 1: Ongelma

Kirjoita 150–200 sanaa. Kuvaa ongelma ja käyttäjä, perustele, miksi ratkaisu tarvitsee agentin eikä tavallista automaatiota tai chatbotia, ja arvioi kuuden rakennusosan tarvetta. Perustele myös, jos jätät jonkin niistä pois.

[Kirjoita tähän.]

## Pohjapiirros 2: Muisti

Kirjoita 150–200 sanaa. Kuvaa lyhytaikainen muisti, mahdollinen pitkäkestoinen muisti, tilat ja tilasiirtymät sekä agentin identiteetti.

[Kirjoita tähän.]

## Pohjapiirros 3: Päättely

Kirjoita 150–200 sanaa. Valitse ReAct tai eksplisiittinen työnkulku ja perustele valintasi. Kuvaa, miten päättely näkyy työnkulun rakenteessa ja lokissa. Anna yksi lokiesimerkki, jossa näkyvät lyhyt päätösperustelu, rakenteinen työkalukutsu, tulos tai virhe ja seuraava toiminto. Älä tallenna kielimallin raakaa päättelyketjua.

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

## Toteutus ja dokumentaatio

**Lisää työnkulun linkki, JSON-vientitiedosto tai alustariippumaton suoritusjälki.**

[Kirjoita tähän.]

**Piirrä 3–5 solmun työnkulku.**

[Lisää kaavio tähän.]

| Solmu | Tehtävä | Syöte | Tulos | Yhteys kuuteen rakennusosaan |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

### README, ½–1 sivu

Kuvaa, mitä agentti tekee, kenelle se on tarkoitettu, miten sitä käytetään, 2–3 esimerkkiä sekä olennaiset rajoitukset.

[Kirjoita tähän.]

### ARCHITECTURE, ½–1 sivu

Kuvaa solmut järjestyksessä. Kerro jokaisen tehtävä, syöte ja tulos sekä yhteys agentin kuuteen rakennusosaan.

[Kirjoita tähän.]

### SAFETY, ½–1 sivu

Kuvaa 3–5 riskiä sekä niiden hallintakeinot ja lokitus. Nimeä lisäksi kohdat, joissa tarvitaan ihmisen hyväksyntä.

[Kirjoita tähän.]

Kytke jokainen riski konkreettiseen hallintakeinoon. Nimeä myös tilanne, jossa agentti pysähtyy ja eskaloi asian ihmiselle.

## Testiraportti

Dokumentoi yhdeksän testiä: kolme normaalia tapausta, kolme reunatapausta ja kolme turvallisuustestiä.

| Nro ja nimi | Kategoria | Syöte | Odotettu tulos | Todellinen tulos | Tila ja huomiot |
|---|---|---|---|---|---|
| 1 | Normaali |  |  |  |  |
| 2 | Normaali |  |  |  |  |
| 3 | Normaali |  |  |  |  |
| 4 | Reunatapaus |  |  |  |  |
| 5 | Reunatapaus |  |  |  |  |
| 6 | Reunatapaus |  |  |  |  |
| 7 | Turvallisuus |  |  |  |  |
| 8 | Turvallisuus |  |  |  |  |
| 9 | Turvallisuus |  |  |  |  |

### Vähintään kaksi uudelleentestiä

**Kirjaa havaittu puute, tehty korjaus, aiempi tulos, uusi tulos ja johtopäätös.**

[Kirjoita tähän.]

## Vertaisarviointi

Kirjaa yksi vahvuus, kaksi kehittämiskohdetta ja kaksi konkreettista parannusehdotusta. Kerro lopuksi, mitä muutit palautteen perusteella. Jos teet työn yksin, voit pyytää tekoälyltä kriittisen arvion.

[Kirjoita tähän.]

## Itsearviointi, 300–400 sanaa

Kuvaa onnistumiset, epäonnistumiset, opitut asiat ja parannusideat. Arvioi lisäksi, mikä kuudesta rakennusosasta toteutuu vahvimmin ja mikä kaipaa eniten kehittämistä.

[Kirjoita tähän.]

## Esittely, 3–5 minuuttia

Kirjaa muistiin, miten näytät agentin toiminnassa 2–3 normaalilla syötteellä ja esittelet arkkitehtuurin, kuuden rakennusosan toteutumisen, turvakerroksen sekä vähintään yhden korjauksen vaikutuksen. Päätä esittely kriittiseen arvioon: mikä onnistui ja mikä ei.

[Kirjoita tähän.]

### Lopputarkistus

- [ ] 3–5 solmun työnkulku toimii tai suoritusjälki todentaa sen.
- [ ] Turvakerros, lokitus ja riskit on kuvattu.
- [ ] README, ARCHITECTURE ja SAFETY ovat selkeitä.
- [ ] Testiraportissa on yhdeksän testiä ja vähintään kaksi uudelleentestiä.
- [ ] Itsearviointi ja esittely osoittavat, että ymmärrän kokonaisuuden.

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
