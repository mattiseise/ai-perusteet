# Opettajan materiaalit — oppitunti 13: pohja, muokkaus ja tarkistus

## Oppitunnin tarkoitus

Oppija käyttää tekoälyä kolmessa rajatussa roolissa: pohjan tekijänä, muokkauksen tukena ja testilukijana. Ihmisen korjaukset, hylkäykset ja perustelut tehdään näkyviksi.

Tunnin tehtävä ei ole opettaa, että tekoälyltä saadaan ensin huono ja sitten hyvä teksti. Oppija harjoittelee erottamaan ehdotuksen päätöksestä. Siksi työssä säilytetään versiot ja kirjataan, mikä muutos perustui lähteeseen, mikä käyttäjän tarpeeseen ja mikä turvalliseen rajaukseen.

## Mallinnettava esimerkkiketju

Käytä yhtä palautusohjetta läpi tunnin. Lähde kertoo 14 päivän määräajan, käyttämättömän tuotteen ehdon ja tilausvahvistuksessa olevan palautuslinkin. Tekoälyn luonnos keksii asiakastilin painikkeen ja jättää yhden ehdon pois. Ihminen korjaa nämä lähteen perusteella. Testilukija huomaa, ettei aloittelija ehkä löydä tilausvahvistusta, mutta ehdottaa myös tärkeän määräajan poistamista. Ihminen hyväksyy selvennyksen ja hylkää poistamisen. Ketju näyttää yhdellä tapauksella kaikki tunnin roolit ilman uusia sisältöalueita.

## Osaamistavoitteet

Oppija:

- pyytää tehtävään rajatun luonnoksen
- tarkistaa ensin sisällön ja vasta sitten tyylin
- tekee vähintään kolme omaa muutosta ja perustelee ne
- antaa tekoälylle yhden nimetyn tarkistusroolin
- hyväksyy, muokkaa tai hylkää saadun palautteen perustellusti
- osoittaa ennen–jälkeen-näytöllä oman vastuunsa lopputuloksesta

## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **annotoitu ennen–jälkeen-tuotos ja päätösloki**.

Pidä esimerkkiketju näkyvissä työskentelyn aikana. Kun oppija jää kiinni tekstin hiomiseen, palauta hänet kysymään, mitä kohtaa hän on muuttamassa ja mihin tietoon päätös perustuu. Kun palautevaihe alkaa, muistuta, ettei testilukijalle siirry lopullista päätösvaltaa.

| Aika | Vaihe | Opettajan tehtävä |
| --- | --- | --- |
| 0–10 min | Vastuunjako | Mallinna ero avun käyttämisen ja työn luovuttamisen välillä. |
| 10–25 min | Pohja | Oppija määrittää tehtävän, aineiston ja yleisön sekä tuottaa luonnoksen. |
| 25–50 min | Oma muokkaus | Oppija nimeää ongelmat ja tekee vähintään kolme perusteltua muutosta. |
| 50–65 min | Testilukija | Tekoäly etsii yhtä nimettyä ongelmatyyppiä. |
| 65–78 min | Päätös | Oppija hyväksyy, muokkaa tai hylkää ehdotukset ja perustelee valinnat. |
| 78–90 min | Ennen–jälkeen | Oppija kokoaa tuotoksen ja kirjoittaa, mikä parani hänen päätöksensä vuoksi. |

## Tyypilliset väärinkäsitykset

Väärinkäsitysten yhteinen tausta on se, että valmis teksti peittää työprosessin. Tee siksi versiot ja perustelut näkyviksi jo mallinnuksessa, älä vasta palautusvaiheessa.

- Pitkä valmis vastaus ei osoita oppijan omaa osaamista.
- Tekoälyn palaute ei ole automaattisesti oikeaa.
- Tyylin silottaminen ei korjaa sisällöllistä virhettä.
- Hyvä oppija voi hylätä tekoälyn luonnoksen tai ehdotuksen kokonaan.

Jos oppija hyväksyy kaiken palautteen, kysy, mikä ehdotus oli ristiriidassa lähteen, kohderyhmän tai tavoitteen kanssa. Jos hän hylkää kaiken, kysy, mikä havainto palautteessa silti auttoi näkemään tekstin käyttäjän silmin. Tarkoitus ei ole saavuttaa tiettyä hyväksymisprosenttia, vaan tehdä perusteltuja päätöksiä.

## Eriyttäminen

**Tukireitti:** anna lyhyt lähdeaineisto, valmis tehtävä ja muutosten luokittelutaulukko.

**Syventävä reitti:** toinen ihminen testaa lopullista tuotosta todellisen käyttäjän näkökulmasta. Pakollinen ydintuotos ei kasva.

Tukireitilläkin oppija tekee itse sisällöllisen päätöksen ja nimeää tarkistuslähteen. Syventävä reitti puolestaan erottaa tekoälyn simuloiman testilukijan aidosta käyttäjähavainnosta. Ne kertovat eri asioista, eikä toista pidä esittää toisen korvikkeena.

## Arvioitava näyttö

Hyväksyttävä työ sisältää alkuperäisen luonnoksen, lopullisen version, vähintään kolme perusteltua omaa muutosta, tekoälyn rajatun tarkistuspalautteen sekä vähintään yhden hyväksytyn tai hylätyn ehdotuksen perusteluineen.

Arvioi ennen kaikkea päätösketjun jäljitettävyyttä. Toisen lukijan pitää pystyä näkemään, mitä tekoäly ehdotti, mitä oppija muutti, mitä testilukija huomasi ja miksi lopullinen ratkaisu hyväksyttiin.
