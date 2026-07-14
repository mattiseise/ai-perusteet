# Agentit-osion lopputyö — n8n-agentin rakentaminen

> Tämä on Agentit-osion (tunnit 19–27) lopputyö. Tutustu tähän tehtävänantoon osion alussa. Palaat siihen joka tunti, kun kerää **⭐️ Agentti -pohjapiirroksiasi** ja rakennat lopulta valmista agenttia.

**Tärkein viesti heti alkuun:** rakennat **hyvin yksinkertaisen agentin** (3–5 solmua). Emme tavoittele mitään monimutkaista — pieni, toimiva agentti, jonka ymmärrät, on koko tehtävän tavoite.

<figure style="margin:24px 0;text-align:center">
<svg viewBox="0 0 880 470" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto" font-family="system-ui, -apple-system, 'Segoe UI', sans-serif" role="img">
  <title>Mitä rakennat: yksinkertainen agentti</title>
  <desc>Tavoite on pieni, toimiva agentti, jossa on 3–5 solmua: käynnistys, agentti yhdellä kielimallilla ja 1–2 työkalulla, sekä lopputulos. Ei monimutkaista järjestelmää.</desc>
  <defs>
    <g id="smp-bolt" fill="none" stroke="currentColor"><path d="M13 2 L5 13.5 H11 L10.5 22 L19 9.5 H12.5 Z" fill="currentColor"/></g>
    <g id="smp-robot" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="8" width="15" height="11.5" rx="3"/><path d="M12 8 V4.5"/><circle cx="12" cy="3.4" r="1.4" fill="currentColor" stroke="none"/><circle cx="9.3" cy="13.5" r="1.3" fill="currentColor" stroke="none"/><circle cx="14.7" cy="13.5" r="1.3" fill="currentColor" stroke="none"/><path d="M9.5 16.6 H14.5"/></g>
    <g id="smp-check" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M7.8 12.2 l2.8 2.8 l5.6-6.2"/></g>
    <g id="smp-x" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M8.7 8.7 L15.3 15.3 M15.3 8.7 L8.7 15.3"/></g>
    <g id="smp-bulb" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 18 H14.5 M10.5 21 H13.5"/><path d="M12 3 a6 6 0 0 1 4 10.3 c-0.8 0.8 -1 1.7 -1 2.7 H9 c0 -1 -0.2 -1.9 -1 -2.7 A6 6 0 0 1 12 3 Z"/></g>
  </defs>
  <rect x="0" y="0" width="880" height="470" rx="16" fill="#FAFBFE"/>
  <text x="440" y="38" text-anchor="middle" font-size="22" font-weight="700" fill="#1B2336">Mitä rakennat: yksinkertainen agentti</text>
  <text x="440" y="64" text-anchor="middle" font-size="13" fill="#5A6478">Tavoite on pieni, toimiva agentti — ei monimutkainen järjestelmä.</text>
  <rect x="28" y="88" width="224" height="80" rx="12" fill="#F0F9F4" stroke="#CDE9D9" stroke-width="1.5"/>
  <use href="#smp-bolt" x="44" y="104" width="20" height="20" style="color:#2F9E69"/>
  <text x="72" y="118" font-size="13.5" font-weight="700" fill="#247A52">Käynnistys</text>
  <text x="44" y="150" font-size="11.5" fill="#3A4253">esim. sähköposti saapuu</text>
  <line x1="252" y1="128" x2="276" y2="128" stroke="#9AA6BD" stroke-width="2.4"/><path d="M280 128 L270 122.5 L270 133.5 Z" fill="#9AA6BD"/>
  <rect x="300" y="88" width="280" height="80" rx="12" fill="#EEF1FE" stroke="#3B5BDB" stroke-width="2"/>
  <use href="#smp-robot" x="316" y="102" width="22" height="22" style="color:#3B5BDB"/>
  <text x="346" y="118" font-size="13.5" font-weight="700" fill="#2F46B0">Agentti</text>
  <text x="316" y="150" font-size="11.5" fill="#3A4253">1 kielimalli + 1–2 työkalua</text>
  <line x1="580" y1="128" x2="604" y2="128" stroke="#9AA6BD" stroke-width="2.4"/><path d="M608 128 L598 122.5 L598 133.5 Z" fill="#9AA6BD"/>
  <rect x="628" y="88" width="224" height="80" rx="12" fill="#E9F6F7" stroke="#BFE6E9" stroke-width="1.5"/>
  <use href="#smp-check" x="644" y="104" width="20" height="20" style="color:#0E9AA7"/>
  <text x="672" y="118" font-size="13.5" font-weight="700" fill="#0B7E89">Lopputulos</text>
  <text x="644" y="150" font-size="11.5" fill="#3A4253">esim. tallennettu vastaus</text>
  <text x="440" y="196" text-anchor="middle" font-size="12.5" font-weight="600" fill="#1B2336">Yhteensä 3–5 solmua.</text>
  <rect x="28" y="216" width="824" height="58" rx="11" fill="#F0F9F4" stroke="#BFE6CF" stroke-width="1.4"/>
  <use href="#smp-check" x="48" y="232" width="22" height="22" style="color:#2F9E69"/>
  <text x="82" y="242" font-size="12.5" font-weight="700" fill="#247A52">Tähän pyritään</text>
  <text x="82" y="262" font-size="12.5" fill="#3A4253">Yksinkertainen, toimiva agentti (3–5 solmua), jonka ymmärrät ja jonka rajat tunnistat.</text>
  <rect x="28" y="286" width="824" height="58" rx="11" fill="#FBEEEE" stroke="#F0C9C9" stroke-width="1.4"/>
  <use href="#smp-x" x="48" y="302" width="22" height="22" style="color:#C0453E"/>
  <text x="82" y="312" font-size="12.5" font-weight="700" fill="#B5403A">Tätä ei tavoitella</text>
  <text x="82" y="332" font-size="12.5" fill="#3A4253">Monimutkainen järjestelmä, kymmeniä solmuja tai moniagenttiverkko — ei tarvita tässä.</text>
  <rect x="28" y="362" width="824" height="82" rx="12" fill="#FFFBEC" stroke="#F2D98E" stroke-width="1.5"/>
  <use href="#smp-bulb" x="48" y="386" width="24" height="24" style="color:#C79100"/>
  <text x="86" y="394" font-size="13" font-weight="700" fill="#8A6A00">Muista</text>
  <text x="86" y="415" font-size="12.5" fill="#5A4A1E">Pieni agentti, joka toimii ja jonka rajat tunnistat, on parempi kuin iso agentti, jota et</text>
  <text x="86" y="433" font-size="12.5" fill="#5A4A1E">ymmärrä. Jos aika loppuu, leikkaa scope ja pidä agentti yksinkertaisena.</text>
</svg>
<figcaption style="font-size:13px;color:#5A6478;margin-top:10px">Tavoitteena on yksinkertainen, toimiva agentti (3–5 solmua) — ei monimutkainen järjestelmä.</figcaption>
</figure>

## Mitä rakennat?

Rakennat **n8n-pohjaisen agentin**, joka ratkaisee yhden konkreettisen ongelman. Agenttisi koostuu **3–5 solmusta**, jotka yhdessä muodostavat toimivan, ohjatun ja turvallisen työnkulun.

**Esimerkkejä mahdollisista agentteista:**

- Päivittäinen sähköpostien luokittelija ja yhteenvetäjä
- Asiakaspalvelun FAQ-botti, joka hakee vastauksia tietokannasta
- Sosiaalisen median seurantarobotti
- Palvelinlokien analysaattori, joka ilmoittaa virheistä
- Asiakkaiden tikettien luokittelija ja jakaja

**Agentin pitää olla yksinkertainen — emme tavoittele mitään monimutkaista.** 3–5 solmua riittää. Tärkeintä on, että agentti on **autonominen**: se tekee päätöksiä tilanteen mukaan, käyttää työkalua tai paria ja toimii itsenäisesti. Pieni agentti, jonka ymmärrät ja jonka rajat tunnistat, on tavoite.

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
Lyhytaikainen muisti (konteksti-ikkuna), pitkäkestoinen muisti, tilat ja tilasiirtymät, agentin identiteetti (soul). 150–200 sanaa.

**3. ⭐️ Agentti: Päättely (tunti 23)**
ReAct vai ketjuajattelu — kumpi sopii agenttisi ongelmaan ja miksi. Miten päättelymalli näkyy n8n-rakenteessa. 150–200 sanaa.

**4. ⭐️ Agentti: Turva (tunti 24)**
Minimioikeusperiaate, suurimmat riskit, turvakerroksen neljä tasoa (validointi, rajoitus, seuranta, palautuminen), lokitus. 150–200 sanaa.

**5. ⭐️ Agentti: Ihminen (tunti 25)**
Missä kohdissa ihmisen täytyy hyväksyä, millainen hyväksyntäportti on, mitä tapahtuu jos ihminen ei vastaa. 150–200 sanaa.

## Lopputuotoksen vaatimukset

::: luokka
Palauta oppimisympäristöön (esimerkiksi Moodle, Itslearning tai Google Classroom) yhtenä pakettina:
:::

::: verkko
Kokoa nämä tuotokset itsellesi yhdeksi paketiksi portfolioosi:
:::

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

::: verkko
Halutessasi jaa työsi — mitään ei palauteta minnekään.
:::

## Työkalut ja työskentelytapa

**Alusta:** n8n.

**Tekoälyapu:** Voit käyttää vapaasti ChatGPT:tä, Claudea tai Copilotia sparrauskumppanina ja suunnittelun tarkistamiseen. Älä anna tekoälyn päättää puolestasi — käytä sitä kyseenalaistamiseen ja näkökulmien laajentamiseen.

**Työskentelytapa:** Voit tehdä lopputyön **yksin tai parin kanssa**. Jos teet parin kanssa, jakakaa työ niin, että molemmat ymmärtävät koko agentin. Vertaisarvio tehdään aina toisen tiimin tai parin kanssa.

::: luokka
## Arviointi

Lopputyö arvioidaan viidellä osa-alueella (yhteensä 100 pistettä):

| Osa-alue | Pisteet |
|---|---|
| Toimiva n8n-työnkulku | 25 |
| Turvallisuus (turvakerros, lokitus, riskien tunnistaminen) | 20 |
| Dokumentaatio (README, ARCHITECTURE, SAFETY) | 20 |
| Testaus (testiraportin kattavuus ja syvyys) | 20 |
| Itsearviointi ja demo | 15 |
:::

::: verkko
## Itsearviointi

Opiskelet omaan tahtiin ilman oppilaitosta, joten arvioit työsi itse. Käy viisi osa-aluetta läpi ennen kuin toteat työn valmiiksi. Painoarvo kertoo, mihin kannattaa panostaa eniten — painotus on sama, jolla työtä muutenkin arvioitaisiin.

| Osa-alue | Painoarvo | Kysy itseltäsi |
|---|---|---|
| **Toimiva n8n-työnkulku** | 25 % | Toimiiko työnkulkuni? Ratkaiseeko se valitsemani ongelman? |
| **Turvallisuus** | 20 % | Ovatko turvakerros, lokitus ja riskien tunnistaminen kunnossa? |
| **Dokumentaatio** | 20 % | Ovatko README, ARCHITECTURE ja SAFETY selkeitä ja kattavia? |
| **Testaus** | 20 % | Onko testiraporttini riittävän kattava ja perusteellinen? |
| **Itsearviointi ja demo** | 15 % | Onko itsearviointini rehellinen ja demo selkeä? |
:::

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
