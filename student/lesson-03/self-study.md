# Miten kone kirjoittaa? — generatiivisen tekoälyn mekaniikka

## Johdanto

Kun käytät ChatGPT:tä, Copilotia tai muuta kielimalliin perustuvaa tekoälyä, vastaus voi näyttää hyvin älykkäältä. Mutta mitä taustalla oikeasti tapahtuu? Taustalla ei ole ajattelua tai ymmärtämistä ihmisen tavoin, vaan matemaattista ennustamista.

Kielimalli on opetettu valtavalla määrällä tekstiä. Se ei ajattele kuten ihminen, vaan ennustaa, mikä sana, sanan osa tai ilmaus sopii seuraavaksi parhaiten. Kun ymmärrät tämän, ymmärrät paremmin sekä mallin vahvuudet että sen rajat.

Tämän tunnin jälkeen ymmärrät, että vaikka tekoäly näyttää älykkäältä, sen perusta on mekaaninen. Se ei ajattele ihmisen tavoin, vaan ennustaa.

## Tokenit — sanat jaetaan pieniksi palasiksi

Kun ChatGPT tai muu kielimalli lukee tekstiä, se ei käsittele sitä varsinaisesti kokonaisina sanoina, vaan **tokeneina** eli pieninä tekstin palasina.

Joskus yksi sana vastaa yhtä tokenia. Näin voi olla esimerkiksi sanoissa ”tekoäly” tai ”koulu”. Pidemmät tai harvinaisemmat sanat voivat kuitenkin jakautua useaan tokeniin. Esimerkiksi sana ”kielentutkimusopiskelijat” voi pilkkoutua useiksi osiksi. Tämä riippuu siitä, miten mallin käyttämä **tokenisaattori** on suunniteltu ja opetettu.

Miksi näin tehdään? Mallia opetettaessa se oppii, mitkä kirjain-, sana- ja sananosayhdistelmät ovat hyödyllisiä. Yleiset sanat tai sananosat voivat muodostaa yhden tokenin. Harvinaisemmat sanat jaetaan pienempiin osiin, jotta malli pystyy käsittelemään myös sanoja, joita se ei ole nähnyt usein.

> **Pysähdy hetkeksi:** Miksi pienempi tokenisarja voisi olla kielimallille parempi kuin pitkien sanojen käsittely kokonaisina?

ChatGPT:n kaltaiselle mallille ”tekoäly” voi olla noin 1–2 tokenia. Sana ”kielentutkimusopiskelijat” voi puolestaan olla useita tokeneita. Malli siis ”näkee” tekstin tokeneina, ei samalla tavalla kuin ihminen näkee sanat ja lauseet.

## Parametrit — miljardeja opittuja numeroita

Kielimallissa on **parametreja** eli numeroarvoja, jotka se on oppinut koulutuksen aikana. Esimerkiksi GPT-3-mallissa oli noin 175 miljardia parametria. Uudemmissa suurissa kielimalleissa parametrimäärät ja tarkat rakenteet voivat olla erilaisia, eikä niitä aina julkaista avoimesti.

Parametrien lukumäärä on niin valtava, että sitä on vaikea hahmottaa. Onneksi perusidea on yksinkertainen: parametrit ovat matemaattisia painoja, jotka ohjaavat mallin toimintaa. Ne vaikuttavat siihen, millaisia yhteyksiä malli tunnistaa tekstissä ja millaisia vastauksia se todennäköisimmin tuottaa.

Voit ajatella parametreja mallin eräänlaisina ”säätiminä”. Ne eivät ole ihmisaivojen kaltaisia ajatuksia tai muistoja, vaan numeroita, joiden avulla malli käsittelee tekstiä. Koulutuksen aikana malli säätää näitä numeroita vähitellen, jotta sen ennusteet paranevat.

Käytännössä malli käy läpi valtavan määrän tekstiesimerkkejä ja yrittää ennustaa, mikä tokeni tulee seuraavaksi. Kun ennuste menee väärin, mallin parametreja säädetään hieman. Kun tätä toistetaan valtavan monta kertaa, malli oppii yhä paremmin, millaiset tokenit sopivat toistensa yhteyteen.

## Seuraavan tokenin ennustaminen — sana kerrallaan

Kielimallin perusmekanismia kutsutaan usein englanniksi nimellä **next-token prediction**. Suomeksi se tarkoittaa **seuraavan tokenin ennustamista**.

Kun annat ChatGPT:lle kysymyksen ”Mikä on Suomen pääkaupunki?”, malli näkee tekstin tokeneina. Yksinkertaistettuna se voi käsitellä sen esimerkiksi näin:

- tokeni: ”Mikä”
- tokeni: ”on”
- tokeni: ”Suomen”
- tokeni: ”pääkaupunki”

Tämän jälkeen malli arvioi parametrien ja koulutusdatan perusteella, mikä tokeni sopii seuraavaksi. Tässä tapauksessa todennäköinen jatko on ”Helsinki”. Malli valitsee sen ja lisää sen vastaukseen.

Sitten malli jatkaa samalla tavalla. Se katsoo aiempaa tekstiä, johon kuuluu nyt myös sen oma tuottama sana, ja ennustaa taas seuraavan tokenin. Tätä jatkuu, kunnes vastaus on valmis tai kunnes pituusraja tulee vastaan.

Tässä on avainasia: malli ei kirjoita vastausta samalla tavalla kuin ihminen suunnittelee esseen tai perustelun. Se valitsee seuraavaa tokenia yksi kerrallaan parametrien ja koulutuksessa näkemänsä datan perusteella. Se näyttää älykkäältä, koska koulutusdata sisälsi valtavasti ihmisten kirjoittamaa älykästä tekstiä. Mutta malli ei ajattele ihmisen tavoin. Se ennustaa.

> **Pysähdy hetkeksi:** Jos malli vain ennustaa seuraavaa tokenia todennäköisyyksien perusteella, miten se voi silti antaa oikeita vastauksia monimutkaisiin kysymyksiin?

<figure class="ai-demo"><span class="ai-demo__tag">// ennusta seuraava token</span>
<div class="ai-demo__stage" style="display:flex;flex-direction:column;justify-content:center;gap:12px;padding:16px 24px">
  <div class="l03tok-prompt">Suomen pääkaupunki on <span class="l03tok-blank">Helsinki</span></div>
  <div class="l03tok-bars">
    <div class="l03tok-bar l03tok-top"><span class="l03tok-w">Helsinki</span><span class="l03tok-tr"><span class="l03tok-fill" style="--p:81%"></span></span><span class="l03tok-p">0.81</span></div>
    <div class="l03tok-bar"><span class="l03tok-w">Turku</span><span class="l03tok-tr"><span class="l03tok-fill" style="--p:7%"></span></span><span class="l03tok-p">0.07</span></div>
    <div class="l03tok-bar"><span class="l03tok-w">Tampere</span><span class="l03tok-tr"><span class="l03tok-fill" style="--p:5%"></span></span><span class="l03tok-p">0.05</span></div>
    <div class="l03tok-bar"><span class="l03tok-w">Espoo</span><span class="l03tok-tr"><span class="l03tok-fill" style="--p:4%"></span></span><span class="l03tok-p">0.04</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Malli ei "tiedä" vastausta. Se laskee jokaiselle mahdolliselle seuraavalle tokenille todennäköisyyden ja valitsee todennäköisimmän — tässä "Helsinki" (0.81). Sitten se toistaa saman seuraavalle sanalle.</figcaption></figure>
<style>
.l03tok-prompt{font-family:var(--font-mono);font-size:13.5px;color:#C7CEE6}
.l03tok-blank{color:oklch(0.66 0.15 264);border-bottom:2px solid oklch(0.66 0.15 264);padding:0 3px;opacity:0;animation:l03reveal 4.5s ease-in-out infinite}
@keyframes l03reveal{0%,45%{opacity:0}55%,92%{opacity:1}100%{opacity:0}}
.l03tok-bars{display:flex;flex-direction:column;gap:6px}
.l03tok-bar{display:flex;align-items:center;gap:10px;font-family:var(--font-mono);font-size:11px;color:#8B94B3}
.l03tok-w{width:74px;text-align:right;color:#C7CEE6}
.l03tok-tr{flex:1;height:13px;background:#11182A;border:1px solid #232C44;border-radius:4px;overflow:hidden}
.l03tok-fill{display:block;height:100%;width:0;background:#3A445F;animation:l03grow 4.5s ease-in-out infinite}
.l03tok-top .l03tok-fill{background:linear-gradient(90deg,oklch(0.66 0.15 264),oklch(0.66 0.15 305))}
.l03tok-top .l03tok-w{color:#E6EAF5}
@keyframes l03grow{0%{width:0}35%{width:var(--p)}92%{width:var(--p)}100%{width:0}}
.l03tok-p{width:30px}
@media (prefers-reduced-motion:reduce){.l03tok-blank{opacity:1}.l03tok-fill{animation:none;width:var(--p)}}
</style>

## Koulutusdata — se, mistä malli oppii

Parametrit opitaan **koulutusdatasta**. Nykyiset kielimallit on koulutettu valtavilla tekstimäärillä, joita on kerätty esimerkiksi kirjoista, artikkeleista, verkkosivuilta, koodista ja internetin keskusteluista. Varhaisetkin suuret kielimallit opetettiin jo biljoonilla tokeneilla. Tässä yhteydessä biljoona tarkoittaa miljoonaa miljoonaa.

Mitä malli oppii tästä aineistosta? Se oppii tilastollisia yhteyksiä ja toistuvia kuvioita. Se voi esimerkiksi oppia, että sanat ”koodaus” ja ”Python” esiintyvät usein yhdessä, että merkkijonon ”2 + 2” jälkeen tulee usein ”= 4” tai että kysymyksen jälkeen seuraa yleensä vastaus.

Tärkeää on kuitenkin ymmärtää, ettei malli ymmärrä asioita samalla tavalla kuin ihminen. Se ei tiedä, miksi 2 + 2 = 4 on totta. Se on oppinut, että tämä yhdistelmä esiintyy aineistossa hyvin usein ja on siksi todennäköinen.

Tästä seuraa myös rajoituksia. Jos koulutusdata sisältää virheitä tai vinoumia, malli voi oppia niitäkin. Jos taas jokin aihe puuttuu datasta kokonaan tai esiintyy siinä vain vähän, malli ei pysty hallitsemaan sitä hyvin.

## Hallusinaatio — kun malli tuottaa väärän mutta uskottavan vastauksen

**Hallusinaatiolla** tarkoitetaan tilannetta, jossa kielimalli tuottaa vastauksen, joka vaikuttaa uskottavalta mutta on todellisuudessa väärä.

Esimerkiksi mallilta voidaan kysyä: ”Kuka kirjoitti romaanin Suuri Mahtava?” Malli saattaa vastata: ”Jane Austen kirjoitti teoksen Suuri Mahtava vuonna 1847.” Vastaus kuulostaa uskottavalta, mutta se on virheellinen. Jane Austen ei ole kirjoittanut tämännimistä teosta. Vastaus näyttää oikealta siksi, että malli on oppinut, että kirjailijan nimi, teoksen nimi ja vuosiluku esiintyvät usein samankaltaisissa yhteyksissä.

Tätä kutsutaan hallusinaatioksi. Malli ei valehtele tietoisesti, koska se ei ymmärrä totuutta tai valhetta ihmisen tavoin. Se ennustaa, mikä ilmaus vaikuttaa todennäköiseltä seuraavaksi. Joskus tämä ennuste osuu väärin, vaikka lopputulos kuulostaisi hyvin vakuuttavalta.

> **Pysähdy hetkeksi:** Miksi hallusinaatio voi olla erityisen vaarallinen silloin, kun vastaus on kirjoitettu itsevarmalla ja asiantuntevalla tyylillä?

## Lämpötila — kontrolli satunnaisuudelle

Kielimalli ei aina valitse kaikkein *todennäköisintä* seuraavaa tokenia. Joskus se voi valita myös hieman epätodennäköisemmän vaihtoehdon, jotta vastaus olisi monipuolisempi tai luovempi.

Tähän vaikuttaa asetus, jota kutsutaan **lämpötilaksi**.

- **Matala lämpötila:** malli valitsee yleensä kaikkein todennäköisimmän jatkon. Vastaukset ovat usein tasaisempia, ennustettavampia ja johdonmukaisempia.
- **Korkea lämpötila:** malli sallii enemmän vaihtelua ja voi valita myös epätodennäköisempiä jatkoja. Vastaukset voivat olla luovempia, mutta myös satunnaisempia ja virhealttiimpia.

Käyttäjä ei tavallisesti säädä lämpötilaa itse tavallisessa chat-käyttöliittymässä, mutta asetus vaikuttaa silti mallin toimintaan. Siksi samaan kysymykseen voi joskus saada hieman erilaisen vastauksen eri kerroilla.

## Kuva-, musiikki- ja videomallit

Kielimallien taustalla oleva ajatus eli seuraavan yksikön ennustaminen ei rajoitu vain tekstiin. Samaa perusajatusta voidaan soveltaa myös kuviin, musiikkiin ja videoihin.

- **Kuvamallit** ennustavat, millaisia visuaalisia piirteitä kuvaan kannattaa muodostaa seuraavaksi.
- **Musiikkimallit** ennustavat, millainen ääni, sävel tai rytminen elementti sopii jatkoksi.
- **Videomallit** ennustavat, millaisia kuvia, liikettä ja joskus myös ääntä seuraavaksi pitäisi syntyä.

Periaate pysyy samankaltaisena, vaikka sisältö muuttuu. Malli tuottaa lopputulosta vaiheittain aiemmin muodostuneen sisällön perusteella. Erona on vain se, käsitelläänkö tekstin sijaan kuvaa, ääntä vai liikkuvaa kuvaa.

## Yhteenveto

Generatiivinen tekoäly ei ajattele tai ymmärrä ihmisen tavoin. Se toimii yksinkertaistettuna näin:

- Se pilkkoo tekstin tokeneiksi.
- Se käyttää koulutuksessa opittuja parametreja.
- Se ennustaa seuraavan tokenin todennäköisyyksien perusteella.
- Se jatkaa tätä, kunnes vastaus on valmis.

Siksi lopputulos voi näyttää älykkäältä, vaikka taustalla on ennen kaikkea matemaattinen ennustaminen. Mallin vahvuus tulee siitä, että se on oppinut valtavasta määrästä ihmisten tuottamaa aineistoa. Ammattilaiselle tämän ymmärtäminen on tärkeää, koska juuri silloin hahmottaa sekä tekoälyn hyödyt että sen rajoitukset.

Seuraavalla tunnilla opit ymmärtämään, että vastaus riippuu suuresti siitä, mitä ja miten kysyt: **konteksti ratkaisee kaiken**.

---
