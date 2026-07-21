# Tekoäly vai tavallinen sääntö? — mistä eron tunnistaa

## Johdanto

Et tarvitse tältä tunnilta aiempaa kokemusta tekoälystä tai tietokoneista. Aloitamme tutusta tilanteesta.

Kuvittele pieni ruokakauppa, joka paistaa joka aamu sämpylöitä. Kauppiaan pitää päättää, kuinka monta sämpylää seuraavaksi päiväksi varataan. Jos niitä on liian vähän, hylly tyhjenee kesken päivän. Jos niitä on liikaa, osa jää myymättä.

Päätöksen voi tehdä usealla tavalla. Tietokoneelle voidaan kirjoittaa valmis sääntö, kuten: ”Jos huomenna on maanantai, varaa 100 sämpylää.” Päätöksen tueksi voidaan myös käyttää aiemmista myyntipäivistä koulutettua koneoppimismallia. Se voi arvioida tarvetta esimerkiksi viikonpäivän, sään ja aiemman menekin perusteella.

Tämän tunnin tärkein kysymys on yksinkertainen: **seuraako järjestelmä valmista sääntöä, käyttääkö se esimerkeistä koulutettua mallia vai yhdistääkö se molemmat?**

## Tietokone voi seurata valmista sääntöä

Tietokoneohjelma on joukko ohjeita, joiden mukaan tietokone toimii. Yksi tavallinen ohje on **jos–niin-sääntö**.

Kaupan sääntö voisi olla tällainen:

> Jos huomenna on maanantai, varaa 100 sämpylää. Muina päivinä varaa 140.

Kun päivä on tiedossa, ohjelma valitsee säännöstä oikean määrän. Se ei arvioi, onko huomenna juhlapäivä, sataako ulkona tai onko lähistöllä tapahtuma. Se tekee juuri sen, mitä sääntöön on kirjoitettu.

Valmis sääntö on usein hyvä ratkaisu, kun tilanne on selkeä ja toiminnan pitää olla ennustettavaa. Esimerkiksi kulkukortilla toimiva ovi voi käyttää sääntöä: jos kortin tunniste on sallittujen listalla, ovi aukeaa. Tällaiseen päätökseen ei tarvita koneoppimismallia.

## Automaattinen toiminta ei yksin tarkoita tekoälyä

**Automaatio** tarkoittaa, että tietokone hoitaa työvaiheen ilman, että ihmisen tarvitsee tehdä jokaista kohtaa käsin.

Kaupan ohjelma voi tarkistaa päivän, valita säännöstä tilausmäärän ja lähettää tilauksen automaattisesti. Toiminta voi olla nopeaa ja hyödyllistä, vaikka siinä ei olisi koneoppimista lainkaan.

Siksi lause ”ohjelma teki sen itse” ei vielä kerro, että kyse on tekoälystä. Ensin pitää kysyä, mihin toiminta perustuu. Se voi perustua valmiiseen sääntöön, koulutettuun malliin tai niiden yhdistelmään.

## Koneoppimismalli koulutetaan esimerkeillä

Kauppiaalla voi olla tallessa tietoa aiemmista myyntipäivistä. Jokaisesta päivästä voidaan tietää esimerkiksi viikonpäivä, sää, mahdollinen juhlapäivä ja myytyjen sämpylöiden määrä. Näitä aiempia tapauksia kutsutaan tässä **esimerkeiksi** tai **dataksi**.

Koneoppimismallin kouluttamisessa järjestelmä muodostaa näistä esimerkeistä yhteyksiä. Se voi huomata, että perjantaisin myynti on usein vilkkaampaa, sateella asiakkaita käy vähemmän tai toritapahtuma lisää kysyntää. Ihmisen ei tarvitse kirjoittaa jokaista mahdollista yhdistelmää erilliseksi säännöksi.

Kun koulutettu malli saa uuden tapauksen, se antaa siitä arvion. Jos huomenna on perjantai, sää on lämmin ja torilla järjestetään tapahtuma, malli voi arvioida, että kauppa tarvitsee tavallista enemmän sämpylöitä.

Arvio ei ole varma tieto tulevaisuudesta. Huominen voi poiketa aiemmista päivistä. Siksi mallin ehdotusta pitää verrata tilanteeseen ja päätöksen seurauksiin.

<figure class="ai-demo"><span class="ai-demo__tag" id="l01a-t"><i aria-hidden="true">// </i>kolme tapaa ohjata toimintaa</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:250px">
  <div class="l01a-wrap" data-once role="img" aria-labelledby="l01a-t" aria-describedby="l01a-d">
    <span class="sr-only" id="l01a-d">Valmis sääntö määrää toiminnan etukäteen. Koulutettu malli antaa aiempien esimerkkien perusteella arvion. Yhdistelmä käyttää mallin arviota ja tarkistaa sen säännöllä.</span>
    <div class="l01a-c c1"><strong style="display:block;margin-bottom:12px;color:#7FD0A8">VALMIS SÄÄNTÖ</strong><span>Maanantai →<br>100 sämpylää</span></div>
    <div class="l01a-c c2"><strong style="display:block;margin-bottom:12px;color:#C9B7F1">KOULUTETTU MALLI</strong><span>Aiemmat päivät →<br>menekkiarvio</span></div>
    <div class="l01a-c c3"><strong style="display:block;margin-bottom:12px;color:#7FD0A8">YHDISTELMÄ</strong><span>Mallin arvio →<br>sääntö tarkistaa</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Valmis sääntö määrää toiminnan etukäteen. Koulutettu malli antaa arvion aiempien esimerkkien perusteella. Samassa järjestelmässä voidaan käyttää molempia.</figcaption></figure>
<style>
.l01a-wrap{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;width:680px;animation:l01aw 11s 1 forwards}
@keyframes l01aw{0%,100%{opacity:1}}
.l01a-c{padding:22px;border:1px solid #34415F;border-radius:14px;background:#172038;color:#EAEEF8;opacity:0;transform:translateY(10px)}
.l01a-c.c1{animation:l01a1 11s 1 forwards}
.l01a-c.c2{animation:l01a2 11s 1 forwards}
.l01a-c.c3{border-color:#2F9E69;animation:l01a3 11s 1 forwards}
@keyframes l01a1{0%,4%{opacity:0;transform:translateY(10px)}16%,100%{opacity:1;transform:none}}
@keyframes l01a2{0%,26%{opacity:0;transform:translateY(10px)}38%,100%{opacity:1;transform:none}}
@keyframes l01a3{0%,48%{opacity:0;transform:translateY(10px)}
  60%{opacity:1;transform:none;box-shadow:0 0 0 0 rgba(47,158,105,0)}
  72%{opacity:1;transform:none;box-shadow:0 0 0 6px rgba(47,158,105,.22)}
  84%,100%{opacity:1;transform:none;box-shadow:0 0 0 0 rgba(47,158,105,0)}}
@media (max-width:680px){.l01a-wrap{width:100%;grid-template-columns:1fr}}
</style>

## Kouluttaminen ja käyttäminen ovat eri vaiheita

Mallin **kouluttaminen** tarkoittaa, että se muodostetaan aiempien esimerkkien avulla. Mallin **käyttäminen** tarkoittaa, että valmista mallia sovelletaan uuteen tapaukseen.

Kaupan malli ei tavallisesti muutu jokaisesta uudesta menekkiennusteesta. Jos kauppias haluaa hyödyntää uusia myyntipäiviä, järjestelmän toteuttajan pitää kerätä uusi data ja päivittää malli erillisessä prosessissa.

Tämä ero on tärkeä. Koulutettu malli voi antaa uusia arvioita, vaikka se ei samalla opi jokaisesta käyttökerrasta.

## Oikea järjestelmä voi yhdistää sääntöjä ja mallin

Kaupan tilaustoiminto voi käyttää koneoppimismallia menekin arvioimiseen ja valmiita sääntöjä toiminnan rajaamiseen.

Malli voi esimerkiksi ehdottaa 220 sämpylän tilausta. Kaupan sääntö voi kuitenkin sanoa, että yli 200 sämpylän tilaus pitää näyttää ihmiselle ennen lähettämistä. Järjestelmässä on silloin kolme osaa:

1. koulutettu malli antaa menekkiarvion
2. valmis sääntö tarkistaa tilauksen koon
3. ihminen hyväksyy tavallista suuremman tilauksen.

Tällainen yhdistelmä on tavallinen. Malli auttaa tilanteessa, jossa huomioon otettavia asioita on paljon. Sääntö pitää toiminnan sovituissa rajoissa.

## Mistä toteutustavan voi päätellä?

Pelkkä järjestelmän nimi tai ulkonäkö ei kerro, miten se toimii. Sama tehtävä voidaan toteuttaa eri tavoin.

Kun arvioit järjestelmää, kysy:

- Onko toiminta kirjoitettu valmiiksi jos–niin-sääntöinä?
- Onko järjestelmässä malli, joka on koulutettu aiemmilla esimerkeillä?
- Käyttääkö järjestelmä molempia?
- Kertooko kuvaus toteutustavasta riittävästi, vai tarvitaanko lisää tietoa?

Jos kuvaus sanoo vain, että ohjelma ”valitsee sopivan määrän”, toteutustapaa ei vielä tiedetä. Jos kuvaus kertoo, että määrä valitaan aina samasta taulukosta, kyse on valmiista säännöstä. Jos kuvaus kertoo, että malli on koulutettu aiempien päivien tiedoilla, mukana on koneoppimista.

## Milloin sääntö ja milloin malli?

Valmis sääntö sopii tilanteeseen, jossa ehdot ovat selvät, muuttuvat vähän ja tuloksen pitää olla ennustettava. Kulkukorttioven avaaminen tai kellonaikaan perustuva muistutus ovat hyviä esimerkkejä.

Koneoppimismallista voi olla hyötyä, kun aiempia esimerkkejä on paljon, tilanteeseen vaikuttaa monta asiaa eikä kaikkea voi kuvata yhdellä selkeällä säännöllä. Menekin arviointi on tällainen tehtävä.

Malli ei silti ole automaattisesti sääntöä parempi. Jos tehtävä ratkeaa yhdellä varmalla ehdolla, koulutettu malli voi tehdä ratkaisusta turhaan monimutkaisen. Jos mallin arvio johtaa kalliiseen, vaaralliseen tai vaikeasti peruttavaan toimintaan, ihmisen tarkistus voi olla tarpeen.

## Yhteenveto

Tietokone voi seurata valmista sääntöä. Kun sääntö suoritetaan automaattisesti, kyse on automaatiosta, mutta automaattisuus ei yksin tarkoita tekoälyä.

Koneoppimismalli muodostetaan aiemmista esimerkeistä. Kun mallia käytetään, se antaa uudesta tapauksesta arvion. Käyttö ei tavallisesti kouluta mallia uudelleen.

Oikea järjestelmä voi yhdistää mallin, valmiit säännöt ja ihmisen tarkistuksen. Siksi järjestelmän toimintaa arvioidaan sen toteutustavan, ei pelkän nimen tai älykkään vaikutelman perusteella.

---

## Lähteet ja tarkistuspäivä

- [OECD: Updated definition of an AI system](https://oecd.ai/en/wonk/definition)
- [Google for Developers: Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)

Tarkistettu 21.7.2026.
