# Opiskelutehtävät: Automaatio vai autonomia

> Tämä tunti tarkistaa lopputyösi suuntaa. Tunnilla 19 valitsit **⭐️ Agentti: Ongelma**. Tänään harjoittelet päätöksentekoa "tarvitaanko tähän agentti vai riittäisikö yksinkertaisempi ratkaisu" — ja sovellat samaa kysymystä omaan valintaasi.

*Kaikkia ei tarvitse tehdä. Valitse tehtävistä 1. Suosittelen kuitenkin "Päätös: agentti vai ei?" -tehtävää — se sparraa suoraan oman lopputyösi valintoja.*

---

## Tehtävä 20.1 — Päätös: agentti vai ei? 🟢 SUOSITELTU

**Miksi tämä on tärkeää:** Agentti on tehokas mutta kallis ratkaisu. Jos ongelma ratkeaa yksinkertaisemmin — skriptillä, työnkululla tai chatbotilla — agentin rakentaminen on tuhlausta.

### Tehtävä

Alla on viisi ongelmakuvausta. Päätä kustakin, mikä on oikea ratkaisutyyppi:

- **Skripti** — toistaa saman toiminnan samalla tavalla, ei päättele tilanteesta
- **Työnkulku** — etenee ennalta määriteltyä polkua, voi haarautua mutta ei tee itsenäisiä päätöksiä
- **Chatbot** — vastaa käyttäjän kysymyksiin, reaktiivinen
- **Agentti** — toimii itsenäisesti, tekee päätöksiä tilanteen mukaan, käyttää useita työkaluja

**Ongelma A: Päivittäinen myyntiraportti.** Joka aamu kello 8 raportti pitää koota: edellisen päivän myyntiluvut Excelistä, muunnos PDF:ksi, lähetys johtoryhmälle sähköpostilla. Tiedot tulevat aina samasta tiedostosta, samassa muodossa.

**Ongelma B: Asiakaspalvelutiketit.** Asiakkaat lähettävät päivittäin 50–100 viestiä, joissa on hyvin erilaisia ongelmia: laskutuskysymyksiä, teknisiä vikailmoituksia, palautusta koskevia pyyntöjä ja yleisiä palautteita. Jokainen viesti pitää luokitella, vastata yksinkertaisiin automaattisesti ja siirtää monimutkaiset oikealle tukihenkilölle. Jos vastaus on kriittinen (esim. korvaus yli 200 €), ihmisen pitää tarkistaa se ennen lähetystä.

**Ongelma C: Kysymys-vastaus -palvelu opiskelijoille.** Kurssin opiskelijat kysyvät usein samoja kysymyksiä Teamsissa: "Milloin tehtävä pitää palauttaa?", "Mistä löydän materiaalit?", "Onko huomenna tunti?". Tarvitaan järjestelmä, joka osaa vastata näihin kysymyksiin tunnin info-kanavan perusteella.

**Ongelma D: Sosiaalisen median seuranta.** Yritys haluaa seurata, mitä siitä puhutaan netissä. Järjestelmän pitää tarkkailla useita lähteitä (Twitter/X, Reddit, blogit), tunnistaa yritystä koskevat keskustelut, päättää onko viesti positiivinen, neutraali vai kriittinen, ja jos viesti on kriittinen ja saa paljon huomiota, lähettää ilmoitus viestintätiimille — mutta vain virka-aikana. Vapaa-aikana huomiot kerätään aamuraporttiin.

**Ongelma E: Varaston täydennys.** Kun varastosaldo putoaa alle 20 kappaleen, tilaajalle pitää lähettää automaattisesti tilaus. Tilaaja, tuotekoodi ja määrä ovat aina samat.

### Vastausohje

Jokaisesta ongelmasta:

1. Valitse ratkaisutyyppi (skripti / työnkulku / chatbot / agentti)
2. Perustele 1–2 lauseella. Käytä argumentteina vähintään yhtä näistä: *onko päätöksiä tehtävä, vaihteleeko tilanne, tarvitaanko useita työkaluja, onko ihmisen valvonta tarpeen, kannattaako monimutkaisempi ratkaisu*.

### Sovellus omaan ⭐️ Agentti: Ongelma -valintaasi

Avaa muistiinpanoistasi ⭐️ Agentti: Ongelma (tunnilta 19). Käy sama analyysi sille. Jos vastaukset osoittavat, että agentti on oikea valinta — hyvä, lopputyösi suunta on oikea. Jos huomaat, että yksinkertaisempi ratkaisu riittäisi, tarkenna ongelmaasi sellaiseksi, jossa agentin autonomisuus tuottaa aidosti lisäarvoa.

### Tekoälyvaihe — sparraa päätöstäsi

```
Olen luokitellut viisi ongelmaa seuraavasti: [liitä vastauksesi].
Lue ne ja kysy 2–3 haastavaa kysymystä, joiden avulla testaan onko
luokitteluni perusteltua. Älä korjaa puolestani — kysy niin että
ajattelen itse.
```

---

## Tehtävä 20.2 — Suunnittele kontrolli agentin rajoittamiseksi 🟣 SYVENTÄVÄ

**Miksi tämä on hyödyllinen:** Tämä tehtävä harjoittelee trade-off -ajattelua, joka on suoraan hyödyllistä tunnin 24 ⭐️ Agentti: Turva -pohjapiirroksessa.

### Tilanne

Sinulla on agentti, joka hoitaa asiakastukitikettejä. Agentti voi:

- Lukea asiakastukitietokantaa
- Etsiä ratkaisuja knowledge base -tietokannasta
- Lähettää sähköposteja asiakkaille
- Merkitä tikettejä "ratkaistuiksi" ja sulkea niitä

Tavoite kuulostaa hyvältä — automatisoida tuki. Mutta mitä pahaa voisi tapahtua?

### Tehtävä

Kirjoita agenttijärjestelmälle **kontrollisuunnitelma**, jossa on 3–4 riski–kontrolli–hinta -paria.

| Riski | Kontrolli | Hinta / trade-off |
|---|---|---|
| Agentti lähettää väärän ratkaisun asiakkaalle | Agentti voi lähettää vain valmiiksi hyväksyttyjä mallivastauksia, ei vapaata tekstiä | Vähemmän joustavuutta, mutta parempi turvallisuus |
| Agentti sulkee tiketin liian aikaisin | Tiketti merkitään "ehdotettu ratkaisu" -tilaan, ja ihminen hyväksyy sulkemisen | Lisää ihmisen työtä, mutta estää tärkeiden tikettien sulkemisen |

Mahdollisia kontrollityyppejä:

- Rajaa agentin työkalut
- Lisää ihminen silmukkaan
- Lisää valvontaa
- Rajaa määrää tai aikaa

> 💡 **Vinkki muistiinpanoihin:** Jos riskien ja kontrollien miettiminen tuottaa havaintoja, joita voit hyödyntää oman agenttisi suunnittelussa, kirjaa ne ylös. Tunnilla 24 teet ⭐️ Agentti: Turva -pohjapiirroksen.

---

**Lopputyön suunta tarkistettu — seuraavaksi muisti ja identiteetti**
