# Opettajan materiaalit — oppitunti 27: viimeistely ja puolustus

## Oppitunnin tavoite

Opiskelija viimeistelee yhden 90 minuutin oppitunnin aikana teknisen n8n-toteutuksen tai dokumentoidun suunnitelman, osoittaa aidon rajatun kielimallivalinnan, ajaa kolme testiä, tekee yhden korjauksen ja uudelleentestin sekä puolustaa ratkaisuaan 2–3 minuutissa. Pakollista työtä ei jätetä kotiin.

Molemmat toteutuspolut ovat samanarvoisia. Tekninen polku näyttää tapahtumat suoritusnäkymästä. Dokumentoitu polku näyttää todellisen kielimallikutsun ja sitä seuraavan simuloidun suoritusjäljen. Arvioinnin kohde on todistusaineisto ja ymmärrys, ei teknisten solmujen määrä.

## Osaamistavoitteet

Oppitunnin jälkeen opiskelija osaa:

- kuvata **syötekäsittelijän**, **päättelijän ja suunnittelijan**, **työkalujen suorittajan**, **muistin ja kontekstin**, **turvakerroksen** sekä **seurannan ja palautesilmukan** vastuut omassa työssään
- osoittaa syötteen, vähintään kaksi sallittua vaihtoehtoa, kielimallin todellisen valinnan ja sitä seuraavan vaiheen
- dokumentoida normaalin, reuna- ja turvallisuustestin
- tehdä yhden perustellun korjauksen ja ajaa saman testin uudelleen
- erottaa toteutetun, simuloidun ja vielä todentamattoman toiminnan
- puolustaa ratkaisunsa tiiviisti ja rehellisesti.

## Valmistelu

Valitse ennen tuntia puolustuksen toteutustapa luokan koon mukaan:

- **pienryhmät:** 3–4 opiskelijaa, jokaiselle 2–3 minuuttia
- **tallenne:** opiskelija tallentaa puheenvuoron tunnin lopussa
- **otos:** opettaja kuulee osan puolustuksista ja muut palauttavat saman rakenteen kirjallisesti tai tallenteena.

Pidä näkyvillä yhteinen näyttöpaketin pohja ja testitaulukko. Varmista, että dokumentoidun polun opiskelijat pääsevät tekemään yhden todellisen kielimallikutsun. Teknisen liitännän häiriötä varten salli turvallinen testiympäristö, tallennettu suoritus tai dokumentoitu rajaus.

## 90 minuutin toteutus ja eriyttäminen

### 0–8 min — aloitus ja rajaus

Kerro heti, että pakollinen suoritus päättyy tunnin lopussa. Opiskelija valitsee yhden pääpolun, jota hän osoittaa. Jos työ on liian suuri, sitä rajataan nyt eikä siirretä kotitehtäväksi.

### 8–30 min — toteutuksen tai suunnitelman viimeistely

Opiskelija tarkistaa kuusi rakennusosaa ja varmistaa aidon rajatun mallivalinnan. Kierrä ja kysy:

- Mikä syöte mallille annetaan?
- Mitkä vähintään kaksi vaihtoehtoa ovat sallittuja?
- Missä mallin valinta näkyy?
- Miten ohjauskehys määrää valintaa seuraavan vaiheen?

Jos dokumentoidussa polussa ei ole todellista mallikutsua tai teknisessä polussa reitti on aina sama ilman mallin valintaa, pyydä korjaamaan tämä ennen testausta.

### 30–48 min — kolme testiä

Opiskelija ajaa yhden normaalin, yhden reuna- ja yhden turvallisuustestin. Jokaisesta kirjataan syöte, odotettu tulos, todellinen tulos ja johtopäätös. Dokumentoidussa polussa todellinen tulos on kielimallin valinta ja käsin seurattu suoritusjälki. Tekninen polku käyttää suoritusnäkymää.

Ohjaa reunatapaus havaittavaan ehtoon, kuten puuttuvaan pakolliseen tietoon tai ristiriitaisiin lähteisiin. Turvallisuustestissä tarkastellaan esimerkiksi toimintorajoitusta, hyväksyntäporttia tai oikeuksia. Mallin itse ilmoittama varmuusprosentti ei ole testattava eskalointiehto.

### 48–63 min — yksi korjaus ja uudelleentesti

Opiskelija valitsee yhden puutteen, tekee rajatun muutoksen ja ajaa saman testin uudelleen samalla syötteellä. Hyvä korjaus voi kohdistua järjestelmäohjeeseen, sallittuihin vaihtoehtoihin, validointiin, työkalusopimukseen, turvarajaan, kaavioon tai virhepolkuun.

Vaadi näkyviin alkuperäinen tulos, muutos, uusi tulos ja johtopäätös. Suuren uuden ominaisuuden rakentamista ei vaadita.

### 63–75 min — tiivis näyttöpaketti

Opiskelija kokoaa yhdelle sivulle, dialle tai vastaavaan näkymään:

- ongelman ja toteutuspolun
- työnkulun tai kaavion sekä kuuden rakennusosan kattavuuden
- aidon rajatun mallivalinnan
- kolmen testin tulokset
- yhden korjauksen ja uudelleentestin
- tärkeimmän turvallisuusrajan ja yhden rehellisen rajoituksen.

Kolmea erillistä pitkää dokumenttia, laajaa itsearviointia tai vertaisarviomuistiota ei vaadita.

### 75–88 min — 2–3 minuutin puolustus

Käynnistä ennalta valittu pienryhmä-, tallenne- tai otosjärjestely. Puolustuksessa opiskelija kertoo ongelman ja polun, näyttää mallivalinnan, vertaa testiä ja uudelleentestiä sekä nimeää turvallisuusrajan ja rajoituksen.

Pienryhmässä kuuntelija esittää yhden tarkentavan kysymyksen. Tallenteessa tai kirjallisessa otoksessa opiskelija vastaa valmiiksi kysymykseen: ”Mitä näyttösi ei vielä todista?”

### 88–90 min — palautus

Opiskelija palauttaa tai tallentaa näyttöpaketin. Keskeneräinen ulkoinen liitäntä merkitään rajoitukseksi. Pakollista työtä ei anneta kotiin.

## Tasapuolinen arviointi

| Kriteeri | Paino | Sama vaatimus molemmille poluille |
|---|---:|---|
| Rakenne ja toteutuspolun näyttö | 20 % | Työnkulku tai kaavio on seurattava ja kuusi rakennusosaa on käsitelty. |
| Aito rajattu mallivalinta | 25 % | Syöte, vaihtoehdot, mallin valinta ja seuraava vaihe näkyvät. |
| Testi, korjaus ja uudelleentesti | 25 % | Kolme testiä ja yksi ennen–jälkeen-korjaus ovat jäljitettävissä. |
| Turvallisuus ja rajat | 20 % | Oikeudet, havaittava eskalointiehto ja rajoitus näkyvät. |
| Puolustus | 10 % | Opiskelija perustelee ratkaisun ja erottaa toteutetun simuloidusta. |

Teknisen polun liitännän toimivuus on kyseisen näytön ominaisuus, ei lisäpisteiden lähde. Dokumentoidun polun työkalusopimusten ja simuloidun suoritusjäljen johdonmukaisuus arvioidaan samalla painolla. Kumpaakaan polkua ei arvioida siitä, mitä toinen polku lupaa osoittaa.

## Tyypilliset tilanteet ja ohjaus

**Työ on liian suuri 90 minuuttiin.** Rajaa yhteen pääpolkuun, yhteen mallivalintaan ja kolmeen testiin. Älä siirrä puuttuvaa laajuutta kotitehtäväksi.

**Mallivalinta ei ole aito.** Pyydä näyttämään vähintään kaksi sallittua vaihtoehtoa ja kaksi syötettä, jotka voivat johtaa eri valintaan. Kiinteä jos–niin-ehto ei yksin riitä.

**Dokumentoitu polku väittää liikaa.** Pyydä merkitsemään todellinen mallikutsu, simuloidut vaiheet ja teknisesti todentamattomat liitännät erikseen.

**Tekninen polku ei käynnisty.** Rajaa virhe, käytä tallennettua suoritusnäyttöä tai siirry rehellisesti dokumentoituun näyttöön. Arvioi ymmärrystä ja todistusaineistoa.

**Ensimmäinen testi onnistuu.** Opiskelija tekee silti reuna- ja turvallisuustestin. Korjaus valitaan mistä tahansa kolmessa testissä tai kattavuustarkistuksessa havaitusta puutteesta.
