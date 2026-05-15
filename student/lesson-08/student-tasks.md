# Opiskelutehtävät — Etiikka, oikeudet ja vastuu

> 📌 **Kaikkia ei tarvitse tehdä.** Valitse tehtävistä 1. Suosittelen tehtävää 8.1 — se opettaa tarkastelemaan samaa tilannetta useasta näkökulmasta, mikä on juuri se ajattelutapa, jota tarvitset tuomaripöydän asiantuntijalausunnossa. Jos sinulla on aikaa ja olet kiinnostunut algoritmisen syrjinnän kysymyksistä, tee lisäksi syventävä tehtävä 8.2.

## Tehtävä 8.1 — Tekijänoikeudet: oikeustapauksen näkökulmat 🟢 SUOSITELTU

**Tavoite:** Opit tarkastelemaan samaa eettistä kysymystä usean osapuolen näkökulmasta — kantajan, vastaajan ja omasta. Tämä on sama ajatteluharjoitus, jota tuomaripöytä vaatii.

### Valitse oikeustapaus

Valitse yksi näistä todellisista oikeustapauksista:

- **The New York Times vs. OpenAI** (2023–) — sanomalehti haastoi OpenAI:n oikeuteen artikkelien käytöstä koulutusdatassa
- **Authors Guild & kirjailijat vs. OpenAI** (2023–) — kirjailijoiden ryhmäkanne ChatGPT:n koulutuksesta romaaneilla
- **Getty Images vs. Stability AI** (2023–) — kuvapankkiyhtiö haastoi Stable Diffusionin tekijät
- **Andersen ym. vs. Stability AI** (2023–) — kuvataiteilijoiden ryhmäkanne kuvageneraattoreiden koulutuksesta

### Vaiheet

#### Vaihe 1 — Selvitä perusfaktat

Etsi tapauksesta tietoa (Wikipedia, uutispalvelut, oikeudelliset analyysit). Vastaa lyhyesti:

- Kuka haastoi kenet, ja milloin?
- Mitä kantaja väittää tapahtuneen?
- Mitä vastaaja sanoo puolustuksekseen?
- Mikä on "reilu käyttö" (fair use) -argumentin ydin?

#### Vaihe 2 — Käytä tekoälyä apuna näkökulmien jäsentämiseen

Avaa ChatGPT, Claude tai Copilot ja anna sille tapaus. **Tärkeä huomio:** tekoäly itse on osapuoli näissä keskusteluissa — se voi olla puolueellinen suuntaan tai toiseen. Pyydä siltä siis tasapainoista näkökulmavertailua:

```
Toimit minulle sparrauskumppanina. Tutkin oikeustapausta [nimeä tapaus]
ja yritän muodostaa siitä oman, perustellun näkemyksen. Auta minua
jäsentämään asiaa esittämällä:

- Kantajan vahvimmat argumentit (3–4 kpl)
- Vastaajan vahvimmat argumentit (3–4 kpl)
- Yhden tai kaksi näkökulmaa, joita en ole ehkä huomannut

Älä kerro minulle, kumpi on oikeassa. Esitä myös, jos huomaat
itsessäsi taipumusta puolueellisuuteen, kun käsittelet aihetta,
joka koskee tekoälyä.
```

Viimeinen pyyntö on tärkeä — se opettaa sinua tunnistamaan, milloin tekoäly itse on osapuoli keskustelussa.

#### Vaihe 3 — Täytä näkökulmataulukko

Käy neljä kysymystä läpi ja kirjoita lyhyt vastaus kuhunkin sarakkeeseen:

| Kysymys | Kantajan näkemys | Vastaajan näkemys | Sinun näkemyksesi |
|---|---|---|---|
| Olisiko tekijöiltä pitänyt pyytää lupa? | | | |
| Pitäisikö tekijöille maksaa korvausta? | | | |
| Onko mallin koulutus "muuntavaa käyttöä" (transformative use)? | | | |
| Mikä on suurin riski yhteiskunnalle, jos tämä jatkuu nykyisellään? | | | |

#### Vaihe 4 — Kirjoita oma johtopäätös

Vastaa 4–6 lauseella:

- Kumpi osapuoli on omasta mielestäsi enemmän oikeassa — ja miksi?
- Mikä on ammattilaisen vastuusi, kun käytät tekoälyä, jonka koulutusdatasta on kiistaa?
- Mikä yhden lauseen sääntö ohjaa toimintaasi jatkossa? *"Käytän generatiivista tekoälyä siten, että…"*

> 💡 **Vinkki:** Tehtävää ei palauteta, mutta säilytä muistiinpanosi huolellisesti. Jos valitset tuomaripöydän skenaarioista Skenaario 3:n (markkinointisisältö ja tekijänoikeudet), tämä taulukko on käytännössä valmis pohja koko analyysillesi.

---

## Tehtävä 8.2 — Algoritminen harha: tositapauksen analyysi 🟣 SYVENTÄVÄ

> **Tämä on syventävä lisätehtävä.** Tee tämä, jos haluat ymmärtää, miten algoritminen syrjintä syntyy käytännössä — ja kuinka se voitaisiin estää. Jos aiot valita tuomaripöydässä Skenaario 2:n (rekrytointialgoritmi), tämä tehtävä antaa sille suoran pohjan.

**Tavoite:** Tunnistat, miksi algoritmi voi olla puolueellinen, vaikka kukaan ei sitä tarkoittaisi. Ymmärrät, miten harha syntyy koulutusdatasta — ja miten sen voi testata ja korjata.

### Valitse tapaus

Valitse yksi tositapaus:

- **Amazonin rekrytointialgoritmi** (2014–2018) — yritti karsia naiset hakijoista
- **COMPAS-algoritmi** — yhdysvaltalaisen oikeusjärjestelmän uusintarikoksen riskiarvio, joka osoittautui rasistiseksi
- **Apple Card -luottoraja** (2019) — paljon korkeammat rajat miehille kuin samassa taloudessa asuville vaimoille
- **Kasvojentunnistus eri ihonväreillä** — toimii merkittävästi huonommin tummaihoisilla naisilla (Joy Buolamwinin Gender Shades -tutkimus)

### Vaiheet

#### Vaihe 1 — Selvitä perusfaktat

Hae tietoa luotettavista lähteistä (Wikipedia, uutispalvelut, tieteelliset artikkelit). Täytä taulukko:

| Kohta | Vastauksesi |
|---|---|
| **Algoritmin tehtävä** | Mitä sillä oli tarkoitus tehdä? |
| **Syrjityn ryhmä** | Ketä se kohteli epäoikeudenmukaisesti? |
| **Harhan lähde** | Mistä koulutusdatasta puolueellisuus syntyi? |
| **Vahinko** | Mitä konkreettista haittaa se aiheutti? |
| **Lopputulos** | Miten asia ratkaistiin tai jatkuuko se? |

#### Vaihe 2 — Käytä tekoälyä apuna juurisyiden tunnistamiseen

Avaa ChatGPT, Claude tai Copilot. Anna sille perusfaktat ja pyydä apua juurisyiden hahmottamiseen:

```
Toimit minulle sparrauskumppanina. Tutkin algoritmisen syrjinnän
tapausta [nimeä tapaus]. Tässä keräämäni perustiedot:

[liitä vaiheen 1 taulukko]

Auta minua ymmärtämään, mistä puolueellisuus syntyi. Erityisesti:
- Mitkä piirteet koulutusdatassa aiheuttivat harhan?
- Olisiko se voitu havaita ennen tuotantokäyttöä?
- Mitä testejä olisi pitänyt tehdä — ja kuka olisi ollut vastuussa
  niiden tekemisestä?

Älä anna minulle valmiita vastauksia. Esitä vastakysymyksiä, joiden
kautta voin ajatella asiaa tarkemmin itse.
```

Tämä on harjoitus siitä, miten tekoälyä käytetään analyysityökaluna eettisissä kysymyksissä — säilyttäen samalla oma harkinta.

#### Vaihe 3 — Suunnittele testausote

Kuvittele, että sinua pyydetään tarkistamaan vastaava algoritmi organisaatiossasi **ennen** sen käyttöönottoa. Kirjoita 3–5 testiä, joilla varmistaisit, ettei algoritmi syrji. Esimerkkejä:

- "Ajaisin algoritmin läpi 100 testidatapistettä, joista puolet kuvaa miehiä ja puolet naisia samalla pätevyydellä. Vertaisin tuloksia."
- "Tarkistaisin koulutusdatan ennen kuin malli edes opetetaan: missä suhteessa eri ryhmiä on edustettuna?"

#### Vaihe 4 — Vastuukysymys

Vastaa lyhyesti (3–4 lausetta):

- Jos algoritmi osoittautuu syrjiväksi, kuka on vastuussa? Algoritmin kehittänyt yritys? Sitä käyttävä organisaatio? Yksittäinen työntekijä, joka ehdotti sen käyttöönottoa?
- Mikä on omat ammatillinen vastuusi, kun käytät tai suosittelet tekoälyjärjestelmää työssäsi?

> 💡 **Vinkki:** Tehtävää ei palauteta, mutta säilytä muistiinpanot. Jos valitset tuomaripöydässä Skenaario 2:n (rekrytointialgoritmi), olet jo puolessa välissä analyysissäsi.

**Tunnin 8 jälkeen olet valmis tuomaripöytään.**
