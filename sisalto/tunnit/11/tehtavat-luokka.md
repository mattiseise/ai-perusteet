# Opiskelutehtävät — Tietosuoja ja työkaluvalinta

**📌 Tähän tuntiin on vain yksi tehtävä.** Se on tärkeä, koska tekoälytyökalun valinta ei perustu pelkkään tekniseen laatuun. Tunnilla 10 vertailit työkaluja niiden vahvuuksien perusteella. Nyt tarkastelet valintaa organisaation näkökulmasta: huomioon pitää ottaa myös **hinta**, **tietosuoja**, **palvelimien sijainti**, **GDPR** ja käyttötarve.

## Tehtävä 11.1 — Tee perusteltu suositus (SUOSITELTU)

**Tavoite:** Opit perustelemaan tekoälytyökalun valinnan organisaation näkökulmasta. Harjoittelet arvioimaan, mikä työkalu sopii tilanteeseen, kun huomioon otetaan **käyttötarve**, **hinta**, **tietosuoja** ja **riskit**. Tämä on vastuullisen käyttäjän ajattelutapa: paras työkalu ei ole aina teknisesti vahvin tai halvin, vaan se, jonka käyttö on tarkoituksenmukaista ja turvallista.

### Tee näin

#### Vaihe 1 — Valitse organisaatio

Valitse yksi seuraavista organisaatioista. Kuvittele, että sinua pyydetään suosittelemaan sille sopivaa tekoälytyökalua.

- **Oppilaitos** (esimerkiksi lukio, ammattikoulu tai kansalaisopisto): opettajat ja opiskelijat hyödyntäisivät tekoälyä, mutta opiskelijoiden tiedot pitää suojata ja GDPR:ää noudattaa.
- **Urheiluseura tai harrastuskerho:** jäsenviestintä, aikataulut ja ilmoittautumiset; mukana on jäsenten yhteystietoja, ja budjetti on pieni.
- **Pieni kahvila tai kioski:** asiakaspalvelua, markkinointia ja somepostauksia, pieni budjetti.
- **Pieni IT-yritys tai pelistudio:** 10–15 hengen tiimi, koodausta ja sisällöntuotantoa, kansainvälisiä asiakkaita.

**Tallenna:** Kirjoita valitsemasi organisaatio muistiin yhdellä lauseella.

#### Vaihe 2 — Kartoita käyttötarve

Kirjoita lyhyt kuvaus siitä, miten valitsemasi organisaatio käyttäisi tekoälyä. Vastaa ainakin seuraaviin kohtiin:

- **Käyttäjät:** Ketkä organisaatiossa käyttäisivät tekoälyä? Esimerkiksi opettajat, lääkärit, koodarit, asiakaspalvelijat tai hallinnon työntekijät.
- **Tehtävät:** Kirjoita 3–4 tyypillistä tehtävää, joissa tekoäly voisi auttaa.
- **Käsiteltävä tieto:** Sisältääkö tehtäviin liittyvä tieto henkilötietoja, potilastietoja, opiskelijatietoja, liikesalaisuuksia tai muuta arkaluonteista tietoa?
- **Budjetti:** Arvioi, onko budjetti suuri, kohtuullinen vai pieni.

#### Vaihe 3 — Vertaa vaihtoehtoja päätöstaulukolla

Täytä alla oleva taulukko **valitsemasi organisaation näkökulmasta**. Arvioi jokaisen työkalun sopivuutta seuraavilla merkeillä:

- **✓ Sopii:** työkalu sopii organisaation tarpeeseen ja riskit ovat hallittavissa.
- **⚠️ Sopii rajoituksin:** työkalua voi käyttää vain tietyissä tehtävissä tai selkeillä säännöillä.
- **✗ Ei sovi:** työkalu aiheuttaa liian suuren riskin tai ei vastaa organisaation tarpeeseen.

Kirjoita perusteluun yksi selkeä lause: miksi työkalu sopii, sopii rajoituksin tai ei sovi.

| Työkalu | Tietosuojan näkökulma | Hinta | Sopivuus ✓ ⚠️ ✗ | Perustelu |
| --- | --- | --- | --- | --- |
| **ChatGPT** | USA | Kallis |  |  |
| **Claude** | USA | Kallis |  |  |
| **Gemini** | USA / EU | Halpa |  |  |
| **Copilot (M365)** | EU mahdollinen | Keskihinta |  |  |
| **DeepSeek** | Kiina | Erittäin halpa |  |  |
| **Llama tai Mistral paikallisesti** | Oma kone tai oma palvelin | Ilmainen + laitteistokulut |  |  |

#### Vaihe 4 — Haasta valintasi tekoälyn avulla

Avaa ChatGPT, Claude tai Copilot ja anna sille valitsemasi organisaation kuvaus, käyttötarve ja päätöstaulukko. Tavoitteena ei ole antaa tekoälyn tehdä päätöstä puolestasi, vaan saada se haastamaan perustelujasi.

Voit käyttää esimerkiksi seuraavaa promptia:

> "Toimit minulle tietoturvasparrauskumppanina. Olen suosittelemassa tekoälytyökalua organisaatiolle ja perustelen valintani. ORGANISAATIO: [kuvaa valitsemasi organisaatio lyhyesti] KÄYTTÖTARVE: [käyttäjät, tehtävät, käsiteltävä tieto ja budjetti] PÄÄTÖSTAULUKKONI: [liitä päätöstaulukkosi] Haasta päätelmiäni. Pohdi erityisesti: Olenko tunnistanut organisaation keskeiset tietosuojariskit? Onko jokin työkalu, jonka hylkäsin liian nopeasti? Olenko liian optimistinen tai liian varovainen jossakin kohdassa? Mitä GDPR-näkökulmaa en ehkä ole vielä huomannut? Mitä rajoituksia työntekijöille pitäisi antaa? Älä tee valintaa puolestani. Anna 2–3 huomiota, joiden pohjalta voin parantaa perustelujani."

Muista arvioida tekoälyn vastaus kriittisesti. Tekoäly voi antaa hyödyllisiä näkökulmia, mutta se ei vastaa organisaation tietosuojapäätöksistä.

#### Vaihe 5 — Kirjoita perusteltu suositus

Kirjoita lopuksi **5–8 lauseen suositus**. Vastaa suosituksessa seuraaviin kysymyksiin:

- **Suositus:** Mitä 1–2 työkalua organisaation kannattaa ottaa käyttöön?
- **Perustelu:** Miksi nämä työkalut sopivat juuri tämän organisaation käyttötarpeeseen?
- **Rajoitukset:** Mitä sääntöjä työntekijöille pitää antaa? Esimerkiksi: *"Henkilötietoja sisältäviä tehtäviä ei saa antaa työkalulle X."*
- **Yksi varoitus:** Mikä on suurin riski, joka organisaation pitää ymmärtää ennen käyttöönottoa?

> **💡 Palautus:** Tehtävää ei palauteta, mutta säilytä päätöstaulukkosi ja suosituksesi. Tämän tehtävän opit palaavat myöhemmin, kun kuratoit oman bottisi tietopohjaa. Silloin joudut arvioimaan, mitä materiaalia voit laittaa Copilotiin, sisältääkö aineisto henkilötietoja ja millaisia rajoituksia sinun pitää noudattaa.

> **💡 Tarkista lopuksi:** Olet valinnut yhden organisaation, kartoittanut sen käyttötarpeen, täyttänyt päätöstaulukon, haastanut perustelujasi tekoälyn avulla ja kirjoittanut 5–8 lauseen suosituksen.

**Halvin ei ole aina paras. Paras työkalu on se, jonka käyttö ei aiheuta uusia ongelmia.**
