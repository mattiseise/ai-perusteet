# Rakennuspalikka 3 — Tietopohjan kuratointi

> 📌 **Tämä on kolmas ja viimeinen rakennuspalikka**, jonka keräät Tekoälyjen käyttö -osion aikana. Käytät niitä oppitunneilla 17 ja 18, kun rakennat *projektin määrittelydokumentin sparrauskumppanin* Microsoft Copilotiin. Säilytä tämä huolellisesti.

## Mitä teet?

Kuratoit bottisi **tietopohjan** — 3–5 dokumenttia, joista botti ammentaa oman alasi asiantuntemuksen. Tietopohja on se, mikä erottaa botin yleiseltä ChatGPT:ltä: kun yleinen tekoäly tietää kaikesta vähän, sinun bottisi tietää *juuri sinun alasi projektidokumentaatiosta* paljon.

Kuratointi ei ole vain "tiedostojen kerääminen". Se on **aktiivista valintaa** — mitä otat mukaan, mitä jätät pois, ja miksi. Hyvä tietopohja vastaa kysymykseen: *"Mitä botin pitää tietää, jotta se osaa auttaa juuri sinun alasi ammattilaista?"*

## Vaiheet

### Vaihe 1 — Palauta mieleen bottisi tarkoitus

Avaa **rakennuspalikka 2** (tunti 14, määrittelydokumentti). Katso erityisesti:

- Kenelle botti on (kohderyhmä)
- Mitä se tekee (tarkoitus)
- Missä järjestyksessä se ohjaa käyttäjää (työnkulku)

Tämä on tärkeää, koska tietopohjan pitää tukea juuri näitä asioita. Älä kerää sattumanvaraisia dokumentteja "joista botti voisi hyötyä" — kerää sellaisia, jotka palvelevat *tämän* botin tarkoitusta.

### Vaihe 2 — Listaa, mitä botin pitää tietää

Kirjoita 5–8 konkreettista **tietotarvetta**, joita botti tarvitsee voidakseen auttaa käyttäjää. Esimerkkejä eri aloilta:

| Ala | Esimerkkejä tietotarpeista |
|---|---|
| **IT-tuki** | Käyttöönottoprojektin rakenne, yleiset riskit järjestelmämuutoksissa, sidosryhmäkartoitus, palvelutason määrittely (SLA) |
| **Kyberturvallisuus** | Riskiarvion rakenne, OWASP:n riskikategoriat, auditoinnin laajuus, raportointivaatimukset, lainsäädännölliset rajat |
| **Pelikoodaus** | Game Design Documentin osat, ydinmekaniikan kuvaaminen, pelitestauksen suunnittelu, alustojen tekniset rajat, monetisaatiomallit |
| **Web-ohjelmointi** | Vaatimusten määrittely, tekninen arkkitehtuuri, käyttöliittymäluonnokset, API-rajapinnan kuvaus, tietoturvavaatimukset |

### Vaihe 3 — Etsi ja valitse 3–5 dokumenttia

Etsi materiaalia, joka kattaa tietotarpeesi. Hyviä lähteitä ovat:

- Kurssimateriaalisi (omat oppikirjat, luentodiat)
- Alasi yleiset standardit ja ohjeistukset
- Esimerkkidokumentit todellisista projekteista (saatavilla esim. GitHubissa, alan blogeissa)
- Wikipedia-artikkelit, mutta vain rakennetietona — älä lähteenä yksityiskohdille

**Tärkeintä:** 3–5 hyvää dokumenttia voittaa 20 keskinkertaista. Älä lataa kaikkea mitä löydät — botti hukuttautuu liialliseen materiaaliin ja sen vastaukset muuttuvat sekaviksi.

Hyviä kriteereitä valinnalle: *"Onko tämä luotettava lähde? Onko se ajantasainen? Tukeeko se botin työnkulkua? Onko siinä konkreettinen rakenne, jota botti voi opettaa eteenpäin?"*

### Vaihe 4 — Testaa tietopohjasi kattavuus tekoälyn kanssa

Avaa ChatGPT, Claude tai Copilot ja anna sille tietotarpeesi ja valitsemasi dokumentit. Esimerkkiprompti:

```
Toimit minulle sparrauskumppanina. Rakennan bottia, joka auttaa oman
alani ammattilaista projektin määrittelydokumentin laatimisessa. Tässä
bottini tietotarpeet ja valitsemani lähdedokumentit:

TIETOTARPEET: [liitä vaiheen 2 lista]

VALITUT DOKUMENTIT:
1. [dokumentin nimi + lyhyt kuvaus]
2. [dokumentin nimi + lyhyt kuvaus]
...

Auta minua arvioimaan kattavuus:
- Mitä tietotarpeita dokumentit eivät kata?
- Onko jokin dokumentti ehkä turha tai päällekkäinen toisen kanssa?
- Onko alalla jokin tyypillinen tieto, jota en ole vielä ottanut huomioon?

Älä ehdota uusia dokumentteja minulle — auta vain tunnistamaan aukot,
jotta voin etsiä lisämateriaalia itse.
```

Tämä on harjoitus siitä, miten tekoälyä käytetään *kattavuuden tarkistajana*. Tekoäly ei kerää tietopohjaa puolestasi, mutta auttaa huomaamaan sokeat pisteet.

### Vaihe 5 — Viimeistele tietopohja (tämä on rakennuspalikkasi)

Tee tekoälyn palautteen pohjalta korjauksia: lisää puuttuva dokumentti, poista päällekkäinen, vaihda parempi. Kokoa lopullinen tietopohja yhteen taulukkoon:

| Dokumentti | Lähde / linkki | Miksi tämä on tietopohjassa? |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

Tallenna tai lataa varsinaiset dokumentit yhteen kansioon — käytät niitä suoraan tunnilla 18, kun lataat ne Copilotiin.

> 💡 **Miksi tämä on tärkeää:** Botti, jonka tunnilla 18 rakennat, tunnistetaan ammattimaiseksi nimenomaan tietopohjan kautta. Yleinen ChatGPT osaa puhua periaatteesta, mutta sinun bottisi tuntee oman alasi käytännöt — koska olet kuratoinut sille oikeat dokumentit. Tämä ero on koko rakennusprojektin sydän.

**3 / 3 rakennuspalikkaa kerätty — valmis tuntiin 17**
