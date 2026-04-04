# Opettajan materiaalit: Etiikka, tekijänoikeudet ja ympäristövaikutukset

## Oppimisen tavoitteet (Bloom: Arvioi)

Tämän lohkon jälkeen opiskelija:

1. Ymmärtää tekijänoikeus- ja koulutus datakysymykset: kuka omistaa datan, kuka teki mallin, onko lupa olemassa.
2. Osaa selittää algoritmisen harhan mekanismin ja sen seurauksista.
3. Tietää, että datan merkitseminen tekoälyä varten on globaali, matalapalkkaisilla työ.
4. Ymmärtää tekoälyn ympäristövaikutukset (energia, vesi, hiili).
5. Osaa argumentoida eettisesti perustellun käytön puolesta ammattilaisena.

---

## Yleinen pedagoginen lähestymistapa

**Tämä oppitunti on arvoksiin liittyvä ja voi olla hankala.**

Opiskelijoilla voi olla reaktioita:
- "En halunnut tietää tämä!" (okei, mutta nyt tiedät)
- "Mitään ei voi tehdä, se on liian suuri." (totta, mutta sinulla on pieni ääni)
- "Oletko kritisoitko tekoälyä?" (kritiikki ≠ boikotti)

**Paras lähestymistapa:**
- Emme vihaa tekoälyä. Emme vihaa avoimesti yrityksiä.
- Mutta ammattilaisena sinulla on vastuu ymmärtää vaikutukset ja tehdä tietoisia valintoja.
- Ammattilaisuus tarkoittaa syvempää pohdintaa.

---

## Sisältöohjeet: Avainasiat

### 1. Tekijänoikeudet ja koulutusdata

**Mitä opettaa:**
- Kielimallit on opetettu miljaardeilla teksteillä Internetistä.
- Tekijöitä ei kysytty, heitä ei korvattu.
- Tämä on johtanut oikeustapauksiin, jotka ovat vielä käynnissä (2024).
- "Reilu käyttö" (fair use) -käsite on kiistanalainen: onko kielimallin koulutus "transformatiivista"?

**Konkreettiset tapaukset:**
- OpenAI vs. kirjailijoiden yhdistys (2023)
- Stability AI vs. kuvataiteilijat (2023)
- Google News vs. journalistit (käyttävät artikkeleita ilman korvausta)

**Mitä EI opeta:**
- "Tekoäly on varkaus ja kaikki yritykset ovat pahoja." (Liian yksinkertainen.)
- "Tekoäly on 100% laillista." (Liian varma — tuomioistuimet eivät ole päättäneet.)

**Tärkeä nuansa:**
- Tekijänoikeuskysymykset ovat JURIDISIA ja EETTISIÄ.
- Joskus laillinen ei ole eettistä (esim. jotain voi olla "fair use", mutta silti epäoikeudenmukaista).
- Ammattilaisena molemmat ovat tärkeitä.

---

### 2. Algoritminen harha

**Mitä opettaa:**
- Algoritminen harha syntyy koulutus datasta.
- Jos data heijastaa historiallista syrjintää, malli oppii syrjinnän.
- Harha ei ole mallin "intentio" — se on matematiikka.
- Harha on testattavissa ja korjattavissa (mutta vaatii aktiivisen työn).

**Konkreettiset tapaukset:**
- Amazon:n rekrytointialgoritmi (yritti systemat.isesti poistaa naisia)
- COMPAS (oikeusjärjestelmän uusintariskiarvio oli rodullisuuden suhteen puolueellinen)
- Kasvojen tunnistus (toimii huonommin tummaihoisille)

**Mitä opiskelijat omaksuvat itsenäisesti:**
- Algoritmi ei ole "objektiivinen" vain koska se on matemaattinen.
- Harha voi olla hienovarainen — se vaatii aktiivista testaamista havaita.
- Jokainen, joka ottaa algoritmin käyttöön, kantaa vastuun siitä.

**Opettajan muistutus:** Tämä ei tarkoita, että algoritmeja ei pidä käyttää. Se tarkoittaa, että niitä on testattava harban varalta.

---

### 3. Datan merkitsijät ja globaali työ

**Mitä opettaa:**
- AI:n opetukseen tarvitaan ihmisillä "merkata" tietoja (sanoa mallille "tämä on kissa", "tämä on negatiivinen").
- Tämä työ tehdään usein globaalin etelässä (Bangladeshi, Intia, Filippiinit) matalapalkkaisesti.
- Työntekijät saavat $2–5 per tunti, ei vakuutusta, rajoitettuja oikeuksia.
- Joskus työ sisältää traumaatisia kuvia (väkivalta, seksuaalisuus), mikä vaikuttaa mielenterveyteen.

**Konkreettiset lähteet:**
- Amazon Mechanical Turk (Amazon:n voimityöalusta)
- Sama Data, Scale AI (data-merkitsemia palvelut)
- Dokumentaarit ja uutiset "AI data labeling workers"

**Mitä ammattilaisesti merkitsee:**
- Kun käytät ChatGPT:tä, käytät mallia, jonka opettivat nämä ihmiset.
- Et maksa heille suoraan, mutta heidän työnsä mahdollistaa arvosi.
- Ammattilaisesti: tiedä tämä, ajattele sitä.

**Mitä EI opeta:**
- "Tekoäly on paha, koska käytetään matalapalkkaisuus." (Yksinkertainen; globaali talous on monimutkainen.)
- "Merkitsijät ansaitsevat enemmän — piste." (Totta, mutta miten?)

---

### 4. Ympäristövaikutukset

**Mitä opettaa:**
- Tekoälyllä on merkittävä energian jalanjälki.
  - 1 ChatGPT-query = ~0,29 wattituntia
  - 200 miljoonaa kyselyä/kuukausi = 58 gigawattituntia/vuosi
- Datakeskukset käyttävät valtavasti vettä jäähdytystä varten.
  - OpenAI:n Texasin data-keskus: 37 miljoonaa gallonaa/vuosi
- Sirujen valmistus (GPU:t) kuluttaa energiaa, vettä ja mineraaleja.
- Hiilen päästöt ovat merkittävät (joskin data-keskuksilla on kasvava osuus uusiutuvista energialähteistä).

**Mitä ammattilaisesti merkitsee:**
- Jokainen tekoälyn käyttö sisältää ympäristökustannuksen.
- "Harkittu käyttö" tarkoittaa: käytä tekoälyä silloin, kun arvo ylittää ympäristökustannukset.
- Organisaatiossa: dokumentoi tekoälyn käyttö, ajattele vaihtoehtoisia ratkaisuja.

**Mitä EI opeta:**
- "Älä koskaan käytä tekoälyä — ympäristövaikutus." (Hyperteroide.)
- "Ympäristövaikutus on mitätön." (Väärin; ne ovat merkittäviä skaalalla.)

---

## Yleisimmät väärinymmärrykset

### Väärinymmärrys 1: "Tekoäly koulutus on ilmaista, joten tekijöille ei tarvitse maksaa."

**Ei. Tekoälyt opetukseen on käytetty tekijöiden työtä.**
- Vaikka operatiivinen "noutaminen" dataa verkosta ei ole kallis, tekijöiden työ on.
- Eettisesti ja juridisesti tekijöillä voi olla oikeus korvaukseen.

**Ammattilaisesti vastaus:** Kun valitset tekoälypalvelua, voit kysyä, onko se maksettu tekijöille ja onko se läpinäkyvää. Valinnat kasautuvat.

### Väärinymmärrys 2: "Algoritmi on objektiivinen koska se on matemaattinen."

**Ei. Algoritmi on yhtä hyvä kuin data, jolla se on opetettu.**
- Jos data on harhainen, malli on harhainen.
- Matematiikka vain "suurentaa" harhan.

**Ammattilaisesti vastaus:** Algoritmisia päätöksiä on testattava harhan varalta. Objektiivisuus on myytti; vastuullisuus on se, mitä tavoitella.

### Väärinymmärrys 3: "Merkitsijät voivat vain hakea parempia töitä."

**Ei näin yksinkertainen.**
- Globaalin etelän taloudellinen tilanne on rajallinen.
- Nämä työt ovat usein parempia kuin paikallisia vaihtoehtoja.
- Mutta ne ovat silti huonosti palkattuja ja hyväksikäytettyjä.

**Ammattilaisesti vastaus:** Ymmärrä konteksti. Kun käytät tekoälyä, tiedä kuka maksoi hintaa.

### Väärinymmärrys 4: "Ympäristövaikutus on pieni — älä ole huoleissasi."

**Ei. Datakeskuksilla on merkittävä päästö ja vesienkulutus.**
- Vuotuinen hiilijalanjälki vastaavat miljoonien autojen päästöihin.
- Vesienkulutus on merkittävää kuivilla alueilla.

**Ammattilaisesti vastaus:** Harkittu käyttö on tärkeä. Älä käytä tekoälyä "vain koska".

---

## Opettajan vinkkejä harjoituksiin

### Harjoitus 1: Oikeustapaus-keskustelu

**Miksi tämä on tärkeä:** Opiskelijat näkevät, että tekijänoikeus ei ole "ratkaistu" — se on *nyt* kiista.

**Jos opiskelijat sanovat "kumpi puoli on oikeassa?":**
- Vastaa: "Tuomioistuimet eivät ole vielä päättäneet. Molemmat puolet väittävät vahvasti."
- Korostaa: "Ammattilaisena sinulla on näkemys — ja se vaikuttaa, mitä palvelua valitset."

**Jos haluaat tehdä siitä emotionaalisen:**
- Kysy: "Jos olisit kirjailija, jonka teoksia käytettiin ilman lupaa — mitä ajattelisit?"

---

### Harjoitus 2: Harha-testiminat

**Miksi tämä on tärkeä:** Opiskelijat näkevät, että harha on *testattavissa* eikä "vain olemassa".

**Jos opiskelijat sanovat "kuinka havaita harhan?":**
- Neuvonta: "Testaa algoritmi usealla demografisella ryhmällä. Vertaa tuloksia. Ovatko ne epäoikeudenmukaisesti erilaiset?"

**Jos opiskelijat sanovat "kuukauden johtajat ei välitä harhasta?":**
- Vastaa: "Silloin sinulla on ammattilinen vastuu nostaa huoli. Dokumentoi, jaa tiedot, vaadi muutosta."

---

### Harjoitus 3: Eettinen keskustelu

**Miksi tämä on tärkeä:** Opiskelijat näkevät, että vastuu on hajaantuneet — mutta heillä on ääni.

**Vältä:**
- Antamatta ratkaisua (esim. "ja sitten kaikki maksoivat reilua palkkaa!").
- Itkeminen (emme halua sentimentaalisuutta).

**Pyri kohti:**
- Ymmärryksen vaativuudesta.
- Näkemystä siitä, että ammattilaisella on valinta.

---

## Aika- ja resurssiehdotukset

| Aktiviteetti | Aika | Resurssi |
|---|---|---|
| Itseopiskeluosa | 40–50 min | Oppikirja, muistiinpano |
| Harjoitus 1 (oikeustapaus) | 25 min | Yhdenvänä opiskelua materiaalit |
| Harjoitus 2 (harha-testiminat) | 20 min | Skenaario-kortit |
| Harjoitus 3 (globaali työ) | 20 min | — |
| Harjoitus 4 (ympäristö) | 15 min | Energian laskusaldoilla |
| Yhteenveto | 10 min | — |
| **Yhteensä** | **~130 min** | — |

---

## Jälkipuolella (Lesson 9)

**Lesson 9** on turvallinen käyttö ja summatiivinen arviointi: prompt injection, tietovuodot, datan hygienia, ja OSP1-arviointi.

Tämä oppitunti (8) perustaa eettisen ymmärryksen. Lesson 9 nysväää käytäntöä ja turvallisuutta.

---

## Opettajan omakotielämä tämän lohkon kanssa

**Tämä oppiaine voivat tuntua raskaalta.** Opiskelijoilla voi olla tunteet: pahoillaan, vihaa, epätoivo.

**Tämä on okei.**

Ammattilaisuus ei tarkoita, että et välitä — se tarkoittaa, että ajattelet syvemmin ja teet eettisesti vastuullisia valintoja siitä huolimatta.

Lopeta oppitunnit sanalla: **"Sinulla on ääni. Käytä sitä."**

