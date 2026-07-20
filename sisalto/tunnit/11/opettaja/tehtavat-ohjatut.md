# Opettajavetoiset tehtävät — datavirta näkyväksi

## Tehtävä 1 — Sama aineisto, kolme ympäristöä

**Kesto:** 15 minuuttia

**Käyttö:** Tunnin yhteinen ohjattu esimerkki
**Tavoite:** Opiskelija huomaa, että käyttöpäätös riippuu sekä aineistosta että koko käsittely-ympäristöstä.

### Valmistelu

Kirjoita taululle kuvitteellinen aineisto:

> **Tiedosto:** `palautteet.txt`
>
> **Sisältö:** osallistujien nimet, sähköpostiosoitteet ja vapaamuotoiset palautteet

Valmistele kolme ympäristökorttia:

1. **Yleinen pilvipalvelu**
   Keskusteluhistoria tallentuu. Organisaation hyväksynnästä ei ole tietoa.
2. **Organisaation hallittu palvelu**
   Palvelusta on sopimus. Käyttö on hyväksytty anonymisoitujen palautteiden tiivistämiseen.
3. **Paikallinen ajo**
   Malli toimii työasemalla. Sovelluksen verkkohaku on oletuksena päällä.

### Toteutus

#### 1. Tunnista aineisto — 3 minuuttia

Kysy:

- Mitä henkilötietoja tiedostossa on?
- Tarvitaanko niitä palautteiden tiivistämiseen?
- Mitä muuta tunnistettavaa palautteissa voi olla?

Kirjaa vastaukset näkyviin. Älä siirry työkalun valintaan ennen aineiston tunnistamista.

#### 2. Piirrä kolme datavirtaa — 7 minuuttia

Piirrä jokaisesta ympäristöstä oma reitti:

> laite → käyttöliittymä → käsittely → säilytys tai jatkokäyttö → vastaus

Pyydä opiskelijoita täydentämään:

- mikä tieto poistuu laitteelta
- kuka käsittelee sitä
- mikä kohta on varmistettu
- mikä kohta tarvitsee lisätietoa

Paikallisen ajon kohdalla kysy erikseen, mitä verkkohaku muuttaa.

#### 3. Tee päätös — 5 minuuttia

Äänestäkää jokaisesta ympäristöstä:

- käytä
- käytä rajatusti
- älä käytä tähän aineistoon

Hyvä yhteinen johtopäätös voi olla:

- yleistä pilvipalvelua ei käytetä tällä aineistolla ilman lisätietoa ja hyväksyntää
- hallittua palvelua käytetään vasta tarpeettomien tunnistetietojen poistamisen jälkeen
- paikallisen ajon verkkohaku poistetaan käytöstä ja datavirta tarkistetaan ennen päätöstä

Korosta, ettei ympäristön nimi yksin ratkaissut mitään. Päätös syntyi aineistosta, asetuksista ja käyttöehdoista yhdessä.

### Tarkistuskysymys

> Mikä yksittäinen muutos voisi muuttaa päätöksen?

Hyviä vastauksia ovat esimerkiksi aineiston anonymisointi, organisaation hyväksyntä, säilytysajan selviäminen tai ulkoisen yhteyden poistaminen.

---

## Tehtävä 2 — Epäselvä kohta on pysähtymismerkki

**Kesto:** 12–15 minuuttia

**Käyttö:** Varatehtävä tai syventävä purku
**Tavoite:** Opiskelija oppii erottamaan tiedon, päätelmän ja oletuksen.

### Tilanne

Anna ryhmille seuraava palvelukuvaus:

> Palvelu osaa tiivistää asiakirjoja. Sen esittelysivulla luvataan ”turvallista käyttöä”. Sivulla ei kerrota säilytysaikaa, mahdollista ihmisen tekemää tarkastusta eikä sitä, käytetäänkö sisältöä palvelun kehittämiseen. Organisaatio ei ole vielä julkaissut palvelusta käyttöohjetta.

### Ryhmän tehtävä

Täyttäkää kolme saraketta:

| Tiedämme | Päättelemme | Meidän pitää selvittää |
| --- | --- | --- |
| Palvelu käsittelee asiakirjoja. | ”Turvallinen” voi viitata tekniseen suojaukseen. | Säilytysaika, jatkokäyttö, käsittelijät ja organisaation hyväksyntä. |

Lisätkää lopuksi käyttöpäätös kahdelle aineistolle:

1. kuvitteellinen harjoitusteksti
2. henkilötietoja sisältävä asiakirja

### Purku

Kysy:

- Miksi sama epäselvä palvelukuvaus johti eri päätökseen eri aineistoilla?
- Mikä väite oli houkutteleva mutta liian epätarkka?
- Keneltä puuttuva tieto pitäisi tarkistaa?

### Mallijohtopäätös

Kuvitteellisella harjoitustekstillä palvelua voi olla mahdollista kokeilla. Henkilötietoja sisältävää asiakirjaa ei lähetetä ennen kuin käsittelyehdot ja organisaation hyväksyntä on selvitetty.

---

## Arviointihavainnot

Seuraa, pystyykö opiskelija:

- nimeämään aineiston ennen työkalua
- erottamaan mallin, palvelun ja ympäristön
- kuvaamaan aineiston reitin myös syötteen lähettämisen jälkeen
- merkitsemään puuttuvan tiedon oletuksen sijasta
- muuttamaan päätöstä, kun aineisto tai datavirta muuttuu

Väärästä ensivastauksesta ei moitita. Pyydä opiskelijaa näyttämään, mihin oletukseen vastaus perustui, ja auta korjaamaan juuri se kohta.
