# Opiskelutehtävät: Gen AI:n luonne

## Todistusaineisto 3: Ammattilaisen verifiointikäytäntö

Tämä on kolmas ja viimeinen todistusaineisto, jonka keräät Teoria-osion aikana. Käytät näitä todistusaineistoja Teoria-osion arvioitavassa tehtävässä "Tuomaripöydän päätös — asiantuntijalausunto tekoälystä" (oppitunti 9). Säilytä tämä huolellisesti.

### Tehtävä

Yhdistä oppituntien 3, 5 ja 7 opit yhdeksi konkreettiseksi käytännöksi. Kirjoita "ammattilaisen tarkistuslista" (200–250 sanaa), jota IT-ammattilainen voisi käyttää arjessaan tekoälyn kanssa.

Tarkistuslistan tulee kattaa neljä asiaa: miten tunnistat hallusinaation (tämän oppitunnin opit), miten varmistat ettei konteksti ole kadonnut pitkässä keskustelussa (oppitunnin 5 opit), miten ymmärrät miksi malli voi tuottaa vakuuttavan mutta väärän vastauksen (oppitunnin 3 opit) ja konkreettiset toimenpiteet, jotka teet ennen kuin luotat tekoälyn vastaukseen.

### Miksi tämä on tärkeä

"Tuomaripöydän päätös" -tehtävässä sinun täytyy ehdottaa konkreettisia käytäntöjä ja osoittaa ammatillista vastuullisuutta. Tämä tarkistuslista on suoraan käytettävissä analyysissäsi — se osoittaa, että osaat soveltaa teoriaa käytäntöön. Yhdessä todistusaineistojen 1 ja 2 kanssa sinulla on vahva perusta koko arvioitavalle tehtävälle.

Alla olevat harjoitustehtävät auttavat sinua keräämään havaintoja ja kokemuksia, joita voit hyödyntää tarkistuslistan kirjoittamisessa.

---

## Tehtävä 7.1: Testaa epädeterminismiä ja lämpötilaa

### Tavoite
Ymmärtää käytännössä, miten epädeterminismi ja lämpötila vaikuttavat tekoälyn vastauksiin. Tämän tehtävän havainnot auttavat sinua todistusaineistossa selittämään, miksi tekoälyyn ei voi luottaa antamaan samaa vastausta kahdesti.

### Ohjeet

Valitse tekoälypalvelu (ChatGPT, Claude tai muu) ja kirjoita sama prompti neljä kertaa eri asetuksilla: alin lämpötila, matala (0,5), korkea (1,0) ja alin uudelleen. Prompti voi olla esimerkiksi "Kirjoita lyhyt, tekninen kuvaus siitä, mitä Python-funktio tekee" tai "Ideoi kolme nimeä uudelle sovellukselle."

Täytä taulukko:

| Asetus | Vastaus (lyhenne) | Johdonmukaisuus | Luovuus | Selkeä ero edellisestä |
|---|---|---|---|---|
| Alin (1. yritys) | | | | |
| Matala | | | | |
| Korkea | | | | |
| Alin (2. yritys) | Sama kuin 1. vai eri? | | | |

Pohdi lopuksi (2–3 lausetta): Vaihtelivatko vastaukset? Oliko alin asetus todella deterministinen? Minkä säädön valitsisit API-dokumentaatioon ja minkä markkinointitekstiin?

---

## Tehtävä 7.2: Etsi hallusinaatioita

### Tavoite
Oppia tunnistamaan hallusinaatioita ja ymmärtämään miksi niitä syntyy. Tämä kokemus on suoraan hyödyllinen todistusaineistossa — opit tunnistamaan merkit, joista tiedät ettei vastaukseen voi luottaa.

### Ohjeet

Kysy tekoälyltä tekninen kysymys, johon vastaus on helppo verifioida — esimerkiksi tietyn kirjaston funktionimi, komentorivikomento tai tekninen fakta.

Kopioi vastaus ja tarkista se kolmesta lähteestä: virallinen dokumentaatio, kokeilemalla itse (jos mahdollista) ja verkkohaku.

Täytä taulukko:

| Kysymys | Tekoälyn vastaus | Dokumentaation vastaus | Oikein vai väärin | Hallusinaation merkkejä |
|---|---|---|---|---|
| | | | | |

Kirjoita analyysi (3–4 lausetta): Oliko vastaus hallusinaatio? Mitä merkkejä huomasit? Oliko vastaus "näyttävä" mutta väärä vai selvästi epävarma? Miksi malli tuotti tämän vastauksen?

---

## Tehtävä 7.3: Suunnittele verifiointiprosessi

### Tavoite
Oppia integroimaan tekoäly osaksi työnkulkua niin, etteivät hallusinaatiot pääse aiheuttamaan virheitä. Tämä tehtävä on suoraan hyödyllinen todistusaineiston "konkreettiset toimenpiteet" -osion kirjoittamisessa.

### Ohjeet

Kuvittele, että työskentelet kehittäjänä ja käytät ChatGPT:tä kirjoittamaan koodia, joka luettelee kaikki tietokantaan tallennetut käyttäjät. Haluat varmistaa, että koodi on turvallinen ja toimii.

Suunnittele viisivaiheinen verifiointiprosessi:

**1. Ennen kuin kysyt tekoälyltä:** Mitä sinun täytyy jo tietää itse?

**2. Kun kysyt:** Miten kirjoitat promptin, jotta saat järkeviä vastauksia?

**3. Kun saat vastauksen:** Mihin asioihin kiinnität huomiota? Mistä merkeistä epäilet hallusinaatiota?

**4. Testaus ja validointi:** Mitä testejä ajat ennen kuin käytät koodia?

**5. Dokumentointi:** Mitä kirjoitat muistiinpanoihin, jotta muut ymmärtävät mitä tekoälyltä pyysit ja miksi?
