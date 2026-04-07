# Opettajan materiaalit: Etiikka, tekijänoikeudet ja ympäristövaikutukset

## Oppimisen tavoitteet (Bloom: Arvioi)

Tämän lohkon jälkeen opiskelija:

1. Ymmärtää tekijänoikeus- ja koulutusdatakysymykset: kuka omistaa datan, kuka teki mallin, onko lupa olemassa.
2. Osaa selittää algoritmisen harhan mekanismin ja sen seuraukset.
3. Tietää, että datan merkitseminen tekoälyä varten on globaalia, matalapalkkaista työtä.
4. Ymmärtää tekoälyn ympäristövaikutukset (energia, vesi, hiili).
5. Osaa argumentoida eettisesti perustellun käytön puolesta ammattilaisena.

---

## Yleinen pedagoginen lähestymistapa

**Tämä oppitunti liittyy arvoihin ja voi olla hankala.**

Opiskelijoilla voi olla reaktioita:
- "En halunnut tietää tätä!" (okei, mutta nyt tiedät)
- "Mitään ei voi tehdä, se on liian suuri." (totta, mutta sinulla on pieni ääni)
- "Kritisoitko tekoälyä?" (kritiikki ≠ boikotti)

**Paras lähestymistapa:**
- Emme vihaa tekoälyä. Emme vihaa avoimesti yrityksiä.
- Mutta ammattilaisena sinulla on vastuu ymmärtää vaikutukset ja tehdä tietoisia valintoja.
- Ammattilaisuus tarkoittaa syvempää pohdintaa.

---

## Sisältöohjeet: Avainasiat

### 1. Tekijänoikeudet ja koulutusdata

**Mitä opettaa:**
- Kielimallit on opetettu miljardeilla teksteillä internetistä.
- Tekijöiltä ei kysytty lupaa, eikä heille maksettu korvausta.
- Tämä on johtanut oikeustapauksiin, jotka ovat vielä käynnissä (2024).
- "Reilu käyttö" (*fair use*) -käsite on kiistanalainen: onko kielimallin koulutus "transformatiivista"?

**Konkreettiset tapaukset:**
- OpenAI vs. kirjailijoiden yhdistys (2023)
- Stability AI vs. kuvataiteilijat (2023)
- Google News vs. journalistit (käyttävät artikkeleita ilman korvausta)

**Mitä EI opettaa:**
- "Tekoäly on varkautta ja kaikki yritykset ovat pahoja." (Liian yksinkertaista.)
- "Tekoäly on 100 % laillista." (Liian varma väite — tuomioistuimet eivät ole päättäneet.)

**Tärkeä nyanssi:**
- Tekijänoikeuskysymykset ovat JURIDISIA ja EETTISIÄ.
- Joskus laillinen ei ole eettistä (esim. jokin voi olla *fair use*, mutta silti epäoikeudenmukaista).
- Ammattilaisena molemmat ovat tärkeitä.

---

### 2. Algoritminen harha

**Mitä opettaa:**
- Algoritminen harha syntyy koulutusdatasta.
- Jos data heijastaa historiallista syrjintää, malli oppii syrjinnän.
- Harha ei ole mallin "intentio" — se on matematiikkaa.
- Harha on testattavissa ja korjattavissa (mutta se vaatii aktiivista työtä).

**Konkreettiset tapaukset:**
- Amazonin rekrytointialgoritmi (yritti systemaattisesti poissulkea naisia)
- COMPAS (oikeusjärjestelmän uusintariskiarvio oli rodullisesti puolueellinen)
- Kasvojentunnistus (toimii huonommin tummaihoisilla)

**Mitä opiskelijoiden tulisi omaksua itsenäisesti:**
- Algoritmi ei ole "objektiivinen" vain siksi, että se on matemaattinen.
- Harha voi olla hienovaraista — sen havaitseminen vaatii aktiivista testaamista.
- Jokainen, joka ottaa algoritmin käyttöön, kantaa siitä vastuun.

**Opettajan muistutus:** Tämä ei tarkoita, että algoritmeja ei pidä käyttää. Se tarkoittaa, että niitä on testattava harhan varalta.

---

### 3. Datan merkitsijät ja globaali työ

**Mitä opettaa:**
- Tekoälyn opetukseen tarvitaan ihmisiä "merkitsemään" tietoa (sanomaan mallille "tämä on kissa", "tämä on negatiivinen").
- Tämä työ tehdään usein globaalissa etelässä (Bangladesh, Intia, Filippiinit) matalapalkkaisesti.
- Työntekijät saavat 2–5 dollaria tunnilta, eivät vakuutusta, ja heidän oikeutensa ovat rajalliset.
- Joskus työ sisältää traumaattisia kuvia (väkivalta, seksuaalisuus), mikä vaikuttaa mielenterveyteen.

**Konkreettiset lähteet:**
- Amazon Mechanical Turk (Amazonin joukkotyöalusta)
- Scale Data, Scale AI (datan merkitsemisen palvelut)
- Dokumentit ja uutiset aiheesta "AI data labeling workers"

**Mitä tämä merkitsee ammattilaiselle:**
- Kun käytät ChatGPT:tä, käytät mallia, jonka opettamiseen nämä ihmiset ovat osallistuneet.
- Et maksa heille suoraan, mutta heidän työnsä mahdollistaa palvelun arvon.
- Ammattilaisena: tiedä tämä, ajattele sitä.

**Mitä EI opettaa:**
- "Tekoäly on paha, koska siinä käytetään matalapalkkaista työtä." (Liian yksinkertaista; globaali talous on monimutkainen.)
- "Merkitsijöiden pitäisi ansaita enemmän — piste." (Totta, mutta miten?)

---

### 4. Ympäristövaikutukset

**Mitä opettaa:**
- Tekoälyllä on merkittävä energiankulutus.
  - 1 ChatGPT-kysely = ~0,29 wattituntia
  - 200 miljoonaa kyselyä/kuukausi = 58 gigawattituntia/vuosi
- Datakeskukset käyttävät valtavasti vettä jäähdytystä varten.
  - OpenAI:n Texasin datakeskus: 37 miljoonaa gallonaa/vuosi
- Sirujen valmistus (GPU:t) kuluttaa energiaa, vettä ja mineraaleja.
- Hiilipäästöt ovat merkittäviä (joskin datakeskuksilla on kasvava osuus uusiutuvia energialähteitä).

**Mitä tämä merkitsee ammattilaiselle:**
- Jokainen tekoälyn käyttö sisältää ympäristökustannuksen.
- "Harkittu käyttö" tarkoittaa: käytä tekoälyä silloin, kun hyöty ylittää ympäristökustannukset.
- Organisaatiossa: dokumentoi tekoälyn käyttö ja mieti vaihtoehtoisia ratkaisuja.

**Mitä EI opettaa:**
- "Älä koskaan käytä tekoälyä — ympäristövaikutusten vuoksi." (Liioittelua.)
- "Ympäristövaikutus on mitätön." (Väärin; ne ovat merkittäviä mittakaavassa.)

---

## Yleisimmät väärinymmärrykset

### Väärinymmärrys 1: "Tekoälyn koulutus on ilmaista, joten tekijöille ei tarvitse maksaa."

**Ei. Tekoälyn opetuksessa on käytetty tekijöiden työtä.**
- Vaikka operatiivinen datan "noutaminen" verkosta ei ole kallista, tekijöiden työ on arvokasta.
- Eettisesti ja juridisesti tekijöillä voi olla oikeus korvaukseen.

**Ammattilaisen vastaus:** Kun valitset tekoälypalvelua, voit kysyä, onko tekijöille maksettu ja onko toiminta läpinäkyvää. Valinnat kasautuvat.

### Väärinymmärrys 2: "Algoritmi on objektiivinen, koska se on matemaattinen."

**Ei. Algoritmi on yhtä hyvä kuin data, jolla se on opetettu.**
- Jos data on harhaista, malli on harhainen.
- Matematiikka vain "suurentaa" harhaa.

**Ammattilaisen vastaus:** Algoritmisia päätöksiä on testattava harhan varalta. Objektiivisuus on myytti; vastuullisuus on se, mitä kannattaa tavoitella.

### Väärinymmärrys 3: "Merkitsijät voivat vain hakea parempia töitä."

**Ei näin yksinkertaisesti.**
- Globaalin etelän taloudellinen tilanne on rajallinen.
- Nämä työt ovat usein parempia kuin paikalliset vaihtoehdot.
- Mutta ne ovat silti huonosti palkattuja ja hyväksikäyttöön perustuvia.

**Ammattilaisen vastaus:** Ymmärrä konteksti. Kun käytät tekoälyä, tiedä, kuka maksoi siitä hintaa.

### Väärinymmärrys 4: "Ympäristövaikutus on pieni — älä ole huolissasi."

**Ei. Datakeskuksilla on merkittävät päästöt ja vedenkulutus.**
- Vuotuinen hiilijalanjälki vastaa miljoonien autojen päästöjä.
- Vedenkulutus on merkittävää kuivilla alueilla.

**Ammattilaisen vastaus:** Harkittu käyttö on tärkeää. Älä käytä tekoälyä "vain koska".

---

## Opettajan vinkkejä harjoituksiin

### Harjoitus 1: Oikeustapauskeskustelu

**Miksi tämä on tärkeää:** Opiskelijat näkevät, että tekijänoikeuskysymys ei ole "ratkaistu" — se on *nyt* kiistanalainen.

**Jos opiskelijat sanovat "kumpi puoli on oikeassa?":**
- Vastaa: "Tuomioistuimet eivät ole vielä päättäneet. Molemmat osapuolet esittävät vahvoja väitteitä."
- Korosta: "Ammattilaisena sinulla on näkemys — ja se vaikuttaa siihen, mitä palvelua valitset."

**Jos haluat tehdä siitä emotionaalisen:**
- Kysy: "Jos olisit kirjailija, jonka teoksia käytettiin ilman lupaa — mitä ajattelisit?"

---

### Harjoitus 2: Harhan testaaminen

**Miksi tämä on tärkeää:** Opiskelijat näkevät, että harha on *testattavissa* eikä "vain olemassa".

**Jos opiskelijat sanovat "kuinka havaita harha?":**
- Neuvo: "Testaa algoritmia useilla demografisilla ryhmillä. Vertaa tuloksia. Ovatko ne epäoikeudenmukaisesti erilaisia?"

**Jos opiskelijat sanovat "johtajat eivät välitä harhasta?":**
- Vastaa: "Silloin sinulla on ammatillinen vastuu nostaa huoli esiin. Dokumentoi, jaa tiedot, vaadi muutosta."

---

### Harjoitus 3: Eettinen keskustelu

**Miksi tämä on tärkeää:** Opiskelijat näkevät, että vastuu on hajaantunut — mutta heillä on ääni.

**Vältä:**
- Ratkaisujen tarjoamista liian yksinkertaisesti (esim. "ja sitten kaikki maksoivat reilua palkkaa!").
- Liiallista sentimentaalisuutta.

**Pyri kohti:**
- Ymmärrystä aiheen vaativuudesta.
- Näkemystä siitä, että ammattilaisella on valinta.

---

## Aika- ja resurssiehdotukset

| Aktiviteetti | Aika | Resurssi |
|---|---|---|
| Itseopiskeluosa | 40–50 min | Oppikirja, muistiinpanot |
| Harjoitus 1 (oikeustapaus) | 25 min | Yhdistetyt opiskelumateriaalit |
| Harjoitus 2 (harhan testaaminen) | 20 min | Skenaariokortit |
| Harjoitus 3 (globaali työ) | 20 min | — |
| Harjoitus 4 (ympäristö) | 15 min | Apua energialaskelmiin |
| Yhteenveto | 10 min | — |
| **Yhteensä** | **~130 min** | — |

---

## Jälkipuoli (Lesson 9)

**Oppitunti 9** käsittelee turvallista käyttöä ja summatiivista arviointia: prompt injection, tietovuodot, datan hygienia ja Teoria-osion arviointi.

Tämä oppitunti (8) luo perustan eettiselle ymmärrykselle. Oppitunti 9 yhdistää käytännön ja turvallisuuden.

---

## Opettajan muistiinpano tämän lohkon kanssa

**Tämä aihe voi tuntua raskaalta.** Opiskelijoilla voi olla tunteita: surua, vihaa, epätoivoa.

**Tämä on okei.**

Ammattilaisuus ei tarkoita, ettet välitä — se tarkoittaa, että ajattelet syvemmin ja teet eettisesti vastuullisia valintoja siitä huolimatta.

Lopeta oppitunti sanoihin: **"Sinulla on ääni. Käytä sitä."**