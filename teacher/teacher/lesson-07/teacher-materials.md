# Opettajan materiaalit: Gen AI:n luonne

## Oppimisen tavoitteet (Bloom: analysoi)

Tämän lohkon jälkeen opiskelija:

1. Ymmärtää, miksi generatiiviset kielimallit ovat epädeterministisiä ja mitä lämpötila tekee.
2. Osaa selittää hallusinaatioiden mekanismin: malli ennustaa todennäköisiä sanoja, ei faktoja.
3. Ymmärtää, miksi AI ei ole totuuskone eikä faktakone.
4. Osaa tunnistaa hallusinaation merkkejä käytännössä.
5. Ymmärtää itsenäisen verifiointiprosessin merkityksen tekniikassa ja kriittisissä konteksteissa.

---

## Yleinen pedagoginen lähestymistapa

**Tämä oppitunti on käsitteellisesti haastava,** koska se vaatii opiskelijoilta ajattelutavan muutosta: "AI on käyttäjäystävällinen ja näyttävä, joten se lienee oikeassa."

**Paras lähestymistapa:** Näytä konkreettisia esimerkkejä ennen abstrakteja selityksiä.
- Harjoitus 1 (eri mallit, sama prompti) osoittaa epädeterminismin.
- Harjoitus 2 (hallusinaatioiden metsästys) osoittaa, että mallit voivat olla täysin väärässä.
- Harjoitus 3 (verifiointiprosessi) osoittaa, mitä ammattilainen tekee.

---

## Sisältöohjeet: Avainasiat

### 1. Epädeterminismi ja lämpötila

**Mitä opettaa:**
- Kielimallit tekevät todennäköisyyspohjaisia valintoja, eivät hakuja.
- Jokainen sana valitaan sen perusteella, mikä seuraava sana on todennäköisin (matemaattisesti softmax-funktiolla).
- Lämpötila ohjaa, miten "rohkea" valinta on.

**Analogia (jos opiskelijat ovat hämmentyneitä):**
"Ajattele rulettipyörää. Matala lämpötila = lähes kaikki punaisella. Korkea lämpötila = tasaisempi jakautuminen (suurempi mustan todennäköisyys). Jokainen pyöräytys tulee hieman erilaiseksi."

**Mitä EI opettaa:**
- "Lämpötila vaikuttaa siihen, kuinka 'onnellinen' malli on." (Väärin.)
- "Korkealla lämpötilalla malli 'loukkaa itseään'." (Väärin.)

---

### 2. Hallusinaatiot

**Mitä opettaa:**
- Hallusinaatio = malli sanoo jotain väärää täysin itsevarmasti.
- Syy: malli ennustaa, "miltä vastaukset näyttävät näissä aiheissa" — ei sitä, "mikä on totta".
- Hallusinaatiot ovat tyypillisempiä tekniikassa (API:t, funktiot, komennot), koska mallia on opetettu koodilla, joka näyttää "oikealta".

**Konkreettiset esimerkit:**
- urllib3 HTTP GET -funktio: Malli on oppinut, että "urllib3-kontekstissa" seuraa usein koodia. Se tuottaa näyttävän koodin — mutta funktiota ei ole olemassa.
- "Suomen ensimmäinen pääministeri": Malli on oppinut, että historian kysymyksissä seuraa usein nimiä ja vuosia. Se tuottaa näyttävän vastauksen — mutta se on väärä.

**Mitä opiskelijat omaksuvat itsenäisesti:**
- Itsevarmuus != oikeellisuus.
- Mallia ei "kiinnosta" totuus — se vain ennustaa.

---

### 3. Totuuskone vs. sanojen ennustaja

**Kriittinen käsite:** Tämä on filosofinen ero, joka muuttaa sitä, miten opiskelijat ajattelevat AI:sta.

**Totuuskone:**
- "Mikä on totta?" → Katsoo tietoa → Vastaa totuudenmukaisesti.
- Esim. relaatiotietokanta: "SELECT * FROM customers WHERE last_name = 'Smith'" → tarkka vastaus.

**Sanojen ennustaja:**
- "Mikä seuraava sana on todennäköisin?" → Katsoo kuvioita → Arvaa seuraavan sanan.
- Sillä voidaan tuottaa tekstiä, koodia ja kuvia — mutta se on *ennustusta*, ei *faktaa*.

**Opettajan muistutus:** Tämä ei tarkoita, etteikö AI voisi antaa hyödyllisiä vastauksia. Se tarkoittaa, että **sinun vastuullasi on verifioida kriittiset vastaukset.**

---

## Yleisimmät väärinymmärrykset

### Väärinymmärrys 1: "Malli hallusinoi, koska se on 'huono'."

**Ei. Hallusinaatiot ovat rakenteellinen seuraus siitä, että malli ennustaa sanoja.**

- Jopa parhaat mallit hallusinoivat.
- Hallusinaatiot eivät ole "virhe", joka voidaan "korjata" — ne ovat seurausta siitä, että malli tekee todennäköisyysennusteita, ei faktahakuja.

**Vastaus opiskelijoille:** "Tämä ei ole asia, jota voisi 'paremmalla koulutuksella' poistaa hallusinaatioista. Se on rakenteellinen rajoitus."

### Väärinymmärrys 2: "Matala lämpötila poistaa hallusinaatiot."

**Ei. Matala lämpötila vähentää *satunnaisuutta*, mutta ei poista hallusinaatioiden *mahdollisuutta*.**

- Matala lämpötila = todennäköisemmin "näyttävä" hallusinaatio.
- Korkea lämpötila = satunnaisempi, selvemmin väärä vastaus.
- Hallusinaatio voi esiintyä millä tahansa lämpötilalla.

---

### Väärinymmärrys 3: "Jos malli kuulostaa varmalta, se tietää, mistä puhuu."

**Ei. Itsevarmuus on tekninen artefakti: malli lopettaa vain, kun se arvioi seuraavan sanan olevan [LOPPU].**

- Malli ei "tiedä" olevansa väärässä.
- Malli ei varoita itseään.
- Itsevarmuus on täysin irrallaan tarkkuudesta.

---

## Opettajan vinkkejä harjoituksiin

### Harjoitus 1: Sama prompti, eri mallit

**Jos haluat dramaattisempia eroja:**
- Käytä asteittain harhaanjohtavampaa promptia.
- Esim. "Kirjoita koodi, joka käyttää urllib3-kirjaston HTTP-metodia 'FETCH'." (FETCH ei ole olemassa.)
- Jopa mallit eroavat siinä, miten ne hallusinoivat.

**Jos opiskelijat kysyvät: "Miksi ChatGPT:n vastaus oli parempi kuin Clauden?"**
- Selitä: Koulutusdata, parametrit ja arkkitehtuuri ovat erilaisia.
- Tämä ei ole "oikein vs. väärin" — vaan kyse on erilaisista parametreista.

### Harjoitus 2: Hallusinaatioiden metsästys

**Case-tutkimusten valinta:**
- Valitse asioita, jotka ovat "lähellä totta" (IT-opiskelijoille tekniikka on parempi kuin historia).
- Testaa kaikki case-tutkimukset etukäteen — ne vaihtelevat malleittain.

**Jos ryhmä ei löydä hallusinaatiota:**
- Kysykää: "Etsi jokin väite, joka on liian yksityiskohtainen. Voitko verifioida sen?"
- Jos he eivät voi verifioida sitä helposti, se on merkki hallusinaatiosta.

### Harjoitus 3: Verifiointiprosessin suunnittelu

**Tämän tulee olla käytännöllinen, ei teoreettinen.**

**Vahva vastaus:**
```
1. Tarkista tietokannan dokumentaation sarakkeet
2. Kysy ChatGPT:ltä spesifisesti: "Tietokannan sarakkeet ovat X, Y, Z. Kirjoita kysely..."
3. Lue vastaus ja tutki syntaksia — vertaa SQL-oppikirjaan tai dokumentaatioon
4. Testaa kysely ensin testiympäristössä (rajallinen data, turvallinen ympäristö)
5. Dokumentoi: "ChatGPT ehdotti X:ää. Käytin sitä, koska Y. Muutin Z:aa, koska Z:ssa oli huoli (linkki dokumentaatioon)."
```

**Heikko vastaus:**
```
"Tarkistan sen silmäilemällä." (Sitten mitä?)
"Luotan ChatGPT:hen." (Sitten et verifioi!)
```

---

---

## Formatiivinen tarkistuspiste — Todistusaineisto 3

### Tavoite
Opiskelija yhdistää oppituntien 3, 5 ja 7 opit yhdeksi käytännön tarkistuslistaksi. Tämä on viimeinen rakennuspalikka ennen Teoria-osion arviointitehtävää.

### Mitä etsiä palautuksesta
- **Synteesi, ei listaus:** Opiskelija yhdistää kolmen oppitunnin käsitteet (tokenien ennustaminen, kontekstin katoaminen, hallusinaatiot) yhdeksi kokonaisuudeksi — ei vain listaa kolmea erillistä asiaa
- **Konkreettiset toimenpiteet:** Tarkistuslistassa on tehtäviä, jotka voi tehdä oikeasti ("tarkista vastaus dokumentaatiosta", "toista rajaukset pitkässä keskustelussa")
- **Ammatillisuus:** Opiskelija puhuu ammattilaisena, ei opiskelijana — "kun käytän tekoälyä työssä, teen näin"

### Yleinen väärinymmärrys
"Riittää kun tarkistaa onko vastaus oikein" → ohjaa kohti prosessia: "Miten tarkistat? Mistä tiedät? Mitä jos et huomaa virhettä?"

### Palautteen antaminen
Tämä on viimeinen tarkistuspiste ennen arviointia. Jos opiskelijan tarkistuslista on heikko, tämä on viimeinen mahdollisuus ohjata ennen arviointituntia. Anna konkreettinen palaute: "Lisää tähän vielä yksi asia: mitä teet jos keskustelu on pitkä ja epäilet kontekstin kadonneen?"

### Yhteys arviointiin
Opiskelijat, jotka ovat tehneet kaikki kolme todistusaineistoa, ovat merkittävästi paremmassa asemassa Teoria-osion arvioinnissa. He eivät joudu aloittamaan tyhjästä, vaan heillä on kolme valmista rakennuspalikkaa. Tämä on tarkoituksellista — formatiivinen arviointi ei ole ylimääräistä työtä, vaan osa oppimisprosessia.

## Aika- ja resurssiehdotukset

| Aktiviteetti | Aika | Resurssi |
|---|---|---|
| Itseopiskeluosa | 30–40 min | Oppikirja, muistiinpanot |
| Harjoitus 1 (eri mallit) | 15 min | Selaimessa avoinna olevat mallit |
| Harjoitus 2 (hallusinaatiot) | 20 min | Case-tutkimukset (jaettu) |
| Harjoitus 3 (verifiointiprosessi) | 25 min | Valkokangas/taulukko ideoille |
| Yhteenveto | 10 min | — |
| **Yhteensä** | **~100 min** | — |

---

## Jälkipuolella (seuraavat oppitunnit)

**Oppitunti 8 jatkaa** eettisestä näkökulmasta: tekijänoikeudet, harha, ympäristövaikutukset.

Tämä oppitunti (7) on tekninen perusta. Oppitunti 8 rakentuu sen päälle.