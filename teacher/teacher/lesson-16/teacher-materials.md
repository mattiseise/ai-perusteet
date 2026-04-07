# Opettajan materiaalit — Oppitunti 16

## Oppimisen tavoitteet

Oppitunnin lopussa oppilas:

1. **Muistaa ja nimeää** kolme pääkategorioiden (kuva, musiikki, video, koodi)
   erikoistuneet tekoälytyökalut ja niiden pääominaisuudet

2. **Ymmärtää** miten erikoistuneet mallit eroavat teksti-LLM:ista (esim. DALL-E
   on opittu kuvilla, Copilot koodilla) ja miksi ne tuottavat erilaisia tuloksia

3. **Soveltaa** oikeaa tekoälytyökalutyyppiä tosielämän tehtävään (budjetti,
   nopeus, laatu) ja käyttää prompt-tekniikkaa tulosten parantamiseksi

4. **Analysoi** eri työkalujen vahvuuksia ja heikkouksia sekä tekijänoikeus-
   riskejä samassa kategoriassa (esim. miksi Midjourney vs. DALL-E)

5. **Arvioi** eettisiä kysymyksiä: kenen data opetti mallit, kuka omistaa
   generoitua sisältöä, onko oikein korvata ammattilaiset, mitä merkintöjä
   tarvitaan

6. **Luo** itselleen todellisen tuotoksen (kuva, musiikki, video, koodi)
   käyttämällä vähintään yhtä erikoistunutta tekoälytyökalutyyppiä ja
   pohtii sen eettisiä näkökohtia

---

## Yleisiä väärinkäsityksiä ja niiden korjaaminen

### Väärinkäsitys 1: "Kaikki tekoälytyökalut ovat samoja, vain eri nimet"

**Todellisuus:** Fundamentaaliset erot ovat olemassa. DALL-E on opittu kuva-teksti-pareista ja harjoiteltu Microsoftin datalla. Se on konservatiivinen turvallisuuden suhteen ja hylkää kyseenalaisia pyyntöjä. Midjourney on yksityinen malli, joka tunnetaan korkeammasta taiteellisesta laadusta ja toimii Discord-pohjaisessa järjestelmässä. Stable Diffusion on avoin lähdekoodi, jonka voit ajaa paikallisesti, ja se on räätälöitävissä. Nämä tuottavat merkittävästi erilaisia tuloksia. Näytä esimerkkejä.

**Korjaus:** "Kuulet usein 'tekoäly', mutta kyse on hyvin erilaisista malleista. Yrityskulttuurit, koulutusdata ja tavoitteet ovat erilaisia. Siksi sama prompt antaa hyvin erilaisia tuloksia."

---

### Väärinkäsitys 2: "Jos tekoäly tekee jotain kerran, siihen on valmis"

**Todellisuus:** Kuten kaikessa luovassa työssä, ensimmäinen yritys on harvoin paras. Tekoäly vaatii iteraatiota — sinun pitää kokeilla, muuttaa sanoja, yrittää uudelleen.

Oppilas, joka sanoo "Yritin tehdä kuvan, mutta se oli huono, tekoäly on huono" ei ehkä ymmärrä, että hän tarvitsee muuttaa ohjeitaan ja yrittää uudelleen.

**Korjaus:** "Ajattele sitä kuten piirtämistä. Ensimmäinen piirros ei ole täydellinen — editoit sitä, lisäät yksityiskohtia, yrität uudelleen. Sama pätee tekoälyyn. Sinun pitää iteroida."

---

### Väärinkäsitys 3: "Jos minä loin sen tekoälylla, minä omistan sen"

**Todellisuus:** Tekijänoikeus on avoin ja riippuu useasta tekijästä: missä maassa olet (USA vs EU vs Suomi), mitä palveluntuotattaja sanoo ehdoissaan, ja kuka haastaa sinut oikeuteen. Konkreettisesti: OpenAI väittää sinulla olevan oikeus DALL-E-kuvaan, mutta Stability AI:ta on haastaa Getty Images tekijänoikeudenloukkauksesta. Jos kuva näyttää samalta kuin Picasso, se ei ole automaattisesti sinun omaisuutta.

**Korjaus:** "Tekijänoikeus on sekaantunut. Palveluntuotattajat sanovat sinulla olevan oikeus, mutta oikeusjutut käydään. Paras käytäntö: ole konservatiivinen, merkitse 'Made with AI', ja älä myy kuvaa, joka näyttää tunnetun taiteilijan töiltä."

---

### Väärinkäsitys 4: "Tekoäly tuhoaa kaikkien työt, siksi se on paha"

**Todellisuus:** Nämä työkalut muuttavat ammatteja, mutta eivät tuhoa niitä. Historiallisesti valokuva ei tuhonnut maalareita — se muutti heidän työtään. Tietokone ei tuhonnut laskijoita — se muutti heidän työtään. Tekoäly ei tuho ammattilaisia — se muuttaa heidän työtään.

Ammattilaiset, jotka oppivat käyttämään näitä työkaluja, voivat tehdä parempia asioita nopeammin.

**Korjaus:** "Teknologia muuttaa aina ammatteja. Paras keino sopeutua on oppia käyttämään sitä. Ammattilaiset, jotka ymmärtävät tekoälyä, ovat enemmän arvostettuja kuin ne, jotka eivät."

---

### Väärinkäsitys 5: "Video-AI on nyt valmiiksi käytettävää, voin tehdä ammattivideon"

**Todellisuus:** Video-AI on vielä kehitysvaiheessa. Nykytilan rajoitukset:
- Lyhyt (alle 15 sekuntia kohtuullisen hyväksi)
- Epätarkka liikkeissä (kasvot muuttuvat, epäjohdonmukaisuus)
- Ihmiset näyttävät usein väärälle

Ammattilaiset käyttävät sitä:
- Storyboard-visualisointiin
- Konseptin nopeaan testaukseen
- Lyhyisiin pilotteihin

Ei ammattilaistuotantoon ilman merkittävää jälkityötä.

**Korjaus:** "Video kehittyy nopeasti, mutta ymmärrä rajoitukset. Se on nyt työkalu konseptin visualisointiin, ei ammattilaiskorvike."

---

## Opettajan fasilitointiohjeet

### Ennen oppituntia

1. **Testaa tekniikka:** Avaa DALL-E ChatGPT:ssä (tai näytä kuvakaappauksia) ja YouTube-video Runway Gen-3:sta. Jos verkkoyhteys pettää, ole valmis näyttämään etukäteen tallennettuja kuvia tai videoita.

2. **Valmistele demo-promptit:** Kirjoita muutama yksinkertainen prompt, joita käytät demossa (esim. "Robotti istuu kahvilassa juomassa kahvia, modernin kahvilan sisällä, valokuvamainen").

3. **Valmistele "backup-sisältö":** Jos verkkoyhteys pettää, näytä generoituja kuvia, videoita tai esimerkkejä, jotka olet tallentanut etukäteen.

4. **Muista aloittelijan näkökulma:** Monet oppilaistasi eivät ole ikinä käyttäneet näitä työkaluja. Selitä kaikki yksinkertaisesti, ikään kuin selittäisit kaverille.

### Oppitunnin aikana

**Tone:** Hieman innostava, mutta realistinen. "Nämä työkalut ovat vaikuttavia, mutta ne eivät ole magia. Ne ovat työkaluja, kuten kamera tai teksti-editori."

**Interaktio:** Pyydä oppilaita ennustamaan, mitä tapahtuu, ennen kuin näytät
demo:
- "Mitä luulet, mitä DALL-E tekee jos sanotaan..."?
- Näytä, mitä se tekee
- "Olivatko oikeassa? Miksi tai miksi ei?"

**Kysymykset, jotka herätävät ajattelua:**
- "Kuka omistaa tämän kuvan?"
- "Olisiko tämä parempi ammattilaisella?"
- "Voitko myydä tämän?"
- "Mistä tämä data tuli?"
- "Miksi tämä tuotos näyttää erilaiselta?"

### Oppitunnin jälkeen

1. **Kerää oppilas-feedback:** "Mikä oli helppoa? Mikä oli vaikeaa? Mikä oli
   yllättävää?"

2. **Tarkkaa seuraavaa oppituntia:** Jos oppilaat olivat innostuneita, voit
   käyttää enemmän aikaa iteraatioon ja demoon. Jos he olivat uuvuttuneet,
   voit supistaa ja keskittyä pienemmäisiin ryhmiin.

3. **Liitä muihin kurssin osiin:** Vertaa tekoälyn ammattilaisten muutokseen,
   joita käsittelimme aiemmin teoriaosuuksissa.

---

## Arviointivinkit

### Tehtävä 16.1: Vertailutaulukko

**Hyvä vastaus sisältää:**
- Vähintään 3 työkalutyyppiä per kategoria
- Hinta-tiedot oikeat (tai lähellä oikeita)
- Selkeät erot ("Paras" vs "Heikoin puoli" ovat tosiasiallisia, ei "hyvä/huono")
- Oma johtopäätös, joka on perusteltu

**Puutteellinen vastaus:**
- Vain 2 työkalutyyppiä
- Hinnat väärät tai puuttuvat
- Erot ovat yleisiä ("hyvä" vs "huono" tuntematta todellisia eroja)
- Ei omaa johtopäätöstä

**Esimerkki hyvästä "paras puoli" -sarakkeesta:**
| Työkaalu | Paras puoli |
|----------|-------------|
| DALL-E   | Ymmärtää luonnollista kieltä hyvin, integroituna ChatGPT:hen |
| Midjourney | Korkea visuaalinen laatu, taiteellinen tyyli |
| Stable D | Avoin lähdekoodi, paikallinen ajo, räätälöitävä |

### Tehtävä 16.2: Praktinen tuotantohanke

**Hyvä vastaus sisältää:**
- *Todellinen tuotos* (ei "yritän myöhemmin")
- Dokumentoidut promitit (tarkkaan, ei vain "robotti")
- Vähintään 2–3 iteraatiota tai yritysten kokeilu
- Reflektio: mitä toimi, mitä ei

**Puutteellinen vastaus:**
- Tuotosta ei ole näkyvissä
- Promitit ovat epämääräisiä
- Vain yksi yritys (ei iteraatiota)
- Ei reflektiota

**Esimerkki hyvästä dokumentaatiosta:**
```
Käyttämäni promitit:
1. "Robot sitting in modern coffee shop, photorealistic"
   → Tulos: Liian abstrakti
2. "Humanoid robot, metallic silver, sitting at wooden table, drinking from white cup,
    bright daylight through window, photorealistic, detailed"
   → Tulos: Paljon parempi!

Iteraatiot: 3 (DALL-E) vs 1 (Midjourney, koska korkeampi laatu ensimmäisellä)
Johtopäätös: Spesifisyys auttaa, mutta Midjourneyllä tarvitsee vähemmän iteraatiota
```

### Tehtävä 16.3: Etiikan analyysi tai Portfolio

**Hyvä "etiikka-analyysi" sisältää:**
- **Johdanto:** Miksi tämä on relevantti *nyt*
- **Vähintään 2 näkökulmaa** (esim. tekijä vs. teknologia-yritys)
- **Konkrettiset esimerkit** (oikeat tapaukset, kuten Getty vs Stability AI)
- **Oman kannan** (et ole neutraali, olet ottanut kantaa)
- **Lähteet** (esim. oikeusriita-artikkelit, palvelun ehdot)

**Hyvä "portfolio-pala" sisältää:**
- **Tuotos** (todella olemassa, näkyvissä)
- **Tuotoksen kuvaus** (mitä tehtiin, mikä työkalu)
- **Eettinen lausuma** (mitä oikeus-ja etiikkakysymyksiä mietit, merkintä)

**Puutteellinen vastaus (kumpi tahansa):**
- Liian pintataso ("tekoäly on hyvä" / "tekoäly on paha")
- Vain yksi näkökulma
- Ei konkreettisia esimerkkejä
- Ei lähteitä tai hyvin heikko perustelut

---

## Lisätietoa opettajille

### Tekijänoikeusprosessi (mistä johtajat huolissaan)

Kolme suurta oikeusriitaa käynnissä:

1. **Getty Images vs. Stability AI (USA, 2024–):**
   - Väitteet: Stability AI opetti mallia Getty-kuvilla ilman lupaa
   - Status: Käsitteillä
   - Relevantti oppilaalle: "Tämä ei ole teoreettinen, se tapahtuu nyt"

2. **Taiteilijoiden joukkokanteita (USA):**
   - Väitteet: Mallit opittiin tekijänoikeussuojatuista teoksista
   - Oppilaiden kohtele: Monet kuuntajat, eri osapuolet

3. **EU AI Act:**
   - Säädäntö, joka tulee vaikuttamaan, miten malleja koulutaan Euroopassa
   - Oppilaiden kohtele: Säädöstö tulee, se on pian todellisuus

### Ammatilliset muutokset

Tämä on hyvin aiheellinen keskustelu oppitunnille:

- **Graafinen muotoilija:** Voisi käyttää tekoälyä konseptin visualisointiin,
  mutta kilpailu on nyt kovempi. Hyödyllinen ammattilaiselle, mutta vaikea
  aloittelevalle.

- **Säveltäjä/muusikko:** Suno/Udio voivat korvata pienempiä keikkoja (podcast-introt,
  taustamusiikki). Ammattilaiselle ehkä mahdollisuus, aloittelevalle uhka.

- **Junior-ohjelmoija:** Cursor/Copilot voivat tehdä rutiinikoodia. Tämä kiihdyttää
  kokeneiden kehitystä, mutta tekee aloittelevista alempia arvostettuja.

**Nuansointi:** Ei ole "tekoäly tuhoaa ammatteja" vaan "tekoäly muuttaa ammatteja".
Jotkut kärsivät, jotkut hyötyvät. Sopeutuminen on avain.

### Oppilaiden auttaminen, joilla on kulttuurista kiinnostusta

Jotkut oppilaat voivat sanoa "Minä olen taitelija / muusikko, ja pelkään tätä."

Vastaa:
- "Ymmärrän pelkosi. Mutta teknologia muuttaa aina ammatteja."
- "Paras keino on oppia käyttämään näitä työkaluja. Ammattilaiset, jotka ymmärtävät
  tekoälyä, voivat käyttää sitä hyväksi."
- "Johdetko luovaa prosessia (ideointi, kuratoiminen, editointi)? Se on se, jota
  tekoäly ei vielä osaa. Panosta siihen."

---

## Verkkolinkit (opettajille)

### Demot ja palvelut
- DALL-E: https://openai.com/dall-e
- Midjourney: https://www.midjourney.com/
- Stable Diffusion: https://stablediffusionweb.com/ (nopea verkkodemo)
- Suno: https://www.suno.ai/
- Runway: https://www.runwayml.com/
- GitHub Copilot: https://github.com/features/copilot
- Cursor: https://www.cursor.com/

### Oikeustapaukset ja uutiset
- Getty vs Stability AI: Hae "Getty Images Stability AI lawsuit 2024"
- EU AI Act: https://digital-strategy.ec.europa.eu/en/policies/ai-act

### Tekijöiden näkökulma
- Artists for Ethical AI: https://artistsforethicalai.org (esim. petitiot)

### Opettajamateriaali
- OpenAI on tekijät opettajille: https://platform.openai.com/docs (eroaa)

---

## Loppumuistutus

Tämä on oppitunti, jossa teknologia muuttuu nopeasti. Linkit ja hintamallit
saattavat vanhentua muutamassa kuukaudessa. **Ennen oppituntia**, tarkista:
- Ovatko hinnat oikeat?
- Ovatko palvelut vielä olemassa?
- Onko uusia työkaluja?

Muuta materiaalia tarpeen mukaan, mutta pidä perusperiaatteet: oppilaiden
tulee ymmärtää *eri työkaluja ja niiden eroja*, *prosessia iteroimalla*, ja
*eettisiä kysymyksiä*.

Onnea oppitunnistasi!
