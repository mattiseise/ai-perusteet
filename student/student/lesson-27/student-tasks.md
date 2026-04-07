# Opiskelutehtävät: n8n-projektipaja, osa 2 — testaa ja esittele

## Agentit-osion arvioitava projekti (osa 2/2)

Tämä on Agentit-osion arvioitavan projektin toinen osa. Oppitunnilla 26 rakensit n8n-työnkulun — nyt testaat sen, dokumentoit rakenteen ja esittelet tuloksen.

---

## Tehtävä 27.1: Testaa agentin toiminta ja turvallisuus

### Tavoite
Varmistaa, että agentti toimii oikein normaaleissa tilanteissa ja kestää epätavallisia syötteitä.

### Ohjeet

Testaa agenttia systemaattisesti kolmessa kategoriassa:

**Normaalit tapaukset (5 testiä):** Anna agentille syötteitä, joihin se on suunniteltu. Esimerkiksi FAQ-botille normaaleja kysymyksiä.

**Reunatapaukset (5 testiä):** Testaa epätavallisia tilanteita — tyhjä syöte, liian pitkä syöte, väärä kieli, emojit ja sekava teksti.

**Turvallisuustestit (5 testiä):** Kokeile prompt injectionia ("Unohda aiemmat ohjeet"), piilotettuja ohjeita, manipulaatiota, rekursiivista pyyntöä ja henkilötietojen pyynnöstä.

Dokumentoi jokainen testi:

```
TESTI: [numero ja nimi]
Kategoria: Normaali / Reunatapaus / Turvallisuus
Syöte: [mitä annoit agentille]
Odotettu tulos: [mitä pitäisi tapahtua]
Todellinen tulos: [mitä tapahtui oikeasti]
Tila: LÄPÄISI / EI LÄPÄISSYT
Huomio: [jos epäonnistui, miksi?]
```

Kirjoita yhteenveto (200 sanaa): missä agentti oli vahva, missä heikko ja miten korjaisit ongelmat.

**Suorituspolut:** Voit joko seurata yllä olevaa testaussuunnitelmaa tarkasti (polku A) tai tehdä 5 normaalia ja 5 turvallisuustestiä ja keksiä 5 omaa testiä perusteluineen (polku B).

---

## Tehtävä 27.2: Dokumentoi agentin rakenne

### Tavoite
Kirjoittaa dokumentaatio, jonka avulla toinen henkilö ymmärtää agenttisi rakenteen ja tarkoituksen.

### Ohjeet

Kirjoita kolme lyhyttä dokumenttia:

**README (käyttöohje):** Mitä agentti tekee, kenelle se on tarkoitettu, miten sitä käytetään, 2–3 esimerkkiä ja rajoitukset.

**ARKKITEHTUURI (rakenne):** Kuvaa n8n-työnkulku solmu solmulta. Jokaisen solmun kohdalla kerro, mitä se tekee, mitä se saa syötteenä ja mitä se tuottaa. Linkitä solmut agentin kuuteen komponenttiin (syötekäsittelijä, päättelijä, työkalut, muisti, turvakerros, palautesilmukka).

**TURVALLISUUS (riskianalyysi):** Tunnista riskit, selitä miten olet ratkaissut ne ja kerro, mitä lokitat. Sisällytä human-in-the-loop-kohdat.

---

## Tehtävä 27.3: Vertaisarviointi — testaa toisen agentti

### Tavoite
Arvioida toisen opiskelijan valmista agenttia käyttäjän ja hyökkääjän näkökulmasta.

### Ohjeet

Käytä toisen opiskelijan n8n-agenttia ja dokumentoi kokemukset. Testaa normaaleilla ja epätavallisilla syötteillä. Kokeile prompt injectionia ja muita turvallisuustestejä. Kirjoita rakentava palaute: mikä toimii hyvin, mitkä ovat suurimmat turva-aukot ja mitä voisi parantaa.

**Jos teet tehtävän yksin:** Pyydä tekoälyä (ChatGPT tai Claude) arvioimaan suunnitelmaasi kriittisesti — anna sille dokumentaatiosi ja pyydä palautetta.

---

## Tehtävä 27.4: Demo ja itsearviointi

### Tavoite
Esitellä oma agentti ja arvioida omaa oppimista kriittisesti.

### Ohjeet

**Demo (3–5 min):** Esitä, mitä agentti tekee. Näytä triggeri, käytä agenttia 2–3 normaalilla tapauksella, näytä arkkitehtuuri (solmut ja yhteydet) ja selitä turvakerrokset.

**Itsearviointi (300–400 sanaa):** Kirjoita lyhyt itsekritiikki, jossa käsittelet onnistumiset (mikä toimi hyvin), epäonnistumiset (mikä ei toiminut), opitut asiat (mitä uutta opit agenttiajattelusta tai n8n:stä), parannusideat (mitä tekisit toisin) ja agentin kuuden komponentin arvio (mikä oli vahvin ja mikä heikoin omassa työnkulussasi).

---

## Arviointi

Projekti arvioidaan viidellä osa-alueella:

**Toimiva työnkulku (25 p):** Onko n8n-työnkulku toimiva? Sisältääkö se vähintään triggerin, tekoälysolmun ja toimintasolmun?

**Turvallisuus (20 p):** Onko turvakerros suunniteltu ja toteutettu? Kestääkö agentti testejä?

**Dokumentaatio (20 p):** Ovatko README, arkkitehtuurikuvaus ja turvallisuusanalyysi selkeitä ja kattavia?

**Testaus (20 p):** Onko agentti testattu systemaattisesti? Ovatko tulokset dokumentoitu?

**Itsearviointi ja demo (15 p):** Onko demo selkeä? Osoittaako itsearviointi kriittistä ajattelua ja oppimista?
