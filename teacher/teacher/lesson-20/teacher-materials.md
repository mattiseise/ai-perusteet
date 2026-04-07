# Opettajan materiaalit – Oppitunti 20

## Osaamistavoitteet (Bloom)

**Ymmärtää / Analysoida:**
- Opiskelija osaa soveltaa päätöspuumenetelmää todellisiin automaatioon liittyviin valintatilanteisiin.
- Opiskelija ymmärtää, että agentti ei aina ole parempi valinta kuin yksinkertaisempi ratkaisu.
- Opiskelija osaa tunnistaa tekijät, jotka tekevät agentista järkevän tai kannattamattoman investoinnin.

Lisäksi opiskelijat oppivat:

1. **Selittää suunnittelusilmukan** – agentti jakaa ongelman askeleisiin ja suunnittelee iteratiivisesti
2. **Tunnistamaan työkalut agenteissa** – ymmärtää, mitä työkaluja agentti tarvitsee ja mitkä ovat turvallisuusriskit
3. **Analysoimaan muistia agenteissa** – konteksti-ikkuna vs. ulkoinen muisti
4. **Ymmärtämään orkestraattorin rooli** – kuinka agenttijärjestelmää koordinoidaan

## Yleisiä väärinkäsityksiä ja korjaukset

### Väärinkäsitys 1: "Agentti vain tekee asioita ilman ajattelua"

**Miksi opiskelija näin ajattelee:** Agentin prosessi näyttää automaattiselta ja mekaaniselta.

**Korjaus:** Agentti käy läpi **suunnittelusilmukan** jokaisen tehtävän kohdalla. Se ei vain reagoi – se ajattelee: "Mitä tarvitsen?", "Mitkä työkalut?", "Entä jos tämä epäonnistuu?" Prosessi on iteratiivinen eikä lineaarinen.

**CFU-kysymys:** "Kuvaa, mitä agentti tekee, kun se kohtaa ongelman, jota se ei osaa ratkaista. Meneekö se vain eteenpäin vai miettiikö se uutta strategiaa?"

### Väärinkäsitys 2: "Kaikkiin ongelmiin on agentille oikeat työkalut"

**Miksi opiskelija näin ajattelee:** Opiskelijat voivat kuvitella agentin universaaliksi ratkaisijajärjestelmäksi.

**Korjaus:** Agentti on vain niin hyvä kuin sen työkalut. Jos agentilla ei ole tietokantahakua, se ei voi hakea tietokannasta. Jos sillä ei ole pääsyä sähköpostijärjestelmään, se ei voi lähettää sähköposteja. Agentti on **spesifioitu**, ei universaali.

**CFU-kysymys:** "Jos agentti tarvitsee apua palvelimen diagnostiikkaan, mutta sillä on vain pääsy wikiin, mitä se voi tehdä?"

### Väärinkäsitys 3: "Muisti ja konteksti ovat sama asia"

**Miksi opiskelija näin ajattelee:** Molemmat liittyvät agentin kykyyn muistaa asioita.

**Korjaus:** Ne eivät ole sama asia:
- **Konteksti-ikkuna** on *lyhytaikainen* ja voimassa vain hetken. Se menetetään, kun istunto päätetään.
- **Ulkoinen muisti** on *pitkäaikainen* ja tallennettu tietokantaan. Se säilyy seuraavaa agentin suoritusta varten.

Hyvä agentti käyttää molempia: konteksti-ikkunaa nykyisen tehtävän ymmärtämiseen, ulkoista muistia oppimiseen.

**CFU-kysymys:** "Jos agentti käsittelee asiakasta, jonka ongelman se on ratkaissut aiemmin, mistä se hakee tiedon aiemmasta ratkaisusta? Konteksti-ikkunasta vai ulkoisesta muistista?"

## Opettajavetoiset tehtävät

### Tehtävä 1: Suunnittelusilmukan valinta (20 min)

Näytä opiskelijoille monimutkainen ongelma ja pyydä heitä kuvaamaan, kuinka agentti ratkaisisi sen.

Esimerkki:
> "Agentti saa tehtävän: 'Analysoi tämä tiketti ja anna ratkaisu.' Tiketti sanoo: 'En pysty kirjautumaan tililleni, saan virheen 502.' Mitä agentti tekee?"

Opiskelijoiden pitäisi kuvata:
1. **Havainnoi**: Lue tiketti, tunnista ongelman tyyppi
2. **Suunnittele**: "502 on palvelinvirhe. Tarvitsen palvelimen lokit. Tarvitsen myös tiedot asiakkaasta, hänen laitteestaan ja käyttöjärjestelmästään"
3. **Toimi**: Hae palvelimen lokit, etsi merkintöjä asiakkaan IP-osoitteesta
4. **Tarkkaile**: Löytyikö ongelma? Jos ei, mitä muuta pitäisi kokeilla?

Tämä harjoitus näyttää, että suunnittelu ei ole "taikaa" — se on systemaattinen prosessi.

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

## CFU-kysymykset

1. **Suunnittelu**: "Miksi agentti jaottelee ongelman askeleisiin? Miksi se ei vain kokeile ensimmäistä ideaa?"

2. **Työkalut**: "Jos agentti saa uuden työkalun (esim. mahdollisuuden soittaa asiakkaalle), mitä uusia tehtäviä se voisi tehdä?"

3. **Muisti**: "Mitä eroa on sillä, että agentti muistaa asiakkaan edellisen tilauksen konteksti-ikkunasta verrattuna ulkoiseen muistiin?"

4. **Orkestraattori**: "Kuka tai mikä kontrolloi prosessia? Entä jos orkestraattori epäonnistuu?"

---

## Lisäresurssit

Opiskelijat voivat tutkia oikeita agenttikehyksiä (LangChain, Autogen, Camel), joissa he näkevät, miten nämä komponentit toteutetaan koodissa. Oppitunnilla fokus on kuitenkin **käsitteistössä**, ei koodissa.