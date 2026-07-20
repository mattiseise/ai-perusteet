# Rakennuspalikka 1 — Promptipankin ensimmäinen kortti

> Tämä on ensimmäinen kolmesta rakennuspalikasta. Tunnin tuotoksena syntyy yksi huolellisesti testattu ja uudelleen käytettävä promptikortti — ei pitkä lista kokeilemattomia prompteja.

## Mitä teet?

Valitset yhden omassa arjessa, opiskelussa tai työssä toistuvan tehtävän. Rakennat sitä varten promptikortin, testaat kaksi versiota samalla aineistolla ja perustelet, mikä muutos paransi tulosta.

Kortista tehdään myöhemmin promptipankin ensimmäinen osa. Tunnilla 17 hyödynnät sen toimivaa rakennetta bottisi järjestelmäpromptin kirjoittamisessa.

Työ etenee tarkoituksella yhdestä päätöksestä seuraavaan. Ensin rajaat tehtävän, sitten kirjoitat arvioitavan kortin ja vasta sen jälkeen kokeilet muutosta. Näin lopputulos ei ole vain hyvältä vaikuttava prompti, vaan dokumentoitu ratkaisu, jonka toimintaa osaat selittää.

## Vaihe 1 — Valitse toistuva tehtävä

Valitse tehtävä, jonka lopputuloksen osaat itse arvioida. Esimerkiksi:

- asiakasviestin tai tiedotteen luonnostelu
- vaikean käsitteen selittäminen tietylle yleisölle
- palautteen jäsentäminen teemoiksi
- opiskelusuunnitelman laatiminen annetun aineiston perusteella
- käyttöohjeen muokkaaminen aloittelijalle sopivaksi

Kirjoita yhdellä lauseella: **Mitä teen, kenelle ja mihin lopputulosta käytetään?**

Esimerkiksi kokousmuistiinpanojen muuttaminen toimintakohdiksi on riittävän rajattu tehtävä, jos osaat tarkistaa lähteestä tehtävät, vastuuhenkilöt ja määräajat. Pelkkä ”tiivistä tekstejä” jää liian väljäksi, koska eri teksteissä onnistuminen tarkoittaa eri asioita.

## Vaihe 2 — Kirjoita kortin versio 1

Täytä promptikortti:

Älä täytä rivejä toisistaan irrallisina. Käyttötilanne kertoo, miksi korttia tarvitaan, tavoite kertoo halutun muutoksen ja laatukriteerit kertovat, mistä onnistuminen myöhemmin nähdään. Jos nämä eivät sovi yhteen, tarkenna tehtävää ennen ensimmäistä ajoa.

| Osa | Sisältö |
| --- | --- |
| Kortin nimi |  |
| Käyttötilanne |  |
| Tavoite |  |
| Käyttäjä tai yleisö |  |
| Lähdeaineisto |  |
| Työvaiheet |  |
| Haluttu muoto |  |
| Tarkistus tai laatukriteerit |  |

Kirjoita kortin pohjalta ensimmäinen prompti. Merkitse vaihdettavat kohdat hakasulkeisiin, esimerkiksi `[yleisö]`, `[lähdeaineisto]` ja `[pituus]`. Näin promptia voi käyttää uudelleen ilman, että koko teksti kirjoitetaan alusta.

## Vaihe 3 — Testaa hallitusti

Anna prompti valitsemallesi tekoälypalvelulle. Tallenna:

- käytetty prompti
- syöte tai lähdeaineisto
- saatu vastaus
- kaksi havaintoa siitä, mikä toimii
- yksi nimetty ongelma

Arvioi vastausta ennen seuraavaa versiota. Älä muuta samalla kertaa kaikkea.

Kirjoita ongelma havaintona. ”Vastaus on huono” ei vielä kerro, mitä pitäisi korjata. ”Vastaus lisäsi määräajan, jota lähteessä ei ollut” nimeää sekä virheen että kohdan, johon seuraavan version muutos voidaan kohdistaa.

## Vaihe 4 — Tee yksi perusteltu muutos

Valitse yksi ongelmaan liittyvä muutos. Voit esimerkiksi:

- tarkentaa yleisöä
- nimetä lähdeaineiston selvemmin
- jakaa tehtävän vaiheisiin
- määrittää vastausrakenteen
- lisätä laatukriteerin tai tarkistuspyynnön

Valitse muutos siksi, että se vastaa nimeämääsi ongelmaan. Jos lähteen tietoja puuttui, ulkoasun vaihtaminen ei ratkaise asiaa. Jos taas sisältö säilyi mutta rakenne oli hankala käyttää, täsmällinen vastausmuoto voi olla oikea muutos.

Kirjoita **versio 2** ja aja se samalla lähtöaineistolla. Jos vaihdat sekä promptin että aineiston, et pysty päättelemään, mistä ero johtui.

## Vaihe 5 — Vertaa näyttöä

Täytä vertailu:

| Arviointikohta | Versio 1 | Versio 2 | Näyttö |
| --- | --- | --- | --- |
| Vastaako tehtävään? |  |  |  |
| Sopiiko yleisölle? |  |  |  |
| Käyttääkö lähdeaineistoa oikein? |  |  |  |
| Onko muoto käyttökelpoinen? |  |  |  |
| Mitä pitää vielä tarkistaa? |  |  |  |

Kirjoita lopuksi johtopäätös:

> Muutin promptissa ____. Muutos vaikutti tulokseen näin: ____. Päätelmä perustuu tähän havaintoon: ____.

Hyvä johtopäätös ei lupaa, että kortti toimii kaikissa tilanteissa. Se kertoo täsmällisesti, mitä tällä aineistolla tapahtui ja mikä kannattaa testata seuraavaksi. Tämä rajaus tekee kortista luotettavamman, ei heikomman.

## Tekoälyvaihe — haasta arvio

```text
Tässä ovat saman tehtävän promptiversiot 1 ja 2 sekä niiden vastaukset.
Oma johtopäätökseni on: [kirjoita]. Esitä kolme kysymystä, joilla
voin tarkistaa, perustuuko päätelmäni näkyvään eroon vai omaan
ennakko-oletukseeni. Älä valitse voittajaa puolestani.
```

Tee tarvittaessa yksi korjaus johtopäätökseesi.

---

**Tallennettava tuotos:** yksi promptikortti, versiot 1 ja 2, molemmat vastaukset, vertailutaulukko sekä yhden muutoksen vaikutusta koskeva johtopäätös.

Kun kortti toimii, voit myöhemmin lisätä pankkiin uusia kortteja samalla rakenteella. Yksi testattu kortti on arvokkaampi kuin seitsemän promptia, joiden toimivuudesta et osaa sanoa mitään.

Tallenna kortti niin, että palaat myöhemmin myös sen perusteluihin. Pelkkä lopullinen prompti kertoo, mitä kirjoitit. Versiot ja havaintosi kertovat, miksi päädyit juuri siihen muotoon.

**1 / 3 rakennuspalikkaa kerätty**
