# Miksi tekoäly valehtelee? — hallusinaatiot ja satunnaisuus

## Johdanto

**Tämän tunnin rajaus:** Tarkastelet yhden kielimallivastauksen tiedollista luotettavuutta: hallusinaatioita, satunnaisuutta ja väitteen tarkistamista lähteestä. Tunnilla 24 siirryt agentin aktiivisiin uhkiin, kuten epäluotettavaan syötteeseen, työkalujen oikeuksiin ja hyökkäysten rajaamiseen.

Olet juuri antanut ChatGPT:lle saman kysymyksen kaksi kertaa. Huomaat kuitenkin jotain outoa: vastaukset ovat erilaiset. Ensimmäisellä kerralla sait selkeän ja hyvin jäsennellyn koodinpätkän. Toisella kerralla sama pyyntö tuotti lähes oikean koodin, mutta funktio kutsuikin API:a, jota ei ole olemassa. Mistä tämä johtuu? Eikö tekoälyn pitäisi olla **deterministinen**, kuten perinteinen ohjelma, joka tuottaa aina samalla syötteellä saman tuloksen?

Vastaus on: ei. **Generatiiviset kielimallit** eivät ole samalla tavalla deterministisiä kuin perinteiset ohjelmat. Ne ovat **todennäköisyyspohjaisia järjestelmiä**, jotka toimivat eri tavalla kuin klassinen ohjelmointi. Tämän ymmärtäminen on tärkeää, kun työskentelet tekoälyn kanssa asiallisesti.

Tämän tunnin jälkeen sinulla on seitsemäs todistusaineisto omaan arviointipöytääsi: tekoäly voi olla yhtä aikaa vahva ja epäluotettava. Se voi tuottaa hyödyllisiä vastauksia, mutta se voi myös väittää itsevarmasti asioita, jotka eivät pidä paikkaansa, koska se ei ymmärrä totuutta samalla tavalla kuin ihminen.

## Miksi tulokset vaihtelevat: epädeterminismi

Kun ChatGPT tai Claude vastaa kysymykseesi, se ei muodosta vastausta samalla tavalla kuin ihminen, joka pohtii asiaa tietoisesti. Sen sijaan malli tekee sarjan valintoja yksi sana tai tekstin osa kerrallaan. Jokaisessa vaiheessa malli arvioi, mikä seuraava sana tai merkkiyhdistelmä on todennäköisin aiemman tekstin perusteella.

Malli voi esimerkiksi arvioida: ”Mikä on todennäköisyys, että seuraava sana on *koodi*? Entä *lohko*? Entä *silmukka*?” Näiden todennäköisyyksien perusteella se valitsee seuraavan osan vastauksesta.

Tähän liittyy usein parametri nimeltä **lämpötila** eli *temperature*. Se vaikuttaa siihen, kuinka ennustettava tai vaihteleva vastaus on. **Matala lämpötila**, esimerkiksi 0,3, ohjaa mallia valitsemaan todennäköisimpiä vaihtoehtoja. Tällöin vastaukset ovat yleensä johdonmukaisempia ja ennustettavampia. **Korkea lämpötila**, esimerkiksi 1,5, sallii epätodennäköisempien vaihtoehtojen valitsemisen. Tällöin vastaukset voivat olla luovempia, mutta myös vaihtelevampia ja epävarmempia.

Tämä ei ole ohjelmointivirhe, vaan mallin rakenteellinen ominaisuus. Korkea lämpötila mahdollistaa luovuuden ja monimuotoisuuden. Matala lämpötila taas lisää johdonmukaisuutta ja ennustettavuutta. Vastuulliselle käyttäjälle tämä tarkoittaa, että esimerkiksi API-dokumentaatiota kirjoittaessa kannattaa suosia johdonmukaisuutta. Ideointivaiheessa, kuten markkinointikampanjan vaihtoehtoja suunniteltaessa, vaihtelevuus voi puolestaan olla hyödyllistä.

> **Pysähdy hetkeksi:** Missä oman työsi tilanteissa tarvitsisit matalaa lämpötilaa eli johdonmukaisuutta? Entä missä tilanteissa korkeampi lämpötila eli luovempi ja vaihtelevampi vastaus voisi olla hyödyllinen?

## Miksi malli hallusinoi: teksti ei ole sama asia kuin fakta

**Hallusinaatio** tarkoittaa tilannetta, jossa tekoäly väittää jotain, mikä ei pidä paikkaansa. Saatat esimerkiksi kysyä: ”Mikä on Pythonin urllib3-kirjaston oikea syntaksi HTTP-kutsulle?” Malli voi vastata uskottavalla koodiesimerkillä, joka näyttää oikealta mutta käyttää funktiota, jota ei todellisuudessa ole olemassa.

Toinen esimerkki: kysyt ”Kuka oli Suomen toinen pääministeri?” ja saat vastauksen, joka kuulostaa varmalta mutta on väärä. Hallusinaatio voi siis olla täysin itsevarmalta vaikuttava virheellinen väite.

Miksi näin tapahtuu? Koska kielimallit ovat **todennäköisyyspohjaisia ennustajia**, eivät faktakoneita. Ne oppivat, millaiset sanat, rakenteet ja sisällöt tyypillisesti seuraavat toisiaan. Kun mallilta kysytään esimerkiksi urllib3-kirjaston HTTP-kutsusta, se on oppinut, että tällaisissa yhteyksissä seuraa usein koodiesimerkkejä. Siksi se tuottaa koodia, joka näyttää uskottavalta.

Ongelma on siinä, että malli ei välttämättä ole tarkistanut vastausta oikeaa dokumentaatiota vasten. Se ennustaa, millainen oikealta näyttävä vastaus sopisi tilanteeseen. Se ei automaattisesti tiedä, ovatko kaikki yksityiskohdat oikein. **Hallusinaatio** syntyy, kun todennäköinen ja uskottavalta kuulostava vastaus onkin virheellinen.

Tämä on erityisen vaarallista tekniikan parissa. Teknisen alan osaajalla voi olla hyvä ”kuulostaa oikealta” -tuntuma, mutta se ei aina riitä. Kriittiset tiedot täytyy aina **verifioida** eli tarkistaa luotettavasta lähteestä ennen käyttöä.

> **Pysähdy hetkeksi:** Missä IT:n käyttötapauksissa hallusinaatiot olisivat vaarallisimpia? Ajattele esimerkiksi tuotantokoodia, tietoturvaa ja asiakastietoja.

<figure class="ai-demo"><span class="ai-demo__tag">// testi: malli vastasi kymmenen kertaa yhtä varmasti — löydätkö keksityt?</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:380px">
  <div class="l07-wrap">
    <input type="radio" name="l07s" id="l07-s1" class="l07-in l07-s1" checked>
    <input type="radio" name="l07s" id="l07-s2" class="l07-in l07-s2">
    <input type="radio" name="l07s" id="l07-s3" class="l07-in l07-s3">
    <input type="radio" name="l07s" id="l07-s4" class="l07-in l07-s4">
    <input type="radio" name="l07s" id="l07-s5" class="l07-in l07-s5">
    <input type="radio" name="l07q1" id="l07-a1" class="l07-in l07-a1"><input type="radio" name="l07q1" id="l07-b1" class="l07-in l07-b1">
    <input type="radio" name="l07q2" id="l07-a2" class="l07-in l07-a2"><input type="radio" name="l07q2" id="l07-b2" class="l07-in l07-b2">
    <input type="radio" name="l07q3" id="l07-a3" class="l07-in l07-a3"><input type="radio" name="l07q3" id="l07-b3" class="l07-in l07-b3">
    <input type="radio" name="l07q4" id="l07-a4" class="l07-in l07-a4"><input type="radio" name="l07q4" id="l07-b4" class="l07-in l07-b4">
    <input type="radio" name="l07q5" id="l07-a5" class="l07-in l07-a5"><input type="radio" name="l07q5" id="l07-b5" class="l07-in l07-b5">
    <span class="l07-cta">▶ KOKEILE ITSE — klikkaa väitettä, joka on totta</span>
    <span class="l07-prog p1">väitepari 1/5</span><span class="l07-prog p2">väitepari 2/5</span><span class="l07-prog p3">väitepari 3/5</span><span class="l07-prog p4">väitepari 4/5</span><span class="l07-prog p5">väitepari 5/5</span>
    <div class="l07-round r1">
      <label for="l07-a1" class="l07-card ca tru"><span class="l07-ans">”Tuntemattoman sotilaan kirjoitti Väinö Linna vuonna 1954.”</span><span class="l07-st st-t">✓ totta</span></label>
      <label for="l07-b1" class="l07-card cb fls"><span class="l07-ans">”Romaanin Suuri Mahtava kirjoitti Jane Austen vuonna 1847.”</span><span class="l07-st st-f">✗ keksitty</span></label>
      <span class="l07-info">Suuri Mahtava -teosta ei ole olemassa — malli yhdistää nimen ja vuosiluvun uskottavasti.</span>
      <label for="l07-s2" class="l07-next">seuraava pari →</label>
    </div>
    <div class="l07-round r2">
      <label for="l07-a2" class="l07-card ca fls"><span class="l07-ans">”Mika Häkkinen voitti Monacon GP:n vuonna 2003.”</span><span class="l07-st st-f">✗ keksitty</span></label>
      <label for="l07-b2" class="l07-card cb tru"><span class="l07-ans">”Kimi Räikkönen voitti F1-maailmanmestaruuden vuonna 2007.”</span><span class="l07-st st-t">✓ totta</span></label>
      <span class="l07-info">Häkkinen lopetti F1-uransa jo 2001 — keksitty voitto kuulostaa silti aidolta.</span>
      <label for="l07-s3" class="l07-next">seuraava pari →</label>
    </div>
    <div class="l07-round r3">
      <label for="l07-a3" class="l07-card ca tru"><span class="l07-ans">”Valo kulkee Auringosta Maahan noin kahdeksassa minuutissa.”</span><span class="l07-st st-t">✓ totta</span></label>
      <label for="l07-b3" class="l07-card cb fls"><span class="l07-ans">”Kuu kiertää Maan noin viikossa.”</span><span class="l07-st st-f">✗ keksitty</span></label>
      <span class="l07-info">Kuun kierros kestää noin 27 päivää — ”viikko” on sujuva mutta väärä.</span>
      <label for="l07-s4" class="l07-next">seuraava pari →</label>
    </div>
    <div class="l07-round r4">
      <label for="l07-a4" class="l07-card ca fls"><span class="l07-ans">”Lahden talviolympialaiset järjestettiin vuonna 1978.”</span><span class="l07-st st-f">✗ keksitty</span></label>
      <label for="l07-b4" class="l07-card cb tru"><span class="l07-ans">”Helsingin kesäolympialaiset järjestettiin vuonna 1952.”</span><span class="l07-st st-t">✓ totta</span></label>
      <span class="l07-info">Lahdessa on pidetty hiihdon MM-kisat, ei olympialaisia — uskottava yhdistelmä huijaa helposti.</span>
      <label for="l07-s5" class="l07-next">seuraava pari →</label>
    </div>
    <div class="l07-round r5">
      <label for="l07-a5" class="l07-card ca fls"><span class="l07-ans">”Minna Canthin romaani Punainen viiva ilmestyi 1893.”</span><span class="l07-st st-f">✗ keksitty</span></label>
      <label for="l07-b5" class="l07-card cb tru"><span class="l07-ans">”Aleksis Kiven Seitsemän veljestä ilmestyi 1870.”</span><span class="l07-st st-t">✓ totta</span></label>
      <span class="l07-info">Punainen viiva on Ilmari Kiannon romaani (1909). Kaikki viisi käyty — pinnasta et voinut tietää kertaakaan. Siksi faktat tarkistetaan aina lähteestä.</span>
      <label for="l07-s1" class="l07-next">↺ alusta</label>
    </div>
  </div>
</div>
<figcaption class="ai-demo__cap">Hallusinaatio: malli esittää keksityn tiedon täsmälleen yhtä itsevarmasti ja sujuvasti kuin oikean, eikä varoita epävarmuudesta. Sujuvuus ei ole todiste totuudesta — kriittiset faktat tarkistetaan aina luotettavasta lähteestä.</figcaption></figure>
<style>
.l07-wrap{position:relative;width:560px;height:340px;font-family:var(--font-mono)}
.l07-in{position:absolute;opacity:0;pointer-events:none}
.l07-cta{position:absolute;left:50%;transform:translateX(-50%);top:0;white-space:nowrap;font-size:11.5px;font-weight:700;letter-spacing:.07em;color:#06212A;background:#46c7cf;border-radius:999px;padding:6px 16px;box-shadow:0 0 0 0 rgba(70,199,207,.5);animation:l07cta 2.2s ease-out infinite}
@keyframes l07cta{0%{box-shadow:0 0 0 0 rgba(70,199,207,.5)}70%{box-shadow:0 0 0 12px rgba(70,199,207,0)}100%{box-shadow:0 0 0 0 rgba(70,199,207,0)}}
.l07-prog{position:absolute;left:0;bottom:0;font-size:10.5px;letter-spacing:.06em;color:#8B94B3;opacity:0}
.l07-round{position:absolute;left:0;right:0;top:46px;bottom:0;opacity:0;pointer-events:none;transition:opacity .35s}
.l07-card{position:absolute;top:8px;width:268px;min-height:150px;background:#11182A;border:2px solid #2B3552;border-radius:13px;padding:14px;cursor:pointer;transition:border-color .25s,transform .2s;display:block;animation:l07invite 2.6s ease-in-out infinite}
.l07-card.cb{animation-delay:1.3s}
@keyframes l07invite{0%,100%{border-color:#2B3552}50%{border-color:#46c7cf}}
.l07-card:hover{border-color:#46c7cf;transform:translateY(-2px)}
.l07-card.ca{left:0}
.l07-card.cb{right:0}
.l07-ans{display:block;font-size:12.5px;line-height:1.55;color:#FFFFFF}
.l07-st{position:absolute;left:14px;bottom:12px;font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;border-radius:999px;padding:2px 9px;opacity:0;transform:scale(1.25);transition:opacity .35s,transform .35s}
.l07-st.st-t{color:#06241a;background:#7FD0A8}
.l07-st.st-f{color:#3A1408;background:#F0A38C}
.l07-info{position:absolute;left:0;right:0;top:188px;font-size:11.5px;line-height:1.5;color:#B9C2DA;text-align:center;opacity:0;transition:opacity .4s .15s}
.l07-next{position:absolute;right:0;bottom:0;min-height:44px;display:flex;align-items:center;font-size:11px;letter-spacing:.05em;color:#06212A;background:#46c7cf;font-weight:600;border-radius:999px;padding:5px 13px;cursor:pointer;opacity:0;pointer-events:none;transition:opacity .3s}
.l07-s1:checked~.l07-round.r1{opacity:1;pointer-events:auto}
.l07-s1:checked~.l07-prog.p1{opacity:1}
.l07-a1:checked~.r1 .l07-st,.l07-b1:checked~.r1 .l07-st{opacity:1;transform:scale(1)}
.l07-a1:checked~.r1 .l07-info,.l07-b1:checked~.r1 .l07-info,.l07-a1:checked~.r1 .l07-next,.l07-b1:checked~.r1 .l07-next{opacity:1;pointer-events:auto}
.l07-a1:checked~.r1 .tru,.l07-b1:checked~.r1 .tru{border-color:#7FD0A8;animation:none}
.l07-a1:checked~.r1 .fls,.l07-b1:checked~.r1 .fls{border-color:#F0A38C;animation:none}
.l07-s2:checked~.l07-round.r2{opacity:1;pointer-events:auto}
.l07-s2:checked~.l07-prog.p2{opacity:1}
.l07-a2:checked~.r2 .l07-st,.l07-b2:checked~.r2 .l07-st{opacity:1;transform:scale(1)}
.l07-a2:checked~.r2 .l07-info,.l07-b2:checked~.r2 .l07-info,.l07-a2:checked~.r2 .l07-next,.l07-b2:checked~.r2 .l07-next{opacity:1;pointer-events:auto}
.l07-a2:checked~.r2 .tru,.l07-b2:checked~.r2 .tru{border-color:#7FD0A8;animation:none}
.l07-a2:checked~.r2 .fls,.l07-b2:checked~.r2 .fls{border-color:#F0A38C;animation:none}
.l07-s3:checked~.l07-round.r3{opacity:1;pointer-events:auto}
.l07-s3:checked~.l07-prog.p3{opacity:1}
.l07-a3:checked~.r3 .l07-st,.l07-b3:checked~.r3 .l07-st{opacity:1;transform:scale(1)}
.l07-a3:checked~.r3 .l07-info,.l07-b3:checked~.r3 .l07-info,.l07-a3:checked~.r3 .l07-next,.l07-b3:checked~.r3 .l07-next{opacity:1;pointer-events:auto}
.l07-a3:checked~.r3 .tru,.l07-b3:checked~.r3 .tru{border-color:#7FD0A8;animation:none}
.l07-a3:checked~.r3 .fls,.l07-b3:checked~.r3 .fls{border-color:#F0A38C;animation:none}
.l07-s4:checked~.l07-round.r4{opacity:1;pointer-events:auto}
.l07-s4:checked~.l07-prog.p4{opacity:1}
.l07-a4:checked~.r4 .l07-st,.l07-b4:checked~.r4 .l07-st{opacity:1;transform:scale(1)}
.l07-a4:checked~.r4 .l07-info,.l07-b4:checked~.r4 .l07-info,.l07-a4:checked~.r4 .l07-next,.l07-b4:checked~.r4 .l07-next{opacity:1;pointer-events:auto}
.l07-a4:checked~.r4 .tru,.l07-b4:checked~.r4 .tru{border-color:#7FD0A8;animation:none}
.l07-a4:checked~.r4 .fls,.l07-b4:checked~.r4 .fls{border-color:#F0A38C;animation:none}
.l07-s5:checked~.l07-round.r5{opacity:1;pointer-events:auto}
.l07-s5:checked~.l07-prog.p5{opacity:1}
.l07-a5:checked~.r5 .l07-st,.l07-b5:checked~.r5 .l07-st{opacity:1;transform:scale(1)}
.l07-a5:checked~.r5 .l07-info,.l07-b5:checked~.r5 .l07-info,.l07-a5:checked~.r5 .l07-next,.l07-b5:checked~.r5 .l07-next{opacity:1;pointer-events:auto}
.l07-a5:checked~.r5 .tru,.l07-b5:checked~.r5 .tru{border-color:#7FD0A8;animation:none}
.l07-a5:checked~.r5 .fls,.l07-b5:checked~.r5 .fls{border-color:#F0A38C;animation:none}
@media (prefers-reduced-motion:reduce){.l07-cta,.l07-card{animation:none}.l07-card,.l07-st,.l07-info,.l07-next,.l07-round{transition:none}}
@media (max-width:680px){
.ai-demo__interaction:has(.l07-wrap){height:520px!important;padding:12px}
.l07-wrap{width:100%;height:480px}
.l07-cta{position:static;display:block;transform:none;white-space:normal;text-align:center;font-size:12px;line-height:1.4;min-height:44px;padding:10px 12px}
.l07-prog{bottom:0;font-size:12px}
.l07-round{top:64px}
.l07-card{left:0!important;right:0!important;width:100%;min-height:108px;padding:12px}
.l07-card.ca{top:0}.l07-card.cb{top:120px}
.l07-ans{font-size:13px;line-height:1.45;padding-right:0;padding-bottom:26px}
.l07-st{left:12px;bottom:10px;font-size:12px}
.l07-info{top:244px;font-size:13px;line-height:1.45;text-align:left}
.l07-next{bottom:0;min-height:44px;display:flex;align-items:center;padding:8px 14px;font-size:13px}
}
</style>

## Miksi tekoäly ei ole totuuskone?

Seuraavaa asiaa ei voi korostaa liikaa: **generatiiviset kielimallit eivät ole faktakoneita, vaan sanojen ja tekstirakenteiden ennustajia.**

Tämä tarkoittaa kolmea tärkeää asiaa:

1. **Itsevarmuus ei tarkoita oikeellisuutta.** Hallusinaatio voi kuulostaa täysin varmalta. Malli voi antaa väärän tiedon täsmällisin yksityiskohdin eikä välttämättä varoita epävarmuudesta. Tämä tekee virheistä erityisen vaarallisia.
2. **Konteksti antaa mallille kuvion, ei varmaa tietoa.** Jos kysyt: ”Mitä Windowsin tasklist-komento tekee?”, malli hyödyntää koulutusdatassa oppimiaan malleja ja esimerkkejä. Se osaa ennustaa, mitä tällainen vastaus yleensä sisältää, mutta vastaus on silti tarkistettava, jos sitä käytetään kriittisessä työssä.
3. **Mallilla voi olla ajallinen raja.** Malli on opetettu aineistolla, joka ulottuu vain tiettyyn ajankohtaan asti. Uudet tapahtumat, API-päivitykset, kirjastoversiot ja dokumentaatiomuutokset voivat siksi olla erityisen alttiita virheille.

Vastuullisena käyttäjänä sinun ei pidä koskaan luottaa tekoälyn vastaukseen ilman itsenäistä tarkistusta kriittisissä asioissa. Käytä mallia ideointiin, koodin rungon luomiseen, vaihtoehtojen vertailuun ja dokumentaation luonnosteluun. Sen jälkeen **tarkista, testaa ja validoi**.

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

Malli ei ole totuuskone, vaan tekstin ennustaja. Vastuullisena käyttäjänä sinun vastuullasi on ymmärtää nämä rajat, tarkistaa kriittiset tiedot ja käyttää tekoälyä oikealla tavalla: apuvälineenä, ei erehtymättömänä auktoriteettina.

Seuraavalla tunnilla siirryt eettisiin kysymyksiin: kenen datalla tekoäly on opetettu, ja mitä se maksaa?

---

## Lähteet ja tarkistuspäivä

- [Vaswani ym.: Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [NIST: Generative AI Profile, NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

Tarkistettu 15.7.2026.
