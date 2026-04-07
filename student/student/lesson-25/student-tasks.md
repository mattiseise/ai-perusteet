# Opiskelutehtävät: Ihminen portinvartijana — human-in-the-loop

## Projektin aihio 5: Suunnittele ihmisen rooli

Tämä on viimeinen viidestä projektin aihiosta, jotka keräät Agentit-osion aikana. Käytät näitä aihioita oppitunneilla 26–27, kun rakennat oman n8n-agenttityönkulun ja esittelet sen. Säilytä tämä huolellisesti.

### Tehtävä

Palaa projektin aihioihin 1–4 (oppitunnit 19, 21, 23 ja 24), joissa valitsit ongelman, suunnittelit muistin, päättelymallin ja turvakerroksen. Suunnittele nyt, missä kohtaa ihminen on mukana agenttisi työnkulussa. Kirjoita lyhyt suunnitelma (150–200 sanaa), jossa vastaat neljään kysymykseen: Missä kohdissa agenttisi työnkulkua ihmisen täytyy hyväksyä tai hylätä agentin päätös? Millainen hyväksyntäportti on — mitä tietoa ihminen näkee ja miten nopeasti hänen täytyy reagoida? Mitä tapahtuu, jos ihminen ei vastaa ajoissa? Miten agentti voi oppia ihmisen päätöksistä ajan myötä?

### Miksi tämä on tärkeä

Oppitunneilla 26–27 rakennat n8n-työnkulun, jossa ihmisen rooli tarkoittaa konkreettisia hyväksyntäsolmuja. Ilman tätä suunnitelmaa et tiedä, mihin kohtiin työnkulkuasi tarvitset pysäytyskohtia. Yhdessä aihioiden 1–4 kanssa sinulla on nyt kattava suunnitelma koko agenttiprojektillesi.

Alla olevat harjoitustehtävät auttavat sinua ymmärtämään, milloin ihmisen osallistuminen on välttämätöntä ja miten hyväksyntäportit suunnitellaan käytännössä.

---

## Tehtävä 25.1: Milloin ihminen täytyy päätökseen? — kolme sääntöä

### Tavoite
Oppia tunnistamaan, mitkä päätökset vaativat ihmisen hyväksynnän. Tämä auttaa sinua projektin aihiossa määrittelemään, mihin kohtiin oma agenttisi tarvitsee hyväksyntäportteja.

### Ohjeet

Sinulla on kuusi agenttipäätöstä. Jokaiselle päätä, tarvitaanko ihmisen hyväksyntä (kyllä, ei tai ehkä), perustele valinta kolmen säännön avulla (rahaa tai rakenne, epävarmuus, poikkeama) ja tunnista, kuka hyväksyy (asiakaspalvelupäällikkö, myyntipäällikkö, tekniikkajohtaja).

Päätökset:

1. Asiakas haluaa tuotteen väriä vaihtaa (väri on varastossa)
2. Asiakas haluaa 50 % alennusta pitkässä sopimuksessa
3. Asiakas kysyy "Mikä on hinta?"
4. Uusi liikekumppani haluaa integroida tietokantamme
5. Asiakas haluaa palauttaa tuotteen (palautusaika on voimassa)
6. Agentti löytää asiakkaan lokeista anomalian (100 ostoa yhdessä tunissa)

---

## Tehtävä 25.2: Hyväksyntäportti — selkeä ja nopea

### Tavoite
Oppia suunnittelemaan hyväksyntäportti, jonka ihminen voi käydä läpi nopeasti. Tämä on suoraan käytettävissä projektin aihiossa ja n8n-työnkulussa.

### Ohjeet

Muotoile hyväksyntäportti seuraavalle tilanteelle: "Asiakas pyytää 50 % alennusta pitkälle sopimukselle. Agentti ehdottaa hyväksyntää."

Portin pitäisi sisältää: mitä päätöstä pyydetään, ketä se koskee, miksi agentti ehdottaa hyväksyntää, mitä tapahtuu jos hyväksyy, mitä tapahtuu jos hylkää ja mitä tehdään jos vastaus ei tule 24 tunnissa. Tavoite on, että ihminen voi käydä portin läpi 30 sekunnissa.

---

## Tehtävä 25.3: Human-in-the-loop-työnkulku

### Tavoite
Ymmärtää, miten agentti ja ihminen tekevät yhteistyötä monivaiheisessa prosessissa. Tämä auttaa sinua projektin aihiossa hahmottamaan, miltä oman agenttisi hybridi-työnkulku näyttää kokonaisuutena.

### Ohjeet

Kuvittele palautuspyynnön käsittelyä viidessä vaiheessa: agentti analysoi asiakkaan viestin, hyväksyntäportti 1 (onko palautusaika voimassa?), agentti lähettää palautustiedot, hyväksyntäportti 2 (tarjotaanko alennusta seuraavaan tilaukseen?) ja agentti lähettää jatkoviestin.

Kirjoita kustakin vaiheesta, mitä agentti tekee, mikä on hyväksyntäportin kysymys (jos on), mitä ihminen vastaa ja mitä agentti tekee seuraavaksi.

---

## Tehtävä 25.4: Agentin oppiminen palautteesta

### Tavoite
Ymmärtää, miten ihmisen päätökset voivat ohjata agentin toimintaa ajan myötä — ja mitä riskejä siihen liittyy.

### Ohjeet

Kuvittele agenttia, joka tekee alennusehdotuksia. Sillä on kaksi hyväksyjää: hyväksyjä A hyväksyy suuret alennukset (40–50 %) ja hyväksyjä B hyväksyy vain pienet (10–15 %). Kuvaile, miten agentti voisi oppia näistä eroista, miten se mukauttaisi ehdotuksensa eri hyväksyjille, mitä dataa se tallentaa tätä varten ja mitä riskejä oppimiseen liittyy (entä jos agentti oppii väärät asiat?).
