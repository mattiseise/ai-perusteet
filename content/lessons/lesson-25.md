# Ihminen portinvartijana — human-in-the-loop käytännössä

## Johdanto

Kaikki, mitä olet tähän mennessä oppinut — **muisti**, **konteksti**, **työkalut**, **suunnittelumallit** ja **turvallisuus** — johtaa yhteen tärkeään ajatukseen: **agentti ei voi tehdä kaikkea yksin**. Joissain tilanteissa agentti täytyy pysäyttää odottamaan, kunnes ihminen sanoo: ”kyllä, jatka” tai ”ei, älä tee sitä”.

Tätä kutsutaan nimellä **human-in-the-loop** eli ihmisen osallistuminen automaation silmukkaan. Se ei tarkoita, että ihminen tekee kaiken itse. Se tarkoittaa, että ihminen hyväksyy kriittiset päätökset, tarkistaa riskialttiit toiminnot ja ohjaa agenttia silloin, kun agentti on epävarma.

Tässä oppitunnissa opit, **milloin ihminen täytyy ottaa mukaan päätöksentekoon, miten hyväksyntäportit suunnitellaan ja miten rakennetaan työnkulkuja, joissa agentti ja ihminen tekevät yhteistyötä**. Näitä periaatteita käytät suoraan seuraavilla oppitunneilla, kun rakennat omaa agenttia n8n:llä.

## Milloin ihminen tarvitaan mukaan päätökseen?

Kaikki agentin päätökset eivät tarvitse ihmisen hyväksyntää. Jos jokainen pieni päätös pysäytetään ihmiselle, seurauksena on hidas ja kuormittava järjestelmä. Ihminen väsyy jatkuviin hyväksyntäpyyntöihin eikä ehdi keskittyä tärkeimpiin päätöksiin. Siksi sinun täytyy **valita strategisesti**, mitkä päätökset ovat niin kriittisiä, että ne vaativat ihmisen hyväksynnän.

Kolme sääntöä auttaa päättämään, milloin ihminen tarvitaan mukaan.

**Sääntö 1: Raha tai rakenne.** Jos päätös liittyy rahaan, se vaatii usein hyväksynnän. Tällaisia päätöksiä ovat esimerkiksi alennus, hyvitys, palkkio tai maksun muuttaminen. Pienen 10 % alennuksen agentti voi ehkä antaa itse, jos se on etukäteen sallittu. Sen sijaan 50 % alennus vaatii yleensä esihenkilön hyväksynnän, koska sillä on suuri taloudellinen vaikutus. Sama koskee rakenteellisia muutoksia: jos päätös muuttaa asiakkaan tietoja, sopimusta, tilausta tai tulevaa asiakassuhdetta, hyväksyntä on usein tarpeen.

**Sääntö 2: Epävarmuus.** Jos agentti ei ole riittävän varma päätöksestään, se tarvitsee ihmisen vahvistuksen. Esimerkiksi jos agentti arvioi olevansa vain 65 % varma siitä, että viesti koskee laskua, ihmisen kannattaa tarkistaa tapaus. Ihminen voi nähdä sävyjä, poikkeuksia ja kontekstia, joita agentti ei välttämättä huomaa.

**Sääntö 3: Poikkeamat.** Jos tilanne ei ole rutiinitapaus, vaan siinä on jotain tavallisesta poikkeavaa, päätös kannattaa ohjata ihmiselle. Tavallisen tilauksen agentti voi käsitellä yksin. Jos tilauksessa on negatiivinen hinta, poikkeuksellisen suuri summa, uusi maksutapa tai muu epätavallinen piirre, agentin täytyy pysäyttää prosessi ja pyytää hyväksyntä.

Näiden sääntöjen avulla voit jakaa päätökset eri ryhmiin. Rutiinipäätökset agentti voi tehdä itsenäisesti. Kriittiset päätökset vaativat ihmisen hyväksynnän ennen toimintaa. Osa päätöksistä voi vaatia hyväksynnän vain silloin, kun agentti on epävarma, ja osa voidaan tarkistaa jälkikäteen lokien perusteella.

> **Pysähdy hetkeksi:** Ajattele omaa työtäsi tai opintojasi. Mitä päätöksiä tekisit itse, ja mitkä veisit opettajalle, esihenkilölle tai toiselle asiantuntijalle? Mitkä päätökset liittyvät rahaan, rakenteeseen, epävarmuuteen tai poikkeamiin?

## Hyväksyntäporttien rakentaminen

Kun tiedät, mitkä päätökset vaativat ihmisen hyväksynnän, seuraava askel on **hyväksyntäporttien** suunnittelu. Hyväksyntäportti on työnkulun kohta, jossa agentti pysähtyy ja odottaa ihmisen vastausta ennen kuin se jatkaa.

Käytännössä hyväksyntäportti näyttää ihmiselle **selkeän kysymyksen ja ehdotuksen**, johon voi vastata esimerkiksi ”hyväksy”, ”hylkää” tai ”kysy lisää”.

**HYVÄKSYNTÄPYYNTÖ**

**Asiakas:** John Smith

**Pyyntö:** 50 % alennus. Tavallinen hinta on 100 €, ehdotettu hinta 50 €.

**Perustelu:** Asiakas on lojaali ja tehnyt 5 ostoa. Kilpailija tarjosi halvempaa hintaa.

**Päätös vaaditaan:** myyntipäällikkö

**Vaihtoehdot:** [HYVÄKSY] [HYLKÄÄ] [KYSY LISÄÄ]

Hyväksyntäportin täytyy olla **selkeä ja nopea käyttää**. Ihmisen pitää nähdä yhdellä silmäyksellä seuraavat asiat:

- **Mitä päätöstä pyydetään?** Esimerkiksi 50 % alennus.
- **Kenelle päätös koskee?** Esimerkiksi asiakkaalle John Smith.
- **Miksi agentti ehdottaa tätä?** Esimerkiksi lojaalisuus, kilpailijan tarjous tai asiakashistoria.
- **Kenen täytyy hyväksyä päätös?** Esimerkiksi myyntipäällikön.
- **Mitä tapahtuu, jos päätös hylätään?** Esimerkiksi agentti tarjoaa asiakkaalle vaihtoehtoisen ratkaisun tai ilmoittaa, ettei alennusta voida antaa.

Hyväksyntäportin jälkeinen toiminta on tärkeä suunnitella etukäteen. Jos ihminen hyväksyy ehdotuksen, agentti jatkaa suunniteltua polkua. Jos ihminen hylkää sen, agentin pitää tietää, mitä seuraavaksi tehdään. Se voi esimerkiksi tarjota asiakkaalle pienemmän alennuksen, ilmaisen toimituksen tai selittää kohteliaasti, miksi pyyntöä ei voida hyväksyä. Agentti ei saa vain jäädä jumiin.

Hyväksyntäportteihin liittyy myös **aikaraja**. Mitä tapahtuu, jos ihminen ei vastaa 24 tunnin kuluessa? Vaihtoehtoja on useita:

- **Oletusarvo:** Jos vastausta ei tule, järjestelmä toimii ennalta sovitulla tavalla. Tämä voi tarkoittaa hyväksyntää tai hylkäystä, mutta sitä pitää käyttää varoen.
- **Eskalointi:** Pyyntö lähetetään toiselle hyväksyjälle, esimerkiksi esihenkilölle tai varahenkilölle.
- **Timeout:** Agentti peruuttaa pyynnön ja ilmoittaa asiakkaalle, että prosessi ei voi jatkua juuri nyt.

Valinta riippuu siitä, kuinka paljon odottaminen maksaa ja kuinka suuri riski väärällä päätöksellä on. Jos asiakas odottaa liian kauan vastausta, hän voi siirtyä kilpailijalle. Silloin eskalointi voi olla hyvä ratkaisu. Jos päätös on hyvin kriittinen, esimerkiksi miljoonan euron sopimus, automaattinen hyväksyntä olisi liian vaarallinen. Silloin timeout tai ihmisen pakollinen hyväksyntä on turvallisempi vaihtoehto.

## Hyväksyntäportit käytännössä: kolme esimerkkiä

Seuraavat esimerkit näyttävät, miten hyväksyntäportin laajuus ja nopeusvaatimus vaihtelevat päätöksen mukaan.

**Esimerkki 1: Pieni päätös — nopea hyväksyntä**

Agentti huomaa, että asiakas haluaa vaihtaa tuotteen värin. Uusi väri on varastossa, eikä vaihto vaikuta hintaan.

- **Portti näyttää:** ”Vaihdetaanko keltainen tuote punaiseen?”
- **Hyväksyjä:** asiakaspalvelupäällikkö.
- **Vastausaika:** päätös voidaan tehdä nopeasti työpäivän aikana.
- **Oletusarvo:** jos vastausta ei tule tunnissa, vaihto voidaan hyväksyä automaattisesti, jos riski on pieni ja asiakaskokemus kärsisi odottamisesta.

**Esimerkki 2: Suuri päätös — perusteellinen hyväksyntä**

Agentti ehdottaa asiakkaalle 50 % alennusta pitkästä sopimuksesta. Päätös vaikuttaa merkittävästi myyntikatteeseen.

- **Portti näyttää:** asiakkaan historian, kilpailijan tarjouksen, tuotteen katteen ja ehdotetun alennuksen prosentteina.
- **Hyväksyjä:** myyntipäällikkö.
- **Vastausaika:** hyväksyjä tarkistaa tiedot ennen päätöstä.
- **Oletusarvo:** jos vastausta ei tule 4 tunnissa, agentti lähettää asiakkaalle viestin: ”Tarjousta arvioidaan tiimissämme. Palaamme sinulle pian.”

**Esimerkki 3: Vakava päätös — monivaiheinen hyväksyntä**

Uusi liikekumppani haluaa integroitua yrityksen tietokantaan. Päätökseen liittyy sekä tietoturvariskejä että liiketoiminnallisia vaikutuksia.

- **Portti näyttää:** tietoturva-analyysin, integraation riskit ja liiketoimintahyödyt.
- **Hyväksyjät:** ensin tekninen johtaja ja sen jälkeen liiketoimintajohtaja.
- **Vastausaika:** päätös tehdään vasta molempien hyväksyntöjen jälkeen.
- **Oletusarvo:** jos jompikumpi hylkää pyynnön, prosessi pysähtyy ja agentti ilmoittaa integraatiokumppanille, ettei prosessia voida jatkaa tällä hetkellä.

Näissä esimerkeissä hyväksyntäportin **laajuus**, **hyväksyjien määrä** ja **aikaraja** muuttuvat päätöksen riskin mukaan. Pienet päätökset voivat olla nopeita. Suuret päätökset vaativat tarkempaa arviointia. Vakavat päätökset voivat tarvita useita hyväksyntäkerroksia.

## Työnkulut, joissa agentti ja ihminen tekevät yhteistyötä

Hyväksyntäportit ovat vain yksi osa human-in-the-loop-työnkulkua. Kokonaisuus on **työnkulku, jossa agentti ja ihminen tekevät yhteistyötä**. Agentti tekee sitä, missä se on hyvä: nopeaa analyysiä, tiedonhakua, toistuvia vaiheita ja yksinkertaisia päätöksiä. Ihminen tekee sitä, missä ihminen on vahva: kriittisiä päätöksiä, empatiaa, tilannearviointia ja poikkeusten käsittelyä.

Kuvittele asiakaspalvelun työnkulku:

1. **Syöte:** Asiakas lähettää viestin: ”Haluan palauttaa tuotteen.”
2. **Agentin analyysi:** Agentti lukee viestin, hakee asiakkaan tilauksen historiasta ja huomaa, että tilaus tehtiin 5 päivää sitten. Palautusaika on 14 päivää, joten asiakas on oikeutettu palautukseen.
3. **Hyväksyntäportti 1:** Agentti näyttää perustelut ihmiselle ja kysyy: ”Onko palautusaika voimassa?” Ihminen vahvistaa: ”Kyllä.”
4. **Agentin toiminta:** Agentti lähettää asiakkaalle palautuslomakkeen, kuljetusohjeet ja palautusehdot.
5. **Hyväksyntäportti 2:** Agentti huomaa, että asiakas on lojaali ja tehnyt 5 ostoa. Se ehdottaa 10 % alennusta seuraavaan tilaukseen. Ihminen hyväksyy ehdotuksen.
6. **Agentin lopetus:** Agentti lähettää asiakkaalle jatkoviestin: ”Pahoittelemme, että palautus oli tarpeellinen. Tässä on 10 % alennus seuraavaan tilaukseesi.”

Koko prosessi on hybridi. Agentti tekee rutiinianalyysin ja toteuttaa toimenpiteet. Ihminen tekee ne päätökset, joissa tarvitaan harkintaa, vastuuta tai asiakassuhteen ymmärtämistä. Näin saadaan sekä nopeutta että laatua.

> **Pysähdy hetkeksi:** Ajattele omaa tulevaa työtäsi. Mikä prosessi voitaisiin automatisoida agentin avulla, mutta vaatisi ihmisen hyväksynnän kriittisissä vaiheissa? Missä kohdissa ihminen täytyy ottaa mukaan?

## Agentin oppiminen ihmisen palautteesta

Human-in-the-loop ei tarkoita vain sitä, että ihminen hyväksyy tai hylkää päätöksiä. Se tarkoittaa myös sitä, että **agentti voi oppia ihmisen palautteesta**. Kun ihminen hylkää agentin ehdotuksen, agentti voi tallentaa hylkäyksen syyn. Kun ihminen hyväksyy ehdotuksen, agentti voi tallentaa, millainen ehdotus hyväksyttiin ja miksi.

Esimerkiksi agentti tekee alennusehdotuksia. Yksi myyntipäällikkö hyväksyy usein 40 % alennuksia, kun taas toinen hyväksyy yleensä vain 15 % alennuksia. Agentti voi oppia palautteesta, että hyväksyjien päätöstyylit eroavat toisistaan. Tämän perusteella se voi myöhemmin tehdä realistisempia ehdotuksia eri hyväksyjille.

Tämä oppiminen perustuu **lokiin ja palautteeseen**. Jokainen hyväksyntä ja hylkäys tallennetaan. Sen jälkeen agentti tai järjestelmän kehittäjä voi etsiä päätöksistä toistuvia kaavoja. Oppiminen ei kuitenkaan tapahdu turvallisesti itsestään. Sinun täytyy suunnitella, mitä palautteesta opitaan, mitä ei opita ja kuka valvoo oppimisen vaikutuksia.

**Vinkki:** Agentin ei kannata oppia kaikesta palautteesta automaattisesti. Jos ihminen teki poikkeuksellisen päätöksen kiireen tai erityistilanteen takia, sitä ei välttämättä pidä muuttaa yleiseksi säännöksi. Palautteen hyödyntäminen vaatii harkintaa ja seurantaa.

## Kohti n8n-projekteja — kaikki yhdistyy

Tämä on viimeinen teoriapainotteinen oppitunti ennen rakentamista. Seuraavaksi näet, miten kaikki aiemmat aiheet yhdistyvät n8n:ssä yhdeksi kokonaisuudeksi.

| Aihe | Mitä opit? | Miten se näkyy n8n:ssä? |
| --- | --- | --- |
| **Agentin rakenne** | Agentin kuusi komponenttia. | Jokainen komponentti toteutuu yhtenä tai useampana n8n-solmuna. |
| **Automaatio vs. autonomia** | Päätöspuu: promptaus, työnkulku vai agentti. | Valitset, riittääkö yksi AI Agent -solmu vai tarvitaanko monivaiheinen työnkulku. |
| **Muisti ja konteksti** | Konteksti-ikkuna, pitkäkestoinen muisti ja tila. | Memory-solmu, tietokanta, Google Sheets tai muu tilan tallennus. |
| **Työkalut** | Tiedostot, verkkohaku ja CLI-komennot. | Read File-, HTTP Request- ja Execute Command -solmut. |
| **Suunnittelumallit** | ReAct, ketjuajattelu ja moniagenttijärjestelmät. | AI Agent ReAct-malliin, solmuketju ketjuajatteluun ja webhook-kutsut moniagenttirakenteeseen. |
| **Turvallisuus** | Prompt injection, hallusinaatiot, minimioikeus ja lokitus. | IF-solmut validointiin, rajatut API-avaimet, hyväksyntäportit ja lokisolmut. |
| **Human-in-the-loop** | Hyväksyntäportit, palaute ja ihmisen rooli kriittisissä päätöksissä. | Hyväksyntäsolmu, Slack- tai Teams-ilmoitus, lomakevastaus ja lokitus. |

Kaikki, mitä olet oppinut, muuttuu n8n:ssä konkreettisiksi solmuiksi ja yhteyksiksi. Näet visuaalisesti, missä työnkulku käynnistyy, missä agentti hakee tietoa, missä se tekee päätöksen ja missä se pysähtyy odottamaan ihmisen hyväksyntää.

n8n:ssä voit rakentaa esimerkiksi:

- **hyväksyntäportteja**, jotka pysäyttävät työnkulun ennen kriittistä toimintoa
- **työnkulkuja**, joissa agentti ja ihminen tekevät yhteistyötä
- **palautteen tallennusta**, jossa jokainen hyväksyntä ja hylkäys kirjataan
- **lokitusta**, joka näyttää, mitä tapahtui ja miksi
- **virheenkäsittelyä**, jossa epäonnistunut toiminto voidaan korjata tai ohjata ihmiselle

Kun opit käyttämään n8n:ää, muista tämä: **jokainen solmu on vaihe agentin toiminnassa**. Hyväksyntäsolmu on kohta, jossa agentti pysähtyy ja odottaa ihmisen päätöstä. API-haku on vaihe, jossa agentti noutaa tietoa. IF-solmu on kohta, jossa työnkulku haarautuu päätöksen perusteella. Yhdessä nämä solmut muodostavat toimivan ja turvallisen agentin.

## Kohti omaa projektia

Tämä on viimeinen suunnitteluaskel ennen rakentamista. Sinulla on nyt koossa viisi **Agentti-pohjapiirrosta**:

- **Ongelma** — tunti 19
- **Muisti** — tunti 21
- **Päättely** — tunti 23
- **Turva** — tunti 24
- **Ihminen** — tämä tunti

Yhdessä nämä muodostavat suunnitelman, jonka pohjalta rakennat n8n-työnkulun oppitunneilla 26–27. Käy pohjapiirrokset vielä kerran läpi ennen rakentamista ja varmista, että ne muodostavat yhtenäisen kokonaisuuden. Tarkista erityisesti, missä kohdissa agentti saa toimia itsenäisesti ja missä kohdissa tarvitaan ihmisen hyväksyntä.

## Yhteenveto

**Human-in-the-loop** ei tarkoita, että ihminen tekee kaiken. Se tarkoittaa, että ihminen hyväksyy suuret päätökset ja ohjaa agenttia epäselvissä tai riskialttiissa tilanteissa. Kolme sääntöä auttaa päättämään, milloin hyväksyntä tarvitaan: päätös liittyy **rahaan tai rakenteeseen**, agentti on **epävarma** tai tilanne on **poikkeava**.

**Hyväksyntäportit** tehdään selkeiksi ja nopeiksi, jotta ihminen voi vastata ilman, että koko prosessi pysähtyy tarpeettoman pitkäksi aikaa. Hyvässä hyväksyntäportissa näkyvät päätös, perustelut, riskit, hyväksyjä ja vaihtoehtoinen polku, jos pyyntö hylätään.

Koko prosessi on hybridi: agentti analysoi, hakee tietoa ja toteuttaa rutiinivaiheita, kun taas ihminen tekee kriittiset päätökset. Agentti voi myös oppia ihmisen palautteesta, kun hyväksynnät ja hylkäykset tallennetaan lokiin ja niitä käytetään toiminnan kehittämiseen.

Seuraavilla oppitunneilla rakennat nämä työnkulut konkreettisesti n8n:ssä. Vedät solmuja työtilaan, kytket hyväksyntäportteja ja näet, miten automaatio ja inhimillinen ohjaus toimivat yhdessä. Tavoitteena ei ole pelkästään nopea automaatio, vaan **älykäs, turvallinen ja hallittu agentti**.

:contentReference[oaicite:0]{index=0}

---
