# Opiskelutehtävät: Agentin muisti ja konteksti

## Projektin aihio 2: Suunnittele agentin muisti

Tämä on toinen viidestä projektin aihiosta, jotka keräät Agentit-osion aikana. Käytät näitä aihioita oppitunneilla 26–27, kun rakennat oman n8n-agenttityönkulun ja esittelet sen. Säilytä tämä huolellisesti.

### Tehtävä

Palaa projektin aihioon 1 (oppitunti 19), jossa valitsit ongelman ja käyttäjän. Suunnittele nyt agenttisi muististrategia. Kirjoita lyhyt suunnitelma (150–200 sanaa), jossa vastaat neljään kysymykseen: Mitä agentin täytyy muistaa yksittäisen keskustelun aikana (konteksti-ikkuna)? Mitä agentin täytyy muistaa keskustelujen välillä (pitkäaikainen muisti)? Mitä tiloja agentillasi on ja mitkä muuttujat ohjaavat siirtymiä tilasta toiseen? Millainen on agenttisi "sielu" — mitä arvoja se noudattaa aina?

### Miksi tämä on tärkeä

Oppitunneilla 26–27 rakennat n8n-työnkulun, jossa muisti on konkreettinen suunnittelupäätös. Ilman muististrategiaa agentti käsittelee jokaisen pyynnön kuin se olisi ensimmäinen — se ei muista aiempia keskusteluja eikä osaa seurata monivaiheista prosessia. Tämä aihio varmistaa, että mietit muistin roolin ennen kuin alat rakentaa.

Alla olevat harjoitustehtävät auttavat sinua ymmärtämään muistin eri tasot käytännössä ja keräämään havaintoja, joita voit hyödyntää suunnitelman kirjoittamisessa.

---

## Tehtävä 21.1: Konteksti-ikkunan suunnittelu

### Tavoite
Ymmärtää käytännössä, miten konteksti-ikkunan koko vaikuttaa agentin toimintaan. Tämän tehtävän opit auttavat sinua projektin aihiossa päättämään, kuinka paljon kontekstia oma agenttisi tarvitsee.

### Ohjeet

Rakennat asiakaspalveluagentin, joka käsittelee pitkiä asiakaspuheluita. Sinun täytyy päättää konteksti-ikkunan koko kolmessa eri skenaariossa:

**Skenaario A**: Yksinkertainen kysymys-vastaus ("Mikä on hinta?")

**Skenaario B**: Monivaiheinen tekninen ongelmanratkaisu (10+ viestiä dialogista)

**Skenaario C**: Neuvotteluprosessi, jossa vaatimukset muuttuvat (20+ viestiä)

Jokaiselle skenaariolle ehdota konteksti-ikkunan koko (viestien lukumäärä), perustele miksi se on sopiva ja kuvaa, mitä tapahtuu jos ikkuna on liian pieni tai liian suuri.

---

## Tehtävä 21.2: Vektoritietokanta — merkitysperusteinen haku

### Tavoite
Ymmärtää, miten pitkäaikainen muisti toimii semanttisen haun avulla. Tämä auttaa sinua projektin aihiossa päättämään, tarvitseeko oma agenttisi pitkäaikaista muistia.

### Ohjeet

Asiakas sanoo: "Minulla oli ongelma kortin kanssa viime kuussa. Se liittyi maksuihin."

Agentti etsii vektoritietokannasta samankaltaisia tapauksia. Kirjoita kolme aikaisempaa tapauksen kuvausta: tapaus, joka on hyvin samankaltainen (sama ongelma), tapaus, joka on osittain samankaltainen (eri tuote, sama tyyppi) ja tapaus, joka on liian erilainen (agentti ei hakisi sitä). Selitä jokaiselle 1–2 lauseella, miksi vektoritietokanta loisi tai ei loisi vastaavuutta.

---

## Tehtävä 21.3: Tila ja muuttujat

### Tavoite
Oppia suunnittelemaan agentin tilat ja tilasiirtymät. Tämä auttaa sinua projektin aihiossa tunnistamaan, mitä tiloja oma agenttisi tarvitsee.

### Ohjeet

Rakennat tilauksen käsittelyagentin. Tilaus käy läpi neljä tilaa: "luotu" → "maksettu" → "pakattu" → "lähetetty". Kutakin tilaa kohden määritä tilan nimi ja numero (esim. 1/4), kolme muuttujaa jotka kuvaavat tilaa ja ehto, joka liikuttaa tilaa seuraavaan.

---

## Tehtävä 21.4: Soul — agentin identiteetti ja arvot

### Tavoite
Oppia kirjoittamaan agentille selkeä identiteetti ja arvopohja. Tämä auttaa sinua projektin aihiossa määrittelemään, millainen oma agenttisi on luonteeltaan.

### Ohjeet

Kirjoita Soul-dokumentti (noin 150 sanaa), jossa määrittelet agentin identiteetin (kuka agentti on), kolme perustavaa arvoa (mitä agentti ei koskaan tee) ja päätöksenteon perustan (miten agentti päättää epäselvissä tilanteissa). Soul-dokumentin tulee olla tarpeeksi konkreettinen, että se ohjaa agentin toimintaa käytännössä.
