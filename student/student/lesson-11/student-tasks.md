# Opiskelutehtävät — Tietosuoja ja työkaluvalinta

> 📌 **Tähän tuntiin on vain yksi tehtävä** — mutta se on tärkeä. Tunnilla 10 vertailit työkaluja niiden vahvuuksien kannalta. Nyt katsot kentän laajempana: hinta, tietosuoja, palvelimien sijainti, GDPR. Ammatillinen valinta ei perustu pelkkään tekniseen paremmuuteen.

## Tehtävä 11.1 — Tee perusteltu suositus 🟢 SUOSITELTU

**Tavoite:** Opit perustelemaan tekoälytyökalun valinnan organisaation näkökulmasta — ottaen huomioon hinnan, tietosuojan ja käyttötarpeen. Tämä on ammattilaisen ajattelutapa.

### Vaiheet

#### Vaihe 1 — Valitse organisaatio

Valitse yksi seuraavista skenaarioista:

- **Pieni IT-yritys** (10 henkeä, ohjelmistokehitystä, pieni budjetti, paljon koodaustehtäviä)
- **Ammatillinen oppilaitos** (opettajat haluavat hyödyntää tekoälyä, opiskelijoiden tiedot suojattava, GDPR pakollinen)
- **Terveysasema** (potilastietoja käsitellään päivittäin, hyvin herkkä tietosuoja, henkilöstö ei ole tekoälyasiantuntijoita)
- **Kunnan tietohallinto** (julkinen organisaatio, julkisia ja sisäisiä asiakirjoja, useita kymmeniä työntekijöitä, kohtuullinen budjetti)
- **Pelistudio** (15 hengen tiimi, koodausta ja sisällöntuotantoa, kansainvälisiä asiakkaita, ideointi tärkeää)

#### Vaihe 2 — Kartoita käyttötarve

Kirjoita lyhyesti:

- **Käyttäjät:** Ketkä organisaatiossa käyttävät tekoälyä? (esim. opettajat, lääkärit, koodarit)
- **Tehtävät:** 3–4 tyypillistä tehtävää, joissa tekoäly auttaisi
- **Käsiteltävä tieto:** Sisältääkö tehtäviin liittyvä tieto henkilötietoja tai liikesalaisuuksia?
- **Budjetti:** Suuri / kohtuullinen / pieni

#### Vaihe 3 — Vertaa malleja päätöstaulukolla

Käy alla oleva taulukko läpi **valitun organisaation näkökulmasta**. Anna kullekin mallille arvio (✓ sopii, ⚠️ rajoituksin, ✗ ei sovi) — ja merkitse perustelu yhdellä lauseella.

| Malli | Tietosuoja | Hinta | Sopiiko? ✓ ⚠️ ✗ | Perustelu |
|---|---|---|---|---|
| ChatGPT | USA | Kallis | | |
| Claude | USA | Kallis | | |
| Gemini | USA / EU | Halpa | | |
| Copilot (M365) | EU mahdollinen | Keskihinta | | |
| DeepSeek | Kiina | Erittäin halpa | | |
| Llama tai Mistral (paikallisesti) | Oma kone | Ilmainen + laitteistokulu | | |

#### Vaihe 4 — Haasta valintasi tekoälyllä

Avaa ChatGPT, Claude tai Copilot ja anna sille koko päätöstaulukkosi sekä valitsemasi organisaation kuvaus. Esimerkkiprompti:

```
Toimit minulle tietoturvasparrauskumppanina. Olen suosittelemassa
tekoälytyökalua organisaatiolle ja perustelen valintani.

ORGANISAATIO: [kuvaa lyhyesti]

KÄYTTÖTARVE: [tehtävät, käsiteltävä tieto, budjetti]

TAULUKKONI: [liitä päätöstaulukko]

Haasta päätelmiäni. Erityisesti:
- Olenko tunnistanut oikean tietosuojariskin organisaation toiminnassa?
- Onko jokin malli, jonka hylkäsin liian nopeasti?
- Olenko ehkä liian optimistinen tai liian varovainen jossakin
  kohdassa?
- Mitä GDPR-näkökulmaa en ehkä ole vielä huomannut?

Älä tee valintaa puolestani — anna 2–3 huomiota, joiden pohjalta
voin viilata perustelujani.
```

#### Vaihe 5 — Kirjoita suositus

Kirjoita lyhyt suositus (5–8 lausetta), joka vastaa kolmeen kysymykseen:

- **Suositus:** Mitä 1–2 mallia organisaation kannattaa ottaa käyttöön?
- **Rajoitukset:** Mitä rajoituksia työntekijöille on annettava? (esim. *"Henkilötietoja sisältäviä tehtäviä ei saa antaa työkalulle X"*)
- **Yksi varoitus:** Mikä on suurin riski, joka organisaation on ymmärrettävä?

> 💡 **Vinkki:** Tehtävää ei palauteta, mutta tämän pohdinnan tulokset palaavat tunnilla 15, kun kuratoit oman bottisi tietopohjaa. Silloin joudut miettimään: *mitä materiaalia voin laittaa Copilotiin? Onko mukana henkilötietoja? Mitä rajoituksia minulla on?* Tunnin 11 oppi muuttuu silloin omaksi käytännön valinnaksi.

**Halvin ei ole aina paras. Paras työkalu on se, jonka käyttö ei aiheuta uusia ongelmia.**
