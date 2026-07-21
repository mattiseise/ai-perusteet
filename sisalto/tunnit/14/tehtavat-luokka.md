# Rakennuspalikka 2 — Botin määrittelydokumentti

**Tämä on toinen kolmesta rakennuspalikasta.** Keräät rakennuspalikat Tekoälyjen käyttö -osion aikana. Apuri-botin rakennustunnilla rakennat niiden avulla apuri-botin valitsemallasi alustalla, ja Apuri-botin viimeistelytunnilla korjaat sekä arvioit toteutuksen. Säilytä työ huolellisesti.

## Mitä teet?

Suunnittelet bottisi **määrittelydokumentin**. Se on botin perustamisasiakirja, jossa kerrot, kenelle botti on tarkoitettu, mitä se tekee, miten se käyttäytyy ja mitä se ei tee.

Tämä on ensimmäinen rakennuspalikka, jossa suunnittelet suoraan tulevaa bottiasi. Aiemmin keräsit yleisiä promptirakenteita. Nyt suunnittelet juuri sitä bottia, jonka rakennat oppitunneilla 17–18.

Et vielä kirjoita **järjestelmäpromptia**, rakenna bottia tai testaa sitä. Tässä tehtävässä suunnittelet botin toiminnan etukäteen. Ajattele tätä pohjapiirroksena: hyvä suunnitelma helpottaa botin rakentamista myöhemmin.

Määrittelyn osat liittyvät toisiinsa. Käyttäjä ja hänen tilanteensa ratkaisevat tehtävän. Tehtävästä seuraa havaittava onnistuminen, ja onnistuminen määrää, millainen keskustelun eteneminen tarvitaan. Rajat puolestaan kertovat, milloin botti ei voi viedä käyttäjää turvallisesti eteenpäin omin voimin.

## Tavoite

Tehtävän jälkeen sinulla on selkeä määrittelydokumentti, jonka avulla osaat myöhemmin rakentaa botin valitsemallasi alustalla. Dokumentti auttaa sinua päättämään:

- mihin aiheeseen ja kohderyhmälle botti rakennetaan,
- mitä tehtävää botti auttaa käyttäjää tekemään,
- millaisella äänensävyllä botti toimii,
- missä järjestyksessä botti ohjaa käyttäjää,
- mitä botin ei pidä tehdä.

Tavoitteena ei ole täyttää mahdollisimman monta kenttää, vaan muodostaa yksi johdonmukainen kuva tulevasta botista. Jos työnkulku lupaa jotakin, jota tarkoitus ei vaadi, tai rajat estävät ydintehtävän kokonaan, palaa aiempaan päätökseen ja korjaa ristiriita.

## Mitä tallennat?

Tallenna lopuksi yksi dokumentti, jossa on:

- valitsemasi apuri-botin aihe,
- täytetty botin määrittelydokumentti,
- tekoälyltä saamasi sparraus tai tiivistelmä siitä,
- viimeistelty versio määrittelystä,
- 2–3 lauseen pohdinta siitä, mikä muuttui sparrauksen jälkeen ja mikä on bottisi ydin.

Säilytä myös ensimmäinen versio tai merkitse muutokset näkyviin. Lopullinen määrittely kertoo, mitä aiot rakentaa. Muutosjälki kertoo, mitä palautteen avulla havaitsit ja minkä päätöksen teit itse.

## Tee näin

### Vaihe 1 — Valitse apuri-bottisi tarkoitus ja aihe

Botti, jonka rakennat myöhemmin, on sinun itse valitsemasi **apuri-botti**: se auttaa sinua tai kavereitasi jossakin sinulle tutussa arjen aiheessa. Valitse ensin, mihin aiheeseen ja mitä tehtävää varten botti rakennetaan.

Valitse itseäsi kiinnostava, omasta arjestasi tuttu aihe. Esimerkkejä:

- **Opiskelu** (esim. selittää käsitteitä, jäsentää tehtäviä, toimii harjoittelukaverina kokeisiin)
- **Harrastus tai kerho** (esim. säännöt, aikataulut, vinkit ja FAQ jäsenille)
- **Tuttu pieni palvelu** (esim. kahvilan, kirjaston tai urheiluseuran FAQ-botti)
- **Pelit, musiikki tai sisältö** (esim. auttaa ideoimaan pelin, biisin tai videon)
- **Arjen apuri** (esim. auttaa suunnittelemaan treenirutiinin tai viikkoaikataulun)

Rajaa aihe heti käyttäjän tilanteeksi. ”Opiskelubotti” voi muuttua esimerkiksi kertauskaveriksi, joka auttaa ensimmäisen vuoden opiskelijaa tunnistamaan yhden kurssin keskeiset käsitteet ennen koetta. Jälkimmäisestä voidaan jo päätellä, mitä botin pitää kysyä, millaista aineistoa se tarvitsee ja mistä onnistuminen näkyy.

**Tallenna:** Kirjoita valitsemasi aihe muistiin. Lisää myös yksi lause siitä, missä tilanteessa ja kenelle tällainen apuri-botti olisi hyödyllinen.

### Vaihe 2 — Täytä botin määrittelydokumentti

Täytä alla oleva taulukko. Kirjoita jokaiseen kohtaan lyhyt mutta selkeä vastaus. Tämä taulukko on bottisi suunnittelun perusta: sen myöhempi käyttäytyminen rakentuu näiden valintojen varaan.

**Vinkki:** Kirjoita mieluummin konkreettisesti kuin yleisesti. Esimerkiksi *"auttaa kerhon uutta jäsentä löytämään vastaukset yleisimpiin kysymyksiin"* on parempi kuin *"auttaa harrastuksessa"*.

Täytä taulukko ylhäältä alas ja lue se sen jälkeen kokonaisena kertomuksena käyttäjän matkasta. Kohderyhmä perustelee tarkoituksen, tarkoitus ohjaa työnkulkua ja työnkulku tekee rajat näkyviksi. Jos yhteys katkeaa, älä paikkaa sitä uusilla ominaisuuksilla, vaan tarkenna aiempaa päätöstä.

| Osa | Mitä siihen kirjoitetaan? | Oma vastauksesi |
| --- | --- | --- |
| **Botin nimi** | Anna botille nimi, joka kertoo selvästi, mitä botti tekee. Nimen ei tarvitse olla nokkela, vaan ymmärrettävä. Esimerkiksi *"Kokeisiin valmistautumisen apuri"* tai *"Kerhon FAQ-botti"*. |  |
| **Kohderyhmä** | Kenelle botti on tarkoitettu? Onko käyttäjä aloittelija vai kokeneempi? Onko hän opiskelija, harrastaja tai palvelun käyttäjä? Esimerkiksi: *"Lukiolainen, joka tarvitsee tukea kokeisiin kertaamisessa."* |  |
| **Tarkoitus** | Mitä konkreettista botti auttaa käyttäjää tekemään? Kirjoita 1–2 lausetta. Esimerkiksi: *"Botti auttaa käyttäjää valmistautumaan kokeeseen käymällä läpi keskeiset käsitteet, esittämällä harjoituskysymyksiä ja antamalla palautetta vastauksista."* |  |
| **Persoona ja äänensävy** | Millainen botti on luonteeltaan? Miten se puhuu käyttäjälle? Esimerkiksi: *"Kannustava harjoittelukaveri, joka kysyy tarkentavia kysymyksiä. Puhuu rennosti mutta selkeästi. Ei käytä turhaa jargonia eikä ole liian leikkisä."* |  |
| **Työnkulku** | Missä järjestyksessä botti ohjaa käyttäjää? Kirjoita 5–7 vaiheen runko. Voit käyttää pohjana rakennetta: **aiheen valinta → lähtötaso → keskeiset käsitteet → harjoituskysymykset → palaute → seuraava askel**. Muokkaa rakennetta oman aiheesi mukaan. |  |
| **Rajat — mitä botti ei tee** | Listaa 3–5 asiaa, joita botti ei saa tehdä. Esimerkiksi: *"Botti ei tee tehtäviä käyttäjän puolesta. Botti ei anna lääketieteellisiä tai oikeudellisia neuvoja. Botti ei keksi faktoja, joita se ei tiedä. Botti ei käsittele oman aiheensa ulkopuolisia asioita."* Rajat tekevät botista luotettavamman. |  |

Esimerkiksi kerhon perehdytysbotin kokonaisuus voi edetä näin: uusi jäsen kysyy ensimmäisestä harjoituksesta, botti tarkistaa aiheen ja tarvittavan lähtötiedon, hakee harjoitusajan hyväksytystä aineistosta ja kertoo varusteet sekä seuraavan askeleen. Jos ajantasainen aika puuttuu, botti kertoo puutteen ja ohjaa nimetylle yhteyshenkilölle. Tässä tarkoitus, työnkulku, tietotarve ja raja tukevat samaa käyttäjän tehtävää.

### Vaihe 3 — Haasta määrittelysi tekoälyn avulla

Avaa käytössäsi oleva hyväksytty tekoälypalvelu ja anna sille koko määrittelydokumenttisi. Pyydä tekoälyä haastamaan suunnitelmaasi. Tarkoitus ei ole, että tekoäly suunnittelee botin puolestasi, vaan että se auttaa huomaamaan puutteita ja epäselvyyksiä.

Voit käyttää esimerkiksi seuraavaa promptia:

> "Toimit minulle sparrauskumppanina. Suunnittelen apuri-bottia, joka auttaa käyttäjää valitsemassani arjen aiheessa. Tässä bottini määrittelydokumentti: [liitä koko taulukkosi tähän] Haasta suunnitelmaani. Pohdi erityisesti: Onko botin tarkoitus tarpeeksi konkreettinen vai jääkö se liian yleiseksi? Onko kohderyhmä riittävän tarkasti rajattu? Puuttuuko työnkulusta jokin tyypillinen vaihe tässä aiheessa? Ovatko botin rajat realistisia vai liian tiukkoja tai liian löysiä? Mikä on yksi sokea piste, jota en ehkä vielä huomaa? Älä kirjoita uutta versiota puolestani. Anna 2–3 konkreettista parannusehdotusta, joiden pohjalta voin tehdä omat muutokseni."

Tämä on harjoitus siitä, miten tekoälyä käytetään *suunnittelukumppanina*. Et anna sen päättää puolestasi, mutta annat sen kyseenalaistaa suunnitelmasi.

Lue palaute kysymyksinä omalle suunnitelmallesi, älä korjauslistana. Tekoäly ei tunne yhteisösi käytäntöjä eikä käyttäjän todellista tilannetta. Hyvä muutos syntyy vasta, kun pystyt yhdistämään ehdotuksen määrittelyn ristiriitaan, puuttuvaan tietoon tai epäselvään rajaan.

### Vaihe 4 — Viimeistele määrittelydokumentti

Tee tekoälyn palautteen pohjalta tarvittavat korjaukset. Viimeistele määrittelydokumentti niin, että sen perusteella voisi rakentaa botin myös toinen henkilö, ei vain sinä itse.

Merkitse vähintään yksi muutos ja sen peruste. Jos et muuta mitään, kirjoita, minkä palautteen tarkistit ja miksi alkuperäinen ratkaisu säilyi. Myös ennallaan pitäminen on päätös, kun se perustuu määrittelyn tavoitteeseen eikä siihen, että palaute jätettiin lukematta.

Tarkista viimeistelyssä erityisesti nämä asiat:

- Botin tarkoitus on konkreettinen ja helposti ymmärrettävä.
- Kohderyhmä on rajattu selkeästi.
- Työnkulku etenee loogisessa järjestyksessä.
- Botin rajat kertovat selvästi, mitä botti ei tee.
- Äänensävy sopii kohderyhmälle ja tehtävän vakavuuteen.

Kirjoita lopuksi 2–3 lauseen pohdinta: *"Mikä määrittelyssä muuttui sparrauksen jälkeen? Mikä on bottini ydin yhdellä lauseella?"*

Ydinlauseessa ei tarvitse luetella kaikkia ominaisuuksia. Sen pitää kertoa käyttäjä, tehtävä ja hyödyllinen lopputulos niin selvästi, että voit käyttää lausetta seuraavilla tunneilla jokaisen lähteen, testin ja toteutusvalinnan mittatikkuna.

> **Miksi tämä on tärkeää:** Apuri-botin rakennustunnilla aloitat botin rakentamisen valitsemallasi alustalla. Määrittely kertoo, mitä järjestelmäpromptiin pitää kirjoittaa, millaista tietopohjaa botti tarvitsee ja milloin se on valmis ensimmäiseen testiin.

> **Tarkista lopuksi:** Olet valinnut apuri-bottisi aiheen, täyttänyt botin määrittelydokumentin, haastanut suunnitelmasi tekoälyn avulla, viimeistellyt dokumentin ja kirjoittanut 2–3 lauseen pohdinnan bottisi ytimestä.

**2 / 3 rakennuspalikkaa kerätty**
