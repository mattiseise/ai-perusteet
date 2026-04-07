# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

1. Opiskelijat voivat selittää, kuinka kielimalli toimii: next-token prediction.
2. Opiskelijat ymmärtävät, että parametrit ovat numeroita, joita opitaan datasta.
3. Opiskelijat tunnistavat hallusinaatiot ja ymmärtävät, miksi ne ovat vaarallisia.
4. Opiskelijat näkevät yhteyden koulutusdatan ja mallin käyttäytymisen välillä.

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: "Kielimalli ymmärtää tekstiä."
**Korjaus:** Ei. Se ennustaa seuraavaa tokenia todennäköisyyksien perusteella. Se näyttää ymmärtävän, koska koulutusdata sisälsi älykkäitä tekstejä. Mutta sisäisesti se on vain matematiikkaa.

### Väärinkäsitys 2: "Parametrit ovat sääntöjä, jotka malli oppi."
**Korjaus:** Ei. Parametrit ovat numeroita eli painoja. Miljaardit numerot yhdessä määrittävät käyttäytymisen, mutta ne eivät ole erillisiä "sääntöjä".

### Väärinkäsitys 3: "Jos malli hallusinoi, se valehtelee tarkoituksella."
**Korjaus:** Ei. Se arvaa väärin. Se ei tiedä, onko vastaus oikein vai väärä. Se ei ole tietoinen.

### Väärinkäsitys 4: "Suurempi malli on aina parempi."
**Korjaus:** Suuremmassa mallissa on enemmän parametreja, mikä auttaa. Mutta jos se on opetettu huonolla datalla, se on huonompi. Koko ja data ratkaisevat.

### Väärinkäsitys 5: "Lämpötila kuvaa mielentilaa — jos se on kuuma, malli on 'poissaolevaisempi'."
**Korjaus:** Lämpötila on matemaattinen parametri, ei mielentila. Se kontrolloi satunnaisuuden tasoa seuraavan tokenin satunnaisessa näytteenotossa.

## Opettajan fasilitointiohjeet

### Ennen luokkaa
- Testaa live-demo ChatGPT:llä ja hallusinaatioesimerkit.
- Ymmärrä itse next-token prediction perinpohjaisesti — tämä on koko lohkon avain.
- Etsi joitakin artikkeleita, joissa selitetään, miten transformers ja attention toimivat. Sinun ei tarvitse osata kaikkea, mutta perusidea auttaa.

### Luokan aikana
- **Aloita käytännöstä.** Arvaa sanoja ChatGPT:n kanssa ennen teoriaa.
- **Näytä live-hallusinaatio.** Konkreettinen esimerkki auttaa ymmärtämään paremmin kuin pelkkä selitys.
- **Yhdistä ammattilaisuuteen.** Kysy aina: "Miten tämä vaikuttaa sinun tulevaan ammattiisi?"

### Yleisten opiskelijakysymysten vastaukset

**Q: "Jos malli vain arvaa sanoja, kuinka se osaa vastata monimutkaisiin kysymyksiin?"**
A: Oikea kysymys! Se osaa, koska koulutusdata sisälsi monimutkaisia vastauksia. Malli näki kuvioita: "Kun kysymys on X, vastaus on yleensä Y." Mutta se ei oikeasti *ratkaista* — se toistaa kuvioita, joita se näki.

**Q: "Voiko hallusinaatiot poistaa?"**
A: Ei täysin. Mutta niitä voi vähentää: käytä parempaa koulutusdataa, validoi vastaukset, käytä matalampaa lämpötilaa kriittisissä tehtävissä ja yhdistä muihin työkaluihin.

**Q: "Kuinka paljon parametreja minulla on aivoissani?"**
A: Ei tiedetä tarkalleen, mutta ihmisen aivot ovat hyvin erilaisia kuin mallit. Aivot eivät ole vain parametreja — ne ovat biologisia ja dynaamisia.

## Arviointivinkit

### Perusymmärryksen tarkistaminen
- Kysy: "Miten kielimalli ennustaa seuraavan sanan?" (Vastaus: se arvaa todennäköisyyksien perusteella parametrien avulla.)
- Kysy: "Mitä hallusinaatio on?" (Vastaus: kun malli arvaa väärän sanayhdistelmän vakuuttavasti.)

### Kriittinen ajattelu
- Näytä hallusinaatio. Kysy: "Mistä tiesit, että se on väärä?" (Vastaus: tarkistetaan muista lähteistä, koska malli näyttää uskottavalta.)
- Kysy: "Missä ammateissa hallusinaatiot ovat vaarallisimpia?" (Vastaus: missä tahansa, missä tarkkuus ratkaisee — lääketiede, oikeus, IT-tietoturva...)

### Itsearviointi
- "Ymmärrän, kuinka next-token prediction toimii" — Täysin samaa mieltä / Jokseenkin / En
- "Näen, miksi hallusinaatiot ovat vaarallisia" — Täysin samaa mieltä / Jokseenkin / En

---

## Formatiivinen tarkistuspiste — Todistusaineisto 1

### Tavoite
Opiskelija prosessoi oppitunnin 3 ydinkäsitteet omin sanoin. Todistusaineisto toimii sekä formatiivisena arviointina että rakennuspalikkana Teoria-osion arviointitehtävälle.

### Mitä etsiä palautuksesta
- **Ydinajatus ymmärretty:** Opiskelija selittää, että malli ennustaa seuraavan tokenin todennäköisyyksien perusteella, ei "ymmärrä" tai "tiedä"
- **Yleinen väärinymmärrys:** "Malli hakee vastauksen tietokannasta" tai "malli tietää faktat" → ohjaa kohti tilastollista ennustamista
- **Luotettavuuskysymys:** Opiskelija yhdistää ennustamisen epäluotettavuuteen — "koska malli ei tiedä, onko vastaus totta, vaan mikä on todennäköisin jatko"

### Palautteen antaminen
Anna lyhyt (2–3 lauseen) palaute ennen seuraavaa oppituntia. Keskity yhteen asiaan:
- Jos ydinajatus on oikein: "Hyvä — muista tämä, kun pääset oppituntiin 9"
- Jos väärinymmärrys: "Tarkista vielä: hakeeko malli vastauksen vai ennustaako se? Tämä ero on tärkeä myöhemmin"