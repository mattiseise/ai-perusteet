# Opettajan materiaalit – Lesson 26: n8n-projektipaja, osa 1

## Osaamistavoitteet (Bloom)

**Muistaa / Ymmärtää:**
- Opiskelija ymmärtää, mitä n8n on ja miten se eroaa perinteisestä ohjelmoimisesta.
- Opiskelija tunnistaa n8n:n solmun, triggerin, webhookin ja yhteyden (viiva solmujen välissä).
- Opiskelija näkee, miten n8n:n solmut vastaa agentin kuuteen komponenttiin (syötekäsittelijä, päättelijä, työkalut, muisti, turvakerros, palaute).

**Soveltaa:**
- Opiskelija pystyy rakentamaan yksinkertaisen n8n-työnkulun (trigger + 2-3 solmu).
- Opiskelija pystyy suunnittelemaan omaa n8n-agenttia ja tekemään siitä yksityiskohtaisen suunnitelman.

---

## Pedagoginen lähestymistapa

### Avaus — "Koodaamisen demokratisointi"

Aloita sanomalla:

"Tähän mennessä olemme puhuneet agentin arkkitehtuurista teoriassa. Nyt rakennamme sen käytännössä. Tämä ei vaadi ohjelmointitietoa — n8n on tarkoitettu kelle tahansa. Näette, miten agentin kuusi komponenttia muuttuvat konkreettisiksi solmuiksi kankaalla."

Tämä motivoi opiskelijoita, joille ohjelmointi saattaa tuntua pelottavalta.

### Keskeinen käsite: visuaalinen ohjelmointi

**Vertaus:**

Perinteinen ohjelmointi on kuin kirjoittaa resepti tekstillä. n8n on kuin rakentaa reseptiä fyysisesti: laitat aineet (solmut) kankaalle, yhdistät ne viivoilla, ja data virtaa niiden läpi.

```
Perinteinen:  if (user.message) { ai.think(user.message); return response; }
n8n:          [Webhook] → [IF] → [OpenAI] → [Discord]
```

Näytä molemmat ja selitä, että ne tekevät saman asian — eri tavalla.

### n8n:n solmujen kolme kategoriaa (opettaa 10 min aikana)

1. **Triggerit** — mistä työnkulku alkaa
   - Manual (käyttäjän painallus)
   - Schedule (ajastin)
   - Webhook (ulkoinen palvelu lähettää viestin)
   
2. **Päätössolmut** — logiikka ja ehto
   - IF-solmu (tarkistaa ehdon)
   - Switch-solmu (monet haarat)
   
3. **Toimintasolmut** — tekevät jotain
   - HTTP Request (kutsuu API:ta)
   - OpenAI (pyynnöstä tekoälyä)
   - Discord / Slack / Email (lähettää viestejä)
   - Google Sheets (lukee/kirjoittaa dataa)

### Virheellinen ajatus nro 1: "n8n on yksinkertaisesti"

**Todellisuus:** n8n on yksinkertainen käytön kannalta (drag-and-drop), mutta sen takana on syvälle meneviä käsitteitä (datanmuunnostus, turvakerrokset, muistin hallinta).

Painota: "Vaikka rajapinta on yksinkertainen, logiikka, jonka rakennamme, on älykkyyttä. Jokainen solmu tekee jotain merkityksellistä."

### Virheellinen ajatus nro 2: "Suunnitelma on turha — aloitetaan vaan rakentaa"

**Opettajan rooli:** Pakota opiskelijat tekemään suunnitelma ennen rakentamista.

"Hyvä insinööri piirtää suunnitelman ennen rakentamista. Huono insinööri rakentaa ja sitten yrittää korjata."

Opiskelijat, jotka ohittavat suunnittelun, päätyvät tekemään paljon turhatöitä ja rakentamaan agentin, joka ei toimi toiveittensa mukaisesti.

---

## Yleisiä väärinkäsityksiä

### 1. "Voiko n8n tehdä mitä tahansa?"

**Todellisuus:** n8n on integraatioalusta. Se voi tehdä vain sitä, mitä sen integraatiot (solmut) tukevat. Jos haluat mukauttaa logiikkaa syvemmin, tarvitset koodisolmua (Code node), joka vaatii ohjelmointitietoa.

**Opetuskäytäntö:** Listaa luokalle, mitä n8n voi ja ei voi tehdä:
- Voi: HTTP-kutsut, tekoäly-palvelut, tietokannat, viestit, sähköpostit
- Ei voi: erikoistuneita tai hyvin uusia palveluita ilman custom-integraatiota

### 2. "Turvakerros on vain vaihtoehtinen"

**Todellisuus:** Turvakerros on pakollinen jokaisen agentin rakentamisessa. Ilman sitä agentti voi tehdä vahinkoa.

**Opetuskäytäntö:** Näytä esimerkki: "Jos agentti voi lähettää sähköpostia ilman tarkistusta, se voi vahingossa lähettää arkaluonteisia tietoja väärään osoitteeseen. Turvakerros estää sen."

### 3. "n8n on helppo koska se on visuaalinen"

**Todellisuus:** Visuaalinen rajapinta tekee oppimisen nopeuemmaksi, mutta monimutkaiset logiikat vaativat silti syvää ajattelua.

Opiskelijat, jotka ajattelevat, että drag-and-drop = helppoa, menettävät motivaationsa kun kohtaavat vaikeuksia.

**Opetuskäytäntö:** Kertaa: "Visuaalinen interface vain näyttää logiikan selkeämmin. Ajattelu on silti vaativaa."

---

## Luokkatehtävän ohjeistus

### TT-A: Kokeile ja dokumentoi

**Tavoite:** Opiskelija osaa rakentaa yksinkertaisen työnkulun ja ymmärtää, miten data virtaa solmujen läpi.

**Yleisiä ongelmia:**
- Opiskelija ei yhdistä solmuja oikein viivalla
  - Ratkaisu: näytä, miten vedät viivan solmun outputista seuraavan solmun inputiin
- Opiskelija painaa "Execute" väärässä solmussa
  - Ratkaisu: selitä, että "Execute" testaa kyseisen solmun kunnes siihen asti
- Opiskelija ei näe, miten data muuttuuu
  - Ratkaisu: avaa solmun "Output" -väilehti ja näytä, mitä dataa solmu palauttaa

**Aikaarvio:** 15-20 min

### TT-B: Arkkitehti — suunnittele

**Tavoite:** Opiskelija tekee realistisen projektinsuunnitelman, joka voidaan toteuttaa n8n:ssä.

**Yleisiä ongelmia:**
- Suunnitelma on liian monimutkainen ensimmäiselle projektille
  - Ratkaisu: suosittele "Taso 1" lähtökohdaksi
- Riippuvuudet eivät ole selkeät (esim. "ensin pitää tehdä X, sitten Y", mutta X riippuu Y:n tuloksesta)
  - Ratkaisu: pyydä kirjoittamaan vaiheet numeroituna järjestyksessä ja testaamaan loogisen järjestyksen
- Hyväksyntäportit puuttuvat kokonaan
  - Ratkaisu: kysy: "Missä kohtaa ihmisen pitää hyväksyä, ennen kuin agentti toimii?"

**Aikaarvio:** 20-25 min

### TT-C: Punainen tiimi

**Tavoite:** Opiskelija oppii arvioimaan kriittisesti ja löytämään ongelmia ennen rakentamista.

**Opettajan rooli:** Varmista, että tiimityö on rakentavaa, ei loukkaavaa.

"Punainen tiimi etsii ongelmia, ei kritisoi ihmisiä. Palautetta tulee antaa ammatillisesti."

**Yleisiä ongelmia:**
- Palaute on liian ankara
  - Ratkaisu: muistuta, että tavoite on kehittää projektia, ei kritisoida tekijää
- Palautelomake on liian lyhyt
  - Ratkaisu: pyydä konkreettisia esimerkkejä: "Mitä voisi mennä pieleen tässä vaiheessa?"

**Aikaarvio:** 15-20 min

### TT-D: Keskustele ja perustele

**Tavoite:** Opiskelija linkittää n8n-solmut agentin kuuteen komponenttiin ja ymmärtää, miten ne työskentelevät yhdessä.

**Yleisiä ongelmia:**
- Opiskelija ei näe linkkiä solmun ja komponentin välillä
  - Ratkaisu: anna konkreettinen esimerkki: "OpenAI-solmu on päättelijä, koska tässä agentti 'ajattelee' ja tekee päätöksen."
- Analyysi on liian pinnallinen
  - Ratkaisu: pyydä selittämään JA MIKSI: "Miksi juuri tämä solmu on syötekäsittelijä? Mitä se tekee?"

**Aikaarvio:** 15-20 min

---

## Tuntiesityksen rakenne (45 minuuttia)

1. **Avaus ja motivaatio** (3 min)
   - "Olemme opinneet agentin teoriaa. Nyt rakennamme sen visuaalisesti n8n:ssä."

2. **n8n-tutoriaali (opettaja näyttää)** (12 min)
   - Avaa n8n, näytä trigger, HTTP Request, IF-solmu, lähetyssolmu
   - Korostaa: "Kukin solmu tekee yhden asian. Data virtaa niiden läpi."

3. **Arkkitehtuurin selitys** (10 min)
   - Näytä, miten solmut vastaavat agentin kuuteen komponenttiin
   - Piirrä taululle: Trigger → Validointi → Päättely → Turva → Toiminta → Palaute

4. **Opiskelijat tekevät tehtäviä itsenäisesti ja pareissa** (15 min)
   - TT-A: Rakentaa yksinkertaisen työnkulun
   - TT-B & TT-D: Suunnittelevat oman projektinsa
   - TT-C: Arvioi toisen projektia (jos aikaa)

5. **Yhteenveto ja seuraavan tunnin esittely** (5 min)
   - "Seuraavassa tunnissa rakennamme ne projektit, jotka suunnittelitte tänään."

---

## Jatkoyhteys Lesson 27:een

Lesson 27 on rakentamisen, testaamisen ja dokumentoinnin tunti. Varmista, että opiskelijat lähettävät suunnitelmansa sinulle ennen 27. lektsiota, jotta:
1. Voit arvioida, onko suunnitelma realistinen
2. Voit antaa palautetta parannuksista
3. Opiskelijat voivat aloittaa rakentamisen 27. tunnilla ilman hidasteita

---

## Materiaalit, jotka opettajalla pitää olla valmiina

- n8n-instanssi (paikallinen tai cloud)
- Esittelyprojekti n8n:ssä (esim. yksinkertainen FAQ-botti)
- Projektin mallit (Taso 1, 2, 3) valmiiksi tekstissä tai näytöllä
- Taulukko: n8n solmut vs. agentin kuusi komponenttia
- Punaisen tiimin palautelomake (printattava tai jaettava digitaalisesti)

---

## Opettajan vihjeet

1. **Liian nopea etenemia:** Jos opiskelijat ovat valmiina nopeasti, anna heille haastavamman tehtävän:
   - "Rakenna n8n-työnkulku, joka integroituu KAHTEEN ulkoiseen palveluun"
   - "Lisää turvakerros, joka estää tietynlaisia syötteitä"

2. **Liian hidas etenema:** Jos aika on tiukalla, voit:
   - Antaa valmiit suunnitelmat (TT-B voidaan antaa mallin muodossa)
   - Ohittaa TT-C (punainen tiimi) ja tehdä sen Lesson 27:ssä

3. **Tekniset ongelmat:** Jos n8n ei toimi (API-virhe, yhteysongelma):
   - Käytä valmiita kuvakaappauksia n8n:n työnkulusta
   - Näytä opiskelijalle, miten ongelmat ratkotaan pyynnöllä: "Kokeilimme tätä ja se ei toiminut. Seuraavaksi..."

