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

<figure class="ai-demo"><span class="ai-demo__tag">// ennusta → valitse → liitä → toista — sana kerrallaan</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:290px">
  <div class="l03-wrap">
    <div class="l03-sent"><span class="l03-fixed">Suomen pääkaupunki</span><span class="l03-tok t1"> on</span><span class="l03-tok t2"> Helsinki</span><span class="l03-tok t3">.</span><i class="l03-caret"></i></div>
    <span class="l03-ph">malli laskee todennäköisyyden jokaiselle jatkolle:</span>
    <div class="l03-cands l03-r1"><div class="l03-c top"><span>on</span><div class="l03-cb"><i style="width:90%"></i></div><b>91 %</b></div><div class="l03-c"><span>sijaitsee</span><div class="l03-cb"><i style="width:6%"></i></div><b>4 %</b></div><div class="l03-c"><span>oli</span><div class="l03-cb"><i style="width:4%"></i></div><b>2 %</b></div></div>
    <div class="l03-cands l03-r2"><div class="l03-c top"><span>Helsinki</span><div class="l03-cb"><i style="width:93%"></i></div><b>94 %</b></div><div class="l03-c"><span>Tukholma</span><div class="l03-cb"><i style="width:4%"></i></div><b>2 %</b></div><div class="l03-c"><span>Turku</span><div class="l03-cb"><i style="width:3%"></i></div><b>1 %</b></div></div>
    <div class="l03-cands l03-r3"><div class="l03-c top"><span>.</span><div class="l03-cb"><i style="width:86%"></i></div><b>87 %</b></div><div class="l03-c"><span>,&nbsp;ja</span><div class="l03-cb"><i style="width:9%"></i></div><b>8 %</b></div><div class="l03-c"><span>!</span><div class="l03-cb"><i style="width:4%"></i></div><b>3 %</b></div></div>
    <span class="l03-loop">…valittu token liitetään tekstiin, ja laskenta alkaa alusta</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Malli ei hae valmista vastausta. Se laskee todennäköisyyden jokaiselle mahdolliselle seuraavalle tokenille, valitsee todennäköisimmän, liittää sen tekstiin — ja laskee sitten kaiken uudelleen. Vastaus syntyy pala kerrallaan.</figcaption></figure>
<style>
.l03-wrap{position:relative;width:560px;height:250px;font-family:var(--font-mono)}
.l03-sent{position:absolute;left:0;right:0;top:0;font-size:15px;font-weight:500;color:#FFFFFF;background:#0E1422;border:1.5px solid #44517A;border-radius:12px;padding:13px 15px;white-space:nowrap}
.l03-tok{color:#7FD0A8;opacity:0}
.l03-tok.t1{animation:l03t1 13s infinite}
.l03-tok.t2{animation:l03t2 13s infinite}
.l03-tok.t3{animation:l03t3 13s infinite}
@keyframes l03t1{0%,24%{opacity:0}27%,98%{opacity:1}100%{opacity:0}}
@keyframes l03t2{0%,56%{opacity:0}59%,98%{opacity:1}100%{opacity:0}}
@keyframes l03t3{0%,88%{opacity:0}91%,98%{opacity:1}100%{opacity:0}}
.l03-caret{display:inline-block;width:2px;height:16px;background:#46c7cf;margin-left:3px;vertical-align:-2px;animation:l03caret 1.1s steps(2) infinite}
@keyframes l03caret{to{visibility:hidden}}
.l03-ph{position:absolute;left:2px;top:62px;font-size:11px;letter-spacing:.04em;color:#8B94B3}
.l03-cands{position:absolute;left:0;top:84px;width:560px;display:flex;gap:12px;opacity:0}
.l03-r1{animation:l03r1 13s infinite}
.l03-r2{animation:l03r2 13s infinite}
.l03-r3{animation:l03r3 13s infinite}
@keyframes l03r1{0%,1%{opacity:0}4%,22%{opacity:1}26%,100%{opacity:0}}
@keyframes l03r2{0%,33%{opacity:0}36%,54%{opacity:1}58%,100%{opacity:0}}
@keyframes l03r3{0%,65%{opacity:0}68%,86%{opacity:1}90%,100%{opacity:0}}
.l03-c{flex:1;background:#141B2D;border:1.5px solid #2B3552;border-radius:11px;padding:9px 11px}
.l03-c span{display:block;font-size:13px;color:#EAEEF8;margin-bottom:6px}
.l03-c b{font-size:11px;color:#B9C2DA;font-weight:600}
.l03-c.top{border-color:#7FD0A8;background:#13251C}
.l03-c.top span{color:#FFFFFF}
.l03-c.top b{color:#7FD0A8}
.l03-cb{height:7px;border-radius:99px;background:#0B0F1A;border:1px solid #232C44;overflow:hidden;margin-bottom:5px}
.l03-cb i{display:block;height:100%;border-radius:99px;background:oklch(0.66 0.15 264)}
.l03-c.top .l03-cb i{background:#7FD0A8}
.l03-loop{position:absolute;left:0;right:0;top:196px;font-size:11px;line-height:1.4;color:#46c7cf;opacity:0;animation:l03loop 13s infinite}
@keyframes l03loop{0%,8%{opacity:0}12%,96%{opacity:.95}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l03-tok,.l03-cands,.l03-caret,.l03-loop{animation:none}
.l03-tok{opacity:1}
.l03-r3{opacity:1}
.l03-loop{opacity:1}}
</style>

## Koulutusdata — se, mistä malli oppii

Parametrit opitaan **koulutusdatasta**. Nykyiset kielimallit on koulutettu valtavilla tekstimäärillä, joita on kerätty esimerkiksi kirjoista, artikkeleista, verkkosivuilta, koodista ja internetin keskusteluista. Nykyiset suuret kielimallit opetetaan biljoonilla tokeneilla. Tässä yhteydessä biljoona tarkoittaa miljoonaa miljoonaa.

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
