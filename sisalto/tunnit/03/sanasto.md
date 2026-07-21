# Sanasto

## Token

Pieni pala tekstiä, joihin sana tai sanaryhmä jaetaan. Esimerkiksi sana "tekoäly" voi olla 1–2 tokenia. Kielimalli näkee tekstin tokeneina, ei kirjaimina tai kokonaisina sanoina.

## Kielimalli (Language Model)

Tekoälymalli, joka on oppinut tekstin kuvioita ja osaa ennustaa seuraavaa tokenia. Kielimalli koulutetaan suurella tekstiaineistolla.

## Parametri

Koulutuksessa opittu numeerinen arvo, joka vaikuttaa siihen, miten malli käsittelee syötettä ja muodostaa ennusteita. Suuressa kielimallissa parametreja voi olla hyvin paljon.

## Next-Token Prediction

Kielimallin perusmekanismi: seuraavan tokenin arvaaminen aikaisempien tokenien ja parametrien perusteella. Malli tekee tämän yksi kerrallaan, kunnes vastaus on valmis.

## Koulutusdata (Training Data)

Tekstiaineisto, jonka esimerkeistä kielimalli oppii koulutuksessa. Aineiston määrän lisäksi sen laatu, kattavuus ja käsittely vaikuttavat mallin toimintaan.

## Hallusinaatio (Hallucination)

Tilanne, jossa kielimalli tuottaa jotain, joka näyttää oikealta, mutta on täysin väärää tai keksittyä. Esimerkiksi tekijän keksiminen tai väärä fakta. Näin tapahtuu, kun malli arvaa väärän tokeniyhdistelmän.

## Lämpötila (Temperature)

Parametri, joka kontrolloi, kuinka satunnaisia mallin valinnat ovat. Matala lämpötila = ennustettavampia vastauksia. Korkea lämpötila = satunnaisempia ja luovempia vastauksia.

## Neuroverkko (Neural Network)

Matemaattinen kerrosrakenne, jossa opitut parametrit muokkaavat tiedon kulkua. Historiallinen inspiraatio liittyy löyhästi biologisiin neuroneihin, mutta neuroverkko ei jäljittele ihmisaivojen toimintaa.

## Embedding

Numeerinen esitys sanasta tai tokenista, jota kielimalli käyttää sisäisesti. Jokainen sana on esitettävä numeroina, jotta malli voi prosessoida sitä matematiikan avulla.

## Attention

Mekanismi kielimallin sisällä, joka päättää, mihin sanaan tai tokeniin keskittyä vastatessa. Se auttaa mallia näkemään yhteyksiä pitkissä teksteissä.

---
