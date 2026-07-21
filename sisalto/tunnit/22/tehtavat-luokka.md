# Opiskelutehtävät: Agentin työkalut — tieto, haku ja rajatut toiminnot

> Tämä tunti tarkentaa lopputyösi työkaluvalintoja. Tunneilla 19 ja 21 olet määritellyt ongelman ja muistirakenteen. Tänään harjoittelet työkalujen valintaa.

*Kaikkia ei tarvitse tehdä. Valitse tehtävistä 1. Suosittelen kuitenkin, että teet työkalu-tehtävän — se tukee suoraan lopputyösi rakentamista.*

---

## Tehtävä 22.1 — Oikea työkalu oikeaan tehtävään — suositeltu

**Miksi tämä on tärkeää:** Agentin teho riippuu siitä, mitä työkaluja se osaa käyttää. Mutta kaikkia työkaluja ei tarvita aina — usein vähemmän on enemmän.

### Tehtävä

Sinulla on kolme erilaista agenttitehtävää:

**Tehtävä A: Asiakkaan laskun käsittely.** Agentti vastaanottaa asiakkaan kysymyksen laskusta, hakee laskutiedot tietokannasta ja vastaa asiakkaalle.

**Tehtävä B: Päivittäinen uutiskooste.** Agentti seuraa valittuja uutissivuja netissä, kokoaa päivän tärkeimmät otsikot yhteen ja kirjoittaa koosteen tiedostoon.

**Tehtävä C: Varaston seuranta.** Agentti lukee varaston tiedostoja, tunnistaa loppumassa olevat tuotteet ja ilmoittaa niistä vastuuhenkilölle.

### Vastausohje

Jokaisesta tehtävästä päätä:

1. **Tarvitseeko verkkohakua?** Miksi tai miksi ei?
2. **Tarvitseeko tiedostojen luku- tai kirjoitusoikeutta?** Mihin tiedostoihin?
3. **Tarvitseeko sähköpostin tai chat-viestin lähetystä?** Mille kanavalle?
4. **Tarvitseeko tietokantakyselyitä?** Mistä tietokannasta?

Kirjoita kuhunkin tehtävään lyhyt työkalulista — eli mitä n8n-solmuja agentti tarvitsisi.

### Sovellus omaan agenttiin

Avaa muistiinpanoistasi Agentti: Ongelma. Käy sama analyysi sille:

- Tarvitseeko agenttisi verkkohakua? Tiedostojen käsittelyä? Viestien lähetystä? Tietokantakyselyitä?
- Listaa lopuksi, mitä n8n-solmuja tarvitset minimissään.
- Mieti: voitko karsia jotain? Liian monta työkalua tekee agentista hauraan.

### Tekoälyvaihe — haasta työkaluvalinnat

```
Olen valinnut agentilleni seuraavat työkalut: [listaa]. Agentin
tehtävä on [kuvaa]. Toimi sparrauskumppanina ja kysy 2–3 kysymystä,
joiden avulla voin arvioida, onko jokin työkalu ylimääräinen tai
puuttuuko jokin. Älä ehdota itse — kysy niin että ajattelen.
```

> **Vinkki muistiinpanoihin:** Kirjaa muistiinpanoihisi agenttisi minimityökalulista. Tämä helpottaa tunnin 26 n8n-rakentamista.

---

## Tehtävä 22.2 — Kirjoita työkalusopimus — syventävä

**Miksi tämä on hyödyllinen:** Työkalusopimus tekee näkyväksi, mitä työkalu saa nähdä ja tehdä. Sama kuvaus auttaa sekä teknisessä toteutuksessa että dokumentoidussa suunnittelusuorituksessa.

### Tehtävä

Valitse yksi oman agenttisi työkalu ja kirjoita siitä lyhyt proosamuotoinen työkalusopimus. Kerro:

1. mitä tarkoitusta varten työkalua käytetään
2. mitä tietoa se saa ja mistä tieto tulee
3. mitä se palauttaa agentille
4. mitä se ei saa tehdä
5. milloin toiminto vaatii ihmisen hyväksynnän
6. mitä tapahtuu, jos työkalu palauttaa virheen.

Nimeä lopuksi n8n-solmu tai solmutyyppi, jolla toteuttaisit toiminnon. Ohjelmointikoodia ei tarvita.

---

**Työkaluvalinnat tarkennettu — seuraavaksi päättelymalli**
