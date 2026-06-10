# Agentin työkalut — tiedostot, haku ja komennot

## Johdanto

Agentti näkee ja muistaa. Mutta miksi se on tehokkaampi kuin yksinkertainen chatbot? Siksi, että agentti voi tehdä todellisia asioita. Se ei vain vastaa — se toimii.

Chatbot voi vastata kysymykseen ”Mikä on tuotteemme hinta?” ja sanoa: ”Se on 50 euroa.” Agentti voi tehdä enemmän. Se hakee tuotteen nykyisen hinnan tietokannasta, tarkistaa varastotason API:sta, vertaa hintaa kilpailijoihin ja vastaa: ”Tuotteemme hinta on 50 euroa, ja meillä on 15 kappaletta varastossa. Kilpailijoiden hinta on 55 euroa, joten olemme heitä edullisempia.” Agentti käytti **työkaluja**, kuten tietokantahakua, API-kutsuja ja laskentaa, jotta vastaus olisi tarkempi ja hyödyllisempi.

Tässä oppitunnissa opit kolme perustyökalua, joita agentti voi käyttää. Ne muodostavat perustan, jonka päälle monet muut työkalut rakentuvat. Kun rakennat agenttia n8n:llä, nämä kolme ovat usein ensimmäisiä integraatioita, joita alat suunnitella.

## Työkalu 1: Tiedostot — lukeminen ja kirjoittaminen

Agentti voi lukea ja kirjoittaa tiedostoja. Tämä on yksinkertainen mutta tehokas työkalu, koska se antaa agentille pääsyn pysyvään dataan.

Kun agentti **lukee tiedostoja**, se näkee maailmaa datan kautta. Se voi lukea esimerkiksi raportteja PDF-muodossa, tietolistoja CSV-muodossa, konfiguraatiotiedostoja JSON-muodossa tai lokeja tekstitiedostoina. Nämä tiedostot antavat agentille tietoa siitä, mitä järjestelmissä tapahtuu. Tapahtumanjärjestäjän agentti voi lukea ilmoittautumislistan ja huomata, että iltapäivän työpaja on jo täynnä. Seuraavalla kerralla, kun osallistuja kysyy ”Onko työpajassa vielä tilaa?”, agentti osaa vastata tarkemmin.

Kun agentti **kirjoittaa tiedostoja**, se vaikuttaa maailmaan. Se voi kirjoittaa raportteja, omia toimintalokejaan tai tiedostoja, joita muut ohjelmat lukevat. Myyntiagentti voi kirjoittaa CSV-tiedoston, joka sisältää listan uusista asiakkaista ja jonka Excel voi avata. Tekninen agentti voi kirjoittaa uuden konfiguraatiotiedoston, jonka palvelin lukee ja ottaa käyttöön automaattisesti.

Tiedostojen käsittely tuo kuitenkin mukanaan **kriittisen turvallisuuskysymyksen**: mitä oikeuksia agentti saa? Voiko se lukea, kirjoittaa ja poistaa tiedostoja missä tahansa, vai rajoitetaanko sen pääsy vain tiettyihin kansioihin?

Jos agentti saa liikaa oikeuksia, se voi vahingossa poistaa tärkeitä tiedostoja ja aiheuttaa todellista vahinkoa. Kuvittele agentti, joka tekee virheellisen päätöksen ja ajaa Linux-komennon `rm -rf /`, joka voi poistaa koko järjestelmän. Jos agentti saa liian vähän oikeuksia, se ei taas pysty tekemään sille annettua tehtävää. Tasapainon löytäminen on ammattilaisen työtä.

Käytännössä tämä tarkoittaa, että agentille annetaan **kirjoitusoikeus vain tiettyyn kansioon**, esimerkiksi `/reports/`, kun se kirjoittaa raportteja. Se voi saada **lukuoikeuden asiakastiedostoihin**, mutta ei kirjoitusoikeutta, jotta se ei voi vahingossa muuttaa asiakastietoja. Sillä ei pitäisi olla oikeuksia **palkkajärjestelmän tiedostoihin**, jos sen tehtävä ei liity palkkahallintoon.

> **Pysähdy hetkeksi:** Jos agentti voi kirjoittaa tiedostoihin, mitkä tiedostot olisivat liian arkaluontoisia sen käsiteltäviksi? Mitkä tiedostot voisivat aiheuttaa vahinkoa, jos agentti muuttaisi niitä virheellisesti?

## Työkalu 2: Verkkohaku — pääsy internetin dataan

Agentti voi hakea tietoa internetistä. Tämä antaa sille pääsyn ajankohtaiseen tietoon, joka on voinut muuttua sen koulutusdatan jälkeen.

Ilman verkkohakua agentilla on käytössään vain ne tiedot, jotka olivat mukana sen koulutuksessa. Jos koulutusdata on vuodelta 2023 ja nyt on vuosi 2026, agentin tieto voi olla vanhentunutta. Osakkeiden hinnat muuttuvat jatkuvasti. Jos agentti ei hae niitä verkosta, se voi antaa vanhan hinnan. Sama koskee uutisia. Jos asiakas kysyy ”Mitä tapahtui tänään?”, agentti ei voi vastata luotettavasti ilman ajantasaista tiedonhakua.

**Verkkohaku** tekee agentista ajankohtaisemman ja relevantimman. Kun asiakas kysyy osakkeen hinnasta, agentti hakee sen verkosta ja antaa tämänhetkisen tiedon. Kun asiakas haluaa tietää päivän uutiset, agentti etsii ne. Kun asiakas kysyy Windows-päivityksistä, agentti voi löytää uusimmat ohjeet eikä vain vanhaa tietoa, joka oli mukana koulutusdatassa.

Verkkohaku tuo kuitenkin mukanaan **kolme merkittävää riskiä**.

Ensimmäinen riski on **väärä tieto**. Haku voi löytää valheellisia tai harhaanjohtavia sivustoja. Jos agentti etsii tietoa esimerkiksi migreenilääkkeistä ja löytää epäluotettavan sivuston, se voi jakaa vaarallisia neuvoja. Ammattilaisena sinun täytyy **rajata lähteet**. Agentin kannattaa hakea tietoa vain virallisista ja tarkistetuista lähteistä, esimerkiksi terveysviranomaisen sivuilta, ei satunnaisista blogeista.

Toinen riski on **kustannukset**. Jotkut hakupalvelut laskuttavat jokaisesta hausta. Jos agenttia ei rajoiteta, se voi aiheuttaa vahingossa kalliita kyselykustannuksia. Kuvittele agentti, joka tekee 100 hakua tunnissa ja jokainen haku maksaa 10 senttiä. Kahden päivän kuluttua lasku voi olla jo huomattavan suuri.

Kolmas riski on **yksityisyys ja turvallisuus**. Agentti voi yrittää hakea liian arkaluontoisia tietoja ilman rajoituksia. Asiakas voi esimerkiksi yrittää saada agentin etsimään henkilötunnuksia, salasanoja tai muuta yksityistä tietoa verkosta. Tämä olisi vakava turvallisuusriski.

Ammattilaisena sinun täytyy asettaa **selkeät rajat hakutyökalulle**. Voit määritellä, miltä sivustoilta agentti saa hakea tietoa. Tätä kutsutaan **whitelist-malliksi**. Lisäksi voit kieltää agenttia hakemasta henkilökohtaisia tai yksityisiä tietoja ja rajoittaa, kuinka monta hakua se saa tehdä yhtä käyttäjän pyyntöä kohden. Nämä rajaukset suojaavat sekä agentin virheiltä että mahdollisilta väärinkäyttöyrityksiltä.

> **Pysähdy hetkeksi:** Kuvittele agentti, jota käytetään asiakaspalvelun tukena. Mitä tietoa sen ei pitäisi hakea verkosta turvallisuussyistä? Entä jos asiakas yrittää saada agentin hakemaan hänen salasanansa?

## Työkalu 3: CLI-komennot — toimiminen palvelimella

**CLI** eli Command Line Interface tarkoittaa komentoriviä. CLI-komentojen avulla agentti voi ajaa palvelinkomentoja. Tämä on yksi voimakkaimmista työkaluista, mutta samalla myös yksi vaarallisimmista.

CLI antaa agentille kyvyn **luoda ja poistaa kansioita, käynnistää ohjelmia ja muokata asetuksia**. Se voi suorittaa komennon `mkdir /backup` luodakseen varmuuskopiokansion. Se voi ajaa komennon `python analyze_sales.py`, joka analysoi myyntidataa minuutissa, vaikka ihmiseltä sama työ voisi viedä tunteja. Se voi ajaa komennon `systemctl restart apache2` käynnistääkseen verkkopalvelimen uudelleen, jos se on kaatunut. CLI on tehokas työkalu, koska sen avulla agentti voi tehdä palvelimella todellisia ja syvälle järjestelmään vaikuttavia asioita.

CLI on kuitenkin myös vaarallinen. Jos agentti voi ajaa mitä tahansa komentoja ilman rajoituksia, se voi vahingossa poistaa kaikki tiedostot komennolla `rm -rf /`. Se voi sammuttaa palvelimen tai muuttaa asetuksia niin pahasti, että järjestelmä hajoaa kokonaan. Yksi virheellinen päätös voi tuhota viikkojen työn. Siksi CLI-pääsy on yksi agenttien riskialttiimmista työkalutyypeistä.

Siksi sinun täytyy asettaa **tiukat rajat**. Yksi strategia on **whitelist** eli luettelo komennoista, joita agentti saa ajaa. Agentti voi esimerkiksi saada luvan ajaa komennot `ls` eli näytä tiedostot, `mkdir` eli luo kansio ja `cp` eli kopioi tiedosto. Sen sijaan se ei saa ajaa komentoja `rm` eli poista, `shutdown` eli sammuta järjestelmä tai `chmod` eli muuta käyttöoikeuksia. Whitelist on tiukka mutta turvallinen ratkaisu.

Toinen strategia on **toimintorajoitus**: agentti voi lukea ja luoda, mutta ei poistaa mitään. Kolmas strategia on **hiekkalaatikko** eli eristetty ympäristö, josta agentti ei voi vaikuttaa oikeaan järjestelmään. Neljäs strategia on **hyväksyntä**: agentti voi ehdottaa komentoa, mutta ihmisen täytyy vahvistaa se ennen suorittamista.

Kun näitä strategioita yhdistetään, agentille voidaan antaa riittävästi valtaa työn tekemiseen mutta samalla estää sitä aiheuttamasta vakavaa vahinkoa.

## Orkestraattori: työkalut oikeassa järjestyksessä

Tähän asti olemme puhuneet työkaluista ikään kuin ne olisivat erillisiä. Todellisuudessa agentti ei kuitenkaan ole yksi suuri neuroverkko, joka tekee kaiken itse. Agentti on **orkestraattori** eli koordinaattori, joka kutsuu eri työkaluja oikeassa järjestyksessä.

<figure class="ai-demo"><span class="ai-demo__tag">// viisi kysymystä, viisi työkalua — agentti valitsee, kysyy ja saa vastauksen</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:300px">
  <div class="l22-wrap">
    <div class="l22-q">
      <span class="l22-qq q1">Sataako huomenna Turussa?</span>
      <span class="l22-qq q2">Olenko vapaa pe klo 10?</span>
      <span class="l22-qq q3">Lähetä Villelle kokousmuistio.</span>
      <span class="l22-qq q4">Paljonko 100 € on puntina?</span>
      <span class="l22-qq q5">Muistuta minua huomenna klo 8.</span>
    </div>
    <div class="l22-agent">AGENTTI<span class="l22-think">tunnistaa tarpeen → valitsee työkalun</span></div>
    <div class="l22-tools">
      <span class="l22-t t1">sää</span>
      <span class="l22-t t2">kalenteri</span>
      <span class="l22-t t3">sähköposti</span>
      <span class="l22-t t4">valuutta</span>
      <span class="l22-t t5">muistutus</span>
    </div>
    <span class="l22-res e1">+2 °C · sadetta 80 %</span>
    <span class="l22-res e2">pe 10–11: varattu</span>
    <span class="l22-res e3">viesti lähetetty ✓</span>
    <span class="l22-res e4">kurssi: 1 € = 0,84 £</span>
    <span class="l22-res e5">muistutus asetettu ✓</span>
    <div class="l22-ans">
      <span class="l22-aa a1">”Huomenna sataa — varaa sateenvarjo.”</span>
      <span class="l22-aa a2">”Et ole — pe klo 10 on jo varaus.”</span>
      <span class="l22-aa a3">”Muistio lähti Villelle.”</span>
      <span class="l22-aa a4">”100 euroa on noin 84 puntaa.”</span>
      <span class="l22-aa a5">”Muistutan sinua huomenna klo 8.”</span>
    </div>
  </div>
</div>
<figcaption class="ai-demo__cap">Agentti ei tiedä säätä, kalenteria eikä kursseja itse. Jokainen kysymys ohjautuu eri työkalulle: agentti tunnistaa tarpeen, kutsuu oikeaa työkalua ja muotoilee vastauksen vasta työkalun palauttamasta tuloksesta.</figcaption></figure>
<style>
.l22-wrap{position:relative;width:560px;height:262px;font-family:var(--font-mono)}
.l22-q{position:absolute;left:0;top:0;width:204px;height:52px}
.l22-qq{position:absolute;inset:0;display:flex;align-items:center;font-size:12px;font-weight:500;line-height:1.4;color:#06212A;background:#46c7cf;border-radius:11px;padding:6px 11px;opacity:0;height:fit-content;min-height:38px}
.l22-qq.q1{animation:l22q1 22.5s infinite}
.l22-qq.q2{animation:l22q2 22.5s infinite}
.l22-qq.q3{animation:l22q3 22.5s infinite}
.l22-qq.q4{animation:l22q4 22.5s infinite}
.l22-qq.q5{animation:l22q5 22.5s infinite}
@keyframes l22q1{0%,1%{opacity:0}3%,17%{opacity:1}19%,100%{opacity:0}}
@keyframes l22q2{0%,21%{opacity:0}23%,37%{opacity:1}39%,100%{opacity:0}}
@keyframes l22q3{0%,41%{opacity:0}43%,57%{opacity:1}59%,100%{opacity:0}}
@keyframes l22q4{0%,61%{opacity:0}63%,77%{opacity:1}79%,100%{opacity:0}}
@keyframes l22q5{0%,81%{opacity:0}83%,97%{opacity:1}99%,100%{opacity:0}}
.l22-agent{position:absolute;left:0;top:96px;width:204px;text-align:center;font-size:12.5px;letter-spacing:.13em;color:#EAEEF8;background:#11182A;border:2px solid oklch(0.66 0.13 208);border-radius:13px;padding:14px 10px}
.l22-think{display:block;margin-top:6px;font-size:9.5px;letter-spacing:.02em;color:#8B94B3}
.l22-tools{position:absolute;right:0;top:8px;display:flex;flex-direction:column;gap:8px;width:150px}
.l22-t{font-size:11.5px;color:#B9C2DA;background:#0E1422;border:1.5px solid #2B3552;border-radius:9px;padding:7px 11px}
.l22-t.t1{animation:l22t1 22.5s infinite}
.l22-t.t2{animation:l22t2 22.5s infinite}
.l22-t.t3{animation:l22t3 22.5s infinite}
.l22-t.t4{animation:l22t4 22.5s infinite}
.l22-t.t5{animation:l22t5 22.5s infinite}
@keyframes l22t1{0%,3%,18%,100%{color:#B9C2DA;border-color:#2B3552;box-shadow:none}6%,15%{color:#FFFFFF;border-color:oklch(0.72 0.13 208);box-shadow:0 0 12px oklch(0.66 0.13 208/.45)}}
@keyframes l22t2{0%,23%,38%,100%{color:#B9C2DA;border-color:#2B3552;box-shadow:none}26%,35%{color:#FFFFFF;border-color:oklch(0.72 0.13 208);box-shadow:0 0 12px oklch(0.66 0.13 208/.45)}}
@keyframes l22t3{0%,43%,58%,100%{color:#B9C2DA;border-color:#2B3552;box-shadow:none}46%,55%{color:#FFFFFF;border-color:oklch(0.72 0.13 208);box-shadow:0 0 12px oklch(0.66 0.13 208/.45)}}
@keyframes l22t4{0%,63%,78%,100%{color:#B9C2DA;border-color:#2B3552;box-shadow:none}66%,75%{color:#FFFFFF;border-color:oklch(0.72 0.13 208);box-shadow:0 0 12px oklch(0.66 0.13 208/.45)}}
@keyframes l22t5{0%,83%,98%,100%{color:#B9C2DA;border-color:#2B3552;box-shadow:none}86%,95%{color:#FFFFFF;border-color:oklch(0.72 0.13 208);box-shadow:0 0 12px oklch(0.66 0.13 208/.45)}}
.l22-res{position:absolute;right:158px;font-size:10.5px;white-space:nowrap;color:#0B0F1A;background:#F7C873;border-radius:999px;padding:3px 9px;opacity:0}
.l22-res.e1{top:12px;animation:l22e1 22.5s infinite}
.l22-res.e2{top:54px;animation:l22e2 22.5s infinite}
.l22-res.e3{top:96px;animation:l22e3 22.5s infinite}
.l22-res.e4{top:138px;animation:l22e4 22.5s infinite}
.l22-res.e5{top:180px;animation:l22e5 22.5s infinite}
@keyframes l22e1{0%,7%{opacity:0;transform:translateX(8px)}10%,16%{opacity:1;transform:translateX(0)}19%,100%{opacity:0}}
@keyframes l22e2{0%,27%{opacity:0;transform:translateX(8px)}30%,36%{opacity:1;transform:translateX(0)}39%,100%{opacity:0}}
@keyframes l22e3{0%,47%{opacity:0;transform:translateX(8px)}50%,56%{opacity:1;transform:translateX(0)}59%,100%{opacity:0}}
@keyframes l22e4{0%,67%{opacity:0;transform:translateX(8px)}70%,76%{opacity:1;transform:translateX(0)}79%,100%{opacity:0}}
@keyframes l22e5{0%,87%{opacity:0;transform:translateX(8px)}90%,96%{opacity:1;transform:translateX(0)}99%,100%{opacity:0}}
.l22-ans{position:absolute;left:0;top:196px;width:340px;height:52px}
.l22-aa{position:absolute;inset:0;display:flex;align-items:center;font-size:12px;line-height:1.45;color:#FFFFFF;background:#1E2740;border:1.5px solid #7FD0A8;border-radius:11px;padding:6px 12px;opacity:0;height:fit-content;min-height:36px}
.l22-aa.a1{animation:l22a1 22.5s infinite}
.l22-aa.a2{animation:l22a2 22.5s infinite}
.l22-aa.a3{animation:l22a3 22.5s infinite}
.l22-aa.a4{animation:l22a4 22.5s infinite}
.l22-aa.a5{animation:l22a5 22.5s infinite}
@keyframes l22a1{0%,11%{opacity:0}14%,17%{opacity:1}20%,100%{opacity:0}}
@keyframes l22a2{0%,31%{opacity:0}34%,37%{opacity:1}40%,100%{opacity:0}}
@keyframes l22a3{0%,51%{opacity:0}54%,57%{opacity:1}60%,100%{opacity:0}}
@keyframes l22a4{0%,71%{opacity:0}74%,77%{opacity:1}80%,100%{opacity:0}}
@keyframes l22a5{0%,91%{opacity:0}94%,97%{opacity:1}100%,100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l22-qq,.l22-t,.l22-res,.l22-aa{animation:none}
.l22-qq.q1,.l22-res.e1,.l22-aa.a1{opacity:1}
.l22-t.t1{color:#FFFFFF;border-color:oklch(0.72 0.13 208)}}
</style>


Orkesterissa kapellimestari ei soita jokaista instrumenttia itse. Hän ohjaa: ”Viulut, teidän vuoronne.” Kun viulujen osuus on valmis, hän ohjaa seuraavan ryhmän: ”Puhaltimet, teidän vuoronne.” Jokainen muusikko on erikoistunut omaan instrumenttiinsa, ja kapellimestari koordinoi toimintaa niin, että syntyy yhtenäinen kokonaisuus. Orkesteri on vahvempi kuin yksittäinen muusikko.

Agentti toimii samalla tavalla. Se kutsuu työkaluja järjestyksessä: ”Tiedostolukija, lue myyntitiedot.csv.” Kun tiedostolukija on valmis, agentti voi jatkaa: ”Verkkohakija, etsi markkinatrendejä.” Kun hakija on palauttanut tulokset, agentti voi pyytää: ”Analyysityökalu, analysoi nämä luvut.” Jokainen työkalu tekee sen, mitä se osaa parhaiten, ja agentti yhdistää tulokset kokonaisuudeksi.

**Orkestraattori tarvitsee ohjeita** eli strategioita tai suunnittelumalleja siitä, miten työkaluja kutsutaan järjestyksessä. Nämä mallit perustuvat siihen, miten monimutkaisia ongelmia ratkaistaan vaiheittain. Kaksi tärkeää mallia ovat **ReAct** ja **chain-of-thought**, joita käsitellään tarkemmin seuraavalla oppitunnilla. Tärkeintä on nyt ymmärtää, että agentti ei käytä kaikkia työkaluja samanaikaisesti. Se käyttää niitä vaiheittain sen mukaan, mitä seuraavaksi tarvitaan.

## Työkalut n8n:ssä — yhteys käytäntöön

Kun rakennat agenttia oppitunneilla 26–27, nämä abstraktit työkalut muuttuvat konkreettisiksi n8n-solmuiksi. Alla oleva taulukko auttaa yhdistämään teorian käytäntöön.

| Työkalu teoriassa | n8n-solmu käytännössä | Esimerkki |
| --- | --- | --- |
| Tiedoston luku | **Read Files** -solmu tai **Google Sheets** -solmu | Agentti lukee myyntiraportin CSV-tiedostosta. |
| Tiedoston kirjoitus | **Write File** -solmu tai **Google Sheets** -solmu | Agentti kirjoittaa analyysitulokset tiedostoon. |
| Verkkohaku | **HTTP Request** -solmu tai **Google Search** -solmu | Agentti hakee tuotteen hinnan kilpailijan sivulta. |
| CLI-komento | **Execute Command** -solmu hiekkalaatikossa | Agentti ajaa skriptin, joka analysoi lokitiedostoja. |
| Sähköposti | **Gmail**- tai **SMTP**-solmu | Agentti lähettää vastauksen asiakkaalle. |
| Tietokantahaku | **MySQL**- tai **PostgreSQL**-solmu | Agentti tarkistaa asiakkaan tilaushistorian. |

Tässä oppitunnissa käsitellyt turvakerrokset, kuten whitelist, toimintorajoitus, hiekkalaatikko ja hyväksynnät, voidaan toteuttaa n8n:ssä esimerkiksi **IF-solmuilla** ehtojen tarkistamiseen, **erillisillä työnkuluilla** turvalliseen eristämiseen ja **hyväksyntäsolmuilla**, joissa ihminen tarkistaa toiminnon ennen suoritusta. Tämä konkretisoituu oppitunneilla 26–27, mutta jo nyt kannattaa kysyä: mikä n8n-solmu toteuttaisi tämän toiminnon?

## Käytännön esimerkki: analytiikka-agentti työvaiheissa

Kuvittele agentti, joka analysoi myyntidataa yrityksen johtajalle. Tässä esimerkissä näet, miten kolme työkalua toimivat yhdessä.

Ensin agentti lukee tiedostoja. Se avaa `myyntitiedot_2026.csv`-tiedoston, joka sisältää kuukausittaiset myyntiluvut: ”Tammikuu: 50 000 €, Helmikuu: 52 000 €, Maaliskuu: 48 000 €.” Tämä on aineisto, johon analyysi perustuu.

Sitten agentti hakee verkosta kontekstia. Se etsii markkinatrendejä, esimerkiksi tiedon siitä, että teknologiasektori kasvoi 8 % viime vuoden vastaavaan aikaan verrattuna. Se hakee kilpailijatietoa ja huomaa, että kilpailija laski hintojaan 5 %. Se hakee asiakaspalautetta ja löytää mainintoja tuotteiden paremmasta saatavuudesta. Tämä verkosta löytyvä konteksti auttaa agenttia ymmärtämään, onko esimerkiksi 4 % lasku myynnissä huono merkki vai osa odotettavaa markkinakehitystä.

Lopuksi agentti tekee työn CLI:n kautta. Se ajaa analyysiskriptin komennolla `python analyze_sales.py`. Skripti käsittelee datan ja tuottaa esimerkiksi myyntikäyriä, trendianalyysin ja ennusteita. Sen jälkeen agentti kirjoittaa tulokset raporttitiedostoon, joka sisältää yhteenvedon, kaaviot ja johtopäätökset. Agentti voi vielä siirtää valmiin raportin oikeaan kansioon komennolla `mv raportti.txt /reports/myyntiraportti_2026_Q1.txt`.

Nämä kolme työkalua muodostavat yhdessä toimivan prosessin: agentti lukee dataa tiedostoista, etsii kontekstia verkosta, tekee analyysin CLI-komennolla ja kirjoittaa tulokset takaisin tiedostoksi. Jokainen työkalu tukee seuraavaa vaihetta.

## Riskinhallinta — jokainen työkalu vaatii rajoituksia

Kolme työkalua — tiedostot, verkkohaku ja CLI — ovat voimakkaita. Voima tuo kuitenkin mukanaan vastuun. Ammattilaisena sinun täytyy **suunnitella rajoitukset jokaiselle työkalulle** ennen kuin annat agentin käyttää niitä.

**Tiedostotyökalulle:** anna lukuoikeus vain välttämättömiin tiedostoihin. Anna kirjoitusoikeus vain erikseen määriteltyihin kansioihin. Älä anna poistooikeutta lainkaan, ellei se ole tehtävän kannalta välttämätöntä. Lokita jokainen tiedoston avaus ja muokkaus, jotta näet myöhemmin, mitä agentti teki.

**Verkkohakutyökalulle:** määritä sallittujen lähteiden whitelist. Rajoita, kuinka monta hakua agentti voi tehdä sekunnissa tai päivässä. Estä haku henkilökohtaisista tai arkaluontoisista termeistä. Kirjaa jokainen haku, jotta näet, mitä agentti etsi.

**CLI-työkalulle:** käytä tiukkaa komentojen whitelistiä tai aja agentin CLI-toiminnot hiekkalaatikossa erillään oikeista palvelimista. Vaadi ihmisen hyväksyntä kriittisille toiminnoille, kuten poistolle tai palvelimen sammuttamiselle. Lokita jokainen suoritettu komento.

Näillä rajoituksilla agentti pysyy hallinnassa. Se voi tehdä työtään, mutta se ei pääse aiheuttamaan katastrofaalista vahinkoa.

## Kohti omaa projektia

Tämän oppitunnin työkaluajattelu auttaa sinua hahmottamaan, mitä konkreettisia toimintoja oma agenttisi tarvitsee. Mieti omaa projektiasi: tarvitseeko agenttisi lukea tiedostoja, hakea tietoa verkosta vai suorittaa komentoja? Miten rajaat työkalut niin, että agentti pääsee käsiksi vain siihen, mitä se todella tarvitsee? Taulukko, jossa yhdistät abstraktit työkalut konkreettisiin n8n-solmuihin, on hyvä lähtökohta rakentamiselle.

## Yhteenveto

Agentti näkee ja muistaa, mutta sen voima syntyy siitä, että se voi **tehdä todellisia asioita**. Kolme perustyökalua — **tiedostot, verkkohaku ja CLI-komennot** — antavat agentille kyvyn toimia maailmassa. Agentti ei ole yksi suuri älykäs ohjelma, vaan **orkestraattori**, joka kutsuu työkaluja järjestyksessä tehtävän ratkaisemiseksi.

Jokainen työkalu tuo kuitenkin mukanaan turvallisuusriskejä, jotka täytyy hallita rajoituksilla. Tiedostojen käytössä hallitaan tiedosto-oikeuksia. Verkkohaussa määritetään sallittujen lähteiden whitelist. CLI-komennoissa käytetään komentojen whitelistiä, hiekkalaatikkoa tai ihmisen hyväksyntää. Kun rakennat agenttia n8n:llä seuraavilla oppitunneilla, nämä työkalut ovat ensimmäisiä integraatioita, joita kytket agentin rinnalle. Jokaisen kohdalla sinun täytyy miettiä, mitä rajoituksia se tarvitsee.

---
