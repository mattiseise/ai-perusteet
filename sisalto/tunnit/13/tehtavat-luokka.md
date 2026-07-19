# Opiskelutehtävät — AI työparina

> **Valitse yksi tehtävä.** Suositeltu tehtävä 13.1 harjoittaa koko työparityöskentelyn sykliä: tekoälyn luonnos → oma muokkaus → kriittinen arviointi. Tee lisäksi syventävä tehtävä 13.2, jos haluat harjoitella virheilmoitusten tulkintaa.

## Tehtävä 13.1 — Kirjoita ohje työparityönä (suositeltu)

**Tavoite:** Opit hyödyntämään tekoälyä koko sykliä: pohjan tekijänä, muokkauksen kohteena ja kriittisenä arvioijana. Ihminen päättää suunnan, tekoäly auttaa nopeuttamaan.

### Vaiheet

#### Vaihe 1 — Valitse aihe

Valitse itseäsi kiinnostava aihe — arjesta, harrastuksesta, opiskelusta tai työelämästä. Esimerkkejä eri aloilta:

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

> **Vinkki:** Säilytä ohje ja muistiinpano omassa kansiossasi, vaikka tehtävää ei palauteta. Tunnilla 18 rakennat oman apuri-bottisi samojen periaatteiden varaan: se ohjaa käyttäjää vaihe vaiheelta ja tarvitsee selkeät rajat.

---

## Tehtävä 13.2 — Tulkitse virheilmoitus tekoälyn kanssa (syventävä)

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

> **Vinkki:** Säilytä selvitys omissa muistiinpanoissasi. Voit käyttää sitä ratkaisupohjana, jos kohtaat samanlaisen virheilmoituksen myöhemmin.

**Tekoäly ehdottaa, sinä päätät.**
