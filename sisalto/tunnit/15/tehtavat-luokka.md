# Rakennuspalikka 3 — Tietopohja ja testisuunnitelma

**Tämä on kolmas ja viimeinen rakennuspalikka.** Keräät rakennuspalikat Tekoälyjen käyttö -osion aikana. Tunnilla 17 rakennat niiden avulla apuri-botin valitsemallasi alustalla, ja tunnilla 18 korjaat sekä arvioit toteutuksen. Säilytä työ huolellisesti.

## Mitä teet?

Kuratoit bottisi **tietopohjan** eli valitset 3–5 dokumenttia, joista botti saa oman aiheesi asiantuntemusta. Tietopohja erottaa oman bottisi yleisestä tekoälystä: yleinen tekoäly tietää monesta asiasta vähän, mutta sinun bottisi keskittyy juuri sinun valitsemaasi aiheeseen.

**Kuratointi** ei tarkoita sitä, että keräät mahdollisimman paljon tiedostoja. Se tarkoittaa aktiivista valintaa: mitä otat mukaan, mitä jätät pois ja miksi. Hyvä tietopohja vastaa kysymykseen: *"Mitä botin pitää tietää, jotta se osaa auttaa käyttäjää juuri minun valitsemassani aiheessa?"*

## Tavoite

Tehtävän jälkeen sinulla on perusteltu tietopohja ja ennen rakentamista kirjoitettu testisuunnitelma. Osaat:

- tunnistaa, mitä tietoa botti tarvitsee toimiakseen hyödyllisesti,
- valita lähdedokumentteja tarkoituksenmukaisesti,
- arvioida dokumenttien luotettavuutta, ajantasaisuutta ja hyödyllisyyttä,
- karsia pois turhat tai päällekkäiset materiaalit,
- perustella, miksi kukin dokumentti kuuluu bottisi tietopohjaan.
- kirjoittaa testille syötteen, odotetun toiminnan ja läpäisyehdon.

## Mitä tallennat?

Tallenna lopuksi yksi dokumentti tai kansio, jossa on:

- lista bottisi tärkeimmistä tietotarpeista,
- 3–5 valittua lähdedokumenttia,
- taulukko, jossa perustellaan jokaisen dokumentin rooli tietopohjassa,
- lyhyt arvio siitä, mitä tietopohja kattaa hyvin ja mitä se ei vielä kata,
- yksi positiivinen testi, yksi negatiivinen testi ja yksi reunatapaus odotettuine tuloksineen,
- varsinaiset dokumentit tallennettuna samaan kansioon myöhempää toteutusta varten.

## Tee näin

### Vaihe 1 — Palauta mieleen bottisi tarkoitus

Avaa **rakennuspalikka 2** eli botin määrittelydokumentti. Katso siitä erityisesti seuraavat kohdat:

- **Kohderyhmä:** kenelle botti on tarkoitettu?
- **Tarkoitus:** mitä botti auttaa käyttäjää tekemään?
- **Työnkulku:** missä järjestyksessä botti ohjaa käyttäjää?
- **Rajat:** mitä botti ei saa tehdä?

Tämä vaihe on tärkeä, koska tietopohjan pitää tukea juuri tämän botin tarkoitusta. Älä kerää sattumanvaraisia dokumentteja vain siksi, että ne liittyvät aiheeseen yleisesti. Valitse materiaalia, joka auttaa bottia auttamaan käyttäjää **valitsemassasi tehtävässä**.

### Vaihe 2 — Listaa, mitä botin pitää tietää

Kirjoita 5–8 konkreettista **tietotarvetta**. Tietotarve tarkoittaa asiaa, joka botin pitää ymmärtää, jotta se osaa auttaa käyttäjää valitsemassasi tehtävässä.

Käytä apuna bottisi työnkulkua. Jos botti esimerkiksi ohjaa käyttäjää käymään läpi keskeiset käsitteet, harjoituskysymykset ja palautteen, sen tietopohjasta pitäisi löytyä materiaalia juuri näihin aiheisiin.

| Aihe | Esimerkkejä tietotarpeista |
| --- | --- |
| **Opiskelu** | Aiheen keskeiset käsitteet, tyypilliset väärinkäsitykset, hyvät harjoituskysymykset, esimerkkivastaukset ja kertaamisen vinkit. |
| **Harrastus tai kerho** | Säännöt, aikataulut, yleisimmät kysymykset, jäsenten vinkit ja yhteystiedot. |
| **Tuttu pieni palvelu** | Aukioloajat, palvelut ja hinnat, usein kysytyt kysymykset, ohjeet ja yhteystiedot. |
| **Pelit, musiikki tai sisältö** | Lajityypin tunnusmerkit, ideointitekniikat, rakenteen mallit, esimerkit ja palautteen periaatteet. |
| **Arjen apuri** | Suunnittelun rakenne, hyvät käytännöt, yleiset sudenkuopat, esimerkkipohjat ja seurannan tavat. |

**Mallipohja omalle listalle:**

1. Botin pitää tietää, mitkä ovat aiheen keskeiset käsitteet.
2. Botin pitää tietää, miten käyttäjän tehtävä jäsennetään selkeiksi vaiheiksi.
3. Botin pitää tietää, millaisia kysymyksiä tästä aiheesta tyypillisesti esitetään.
4. Botin pitää tietää, millaisia yleisiä virheitä tai sudenkuoppia aiheeseen liittyy.
5. Botin pitää tietää, millainen hyvä lopputulos tai vastaus näyttää.

### Vaihe 3 — Etsi ja valitse 3–5 dokumenttia

Etsi materiaalia, joka kattaa vaiheessa 2 listaamasi tietotarpeet. Valitse lopuksi **3–5 dokumenttia**. Laatu on tärkeämpää kuin määrä.

Hyviä lähteitä voivat olla:

- kurssimateriaalit, kuten oppikirjat, luentodiat tai aiemmat tehtäväpohjat,
- aiheesi yleiset standardit ja ohjeistukset,
- mallipohjat tai esimerkkidokumentit aiheesi todellisista tilanteista,
- luotettavat alan blogit, dokumentaatiot tai viralliset ohjeet,
- Wikipedia-artikkelit vain yleisen rakenteen hahmottamiseen, ei tarkkojen yksityiskohtien päälähteeksi.

**Tärkeää:** Älä lataa kaikkea, mitä löydät. Liian suuri tai sekava tietopohja voi tehdä botin vastauksista epäselviä. Kolme hyvin valittua dokumenttia voi olla parempi kuin kaksikymmentä keskinkertaista.

Arvioi jokaista dokumenttia seuraavien kysymysten avulla:

- Onko lähde luotettava?
- Onko dokumentti ajantasainen?
- Tukeeko se bottini työnkulkua?
- Auttaako se käyttäjää valitsemassasi tehtävässä?
- Onko dokumentissa konkreettinen rakenne, mallipohja tai tarkistuslista, jota botti voi hyödyntää?
- Sisältääkö dokumentti henkilötietoja, salassa pidettävää tietoa tai muuta aineistoa, jota ei saa ladata valitulle alustalle?

### Vaihe 4 — Arvioi tietopohjan kattavuus tekoälyn avulla

Avaa käytössäsi oleva hyväksytty tekoälypalvelu ja anna sille bottisi tietotarpeet sekä valitsemiesi dokumenttien turvalliset kuvaukset. Tässä vaiheessa et vielä rakenna tietopohjaa alustalle, vaan arvioit, kattaako suunnitelma oikeat asiat.

Voit käyttää esimerkiksi seuraavaa promptia:

> "Toimit minulle sparrauskumppanina. Rakennan apuri-bottia, joka auttaa käyttäjää valitsemassani aiheessa. BOTTINI TARKOITUS: [kuvaa bottisi tarkoitus lyhyesti] TIETOTARPEET: [liitä vaiheessa 2 tekemäsi lista] VALITUT DOKUMENTIT: 1. [dokumentin nimi + lyhyt kuvaus] 2. [dokumentin nimi + lyhyt kuvaus] 3. [dokumentin nimi + lyhyt kuvaus] Auta minua arvioimaan tietopohjan kattavuus: Mitä tietotarpeita dokumentit eivät kata? Onko jokin dokumentti turha tai päällekkäinen toisen kanssa? Onko aiheessa jokin tyypillinen tieto, jota en ole vielä ottanut huomioon? Onko jokin dokumentti liian yleinen tai liian vaikea kohderyhmälleni? Näetkö tietosuoja- tai luottamuksellisuusriskin siinä, että jokin dokumentti ladattaisiin bottiin? Älä ehdota uusia dokumentteja suoraan minulle. Auta tunnistamaan aukot, jotta voin etsiä lisämateriaalia itse."

Tämä on harjoitus siitä, miten tekoälyä käytetään *kattavuuden tarkistajana*. Tekoäly ei kerää tietopohjaa puolestasi, mutta se voi auttaa huomaamaan sokeita pisteitä.

### Vaihe 5 — Viimeistele tietopohja

Tee tekoälyn palautteen pohjalta tarvittavat korjaukset. Voit esimerkiksi lisätä puuttuvan dokumentin, poistaa päällekkäisen dokumentin tai vaihtaa liian yleisen lähteen parempaan.

Kokoa lopullinen tietopohja alla olevaan taulukkoon.

| Dokumentti | Lähde tai linkki | Miksi tämä kuuluu tietopohjaan? | Mitä tietotarvetta se tukee? |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Tallenna tai lataa varsinaiset dokumentit yhteen kansioon. Käytät niitä oppitunnilla 17, kun lataat tietopohjan valitsemallesi alustalle tai teet dokumentoidun kuivaharjoittelun.

Kirjoita 2–3 lauseen arvio: *"Mitä tietopohjani kattaa hyvin? Mitä se ei vielä kata täydellisesti? Mitä botin pitää tehdä silloin, kun vastausta ei löydy?"*

### Vaihe 6 — Kirjoita testit ennen rakentamista

Kirjoita kolme testiä, jotka ajat ensimmäisen kerran tunnilla 17:

| Testityyppi | Syöte | Odotettu toiminta | Läpäisyehto |
| --- | --- | --- | --- |
| Positiivinen testi | Kysymys, johon tietopohja vastaa |  |  |
| Negatiivinen testi | Pyyntö, josta botin pitää kieltäytyä tai jonka se ohjaa eteenpäin |  |  |
| Reunatapaus | Tyhjä, sekava tai muuten epätavallinen syöte |  |  |

Älä muuta odotettua toimintaa myöhemmin vain siksi, että botti vastaa eri tavalla. Testin tehtävä on paljastaa korjaustarve, ei todistaa ensimmäistä versiota onnistuneeksi.

> **Miksi tämä on tärkeää:** Tietopohja erottaa aiheeseen rajatun botin yleisestä tekoälypalvelusta. Kuratoitujen dokumenttien avulla botti voi vastata juuri oman aiheesi käytäntöjen perusteella.

> **Tarkista lopuksi:** Olet palauttanut mieleen bottisi tarkoituksen, listannut 5–8 tietotarvetta, valinnut 3–5 dokumenttia, arvioinut kattavuuden, kirjannut aukot, laatinut kolme testiä odotuksineen ja tallentanut dokumentit myöhempää käyttöä varten.

**3 / 3 rakennuspalikkaa kerätty — valmis tuntiin 17**
