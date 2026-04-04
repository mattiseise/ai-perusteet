# Sanasto

## Token
Pieni pala tekstiä, johon sana tai sanaryhmä jaetaan. Esimerkiksi sana "tekoäly" voi olla 1-2 tokenia. Kielimalli näkee tekstin tokeneina, ei kirjaimina tai kokonaisina sanaina.

## Kielimalli (Language Model)
Tekoälymalli, joka on oppinut tekstin kuvioista ja osaa ennustaa seuraavaa tokenia. ChatGPT, Claude, Gemini ovat kielimalleja. Ne on opittu miljaardeilla tekstin tokeneilla.

## Parametri
Numero kielimallin "aivoissa", jota se oppi koulutuksessa. ChatGPT-3:ssa on 175 miljardia parametria. Ne määrittävät, kuinka malli prosessoi ja ennustaa tekstiä.

## Next-Token Prediction
Kielimallin perusmekanismi: arvaa seuraava tokeni perustuen aikaisempiin tokeneihin ja parametreihin. Malli tekee tämän kerrallaan kunnes vastaus on valmis.

## Koulutusdata (Training Data)
Tekstiaineisto, jolla kielimalli opitaan. GPT-4 on opittu noin 15 triljoona tokenista. Mitä enemmän ja parempi data, sitä parempi malli.

## Hallusinaatio (Hallucination)
Kun kielimalli tuottaa jotain, joka näyttää oikealta, mutta on täysin väärää tai keksittyä. Esimerkiksi tekijän keksiminen tai väärä fakta. Tapahtuu, kun malli arvaa väärän tokenin yhdistelmän.

## Lämpötila (Temperature)
Parametri, joka kontrolloi, kuinka satunnainen mallin valinnat ovat. Matala lämpötila = ennustettavampia vastauksia. Korkea lämpötila = satunnaisempia ja luovempia vastauksia.

## Neurosverkko (Neural Network)
Matemaattinen rakenne, joka jäljittelee ihmisen aivojen verkkoa. Kielimallilla on neurosverkkoja, joissa miljardeja parametreja yhdistävät eri tavoin.

## Embedding
Numeerinen esitys sanasta tai tokenista, jota kielimalli käyttää sisäisesti. Jokainen sana on esitettävä numeroina, jotta malli voi prosessoida sitä matematiikalla.

## Attentio (Attention)
Mekanismi kielimallin sisällä, joka päättää, mihin sanaan tai tokeniin keskittyä vastatessa. Se auttaa mallia näkemään yhteyksiä pitkissä teksteissä.
