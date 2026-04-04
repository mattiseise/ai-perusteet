# Lesson 24: Sanasto — Työkalut agenteissa: tiedostot, haku ja CLI

| Termi | Määritelmä |
|-------|-----------|
| **Työkalu** (tool) | Instrumentti, jonka kautta agentti voi vaikuttaa maailmaan — esim. tiedostojen lukeminen, verkkohaku, CLI-komennot. |
| **Tiedostojärjestelmä** (file system) | Agentti voi lukea ja kirjoittaa tiedostoja. Tämä antaa sille pääsyn tietoihin ja kyvyn kirjoittaa raportteja. |
| **Verkkohaku** (web search) | Agentti voi hakea tietoa internetistä, joten sillä on pääsy ajankohtaisiin tietoihin. |
| **CLI** (Command Line Interface) | Agentti voi ajaa palvelinkomentoja — voimakas työkalu, mutta vaatii rajoituksia turvallisuuden vuoksi. |
| **Käyttöoikeus** (permission) | Mitä oikeuksia agentti tarvitsee? Lukea, kirjoittaa, poistaa? |
| **Whitelist** | Sallittujen komentojen lista — agentti voi ajaa vain näitä komentoja. |
| **Sandbox** (hiekkalaatikko) | Erillinen, turvallinen ympäristö, jossa agentti voi ajaa komentoja ilman pääsyä todelliseen järjestelmään. |
| **Orkestraattori** (orchestrator) | Agentti ei ole yksi neuroverkko vaan orkestraattori, joka kutsuu eri työkaluja ja yhdistää niiden tulokset. |
| **Prosessiketju** | Sarja vaiheita, jotka tapahtuvat järjestyksessä, joissa jotkut vaiheet vaativat hyväksyntää. |
