# Milloin tekoälyn tulokseen voi luottaa? — hallusinaatiot ja luokitteluvirheet

## Johdanto

Pankin järjestelmä arvioi tuhat maksutapahtumaa. Niistä kymmenen on petoksia. Järjestelmä löytää kahdeksan petosta, mutta pysäyttää samalla 42 tavallista maksua. Onko järjestelmä hyvä?

Yhteen lukuun ei voi vastata. Ensin on kysyttävä, millaisia virheitä järjestelmä tekee ja mitä niistä seuraa. Sama periaate koskee myös generatiivista tekoälyä: sujuva vastaus ei vielä osoita, että sisältö on oikein.

**Tämän tunnin rajaus:** Tarkastelet kahta erilaista luotettavuusongelmaa. Kielimalli voi tuottaa hallusinaation, ja luokittelumalli voi merkitä tapauksen väärään luokkaan. Turvallisuus-tunnilla siirryt agenttien aktiivisiin uhkiin, kuten epäluotettavaan syötteeseen ja liian laajoihin työkalujen oikeuksiin.

Tämän tunnin jälkeen sinulla on kolmas ja viimeinen todistusaineisto omaan arviointipöytääsi. Osaat perustella, miksi yhtä tekoälytulosta pitää tarkastella tehtävän, virhetyypin ja seurauksen kautta.

## Kielimallin vastaus voi vaihdella

Tämä koskee kaikkia keskustelevia tekoälypalveluita — ChatGPT:tä, Claudea, Microsoft Copilotia ja Google Geminiä yhtä lailla. Kyse ei ole yhden palvelun viasta vaan siitä, miten kielimallit toimivat. Siksi tarkistamisen tapa on tärkeämpi opetella kuin se, mikä palvelu on juuri nyt tarkin.

Generatiivinen kielimalli rakentaa vastauksen token kerrallaan. Se arvioi jokaisessa vaiheessa, millainen jatko sopii aiempaan tekstiin. Valintaan voi sisältyä vaihtelua, joten sama prompti ei aina tuota täsmälleen samaa vastausta. Tätä kutsutaan **epädeterminismiksi**.

Joissakin järjestelmissä vaihteluun vaikuttaa **lämpötila**. Matala lämpötila suosii todennäköisimpiä jatkoja, korkea sallii enemmän vaihtelua. Asetus ei kuitenkaan tee vastauksesta totta. Johdonmukainen vastaus voi olla väärä, ja vaihteleva vastaus voi olla käyttökelpoinen.

**Hallusinaatio** on uskottavasti esitetty väite, jota vastaus ei pysty perustamaan luotettavaan tietoon ja joka voi olla virheellinen tai keksitty. Hallusinaatio ei tarkoita, että malli valehtelisi tarkoituksella. Malli tuottaa kielellisesti sopivaa jatkoa, eikä sujuvuus ole totuuden tarkistus.

Esimerkiksi työvuoro-ohjetta laativa kielimalli voi keksiä täsmällisen pykälän tai laitteen ominaisuuden. Siksi kriittinen väite tarkistetaan riippumattomasta ja mieluiten ensisijaisesta lähteestä, kuten viranomaisen ohjeesta tai valmistajan dokumentaatiosta.

> **Pysähdy hetkeksi:** Millainen virhe voisi näyttää pieneltä tekstissä mutta aiheuttaa suuren seurauksen todellisessa käyttötilanteessa?

## Luokittelumalli tekee toisenlaisia virheitä

Luokittelumalli sijoittaa tapauksen johonkin ennalta määriteltyyn luokkaan. Petosten tunnistuksessa luokat voivat olla *petos* ja *tavallinen maksu*. Mallin tulosta verrataan myöhemmin siihen, mikä tapaus todella oli.

Kun malli pysäyttää tavallisen maksun petoksena, kyse on **väärästä positiivisesta**. Kun se päästää petoksen läpi tavallisena maksuna, kyse on **väärästä negatiivisesta**. Nimet kertovat mallin antamasta tuloksesta: positiivinen tarkoittaa tässä petosepäilyä, ei hyvää lopputulosta.

Virheillä on eri seuraukset. Väärä positiivinen voi keskeyttää asiakkaan maksun turhaan. Väärä negatiivinen voi aiheuttaa taloudellisen vahingon. Siksi mallia ei pidä arvioida vain sillä perusteella, kuinka monta tapausta se luokittelee oikein.

## Kolme mittaria kertoo eri asioista

**Kokonaistarkkuus** eli *accuracy* kertoo, kuinka suuri osa kaikista tapauksista luokiteltiin oikein. Se voi näyttää erinomaiselta, vaikka malli olisi käytännössä hyödytön. Jos tuhannesta maksusta vain kymmenen on petoksia, malli saa 99 prosentin kokonaistarkkuuden ilmoittamalla jokaisen maksun tavalliseksi. Se ei silti löydä yhtään petosta.

**Osumatarkkuus** eli *precision* kysyy: kuinka suuri osa petokseksi merkityistä tapauksista oli todella petoksia? Korkea osumatarkkuus merkitsee, että hälytyksissä on vähän tavallisia maksuja.

**Kattavuus** eli *recall* kysyy: kuinka suuri osa kaikista todellisista petoksista löydettiin? Korkea kattavuus merkitsee, että vain harva petos pääsee ohi.

Johdannon järjestelmä antoi 50 hälytystä, joista kahdeksan oli todellisia petoksia. Sen osumatarkkuus oli siis 8/50 eli 16 prosenttia. Se löysi kahdeksan kaikkiaan kymmenestä petoksesta, joten kattavuus oli 8/10 eli 80 prosenttia. Kokonaistarkkuus oli korkea, mutta hälytyksistä suuri osa osui tavallisiin maksuihin.

Mikään näistä mittareista ei yksin ratkaise, onko malli riittävän hyvä. Valinta riippuu seurauksista. Sairaudessa tai petoksessa väärä negatiivinen voi olla erityisen vakava. Jos jokainen hälytys vaatii kalliin käsittelyn, myös väärien positiivisten määrä ratkaisee.

> **Pysähdy hetkeksi:** Kumpi olisi omassa esimerkissäsi vakavampi: väärä positiivinen vai väärä negatiivinen? Perustele seurauksella, älä mittarin nimellä.

<figure class="ai-demo"><span class="ai-demo__tag">// sujuva väite kulkee tarkistuksen läpi</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:300px">
  <div class="l07-check" data-once role="img" aria-label="Animaatio näyttää tekoälyn esittämän täsmällisen väitteen, sen tarkistamisen riippumattomasta lähteestä ja lopputuloksen, jossa väite hylätään keksittynä.">
    <div class="l07-step s1"><b>1 · VÄITE</b><span>”Laitteen huoltoväli on täsmälleen 1 200 tuntia.”</span></div>
    <div class="l07-arrow">→</div>
    <div class="l07-step s2"><b>2 · LÄHDE</b><span>Valmistajan virallinen huolto-ohje</span></div>
    <div class="l07-arrow">→</div>
    <div class="l07-step s3"><b>3 · ARVIO</b><span>Ohjeessa ei ole väitettyä lukua — älä käytä väitettä.</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Hallusinaatiota ei tunnista tekstin varmuudesta. Kuvitteellisessa esimerkissä täsmällinen huoltoväite näyttää uskottavalta, mutta riippumaton lähde ei tue sitä. Tarkistus voi myös vahvistaa väitteen — ratkaisevaa on lähteen näyttö, ei mallin sävy.</figcaption></figure>
<style>
.l07-check{display:flex;align-items:stretch;gap:10px;width:560px;font-family:var(--font-mono);animation:l07checkw 9s 1 forwards}
.l07-step{flex:1;min-height:150px;border:2px solid #2B3552;border-radius:13px;background:#11182A;padding:16px;opacity:.35;transform:translateY(8px);animation:l07flow 9s infinite}
.l07-step b{display:block;font-size:10.5px;letter-spacing:.09em;color:#8B94B3;margin-bottom:14px}.l07-step span{display:block;font-size:12px;line-height:1.55;color:#EAEEF8}
.l07-step.s2{animation-delay:3s;border-color:#46c7cf}.l07-step.s3{animation-delay:6s;border-color:#F0A38C}.l07-arrow{align-self:center;color:#8B94B3;font-size:22px}
@keyframes l07flow{0%,28%{opacity:.35;transform:translateY(8px)}8%,22%{opacity:1;transform:translateY(0)}33%,100%{opacity:.35;transform:translateY(8px)}}
@media (prefers-reduced-motion:reduce){.l07-step{animation:none;opacity:1;transform:none}}
@media (max-width:680px){.l07-check{width:100%;flex-direction:column}.l07-step{min-height:auto}.l07-arrow{transform:rotate(90deg)}.ai-demo__stage:has(.l07-check){height:520px!important}}
@keyframes l07checkw{0%,100%{opacity:1}}
</style>

## Luotettavuus on näyttöön perustuva arvio

Tekoälyjärjestelmän arviointi alkaa tehtävästä. Mitä järjestelmän pitäisi tehdä, millaisissa tilanteissa ja kenelle? Sen jälkeen tarkastellaan oikeita testitapauksia, eri ryhmiä ja käytön seurauksia. Yksi keskiarvo ei kerro, toimiiko malli tasapuolisesti tai säilyykö suorituskyky maailman muuttuessa.

Kielimallin väitteelle etsitään lähde. Luokittelumallille tarkastellaan ainakin virhetyyppejä ja tehtävään sopivia mittareita. Kriittisessä käytössä sovitaan myös, milloin ihminen tarkistaa tuloksen ja mitä tapahtuu, jos malli on epävarma tai väärässä.

## Yhteenveto

Kielimallin sujuvuus ei todista vastauksen oikeellisuutta. Hallusinaatio tarkistetaan luotettavasta lähteestä.

Luokittelumallissa väärä positiivinen ja väärä negatiivinen ovat eri virheitä, joilla voi olla erilaiset seuraukset. Kokonaistarkkuus kertoo oikein luokiteltujen osuuden, osumatarkkuus petoshälytysten osuvuuden ja kattavuus löydettyjen petosten osuuden. Vastuullinen arvio yhdistää mittarit, seuraukset ja ihmisen valvonnan.

---

## Lähteet ja tarkistuspäivä

- [Google Machine Learning: Accuracy, precision, and recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)
- [NIST: Generative AI Profile, NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

Tarkistettu 21.7.2026.
