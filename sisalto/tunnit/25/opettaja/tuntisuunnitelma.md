# Opettajamateriaali — oppitunti 25: Ihmisen osallistuminen päätöksentekoon

## Oppitunnin ydinajatukset

Tämän oppitunnin keskeinen viesti on, että agentti ei ole täysin autonominen järjestelmä. Kriittisissä kohdissa tarvitaan ihminen mukaan päätöksentekoon. **Ihmisen osallistuminen päätöksentekoon** yhdistää automaation ja ihmisen harkinnan: agentti tekee rutiinityötä ja ihminen osallistuu silloin, kun päätös on riskialtis, epävarma tai poikkeuksellinen.

Oppitunti rakentaa siltaa kohti **n8n-projektia**, jossa opiskelijat suunnittelevat ja rakentavat oman agenttinsa. Viimeiset viisi oppituntia muodostavat agentin rakentamisen keskeiset rakennuspalikat:

1. **Oppitunti 21: Muisti ja konteksti** — agentti muistaa ja hyödyntää aiempaa tietoa.
2. **Oppitunti 22: Työkalut** — agentti käyttää työkaluja ja tekee toimintoja.
3. **Oppitunti 23: Suunnittelumallit** — agentti etenee järjestelmällisesti ja valitsee sopivan toimintamallin.
4. **Oppitunti 24: Turvallisuus** — agentti toimii rajatusti, valvotusti ja turvallisesti.
5. **Oppitunti 25: Ihmisen osallistuminen päätöksentekoon** — agentti tekee yhteistyötä ihmisen kanssa.

**Opettajan painotus:** Korosta opiskelijoille, että hyväksyntä ei ole irrallinen viesti ihmiselle vaan harnessin toteuttama tila. Harness pysäyttää suorituksen, säilyttää tarvittavat tiedot ja jatkaa, hylkää tai eskaloi sovitun säännön mukaan. Kielimalli voi valmistella ehdotuksen, mutta se ei saa hyväksyä omaa ehdotustaan.

---

## Kolme sääntöä hyväksynnälle

Ihmisen hyväksyntää ei tarvita jokaiseen päätökseen. Jos kaikki päätökset pysäytetään hyväksyttäväksi, agentti hidastaa työnkulkua. Jos taas hyväksyntää ei vaadita riskikohdissa, agentti voi aiheuttaa todellista vahinkoa.

Hyvä perusmalli on arvioida hyväksynnän tarvetta kolmen säännön avulla:

1. **Rahaa tai rakenteita koskeva päätös:** alennukset, hyvitykset, sopimukset, asiakastietojen muutokset ja pysyvät tietokantamuutokset vaativat hyväksynnän.
2. **Epävarmuus:** jos agentin varmuus on alle sovitun rajan, esimerkiksi alle 70 %, päätös siirretään ihmiselle.
3. **Poikkeama:** jos tilanne on epätavallinen, tunnepitoinen, riskialtis tai poikkeaa normaalista prosessista, tarvitaan ihmisen arvio.

| Sääntö | Esimerkki | Miksi ihminen tarvitaan? |
| --- | --- | --- |
| **Rahaa tai rakenteita** | Agentti ehdottaa 50 % hyvitystä asiakkaalle. | Päätös vaikuttaa yrityksen rahaan, asiakassuhteeseen ja mahdollisesti käytäntöihin. |
| **Epävarmuus** | Agentti on vain 64 % varma, että asiakkaalla on oikeus palautukseen. | Matala varmuus lisää virheellisen päätöksen riskiä. |
| **Poikkeama** | Asiakas on vihainen, uhkaa lopettaa sopimuksen ja vaatii poikkeuksellista hyvitystä. | Tilanne vaatii harkintaa, empatiaa ja mahdollisesti poikkeusmenettelyä. |

**Opettajan huomio:** Hyväksyntää ei pidä ajatella epäluottamuksena agenttia kohtaan. Se on suunniteltu vastuunjako: agentti valmistelee, ihminen kantaa vastuun kriittisestä päätöksestä.

---

## Hyväksyntäportin suunnittelu

**Hyväksyntäportti** on kohta työnkulussa, jossa agentti pysähtyy ja pyytää ihmiseltä päätöstä ennen toiminnon suorittamista. Hyvä hyväksyntäportti on **selkeä**, **nopea** ja **päätöstä tukeva**.

Hyväksyntäportissa pitää näkyä ainakin seuraavat asiat:

- **Mitä päätöstä pyydetään?**
- **Kenestä tai mistä päätös koskee?**
- **Miksi agentti ehdottaa tätä päätöstä?**
- **Kuka päätöksen hyväksyy?**
- **Mitä tapahtuu, jos päätös hylätään?**

**HYVÄKSYNTÄPYYNTÖ**

**Asiakas:** Jane Smith, 3 aiempaa ostoa

**Pyyntö:** 50 % alennus, 100 € → 50 €

**Agentin perustelu:** Asiakas on lojaali ja kertoo kilpailijan tarjonneen halvempaa hintaa.

**Päätöksen tekee:** Myyntipäällikkö

**Vaihtoehto, jos hylätään:** Tarjoa ilmainen toimitus.

**Toiminnot:** [HYVÄKSY] [HYLKÄÄ] [KYSY LISÄÄ]

Hyväksyntäportin ei pidä olla pelkkä painike. Jos ihminen näkee vain vaihtoehdon “hyväksy” tai “hylkää” ilman taustatietoja, hän ei voi tehdä laadukasta päätöstä. Toisaalta hyväksyntäportti ei saa myöskään olla liian raskas. Jos siinä on liikaa tietoa, hyväksyjä alkaa helposti ohittaa yksityiskohtia.

**Esimerkki opetukseen**

Näytä opiskelijoille kaksi hyväksyntäporttia: toinen liian suppea ja toinen liian pitkä. Pyydä opiskelijoita arvioimaan, kummalla hyväksyjä tekee todennäköisemmin virheen ja miksi.

---

## Ihmisen osallistava työnkulku

**Ihmisen osallistava työnkulku** tarkoittaa koko prosessia, jossa agentti ja ihminen tekevät yhteistyötä. Tavoitteena ei ole siirtää kaikkea ihmiselle, vaan jakaa vastuu järkevästi.

| Agentti tekee | Ihminen tekee |
| --- | --- |
| Nopeat analyysit ja alustavat luokittelut | Kriittiset päätökset ja poikkeukset |
| Rutiinitehtävät ja toistuvat vaiheet | Epäselvät, tunnepitoiset tai riskialttiit tilanteet |
| Yksinkertaiset ehdotukset ja päätösten valmistelu | Oppimisen ohjaaminen ja lopullinen vastuu |

**Ihmisen osallistavan työnkulun perusmalli**

|  |
| --- |
| **1. Agentti lukee syötteen** Asiakasviesti, lomake, tiketti tai tilaus. |
| ↓ |
| **2. Agentti tekee alustavan arvion** Luokittelu, riskitaso ja ehdotus. |
| ↓ |
| **3. Hyväksyntäportti** Ihminen hyväksyy, hylkää tai pyytää lisätietoa. |
| ↓ |
| **4. Agentti suorittaa turvallisen toiminnon** Viesti, päivitys, raportti tai ohje. |

Hyvä työnkulku sijoittaa ihmisen mukaan niihin kohtiin, joissa päätöksellä on suuri vaikutus tai joissa agentin virhe voisi aiheuttaa vahinkoa. Ihmistä ei kannata lisätä työnkulkuun vain varmuuden vuoksi, jos päätös on yksinkertainen ja turvallinen automatisoida.

---

## Oppiminen palautteesta

Ihmisen osallistuminen päätöksentekoon ei ole vain päätösten hyväksymistä. Se on myös tapa tuottaa palautetta agentin toiminnan kehittämiseksi. Kun ihminen hyväksyy, hylkää tai muokkaa agentin ehdotusta, järjestelmä voi oppia, millaiset ehdotukset ovat hyviä ja millaiset tarvitsevat korjaamista.

Palautteesta oppiminen voidaan kuvata nelivaiheisena prosessina:

1. **Tallennetaan hyväksynnät ja hylkäykset:** jokainen päätös kirjataan riittävillä taustatiedoilla.
2. **Agentti analysoi kuvioita:** mitkä ehdotukset hyväksytään usein ja mitkä hylätään?
3. **Agentti mukauttaa ehdotuksiaan:** tulevat ehdotukset muuttuvat aiemman palautteen perusteella.
4. **Riski arvioidaan:** agentti voi oppia myös väärin, jos palaute on vinoutunutta, epäjohdonmukaista tai puutteellista.

**Opettajan tarkistuskysymys:** Jos opiskelija sanoo “agentti oppii hyväksyjien päätöksistä”, pyydä häntä tarkentamaan, mitä agentti saa oppia. Oppiiko se organisaation säännön, päätösmallin vai yksittäisen ihmisen henkilökohtaisen tavan toimia?

Väärä oppiminen voi syntyä esimerkiksi silloin, kun yksi hyväksyjä tekee jatkuvasti poikkeuksellisia päätöksiä, mutta agentti tulkitsee ne yleiseksi säännöksi. Siksi palautedataa pitää arvioida kriittisesti, eikä agentille pidä antaa rajatonta vapautta muuttaa toimintaansa pelkän hyväksyntähistorian perusteella.

---

## Harjoitukset

Oppitunnin harjoitusten tarkoituksena on siirtää ihmisen osallistumista korostava ajattelu konkreettiseen suunnitteluun. Harjoitukset kannattaa sitoa opiskelijan omaan agenttiprojektiin aina kun mahdollista.

1. **Kolme sääntöä: päätösten luokittelu**
   Opiskelija arvioi, mitkä päätökset vaativat ihmisen hyväksynnän ja perustelee valinnan rahaan, epävarmuuteen tai poikkeamaan liittyvällä säännöllä.
2. **Hyväksyntäportti: suunnittelu**
   Opiskelija suunnittelee hyväksyntäpyynnön, jossa näkyvät päätöksen kohde, perustelu, riskit, hyväksyjä ja vaihtoehdot.
3. **Työnkulku: kaavio**
   Opiskelija kuvaa työnkulun, jossa näkyy, missä vaiheessa agentti toimii ja missä vaiheessa ihminen osallistuu.
4. **Oppiminen: mekanismi**
   Opiskelija suunnittelee, mitä palautedataa tallennetaan ja miten väärä oppiminen estetään.

**Vinkki arviointiin:** Hyvä vastaus ei vain sano “ihminen hyväksyy päätöksen”, vaan kertoo, millä perusteella päätös pysähtyy hyväksyttäväksi, mitä tietoja hyväksyjä näkee ja mitä tapahtuu hyväksynnän tai hylkäyksen jälkeen.

---

## Yhteys n8n-projektiin

n8n-projektissa tämän oppitunnin ajatukset voidaan toteuttaa konkreettisina työnkulun osina. Opiskelijoiden kannattaa suunnitella ihmisen osallistuminen päätöksentekoon jo ennen kuin he rakentavat agentin teknisesti.

| Ihmisen osallistuminen | Toteutus n8n:ssä | Mihin sitä käytetään? |
| --- | --- | --- |
| **Hyväksyntäportti** | Approval node tai vastaava hyväksyntävaihe | Riskialttiit päätökset pysäytetään ihmiselle. |
| **Ehdollinen päätös** | Conditional node | Jos varmuus on matala tai päätös koskee rahaa, siirrytään hyväksyntään. |
| **Lokitus** | Tietokanta, Google Sheets, lokitiedosto tai muu tallennus | Päätökset, hyväksyjät ja perustelut tallennetaan jäljitettävästi. |
| **Ihmisen vastaus** | Webhook tai lomakevastaus | Ihminen voi hyväksyä, hylätä tai pyytää lisätietoja. |

**Esimerkki n8n-työnkulusta**

Agentti arvioi asiakkaan hyvityspyynnön. Jos hyvitys on alle 20 € ja varmuus on yli 90 %, agentti voi lähettää vastauksen automaattisesti. Jos hyvitys on yli 20 €, varmuus on alle 70 % tai viestissä on vihainen sävy, työnkulku ohjaa päätöksen hyväksyntäporttiin.

---

## Yhteiset virheet ja opettajan korjaukset

| Yleinen virhe | Korjaava näkökulma |
| --- | --- |
| ”Ihminen kannattaa lisätä jokaiseen päätökseen.” | Ei välttämättä. Jos jokainen päätös vaatii ihmisen, agentti menettää tehokkuutensa. Ihminen lisätään riskikohtiin. |
| ”Jos agentti on varma, ihminen ei koskaan tarvita.” | Varmuus ei yksin riitä. Päätös voi silti koskea rahaa, henkilötietoja tai poikkeustilannetta. |
| ”Hyväksyntäportti on vain hyväksy/hylkää-painike.” | Hyväksyntäportin pitää antaa päätöksen kannalta olennainen tieto: mitä, kenelle, miksi, riski ja vaihtoehdot. |
| ”Agentti oppii automaattisesti oikein hyväksynnöistä.” | Ei aina. Palaute voi olla vinoutunutta, epäjohdonmukaista tai yksittäisen henkilön tyyliin perustuvaa. Oppiminen pitää rajata ja tarkistaa. |
| ”Hyväksyntä on järjestelmän ulkopuolinen viesti ihmiselle.” | Ei. Harnessin pitää hallita odotustila, päätöstiedot, aikaraja ja varapolku, jotta suoritus jatkuu hallitusti myös silloin, kun ihminen ei vastaa. |

---

## Oppitunnin lopetus

Oppitunnin lopussa opiskelijoiden tulisi ymmärtää, että **ihmisen osallistuminen päätöksentekoon** ei ole automaation vastakohta. Se on vastuullisen automaation muoto. Agentti voi tehdä paljon, mutta ihmisen pitää osallistua niissä kohdissa, joissa tarvitaan harkintaa, vastuuta ja eettistä päätöksentekoa.

Hyvä päätöskysymys tunnin loppuun:

> **Pohdi:** Missä kohdassa oman agenttisi pitäisi pysähtyä ja pyytää ihmiseltä hyväksyntä? Mitä tietoa ihmisen pitää nähdä, jotta hän voi tehdä hyvän päätöksen?

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **hyväksyntä- ja eskalointimatriisi varapolkuineen**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–10 min | Virittäytyminen | Kytke ydinkysymys tuttuun tilanteeseen ja tarkista lähtötaso. |
| 10–25 min | Ydinkäsite | Mallinna tunnin keskeinen ero yhdellä vastaesimerkillä. |
| 25–65 min | Perustuotos | Oppija sijoittaa kolme toimintoa hyväksyntä- ja eskalointimatriisiin varapolkuineen. Tämä 40 minuutin jakso on itsenäistä tai parin kanssa tehtävää työskentelyä. |
| 65–80 min | Testaus ja purku | Testauta tuotos annetulla tapauksella ja pura yksi onnistuminen sekä yksi korjaus. |
| 80–90 min | Tallennus ja lopputehtävä | Varmista tiedoston nimi, tallennuspaikka ja yhden lauseen johtopäätös. |

### Tukireitti

Oppija käyttää valmiita riskitasokortteja. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis, oppija lisää aikakatkaisun ja poikkeuksen turvalliset oletukset. Syventävä työ ei kasvata pakollista ydintuotosta.
