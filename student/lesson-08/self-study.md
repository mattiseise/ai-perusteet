# Kenen teksti se on? — etiikka, oikeudet ja vastuu

## Johdanto

Olet juuri käyttänyt ChatGPT:tä asiakkaalle tarkoitetun raportin kirjoittamiseen. Raportti on erinomainen, ja asiakas on tyytyväinen. Pari viikkoa myöhemmin huomaat, että samantyyppinen raportti on ilmestynyt kilpailijayrityksen sivuille. Miten se on mahdollista?

Tai huolesi voi olla tämä: ChatGPT on koulutettu verkkosivujesi teksteillä ilman lupaa ja ilman korvausta. Nyt kilpailijoillakin on käytössään samaan aineistoon perustuva ”oppi”.

Tai ajatellaan toista tilannetta: käytät ChatGPT:tä asiakaspalvelussa. Malli on opetettu miljoonilla asiakaspalveluteksteillä, joiden kirjoittajat eivät tienneet, että heidän tekstejään käytetään koulutusdatana. Osa tekoälyn taustatyöstä tehdään globaalissa etelässä: esimerkiksi merkintätyöntekijät voivat merkitä kuvia ja tekstejä pienellä tuntipalkalla, jotta tekoälymallit oppisivat toimimaan paremmin. Heidän työnsä hyödyttää järjestelmiä, joiden tuotot menevät usein suurille teknologiayrityksille.

Tai ajatellaan ympäristöä: tekoälyä pyörittävät datakeskukset kuluttavat paljon sähköä ja vettä. Jos vesi otetaan alueelta, jolla sitä on muutenkin niukasti, tekoälyn käyttö voi vaikuttaa paikallisiin vesivaroihin.

Nämä ovat **eettisiä kysymyksiä**, eivätkä ne ole tekoälyn sivujuonne. Ne liittyvät suoraan siihen, miten tekoälyä rakennetaan, käytetään ja kaupallistetaan.

Tämän tunnin jälkeen sinulla on kahdeksas todistusaineisto omaan arviointipöytääsi: **tekoäly ei ole neutraali väline**. Sen taustalla on muiden ihmisten työtä, dataa, oikeuksia ja ympäristövaikutuksia.

## Tekijänoikeudet ja koulutusdata

Kun ChatGPT vastaa sinulle, se hyödyntää tietoa, jota sille on opetettu. Mutta mistä tieto tulee? Vastaus on monimutkainen: mallit on koulutettu suurilla tekstiaineistoilla, joihin voi sisältyä verkkosivustoja, blogeja, kirjoja, artikkeleita ja muuta internetissä saatavilla olevaa tekstiä.

Monien aineistojen tekijät, kuten journalistit, kirjailijat, tutkijat ja bloggaajat, eivät välttämättä ole antaneet erillistä lupaa siihen, että heidän tekstejään käytetään tekoälymallien kouluttamiseen. He eivät myöskään välttämättä ole saaneet siitä korvausta.

<figure class="ai-demo"><span class="ai-demo__tag">// yksi näppärä vastaus — ja kolme asiaa sen takana</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:330px">
  <div class="l08-wrap">
    <div class="l08-chat"><span class="l08-u">Kirjoita tiivistelmä raportista.</span><span class="l08-a">”Tässä tiivistelmä: raportin mukaan…” <i>valmis 3 sekunnissa</i></span></div>
    <span class="l08-peek">mitä tämän takana on? ▼</span>
    <div class="l08-layer y1"><b>1 · KOULUTUSDATA</b><span>miljoonien ihmisten tekstejä — usein ilman lupaa tai korvausta</span></div>
    <div class="l08-layer y2"><b>2 · NÄKYMÄTÖN TYÖ</b><span>merkitsijät luokittelevat sisältöä matalalla palkalla globaalissa etelässä</span></div>
    <div class="l08-layer y3"><b>3 · YMPÄRISTÖ</b><span>datakeskukset kuluttavat sähköä ja vettä — Irlannissa 22 % maan sähköstä</span></div>
    <span class="l08-note">vastaus ei synny tyhjästä — siksi tekoälyn käyttö on myös eettinen valinta</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Tekoäly ei ole neutraali väline. Jokaisen sujuvan vastauksen takana on kolme kerrosta: muiden ihmisten työstä koottu koulutusdata, näkymätön merkintätyö ja datakeskusten sähkön- ja vedenkulutus. Ammattilainen tuntee koko ketjun.</figcaption></figure>
<style>
.l08-wrap{position:relative;width:560px;height:292px;font-family:var(--font-mono)}
.l08-chat{position:absolute;left:0;right:0;top:0;display:flex;flex-direction:column;gap:7px}
.l08-u{align-self:flex-end;font-size:11.5px;font-weight:500;color:#06212A;background:#46c7cf;border-radius:10px;padding:7px 11px}
.l08-a{align-self:flex-start;font-size:11.5px;line-height:1.4;color:#FFFFFF;background:#1E2740;border:1.5px solid #44517A;border-radius:10px;padding:7px 11px;opacity:0;animation:l08a 18s infinite}
.l08-a i{font-style:normal;font-size:10px;color:#7FD0A8;margin-left:6px}
@keyframes l08a{0%,4%{opacity:0}8%,97%{opacity:1}100%{opacity:0}}
.l08-peek{position:absolute;left:0;top:84px;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:#F0A38C;opacity:0;animation:l08peek 18s infinite}
@keyframes l08peek{0%,12%{opacity:0}16%,96%{opacity:1}100%{opacity:0}}
.l08-layer{position:absolute;left:0;right:0;background:#11182A;border:1.5px solid #2B3552;border-left:4px solid oklch(0.66 0.15 264);border-radius:11px;padding:8px 12px;opacity:0;transition:border-color .25s,background .25s}
.l08-layer:hover{background:#161F35;border-color:oklch(0.7 0.15 264)}
.l08-layer b{display:block;font-size:10.5px;letter-spacing:.1em;color:#EAEEF8;margin-bottom:3px}
.l08-layer span{display:block;font-size:11px;line-height:1.45;color:#B9C2DA}
.l08-layer.y1{top:108px;animation:l08y1 18s infinite}
.l08-layer.y2{top:162px;border-left-color:#c9b7f1;animation:l08y2 18s infinite}
.l08-layer.y3{top:216px;border-left-color:#F7C873;animation:l08y3 18s infinite}
@keyframes l08y1{0%,16%{opacity:0;transform:translateY(-14px)}22%,97%{opacity:1;transform:translateY(0)}100%{opacity:0}}
@keyframes l08y2{0%,30%{opacity:0;transform:translateY(-14px)}36%,97%{opacity:1;transform:translateY(0)}100%{opacity:0}}
@keyframes l08y3{0%,44%{opacity:0;transform:translateY(-14px)}50%,97%{opacity:1;transform:translateY(0)}100%{opacity:0}}
.l08-note{position:absolute;left:0;right:0;top:272px;font-size:11px;line-height:1.4;color:#7FD0A8;opacity:0;animation:l08note 18s infinite}
@keyframes l08note{0%,58%{opacity:0}64%,96%{opacity:1}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l08-a,.l08-peek,.l08-layer,.l08-note{animation:none}
.l08-a,.l08-peek,.l08-layer,.l08-note{opacity:1}}
</style>

Tämä on johtanut oikeustapauksiin ja laajaan keskusteluun. Kirjailijat, kuvataiteilijat ja muut sisällöntuottajat ovat kyseenalaistaneet sen, onko heidän teostensa käyttäminen tekoälyn kouluttamiseen hyväksyttävää ilman lupaa tai korvausta. Perusväite on sama: ”Teidän työkalunne on opetettu meidän luomuksillamme ilman suostumustamme.”

Juridisesti kysymys on monimutkainen. Esimerkiksi Yhdysvaltain tekijänoikeuslaissa tunnetaan **fair use** eli reilun käytön käsite, joka voi joissakin tilanteissa sallia aineiston käytön ilman lupaa. Suomen ja EU:n tekijänoikeuslainsäädännössä vastaavaa yleistä poikkeusta ei ole, mutta tekstin- ja tiedonlouhinnalle on omat poikkeussäännöksensä. Yksi keskeinen kysymys on, onko tekoälymallin kouluttaminen riittävän **transformatiivista** eli muuttaako se alkuperäistä aineistoa tavalla, joka tekee käytöstä hyväksyttävää. Tästä ei ole kaikissa tilanteissa selvää tai yksiselitteistä vastausta.

Eettisesti kysymys on kuitenkin helpompi ymmärtää: jos tekijöiden työtä käytetään ilman lupaa, näkyvyyttä tai korvausta, kyse ei ole vain teknisestä ratkaisusta vaan myös vallasta, oikeuksista ja vastuusta. Ammattilaisena et voi sivuuttaa tätä sanomalla vain: ”Palveluntarjoaja teki sen.” Kun käytät tekoälyä työssäsi, osallistut myös sen käyttöön liittyviin eettisiin valintoihin.

> **Pysähdy hetkeksi:** Kuvittele, että kirjoitit artikkelin blogiisi. Tietämättäsi se päätyi tekoälymallin koulutusdataan. Nyt tekoäly tuottaa tekstiä, joka muistuttaa omaa tekstiäsi. Miltä sinusta tuntuisi? Pitäisikö sinulla olla oikeus tietää tästä ja halutessasi kieltää tekstisi käyttö?

## Algoritminen harha: kuka päättelee oikein?

**Algoritminen harha** eli *algorithmic bias* tarkoittaa tilannetta, jossa tekoälyn tai algoritmin tuottamat päätökset syrjivät tiettyä ryhmää tai kohtelevat ryhmiä epäreilusti.

Konkreettinen esimerkki liittyy rekrytointiin. Jos tekoälyä koulutetaan historiallisella palkkausdatalla ja aiemmissa rekrytoinneissa on suosittu tiettyä ryhmää, malli voi oppia toistamaan saman vinouman. Se ei välttämättä ymmärrä, että kyse on syrjivästä rakenteesta. Se vain löytää datasta toistuvia kuvioita ja käyttää niitä päätösten pohjana.

Näin voi syntyä tilanne, jossa tekoäly suosii esimerkiksi tietyn sukupuolen, etnisen taustan, iän tai koulutustaustan edustajia. Ongelma ei välttämättä johdu siitä, että malli olisi ”tarkoituksella syrjivä”. Se johtuu siitä, että malli oppii datasta, joka voi heijastaa yhteiskunnan aiempia epäoikeudenmukaisuuksia.

Toinen esimerkki liittyy kasvojentunnistukseen. Jos koulutusdata sisältää enemmän vaaleaihoisia kuin tummaihoisia ihmisiä, järjestelmä voi toimia paremmin vaaleaihoisilla käyttäjillä ja huonommin muilla ryhmillä. Tällöin algoritmi on puolueellinen, koska sen opetusdata ei ole edustavaa.

Ammattilaisena sinun on ymmärrettävä tämä periaate: **jos käytät tekoälyä päätöksiin, jotka vaikuttavat ihmisiin, sinun on arvioitava mallin mahdolliset harhat.** Tämä koskee esimerkiksi palkkausta, luottopäätöksiä, asiakasluokittelua, koulutusta, terveydenhuoltoa ja oikeusjärjestelmää.

> **Pysähdy hetkeksi:** Kuvittele, että organisaatiosi käyttää tekoälyä työnhakijoiden seulontaan ja järjestelmä karsii järjestelmällisesti tietyn etnisen ryhmän edustajia. Kuka on vastuussa: järjestelmän kehittäjä, organisaatio vai henkilö, joka päätti ottaa järjestelmän käyttöön?

## Datan merkitsijät: näkymätön globaali työ

Moni ei tiedä, että tekoälyn kehittämiseen tarvitaan usein ihmisiä, jotka merkitsevät ja luokittelevat dataa. **Datan merkitseminen** tarkoittaa esimerkiksi sitä, että ihmiset kertovat järjestelmälle, mitä kuvassa näkyy, mitä tekstissä sanotaan tai millainen sävy viestissä on.

Esimerkkejä merkintätyöstä:

- Kuvasta merkitään, että siinä on kissa, auto tai liikennemerkki.
- Asiakaspalautteesta merkitään, onko se myönteinen, neutraali vai kielteinen.
- Tekstistä merkitään, sisältääkö se haitallista, väkivaltaista tai muuten sopimatonta sisältöä.

Tätä työtä tehdään usein maissa, joissa palkkataso on matala. Työntekijät voivat istua tuntikausia tietokoneen ääressä merkitsemässä kuvia, tekstejä ja videoita. He eivät aina tiedä tarkasti, mihin dataa käytetään, eivätkä he välttämättä voi puhua työstään avoimesti sopimusten vuoksi.

Työ voi olla myös henkisesti raskasta. Osa merkintätyöstä liittyy haitallisen sisällön tunnistamiseen ja poistamiseen. Tällöin työntekijät voivat joutua katsomaan väkivaltaista, seksuaalisesti hyväksikäyttävää tai muuten järkyttävää materiaalia. Tämän työn psyykkiset vaikutukset voivat olla vakavia, vaikka palkka ja työehdot olisivat heikot.

Kun käytät tekoälyä, käytät usein järjestelmää, jonka taustalla on myös tällaista näkymätöntä ihmistyötä. Et näe näitä työntekijöitä, eikä organisaatiosi välttämättä maksa heille suoraan. Silti heidän työnsä on osa sitä ketjua, joka mahdollistaa tekoälyn hyödyntämisen.

Ammattilaisena eettinen vastuu on tämä: **tiedosta, mistä mallit tulevat, ketkä ovat osallistuneet niiden rakentamiseen ja millaisissa olosuhteissa työtä on tehty.**

## Ympäristövaikutukset

Tekoäly vaatii paljon laskentatehoa. Laskentateho puolestaan vaatii sähköä, jäähdytystä, palvelimia ja laitteistoa. Siksi tekoälyllä on myös **ympäristövaikutuksia**.

Yksittäinen tekoälykysely voi tuntua pieneltä teolta. Kun kyselyitä tehdään miljoonia tai miljardeja, kokonaisvaikutus kasvaa merkittäväksi. Kansainvälisen energiajärjestö IEA:n arvion mukaan datakeskukset kuluttivat vuonna 2024 noin 415 terawattituntia sähköä, mikä oli noin 1,5 % maailman sähkönkulutuksesta. IEA arvioi, että datakeskusten sähkönkulutus voi lähes kaksinkertaistua vuoteen 2030 mennessä noin 945 terawattituntiin.

**Konkreettinen vertailu:** 945 terawattituntia on valtava määrä sähköä. Se ei tarkoita, että kaikki sähkö kuluisi pelkästään tekoälyyn, sillä datakeskukset pyörittävät myös esimerkiksi pilvipalveluita, videoita, verkkosivustoja ja yritysten järjestelmiä. Tekoäly kuitenkin kasvattaa datakeskusten laskentatarvetta nopeasti.

### Vedenkulutus riippuu sijainnista

Datakeskukset tarvitsevat jäähdytystä, koska palvelimet tuottavat paljon lämpöä. Jäähdytys voidaan toteuttaa eri tavoin: joskus käytetään paljon sähköä kuluttavaa ilmajäähdytystä, joskus vettä hyödyntäviä jäähdytysjärjestelmiä. Siksi datakeskuksen ympäristövaikutus riippuu voimakkaasti siitä, **missä päin maailmaa** se sijaitsee.

Täällä Pohjolassa vedenkulutus ei yleensä ole samanlainen ongelma kuin kuivilla alueilla. Pohjoisissa maissa on viileämpi ilmasto, ja vettä on monilla alueilla enemmän saatavilla kuin esimerkiksi Kaliforniassa, Arizonassa tai Chilen kuivuudesta kärsivillä alueilla. Tämä ei silti tarkoita, että datakeskus olisi automaattisesti ongelmaton: se voi silti kuluttaa paljon sähköä, kuormittaa paikallista sähköverkkoa ja vaatia huolellista suunnittelua.

Kaliforniassa tilanne on erilainen. Siellä datakeskusten vedenkäyttöä pidetään kasvavana riskinä, koska datakeskuksia rakennetaan myös alueille, joilla veden saatavuus on jo valmiiksi kuormittunut. Jos jäähdytykseen käytetään paikallista vettä, sama resurssi voi olla pois asukkailta, maataloudelta tai ekosysteemeiltä.

Myös Chilessä datakeskusten kasvu on herättänyt huolta. Santiagon alueella datakeskusten on arvioitu lisäävän painetta vesivaroihin paikassa, joka on kärsinyt pitkäaikaisesta kuivuudesta. Tällaisessa ympäristössä sama määrä vettä on paljon kriittisempi kysymys kuin alueella, jossa vettä on runsaammin saatavilla.

### Sähkönkulutus voi kuormittaa sähköverkkoa

Sähkönkulutuksessa ongelma ei ole vain kokonaismäärä, vaan myös se, mihin kulutus keskittyy. Jos samalle alueelle rakennetaan paljon datakeskuksia, ne voivat kuormittaa paikallista sähköverkkoa ja lisätä tarvetta uusille voimalinjoille, sähköntuotannolle ja varavoimalle.

Irlanti on hyvä esimerkki sähköverkon kuormituksesta. Irlannin tilastokeskuksen mukaan datakeskusten osuus maan mitatusta sähkönkulutuksesta nousi 5 prosentista vuonna 2015 yhteensä 22 prosenttiin vuonna 2024. Tämä tarkoittaa, että datakeskukset käyttivät Irlannissa enemmän mitattua sähköä kuin kaikki kaupunkitaloudet yhteensä.

Pohjolassa vaikutus voi olla erilainen. Suomessa ja muissa pohjoisissa maissa viileä ilmasto voi helpottaa jäähdytystä, ja datakeskusten hukkalämpöä voidaan hyödyntää kaukolämmössä. Esimerkiksi Suomessa datakeskusten hukkalämpöä voidaan siirtää kaukolämpöverkkoon, jolloin palvelinten tuottama lämpö ei mene kokonaan hukkaan. Tämä voi pienentää lämmöntuotannon päästöjä, jos se korvaa fossiilista lämmöntuotantoa.

### Esimerkkejä eri puolilta maailmaa

| Alue | Keskeinen vaikutus | Miksi sillä on väliä? |
| --- | --- | --- |
| **Pohjola** | Sähkönkulutus ja sähköverkon kuormitus | Veden saatavuus ei yleensä ole suurin ongelma, mutta datakeskukset voivat kuluttaa paljon sähköä. Hukkalämpöä voidaan joissakin tapauksissa hyödyntää kaukolämmössä. |
| **Kalifornia** | Vedenkulutus kuivilla ja kuormittuneilla alueilla | Datakeskukset voivat lisätä painetta alueilla, joilla pohjavesi ja pintavesi ovat jo valmiiksi niukkoja resursseja. |
| **Irlanti** | Erittäin suuri osuus sähkönkulutuksesta | Datakeskukset käyttivät vuonna 2024 noin 22 % maan mitatusta sähköstä, mikä kertoo paikallisen sähköverkon kuormituksesta. |
| **Chile** | Datakeskusten kasvu kuivuudesta kärsivällä alueella | Pitkäaikainen kuivuus tekee vedenkäytöstä erityisen herkän kysymyksen, koska sama vesi voi olla pois ihmisiltä, maataloudelta tai ekosysteemeiltä. |

Ammattilaisena tämä tarkoittaa seuraavaa: **tekoälyn käyttö ei ole täysin aineetonta.** Jokaisella käyttökerralla on pieni sähkö- ja mahdollisesti vesijalanjälki. Jos organisaatio käyttää tekoälyä laajasti, nämä vaikutukset kasautuvat.

Tämä ei tarkoita, että tekoälyä pitäisi boikotoida kaikissa tilanteissa. Se tarkoittaa, että tekoälyä kannattaa käyttää **harkiten** ja **tarkoituksenmukaisesti**. Esimerkiksi luonnoksen tiivistäminen tekoälyllä voi olla perusteltua, mutta miljoonien turhien automaattisten kyselyiden ajaminen vain siksi, että se on teknisesti mahdollista, ei ole vastuullista.

> **Pysähdy hetkeksi:** Jos organisaatiosi käyttäisi tekoälyä miljooniin kyselyihin päivässä, miten arvioisit sen ympäristövaikutuksia? Milloin käyttö olisi perusteltua, ja milloin kulutus olisi suurempi kuin saavutettu hyöty?

## Vastuullinen käyttö ja ammatillinen etiikka

Mitä tämä tarkoittaa ammattilaiselle? Vastuullinen tekoälyn käyttö edellyttää, että ymmärrät sekä hyödyt että riskit.

1. **Selvitä, mistä data tulee.** Jos käytät tekoälypalvelua, tutustu sen tietosuojakäytäntöihin, käyttöehtoihin ja mahdollisuuksien mukaan tietoihin opetusdatasta. Läpinäkyvä palvelu on vastuullisempi valinta kuin sellainen, joka ei kerro käytännöistään.
2. **Arvioi mallin mahdolliset harhat.** Jos käytät tekoälyä päätöksiin, jotka vaikuttavat ihmisiin, testaa järjestelmää vinoumien varalta. Tarvittaessa pyydä mukaan tilastotieteen, etiikan, tietosuojan tai juridiikan asiantuntijoita.
3. **Dokumentoi käyttö.** Jos organisaatiosi käyttää tekoälyä, dokumentoi miksi sitä käytetään, mihin tarkoitukseen, millä datalla ja mitä riskejä on tunnistettu. Dokumentointi auttaa arvioimaan päätöksiä jälkikäteen.
4. **Käytä tekoälyä harkiten.** Älä käytä tekoälyä jokaiseen tehtävään vain siksi, että se on mahdollista. Jotkut tehtävät ovat liian kriittisiä hallusinaatioille, ja jotkut aineistot ovat liian arkaluonteisia ulkoisiin palveluihin vietäviksi.
5. **Ota vastuu ja puhu ääneen.** Jos organisaatiosi käyttää tekoälyä vastuuttomasti, nosta asia esiin. Ammattilaisen tehtävä ei ole vain käyttää työkaluja tehokkaasti, vaan myös ymmärtää niiden vaikutukset.

## Yhteenveto

**Tekoäly ei ole neutraali työkalu.** Sen taustalla on koulutusdataa, tekijänoikeuskysymyksiä, ihmisten tekemää näkymätöntä työtä, algoritmisia harhoja ja ympäristövaikutuksia.

Ammattilaisena ei riitä, että osaat käyttää tekoälyä teknisesti hyvin. Sinulla on myös vastuu ymmärtää, millaisia valintoja ja vaikutuksia käytön taustalla on. ”Kaikki muutkin käyttävät sitä” ei ole eettinen perustelu. Ammatillisuus tarkoittaa sitä, että pysähdyt arvioimaan seurauksia ja teet perusteltuja valintoja.

Seuraavalla tunnilla tuotamme asiantuntijalausunnon tekoälyn avulla. Emme kirjoita sitä itse, vaan käytämme tekoälyä tekemään luettavan tuotoksen.

---
