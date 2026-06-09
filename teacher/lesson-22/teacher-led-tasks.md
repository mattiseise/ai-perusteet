# Opettajavetoiset tehtävät — oppitunti 22

## Aktiviteetti 1: Whitelist-mallit noin 20 minuuttia

### Tavoite

Aktiviteetin tavoitteena on auttaa opiskelijoita ymmärtämään, mitä **whitelist** tarkoittaa agenttien turvallisuudessa ja miksi agentille pitää määritellä tarkasti, mitä se saa tehdä.

**Opettajan painotus:** Korosta, että whitelist on turvallisuuden perusperiaate. Agentille ei anneta oikeuksia varmuuden vuoksi, vaan vain ne oikeudet, joita se tarvitsee tehtävänsä suorittamiseen.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> Whitelist tarkoittaa sallittujen toimintojen listaa. Agentti saa tehdä vain ne asiat, jotka on erikseen sallittu. Kaikki muu on kiellettyä. Tämä on tärkeä turvallisuusperiaate, koska agentille ei pidä antaa enempää oikeuksia kuin se oikeasti tarvitsee.

### Esittely: kolme whitelist-mallia

Näytä opiskelijoille kolme erilaista whitelist-esimerkkiä: liian tiukka, kohtuullinen ja liian löysä.

```
TIUKKA, liian rajoitettu:- CLI: vain ls- Tiedostot: saa vain lukea kansiota /reports/, ei saa kirjoittaa- Verkkohaku: ei sallittuKOHTUULLINEN:- CLI: ls, mkdir, cp- CLI: ei sallita komentoja rm tai rm -rf- Tiedostot: saa lukea kansiota /data/ ja kirjoittaa kansioon /reports/- Verkkohaku: sallittu vain luotetuilla sivustoilla, esimerkiksi Wikipedia ja hallitus.fiLIIAN LÖYSÄ:- CLI: kaikki komennot sallittu- Tiedostot: kaikki kansiot sallittu- Verkkohaku: kaikki sivustot sallittu
```

Kysy opiskelijoilta:

- Mikä näistä on turvallisin?
- Mikä näistä on käytännössä hyödyllisin?
- Miksi liian tiukka whitelist voi estää agenttia tekemästä työtään?
- Miksi liian löysä whitelist on vaarallinen?

**Esimerkki opetukseen**

Kysy opiskelijoilta, mitä tapahtuisi, jos analytiikka-agentti saisi lukea dataa mutta ei kirjoittaa raporttia. Sen jälkeen kysy, mitä tapahtuisi, jos sama agentti saisi poistaa kaikki tiedostot. Näin opiskelijat näkevät eron liian tiukan ja liian löysän oikeusmallin välillä.

### Ryhmätyö

Jaa opiskelijat pienryhmiin. Ryhmät suunnittelevat whitelistin yhdelle tai useammalle seuraavista agenttityypeistä:

1. **Asiakastukiagentti:** auttaa asiakkaita yleisissä kysymyksissä ja hakee tietoa ohjedokumenteista.
2. **Analytiikka-agentti:** lukee dataa, ajaa analyysin ja tuottaa raportin.
3. **Tapahtuma-agentti:** auttaa tapahtuman järjestelyissä ja voi lukea ilmoittautumislistoja tai ehdottaa aikataulumuutoksia.

Ryhmän tehtävänä on määritellä:

- mitä tiedostoja agentti saa lukea,
- mihin agentti saa kirjoittaa,
- mitä komentoja agentti saa käyttää,
- saako agentti tehdä verkkohakuja,
- mihin agentti ei saa koskaan koskea,
- missä tilanteessa agentin pitää pyytää ihmiseltä lupa.

| Oikeus tai toiminto | Sallitaan? | Perustelu | Milloin tarvitaan ihmisen hyväksyntä? |
| --- | --- | --- | --- |
| Tiedostojen lukeminen |  |  |  |
| Tiedostojen kirjoittaminen |  |  |  |
| CLI-komennot |  |  |  |
| Verkkohaku |  |  |  |
| Arkaluonteiset tiedot |  |  |  |

**Esitys ja keskustelu:**

Ryhmät esittelevät whitelistinsä. Vertailkaa ratkaisuja yhdessä.

Keskustelukysymyksiä:

- Miksi eri agenteilla on erilaiset oikeudet?
- Mikä oikeus on välttämätön agentin tehtävän kannalta?
- Mikä oikeus olisi liian suuri riski?
- Miten whitelist suojaa käyttäjää, organisaatiota ja järjestelmää?

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että whitelist määrittää agentin sallitut toiminnot.
- Opiskelijat osaavat erottaa liian tiukan, sopivan ja liian löysän whitelistin.
- Opiskelijat ymmärtävät, että agentille annetaan vain ne oikeudet, joita se oikeasti tarvitsee.

---

## Aktiviteetti 2: Orkestrointi — järjestys on kriittinen noin 20 minuuttia

### Tavoite

Aktiviteetin tavoitteena on näyttää opiskelijoille, että agentin työkalujen käyttö ei ole satunnaista. **Orkestrointi** tarkoittaa sitä, että agentti käyttää työkaluja oikeassa järjestyksessä ja siirtää yhden vaiheen tulokset seuraavan vaiheen käyttöön.

**Opettajan painotus:** Korosta, että oikeat työkalut eivät riitä, jos agentti käyttää niitä väärässä järjestyksessä. Työnkulun järjestys vaikuttaa suoraan lopputuloksen oikeellisuuteen ja turvallisuuteen.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> Agentti voi käyttää monia työkaluja, kuten tiedostoja, verkkohakua, komentoriviä ja raportin kirjoittamista. Näiden työkalujen järjestys on tärkeä. Jos agentti tekee vaiheet väärässä järjestyksessä, lopputulos voi olla virheellinen, tyhjä tai vaarallinen.

### Esittely: analytiikka-agentin prosessi

1. **Lue tiedostot:** agentti lukee esimerkiksi tiedoston `myyntitiedot.csv`.
2. **Hae verkosta taustatietoa:** agentti etsii markkinatrendejä ja kilpailijatietoa luotetuista lähteistä.
3. **Aja analyysiskripti:** agentti käyttää CLI:tä tai muuta työkalua datan analysointiin.
4. **Kirjoita raportti:** agentti kokoaa tulokset raportiksi.

**Väärän järjestyksen esimerkit:**

- Agentti ajaa analyysiskriptin ennen kuin tiedostot on luettu. Seurauksena voi olla virhe tai tyhjä analyysi.
- Agentti kirjoittaa raportin ennen kuin analyysi on tehty. Seurauksena on puutteellinen tai virheellinen raportti.
- Agentti tekee verkkohakuja lopuksi, vaikka taustatieto olisi pitänyt huomioida analyysin alussa.

### Ryhmätyö

Opiskelijat valitsevat yhden prosessin ja järjestävät työkalut oikeaan järjestykseen.

Esimerkkiprosesseja:

- asiakaspalautteiden analysointi,
- varaston seurantaan perustuva tilausraportti,
- uutisten seuranta ja päivittäinen kooste,
- myyntidatan analyysi ja kuukausiraportti.

**Tehtävä:**

Piirtäkää työnkulkukaavio, jossa näkyy:

- mikä on ensimmäinen vaihe,
- mitä työkalua käytetään missäkin vaiheessa,
- mitä tietoa vaihe tuottaa,
- mihin seuraava vaihe tarvitsee edellisen vaiheen tulosta,
- missä kohdassa tarvitaan ihmisen tarkistus.

**Työnkulun mallipohja**

|  |
| --- |
| **1. Syöte tai tiedon lukeminen** Mitä tietoa agentti saa ensin? |
| ↓ |
| **2. Taustatiedon haku tai tarkistus** Mitä lisätietoa tarvitaan? |
| ↓ |
| **3. Analyysi tai päätös** Mitä agentti päättelee? |
| ↓ |
| **4. Ihmisen tarkistus tarvittaessa** Missä kohdassa pysähdytään? |
| ↓ |
| **5. Toiminto tai raportti** Mitä agentti tekee lopuksi? |

**Keskustelu:**

- Mikä vaihe on kriittisin?
- Mikä vaihe ei saa tapahtua liian aikaisin?
- Mitä tapahtuu, jos agentti ohittaa tarkistusvaiheen?
- Miten työnkulun voi suunnitella niin, että virheet huomataan ajoissa?

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että agentin työkalujen käyttö tarvitsee suunnitellun järjestyksen.
- Opiskelijat osaavat kuvata yksinkertaisen agenttityönkulun vaiheittain.
- Opiskelijat ymmärtävät, että väärä järjestys voi aiheuttaa virheitä, tyhjiä tuloksia tai vaarallisia päätöksiä.

---

## Aktiviteetti 3: Riskiskenaariot noin 20 minuuttia

### Tavoite

Aktiviteetin tavoitteena on auttaa opiskelijoita tunnistamaan, että jokainen agentille annettu työkalu tuo mukanaan riskejä. Opiskelijat harjoittelevat riskin syntymisen, haitan ja ehkäisyn analysointia.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> Agentti voi tehdä hyödyllisiä asioita, jos sillä on työkaluja. Samat työkalut voivat kuitenkin aiheuttaa vahinkoa, jos agentti käyttää niitä väärin. Siksi jokaiselle työkalulle pitää miettiä rajoitukset, seuranta ja tarvittaessa ihmisen hyväksyntä.

### Esittely: kolme riskiskenaariota

```
TIEDOSTOT:Agentti kirjoittaa väärään kansioon tai poistaa tärkeitä tiedostoja.VERKKOHAKU:Agentti etsii tietoa epäluotettavista lähteistä, paljastaa salaisia tietoja hakukyselyssä tai käyttää kallista hakupalvelua hallitsemattomasti.CLI:Agentti ajaa vaarallisen komennon, kuten rm -rf /, ja voi poistaa koko järjestelmän.
```

### Ryhmätyö

Jokainen ryhmä valitsee yhden riskiskenaarion ja analysoi sen seuraavan rakenteen avulla:

1. **Miten riski syntyy?** Mitä agentti tekee väärin tai liian vapaasti?
2. **Mitä haittaa se aiheuttaa?** Kenelle syntyy vahinkoa ja millaista?
3. **Miten riski olisi voitu estää?** Mitä whitelist, rajoitus, seuranta tai ihmisen hyväksyntä olisi tarvittu?

| Riskiskenaario | Miten riski syntyy? | Mitä haittaa syntyy? | Miten riski estetään? |
| --- | --- | --- | --- |
|  |  |  |  |

**Esitykset:**

Ryhmät esittelevät riskinsä ja ehkäisykeinonsa.

**Opettajan tarkentavia kysymyksiä:**

- Mikä olisi pahin mahdollinen seuraus?
- Olisiko riski estettävissä pelkällä whitelistillä?
- Tarvitaanko lokitusta tai jäljitettävyyttä?
- Missä kohdassa ihmisen pitäisi hyväksyä toiminto?
- Miten käyttäjälle kerrotaan, mitä agentti aikoo tehdä?

**Opettajan tarkistuskysymys:** Jos opiskelijat ehdottavat vain yhtä suojauskeinoa, kysy: “Mitä tapahtuu, jos tämä suojaus pettää? Mikä olisi seuraava puolustuskerros?”

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että agentin työkalut tuovat sekä hyötyjä että riskejä.
- Opiskelijat osaavat analysoida riskin syntymisen, haitan ja ehkäisyn.
- Opiskelijat ymmärtävät whitelistien, rajoitusten, seurannan ja ihmisen hyväksynnän merkityksen.

---

## Aktiviteetti 4: Oikea työkalu oikeaan tehtävään noin 15 minuuttia

### Tavoite

Aktiviteetin tavoitteena on opettaa opiskelijoille, että agentille ei pidä antaa kaikkia mahdollisia työkaluja, vaan vain tehtävän kannalta tarpeelliset työkalut. Työkalujen valinta perustuu tehtävään, riskeihin ja tarvittavaan tietoon.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> Jokainen tehtävä tarvitsee erilaiset työkalut. Turvallinen agentti ei saa kaikkia oikeuksia varmuuden vuoksi. Se saa vain ne työkalut, joita tehtävä oikeasti vaatii.

### Esittely: kolme tehtävää ja niiden työkalutarpeet

| Tehtävä | Tarvittavat työkalut | Mitä ei yleensä tarvita? |
| --- | --- | --- |
| **Laskun käsittely** | Tietokanta- tai API-yhteys laskutietoihin sekä mahdollisesti lokitiedostot. | Verkkohaku, ellei laskuttajan taustaa tarvitse erikseen tarkistaa. |
| **Uutiskooste** | Verkkohaku ajankohtaisiin uutisiin ja koosteen kirjoittaminen tiedostoon. | Laajat kirjoitusoikeudet tuotantojärjestelmiin ilman hyväksyntää. |
| **Varaston seuranta** | Varaston tiedostojen lukeminen ja ilmoituksen lähettäminen. | Verkkohaku, jos seuranta perustuu vain sisäisiin tiedostoihin. |

### Ryhmätyö

Opiskelijat valitsevat yhden tehtävän ja päättävät, mitä työkaluja agentti tarvitsee.

Ryhmän tulee täyttää seuraava taulukko:

| Tehtävä | Tarvittava työkalu | Miksi tarvitaan? | Mitä ei sallita? | Mikä riski jää jäljelle? |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

**Keskustelu:**

- Mikä työkalu on tehtävän kannalta välttämätön?
- Mikä työkalu olisi turha tai vaarallinen?
- Mitä agentti ei saa tehdä, vaikka sillä olisi teknisesti mahdollisuus siihen?
- Miten rajaisitte työkalujen käyttöä?

### Odotettu oppimistulos

- Opiskelijat osaavat valita agentille tehtävän kannalta sopivat työkalut.
- Opiskelijat ymmärtävät, miksi kaikkien työkalujen antaminen agentille on riski.
- Opiskelijat osaavat perustella, miksi jokin työkalu sallitaan ja jokin toinen kielletään.

---

## Herättävät keskustelukysymykset

- **Mitä tapahtuu, jos whitelist on liian tiukka?**
- **Mitä tapahtuu, jos whitelist on liian löysä?**
- **Voiko agentti tehdä vahinkoa pelkällä verkkohakulla?**
- **Mitä tapahtuu, jos agentti kutsuu työkalut väärässä järjestyksessä?**
- **Milloin agentin pitää pyytää ihmiseltä lupa ennen työkalun käyttöä?**
- **Miksi agentille ei pidä antaa järjestelmänvalvojan oikeuksia ilman tarkkoja rajoituksia?**

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- selittää, mitä **whitelist** tarkoittaa agentin turvallisuudessa,
- suunnitella agentille sopivia sallittuja ja kiellettyjä toimintoja,
- kuvata, miksi työkalujen käyttöjärjestys eli **orkestrointi** on tärkeää,
- tunnistaa agentin työkaluihin liittyviä riskejä,
- ehdottaa riskien ehkäisyyn sopivia keinoja, kuten rajoituksia, seurantaa, lokitusta ja ihmisen hyväksyntää,
- valita oikeat työkalut oikeaan tehtävään ja perustella valinnat turvallisuuden näkökulmasta.

---
