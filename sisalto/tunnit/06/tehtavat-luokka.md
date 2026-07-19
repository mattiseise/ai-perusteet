# Opiskelutehtävät — Kuvat, ääni ja teksti

> **Kaikkia ei tarvitse tehdä.** Valitse tehtävistä yksi. Suosittelen tehtävää 6.1, joka harjoittaa tunnin ydintaitoa. Jos tietoturva kiinnostaa sinua, tee lisäksi syventävä tehtävä 6.2. Siinä harjoittelet käytännön työelämätaitoa, jota ei muualla kurssilla käsitellä yhtä konkreettisesti.

## Tehtävä 6.1 — Näyttö vai kuvaus? — SUOSITELTU

**Tavoite:** Näet käytännössä, miten paljon kuvakaappaus muuttaa tekoälyn kykyä auttaa. Kokeilet samaa ongelmaa kahdessa muodossa — pelkällä sanakuvauksella ja multimodaalisesti — ja huomaat itse, milloin "näyttö" kannattaa.

### Valitse ongelmasi

Valitse tilanne, jossa on **jokin visuaalinen elementti** — mikä tahansa näkymä, jonka haluat tekoälyn tulkitsevan. Voit valita reitin arjesta, opiskelusta tai työstä. Esimerkkejä:

- Kaavio, taulukko tai diagrammi, jota et täysin ymmärrä (vaikka uutisessa, laskussa tai opiskelumateriaalissa)
- Laitteen tai sovelluksen näyttö, johon haluat apua (esimerkiksi pesukoneen paneeli, puhelimen asetussivu tai verkkopankki)
- Virheilmoitus ohjelmassa, sovelluksessa tai verkkosivulla
- Käsin kirjoitettu resepti, ohje tai muistiinpano, jonka haluat mallin selittävän
- Valokuva jostakin, jonka haluat mallin tunnistavan tai selittävän (kasvi, kyltti, tuotteen pakkausteksti)

Jos sinulla ei ole valmista esimerkkiä, voit etsiä jonkun. Mitä konkreettisempi, sen parempi.

### Vaiheet

#### Vaihe 1 — Versio A: vain sanakuvaus

Avaa ChatGPT, Claude tai Copilot. **Älä lähetä kuvaa** — kuvaile ongelma vain sanoilla, niin tarkasti kuin osaat:

- Mitä näet?
- Mitä värejä ja muotoiluja näytöllä on?
- Mitä tekstiä näkyy (kopioi se mukaan, jos voit)?
- Mitä yritit tehdä, kun ongelma ilmestyi?

Kysy: *"Mistä tämä voisi johtua ja miten korjaisin sen?"* Tallenna vastaus.

#### Vaihe 2 — Versio B: kuva mukaan

Avaa **uusi keskustelu** (tärkeää, ettei edellinen vastaus vaikuta).

Käytä mallia, joka osaa katsoa kuvia — esim. ChatGPT, Claude, Gemini tai Copilot hyväksyvät kuvaliitteet. Anna sama sanakuvaus kuin vaiheessa 1 **JA** liitä mukaan kuvakaappaus.

Kysy sama kysymys. Tallenna vastaus.

#### Vaihe 3 — Vertaa

Aseta kaksi vastausta vierekkäin ja täytä taulukko:

| Mitä vertaillaan | Versio A (vain teksti) | Versio B (kuva + teksti) |
|---|---|---|
| Osuvuus juuri sinun ongelmaan | | |
| Ehdotettujen ratkaisujen määrä | | |
| Mainitsiko visuaalisia yksityiskohtia (värit, sijainnit, ikonit)? | | |
| Hyödyllisyys arvolla 1–5 | | |

#### Vaihe 4 — Kirjoita pohdinta

Vastaa 3–5 lauseella:

- Kumpi versio oli parempi, ja missä ero oli suurin?
- Millaisissa tilanteissa multimodaalinen syöte on välttämätön? Milloin pelkkä teksti riittää?
- Onko tilanteita, joissa kuvan lähettäminen voisi olla **huono** idea? (Vihjeitä: kuvassa näkyvä tieto, salaisuudet, henkilöt.)

> **Vinkki:** Tehtävää ei palauteta, mutta säilytä havaintosi. Etenkin viimeinen pohdintakysymys johdattaa seuraavaan tehtävään sekä koko kurssin etiikka- ja vastuukysymyksiin.

---

## Tehtävä 6.2 — Mitä et saa lähettää tekoälylle? — SYVENTÄVÄ

> **Tämä on syventävä tietoturvatehtävä.** Tee tämä, jos haluat oppia tunnistamaan vaaralliset asiat ennen kuin lähetät niitä tekoälylle. Tämä on käytännön työelämän taito, jonka takia moni työpaikka kieltää tekoälyn käytön kokonaan — ja jonka osaaminen erottaa vastuullisen käyttäjän aloittelijasta.

**Tavoite:** Tunnistat herkät tiedot kuvakaappauksessa, lokissa tai konfiguraatiotiedostossa. Opit sensuroimaan ne pois ja päättämään, mitä voi turvallisesti jakaa tekoälylle.

### Skenaariot

Alla on kaksi tilannetta, joissa IT-tukea pyytävä työntekijä on aikomassa lähettää tekoälylle pyynnön. Toimi kummassakin näin:

1. Tunnista herkät tiedot
2. Kirjoita sensuroitu, turvallinen versio
3. Perustele, miksi nämä tiedot ovat herkkiä
4. Päätä: voiko tekoäly silti auttaa sensuroinnin jälkeen?

#### Skenaario 1 — Tietokantayhteyden virhe

Työntekijä haluaa kysyä tekoälyltä, miksi tietokanta ei vastaa. Hän kopioi lokin sellaisenaan:

```
2024-03-14 10:23:45 ERROR: Failed to connect to database
2024-03-14 10:23:46 ERROR: Connection string:
  postgresql://admin:MyPassword123!@db.company.com:5432/users
2024-03-14 10:23:47 ERROR: Connection timeout after 30s
```

**Tehtäväsi:** Mikä tästä on vaarallista lähettää? Kirjoita turvallinen versio.

#### Skenaario 2 — Konfiguraatiotiedoston jakaminen

Kehittäjä haluaa kysyä tekoälyltä, miksi sovellus ei käynnisty. Hän on kopioimassa koko konfiguraatiotiedoston:

```json
{
  "app_name": "PaymentProcessor",
  "environment": "production",
  "database": {
    "host": "db.prod.company.com",
    "port": 5432,
    "user": "app_user",
    "password": "C0mp1ex!P@ssw0rd2024"
  },
  "api_keys": {
    "stripe": "sk_live_51234567890abcdef",
    "twilio": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  },
  "slack_webhook":
    "https://hooks.slack.com/services/T123/B456/xxxxxx"
}
```

**Tehtäväsi:** Voiko tämän jakaa ollenkaan? Jos voi, mitä sensuroit? Mikä on parempi tapa pyytää apua?

### Päätöskehikko

Täytä molemmista skenaarioista taulukko:

| Skenaario | Mitkä tiedot ovat herkkiä? | Mitä vahinkoa hyökkääjä voisi tehdä? | Voiko tekoäly auttaa sensuroinnin jälkeen? |
|---|---|---|---|
| 1 (tietokanta) | | | |
| 2 (config) | | | |

### Käytä tekoälyä apuna: testaa sensurointiasi

Avaa ChatGPT, Claude tai Copilot ja anna sille **oma sensuroitu versiosi**. Esimerkkiprompti:

```
Toimit minulle tietoturvasparrauskumppanina. Opettelen tunnistamaan
herkät tiedot, joita ei saa jakaa tekoälylle. Tässä alkuperäinen
materiaali ja oma sensuroitu versioni:

[liitä alkuperäinen]

[liitä oma sensuroitu versiosi]

Tarkista sensurointini. Jätinkö jotain herkkää huomaamatta? Onko
jotain, mitä sensuroin turhaan ja mikä olisi voinut jäädä mukaan?
Älä paljasta suoraan vastauksia — esitä kysymyksiä, joiden avulla
huomaan itse, jos joku kohta on ohi mennyt.
```

Tämä on harjoitus siitä, miten tekoälyä käytetään *tarkistajana*, ei korvikkeena omalle harkinnalle. Tietoturvassa lopullinen vastuu on aina ihmisellä.

### Yhteenveto

Kirjoita 2–3 lausetta: *"Säännöt, joita seuraan jatkossa ennen kuin jaan minkään materiaalin tekoälylle…"*

> **Vinkki:** Tehtävää ei palauteta, mutta yhden lauseen sääntö on yksi koko kurssin arvokkaimmista työelämän työkaluista. Säilytä se.

**Tunnin 6 jälkeen tiedät, milloin kuva auttaa — ja milloin se on riski.**
