# Rakenna uudelleen käytettävä promptikortti

## Johdanto: hyvä prompti osoitetaan kokeella

Tunnilla 4 opit, että konteksti muuttaa vastausta. Nyt viet taidon käytäntöön yhdessä toistuvassa tehtävässä. Tavoitteena ei ole kerätä mahdollisimman monta näyttävää promptia, vaan rakentaa **yksi promptikortti**, jonka käyttötilanteen, toimivuuden ja rajat osaat perustella.

Promptikortti yhdistää kolme asiaa:

1. pysyvän ohjeen, jota käytät uudelleen
2. vaihtuvan aineiston, jonka lisäät joka käyttökerralla
3. laatukriteerit, joilla tarkistat vastauksen

Ajattele korttia työohjeena, jonka toinenkin ihminen voisi ottaa käyttöön. Pysyvä ohje kertoo, mikä työ tehdään ja millä ehdoilla. Vaihtuva aineisto tuo jokaiseen käyttökertaan uuden sisällön. Laatukriteerit puolestaan estävät hyväksymästä vastausta vain siksi, että se kuulostaa sujuvalta. Jos jokin näistä kolmesta puuttuu, korttia on vaikea käyttää johdonmukaisesti tai kehittää havaintojen perusteella.

> **Tunnin ydinkysymys:** Mikä yksi promptimuutos paransi vastausta — ja millä havainnolla osoitat vaikutuksen?

<figure class="ai-demo"><span class="ai-demo__tag" id="l12-t"><i aria-hidden="true">// </i>sama koe — yksi nimetty muutos kerrallaan</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:332px">
  <div class="l12-wrap" data-once role="img" aria-labelledby="l12-t" aria-describedby="l12-d">
    <span class="sr-only" id="l12-d">Kriteerit lukitaan ennen ajoa, korttiin tehdään yksi nimetty muutos ja sama aineisto ajetaan uudelleen. Juuri se kriteeri kääntyy hyväksytyksi — muutos on tässä ajossa eron todennäköinen selitys, mutta yksi vertailupari ei todista syytä, joten koe toistetaan toisella vastaavalla aineistolla.</span>
    <div class="l12-card"><i class="l12-ph">PROMPTIKORTTI</i>
      <span class="l12-ln"><i class="l12-bar"></i>tehtävä</span>
      <span class="l12-ln"><i class="l12-bar"></i>vastausmuoto</span>
      <span class="l12-ln"><i class="l12-bar"></i>pysyvä raja</span>
      <span class="l12-ch"><b class="l12-old">—</b><b class="l12-new">+ älä keksi puuttuvia määräaikoja</b></span>
      <em class="l12-same">muut rivit ennallaan</em>
      <span class="l12-cnt">muutoksia: 1</span></div>
    <div class="l12-kp"><i class="l12-ph">KRITEERIT · <b class="l12-pre">ennen ajoa</b></i>
      <span class="l12-hv"><b class="hv1">V1</b><b class="hv2">V2</b></span>
      <span class="l12-kr">kaikki kohdat mukana<b class="l12-m a1">✓</b><b class="l12-m b1">✓</b></span>
      <span class="l12-kr">alkaa verbillä<b class="l12-m a2">✓</b><b class="l12-m b2">✓</b></span>
      <span class="l12-kr">ei keksittyjä määräaikoja<b class="l12-m x a3">✗</b><b class="l12-m b3 ring">✓</b></span>
      <em class="l12-note">V1: keksi 2 määräaikaa</em></div>
    <span class="l12-data d1">aineisto</span>
    <span class="l12-data d2">sama aineisto</span>
    <span class="l12-res">muutos on todennäköinen selitys — yksi pari ei todista</span>
    <span class="l12-cond">sama aineisto · sama malli ja asetukset · uusi keskustelu · 1 muutos</span>
    <span class="l12-rep">Toista koe toisella vastaavalla aineistolla</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Vaikutuksen voi väittää vain, kun kriteerit lukittiin ennen ajoa ja vain yksi asia muuttui. Silloin muutos on tässä ajossa eron todennäköinen selitys — yksi vertailupari ei vielä todista syytä. Toista koe toisella samaan tehtävätyyppiin kuuluvalla aineistolla.</figcaption></figure>
<style>
.l12-wrap{position:relative;width:560px;height:316px;font-family:var(--font-mono);animation:l12w 21s 1 forwards}
.l12-ph{display:block;font-style:normal;font-size:12px;font-weight:700;letter-spacing:.08em;color:#EAEEF8}
.l12-ph .l12-pre{color:#7FD0A8;animation:l12pre 21s 1 forwards;display:inline-block}
.l12-card{position:absolute;left:2px;top:8px;width:238px;height:236px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:10px 12px}
.l12-ln{display:flex;align-items:center;gap:7px;margin-top:12px;font-size:12px;color:#B9C2DA}
.l12-bar{display:inline-block;width:64px;height:10px;border-radius:5px;background:#2E3A5C;flex:none}
.l12-ch{position:relative;display:block;margin-top:12px;height:30px}
.l12-ch b{position:absolute;left:0;top:0;width:100%;box-sizing:border-box;font-size:12px;line-height:1.25;font-weight:400}
.l12-old{color:#8B94B3;padding-top:6px;animation:l12old 21s 1 forwards}
.l12-new{color:#0B0F1A;background:#C9B7F1;border-radius:7px;padding:4px 8px;font-weight:700;opacity:0;animation:l12new 21s 1 forwards}
.l12-same{position:absolute;left:12px;bottom:30px;font-style:normal;font-size:12px;color:#7FD0A8;opacity:0;animation:l12same 21s 1 forwards}
.l12-cnt{position:absolute;left:12px;bottom:8px;font-size:12px;font-weight:700;color:#C9B7F1;border:1px solid #C9B7F1;border-radius:999px;padding:2px 8px;opacity:0;animation:l12cnt 21s 1 forwards}
.l12-kp{position:absolute;left:256px;top:8px;width:302px;height:236px;box-sizing:border-box;background:#11182A;border:1px solid #2B3552;border-radius:12px;padding:10px 12px}
.l12-hv{position:absolute;right:12px;top:9px;width:64px;display:flex;gap:12px}
.l12-hv b{width:26px;text-align:center;font-size:12px;color:#B9C2DA}
.l12-kr{position:relative;display:block;margin-top:14px;padding-right:76px;font-size:12px;line-height:1.3;color:#EAEEF8}
.l12-kr .l12-m{position:absolute;top:-2px;width:26px;text-align:center;font-size:13px;font-weight:700;color:#7FD0A8;opacity:0;transform:scale(.4)}
.l12-kr .l12-m.x{color:#FFD79A}
.l12-kr b:nth-of-type(1){right:50px}
.l12-kr b:nth-of-type(2){right:12px}
.l12-m.ring{border:1.5px solid #C9B7F1;border-radius:50%;line-height:1.4;height:22px;top:-4px}
.l12-m.a1{animation:l12a1 21s 1 forwards}.l12-m.a2{animation:l12a2 21s 1 forwards}.l12-m.a3{animation:l12a3 21s 1 forwards}
.l12-m.b1{animation:l12b1 21s 1 forwards}.l12-m.b2{animation:l12b2 21s 1 forwards}.l12-m.b3{animation:l12b3 21s 1 forwards}
.l12-note{position:absolute;left:12px;bottom:8px;font-style:normal;font-size:12px;color:#FFD79A;opacity:0;animation:l12note 21s 1 forwards}
.l12-data{position:absolute;left:8px;top:254px;font-size:12px;color:#06212A;background:#46C7CF;border-radius:999px;padding:3px 10px;opacity:0}
.l12-data.d1{animation:l12d1 21s 1 forwards}
.l12-data.d2{animation:l12d2 21s 1 forwards}
.l12-cond{position:absolute;left:0;top:276px;width:560px;text-align:center;font-size:12px;color:#8B94B3}
.l12-rep{position:absolute;left:0;top:296px;width:560px;text-align:center;font-size:12px;color:#7FD0A8;opacity:0;animation:l12rep 21s 1 forwards}
.l12-res{position:absolute;right:0;top:254px;font-size:12px;font-weight:600;color:#FFD79A;opacity:0;animation:l12res 21s 1 forwards}
@keyframes l12w{0%{opacity:0}3%{opacity:1}97%,100%{opacity:1}}
@keyframes l12pre{0%,2%{transform:scale(1)}5%{transform:scale(1.12)}8%,100%{transform:scale(1)}}
@keyframes l12d1{0%,8%{opacity:0;transform:translateX(-40px)}13%{opacity:1;transform:none}30%{opacity:1}34%,100%{opacity:0}}
@keyframes l12a1{0%,15%{opacity:0;transform:scale(.4)}18%,100%{opacity:1;transform:scale(1)}}
@keyframes l12a2{0%,20%{opacity:0;transform:scale(.4)}23%,100%{opacity:1;transform:scale(1)}}
@keyframes l12a3{0%,25%{opacity:0;transform:scale(.4)}28%,100%{opacity:1;transform:scale(1)}}
@keyframes l12note{0%,28%{opacity:0}31%,100%{opacity:1}}
@keyframes l12old{0%,38%{opacity:1}42%,100%{opacity:0}}
@keyframes l12new{0%,40%{opacity:0;transform:translateX(-8px)}45%,100%{opacity:1;transform:none}}
@keyframes l12same{0%,47%{opacity:0}50%,100%{opacity:1}}
@keyframes l12cnt{0%,52%{opacity:0;transform:scale(.7)}55%,100%{opacity:1;transform:scale(1)}}
@keyframes l12d2{0%,62%{opacity:0;transform:translateX(-40px)}66%{opacity:1;transform:none}86%{opacity:1}90%,100%{opacity:0}}
@keyframes l12b1{0%,70%{opacity:0;transform:scale(.4)}73%,100%{opacity:1;transform:scale(1)}}
@keyframes l12b2{0%,74%{opacity:0;transform:scale(.4)}77%,100%{opacity:1;transform:scale(1)}}
@keyframes l12b3{0%,78%{opacity:0;transform:scale(.4)}81%,100%{opacity:1;transform:scale(1)}}
@keyframes l12res{0%,84%{opacity:0}88%,100%{opacity:1}}
@keyframes l12rep{0%,88%{opacity:0}92%,100%{opacity:1}}
@media (prefers-reduced-motion:reduce){
  .l12-wrap,.l12-wrap *{animation:none!important}
  .l12-wrap,.l12-note,.l12-new,.l12-same,.l12-cnt,.l12-res,.l12-rep{opacity:1}
  .l12-kr .l12-m{opacity:1;transform:scale(1)}
  .l12-old,.l12-data{opacity:0}
}
</style>

## Valitse toistuva tehtävä, jonka osaat arvioida

Hyvä promptikortti ratkaisee rajatun tehtävän, joka toistuu samankaltaisena mutta saa joka kerta uuden aineiston. Esimerkiksi:

- viestin muuttaminen kolmeksi toimintakohdaksi
- muistiinpanojen muuttaminen kertauskysymyksiksi
- tekstiluonnoksen muokkaaminen tietylle yleisölle
- palautteiden jäsentäminen ennalta sovittuihin teemoihin.

Viikoittaisten kokousmuistiinpanojen muuttaminen toimintakohdiksi on hyvä esimerkki. Aineisto vaihtuu joka viikko, mutta haluttu työ pysyy samana: tehtävä, vastuuhenkilö ja määräaika poimitaan näkyviin. Sen sijaan ”auta minua työssäni” ei vielä kuvaa toistettavaa tehtävää eikä anna perustaa vastauksen arvioinnille.

Vältä tehtävää, jonka hyvyyttä et pysty itse arvioimaan. Jos et tunne aihetta tai oikeaa lopputulosta, et myöskään tiedä, paransiko promptin muutos vastausta.

Kirjoita tehtävä yhdellä lauseella:

> Muunnan **[vaihtuvan aineiston]** muotoon **[haluttu tuotos]**, jotta **[käyttäjä]** voi **[käyttötarkoitus]**.

## Erota pysyvä ohje ja vaihtuva syöte

Uudelleen käytettävässä promptissa kaikkea ei kirjoiteta joka kerta uudelleen. Pysyvä osa kertoo työn ja sen ehdot. Vaihtuva osa merkitään selkeästi esimerkiksi hakasulkeilla.

```text
Muuta alla oleva [LÄHDEAINEISTO] kolmeksi toimintakohdaksi.

Kohderyhmä: [YLEISÖ]
Käyttötarkoitus: [TARKOITUS]

Säilytä lähteen nimet, päivämäärät ja vastuut täsmällisinä.
Älä lisää tietoa, jota lähteessä ei ole.

Vastausmuoto:
1. tehtävä
2. vastuuhenkilö, jos lähteessä mainitaan
3. määräaika, jos lähteessä mainitaan

LÄHDEAINEISTO:
[LIITÄ VAIHTUVA AINEISTO TÄHÄN]
```

Kortti ei ole vain pitkä prompti. Sen pitää kertoa myös, milloin rakennetta käytetään ja milloin ei.

Esimerkin hakasulkeet tekevät vastuunjaon näkyväksi. Kortti ei arvaa yleisöä, tarkoitusta tai lähdeaineistoa, vaan käyttäjä täyttää ne joka käyttökerralla. Samalla pysyvät vaatimukset — kuten lähteen nimien ja määräaikojen säilyttäminen — pysyvät samoina. Juuri tämä erottaa uudelleen käytettävän rakenteen keskusteluun kerran kirjoitetusta pyynnöstä.

## Päätä laatukriteerit ennen ensimmäistä ajoa

Ilman ennalta päätettyjä kriteereitä arvio helposti mukautuu siihen, millaisen vastauksen malli tuotti. Valitse 2–4 havaittavaa ominaisuutta.

| Epämääräinen arvio | Havaittava kriteeri |
| --- | --- |
| ”Vastaus on parempi.” | Kaikki lähteen neljä tehtävää ovat mukana. |
| ”Teksti on selkeä.” | Jokainen kohta alkaa tekemistä kuvaavalla verbillä. |
| ”Malli käytti aineistoa hyvin.” | Vastaus ei lisää nimiä, lukuja tai määräaikoja. |
| ”Muoto on käyttökelpoinen.” | Vastauksen voi siirtää tehtävälistaan ilman rakenteen korjaamista. |

Kriteeri on käyttökelpoinen, kun toinenkin ihminen voisi tarkistaa sen samasta vastauksesta.

Kriteeri toimii siis pienenä sopimuksena ennen testiä. Kun päätät etukäteen, ettei mallin pidä keksiä puuttuvia määräaikoja, voit tarkistaa vastauksesta yksiselitteisesti, tapahtuiko näin. Jos arviointiperuste syntyy vasta vastauksen jälkeen, sitä on helppo muuttaa huomaamatta mallin tuotoksen eduksi.

## Tee kaksi vertailukelpoista versiota

Aja ensin versio 1 turvallisella aineistolla ja säilytä sekä prompti että vastaus. Arvioi vastausta valituilla kriteereillä. Nimeä yksi puute, jonka haluat korjata.

Muuta seuraavaksi vain yhtä asiaa. Voit esimerkiksi:

- täsmentää kohderyhmän
- lisätä vastausrakenteen
- lisätä lähteeseen pitäytymistä koskevan rajan
- määrittää puuttuvan tiedon käsittelyn.

Avaa uusi keskustelu ja aja versio 2 samalla aineistolla. Jos jatkat samassa keskustelussa, aiempi vastaus voi vaikuttaa tulokseen. Jos vaihdat aineiston, et enää testaa vain promptin muutosta.

Tämä on eri asia kuin tavallinen keskustelullinen hiominen, jossa käyttäjä muuttaa useita asioita kerralla ja tyytyy lopulta mieluisaan vastaukseen. Hallitussa kokeessa säilytät lähtötilanteen, jotta pystyt myöhemmin sanomaan, mikä muutos todennäköisesti vaikutti tulokseen.

## Kirjaa vaikutus havaintona

Hyvä johtopäätös nimeää muutoksen, tuloksen ja näytön:

> Lisäsin ohjeen ”älä lisää puuttuvia määräaikoja”. Versio 1 keksi kahdelle tehtävälle määräajan, mutta versio 2 merkitsi ne puuttuviksi. Muutos paransi lähdeuskollisuutta tällä aineistolla.

Huomaa rajaus: yksi testi ei osoita, että kortti toimii kaikilla aineistoilla. Se osoittaa, miten kortti toimi tässä kokeessa. Seuraava hyödyllinen testi käyttää erilaista mutta samaan tehtävään kuuluvaa syötettä.

Näin kortin kehittäminen jatkuu perustellusti. Ensimmäinen koe osoittaa yhden vaikutuksen, seuraava koe koettelee rakennetta uudella aineistolla ja versiohistoria säilyttää tiedon siitä, miksi korttia muutettiin. Kortti ei ole koskaan ”valmis totuus”, vaan dokumentoitu työväline, jonka käyttöalue tunnetaan.

## Korttiin kuuluu myös tunnettu raja

Kirjaa vähintään yksi tilanne, jossa korttia ei pidä käyttää sellaisenaan. Raja voi liittyä esimerkiksi:

- aineistoon, jota ei saa lähettää palveluun
- tehtävään, jossa tarvitaan alan asiantuntijan päätös
- poikkeavaan syötteeseen, jota ei ole testattu
- tilanteeseen, jossa lähde on puutteellinen tai ristiriitainen.

Tunnettu raja ei heikennä korttia. Se estää käyttämästä toimivaa rakennetta väärässä tehtävässä.

## Yhteenveto

Yksi testattu promptikortti on hyödyllisempi kuin suuri lista prompteja, joiden toimivuudesta ei ole näyttöä. Rajaa toistuva tehtävä, erota pysyvä ohje vaihtuvasta aineistosta, päätä laatukriteerit etukäteen ja muuta vain yhtä asiaa kerrallaan.

Tallenna korttiin versiot, vastaukset, havaittu vaikutus ja tunnettu raja. Tunnilla 17 hyödynnät toimivaksi osoitettua rakennetta botin järjestelmäpromptissa.

> **Lopuksi pohdittavaksi:** Mikä promptisi osa on aidosti uudelleen käytettävä — ja mikä pitää päättää uudelleen jokaisessa käyttötilanteessa?

---

## Lähteet ja tarkistuspäivä

- [NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Microsoft: Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering)

Tarkistettu 20.7.2026.
