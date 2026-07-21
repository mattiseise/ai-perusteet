# Opettajavetoiset tehtävät

## Näin käytät tehtäviä

Tehtävät tukevat saman roskapostiesimerkin käsittelyä. Ne eivät ole yksi pitkä tehtävälista. Perusreitillä käytä tehtävää A aineistojaon yhteydessä ja tehtävää C ennen ydintuotoksen C-osaa. Tehtävä B sopii lyhyeksi välitarkistukseksi. Opiskelijan varsinainen tallennettava työ on tehtävä 2.1.

## Ohjattu tehtävä A: Harjoitus, harjoituskoe ja lopullinen koe

### Tavoite

Opiskelija erottaa koulutus-, validointi- ja testiaineiston tehtävät.

### Toteutus, noin 12 minuuttia

Kirjoita näkyviin kolme otsikkoa:

- harjoitustehtävät
- harjoituskoe
- lopullinen koe.

Pyydä pareja yhdistämään niihin sanat **koulutusaineisto**, **validointiaineisto** ja **testiaineisto**. Anna sen jälkeen kolme lyhyttä kuvausta:

1. Näiden viestien avulla roskapostimalli oppii.
2. Näiden viestien avulla kahta malliversiota verrataan.
3. Näillä sivussa pidetyillä viesteillä valittu malli arvioidaan viimeisen kerran ennen käyttöönottoa.

Pari sijoittaa kuvaukset oikeiden otsikoiden alle ja perustelee yhden valinnan.

### Purku

Kysy: ”Mitä tapahtuu, jos lopullisen kokeen vastauksia käytetään harjoitteluun?” Kokoa vastaus omin sanoin: testi alkaa ohjata rakentamista eikä enää ole riippumaton tarkistus.

Älä jää kiinni täydelliseen koevertaukseen. Sen tehtävä on auttaa muistamaan aineistojen eri roolit.

---

## Ohjattu tehtävä B: Uusi viesti paljastaa eron

### Tavoite

Opiskelija erottaa yleistymisen ja ylioppimisen.

### Toteutus, noin 8 minuuttia

Kuvaa kaksi roskapostimallia:

- Malli A tunnistaa koulutusaineiston viestit lähes täydellisesti mutta erehtyy usein uusissa viesteissä.
- Malli B tekee koulutusaineistossa muutaman virheen mutta tunnistaa hyvin myös uudet samankaltaiset viestit.

Pyydä opiskelijoita valitsemaan, kumpi malli todennäköisemmin yleistää ja kummassa näkyy ylioppimisen riski. Pari täydentää kaksi lausetta:

- ”Yleistyminen näkyy siinä, että…”
- ”Ylioppiminen näkyy siinä, että…”

### Purku

Korosta, ettei harjoittelun paras tulos yksin ratkaise mallin käyttökelpoisuutta. Uudet tapaukset ovat olennainen tarkistus.

---

## Ohjattu tehtävä C: Sama palvelu, kaksi kuvausta

### Tavoite

Opiskelija ymmärtää, etteivät kapea ja generatiivinen tekoäly sulje toisiaan pois, ja erottaa ne AGI- ja ASI-väitteistä.

### Toteutus, noin 12 minuuttia

Kirjoita taululle yksi kuvitteellinen sähköpostipalvelu:

> Palvelu tunnistaa roskapostin ja luonnostelee käyttäjälle varoitusviestin.

Kysy ryhmältä kaksi kysymystä:

1. Mikä toiminto on rajattu tunnistustehtävä?
2. Mikä toiminto tuottaa uutta sisältöä?

Merkitse tunnistamisen viereen **kapea tekoäly** ja luonnoksen viereen **generatiivinen tekoäly**. Piirrä niiden ympärille yksi yhteinen kehys. Sama palvelu voi sisältää molemmat toiminnot.

Lisää sen jälkeen kaksi väitettä:

- ”Palvelu oppii itsenäisesti minkä tahansa uuden työn ihmisen tavoin.”
- ”Palvelu ylittää ihmisen kyvyt laajasti kaikilla aloilla.”

Opiskelijat nimeävät ensimmäisen AGI-väitteeksi ja toisen ASI-väitteeksi. Pyydä heitä kertomaan, miksi alkuperäinen roskapostiesimerkki ei vielä tue kumpaakaan väitettä.

### Mallipurku

Roskapostin tunnistaminen osoittaa rajattua luokittelukykyä. Varoitusviestin luonnosteleminen osoittaa tekstin tuottamisen kykyä. Kumpikaan ei yksin osoita joustavaa oppimista hyvin erilaisissa tehtävissä eikä ihmisen kykyjen laajaa ylittämistä.

---

## Ohjattu tehtävä D: Miksi seurantaa tarvitaan? — valinnainen

### Tavoite

Opiskelija tunnistaa käytönaikaisen seurannan tarpeen ilman uusia erikoistermejä.

### Toteutus, noin 10 minuuttia

Anna tilanne:

> Roskapostimalli testattiin tammikuussa. Syksyllä huijausviestit on kirjoitettu uudella tavalla, ja niitä jää aiempaa enemmän saapuneisiin.

Pyydä pareja vastaamaan:

1. Mitä virhettä seurannassa pitäisi laskea tai tarkastella?
2. Miksi tammikuun hyvä testitulos ei riitä syksyllä?
3. Mitä pitää tehdä ennen korjatun mallin käyttöönottoa?

Hyvä vastaus mainitsee muuttuneet viestit, virheiden havaitsemisen sekä uuden version kouluttamisen ja erillisen testaamisen. Malli ei korjaa itseään automaattisesti pelkästään näkemällä uusia viestejä.

## Tunnin lopun yhteinen tarkistus

Pyydä jokaista opiskelijaa valitsemaan yksi väite ja jatkamaan sitä ääneen tai kirjallisesti:

- ”Testiaineisto pidetään erillään, koska…”
- ”Mallia seurataan käytössä, koska…”
- ”Kapea ja generatiivinen voivat kuvata samaa järjestelmää, koska…”
- ”Hyvä roskapostin tunnistus ei osoita AGI:a tai ASI:a, koska…”

Jos vastaus jää kesken, tarjoa yksi konkreettinen esimerkki ja anna opiskelijan yrittää uudelleen. Tavoite on käsitteen ymmärtäminen, ei nopea vastaaminen.
