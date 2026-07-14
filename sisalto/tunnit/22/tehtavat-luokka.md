# Opiskelutehtävät: Agentin työkalut — tiedostot, haku ja komennot

> Tämä tunti tarkentaa lopputyösi työkaluvalintoja. Tunneilla 19 ja 21 olet määritellyt ongelman ja muistirakenteen. Tänään harjoittelet työkalujen valintaa.

*Kaikkia ei tarvitse tehdä. Valitse tehtävistä 1. Suosittelen kuitenkin, että teet työkalu-tehtävän — se sparraa suoraan lopputyösi rakentamista.*

---

## Tehtävä 22.1 — Oikea työkalu oikeaan tehtävään 🟢 SUOSITELTU

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

Avaa muistiinpanoistasi ⭐️ Agentti: Ongelma. Käy sama analyysi sille:

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

> 💡 **Vinkki muistiinpanoihin:** Kirjaa muistiinpanoihisi agenttisi minimityökalulista. Tämä helpottaa tunnin 26 n8n-rakentamista.

---

## Tehtävä 22.2 — Tutustu n8n-työnkulkuun 🟣 SYVENTÄVÄ

**Miksi tämä on hyödyllinen:** Tunnilla 26 rakennat oman agenttisi n8n:ssä. Tämä tehtävä antaa ennakkonäkymän käyttöliittymään.

### Tehtävä

1. Avaa n8n.
2. Tuo esimerkkityönkulku ("Import from File", opettajan jakama tiedosto).
3. Tutki työnkulkua ja vastaa kysymyksiin.

**A. Tunnista agentin osat.** Käy solmut läpi vasemmalta oikealle. Mahdolliset komponentit: **syötekäsittelijä, päättelijä, työkalu, turvakerros, tulosteen muotoilija**.

| Solmu (vasemmalta oikealle) | Mikä agentin osa tämä on? | Mitä se tekee? |
|---|---|---|
| Ensimmäinen | | |
| Toinen | | |
| Kolmas | | |
| Neljäs | | |
| Viimeinen | | |

**B. Jäljitä tiedon kulku.** Kirjoita omin sanoin 3–4 lausetta: mistä data tulee sisään, mitä sille tapahtuu matkalla ja mitä tulee ulos.

**C. Yhdistä teoriaan.** Mikä tunnin 22 työkalu (verkkohaku, tiedostot, viestit, tietokanta) on tässä työnkulussa käytössä? Jos haluaisit lisätä toisen työkalun, minkä lisäisit ja miksi?

> 💡 **Vinkki muistiinpanoihin:** Pidä silmällä esimerkkiä, jotta tunnilla 26 tunnistat solmutyypit nopeammin.

**Opettajalle:** tämä tehtävä vaatii esimerkki-n8n-työnkulun (esim. `esimerkki-agentti.json`), jonka jaat tunnin yhteydessä.

---

**Työkaluvalinnat tarkennettu — seuraavaksi päättelymalli**
