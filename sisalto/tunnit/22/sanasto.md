# Sanasto – oppitunti 22: Agentin työkalut

## Työkalu (tool)

Funktio tai ohjelma, jonka agentti kutsuu tehtävänsä suorittamiseksi. Kolme perustyökalua: tiedostot, verkkohaku, komentorivi.

## Tiedostotyökalu (file tool)

Agentti voi lukea ja kirjoittaa tiedostoja. Lukuoikeus antaa pääsyn tietoihin, kirjoitusoikeus antaa vaikutuksen.

## Verkkohakutyökalu (web search tool)

Agentti voi hakea tietoa internetistä. Ajankohtainen tieto, mutta riskit: väärä tieto, kustannukset, yksityisyys.

## Komentorivityökalu (CLI, command-line interface tool)

Agentti voi ajaa järjestelmäkomentoja (komentorivikomentoja). Voimakkain työkalu, myös vaarallisin. Sallittujen kohteiden luettelo on kriittinen.

## Sallittujen kohteiden luettelo

Luettelo asioista, joita agentti saa tehdä. Hyväksytyt komennot, hakusivustot, kansiot.

## Minimioikeusperiaate (principle of least privilege)

Anna agentille vain minimaalinen pääsy, jonka se tarvitsee. Rajoitus tekee järjestelmästä turvallisemman.

## Orkestraattori (orchestrator)

Harnessin osa, joka koordinoi työkalujen käyttöä. Kielimalli ehdottaa rakenteista kutsua, mutta orkestraattori tarkistaa työkalun ja oikeudet, suorittaa kutsun sekä palauttaa tuloksen tai virheen mallille.

## API (Application Programming Interface)

Rajapinta, jonka kautta agentti kommunikoi muiden ohjelmien kanssa. Esim. varastojärjestelmä, pankkijärjestelmä.

## Loggaus (logging)

Kirjaus siitä, mitä agentti tekee. Jokainen funktiokutsu, API-kutsu ja päätös tallennetaan.

## Riskinhallinta (risk management)

Suunnittelu siihen, mitä tapahtuu, jos agentti tekee virheen. Neljä kerrosta: validointi, rajoitus, seuranta, palautuminen.

## Hiekkalaatikko (sandbox)

Eristetty ympäristö, jossa agentti ei voi vaikuttaa oikeaan järjestelmään. Turvallinen testaus.

## API-avain (API key)

Tunnus, jolla agentti todistaa oikeutensa käyttää palvelua. Salassa pidettävä, ei lokeihin.

## CSV (Comma-Separated Values)

Tekstitiedostomuoto, jossa tiedot ovat rivillä pilkuilla erotettuja. Helppo lukea ja käsitellä.

## JSON (JavaScript Object Notation)

Tekstitiedostomuoto, jossa tiedot ovat rakenteiset. Agentti käyttää sitä konfiguraatioissa.

## MCP (Model Context Protocol)

Avoin standardi, joka määrittelee yhteisen tavan kytkeä työkalu agenttiin: sama työkalu toimii eri agenteissa. Julkaistu vuonna 2024, ja vuonna 2026 se on alan yleinen käytäntö.

## Konnektori (connector)

Valmisagentin liitin ulkoiseen palveluun tai tietolähteeseen, kuten sähköpostiin, kalenteriin tai tiedostoihin. Perustuu MCP:n kaltaiseen standardikytkentään.

---
