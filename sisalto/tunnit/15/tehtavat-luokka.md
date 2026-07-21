# Rakennuspalikka 3 — Tietopohja ja testisuunnitelma

**Tämä on kolmas ja viimeinen rakennuspalikka.** Keräät rakennuspalikat Tekoälyjen käyttö -osion aikana. Tunnilla 17 rakennat niiden avulla apuri-botin valitsemallasi alustalla, ja tunnilla 18 korjaat sekä arvioit toteutuksen. Säilytä työ huolellisesti.

## Mitä teet?

Kuratoit bottisi **tietopohjan** eli valitset 2–4 huolella valittua dokumenttia, joihin sen vastaukset voivat nojata. Tietopohjan tehtävä ei ole tehdä botista kaikkitietävää, vaan auttaa sitä toimimaan luotettavasti juuri valitsemassasi aiheessa.

**Kuratointi** ei tarkoita mahdollisimman suuren tiedostomäärän keräämistä. Se on aktiivista valintaa: mitä otat mukaan, mitä jätät pois ja miksi. Kun jokaisella lähteellä on selvä tehtävä, sinun on myöhemmin helpompi havaita myös se, mitä tietopohja ei vielä kata. Pidä työn ajan mielessä kysymys: *”Mitä botin pitää tietää, jotta se osaa auttaa käyttäjää juuri minun valitsemassani aiheessa?”*

## Tavoite

Tehtävän jälkeen sinulla on perusteltu tietopohja ja ennen rakentamista kirjoitettu testisuunnitelma. Osaat:

- tunnistaa, mitä tietoa botti tarvitsee toimiakseen hyödyllisesti,
- valita lähdedokumentteja tarkoituksenmukaisesti,
- arvioida dokumenttien luotettavuutta, ajantasaisuutta ja hyödyllisyyttä,
- karsia pois turhat tai päällekkäiset materiaalit,
- perustella, miksi kukin dokumentti kuuluu bottisi tietopohjaan,
- kirjoittaa testille syötteen, odotetun toiminnan ja läpäisyehdon,
- erottaa haun onnistumisen siitä, muodostiko kielimalli lähteen tukeman vastauksen,
- rajata, mitä aineistoa eri käyttäjät saavat hakea.

## Mitä tallennat?

Tallenna lopuksi yksi dokumentti tai kansio, jossa on:

- lista bottisi tärkeimmistä tietotarpeista,
- 2–4 valittua lähdedokumenttia,
- taulukko, jossa perustellaan jokaisen dokumentin rooli tietopohjassa,
- lyhyt arvio siitä, mitä tietopohja kattaa hyvin ja mitä se ei vielä kata,
- yksi positiivinen testi, yksi negatiivinen testi ja yksi reunatapaus odotettuine tuloksineen,
- varsinaiset dokumentit tallennettuna samaan kansioon myöhempää toteutusta varten.

## Tee näin

### Vaihe 1 — Palauta mieleen bottisi tarkoitus

Avaa **rakennuspalikka 2** eli botin määrittelydokumentti. Lue siitä uudelleen:

- **kohderyhmä:** kenelle botti on tarkoitettu
- **tarkoitus:** mitä se auttaa käyttäjää tekemään
- **työnkulku:** missä järjestyksessä se ohjaa tehtävää
- **rajat:** mitä se ei saa tehdä.

Nämä neljä asiaa antavat tietopohjalle suunnan.

Älä siis kerää dokumentteja vain siksi, että ne liittyvät aiheeseen yleisesti. Valitse aineistoa, joka auttaa juuri sinun käyttäjääsi juuri siinä tehtävässä, jonka olet botille määritellyt. Jos lähteen yhteys tähän tehtävään jää epäselväksi, jätä se ainakin toistaiseksi pois.

### Vaihe 2 — Listaa, mitä botin pitää tietää

Kirjoita 5–8 konkreettista **tietotarvetta**. Tietotarve tarkoittaa asiaa, joka botin pitää ymmärtää, jotta se osaa auttaa käyttäjää valitsemassasi tehtävässä.

Käytä apuna bottisi työnkulkua. Kulje se mielessäsi vaihe vaiheelta ja kysy jokaisessa kohdassa, mitä botin täytyy tietää jatkaakseen. Jos botti esimerkiksi auttaa opiskelijaa kertaamaan käsitteet, harjoittelemaan ja tulkitsemaan palautetta, tietopohjasta pitää löytyä aineistoa kaikkiin näihin vaiheisiin.

| Aihe | Esimerkkejä tietotarpeista |
| --- | --- |
| **Opiskelu** | Aiheen keskeiset käsitteet, tyypilliset väärinkäsitykset, hyvät harjoituskysymykset, esimerkkivastaukset ja kertaamisen vinkit. |
| **Harrastus tai kerho** | Säännöt, aikataulut, yleisimmät kysymykset, jäsenten vinkit ja yhteystiedot. |
| **Tuttu pieni palvelu** | Aukioloajat, palvelut ja hinnat, usein kysytyt kysymykset, ohjeet ja yhteystiedot. |
| **Pelit, musiikki tai sisältö** | Lajityypin tunnusmerkit, ideointitekniikat, rakenteen mallit, esimerkit ja palautteen periaatteet. |
| **Arjen apuri** | Suunnittelun rakenne, hyvät käytännöt, yleiset sudenkuopat, esimerkkipohjat ja seurannan tavat. |

Voit aloittaa jokaisen tarpeen samalla rungolla: ”Botin pitää tietää…”. Kirjoita sen jälkeen mahdollisimman täsmällisesti esimerkiksi aiheen keskeinen käsite, tehtävän yksi vaihe, tyypillinen kysymys, tavallinen sudenkuoppa tai hyvän lopputuloksen tunnusmerkki. Mitä tarkemmin nimeät tarpeen, sitä helpompi lähteen sopivuutta on arvioida.

### Vaihe 3 — Etsi ja valitse 2–4 dokumenttia

Etsi materiaalia, joka kattaa vaiheessa 2 nimeämäsi tietotarpeet, ja valitse lopuksi **2–4 dokumenttia**. Laatu on tärkeämpää kuin määrä. Käyttökelpoinen lähde voi olla kurssimateriaali, virallinen ohje, alan standardi, luotettava dokumentaatio tai todelliseen tilanteeseen tehty mallipohja. Yleislähteestä voi olla apua aiheen hahmottamisessa, mutta tarkkojen käytäntöjen päälähteeksi tarvitset aineiston, jonka alkuperä ja ajantasaisuus voidaan osoittaa.

**Tärkeää:** Älä lataa kaikkea, mitä löydät. Liian suuri tai sekava tietopohja voi tehdä botin vastauksista epäselviä. Kolme hyvin valittua dokumenttia voi olla parempi kuin kaksikymmentä keskinkertaista.

Käy jokainen ehdokas läpi seuraavien kysymysten avulla. Kysymykset ovat tässä vaiheessa tarpeellinen tarkistuslista, sillä yhdenkin kohdan unohtaminen voi heikentää koko tietopohjaa:

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

Tämä on harjoitus siitä, miten tekoälyä käytetään *kattavuuden tarkistajana*. Se voi nostaa esiin aukon tai ristiriidan, mutta se ei tunne lähteiden todellista laatua eikä päätä, mitä saat ladata palveluun. Sinä teet lopulliset valinnat ja pystyt perustelemaan ne.

### Vaihe 5 — Viimeistele tietopohja

Tee palautteen pohjalta vain sellaiset korjaukset, jotka pystyt itse perustelemaan. Saatat lisätä puuttuvan dokumentin, poistaa päällekkäisen aineiston tai vaihtaa liian yleisen lähteen täsmällisempään. Jos palautteen ehdotus ei sovi määrittelemääsi tehtävään, sitä ei tarvitse noudattaa.

Kokoa lopullinen tietopohja alla olevaan taulukkoon.

| Dokumentti | Lähde tai linkki | Miksi tämä kuuluu tietopohjaan? | Mitä tietotarvetta se tukee? |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Tallenna varsinaiset dokumentit yhteen kansioon. Käytät niitä oppitunnilla 17, kun kytket tietopohjan valitsemallesi alustalle tai kuvaat dokumentoidulla suunnittelupolulla haun, lähdekatkelmat ja käyttöoikeusrajauksen.

Kirjaa samalla, miten aineisto tulee botin käyttöön. Jos alusta hakee kysymykseen sopivia katkelmia ennen vastausta, kyse on RAG-toteutuksesta. Merkitse jokaiselle lähteelle myös, kuka saa käyttää sitä. Jos lähde on tarkoitettu vain tietylle ryhmälle, teknisen toteutuksen pitää rajata se pois muiden käyttäjien hausta. Dokumentoidussa suunnittelupolussa kuvaat tämän rajauksen suunnitelmana etkä väitä testanneesi todellisia käyttöoikeuksia.

Kirjoita 2–3 lauseen arvio: *"Mitä tietopohjani kattaa hyvin? Mitä se ei vielä kata täydellisesti? Mitä botin pitää tehdä silloin, kun vastausta ei löydy?"*

### Vaihe 6 — Kirjoita testit ennen rakentamista

Kirjoita kolme testiä, jotka ajat ensimmäisen kerran tunnilla 17:

| Testityyppi | Syöte | Odotettu toiminta | Mitä tarkistat hausta? | Läpäisyehto vastaukselle |
| --- | --- | --- | --- | --- |
| Positiivinen testi | Kysymys, johon tietopohja vastaa |  | Löytyykö oikea lähde? |  |
| Negatiivinen testi | Pyyntö, josta botin pitää kieltäytyä tai jonka se ohjaa eteenpäin |  | Pääseekö haku vain käyttäjälle sallittuihin lähteisiin? |  |
| Reunatapaus | Tyhjä, sekava tai muuten epätavallinen syöte |  | Käynnistyykö haku vain tarvittaessa? |  |

Kirjoita odotus niin täsmällisesti, että toinen ihminen voisi ratkaista sen perusteella, läpäisikö botti testin. Älä myöhemmin muuta odotettua toimintaa vain siksi, että botti vastaa eri tavalla. Testin tehtävä on paljastaa korjaustarve, ei todistaa ensimmäistä versiota onnistuneeksi.

> **Miksi tämä on tärkeää:** Tietopohja antaa aiheeseen rajatulle botille perustan, jota yleisellä kielimallilla ei ole. Kun lähteet on valittu tehtävän mukaan ja niiden aukot tunnetaan, botti voi nojata oman aiheesi käytäntöihin arvaamisen sijaan.

> **Tarkista lopuksi:** Olet palauttanut mieleen bottisi tarkoituksen, listannut 5–8 tietotarvetta, valinnut 2–4 dokumenttia, arvioinut kattavuuden, kirjannut aukot, laatinut kolme testiä odotuksineen ja tallentanut dokumentit myöhempää käyttöä varten.

**3 / 3 rakennuspalikkaa kerätty — valmis tuntiin 17**
