# Opiskelutehtävät

## Tehtävä 3.1: Omaa kielimallia testaaminen — Next-Token Simulation

### Tavoite
Ymmärtää käytännössä, miten next-token prediction toimii ja miksi malli tekee virheitä.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

**Vaihe 1: Manuaalinen ennustus**
Antaa tekstinpalan:
"Koodi on kirjoitettu Python:ssa. Seuraava askel on..."

Ryhmä ennustaa yksitellen, mikä sana tulee seuraavaksi. Kirjoita kaikki vastaukset:
- Henkilö 1: ____
- Henkilö 2: ____
- Henkilö 3: ____

**Vaihe 2: Vertailu ChatGPT:iin**
Kopioi sama teksti ChatGPT:iin. Anna kehotus: "Jatka vain seuraavalla sanalla."

Dokumentoi ChatGPT:n vastaus.

**Vaihe 3: Analyysi**
- Oliko ChatGPT:n vastaus yksi teistä?
- Jos ei, miksi se valitsi toisen sanan?
- Mikä on todennäköisintä, ja mikä on "oikea" vastaus?

### Odotettu tuotos

Dokumentti, jossa:
- Kolme ennustusta ryhmältä
- ChatGPT:n vastaus
- Analyysi: "Miksi seuraava sana on vaikea ennustaa? Mistä ChatGPT tiesi vastauksen?"

**Jos teet tehtävän yksin:**
Tee vaihe 1-2. Anna oma ennustuksesi ja ChatGPT:n vastaus, sitten pohdi eroja.

---

## Tehtävä 3.2: Hallusinaatiot — Tunnista väärät tiedot

### Tavoite
Nähdä konkreettisesti, miten kielimalli voi luoda vakuuttavan mutta väärän vastauksen.

### Ohjeet (pareittain tai yksin)

Kysy ChatGPT:ltä tai vastaavalta mallilta kolme hyvin spesifikkä kysymystä. Varmista, että vastaukset ovat väärät:

Esimerkiksi:
1. "Kuka ohjasi elokuvan 'Suuri Mahtava'?" (Ei ole olemassa)
2. "Mikä on Suomen 8. suurin kaupunki vuonna 2026?" (Voisi olla väärä)
3. "Kuka on Teknillisen korkeakoulun rehtori vuonna 2026?" (Voisi olla väärä)

**Jokaiselle vastaukselle:**
- Dokumentoi ChatGPT:n vastaus.
- Tutki, onko se oikein vai väärä.
- Jos väärä, kirjoita: "Miksi malli voi uskotella näin?"

### Odotettu tuotos

Dokumentti, jossa:
- Kolme kysymystä ja ChatGPT:n vastaukset
- Tarkistus: Mikä oli oikein, mikä väärä
- Analyysi (3-5 lausetta): "Miten kielimalli voi tuottaa hallusinaatioita? Miksi vakuuttavasti näyttävät väärät vastaukset ovat vaarallisia?"

**Jos teet tehtävän yksin:**
Tee yhdellä kysymyksellä ja vastuksella. Analysoi se.

---

## Tehtävä 3.3: Lämpötilan vaikutus — Kokeile satunnaisuuden tasoa

### Tavoite
Ymmärtää, miten lämpötila vaikuttaa kielimallin luovuuteen ja johdonmukaisuuteen.

### Ohjeet (pareittain tai yksin)

Jos sinulla on pääsy malliin, jossa voit säätää lämpötilaa (tai käytät sellaista versiota):

**Testi 1: Matala lämpötila (0.2)**
- Anna kehotus: "Kirjoita lyhyt runo keväästä, 4 riviä."
- Kirjoita runo kolme kertaa samalla kehotuksella.
- Dokumentoi vastaukset.

**Testi 2: Korkea lämpötila (0.9)**
- Anna sama kehotus samalla mitalla.
- Kirjoita runo kolme kertaa.
- Dokumentoi vastaukset.

**Analyysi:**
- Kumpi lämpötila tuotti samankaltaisia runoja?
- Kumpi tuotti erilaisia?
- Kumpi on parempi runon kirjoittamiseen? Ja miksi?

### Odotettu tuotos

Dokumentti, jossa:
- Kolme runoa matalalla lämpötilalla
- Kolme runoa korkealla lämpötilalla
- Vertailu: "Miten lämpötila vaikutti tuloksiin?"
- Johtopäätös: "Kumpi lämpötila on parempi mitäkin tehtävää varten?"

**Jos sinulla ei ole pääsy lämpötila-säätöön:**
Voit tehdä tehtävän samoin, mutta dokumentoida, miksi lämpötilan säätäminen voisi olla hyödyllistä.
