# Työkalut agenteissa: tiedostot, haku ja CLI

## Johdanto: Agentti näkee maailman työkalujen kautta

Agentti ei koskaan näe maailmaa suoraan. Se näkee sen vain **työkalujen kautta** — instrumenttien kautta, joilla se voi lukea, kirjoittaa, hakea ja toimia. Nämä työkalut ovat agenttijärjestelmän "aistit" ja "kädet".

Kuvittele sokea henkilö, jolla on apuvälineet: sormenpää (kosketus), ääni (kuuntelu) ja keppi (etäisyys). Nämä apuvälineet ovat hänen aisteistaan. Ilman niitä hän ei näkisi tai tekisi mitään. Samalla tavalla agentti tarvitsee työkaluja.

Tässä oppitunnissa käsittelemme kolme perustyökalua: **tiedostojen lukeminen ja kirjoittaminen**, **verkkohaku** ja **CLI-komentojen ajo**.

## Työkalu 1: Tiedostot — agentti lukee ja kirjoittaa

Agentti voi lukea tiedostoja tai kirjoittaa niitä. Tämä on yksinkertainen, mutta tehokas työkalu.

**Lukeminen:**
- Agentti voi lukea dokumentteja (PDF, txt, CSV)
- Agentti voi lukea konfiguraatiotiedostoja
- Agentti voi lukea lokeja

Esimerkiksi: IT-agentti voi lukea palvelimen lokeja ja sanoa "näen tässä virheen klo 15:30 — tämä oli vika."

**Kirjoittaminen:**
- Agentti voi kirjoittaa raportteja
- Agentti voi kirjoittaa lokeja omista toimistaan
- Agentti voi kirjoittaa tiedostoja muille ohjelmistoille käsiteltäviksi

Esimerkiksi: Myyntiagentti voi kirjoittaa CSV-tiedoston, jossa on listan kaikista uusista asiakkaista, jonka Excel voi lukea.

**Käyttöoikeudet (permissions) ovat kriittisiä:**
- Mitä oikeuksia agentti tarvitsee? (lukea, kirjoittaa, poistaa?)
- Mitkä tiedostot sille annetaan? (kaikki vai vain tiettyjä?)
- Voiko se poistaa tiedostoja vai vain lukea?

Jos agentti saa liian paljon oikeuksia, se voi vahingossa poistaa tärkeitä tiedostoja. Jos se saa liian vähän, se ei voi tehdä mitään.

**Pysähdy hetkeksi: Jos agentti voi kirjoittaa tiedostoihin, mitkä tiedostot olisivat liian herkkiä hänelle käsiteltäväksi?**

## Työkalu 2: Verkkohaku — agentti etsii internetistä

Agentti voi hakea tietoa internetistä käyttämällä hakumoottoria tai API:ta. Tämä antaa sille pääsyn ajankohtaisiin tietoihin.

Ilman verkkohakua agentti on vain se tieto, jonka se sai koulutuksensa aikana. Jos tieto on vanhaa, agentti antaa vanhaa tietoa. Verkkohakulla agentti voi löytää uusimmat tiedot.

Esimerkiksi:
- Asiakas kysyy: "Mikä on tämän osakkeen hinta?" Agentti hakee verkosta → löytää nykyisen hinnan
- Asiakas kysyy: "Mitä tapahtui tänään uutisissa?" Agentti hakee verkosta → löytää tämän päivän uutiset
- Asiakas kysyy: "Kuinka päivitetään Windows?" Agentti hakee verkosta → löytää uusimmat ohjeet

**Haun riskit:**
- Haku voi löytää väärää tietoa (valheita tai väärät sivustot)
- Haku voi olla hidas
- Haku maksaa (jotkut hakupalvelut laskuttavat jokaisen haun)
- Agentti voi hakea liian herkkiä tai yksityisiä tietoja

Ammattilaisena sinun täytyy asettaa rajauksia:
- "Hae vain näiltä sivustoilta"
- "Älä hae henkilökohtaisia tietoja"
- "Hae enintään 3 kertaa per käyttäjän pyynnöstä"

**Pysähdy hetkeksi: Kuvittele agentin, jonka käytät. Mitä tietoa se ei pitäisi hakea verkosta turvallisuussyistä?**

## Työkalu 3: CLI — agentti ajaa komentoja

CLI (Command Line Interface) on kyky ajaa palvelinkomentoja. Tämä on voimakas työkalu, mutta myös vaarallinen.

Agentti voi:
- Luoda kansioita ja tiedostoja
- Poistaa tiedostoja
- Käynnistää ohjelmia
- Muokata asetuksia
- Ja paljon muuta

Esimerkiksi:
- Agentti voi suorittaa "mkdir /backup" → luo varmuuskopioiden kansion
- Agentti voi suorittaa "python script.py" → ajaa Python-skriptin
- Agentti voi suorittaa "rm old_file.txt" → poistaa tiedoston

**CLI:n suurin riski:** Jos agentti voi ajaa mitä tahansa komentoja, se voi vahingolla:
- Poistaa kaikki tiedostot
- Sammuttaa palvelimen
- Muuttaa konfiguraatioita siten, että järjestelmä hajoaa

Siksi sinun täytyy asettaa **rajoitukset**:
- Whitelist: "Agentti saa ajaa vain näitä komentoja: ls, mkdir, cp"
- Ei poisto-oikeuksia: "Agentti voi lukea ja luoda, mutta ei poistaa"
- Erilliset ympäristöt: "Agentti ajaa sisällä "hiekkalaatikko" (sandbox), josta se ei voi vaikuttaa todelliseen järjestelmään"

## Käytännön esimerkki: Yksinkertainen analytics-agentti

Kuvittele agentia, joka analysoi myyntidataa:

**Tiedostot:**
- Lukee: myyntitiedot.csv (kuukausittaiset luvut)
- Kirjoittaa: raportti.txt (yhteenveto)

**Verkkohaku:**
- Hakee: "markkinoiden trendejä" → löytää kilpailijoista tietoa
- Hakee: "asiakasfeedback" → löytää mitä asiakkaat sanovat

**CLI:**
- Ajaa: "python analyze.py" → ajaa analyysiskriptin
- Ajaa: "mv raportti.txt /reports/" → siirtää raportin oikeaan paikkaan

Nämä kolme työkalu yhdessä tekevät agentista hyödyllisen:
1. Se lukee dataa (tiedostot)
2. Se etsii kontekstia (haku)
3. Se tekee työtä (CLI)
4. Se kirjoittaa tulokset (tiedostot)

## Orkestraattori: agentti on orkesteri

Tämä on tärkeä käsite: **agentti ei ole yksi iso neuroverkko, joka tekee kaiken**. Agentti on **orkestraattori**, joka kutsuu eri työkaluja järjestyksessä.

Ajattele orkesteria:
- Kapellimestari ei pelaa jokaista instrumenttia
- Kapellimestari ohjaa, milloin viulunsoittajat soittavat, milloin paukuista soittavat, jne.
- Jokainen instrumentti on erikoistunut

Samalla tavalla agentti:
- Ei ole neuroverkkoa, joka tekee kaiken
- On orkestraattori, joka kutsuu: "Tiedostolukija, lue tämä" → "Analyysityökalu, analysoi" → "Raportin kirjoittaja, kirjoita"

Tämä on agenttien todellinen voima — ne voivat **yhdistää** eri työkaluja ja tehdä monimutkaisia tehtäviä.

## Yhteenveto

Agentti näkee maailman kolmen päätyökalun kautta: **tiedostojen lukeminen ja kirjoittaminen**, **verkkohaku** ja **CLI-komentojen ajo**. Jokainen työkalu on voimakas, mutta vaatii rajoitukset turvallisuuden vuoksi. Agentti ei ole yksi suuri älykäs ohjelma — se on **orkestraattori**, joka kutsuu eri työkaluja ja yhdistää niiden tulokset. Ammattilaisena sinun täytyy ymmärtää, mitä työkaluja agentti tarvitsee, mitä rajoituksia sille pitäisi asettaa, ja miten ne työkalut yhdessä tekevät hyödyllisen systeemin.
