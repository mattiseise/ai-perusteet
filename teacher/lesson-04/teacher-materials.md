# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

1. Opiskelijat ymmärtävät, että konteksti on kaiken tekoälyviestinnän perusta ja että se koostuu roolista, taustatieto, tavoitteesta, rajauksista ja esimerkeistä.

2. Opiskelijat pystyvät tunnistamaan eron "hyvän promptin" ja "hyvän kontekstin" välillä, ja he näkevät, että konteksti, ei prompti, määrittää vastauksen hyödyllisyyden.

3. Opiskelijat pystyvät rakentamaan omasta IT-ongelmastaan selkeän, terävän kontekstin ja käyttämään sitä tekoälyyn keskustellessaan.

4. Opiskelijat ymmärtävät, että kontekstin rakentaminen säästää aikaa ja antaa ammattimaisia, käyttökelpoisia vastauksia.

## Yleisiä väärinkäsityksiä

**Väärinkäsitys 1: "Hyvä prompti = hyvä vastaus"**
- **Todellisuus:** Hyvä konteksti = hyvä vastaus. Prompti on kysymys, konteksti on pohja. Voit antaa saman promptin kahdelle tekoälylle eri kontekstilla ja saada täysin erilaiset vastaukset.
- **Korjaus:** Näytä opiskelijoille konkreettinen esimerkki (tehtävä 4.1). Kerro: "Näet, kuinka saman kysymyksen vastaus muuttuu drastisesti kontekstin mukaan."

**Väärinkäsitys 2: "Konteksti tarkoittaa 'vain pitkää tekstiä'"**
- **Todellisuus:** Konteksti on rakennettu: se sisältää viisi spesifistä osaa — rooli, taustatieto, tavoite, rajaukset, esimerkki. Pitkä, sekava teksti ei ole hyvä konteksti.
- **Korjaus:** Opeta viiden komponentin malli selkeästi (tehtävä 4.2). Näytä, kuinka lyhyt, jäsennelty konteksti on parempi kuin pitkä, sekavirta teksti.

**Väärinkäsitys 3: "Tekoäly ymmärtää aina, mitä tarkoitan"**
- **Todellisuus:** Tekoäly tekee oletuksia puuttuvan tiedon paikalla — ja arvaukset ovat usein väärät.
- **Korjaus:** Käytä "Miksi huono konteksti tuottaa huonoa jälkeä" -osiota. Kerro: "Jos jätät kontekstin vaillinaiseksi, tekoäly arvaa — eikä arvaa oikein."

**Väärinkäsitys 4: "Konteksti on ylimääräinen; liian pitkä vastaus on parempi"**
- **Todellisuus:** Konteksti tekee vastauksen lyhyemmäksi JA hyödyllisemmäksi, koska tekoäly tietää, mihin kohdistaa.
- **Korjaus:** Vertaa tehtävä 4.1:ssä vastausten pituuksia. Näytä, että konteksti auttaa tekoälyä säilyttämään vain relevantin tiedon.

## Opettajan fasilitointiohjeet

### Ennen oppituntia
- Lue itse oppilasmateriaalit ja tutustu viiden komponentin malliin.
- Valitse konkrettiset IT-esimerkit, joiden tiedät resonoivan opiskelijoidesi kanssa. (Ei liian edistyneet, ei liian yksinkertaiset.)
- Testaa tehtävä 4.1 etukäteen: käytä oikeaa tekoälyä ja näe, mitä eroja tulee.

### Oppitunnin aikana
- **Avaa johdanto-skenaariolla:** "IT-tukihenkilö saa viestin 'Tietokone ei toimi.'" Pyydä opiskelijoita pohtimaan: mitä he tekisivät seuraavaksi? (He tajuavat, että tarvitsevat lisätietoa — tämä on konteksti!)

- **Korostaa viiden komponentin mallia:** Piirrä malli tauluun. Käytä tehtävää 4.2, vaikka opiskelijat rakentaisivat yhdessä mallia selkeästi näkyvät vaiheet.

- **Anna konkreettiset esimerkit:** Älä vain puhu abstraktisti. Näytä:
  - Huono: "Kuinka debugaan ohjelmaa?" → konteksti puuttuu
  - Hyvä: "Olen kirjoittanut Python-ohjelman, joka... (taustatieto), haluan oppia debuggaamaan systematisesti... (tavoite)" → selkeä vastaus

- **Omaksu opiskelijoiden IT-maailma:** Käytä esimerkkejä, jotka ovat relevantteja heidän opiskelualleen. Jos he tekevät Linux-projektia, käytä Linux-esimerkkejä. Jos he tekevät tietokantaprojektia, käytä SQL-esimerkkejä.

### Yleisiä haasteita ja ratkaisuja

**Haaste: "Opiskelijat antavat silti liian yleiset kontekstit"**
- Ratkaisu: Toista vaihe 5 (esimerkki) stressaavasti. Kerro: "Tekoäly ei näe mitään, jos et näytä sitä. Näytä virheilmoitus, näytä koodi, näytä ruutukaappaus."

**Haaste: "Konteksti kuulostaa opiskelijoista 'liian formaalilta' tai 'liian pitkältä'"**
- Ratkaisu: Näytä, että konteksti ei tarvitse olla kirjoitus. Voit käyttää:
  - Luetteloa: "Rooli: opiskelijana. Taustatieto: neljä viikkoa Linux-kurssilla. Tavoite: debugata SSH..."
  - Lyhyitä kappaleita: Konteksti voi olla 2-3 lausetta per komponentti.

**Haaste: "Opiskelijat kysyvät: 'Mutta mikä tekoälyyn näyttää kontekstin kirjoittamisen merkinneet?'"**
- Ratkaisu: Näytä konkreettisesti. Tehtävä 4.1 osoittaa tämän — jokainen opiskelija näkee, että vastaukset ovat erilaiset. Tämä on riittävä todistus.

## Arviointivinkit

**Epävirallinen arviointi tehtävä 4.1 jälkeen:**
- Katso opiskelijoiden täyttämää vertailutaulukkoa. Osoittaako se, että he näkivät eroa vastausten välillä?
- Kuuntele pohdinnan: Voitko kuulla sanoja kuten "spesifisempi", "relevantimpi", "käytettävämpi"? Hyviä merkkejä.
- Jos opiskelija sanoo "ei ollut paljon eroa", kysy: "Mitä kontekstin osaa lisäsimme?" Auta häntä näkemään ero.

**Epävirallinen arviointi tehtävä 4.2 jälkeen:**
- Lue opiskelijoiden konteksti-kysymykset. Sisältävätkö ne kaikki viisi osaa?
- Etsi kohdat, joissa on spesifisiä esimerkkejä (koodi, virheilmoitus, ruutukaappaus). Nämä osoittavat ymmärrystä.
- Keskustele ryhmän kanssa: "Mitä kontekstin osaa harkitsit tärkeimmäksi omassa ongelmassasi? Miksi?"

**Kehittämisalueita:**
- Jos opiskelija jättää esimerkit pois: "Näytä minulle virheilmoituksesi. Kuinka tekoäly voi auttaa, jos se ei näe virhettä?"
- Jos rooli on epäselvä: "Ketkä olet tässä? Kuinka paljon kokemusta sinulla on?" Auta häntä articuloimaan itseään.

## Jatkava integraatio tulevilla oppitunneilla

- **Oppitunti 5 (Konteksti-ikkuna):** Rakennat tällä opituilla kontekstin-taidoilla, mutta nyt opiskelijat näkevät, mitä tapahtuu, kun konteksti-ikkuna on rajallinen. Hyvät kontekstit oppitunnilla 4 tekevät oppitunnin 5 käsittelystä luontevampaa.

- **Oppitunti 6 (Multimodaalisuus):** Konteksti käsittelee myös kuvia, lokkeja ja muita modaliteetteja — kaikki on kontekstia. Viiden komponentin malli laajenee: "Entä jos esimerkki on kuvakaappaus, ei teksti?"

Tämä oppitunti on kurssin selkäranka. Pidetään siitä huoli!
