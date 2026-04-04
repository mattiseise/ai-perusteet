# Opiskelutehtävät: Suunnittelumallit — ReAct ja ketjuajattelu

## Projektin aihio 3: Valitse päättelymalli

Tämä on kolmas viidestä projektin aihiosta, jotka keräät Agentit-osion aikana. Käytät näitä aihioita oppitunneilla 26–27, kun rakennat oman n8n-agenttityönkulun ja esittelet sen. Säilytä tämä huolellisesti.

### Tehtävä

Palaa projektin aihioihin 1 ja 2 (oppitunnit 19 ja 21), joissa valitsit ongelman ja suunnittelit muististrategian. Valitse nyt agenttisi päättelymalli. Kirjoita lyhyt perustelu (150–200 sanaa), jossa vastaat kolmeen kysymykseen: Kumpi malli sopii paremmin omaan ongelmaasi — ReAct (ajattele-toimi-ajattele) vai ketjuajattelu (vaihe vaiheelta)? Miksi tämä malli sopii juuri sinun käyttötapaukseesi? Tarvitseeko ongelmasi useamman agentin yhteistyötä (moniagenttijärjestelmä) vai riittääkö yksi agentti?

### Miksi tämä on tärkeä

Päättelymalli määrittää, miten agenttisi ajattelee. ReAct sopii tilanteisiin, joissa agentti tarvitsee reaaliaikaista palautetta työkaluiltaan, kun taas ketjuajattelu sopii tilanteisiin, joissa ongelma on pilkottavissa selkeisiin vaiheisiin. Väärä valinta johtaa joko turhiin iteraatioihin tai liian jäykkään prosessiin. Tämä aihio varmistaa, että valitset tietoisesti — et vain oletuksena.

Alla olevat harjoitustehtävät auttavat sinua ymmärtämään eri päättelymallien vahvuudet ja rajoitukset käytännössä, jotta valintasi projektin aihiossa on perusteltu.

---

## Tehtävä 23.1: ReAct-malli — ajattele, toimi, ajattele uudelleen

### Tavoite
Kokea käytännössä, miten ReAct-prosessi toimii vaihe vaiheelta. Tämä auttaa sinua projektin aihiossa arvioimaan, sopiiko ReAct omaan ongelmaasi.

### Ohjeet

Kuvittele agenttia, joka käsittelee seuraavaa pyyntöä: "Asiakas haluaa tuotteen väriä muuttaa tilauksesta #12345. Väri on sininen, haluttu väri on punainen."

Kirjoita ReAct-prosessi, jossa jokainen vaihe näkyy lokimerkintänä:

```
[AJATTELU]: ...
[TOIMINTA]: ...
[HAVAINTO]: ...
[AJATTELU]: ...
[TOIMINTA]: ...
```

Kirjoita lopuksi yhteenveto: mitä agentti oppi prosessin aikana ja missä kohtaa se olisi voinut tehdä virheen?

---

## Tehtävä 23.2: Ketjuajattelu — vaihe vaiheelta

### Tavoite
Kokea käytännössä, miten ketjuajattelu pilkkoo ongelman selkeisiin vaiheisiin. Tämä auttaa sinua projektin aihiossa arvioimaan, sopiiko ketjuajattelu omaan ongelmaasi.

### Ohjeet

Palautuspyynnön käsittely on hyvä esimerkki ketjuajattelusta. Pyyntö: "Haluan palauttaa tuotteen, joka tuli kolme päivää sitten."

Kirjoita ketjuajatteluprosessi viidessä vaiheessa: selvitä asiakkaan pyyntö, tarkista palautusaika, tarkista yrityksen palautuskäytäntö, tee päätös ja toteuta toimenpide. Jokaiselle vaiheelle kirjoita, mitä agentti tarkistaa ja mitä voi mennä pieleen.

---

## Tehtävä 23.3: ReAct vs. ketjuajattelu — milloin käytät mitä?

### Tavoite
Oppia valitsemaan oikea päättelymalli ongelman luonteen perusteella. Tämä on suoraan hyödyllinen projektin aihion kirjoittamisessa.

### Ohjeet

Sinulla on neljä tehtävää:

**A:** "Asiakkaan tili on jäädytetty. Avaa se."

**B:** "Asiakas ei ole varma, mitä tuotetta hän haluaa. Auta valitsemaan."

**C:** "Tilaus on epätavallinen (negatiivinen hinta). Tarkista."

**D:** "Asiakkaalle tulee joka kuukausi tilaukseen ongelma. Ratkaise juurisyy."

Jokaiselle tehtävälle päätä, sopiiko ReAct vai ketjuajattelu paremmin, perustele miksi ja arvioi, kuinka monta vaihetta tai iteraatiota tarvitaan.

---

## Tehtävä 23.4: Moniagenttijärjestelmä — erikoistuneet agentit

### Tavoite
Ymmärtää, miten useampi agentti voi tehdä yhteistyötä ja milloin se on perusteltua. Tämä auttaa sinua projektin aihiossa arvioimaan, riittääkö yksi agentti vai tarvitseeko ongelmasi useampia.

### Ohjeet

Kuvittele moniagenttijärjestelmää, jossa on neljä agenttia: analyysi-agentti (lukee asiakkaan viestin), tiedonhaku-agentti (hakee asiakkaan historian), kirjoitus-agentti (kirjoittaa vastauksen) ja validointi-agentti (tarkistaa, onko vastaus turvallinen).

Kuvaile lyhyesti (150–200 sanaa), miten nämä neljä agenttia toimivat yhdessä: mikä agentti aloittaa, miten tieto kulkee agentilta toiselle, missä vaiheessa johtaja-agentti päättää seuraavasta askeleesta ja mitä tapahtuu, jos validointi-agentti löytää ongelman.