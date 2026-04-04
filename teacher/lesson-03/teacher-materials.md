# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

1. Opiskelijat voivat selittää, kuinka kielimalli toimii: next-token prediction.
2. Opiskelijat ymmärtävät, että parametrit ovat numero, joita opitaan datasta.
3. Opiskelijat tunnistavat hallusinaatiot ja ymmärtävät, miksi ne ovat vaarallisia.
4. Opiskelijat näkevät yhteyden koulutus-datan ja mallin käyttäytymisen välillä.

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: "Kielimalli ymmärtää tekstiä."
**Korjaus:** Ei. Se ennustaa seuraavaa tokenia todennäköisyyden perusteella. Se näyttää ymmärtävän, koska koulutusdata sisälsi älykkäitä tekstejä. Mutta sisäisesti se on vain matematiikkaa.

### Väärinkäsitys 2: "Parametrit ovat säännöt, jotka malli oppi."
**Korjaus:** Ei. Parametrit ovat numeroita — painoja. Miljardeja numeroita yhdessä määrittävät käyttäytymisen, mutta ne eivät ole erillisiä "sääntöjä".

### Väärinkäsitys 3: "Jos malli hallusinoivoi, se valehtelee tarkoituksella."
**Korjaus:** Ei. Se arvaa väärin. Se ei tiedä, onko vastaus oikein vai väärä. Se ei ole tietoinen.

### Väärinkäsitys 4: "Suurempi malli on aina parempi."
**Korjaus:** Suuremmalla mallilla on enemmän parametreja, mikä auttaa. Mutta jos se on opittu huonolla datalla, se on huonompi. Koko ja data ratkaisevat.

### Väärinkäsitys 5: "Lämpötila on merkitty mielentila — jos se on kuuma, malli on 'poissaolevaisempi'."
**Korjaus:** Lämpötila on matemaattinen parametri, ei mielentila. Se kontrolloi satunnaisuuden tasoa satunnaisen näytteitä-ottamisessa seuraavasta tokenista.

## Opettajan fasilitointiohjeet

### Ennen luokkaa
- Testaa live-demo ChatGPT:llä ja hallusinaatio-esimerkit.
- Ymmärrä itse next-token prediction perinpohjaisesti — tämä on avain koko lohkolle.
- Etsi joitain artikkeleita, joissa selitetään, miten transformers ja attention toimivat. Sinun ei tarvitse osata kaikkea, mutta perusidea auttaa.

### Luokan aikana
- **Aloita käytännöstä.** Arvaa sanoja ChatGPT:n kanssa ennen kuin teoriaa.
- **Näytä live-hallusinaatio.** Konkreettinen esimerkki ymmärtää paremmin kuin selitys.
- **Yhdistä ammattilaisuuteen.** Kysy aina: "Miten tämä vaikuttaa sinun tulevaan ammattiin?"

### Yleisten opiskelija-kysymysten vastaukset

**Q: "Jos malli vain arvaa sanoja, kuinka se osaa vastata monimutkaisiin kysymyksiin?"**
A: Oikea kysymys! Se osaa, koska koulutusdata sisälsi monimutkaisesti vastauksia. Malli näkyi kuvioita "kun kysymys on X, vastaus on yleensä Y". Mutta se ei oikeasti *ratkaise* — se toistaa kuvioita, joita näki.

**Q: "Voiko hallusinaatiot poistaa?"**
A: Ei täysin. Mutta voit pienentää niitä: käytä parempaa koulutus-dataa, validoi vastaukset, käytä matalaammalla lämpötilaa kriittissä tehtävissä, yhdistä muihin työkaluihin.

**Q: "Kuinka paljon parametreja minulla on aivoissani?"**
A: Ei tiedetä tarkalleen, mutta ihmisen aivot ovat hyvin erilaisia malleista. Aivot eivät ole vain parametreja — ne ovat biologisia ja dynaamisia.

## Arviointivinkit

### Perusymmärryksen tarkistaminen
- Kysy: "Miten kielimalli ennustaa seuraavaa sanaa?" (Vastaus: arvaa todennäköisyyden perusteella parametrien perusteella.)
- Kysy: "Mitä hallusinaatio on?" (Vastaus: kun malli arvaa väärän sanan yhdistelmän vakuuttavasti.)

### Kriittinen ajattelu
- Näytä hallusinaatio. Kysy: "Mistä tiesit, että se on väärä?" (Vastaus: tarkistetaan muista lähteistä, koska malli näyttää uskottavalta.)
- Kysy: "Mihin ammattiin hallusinaatiot ovat vaarallisimmat?" (Vastaus: missä tahansa, missä tarkkuus ratkaisee — lääketiede, oikeus, IT-tietoturva...)

### Itsearviointi
- "Ymmärrän, kuinka next-token prediction toimii" — Täysin samaa mieltä / Jokseenkin / En
- "Näen, miksi hallusinaatiot ovat vaarallisia" — Täysin samaa mieltä / Jokseenkin / En
