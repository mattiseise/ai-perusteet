# Opiskelutehtävät: Kontekstin antaminen

## Botin rakennuspala 2: Suunnittele kontekstistrategia

Tämä on toinen neljästä botin rakennuspalasta, jotka keräät Tekoälyjen käyttö -osion aikana. Käytät näitä rakennuspaloja oppitunneilla 17–18, kun rakennat oman Custom-botin ja esittelet sen. Säilytä tämä huolellisesti.

### Tehtävä

Palaa rakennuspalaan 1 (oppitunti 10), jossa valitsit alustan ja käyttötapauksen. Suunnittele nyt, miten bottisi saa kontekstia käyttäjältä. Kirjoita lyhyt suunnitelma (150–200 sanaa), jossa vastaat kolmeen kysymykseen: Mitä kontekstia bottisi tarvitsee käyttäjältä toimiakseen hyvin (esim. käyttäjän rooli, tehtävän laajuus, taustatiedot)? Miten botti pyytää kontekstia — kysyykö se aktiivisesti vai odottaako käyttäjän antavan tiedot? Miten pilkot monimutkaisen tehtävän osiin, jotta konteksti-ikkuna ei täyttyisi?

### Miksi tämä on tärkeä

Oppitunneilla 17–18 kirjoitat bottisi system promptin, joka ohjaa botin käyttäytymistä. Kontekstistrategia on system promptin ydin — se määrittää, miten botti kerää tietoa käyttäjältä ja miten se rakentaa ymmärryksensä tehtävästä. Ilman kontekstistrategiaa system promptista tulee epämääräinen ja botti antaa yleisiä vastauksia.

Alla olevat harjoitustehtävät auttavat sinua ymmärtämään käytännössä, miten kontekstin laatu vaikuttaa tekoälyn vastauksiin ja miten kontekstia rakennetaan asteittain.

---

## Tehtävä 12.1: Kontekstin rakentaminen asteittain

### Tavoite
Kokea käytännössä, miten kontekstin määrä ja laatu vaikuttavat tekoälyn vastauksiin. Tämä auttaa sinua rakennuspalassa suunnittelemaan, mitä kontekstia oma bottisi tarvitsee.

### Ohjeet

Valitse aihe (esim. esseen kirjoittaminen, ryhmätyön raportti, tenttiin valmistautuminen tai harjoitteluhakemuksen kirjoittaminen). Tee neljä erilaista pyyntöä tekoälylle, joissa jokainen on parempi kuin edellinen:

**Kierros 1 — Huono pyyntö (liian yleinen):** Yksinkertainen, epämääräinen pyyntö kuten "Auta minua esseen kanssa."

**Kierros 2 — Parempi pyyntö (joitain tietoja):** Lisää kontekstia — kuka olet, mitä haluat, mihin käytät sitä.

**Kierros 3 — Vielä parempi (lisää yksityiskohtia):** Tarkenna lisää — mitä tiedät jo, mitä et tiedä, mihin tasoon kirjoittaa, mitä muotoa haluat.

**Kierros 4 — Paras pyyntö (täysi konteksti + pilkkominen):** Pilko tehtävä osiin ja kerro tarkasti mitä haluat.

Tallenna kaikki neljä pyyntöä ja vastaukset. Kirjoita yhteenveto, jossa vertaat ensimmäisen ja neljännen vastauksen eroja, analysoit kontekstin vaikutusta ja pohdit, miten sovellat oppimaasi seuraavalla kerralla.

---

## Tehtävä 12.2 (valinnainen): Iteraation harjoittelu

### Tavoite
Harjoitella kontekstin rakentamista iteratiivisesti samaan tehtävään. Tämä syventää ymmärrystäsi siitä, miten konteksti rakentuu vaiheittain — sama periaate pätee bottisi vuorovaikutukseen käyttäjän kanssa.

### Ohjeet

Valitse yksi IT-alan aihe (esim. verkot, tietoturva, palvelimet, koneoppiminen). Tee neljä kierrosta, joissa jokaisella kerralla tarkennat pyyntöä: yksinkertaisesta kysymyksestä ("Kerro aiheesta") tarkkaan pilkkomiseen ("Haluan oppia aiheesta 30 minuutissa. Anna lyhyt selitys, esimerkit, väärinkäsitykset ja testikysymykset."). Kirjoita yhteenveto vastausten laadun eroista ja siitä, mitkä muutokset olivat tärkeimpiä.
