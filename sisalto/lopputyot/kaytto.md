# Tekoälyjen käyttö -osion lopputyö: Rakenna oma apuri-botti

Tämä on Tekoälyjen käyttö -osion arvioitava lopputyö. Rakennat itse suunnittelemasi **apuri-botin** valitsemallasi saatavilla olevalla alustalla. Jos bottialustaa tai tiliä ei ole käytettävissä, teet vastaavan dokumentoidun kuivaharjoittelun tavallisessa kielimallichatissa. Et tee koko työtä yhdellä istumalla — keräät matkan varrella **kolme rakennuspalikkaa**, joista kasaat botin tunnilla 17 ja viimeistelet sen tunnilla 18.

> **Miksi näin?** Hyvää bottia ei rakenneta yhdellä tunnilla. Sen pohjana ovat kolme rakennuspalikkaa, jotka kerätään koko osion aikana — promptauspankki (tunti 12), botin määrittely (tunti 14) ja kuratoitu tietopohja (tunti 15). Kun palikat ovat valmiina, tunneilla 17–18 voit keskittyä rakentamiseen, testaamiseen ja viimeistelyyn.

## Mitä rakennat?

**Apuri-botti tai sen todennettava kuivaharjoittelu**, joka auttaa rajatussa arjen, opiskelun, harrastuksen tai muun itse valitun tilanteen tehtävässä. Botti on *ohjaava, ei kirjoittava* — se ei tee kaikkea käyttäjän puolesta, vaan auttaa käyttäjää etenemään hallitusti.

Valitset itseäsi kiinnostavan, omasta arjestasi tutun aiheen, esimerkiksi:

- **Opiskelu** — selittää käsitteitä, auttaa jäsentämään tehtäviä, toimii harjoittelukaverina kokeisiin
- **Harrastus tai kerho** — säännöt, aikataulut, vinkit ja FAQ jäsenille
- **Tuttu pieni palvelu** — kahvilan, kirjaston tai urheiluseuran FAQ-botti
- **Pelit, musiikki tai sisältö** — auttaa ideoimaan pelin, biisin tai videon
- **Arjen apuri** — auttaa suunnittelemaan vaikka treenirutiinin tai viikkoaikataulun

Valitse aihe, jonka tunnet hyvin omasta arjestasi. Bottisi tuntee juuri sinun aiheesi termit ja tilanteet — se ei ole yleinen avustaja, vaan erikoistunut juuri sinun valitsemaasi aiheeseen. Tämä erottaa sinun bottisi yleisestä ChatGPT:stä.

## Polku alusta loppuun

Lopputyö rakentuu kolmesta rakennuspalikasta, jotka kerätään matkan varrella ja kootaan botiksi tunnilla 17.

| Tunti | Mitä teet | Tuotos |
|---|---|---|
| 10–11 | Kilpailutat tekoälyt ja opit tietosuojan | (perusta, ei palautusta) |
| **12** | Rakennat oman promptauspankkisi | **Rakennuspalikka 1: Promptauspankki** |
| 13 | Harjoittelet AI:tä työparina | (tarkennus, ei palautusta) |
| **14** | Suunnittelet botin määrittelyn | **Rakennuspalikka 2: Botin määrittely** |
| **15** | Kuratoit botin tietopohjan | **Rakennuspalikka 3: Tietopohja** |
| 16 | Tutustut erikoisalojen tekoälytyökaluihin | (tarkennus, ei palautusta) |
| **17** | **Kasaat kolme rakennuspalikkaa botiksi tai kuivaharjoitteluksi** | **Ensimmäinen toimiva toteutus** |
| **18** | **Testaat, viimeistelet ja esittelet** | **Lopputyö valmis** |

> 💡 **Vinkki:** Tee oma muistiinpanodokumentti (Word, OneNote, Google Docs tai mikä tahansa), johon kerää kolme rakennuspalikkaa omiksi alaotsikoikseen. Tunnilla 17 sinulla on yksi tiedosto auki, ei kolme.

## Kolmen rakennuspalikan yleiskuvaus

Yksityiskohtaiset ohjeet kunkin rakennuspalikan tekemiseen saat kyseisellä tunnilla. Tässä lyhyt yleiskuvaus, jotta näet kokonaisuuden.

**Rakennuspalikka 1: Promptauspankki (tunti 12)**
Oma kokoelma toimivia prompteja valitsemaasi arjen tai harrastuksen, opiskelun tai työelämän rooliskenaarioon. Tämä antaa pohjan botin järjestelmäpromptille, joka määrittää botin käytöksen.

**Rakennuspalikka 2: Botin määrittely (tunti 14)**
Botin "perustamisasiakirja": kenelle botti on, mitä se osaa, mitä se ei tee, mitkä ovat sen rajat. Ilman tätä botti kasvaa hallitsemattomasti.

**Rakennuspalikka 3: Tietopohja (tunti 15)**
3–5 dokumenttia, joista botti saa valitun kontekstin tiedon. Tämä on botin tietopohja. Kuratointi on tärkeämpää kuin määrä.

## Lopputuotoksen vaatimukset

::: luokka
Tunti 18:n päätteeksi palautat ja esittelet seuraavat:
:::

::: verkko
Lopputyön tuotokset:
:::

**1. Toimiva botti tai kuivaharjoittelu**
Linkki bottiin tai dokumentoitu suoritusjälki, josta näkyvät järjestelmäprompti, käyttäjän syötteet, vastaukset ja odotetut työkaluvaiheet. Molemmat vaihtoehdot arvioidaan samoilla kriteereillä.

**2. Botin määrittely**
Tunnin 14 botin määrittely (rakennuspalikka 2), päivitettynä lopputyösi botin mukaisesti.

**3. Järjestelmäprompti kokonaisuudessaan**
Kopioituna tiedostoon. Tämä on botin "DNA" ja arvioinnin tärkein lähde.

**4. Lista tietopohjan dokumenteista**
3–5 dokumenttia ja perustelu, miksi valitsit juuri nämä.

**5. Testimatriisi ja korjausketju**
Vähintään normaali tapaus, kielteinen testi ja reunatapaus. Kirjaa jokaisesta syöte, odotus, todellinen tulos ja johtopäätös. Tee vähintään yksi nimetty korjaus ja aja sitä koskeva testi uudelleen.

**6. Reflektio (200–300 sanaa)**
Mitä opit botin rakentamisesta? Mikä toimi heti, mikä vaati monta yritystä? Mitä tekisit toisin?

## Lyhyt esittely ja puolustus

Pidä 2–3 minuutin esittely: kerro kenelle botti on rakennettu, näytä yksi ennen–jälkeen-korjaus ja perustele yksi rajaus. Esitys voi olla live, nauhoitettu video tai kuvakaappauskooste. Vastaa lopuksi yhteen jatkokysymykseen omista valinnoistasi.

> 💡 **Vinkki esimerkkikäyttäjästä:** Kun testaat ja esittelet, kuvittele yksi tyypillinen käyttäjä — esimerkiksi luokkakaveri, joka aloittaa harrastuksessa, tai uusi jäsen, joka etsii vastauksia kerhon FAQ:sta. Botin pitää toimia juuri hänelle.

## Työkalut ja työskentelytapa

**Alusta:** valitse saatavilla oleva bottialusta tai tavallinen kielimallichat kuivaharjoitteluun.

::: luokka
Opettaja kertoo käytettävissä olevat alustat tunnilla 17. Tunnuksen puuttuminen ei estä työn tekemistä.
:::
::: verkko
Et tarvitse tietyn palvelun tiliä. Käytä saatavilla olevaa palvelua tai tee dokumentoitu kuivaharjoittelu.
:::

**Tekoälytyökalu botin rakentamiseen:** Voit valita vapaasti — ChatGPT, Claude, Copilot tai muu. Tarkoitus ei ole keksiä kaikkea itse, vaan ohjata tekoälyä auttamaan sinua suunnittelussa, testauksessa ja viimeistelyssä. Sinun vastuullasi on, että botti toimii ammattimaisesti ja että ymmärrät sen rakenteen kokonaan.

**Yksin tai pareittain:** Lopputyö tehdään yksin, koska bottisi on juuri sinun valitsemasi aiheen näköinen. Voit kuitenkin sparrata luokkakavereiden kanssa rakennuspalikoiden kokoamisessa.

::: luokka
## Arviointi

Lopputyö arvioidaan viiden kriteerin pohjalta. Yhteensä 100 pistettä.

| Kriteeri | Pisteet | Mitä arvioidaan |
|---|---|---|
| **Toimiva botti** | 25 p | Toimiiko botti? Ohjaako se käyttäjää järjestelmällisesti tehtävän vaiheiden läpi? |
| **Järjestelmäprompti** | 20 p | Onko järjestelmäpromptissa selkeä rooli, työnkulku ja rajat? Käyttääkö se oman aiheesi termejä? |
| **Tietopohja** | 20 p | Onko tietopohjassa 3–5 hyvää, perusteltua dokumenttia? Tukevatko ne botin tehtävää? |
| **Testaaminen ja iterointi** | 20 p | Kattavatko testit normaalin, kielteisen ja reunatapauksen? Näkyvätkö korjaus ja uudelleentesti? |
| **Reflektio ja puolustus** | 15 p | Perustellaanko valinnat, rajat ja ennen–jälkeen-korjaus lyhyessä esittelyssä? |
:::

::: verkko
## Itsearviointi

Opiskelet omaan tahtiin ilman oppilaitosta, joten arvioit bottisi itse. Käy viisi kriteeriä läpi ennen kuin toteat sen valmiiksi. Painoarvo kertoo, mihin kannattaa panostaa eniten — painotus on sama, jolla työtä muutenkin arvioitaisiin.

| Kriteeri | Painoarvo | Kysy itseltäsi |
|---|---|---|
| **Toimiva botti** | 25 % | Toimiiko bottini? Ohjaako se käyttäjää järjestelmällisesti tehtävän vaiheiden läpi? |
| **Järjestelmäprompti** | 20 % | Onko järjestelmäpromptissani selkeä rooli, työnkulku ja rajat? Käyttääkö se oman aiheeni termejä? |
| **Tietopohja** | 20 % | Onko tietopohjassani 3–5 hyvää, perusteltua dokumenttia? Tukevatko ne botin tehtävää? |
| **Testaaminen ja iterointi** | 20 % | Olenko ajanut normaalin, kielteisen ja reunatapauksen sekä dokumentoinut korjauksen ja uudelleentestin? |
| **Reflektio ja puolustus** | 15 % | Perustelenko valintani ja rajani sekä näytänkö ymmärrykseni lyhyessä esittelyssä? |
:::

## Aikabudjetti

Lopputyö hajautuu yhdeksälle oppitunnille. Tässä karkea aika-arvio, joka auttaa sinua suunnittelemaan omaa työtäsi.

| Vaihe | Aika-arvio |
|---|---|
| Yksi rakennuspalikka (tunnit 12, 14, 15) | ~25–30 min / palikka |
| Botin rakentaminen tai kuivaharjoittelu (tunti 17) | ~75 min (koko tunti) |
| Testaus, viimeistely ja esittely (tunti 18) | ~75 min (koko tunti) |
| **Yhteensä lähiaikaa** | **~3–4 tuntia** |

> 💡 **Vinkki ajankäyttöön:** Jos joku rakennuspalikka jää kesken tunnilla, viimeistele se kotona ennen seuraavaa tuntia. Tunnilla 17 sinulla pitää olla kolme rakennuspalikkaa valmiina — muuten kokoaminen ei onnistu.

::: luokka
## Palautus

Palautat tunnilla 18 yhden tiedoston (esim. PDF tai Word), joka sisältää:

- Botin määrittely (päivitettynä)
- Järjestelmäprompti kokonaisuudessaan
- Tietopohjan dokumenttien lista perusteluineen
- Testimatriisi sekä korjauksen ennen–jälkeen-näyttö
- Reflektio (200–300 sanaa)
- Linkki bottiin tai kuivaharjoittelun suoritusjälki
:::

::: verkko
## Kokoa tuotoksesi

Kokoa työsi yhdeksi tiedostoksi (esim. PDF tai Word) omaan portfolioosi. Näin koko botti dokumentteineen on tallessa yhdessä paikassa:

- Botin määrittely (päivitettynä)
- Järjestelmäprompti kokonaisuudessaan
- Tietopohjan dokumenttien lista perusteluineen
- Testimatriisi sekä korjauksen ennen–jälkeen-näyttö
- Reflektio (200–300 sanaa)
- Linkki bottiin tai kuivaharjoittelun suoritusjälki

Käy lopuksi läpi yllä oleva itsearviointilista. Halutessasi jaa bottisi tai paketti — mitään ei palauteta minnekään.
:::

---

**Et opettele käyttämään tekoälyä — opit rakentamaan sillä.**


## Arviointitasot

| Kriteeri | Erinomainen | Hyvä | Tyydyttävä | Välttävä | Ei vielä hyväksyttävä |
|---|---|---|---|---|---|
| Toimiva botti (25 p) | Botti ratkaisee rajatun tehtävän johdonmukaisesti, rajat näkyvät ja toteutus tai kuivaharjoittelu on todennettava. | Ydintehtävä toimii tai on todennettu selkeällä suoritusjäljellä. | Ydintehtävä toimii useimmissa testeissä, mutta yksi olennainen kohta on epävarma. | Osa työnkulusta näkyy, mutta ydintehtävä ei toimi luotettavasti. | Toteutusta tai todennettavaa kuivaharjoittelujälkeä ei ole. |
| Järjestelmäprompti (20 p) | Tarkoitus, rooli, ohjeet, rajat ja epävarmuuden käsittely ovat täsmällisiä ja testien perusteella parannettuja. | Prompti määrittää tarkoituksen, ohjeet ja rajat selkeästi. | Prompti ohjaa ydintehtävää, mutta rajat tai poikkeustilanteet ovat osittaisia. | Prompti on yleinen tai ristiriitainen. | Järjestelmäprompti puuttuu tai ei ohjaa tehtävää. |
| Tietopohja (20 p) | Lähteet ovat tarkoituksenmukaisia, jäljitettäviä, rajattuja ja ajantasaisuus arvioidaan. | Tietopohja tukee tehtävää ja lähteet on nimetty. | Tietopohja on käyttökelpoinen, mutta lähde- tai ajantasaisuustieto on osittainen. | Aineiston sopivuutta ei perustella tai siinä on selviä aukkoja. | Tietopohja tai sitä korvaava annettu aineisto puuttuu. |
| Testaus ja iterointi (20 p) | Testit kattavat normaalit, kielteiset ja reunatapaukset; korjaus ja uudelleentesti osoittavat syy–seuraussuhteen. | Kaikki kolme testityyppiä, korjaus ja uudelleentesti on dokumentoitu. | Testit kattavat ydintoiminnan, mutta korjausketju jää osittaiseksi. | Testejä on vähän tai tuloksia ei verrata odotukseen. | Testaus ja iterointi puuttuvat. |
| Reflektio ja puolustus (15 p) | Oppija perustelee valinnat, tunnistaa rajat ja vastaa demossa täsmällisesti jatkokysymyksiin. | Valinnat ja rajat perustellaan, ja demo osoittaa oman ymmärryksen. | Reflektio kuvaa työtä, mutta perustelut tai demo jäävät yleisiksi. | Reflektio on luettelomainen tai oma ymmärrys jää epäselväksi. | Reflektio ja demo tai puolustus puuttuvat. |
