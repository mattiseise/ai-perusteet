# Opiskelutehtävät: Bottiprojekti, osa 2 — testaa ja esittele

## Tekoälyjen käyttö -osion arvioitava projekti (osa 2/2)

Tämä on Tekoälyjen käyttö -osion arvioitavan projektin toinen osa. Oppitunnilla 17 suunnittelit ja rakensit botin — nyt viimeistelet sen, testaat reunatapaukset ja esittelet tuloksen. Muista käyttää kaikkia neljää rakennuspalaa (oppitunnit 10, 12, 14 ja 16) työssäsi.

---

## Tehtävä 18.1: Viimeistele botti — testaa rajaukset ja reunatapaukset (20 min)

### Tavoite

Varmistaa, että botti toimii johdonmukaisesti erilaisissa tilanteissa ja että sen rajaukset ovat selkeät.

### Ohjeet

1. Avaa bottiasi ja lue sen system prompt uudelleen. Kirjoita muistiin, mitä rajoituksia sillä on — mihin aiheisiin se vastaa ja mihin ei? (Rakennuspala 4 kertoo vastuullisesta käytöstä ja eettisyydestä.)

2. **Testaa positiivisia tapauksia** (3–4 kappaletta):
   - Esitä botille projektista kolme tai neljä järkevää kysymystä, kuten todelliset käyttäjät tekisivät.
   - Dokumentoi, vastasiko botti oikein ja oliko vastaus hyödyllinen.

3. **Testaa negatiivisia ja reunatapauksia** (3–4 kappaletta):
   - Kirjoita tyhjä viesti tai yksittäinen sana ("no", "kyllä")
   - Kysy botilta asiasta, joka ei liity projekteihin (esim. "Kerro vitsi" tai "Opeta minua ruoanlaittoon")
   - Esitä sekava mutta epäselvä kysymys
   - Dokumentoi, kieltäytyikö botti asianmukaisesti vai yrittikö se vastata. Testaa, noudattiko se rakennuspalan 4 rajauksia.

4. **Paranna system promptia** tarvittaessa:
   - Jos botti epäonnistui joissain testeissä, muokkaa system promptia ja testaa uudelleen
   - Dokumentoi muutokset: mikä meni pieleen ja miten korjasit
   - Päivitä viittaukset rakennuspalaan 4 (vastuullinen käyttö)

5. **Dokumentoi tulokset** pieneen taulukkoon:
   ```
   Testi: [kuvaus]
   Odotus: [mitä haluat tapahtua]
   Tulos: [mitä tapahtui]
   Status: ✓ ONNISTUI / ✗ EPÄONNISTUI
   Rakennuspala: [1, 2, 3 vai 4]
   ```

---

## Tehtävä 18.2: Valmistele esittely — kirjoita kuvaus ja käsikirjoitus (20 min)

### Tavoite

Kirjoittaa lyhyt, vakuuttava kuvaus botista ja valmistella sen esittelyä varten. Varmista, että esittelyssä näkyvät kaikki neljä rakennuspalaa.

### Ohjeet

1. **Kirjoita botin kuvaus** (3–4 virkettä):
   - Mitä botti tekee? (Rakennuspala 1)
   - Kenelle se on hyödyllinen?
   - Miksi se on parempi kuin muut tavat dokumentoida projekteja?

   *Esimerkki:* "Projektidokumenttibotti on custom GPT, joka kyselee sinulta projektista (rakennuspala 2), omaa roolinsa mentorina (rakennuspala 3) ja luo siitä automaattisesti strukturoidun suunnitelman turvallisesti (rakennuspala 4). Perinteisesti projektien dokumentointi on käsityötä — botti automatisoi prosessia, säästää aikaa ja varmistaa, että mitään oleellista ei unohdu."

2. **Suunnittele esittelykäsikirjoitus**:
   - Valitse yksi realistinen projektiskenaario (esim. "Verkkosivuston rakentaminen pienelle kaupalle")
   - Mitkä ovat botin neljä tai viisi ensimmäistä kysymystä projektista? (Perusta rakennuspalaan 2)
   - Kirjoita lyhyet vastaukset, joita käytät livedemoissa
   - Lisää muistiinpanot: missä kohdassa haluat pysäyttää videon, näyttää dokumenttia jne.

3. **Testaa esittely**:
   - Avaa botti ja suorita livedemo kerran, missä kysyt ja vastaat omien muistiinpanojen perusteella
   - Mittaa aika — kuinka kauan menee? (Tavoite: ~5–7 minuuttia koko demosta)
   - Merkitse kohdat, joissa botti vastaa nopeasti ja kohdat, joissa se hidastuu

4. **Dokumentoi** esittelykäsikirjoitus ja aikarajoitukset:
   - Tallenna käsikirjoitus tekstidokumenttiin
   - Kirjoita: "Esittely kestää noin X minuuttia. Botin vastauksiin kuluu Y sekuntia."
   - Viittaa rakennuspalain 1–4 siinä, missä ne näkyvät esittelyssä

---

## Tehtävä 18.3: Esittele botti ryhmälle — livedemo + vertaisarviointi (30 min)

### Tavoite

Esitellä botti muille opiskelijoille ja vastaanottaa sekä antaa rakentavaa palautetta.

### Ohjeet

Tämä tehtävä on luokkahuoneessa tai virtuaalisesti. Kaikki opiskelijat esittelevät bottinsa peräkkäin.

**Esittely (3–4 min per opiskelijalle):**
- Kerro ensin lyhyesti, mitä botti tekee (käytä tehtävän 18.2 kuvausta — sisältää rakennuspalat 1–4)
- Suorita livedemo: avaa botti, esitä kysymyksiä, näytä, kuinka se generoi dokumenttia
- Anna muille hetki lukea lopullista dokumenttia

**Vertaisarviointi (2 min):**
- Kun toinen opiskelija esittelee, kirjoita muistiinpanot:
  - Mikä oli hyvää?
  - Mikä voisi olla paremmin?
  - Mikä oli yllättävää tai mielenkiintoista?

- Kun on sinun vuorosi vastaanottaa palautetta, kuuntele muiden kommentit
- Kirjoita alas kaikki muiden palautteet ja ehdotukset

**Arviointikaavake (jokaisen botin osalta):**
```
Oppilaan nimi: [nimi]
Botin tarkoitus: [mitä se tekee]

Vahvuudet:
- [positiivinen havainto 1]
- [positiivinen havainto 2]

Kehitettävää:
- [parannusidea 1]
- [parannusidea 2]

Yleinen kommentti:
[1–2 virkettä]

Rakennuspalat (1–4):
- Näkyivätkö kaikki neljä rakennuspalaa esittelyssä?
```

---

## Tehtävä 18.4: Kirjoita reflektio — mitä opit, mitä tekisit toisin (20 min)

### Tavoite

Pohtia omaa oppimisprosessiasi ja osoittaa ymmärrystä siitä, miten botti saisi kehittyä agentiksi. Arvioida myös, kuinka hyvin integroit neljä rakennuspalaa.

### Ohjeet

Kirjoita lyhyt reflektio (300–400 sanaa) seuraavista aiheista:

1. **Oppiminen:** Mitä opit rakentamalla bottiasi? Mitkä asiat olivat vaikeita? Mitkä tulivat helposti? Miten rakennuspalat (10, 12, 14, 16) auttoivat prosessissa?

2. **Iterointi:** Mistä ongelmista törmäsit testauksessa? Kuinka korjasit ne? Entä jos sinulla olisi ollut enemmän aikaa — mitä tekisit toisin? Muuttaisitko rakennuspaloja?

3. **Esittely:** Kuinka livedemo meni? Mitä sait muilta palautetta? Oletko samaa mieltä palautteen kanssa? Näytyikö esittelyssä kaikki neljä rakennuspalaa?

4. **Silta agenteihin:** Nyt botti vain kuuntelee sinua. Mitä agentti tekisi toisin? Mitä uusia ominaisuuksia se voisi saada? (Esim. agentti saattaisi automaattisesti lähettää dokumentin sähköpostiin tai tallentaa sen pilveen.)

### Odotettu tuotos

Tekstitiedosto, joka on noin 300–400 sanaa. Kirjoita omilla sanoillasi, älä jäljitele tehtävän kuvausta. Opettaja haluaa kuulla sinua, ei tehtävänasettelua. **Viittaa rakennuspalain 1–4 omassa tekstissäsi.**

---

## Arviointikriteerit (koko oppitunnit 17 ja 18, yhteensä 20 pistettä)

Koko "Bottiprojekti" -arviointitehtävä kattaa sekä L17:n rakentamisen että L18:n viimeistelyt ja esittelyn. Arvioidaan seuraavilla kriteereillä:

### 1. Botin suunnittelu ja tarkoitus (4 pistettä)

**Erinomainen (4 p):** Botin tarkoitus on kristallin kirkas ja perustuu rakennuspalaan 1. System prompt on selkeä ja johdattaa bottia johdonmukaisesti. Kysymykset ovat relevantteja, rakentuu rakennuspalasta 2 ja rakentavat realistisen kuvan projektista. Botti tekee tarkalleen, mitä se on suunniteltu tekemään.

**Hyvä (3 p):** Tarkoitus on selkeä ja perustuu rakennuspalaan 1. System prompt toimii hyvin. Kysymykset ovat pääosin hyviä rakennuspalasta 2, vaikka yksi tai kaksi voisi olla tarkempi.

**Tyydyttävä (2 p):** Tarkoitus on enemmän tai vähemmän selkeä. System prompt on olemassa, mutta vaikea seurata. Kysymykset ovat ok, mutta satunnaisia. Rakennuspalat näkyvät vain osittain.

**Välttävä (1 p):** Tarkoitus on epäselvä tai puutteellinen. Kysymykset ovat sekavia tai epärelevantit. Bottia ei ymmärrä tai se ei tee mitään järkevää. Rakennuspalat eivät näy työssä.

### 2. System prompt ja ohjeet (4 pistettä)

**Erinomainen (4 p):** System prompt on kirjoitettu hyvin, selkeä ja johdonmukainen. Sisältää kaikki neljä rakennuspalaa (1: tarkoitus, 2: kontekstin kerääminen, 3: rooli ja persoonallisuus, 4: rajaukset). Botti ymmärtää roolinsa ja noudattaa ohjeita.

**Hyvä (3 p):** System prompt on hyvä ja pääosin toimii. Sisältää useimmat rakennuspalat. Pieni epäselvyys tai epäjohdonmukaisuus ei haittaa.

**Tyydyttävä (2 p):** System prompt on olemassa ja toimii yleensä. Sisältää joitain rakennuspaloja, mutta voisi olla täydellisempi. Selkeyttä voisi parantaa.

**Välttävä (1 p):** System prompt on epäselvä, puutteellinen tai johtaa bottia väärin. Rakennuspalat puuttuvat tai niistä on vain heikot viittaukset.

### 3. Testaus ja iterointi (4 pistettä)

**Erinomainen (4 p):** Botti on testattu perusteellisesti positiivisissa, negatiivisissa ja reunatapauksissa. Testit dokumentoivat myös, miten rakennuspalat (erityisesti 2 ja 4) näkyvät testeissä. Kaikki testit on dokumentoitu selvästi. Virheet löydettiin ja korjattiin.

**Hyvä (3 p):** Botti on testattu hyvin. Useimmat testit dokumentoitu. Ongelmia korjattiin. Rakennuspalat näkyvät testeissä.

**Tyydyttävä (2 p):** Botti on testattu jonkin verran. Dokumentaatio on olemassa, mutta puutteellinen. Joitain ongelmia korjattiin. Rakennuspalat näkyvät osittain.

**Välttävä (1 p):** Testaus on minimaalista. Dokumentaatio on heikko. Bottia ei ole testattu tai testaus ei ole dokumentoitu. Rakennuspalat eivät näy testauksessa.

### 4. Esittely ja viestintä (4 pistettä)

**Erinomainen (4 p):** Opiskelija selittää bottiaan selkeästi ja vakuuttavasti. Esittelystä näkyvät kaikki neljä rakennuspalaa. Livedemo sujuu hyvin. Muille on selvää, mitä botti tekee ja miksi se on hyödyllinen.

**Hyvä (3 p):** Selitys on hyvä ja livedemo onnistuu pääosin. Useimmat rakennuspalat näkyvät. Ihmiset ymmärtävät botin tarkoituksen.

**Tyydyttävä (2 p):** Selitys on ok ja livedemo onnistuu. Joitain epäselvyyksiä. Jotkut rakennuspalat näkyvät.

**Välttävä (1 p):** Selitys on epäselvä tai livedemo ei onnistu hyvin. Selitys on sekava tai esittelyä ei ole. Rakennuspalat eivät näy esittelyssä.

### 5. Reflektio ja oppiminen (4 pistettä)

**Erinomainen (4 p):** Reflektio on syvä ja pohtiva. Opiskelija osoittaa ymmärtävänsä omaa oppimistaan, iteroinnin merkitystä ja sitä, kuinka botti voisi kehittyä. Viittaa selkeästi rakennuspalain 1–4 omassa pohdinnassaan. Ehdotukset agentin ominaisuuksista ovat intelligentit.

**Hyvä (3 p):** Reflektio on hyvä. Opiskelija pohtii oppimistaan ja kehitysideoitaan. Viittaa rakennuspalain joihin. Ymmärrys näkyy selvästi.

**Tyydyttävä (2 p):** Reflektio on olemassa ja käsittelee aihetta. Mainitsee rakennuspaloja, mutta voisi olla syvempi.

**Välttävä (1 p):** Reflektio on pinnallinen tai epäselvä. Viittaukset rakennuspalain puuttuvat. Reflektio puuttuu tai ei ole yhteydessä tehtävään.

---

## Palautusvaatimukset

Palauta seuraavat dokumentit:

1. **Testausdokumentti** (tehtävä 18.1)
   - Taulukko testeistä (positiiviset, negatiiviset, reunatapaukset)
   - Viittaukset rakennuspalain niihin (erityisesti rakennuspala 4)
   - Muutokset system promptiin, jos tehtiin
   - ~1 sivu

2. **Esittelykäsikirjoitus** (tehtävä 18.2)
   - Botin kuvaus (3–4 virkettä) — sisältää rakennuspalat 1–4
   - Käsikirjoitus livedemolle (projektiskenaario ja muistiinpanot)
   - Aikarajoitus
   - ~1 sivu

3. **Vertaisarvioinnit** (tehtävä 18.3)
   - Arviointikaavakkeet jokaisesta esitellystä botista (muista kuin omasta)
   - Huomiot rakennuspalain näkyvyydestä
   - 2–3 arvioita

4. **Reflektio** (tehtävä 18.4)
   - 300–400 sanainen teksti
   - Viittaukset rakennuspalain 1–4
   - Pohjautuu L17 ja L18 kokemuksiin
   - ~1 sivu

**Yhteensä:** ~4 sivua dokumentaatiota + esittely

---

## Vihje

- **Rakennuspalat:** Varmista, että kaikki neljä rakennuspalaa (oppitunnit 10, 12, 14, 16) näkyvät jokaisessa tehtävässä.
- **Testaus:** Ole perusteellinen. Parempi testata liian paljon kuin liian vähän.
- **Esittely:** Harjoittele ennen kuin näytät muille. Mitä paremmin harjoittelet, sitä vaikuttavammalta se näyttää.
- **Palaute muille:** Ole ystävällinen, mutta rehellinen. Rakentava palaute auttaa kaikkia kehittymään.
- **Reflektio:** Kirjoita rehellisesti. On OK sanoa, että jokin oli vaikeaa tai että tekisit toisin. Opettaja haluaa nähdä ajattelua, ei perfektioita tai virheettömiä vastauksia.

---

## Aikataulu

- **Tehtävä 18.1** (testaus + iterointi): 20 min
- **Tehtävä 18.2** (esittelyn valmistelu): 20 min
- **Tehtävä 18.3** (esittely ja palaute): 30 min
- **Tehtävä 18.4** (reflektio): 20 min

**Yhteensä: ~90 minuuttia**

Tehtävät 18.1–18.3 tehdään samalla oppitunnilla. Reflektio (18.4) voidaan tehdä heti perään tai pohdiskella vielä muutaman päivän jälkeen.

---

## Mitä seuraavaksi?

Kun olet valmis tämän kanssa, sinulla on toimiva, testattu ja esitetty bottiprojekti. Projektissa olet hyödyntänyt neljää rakennuspalaa (oppitunnit 10, 12, 14, 16) ja yhdistänyt ne yhdeksi kokonaiseksi ratkaisuksi. Seuraavassa osiossa (oppitunnit 19–27) botti muuttuu agentiksi. Agentti voi tehdä enemmän — käsitellä tiedostoja, ajaa komentoja ja tehdä päätöksiä itsenäisesti. Pohja, jonka rakennat täällä, on agenttisi perusta.
