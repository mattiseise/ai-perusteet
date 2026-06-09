# Opettajan materiaalit: generatiivisen tekoälyn luonne

## Oppimisen tavoitteet tälle lohkolle

Tämän lohkon tavoitteena on, että opiskelija ymmärtää **generatiivisen tekoälyn** toimintaperiaatteen ja siihen liittyvät rajoitukset. Oppitunnin ydin on, että kielimalli ei ole **totuuskone** tai faktakone, vaan todennäköisyyksiin perustuva **sanojen ja tokenien ennustaja**. Tämä selittää sekä mallien hyödyllisyyden että niiden virheet.

### Muistaa ja ymmärtää

- Opiskelija ymmärtää, miksi generatiiviset kielimallit ovat **epädeterministisiä** eli miksi sama prompti voi tuottaa eri vastauksia eri kerroilla tai eri malleilla.
- Opiskelija ymmärtää, mitä **lämpötila** tekee ja miksi se vaikuttaa vastausten vaihteluun.
- Opiskelija osaa selittää **hallusinaatioiden** perusmekanismin: malli ennustaa todennäköisiä sanoja, ei tarkista faktoja samalla tavalla kuin tietokanta.
- Opiskelija ymmärtää, miksi tekoäly ei ole automaattisesti luotettava tietolähde.

### Soveltaa ja analysoida

- Opiskelija osaa tunnistaa hallusinaation merkkejä käytännössä.
- Opiskelija osaa erottaa mallin itsevarman ilmaisun vastauksen oikeellisuudesta.
- Opiskelija osaa arvioida, milloin tekoälyn vastaus täytyy verifioida erityisen huolellisesti.
- Opiskelija ymmärtää, miksi kriittisissä teknisissä tehtävissä tarvitaan **itsenäinen verifiointiprosessi**.

### Luoda ja arvioida

- Opiskelija osaa rakentaa käytännöllisen tarkistuslistan tekoälyn vastausten arviointiin.
- Opiskelija osaa suunnitella verifiointiprosessin esimerkiksi koodille, SQL-kyselylle, API-kutsulle tai tekniselle ohjeelle.
- Opiskelija osaa yhdistää aiemmat opit tokenien ennustamisesta, kontekstin katoamisesta ja hallusinaatioista ammatilliseen tekoälyn käyttöön.

**Opettajan painotus:** Tämän oppitunnin tärkein viesti on, että tekoälyn itsevarma vastaus ei ole sama asia kuin oikea vastaus. Generatiivinen tekoäly voi olla erittäin hyödyllinen, mutta ammattilaisen vastuulla on tarkistaa kriittiset vastaukset ja käyttää mallia hallitusti.

---

## Pedagoginen lähestymistapa

### Ydinviesti: tekoäly ei ole totuuskone

Tämä oppitunti on käsitteellisesti haastava, koska se vaatii opiskelijalta ajattelutavan muutosta. Monet opiskelijat kokevat tekoälyn käyttäjäystävälliseksi, sujuvaksi ja vakuuttavaksi. Siksi he voivat olettaa, että hyvältä kuulostava vastaus on myös totta.

> **Kielimalli ei kysy: ”Mikä on totta?” Se kysyy matemaattisesti: ”Mikä token näyttää seuraavaksi todennäköiseltä?”**

Paras opetustapa on aloittaa konkreettisista esimerkeistä ennen abstrakteja selityksiä. Näytä ensin, että sama prompti voi tuottaa erilaisia vastauksia. Näytä sitten, että malli voi vastata täysin itsevarmasti väärin. Vasta tämän jälkeen avaa tekninen selitys: malli ennustaa todennäköisiä jatkoja, ei tee faktahakua.

Oppitunnin kolme keskeistä havaintoa ovat:

- **Epädeterminismi:** sama prompti voi tuottaa erilaisia vastauksia, koska malli tekee todennäköisyyspohjaisia valintoja.
- **Hallusinaatiot:** malli voi tuottaa uskottavalta kuulostavia mutta virheellisiä väitteitä.
- **Verifiointi:** kriittinen vastaus täytyy tarkistaa itsenäisesti, erityisesti tekniikassa, ohjelmoinnissa ja päätöksenteossa.

### Epädeterminismi ja lämpötila

**Epädeterminismi** tarkoittaa, että malli ei välttämättä anna aina samaa vastausta samaan promptiin. Kielimalli tekee todennäköisyyspohjaisia valintoja: se arvioi, mitkä tokenit ovat seuraavaksi todennäköisiä, ja valitsee niistä yhden mallin asetusten perusteella.

**Lämpötila** ohjaa sitä, kuinka paljon vaihtelua mallin vastauksessa on. Matala lämpötila tekee vastauksesta ennakoitavamman. Korkeampi lämpötila lisää vaihtelua ja voi tehdä vastauksesta luovemman, mutta myös arvaamattomamman.

| Asetus | Mitä tapahtuu? | Milloin hyödyllinen? |
| --- | --- | --- |
| **Matala lämpötila** | Malli valitsee todennäköisempiä ja ennakoitavampia jatkoja. | Tekniset ohjeet, tiivistelmät, faktapainotteiset tehtävät ja asiakasviestit. |
| **Korkea lämpötila** | Malli valitsee vaihtelevampia ja luovempia jatkoja. | Ideointi, luova kirjoittaminen, vaihtoehtoisten näkökulmien tuottaminen. |

**Analogia opetukseen**

Ajattele rulettipyörää. Matala lämpötila tarkoittaa, että suurin osa painosta on todennäköisimmillä vaihtoehdoilla. Korkea lämpötila jakaa painoa useammille vaihtoehdoille. Jokainen pyöräytys voi tuottaa hieman erilaisen lopputuloksen.

**Opettajan huomio:** Älä selitä lämpötilaa mielentilana. Lämpötila ei tarkoita, että malli on ”rohkea”, ”iloinen” tai ”epävarma” inhimillisessä mielessä. Se on matemaattinen asetus, joka vaikuttaa tokenien valintaan.

### Hallusinaatiot

**Hallusinaatio** tarkoittaa tilannetta, jossa malli tuottaa väärän, keksityn tai tarkistamattoman vastauksen vakuuttavasti. Malli ei valehtele tarkoituksella. Se tuottaa vastauksen, joka näyttää tilastollisesti sopivalta siihen kontekstiin, jossa se toimii.

Hallusinaatioita syntyy erityisesti silloin, kun malli kohtaa aiheita, joissa vastaus näyttää tutulta mutta yksityiskohdat eivät ole varmasti hallussa. Teknisissä tehtävissä tämä voi tarkoittaa esimerkiksi olemattomia API-metodeja, väärin nimettyjä funktioita, virheellisiä komentorivikomentoja tai vanhentuneita kirjastojen käyttötapoja.

| Esimerkki | Miksi se on riski? | Miten tarkistetaan? |
| --- | --- | --- |
| Malli ehdottaa olematonta `urllib3`-funktiota. | Koodi näyttää uskottavalta, mutta ei toimi oikeassa ympäristössä. | Tarkista virallinen dokumentaatio ja testaa koodi erillisessä ympäristössä. |
| Malli antaa historian tai lainsäädännön yksityiskohdan itsevarmasti. | Vastaus voi kuulostaa oikealta, vaikka nimi, vuosiluku tai pykälä on väärä. | Tarkista riippumattomasta luotettavasta lähteestä. |
| Malli kirjoittaa SQL-kyselyn, jossa on väärä sarakenimi. | Kysely voi kaatua tai palauttaa väärää dataa. | Vertaa kyselyä tietokannan skeemaan ja testaa turvallisella testidatalla. |

> **Itsevarmuus ei ole todiste oikeellisuudesta.** Malli voi kuulostaa varmalta myös silloin, kun se on väärässä.

### Totuuskone vs. sanojen ennustaja

Oppitunnin tärkein käsitteellinen ero on **totuuskoneen** ja **sanojen ennustajan** ero. Tämä ero auttaa opiskelijaa muuttamaan tapaa, jolla hän käyttää tekoälyä.

| Ajattelumalli | Miten se toimii? | Esimerkki |
| --- | --- | --- |
| **Totuuskone** | Tarkistaa tiedon luotettavasta lähteestä ja palauttaa täsmällisen vastauksen. | Relaatiotietokanta: `SELECT * FROM customers WHERE last_name = 'Smith'`. |
| **Sanojen ennustaja** | Tuottaa todennäköiseltä näyttävän jatkon annetulle kontekstille. | Kielimalli kirjoittaa vastauksen aiemman tekstin ja koulutusdatan kuvioiden perusteella. |

Tämä ei tarkoita, etteikö tekoäly voisi olla hyödyllinen. Se tarkoittaa, että käyttäjän täytyy ymmärtää, mitä tekoäly tekee ja mitä se ei tee. Tekoäly voi auttaa ideoimaan, selittämään, tiivistämään, kirjoittamaan luonnoksia ja ehdottamaan ratkaisuja. Kriittiset väitteet täytyy kuitenkin tarkistaa.

**Opettajan painotus:** Tekoälyä ei pidä opettaa opiskelijoille joko ihmeenä tai huijauksena. Se on hyödyllinen työkalu, jonka rajat pitää ymmärtää. Ammattilainen käyttää tekoälyä, mutta ei ulkoista sille omaa vastuutaan.

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: ”Malli hallusinoi, koska se on huono.”

**Korjaava näkökulma:** Hallusinaatiot eivät ole vain huonojen mallien ongelma. Ne liittyvät rakenteellisesti siihen, että kielimalli ennustaa todennäköisiä jatkoja eikä tarkista faktoja kuten tietokanta. Parempi malli voi hallusinoida vähemmän, mutta hallusinaatioiden mahdollisuutta ei voi poistaa kokonaan.

> Hallusinaatio ei ole vain virheellinen vastaus. Se on muistutus siitä, millainen työkalu kielimalli on.

### Väärinkäsitys 2: ”Matala lämpötila poistaa hallusinaatiot.”

**Korjaava näkökulma:** Matala lämpötila vähentää satunnaisuutta, mutta ei poista hallusinaatioita. Malli voi antaa hyvin johdonmukaisen ja itsevarman vastauksen, joka on silti väärä. Siksi verifiointi on tarpeen myös matalalla lämpötilalla.

### Väärinkäsitys 3: ”Jos malli kuulostaa varmalta, se tietää, mistä puhuu.”

**Korjaava näkökulma:** Mallin itsevarmuus on tekstin tyyliä, ei totuuden mittari. Malli ei välttämättä tiedä, että se on väärässä, eikä se aina varoita käyttäjää epävarmuudestaan. Siksi käyttäjän pitää erottaa vakuuttava muoto ja todellinen oikeellisuus.

### Väärinkäsitys 4: ”Tekoälyn vastaus riittää, jos se näyttää järkevältä.”

**Korjaava näkökulma:** Teknisessä työssä järkevältä näyttävä vastaus voi silti olla vaarallinen. Koodi voi sisältää väärän metodin, komento voi toimia eri tavalla kuin malli väittää ja ohje voi perustua vanhentuneeseen kirjastoversioon. Kriittiset vastaukset tarkistetaan aina.

### Väärinkäsitys 5: ”Verifiointi tarkoittaa vain sitä, että luen vastauksen nopeasti läpi.”

**Korjaava näkökulma:** Silmäily ei ole verifiointiprosessi. Verifiointi tarkoittaa, että vastaus tarkistetaan lähteestä, dokumentaatiosta, testistä tai toisesta riippumattomasta menetelmästä.

---

## Opettajan fasilitointiohjeet

### Ennen oppituntia

- Testaa etukäteen harjoitus, jossa sama prompti annetaan eri malleille tai samalle mallille useita kertoja. Valitse prompti, joka tuottaa selvästi hieman erilaisia vastauksia.
- Valitse 2–3 hallusinaatioesimerkkiä, jotka sopivat opiskelijoiden osaamistasoon. IT-opiskelijoille tekniset esimerkit, kuten API:t, kirjastot, komennot ja SQL-kyselyt, ovat usein tehokkaampia kuin yleishistoria.
- Varmista, että hallusinaatioesimerkit voi tarkistaa nopeasti virallisesta dokumentaatiosta tai muusta luotettavasta lähteestä.
- Valmistele verifiointiprosessin malli, jota opiskelijat voivat soveltaa omiin tehtäviinsä.

### Oppitunnin aikana

- **Aloita havainnolla:** näytä sama prompti eri malleille tai aja sama prompti useamman kerran. Keskustelkaa, miksi vastaukset eroavat.
- **Siirry hallusinaatioon:** näytä vastaus, joka kuulostaa oikealta mutta sisältää virheen. Anna opiskelijoiden etsiä virhe.
- **Selitä vasta lopuksi mekanismi:** kun opiskelijat ovat nähneet ilmiön, selitä next-token prediction, lämpötila ja todennäköisyysvalinnat.
- **Pidä painopiste ammatillisessa toiminnassa:** tärkeintä ei ole vain tietää, että hallusinaatioita on, vaan osata toimia oikein niiden riskin kanssa.

### Yleisiä haasteita ja ratkaisuja

**Haaste: Opiskelijat ajattelevat, että tekoäly on epäluotettava eikä sitä kannata käyttää.**
**Ratkaisu:** Korosta, että työkalu on hyödyllinen, kun sen rajat ymmärretään. Tavoite ei ole hylätä tekoälyä, vaan käyttää sitä ammattimaisesti.

**Haaste: Opiskelijat eivät löydä hallusinaatiota.**
**Ratkaisu:** Pyydä heitä etsimään liian tarkkoja väitteitä: funktioiden nimiä, versioita, vuosilukuja, komentoja tai lähdeviittauksia. Kysy: ”Voitko varmistaa tämän riippumattomasta lähteestä?”

**Haaste: Verifiointi jää yleiseksi.**
**Ratkaisu:** Vaadi konkreettinen tarkistusaskel. ”Tarkistan” ei riitä. Kysy: mistä tarkistat, miten tarkistat, missä ympäristössä testaat ja mitä dokumentoit?

---

## Luokkatehtävien ohjeistus

### TT-A: Sama prompti, eri vastaukset

**Tavoite:** Opiskelija ymmärtää epädeterminismiä ja mallien välisiä eroja käytännössä.

**Tehtävä:** Anna sama prompti kahdelle eri tekoälymallille tai samalle mallille useita kertoja. Vertaa vastauksia.

| Kysymys | Havainto | Mitä tämä opettaa? |
| --- | --- | --- |
| Ovatko vastaukset täysin samat? | Usein eivät. | Malli tekee todennäköisyyspohjaisia valintoja. |
| Onko toinen vastaus parempi? | Voi olla, mutta se pitää arvioida kriteereillä. | Vastausta ei arvioida vain sujuvuuden perusteella. |
| Mitä eroja huomaat? | Sävy, rakenne, yksityiskohdat, varmuus tai ehdotettu ratkaisu voi vaihdella. | Mallin vastaus ei ole yksi ainoa totuus, vaan tuotettu ehdotus. |

**Aika-arvio:** 15 minuuttia

---

### TT-B: Hallusinaatioiden metsästys

**Tavoite:** Opiskelija oppii tunnistamaan, että vakuuttava tekninen vastaus voi sisältää virheitä.

**Tehtävä:** Anna opiskelijoille tekoälyn tuottama vastaus, jossa on mahdollinen hallusinaatio. Opiskelijan tehtävä on tunnistaa tarkistettavat väitteet ja varmistaa ne luotettavasta lähteestä.

**Ohje opiskelijalle:**

1. Etsi vastauksesta väitteet, jotka kuulostavat faktoilta.
2. Merkitse erityisesti funktioiden nimet, komennot, kirjastot, versiot, vuosiluvut ja lähdeviitteet.
3. Tarkista vähintään kaksi väitettä luotettavasta lähteestä.
4. Kirjoita, mikä oli oikein, mikä oli väärin ja miten varmistit asian.

**Opettajan ohjaava kysymys:** Mikä väite on niin tarkka, että sen täytyy olla joko oikein tai väärin? Juuri sellaiset väitteet kannattaa tarkistaa ensimmäisenä.

**Aika-arvio:** 20 minuuttia

---

### TT-C: Verifiointiprosessin suunnittelu

**Tavoite:** Opiskelija osaa suunnitella käytännöllisen tarkistusprosessin tekoälyn vastaukselle.

**Tehtävä:** Opiskelija valitsee teknisen tilanteen, jossa tekoäly ehdottaa ratkaisua. Hän kirjoittaa, miten vastaus tarkistetaan ennen käyttöä.

**1.** Tarkista tietokannan dokumentaatiosta, mitä tauluja ja sarakkeita on olemassa.

**2.** Anna tekoälylle täsmällinen rajaus: ”Taulut ja sarakkeet ovat X, Y ja Z. Kirjoita kysely näiden perusteella.”

**3.** Vertaa tekoälyn ehdottamaa syntaksia SQL-dokumentaatioon tai kurssimateriaaliin.

**4.** Testaa kysely ensin testiympäristössä pienellä ja turvallisella datalla.

**5.** Dokumentoi, mitä tekoäly ehdotti, mitä muutit ja miksi.

**Hyvä vastaus sisältää:**

- tarkan lähteen tai dokumentaation, josta vastaus tarkistetaan
- turvallisen testausympäristön tai testidatan
- selityksen siitä, mitä tehdään, jos tekoälyn vastaus on väärä
- lyhyen dokumentoinnin päätöksistä ja muutoksista

**Heikko vastaus näyttää tältä:**

- ”Tarkistan sen silmäilemällä.”
- ”Luotan ChatGPT:hen.”
- ”Kokeilen suoraan tuotannossa.”

**Aika-arvio:** 25 minuuttia

---

## Formatiivinen tarkistuspiste — todistusaineisto 3

### Tavoite

Opiskelija yhdistää oppituntien aiemmat ydinkäsitteet yhdeksi käytännön tarkistuslistaksi. Tämä todistusaineisto toimii viimeisenä rakennuspalikkana ennen teoriaosion arviointitehtävää.

### Tehtävänanto opiskelijalle

Laadi tarkistuslista, jota käyttäisit ammattilaisena, kun hyödynnät tekoälyä teknisessä työssä. Tarkistuslistan pitää yhdistää seuraavat aiheet:

- **tokenien ennustaminen:** miksi tekoäly ei ole automaattisesti oikeassa
- **kontekstin katoaminen:** mitä teet, jos keskustelu on pitkä tai projekti jatkuu useassa osassa
- **hallusinaatiot:** miten tunnistat ja tarkistat mahdolliset virheet
- **verifiointi:** miten tarkistat vastauksen ennen käyttöä

**Valmis tuotos:** 6–10 kohdan käytännöllinen tarkistuslista.

### Mitä etsiä palautuksesta?

- **Synteesi, ei pelkkä listaus:** opiskelija yhdistää tokenien ennustamisen, kontekstin katoamisen ja hallusinaatiot yhdeksi työskentelyprosessiksi.
- **Konkreettiset toimenpiteet:** tarkistuslistassa on asioita, jotka voi oikeasti tehdä, kuten ”tarkista vastaus virallisesta dokumentaatiosta” tai ”toista rajaukset pitkän keskustelun alussa”.
- **Ammatillinen näkökulma:** opiskelija kirjoittaa ammattilaisen näkökulmasta, esimerkiksi ”kun käytän tekoälyä työssä, teen näin”.

### Yleinen väärinymmärrys

**”Riittää, että tarkistan, onko vastaus oikein.”**
Korjaus: Ohjaa opiskelijaa kohti prosessia. Kysy: miten tarkistat, mistä tarkistat, miten huomaat virheen ja mitä teet, jos et ole varma?

### Palautteen antaminen

Tämä on viimeinen tarkistuspiste ennen arviointia. Jos opiskelijan tarkistuslista on heikko, anna konkreettinen ohjaus ennen arviointituntia.

- **Jos tarkistuslista on hyvä:** ”Hyvä — listasi sisältää konkreettisia työvaiheita ja yhdistää tekoälyn tekniset rajoitukset ammatilliseen tarkistamiseen.”
- **Jos kontekstin katoaminen puuttuu:** ”Lisää vielä kohta: mitä teet, jos keskustelu on pitkä ja epäilet, että aiempi tieto on pudonnut pois?”
- **Jos verifiointi jää yleiseksi:** ”Tarkenna vielä: mistä lähteestä tarkistat ja miten testaat vastauksen ennen käyttöä?”

### Yhteys arviointiin

Opiskelijat, jotka ovat tehneet kaikki kolme todistusaineistoa, ovat paremmassa asemassa teoriaosion arvioinnissa. He eivät aloita tyhjästä, vaan heillä on valmiina kolme rakennuspalikkaa: kielimallin toimintaperiaate, kontekstin hallinta ja tekoälyn vastausten verifiointi.

---

## Aika- ja resurssiehdotukset

| Aktiviteetti | Aika | Resurssi |
| --- | --- | --- |
| Itseopiskeluosa | 30–40 min | Oppikirja ja muistiinpanot |
| Harjoitus 1: sama prompti, eri mallit | 15 min | Selaimessa avoinna olevat tekoälymallit |
| Harjoitus 2: hallusinaatioiden metsästys | 20 min | Opettajan valitsemat case-esimerkit |
| Harjoitus 3: verifiointiprosessi | 25 min | Valkokangas, taulukko tai yhteinen dokumentti |
| Yhteenveto | 10 min | Yhteinen keskustelu |
| **Yhteensä** | **Noin 100 min** | — |

---

## Jatkuva integraatio tulevilla oppitunneilla

### Yhteys seuraavaan oppituntiin

Seuraava oppitunti jatkaa eettisestä näkökulmasta: tekijänoikeudet, harhat, ympäristövaikutukset ja vastuullinen käyttö. Tämä oppitunti antaa teknisen perustan: opiskelija ymmärtää, miksi tekoälyn vastauksia ei voi ottaa vastaan kritiikittömästi.

### Yhteys ammatilliseen tekoälyn käyttöön

Jatkossa opiskelijoiden tulisi palata tämän oppitunnin periaatteisiin aina, kun he käyttävät tekoälyä teknisessä työssä. Erityisesti koodi, tietokantakyselyt, API-ohjeet, komentorivikomennot ja turvallisuusohjeet pitää tarkistaa ennen käyttöä.

**Opettajan muistutus:** Tämä oppitunti ei pyri vähentämään tekoälyn käyttöä, vaan tekemään siitä ammattimaisempaa. Tavoitteena on opiskelija, joka hyödyntää tekoälyä tehokkaasti mutta tarkistaa kriittiset kohdat itsenäisesti.

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että generatiivinen tekoäly on voimakas apuväline mutta ei totuuden takaaja. Se tuottaa vastauksia todennäköisyyksien perusteella, ja siksi se voi olla hyödyllinen, luova, nopea ja samalla virhealtis.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Jos tekoäly antaa sinulle teknisen ratkaisun, jota et itse täysin ymmärrä, mitä tarkistat ennen kuin käytät sitä oikeassa työssä?

---
