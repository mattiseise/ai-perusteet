# Opettajavetoiset tehtävät

## Tehtävä 15.3: Live-dokumentaation kirjoittaminen

### Tavoite

Osoittaa konkreettisesti, miten AI voi auttaa dokumentaation kirjoittamisessa — ja että dokumentaatio ei ole "kuolleita asioita", vaan ammattilaisuutta.

### Opettajan ohjeet ja fasilitaatio

Tämä tehtävä tehdään opettajan johdolla koko luokalle. Live-esittely on tehokkain.

**Valmistelu (ennen lähiosaa):**
- Valitse todellinen projekti (vaikka yksinkertainen)
- Testaa AI:n kanssa: pyydä README-pohja, muokkaa sitä
- Valmista 2-3 erilaista versiota: AI:n tuottama, muokattu, täydellinen

**Tehtävän vaiheet (20 min):**

1. **Johdanto (2 min):** "Dokumentaatio on ammattilaisuutta. Mutta se ei ole tylsää — se on hyödyllistä."

2. **Esimerkki 1: AI:n pohja (6 min)**
   - Näytä todellinen projekti (GitHub-sivu tai paikallinen hakemisto)
   - Pyydä AI:ta: "Kirjoita README-tiedosto tälle Python-projektille, joka... [spesifikaatiot]"
   - Näytä AI:n tuottama pohja
   - Kysy: "Mitä on hyvää? Mitä puuttuu?"

3. **Muokkaus (8 min)**
   - Muokkaa README yhdessä luokan kanssa
   - Lisää todellisia komentoja, esimerkkejä, linkkejä
   - Näytä, miten muokkaus tekee siitä ammattilaisemmaksi
   - Kysy: "Nyt pitäisikö uuden käyttäjän osata asentaa tämä?"

4. **Loki-analyysi (3 min)**
   - Näytä loki, jossa on virheitä
   - Pyydä AI:ta: "Analysoi tämä loki ja kerro: mitä meni pieleen?"
   - Näytä AI:n vastaus
   - Kysy: "Pystyikö AI näkemään virheitä nopeammin kuin sinä?"

5. **Yhteenveto (1 min):** Kolme asiaa:
   - Dokumentaatio on tärkeää ammattilaisena
   - AI voi auttaa pohjan luomisessa
   - Sinä olet vastuussa laadusta — AI on apulainen

### Odotettu oppimistulos

- Opiskelijat näkevät, että dokumentaatio ei ole vaikea — se on rakenne
- Opiskelijat näkevät, että AI voi säästää aikaa
- Opiskelijat ymmärtävät, että ammattilaisella on dokumentaatio, ei vain koodi

---

## Tehtävä 15.4: Pienryhmä-harjoitus: Dokumentaation tarkistus

### Tavoite

Opiskelija oppii kritisoimaan ja parantamaan dokumentaatiota.

### Opettajan ohjeet ja fasilitaatio

Pienryhmät (2–3 henkilöä), opettaja valvoo.

**Valmistelu:**
- Valmista 2-3 dokumentaatiopohjaa: yksi huono, yksi ok, yksi hyvä
- Varmista, että ryhmät näkevät jokaisen version

**Tehtävän vaiheet (20 min):**

1. **Jakelu (1 min):** Jokainen ryhmä saa dokumentaation

2. **Analyysivaihe (10 min):** Ryhmä arvioi:
   - Mitä dokumentaatio kertoo? (selkeä?)
   - Mitä puuttuu? (asennus? käyttö? esimerkit?)
   - Pystyisikö uusi käyttäjä asentamaan sen näiden ohjeiden mukaisesti?
   - Mitä muokkaa?

3. **Muokkaus-ehdotukset (8 min):** Ryhmä kirjoittaa:
   - Yksi asia, joka on hyvää
   - Kolme asiaa, joka puuttuu tai on sekavaa
   - Yksi muokkaus-ehdotus

4. **Raportointi (1 min per ryhmä):** Ryhmä sanoo:
   - Dokumentaation tyyppi (README, API-dokumentaatio jne.)
   - Yksi asia, joka on hyvää
   - Yksi asia, jota pitää parantaa

### Odotettu oppimistulos

- Opiskelijat näkevät, että dokumentaation laadulla on vaikutusta
- Opiskelijat osaa arvioida: onko dokumentaatio riittävä uudelle käyttäjälle?
- Opiskelijat on valmiita kirjoittamaan omaa dokumentaatiota

---

## Tehtävä 15.5: Turvallisuus: CLI-komennot ja validointi

### Tavoite

Osoittaa, että komentorivikomennot voivat olla vaarallisia — ja miten AI:ta käytetään turvallisesti.

### Opettajan ohjeet ja fasilitaatio

Tämä tehtävä tehdään opettajan johdolla koko luokalle.

**Valmistelu:**
- Valmista 3-4 CLI-komentoa: jotkut turvallisia, jotkut vaarallisia
- Testaa ne etukäteen
- Valmista selitys jokaiselle

**Tehtävän vaiheet (15 min):**

1. **Johdanto (2 min):** "CLI-komennot voivat tehdä mitä tahansa — asentaa, poistaa, muuttaa. Sinun täytyy ymmärtää ne ennen ajamista."

2. **Esimerkki 1: Vaarallinen komento (5 min)**
   - Näytä komento: `rm -rf /etc/`
   - Kysy: "Mitä tämä tekee? Onko se turvallinen?"
   - Selitä: `rm` poistaa, `-rf` poistaa rekursiivisesti ilman vahvistusta, `/etc/` on kriittinen järjestelmä-hakemisto
   - Näytä: "Jos ajaisi tämän, järjestelmä hajoaa."

3. **Esimerkki 2: Turvallinen alternatiivi (5 min)**
   - Näytä turvallisempi komento: `find /home -name "*.tmp" -type f | head -20`
   - Selitä: tämä näyttää ensin mitä poistettaisiin
   - Näytä: kuinka voit muuttaa sen poistamiseen `| xargs rm` jälkeen
   - Näytä: kaksi askelta = turvallisempi

4. **AI:n käyttö (2 min):**
   - Näytä: "Kun AI antaa komentoja, kysy ENSIN mitä se tekee, sitten kokeile ensin turvallisesti"
   - Esimerkki: `ls` ensin, sitten `rm`

5. **Yhteenveto (1 min):** Neljä sääntöä:
   - Ymmärrä komento ennen ajamista
   - Testaa turvallisesti ennen oikeaa versiota
   - Vaa harkat komennot (`-delete`, `rm`, `dd`) vaativat erityistä huomiota
   - AI auttaa, mutta sinä olet vastuussa

### Odotettu oppimistulos

- Opiskelijat näkevät, että CLI voi vahingoittaa
- Opiskelijat osaa ajatella turvallisuudesta
- Opiskelijat ei kopioi-liitä komentoja sokeasti

