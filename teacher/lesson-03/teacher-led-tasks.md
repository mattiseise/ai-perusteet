# Opettajavetoiset tehtävät

## Tehtävä 3.1: Seuraavan sanan ennustaminen — luokkakeskustelu ja demo

### Tavoite

Tehtävän tavoitteena on näyttää konkreettisesti, miten **kielimalli** tuottaa tekstiä ennustamalla seuraavaa sanaa tai tekstin osaa yksi vaihe kerrallaan. Opiskelijat ymmärtävät, että kielimallin vastaus rakentuu vaiheittaisista ennusteista eikä valmiiksi suunnitellusta kokonaisvastauksesta.

**Opettajan painotus:** Korosta, että kielimalli ei “tiedä” seuraavaa sanaa samalla tavalla kuin ihminen. Se arvioi, mikä tekstin osa on todennäköinen aiemman kontekstin ja opetusdatan perusteella.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**

Valmista lyhyt teksti, josta puuttuu sanoja. Voit käyttää esimerkiksi seuraavaa lausetta:

Seuraavaksi hän avasi \_\_\_\_\_ ja luki kirjeitä. Kaikki olivat \_\_\_\_\_.

Projisoi teksti tai kirjoita se taululle niin, että opiskelijat näkevät puuttuvat kohdat selvästi.

### Toteutus noin 20 minuuttia

1. **Avaus noin 2 minuuttia:**


   Kerro opiskelijoille:

   > Nyt harjoittelemme, miten kielimalli tuottaa tekstiä. Se ei kirjoita koko vastausta valmiiksi yhdellä kertaa, vaan ennustaa seuraavaa sanaa tai tekstin osaa vaihe kerrallaan. Kokeillaan, miten hyvin me osaamme tehdä saman.
2. **Ensimmäisen puuttuvan sanan arvaaminen noin 5 minuuttia:**

   1. Näytä lauseen alku: `Seuraavaksi hän avasi _____`
   2. Kysy luokalta: **Mikä sana voisi tulla seuraavaksi?**
   3. Kerää taululle 5–6 opiskelijoiden ehdotusta.
   4. Kysy: **Mitä yhteistä näillä sanoilla on? Miksi juuri nämä sanat tuntuvat mahdollisilta?**
   5. Näytä halutessasi ChatGPT:n tai muun kielimallin vastaus samalla lauseen alulla.
3. **Toisen puuttuvan sanan arvaaminen noin 5 minuuttia:**

   1. Näytä lauseen toinen kohta: `Kaikki olivat _____.`
   2. Kysy opiskelijoilta uusia ehdotuksia.
   3. Kirjoita ehdotukset taululle.
   4. Keskustelkaa siitä, mitkä ehdotukset sopivat lauseeseen ja mitkä eivät.
4. **Analyysi noin 5 minuuttia:**

   Selitä opiskelijoille:

   > Kielimalli valitsee seuraavan sanan tai tekstin osan todennäköisyyksien perusteella. Se ei tiedä samalla tavalla kuin ihminen, mikä sana on varmasti oikea. Se arvioi, mitkä sanat ovat esiintyneet usein samankaltaisissa yhteyksissä sen opetusdatassa.

   Kirjoita taululle:

   Next-token prediction = seuraavan tekstiosan ennustaminen todennäköisyyksien perusteella.
5. **Johtopäätös noin 3 minuuttia:**

   Kerro opiskelijoille:

   > Tämän vuoksi ChatGPT voi vaikuttaa älykkäältä. Se pystyy tuottamaan hyvin toimivia sanayhdistelmiä, mutta se tekee sen ennustamalla tekstiä vaihe vaiheelta.

### Keskustelun tueksi

| Kysymys opiskelijoille | Mitä kysymyksellä tavoitellaan? |
| --- | --- |
| Miksi jotkin sanat tuntuivat todennäköisemmiltä kuin toiset? | Opiskelija huomaa, että konteksti rajaa mahdollisia jatkoja. |
| Voiko sama alku johtaa useaan järkevään jatkoon? | Opiskelija ymmärtää, että yksi ainoa “oikea” jatko ei aina ole olemassa. |
| Mitä tapahtuu, jos ensimmäinen ennuste ohjaa tekstin väärään suuntaan? | Opiskelija ymmärtää, että virhe voi kasautua seuraavissa vaiheissa. |

**Esimerkki opetukseen**

Jos opiskelijat ehdottavat erilaisia sanoja, älä etsi heti yhtä oikeaa vastausta. Käytä tilannetta osoittamaan, että kielimallikin voi valita monen todennäköisen vaihtoehdon väliltä.

### Odotettu oppimistulos

Tehtävän jälkeen opiskelijat ymmärtävät, että:

- **kielimalli** ei suunnittele koko vastausta samalla tavalla kuin ihminen, vaan ennustaa tekstiä vaiheittain,
- mallin tuottama vaikutelma älykkyydestä syntyy siitä, että se osaa yhdistää sanoja ja ilmauksia usein toimivalla tavalla,
- malli voi mennä pieleen missä tahansa vaiheessa, jos sen ennuste ohjautuu väärään suuntaan.

---

## Tehtävä 3.2: Hallusinaatiot livenä — näytä virhe ja analysoi

### Tavoite

Tehtävän tavoitteena on osoittaa, että **kielimalli** voi tuottaa vakuuttavalta kuulostavia mutta virheellisiä vastauksia. Tätä ilmiötä kutsutaan **hallusinaatioksi**. Opiskelijat oppivat, miksi tekoälyn tuottamaa tietoa pitää tarkistaa kriittisesti.

**Opettajan painotus:** Hallusinaation vaarallisuus ei ole vain siinä, että vastaus on väärä. Erityisen vaarallista on se, että väärä vastaus voi kuulostaa varmalta, sujuvalta ja asiantuntevalta.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**

Valitse etukäteen kolme kysymystä, joiden avulla voit testata kielimallin luotettavuutta. Valitse kysymyksiä, joissa on riski, että malli keksii uskottavalta kuulostavan mutta väärän vastauksen.

Voit käyttää esimerkiksi seuraavia kysymystyyppejä:

1. Kysymys olemattomasta kirjasta, elokuvasta tai käsitteestä.
2. Kysymys ajankohtaisesta faktasta, joka pitää tarkistaa luotettavasta lähteestä.
3. Kysymys henkilöstä, organisaatiosta tai roolista, jossa malli voi arvata väärin.

**Esimerkkejä testikysymyksistä:**

- `Kuka kirjoitti romaanin "Suuri Älyntestaus"?`
- `Mikä on Suomen pääkaupunki vuonna 2026?`
- `Kuka on Teknillisen korkeakoulun rehtori vuonna 2026?`

**Huomio:** Tarkista esimerkkien oikeat tiedot etukäteen luotettavasta lähteestä, jotta voit näyttää opiskelijoille, miten vastaus varmistetaan. Ajankohtaiset henkilö- ja organisaatiotiedot voivat muuttua, joten niitä ei kannata käsitellä muistin varassa.

### Toteutus noin 20 minuuttia

1. **Avaus noin 2 minuuttia:**


   Kerro opiskelijoille:

   > Näytän teille, miten kielimalli voi vaikuttaa vakuuttavalta myös silloin, kun se on väärässä. Tätä kutsutaan hallusinaatioksi.
2. **Testi 1 noin 5 minuuttia:**

   1. Kysy kielimallilta esimerkiksi: `Kuka kirjoitti romaanin "Suuri Älyntestaus"?`
   2. Näytä vastaus luokalle.
   3. Kysy opiskelijoilta: **Näyttääkö vastaus uskottavalta? Mistä voimme tietää, onko se totta?**
   4. Tarkistakaa vastaus yhdessä luotettavasta lähteestä tai osoittakaa, ettei teoksesta löydy luotettavaa tietoa.
   5. Selitä: “Malli ei välttämättä tiedä, onko teos olemassa. Se voi tuottaa uskottavalta kuulostavan vastauksen, koska sanat sopivat sen oppimiin tekstikuvioihin.”
3. **Testit 2 ja 3 noin 8 minuuttia:**

   1. Tee kaksi muuta testiä samalla tavalla.
   2. Näytä mallin vastaus.
   3. Kysy jokaisen vastauksen jälkeen: **Miten tämän voisi tarkistaa?**
   4. Kysy myös: **Valehteleeko malli tarkoituksella vai ennustaako se väärän vastauksen?**
4. **Analyysi noin 5 minuuttia:**

   Kirjoita taululle:

   Hallusinaatio = kielimalli tuottaa virheellistä tai keksittyä sisältöä, joka voi kuulostaa uskottavalta.

   Korosta opiskelijoille:

   - Malli ei valehtele tarkoituksella.
   - Se tuottaa sanoja ja lauseita todennäköisyyksien perusteella.
   - Vaarallista on se, että virheellinen vastaus voi näyttää luotettavalta.

   Kysy lopuksi: **Missä ammatillisissa tilanteissa hallusinaatiot olisivat erityisen vaarallisia?**

   Esimerkkejä keskusteluun:

   - lääketiede,
   - oikeudelliset kysymykset,
   - tietoturva,
   - asiakasviestintä,
   - liikesalaisuudet ja yrityksen päätöksenteko.

### Hallusinaation tarkistusmalli

| Tarkistuskysymys | Miksi se on tärkeä? |
| --- | --- |
| Mihin lähteeseen vastaus perustuu? | Ilman lähdettä vastaus voi olla pelkkä uskottava arvaus. |
| Voiko tieto olla vanhentunutta? | Ajankohtaiset tiedot, roolit ja organisaatiot muuttuvat. |
| Onko kysymyksessä virheellinen oletus? | Malli voi vastata kysymykseen, vaikka kysymyksen lähtökohta olisi väärä. |
| Kuulostaako vastaus varmalta ilman perusteluja? | Itsevarma sävy ei todista, että tieto on oikein. |

**Esimerkki opetukseen**

Kun kielimalli antaa uskottavan vastauksen, pysähdy ennen oikean tiedon paljastamista ja kysy opiskelijoilta: “Mikä tässä saa vastauksen tuntumaan luotettavalta?” Näin opiskelijat oppivat tunnistamaan uskottavan kielen ja todellisen luotettavuuden eron.

### Odotettu oppimistulos

Tehtävän jälkeen opiskelijat ymmärtävät, että:

- **kielimalli** ei automaattisesti tiedä, onko sen vastaus oikein,
- **hallusinaatiot** voivat olla turvallisuusriski, koska virheelliset vastaukset voivat kuulostaa uskottavilta,
- ammattilaisen pitää tarkistaa tekoälyn tuottama tieto eikä luottaa siihen sokeasti,
- tekoälyn käyttö vaatii kriittistä ajattelua ja lähteiden arviointia.

---

## Tehtävä 3.3: Lämpötilan ymmärtäminen — pareittain käytävä keskustelu

### Tavoite

Tehtävän tavoitteena on ymmärtää, mitä **lämpötila** tarkoittaa kielimallin asetuksena ja miten se vaikuttaa vastausten luovuuteen, vaihteluun ja johdonmukaisuuteen.

**Opettajan painotus:** Lämpötila ei tee vastauksesta automaattisesti parempaa tai huonompaa. Sopiva lämpötila riippuu tehtävästä: faktatehtävissä halutaan usein vakautta, luovissa tehtävissä voidaan hyötyä vaihtelusta.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**

Valitse kaksi erilaista tehtävää:

1. **Tarkkuutta vaativa tehtävä:** `Kuka voitti jalkapallon maailmanmestaruuden vuonna 1998?`
2. **Luova tehtävä:** `Kirjoita runo syksystä.`

### Toteutus noin 15 minuuttia

1. **Peruskäsite noin 3 minuuttia:**


   Selitä opiskelijoille:

   > Lämpötila säätelee sitä, kuinka paljon vaihtelua ja satunnaisuutta kielimallin vastauksissa on. Matala lämpötila tekee vastauksista yleensä johdonmukaisempia ja ennustettavampia. Korkea lämpötila lisää vaihtelua ja luovuutta, mutta voi myös lisätä virheiden tai outojen ilmausten riskiä.

   Kirjoita taululle:

   Lämpötila 0.1 = hyvin vähän vaihtelua, usein sama tai lähes sama vastaus.

   Lämpötila 0.5 = jonkin verran vaihtelua.

   Lämpötila 1.0 tai enemmän = paljon vaihtelua ja enemmän luovuutta, mutta myös enemmän riskejä.
2. **Tehtävä 1: Tarkkuus noin 5 minuuttia:**

   1. Kysy opiskelijoilta: **Kuka voitti jalkapallon maailmanmestaruuden vuonna 1998?**
   2. Kerro, että tällainen tehtävä vaatii mahdollisimman tarkan ja luotettavan vastauksen.
   3. Selitä: “Tässä tilanteessa matala lämpötila on yleensä parempi, koska emme halua luovia vaihtoehtoja vaan oikean vastauksen.”
   4. Kysy opiskelijoilta: **Mitä voisi tapahtua, jos lämpötila olisi korkea?**

   **Keskeinen havainto:** Korkea lämpötila voi lisätä vaihtelua, mutta faktakysymyksissä vaihtelu ei yleensä ole hyödyllistä.
3. **Tehtävä 2: Luovuus noin 5 minuuttia:**

   1. Kysy opiskelijoilta: **Millainen vastaus sopisi tehtävään “Kirjoita runo syksystä”?**
   2. Selitä: “Tässä tehtävässä korkeampi lämpötila voi olla hyödyllinen, koska tavoitteena on saada erilaisia, luovia ja yllättäviä vaihtoehtoja.”
   3. Keskustelkaa pareittain: **Milloin luovuus on hyödyllistä? Milloin se voi olla haitallista?**

   **Keskeinen havainto:** Luovissa tehtävissä vaihtelu voi olla hyödyllistä, mutta liian korkea lämpötila voi tehdä vastauksista sekavia tai epäluotettavia.
4. **Johtopäätös noin 2 minuuttia:**

   - Kriittisissä ja tarkkuutta vaativissa tehtävissä kannattaa käyttää matalaa lämpötilaa.
   - Luovissa tehtävissä korkeampi lämpötila voi auttaa tuottamaan vaihtelevampia vastauksia.
   - Yhtä oikeaa lämpötilaa ei ole, vaan sopiva asetus riippuu tehtävän tavoitteesta.

### Lämpötilan valinnan yhteenveto

| Tehtävän tyyppi | Sopiva lämpötila | Perustelu |
| --- | --- | --- |
| **Faktakysymys** | Matala | Tavoitteena on johdonmukainen ja tarkka vastaus, ei luova vaihtelu. |
| **Ohje tai prosessi** | Matala tai keskitaso | Vaiheiden pitää pysyä selkeinä, mutta sanamuodoissa voi olla hieman joustoa. |
| **Ideointi** | Keskitaso tai korkea | Vaihtelu voi auttaa löytämään uusia vaihtoehtoja. |
| **Luova kirjoittaminen** | Korkeampi | Tavoitteena voi olla omaperäisyys, tyyli ja yllättävät ilmaisut. |

### Parikeskustelu

Pyydä opiskelijoita keskustelemaan pareittain seuraavista kysymyksistä:

- Missä tehtävissä haluaisit tekoälyltä mahdollisimman saman vastauksen joka kerta?
- Missä tehtävissä erilaiset vastaukset voisivat olla hyödyllisiä?
- Miksi korkea luovuus voi olla ongelma esimerkiksi asiakasviestinnässä, tietoturvassa tai lääketieteessä?
- Miten valitsisit lämpötilan omaan tekoälytehtävääsi?

**Vinkki arviointiin:** Hyvä opiskelijavastaus ei vain sano “matala” tai “korkea” lämpötila, vaan perustelee valinnan tehtävän tavoitteen kautta: tarvitaanko tarkkuutta, luovuutta, vaihtelua vai turvallisuutta?

### Odotettu oppimistulos

Tehtävän jälkeen opiskelijat ymmärtävät, että:

- **lämpötila** vaikuttaa kielimallin vastausten luovuuteen, vaihteluun ja johdonmukaisuuteen,
- matala lämpötila sopii paremmin tarkkuutta vaativiin tehtäviin,
- korkeampi lämpötila voi sopia luoviin tehtäviin,
- sopiva lämpötila valitaan tehtävän tavoitteen mukaan.

---

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- selittää, mitä **seuraavan tekstiosan ennustaminen** tarkoittaa,
- kuvata, miten kielimalli rakentaa vastauksen vaiheittain,
- tunnistaa **hallusinaatioiden** riskin ja selittää, miksi ne voivat olla vaarallisia,
- kuvata, miten tekoälyn tuottama tieto tarkistetaan luotettavista lähteistä,
- selittää, mitä **lämpötila** tarkoittaa kielimallin asetuksena,
- perustella, millainen lämpötila sopii tarkkuutta vaativaan tai luovaan tehtävään.

---
