# Kuvat, ääni ja teksti — multimodaalinen ongelmanratkaisu

## Johdanto

Olet varmasti nähnyt, miten IT-ammattilainen ottaa kuvakaappauksen virheilmoituksesta ja lähettää sen verkkofoorumille apua pyytäessään. Tai olet nähnyt koodarin sanovan: ”Tässä on kuvakaappaus, jossa ongelma näkyy.” Monille aloittelijoille kuvakaappaus on vain kuva, ja siksi he voivat pitää sitä vähemmän hyödyllisenä kuin tekstiä. Ammattilaiselle **kuvakaappaukset**, **lokit** ja **dokumentit** ovat kuitenkin kaikki tärkeitä kontekstin muotoja.

Tämän oppitunnin jälkeen ymmärrät, miksi näyttäminen on usein parempi kuin pelkkä kertominen. Opit rakentamaan **multimodaalista kontekstia** eli yhdistämään tekstiä, kuvia, lokeja ja koodia debuggauksen ja ongelmanratkaisun tueksi. Lisäksi näet, miten tekoäly voi hyödyntää muutakin kuin tekstiä ja miksi se tekee siitä tehokkaamman työkalun.

## Mitä multimodaalisuus on?

**Multimodaalisuus** tarkoittaa, että tekoälymallit voivat käsitellä erilaisia tietomuotoja, kuten tekstiä, kuvia, koodia, ääntä ja videota. Ensimmäiset laajasti käyttöön tulleet kielimallit, kuten GPT-3, käsittelivät vain tekstiä. Modernit mallit, kuten nykyiset ChatGPT-, Microsoft Copilot- ja Claude-mallit, voivat puolestaan tulkita myös kuvia. Jotkin mallit voivat lisäksi käsitellä ääntä ja analysoida videoita.

Tämä avaa täysin uuden tavan antaa tekoälylle kontekstia. Aiemmin tilanne saattoi olla tämä: ”Tietokannassa on virhe. Lokit ovat pitkät, enkä pysty hahmottamaan, missä virhe on, koska tekstiä on niin paljon.” Nyt voit toimia toisin: ”Otan kuvakaappauksen virheilmoituksesta ja lähetän sen tekoälylle.” Aiemmin saattoi tuntua mahdottomalta kuvata käyttöliittymän bugia pelkällä tekstillä. Nyt voit ottaa kuvakaappauksen ja näyttää tekoälylle tarkasti, mitä näkyy.

**Modaliteetti** tarkoittaa tietomuotoa. Teksti on yksi modaliteetti ja kuva toinen. Koodi on kolmas, vaikka se on teknisesti tekstiä, koska sillä on oma rakenteensa ja merkityksensä. Lokit ovat neljäs. Kun käytät kahta tai useampaa modaliteettia yhdessä, puhutaan **multimodaalisuudesta**. Käytännössä monet nykyiset chatpohjaiset kielimallit ovat multimodaalisia.

Multimodaaliset mallit ovat tehokkaita työkaluja, koska ne voivat nähdä kuvakaappauksista suoraan, mitä tarkoitat. Jos kirjoitat ”ohjelma on hidas”, tekoäly voi vain arvata, mitä yrität sanoa. Jos taas näytät kuvakaappauksen, jossa näkyy prosessin käyttävän 99 % suorittimesta, tekoäly saa ongelmasta paljon täsmällisemmän kuvan.

> **Pysähdy hetkeksi:** Ajattele projektia, jota työstät nyt. Mitä muita tietomuotoja kuin tekstiä käytät päivittäin? Käytätkö esimerkiksi kuvakaappauksia, lokitietoja, taulukoita tai kaavioita? Kuinka usein jätät ne pois, koska oletat, ettei tekoäly voi käsitellä niitä?

## Kuvakaappaukset — näytä, älä vain kuvaile

**Kuvakaappaus** eli screenshot on yksi tärkeimmistä kontekstityökaluista IT-ammattilaisen työssä. Se näyttää tekoälylle täsmälleen sen, mitä itse näet. Jos näet virheen, ota siitä kuvakaappaus. Jos käyttöliittymässä on ongelma, ota kuvakaappaus. Jos käyttöjärjestelmä käyttäytyy oudosti, kuvakaappaus voi kertoa tilanteesta enemmän kuin pitkä tekstikuvaus.

Kuvakaappaus on tehokas, koska se vähentää arvailua. Kun sanot ”Apache-palvelimen konfiguraatio on väärä”, tekoäly voi joutua arvaamaan useita erilaisia virheen syitä. Kun taas näytät kuvakaappauksen `httpd.conf`-tiedostosta, jossa `SSLEngine off` on sijoitettu väärään kohtaan, tekoäly voi nähdä ongelman tarkemmin ja ehdottaa täsmällisempää korjausta.

### Hyvän kuvakaappauksen tekeminen

Ammattilainen ottaa kuvakaappauksia harkitusti:

1. **Älä lähetä koko ruutua**, ellei se ole ongelman kannalta olennaista. Rajaa kuva tärkeimpään kohtaan.
2. **Osoita virheellinen kohta**. Monet kuvakaappaustyökalut mahdollistavat nuolten, kehysten tai korostusten lisäämisen.
3. **Lisää lyhyt selitys:** ”Tässä on virhe. Katso punaisella näkyvää virheilmoitusta.”
4. **Valitse sopiva rajaus:**
   - Koko ruudun kuvakaappaus voi olla hyödyllinen, mutta se voi sisältää häiritsevää tai arkaluonteista tietoa.
   - Pelkkä virheilmoitus on usein parempi, koska se on kohdennetumpi.
   - Virheilmoitus ja muutama rivi kontekstia on usein paras vaihtoehto, koska se näyttää sekä virheen että sen taustan.

Modernit tekoälyt voivat lukea kuvakaappauksia samaan tapaan kuin ihminen. Ne voivat tunnistaa tekstiä, värejä, kuvakkeita ja asettelua. Jos virheviesti näkyy punaisella, malli voi päätellä, että kyse on virheestä. Jos näytät lokin virheilmoituksia, malli voi lukea niistä olennaisia tietoja.

> **Pysähdy hetkeksi:** Mieti viimeisintä IT-ongelmaa, johon pyysit apua. Olisiko kuvakaappaus ollut parempi konteksti kuin pelkkä tekstikuvaus? Miten tekoäly olisi voinut auttaa paremmin, jos se olisi nähnyt tilanteen?

## Lokitiedostot — järjestelmän oma kertomus

**Lokit** eli logs ovat tietueita siitä, mitä järjestelmässä tapahtuu. Kun ohjelmassa on virhe, lokit kertovat usein, mikä meni pieleen ja milloin.

Opiskelijat sanovat usein: ”Minulla on virhe, mutta en tiedä, mikä se on.” Ammattilainen kysyy ensimmäiseksi: ”Mitä lokit kertovat?” Tämä johtuu siitä, että lokit ovat usein ihmisen luettavissa ja sisältävät tärkeää tietoa ongelman syystä.

`2024-03-14 10:23:45 ERROR: Failed to connect to database at localhost:5432
2024-03-14 10:23:45 ERROR: Connection timeout after 5 seconds
2024-03-14 10:23:46 WARNING: Retrying connection attempt 2 of 3`

Kun annat lokit tekoälylle, se voi lukea rivit ja päätellä esimerkiksi: ”Tietokanta ei ole saatavilla, koska portti 5432 ei vastaa.”

### Lokien tyypit

Lokit voivat tulla useista lähteistä:

- **Sovelluksen lokit:** kertovat, mitä koodi tekee, esimerkiksi funktiokutsut, tietojen käsittelyn ja hakujen tulokset.
- **Järjestelmän lokit:** kertovat, mitä käyttöjärjestelmässä tapahtuu, esimerkiksi muistin käytöstä, prosesseista ja laitteista.
- **Verkkolokit:** kertovat, mitä palvelimella tapahtuu, esimerkiksi HTTP-pyynnöistä, yhteyksistä ja kaistan käytöstä.
- **Virhelokit:** kertovat, mitä ohjelma ilmoittaa virhetilanteessa, esimerkiksi poikkeuksista, kaatumisista ja varoituksista.

### Lokien valitseminen kontekstiksi

Kun käytät tekoälyä, älä lähetä 5 000 riviä lokia sellaisenaan. Valitse olennaiset kohdat:

1. **Etsi virhe tai varoitus** lokista.
2. **Merkitse olennaiset rivit**, kuten viimeiset 20 riviä, grep-haun tulokset tai kuvakaappaus kriittisestä kohdasta.
3. **Lisää konteksti:** ”Ohjelma kaatui kello 10.45. Näetkö näistä lokeista mahdollisen syyn?”

Tekoäly voi tämän jälkeen etsiä virheilmoituksia, tarkastella tapahtumien ajoitusta ja ehdottaa ratkaisuja.

> **Pysähdy hetkeksi:** Missä sovelluksessa tai järjestelmässä olet nähnyt lokeja? Mitä sellaista lokeista voidaan oppia, mitä et näkisi muuten?

## Koodi ja konfiguraatiotiedostot — näytä rakenne

Usein ongelma löytyy itse koodista. Skripti ei ehkä toimi, konfiguraatiotiedosto voi olla virheellinen tai Python-funktio voi käyttäytyä odottamattomasti.

### Koodin antaminen kontekstiksi

Kun annat tekoälylle koodia, se voi analysoida sen rakennetta ja toimintaa:

```
def calculate_discount(price, discount_percent):    return price - (price * discount_percent)
```

Voit kysyä esimerkiksi: ”Näetkö tässä ongelmaa? Kun `discount_percent` on 0.1 eli 10 %, tulos on oikea. Mutta kun arvo on 1 eli 100 %, hinta muuttuu nollaksi. Pitäisikö funktioon lisätä tarkistus sallituille arvoille?”

Kun annat koodia, muista kolme asiaa:

1. **Konteksti:** Mikä ohjelma on kyseessä? Mitä ohjelmointikieltä käytetään?
2. **Vika-alue:** Mitkä rivit ovat todennäköisesti ongelmallisia? Näytä mieluummin muutama kymmenen riviä kuin satoja rivejä.
3. **Käyttäytyminen:** Mitä ohjelman pitäisi tehdä? Mitä se tekee todellisuudessa?

### Konfiguraatiotiedostot

Myös **konfiguraatiotiedostot** voivat aiheuttaa ongelmia:

```
{  "database": {    "host": "localhost",    "port": 5432,    "user": "admin",    "password": "admin123"  }}
```

Voit kysyä esimerkiksi: ”Tässä on konfiguraatiotiedosto. Näetkö siinä turvallisuusongelman?” Tässä tapauksessa salasana on kovakoodattu tiedostoon.

Tekoäly voi lukea sekä tekstiä että kuvakaappauksia koodista. Usein koodi kannattaa kuitenkin antaa tekstinä, koska silloin tekoäly voi analysoida ja muokata sitä helpommin.

## Turvallisuus — redaktointi ja yksityisyys

**Tärkeä huomio: älä koskaan näytä salasanoja, API-avaimia tai muita salaisuuksia tekoälylle.** Jos kuvakaappaus tai lokit sisältävät arkaluonteisia tietoja, poista tai peitä ne ennen jakamista.

### Salaisuuksien redaktointi

- **Salasanakenttä:** näytä `[REDACTED]` tai `***`.
- **API-avain:** näytä esimerkiksi `sk-***...xyz`, eli vain alun ja lopun merkit.
- **Tunnus eli token:** näytä esimerkiksi `jti_12345...abcdef`.
- **Luottokorttinumero:** näytä esimerkiksi `****-****-****-6789`.
- **Käyttäjätunnus:** näytä vain osa tunnuksesta, esimerkiksi `user_123...`.

Jos lokit sisältävät käyttäjä- tai asiakastietoja, poista ne tai anonymisoi ne kokonaan ennen jakamista.

### Miksi turvallisuus on pakollista?

Turvallisuus ei ole valinnainen asia, vaan osa ammattilaisen perustyötä. Se suojaa sekä sinua että muita:

- Se estää salaisuuksien, kuten salasanojen ja API-avainten, vuotamisen ulkopuolisiin palveluihin.
- Se suojaa muita käyttäjiä, joiden tietoja saattaa näkyä lokeissa.
- Se ylläpitää luottamusta organisaatiossa ja työyhteisössä.

> **Pysähdy hetkeksi:** Ajattele IT-järjestelmää, jossa käyttäjät voivat nähdä toistensa tietoja. Mitä turvallisuusriskejä syntyisi, jos jakaisit lokit tekoälylle muokkaamatta niitä?

## Yhdistäminen — multimodaalinen konteksti käytännössä

Ammattilaisen ongelmanratkaisu yhdistää usein useita tietomuotoja:

**Tekstin, kuvakaappausten, lokien ja koodin yhdistäminen:**

”Tässä on kuvakaappaus virheilmoituksesta. Tässä ovat lokin viimeiset 20 riviä. Tässä on myös koodin vika-alue eli rivit 45–55. Yritin päivittää käyttäjän profiilia, mutta validointi epäonnistuu. Kunkin kentän pitäisi hyväksyä vain tietynlaista dataa, mutta validointi epäonnistuu myös silloin, kun data on oikeassa muodossa.”

Nyt tekoälyllä on käytössään useita konteksteja:

- **Visuaalinen konteksti:** kuvakaappaus.
- **Ajoituksen ja ympäristön konteksti:** lokit.
- **Koodin konteksti:** vika-alue.
- **Käyttäytymisen konteksti:** mitä pitäisi tapahtua ja mitä tapahtuu todellisuudessa.

Tämä on huomattavasti parempi lähtökohta kuin pelkkä ilmoitus: ”Minulla on validointivirhe.”

### Päätösten tekeminen: milloin käyttää mitäkin?

Kuvakaappaukset ovat tehokkaita, mutta ne kuluttavat paljon tokeneita. Ammattilainen valitsee kontekstin strategisesti:

| Tilanne | Käytä kuvakaappausta? | Käytä tekstiä? | Käytä lokeja? |
| --- | --- | --- | --- |
| Käyttöliittymän bugi | ✅ Kyllä | Ei välttämättä, jos kuvakaappaus kertoo olennaisen | Ei yleensä |
| Virheilmoitus näytöllä | ✅ Kyllä | Kyllä, lyhyt selitys auttaa | Ehkä, jos ongelman syy ei näy ruudulla |
| Sovellus kaatuu | ❓ Kyllä, jos virhe näkyy ruudulla | ✅ Kyllä | ✅ Kyllä, usein kriittistä |
| Koodin virhe | Ei yleensä | ✅ Kyllä, koodi kannattaa antaa tekstinä | Ehkä, jos kyse on ajonaikaisesta virheestä |
| Verkko-ongelma | ❓ Ehkä | Kyllä, kuvaile mitä yritit tehdä | ✅ Kyllä, verkkolokit ovat usein hyödyllisiä |
| Hidas sovellus | Kyllä, jos suorituskykytiedot näkyvät ruudulla | Kyllä, kuvaile tilanne ja ajankohta | ✅ Kyllä, suorituskykylokit ovat hyödyllisiä |

## Multimodaalisten mallien rajoitukset

Multimodaaliset mallit ovat tehokkaita, mutta niillä on myös rajoituksia.

### 1. Kuvakaappaukset kuluttavat tokeneita

Yksittäinen kuva voi kuluttaa huomattavasti enemmän tokeneita kuin sama tieto tekstinä. Tämä täyttää konteksti-ikkunaa nopeammin. Siksi kuvakaappauksia kannattaa käyttää harkitusti: kriittisiin kohtiin, ei kaikkeen.

### 2. Tarkkuusrajoitukset

Tekoäly voi lukea kuvakaappauksia, mutta se voi myös tehdä virheitä:

- Pieniä fontteja voi olla vaikea tulkita.
- Sekavat taustat voivat tehdä tekstistä epäselvää.
- Monimutkainen käyttöliittymä voi hämmentää mallia.

Siksi kuvakaappaus yhdessä lyhyen tekstiselityksen kanssa on usein parempi kuin kuvakaappaus yksin.

### 3. Mallien kyvyt vaihtelevat

Kaikki tekoälymallit eivät ole multimodaalisia. Vanhat mallit, jotkin erikoistuneet mallit ja osa kevyemmistä malleista käsittelevät vain tekstiä. Siksi on tärkeää tietää, mitä mallia käytät.

Ammattilainen tuntee käyttämänsä mallin kyvyt ja valitsee työskentelytavan sen mukaan:

- Jos malli on multimodaalinen, voit hyödyntää kuvakaappauksia.
- Jos malli käsittelee vain tekstiä, kuvaile ongelma mahdollisimman tarkasti tekstinä.
- Vaihda mallia tarpeen mukaan: joskus pieni tekstimalli on nopeampi, joskus suuri multimodaalinen malli on parempi.

## Multimodaalisuus käytännössä

Käytännössä ammattilainen voi noudattaa seuraavaa työnkulkua:

1. **Ongelma syntyy** → ota kuvakaappaus, jos ongelma näkyy ruudulla.
2. **Lokit kertovat virheistä** → suodata olennainen osa ja näytä se tekstinä.
3. **Koodia täytyy tarkastella** → anna koodi tekstinä.
4. **Rakenne täytyy nähdä** → käytä kuvakaappausta, taulukkoa tai muuta selkeää esitystapaa.
5. **Ennen jakamista** → tarkista, että olet redaktoinut salaisuudet ja henkilötiedot.

### Käytännön työkalut

- **Kuvakaappaustyökalu:** Asenna hyvä kuvakaappaussovellus, kuten Snagit tai ShareX, tai käytä Windowsin sisäänrakennettua Snipping Tool -sovellusta. Rajaa kuva olennaiseen ja lisää tarvittaessa nuolia tai tekstiä.
- **Lokien suodatus:** Älä lähetä tuhansia rivejä lokia. Valitse olennaiset virheet, esimerkiksi viimeiset 20 riviä tai grep-haun tulokset.
- **Rakenteinen tieto:** Kielimallit hyötyvät rakenteisesta tiedosta, kuten CSV-datasta, JSON-tietueista ja taulukoista.
- **Koodinäyte:** Näytä vain olennainen osa koodista tekstinä, esimerkiksi muutama kymmenen riviä. Kuvakaappaus koodista on harvoin yhtä hyödyllinen kuin kopioitava tekstimuotoinen koodi.

## Yhteenveto

**Multimodaalisuus** auttaa IT-ammattilaista hallitsemaan kontekstia ja ratkaisemaan ongelmia tehokkaammin. Kun tekoäly voi käsitellä kuvia, lokeja ja koodia, se ymmärtää ongelman paremmin ja voi antaa täsmällisempiä ratkaisuja.

Ammattilaisena toimit näin:

- **Näytät ennen kuin kuvailet:** kuvakaappaukset vähentävät tulkinnanvaraisuutta.
- **Suodatat lokit:** näytät vain olennaiset rivit.
- **Annat koodia tekstinä:** silloin tekoäly voi analysoida ja muokata sitä helpommin.
- **Yhdistät kontekstin strategisesti:** teksti, kuva, lokit ja koodi muodostavat yhdessä vahvan kokonaisuuden.
- **Tarkistat turvallisuuden:** redaktoit salaisuudet ja henkilötiedot ennen jakamista.
- **Tunnet mallin kyvyt:** valitset oikean mallin oikeaan tehtävään.

Näin tekoälystä tulee aidosti hyödyllinen työkaveri IT-työssä ja ongelmanratkaisussa.

---
