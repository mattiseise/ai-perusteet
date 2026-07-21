# Opiskelutehtävät: Agentin muisti ja konteksti

> Tämä tunti rakentaa lopputyösi toista osaa. Tänään suunnittelet, mitä agentti näkee nyt, mitä se säilyttää myöhemmäksi ja miten tehtävän tila kuvataan. Tuotos: **Agentti: Muisti** (2/5).

*Kaikkia ei tarvitse tehdä. Valitse tehtävistä 1. Suosittelen kuitenkin, että teet ainakin Agentti: Muisti -tehtävän — se on lopputyösi osa.*

---

## Agentti: Muisti — suositeltu

**Miksi tämä on tärkeää:** Tunnilla 26 rakennat n8n-työnkulun, jossa muisti on konkreettinen suunnittelupäätös. Ilman muististrategiaa agentti käsittelee jokaisen pyynnön kuin se olisi ensimmäinen.

### Tehtävä

Avaa muistiinpanoistasi Agentti: Ongelma. Kirjoita yhteensä 150–200 sanaa, jaettuna neljään lyhyeen osaan (~40–50 sanaa kukin):

**1. Konteksti ja keskusteluhistoria.** Mitä tietoa malli tarvitsee juuri tässä suorituksessa? Mitä historiasta valitaan tai tiivistetään kontekstiin?

**2. Pitkäkestoinen tieto ja tietopohja.** Mitä täsmällistä tietoa säilytetään rakenteisesti? Tarvitaanko erillistä tietopohjaa ja RAG-hakua? Perustele, miksi tieto kuuluu juuri tähän paikkaan.

**3. Tilat ja tilasiirtymät.** Mitä eri tiloja agentillasi voi olla? Mitkä ehdot liikuttavat tilasta toiseen? Jos agenttisi suorittaa tehtävän kerralla ilman tilamuutoksia, riittää maininta tästä.

**4. Käyttöoikeudet ja toimintaperiaatteet.** Kerro, kenen tietoja saa hakea, miten käyttäjä- tai organisaatiorajaus varmistetaan ja miten lähde tarkistetaan. Merkitse erikseen ohjauskehyksen säännöt — ne eivät ole muistia.

### Tekoälyvaihe — arvioi muistivalinnat

```
Olen suunnitellut agentilleni seuraavan muistirakenteen: [liitä
neljä osaa]. Agenttini tehtävä on [kuvaa]. Toimi sparrauskumppanina
ja kysy 2–3 kysymystä, jotka paljastavat, ovatko muistipäätökseni
perusteltuja. Erityisesti: tarvitseeko agentti pitkäkestoista muistia?
Onko tilamuutokset oikeasti tarpeen? Älä korjaa puolestani — kysy
niin että ajattelen.
```

> **Vinkki muistiinpanoihin:** Tallenna Agentti: Muisti muistiinpanodokumenttiisi. Tämä on 2/5 lopputyösi osista.

---

## Tehtävä 21.1 — Tieto oikeaan paikkaan — syventävä

**Miksi tämä on hyödyllinen:** Luotettava agentti ei käsittele kaikkea tietoa yhtenä muistina. Täsmällinen tilaustieto, keskusteluhistoria ja ohjekatkelma tarvitsevat eri käsittelyn.

### Tehtävä

Rakennat asiakaspalveluagentin. Luokittele seuraavat tiedot: nykyinen konteksti, keskusteluhistoria, prosessin tila, rakenteinen pitkäkestoinen tieto tai tietopohjasta RAGilla haettava katkelma.

- asiakkaan uusin kysymys
- tilausnumero ja toimituksen tila
- tiivistelmä aiemmista kokeiluista
- hyväksytty palautusehto
- tieto siitä, odottaako tapaus ihmisen hyväksyntää

Perustele jokaisesta, mistä tieto haetaan, kuka saa nähdä sen ja miten sen ajantasaisuus tai lähde tarkistetaan.

> **Vinkki muistiinpanoihin:** Tätä tehtävää ei palauteta, mutta jos havaitsemasi periaatteet vaikuttavat omaan Agentti: Muisti -valintaasi, päivitä se.

---

**Agentti: Muisti valmis — 2/5 lopputyöstä koossa**
