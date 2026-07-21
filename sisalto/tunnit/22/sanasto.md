# Sanasto – oppitunti 22: Agentin työkalut

## Työkalu (tool)

Rajattu kyvykkyys, jonka avulla agentti saa tietoa tai tekee nimetyn toiminnon. Työkalulla on syöte, tulos, oikeudet ja virhetilanne.

## Tiedostotyökalu (file tool)

Agentti voi lukea ja kirjoittaa tiedostoja. Lukuoikeus antaa pääsyn tietoihin, kirjoitusoikeus antaa vaikutuksen.

## Verkkohakutyökalu (web search tool)

Agentti voi hakea tietoa internetistä. Ajankohtainen tieto, mutta riskit: väärä tieto, kustannukset, yksityisyys.

## Rajattu toimintotyökalu

Työkalu, jolla agentti tekee nimetyn toiminnon, kuten lisää luonnoksen taulukkoon tai valmistelee viestin. Oikeus rajataan kohteeseen ja toimintoon.

## Sallittujen kohteiden luettelo

Luettelo asioista, joita agentti saa tehdä. Siinä nimetään esimerkiksi hyväksytyt lähteet, tiedostot, vastaanottajat ja toimintotyypit.

## Minimioikeusperiaate (principle of least privilege)

Anna agentille vain minimaalinen pääsy, jonka se tarvitsee. Rajoitus tekee järjestelmästä turvallisemman.

## Orkestraattori (orchestrator)

Agentin ohjauskehyksen osa, joka koordinoi työkalujen käyttöä. Kielimalli ehdottaa toimintoa, mutta ohjauskehys tarkistaa työkalun ja oikeudet, suorittaa kutsun sekä palauttaa tuloksen tai virheen mallille.

## Liitin

Valmis yhteys, jonka kautta n8n voi käyttää toista palvelua. Aloittelijan ei tarvitse ohjelmoida yhteyttä itse.

## Loggaus (logging)

Kirjaus siitä, mitä agentti tekee. Tehtävän kannalta olennaiset valinnat, työkalujen käytöt, tulokset ja virheet tallennetaan ilman tarpeettomia henkilötietoja tai salaisuuksia.

## Riskinhallinta (risk management)

Suunnittelu siihen, mitä tapahtuu, jos agentti tekee virheen. Neljä kerrosta: validointi, rajoitus, seuranta, palautuminen.

## Hiekkalaatikko (sandbox)

Eristetty ympäristö, jossa agentti ei voi vaikuttaa oikeaan järjestelmään. Turvallinen testaus.

## Tunnistetieto

Salainen tieto, jolla palvelu tunnistaa käyttäjän tai järjestelmän. Sitä ei kirjoiteta promptiin eikä lokiin.

## CSV (Comma-Separated Values)

Tekstitiedostomuoto, jossa tiedot ovat rivillä pilkuilla erotettuja. Helppo lukea ja käsitellä.

## Työkalusopimus

Proosana tai rakenteisesti kuvattu sopimus siitä, mitä tietoa työkalu saa, mitä se palauttaa, mitä se ei saa tehdä ja miten virhe käsitellään.

---
