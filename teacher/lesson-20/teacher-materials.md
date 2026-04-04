# Opettajan materiaalit – Lesson 20

## Osaamistavoitteet (Bloom)

**Ymmärtää / Analysoi:**
- Opiskelija osaa soveltaa päätöspuu-metodia todellisiin automaatioratkaisujen valintatilanteisiin.
- Opiskelija ymmärtää, että agentti ei aina ole parempi valinta kuin yksinkertaisempi ratkaisu.
- Opiskelija osaa tunnistaa tekijät, jotka tekevät agentin järkevän tai kannattamattoman investoinnin.

1. **Selittää suunnittelusilmukan** — agentti jaottelee ongelman askeleihin ja suunnittelee iteratiivisesti
2. **Tunnistaa työkalut agenteissa** — ymmärtää, mitä työkaluja agentti tarvitsee ja mitkä ovat turvallisuusriskit
3. **Analysoida muistia agenteissa** — konteksti-ikkuna vs. ulkoinen muisti
4. **Ymmärtää orkestraattorin roolia** — kuinka agenttijärjestelmä koordinoidaan

## Yleisiä väärinkäsityksiä ja korjaukset

### Väärinkäsitys 1: "Agentti vain tekee asioita ilman ajattelua"

**Miksi opiskelija näin ajattelee:** Agentin prosessi näyttää automaattiselta ja mekaaniselta.

**Korjaus:** Agentti käy läpi **suunnittelusilmukan** jokaisen askeleen kohdalla. Se ei vain reagoi — se ajattelee "mitä tarvitsen?", "mitkä työkalut?", "entä jos epäonnistuu?". Prosessi on iteroiva, ei lineaarinen.

**CFU-kysymys:** "Kuvaa, mitä agentti tekee, kun se kohtaa ongelman, jota se ei osaa ratkaista. Meneekö se vain eteenpäin, vai ajattelee uutta strategiaa?"

### Väärinkäsitys 2: "Kaikkiin ongelmiin on agentille oikeat työkalut"

**Miksi opiskelija näin ajattelee:** Opiskelijat voivat kuvitella, että agentti on universaali ratkaisijaorganisaatio.

**Korjaus:** Agentti on vain niin hyvä kuin sen työkalut. Jos agentilla ei ole tietokantahakua, se ei voi hakea tietokannasta. Jos sillä ei ole sähköpostijärjestelmään pääsyä, se ei voi lähettää sähköposteja. Agentti on **spesifioitu**, ei universaali.

**CFU-kysymys:** "Jos agentti tarvitsee apua palvelimen diagnostiikasta, mutta sillä on vain pääsy wikiin, mitä se voi tehdä?"

### Väärinkäsitys 3: "Muisti ja konteksti ovat sama asia"

**Miksi opiskelija näin ajattelee:** Molemmat liittyvät agentin kykyyn muistaa asioita.

**Korjaus:** Ne eivät ole sama:
- **Konteksti-ikkuna** on *lyhytaikainen*, jonkin hetken voimassaoleva. Se menetetään, kun agentti suljetaan.
- **Ulkoinen muisti** on *pitkäaikainen*, tallennettu tietokantaan. Se säilyy seuraavaa agentin suoritusta varten.

Hyvä agentti käyttää molempia: konteksti-ikkunaa nykyisen tehtävän ymmärtämiselle, ulkoista muistia oppimiselle.

**CFU-kysymys:** "Jos agentti käsittelee asiakasta, jolle se on ratkaissut ongelman aiemmin, mistä se hakee tiedon aiemmasta ratkaisusta? Konteksti-ikkunasta vai ulkoisesta muistista?"

## Opettajavetoiset tehtävät

### Tehtävä 1: Suunnittelusilmukan valinta (20 min)

Näytä opiskelijoille kompleksi ongelma ja pyydä heitä kuvaamaan, kuinka agentti ratkaisisi sen.

Esimerkki:
> "Agentti saa tehtävän: 'Analysoi tämä tiiketti ja anna ratkaisu.' Tiketti sanoo: 'En pysty kirjautumaan tililleni, saan virheen 502.' Mitä agentti tekee?"

Opiskelijoiden pitäisi kuvata:
1. **Havainnoi**: Lue tiiketti, tunnista ongelman tyyppi
2. **Suunnittele**: "502 on palvelimen virhe. Tarvitsen palvelimen lokeja. Tarvitsen myös tietää asiakkaasta, heidän laitteet, käyttöjärjestelmä"
3. **Toimi**: Hae palvelimen lokit, etsi merkintöjä asiakkaan IP:stä
4. **Tarkkaile**: Löyditkö ongelman? Jos ei, mitä muuta pitäisi kokeilla?

Tämä harjoitus näyttää, että suunnittelu ei ole "taika" — se on systemaattinen prosessi.

### Tehtävä 2: Työkalun merkitys (15 min)

Anna opiskelijoille luettelo työkaluista ja pyydä heitä arvioimaan, mitä agentti voi tehdä:

```
Agentti saa nämä työkalut:
- Web-haku
- Sähköpostiin pääsy (luku- ja lähetys)
- Tietokanta-haku (vain luku)

Mitkä näistä tehtävistä agentti voi tehdä?
1. Etsiä dokumentaatioita verkosta → kyllä (web-haku)
2. Lähettää asiakkaalle vastauksen → kyllä (sähköposti)
3. Muokata asiakkaan tilannetta tietokannassa → ei (vain luku)
4. Hakea vanhat tapaukset tietokannasta → kyllä (tietokanta-luku)
5. Poistaa asiakkaan tiedot tietokannasta → ei (ei oikeutta)
```

Keskustelu: "Mitä riskejä olisi, jos agentilla olisi muokkausoikeus tietokantaan?"

---

## CFU-Kysymykset

1. **Suunnittelu**: "Miksi agentti jaottelee ongelman askeleihin? Miksi se ei vain kokeile ensimmäistä ideaa?"

2. **Työkalut**: "Jos agentti saa uuden työkalun (esim. puhelun tekeminen asiakkaalle), mitä uusia tehtäviä se voisi tehdä?"

3. **Muisti**: "Mitä eroa on sillä, että agentti muistaa asiakkaan edellisen tilauksen konteksti-ikkunasta vs. ulkoisesta muistista?"

4. **Orkestraattori**: "Kuka tai mikä kontrolli prosessia? Entä jos orkestraattori epäonnistuu?"

---

## Lisäresurssit

Opiskelijat voivat tutkia oikeita agenttikehyksiä (LangChain, Autogen, Camel), joissa näkevät, miten nämä komponentit toteutetaan koodissa. Mutta oppitunnissa fokus on **käsitteistö**, ei koodi.
