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

<figure class="ai-demo"><span class="ai-demo__tag">// näytä, älä vain kerro — jokainen syöte tarkentaa diagnoosia</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:290px">
  <div class="l06-wrap">
    <span class="l06-q">”Sovellus ei toimi.”</span>
    <div class="l06-src l06-s1">▣ kuvakaappaus</div>
    <div class="l06-src l06-s2">≡ loki (20 riviä)</div>
    <div class="l06-src l06-s3">‹/› koodi</div>
    <i class="l06-fly l06-f1"></i><i class="l06-fly l06-f2"></i><i class="l06-fly l06-f3"></i>
    <div class="l06-model">MALLI<div class="l06-meterbox"><div class="l06-meter"></div></div><span class="l06-pct l06-p1">tarkkuus 35 %</span><span class="l06-pct l06-p2">tarkkuus 70 %</span><span class="l06-pct l06-p3">tarkkuus 95 %</span></div>
    <div class="l06-a l06-a1">Syitä voi olla monia — kokeile käynnistää uudelleen? <span class="l06-tag l06-t1">arvaus</span></div>
    <div class="l06-a l06-a2">Virheilmoitus viittaa tietokantaan — lokissa ”timeout 5432”. <span class="l06-tag l06-t2">tarkentuu</span></div>
    <div class="l06-a l06-a3">Tietokantaportti 5432 ei vastaa: korjaa yhteysasetus rivillä 12. <span class="l06-tag l06-t3">✓ täsmällinen</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Pelkkä ”ei toimi” pakottaa mallin arvaamaan. Kun lisäät kuvakaappauksen, lokit ja koodin, diagnoosi tarkentuu vaihe vaiheelta — jokainen modaliteetti tuo tietoa, jota muut eivät sisällä.</figcaption></figure>
<style>
.l06-wrap{position:relative;width:560px;height:250px}
.l06-q{position:absolute;left:0;top:6px;font-family:var(--font-mono);font-size:12.5px;color:#06212A;background:#46c7cf;font-weight:500;border-radius:10px;padding:7px 11px}
.l06-src{position:absolute;left:0;width:172px;font-family:var(--font-mono);font-size:12px;color:#EAEEF8;background:#1E2740;border:1.5px solid #44517A;border-radius:10px;padding:8px 11px}
.l06-s1{top:64px;animation:l06s1 12s infinite}
.l06-s2{top:112px;animation:l06s2 12s infinite}
.l06-s3{top:160px;animation:l06s3 12s infinite}
@keyframes l06s1{0%,7%,17%,100%{border-color:#44517A}9%,15%{border-color:oklch(0.72 0.15 264);box-shadow:0 0 12px oklch(0.66 0.15 264 / .5)}}
@keyframes l06s2{0%,33%,43%,100%{border-color:#44517A}35%,41%{border-color:oklch(0.72 0.15 264);box-shadow:0 0 12px oklch(0.66 0.15 264 / .5)}}
@keyframes l06s3{0%,59%,69%,100%{border-color:#44517A}61%,67%{border-color:oklch(0.72 0.15 264);box-shadow:0 0 12px oklch(0.66 0.15 264 / .5)}}
.l06-fly{position:absolute;left:176px;width:9px;height:9px;border-radius:50%;background:oklch(0.72 0.15 264);opacity:0}
.l06-f1{top:78px;animation:l06f1 12s infinite}
.l06-f2{top:126px;animation:l06f2 12s infinite}
.l06-f3{top:174px;animation:l06f3 12s infinite}
@keyframes l06f1{0%,8%{opacity:0;transform:translate(0,0)}10%{opacity:1}15%{opacity:1;transform:translate(64px,42px)}17%,100%{opacity:0;transform:translate(64px,42px)}}
@keyframes l06f2{0%,34%{opacity:0;transform:translate(0,0)}36%{opacity:1}41%{opacity:1;transform:translate(64px,-6px)}43%,100%{opacity:0;transform:translate(64px,-6px)}}
@keyframes l06f3{0%,60%{opacity:0;transform:translate(0,0)}62%{opacity:1}67%{opacity:1;transform:translate(64px,-54px)}69%,100%{opacity:0;transform:translate(64px,-54px)}}
.l06-model{position:absolute;left:248px;top:84px;width:132px;text-align:center;font-family:var(--font-mono);font-size:12px;letter-spacing:.14em;color:#EAEEF8;background:#11182A;border:2px solid oklch(0.66 0.15 264);border-radius:12px;padding:12px 10px 10px}
.l06-meterbox{margin:9px 6px 5px;height:8px;border-radius:99px;background:#0B0F1A;border:1px solid #232C44;overflow:hidden}
.l06-meter{height:100%;border-radius:99px;background:linear-gradient(90deg,oklch(0.66 0.15 264),#7FD0A8);animation:l06meter 12s infinite}
@keyframes l06meter{0%,14%{width:35%}18%,40%{width:35%}44%,66%{width:70%}70%,96%{width:95%}100%{width:35%}}
.l06-pct{position:absolute;left:0;right:0;bottom:-22px;font-size:10.5px;letter-spacing:.05em;color:#B9C2DA;opacity:0}
.l06-p1{animation:l06p1 12s infinite}.l06-p2{animation:l06p2 12s infinite}.l06-p3{animation:l06p3 12s infinite;color:#7FD0A8}
@keyframes l06p1{0%,2%{opacity:0}5%,40%{opacity:1}44%,100%{opacity:0}}
@keyframes l06p2{0%,42%{opacity:0}46%,66%{opacity:1}70%,100%{opacity:0}}
@keyframes l06p3{0%,68%{opacity:0}72%,96%{opacity:1}100%{opacity:0}}
.l06-a{position:absolute;left:400px;top:72px;width:160px;font-family:var(--font-mono);font-size:11.5px;line-height:1.45;color:#FFFFFF;background:#1E2740;border:1.5px solid #44517A;border-radius:11px;padding:9px 11px;opacity:0}
.l06-a1{animation:l06a1 12s infinite}
.l06-a2{animation:l06a2 12s infinite}
.l06-a3{animation:l06a3 12s infinite}
@keyframes l06a1{0%,3%{opacity:0}7%,38%{opacity:1}42%,100%{opacity:0}}
@keyframes l06a2{0%,42%{opacity:0}46%,64%{opacity:1}68%,100%{opacity:0}}
@keyframes l06a3{0%,68%{opacity:0}72%,96%{opacity:1}100%{opacity:0}}
.l06-a3{border-color:#7FD0A8}
.l06-tag{display:inline-block;margin-top:5px;font-size:10px;letter-spacing:.06em;text-transform:uppercase;border-radius:999px;padding:1px 7px}
.l06-t1{color:#3A1408;background:#F0A38C}
.l06-t2{color:#06212A;background:#46c7cf}
.l06-t3{color:#06241a;background:#7FD0A8}
@media (prefers-reduced-motion:reduce){
.l06-s1,.l06-s2,.l06-s3,.l06-f1,.l06-f2,.l06-f3,.l06-meter,.l06-p1,.l06-p2,.l06-a1,.l06-a2{animation:none}
.l06-f1,.l06-f2,.l06-f3,.l06-a1,.l06-a2,.l06-p1,.l06-p2{opacity:0;display:none}
.l06-a3,.l06-p3{animation:none;opacity:1}
.l06-meter{width:95%}}
</style>

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
