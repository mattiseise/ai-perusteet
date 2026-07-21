# Keneen tekoäly vaikuttaa? — etiikka, oikeudet ja vastuu

## Johdanto

Organisaatio ottaa käyttöön tekoälyjärjestelmän, joka auttaa seulomaan työnhakijoita. Järjestelmä nopeuttaa työtä, mutta sen koulutusdata kuvaa lähinnä aiempia työntekijöitä. Hakijat eivät tiedä, miten järjestelmää käytetään, eikä kukaan ole sopinut, kuka tarkistaa sen ehdotukset.

Tilanne ei ratkea kysymällä vain, toimiiko tekniikka. On kysyttävä myös, keitä data edustaa, keneen päätös vaikuttaa, mitä oikeuksia ihmisillä on ja kuka kantaa vastuun.

Tällä tunnilla saat arviointipöytääsi uuden näkökulman: **tekoäly ei ole neutraali väline**. Sen taustalla on dataa, ihmisten työtä, luonnonvaroja ja päätöksiä siitä, millainen virhe hyväksytään.

## Edustava data ei synny pelkästä määrästä

**Edustavuus** tarkoittaa sitä, että aineisto kuvaa riittävän hyvin niitä ihmisiä, tilanteita ja olosuhteita, joissa järjestelmää aiotaan käyttää. Suuri aineisto voi silti olla epäedustava. Jos rekrytointimalli oppii vain yhden alan aiemmista palkkauksista, se voi arvioida heikommin uudenlaisia hakijoita tai toistaa historian vinoumia.

**Algoritminen harha** syntyy, kun järjestelmän tulokset kohtelevat ryhmiä järjestelmällisesti eri tavoin. Syynä voi olla aineiston valinta, puuttuvat ryhmät, virheelliset merkinnät, huonosti valittu tavoite tai tapa, jolla järjestelmää käytetään. Malli ei tarvitse tietoa ihmisen etnisestä taustasta tuottaakseen eriarvoisia tuloksia: esimerkiksi asuinalue tai koulutushistoria voi toimia sen sijaismuuttujana.

Edustavuutta arvioitaessa kannattaa kysyä:

- Ketkä näkyvät aineistossa ja ketkä puuttuvat?
- Kuvaako aineisto nykyistä käyttötilannetta vai menneisyyttä?
- Onko tuloksia testattu eri ryhmillä ja poikkeavissa tilanteissa?
- Kuka voi ilmoittaa virheestä ja saada päätöksen uudelleen arvioitavaksi?

> **Pysähdy hetkeksi:** Millainen ihminen tai tilanne voisi jäädä oman alasi tavallisesta aineistosta näkymättömiin?

<figure class="ai-demo"><span class="ai-demo__tag">// yksi tekoälytulos — monta vaikutuskerrosta</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:320px">
  <div class="l08-layers" role="img" aria-label="Animaatio näyttää tekoälyjärjestelmän viisi tarkasteltavaa vaikutuskerrosta: data ja oikeudet, ihmisten työ, energia ja vesi, järjestelmän tulos sekä ihmiseen kohdistuva päätös.">
    <div class="l08-core">TEKOÄLYN<br/>TULOS</div>
    <div class="l08-layer a"><b>DATA JA OIKEUDET</b><span>Ketkä näkyvät aineistossa?</span></div>
    <div class="l08-layer b"><b>IHMISTEN TYÖ</b><span>Millaisissa oloissa työ tehtiin?</span></div>
    <div class="l08-layer c"><b>ENERGIA JA VESI</b><span>Mitä käyttö kuluttaa?</span></div>
    <div class="l08-layer d"><b>PÄÄTÖS JA VASTUU</b><span>Keneen tulos vaikuttaa?</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Tekoälytuloksen vaikutukset eivät rajoitu käyttöliittymään. Kaikissa järjestelmissä jokainen kerros ei ole yhtä merkittävä, mutta vastuullinen arvio tarkistaa datan ja oikeudet, työn, luonnonvarojen käytön sekä päätöksen vaikutukset ennen käyttöönottoa.</figcaption></figure>
<style>
.l08-layers{position:relative;width:560px;height:270px;font-family:var(--font-mono)}
.l08-core{position:absolute;left:218px;top:94px;width:124px;height:82px;border-radius:18px;background:#46c7cf;color:#06212A;font-size:12px;font-weight:800;line-height:1.45;display:flex;align-items:center;justify-content:center;text-align:center;z-index:2}
.l08-layer{position:absolute;width:210px;min-height:72px;border:2px solid #2B3552;border-radius:12px;background:#11182A;padding:11px 13px;opacity:.35;animation:l08pulse 12s infinite}
.l08-layer b{display:block;font-size:10px;letter-spacing:.08em;color:#EAEEF8;margin-bottom:6px}.l08-layer span{display:block;font-size:11px;line-height:1.4;color:#B9C2DA}
.l08-layer.a{left:0;top:8px}.l08-layer.b{right:0;top:8px;animation-delay:3s}.l08-layer.c{left:0;bottom:8px;animation-delay:6s}.l08-layer.d{right:0;bottom:8px;animation-delay:9s}
@keyframes l08pulse{0%,24%{opacity:.35;border-color:#2B3552;transform:scale(.98)}6%,18%{opacity:1;border-color:#46c7cf;transform:scale(1)}25%,100%{opacity:.35;border-color:#2B3552;transform:scale(.98)}}
@media (prefers-reduced-motion:reduce){.l08-layer{animation:none;opacity:1;transform:none}}
@media (max-width:680px){.l08-layers{width:100%;height:470px}.l08-core{left:calc(50% - 62px);top:194px}.l08-layer{left:0!important;right:0!important;width:100%}.l08-layer.a{top:0}.l08-layer.b{top:94px}.l08-layer.c{top:288px;bottom:auto}.l08-layer.d{top:382px;bottom:auto}.ai-demo__stage:has(.l08-layers){height:520px!important}}
</style>

## Tekijänoikeudet ja ihmisten työ

Generatiivisia malleja koulutetaan laajoilla teksti-, kuva- ja muilla aineistoilla. Aineistoon voi sisältyä tekijänoikeudella suojattuja teoksia. EU:ssa tekstin- ja tiedonlouhintaa koskevat omat säännöt, mutta kaikki käyttötavat eivät ratkea yhdellä yleissäännöllä. Käyttäjän kannattaa erottaa kaksi kysymystä: saako aineistoa käyttää, ja onko käyttö tekijää kohtaan reilua.

Tekoälyjärjestelmän taustalla on myös ihmistyötä. Datan merkitsijät luokittelevat aineistoa, arvioivat mallien vastauksia ja voivat joutua käsittelemään raskasta sisältöä. Vastuullinen hankinta tarkastelee hinnan ja teknisen laadun lisäksi työoloja, korvausta ja sitä, kuinka avoimesti palveluntarjoaja kertoo tuotantoketjustaan.

Kun julkaiset tekoälyn avulla tehdyn tuotoksen, vastuu ei siirry mallille. Tarkistat oikeudet, lähteet ja sen, ettei lopputulos johda harhaan tai kopioi tunnistettavasti toisen teosta.

## Käyttö kuluttaa energiaa ja vettä

Tekoälyn koulutus ja käyttö tapahtuvat datakeskuksissa. Ne tarvitsevat sähköä, laitteita ja jäähdytystä, joka voi kuluttaa vettä. Vaikutus riippuu muun muassa mallista, käyttömäärästä, sähköntuotannosta, jäähdytystavasta ja datakeskuksen sijainnista. Siksi yksittäisestä kyselystä esitetty yleisluku voi antaa liian varman kuvan.

Kansainvälinen energiajärjestö IEA arvioi datakeskusten kuluttaneen vuonna 2024 noin 415 terawattituntia sähköä maailmanlaajuisesti. Luku sisältää muutakin laskentaa kuin tekoälyn. Tekoäly on kuitenkin yksi kulutuksen kasvua lisäävistä tekijöistä.

Vastuullinen organisaatio arvioi hyödyn ja kulutuksen suhdetta. Turhia automaattisia kyselyitä voidaan vähentää, tehtävään voidaan valita riittävän pieni malli ja käyttöä voidaan seurata. Tavoite ei ole laskea jokaiselle promptille täydellistä jalanjälkeä, vaan tehdä kulutus näkyväksi päätöksenteossa.

## EU:n tekoälysäädös aloittelijalle

EU:n tekoälysäädös eli **AI Act** noudattaa riskiperusteista ajattelua. Mitä suurempi vaara järjestelmästä voi aiheutua ihmisten terveydelle, turvallisuudelle tai perusoikeuksille, sitä tiukemmat velvollisuudet siihen liittyvät. Osa käyttötavoista on kielletty, suuri osa arjen tekoälystä kuuluu kevyempien velvollisuuksien piiriin ja tietyt käyttötavat luokitellaan suuririskisiksi.

Esimerkiksi koulutuksessa pääsyä, opiskelupaikkojen jakamista tai oppimistulosten arviointia koskeva järjestelmä voi olla suuririskinen. Työelämässä sama voi koskea rekrytointia, hakijoiden suodattamista sekä työntekijöiden arviointia. Luokittelu riippuu järjestelmän käyttötarkoituksesta ja säädöksen ehdoista, joten pelkkä tuotteen nimi ei ratkaise asiaa.

Säädöksessä erotetaan muun muassa **tarjoaja** ja **käyttöönottaja**. Tarjoaja kehittää tekoälyjärjestelmän tai teettää sen ja saattaa järjestelmän markkinoille tai käyttöön omalla nimellään tai tavaramerkillään. Käyttöönottaja käyttää järjestelmää omassa toiminnassaan. Käyttöönottajan vastuulla voi olla esimerkiksi ohjeiden noudattaminen, ihmisen valvonnan järjestäminen, syötedatan asianmukaisuus ja toiminnan seuraaminen. Jos organisaatio muuttaa järjestelmää olennaisesti tai antaa sille oman nimensä, sen rooli ja velvollisuudet voivat muuttua.

Säädös sisältää myös läpinäkyvyyttä koskevia velvollisuuksia. Ihmiselle voidaan joutua kertomaan, että hän asioi tekoälyn kanssa tai että sisältö on tekoälyn tuottamaa tai muokkaamaa. Tekoälylukutaitoa koskeva velvoite kohdistuu tekoälyjärjestelmien tarjoajiin ja käyttöönottajiin: niiden on parhaansa mukaan huolehdittava henkilöstönsä ja puolestaan toimivien henkilöiden riittävästä **tekoälylukutaidosta**. Käytännössä osaamisen tason pitää vastata tehtävää, käyttötilannetta, käyttäjäryhmää ja järjestelmän riskejä.

Säädöstä sovelletaan vaiheittain, ja yksityiskohdat voivat täsmentyä. Tarkista ajantasainen tilanne Euroopan komission ja EUR-Lexin virallisista lähteistä. Tämä oppitunti antaa yleiskuvan, ei oikeudellista neuvontaa.

## Ihmiseen vaikuttava käyttö dokumentoidaan

Kun tekoäly osallistuu ihmisiä koskevaan päätökseen, vastuullinen käyttöönotto alkaa ennen ensimmäistä päätöstä. Organisaatio kuvaa käyttötarkoituksen, arvioi keihin järjestelmä vaikuttaa, testaa tuloksia eri ryhmillä ja nimeää vastuuhenkilöt. Lisäksi sovitaan, milloin ihminen puuttuu päätökseen ja miten päätöksen kohde voi pyytää oikaisua.

EU:n tekoälysäädös edellyttää tietyiltä julkisoikeudellisilta toimijoilta ja tietyiltä julkisia palveluja tarjoavilta käyttöönottajilta perusoikeusvaikutusten arviointia ennen suuririskisen järjestelmän käyttöä. Vaikka muodollinen velvollisuus ei koskisi omaa tilannetta, sama ajattelutapa on hyödyllinen: kirjaa ennakoitavat haitat, suojatoimet, valvonta ja jälkiseuranta.

Hyvä dokumentointi vastaa ainakin kysymyksiin: miksi järjestelmää käytetään, millä aineistolla sitä arvioitiin, millaisia virheitä sallitaan, kuka seuraa toimintaa ja miten käyttö voidaan keskeyttää. Ihmisen valvonta ei tarkoita kumileimasinta. Valvojalla pitää olla osaaminen, tieto ja valta poiketa järjestelmän ehdotuksesta.

> **Pysähdy hetkeksi:** Jos tekoäly suosittelee ihmistä koskevaa päätöstä, mitä valvojan pitäisi tietää ennen hyväksymistä?

## Valitse lähteet seuraavan tunnin lopputyöhön

Tunnin lopussa valitset jo yhden seuraavan tunnin skenaarioista: asiakaspalvelun tietovuodon, rekrytointialgoritmin ja AI Actin tai markkinointisisällön ja tekijänoikeudet. Arvioi skenaariota varten kaksi lähdettä. Hyvä lähdepari tukee vähintään kahta analyysin keskeistä väitettä eikä toista vain samaa yleiskuvausta kahdessa eri muodossa.

Kirjaa kummastakin lähteestä, kuka sen on julkaissut, mitä väitettä se tukee, miksi se on tähän tehtävään riittävän luotettava ja ajantasainen sekä mitä se ei ratkaise. Virallinen säädös tai viranomaislähde sopii oikeudellisen väitteen tarkistamiseen. Tutkimus tai asiantuntijaorganisaation aineisto voi täydentää sitä vaikutusten ja käytännön toimintatapojen arvioinnissa.

Tallenna lähdepari lähdekortiksi. Käytät sitä tunnilla 9. Jos jokin työn keskeinen väite jää näiden lähteiden jälkeen ilman tukea, saat tehdä tunnilla 9 enintään yhden uuden lähdetarkistuksen. Tarkoitus ei ole kerätä mahdollisimman paljon linkkejä, vaan valita rajattu aineisto, jonka sisältöä osaat käyttää ja jonka rajat tunnistat.

## Yhteenveto

Vastuullinen tekoälyn käyttö tarkastelee koko ketjua. Edustaako data todellista käyttötilannetta? Kohteleeko järjestelmä ryhmiä reilusti? Onko aineiston, ihmistyön ja luonnonvarojen käyttö perusteltua? Tietävätkö ihmiset, milloin tekoäly vaikuttaa heihin?

EU:n tekoälysäädös jakaa velvollisuuksia riskin ja toimijan roolin perusteella. Organisaation on tunnettava oma käyttötarkoituksensa, huolehdittava tekoälylukutaidosta ja järjestettävä todellinen ihmisen valvonta. Vastuu ei kuulu abstraktille ”tekoälylle”, vaan ihmisille ja organisaatioille, jotka rakentavat, tarjoavat ja käyttävät järjestelmää.

---

## Lähteet ja tarkistuspäivä

- [EUR-Lex: Euroopan parlamentin ja neuvoston asetus (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [Euroopan komissio: AI Act — regulatory framework for artificial intelligence](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Euroopan komissio: AI literacy — questions and answers](https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers)
- [Euroopan komissio: GDPR:n henkilötietojen käsittelyn periaatteet](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr/overview-principles/what-data-can-we-process-and-under-which-conditions_en)
- [Euroopan komissio: Copyright and new technologies](https://digital-strategy.ec.europa.eu/en/library/study-copyright-and-new-technologies)
- [International Energy Agency: Energy and AI](https://www.iea.org/reports/energy-and-ai)
- [UNESCO: Recommendation on the Ethics of Artificial Intelligence](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence)

Tarkistettu 21.7.2026.
