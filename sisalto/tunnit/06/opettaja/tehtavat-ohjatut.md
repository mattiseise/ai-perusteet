# Opettajavetoiset tehtävät

## Tehtävä 6.1: Multimodaalinen tekoäly vai pelkkä teksti? — live-demonstraatio

### Tavoite

Tehtävän tavoitteena on näyttää opiskelijoille konkreettisesti, miten **kuvakaappaus** ja **tekstikuvaus** voivat yhdessä antaa tekoälylle paremman kontekstin IT-ongelman ratkaisemiseen kuin pelkkä tekstikuvaus.

**Opettajan painotus:** Korosta, että **multimodaalisuus** ei tarkoita vain kuvan lisäämistä tekstin rinnalle. Tärkeää on valita sellainen materiaali, joka oikeasti auttaa tekoälyä ymmärtämään ongelman paremmin.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**

- Valitse ongelma tai tilanne, jossa on selvä visuaalinen osa — arjesta, opiskelusta tai työstä. Sopivia esimerkkejä ovat **virheilmoitus**, käyttöliittymävika, verkkosivun asetteluongelma, konfiguraationäkymä, pesukoneen ohjauspaneeli, laskun taulukko tai väreillä erotellut lokit.
- Ota ongelmasta **kuvakaappaus**.
- Kirjoita samasta ongelmasta noin 150 sanan **tekstikuvaus**.
- Valmistele sama kysymys molempiin testeihin, esimerkiksi: `Mikä on tämän ongelman todennäköinen syy ja miten korjaan sen?`

### Toteutus noin 20 minuuttia

1. **Johdanto noin 2 minuuttia:**


   Kerro opiskelijoille:

   > Tekoäly voi käsitellä muutakin kuin tekstiä. Se voi hyödyntää esimerkiksi kuvia, kuvakaappauksia ja tekstiä yhdessä. Tätä kutsutaan **multimodaalisuudeksi**. Tässä demossa vertaamme, miten tekoälyn vastaus muuttuu, kun se saa pelkän tekstin sijaan myös kuvan.
2. **Ensimmäinen testi: vain teksti noin 5 minuuttia:**

   1. Näytä opiskelijoille ongelman tekstikuvaus.
   2. Lähetä tekstikuvaus tekoälylle ilman kuvaa.
   3. Käytä samaa kysymystä, jonka käytät myös toisessa testissä: `Mikä on tämän ongelman todennäköinen syy ja miten korjaan sen?`
   4. Tallenna tai kopioi tekoälyn vastaus näkyviin vertailua varten.
   5. Kysy opiskelijoilta: **Kuinka hyödyllinen vastaus on? Antaako se tarkan ratkaisun vai jääkö se yleiselle tasolle?**
3. **Toinen testi: teksti ja kuvakaappaus noin 5 minuuttia:**

   1. Näytä opiskelijoille sama tekstikuvaus sekä kuvakaappaus ongelmasta.
   2. Lähetä molemmat tekoälylle.
   3. Käytä täsmälleen samaa kysymystä kuin ensimmäisessä testissä.
   4. Tallenna tai kopioi vastaus vertailua varten.
   5. Kysy opiskelijoilta: **Onko tämä vastaus tarkempi tai käytännöllisempi kuin ensimmäinen? Mitä lisätietoa kuvakaappaus antoi?**
4. **Vastausten vertailu noin 5 minuuttia:**

   Piirrä taululle tai näytä opiskelijoille seuraava vertailutaulukko. Täyttäkää se yhdessä opiskelijoiden havaintojen perusteella.

   | Vastaus | Spesifisyys | Käytännöllisyys | Visuaalisen tiedon hyödyntäminen |
   | --- | --- | --- | --- |
   | **Vain teksti** |  |  |  |
   | **Teksti ja kuva** |  |  |  |

   Kysy opiskelijoilta:

   - Mitä tekoäly pystyi päättelemään pelkästä tekstistä?
   - Mitä lisätietoa kuvakaappaus antoi?
   - Missä kohdassa kuva teki vastauksesta tarkemman?
   - Olisiko kuvakaappaus voinut myös johtaa harhaan? Miksi?
5. **Johtopäätös noin 3 minuuttia:**

   Kerro opiskelijoille:

   > Tärkeä taito on valita oikea konteksti. Jos ongelma näkyy käyttöliittymässä, kuvakaappaus voi olla erittäin hyödyllinen. Jos ongelma näkyy lokissa tai koodissa, teksti, lokirivit tai koodikatkelma voivat olla tärkeämpiä. Usein paras tulos syntyy, kun teksti ja kuva täydentävät toisiaan.

**Esimerkki opetukseen**

Jos kuvakaappauksessa näkyy esimerkiksi lomake, virheilmoitus ja selaimen osoiterivi, kysy opiskelijoilta, mitä näistä tekoäly voi hyödyntää ja mikä tieto olisi pitänyt kirjoittaa tekstinä tarkemmin.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, mitä **multimodaalisuus** tarkoittaa tekoälyn käytössä.
- Opiskelijat näkevät konkreettisesti, miten kuvakaappaus voi parantaa tekoälyn kykyä ymmärtää IT-ongelmaa.
- Opiskelijat ymmärtävät, että kuvakaappaukset eivät ole vain visuaalinen lisä, vaan ne voivat toimia tärkeänä **kontekstitietona**.
- Opiskelijat osaavat arvioida, milloin ongelma kannattaa kuvata tekstillä, milloin kuvalla ja milloin molemmilla.

---

## Tehtävä 6.2: Multimodaalisen kontekstin suunnittelu — ohjattu harjoitus

### Tavoite

Tehtävän tavoitteena on opettaa opiskelijoille, miten rakennetaan tehokas **multimodaalinen konteksti**. Opiskelijat harjoittelevat valitsemaan, milloin tekoälylle kannattaa antaa tekstiä, kuvakaappauksia, lokitietoja, koodia tai näiden yhdistelmä.

**Opettajan painotus:** Korosta, että kaikkea mahdollista materiaalia ei kannata lähettää tekoälylle. Hyvä multimodaalinen konteksti on **valikoitu**, **rajattu** ja **turvallinen**.

### Opettajan ohjeet ja fasilitointi

**Valmistelu:**

- Valitse opiskelijoille tuttu projekti tai ongelmatilanne.
- Sopivia esimerkkejä ovat verkkopalvelun virheen selvittäminen, tietokantaongelma, käyttöliittymävika, ohjelmakoodin virhe tai arkinen tilanne, kuten sovelluksen sekava asetusnäkymä tai epäselvä lasku.
- Valmista lyhyt ongelmakuvaus, jota käytetään harjoituksen pohjana.

### Toteutus noin 25 minuuttia

1. **Asetelman muuttaminen noin 2 minuuttia:**


   Kerro opiskelijoille:

   > Multimodaalinen konteksti ei tarkoita sitä, että tekoälylle annetaan kaikki mahdollinen materiaali kerralla. Ammattimainen tapa on valita tarkoituksenmukainen yhdistelmä eri tietomuotoja.
2. **Vaihe 1: Mitä materiaalia on käytettävissä? noin 5 minuuttia**

   Piirrä taululle tai näytä opiskelijoille seuraava taulukko:

   | Materiaali | Esimerkki | Hyödyt | Rajoitukset |
   | --- | --- | --- | --- |
   | **Teksti** | Lyhyt kuvaus ongelmasta | Nopea, selkeä ja helppo kohdentaa. | Voi jäädä epätarkaksi, jos kuvaaja ei huomaa kaikkea olennaista. |
   | **Kuvakaappaus** | Virheilmoitus tai käyttöliittymänäkymä | Näyttää tilanteen sellaisena kuin käyttäjä sen näkee. | Voi sisältää ylimääräistä tai arkaluonteista tietoa. |
   | **Lokit** | Virherivit palvelimen lokista | Antavat teknisiä yksityiskohtia, aikaleimoja ja virhekoodeja. | Voivat olla pitkiä, sekavia tai sisältää paljon epäolennaista tietoa. |
   | **Koodi** | Funktio, komponentti tai konfiguraatiotiedosto | Näyttää ongelman teknisen rakenteen. | Liian pitkä koodi voi vaikeuttaa olennaisen löytämistä. |

   Kysy opiskelijoilta:

   - Mitä näistä materiaaleista olisi käytettävissä valitussa ongelmatilanteessa?
   - Mikä materiaali olisi todennäköisesti tärkein?
   - Mikä materiaali voisi olla turhaa tai jopa häiritsevää?
3. **Vaihe 2: Miten valitset oikean materiaalin? noin 8 minuuttia**

   Käy läpi valinnan peruslogiikka:

   - **Teksti:** Käytä, kun ongelma voidaan kuvata selkeästi sanallisesti ja haluat rajata tehtävän nopeasti.
   - **Kuvakaappaus:** Käytä, kun visuaalinen tieto on olennainen osa ongelmaa, esimerkiksi värit, asettelu, kuvakkeet, virheilmoituksen sijainti tai käyttöliittymän tila.
   - **Lokit:** Käytä, kun virheen syy näkyy teknisesti lokitiedostossa, virhekoodissa tai aikaleimoissa.
   - **Koodi:** Käytä, kun ongelma liittyy ohjelman toimintaan, funktioon, komponenttiin, rajapintaan tai konfiguraatioon.

   **Esimerkkitilanne:**

   Verkkopalvelussa näkyy virhe 500, kun käyttäjä lähettää lomakkeen.

   Keskustelkaa, mitä materiaalia tekoälylle kannattaisi antaa:

   - **Teksti:** “Käyttäjä saa error 500 -virheen, kun hän lähettää lomakkeen.”
   - **Kuvakaappaus:** näyttää, missä kohtaa sivua virhe näkyy ja mitä käyttäjä näkee.
   - **Lokit:** näyttävät palvelimen virheilmoituksen ja mahdollisen stack tracen.
   - **Koodi:** näyttää lomakkeen käsittelevän kontrollerin tai palvelinpuolen funktion.

   Kysy opiskelijoilta:

   - Mikä näistä auttaisi tekoälyä eniten?
   - Mikä pitäisi rajata vain olennaiseen osaan?
   - Mitä tietoja pitäisi poistaa ennen tekoälylle lähettämistä?
4. **Vaihe 3: Yhdistä materiaalit tehokkaaksi kontekstiksi noin 7 minuuttia**

   Kirjoita taululle malli multimodaalisesta kontekstista:

   1. **Teksti:** Käyttäjä saa error 500 -virheen, kun hän lähettää lomakkeen X.
   2. **Kuvakaappaus:** Näyttää virheilmoituksen käyttäjän näkymässä.
   3. **Lokit:** Viimeiset 5–10 olennaista virheriviä palvelimen lokista.
   4. **Koodi:** Lomakkeen käsittelevä funktio tai kontrollerin osa, jossa virhe todennäköisesti syntyy.
   5. **Kysymys tekoälylle:** `Tunnista todennäköisin syy ja ehdota korjausvaiheet. Kerro myös, mitä tietoa tarvitset lisää, jos ratkaisu ei ole varma.`

   Selitä opiskelijoille:

   > Tämä on tehokas konteksti, koska tekoäly saa ongelmasta useita näkökulmia: käyttäjän kuvauksen, visuaalisen tilanteen, tekniset lokit ja relevantin koodin. Samalla materiaali on rajattu niin, ettei mukana ole kaikkea mahdollista.
5. **Strategia ja rajoitukset noin 3 minuuttia:**

   Korosta opiskelijoille:

   - Kuvakaappauksia kannattaa käyttää harkiten, koska ne voivat viedä paljon kontekstitilaa.
   - Yleensä 1–2 hyvin valittua kuvaa on parempi kuin suuri määrä kuvia.
   - Lokit ja koodi kannattaa rajata olennaisiin kohtiin.
   - Arkaluonteiset tiedot, kuten nimet, sähköpostiosoitteet, käyttäjätunnukset, avaimet ja salasanat, pitää poistaa ennen materiaalin lähettämistä tekoälylle.
   - Jos konteksti alkaa täyttyä, säilytä ensin lyhyt ongelmakuvaus, olennaiset lokit, relevantti koodi ja tiivistelmä aiemmista havainnoista.

**Opettajan tarkistuskysymys:** Jos opiskelijat ehdottavat kaiken materiaalin lähettämistä tekoälylle, kysy: “Mikä tästä on oikeasti välttämätöntä ratkaisun kannalta, ja mikä voi lisätä kohinaa tai tietosuojariskiä?”

### Opiskelijoiden oma harjoitus

Pyydä opiskelijoita valitsemaan yksi ongelma tai tilanne — arjesta, opiskelusta tai työstä — ja suunnittelemaan siihen multimodaalinen konteksti.

| Kontekstin osa | Mitä annetaan tekoälylle? | Miksi tämä osa tarvitaan? | Mitä pitää poistaa tai rajata? |
| --- | --- | --- | --- |
| **Teksti** |  |  |  |
| **Kuvakaappaus** |  |  |  |
| **Lokit** |  |  |  |
| **Koodi** |  |  |  |

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että **multimodaalinen konteksti** on harkittu yhdistelmä eri tietomuotoja.
- Opiskelijat osaavat valita tilanteeseen sopivan materiaalin: tekstin, kuvakaappauksen, lokitiedot, koodin tai näiden yhdistelmän.
- Opiskelijat ymmärtävät, että kaiken materiaalin lähettäminen tekoälylle ei ole tehokasta eikä aina turvallista.
- Opiskelijat osaavat huomioida **konteksti-ikkunan** rajallisuuden ja tietosuojan, kun he käyttävät tekoälyä IT-ongelmien ratkaisemiseen.

---

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- selittää, mitä **multimodaalisuus** tarkoittaa tekoälyn käytössä,
- vertailla pelkän tekstikuvauksen ja tekstin sekä kuvan yhdistelmän hyötyjä,
- tunnistaa, milloin kuvakaappaus parantaa ongelman ymmärtämistä,
- valita IT-ongelman ratkaisemiseen sopivat materiaalit, kuten tekstin, kuvan, lokit ja koodin,
- rajata multimodaalisen kontekstin niin, että mukana on vain olennainen tieto,
- huomioida tietosuoja ja poistaa arkaluonteiset tiedot ennen tekoälyn käyttöä.

---
