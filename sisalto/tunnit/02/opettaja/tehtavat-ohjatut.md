# Opettajavetoiset tehtävät

## Tehtävien valinta 90 minuutin tunnille

Seuraavat tehtävät ovat vaihtoehtoja, eivät yksi peräkkäinen kokonaisuus. Tuntisuunnitelman perusreitillä käytetään ohjattua tehtävää A aineistojaon ja driftien käsittelyyn, minkä jälkeen opiskelija tekee opiskelijatehtävän 2.1 mukaisen elinkaarikuvauksen omana ydintuotoksenaan. AGI ja ASI käsitellään tunnin lopussa tiiviinä rajauksena. Jos käytät ohjattua tehtävää C tai D kokonaisena, korvaa sillä osa ydintuotoksen ohjausajasta tai siirrä se toiselle tapaamiskerralle.

- **Perusreitti:** ohjattu tehtävä A, opiskelijan elinkaarikuvaus ja 10–12 minuutin AGI–ASI-rajaus.
- **Soveltava reitti:** sama ydintuotos, mutta yksi elinkaaren vaihe puretaan ohjatun tehtävän D näyttökysymyksillä.
- **Itsenäinen reitti:** viisi Harjoittele-tehtävää ja tehtävän 2.1 elinkaarikuvaus; opettajavetoisia tehtäviä ei tarvita.

## Ohjattu tehtävä A: Kolme aineistoa ja yksi muuttuva maailma

### Tavoite

Opiskelija erottaa koulutus-, validointi- ja testiaineiston sekä ymmärtää, miksi käyttöönotettu malli tarvitsee seurantaa.

### Toteutus, noin 15 minuuttia

Anna ryhmille 30 kuvitteellista petostapausta paperilappuina. Pyydä ryhmää jakamaan ne kolmeen pinoon ja nimeämään kunkin pinon tehtävä. Kysy sitten, mitä tapahtuu, jos testipino avataan aina, kun mallia halutaan parantaa. Oikea havainto on, että testi alkaa ohjata rakentamista eikä enää toimi riippumattomana tarkistuksena.

Anna lopuksi uusi tilanne: maksaminen siirtyy nopeasti uudelle laitteelle ja petollinen toiminta muuttaa muotoaan. Ryhmä nimeää, kumpi esimerkki kuvaa datadriftiä ja kumpi mallidriftiä, sekä kertoo, mitä seurannassa pitäisi havaita ennen päivityspäätöstä.

### Purku

Korosta, ettei driftin havaitseminen automaattisesti tarkoita mallin uudelleenkoulutusta. Ensin selvitetään muutoksen syy, tarkistetaan aineiston laatu ja päätetään, millä erillisellä testillä korjaus osoitetaan.

---

## Ohjattu tehtävä B: Viisi käsitettä — korttilajittelu

### Tavoite

Opiskelija erottaa tunnin viisi käsitettä ja tunnistaa, mitkä niistä kuvaavat nykyisiä järjestelmiä ja mitkä tulevaisuuspuhetta.

### Valmistelu

Tee viisi otsikkokorttia:

- sääntöpohjainen järjestelmä
- kapea tekoäly
- generatiivinen tekoäly
- AGI
- ASI

Tee lisäksi seuraavat esimerkkikortit:

1. Lasku siirtyy tarkistukseen, jos summa ylittää ennalta päätetyn rajan.
2. Malli tunnistaa kuvasta, onko tuote vahingoittunut.
3. Järjestelmä kirjoittaa tuotekuvauksen promptin perusteella.
4. Suositusmalli arvioi, mikä kappale kiinnostaisi käyttäjää.
5. Kuvageneraattori tekee tapahtumajulisteen tekstikuvauksesta.
6. Väite järjestelmästä, joka oppisi joustavasti minkä tahansa ammatin.
7. Oletus tekoälystä, joka ylittäisi ihmisen kyvyt kaikilla tieteenaloilla.
8. Käyttäjätunnus lukitaan viiden virheellisen salasanan jälkeen.

### Toteutus, noin 25 minuuttia

1. Jaa opiskelijat 2–4 hengen ryhmiin.
2. Anna ryhmälle otsikko- ja esimerkkikortit.
3. Pyydä ryhmää sijoittamaan jokainen esimerkki tarkimman käsitteen alle.
4. Pyydä ryhmää merkitsemään jokainen otsikko joko **nykyiseksi järjestelmäksi** tai **tulevaisuuskäsitteeksi**.
5. Pura ratkaisut yhdessä. Kysy jokaisesta kortista: ”Mitä järjestelmä tekee tai mitä väitteessä oletetaan?”

### Malliratkaisu

| Esimerkki | Tarkin käsite | Perustelu |
|---|---|---|
| Laskun raja | Sääntöpohjainen järjestelmä | Toiminta perustuu ihmisen kirjoittamaan ehtoon |
| Vaurion tunnistus | Kapea tekoäly | Malli tekee rajattua tunnistustehtävää |
| Tuotekuvauksen kirjoittaminen | Generatiivinen tekoäly | Järjestelmä tuottaa uutta tekstiä |
| Kappalesuositus | Kapea tekoäly | Järjestelmä tekee rajattua ennustetta |
| Julisteen tekeminen | Generatiivinen tekoäly | Järjestelmä tuottaa uuden kuvan |
| Minkä tahansa ammatin oppiminen | AGI-väite | Väite koskee laaja-alaista ja joustavaa oppimista |
| Ihmisen laaja ylittäminen | ASI-väite | Väite koskee ihmistä laajasti kyvykkäämpää tekoälyä |
| Tunnuksen lukitus | Sääntöpohjainen järjestelmä | Toiminta seuraa ennalta päätettyä rajaa |

### Tärkeä purku

Generatiivisissa esimerkeissä osoitettu tehtävä on rajattu tekstin tai kuvan tuottamiseen. Tässä lajittelussa ne sijoitetaan generatiivisen tekoälyn alle, koska se on näkyvän toiminnan tarkin kuvaus. Merkitse samalla, että esimerkin käyttötarkoitus on rajattu. Älä päättele generatiivisuuden perusteella, että järjestelmän kyvyt olisivat yleisesti laajat.

### Odotettu oppimistulos

Opiskelija ymmärtää, että käsitteet eivät ole saman asteikon peräkkäisiä tasoja. Hän erottaa generatiivisuuden kykyjen rajauksesta ja tunnistaa, että sama järjestelmä voi olla molempia. Lisäksi hän erottaa AGI- ja ASI-väitteet nykyisistä järjestelmistä.

---

## Ohjattu tehtävä C: Sama suoritus, liian suuri johtopäätös

### Tavoite

Opiskelija erottaa järjestelmän osoitetun suorituksen sitä laajemmasta tulkinnasta.

### Valmistelu

Kirjoita näkyviin seuraava tilanne:

> Tekstitekoäly kirjoittaa selkeän hakemuksen, tiivistää pitkän tekstin ja vastaa jatkokysymyksiin. Käyttäjä päättelee: ”Se osaa jo lähes kaiken tietotyön, joten se on AGI.”

### Toteutus, noin 20 minuuttia

1. Pyydä opiskelijoita alleviivaamaan, mitä järjestelmä **osoitetusti teki**.
2. Pyydä ympyröimään, mitä käyttäjä **päättelee**.
3. Kootkaa taululle kaksi saraketta: **näyttö** ja **johtopäätös**.
4. Pyydä opiskelijoita kirjoittamaan väite uudelleen niin, että se vastaa näyttöä.

### Mallipurku

**Näyttö:** Järjestelmä tuotti ja muokkasi tekstiä sekä vastasi tekstimuotoisiin jatkokysymyksiin.

**Liian suuri johtopäätös:** Se osaa lähes kaiken tietotyön ja on AGI.

**Täsmällinen muotoilu:** Järjestelmä osoitti monipuolista tekstin tuottamisen ja käsittelyn kykyä. Tämä ei yksin osoita, että se oppisi itsenäisesti minkä tahansa työn tai toimisi joustavasti kaikissa uusissa tilanteissa.

### Jatkokysymykset

- Mitä muuta näyttöä AGI-väite vaatisi?
- Millainen tehtävä olisi aidosti erilainen kuin tekstin käsittely?
- Mitä järjestelmän luotettavuudesta, oppimisesta tai itsenäisestä toiminnasta ei vielä tiedetä?

### Odotettu oppimistulos

Opiskelija ei torju näkyvää suoritusta, mutta ei myöskään tee siitä näyttöä laajempaa päätelmää.

---

## Ohjattu tehtävä D: Tekoälyväitteen purkaminen

### Tavoite

Opiskelija käyttää tunnin käsitteitä uutisotsikon, mainoslauseen tai muun väitteen kriittiseen arviointiin.

### Valmistelu

Valitse yksi ajankohtainen tekoälyä koskeva otsikko tai käytä seuraavaa esimerkkiväitettä:

> ”Uusi tekoäly korvaa pian asiantuntijat — se suoriutui testissä ihmistä paremmin.”

### Toteutus, noin 25 minuuttia

Pyydä pareja vastaamaan viiteen kysymykseen:

1. Mitä väitteessä sanotaan tapahtuneen?
2. Mikä oli mahdollisesti rajattu testi tai tehtävä?
3. Mihin tunnin käsitteeseen osoitettu suoritus sopii?
4. Sisältääkö otsikko AGI- tai ASI-oletuksen?
5. Miten otsikko pitäisi kirjoittaa, jotta se vastaisi näyttöä?

### Purkumalli

Ohjaa opiskelijoita välttämään kahta ääripäätä:

- ”Tekoäly osaa kaiken, koska se voitti ihmisen testissä.”
- ”Tuloksella ei ole mitään merkitystä, koska järjestelmä ei ole AGI.”

Täsmällinen tulkinta tunnustaa rajatun suorituksen ja rajaa johtopäätöksen samaan tehtävään. Esimerkiksi:

> Järjestelmä suoriutui määritellyssä testissä vertailuryhmää paremmin. Tulos ei vielä osoita, että järjestelmä hallitsisi asiantuntijatyön muut tehtävät tai toimisi niissä luotettavasti.

### Odotettu oppimistulos

Opiskelija osaa kuvata, mitä järjestelmä teki, nimetä väitteen käsitteellisen tason ja sanoa, mitä lisätietoa tarvitaan.

---

## Arviointi

Arvioi opiskelijan kykyä:

- käyttää viittä käsitettä johdonmukaisesti,
- erottaa sääntöpohjainen toiminta rajatusta tekoälytehtävästä,
- erottaa generatiivisuuden kykyjen rajauksesta,
- erottaa AGI- ja ASI-väitteet nykyisistä järjestelmistä,
- rajata johtopäätös käytettävissä olevaan näyttöön.

## Tunnin lopun itsearviointi

Pyydä opiskelijaa valitsemaan jokaisesta väitteestä yksi vaihtoehto: **osaan**, **tarvitsen vielä yhden esimerkin** tai **tarvitsen ohjausta**.

- Osaan selittää viiden käsitteen erot.
- Osaan selittää, miten generatiivinen järjestelmä voi olla tehtävältään rajattu ja miksi generatiivisuus ei yksin osoita AGI:a.
- Osaan erottaa nykyisen järjestelmän AGI- tai ASI-väitteestä.
- Osaan sanoa, mitä tekoälyväitteestä ei vielä voida päätellä.
