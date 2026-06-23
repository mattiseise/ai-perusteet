# Opiskelutehtävät — AI työparina

> 📌 **Kaikkia ei tarvitse tehdä.** Valitse tehtävistä 1. Suosittelen tehtävää 13.1, jossa harjoittelet koko työparityöskentelyn sykliä: pohja tekoälyltä → oma muokkaus → kriittinen arviointi. Jos sinulla on aikaa ja haluat lisäharjoitusta virheilmoitusten tulkinnassa, tee lisäksi syventävä tehtävä 13.2.

## Tehtävä 13.1 — Kirjoita ohje työparityönä 🟢 SUOSITELTU

**Tavoite:** Opit hyödyntämään tekoälyä koko sykliä: pohjan tekijänä, muokkauksen kohteena ja kriittisenä arvioijana. Ihminen päättää suunnan, tekoäly auttaa nopeuttamaan.

### Vaiheet

#### Vaihe 1 — Valitse aihe omalta alaltasi

Valitse itseäsi kiinnostava aihe tai ala. Esimerkkejä eri aloilta:

- **Liiketalous ja kauppa:** Miten asiakas tekee palautuksen verkkokaupassa — vaihe vaiheelta
- **Sosiaali- ja terveysala:** Miten omainen varaa ajan terveysaseman sähköisestä palvelusta
- **Media ja viestintä:** Miten julkaiset ensimmäisen videon suoratoistopalveluun
- **Ravintola- ja catering:** Miten uusi työntekijä käyttää kassajärjestelmää tilauksen kirjaamiseen
- **Harrastukset:** Miten asennat ja otat käyttöön treenipäiväkirja-sovelluksen
- **IT:** Miten käyttäjä jakaa työpöytänsä etänä (esim. Quick Assist) — vaihe vaiheelta

Ohjeen kohderyhmänä on **aloittelija** — joku, joka ei tiedä aiheesta ennestään mitään. Pituus enintään 8 vaihetta.

#### Vaihe 2 — Pyydä pohja tekoälyltä

Avaa ChatGPT, Claude tai Copilot. Anna tekoälylle selkeä pyyntö, jossa määrittelet kohderyhmän, käyttöjärjestelmän tai laitteen ja pituuden. Esimerkkiprompti:

```
Kirjoita selkeä, vaiheittainen ohje aiheesta [aihe].

Kohderyhmä: [kuvaa kuka käyttäjä on ja mitä hän osaa]
Käyttöjärjestelmä tai laite: [tarkenna]
Pituus: enintään 8 vaihetta

Käytä yksinkertaista kieltä, ei teknistä jargonia. Aloita aina
vaihe verbillä ('Avaa…', 'Klikkaa…', 'Valitse…').
```

Tallenna saamasi vastaus.

#### Vaihe 3 — Arvioi ja muokkaa

Lue ohje rauhassa kuin olisit itse aloittelija. Vastaa mielessäsi:

- Onko jokin vaihe epäselvä?
- Puuttuuko jokin oleellinen kohta (esim. ohjelman lataaminen ennen asennusta)?
- Onko jokin teknisesti väärin? (Esim. valikon nimet, painikkeiden nimet — tekoäly arvailee usein)
- Onko jokin liian tekninen kohderyhmälle?

Muokkaa ohje. Korjaa, lisää puuttuvat kohdat, yksinkertaista vaikeat. Tämä on **tärkein vaihe** — tässä ihminen ottaa ohjat.

#### Vaihe 4 — Käytä tekoälyä toistamiseen, nyt kriittisenä lukijana

Avaa tekoäly uudelleen (uusi keskustelu suositeltava). Anna sille muokkaamasi versio ja pyydä sitä toimimaan *kohderyhmänä*:

```
Toimit minulle koehenkilönä. Olet [kohderyhmäsi kuvaus —
esim. 'eläkkeellä oleva henkilö, joka osaa lukea sähköposteja
mutta ei ole asentanut ohjelmistoja ennen'].

Lue seuraava ohje hitaasti, ikään kuin yrittäisit oikeasti
seurata sitä. Kerro:

- Mihin kohtaan jäisit jumiin?
- Mikä sanavalinta on epäselvä?
- Mitä tietoa kaipaisit lisää?

OHJE:
[liitä muokkaamasi versio]

Älä korjaa ohjetta puolestani — kerro vain, mikä siinä ei toimi
sinulle kohderyhmänä.
```

Tekoäly antaa palautetta — käytä sitä ohjeen viimeistelyyn. Tämä on harjoitus siitä, miten tekoälyä käytetään *testaajana*, ei kirjoittajana.

#### Vaihe 5 — Viimeistele ja kirjoita lyhyt huomio

Tee viimeiset korjaukset palautteen perusteella. Lopuksi vastaa mielessäsi 2–3 lauseella:

- Mitä tekoälyn pohjassa oli hyvää, mikä säilyi loppuun saakka?
- Mitä piti muuttaa, koska tekoäly ei tiennyt todellisuutta?
- Mitä huomasit, kun tekoäly toimi kohderyhmänä — auttoiko se?

> 💡 **Vinkki:** Tehtävää ei palauteta, mutta säilytä ohje ja muistiinpano omassa kansiossasi. Tunnilla 18 rakentamasi *oma apuri-botti* tekee periaatteessa samaa: ohjaa käyttäjää vaihe vaiheelta jonkin asian läpi. Ymmärrät paremmin, miksi rajat ja tarkennukset ovat tärkeitä, kun olet itse joutunut tekemään ohjetta.

---

## Tehtävä 13.2 — Tulkitse virheilmoitus tekoälyn kanssa 🟣 SYVENTÄVÄ

> **Tämä on syventävä lisätehtävä.** Tee tämä, jos haluat harjoitella tärkeää digiarjen taitoa: virheilmoitusten tulkintaa.

**Tavoite:** Opit selvittämään tuntemattomia virheilmoituksia järjestelmällisesti tekoälyn avulla — ja arvioimaan, milloin tekoälyä voi uskoa ja milloin pitää tarkistaa toisaalta.

### Vaiheet

#### Vaihe 1 — Valitse virheilmoitus

Valitse **yksi** seuraavista (tai käytä omaa, jos sellainen on tullut vastaan):

- `Your connection is not private — NET::ERR_CERT_DATE_INVALID`
- `0x80070005 — Access Denied`
- `No Internet — DNS_PROBE_FINISHED_NXDOMAIN`
- `ECONNREFUSED 127.0.0.1:5432`
- `The disk you inserted was not readable by this computer`

#### Vaihe 2 — Kysy tekoälyltä, mutta strukturoidusti

Kopioi virheilmoitus tarkalleen — älä kirjoita ulkomuistista. Esimerkkiprompti:

```
Sain seuraavan virheilmoituksen:

[VIRHEILMOITUS]

Selitä minulle:
1. Mitä tämä virheilmoitus tarkoittaa selkokielellä?
2. Mikä on todennäköisin syy?
3. Mitä kannattaa kokeilla ensin (vähiten riskialtis ratkaisu)?
4. Onko tilanteita, joissa tämän virheilmoituksen näkeminen on
   merkki vakavammasta ongelmasta?
5. Onko jokin toimenpide, jota EI kannata tehdä tämän
   virheilmoituksen yhteydessä?
```

#### Vaihe 3 — Tarkista tekoälyn vastaus toisaalta

Tekoäly voi olla väärässä vakuuttavasti. Tarkista vähintään yhdellä lähteellä:

- Microsoftin / Applen / Googlen tukisivut, jos kyseessä on käyttöjärjestelmävirhe
- Stack Overflow tai virallinen dokumentaatio teknisille virhekoodeille
- Toinen tekoälytyökalu — kysy samaa kysymystä ChatGPT:ltä ja Claudelta, vertaa

Merkitse muistiin: **vastasivatko lähteet tekoälyn selitystä?** Jos ei, miten ne erosivat?

#### Vaihe 4 — Kirjoita lyhyt selvitys

Kirjoita 5–8 lauseen selvitys, jossa:

- Selität virheilmoituksen omilla sanoillasi (ei kopioi tekoälyn vastausta)
- Listaat ensimmäinen ratkaisuyritys
- Mainitset mahdollisen vakavamman taustasyyn, jos sellainen on
- Kommentoit: kuinka luotettavalta tekoälyn vastaus tuntui, kun tarkistit sen toisaalta?

> 💡 **Vinkki:** Tehtävää ei palauteta, mutta tämän taidon arvo kasvaa työuran mittaan. Säilytä selvitys omiin muistiinpanoihin — kun samanlainen virheilmoitus tulee vastaan toistamiseen, sinulla on jo valmis ratkaisupohja.

**Tekoäly ehdottaa, sinä päätät.**
