# Opiskelutehtävät — Mikä tekoäly oikeasti on?

> 📌 **Kaikkia ei tarvitse tehdä.** Valitse tehtävistä 1. Suosittelen kuitenkin tehtävää 1.1, joka osuu suoraan tunnin ydintaidon ytimeen. Jos sinulla on aikaa ja kiinnostusta, voit lisäksi tehdä syventävän tehtävän 1.2.

## Tehtävä 1.1 — AI vai ei AI? 🟢 SUOSITELTU

**Tavoite:** Opit erottamaan tekoälyn tavallisesta ohjelmoinnista konkreettisten esimerkkien avulla. Tämä on koko Teoria-osion peruskivi.

### Vaiheet

#### Vaihe 1 — Luokittele itse ensin

Käy alla oleva taulukko läpi **omin päin**. Merkitse jokaiselle: AI / Ei AI / Epäselvä — ja kirjoita yhden lauseen perustelu. Älä vielä käytä tekoälyä apuna; tarkoitus on, että muodostat ensin oman käsityksen.

| Järjestelmä | Kuvaus | AI / Ei AI / Epäselvä | Perustelu |
|---|---|---|---|
| Sähköpostin roskapostisuodatin | Lajittelee viestit roskapostiin sanojen perusteella | | |
| Netflix-suositukset | Näyttää elokuvia ja sarjoja, joista todennäköisesti pidät | | |
| Pankin lainahakemus | Tekee hyväksyntä-/hylkäyspäätöksen automaattisesti | | |
| Puhelinluettelo | Järjestää yhteystiedot aakkosjärjestykseen | | |
| Google Maps | Ohjaa reitille reaaliaikaisen liikennetiedon perusteella | | |
| Pankkiautomaatti | Antaa rahaa, kun syötät PIN-koodin | | |
| Auto-correct | Korvaa väärän kirjoitusasun oikealla sanalla | | |

#### Vaihe 2 — Haasta itsesi tekoälyn kanssa

Avaa ChatGPT tai Claude ja anna tekoälylle **oma luokittelusi**. Pyydä sitä haastamaan päätelmäsi. Esimerkkiprompti:

```
Toimit minulle sparrauskumppanina. Opiskelen tekoälyn perusteita ja
yritän oppia erottamaan, milloin järjestelmä on tekoälyä ja milloin
'pelkkä ohjelma'. Tässä oma luokitteluni perusteluineen:

[liitä taulukkosi tähän]

Haasta päätelmäni. Missä kohdissa voisin olla väärässä? Onko jokin
'Ei AI' itse asiassa AI:n rajatapaus, tai päinvastoin? Älä paljasta
suoraan oikeita vastauksia — esitä vastakysymyksiä ja pyydä minua
perustelemaan vielä tarkemmin.
```

Tämä on harjoitus siitä, miten tekoälyä käytetään *ajattelun terävöittäjänä*, ei vastauspalveluna. Huomaat samalla, että tekoälyn vastauksiakaan ei kannata niellä sellaisenaan.

#### Vaihe 3 — Kirjoita yhteenveto

Tekoälykeskustelun jälkeen muokkaa taulukkoasi tarvittaessa ja kirjoita lyhyt yhteenveto (3–5 lausetta):

- Mikä on tärkein ero tekoälyn ja tavallisen ohjelman välillä?
- Mikä esimerkeistä oli vaikein luokitella ja miksi?
- Muuttuiko jokin päätös tekoälykeskustelun aikana? Jos, niin mikä — ja miksi?

> 💡 **Vinkki:** Tehtävää ei palauteta, mutta kannattaa pitää itselle oma muistiinpanodokumentti tämän ja muiden tunnin tehtävien tuloksista. Käytät niitä myöhemmin tukena, kun pohdit miten tekoäly toimii ja missä sen rajat ovat.

---

## Tehtävä 1.2 — Petoksentunnistus: sääntö vs. tekoäly 🟣 SYVENTÄVÄ

> **Tämä on syventävä lisätehtävä.** Tee tämä, jos haluat ymmärtää *miksi* tekoäly on parempi kuin säännöt monimutkaisissa päätöksissä — etkä vain *että* niin on.

**Tavoite:** Huomaat omakohtaisesti, miksi kiinteät säännöt eivät riitä tilanteissa, joissa on monta muuttujaa ja poikkeuksia.

### Tilanne

Olet pankin tietoturvatiimissä. Tehtäväsi on suojata asiakkaiden tilit petoksilta. Alla on 10 transaktiota, joissa **oikea vastaus on jo paljastettu** ("Petos" tai "Laillinen"). Sinun haasteesi: kehittää sääntöjoukko, joka tunnistaa nämä oikein.

| # | Summa (€) | Kello | Paikka | Tavallinen käyttö | Lopputulos |
|---|---|---|---|---|---|
| 1 | 5 500 | 14:30 | Koulu | Yleensä < 1 000 | Laillinen |
| 2 | 2 000 | 03:15 | Tuntematon maa | Harvoin yöllä | **Petos** |
| 3 | 150 | 10:00 | Ruokakauppa | Päivittäinen | Laillinen |
| 4 | 8 000 | 19:45 | Koti | Kerran kuussa | Laillinen |
| 5 | 300 | 02:30 | Verkkokauppa | Ei koskaan yöllä | **Petos** |
| 6 | 50 | 12:00 | Kahvila | Päivittäinen | Laillinen |
| 7 | 10 000 | 15:00 | Tuntematon maa | Ensimmäinen kerta | **Petos** |
| 8 | 3 000 | 20:00 | Koti | Kuukausittain | Laillinen |
| 9 | 600 | 23:45 | Tuntematon kauppa | Ei koskaan | **Petos** |
| 10 | 75 | 11:00 | Ruokakauppa | Päivittäinen | Laillinen |

### Vaiheet

#### Vaihe 1 — Kirjoita oma sääntöjoukkosi

Kirjoita 3–5 sääntöä muodossa: *"Jos [ehto], merkitse petokseksi."*

Esimerkki: `"Jos summa > 1 000 € JA kello on välillä 00:00–06:00 → petos."`

#### Vaihe 2 — Testaa sääntöjäsi

Käy 10 transaktiota läpi sääntöjesi mukaan ja merkitse:

- **Oikein tunnistetut petokset:** ___ / 4
- **Vääriä hälytyksiä** (laillinen → "petos"): ___ / 6
- **Missatut petokset** ("laillinen", oikeasti petos): ___ / 4

#### Vaihe 3 — Käytä tekoälyä apuna analysointiin

Avaa tekoäly ja anna sille sääntöjoukkosi sekä testituloksesi:

```
Toimit minulle sparrauskumppanina. Olen opiskelija ja yritän
ymmärtää, miksi kiinteät säännöt eivät riitä petoksentunnistukseen.

Tässä sääntöni ja niiden tulokset:

Säännöt:
[liitä sääntösi]

Tulokset: [missatut, väärät hälytykset, oikeat osumat]

Auta minua ymmärtämään, mitkä piirteet petostransaktioissa ovat
sellaisia, että niitä on vaikea pukea yhdeksi säännöksi. Miksi
oikea petos voi näyttää joskus 'normaalilta'? Älä kerro minulle
suoraan, miten tekoäly ratkaisisi tämän — auta minua löytämään
se itse.
```

Huomaa, että tekoäly itse on tällaisten ongelmien ratkaisija — käytät sitä siis omakohtaisesti samalla, kun opettelet ymmärtämään, miksi se on tarpeen.

#### Vaihe 4 — Vastaa pääkysymykseen

Kirjoita 3–5 lausetta:

*"Miksi tekoäly olisi parempi tähän tehtävään kuin kiinteät säännöt?"*

**Tunnin 1 jälkeen osaat erottaa tekoälyn tavallisesta ohjelmasta.**
