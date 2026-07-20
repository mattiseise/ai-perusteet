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

<figure class="ai-demo"><span class="ai-demo__tag">// yksi aineisto — kolme mahdollista käsittely-ympäristöä</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:286px">
  <div class="l11-flow">
    <div class="l11-source"><b>SINÄ</b><span>”asiakaspalaute.txt”</span></div>
    <div class="l11-arrow l11-a1">→</div><div class="l11-arrow l11-a2">→</div><div class="l11-arrow l11-a3">→</div>
    <div class="l11-target l11-t1"><b>Yleinen pilvipalvelu</b><span>Aineisto poistuu laitteelta. Tarkista ehdot ja asetukset.</span></div>
    <div class="l11-target l11-t2"><b>Organisaation hallittu palvelu</b><span>Käyttö perustuu sopimukseen, asetuksiin ja organisaation ohjeisiin.</span></div>
    <div class="l11-target l11-t3"><b>Paikallinen ajo</b><span>Aineisto voi pysyä laitteella, jos toteutus ei käytä ulkoisia yhteyksiä.</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Ratkaisevaa ei ole työkalun nimi vaan koko reitti: mitä aineistoa lähetetään, missä se käsitellään ja millä ehdoilla.</figcaption></figure>
<style>
.l11-flow{position:relative;width:760px;height:246px;font-family:var(--font-mono)}
.l11-source{position:absolute;left:0;top:86px;width:176px;padding:18px 14px;text-align:center;color:#EAEEF8;background:#11182A;border:2px solid #44517A;border-radius:14px}
.l11-source b{display:block;font-size:13px;letter-spacing:.14em}
.l11-source span{display:block;margin-top:9px;padding:5px 7px;color:#06212A;background:#46C7CF;border-radius:8px;font-size:11px}
.l11-arrow{position:absolute;left:192px;color:#0E9AA7;font-size:26px;font-weight:700}
.l11-a1{top:30px;transform:rotate(-18deg)}.l11-a2{top:108px}.l11-a3{top:184px;transform:rotate(18deg)}
.l11-target{position:absolute;left:248px;width:500px;padding:13px 16px;color:#EAEEF8;background:#141B2D;border:1.5px solid #2B3552;border-radius:12px}
.l11-target b{display:block;font-size:12.5px;color:#FFFFFF}.l11-target span{display:block;margin-top:4px;color:#B9C2DA;font-size:11px;line-height:1.4}
.l11-t1{top:0;border-color:#D2A43B}.l11-t2{top:84px;border-color:#6E86E8}.l11-t3{top:168px;border-color:#54B983}
@media(max-width:700px){.l11-flow{width:620px;transform:scale(.82);transform-origin:center}.ai-demo__stage{overflow:hidden}}
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
