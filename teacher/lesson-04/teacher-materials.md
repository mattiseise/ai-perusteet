# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

Tämän lohkon tavoitteena on, että opiskelija ymmärtää **kontekstin** ja **promptin** merkityksen tekoälyn kanssa työskentelyssä. Oppitunnin ydin on, että tekoälyltä saatu vastaus ei riipu vain kysymyksestä, vaan myös siitä, millaisen tilanteen, taustan, tavoitteen ja rajaukset käyttäjä antaa.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, että **konteksti** on tekoälyviestinnän perusta.
- Opiskelija tunnistaa kontekstin viisi keskeistä osaa: **rooli**, **taustatieto**, **tavoite**, **rajaukset** ja **esimerkit**.
- Opiskelija ymmärtää, että **prompti** on kysymys tai tehtävänanto, joka rakentuu kontekstin päälle.
- Opiskelija tunnistaa hyvän promptin viisi elementtiä: **tavoite**, **rooli**, **rajoitukset**, **outputformaatti** ja **esimerkit**.

### Soveltaa ja analysoida

- Opiskelija osaa erottaa **hyvän kontekstin** ja **hyvän promptin** toisistaan.
- Opiskelija osaa arvioida, miksi sama prompti voi tuottaa erilaisia vastauksia eri kontekstissa.
- Opiskelija osaa tunnistaa tilanteita, joissa tekoäly joutuu arvaamaan, koska konteksti tai prompti on puutteellinen.

### Luoda ja arvioida

- Opiskelija osaa rakentaa omasta IT-ongelmastaan selkeän kontekstin ja terävän promptin.
- Opiskelija osaa käyttää kontekstia ja promptia iteratiivisesti: ensin luodaan pohja, sitten tarkennetaan vastausten perusteella.
- Opiskelija ymmärtää, että hyvä konteksti ja prompti säästävät aikaa ja tuottavat ammattimaisempia, käyttökelpoisempia vastauksia.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että hyvä tekoälyvastaus syntyy kahdesta asiasta: hyvästä kontekstista ja terävästä promptista. Prompti kertoo, mitä tekoälyn pitää tehdä. Konteksti kertoo, missä tilanteessa tehtävä tehdään.

---

## Pedagoginen lähestymistapa

### Ydinviesti: konteksti on pohja, prompti on tehtävänanto

Opiskelijoille kannattaa havainnollistaa kontekstin ja promptin ero arkisella esimerkillä. Jos saat kaverilta viestin ”Tää ei toimi”, et voi auttaa luotettavasti ilman lisätietoja. Tarvitset kontekstia: mistä on kyse, mitä toinen yritti tehdä, milloin ongelma alkoi, näkyykö jokin virheilmoitus ja mitä on jo kokeiltu.

> **Konteksti kertoo tilanteen. Prompti kertoo tehtävän.**

Korosta opiskelijoille:

- **Konteksti** antaa taustan, jonka perusteella tekoäly ymmärtää tilanteen paremmin.
- **Prompti** ohjaa tekoälyä tekemään tietyn tehtävän kontekstin perusteella.
- Hyvä konteksti ilman selkeää promptia voi tuottaa epätarkan vastauksen.
- Hyvä prompti ilman kontekstia voi tuottaa väärän tai liian yleisen vastauksen.

### Kontekstin viisi osaa

Konteksti ei tarkoita vain pitkää tekstimassaa. Hyvä konteksti on jäsennelty ja sisältää tehtävän kannalta olennaiset tiedot. Opeta opiskelijoille viiden osan malli.

| Kontekstin osa | Mitä se kertoo? | IT-esimerkki |
| --- | --- | --- |
| **Rooli** | Kuka käyttäjä on ja millä osaamistasolla hän toimii? | ”Olen ensimmäisen vuoden IT-opiskelija.” |
| **Taustatieto** | Mitä tilanteesta tiedetään jo? | ”Harjoittelen Linux-palvelimen SSH-yhteyttä.” |
| **Tavoite** | Mitä käyttäjä haluaa saavuttaa? | ”Haluan selvittää, miksi yhteys ei muodostu.” |
| **Rajaukset** | Mitä ei saa tehdä tai mitä pitää huomioida? | ”Älä ehdota palvelimen uudelleenasennusta.” |
| **Esimerkit** | Mitä konkreettista tekoäly näkee? | Virheilmoitus, komento, lokirivi tai kuvakaappaus. |

### Promptin viisi elementtiä

Kun konteksti on rakennettu, sen päälle kirjoitetaan prompti. Promptin tehtävä on ohjata tekoälyä tuottamaan juuri sellainen vastaus, jota käyttäjä tarvitsee.

| Promptin elementti | Mitä se ohjaa? | Esimerkki |
| --- | --- | --- |
| **Tavoite** | Mitä tekoälyn pitää tehdä? | ”Auta minua selvittämään virheen todennäköisin syy.” |
| **Rooli** | Mistä näkökulmasta tekoäly vastaa? | ”Vastaa kuin kärsivällinen IT-opettaja.” |
| **Rajoitukset** | Mitä vastaus ei saa sisältää tai tehdä? | ”Älä anna valmista ratkaisua ennen kuin selität tarkistusvaiheet.” |
| **Outputformaatti** | Millaisessa muodossa vastaus annetaan? | ”Anna vastaus numeroituna tarkistuslistana.” |
| **Esimerkit** | Millainen vastaus tai syöte toimii mallina? | ”Tässä on virheilmoitus: Permission denied (publickey).” |

**Opettajan huomio:** Hyvä prompti ei korvaa kontekstia. Terävä prompti ilman taustatietoa johtaa helposti yleisiin vastauksiin. Hyvä konteksti ilman selkeää tehtävänantoa voi taas tuottaa vastauksen, joka ei tee sitä, mitä opiskelija tarvitsi.

### Iteratiivinen työskentely

Opiskelijoiden kannattaa ymmärtää kontekstin ja promptin rakentaminen **iteratiivisena prosessina**. Ammattilaiset eivät aina kirjoita täydellistä promptia ensimmäisellä yrityksellä. He aloittavat olennaisesta, lukevat vastauksen, tarkentavat kontekstia ja muokkaavat promptia seuraavalla kierroksella.

1. **Ensimmäinen kierros:** anna peruskonteksti ja päätehtävä.
2. **Tarkistus:** arvioi, mikä vastauksessa oli hyödyllistä ja mikä jäi puuttumaan.
3. **Tarkennus:** lisää puuttuva taustatieto, rajaus tai esimerkki.
4. **Uusi prompti:** pyydä tarkempi vastaus halutussa muodossa.

> **Hyvä tekoälytyöskentely ei ole yksi täydellinen kysymys. Se on ohjattu keskustelu.**

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”Hyvä prompti tarkoittaa automaattisesti hyvää vastausta.”

**Korjaava näkökulma:** Hyvä vastaus syntyy hyvästä kontekstista ja terävästä promptista yhdessä. Prompti on kysymys tai tehtävä, mutta konteksti antaa tilanteen, johon vastaus sovitetaan. Sama prompti voi tuottaa hyvin erilaisen vastauksen, jos konteksti vaihtuu.

> Prompti kertoo, mitä tehdään. Konteksti kertoo, miksi, kenelle ja missä tilanteessa.

### Väärinkäsitys 2: ”Konteksti ja prompti ovat sama asia.”

**Korjaava näkökulma:** Ne liittyvät toisiinsa, mutta eivät ole sama asia. Konteksti on pohja: rooli, taustatieto, tavoite, rajaukset ja esimerkit. Prompti on tehtävänanto, joka käyttää tätä pohjaa.

### Väärinkäsitys 3: ”Konteksti tarkoittaa vain pitkää tekstiä.”

**Korjaava näkökulma:** Pitkä teksti ei ole automaattisesti hyvä konteksti. Hyvä konteksti on jäsennelty, tarpeellinen ja tehtävän kannalta olennainen. Lyhyt ja selkeä konteksti on usein parempi kuin pitkä ja sekava taustoitus.

### Väärinkäsitys 4: ”Tekoäly ymmärtää aina, mitä tarkoitan.”

**Korjaava näkökulma:** Tekoäly tekee oletuksia, jos tieto puuttuu. Nämä oletukset voivat olla vääriä. Jos opiskelija ei kerro rooliaan, tavoitteitaan, rajoituksiaan tai esimerkkejään, tekoäly täyttää aukot itse.

### Väärinkäsitys 5: ”Hyvä prompti riittää ilman kontekstia.”

**Korjaava näkökulma:** Hyvä prompti ilman kontekstia voi silti tuottaa väärän tai liian yleisen vastauksen. Tekoäly ei tiedä käyttäjän osaamistasoa, tehtävän tarkoitusta tai rajoituksia, ellei niitä kerrota.

### Väärinkäsitys 6: ”Konteksti ja prompti ovat ylimääräistä työtä.”

**Korjaava näkökulma:** Hyvä konteksti ja prompti säästävät aikaa. Muutama lisärivi alussa voi vähentää väärien vastausten, korjauskierrosten ja turhan säätämisen määrää.

---

## Opettajan fasilitointiohjeet

### Ennen oppituntia

- Lue oppilasmateriaali ja varmista, että osaat erottaa **kontekstin viisi osaa** ja **promptin viisi elementtiä**.
- Valitse konkreettiset IT-esimerkit, jotka sopivat opiskelijoiden tasolle. Hyviä aiheita ovat esimerkiksi Linux, Python, SQL, verkkoyhteydet, kirjautumisongelmat tai virheilmoitusten tulkinta.
- Testaa tehtävä 4.1 etukäteen oikealla tekoälyllä. Vertaa, miten vastaus muuttuu, kun heikko kysymys korvataan hyvällä kontekstilla ja terävällä promptilla.
- Valmistele opettajajohtoiseen tehtävään 4.2 malli, jossa rakennetaan ensin konteksti ja sen jälkeen prompti.

### Oppitunnin aikana

- **Aloita johdantoskenaariolla:** ”Saat kaverilta viestin: Tää ei toimi.” Kysy opiskelijoilta, mitä lisätietoa he tarvitsisivat. Tämä johdattaa kontekstin käsitteeseen.
- **Jatka promptiin:** Kun konteksti on selvitetty, kysy opiskelijoilta, mitä tekoälyltä kannattaisi pyytää. Tämä auttaa näkemään, että prompti rakentuu kontekstin päälle.
- **Piirrä kaksi mallia näkyviin:** kontekstin viisi osaa ja promptin viisi elementtiä. Palaa niihin harjoitusten aikana.
- **Käytä opiskelijoiden omia esimerkkejä:** rakenna esimerkit opiskelijoiden omista aiheista ja aloista. Jos ryhmällä on yhteinen projekti tai harrastus, ammenna siitä.
- **Korosta iterointia:** ammattilaiset eivät aina kirjoita täydellistä promptia ensimmäisellä yrityksellä. He tarkentavat kontekstia ja promptia vastausten perusteella.

### Yleisiä haasteita ja ratkaisuja

**Haaste: Opiskelijat antavat liian yleisiä konteksteja tai heikkoja prompteja.**
**Ratkaisu:** Pyydä opiskelijoita lisäämään konkreettinen esimerkki: virheilmoitus, koodinpätkä, komento, lokirivi tai kuvakaappauksen sisältö. Kysy: ”Mitä tekoäly ei voi tietää, ellet kerro sitä?”

**Haaste: Opiskelijat sekoittavat kontekstin ja promptin.**
**Ratkaisu:** Käytä metaforaa: konteksti on huone, jossa keskustelu tapahtuu. Prompti on kysymys, jonka esität siinä huoneessa. Sama kysymys eri huoneessa voi tarkoittaa eri asiaa.

**Haaste: Konteksti ja prompti tuntuvat opiskelijoista liian formaaleilta tai pitkiltä.**
**Ratkaisu:** Näytä, että ne voi kirjoittaa lyhyenä luettelona. Esimerkiksi: ”Rooli: IT-opiskelija. Tausta: harjoittelen SSH-yhteyttä. Tavoite: selvittää virhe. Rajaus: älä ehdota uudelleenasennusta. Prompti: anna tarkistuslista.”

**Haaste: Opiskelijat eivät näe, miksi kontekstin ja promptin kirjoittaminen on hyödyllistä.**
**Ratkaisu:** Näytä ero käytännössä. Syötä tekoälylle ensin heikko kysymys ja sitten sama aihe hyvällä kontekstilla ja promptilla. Anna opiskelijoiden vertailla vastausten tarkkuutta, hyödyllisyyttä ja käyttökelpoisuutta.

---

## Luokkatehtävien ohjeistus

### TT-A: Heikko kysymys vs. hyvä konteksti ja prompti

**Tavoite:** Opiskelija näkee konkreettisesti, miten vastaus muuttuu, kun konteksti ja prompti paranevat.

**Tehtävä:** Opiskelija antaa tekoälylle ensin heikon kysymyksen ja sen jälkeen saman aiheen jäsennellyllä kontekstilla ja promptilla. Lopuksi hän vertailee vastauksia.

| Versio | Esimerkki | Mitä todennäköisesti tapahtuu? |
| --- | --- | --- |
| **Heikko kysymys** | ”Miten debuggaan ohjelmaa?” | Vastaus on yleinen eikä välttämättä auta juuri opiskelijan ongelmaan. |
| **Hyvä konteksti + prompti** | ”Olen aloittelija Pythonissa. Ohjelmani antaa virheen IndexError rivillä 14. Tässä koodi... Auta minua selvittämään virhe vaiheittain ilman valmista ratkaisua.” | Vastaus on tarkempi, käyttökelpoisempi ja paremmin opiskelijan osaamistasoon sopiva. |

**Ohje opiskelijalle:**

1. Kirjoita ensin heikko kysymys tekoälylle.
2. Tallenna tai kopioi vastaus.
3. Rakenna samaan aiheeseen konteksti viiden osan avulla.
4. Kirjoita sen päälle prompti viiden elementin avulla.
5. Vertaa vastauksia: kumpi oli hyödyllisempi ja miksi?

**Aika-arvio:** 20–25 minuuttia

---

### TT-B: Rakenna konteksti ja prompti omasta IT-ongelmasta

**Tavoite:** Opiskelija osaa rakentaa oman IT-ongelmansa pohjalta sekä kontekstin että promptin.

**Tehtävä:** Opiskelija valitsee oman IT-aiheisen ongelman, esimerkiksi virheilmoituksen, koodiongelman, palvelinyhteyden ongelman tai tietokantakyselyn. Hän kirjoittaa ensin kontekstin ja sen jälkeen promptin.

| Osa | Kirjoita tähän |
| --- | --- |
| **Rooli** | Kuka olet ja mikä on osaamistasosi? |
| **Taustatieto** | Mitä olet tekemässä ja mitä olet jo kokeillut? |
| **Tavoite** | Mitä haluat saada aikaan? |
| **Rajaukset** | Mitä tekoäly ei saa tehdä tai mitä sen pitää huomioida? |
| **Esimerkit** | Liitä virheilmoitus, komento, lokirivi, koodi tai muu konkreettinen esimerkki. |

**Promptin tarkistuslista:**

- Onko tehtävän tavoite selkeä?
- Onko tekoälyn rooli määritelty?
- Onko rajoitukset kerrottu?
- Onko vastausmuoto pyydetty?
- Onko mukana esimerkki tai malli?

**Aika-arvio:** 25–30 minuuttia

---

## Arviointivinkit

### Epävirallinen arviointi tehtävän TT-A jälkeen

- Tarkista, huomasiko opiskelija eron vastausten välillä.
- Kuuntele, käyttääkö opiskelija sanoja kuten **spesifisempi**, **relevantimpi**, **käyttökelpoisempi** ja **konkreettisempi**.
- Jos opiskelija sanoo, ettei vastauksissa ollut eroa, pyydä häntä nimeämään, mitä kontekstin osia ja promptin elementtejä hän lisäsi.
- Tarkista, ymmärtääkö opiskelija eron kontekstin ja promptin välillä vai sekoittaako hän ne.

### Epävirallinen arviointi tehtävän TT-B jälkeen

- Sisältääkö opiskelijan konteksti kaikki viisi osaa?
- Sisältääkö opiskelijan prompti kaikki viisi elementtiä?
- Onko mukana konkreettisia esimerkkejä, kuten koodi, virheilmoitus, lokirivi tai komento?
- Onko outputformaatti selkeästi pyydetty?

### Kehittämisalueita

- Jos opiskelija jättää esimerkit pois, kysy: ”Miten tekoäly voi auttaa, jos se ei näe virheilmoitusta tai koodia?”
- Jos rooli on epäselvä, kysy: ”Kuka olet tässä tilanteessa ja kuinka paljon kokemusta sinulla on?”
- Jos promptin formaatti puuttuu, kysy: ”Haluatko vastauksen vaiheina, taulukkona, tarkistuslistana vai lyhyenä tiivistelmänä?”
- Jos rajaukset puuttuvat, kysy: ”Mitä tekoälyn ei pitäisi tehdä tässä tehtävässä?”

---

## Jatkuva integraatio tulevilla oppitunneilla

### Seuraava oppitunti: konteksti-ikkuna

Seuraavalla oppitunnilla opiskelijat oppivat, että konteksti-ikkuna on rajallinen. Tämä oppitunti luo pohjan sille, että opiskelijat ymmärtävät, miksi kontekstia pitää priorisoida. Kun kaikkea ei voi antaa tekoälylle kerralla, tärkeää on valita olennaisin rooli, taustatieto, tavoite, rajaukset ja esimerkit.

### Multimodaalisuus

Myöhemmillä oppitunneilla konteksti ei ole vain tekstiä. Se voi olla myös kuva, lokitiedosto, taulukko, ruutukaappaus tai datajoukko. Sama periaate pätee: tekoäly tarvitsee tilanteen, tavoitteen ja rajaukset myös silloin, kun syöte on muuta kuin tekstiä.

### Iteratiivinen työskentely

Muistuta opiskelijoita tulevilla oppitunneilla, että kontekstia ja promptia rakennetaan kierros kierrokselta. Ensimmäinen prompti antaa pohjan, seuraava tarkentaa ja kolmas voi pyytää muokkausta, tarkistusta tai toista näkökulmaa.

**Opettajan muistutus:** Tämä oppitunti on kurssin tekoälyviestinnän perusta. Jos opiskelija oppii rakentamaan hyvän kontekstin ja promptin, hän saa myöhemmistä tekoälyharjoituksista huomattavasti enemmän irti.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että tekoälyn kanssa työskentely ei ole pelkkää kysymysten heittämistä. Se on tilanteen jäsentämistä, tavoitteiden määrittelyä, rajausten tekemistä ja vastausmuodon ohjaamista.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Mitä tekoäly tarvitsee tietää, jotta se voi auttaa sinua omassa IT-ongelmassasi ilman turhia arvauksia?

:contentReference[oaicite:0]{index=0}

---
