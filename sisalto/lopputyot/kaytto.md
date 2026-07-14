# Tekoälyjen käyttö -osion lopputyö: Rakenna oma apuri-botti

Tämä on Tekoälyjen käyttö -osion arvioitava lopputyö. Rakennat itse suunnittelemasi **apuri-botin** Microsoft Copilot Agent -alustalle. Botti auttaa jossakin sinulle tutussa arjen aiheessa — opiskelussa, harrastuksessa, tutussa pienessä palvelussa tai vaikka pelin tai sisällön ideoinnissa. Et tee koko työtä yhdellä istumalla — keräät matkan varrella **kolme rakennuspalikkaa**, joista kasaat botin tunnilla 17 ja viimeistelet sen tunnilla 18.

> **Miksi näin?** Hyvää bottia ei rakenneta yhdellä tunnilla. Sen pohjana ovat kolme rakennuspalikkaa, jotka kerätään koko osion aikana — promptauspankki (tunti 12), botin määrittely (tunti 14) ja kuratoitu tietopohja (tunti 15). Kun palikat ovat valmiina, tunneilla 17–18 voit keskittyä rakentamiseen, testaamiseen ja viimeistelyyn.

## Mitä rakennat?

**Microsoft Copilot Agent -botti**, joka auttaa sinua tai kavereitasi jossakin sinulle tutussa arjen aiheessa. Botti on *ohjaava, ei kirjoittava* — se ei tee asioita käyttäjän puolesta, vaan auttaa käyttäjää onnistumaan paremmin kuin yksin.

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
| **17** | **Kasaat kolme rakennuspalikkaa botiksi Copilotissa** | **Ensimmäinen toimiva botti** |
| **18** | **Testaat, viimeistelet ja esittelet** | **Lopputyö valmis** |

> 💡 **Vinkki:** Tee oma muistiinpanodokumentti (Word, OneNote, Google Docs tai mikä tahansa), johon kerää kolme rakennuspalikkaa omiksi alaotsikoikseen. Tunnilla 17 sinulla on yksi tiedosto auki, ei kolme.

## Kolmen rakennuspalikan yleiskuvaus

Yksityiskohtaiset ohjeet kunkin rakennuspalikan tekemiseen saat kyseisellä tunnilla. Tässä lyhyt yleiskuvaus, jotta näet kokonaisuuden.

**Rakennuspalikka 1: Promptauspankki (tunti 12)**
Oma kokoelma toimivia prompteja oman alasi tilanteisiin. Tämä antaa pohjan botin järjestelmäpromptille — sen "DNA:lle", joka määrittää miten botti käyttäytyy.

**Rakennuspalikka 2: Botin määrittely (tunti 14)**
Botin "perustamisasiakirja": kenelle botti on, mitä se osaa, mitä se ei tee, mitkä ovat sen rajat. Ilman tätä botti kasvaa hallitsemattomasti.

**Rakennuspalikka 3: Tietopohja (tunti 15)**
3–5 dokumenttia, joista botti ammentaa oman alasi tietoa. Tämä on botin "kirjasto". Kuratointi on tärkeämpää kuin määrä.

## Lopputuotoksen vaatimukset

::: luokka
Tunti 18:n päätteeksi palautat ja esittelet seuraavat:
:::

::: verkko
Lopputyön tuotokset:
:::

**1. Toimiva botti Copilotissa**
Linkki bottiin, jotta kuka tahansa linkin saanut pääsee testaamaan sitä itse. Botti tunnistaa oman aiheesi termit ja ohjaa käyttäjää valitsemasi tehtävän vaiheiden läpi.

**2. Botin määrittely**
Tunnin 14 botin määrittely (rakennuspalikka 2), päivitettynä lopputyösi botin mukaisesti.

**3. Järjestelmäprompti kokonaisuudessaan**
Kopioituna tiedostoon. Tämä on botin "DNA" ja arvioinnin tärkein lähde.

**4. Lista tietopohjan dokumenteista**
3–5 dokumenttia ja perustelu, miksi valitsit juuri nämä.

**5. Testikeskustelu**
Vähintään yksi täysi keskustelu, jossa botti ohjaa kuvitellun käyttäjän valitsemasi tehtävän läpi alusta loppuun (kuvakaappaukset tai kopio).

**6. Reflektio (200–300 sanaa)**
Mitä opit botin rakentamisesta? Mikä toimi heti, mikä vaati monta yritystä? Mitä tekisit toisin?

## Esittely (valinnainen)

Voit halutessasi pitää bottisi esittelyn ryhmälle: kerro kenelle botti on rakennettu, näytä yksi konkreettinen testikeskustelu ja kerro yksi asia, jonka opit matkan varrella. Esitys voi olla live, nauhoitettu video tai kuvakaappauskooste.

> 💡 **Vinkki esimerkkikäyttäjästä:** Kun testaat ja esittelet, kuvittele yksi tyypillinen käyttäjä — esimerkiksi luokkakaveri, joka aloittaa harrastuksessa, tai uusi jäsen, joka etsii vastauksia kerhon FAQ:sta. Botin pitää toimia juuri hänelle.

## Työkalut ja työskentelytapa

**Alusta:** Microsoft Copilot Agent. Saat tunnukset opettajalta tunnilla 17.

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
| **Testaaminen ja iterointi** | 20 p | Onko bottia testattu oikealla käyttötilanteella? Onko järjestelmäpromptia iteroitu vähintään kahdesti? |
| **Reflektio** | 15 p | Kuvaako reflektio mitä opit — ei vain mitä teit? |
:::

::: verkko
## Itsearviointi

Opiskelet omaan tahtiin ilman oppilaitosta, joten arvioit bottisi itse. Käy viisi kriteeriä läpi ennen kuin toteat sen valmiiksi. Painoarvo kertoo, mihin kannattaa panostaa eniten — painotus on sama, jolla työtä muutenkin arvioitaisiin.

| Kriteeri | Painoarvo | Kysy itseltäsi |
|---|---|---|
| **Toimiva botti** | 25 % | Toimiiko bottini? Ohjaako se käyttäjää järjestelmällisesti tehtävän vaiheiden läpi? |
| **Järjestelmäprompti** | 20 % | Onko järjestelmäpromptissani selkeä rooli, työnkulku ja rajat? Käyttääkö se oman aiheeni termejä? |
| **Tietopohja** | 20 % | Onko tietopohjassani 3–5 hyvää, perusteltua dokumenttia? Tukevatko ne botin tehtävää? |
| **Testaaminen ja iterointi** | 20 % | Olenko testannut bottia oikealla käyttötilanteella? Olenko iteroinut järjestelmäpromptia vähintään kahdesti? |
| **Reflektio** | 15 % | Kuvaako reflektioni mitä opin — ei vain mitä tein? |
:::

## Aikabudjetti

Lopputyö hajautuu yhdeksälle oppitunnille. Tässä karkea aika-arvio, joka auttaa sinua suunnittelemaan omaa työtäsi.

| Vaihe | Aika-arvio |
|---|---|
| Yksi rakennuspalikka (tunnit 12, 14, 15) | ~25–30 min / palikka |
| Botin rakentaminen Copilotissa (tunti 17) | ~75 min (koko tunti) |
| Testaus, viimeistely ja esittely (tunti 18) | ~75 min (koko tunti) |
| **Yhteensä lähiaikaa** | **~3–4 tuntia** |

> 💡 **Vinkki ajankäyttöön:** Jos joku rakennuspalikka jää kesken tunnilla, viimeistele se kotona ennen seuraavaa tuntia. Tunnilla 17 sinulla pitää olla kolme rakennuspalikkaa valmiina — muuten kokoaminen ei onnistu.

::: luokka
## Palautus

Palautat tunnilla 18 yhden tiedoston (esim. PDF tai Word), joka sisältää:

- Botin määrittely (päivitettynä)
- Järjestelmäprompti kokonaisuudessaan
- Tietopohjan dokumenttien lista perusteluineen
- Testikeskustelu (kuvakaappauksina tai kopioituna)
- Reflektio (200–300 sanaa)
- Linkki bottiisi Copilotissa
:::

::: verkko
## Kokoa tuotoksesi

Kokoa työsi yhdeksi tiedostoksi (esim. PDF tai Word) omaan portfolioosi. Näin koko botti dokumentteineen on tallessa yhdessä paikassa:

- Botin määrittely (päivitettynä)
- Järjestelmäprompti kokonaisuudessaan
- Tietopohjan dokumenttien lista perusteluineen
- Testikeskustelu (kuvakaappauksina tai kopioituna)
- Reflektio (200–300 sanaa)
- Linkki bottiisi Copilotissa

Käy lopuksi läpi yllä oleva itsearviointilista. Halutessasi jaa bottisi tai paketti — mitään ei palauteta minnekään.
:::

---

**Et opettele käyttämään tekoälyä — opit rakentamaan sillä.**
