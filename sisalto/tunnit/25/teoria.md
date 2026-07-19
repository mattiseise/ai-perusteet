# Ihminen portinvartijana — ihmisen osallistuminen päätöksentekoon käytännössä

## Johdanto

Kaikki, mitä olet tähän mennessä oppinut — **muisti**, **konteksti**, **työkalut**, **suunnittelumallit** ja **turvallisuus** — johtaa yhteen tärkeään ajatukseen: **agentti ei voi tehdä kaikkea yksin**. Joissain tilanteissa agentti täytyy pysäyttää odottamaan, kunnes ihminen sanoo: ”kyllä, jatka” tai ”ei, älä tee sitä”.

Tässä toimintatavassa **ihminen osallistuu päätöksentekoon** automaation rinnalla. Se ei tarkoita, että ihminen tekee kaiken itse. Se tarkoittaa, että ihminen hyväksyy kriittiset päätökset, tarkistaa riskialttiit toiminnot ja ohjaa agenttia silloin, kun agentti on epävarma.

Tässä oppitunnissa opit, **milloin ihminen täytyy ottaa mukaan päätöksentekoon, miten hyväksyntäportit suunnitellaan ja miten rakennetaan työnkulkuja, joissa agentti ja ihminen tekevät yhteistyötä**. Näitä periaatteita käytät suoraan seuraavilla oppitunneilla, kun rakennat omaa agenttia n8n:llä.

## Milloin ihminen tarvitaan mukaan päätökseen?

Kaikki agentin päätökset eivät tarvitse ihmisen hyväksyntää. Jos jokainen pieni päätös pysäytetään ihmiselle, seurauksena on hidas ja kuormittava järjestelmä. Ihminen väsyy jatkuviin hyväksyntäpyyntöihin eikä ehdi keskittyä tärkeimpiin päätöksiin. Siksi sinun täytyy **valita strategisesti**, mitkä päätökset ovat niin kriittisiä, että ne vaativat ihmisen hyväksynnän.

Kolme sääntöä auttaa päättämään, milloin ihminen tarvitaan mukaan.

**Sääntö 1: Raha tai rakenne.** Jos päätös liittyy rahaan, se vaatii usein hyväksynnän. Tällaisia päätöksiä ovat esimerkiksi alennus, hyvitys, palkkio tai maksun muuttaminen. Pienen 10 % alennuksen agentti voi ehkä antaa itse, jos se on etukäteen sallittu. Sen sijaan 50 % alennus vaatii yleensä esihenkilön hyväksynnän, koska sillä on suuri taloudellinen vaikutus. Sama koskee rakenteellisia muutoksia: jos päätös muuttaa asiakkaan tietoja, sopimusta, tilausta tai tulevaa asiakassuhdetta, hyväksyntä on usein tarpeen.

**Sääntö 2: Epävarmuus.** Jos agentti ei ole riittävän varma päätöksestään, se tarvitsee ihmisen vahvistuksen. Esimerkiksi jos agentti arvioi olevansa vain 65 % varma siitä, että viesti koskee laskua, ihmisen kannattaa tarkistaa tapaus. Ihminen voi nähdä sävyjä, poikkeuksia ja kontekstia, joita agentti ei välttämättä huomaa.

**Sääntö 3: Poikkeamat.** Jos tilanne ei ole rutiinitapaus, vaan siinä on jotain tavallisesta poikkeavaa, päätös kannattaa ohjata ihmiselle. Tavallisen tilauksen agentti voi käsitellä yksin. Jos tilauksessa on negatiivinen hinta, poikkeuksellisen suuri summa, uusi maksutapa tai muu epätavallinen piirre, agentin täytyy pysäyttää prosessi ja pyytää hyväksyntä.

Näiden sääntöjen avulla voit jakaa päätökset eri ryhmiin. Rutiinipäätökset agentti voi tehdä itsenäisesti. Kriittiset päätökset vaativat ihmisen hyväksynnän ennen toimintaa. Osa päätöksistä voi vaatia hyväksynnän vain silloin, kun agentti on epävarma, ja osa voidaan tarkistaa jälkikäteen lokien perusteella.

> **Pysähdy hetkeksi:** Ajattele omaa työtäsi tai opintojasi. Mitä päätöksiä tekisit itse, ja mitkä veisit opettajalle, esihenkilölle tai toiselle asiantuntijalle? Mitkä päätökset liittyvät rahaan, rakenteeseen, epävarmuuteen tai poikkeamiin?

## Hyväksyntäporttien rakentaminen

Kun tiedät, mitkä päätökset vaativat ihmisen hyväksynnän, seuraava askel on **hyväksyntäporttien** suunnittelu. Hyväksyntäportti on työnkulun kohta, jossa agentti pysähtyy ja odottaa ihmisen vastausta ennen kuin se jatkaa.

<figure class="ai-demo"><span class="ai-demo__tag">// rutiini kulkee läpi — kriittinen pysähtyy: ihminen hyväksyy tai hylkää</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:320px">
  <div class="l25-wrap">
    <div class="l25-human">IHMINEN<span class="l25-btns"><i class="l25-ok">HYVÄKSY</i><i class="l25-no">HYLKÄÄ</i></span></div>
    <i class="l25-beam l25-bm1"></i><i class="l25-beam l25-bm2"></i>
    <div class="l25-pipe"></div>
    <div class="l25-node" style="left:0">AGENTTI</div>
    <div class="l25-gatebox"><div class="l25-gate"></div><span class="l25-glbl g-open">portti auki</span><span class="l25-glbl g-stop">vaatii ihmisen</span></div>
    <div class="l25-node" style="right:0">TOIMINTO</div>
    <div class="l25-pkt k1">rutiinivastaus</div>
    <div class="l25-pkt k2">50 % alennus · 5 000 €</div>
    <div class="l25-pkt k3">70 % alennus!?</div>
    <span class="l25-done d1">✓ suoritettu</span>
    <span class="l25-done d2">✓ suoritettu — ihmisen luvalla</span>
    <span class="l25-alt">✗ hylätty → agentti tarjoaa vaihtoehdon: 10 % ja ilmainen toimitus</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Agentti hoitaa rutiinit itse, mutta kriittinen päätös pysähtyy hyväksyntäportille. Ihminen näkee ehdotuksen ja perustelut: hyväksyntä avaa portin, hylkäys ohjaa agentin vaihtoehtoiselle polulle — se ei jää jumiin eikä riko sääntöä.</figcaption></figure>
<style>
.l25-wrap{position:relative;width:560px;height:282px;font-family:var(--font-mono)}
.l25-pipe{position:absolute;left:0;right:0;top:158px;height:3px;background:#2B3552}
.l25-node{position:absolute;top:138px;width:110px;text-align:center;font-size:11.5px;letter-spacing:.1em;color:#EAEEF8;background:#11182A;border:2px solid oklch(0.66 0.13 208);border-radius:11px;padding:13px 6px}
.l25-gatebox{position:absolute;left:248px;top:120px;width:64px;height:80px}
.l25-gate{position:absolute;left:26px;top:0;width:12px;height:80px;border-radius:6px;background:#7FD0A8;animation:l25gate 21s infinite}
@keyframes l25gate{0%,20%{background:#7FD0A8;transform:scaleY(.24);transform-origin:top}24%,50%{background:#F0A38C;transform:scaleY(1);transform-origin:top}54%,62%{background:#7FD0A8;transform:scaleY(.24);transform-origin:top}66%,97%{background:#F0A38C;transform:scaleY(1);transform-origin:top}100%{background:#7FD0A8;transform:scaleY(.24);transform-origin:top}}
.l25-glbl{position:absolute;left:50%;transform:translateX(-50%);top:88px;font-size:10px;letter-spacing:.06em;text-transform:uppercase;white-space:nowrap;border-radius:999px;padding:1px 8px}
.l25-glbl.g-open{color:#06241a;background:#7FD0A8;animation:l25go 21s infinite}
.l25-glbl.g-stop{color:#3A1408;background:#F0A38C;opacity:0;animation:l25gs 21s infinite}
@keyframes l25go{0%,20%{opacity:1}24%,50%{opacity:0}54%,62%{opacity:1}66%,97%{opacity:0}100%{opacity:1}}
@keyframes l25gs{0%,20%{opacity:0}24%,50%{opacity:1}54%,62%{opacity:0}66%,97%{opacity:1}100%{opacity:0}}
.l25-pkt{position:absolute;top:128px;left:104px;font-size:10.5px;font-weight:500;white-space:nowrap;color:#06212A;background:#46c7cf;border-radius:999px;padding:3px 9px;opacity:0}
.l25-pkt.k1{animation:l25k1 21s infinite}
.l25-pkt.k2{animation:l25k2 21s infinite;background:#F7C873}
.l25-pkt.k3{animation:l25k3 21s infinite;background:#F0A38C}
@keyframes l25k1{0%,1%{opacity:0;transform:translate(0,0)}4%{opacity:1}9%{opacity:1;transform:translate(170px,0)}15%{opacity:1;transform:translate(330px,0)}18%,100%{opacity:0;transform:translate(330px,0)}}
@keyframes l25k2{0%,23%{opacity:0;transform:translate(0,0)}26%{opacity:1}31%,49%{opacity:1;transform:translate(128px,0)}55%{opacity:1;transform:translate(330px,0)}59%,100%{opacity:0;transform:translate(330px,0)}}
@keyframes l25k3{0%,65%{opacity:0;transform:translate(0,0)}68%{opacity:1}72%,84%{opacity:1;transform:translate(128px,0)}90%,94%{opacity:1;transform:translate(128px,72px)}97%,100%{opacity:0;transform:translate(128px,72px)}}
.l25-human{position:absolute;left:204px;top:6px;width:152px;text-align:center;font-size:11px;letter-spacing:.1em;color:#EAEEF8;background:#141B2D;border:1.5px solid #44517A;border-radius:11px;padding:9px 8px;opacity:0;animation:l25hum 21s infinite}
@keyframes l25hum{0%,26%{opacity:0;transform:translateY(-8px)}31%,52%{opacity:1;transform:translateY(0)}56%,68%{opacity:0}73%,90%{opacity:1;transform:translateY(0)}94%,100%{opacity:0}}
.l25-btns{display:flex;gap:7px;justify-content:center;margin-top:7px}
.l25-btns i{font-style:normal;font-size:10px;letter-spacing:.05em;border-radius:7px;padding:3px 8px}
.l25-ok{color:#06241a;background:#7FD0A8;animation:l25okp 21s infinite}
.l25-no{color:#3A1408;background:#F0A38C;animation:l25nop 21s infinite}
@keyframes l25okp{0%,42%{box-shadow:none;transform:scale(1)}45%,49%{box-shadow:0 0 14px rgba(127,208,168,.9);transform:scale(1.12)}52%,100%{box-shadow:none;transform:scale(1)}}
@keyframes l25nop{0%,80%{box-shadow:none;transform:scale(1)}83%,87%{box-shadow:0 0 14px rgba(240,163,140,.9);transform:scale(1.12)}90%,100%{box-shadow:none;transform:scale(1)}}
.l25-beam{position:absolute;left:279px;top:58px;width:2px;height:60px;opacity:0}
.l25-bm1{background:linear-gradient(180deg,#7FD0A8,transparent);animation:l25bm1 21s infinite}
.l25-bm2{background:linear-gradient(180deg,#F0A38C,transparent);animation:l25bm2 21s infinite}
@keyframes l25bm1{0%,46%{opacity:0}49%,54%{opacity:1}58%,100%{opacity:0}}
@keyframes l25bm2{0%,84%{opacity:0}87%,92%{opacity:1}96%,100%{opacity:0}}
.l25-done{position:absolute;right:0;top:196px;font-size:10.5px;letter-spacing:.05em;color:#7FD0A8;opacity:0}
.l25-done.d1{animation:l25d1 21s infinite}
.l25-done.d2{animation:l25d2 21s infinite}
@keyframes l25d1{0%,14%{opacity:0}17%,22%{opacity:1}26%,100%{opacity:0}}
@keyframes l25d2{0%,55%{opacity:0}58%,64%{opacity:1}68%,100%{opacity:0}}
.l25-alt{position:absolute;left:104px;top:236px;font-size:10.5px;letter-spacing:.02em;color:#F0A38C;opacity:0;animation:l25alt 21s infinite}
@keyframes l25alt{0%,88%{opacity:0}92%,98%{opacity:1}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l25-gate,.l25-glbl,.l25-pkt,.l25-human,.l25-ok,.l25-no,.l25-beam,.l25-done,.l25-alt{animation:none}
.l25-gate{background:#F0A38C;transform:scaleY(1)}
.l25-glbl.g-open{opacity:0}.l25-glbl.g-stop{opacity:1}
.l25-pkt.k3{opacity:1;transform:translate(128px,72px)}
.l25-human,.l25-alt{opacity:1}}
</style>

Käytännössä hyväksyntäportti näyttää ihmiselle **selkeän kysymyksen ja ehdotuksen**, johon voi vastata esimerkiksi ”hyväksy”, ”hylkää” tai ”kysy lisää”.

**HYVÄKSYNTÄPYYNTÖ**

**Asiakas:** John Smith

**Pyyntö:** 50 % alennus. Tavallinen hinta on 100 €, ehdotettu hinta 50 €.

**Perustelu:** Asiakas on lojaali ja tehnyt 5 ostoa. Kilpailija tarjosi halvempaa hintaa.

**Päätös vaaditaan:** myyntipäällikkö

**Vaihtoehdot:** [HYVÄKSY] [HYLKÄÄ] [KYSY LISÄÄ]

Hyväksyntäportin täytyy olla **selkeä ja nopea käyttää**. Ihmisen pitää nähdä yhdellä silmäyksellä seuraavat asiat:

- **Mitä päätöstä pyydetään?** Esimerkiksi 50 % alennus.
- **Kenelle päätös koskee?** Esimerkiksi asiakkaalle John Smith.
- **Miksi agentti ehdottaa tätä?** Esimerkiksi lojaalisuus, kilpailijan tarjous tai asiakashistoria.
- **Kenen täytyy hyväksyä päätös?** Esimerkiksi myyntipäällikön.
- **Mitä tapahtuu, jos päätös hylätään?** Esimerkiksi agentti tarjoaa asiakkaalle vaihtoehtoisen ratkaisun tai ilmoittaa, ettei alennusta voida antaa.

Hyväksyntäportin jälkeinen toiminta on tärkeä suunnitella etukäteen. Jos ihminen hyväksyy ehdotuksen, agentti jatkaa suunniteltua polkua. Jos ihminen hylkää sen, agentin pitää tietää, mitä seuraavaksi tehdään. Se voi esimerkiksi tarjota asiakkaalle pienemmän alennuksen, ilmaisen toimituksen tai selittää kohteliaasti, miksi pyyntöä ei voida hyväksyä. Agentti ei saa vain jäädä jumiin.

Hyväksyntäportteihin liittyy myös **aikaraja**. Mitä tapahtuu, jos ihminen ei vastaa 24 tunnin kuluessa? Vaihtoehtoja on useita:

- **Oletusarvo:** Jos vastausta ei tule, järjestelmä toimii ennalta sovitulla tavalla. Tämä voi tarkoittaa hyväksyntää tai hylkäystä, mutta sitä pitää käyttää varoen.
- **Eskalointi:** Pyyntö lähetetään toiselle hyväksyjälle, esimerkiksi esihenkilölle tai varahenkilölle.
- **Aikaraja:** Agentti peruuttaa pyynnön ja ilmoittaa asiakkaalle, että prosessi ei voi jatkua juuri nyt.

Valinta riippuu siitä, kuinka paljon odottaminen maksaa ja kuinka suuri riski väärällä päätöksellä on. Jos asiakas odottaa liian kauan vastausta, hän voi siirtyä kilpailijalle. Silloin eskalointi voi olla hyvä ratkaisu. Jos päätös on hyvin kriittinen, esimerkiksi miljoonan euron sopimus, automaattinen hyväksyntä olisi liian vaarallinen. Silloin aikaraja tai ihmisen pakollinen hyväksyntä on turvallisempi vaihtoehto.

## Hyväksyntäportit käytännössä: kolme esimerkkiä

Seuraavat esimerkit näyttävät, miten hyväksyntäportin laajuus ja nopeusvaatimus vaihtelevat päätöksen mukaan.

**Esimerkki 1: Pieni päätös — nopea hyväksyntä**

Agentti huomaa, että asiakas haluaa vaihtaa tuotteen värin. Uusi väri on varastossa, eikä vaihto vaikuta hintaan.

- **Portti näyttää:** ”Vaihdetaanko keltainen tuote punaiseen?”
- **Hyväksyjä:** asiakaspalvelupäällikkö.
- **Vastausaika:** päätös voidaan tehdä nopeasti työpäivän aikana.
- **Oletusarvo:** jos vastausta ei tule tunnissa, vaihto voidaan hyväksyä automaattisesti, jos riski on pieni ja asiakaskokemus kärsisi odottamisesta.

**Esimerkki 2: Suuri päätös — perusteellinen hyväksyntä**

Agentti ehdottaa asiakkaalle 50 % alennusta pitkästä sopimuksesta. Päätös vaikuttaa merkittävästi myyntikatteeseen.

- **Portti näyttää:** asiakkaan historian, kilpailijan tarjouksen, tuotteen katteen ja ehdotetun alennuksen prosentteina.
- **Hyväksyjä:** myyntipäällikkö.
- **Vastausaika:** hyväksyjä tarkistaa tiedot ennen päätöstä.
- **Oletusarvo:** jos vastausta ei tule 4 tunnissa, agentti lähettää asiakkaalle viestin: ”Tarjousta arvioidaan tiimissämme. Palaamme sinulle pian.”

**Esimerkki 3: Vakava päätös — monivaiheinen hyväksyntä**

Uusi liikekumppani haluaa integroitua yrityksen tietokantaan. Päätökseen liittyy sekä tietoturvariskejä että liiketoiminnallisia vaikutuksia.

- **Portti näyttää:** tietoturva-analyysin, integraation riskit ja liiketoimintahyödyt.
- **Hyväksyjät:** ensin tekninen johtaja ja sen jälkeen liiketoimintajohtaja.
- **Vastausaika:** päätös tehdään vasta molempien hyväksyntöjen jälkeen.
- **Oletusarvo:** jos jompikumpi hylkää pyynnön, prosessi pysähtyy ja agentti ilmoittaa integraatiokumppanille, ettei prosessia voida jatkaa tällä hetkellä.

Näissä esimerkeissä hyväksyntäportin **laajuus**, **hyväksyjien määrä** ja **aikaraja** muuttuvat päätöksen riskin mukaan. Pienet päätökset voivat olla nopeita. Suuret päätökset vaativat tarkempaa arviointia. Vakavat päätökset voivat tarvita useita hyväksyntäkerroksia.

## Työnkulut, joissa agentti ja ihminen tekevät yhteistyötä

Hyväksyntäportit ovat vain yksi osa ihmisen osallistava työnkulkua. Kokonaisuus on **työnkulku, jossa agentti ja ihminen tekevät yhteistyötä**. Agentti tekee sitä, missä se on hyvä: nopeaa analyysiä, tiedonhakua, toistuvia vaiheita ja yksinkertaisia päätöksiä. Ihminen tekee sitä, missä ihminen on vahva: kriittisiä päätöksiä, empatiaa, tilannearviointia ja poikkeusten käsittelyä.

Kuvittele asiakaspalvelun työnkulku:

1. **Syöte:** Asiakas lähettää viestin: ”Haluan palauttaa tuotteen.”
2. **Agentin analyysi:** Agentti lukee viestin, hakee asiakkaan tilauksen historiasta ja huomaa, että tilaus tehtiin 5 päivää sitten. Palautusaika on 14 päivää, joten asiakas on oikeutettu palautukseen.
3. **Hyväksyntäportti 1:** Agentti näyttää perustelut ihmiselle ja kysyy: ”Onko palautusaika voimassa?” Ihminen vahvistaa: ”Kyllä.”
4. **Agentin toiminta:** Agentti lähettää asiakkaalle palautuslomakkeen, kuljetusohjeet ja palautusehdot.
5. **Hyväksyntäportti 2:** Agentti huomaa, että asiakas on lojaali ja tehnyt 5 ostoa. Se ehdottaa 10 % alennusta seuraavaan tilaukseen. Ihminen hyväksyy ehdotuksen.
6. **Agentin lopetus:** Agentti lähettää asiakkaalle jatkoviestin: ”Pahoittelemme, että palautus oli tarpeellinen. Tässä on 10 % alennus seuraavaan tilaukseesi.”

Koko prosessi on hybridi. Agentti tekee rutiinianalyysin ja toteuttaa toimenpiteet. Ihminen tekee ne päätökset, joissa tarvitaan harkintaa, vastuuta tai asiakassuhteen ymmärtämistä. Näin saadaan sekä nopeutta että laatua.

> **Pysähdy hetkeksi:** Ajattele omaa tulevaa työtäsi. Mikä prosessi voitaisiin automatisoida agentin avulla, mutta vaatisi ihmisen hyväksynnän kriittisissä vaiheissa? Missä kohdissa ihminen täytyy ottaa mukaan?

## Agentin oppiminen ihmisen palautteesta

Ihmisen osallistuminen päätöksentekoon ei tarkoita vain sitä, että ihminen hyväksyy tai hylkää päätöksiä. Se tarkoittaa myös sitä, että **agentti voi oppia ihmisen palautteesta**. Kun ihminen hylkää agentin ehdotuksen, agentti voi tallentaa hylkäyksen syyn. Kun ihminen hyväksyy ehdotuksen, agentti voi tallentaa, millainen ehdotus hyväksyttiin ja miksi.

Esimerkiksi agentti tekee alennusehdotuksia. Yksi myyntipäällikkö hyväksyy usein 40 % alennuksia, kun taas toinen hyväksyy yleensä vain 15 % alennuksia. Agentti voi oppia palautteesta, että hyväksyjien päätöstyylit eroavat toisistaan. Tämän perusteella se voi myöhemmin tehdä realistisempia ehdotuksia eri hyväksyjille.

Tämä oppiminen perustuu **lokiin ja palautteeseen**. Jokainen hyväksyntä ja hylkäys tallennetaan. Sen jälkeen agentti tai järjestelmän kehittäjä voi etsiä päätöksistä toistuvia kaavoja. Oppiminen ei kuitenkaan tapahdu turvallisesti itsestään. Sinun täytyy suunnitella, mitä palautteesta opitaan, mitä ei opita ja kuka valvoo oppimisen vaikutuksia.

**Vinkki:** Agentin ei kannata oppia kaikesta palautteesta automaattisesti. Jos ihminen teki poikkeuksellisen päätöksen kiireen tai erityistilanteen takia, sitä ei välttämättä pidä muuttaa yleiseksi säännöksi. Palautteen hyödyntäminen vaatii harkintaa ja seurantaa.

## Kohti n8n-projekteja — kaikki yhdistyy

Tämä on viimeinen teoriapainotteinen oppitunti ennen rakentamista. Seuraavaksi näet, miten kaikki aiemmat aiheet yhdistyvät n8n:ssä yhdeksi kokonaisuudeksi.

| Aihe | Mitä opit? | Miten se näkyy n8n:ssä? |
| --- | --- | --- |
| **Agentin rakenne** | Agentin kuusi komponenttia. | Jokainen komponentti toteutuu yhtenä tai useampana n8n-solmuna. |
| **Automaatio vs. autonomia** | Päätöspuu: promptaus, työnkulku vai agentti. | Valitset, riittääkö yksi AI Agent -solmu vai tarvitaanko monivaiheinen työnkulku. |
| **Muisti ja konteksti** | Konteksti-ikkuna, pitkäkestoinen muisti ja tila. | Memory-solmu, tietokanta, Google Sheets tai muu tilan tallennus. |
| **Työkalut** | Tiedostot, verkkohaku ja CLI-komennot. | Read File-, HTTP Request- ja Execute Command -solmut. |
| **Suunnittelumallit** | ReAct, ketjuajattelu ja moniagenttijärjestelmät. | AI Agent ReAct-malliin, solmuketju ketjuajatteluun ja webhook-kutsut moniagenttirakenteeseen. |
| **Turvallisuus** | Promptihyökkäys, hallusinaatiot, minimioikeus ja lokitus. | IF-solmut validointiin, rajatut API-avaimet, hyväksyntäportit ja lokisolmut. |
| **Ihmisen osallistuminen päätöksentekoon** | Hyväksyntäportit, palaute ja ihmisen rooli kriittisissä päätöksissä. | Hyväksyntäsolmu, Slack- tai Teams-ilmoitus, lomakevastaus ja lokitus. |

Kaikki, mitä olet oppinut, muuttuu n8n:ssä konkreettisiksi solmuiksi ja yhteyksiksi. Näet visuaalisesti, missä työnkulku käynnistyy, missä agentti hakee tietoa, missä se tekee päätöksen ja missä se pysähtyy odottamaan ihmisen hyväksyntää.

n8n:ssä voit rakentaa esimerkiksi:

- **hyväksyntäportteja**, jotka pysäyttävät työnkulun ennen kriittistä toimintoa
- **työnkulkuja**, joissa agentti ja ihminen tekevät yhteistyötä
- **palautteen tallennusta**, jossa jokainen hyväksyntä ja hylkäys kirjataan
- **lokitusta**, joka näyttää, mitä tapahtui ja miksi
- **virheenkäsittelyä**, jossa epäonnistunut toiminto voidaan korjata tai ohjata ihmiselle

Kun opit käyttämään n8n:ää, muista tämä: **jokainen solmu on vaihe agentin toiminnassa**. Hyväksyntäsolmu on kohta, jossa agentti pysähtyy ja odottaa ihmisen päätöstä. API-haku on vaihe, jossa agentti noutaa tietoa. IF-solmu on kohta, jossa työnkulku haarautuu päätöksen perusteella. Yhdessä nämä solmut muodostavat toimivan ja turvallisen agentin.

## Kohti omaa projektia

Tämä on viimeinen suunnitteluaskel ennen rakentamista. Sinulla on nyt koossa viisi **Agentti-pohjapiirrosta**:

- **Ongelma** — tunti 19
- **Muisti** — tunti 21
- **Päättely** — tunti 23
- **Turva** — tunti 24
- **Ihminen** — tämä tunti

Yhdessä nämä muodostavat suunnitelman, jonka pohjalta rakennat n8n-työnkulun oppitunneilla 26–27. Käy pohjapiirrokset vielä kerran läpi ennen rakentamista ja varmista, että ne muodostavat yhtenäisen kokonaisuuden. Tarkista erityisesti, missä kohdissa agentti saa toimia itsenäisesti ja missä kohdissa tarvitaan ihmisen hyväksyntä.

## Yhteenveto

**Ihmisen osallistuminen päätöksentekoon** ei tarkoita, että ihminen tekee kaiken. Se tarkoittaa, että ihminen hyväksyy suuret päätökset ja ohjaa agenttia epäselvissä tai riskialttiissa tilanteissa. Kolme sääntöä auttaa päättämään, milloin hyväksyntä tarvitaan: päätös liittyy **rahaan tai rakenteeseen**, agentti on **epävarma** tai tilanne on **poikkeava**.

**Hyväksyntäportit** tehdään selkeiksi ja nopeiksi, jotta ihminen voi vastata ilman, että koko prosessi pysähtyy tarpeettoman pitkäksi aikaa. Hyvässä hyväksyntäportissa näkyvät päätös, perustelut, riskit, hyväksyjä ja vaihtoehtoinen polku, jos pyyntö hylätään.

Koko prosessi on hybridi: agentti analysoi, hakee tietoa ja toteuttaa rutiinivaiheita, kun taas ihminen tekee kriittiset päätökset. Agentti voi myös oppia ihmisen palautteesta, kun hyväksynnät ja hylkäykset tallennetaan lokiin ja niitä käytetään toiminnan kehittämiseen.

Seuraavilla oppitunneilla rakennat nämä työnkulut konkreettisesti n8n:ssä. Vedät solmuja työtilaan, kytket hyväksyntäportteja ja näet, miten automaatio ja inhimillinen ohjaus toimivat yhdessä. Tavoitteena ei ole pelkästään nopea automaatio, vaan **älykäs, turvallinen ja hallittu agentti**.


---

## Lähteet ja tarkistuspäivä

- [NIST: Strengthening AI Agent Hijacking Evaluations](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations)
- [OWASP: Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
- [OWASP: Excessive Agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html)

Tarkistettu 15.7.2026.
