# Opiskelutehtävät: Viimeistele, testaa ja esittele

> Tämä on Agentit-osion lopputyön viimeistelytunti. Tunnilla 26 rakensit agenttisi minimiversion. Tänään lisäät turvakerroksen, testaat agentin, dokumentoit työn ja esittelet sen.

*Tunnilla on neljä vaihetta. Kaikki kuuluvat lopputyöhön — etene järjestyksessä, koska seuraava vaihe rakentuu edellisen päälle.*

---

## Vaihe 1: Viimeistele agenttisi ja testaa 🟢 PAKOLLINEN

### A. Viimeistele agenttisi (~15 min)

1. **Lisää turvakerros.** Avaa ⭐️ Agentti: Turva ja toteuta sen turvasuunnitelma. Tyypillisesti IF-solmu heti triggerin jälkeen (syötteen validointi) ja toinen IF-solmu tekoälysolmun jälkeen (vastauksen tarkistus).
2. **Lisää human-in-the-loop, jos tarpeen.** Avaa ⭐️ Agentti: Ihminen. Jos agenttisi tekee kriittisiä toimia, lisää hyväksyntäportti.
3. **Lisää lokitus.** Yksinkertainenkin riittää: solmu, joka tallentaa jokaisen suorituksen tiedot.

### B. Testaa systemaattisesti (~15 min)

Tee yhteensä 15 testiä:

- **5 normaalia tapausta**
- **5 reunatapausta** (tyhjä syöte, liian pitkä, väärä kieli, emojit, sekava teksti)
- **5 turvallisuustestiä** (prompt injection, piilotetut ohjeet, manipulaatio, henkilötietopyynnöt, rekursiivinen pyyntö)

Dokumentoi jokainen:

```
TESTI: [numero ja nimi]
Kategoria: Normaali / Reunatapaus / Turvallisuus
Syöte: [mitä annoit agentille]
Odotettu tulos: [mitä pitäisi tapahtua]
Todellinen tulos: [mitä tapahtui]
Tila: LÄPÄISI / EI LÄPÄISSYT
Huomio: [jos epäonnistui, miksi?]
```

### Tekoälyvaihe — sparraa testitapauksia

```
Olen rakentanut agentin, joka tekee [kuvaa]. Olen testannut sitä
näillä syötteillä: [liitä]. Ehdota 3 uutta testitapausta jokaiseen
kategoriaan, joita en ole vielä keksinyt. Älä kerro odotettua
tulosta — sen päätän itse.
```

---

## Vaihe 2: Dokumentoi agenttisi 🟢 PAKOLLINEN

Kirjoita kolme lyhyttä dokumenttia:

**README — käyttöohje (½–1 sivu).**

- Mitä agentti tekee, kenelle, miten käytetään, 2–3 esimerkkiä, rajoitukset.

**ARCHITECTURE — rakenne (½–1 sivu).**

- Listaa jokainen n8n-solmu järjestyksessä. Mitä se tekee, syöte, palautus.
- **Linkitä solmut agentin kuuteen komponenttiin.** Tämä on tärkein osa.

**SAFETY — turvallisuus (½–1 sivu).**

- 3–5 pahinta riskiä, miten torjuit ne, mitä lokitat, human-in-the-loop -kohdat.

---

## Vaihe 3: Vertaisarvio — testaa toisen agentti 🟢 PAKOLLINEN

Vertaisarvio on punaisen tiimin työtä: tavoite löytää ongelmia, ei kritisoida ihmistä.

### Ohjeet

1. Pari (tai toinen tiimi) antaa sinulle pääsyn agenttiinsa.
2. Käytä agenttia kuin oikea käyttäjä (2–3 normaalia tapausta).
3. Yritä murtaa se (prompt injection, reunatapaukset).
4. Kirjoita palaute: **1 vahvuus, 2 ongelmaa, 2 parannusehdotusta** — konkreettisesti.
5. Anna palaute parille, keskustele 5 minuuttia.

**Jos teet lopputyön yksin etkä saa paria:** anna AI:lle dokumentaatiosi ja testiraporttisi. Pyydä sitä toimimaan kriittisenä arvioijana ja kysymään 3–5 haastavaa kysymystä.

---

## Vaihe 4: Demo ja itsearviointi 🟢 PAKOLLINEN

### Demo (3–5 min luokassa)

1. Näytä agentti toiminnassa (2–3 normaalia syötettä).
2. Selitä arkkitehtuuri (osoita n8n-kankaalta, mainitse 6 komponenttia).
3. Kerro turvakerroksesta.
4. Arvioi kriittisesti — mikä onnistui, mikä ei.

> Hyvä demo ei ole täydellinen suoritus — se on rehellinen.

### Itsearviointi (300–400 sanaa)

- **Onnistumiset:** Mikä toimi hyvin?
- **Epäonnistumiset:** Mikä ei toiminut? Miksi?
- **Opitut asiat:** Mitä uutta opin?
- **Parannusideat:** Mitä tekisin toisin?
- **Kuusi komponenttia:** Mikä oli vahvin, mikä heikoin?

---

## Lopputyön palautus

Palauta Itslearningiin yhtenä pakettina:

- Linkki n8n-työnkulkuusi tai vientitiedosto (JSON)
- Koottu suunnitelma (viisi pohjapiirrosta + tarkistettu kokonaisuus)
- README, ARCHITECTURE, SAFETY -dokumentit
- Testiraportti (15 testiä)
- Itsearviointi (300–400 sanaa)
- Vertaisarviomuistio

Tarkista lopputyön tehtävänannosta arviointikriteerit (25/20/20/20/15 p).

---

**Lopputyön rakentaminen 2/2 — agenttisi on valmis**
