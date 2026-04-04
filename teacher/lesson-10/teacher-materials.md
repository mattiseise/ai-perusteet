# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

Tämän lohkon jälkeen opiskelija:
1. Osaa luetella ainakin kolme erilaista kielimallia ja niiden perusominaisuuksia.
2. Ymmärtää, että eri AI-työkalut on optimoitu eri tehtäviin.
3. Osaa testata samaa tehtävää usealla työkalulla ja dokumentoida erot.
4. Tunnistaa ammattilaiset näkökohdat (hinta, yksityisyys, oikeudet) työkalun valinnassa.

---

## Yleisiä väärinkäsityksiä

### 1. "ChatGPT on paras AI-työkalu, joten pitäisi käyttää sitä kaikkeen."

**Todellisuus:** ChatGPT on yksi työkalu monista. Se on hyvä teksti­pohjaisiin tehtäviin, mutta se ei ole ihanteellinen kuvien luomiseen, videoon tai offline-käyttöön. Ammattilaisena valitset työkalun tehtävän perusteella.

### 2. "Jos käytän tekoälyä, valitsen sen, joka on halvin / nopein / suosituin."

**Todellisuus:** Halvin ei ole aina paras, nopein ei välttämättä anna riittävän hyvää laatua, ja suosituin ei ehkä sovi sinun käyttötapaukseen. Ammattilaisesti arvioit kontekstia.

### 3. "Generoidut kuvat ovat yhtä laadukkaita kuin todellisen valokuvaajan ottamat kuvat."

**Todellisuus:** Kuvan generaattorit voivat tuottaa hyviä visuaalisia aineistoja ideointiin ja mockup-malleihin, mutta ne voivat sisältää virheitä ja eivät ole "todellisia" kuvia. Ammattilaisesti tiedät niiden rajoitukset.

### 4. "Kun avaan komentorivin, en voi käyttää tekoälyä."

**Todellisuus:** Komentorivin tekoälytyökalut (ollama, Copilot CLI) mahdollistavat offline-käytön, integraation koodiin ja yksityisyyden suojan. Nämä ovat merkittävä arkkitehtuuri-valinta ammattilaisille.

---

## Opettajan fasilitointiohjeet

### Ennen lähiosaa

- Testaa itse ChatGPT, Claude ja yksi muu kielimalli etukäteen.
- Testaa yksi kuvan generaattori (DALL-E tai vaihtoehto) ja dokumentoi prosessia ja tulosta.
- Valmistele kolme "kehotusta" (prompts), jotka käytät live-testauksessa.
- Jos mahdollista, asenna ollama tai käytä Copilot CLI omalla konelloasi näyttämiseen.

### Lähiosassa (90 minuuttia)

- Käynnistä live-testaus (Tehtävä 10.1) ensimmäiseksi. Opiskelijat näkevät konkreettisesti, kuinka työkalut eroavat.
- Liitä kuvan generaattoreiden testaus (Tehtävä 10.2). Opiskelijat näkevät, että tekoäly ei ole vain tekstiä.
- Pääty luokkakeskusteluun (Tehtävä 10.3), jossa arvioidaan konteksti­pohjaisia valintoja.
- Säilytä aina linkki ammattilaisiin tapauksiin — älä jää pelkälle väline­käytölle.

### Yleinen neuvo

- Monet opiskelijat näkevät ChatGPT:n "oikeaksi" välineeksi, koska se on suosituin. Korjaa tämä: suosio ei tarkoita sopivuutta.
- Korostaa, että ammattilaisena testaat. Et arvaa. Et valitse "koska kaikki muut käyttävät sitä".
- Jos opiskelijat haluavat käyttää komentoriviä, kannusta heitä — se on tärkeä ammattilaisille.

---

## Tarkistustehtävät (Checking-for-Understanding)

### 1. Perustieto
**"Mitkä ovat kolme teksti­pohjaista kielimallia, joista puhuimme? Kerro niistä lyhyesti."**
- *Mitä etsit:* Opiskelija nimeää ChatGPT, Claude ja Copilot; osaa sanoa niiden eroista.

### 2. Konteksti­pohjainen valinta
**"Sinulla on tehtävä: kirjoita funktio ja luo sille kuva. Mitä työkaluja käyttäisit? Miksi kutakin?"**
- *Mitä etsit:* Opiskelija valitsee tekstimallin koodille ja kuva­generaattorin kuvalle; osaa perustella valintoja.

### 3. Testaus ja dokumentointi
**"Testasit kaksi työkalua samalla kehotuksella. Mitä eroja huomasit? Miten dokumentoit?"**
- *Mitä etsit:* Opiskelija kertoo erosta ja ymmärtää, miksi dokumentointi on tärkeää.

### 4. Ammattilaiset näkökohdat
**"Mitä sinun täytyy tietää ennen kuin valitset kuvan generaattoria yrityksen markkinointiin?"**
- *Mitä etsit:* Opiskelija nimeää hintaa, oikeuksia, laatua ja laillisuutta.

### 5. Offline-käyttö
**"Miksi kehittäjä voisi haluta käyttää ollamaa ChatGPT:n sijaan?"**
- *Mitä etsit:* Opiskelija ymmärtää offline-tilan, yksityisyyden ja integraation hyödyt.

---

## Yleisiä vaikeuksia ja niihin vastaamisen strategiat

### Vaikeus 1: Opiskelijat luulevat ChatGPT:n olevan "paras" ja haluavat käyttää sitä kaikkeen

**Mitä kuuluu:** "ChatGPT osaa kaiken, joten miksi käytämme muita?"

**Vastaus:** "ChatGPT on hyvä tekstiin, mutta se ei luo kuvia. Jos tarvitset kuvaa, et käytä tekstimallia — käytät kuva­generaattoria. Ammattilaisesti valitset työkalun tehtävän, ei suosion perusteella."

**Strategia:** Näytä live-testaus, jossa ChatGPT yrittää "luoda kuvaa" — antaa tekstikuvauksena, ei todellisena kuvana. Osoita sitten kuva­generaattori. Konkreettinen näyttö auttaa.

### Vaikeus 2: Opiskelijat eivät ymmärrä, miksi kielimallit antavat eri vastauksia

**Mitä kuuluu:** "Hän sanoivat ne ovat kaikki 'tekoälyä' — miksi ne antavat erilaisia vastauksia?"

**Vastaus:** "Koska ne on koulutettu eri datalla ja niillä on eri parametrit. Kuten ihmiset: kaksi insinööriä voivat ratkaista saman ongelman eri tavalla, koska heillä on eri koulutus."

**Strategia:** Anna konkreettinen esimerkki: "ChatGPT oppi tekstistä Internetissä. Claude oppi tekstistä, jossa painotettiin turvallisuutta. Joten ne tekevät eri valintoja."

### Vaikeus 3: Opiskelijat luulevat kuva­generaattorin tuottamien kuvien olevan "oikein todellisia"

**Mitä kuuluu:** "Generoin kuvan — se näyttää todelliselta! Voinko käyttää sitä?"

**Vastaus:** "Näyttää siltä, mutta se on generaatio, ei kuva. Se voi sisältää virheitä, ja oikeus­asiat ovat komplekseja. Ammattilaisesti: tiedät sen rajoitukset."

**Strategia:** Näytä kuva, jossa on hienovarainen virhe (esim. väärä määrä sormia, outoja kirjoituksia). Opiskelijat näkevät heti — kuva­generaattorit tekevät virheitä.

### Vaikeus 4: Opiskelijat eivät näe, miksi komentorivin tekoäly on merkittävä

**Mitä kuuluu:** "Miksi käyttäisin komentoriviä? Voin vain avata ChatGPT:n selaimessa."

**Vastaus:** "Komentorivillä on etuja: offline-käyttö, integraatio koodiin, yksityisyys. Kehittäjälle nämä ovat kriittisiä."

**Strategia:** Näytä komentorivin tekoäly toiminnassa. Osoita, kuinka sitä kutsutaan koodista. Merkitseväksi tulee, kun he näkevät, miten se integroituu.

---

## Oppimisresurssit, joihin opettaja voi viitata

1. **Builder-materiaali (lesson-10.md):** Kaikki perusideat ja esimerkit ovat siellä. Varmista, että opiskelijat ovat tutustuneet.
2. **Live-testaus:** Testaa työkalut itse ennen osaa. Kerää näyttökaappaukset tai videot testeistä.
3. **Ammattilaiset esimerkit:** Etsi uutisia siitä, missä kuvan generointioikeudet joivat riitaa, tai mistä yritykset valitsivat tietyn työkalun ja miksi.
4. **Opiskelijoiden omat testit:** Kannusta heitä testaamaan ja dokumentoimaan omia havaintojaan.

---

## Lisämateriaalia opettajalle

### Taustatietojen for opettaja

- **ChatGPT vs. Claude:** ChatGPT on pienempi ja reagoivampi lyhyihin tehtäviin. Claude on isompi ja parempi pitkien dokumenttien luvussa ja analysoinnissa.
- **DALL-E vs. Midjourney:** DALL-E on nopeampi ja integroitu OpenAI:n ekosysteemiin. Midjourney on tunnettu korkeammasta visuaalisesta laadusta, mutta kalliimpi.
- **Ollama vs. Copilot CLI:** Ollama on täysin offline, avoin lähde, maksutonta. Copilot CLI on Microsoft-integroitu ja verkkoyhteys­pohjainen, mutta tarkemmin optimoitu Windows-kehittäjille.

### Kysymyksiä opiskelijoille

- "Testasit kielimallia. Mitkä olivat vahvuudet? Mitkä heikkoudet?"
- "Kuinka määrittäisit, kumpi työkalu on 'parempi' — pintatason laadun vs. hinnan vs. yksityisyyden perusteella?"
- "Jos yrityksesi käyttäisi tekoälyä, mitä sinun pitäisi tietää sen valinnasta?"
