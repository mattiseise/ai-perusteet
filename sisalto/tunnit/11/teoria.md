# Minne aineistosi menee? — pilvipalvelu, paikallinen ajo ja tietosuoja

## Johdanto: toimiva työkalu ei vielä ole sallittu työkalu

Tunnilla 10 vertailit, miten eri tekoälytyökalut suoriutuvat tehtävästä. Nyt kysymys vaihtuu. Enää ei riitä, että työkalu tuottaa hyvän vastauksen. Sinun pitää myös tietää, **mitä aineistolle tapahtuu käytön aikana**.

Kun kirjoitat promptin, liität asiakirjan tai annat työkalulle kuvan, aineisto voi poistua laitteeltasi. Se voidaan käsitellä palveluntarjoajan ympäristössä, säilyttää jonkin aikaa tai käyttää palvelun kehittämiseen. Käytäntö riippuu palvelusta, käyttöehdoista, asetuksista ja mahdollisesta organisaation sopimuksesta.

> **Tämän tunnin tavoite:** Opit seuraamaan aineiston datavirtaa, tunnistamaan käsiteltävän tiedon luonteen ja tekemään perustellun käyttöpäätöksen.

Tunnin lopussa et siis nimeä ”parasta mallia”. Osaat sanoa: **käytä**, **käytä näillä rajoituksilla** tai **älä käytä tähän aineistoon** — ja perustella päätöksesi.

## 1. Erota malli, palvelu ja käyttöympäristö

Tekoälystä puhuttaessa kolme eri asiaa sekoittuu helposti.

### Kielimalli

**Kielimalli** tuottaa tekstiä, koodia tai muuta sisältöä saamansa syötteen perusteella. Malli on järjestelmän laskennallinen osa, ei koko käyttäjälle näkyvä palvelu.

### Tekoälypalvelu

**Tekoälypalvelu** on käyttöliittymä tai ohjelmointirajapinta, jonka kautta mallia käytetään. Palvelu määrittää esimerkiksi kirjautumisen, tiedostojen käsittelyn, keskusteluhistorian, käyttöehdot ja tietosuoja-asetukset.

### Käyttöympäristö

**Käyttöympäristö** kertoo, missä palvelu tai malli toimii. Se voi olla palveluntarjoajan pilvi, organisaation hallitsema ympäristö tai käyttäjän oma laite.

Erottelu on tärkeä, koska palvelun nimi ei yksin kerro, mitä aineistolle tapahtuu. Sama malliperhe voidaan tarjota eri palveluissa ja eri ehdoilla. Palvelu voi myös vaihtaa taustalla käyttämäänsä mallia. Siksi käyttöpäätös tehdään koko toteutuksesta, ei pelkän mallin nimen perusteella.

## 2. Seuraa aineiston datavirtaa

**Datavirta** kuvaa, mistä aineisto lähtee, minkä järjestelmien kautta se kulkee ja mitä sille tapahtuu matkalla. Tekoälypalvelun datavirtaa voi selvittää viidellä kysymyksellä:

1. **Mitä lähetän?** Promptin, tiedoston, kuvan, äänitteen vai tietokannan tietoja?
2. **Poistuuko aineisto laitteeltani?** Lähetetäänkö se verkon kautta ulkopuoliseen palveluun?
3. **Kuka käsittelee aineistoa?** Palveluntarjoaja, sen alihankkija vai oma organisaatio?
4. **Säilytetäänkö tai käytetäänkö aineistoa myöhemmin?** Tallentuuko historia, voiko ihminen tarkastaa sisältöä tai käytetäänkö sitä palvelun kehittämiseen?
5. **Mihin muihin järjestelmiin palvelu on yhteydessä?** Voiko aineisto siirtyä esimerkiksi hakupalveluun, tiedostovarastoon tai toiseen rajapintaan?

<figure class="ai-demo"><span class="ai-demo__tag">// sama tiedosto — kolme reittiä, ja mitä kustakin jää jäljelle</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:312px">
  <div class="l11-wrap" role="img" aria-label="Sama tiedosto kulkee kolme reittiä. Pilvipalveluun lähetetty kopio ylittää verkon rajan, ja vastauksen palattua palveluun voi jäädä kopio — tarkista ehdot. Organisaation palveluun lähetetty kopio ylittää myös rajan, mutta sopimus määrittää käsittelyn. Paikallinen ajo ei ylitä verkon rajaa, mutta silti on tarkistettava yhteydet ja päivitykset. Päätös luetaan reitistä, ei työkalun nimestä.">
    <div class="l11-dev"><i class="l11-ph">SINUN LAITTEESI</i>
      <span class="l11-file">palaute.txt</span>
      <div class="l11-loc"><i class="l11-ph phl">PAIKALLINEN AJO</i>
        <span class="l11-ll">ei ylitä verkon rajaa</span>
        <span class="l11-lw">silti: yhteydet, päivitykset?</span></div></div>
    <i class="l11-bnd"></i><i class="l11-bfl f1"></i><i class="l11-bfl f2"></i>
    <span class="l11-bl">verkon raja</span>
    <div class="l11-tp t1"><i class="l11-ph phc">YLEINEN PILVIPALVELU</i>
      <span class="l11-gh g1">palaute.txt</span>
      <span class="l11-tl w1">kopio voi säilyä?</span>
      <em class="l11-tb b1">» tarkista ehdot ja asetukset</em></div>
    <div class="l11-tp t2"><i class="l11-ph pho">ORGANISAATION PALVELU</i>
      <span class="l11-gh g2">palaute.txt</span>
      <span class="l11-tl w2">hallittu ympäristö</span>
      <em class="l11-tb b2">» sopimus ja ohjeet määrittävät</em></div>
    <span class="l11-mv m1">palaute.txt</span>
    <span class="l11-mv m2">palaute.txt</span>
    <span class="l11-mv m3">palaute.txt</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Käyttöpäätös luetaan aineiston reitistä: ylittääkö tiedosto verkon rajan ja mitä siitä jää käsittely-ympäristöön. Pilvessä kopio voi säilyä vastauksen jälkeenkin, organisaation palvelussa sopimus määrittää — eikä paikallinenkaan ajo ole automaattisesti turvallinen. Vie hiiri kuvan päälle pysäyttääksesi.</figcaption></figure>
<style>
.l11-wrap{position:relative;width:560px;height:296px;font-family:var(--font-mono);animation:l11w 21s infinite}
.l11-wrap:hover,.l11-wrap:hover *{animation-play-state:paused}
.l11-ph{display:block;font-style:normal;font-size:10.5px;font-weight:700;letter-spacing:.08em;color:#EAEEF8}
.l11-ph.phl{color:#7FD0A8}.l11-ph.phc{color:#FFD79A}.l11-ph.pho{color:#C9B7F1}
.l11-dev{position:absolute;left:2px;top:8px;width:206px;height:280px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:9px 11px}
.l11-file{display:inline-block;margin-top:8px;font-size:11px;color:#06212A;background:#46C7CF;border-radius:7px;padding:4px 9px;animation:l11file 21s infinite}
.l11-loc{position:absolute;left:10px;bottom:10px;width:184px;height:118px;box-sizing:border-box;border:1.5px solid #7FD0A8;border-radius:10px;padding:8px 9px;background:#0E1524}
.l11-ll{display:block;margin-top:9px;font-size:10.5px;line-height:1.3;color:#7FD0A8;opacity:0;animation:l11ll 21s infinite}
.l11-lw{display:block;margin-top:7px;font-size:10.5px;line-height:1.3;color:#FFD79A;opacity:0;animation:l11lw 21s infinite}
.l11-bnd{position:absolute;left:236px;top:8px;height:280px;width:0;border-left:2px dashed #7E88A8}
.l11-bfl{position:absolute;left:230px;top:8px;height:280px;width:12px;background:radial-gradient(50% 50% at 50% 50%,rgba(255,215,154,.5),transparent);opacity:0}
.l11-bfl.f1{animation:l11f1 21s infinite}
.l11-bfl.f2{animation:l11f2 21s infinite}
.l11-bl{position:absolute;left:180px;top:290px;width:112px;text-align:center;font-size:10px;color:#B9C2DA}
.l11-tp{position:absolute;left:262px;width:296px;height:132px;box-sizing:border-box;background:#11182A;border-radius:12px;padding:9px 11px}
.l11-tp.t1{top:8px;border:1.5px solid rgba(255,215,154,.55)}
.l11-tp.t2{top:156px;border:1.5px solid rgba(201,183,241,.55)}
.l11-gh{display:inline-block;margin-top:7px;font-size:11px;color:#46C7CF;border:1.5px dashed #46C7CF;border-radius:7px;padding:3px 8px;opacity:0}
.l11-gh.g1{animation:l11g1 21s infinite}
.l11-gh.g2{animation:l11g2 21s infinite}
.l11-tl{display:block;margin-top:7px;font-size:10.5px;line-height:1.25;opacity:0}
.l11-tl.w1{color:#FFD79A;animation:l11w1 21s infinite}
.l11-tl.w2{color:#C9B7F1;animation:l11w2 21s infinite}
.l11-tb{display:block;margin-top:5px;font-style:normal;font-size:10.5px;line-height:1.25;color:#B9C2DA;opacity:0}
.l11-tb.b1{animation:l11b1 21s infinite}
.l11-tb.b2{animation:l11b2 21s infinite}
.l11-mv{position:absolute;left:24px;top:36px;font-size:11px;color:#06212A;background:#46C7CF;border-radius:7px;padding:4px 9px;opacity:0;white-space:nowrap}
.l11-mv.m1{animation:l11m1 21s infinite}
.l11-mv.m2{animation:l11m2 21s infinite}
.l11-mv.m3{animation:l11m3 21s infinite}
@keyframes l11w{0%{opacity:0}3%{opacity:1}97%{opacity:1}100%{opacity:0}}
@keyframes l11file{0%,2%{transform:scale(1)}4%{transform:scale(1.12)}6%,100%{transform:scale(1)}}
@keyframes l11m1{0%,6%{opacity:0;transform:translate(0,0)}8%{opacity:1}19%{opacity:1;transform:translate(258px,10px)}24%,100%{opacity:0;transform:translate(258px,10px)}}
@keyframes l11g1{0%,21%{opacity:0}26%,100%{opacity:.5}}
@keyframes l11w1{0%,26%{opacity:0}30%,100%{opacity:1}}
@keyframes l11b1{0%,30%{opacity:0}34%,100%{opacity:1}}
@keyframes l11f1{0%,10%{opacity:0}13%{opacity:1}18%,100%{opacity:0}}
@keyframes l11m2{0%,38%{opacity:0;transform:translate(0,0)}40%{opacity:1}51%{opacity:1;transform:translate(258px,158px)}56%,100%{opacity:0;transform:translate(258px,158px)}}
@keyframes l11g2{0%,53%{opacity:0}58%,100%{opacity:.5}}
@keyframes l11w2{0%,58%{opacity:0}62%,100%{opacity:1}}
@keyframes l11b2{0%,62%{opacity:0}66%,100%{opacity:1}}
@keyframes l11f2{0%,42%{opacity:0}45%{opacity:1}50%,100%{opacity:0}}
@keyframes l11m3{0%,70%{opacity:0;transform:translate(0,0)}72%{opacity:1}80%{opacity:1;transform:translate(4px,120px)}84%,100%{opacity:0;transform:translate(4px,120px)}}
@keyframes l11ll{0%,80%{opacity:0}84%,100%{opacity:1}}
@keyframes l11lw{0%,86%{opacity:0}90%,100%{opacity:1}}
@media (prefers-reduced-motion:reduce){
  .l11-wrap,.l11-wrap *{animation:none!important}
  .l11-wrap,.l11-tl,.l11-tb,.l11-ll,.l11-lw{opacity:1}
  .l11-gh{opacity:.5}
  .l11-mv{opacity:0}
}
</style>

Jos jokin datavirran kohta on epäselvä, sitä ei pidä arvata. Merkitse se **selvitettäväksi asiaksi** ja tarkista palvelun ehdot, tietosuoja-asetukset sekä organisaation ohjeet.

## 3. Tunnista aineiston luonne

Sama palvelu voi sopia yhteen tehtävään mutta olla väärä valinta toiseen. Ratkaiseva ero on usein aineistossa.

| Aineiston luonne | Esimerkki | Ensimmäinen toimintatapa |
| --- | --- | --- |
| **Julkinen tai kuvitteellinen** | Julkaistu verkkoteksti tai itse keksitty harjoitustapaus | Pilvipalvelu voi sopia, kun ehdot ja käyttötarkoitus ovat kunnossa. |
| **Organisaation sisäinen** | Keskeneräinen suunnitelma, sisäinen muistio tai julkaisematon tuoteidea | Tarkista organisaation ohje ja käytä vain tehtävään hyväksyttyä palvelua. |
| **Henkilötieto** | Nimi, sähköpostiosoite, asiakasnumero tai tunnistettava palaute | Selvitä käsittelyperuste ja hyväksytty ympäristö. Poista tarpeettomat tunnistetiedot. |
| **Salassa pidettävä tai erityistä suojaa vaativa tieto** | Potilastieto, oppilashuollon tieto, salasana tai liikesalaisuus | Älä syötä yleiseen tekoälypalveluun. Noudata organisaation päätöksiä ja lakisääteisiä velvoitteita. |

Tietosuojan perusajatus on **tietojen minimointi**: käytä vain sitä aineistoa, joka on tehtävän kannalta välttämätöntä. Nimen poistaminen ei aina riitä, jos henkilö voidaan tunnistaa muista yksityiskohdista.

## 4. Kolme käyttöympäristöä

### Yleinen pilvipalvelu

Yleinen pilvipalvelu on helppo ottaa käyttöön. Aineisto kuitenkin siirtyy palveluntarjoajan järjestelmään. Ennen käyttöä pitää tarkistaa ainakin säilytys, palvelun kehittämiseen liittyvä käyttö, mahdollinen ihmisen tekemä tarkastus ja organisaation lupa.

### Organisaation hallittu palvelu

Organisaation hallittu palvelu voi näyttää käyttäjälle samalta kuin yleinen verkkopalvelu, mutta sen käyttö perustuu organisaation sopimukseen, määrittämiin asetuksiin ja käyttöoikeuksiin. Tämä ei tee kaikesta käytöstä automaattisesti sallittua, mutta vastuut ja rajat on mahdollista määritellä.

### Paikallinen ajo

Paikallisessa ajossa malli toimii omalla laitteella tai organisaation omassa ympäristössä. Aineisto voi pysyä hallitussa ympäristössä, mutta käyttäjä tai organisaatio vastaa tällöin laitteesta, käyttöoikeuksista, päivityksistä, mallin lisenssistä ja toteutuksen ulkoisista yhteyksistä.

| Kysymys | Yleinen pilvipalvelu | Organisaation hallittu palvelu | Paikallinen ajo |
| --- | --- | --- | --- |
| Poistuuko aineisto laitteelta? | Tavallisesti kyllä | Tavallisesti kyllä, mutta hallittuun ympäristöön | Ei välttämättä |
| Kuka määrittää ehdot? | Palveluntarjoaja | Palveluntarjoaja ja organisaatio | Käyttäjä tai organisaatio |
| Keskeinen etu | Helppous ja käytettävyys | Hallitut oikeudet ja sopimukset | Kontrolli aineiston reitistä |
| Mitä pitää tarkistaa? | Ehdot, asetukset ja aineiston sopivuus | Hyväksytty käyttötarkoitus ja käyttöoikeudet | Tietoturva, lisenssi ja ulkoiset yhteydet |

## 5. Käyttöpäätöksen neljä kysymystä

Ennen kuin lähetät aineiston tekoälylle, pysähdy neljän kysymyksen äärelle:

1. **Mitä tietoa aineisto sisältää?**
2. **Mihin aineisto kulkee ja mitä sille tapahtuu?**
3. **Millä ehdoilla ja oikeuksilla sitä käsitellään?**
4. **Onko ratkaisu hyväksytty juuri tähän käyttötarkoitukseen?**

Vastauksen perusteella tee yksi kolmesta päätöksestä:

- **Käytä:** Aineisto ja käyttötarkoitus sopivat ympäristöön.
- **Käytä rajatusti:** Poista tarpeettomat tiedot, rajaa ominaisuuksia tai vaihda organisaation hyväksymään ympäristöön.
- **Älä käytä tähän aineistoon:** Datavirta, käsittelyehdot tai hyväksyntä eivät riitä.

Hyvä päätös sisältää myös epävarmuuden. Jos et tiedä, tallentuuko aineisto tai siirtyykö se toiseen palveluun, oikea johtopäätös ei ole ”luultavasti turvallinen” vaan ”selvitä ennen käyttöä”.

## 6. Paikallinen ei tarkoita automaattisesti turvallista

Paikallinen ajo vähentää yhtä riskiä: aineistoa ei tarvitse lähettää yleiseen pilvipalveluun. Se ei poista muita vastuita.

Tarkista myös:

- onko laite suojattu ja ajan tasalla
- kenellä on pääsy laitteeseen ja tallennettuihin keskusteluihin
- käyttääkö sovellus verkkohakua, telemetriaa tai ulkoisia rajapintoja
- millä lisenssillä mallia saa käyttää
- kuka vastaa mallin päivittämisestä ja virhetilanteista
- sopiiko mallin laatu ja nopeus tehtävään

Paikallinen ajo on siis **käyttöympäristöä koskeva valinta**, ei yleinen turvallisuusleima.

## 7. Esimerkki: asiakaspalautteiden tiivistäminen

Pienellä yrityksellä on sata asiakaspalautetta. Palautteissa on nimiä, sähköpostiosoitteita ja kuvauksia yksittäisistä palvelutilanteista.

Huono ratkaisu olisi kopioida aineisto suoraan ensimmäiseen helposti saatavaan verkkopalveluun. Parempi eteneminen on:

1. tunnista henkilötiedot ja yrityksen sisäiset tiedot
2. poista tehtävän kannalta tarpeettomat tunnistetiedot
3. tarkista, mikä ympäristö on organisaation hyväksymä
4. piirrä aineiston reitti ja merkitse epäselvät kohdat
5. tee käyttöpäätös vasta näiden tietojen perusteella

Jos palautteet voidaan anonymisoida luotettavasti, tiivistäminen voi onnistua hyväksytyssä pilvipalvelussa. Jos tunnistettavuus on tehtävän kannalta välttämätöntä, tarvitaan organisaation hyväksymä ja tähän käsittelyyn soveltuva ratkaisu.

## Kohti omaa projektia

Kun rakennat myöhemmin oman botin, mallin laatu on vain yksi suunnittelukysymys. Sinun pitää pystyä kuvaamaan myös, mitä aineistoa botti vastaanottaa, missä sitä käsitellään, mitä tallennetaan ja millä oikeuksilla järjestelmä toimii.

Tämän tunnin datavirtakaavio toimii myöhemmin botin tietosuoja- ja käyttörajojen perustana.

## Yhteenveto

1. **Malli, palvelu ja käyttöympäristö ovat eri asioita.**
2. **Palvelun nimi ei vielä kerro aineiston koko reittiä.**
3. **Käyttöpäätös alkaa aineiston luonteen tunnistamisesta.**
4. **Pilvipalvelu, hallittu palvelu ja paikallinen ajo jakavat vastuut eri tavoin.**
5. **Epäselvä datavirta pitää selvittää ennen käyttöä.**

> **Tunnin ajattelukysymys:** Mihin aineisto kulkee, millä ehdoilla sitä käsitellään ja saako ratkaisua käyttää?

---

## Lähteet ja tarkistuspäivä

- [European Data Protection Board: International transfers and international cooperation](https://www.edpb.europa.eu/topics/international-transfers-and-international-cooperation_en)
- [Euroopan komissio: Mitä henkilötietoja voidaan käsitellä ja millä edellytyksillä?](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr/overview-principles/what-data-can-we-process-and-under-which-conditions_fi)
- [Open Source Initiative: The Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition)

Tarkistettu 20.7.2026.
