# Opettajavetoiset tehtävät

## Tehtävä 5.1: Konteksti-ikkunan rajoitukset — live-vertailu

### Tavoite

Tehtävän tavoitteena on näyttää opiskelijoille konkreettisesti, miten **konteksti-ikkunan** rajallisuus voi vaikuttaa tekoälyn vastauksiin pitkissä keskusteluissa. Samalla opiskelijat ymmärtävät, miksi **kontekstin hallinta** on välttämätön taito tekoälyn käytössä.

**Opettajan painotus:** Korosta, että tekoälyn “muisti” ei ole rajaton. Pitkässä keskustelussa osa aiemmasta tiedosta voi jäädä pois käytettävissä olevasta kontekstista, vaikka keskustelu näkyisi käyttäjälle edelleen ruudulla.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**

- Valitse **IT-loki** tai virheilmoitusten sarja, joka sisältää useita virheitä. Sopiva pituus on noin 1 000–2 000 tokenia.
- Vaihtoehtoisesti voit kirjoittaa synteettisen noin 10 kysymyksen keskusteluketjun, jossa samaa ongelmaa käsitellään eri näkökulmista.
- Valitse etukäteen alkuperäinen **rooli**, **taustatilanne** ja **tavoite**, jotka mallin pitäisi muistaa keskustelun ajan.

### Toteutus noin 20 minuuttia

1. **Johdanto noin 2 minuuttia:**

   ```

   Kerro opiskelijoille:

   > Tekoälyn keskustelumuisti on rajallinen. Sitä voidaan ajatella muistikirjana, johon mahtuu vain tietty määrä tekstiä. Kun muistikirja täyttyy, vanhempaa tietoa voi jäädä pois mallin käytettävissä olevasta kontekstista.
2. **Näytös: pitkä keskustelu noin 8 minuuttia:**

   1. Avaa tekoälytyökalu näytölle.
   2. Anna keskustelun alkuun selkeä konteksti, esimerkiksi:

   Rooli: Olet Linux-järjestelmänhallitsija. Tausta: palvelin kaatuu satunnaisesti. Tavoite: etsi lokivirhe ja ehdota korjausta.

   3. Lähetä tämän jälkeen noin 10 kysymystä peräkkäin. Kysymysten tulee liittyä samaan ongelmaan, mutta tarkastella sitä eri näkökulmista.
   4. Pyydä opiskelijoita havainnoimaan, missä vaiheessa vastaukset alkavat irrota alkuperäisestä kontekstista.

   **Tarkkailkaa erityisesti:**

   - Muistaako malli edelleen alkuperäisen roolin eli Linux-järjestelmänhallitsijan näkökulman?
   - Viittaako malli edelleen alkuperäiseen ongelmaan eli satunnaisesti kaatuvaan palvelimeen?
   - Alkaako malli antaa yleisiä vastauksia sen sijaan, että se hyödyntäisi alussa annettua taustatietoa?
3. **Analyysi noin 5 minuuttia:**

   Kysy opiskelijoilta:

   - Huomasitteko, missä vaiheessa vastaukset alkoivat muuttua yleisemmiksi?
   - Mikä tieto näytti heikkenevän tai häviävän keskustelun aikana?
   - Kuinka moni vastaus hyödynsi alkuperäistä kontekstia selvästi?
   - Kuinka moni vastaus olisi ollut parempi, jos alkuperäinen konteksti olisi toistettu uudelleen?
4. **Johtopäätös noin 5 minuuttia:**

   Kirjoita taululle yksinkertainen malli konteksti-ikkunan täyttymisestä:

   Alkukonteksti + kysymykset + vastaukset = keskustelun kokonaiskonteksti

   Voit havainnollistaa asiaa myös näin:

   Konteksti 80 tokenia + K1 30 tokenia + V1 50 tokenia + K2 30 tokenia + V2 50 tokenia + ... = ikkuna täyttyy vähitellen

   Selitä opiskelijoille:

   > Mitä pidemmäksi keskustelu kasvaa, sitä tärkeämpää on hallita kontekstia. Siksi tarvitaan strategioita, kuten **tiivistämistä**, **ankkurointia** ja **tehtävän pilkkomista**.
```

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että **konteksti-ikkuna** ei ole vain teoreettinen käsite, vaan se voi vaikuttaa tekoälyn vastausten laatuun.
- Opiskelijat tunnistavat tilanteita, joissa tekoäly voi menettää osan aiemmasta keskustelusta.
- Opiskelijat ymmärtävät, miksi pitkissä tehtävissä tarvitaan kontekstin hallintaa, tiivistämistä ja ankkurointia.

---

## Tehtävä 5.2: Pilkkomisen suunnitteleminen — ohjattu harjoitus

### Tavoite

Tehtävän tavoitteena on opettaa opiskelijoille, miten suuri projekti tai laaja aineisto pilkotaan hallittaviin osiin ennen tekoälyn käyttöä. Samalla harjoitellaan **strategista työskentelyä**, **tiivistämistä** ja **ankkurointia**.

**Opettajan painotus:** Korosta, että ammattimainen tekoälyn käyttö suurissa tehtävissä alkaa suunnittelusta. Kaikkea ei kannata syöttää tekoälylle kerralla, vaikka se teknisesti näyttäisi mahdolliselta.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**

- Valitse laaja IT-tehtävä, jota ei ole järkevää antaa tekoälylle kerralla.
- Esimerkkejä sopivista tehtävistä:
  - 3 000 rivin tietokantaskeman analysointi,
  - 50 000 rivin lokitiedoston virheiden selvittäminen,
  - laajan ohjelmakoodin rakenteen arviointi.
- Valmistele lyhyt kuvaus tehtävästä, sen koosta ja tavoitteesta.

### Toteutus noin 25 minuuttia

1. **Asetelman muuttaminen noin 2 minuuttia:**

   ```

   Kerro opiskelijoille:

   > Kun tekoälyä käytetään isoon tehtävään, kaikkea ei kannata syöttää mallille kerralla. Ammattimainen tapa on suunnitella ensin, miten tehtävä pilkotaan pienempiin osiin.
2. **Vaihe 1: Ymmärtäkää tehtävän koko noin 4 minuuttia:**

   1. Näytä valitsemasi tehtävä, esimerkiksi tietokantaskema tai lokitiedosto.
   2. Kysy opiskelijoilta: **Kuinka suuri tämä aineisto on?**
   3. Arvioikaa tokenimäärää karkeasti. Voitte käyttää nyrkkisääntöä: noin neljä merkkiä vastaa yhtä tokenia.
   4. Keskustelkaa: **Mahtuisiko koko tehtävä yhteen konteksti-ikkunaan? Vaikka mahtuisi, olisiko se järkevää?**
3. **Vaihe 2: Pilkkokaa tehtävä vaiheiksi noin 8 minuuttia:**

   Piirrä taululle rakenne, johon opiskelijat voivat ehdottaa osia.

   **Tietokantaesimerkki:**

   Osa 1: Analysoi taulukot 1–50.

   Osa 2: Analysoi taulukot 51–100.

   Osa 3: Analysoi taulukot 101–150.

   Osa 4: Tee yhteenveto kaikista havainnoista.

   **Lokiesimerkki:**

   Osa 1: Analysoi loki ajalta 08.00–10.00.

   Osa 2: Analysoi loki ajalta 10.00–12.00.

   Osa 3: Analysoi loki ajalta 12.00–14.00.

   Osa 4: Tee yhteenveto kaikista virheistä ja toistuvista kaavoista.

   Kysy opiskelijoilta:

   - Kuinka monta osaa tarvitaan?
   - Miksi juuri tällainen jako olisi järkevä?
   - Mitä riskejä syntyy, jos jako tehdään liian suuriin osiin?
   - Mitä riskejä syntyy, jos jako tehdään liian pieniin osiin?
4. **Vaihe 3: Ankkuroikaa jokainen osa noin 6 minuuttia:**

   Selitä opiskelijoille, että **ankkurointi** tarkoittaa tärkeän taustatiedon toistamista jokaisen osatehtävän alussa. Näin malli pysyy samassa tehtävässä ja tavoitteessa, vaikka keskustelu pitenee.

   Kirjoita taululle esimerkkirakenne:

   Projekti: 3 000 rivin tietokantaskeman analyysi.

   Kokonaistehtävä: tunnista ongelmalliset taulurakenteet ja mahdolliset riippuvuudet.

   Nyt analysoitava osa: taulukot 1–50.

   Tulevat osat: taulukot 51–100 ja 101–150.

   Palauta lopuksi tiivis yhteenveto tämän osan havainnoista.

   Jatko-osassa ankkurointi voi näyttää tältä:

   Edellisen osan yhteenveto: [lyhyt yhteenveto]. Nyt analysoidaan taulukot 51–100 samalla arviointitavalla.

   Selitä opiskelijoille:

   > Ankkurointi auttaa mallia pysymään tehtävässä, vaikka keskustelu pitenee. Se ei poista kaikkia virheitä, mutta vähentää kontekstin katoamisen riskiä.
5. **Lopullinen suunnitelma noin 5 minuuttia:**

   Kirjoita taululle projektisuunnitelman malli:

   Projekti: [nimi]

   Kokonaisuus: [arvioitu koko tokenina tai riveinä]

   Konteksti-ikkuna: [käytettävissä oleva raja]

   Osien määrä: [määrä]

   Strategia: pilkkominen + tiivistäminen + ankkurointi

   Dokumentointi: jokaisesta osasta tehdään yhteenveto

   Kerro opiskelijoille:

   > Tämä on ammattimainen tapa käyttää tekoälyä suurissa IT-tehtävissä. Ensin suunnitellaan kokonaisuus, sitten käsitellään osat ja lopuksi yhdistetään havainnot.
```

**Vinkki arviointiin:** Hyvä pilkkomissuunnitelma ei ole vain lista osista. Siinä näkyy myös, miten osien tulokset tiivistetään ja miten seuraava osa ankkuroidaan edelliseen.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että suuren projektin hallinta vaatii suunnittelua ennen tekoälyn käyttöä.
- Opiskelijat osaavat selittää kolme keskeistä strategiaa: **pilkkominen**, **tiivistäminen** ja **ankkurointi**.
- Opiskelijat pystyvät laatimaan yksinkertaisen suunnitelman oman projektinsa tai aineistonsa käsittelyyn tekoälyn avulla.

---

## Tehtävä 5.3: Kontekstin katoaminen livenä — epäonnistumisen demonstraatio

### Tavoite

Tehtävän tavoitteena on näyttää opiskelijoille reaaliaikaisesti, että tekoäly voi menettää osan aiemmasta kontekstista ilman selkeää varoitusta. Samalla harjoitellaan ammatillista ajattelua: tekoälyn vastaukset on aina tarkistettava suhteessa tehtävän tavoitteeseen ja rajauksiin.

**Opettajan painotus:** Korosta, että virheellinen vastaus voi kuulostaa yhtä varmalta kuin oikea vastaus. Siksi ammattilaisen tehtävä on tarkistaa, noudattaako vastaus annettua kontekstia ja rajauksia.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**

- Valmistele etukäteen noin 15–20 kysymyksen sarja, joka kuormittaa konteksti-ikkunaa.
- Testaa etukäteen, missä vaiheessa valitsemasi tekoälymalli alkaa unohtaa alkuperäisiä rajauksia tai antaa yleisempiä vastauksia.
- Valitse selkeä alkuasetelma, jossa on tarkkoja teknisiä rajauksia.

### Toteutus noin 20 minuuttia

1. **Asetelma noin 3 minuuttia:**

   ```

   Kerro opiskelijoille:

   > Teemme kokeen, jossa katsomme, kuinka luotettava tekoälyn keskustelumuisti on pitkän keskustelun aikana.

   Avaa tekoälytyökalu ja anna selkeä alkurajaus, esimerkiksi:

   Käytämme Ubuntu 22.04 -käyttöjärjestelmää, PostgreSQL-tietokantaa ja Python 3.9 -versiota. Älä ehdota Windows-ratkaisuja tai muita tietokantoja.

   Kysy ensin kolme kysymystä, jotka liittyvät tähän ympäristöön. Tavoitteena on näyttää, että malli hyödyntää alkurajausta keskustelun alussa.
2. **Kontekstin kuormittaminen noin 7 minuuttia:**

   1. Kysy nopeasti 15–20 eri aihetta koskevaa kysymystä.
   2. Älä toista alkurajauksia kysymysten välissä.
   3. Pyydä opiskelijoita seuraamaan, pysyykö malli alkuperäisissä teknisissä rajauksissa.
3. **Paljastus noin 5 minuuttia:**

   1. Kysy lopuksi: `Miten asennan tietokantapalvelimen?`
   2. Jos malli ehdottaa Windows-ratkaisua, väärää tietokantaa tai unohtaa Ubuntu- ja PostgreSQL-rajaukset, pysäytä demo.
   3. Kysy luokalta: **Huomasitteko, mitä tapahtui? Malli unohti osan alkuperäisestä rajauksesta, eikä se kertonut siitä meille.**
   4. Jos malli muistaa rajaukset, tarkenna kysymystä tai jatka vielä muutamalla kuormittavalla kysymyksellä. Voit kysyä esimerkiksi: `Entä käyttöjärjestelmäkohtaiset asennusvaiheet?`
4. **Korjaus livenä noin 2 minuuttia:**

   Toista alkurajaukset eli ankkuroi tehtävä uudelleen:

   Muistathan, että käytämme Ubuntu 22.04 -käyttöjärjestelmää, PostgreSQL-tietokantaa ja Python 3.9 -versiota.

   Kysy sama kysymys uudelleen:

   Miten asennan tietokantapalvelimen?

   Näytä opiskelijoille, miten **ankkurointi** voi palauttaa vastauksen takaisin oikeaan kontekstiin.
5. **Keskustelu noin 3 minuuttia:**

   Kysy opiskelijoilta:

   - Mitä opimme tekoälyn muistista?
   - Varoittiko malli selvästi, että se oli menettänyt osan kontekstista?
   - Miksi väärä vastaus voi olla vaarallinen, jos se kuulostaa varmalta?
   - Miten ammattilainen voi ehkäistä tällaisia virheitä?

   Kokoa lopuksi tärkein havainto:

   > Tekoäly voi antaa väärän tai väärään kontekstiin perustuvan vastauksen yhtä vakuuttavasti kuin oikean vastauksen. Ammattilaisen vastuulla on tarkistaa, että vastaus noudattaa tehtävän rajauksia.
```

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että tekoäly voi menettää osan kontekstista ilman selkeää varoitusta.
- Opiskelijat ymmärtävät, miksi **ankkurointi**, **dokumentointi** ja vastausten tarkistaminen ovat välttämättömiä taitoja.
- Opiskelijat oppivat, että virheen tapahtuminen ei ole häpeällistä, mutta virheen tunnistaminen ja korjaaminen on osa ammattitaitoa.

---

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- selittää, mitä **konteksti-ikkuna** tarkoittaa ja miksi sen rajallisuus vaikuttaa tekoälyn käyttöön,
- tunnistaa tilanteita, joissa tekoälyn vastaus alkaa irrota alkuperäisestä kontekstista,
- suunnitella laajan tehtävän pilkkominen hallittaviin osiin,
- käyttää **tiivistämistä** ja **ankkurointia** pitkissä tekoälyavusteisissa tehtävissä,
- tarkistaa, noudattaako tekoälyn vastaus annettuja rajauksia ja tavoitteita,
- korjata kontekstin katoamista toistamalla tehtävän keskeiset rajaukset ja tavoitteen.

---
