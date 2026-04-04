# Opettajan materiaalit: Gen AI:n luonne

## Oppimisen tavoitteet (Bloom: Analysoi)

Tämän lohkon jälkeen opiskelija:

1. Ymmärtää, miksi generatiiviset kielimallit ovat epädeterminisiä ja mitä lämpötila tekee.
2. Osaa selittää hallusinaatioiden mekanismin: malli ennustaa todennäköisiä sanoja, ei faktoja.
3. Ymmärtää, miksi AI ei ole totuuskone eikä faktakone.
4. Osaa tunnistaa hallusinaation merkkejä käytännössä.
5. Ymmärtää itsenäisen verifiointiprosessin merkityksen tekniikan ja kriittisissä konteksteissa.

---

## Yleinen pedagoginen lähestymistapa

**Tämä oppitunti on käsitteellisesti haastava,** koska se vaatii opiskelijoilta ajatusten muutosta: "AI on käyttäjäystävällinen ja näyttävä, joten se lienee oikeassa."

**Paras lähestymistapa:** Näytä konkreettisia esimerkkejä ennen abstrakteja selityksiä.
- Harjoitus 1 (eri mallit, sama promt) osoittaa epädeterminismin.
- Harjoitus 2 (hallusinaatioiden metsästys) osoittaa, että mallit voivat olla täysin väärässä.
- Harjoitus 3 (verifiointiprosessi) osoittaa, mitä ammattilaisesti tehdään.

---

## Sisältöohjeet: Avainasiat

### 1. Epädeterminismi ja lämpötila

**Mitä opettaa:**
- Kielimallit tekevät todennäköisyyspohjaisia valintoja, eivät hakuja.
- Jokainen sana valitaan perusteella "mikä seuraava sana on todennäköisesti" (matemaattisesti, softmax-funktiolla).
- Lämpötila ohjaa, miten "rohkea" valinta on.

**Analogia (jos opiskelijat ovat hämmentyneet):**
"Ajattele rullettipyörää. Matala lämpötila = lähes kaikki punaisella. Korkea lämpötila = tasaisempi jakautuminen (enemmän mustan todennäköisyys). Jokainen spinni tulee hieman erilaiseksi."

**Mitä EI opeta:**
- "Lämpötila vaikuttaa siihen, kuinka 'onnellinen' malli on." (Väärä.)
- "Korkealla lämpötilalla malli 'loukkaansa'." (Väärä.)

---

### 2. Hallusinaatiot

**Mitä opettaa:**
- Hallusinaatio = malli sanoo jotain väärää täysin itsevarmuudella.
- Syy: malli ennustaa "mitä näyttävät vastaukset näyttävät näillä aiheilla" — ei "mikä on totta".
- Hallusinaatiot ovat tyypillisempiä tekniikan kanssa (API:t, funktiot, komennot), koska mallia on opetettu koodista, joka näyttää "oikealta".

**Konkreettiset esimerkit:**
- urllib3 HTTP GET -funktio: Malli on oppinut, että "urllib3 kontekstissa" seuraa usein koodia. Se tuottaa näyttävän koodin — mutta funktio ei ole olemassa.
- "Suomen ensimmäinen pääministeri": Malli on oppinut, että "historian kysymyksissä" seuraa usein nimiä ja vuosia. Se tuottaa näyttävän vastauksen — mutta se on väärä.

**Mitä opiskelijat omaksuvat itsenäisesti:**
- Itsevarmuus != oikeellisuus.
- Mallia ei "kiinnosta" totuus — se vain ennustaa.

---

### 3. Totuuskone vs. sanojen ennustaja

**Kriittinen käsite:** Tämä on filosofinen ero, joka muuttaa, miten opiskelijat ajattelevat AI:sta.

**Totuuskone:**
- "Mikä on totta?" → Katsoo tietoa → Vastaa totta.
- Esim. relaatiotietokanta: "SELECT * FROM customers WHERE last_name = 'Smith'" → tarkka vastaus.

**Sanojen ennustaja:**
- "Mikä seuraava sana on todennäköisesti?" → Katsoo kuvioita → Arvaa seuraavan sanan.
- Voidaan tuottaa tekstiä, koodia, kuvia — mutta se on *ennustusta*, ei *faktaa*.

**Opettajan muistutus:** Tämä ei tarkoita, etteikö AI voisi antaa hyödyllisiä vastauksia. Se tarkoittaa, että **sinun vastuullasi on verifioidaan kriittiset vastaukset.**

---

## Yleisimmät väärinymmärrykset

### Väärinymmärrys 1: "Malli hallusinoi koska se on 'huono'."

**Ei. Hallusinaatiot ovat rakenteellinen seuraus siitä, että malli ennustaa sanoja.**

- Jopa parhaat mallit hallusinoivat.
- Hallusinaatiot eivät ole "virhe", joka voidaan "korjata" — ne ovat seurausta siitä, että malli tekee todennäköisyysennustuksia, ei faktahakuja.

**Vastaus opiskelijoille:** "Tämä ei ole malli, jota voi 'paremmin kouluttaa pois' hallusinaatioista. Se on rakenteellinen rajatus."

### Väärinymmärrys 2: "Matala lämpötila poistaa hallusinaatiot."

**Ei. Matala lämpötila vähentää *satunnaisuutta*, mutta ei poista hallusinaatioiden *mahdollisuutta*.**

- Matala lämpötila = todennäköisemmin "näyttävä" hallusinaatio.
- Korkea lämpötila = satunnaisempi, selvemmin väärä vastaus.
- Hallusinaatio voi esiintyä millä tahansa lämpötilalla.

---

### Väärinymmärrys 3: "Jos malli kuulostaa varmalta, se tietää, mistä se puhuu."

**Ei. Itsevarmuus on tekninen artefakti: malli lopettaa vain, kun se ajattelee seuraavan sanan olevan [LOPPU].**

- Malli ei "tiedä" olevansa väärässä.
- Malli ei varoita itseään.
- Itsevarmuus on täysin irrallaan tarkkuudesta.

---

## Opettajan vinkkejä harjoituksiin

### Harjoitus 1: Sama promt, eri mallit

**Jos haluat dramaattisempia eroja:**
- Käytä asteittain harhaanjohtavampaa promptia.
- Esim: "Kirjoita koodi, joka käyttää urllib3-kirjaston HTTP-metodia 'FETCH'." (FETCH ei ole olemassa.)
- Jopa mallit ovat erilaisia siinä, kuinka ne hallusinoivat.

**Jos opiskelijat kysyvät "Miksi ChatGPT:n vastaus oli parempi kuin Clauden?":**
- Selitä: Koulutusdata, parametrit ja arkkitehtuuri ovat eri.
- Tämä ei ole "oikein vs. väärin" — se on "eri parametroisuus".

### Harjoitus 2: Hallusinaatioiden metsästys

**Case-tutkimusten valinta:**
- Valitse asiat, jotka ovat "lähellä tosi" (IT-opiskelijoille tekniikka on parempi kuin historia).
- Testaa kaikki case-tutkimukset etukäteen — ne vaihtelevat malleittain.

**Jos ryhmä ei löydä hallusinaatiota:**
- Kysykää: "Etsi jokin väite, joka on liian yksityiskohtainen. Voitko verifioidaan sen?"
- Jos he eivät voi verifioidaan helppokäyttöisesti, se on merkki hallusinaatiosta.

### Harjoitus 3: Verifiointiprosessin suunnittelu

**Tämän tulee olla käytännöllinen, ei teoreettinen.**

**Vahva vastaus:**
```
1. Tarkista tietokannan dokumentaation sarakkeet
2. Kysy ChatGPT:ltä spesifisesti: "Tietokannan sarakkeet ovat X, Y, Z. Kirjoita kysely..."
3. Lue vastaus ja tutki syntaksia — vertaa SQL-oppikirjaan tai dokumentaatioon
4. Testaa kyselyt testiajosta ensin (rajallinen data, turvallinen ympäristö)
5. Dokumentoi: "ChatGPT ehdotti X. Käytin sen koska Y. Muutin Z koska Z:lla oli huoli (linkki dokumentaatioon)."
```

**Heikko vastaus:**
```
"Tarkistan sen silmäilemällä." (Sitten mitä?)
"Luotan ChatGPT:hen." (Sitten et verifioi!)
```

---

## Aika- ja resurssiehdotukset

| Aktiviteetti | Aika | Resurssi |
|---|---|---|
| Itseopiskeluosa | 30–40 min | Oppikirja, muistiinpano |
| Harjoitus 1 (eri mallit) | 15 min | Selaimen avoimet mallit |
| Harjoitus 2 (hallusinaatiot) | 20 min | Case-tutkimukset (jaettu) |
| Harjoitus 3 (verifiointiprosessi) | 25 min | Valkokangas/taulukko ideoille |
| Yhteenveto | 10 min | — |
| **Yhteensä** | **~100 min** | — |

---

## Jälkipuolella (seuraavat oppitunnit)

**Lesson 8 jatkaa** eettisestä näkökulmasta: tekijänoikeudet, harha, ympäristövaikutukset.

Tämä oppitunti (7) on tekninen perusta. Lesson 8 on moraalinen rakentaminen päälle.

