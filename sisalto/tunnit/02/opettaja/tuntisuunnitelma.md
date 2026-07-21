# Opettajan materiaalit — oppitunti 2

## Tunnin ydin

Tunti rakentuu yhden roskapostiesimerkin ja kolmen kysymyksen ympärille:

1. Miten malli oppii esimerkeistä ja miten sen toiminta tarkistetaan?
2. Miksi mallia pitää seurata käytössä?
3. Miksi nykyisen järjestelmän onnistuminen ei vielä osoita AGI:a tai ASI:a?

Pidä sama esimerkki mukana koko tunnin ajan. Kun tilanne pysyy tuttuna, opiskelijan huomio voi kohdistua käsitteisiin eikä uuden toimintaympäristön ymmärtämiseen.

## Oppimistavoitteet

Tunnin jälkeen opiskelija osaa:

- kuvata koulutus-, validointi- ja testiaineiston eri tehtävät arkisella koevertauksella,
- selittää yleistymisen ja ylioppimisen eron,
- kertoa, miksi mallia seurataan käyttöönoton jälkeen,
- erottaa kapean ja generatiivisen tekoälyn toisistaan ja ymmärtää, että sama järjestelmä voi olla molempia,
- kuvata AGI:n ja ASI:n perusidean sekä erottaa ne nykyisten järjestelmien osoitetuista kyvyistä.

**Tunnin ydinviesti:** Malli oppii koulutusaineistosta, rakentamisen valintoja tarkistetaan validointiaineistolla ja valittu malli arvioidaan erillisellä testiaineistolla. Käyttöönoton jälkeen toimintaa seurataan. Hyvä rajattu tai generatiivinen suoritus ei yksin osoita AGI:a tai ASI:a.

## Pedagoginen eteneminen

### 1. Aloita yhdestä tutusta virheestä

Kysy, onko tärkeä viesti joskus päätynyt roskapostiin tai huijausviesti saapuneisiin. Jos opiskelijoilla ei ole kokemusta sähköpostista, kuvaa tilanne itse: järjestelmä lajittelee viestejä kahteen kansioon mutta voi erehtyä.

Näytä ensin ihmisen kirjoittama sääntö: ”Jos lähettäjä on estolistalla, siirrä viesti roskapostiin.” Vertaa sitä malliin, joka on koulutettu valmiiksi merkityillä viesteillä. Kerro myös, että todellinen palvelu voi yhdistää sääntöjä ja mallin arvioita.

### 2. Tee aineistojako näkyväksi koevertauksella

Piirrä kolme laatikkoa: **koulutus**, **validointi** ja **testi**. Käytä rinnalla opiskelun vertausta:

- koulutusaineisto vastaa harjoitustehtäviä,
- validointiaineisto vastaa harjoituskoetta, jonka avulla huomataan korjattavaa,
- testiaineisto vastaa lopullista koetta, jonka vastauksia ei katsota harjoittelun aikana.

Tavoitteena ei ole tekninen yksityiskohtaisuus. Riittää, että opiskelija ymmärtää, miksi sama aineisto ei voi toimia yhtä aikaa harjoitteluna ja riippumattomana viimeisenä tarkistuksena.

### 3. Selitä yleistyminen ja ylioppiminen samalla vertauksella

Hyvin yleistävä malli tunnistaa myös uudenlaisen roskapostiviestin. Ylioppinut malli muistaa koulutusviestien yksityiskohtia mutta hämmentyy, kun viestin muoto muuttuu.

Palaa opiskeluun: ulkoa opeteltu vastausrivi ei auta, jos kysymys esitetään uudella tavalla. Pyydä opiskelijaa kertomaan ero yhdellä omalla virkkeellä ennen etenemistä.

### 4. Jatka käyttöönottoon ja seurantaan

Kerro, ettei hyvä testi päätä työtä. Käytössä seurataan esimerkiksi väärään kansioon päätyneitä viestejä ja uudenlaisia huijausviestejä. Jos toiminta heikkenee, syy selvitetään. Uusi versio koulutetaan ja testataan ennen käyttöönottoa.

Korosta yhtä rajaa: käytössä oleva malli ei automaattisesti opi jokaisesta uudesta viestistä.

### 5. Erota kaksi nykyistä kuvaustapaa

Roskapostin tunnistaminen on rajattu tehtävä ja siksi esimerkki **kapeasta tekoälystä**. Varoitusviestin luonnosteleminen on sisällön tuottamista ja siksi **generatiivista tekoälyä**.

Älä pyydä valitsemaan näistä vain yhtä koko järjestelmälle. Kapeus kertoo kykyjen rajauksesta ja generatiivisuus sisällön tuottamisesta. Sama järjestelmä voi olla molempia.

### 6. Vedä selvä raja AGI:hin ja ASI:hin

Käsittele AGI ja ASI näkyvästi mutta tiiviisti:

- AGI tarkoittaisi joustavaa oppimista ja toimimista hyvin erilaisissa tehtävissä. Yleisesti hyväksyttyä nykyistä esimerkkiä ei ole.
- ASI tarkoittaisi ihmisen kykyjen laajaa ylittämistä. Se on hypoteettinen ja spekulatiivinen käsite.

Palaa roskapostiesimerkkiin. Täydellinenkään tulos yhdessä testissä ei osoita, että järjestelmä oppisi minkä tahansa tehtävän tai ylittäisi ihmisen kyvyt laajasti. AGI ja ASI eivät myöskään ole mallin elinkaaren seuraavia vaiheita.

## 90 minuutin toteutus ja eriyttäminen

Opiskelija täydentää ydintuotostaan kahdessa osassa, jotta kirjoittaminen ei kasaannu tunnin loppuun.

| Aika | Vaihe | Opettajan tehtävä | Opiskelijan toiminta |
|---|---|---|---|
| 0–8 min | Aloitus | Esittele roskapostivirhe ja tunnin kolme kysymystä | Kuvaa, millaisen virheen lajittelu voi tehdä |
| 8–23 min | Koulutus, validointi ja testi | Piirrä kolme laatikkoa ja käytä koevertauksia | Selittää laatikoiden tehtävät parille |
| 23–35 min | Yleistyminen ja ylioppiminen | Mallinna ero kahdella viestillä | Muotoilee eron omin sanoin |
| 35–45 min | Käyttöönotto ja seuranta | Näytä, mitä virheitä käytössä seurataan | Nimeää yhden seurattavan virheen |
| 45–62 min | Ydintuotos, osat A–B | Ohjaa tehtävän 2.1 ensimmäisiä viittä kohtaa | Laatii oppimisen, tarkistamisen ja seurannan kuvauksen |
| 62–74 min | Kapea, generatiivinen, AGI ja ASI | Tee nykyisyyden raja näkyväksi | Vertaa neljää käsitettä roskapostiesimerkissä |
| 74–85 min | Ydintuotos, osa C | Anna tarvittaessa lauseenalut | Kirjoittaa kolme rajauslausetta |
| 85–90 min | Tarkistus ja tallennus | Palaa kolmeen kysymykseen | Tarkistaa ja tallentaa yhden sivun tuotoksen |

## Eriyttäminen

### Tukireitti

Anna tehtävän 2.1 otsikot valmiina ja käytä seuraavia lauseenalkuja:

- ”Koulutusaineistolla malli…”
- ”Validointiaineistolla rakentaja…”
- ”Testiaineisto pidetään erillään, koska…”
- ”Käytössä seurataan…”
- ”Tämä ei vielä osoita AGI:a, koska…”

Opiskelija voi vastata puhumalla, jos opettaja tai pari kirjaa vastaukset.

### Syventävä reitti

Pyydä opiskelijaa lisäämään seurantaosaan vastuuhenkilö, keskeytysraja ja tapa, jolla korjattu versio testataan. Tehtävä 2.2 sopii lisätyöksi vasta ydintuotoksen jälkeen.

## Itsenäinen suoritus

Itsenäinen opiskelija etenee näin:

1. Lue teoria yhden roskapostiesimerkin mukana.
2. Tee viisi lyhyttä Harjoittele-tehtävää ja lue palaute.
3. Tee tehtävän 2.1 yhden sivun ydintuotos.
4. Tarkista, että vastaat kaikkiin kolmeen ydinkysymykseen ja että AGI ja ASI eivät näytä mallin elinkaaren seuraavilta vaiheilta.

Suoritus ei edellytä käyttäjätiliä tai ulkoista tekoälypalvelua.

## Arviointi

Hyväksytty suoritus osoittaa, että opiskelija:

- antaa koulutus-, validointi- ja testiaineistolle eri tehtävät,
- erottaa yleistymisen ylioppimisesta,
- nimeää perustellun syyn käytönaikaiselle seurannalle,
- ymmärtää, että kapea ja generatiivinen voivat kuvata samaa järjestelmää,
- erottaa nykyisen rajatun suorituksen AGI- ja ASI-käsitteistä.

Täydellistä ammattisanastoa tärkeämpää on, että ajatus on oikein ja opiskelija pystyy selittämään sen omin sanoin.

## Tunnin lopetus

Palaa alun kolmeen kysymykseen. Pyydä opiskelijaa viimeistelemään yksi lause:

> Roskapostimallin hyvä tulos kertoo…, mutta se ei vielä kerro…

Hyvä vastaus rajaa näytön roskapostin tunnistamiseen ja toteaa, ettei tulos yksin osoita yleistä tai ihmisen laajasti ylittävää älykkyyttä.
