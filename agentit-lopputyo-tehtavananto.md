# Agentit-osion lopputyö — n8n-agentin rakentaminen

> Tämä on Agentit-osion (tunnit 19–27) lopputyö. Tutustu tähän tehtävänantoon osion alussa. Palaat siihen joka tunti, kun kerää **⭐️ Agentti -pohjapiirroksiasi** ja rakennat lopulta valmista agenttia.

## Mitä rakennat?

Rakennat **n8n-pohjaisen agentin**, joka ratkaisee yhden konkreettisen ongelman. Agenttisi koostuu **3–5 solmusta**, jotka yhdessä muodostavat toimivan, ohjatun ja turvallisen työnkulun.

**Esimerkkejä mahdollisista agentteista:**

- Päivittäinen sähköpostien luokittelija ja yhteenvetäjä
- Asiakaspalvelun FAQ-botti, joka hakee vastauksia tietokannasta
- Sosiaalisen median seurantarobotti
- Palvelinlokien analysaattori, joka ilmoittaa virheistä
- Asiakkaiden tikettien luokittelija ja jakaja

Agentin ei tarvitse olla monimutkainen. Tärkeintä on, että se on **autonominen** — tekee päätöksiä tilanteen mukaan, käyttää useita työkaluja ja toimii itsenäisesti.

## Polku alusta loppuun

Lopputyö rakentuu yhdeksän tunnin aikana. Joka tunti tuottaa konkreettisen palan, joka päätyy lopulliseen agenttiisi.

| Tunti | Mitä teet | Mitä syntyy |
|---|---|---|
| **19** | Valitset ongelman ja perustelet, miksi agentti sopii | ⭐️ Agentti: Ongelma (1/5) |
| **20** | Tarkistat, että ratkaisu vaatii todella agentin | Päätösharjoittelu |
| **21** | Suunnittelet muistirakenteen ja identiteetin | ⭐️ Agentti: Muisti (2/5) |
| **22** | Valitset työkalut (n8n-solmut) | Työkalulista |
| **23** | Valitset päättelymallin (ReAct vai ketjuajattelu) | ⭐️ Agentti: Päättely (3/5) |
| **24** | Suunnittelet turvakerroksen | ⭐️ Agentti: Turva (4/5) |
| **25** | Suunnittelet ihmisen roolin (hyväksyntäportit) | ⭐️ Agentti: Ihminen (5/5) |
| **26** | Kasaa pohjapiirrokset, tutustut n8n:ään, rakennat minimiversion | Toimiva minimiagentti |
| **27** | Viimeistelet, testaat, dokumentoit, esittelet | Valmis lopputyö |

## Viisi ⭐️ Agentti -pohjapiirrosta

Pohjapiirrokset ovat suunnitelmadokumentteja, joita kerätä omaan muistiinpanodokumenttiisi. Yhdessä ne muodostavat **kattavan suunnitelman**, jonka pohjalta rakennat n8n-työnkulun.

**1. ⭐️ Agentti: Ongelma (tunti 19)**
Mikä ongelma on kyseessä, kenelle se on, miksi juuri agentti sopii ratkaisuksi. 150–200 sanaa.

**2. ⭐️ Agentti: Muisti (tunti 21)**
Lyhytaikainen muisti (konteksti-ikkuna), pitkäaikainen muisti, tilat ja tilasiirtymät, agentin identiteetti (soul). 150–200 sanaa.

**3. ⭐️ Agentti: Päättely (tunti 23)**
ReAct vai ketjuajattelu — kumpi sopii agenttisi ongelmaan ja miksi. Miten päättelymalli näkyy n8n-rakenteessa. 150–200 sanaa.

**4. ⭐️ Agentti: Turva (tunti 24)**
Minimioikeusperiaate, suurimmat riskit, turvakerroksen neljä tasoa (validointi, rajoitus, seuranta, palautuminen), lokitus. 150–200 sanaa.

**5. ⭐️ Agentti: Ihminen (tunti 25)**
Missä kohdissa ihmisen täytyy hyväksyä, millainen hyväksyntäportti on, mitä tapahtuu jos ihminen ei vastaa. 150–200 sanaa.

## Lopputuotoksen vaatimukset

Palauta Itslearningiin yhtenä pakettina:

1. **Linkki n8n-työnkulkuusi** tai vientitiedosto (JSON)
2. **Koottu suunnitelma** — viisi ⭐️ Agentti -pohjapiirrosta yhdessä tiedostossa, tarkistettuna johdonmukaiseksi kokonaisuudeksi
3. **Kolme lyhyttä dokumenttia** (½–1 sivu kukin):
   - **README** — mitä agentti tekee, kenelle, miten käytetään, esimerkit ja rajoitukset
   - **ARCHITECTURE** — jokainen n8n-solmu järjestyksessä, mitä se tekee, miten ne linkittyvät agentin kuuteen komponenttiin
   - **SAFETY** — pahimmat riskit, miten ne torjuttiin, lokitus, human-in-the-loop -kohdat
4. **Testiraportti** — 15 testitapausta (5 normaalia, 5 reunatapausta, 5 turvallisuustestiä)
5. **Demo luokassa** (3–5 min) tai nauhoitettuna videona
6. **Itsearviointi** (300–400 sanaa) — onnistumiset, epäonnistumiset, opitut asiat, parannusideat
7. **Vertaisarviomuistio** — toiselta opiskelijalta saatu palaute (tai AI-pohjainen kriittinen arvio jos teet työn yksin)

## Työkalut ja työskentelytapa

**Alusta:** n8n (koulun instanssi, tunnukset opettajalta).

**Tekoälyapu:** Voit käyttää vapaasti ChatGPT:tä, Claudea tai Copilotia sparrauskumppanina ja suunnittelun tarkistamiseen. Älä anna tekoälyn päättää puolestasi — käytä sitä kyseenalaistamiseen ja näkökulmien laajentamiseen.

**Työskentelytapa:** Voit tehdä lopputyön **yksin tai parin kanssa**. Jos teet parin kanssa, jakakaa työ niin, että molemmat ymmärtävät koko agentin. Vertaisarvio tehdään aina toisen tiimin tai parin kanssa.

## Arviointi

Lopputyö arvioidaan viidellä osa-alueella (yhteensä 100 pistettä):

| Osa-alue | Pisteet |
|---|---|
| Toimiva n8n-työnkulku | 25 |
| Turvallisuus (turvakerros, lokitus, riskien tunnistaminen) | 20 |
| Dokumentaatio (README, ARCHITECTURE, SAFETY) | 20 |
| Testaus (testiraportin kattavuus ja syvyys) | 20 |
| Itsearviointi ja demo | 15 |

**Hyvä lopputyö** ei ole täydellinen — se on **rehellinen ja perusteltu**. Pieni agentti, joka toimii ja jonka rajat tunnistat, on parempi kuin iso agentti, jota et ymmärrä.

## Aikabudjetti — näin paljon työtä kannattaa varata

Tämä aikabudjetti näkyy vain tässä tehtävänannossa, ei yksittäisten tuntien tehtävissä. Tämä on tietoinen pedagoginen valinta — sinun ei tarvitse stressata yksittäisten tehtävien kestosta, vaan kokonaisuudesta.

| Vaihe | Aika (yksin) | Aika (parin kanssa) |
|---|---|---|
| Pohjapiirrokset 1–5 (tunnit 19, 21, 23, 24, 25) | ~30 min / tunti | ~30 min / tunti |
| Välitunnit (20, 22) — sparrausharjoittelua | ~20 min / tunti | ~20 min / tunti |
| Tunti 26 — kasaus, n8n-tutustuminen, minimiversio | 60–90 min | 45–60 min |
| Tunti 27 — viimeistely, testaus, dokumentointi, demo | 90–120 min | 60–90 min |
| **Yhteensä** | **~5–7 h** | **~4–5 h** |

Jos jossain vaiheessa tuntuu, että et ehdi — **leikkaa scope**. Yksinkertaisempi mutta toimiva agentti on parempi kuin monimutkainen mutta keskeneräinen.

## Hyvä alku

1. Lue tämä tehtävänanto kokonaan.
2. Selaa tuntien 19–27 otsikot ja saa kokonaiskuva polusta.
3. Aloita rauhassa: tunnilla 19 tärkein päätös on **valita oikea ongelma**. Älä jää jumiin perfektionismiin — voit tarkentaa ongelmaa myöhemmin.
4. Pidä **muistiinpanodokumenttia** mukana joka tunti. Sinne kerätä pohjapiirroksesi.

---

**Tämä lopputyö ei testaa, osaatko käyttää tekoälyä. Se testaa, osaatko *rakentaa* sillä jotain mitä joku muu voi käyttää.**
