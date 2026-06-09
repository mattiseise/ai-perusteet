# Opettajavetoiset tehtävät — oppitunti 21

## Aktiviteetti 1: Konteksti-ikkunan koko noin 15 minuuttia

### Tavoite

Aktiviteetin tavoitteena on auttaa opiskelijoita ymmärtämään, mitä **konteksti-ikkuna** tarkoittaa ja miksi sen koko vaikuttaa agentin toimintaan. Opiskelijat näkevät, että agentti ei välttämättä muista kaikkea aiemmasta keskustelusta, vaan toimii sen perusteella, mitä sillä on käytettävissään nykyisessä kontekstissa.

**Opettajan painotus:** Korosta, että konteksti-ikkuna ei ole sama asia kuin pitkäaikainen muisti. Konteksti-ikkuna sisältää vain sen tiedon, joka on mukana juuri tässä käsittelyhetkessä.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> Konteksti-ikkuna on kuin muistilaatikko. Siihen mahtuu vain tietty määrä keskustelua, ohjeita ja tietoa. Kun keskustelu kasvaa liian pitkäksi, vanhinta tietoa voi jäädä pois.

**Demo:**

1. Näytä opiskelijoille pitkä asiakaskeskustelu.
2. Merkitse taululle tai diaan, mitä agentti näkisi eri kokoisilla konteksti-ikkunoilla:
   - **10 viestin ikkuna:** agentti näkee vain viimeisimmät viestit.
   - **50 viestin ikkuna:** agentti näkee enemmän taustaa ja aiempia yksityiskohtia.
   - **200 viestin ikkuna:** agentti näkee laajemman keskusteluhistorian, mutta käsittely voi olla hitaampaa ja kalliimpaa.
3. Näytä fyysisesti, mitkä viestit jäävät pois pienellä ikkunalla. Voit esimerkiksi peittää vanhemmat viestit tai siirtää ne sivuun.

**Keskustelu:**

- **Mitä menetetään pienellä konteksti-ikkunalla?**
  Konteksti voi kadota, agentti voi kysyä samoja asioita uudelleen tai antaa vastauksen, joka ei huomioi aiempaa keskustelua.
- **Mitä suuresta konteksti-ikkunasta maksetaan?**
  Suuri ikkuna käsittelee enemmän dataa. Tämä voi lisätä kustannuksia, hidastaa käsittelyä ja kasvattaa tietosuojariskejä.
- **Missä on sopiva tasapaino?**
  Sopiva koko riippuu tehtävästä. Lyhyt asiakaspalvelukysymys tarvitsee vähemmän kontekstia kuin pitkä projektisuunnittelu tai tekninen ongelmanratkaisu.

### Tehtävä opiskelijoille

Opiskelijat suunnittelevat sopivan konteksti-ikkunan koon kolmelle erilaiselle tehtävälle ja perustelevat valintansa.

| Tehtävä | Sopiva konteksti-ikkuna | Perustelu |
| --- | --- | --- |
| Yksinkertainen asiakaskysymys |  |  |
| Pitkä tekninen ongelmanratkaisu |  |  |
| Usean viikon projektisuunnittelu |  |  |

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että konteksti-ikkuna rajaa sitä, mitä agentti voi hyödyntää vastauksessaan.
- Opiskelijat osaavat selittää, miksi liian pieni ikkuna voi heikentää vastauksen laatua.
- Opiskelijat ymmärtävät, että suuri konteksti-ikkuna ei ole aina paras ratkaisu, koska siihen liittyy kustannuksia, hitautta ja riskejä.

---

## Aktiviteetti 2: Vektoritietokanta noin 20 minuuttia

### Tavoite

Aktiviteetin tavoitteena on havainnollistaa, että **vektoritietokanta** etsii tietoa merkityksen perusteella eikä pelkästään täsmällisten sanojen avulla.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> Tavallinen haku etsii usein samoja sanoja. Vektoritietokanta yrittää löytää samankaltaisen merkityksen, vaikka sanat olisivat erilaisia. Se voi esimerkiksi ymmärtää, että “kortti hylättiin” ja “maksua ei voitu käsitellä” liittyvät samaan ongelmaan.

**Käsityöharjoitus:**

Anna opiskelijoille seuraavat viisi asiakastapauksen kuvausta:

- Maksua ei voida käsitellä.
- Kortti hylkäytyi.
- Laskutus epäonnistui.
- En saa tuotetta toimitetuksi.
- Maksujärjestelmä sanoo ei.

**Opiskelijoiden tehtävä:**

1. Lukekaa kaikki asiakastapaukset.
2. Ryhmitelkää tapaukset merkityksen perusteella.
3. Nimetkää ryhmät.
4. Perustelkaa, miksi sijoititte tapaukset juuri näihin ryhmiin.

**Odotetut ryhmät:**

| Ryhmä | Tapaukset | Perustelu |
| --- | --- | --- |
| **Maksuongelmat** | Maksua ei voida käsitellä, kortti hylkäytyi, laskutus epäonnistui, maksujärjestelmä sanoo ei. | Kaikki kuvaavat eri sanoilla samaa ongelma-aluetta: maksaminen ei onnistu. |
| **Logistiikkaongelma** | En saa tuotetta toimitetuksi. | Tapaus liittyy toimitukseen, ei maksamiseen. |

**Johtopäätös:**

Kerro opiskelijoille:

> Tämä on se periaate, jolla vektoritietokanta toimii. Se ei etsi vain samoja sanoja, vaan samankaltaista merkitystä. Siksi se voi löytää aiemman tapauksen, vaikka asiakas käyttäisi eri sanoja.

**Esimerkki opetukseen**

Vertaa vektoritietokantaa opiskelijoille tuttuun tilanteeseen: ihminen ymmärtää, että “läppäri ei yhdistä nettiin” ja “kone ei pääse Wi-Fiin” tarkoittavat todennäköisesti samaa ongelmaa, vaikka sanat ovat eri.

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että vektoritietokanta auttaa agenttia löytämään merkitykseltään samankaltaista tietoa.
- Opiskelijat osaavat erottaa sanahaun ja merkityshaun toisistaan.
- Opiskelijat näkevät, miksi pitkäaikainen muisti voi parantaa agentin vastauksia.

---

## Aktiviteetti 3: Tila ja muuttujat noin 25 minuuttia

### Tavoite

Aktiviteetin tavoitteena on opettaa opiskelijoille, mitä **tila** ja **muuttujat** tarkoittavat agentin toiminnassa. Opiskelijat harjoittelevat kuvaamaan prosessin vaiheita ja niihin liittyviä tietoja.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> Tila kertoo, missä vaiheessa prosessi on. Muuttujat kertovat, mitä tietoja agentin pitää muistaa kyseisessä vaiheessa. Esimerkiksi tilaus voi olla luotu, maksettu, pakattu tai lähetetty. Muuttujia voivat olla tilausnumero, asiakkaan nimi, maksun tila ja toimitusosoite.

### Esittely: tilauksen eteneminen

| Tila | Tärkeät muuttujat | Seuraava siirtymä |
| --- | --- | --- |
| **Luotu** | tilausnumero, asiakas, tuotteet | maksu vastaanotetaan |
| **Maksettu** | maksutapa, maksun tila, summa | tilaus siirtyy pakattavaksi |
| **Pakattu** | varastotiedot, pakkauspäivä, tuotteiden saatavuus | tilaus luovutetaan kuljetukseen |
| **Lähetetty** | seurantakoodi, kuljetusyhtiö, toimitusosoite | toimitus seurataan valmiiksi |

### Ryhmätyö

Opiskelijat valitsevat yhden prosessin:

- tilausprosessi,
- ajanvarausprosessi,
- asiakaspalvelupyyntö,
- asiakaspalautteen käsittely.

Ryhmän tehtävänä on määritellä:

1. kaikki prosessin tilat oikeassa järjestyksessä,
2. tärkeät muuttujat jokaisessa tilassa,
3. siirtymät tilasta toiseen,
4. tilanne, jossa agentin pitää pyytää ihmiseltä apua.

| Prosessin tila | Muuttujat | Siirtymä seuraavaan tilaan | Milloin pyydetään ihmiseltä apua? |
| --- | --- | --- | --- |
|  |  |  |  |

**Esitykset:**

Ryhmät esittelevät prosessinsa lyhyesti. Pyydä jokaista ryhmää näyttämään ainakin yksi tilasiirtymä ja siihen liittyvät muuttujat.

**Keskustelukysymys:**

“Mitä voi mennä pieleen, jos agentti unohtaa tärkeän muuttujan?”

**Mahdollisia vastauksia:**

- Agentti voi lähettää tilauksen väärään osoitteeseen.
- Agentti voi käsitellä maksamattoman tilauksen maksettuna.
- Agentti voi varata saman ajan kahdelle ihmiselle.
- Agentti voi antaa asiakkaalle väärää tietoa prosessin vaiheesta.

**Opettajan tarkistuskysymys:** Jos opiskelijat listaavat vain prosessin vaiheita, kysy: “Mitä tietoja agentin pitää muistaa juuri tässä vaiheessa, jotta se voi tehdä oikean päätöksen?”

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että tila kuvaa prosessin vaihetta.
- Opiskelijat osaavat nimetä muuttujia, joita agentin pitää muistaa eri vaiheissa.
- Opiskelijat ymmärtävät, että tilan tai muuttujan unohtaminen voi johtaa vakaviin virheisiin.

---

## Aktiviteetti 4: Agentin “soul” eli pysyvä identiteetti ja arvot noin 20 minuuttia

### Tavoite

Aktiviteetin tavoitteena on auttaa opiskelijoita ymmärtämään, miten agentin pysyvä **identiteetti**, **arvot** ja toimintaperiaatteet vaikuttavat sen päätöksiin ja viestintätyyliin.

### Opettajan ohjeet ja fasilitointi

**Selitys:**

Selitä opiskelijoille:

> Tässä yhteydessä soul tarkoittaa agentin pysyvää identiteettiä ja arvoja. Se ei tarkoita, että agentilla olisi oikea tietoisuus tai tunteet. Kyse on siitä, millaiseksi agentin toiminta ja tyyli on suunniteltu.

### Esittely: sama tilanne, eri identiteetti

**Tilanne:** Asiakas kysyy hyvitystä, koska toimitus on myöhässä.

| Agentin identiteetti | Mahdollinen vastaus | Mitä vastaus kertoo arvoista? |
| --- | --- | --- |
| **Aggressiivinen myyjä** | “Ymmärrän tilanteen, mutta suosittelen tilaamaan seuraavalla kerralla nopeamman toimituksen. Voit myös ostaa premium-palvelun.” | Agentti painottaa lisämyyntiä enemmän kuin asiakkaan kokemusta. |
| **Empaattinen neuvonantaja** | “Ymmärrän, että viivästys on harmillinen. Tarkistan ensin tilauksen tilanteen ja katson, onko hyvitys mahdollinen.” | Agentti painottaa asiakkaan kuulemista, reiluutta ja tilanteen selvittämistä. |

Kysy opiskelijoilta:

- Miten agentin identiteetti muutti vastausta?
- Kumpi vastaus sopii paremmin asiakaspalveluun?
- Voiko sama tieto johtaa eri päätökseen, jos agentin arvot ovat erilaiset?

### Ryhmätyö

Opiskelijat valitsevat agentin roolin. Esimerkkejä:

- asiakaspalvelubotti,
- myyntiagentti,
- terveydenhuollon neuvontabotti,
- opiskelun ohjaaja,
- projektimentori.

Ryhmän tehtävänä on kirjoittaa:

1. **Identiteetti:** kaksi lausetta siitä, millainen agentti on ja ketä se auttaa.
2. **Kolme perustavaa arvoa:** esimerkiksi turvallisuus, selkeys, rehellisyys, empaattisuus, tehokkuus tai käyttäjän oppiminen.
3. **Yksi rajaus:** mitä agentti ei tee, vaikka käyttäjä pyytäisi.

| Kohta | Ryhmän vastaus |
| --- | --- |
| **Identiteetti** |  |
| **Arvo 1** |  |
| **Arvo 2** |  |
| **Arvo 3** |  |
| **Rajaus** |  |

**Esitykset:**

Joitakin ryhmiä pyydetään lukemaan agenttinsa identiteetti ja arvot ääneen.

**Keskustelu:**

- Miten arvot vaikuttavat agentin päätöksiin?
- Mitä tapahtuu, jos agentin arvot ovat ristiriidassa käyttäjän pyynnön kanssa?
- Miksi terveydenhuollon agentilla pitää olla erilaiset arvot kuin myyntiagentilla?

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, että agentin identiteetti ja arvot vaikuttavat sen toimintaan.
- Opiskelijat osaavat kirjoittaa agentille selkeän identiteetin ja perusarvot.
- Opiskelijat ymmärtävät, että agentin arvot voivat ohjata päätöksiä myös epäselvissä tilanteissa.

---

## Aktiviteetti 5: Kokonaisuus — neljä tekijää yhdessä noin 15 minuuttia

### Tavoite

Aktiviteetin tavoitteena on yhdistää oppitunnin neljä keskeistä käsitettä: **konteksti-ikkuna**, **pitkäaikainen muisti**, **tila ja muuttujat** sekä agentin **identiteetti ja arvot**. Opiskelijat ymmärtävät, miten nämä tekijät yhdessä tuottavat vaikutelman älykkäästä toiminnasta.

### Tapaus

Näytä opiskelijoille seuraava tilanne:

> Asiakas ottaa yhteyttä ja sanoo: “Minulla oli ongelma viimeksi, ja nyt on taas sama tilanne.” Asiakas on ollut yrityksen asiakkaana kaksi vuotta.

### Vaiheittainen analyysi

1. **Konteksti-ikkuna:**

   ```

   Agentti näkee viimeisimmät viisi viestiä.

   Kysy opiskelijoilta:

   - Mitä agentti näkee?
   - Mitä se ei ehkä näe?
   - Voiko agentti ymmärtää ongelman pelkän nykyisen keskustelun perusteella?
2. **Pitkäaikainen muisti:**

   Agentti hakee vektoritietokannasta aiempia samankaltaisia tapauksia.

   Kysy opiskelijoilta:

   - Mitä aiemmista tapauksista voisi löytyä?
   - Voiko asiakas käyttää eri sanoja, vaikka ongelma olisi sama?
   - Miten vektoritietokanta auttaa tässä?
3. **Tila ja muuttujat:**

   Tilanne on esimerkiksi **avoin ongelma**.

   Mahdollisia muuttujia ovat:

   - asiakasnumero,
   - ongelman tyyppi,
   - edellisen tapauksen päivämäärä,
   - edellinen ratkaisu,
   - nykyisen tapauksen kiireellisyys,
   - asiakkaan tyytyväisyystaso.

   Kysy opiskelijoilta:

   - Mikä tieto on kriittinen päätöksen kannalta?
   - Mitä tapahtuu, jos agentti unohtaa edellisen ratkaisun?
   - Miten agentti tietää, onko asia yhä kesken vai uusi tapaus?
4. **Identiteetti ja arvot:**

   Agentin periaate voi olla esimerkiksi: `Lojaali asiakas saa etusijan, jos sama ongelma toistuu.`

   Kysy opiskelijoilta:

   - Miten tämä arvo vaikuttaa agentin päätökseen?
   - Antaako agentti asiakkaalle nopeamman käsittelyn?
   - Siirtääkö agentti tapauksen suoraan ihmiselle?
   - Miten vastaus muuttuisi, jos agentin tärkein arvo olisi kustannusten minimointi?
```

### Johtopäätös

Kerro opiskelijoille:

> Agentin näennäinen älykkyys ei synny yhdestä asiasta. Se syntyy siitä, että agentti yhdistää nykyisen keskustelun, pitkäaikaisen muistin, prosessin tilan, tarvittavat muuttujat sekä pysyvän identiteetin ja arvot.

Näytä yhteenveto:

Konteksti-ikkuna + pitkäaikainen muisti + tila ja muuttujat + identiteetti ja arvot = johdonmukainen agenttikäyttäytyminen

### Odotettu oppimistulos

- Opiskelijat ymmärtävät, miten eri muistamisen ja ohjauksen mekanismit toimivat yhdessä.
- Opiskelijat osaavat selittää, miksi agentti voi vaikuttaa älykkäältä ilman, että sillä olisi ihmisen kaltaista tietoisuutta.
- Opiskelijat ymmärtävät, että agentin toiminta riippuu sekä teknisestä muistista että suunnitelluista arvoista ja rajauksista.

---

## Herättävät keskustelukysymykset

- **Entä jos konteksti-ikkuna näkee viimeiset 20 viestiä, mutta vektoritietokanta löytää aiemman tapauksen, joka viittaa aivan eri ongelmatyyppiin? Kumpaa agentin pitäisi painottaa?**
- **Entä jos agentin identiteetti sanoo “älä anna asiakkaan odottaa liian kauan”, mutta prosessin tila on “odottaa maksua”? Miten agentin pitäisi päättää?**
- **Voivatko kaksi agenttia, joilla on sama muisti mutta eri arvot ja identiteetti, tehdä erilaisia päätöksiä?**
- **Milloin agentin pitäisi pysähtyä ja pyytää ihmisen arviota?**
- **Mitä riskejä syntyy, jos agentin pitkäaikainen muisti sisältää virheellistä tai vanhentunutta tietoa?**

## Arviointi

Opettaja arvioi opiskelijoiden kykyä:

- selittää, mitä **konteksti-ikkuna** tarkoittaa ja miten sen koko vaikuttaa agenttiin,
- kuvata, miten **vektoritietokanta** auttaa löytämään merkitykseltään samankaltaista tietoa,
- tunnistaa prosessin **tilat**, **muuttujat** ja **siirtymät**,
- kirjoittaa agentille selkeä **identiteetti**, **arvot** ja rajaus,
- selittää, miten nämä osat yhdessä vaikuttavat agentin päätöksiin ja käyttäytymiseen.

---
