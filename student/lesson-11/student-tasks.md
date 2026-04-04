# Opiskelutehtävät

## Tehtävä 11.1: Huonosta promptista hyvään — Parantamisen harjoitus

### Tavoite
Oppia tunnistamaan huonon promptin piirteet ja parantamaan ne viiden elementin (tavoite, rooli, rajat, formaatti, esimerkit) avulla.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

1. **Sinulle annetut huonot promptit:**
   - Prompt A: "Kirjoita funktio validoinnille."
   - Prompt B: "Selitä, mitä on API."
   - Prompt C: "Korjaa tämä koodi."

2. **Valitse kaksi kolmesta promptista ja paranna niitä**
   - Lisää **tavoite**: Tee se erityiseksi ja selkeäksi.
   - Lisää **rooli**: Mitä roolissa tekoäly on? (esim. Python-kehittäjä, opettaja, turva-asiantuntija)
   - Lisää **rajat**: Mitä EI tehdä? Kuinka yksityiskohtaista? Kuinka pitkää?
   - Lisää **formaatti**: Miten vastaus muotoillaan? (koodi, taulukko, lista, vaiheet?)
   - Lisää **esimerkit**: Anna vähintään yksi konkreettinen esimerkki, mitä haluat nähdä.

3. **Dokumentointi-taulukko**
   - Täytä tämä taulukko jokaiselle parantamallesi promptille:

| Elementti | Alkuperäinen prompt | Parannettu prompt |
|-----------|-------------------|------------------|
| Tavoite | (mitä puuttui) | (miten lisäsit sen) |
| Rooli | | |
| Rajat | | |
| Formaatti | | |
| Esimerkki | | |

4. **Testaaminen (valinnainen, jos pääsy ChatGPT:hen)**
   - Testaa alkuperäinen prompt tekoälyssä.
   - Testaa parannettu prompt.
   - Vertaa vastauksia: mikä oli parempi?

### Odotettu tuotos

- Kaksi täytettyä dokumentaatio­taulukkoa
- Parannetut promptit (kirjoitettuna kokonaisuudessaan)
- Jos testaavat: kuvakaappaukset molemmista vastauksista ja havaintoja eroista

**Jos teet tehtävän yksin:**
Paranna kahta kolmesta annetuista huonoista prompteista ja dokumentoi samalla tavalla.

---

## Tehtävä 11.2: Iteratiivinen prompt-rakentaminen — Kierros kierrokselta

### Tavoite
Ymmärtää, kuinka ammattilaiset rakentavat kontekstia iteratiivisesti — ensimmäinen prompt antaa perusvastauksen, seuraavat promptit terävöittävät sitä.

### Ohjeet (ryhmätehtävä, 2–3 henkilöä)

1. **Tehtävä: Rakenna Python-validointifunktio iteratiivisesti**

2. **Kierros 1 — Peruspromt­ti:**
   - Kirjoita perus­prompt: "Kirjoita Python-funktio, joka validoi sähköpostiosoitteen."
   - Jos pääsy ChatGPT:hen: testaa ja kopioi vastaus.
   - Jos ei pääsyä: dokumentoi, mitä odottaisit saavasi.

3. **Kierros 2 — Lisäys 1:**
   - Jatkoprompti: "Lisää docstring ja kommentit. Hylkää välilyönnit."
   - Dokumentoi: mitä muuttui? Mitä parannettiin?

4. **Kierros 3 — Lisäys 2:**
   - Jatkoprompti: "Nyt kirjoita vähintään 3 testit funktiolle. Käytä assert-lauseita."
   - Dokumentoi: mitä saivat? Oliko se yhdistetty edelliseen kontekstiin?

5. **Kierros 4 — Iteraatio 3:**
   - Jatkoprompti: "Muuta testit pytest-muotoon ja lisää edge-case varten (esim. osoite ilman @-merkkiä)."
   - Dokumentoi: kuinka hyvä lopputulos oli?

6. **Yhteenveto-taulukko**
   - Täytä tämä taulukko:

| Kierros | Prompt | Saatu vastaus (yhteenveto) | Mitä parannettiin | Konteksti kertyi |
|---------|--------|--------------------------|------------------|-----------------|
| 1 | Peruspromt­ti | [yhteenveto] | Perusfunktio | Kyllä |
| 2 | Lisää docstring | | | |
| 3 | Kirjoita testit | | | |
| 4 | Pytest-muoto | | | |

### Odotettu tuotos

- Täytetty iteraatio­taulukko
- Dokumentaatio jokaisesta kierroksesta (tai kuvakaappaukset testauksista)
- Johtopäätös: "Iteratiivinen lähestyminen oli tehokkaampi kuin [vaihtoehto], koska..."

**Jos teet tehtävän yksin:**
Tee kolme kierrosta samalla tavalla ja dokumentoi ne.

---

## Tehtävä 11.3: Prompt vs. konteksti — Eroja ja linkkejä

### Tavoite
Ymmärtää ero promptin (tehtävänanto) ja kontekstin (ympäröivä tieto) välillä ja osata käyttää niitä ammattilaisesti.

### Ohjeet (ryhmä tai yksin)

1. **Annettu skenaario:**
   - Sinun on kirjoitettava asiakaspalvelun sähköpostin vastaus asiakkaalle, joka on valittanut hitaasta palvelusta.

2. **Ensimmäinen: Prompt ilman kontekstia**
   - Prompt: "Kirjoita sähköpostin vastaus valituksen johdosta."
   - Jos pääsy tekoälyyn: testaa ja näe, mitä saat.
   - Dokumentoi: Oliko vastaus sopivan sävyä? Onko se riittävän henkilökohtainen? Mitä puuttuu?

3. **Toinen: Sama prompt + konteksti**
   - Lisää konteksti: "Asiakas otti yhteyttä kahdesti. Ensimmäisellä kerralla ei saanut vastausta 48 tunnissa. Toisella kerralla sai vastauksen, mutta se ei ratkaissut ongelmaansa. Asiakas on ollut asiakkaana 5 vuotta."
   - Prompt: "Kirjoita sähköpostin vastaus valituksen johdosta. Asiakas on arvokas pitkäaikainen asiakas, joka on pettynyt hitauteen ja ratkaisun puuttumiseen."
   - Jos pääsy tekoälyyn: testaa ja näe, mitä saat.
   - Dokumentoi: Miten vastaus muuttui?

4. **Analyysi-taulukko**

| Aspekti | Prompt ilman kontekstia | Prompt + konteksti |
|---------|-------------------------|-------------------|
| Sävy | [esim. Neutraali] | [esim. Pahoitteleva] |
| Henkilökohtaisuus | [esim. Vähän] | [esim. Paljon] |
| Ymmärrys asiakkaan tilanteesta | | |
| Laatu | 1-5 | 1-5 |

5. **Johtopäätös**
   - Miksi konteksti on kriittinen?
   - Ammattilaisesti: kuinka rakentaisit kontekstia asiakaspalvelutehtävässä?

### Odotettu tuotos

- Täytetty vertailu­taulukko
- Kuvakaappaukset tai dokumentaatio molemmista testeistä (jos testattu)
- Kirjallinen johtopäätös (2-3 lausetta) siitä, miksi konteksti ratkaisee

**Jos teet tehtävän yksin:**
Tee sama harjoitus yksin ja dokumentoi omat havainnot.
