# Opiskelutehtävät

## Todistusaineisto 2: Kun tekoäly unohtaa — mitä se tarkoittaa käytännössä

Tämä on toinen kolmesta todistusaineistosta, jotka keräät Teoria-osion aikana. Käytät näitä todistusaineistoja Teoria-osion arvioitavassa tehtävässä "Tuomaripöydän päätös — asiantuntijalausunto tekoälystä" (oppitunti 9). Säilytä tämä huolellisesti.

### Tehtävä

Kirjoita lyhyt tapausesimerkki (150–200 sanaa) todellisesta tai kuvitteellisesta työtilanteesta, jossa kontekstin katoaminen aiheuttaisi ongelman. Voit käyttää inspiraationa alla olevien harjoitustehtävien kokemuksiasi — erityisesti tehtävässä 5.3 näet omin silmin, miten kontekstin katoaminen tapahtuu.

Tapausesimerkin tulee kattaa neljä asiaa: mikä tilanne on kyseessä (esimerkiksi IT-tuki, koodiprojekti tai asiakaspalvelu), mitä tekoäly unohtaa ja miksi (konteksti-ikkunan FIFO-periaate), mitä seurauksia unohtamisella on (virheellinen vastaus, turvallisuusriski tai aikahukka) ja miten ammattilainen estäisi tämän (ankkurointi, pilkkominen, dokumentointi).

### Miksi tämä on tärkeä

"Tuomaripöydän päätös" -tehtävässä analysoit skenaarion, jossa tekoälyn rajoitukset aiheuttavat käytännön ongelmia. Tämä tapausesimerkki on valmis todiste, jonka voit liittää analyysiisi — se osoittaa konkreettisesti, että ymmärrät tekoälyn muistin rajat ja osaat ehdottaa ratkaisuja.

Alla olevat harjoitustehtävät auttavat sinua ymmärtämään kontekstin hallintaa käytännössä ja keräämään havaintoja todistusaineiston kirjoittamista varten.

---

## Tehtävä 5.1: Konteksti-ikkunan hallinta — token-laskenta ja pilkkomisen käytäntö

### Tavoite
Ymmärtää käytännössä, miten suuria tehtäviä pilkotaan, jotta tekoälyn konteksti-ikkuna ei täyttyisi. Tämän tehtävän opit auttavat sinua todistusaineistossa kuvaamaan, miten ammattilainen hallitsee kontekstin rajoituksia.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

Valitkaa suuri tehtävä, jota käsittelisitte tekoälyn kanssa useassa vaiheessa — esimerkiksi pitkän dokumentin analysointi, laajan ongelman debuggaaminen tai monivaiheinen suunnitelma.

Arvioikaa tehtävän tokenikoko kopioimalla se tekoälylle tai käyttämällä nyrkkisääntöä (1 token ≈ 4 merkkiä). Dokumentoikaa arvio ja vertailkaa sitä mallin konteksti-ikkunaan.

Pilkokaa tehtävä pienemmiksi osiksi ja kirjoittakaa suunnitelma taulukkoon:

| Osa | Tokenit (arvio) | Pääkysymys | Ankkuri (mitä toistaa seuraavassa osassa) |
|-----|---------|-----------|---------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

Kirjoittakaa lisäksi ankkurikonteksti, jota käytätte jokaisen osan alussa: yhteenveto projektista, edellisen osan tulokset ja seuraavan osan tavoite.

### Odotettu tuotos
Täytetty pilkkomistaulukko, ankkurikontekstimallit ja lyhyt suunnitelmadokumentti.

**Jos teet tehtävän yksin:**
Valitse itsellesi sopiva tehtävä ja tee kaikki vaiheet.

---

## Tehtävä 5.2: Pitkä projekti pilkottuna — kahden päivän simulaatio

### Tavoite
Simuloida oikeaa pitkää projektia tekoälyn kanssa, jossa konteksti-ikkunaa hallitaan pilkkomisen ja ankkuroinnin avulla. Tämä antaa sinulle konkreettista kokemusta siitä, miten tieto säilyy tai katoaa — suoraan käytettävissä todistusaineistossa.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

Valitkaa simuloitu kahden päivän projekti. Se voi olla esimerkiksi tietokannan suunnittelu (päivä 1: vaatimukset, päivä 2: rakenne), ohjelman debuggaaminen (päivä 1: virheen etsintä, päivä 2: korjaus) tai dokumentaation kirjoittaminen (päivä 1: luonnos, päivä 2: editointi).

**Päivä 1:** Aloittakaa uusi keskustelu tekoälyn kanssa. Antakaa ankkurikonteksti (rooli, tausta, tavoite, rajaukset) ja tehkää ensimmäinen tehtävä. Dokumentoikaa vastaus ja erityisesti olennainen tieto, joka täytyy muistaa.

**Siirtymä:** Tiivistäkää päivän 1 tulokset 200–300 sanaan. Mitä saatiin selville? Mitä täytyy muistaa?

**Päivä 2:** Aloittakaa uusi keskustelu (puhdas ikkuna). Kirjoittakaa päivitetty ankkurikonteksti, joka sisältää päivän 1 yhteenvedon, ja jatkakaa projektia.

**Analyysi:** Vastasiko päivän 2 tekoäly johdonmukaisesti päivän 1 kanssa? Palauttiko se tiedot ankkuroinnin avulla? Mitä olisi mennyt pieleen ilman dokumentointia?

### Odotettu tuotos
Dokumentti, jossa on molempien päivien ankkurikontekstit, tulokset ja vertailuanalyysi siitä, miten hyvin tieto säilyi.

**Jos teet tehtävän yksin:**
Simuloi projektin kaksi päivää ja vertaa ankkuroinnin vaikutusta.

---

## Tehtävä 5.3: Kun malli unohtaa — virheen tunnistaminen ja korjaaminen

### Tavoite
Kokea käytännössä kontekstin katoaminen ja oppia tunnistamaan, milloin tekoäly on unohtanut annetut ohjeet. Tämä on erityisen hyödyllinen kokemus todistusaineiston kirjoittamiseen — näet tarkalleen, miten ja milloin muisti pettää.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä, tai yksin)

Aloita uusi keskustelu tekoälyn kanssa. Anna selkeä rajaus ensimmäisessä viestissä, esimerkiksi: "Olet Linux-järjestelmänhallitsija. Käytämme AINA Ubuntu 22.04:ää, Python 3.9:ää ja PostgreSQL:ää. Älä koskaan ehdota Windows-ratkaisuja tai muita tietokantoja."

Kysy ensin 3–4 kysymystä, jotka liittyvät tähän ympäristöön, ja dokumentoi vastaukset. Kysy sitten 15–20 kysymystä eri aiheista (verkkokonfiguraatio, käyttäjähallinta, tiedostojärjestelmä, palomuurit, varmuuskopiot) tarkoituksenasi täyttää konteksti-ikkunaa.

Lopuksi kysy: "Miten asennan tietokantapalvelimen tähän ympäristöön?" Älä toista rajauksia. Katso, muistaako malli mitä tietokantaa ja käyttöjärjestelmää käytät.

Analysoi tulos: Muistiko malli rajaukset? Jos ei, missä kohtaa keskustelua se unohti? Korjaa tilanne toistamalla rajaukset ja kysy sama kysymys uudelleen — paraniko vastaus?

### Odotettu tuotos
Dokumentti, jossa on alkuperäinen rajaus, kohta jossa malli unohti, virheellinen vastaus, korjattu vastaus ankkuroinnin jälkeen ja johtopäätös (2–3 lausetta) siitä, mitä kontekstin katoaminen tarkoittaa käytännössä.
