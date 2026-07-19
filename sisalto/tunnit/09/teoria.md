# Oppitunti 9 — Tuomaripöydän päätös: asiantuntijalausunto tekoälystä

## Mitä tällä tunnilla tapahtuu?

Tähän mennessä olet kerännyt kahdeksan oppitunnin aikana sanastoa, käsitteitä ja näkemyksiä. Nyt asetut tuomaripöydän taakse ja teet niistä jotain konkreettista: **asiantuntijalausunnon**, jossa analysoit todellista tekoälyyn liittyvää ongelmaa ja esität siihen perustellun ratkaisun.

Tällä tunnilla et enää opiskele uusia teoreettisia käsitteitä. Sen sijaan opit **käyttämään** sitä, mitä jo osaat. Et kirjoita lausuntoa itse, vaan ohjaat tekoälyä tuottamaan sen — tämä materiaali auttaa sinua tekemään siitä sellaisen, joka kestää sekä teknisen että asiallisen tarkastelun.

## Mikä on asiantuntijalausunto?

Asiantuntijalausunto on **perusteltu analyysi**, jonka kirjoittaa oman alansa tunteva vastuullinen käyttäjä. Sitä ei kirjoiteta tunteiden tai pelkkien mielipiteiden varaan, vaan käsitteiden, havaintojen ja loogisten päätelmien avulla. Lausunnon lukija, kuten esimies, tietosuojavaltuutettu, asiakas tai kollega, ei välttämättä ole tekoälyn asiantuntija. Sinun tehtäväsi on selittää tilanne niin, että lukija ymmärtää sen ja voi luottaa päätelmiisi.

Asiantuntijalausunto eroaa esseestä ja blogitekstistä kolmella tavalla:

1. **Se on neutraali, ei tunteellinen.** Et kirjoita ”tämä on järkyttävää”, vaan ”tilanne sisältää merkittävän tietosuojariskin, koska…”.
2. **Se nojaa käsitteisiin.** Et kirjoita ”tekoäly sekoili”, vaan ”kyseessä on hallusinaatio, joka selittyy mallin generatiivisella toimintalogiikalla”.
3. **Se päätyy konkreettiseen suositukseen.** Et jätä lukijaa arvailemaan, vaan kerrot selkeästi, mitä tilanteessa pitäisi tehdä.

## Lausunnon rakenne

Tehtävänannossa on neljä osaa. Käytä niitä otsikoina tai vähintään lausunnon selkeänä runkona:

**1. Mitä tapahtui?** Kuvaile tilanne neutraalisti, aivan kuin tutkija raportoisi tapahtumista. Mitä konkreettisesti meni pieleen? Ketkä olivat osallisina? Älä vielä selitä syitä, vaan keskity tilanteen kuvaamiseen.

**2. Miksi se tapahtui?** Tässä kohdassa otat käsitteet käyttöön. Mikä mekanismi selittää tapahtuneen? Hyödynnä tässä osiossa todistusaineistoasi tunneilta 3, 5 ja 7. Älä vain luettele käsitteitä, vaan *sovella* niitä käsiteltävään tilanteeseen.

**3. Miten tilanne pitäisi hoitaa?** Esitä konkreettisia toimenpiteitä: mitä organisaation pitäisi tehdä heti, mitä viikon sisällä ja mitä pysyvästi. Anna toimenpiteitä, älä pelkkiä toiveita.

**4. Asiallinen vastuu.** Kuka kantaa vastuun? Mikä on sinun roolisi vastuullisena käyttäjänä? Tässä kohdassa lausunto nousee teknisestä raportista aidoksi asiantuntijatekstiksi.

## Lausunnon kieli

| Vältä | Käytä |
| --- | --- |
| ”Mun mielestä” | ”Arvioin, että…” |
| ”Tekoäly meni rikki” | ”Mallin tuotos sisälsi hallusinaation, koska…” |
| ”Sen ei pitäisi tehdä noin” | ”Käytäntö rikkoo tietosuoja-asetusta ja organisaation linjausta, koska…” |
| ”Tää on tosi paha” | ”Riski on merkittävä, koska se koskee henkilötietoja ja toistuu päivittäin.” |
| ”Joku pitäisi korjata” | ”Toimitusjohtajan vastuulla on lopettaa nykyinen käytäntö välittömästi ja…” |

Asiantuntijan kielen tunnistaa siitä, että se on **täsmällistä, perusteltua ja vastuuta osoittavaa**. Se ei ole vaikeaselkoista virkamiestyyliä eikä kuivaa raportointia, vaan selkeää ja uskottavaa tekstiä.

## Hyvä ja heikko lausunto: esimerkkejä

Alla on saman asian eri versioita yhdestä skenaariosta: **Skenaario 1 — asiakaspalvelun tietovuoto**. Vertaa, miten sama tilanne voidaan kuvata heikosti tai vahvasti.

### Miksi se tapahtui? — Heikko versio

> Asiakaspalvelijat laittoivat ChatGPT:hen asiakkaiden tietoja, vaikka niin ei olisi pitänyt tehdä. Tekoäly tallentaa kaiken, mitä sille annetaan, ja siksi tiedot vuotivat. Tämä on aika selkeä juttu, eikä siinä ole paljon mietittävää.

**Mikä tekstissä on ongelmana:** Kieli on puhekielistä. Väite ”tekoäly tallentaa kaiken” on epätarkka, koska se sekoittaa kontekstimuistin ja koulutusdatan. Käsitteitä ei käytetä täsmällisesti. Lopetus heikentää lausunnon asiantuntevuutta.

### Miksi se tapahtui? — Vahva versio

> Tilanteessa toteutui kolme samanaikaista riskiä. Ensinnäkin asiakaspalvelijat syöttivät henkilötietoja kolmannen osapuolen palveluun ilman tietojenkäsittelysopimusta. Tämä on jo sellaisenaan tietosuojariski. Toiseksi, kuten oppitunti 5 osoitti, kielimallin konteksti-ikkuna ei toimi luotettavana muistina. Vaikka käyttäjä luulisi keskustelun olevan yksityinen, syötteet saattavat tallentua palveluntarjoajan järjestelmiin esimerkiksi lokitusta tai mallin kehittämistä varten. Kolmanneksi oppitunnin 3 mekaniikka selittää, miksi mallin vastauksiin ei voi luottaa sokeasti: malli ennustaa todennäköisimmän jatkon, ei välttämättä oikeaa vastausta. Asiakaspalvelija on saattanut välittää asiakkaalle tietoa, joka kuulosti oikealta mutta oli keksittyä.

**Mikä toimii:** Käsitteitä käytetään täsmällisesti ja niitä sovelletaan juuri tähän tilanteeseen. Todistusaineistoihin viitataan, mutta niitä ei pelkästään toisteta. Kolme erillistä riskiä eritellään selkeästi.

### Miten tilanne pitäisi hoitaa? — Heikko versio

> Pitäisi kieltää ChatGPT:n käyttö ja antaa koulutusta. Sitten asia on hoidettu.

**Mikä tekstissä on ongelmana:** Teksti jää pinnalliseksi. Siinä ei ole selkeää toimenpidesuunnitelmaa, aikataulua eikä vastuuhenkilöä.

### Miten tilanne pitäisi hoitaa? — Vahva versio

> Esitän kolmiportaisen toimintamallin. **Välittömästi (24 h):** nykyinen käytäntö keskeytetään, asiakaspalvelijoille tiedotetaan asiasta ja tietosuojavastaavalle toimitetaan alustava selvitys. **Lyhyellä aikavälillä (2 viikkoa):** otetaan käyttöön yritysversio tekoälypalvelusta, jossa on tietojenkäsittelysopimus ja jossa syötteiden tallennus on estetty. Lisäksi laaditaan kirjallinen ohjeistus sallituista ja kielletyistä syötteistä. **Pysyvästi:** tekoälyn käyttö lisätään tietoturvakoulutuksen vakio-osaksi, ja jokaisen uuden tekoälytyökalun käyttöönotto edellyttää IT- ja tietosuojavastaavan hyväksyntää.

**Mikä toimii:** Toimenpiteet on aikataulutettu, vastuutettu ja konkretisoitu. Lukija tietää, mitä pitää tehdä heti ja mitä kahden viikon kuluessa.

## Promptausvinkit: miten ohjaat tekoälyä tässä tehtävässä

Tämän tehtävän tarkoitus ei ole, että kirjoitat tekstin yksin tyhjästä. Tarkoitus on, että **osaat ohjata** tekoälyä tuottamaan asiantuntijatekstiä ja muokkaat lopputuloksen omaksesi. Hyödynnä seuraavia periaatteita:

**1. Anna tekoälylle konteksti, älä pelkkää aihetta.**

*Heikko prompt:* ”Kirjoita asiantuntijalausunto tietovuodosta.”

*Vahva prompt:* ”Olen IT-vastaava verkkokauppayrityksessä. Tehtäväni on kirjoittaa asiantuntijalausunto, jossa analysoin seuraavan tilanteen: [kuvaa skenaario]. Lausunnon tulee perustua näihin käsitteisiin: hallusinaatio, kontekstimuisti, tekijänoikeudet ja vastuullisen käyttäjän tarkistuslista. Auta minua jäsentämään analyysi. Älä kirjoita lopullista tekstiä, vaan anna ehdotuksia rakenteesta ja näkökulmista.”

**2. Liitä mukaan oma todistusaineistosi.**

Liitä prompttiin omat muistiinpanosi tunneilta 3, 5 ja 7. Pyydä tekoälyä käyttämään niitä argumentaation pohjana, ei keksimään uutta. Näin lausuntosi perustuu siihen, mitä *sinä* olet oppinut, eikä siihen, mitä malli sattuu tuottamaan.

**3. Pyydä useita versioita ja valitse niistä paras.**

Voit esimerkiksi pyytää: ”Anna kolme erilaista tapaa aloittaa lausunto: yksi neutraali, yksi terävä ja yksi varovainen.” Tämän jälkeen valitset version, joka sopii parhaiten omaan tyyliisi, ja muokkaat siitä oman tekstisi.

**4. Tarkista, älä luota sokeasti.**

Tekoäly voi hallusinoida. Erityisesti se voi keksiä lakipykäliä, sääntelyn yksityiskohtia ja vuosilukuja. Jos lausuntosi väittää esimerkiksi, että ”GDPR:n artikla 17 kieltää tämän”, tarkista artiklan sisältö itse. Asiantuntija ei lähetä tekstiä, jota hän ei ole tarkistanut.

::: luokka
## Tarkistuslista ennen palautusta

Käy nämä kohdat läpi ennen kuin palautat tehtävän:
:::

::: verkko
## Tarkistuslista ennen kuin työ on valmis

Käy nämä kohdat läpi ennen kuin toteat työsi valmiiksi:
:::

- ☐ Lausunto on 750–1000 sanaa.
- ☐ Kaikki neljä osaa on käsitelty: mitä tapahtui, miksi se tapahtui, miten tilanne pitäisi hoitaa ja kuka kantaa vastuun.
- ☐ Käytin vähintään kahta omaa todistusaineistoani tunneilta 3, 5 ja 7 ja viittasin niihin selkeästi.
- ☐ Käytin teoriaosion käsitteitä täsmällisesti, en suurpiirteisesti.
- ☐ Toimenpide-ehdotuksissa on konkretiaa: kuka tekee, mitä tekee, milloin tekee ja miten tekee.
- ☐ Vastuukysymys on käsitelty omana osanaan, ei vain mainittu sivulauseessa.
- ☐ Tarkistin tekstistä mahdolliset hallusinaatiot, kuten lait, vuosiluvut ja lähteet.
- ☐ Kieli on neutraalia ja asiantuntevaa: ei puhekieltä eikä tunteenpurkauksia.
- ☐ Teksti on minun näköiseni, ei tekoälyn muokkaamaton raakatuotos.
- ☐ Lopussa on selkeä johtopäätös, ei vain äkillinen tekstin päättyminen.

## Lopuksi

Asiantuntijalausunto on **näyttö osaamisestasi**: sekä kurssin sisällöstä että siitä taidosta, jota osio 2 lähtee syventämään eli tekoälyn ohjaamisesta. Et osoita osaamistasi sillä, että kirjoitat kaiken yksin. Osoitat sen sillä, että otat tekoälyn työpariksi, ohjaat sitä taitavasti ja tunnistat itse, mikä sen tuotoksessa on oikein ja mikä ei.

Tuomaripöydän takana ei istu kone. Siellä istut sinä.

---

## Lähteet ja tarkistuspäivä

- [NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [UNESCO: Recommendation on the Ethics of Artificial Intelligence](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence)
- [European Commission: GDPR principles](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr/overview-principles/what-data-can-we-process-and-under-which-conditions_en)

Tarkistettu 15.7.2026.
