# Miksi tekoäly valehtelee? — hallusinaatiot ja satunnaisuus

## Johdanto

Olet juuri antanut ChatGPT:lle saman kysymyksen kaksi kertaa. Huomaat kuitenkin jotain outoa: vastaukset ovat erilaiset. Ensimmäisellä kerralla sait selkeän ja hyvin jäsennellyn koodinpätkän. Toisella kerralla sama pyyntö tuotti lähes oikean koodin, mutta funktio kutsuikin API:a, jota ei ole olemassa. Mistä tämä johtuu? Eikö tekoälyn pitäisi olla **deterministinen**, kuten perinteinen ohjelma, joka tuottaa aina samalla syötteellä saman tuloksen?

Vastaus on: ei. **Generatiiviset kielimallit** eivät ole samalla tavalla deterministisiä kuin perinteiset ohjelmat. Ne ovat **todennäköisyyspohjaisia järjestelmiä**, jotka toimivat eri tavalla kuin klassinen ohjelmointi. Tämän ymmärtäminen on tärkeää, kun työskentelet tekoälyn kanssa ammatillisesti.

Tämän tunnin jälkeen sinulla on seitsemäs todistusaineisto omaan arviointipöytääsi: tekoäly voi olla yhtä aikaa vahva ja epäluotettava. Se voi tuottaa hyödyllisiä vastauksia, mutta se voi myös väittää itsevarmasti asioita, jotka eivät pidä paikkaansa, koska se ei ymmärrä totuutta samalla tavalla kuin ihminen.

## Miksi tulokset vaihtelevat: epädeterminismi

Kun ChatGPT tai Claude vastaa kysymykseesi, se ei muodosta vastausta samalla tavalla kuin ihminen, joka pohtii asiaa tietoisesti. Sen sijaan malli tekee sarjan valintoja yksi sana tai tekstin osa kerrallaan. Jokaisessa vaiheessa malli arvioi, mikä seuraava sana tai merkkiyhdistelmä on todennäköisin aiemman tekstin perusteella.

Malli voi esimerkiksi arvioida: ”Mikä on todennäköisyys, että seuraava sana on *koodi*? Entä *lohko*? Entä *silmukka*?” Näiden todennäköisyyksien perusteella se valitsee seuraavan osan vastauksesta.

Tähän liittyy usein parametri nimeltä **lämpötila** eli *temperature*. Se vaikuttaa siihen, kuinka ennustettava tai vaihteleva vastaus on. **Matala lämpötila**, esimerkiksi 0,3, ohjaa mallia valitsemaan todennäköisimpiä vaihtoehtoja. Tällöin vastaukset ovat yleensä johdonmukaisempia ja ennustettavampia. **Korkea lämpötila**, esimerkiksi 1,5, sallii epätodennäköisempien vaihtoehtojen valitsemisen. Tällöin vastaukset voivat olla luovempia, mutta myös vaihtelevampia ja epävarmempia.

Tämä ei ole ohjelmointivirhe, vaan mallin rakenteellinen ominaisuus. Korkea lämpötila mahdollistaa luovuuden ja monimuotoisuuden. Matala lämpötila taas lisää johdonmukaisuutta ja ennustettavuutta. Ammattilaiselle tämä tarkoittaa, että esimerkiksi API-dokumentaatiota kirjoittaessa kannattaa suosia johdonmukaisuutta. Ideointivaiheessa, kuten markkinointikampanjan vaihtoehtoja suunniteltaessa, vaihtelevuus voi puolestaan olla hyödyllistä.

> **Pysähdy hetkeksi:** Missä oman työsi tilanteissa tarvitsisit matalaa lämpötilaa eli johdonmukaisuutta? Entä missä tilanteissa korkeampi lämpötila eli luovempi ja vaihtelevampi vastaus voisi olla hyödyllinen?

## Miksi malli hallusinoi: teksti ei ole sama asia kuin fakta

**Hallusinaatio** tarkoittaa tilannetta, jossa tekoäly väittää jotain, mikä ei pidä paikkaansa. Saatat esimerkiksi kysyä: ”Mikä on Pythonin urllib3-kirjaston oikea syntaksi HTTP-kutsulle?” Malli voi vastata uskottavalla koodiesimerkillä, joka näyttää oikealta mutta käyttää funktiota, jota ei todellisuudessa ole olemassa.

Toinen esimerkki: kysyt ”Kuka oli Suomen toinen pääministeri?” ja saat vastauksen, joka kuulostaa varmalta mutta on väärä. Hallusinaatio voi siis olla täysin itsevarmalta vaikuttava virheellinen väite.

Miksi näin tapahtuu? Koska kielimallit ovat **todennäköisyyspohjaisia ennustajia**, eivät faktakoneita. Ne oppivat, millaiset sanat, rakenteet ja sisällöt tyypillisesti seuraavat toisiaan. Kun mallilta kysytään esimerkiksi urllib3-kirjaston HTTP-kutsusta, se on oppinut, että tällaisissa yhteyksissä seuraa usein koodiesimerkkejä. Siksi se tuottaa koodia, joka näyttää uskottavalta.

Ongelma on siinä, että malli ei välttämättä ole tarkistanut vastausta oikeaa dokumentaatiota vasten. Se ennustaa, millainen oikealta näyttävä vastaus sopisi tilanteeseen. Se ei automaattisesti tiedä, ovatko kaikki yksityiskohdat oikein. **Hallusinaatio** syntyy, kun todennäköinen ja uskottavalta kuulostava vastaus onkin virheellinen.

Tämä on erityisen vaarallista tekniikan parissa. IT-ammattilaisella voi olla hyvä ”kuulostaa oikealta” -tuntuma, mutta se ei aina riitä. Kriittiset tiedot täytyy aina **verifioida** eli tarkistaa luotettavasta lähteestä ennen käyttöä.

> **Pysähdy hetkeksi:** Missä IT:n käyttötapauksissa hallusinaatiot olisivat vaarallisimpia? Ajattele esimerkiksi tuotantokoodia, tietoturvaa ja asiakastietoja.

<figure class="ai-demo"><span class="ai-demo__tag">// kokeile itse: kumpi väite on totta? klikkaa korttia</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:344px">
  <div class="l07-wrap">
    <input type="radio" name="l07q" id="l07-r0" class="l07-in l07-r0" checked>
    <input type="radio" name="l07q" id="l07-ra" class="l07-in l07-ra">
    <input type="radio" name="l07q" id="l07-rb" class="l07-in l07-rb">
    <span class="l07-ask">Malli vastasi kahteen kysymykseen yhtä itsevarmasti. <b>Klikkaa sitä, jota pidät totena.</b></span>
    <label for="l07-ra" class="l07-card l07-a"><span class="l07-q">Kuka kirjoitti Tuntemattoman sotilaan?</span><span class="l07-ans">”Tuntemattoman sotilaan kirjoitti Väinö Linna. Romaani ilmestyi vuonna 1954.”</span><span class="l07-st l07-true">✓ totta</span></label>
    <label for="l07-rb" class="l07-card l07-b"><span class="l07-q">Kuka kirjoitti romaanin Suuri Mahtava?</span><span class="l07-ans">”Romaanin Suuri Mahtava kirjoitti Jane Austen. Teos ilmestyi vuonna 1847.”</span><span class="l07-st l07-fake">✗ keksitty</span></label>
    <span class="l07-res l07-resa">Oikein — mutta huomaa: et voinut <b>nähdä</b> sitä vastauksesta. Molemmat olivat yhtä varmoja ja sujuvia. Siksi faktat tarkistetaan lähteestä.</span>
    <span class="l07-res l07-resb">Tämä oli keksitty — Jane Austen ei kirjoittanut tällaista teosta. Se näytti silti täsmälleen yhtä uskottavalta kuin tosi vastaus. Siksi faktat tarkistetaan lähteestä.</span>
    <label for="l07-r0" class="l07-reset">↺ kokeile uudelleen</label>
  </div>
</div>
<figcaption class="ai-demo__cap">Hallusinaatio: malli esittää keksityn tiedon täsmälleen yhtä itsevarmasti ja sujuvasti kuin oikean, eikä varoita epävarmuudesta. Sujuvuus ei ole todiste totuudesta — kriittiset faktat tarkistetaan aina luotettavasta lähteestä.</figcaption></figure>
<style>
.l07-wrap{position:relative;width:560px;height:306px;font-family:var(--font-mono)}
.l07-in{position:absolute;opacity:0;pointer-events:none}
.l07-ask{position:absolute;left:0;right:0;top:0;font-size:12px;line-height:1.5;color:#EAEEF8;text-align:center}
.l07-ask b{color:#46c7cf}
.l07-card{position:absolute;top:50px;width:268px;min-height:158px;background:#11182A;border:2px solid #2B3552;border-radius:13px;padding:12px 14px;cursor:pointer;transition:border-color .25s,box-shadow .25s,transform .25s;display:block}
.l07-a{left:0}
.l07-b{right:0}
.l07-r0:checked~.l07-card{animation:l07invite 2.6s ease-in-out infinite}
.l07-r0:checked~.l07-b{animation-delay:1.3s}
@keyframes l07invite{0%,100%{border-color:#2B3552}50%{border-color:#46c7cf;box-shadow:0 0 14px rgba(70,199,207,.25)}}
.l07-card:hover{border-color:#46c7cf;transform:translateY(-2px)}
.l07-q{display:block;font-size:11px;line-height:1.4;color:#06212A;background:#46c7cf;font-weight:500;border-radius:8px;padding:6px 9px;margin-bottom:9px}
.l07-ans{display:block;font-size:12px;line-height:1.5;color:#FFFFFF}
.l07-st{position:absolute;left:14px;bottom:11px;font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;border-radius:999px;padding:2px 9px;opacity:0;transform:scale(1.25);transition:opacity .35s,transform .35s}
.l07-true{color:#06241a;background:#7FD0A8}
.l07-fake{color:#3A1408;background:#F0A38C}
.l07-ra:checked~.l07-card .l07-st,.l07-rb:checked~.l07-card .l07-st{opacity:1;transform:scale(1)}
.l07-ra:checked~.l07-card,.l07-rb:checked~.l07-card{animation:none;cursor:default}
.l07-ra:checked~.l07-a{border-color:#7FD0A8}
.l07-rb:checked~.l07-b{border-color:#F0A38C}
.l07-res{position:absolute;left:0;right:0;top:226px;font-size:11.5px;line-height:1.5;color:#B9C2DA;text-align:center;opacity:0;transition:opacity .4s .15s}
.l07-res b{color:#EAEEF8}
.l07-ra:checked~.l07-resa{opacity:1}
.l07-rb:checked~.l07-resb{opacity:1}
.l07-reset{position:absolute;right:0;bottom:0;font-size:10.5px;letter-spacing:.04em;color:#46c7cf;border:1.5px solid #2B3552;border-radius:999px;padding:3px 10px;cursor:pointer;opacity:0;pointer-events:none;transition:opacity .3s}
.l07-ra:checked~.l07-reset,.l07-rb:checked~.l07-reset{opacity:1;pointer-events:auto}
.l07-ra:checked~.l07-ask,.l07-rb:checked~.l07-ask{opacity:.35}
@media (prefers-reduced-motion:reduce){
.l07-r0:checked~.l07-card{animation:none}
.l07-card,.l07-st,.l07-res,.l07-reset{transition:none}}
</style>

## Miksi tekoäly ei ole totuuskone?

Seuraavaa asiaa ei voi korostaa liikaa: **generatiiviset kielimallit eivät ole faktakoneita, vaan sanojen ja tekstirakenteiden ennustajia.**

Tämä tarkoittaa kolmea tärkeää asiaa:

1. **Itsevarmuus ei tarkoita oikeellisuutta.** Hallusinaatio voi kuulostaa täysin varmalta. Malli voi antaa väärän tiedon täsmällisin yksityiskohdin eikä välttämättä varoita epävarmuudesta. Tämä tekee virheistä erityisen vaarallisia.
2. **Konteksti antaa mallille kuvion, ei varmaa tietoa.** Jos kysyt: ”Mitä Windowsin tasklist-komento tekee?”, malli hyödyntää koulutusdatassa oppimiaan malleja ja esimerkkejä. Se osaa ennustaa, mitä tällainen vastaus yleensä sisältää, mutta vastaus on silti tarkistettava, jos sitä käytetään kriittisessä työssä.
3. **Mallilla voi olla ajallinen raja.** Malli on opetettu aineistolla, joka ulottuu vain tiettyyn ajankohtaan asti. Uudet tapahtumat, API-päivitykset, kirjastoversiot ja dokumentaatiomuutokset voivat siksi olla erityisen alttiita virheille.

Ammattilaisena sinun ei pidä koskaan luottaa tekoälyn vastaukseen ilman itsenäistä tarkistusta kriittisissä asioissa. Käytä mallia ideointiin, koodin rungon luomiseen, vaihtoehtojen vertailuun ja dokumentaation luonnosteluun. Sen jälkeen **tarkista, testaa ja validoi**.

> **Pysähdy hetkeksi:** Jos annat asiakkaalle raportin, jonka olet luonut tekoälyn avulla, kenen vastuulla datan oikeellisuus on: sinun vai mallin?

## Epäluotettavuuden merkkejä käytännössä

Seuraavat merkit voivat kertoa, että tekoälyn vastaus saattaa sisältää hallusinaatioita:

- **Vastaus on liian näyttävä:** se on hyvin muotoiltu ja yksityiskohtainen, mutta väitteet ovat hyvin tarkkoja eikä niiden paikkansapitävyyttä ole helppo tarkistaa.
- **Vastaus ei sovi ajankohtaan:** kysyt uusimmasta tekniikasta, mutta mallilla voi olla vanhentunutta tietoa.
- **Logiikka ei kestä tarkastelua:** vastaus vaikuttaa aluksi johdonmukaiselta, mutta tarkempi pohdinta paljastaa ristiriidan.
- **Kokonaisuus sisältää heikkouksia:** yksittäiset lauseet kuulostavat oikeilta, mutta vastaus kokonaisuutena on ristiriitainen tai epäselvä.

**Paras puolustus on terve skeptisyys, erityisesti teknisissä ja kriittisissä asioissa.**

## Yhteenveto

**Generatiiviset kielimallit** ovat epädeterministisiä ja todennäköisyyspohjaisia. Tämä mahdollistaa luovuuden ja monipuoliset vastaukset, mutta tarkoittaa myös sitä, että mallit voivat **hallusinoida**: ne voivat tuottaa itsevarmasti väitteitä, jotka eivät pidä paikkaansa.

Malli ei ole totuuskone, vaan tekstin ennustaja. Ammattilaisena sinun vastuullasi on ymmärtää nämä rajat, tarkistaa kriittiset tiedot ja käyttää tekoälyä oikealla tavalla: apuvälineenä, ei erehtymättömänä auktoriteettina.

Seuraavalla tunnilla siirryt eettisiin kysymyksiin: kenen datalla tekoäly on opetettu, ja mitä se maksaa?

---
