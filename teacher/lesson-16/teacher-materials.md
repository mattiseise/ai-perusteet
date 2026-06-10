# Opettajan materiaalit — Oppitunti 16: erikoistuneet tekoälytyökalut

## Oppimisen tavoitteet

Tämän oppitunnin tavoitteena on, että opiskelija ymmärtää, miten **erikoistuneet tekoälytyökalut** eroavat yleisistä tekstimalleista ja miksi oikea työkalu pitää valita tehtävän mukaan. Oppitunnin ydin on, että kuva-, musiikki-, video- ja koodityökalut eivät ole vain saman tekoälyn eri käyttöliittymiä, vaan ne on rakennettu ja koulutettu eri tarkoituksiin.

### Muistaa ja ymmärtää

- Opiskelija osaa nimetä tekoälytyökaluja ainakin seuraavista kategorioista: **kuva**, **musiikki**, **video** ja **koodi**.
- Opiskelija ymmärtää, että erikoistuneet mallit eroavat tekstipohjaisista LLM-malleista koulutusdatan, käyttötarkoituksen ja tuotoksen perusteella.
- Opiskelija ymmärtää, että esimerkiksi kuvamalli on koulutettu kuva- ja tekstiaineistolla, kun taas koodiavustaja on optimoitu ohjelmointityöhön.
- Opiskelija ymmärtää, että sama prompti voi tuottaa hyvin erilaisia tuloksia eri työkaluilla.

### Soveltaa ja analysoida

- Opiskelija osaa valita oikean tekoälytyökalutyypin tosielämän tehtävään, kun valintaan vaikuttavat esimerkiksi **budjetti**, **nopeus**, **laatu** ja **käyttötarkoitus**.
- Opiskelija osaa vertailla saman kategorian työkaluja, esimerkiksi ChatGPT:n kuvanluontia, Midjourneytä ja Stable Diffusionia.
- Opiskelija osaa käyttää promptin tarkentamista ja **iteraatiota** tuotoksen parantamiseen.
- Opiskelija osaa tunnistaa erikoistuneisiin työkaluihin liittyviä tekijänoikeus- ja eettisiä riskejä.

### Luoda ja arvioida

- Opiskelija tuottaa vähintään yhden konkreettisen tuotoksen erikoistuneella tekoälytyökalulla, esimerkiksi kuvan, musiikkipätkän, videoluonnoksen tai koodiavusteisen ratkaisun.
- Opiskelija dokumentoi käyttämänsä promptit ja vähintään muutaman iteraatiokierroksen.
- Opiskelija arvioi oman tuotoksensa laatua, käyttötarkoitusta ja eettisiä kysymyksiä.
- Opiskelija osaa pohtia, kuka hyötyy tekoälytyökalusta, kuka kantaa riskit ja mitä tuotoksen yhteydessä pitäisi merkitä näkyviin.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että erikoistuneet tekoälytyökalut ovat oikeita työvälineitä, eivät taikakoneita. Hyvä lopputulos vaatii oikean työkalun, hyvän promptin, iteraatiota ja eettistä harkintaa.

---

## Pedagoginen lähestymistapa

### Ydinviesti: kaikki tekoälytyökalut eivät ole samanlaisia

Opiskelijat voivat helposti ajatella, että kaikki tekoälytyökalut ovat samaa teknologiaa eri nimillä. Tällä tunnilla tärkeintä on näyttää konkreettisesti, että eri työkalut tuottavat erilaisia tuloksia, koska ne on koulutettu eri aineistoilla ja suunniteltu eri käyttötarkoituksiin.

> **”Tekoäly” ei ole yksi työkalu. Se on joukko erilaisia työkaluja, joilla on eri vahvuudet, rajat ja riskit.**

Korosta opiskelijoille:

- **Kuvatyökalut** sopivat visuaalisten ideoiden, konseptien, kuvitusten ja tyylikokeilujen tekemiseen.
- **Musiikkityökalut** sopivat esimerkiksi demojen, taustamusiikin, ideoinnin ja lyhyiden äänikonseptien tuottamiseen.
- **Videotyökalut** sopivat tällä hetkellä erityisesti ideointiin, storyboardeihin ja lyhyisiin konsepteihin, eivät suoraan valmiiseen ammattilaistuotantoon.
- **Koodityökalut** sopivat ohjelmoinnin tukemiseen, virheiden selittämiseen ja rutiinikoodin nopeuttamiseen, mutta niiden tuotos pitää tarkistaa.

### Erikoistuneet työkalut verrattuna yleiseen tekstimalliin

| Työkalutyyppi | Mihin se on optimoitu? | Esimerkkejä | Opetuksen ydin |
| --- | --- | --- | --- |
| **Kuva** | Kuvan tuottamiseen tekstikuvauksen perusteella. | ChatGPT:n kuvanluonti, Midjourney, Stable Diffusion. | Sama prompti voi tuottaa hyvin erilaisia visuaalisia tuloksia. |
| **Musiikki** | Äänen, laulun, taustan tai musiikkiluonnoksen tuottamiseen. | Suno, Udio. | Nopea ideointi on vahvuus, mutta tekijänoikeus ja alkuperä pitää huomioida. |
| **Video** | Lyhyiden videokonseptien ja liikkuvan kuvan luonnosten tuottamiseen. | Runway, muut videomallit. | Video-AI on vaikuttava mutta vielä rajoittunut erityisesti jatkuvuudessa ja liikkeessä. |
| **Koodi** | Koodin kirjoittamisen, täydentämisen, selittämisen ja virheiden ratkaisemisen tukemiseen. | GitHub Copilot, Cursor. | Työkalu nopeuttaa kehitystä, mutta vastuu koodin toimivuudesta jää ihmiselle. |

**Opettajan huomio:** Työkalujen hinnat, käyttöehdot ja ominaisuudet muuttuvat nopeasti. Tarkista ajankohtaiset tiedot ennen tuntia ja esitä hintatiedot opiskelijoille muuttuvina, ei pysyvinä faktoina.

---

## Työkalukategoriat käytännössä

### Kuvatyökalut

Kuvatyökalut ovat hyvä lähtökohta demolle, koska opiskelijat näkevät tuloksen nopeasti. Näytä sama prompti useammassa työkalussa tai näytä etukäteen tallennetut tulokset. Tavoite ei ole päättää, mikä työkalu on ”paras”, vaan huomata, että eri työkalut painottavat eri asioita.

| Työkalu | Vahvuus | Rajoitus tai huomio |
| --- | --- | --- |
| **ChatGPT:n kuvanluonti** | Ymmärtää luonnollista kieltä hyvin ja toimii samassa keskustelussa muun työskentelyn kanssa. | Turvarajaukset voivat estää joitakin pyyntöjä. |
| **Midjourney** | Usein vahva taiteellisessa laadussa ja visuaalisessa tyylissä. | Käyttöliittymä ja työnkulku voivat olla aloittelijalle vieraampia. |
| **Stable Diffusion** | Avoin, muokattava ja mahdollinen ajaa paikallisesti. | Vaatii enemmän teknistä osaamista, jos sitä käytetään paikallisesti tai räätälöidään. |

### Musiikkityökalut

Musiikkityökalut herättävät usein vahvoja reaktioita, koska ne koskevat luovaa työtä, tekijyyttä ja muusikoiden toimeentuloa. Pidä keskustelu tasapainossa: työkalut voivat olla hyödyllisiä ideointiin, mutta niihin liittyy eettisiä ja tekijänoikeudellisia kysymyksiä.

- **Hyödyllisiä käyttötapoja:** demo, taustamusiikin luonnos, podcastin tunnusmusiikki, ideointi.
- **Riskejä:** koulutusdatan alkuperä, artistien työn käyttö, kaupallinen käyttö ja tuotoksen merkitseminen.
- **Opetuksen painotus:** opiskelija ei vain tuota musiikkia, vaan pohtii, mistä malli on oppinut ja miten tuotosta saa käyttää.

### Videotyökalut

Video-AI on opiskelijoiden mielestä usein vaikuttavaa, mutta juuri siksi rajoitukset pitää sanoittaa selkeästi. Tällä hetkellä videomallit sopivat erityisesti konseptien visualisointiin, eivät aina suoraan viimeisteltyyn tuotantoon.

> **Video-AI on vahva ideoinnissa ja konseptoinnissa, mutta se ei vielä automaattisesti korvaa ammattimaista videotuotantoa.**

Korosta erityisesti seuraavia rajoituksia:

- videot ovat usein lyhyitä
- liike voi olla epäjohdonmukaista
- kasvot, kädet ja yksityiskohdat voivat muuttua
- sama hahmo ei välttämättä pysy samanlaisena koko videon ajan
- ammattikäyttö vaatii usein jälkityötä

### Koodityökalut

Koodityökalut, kuten Copilot ja Cursor, voivat nopeuttaa ohjelmointia merkittävästi. Opiskelijoille pitää kuitenkin tehdä selväksi, että koodiavustajan ehdotus ei ole automaattisesti oikein, turvallinen tai ymmärretty.

Hyvä opetusnäkökulma on: koodityökalu voi olla erinomainen työpari, mutta opiskelijan pitää edelleen ymmärtää, mitä koodi tekee.

- **Hyvä käyttötapa:** pyydä selitystä, vaihtoehtoja, testejä ja virheen paikannusta.
- **Huono käyttötapa:** hyväksy koodi suoraan ymmärtämättä sitä.
- **Ammatillinen taito:** tarkista, testaa ja dokumentoi tekoälyn ehdottama koodi.

---

## Iteraatio ja promptien parantaminen

### Ensimmäinen yritys ei yleensä ole paras

Erikoistuneissa luovissa työkaluissa iteraatio on keskeinen taito. Opiskelijan pitää ymmärtää, että huono ensimmäinen tulos ei tarkoita, että työkalu on hyödytön. Se tarkoittaa usein, että promptia pitää tarkentaa.

**Prompt 1:** Robot sitting in modern coffee shop, photorealistic.

**Havainto:** Tulos voi olla liian yleinen tai abstrakti.

**Prompt 2:** Humanoid robot, metallic silver, sitting at a wooden table, holding a white coffee cup, bright daylight through the window, realistic café interior, photorealistic, detailed.

**Havainto:** Tarkempi kuvaus ohjaa mallia paremmin.

Ohjaa opiskelijoita dokumentoimaan jokainen yritys:

- Mikä prompti annettiin?
- Mikä tuloksessa onnistui?
- Mikä ei onnistunut?
- Mitä muutettiin seuraavaan promptiin?
- Miten muutos vaikutti lopputulokseen?

---

## Eettiset ja tekijänoikeudelliset kysymykset

### Miksi etiikka kuuluu tähän tuntiin?

Erikoistuneet tekoälytyökalut liittyvät vahvasti luovaan työhön. Siksi oppitunti ei voi olla pelkkää työkalujen kokeilua. Opiskelijan pitää myös pohtia, kenen datalla malli on koulutettu, kuka omistaa tuotoksen, miten tuotosta saa käyttää ja miten tekoälyn käyttö pitäisi merkitä.

| Kysymys | Miksi se on tärkeä? | Opiskelijan pitäisi pohtia |
| --- | --- | --- |
| **Kenen datalla malli on koulutettu?** | Mallin laatu perustuu ihmisten tuottamaan aineistoon. | Oliko tekijöillä lupa, korvaus tai mahdollisuus vaikuttaa käyttöön? |
| **Kuka omistaa tuotoksen?** | Tekijänoikeustilanne voi riippua palvelun ehdoista ja lainsäädännöstä. | Saako tuotosta käyttää koulussa, somessa, portfoliossa tai kaupallisesti? |
| **Korvaako työkalu ammattilaisen?** | Työkalut muuttavat luovia ammatteja ja työn arvoa. | Mitä tehtäviä työkalu helpottaa ja missä ihmisen asiantuntemus on edelleen ratkaisevaa? |
| **Pitääkö tekoälyn käyttö merkitä?** | Läpinäkyvyys lisää luottamusta. | Milloin tuotokseen pitäisi lisätä merkintä, kuten ”tehty tekoälyn avulla”? |

**Opettajan huomio:** Tekijänoikeus on osittain avoin ja muuttuva alue. Älä esitä keskeneräisiä oikeustapauksia lopullisesti ratkaistuina. Opeta opiskelijoille varovainen ja vastuullinen toimintatapa: tarkista palvelun ehdot, merkitse tekoälyn käyttö ja vältä tunnetun taiteilijan tyylin jäljittelyä kaupallisessa käytössä.

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”Kaikki tekoälytyökalut ovat samoja, vain eri nimillä.”

**Korjaava näkökulma:** Eri työkalut on koulutettu eri aineistoilla ja suunniteltu eri tarkoituksiin. ChatGPT:n kuvanluonti, Midjourney ja Stable Diffusion voivat kaikki tuottaa kuvia, mutta niiden tyyli, käyttöliittymä, rajaukset, muokattavuus ja tulokset eroavat toisistaan.

### Väärinkäsitys 2: ”Jos tekoäly tekee huonon tuloksen kerran, työkalu on huono.”

**Korjaava näkökulma:** Ensimmäinen tulos on harvoin paras. Promptia pitää tarkentaa, yksityiskohtia lisätä ja tuotosta iteroida. Tämä kuuluu luovaan työskentelyyn.

### Väärinkäsitys 3: ”Jos minä loin sen tekoälyllä, minä omistan sen automaattisesti täysin.”

**Korjaava näkökulma:** Tekijänoikeus riippuu palvelun ehdoista, lainsäädännöstä, käyttötarkoituksesta ja siitä, muistuttaako tuotos vahvasti jonkun toisen teosta. Turvallinen toimintatapa on tarkistaa ehdot, käyttää omaa luovaa panosta ja merkitä tekoälyn käyttö läpinäkyvästi.

### Väärinkäsitys 4: ”Tekoäly tuhoaa kaikki luovat ammatit.”

**Korjaava näkökulma:** Tekoäly muuttaa ammatteja, mutta ei yksinkertaisesti poista kaikkea ihmistyötä. Ammattilaisen työ voi siirtyä enemmän ideointiin, ohjaamiseen, kuratointiin, editointiin ja laadun arviointiin.

### Väärinkäsitys 5: ”Video-AI on nyt valmis korvaamaan ammattivideotuotannon.”

**Korjaava näkökulma:** Video-AI on kehittyvä ja vaikuttava työkalu, mutta siinä on edelleen rajoituksia esimerkiksi jatkuvuudessa, liikkeessä, kasvoissa ja yksityiskohdissa. Se sopii hyvin konseptien visualisointiin ja lyhyisiin kokeiluihin, mutta ammattituotanto vaatii usein ihmisen ohjausta ja jälkityötä.

---

## Opettajan fasilitointiohjeet

### Ennen oppituntia

1. **Testaa tekniikka:** varmista, että valitsemasi kuvageneraattori, videoesimerkki tai muu demo toimii luokkatilanteessa.
2. **Valmistele demo-promptit:** kirjoita 2–3 promptia, joita voit käyttää live-demossa tai näyttää tallennettuina tuloksina.
3. **Tallenna varamateriaali:** ota mukaan etukäteen tallennettuja kuvia, videoita tai kuvakaappauksia siltä varalta, että verkkoyhteys tai palvelu ei toimi.
4. **Tarkista ajankohtaiset tiedot:** hinnat, käyttöehdot ja saatavuus voivat muuttua nopeasti.
5. **Valmistele eettinen keskustelukysymys:** esimerkiksi ”Voisitko käyttää tätä kuvaa yrityksen mainoksessa?” tai ”Pitäisikö tekoälyn käyttö merkitä portfolioon?”

### Lähiosan rakenne, 90 minuuttia

| Vaihe | Aika | Tavoite |
| --- | --- | --- |
| **Johdanto** | 10 min | Avaa ajatus: eri tekoälytyökalut on suunniteltu eri tehtäviin. |
| **Demo: sama prompti eri työkaluille** | 20 min | Näytä, miten työkalujen erot näkyvät käytännössä. |
| **Tehtävä 16.1: vertailutaulukko** | 20 min | Opiskelijat vertailevat työkaluja kategorian, hinnan, vahvuuksien ja rajoitusten perusteella. |
| **Tehtävä 16.2: tuotoksen tekeminen** | 25 min | Opiskelijat tekevät oman tuotoksen ja dokumentoivat promptit sekä iteraatiot. |
| **Tehtävä 16.3: etiikan pohdinta** | 10 min | Keskustellaan tuotoksen käytöstä, omistajuudesta ja merkitsemisestä. |
| **Yhteenveto** | 5 min | Kokoa ydin: oikea työkalu, iterointi ja vastuullinen käyttö. |

### Johdantolause opettajalle

> Tänään emme puhu tekoälystä yhtenä työkaluna. Katsomme, miten erilaiset tekoälytyökalut tuottavat kuvia, musiikkia, videoita ja koodia — ja miksi oikea työkalu valitaan aina tehtävän mukaan.

---

## Luokkatehtävien ohjeistus

### TT-A: Vertailutaulukko

**Tavoite:** Opiskelija oppii vertailemaan erikoistuneita tekoälytyökaluja tehtävän, hinnan, vahvuuksien ja rajoitusten perusteella.

**Tehtävä:** Valitse vähintään kolme tekoälytyökalua samasta kategoriasta tai eri kategorioista. Täytä vertailutaulukko ja kirjoita lyhyt johtopäätös siitä, mihin tilanteeseen kukin työkalu sopii.

| Työkalu | Kategoria | Paras puoli | Heikoin puoli tai riski | Sopiva käyttötarkoitus |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

**Hyvä johtopäätös vastaa:**

- Mikä työkalu sopii nopeaan ideointiin?
- Mikä työkalu sopii laadukkaampaan lopputulokseen?
- Mikä työkalu vaatii eniten teknistä osaamista?
- Mitä eettisiä tai tekijänoikeudellisia riskejä pitää huomioida?

**Aika-arvio:** 20 minuuttia

---

### TT-B: Oma tuotantohanke

**Tavoite:** Opiskelija tekee oikean tuotoksen erikoistuneella tekoälytyökalulla ja dokumentoi prosessinsa.

**Tehtävä:** Tee tekoälyn avulla yksi konkreettinen tuotos: kuva, lyhyt musiikkiluonnos, videokonsepti tai koodiavusteinen ratkaisu. Dokumentoi promptit ja vähintään kaksi iteraatiota.

**Tee näin:**

1. Valitse työkalu ja tuotostyyppi.
2. Kirjoita ensimmäinen prompti.
3. Tallenna tulos tai kuvaile se tarkasti.
4. Muuta promptia ja tee uusi yritys.
5. Dokumentoi, mikä muuttui ja miksi.
6. Kirjoita lyhyt reflektio: mikä onnistui, mikä ei ja mitä tekisit seuraavaksi?

| Iteraatio | Prompti | Tulos | Mitä muutin seuraavaksi? |
| --- | --- | --- | --- |
| **1** |  |  |  |
| **2** |  |  |  |
| **3** |  |  |  |

**Aika-arvio:** 25 minuuttia

---

### TT-C: Etiikka-analyysi tai portfolio-merkintä

**Tavoite:** Opiskelija pohtii tekoälytuotoksen käyttöä, tekijyyttä ja läpinäkyvyyttä.

**Tehtävä:** Valitse toinen vaihtoehto:

1. **Etiikka-analyysi:** kirjoita lyhyt analyysi tekoälytuotoksen eettisistä kysymyksistä.
2. **Portfolio-merkintä:** esittele oma tuotoksesi ja kirjoita sen yhteyteen lyhyt eettinen lausuma.

**Hyvä etiikka-analyysi sisältää:**

- miksi aihe on ajankohtainen
- vähintään kaksi näkökulmaa, esimerkiksi käyttäjä, tekijä, yritys tai ammattilainen
- konkreettisen esimerkin
- oman perustellun kannan
- maininnan siitä, miten tekoälyn käyttö pitäisi merkitä

**Hyvä portfolio-merkintä sisältää:**

- tuotoksen tai sen kuvauksen
- käytetyn työkalun
- keskeiset promptit tai prosessin kuvauksen
- eettisen lausuman, esimerkiksi: ”Tämä tuotos on tehty tekoälyn avulla. Käytin tekoälyä ideointiin ja kuvan luomiseen, mutta valitsin lopullisen version itse.”

**Aika-arvio:** 15–20 minuuttia

---

## Arviointivinkit

### Tehtävä 16.1: Vertailutaulukko

**Hyvä vastaus sisältää:**

- vähintään kolme työkalua tai työkalutyyppiä
- selkeät erot työkalujen vahvuuksissa ja rajoituksissa
- ajantasaiset tai ainakin tarkistettavaksi merkityt hintatiedot
- oman johtopäätöksen, joka on perusteltu
- eettisen tai tekijänoikeudellisen huomion

**Puutteellinen vastaus näyttää tältä:**

- työkaluja on liian vähän
- erot jäävät tasolle ”hyvä” ja ”huono”
- hinnat, käyttöehdot tai rajoitukset puuttuvat
- oma johtopäätös puuttuu

### Tehtävä 16.2: Tuotantohanke

**Hyvä vastaus sisältää:**

- todellisen tuotoksen tai selkeästi dokumentoidun kokeilun
- tarkat promptit
- vähintään 2–3 iteraatiota tai perustellun kokeilukierroksen
- reflektion siitä, mikä toimi ja mikä ei
- maininnan siitä, miten tuotosta voisi käyttää vastuullisesti

**Puutteellinen vastaus näyttää tältä:**

- tuotosta ei ole
- promptit ovat epämääräisiä
- vain yksi yritys eikä iteraatiota
- ei pohdintaa tuotoksen laadusta tai eettisistä kysymyksistä

### Tehtävä 16.3: Etiikka-analyysi tai portfolio

**Hyvä vastaus sisältää:**

- selkeän kannanoton, ei pelkkää yleistä toteamusta
- vähintään kaksi näkökulmaa
- konkreettisen esimerkin
- pohdinnan tekijänoikeudesta, läpinäkyvyydestä tai työn muutoksesta
- merkinnän siitä, miten tekoälyn käyttö kerrotaan muille

**Puutteellinen vastaus näyttää tältä:**

- ”tekoäly on hyvä” tai ”tekoäly on paha” ilman perustelua
- vain yksi näkökulma
- ei esimerkkejä
- ei omaa kantaa
- ei mainintaa tekoälyn käytön merkitsemisestä

**Opettajan arviointikysymys:** Näkyykö opiskelijan työssä vain työkalun kokeilu vai myös ymmärrys siitä, miksi juuri tämä työkalu valittiin, miten tulosta parannettiin ja mitä eettisiä seurauksia käyttöön liittyy?

---

## Yleisiä vaikeuksia ja vastaamisen strategiat

| Vaikeus | Miten ohjaat? |
| --- | --- |
| Opiskelija ajattelee, että kaikki työkalut ovat samoja. | Näytä sama prompti eri työkaluilla. Pyydä opiskelijaa vertaamaan tyyliä, laatua, rajauksia ja käyttökokemusta. |
| Opiskelija luovuttaa ensimmäisen huonon tuloksen jälkeen. | Korosta iteraatiota. Pyydä lisäämään promptiin tarkempi kohde, tyyli, ympäristö, valaistus, käyttötarkoitus tai rajoitus. |
| Opiskelija olettaa omistavansa tuotoksen täysin. | Ohjaa tarkistamaan palvelun ehdot ja pohtimaan, saako tuotosta käyttää koulussa, somessa, portfoliossa tai kaupallisesti. |
| Opiskelija pelkää tekoälyn vievän luovat työt. | Tunnista huoli ja ohjaa keskustelu siihen, miten ammattilaisen työ muuttuu: ideointi, ohjaaminen, editointi ja laadun arviointi korostuvat. |
| Opiskelija yliarvioi video-AI:n valmiuden. | Näytä rajoitukset konkreettisesti: lyhyt kesto, liikkeen epäjohdonmukaisuus ja hahmojen muuttuminen. |

---

## Eriyttäminen ja tuki

### Jos opiskelija tarvitsee tukea

- Anna valmiit työkaluvaihtoehdot ja pyydä vertaamaan vain kahta työkalua.
- Anna valmiit promptipohjat, joita opiskelija voi muokata.
- Anna mahdollisuus käyttää opettajan valmiiksi tuottamia esimerkkikuvia, jos työkaluihin kirjautuminen ei onnistu.
- Ohjaa opiskelija dokumentoimaan vain kaksi iteraatiota, jos tehtävä tuntuu liian laajalta.

### Jos opiskelija on edellä

- Pyydä vertaamaan samaa promptia kolmessa eri kuvamallissa.
- Pyydä tekemään sama konsepti kahdessa eri muodossa, esimerkiksi kuvana ja lyhyenä videokonseptina.
- Pyydä kirjoittamaan vahvempi etiikka-analyysi, jossa on useampi näkökulma.
- Pyydä arvioimaan, miten työkalun käyttö muuttaisi jonkin ammattilaisen työnkulkua.

---

## Oppimisresurssit opettajalle

### Demot ja palvelut

- **ChatGPT:n kuvanluonti:** kuvan tuottaminen tekstistä.
- **Midjourney:** visuaalisesti vahvat ja tyylitellyt kuvat.
- **Stable Diffusion:** avoimempi ja muokattavampi kuvamallien ekosysteemi.
- **Suno ja Udio:** musiikin ja laulun tuottaminen.
- **Runway:** videon generointi ja videokonseptien kokeilu.
- **GitHub Copilot ja Cursor:** ohjelmoinnin ja koodityön avustaminen.

### Keskustelun tueksi

- Tekijänoikeus ja koulutusdata.
- Palveluiden käyttöehdot ja kaupallinen käyttö.
- Tekoälyn käytön merkitseminen portfolioon tai julkaisuun.
- Luovien alojen työn muutos.
- Ammattilaisen rooli: ideointi, kuratointi, editointi, laadunvarmistus ja vastuu.

---

## Yhteys aiempiin ja tuleviin oppitunteihin

- **Aiemmin:** opiskelijat ovat oppineet valitsemaan tekoälytyökaluja tehtävän, kontekstin ja tietosuojan perusteella.
- **Tällä tunnilla:** opiskelijat soveltavat samaa ajattelua erikoistuneisiin luoviin ja teknisiin työkaluihin.
- **Seuraavaksi:** opiskelijat voivat hyödyntää erikoistuneita työkaluja omissa projekteissaan, boteissaan ja portfoliotöissään.

**Opettajan muistutus:** Tämän tunnin jälkeen opiskelijan pitäisi osata sanoa: ”En valitse tekoälytyökalua vain siksi, että se on tunnettu. Valitsen sen siksi, että se sopii juuri tähän tuotokseen, tähän käyttötarkoitukseen ja näihin eettisiin reunaehtoihin.”

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että erikoistuneet tekoälytyökalut ovat voimakkaita mutta rajallisia työvälineitä. Niiden käyttö vaatii oikean työkalun valintaa, hyvää promptausta, iterointia, tulosten arviointia ja vastuullista suhtautumista tekijyyteen sekä datan alkuperään.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Kun valitset tekoälytyökalun kuvan, musiikin, videon tai koodin tekemiseen, mitkä kolme asiaa tarkistat ennen kuin päätät käyttää sitä?

> **Lopetuslause opettajalle:** Tekoälytyökalu ei tee sinusta ammattilaista. Ammattilaiseksi tekee se, että osaat valita työkalun, ohjata sitä, arvioida tulosta ja kantaa vastuun sen käytöstä.

---
