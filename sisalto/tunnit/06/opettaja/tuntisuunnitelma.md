# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

Tämän lohkon tavoitteena on, että opiskelija ymmärtää, mitä **multimodaalisuus** tarkoittaa tekoälyn käytössä ja miten erilaisia tietomuotoja voidaan hyödyntää IT-ongelmien ratkaisemisessa. Oppitunnin ydin on, että tekoälylle voidaan antaa tekstin lisäksi myös esimerkiksi kuvia, kuvakaappauksia, koodia, lokeja ja taulukoita. Samalla opiskelijan täytyy oppia valitsemaan, mitä materiaalia kannattaa antaa tekoälylle ja missä muodossa.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, että **multimodaalisuus** tarkoittaa tekoälyn kykyä käsitellä useita tietomuotoja, kuten tekstiä, kuvia, koodia ja lokeja.
- Opiskelija ymmärtää, että kuvakaappaukset voivat parantaa kontekstia erityisesti visuaalisissa IT-ongelmissa.
- Opiskelija tunnistaa, että kaikki tekoälymallit eivät ole multimodaalisia.
- Opiskelija ymmärtää, että multimodaalinen konteksti kuluttaa konteksti-ikkunaa ja voi lisätä token-kustannuksia.

### Soveltaa ja analysoida

- Opiskelija osaa arvioida, milloin kannattaa käyttää tekstiä, milloin kuvakaappausta ja milloin molempia.
- Opiskelija osaa rakentaa tehokkaan **multimodaalisen kontekstin** IT-ongelman ratkaisemiseksi.
- Opiskelija osaa tunnistaa tilanteita, joissa kuvakaappaus auttaa tekoälyä enemmän kuin pelkkä sanallinen kuvaus.
- Opiskelija osaa tunnistaa tilanteita, joissa teksti on parempi syötemuoto kuin kuva.

### Luoda ja arvioida

- Opiskelija osaa valita tehtävään sopivan materiaalin tekoälylle: tekstin, kuvan, lokin, koodin tai näiden yhdistelmän.
- Opiskelija osaa perustella, miksi tietty materiaali annetaan tekoälylle ja miksi jokin muu materiaali jätetään pois.
- Opiskelija ymmärtää multimodaalisten mallien rajoitukset ja tekee niiden perusteella tarkoituksenmukaisia valintoja.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että multimodaalisuus ei tarkoita kaiken materiaalin lisäämistä kerralla. Vastuullinen käyttäjä valitsee tehtävän kannalta olennaisen tiedon: joskus paras syöte on kuvakaappaus, joskus lokirivi tekstinä ja joskus näiden yhdistelmä.

---

## Pedagoginen lähestymistapa

### Ydinviesti: tekoälylle voidaan näyttää muutakin kuin tekstiä

Oppitunti kannattaa aloittaa konkreettisella IT-tilanteella. Esimerkiksi opiskelija voi yrittää selittää käyttöliittymävirhettä sanallisesti: ”Painike on oudossa paikassa ja värit näyttävät vääriltä.” Tekoäly voi antaa yleisiä ehdotuksia, mutta kuvakaappauksen avulla se näkee asettelun, värit, virheilmoituksen sijainnin ja käyttöliittymän kokonaisuuden.

> **Jos ongelma näkyy ruudulla, kuvakaappaus voi olla parempi konteksti kuin pitkä sanallinen selitys.**

Korosta opiskelijoille:

- **Teksti** sopii hyvin koodiin, lokiriveihin, komentoihin ja tarkkoihin virheilmoituksiin.
- **Kuvakaappaus** sopii hyvin käyttöliittymävirheisiin, asetteluun, väreihin, näkymiin ja visuaalisiin ongelmiin.
- **Yhdistelmä** on usein paras ratkaisu: kuva näyttää tilanteen, teksti kertoo tavoitteen, rajaukset ja tarkan ongelman.
- **Kaikkea ei kannata antaa tekoälylle kerralla**, koska konteksti-ikkuna ja token-kustannukset ovat rajallisia.

### Milloin teksti, milloin kuva?

Opiskelijoiden pitää oppia valitsemaan syötemuoto tehtävän mukaan. Tärkeää on kysyä: mikä tieto on ongelman ratkaisemisen kannalta olennaista, ja missä muodossa se välittyy tekoälylle parhaiten?

| Tilanne | Paras muoto | Perustelu |
| --- | --- | --- |
| Koodissa on virhe, ja opiskelija haluaa korjausehdotuksen. | **Koodi tekstinä** | Tekoäly voi lukea ja muokata tekstimuotoista koodia tarkasti. |
| Sivun asettelu näyttää väärältä selaimessa. | **Kuvakaappaus + lyhyt selitys** | Visuaalinen tieto, kuten sijainti, värit ja asettelu, näkyy kuvasta paremmin kuin sanallisesta kuvauksesta. |
| Palvelimen lokissa näkyy virheitä. | **Olennaiset lokirivit tekstinä** | Tekstinä lokit ovat pienempiä, helpommin haettavia ja tarkemmin käsiteltäviä kuin kuvakaappauksena. |
| Käyttöliittymässä näkyy virheilmoitus, mutta sen sijainti ja ympäristö ovat tärkeitä. | **Kuvakaappaus + virheilmoitus tekstinä** | Kuva näyttää kontekstin, ja tekstinä annettu virheilmoitus varmistaa, että tekoäly lukee sen oikein. |

### Multimodaalisen kontekstin rakentaminen

Hyvä multimodaalinen konteksti ei ole pelkkä kuvakaappaus. Sen ympärille tarvitaan selitys: mitä kuvassa pitäisi huomata, mikä on tavoite ja mitä tekoälyltä pyydetään.

Opeta opiskelijoille seuraava rakenne:

1. **Tavoite:** Mitä haluat selvittää tai korjata?
2. **Materiaali:** Mitä annat tekoälylle: kuva, koodi, loki, taulukko vai useampi näistä?
3. **Rajaus:** Mihin tekoälyn pitää keskittyä?
4. **Toivottu vastausmuoto:** Haluatko tarkistuslistan, korjausehdotuksen, selityksen vai vaiheittaisen ohjeen?

**TAVOITE:** Selvitä, miksi kirjautumissivun painike ei näy oikein mobiilinäkymässä.

**MATERIAALI:** Liitän kuvakaappauksen mobiilinäkymästä ja CSS-koodin tekstinä.

**RAJAUS:** Keskity vain painikkeen sijaintiin ja näkyvyyteen, älä ehdota koko ulkoasun uudistamista.

**VASTAUSMUOTO:** Anna kolme todennäköisintä syytä ja niiden tarkistusvaiheet.

### Token-kustannukset ja konteksti-ikkuna

Multimodaalisuus liittyy suoraan aiempaan konteksti-ikkunan hallintaan. Kuvakaappaus voi viedä paljon enemmän tilaa kontekstista kuin lyhyt tekstinpätkä. Siksi opiskelijan pitää valita kuvat harkiten.

**Opettajan huomio:** Käytä token-kustannuksia havainnollistavana arviona, ei absoluuttisena totuutena. Kuvan kuluttama konteksti riippuu mallista, kuvan koosta ja käsittelytavasta. Pedagoginen viesti on: kuvat voivat olla kalliimpia kuin teksti, joten niitä käytetään strategisesti.

Korosta opiskelijoille:

- Yksi hyvin valittu kuvakaappaus voi olla arvokkaampi kuin monta epäselvää kuvaa.
- Koodi kannattaa yleensä antaa tekstinä, ei kuvana.
- Lokit kannattaa suodattaa ja kopioida olennaisina riveinä.
- Kuvakaappaus sopii parhaiten silloin, kun ongelman visuaalinen sijainti, asettelu tai näkymä on tärkeä.

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”Multimodaalisuus tarkoittaa, että voin antaa kaiken materiaalin kerralla.”

**Korjaava näkökulma:** Multimodaalisuus on tehokas työkalu, mutta konteksti-ikkuna on edelleen rajallinen. Kuvakaappaukset, pitkät lokit, koodi ja dokumentaatio voivat täyttää ikkunan nopeasti. Vastuullinen käyttäjä valitsee vain olennaisen materiaalin.

> Multimodaalisuus ei tarkoita ”kaikki mukaan”. Se tarkoittaa oikea materiaali oikeassa muodossa.

### Väärinkäsitys 2: ”Kuvakaappaukset ovat aina parempia kuin teksti.”

**Korjaava näkökulma:** Kuvakaappaukset ovat hyviä visuaalisissa ongelmissa, mutta eivät aina paras muoto. Jos tekoälyn pitää muokata koodia, koodi kannattaa antaa tekstinä. Teksti on tarkempi, kevyempi ja helpommin muokattava.

### Väärinkäsitys 3: ”Kaikki tekoälymallit osaavat käsitellä kuvia.”

**Korjaava näkökulma:** Kaikki mallit eivät ole multimodaalisia. Osa malleista käsittelee vain tekstiä. Vastuullisen käyttäjän pitää tarkistaa, tukeeko käytettävä malli kuvia, tiedostoja tai muita tietomuotoja.

### Väärinkäsitys 4: ”Lokit kannattaa näyttää kuvakaappauksena.”

**Korjaava näkökulma:** Useimmiten lokit kannattaa antaa tekstinä. Tekstimuotoiset lokirivit ovat kevyempiä, tarkempia ja helpompia analysoida. Kuvakaappausta voi käyttää, jos lokin ympäristö tai käyttöliittymä on olennainen, mutta itse lokitiedot kannattaa yleensä kopioida tekstinä.

### Väärinkäsitys 5: ”Kuva riittää ilman selitystä.”

**Korjaava näkökulma:** Kuva antaa visuaalista tietoa, mutta tekoäly tarvitsee silti tehtävänannon. Ilman tavoitetta ja rajausta malli voi keskittyä vääriin asioihin tai antaa liian yleisen vastauksen.

---

## Opettajan fasilitointiohjeet

### Ennen oppituntia

- Testaa tehtävä 6.1 etukäteen ja vertaa, miten tekoälyn vastaus muuttuu, kun käytössä on pelkkä sanallinen kuvaus, pelkkä kuvakaappaus ja näiden yhdistelmä.
- Valitse konkreettinen IT-ongelma, jonka opiskelijat tunnistavat. Hyviä aiheita ovat käyttöliittymävirhe, lomakkeen virheilmoitus, CSS-asetteluongelma, mobiilinäkymän ongelma tai kirjautumissivun virhe.
- Tarkista, mitä multimodaalisia ominaisuuksia käytössä oleva tekoälymalli tukee. Voiko se käsitellä kuvia, tiedostoja, taulukoita tai koodia?
- Valmistele esimerkki, jossa koodi annetaan tekstinä ja käyttöliittymävirhe kuvana. Tämä havainnollistaa, miksi yhdistelmä voi olla paras.

### Oppitunnin aikana

- **Avaa konkreettisella esimerkillä:** ”Tekoäly voi nyt nähdä kuvia. Mitä tämä muuttaa IT-tuen, ohjelmoinnin ja käyttöliittymäongelmien ratkaisemisessa?”
- **Näytä vastausten ero:** anna tekoälylle ensin pelkkä sanallinen kuvaus ongelmasta ja sen jälkeen kuvakaappaus. Vertailu tekee oppimisen näkyväksi.
- **Korosta valinnan tärkeyttä:** opiskelijan pitää osata päättää, mitä materiaalia annetaan ja mitä jätetään pois.
- **Palaa konteksti-ikkunaan:** multimodaalinen tieto vie tilaa. Jokainen kuva, pitkä loki tai suuri kooditiedosto vaikuttaa siihen, mitä muuta mahtuu mukaan.
- **Käytä opiskelijoiden IT-maailmaa:** harjoittele kuvakaappausten, koodin ja lokien valintaa tilanteissa, joita opiskelijat kohtaavat opinnoissaan.

### Yleisiä haasteita ja ratkaisuja

**Haaste: Opiskelijat kysyvät, miksi pitäisi käyttää kuvakaappausta, jos tilanteen voi selittää sanallisesti.**
**Ratkaisu:** Näytä kaksi vastausta rinnakkain. Pelkkä sanallinen kuvaus tuottaa usein yleisemmän vastauksen, kun taas kuvakaappaus auttaa tunnistamaan visuaalisen ongelman tarkemmin.

**Haaste: Opiskelijat ylikuormittavat kontekstia kuvilla.**
**Ratkaisu:** Ohjaa heitä valitsemaan 1–2 olennaista kuvakaappausta ja antamaan muu materiaali tekstinä. Kysy: ”Mikä kuvassa on ratkaisemisen kannalta välttämätöntä?”

**Haaste: Opiskelijat eivät tiedä, tukeeko malli kuvia.**
**Ratkaisu:** Opeta tarkistamaan mallin ominaisuudet ennen tehtävän aloittamista. Vastuullinen käyttäjä ei oleta, vaan varmistaa, mitä työkalu osaa.

---

## Luokkatehtävien ohjeistus

### TT-A: Pelkkä teksti vs. kuvakaappaus

**Tavoite:** Opiskelija näkee konkreettisesti, miten kuvakaappaus voi parantaa tekoälyn antamaa vastausta visuaalisessa IT-ongelmassa.

**Tehtävä:** Opiskelija kuvaa IT-ongelman ensin pelkällä tekstillä. Sen jälkeen hän antaa tekoälylle saman ongelman kuvakaappauksen kanssa. Lopuksi hän vertailee vastauksia.

| Versio | Mitä annetaan tekoälylle? | Mitä arvioidaan? |
| --- | --- | --- |
| **Versio 1** | Pelkkä sanallinen kuvaus ongelmasta. | Onko vastaus yleinen vai tarkka? |
| **Versio 2** | Sama kuvaus + kuvakaappaus. | Huomaako tekoäly asioita, joita tekstissä ei kerrottu? |

**Ohje opiskelijalle:**

1. Valitse visuaalinen IT-ongelma, esimerkiksi käyttöliittymävirhe, väärä asettelu tai virheilmoitus ruudulla.
2. Kirjoita ongelmasta ensin pelkkä sanallinen kuvaus.
3. Pyydä tekoälyltä apua ja tallenna vastaus.
4. Lisää kuvakaappaus ja sama tehtävänanto.
5. Vertaa vastauksia: kumpi oli tarkempi, hyödyllisempi ja miksi?

**Aika-arvio:** 20–25 minuuttia

---

### TT-B: Multimodaalisen kontekstin rakentaminen

**Tavoite:** Opiskelija osaa valita, mitä materiaalia tekoälylle kannattaa antaa ja missä muodossa.

**Tehtävä:** Opiskelija rakentaa multimodaalisen kontekstin valittuun IT-ongelmaan. Kontekstissa pitää olla vähintään kaksi tietomuotoa, esimerkiksi kuvakaappaus ja tekstinä annettu virheilmoitus, koodi tai lokirivi.

| Kontekstin osa | Opiskelijan valinta | Perustelu |
| --- | --- | --- |
| **Kuva tai kuvakaappaus** | Mikä kuva annetaan? | Miksi tämä kuva on olennainen? |
| **Teksti** | Mikä virheilmoitus, koodi, loki tai selitys annetaan tekstinä? | Miksi tämä kannattaa antaa tekstinä eikä kuvana? |
| **Rajaus** | Mihin tekoälyn pitää keskittyä? | Miten rajaus vähentää turhaa vastausta? |

**Ohje opiskelijalle:**

1. Valitse IT-ongelma, jossa on sekä visuaalista että tekstimuotoista tietoa.
2. Päätä, mikä tieto kannattaa antaa kuvana.
3. Päätä, mikä tieto kannattaa antaa tekstinä.
4. Kirjoita tekoälylle selkeä tavoite ja rajaus.
5. Perustele, miksi valitsit juuri nämä materiaalit.

**Aika-arvio:** 25–30 minuuttia

---

## Arviointivinkit

### Tehtävän TT-A jälkeen

- Tarkista opiskelijoiden vertailu. Huomasivatko he eron pelkän tekstin ja kuvakaappauksen välillä?
- Kysy: ”Missä tilanteessa kuvakaappaus oli olennainen?” Hyvä vastaus liittyy esimerkiksi väriin, asetteluun, sijaintiin, näkymään tai käyttöliittymän visuaaliseen tilaan.
- Jos opiskelija ei näe eroa, tarkista, oliko valittu ongelma oikeasti visuaalinen vai olisiko se sopinut paremmin tekstinä käsiteltäväksi.

### Tehtävän TT-B jälkeen

- Tarkista, osoittaako opiskelijan multimodaalinen konteksti strategista ajattelua.
- Etsi merkkejä siitä, että opiskelija ymmärtää konteksti-ikkunan ja token-kustannusten vaikutuksen.
- Kysy: ”Miksi valitsit tämän materiaalin?” ja ”Miksi jätit tuon pois?”
- Hyvä vastaus osoittaa, että materiaali valittiin olennaisuuden, tarkkuuden ja kontekstin säästämisen perusteella.

---

## Jatkuva integraatio jatkoprojekteissa

### Jokainen projekti voi hyödyntää multimodaalisuutta

Kun opiskelijat käyttävät tekoälyä jatkossa, ohjaa heitä miettimään, mikä tietomuoto auttaa parhaiten. Koodia ei yleensä kannata kuvata, vaan se kannattaa kopioida tekstinä. Käyttöliittymävirhe taas kannattaa usein näyttää kuvakaappauksena.

### Ammattitaito IT-työssä

Multimodaalisen kontekstin rakentaminen on tärkeä teknisen alan osaajan taito. Se, joka osaa antaa tekoälylle oikean kuvakaappauksen, olennaiset lokirivit ja selkeän rajauksen, saa parempia vastauksia nopeammin.

### Konteksti-kolmikon viimeinen osa

Tämä oppitunti viimeistelee kurssin kontekstia käsittelevän kokonaisuuden. Ensin opiskelijat oppivat, mitä konteksti ja promptaus ovat. Sen jälkeen he oppivat hallitsemaan konteksti-ikkunaa pitkissä projekteissa. Nyt he oppivat käyttämään erilaisia tietomuotoja tarkoituksenmukaisesti.

**Opettajan muistutus:** Yhdessä nämä kolme taitoa muodostavat tekoälyn ammattimaisen käytön perustan: anna oikea konteksti, hallitse konteksti-ikkunaa ja valitse oikea tietomuoto.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että multimodaalisuus tekee tekoälystä hyödyllisemmän IT-työssä, mutta vain silloin, kun sitä käytetään harkiten. Kuvakaappaus voi ratkaista ongelman, jota on vaikea selittää sanallisesti. Toisaalta koodi, lokit ja virheilmoitukset kannattaa usein antaa tekstinä, koska ne ovat tarkempia ja helpommin muokattavia.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Milloin sinun kannattaa näyttää tekoälylle kuva ongelmasta, ja milloin sama tieto kannattaa antaa tekstinä?

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **aineistovalinta- ja redaktointilomake**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–10 min | Virittäytyminen | Kytke ydinkysymys tuttuun tilanteeseen ja tarkista lähtötaso. |
| 10–25 min | Ydinkäsite | Mallinna tunnin keskeinen ero yhdellä vastaesimerkillä. |
| 25–65 min | Perustuotos | Oppija valitsee kaksi aineistomuotoa ja perustelee, mitä lisätietoa kumpikin tuo sekä mitä poistetaan. Tämä 40 minuutin jakso on itsenäistä tai parin kanssa tehtävää työskentelyä. |
| 65–80 min | Testaus ja purku | Testauta tuotos annetulla tapauksella ja pura yksi onnistuminen sekä yksi korjaus. |
| 80–90 min | Tallennus ja exit ticket | Varmista tiedoston nimi, tallennuspaikka ja yhden lauseen johtopäätös. |

### Tukireitti

Oppija käyttää valmista tapausta ja redaktointilistaa. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis, oppija perustelee myös, miksi yksi tarjolla oleva aineisto jätetään pois. Syventävä työ ei kasvata pakollista ydintuotosta.
