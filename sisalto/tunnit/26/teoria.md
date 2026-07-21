# Kädet saveen — tee agentista testattava minimiversio

## Johdanto: teoriasta tekemiseen

Olet oppinut, miten tällä kurssilla rajattu agentti toimii, miten sitä turvataan ja miten se eroaa tavallisesta työnkulusta. Olet myös kerännyt matkan varrella **viisi pohjapiirrosta** tunneilta 19, 21, 23, 24 ja 25. Tällä tunnilla kokoat ne yhteen ja teet ensimmäisen testattavan version. Voit rakentaa sen teknisenä n8n-toteutuksena tai dokumentoituna suunnitelmana. Molemmissa kielimallin on tehtävä vähintään yksi todellinen, tilanteen mukaan muuttuva valinta.

**n8n** lausutaan ”n-eight-n”. Se on visuaalinen automaatioympäristö, jota voi käyttää pilvipalveluna tai ylläpitää itse sen lisenssiehtojen mukaisesti. Työnkulku rakennetaan **solmuista** eli nodeista kankaalle. Jokainen solmu tekee yhden asian: vastaanottaa viestin, kutsuu kielimallia, lukee rajattua tietoa tai valmistelee toiminnon. Solmujen välille vedetään yhteys, ja tieto kulkee vaiheesta toiseen.

Miksi juuri n8n? Koska se poistaa yhden suurimmista esteistä agentin rakentamisessa: sinun ei tarvitse osata ohjelmoida kaikkea käsin. Kaikki, mitä olet oppinut agentin rakenteesta — **syötekäsittelijä**, **päättelijä ja suunnittelija**, **työkalujen suorittaja**, **muisti ja konteksti**, **turvakerros** sekä **seuranta ja palautesilmukka** — voidaan toteuttaa n8n:ssä visuaalisesti. Näet agentin arkkitehtuurin konkreettisesti solmuina ja yhteyksinä.

> **Agentin ohjauskehyksen näkökulma:** n8n ei ole automaattisesti agentti. Se on ympäristö, jossa ohjauskehyksen vastuut voidaan toteuttaa näkyvänä työnkulkuna: yksi solmu kutsuu kielimallia, muut huolehtivat syötteistä, työkaluista, tilasta, turvarajoista ja toiminnan jatkumisesta. Dokumentoidussa suunnittelupolussa samat vastuut kuvataan kaaviona, sopimuksina ja suoritusjälkinä. Kuusi rakennusosaa toimii kummassakin polussa kattavuuden tarkistuslistana.

**Pysähdy hetkeksi:** Mieti jotakin toistuvaa tehtävää arjessasi tai koulussa. Voisiko kone hoitaa sen puolestasi, jos sillä olisi pääsy oikeisiin työkaluihin?

Tältä valmis n8n-työnkulku näyttää. Tämä on esimerkki siitä, millaisen yksinkertaisen agentin voit rakentaa:

<figure style="margin:26px 0;text-align:center">
<svg viewBox="0 0 920 410" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:840px;height:auto" font-family="system-ui, -apple-system, 'Segoe UI', sans-serif" role="img">
  <title>Esimerkki-työnkulku: sähköpostien luokittelu n8n:ssä</title>
  <desc>Päivittäin ajettava järjestelmä hakee sähköpostit. Kielimalli arvioi tilanteen ja valitsee rajatuista työkaluista tarvittavan toiminnon. Tulos muotoillaan ja tallennetaan rajattuun taulukkoon.</desc>
  <defs>
    <g id="cls-mail" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="12" rx="2.2"/><path d="M3.5 7.5 L12 13 L20.5 7.5"/></g>
    <g id="cls-robot" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="8" width="15" height="11.5" rx="3"/><path d="M12 8 V4.5"/><circle cx="12" cy="3.4" r="1.4" fill="currentColor" stroke="none"/><circle cx="9.3" cy="13.5" r="1.3" fill="currentColor" stroke="none"/><circle cx="14.7" cy="13.5" r="1.3" fill="currentColor" stroke="none"/><path d="M9.5 16.6 H14.5"/></g>
    <g id="cls-braces" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6 L5 12 L9 18 M15 6 L19 12 L15 18"/></g>
    <g id="cls-sheet" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3.5" width="16" height="17" rx="2"/><path d="M4 9 H20 M4 14.5 H20 M10 9 V20.5 M15 9 V20.5"/></g>
    <g id="cls-clock" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7 V12 L15.5 14"/></g>
    <g id="cls-tag" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 12 V4.8 a1.3 1.3 0 0 1 1.3 -1.3 H12 L20.5 12 a1.3 1.3 0 0 1 0 1.8 L13.6 20.5 a1.3 1.3 0 0 1 -1.8 0 Z"/><circle cx="7.5" cy="7.5" r="1.3"/></g>
    <g id="cls-ai" fill="none" stroke="currentColor"><path d="M12 3 L13.8 9.6 L20.5 11.4 L13.8 13.2 L12 20 L10.2 13.2 L3.5 11.4 L10.2 9.6 Z" fill="currentColor"/></g>
  </defs>
  <rect x="0" y="0" width="920" height="410" rx="16" fill="#FAFBFE"/>
  <text x="460" y="36" text-anchor="middle" font-size="22" font-weight="700" fill="#1B2336">Esimerkki-työnkulku: sähköpostien luokittelu</text>
  <text x="460" y="62" text-anchor="middle" font-size="13" fill="#5A6478">Kielimalli valitsee sallitun työkalun viestin perusteella.</text>
  <rect x="28" y="92" width="176" height="78" rx="12" fill="#F0F9F4" stroke="#CDE9D9" stroke-width="1.5"/>
  <use href="#cls-clock" x="44" y="108" width="19" height="19" style="color:#2F9E69"/>
  <text x="70" y="121" font-size="12.5" font-weight="700" fill="#247A52">Sähköpostien haku</text>
  <text x="44" y="150" font-size="11" fill="#3A4253">Päivittäin klo 08:00</text>
  <line x1="204" y1="131" x2="240" y2="131" stroke="#9AA6BD" stroke-width="2.2"/><path d="M244 131 L234 126 L234 136 Z" fill="#9AA6BD"/>
  <rect x="244" y="92" width="200" height="78" rx="12" fill="#EEF1FE" stroke="#3B5BDB" stroke-width="2"/>
  <use href="#cls-robot" x="260" y="106" width="22" height="22" style="color:#3B5BDB"/>
  <text x="290" y="121" font-size="12.5" font-weight="700" fill="#2F46B0">AI Agent</text>
  <text x="260" y="150" font-size="11" fill="#3A4253">Luokittele ja tee yhteenveto</text>
  <line x1="444" y1="131" x2="480" y2="131" stroke="#9AA6BD" stroke-width="2.2"/><path d="M484 131 L474 126 L474 136 Z" fill="#9AA6BD"/>
  <rect x="484" y="92" width="176" height="78" rx="12" fill="#F0F9F4" stroke="#CDE9D9" stroke-width="1.5"/>
  <use href="#cls-braces" x="500" y="108" width="19" height="19" style="color:#2F9E69"/>
  <text x="526" y="121" font-size="12.5" font-weight="700" fill="#247A52">Muotoilu</text>
  <text x="500" y="150" font-size="11" fill="#3A4253">Muotoile yhteenveto</text>
  <line x1="660" y1="131" x2="696" y2="131" stroke="#9AA6BD" stroke-width="2.2"/><path d="M700 131 L690 126 L690 136 Z" fill="#9AA6BD"/>
  <rect x="700" y="92" width="192" height="78" rx="12" fill="#E9F6F7" stroke="#BFE6E9" stroke-width="1.5"/>
  <use href="#cls-sheet" x="716" y="108" width="19" height="19" style="color:#0E9AA7"/>
  <text x="742" y="121" font-size="12.5" font-weight="700" fill="#0B7E89">Tallennus</text>
  <text x="716" y="150" font-size="11" fill="#3A4253">rajattuun taulukkoon</text>
  <g stroke="#B7C0D6" stroke-width="1.5" stroke-dasharray="4 4" fill="none">
    <path d="M344 170 V196 H126 V232"/><path d="M344 170 V196 H344 V232"/><path d="M344 170 V196 H560 V232"/><path d="M344 170 V196 H770 V232"/>
  </g>
  <text x="460" y="190" text-anchor="middle" font-size="10.5" fill="#7E88A8">Agentin työkalut</text>
  <rect x="46" y="232" width="160" height="56" rx="10" fill="#FFFFFF" stroke="#D8DEEC" stroke-width="1.3"/>
  <use href="#cls-tag" x="60" y="248" width="18" height="18" style="color:#3B5BDB"/><text x="84" y="261" font-size="11.5" font-weight="600" fill="#1B2336">Luokittelusäännöt</text>
  <text x="60" y="280" font-size="10.3" fill="#5A6478">prioriteetit, kategoriat</text>
  <rect x="264" y="232" width="160" height="56" rx="10" fill="#FFFFFF" stroke="#D8DEEC" stroke-width="1.3"/>
  <use href="#cls-ai" x="278" y="248" width="18" height="18" style="color:#3B5BDB"/><text x="302" y="261" font-size="11.5" font-weight="600" fill="#1B2336">Kielimalli (LLM)</text>
  <text x="278" y="280" font-size="10.3" fill="#5A6478">tekee yhteenvedon</text>
  <rect x="482" y="232" width="160" height="56" rx="10" fill="#FFFFFF" stroke="#D8DEEC" stroke-width="1.3"/>
  <use href="#cls-sheet" x="496" y="248" width="18" height="18" style="color:#3B5BDB"/><text x="520" y="261" font-size="11.5" font-weight="600" fill="#1B2336">taulukko</text>
  <text x="496" y="280" font-size="10.3" fill="#5A6478">tallentaa viestit</text>
  <rect x="700" y="232" width="160" height="56" rx="10" fill="#FFFFFF" stroke="#D8DEEC" stroke-width="1.3"/>
  <use href="#cls-mail" x="714" y="248" width="18" height="18" style="color:#3B5BDB"/><text x="738" y="261" font-size="11.5" font-weight="600" fill="#1B2336">Sähköposti</text>
  <text x="714" y="280" font-size="10.3" fill="#5A6478">lähettää yhteenvedon</text>
  <rect x="46" y="320" width="814" height="44" rx="10" fill="#FFFBEC" stroke="#F2D98E" stroke-width="1.3"/>
  <use href="#cls-clock" x="62" y="332" width="20" height="20" style="color:#C79100"/>
  <text x="90" y="340" font-size="11.5" font-weight="700" fill="#8A6A00">Ajastettu ja itsenäinen</text>
  <text x="90" y="356" font-size="11.5" fill="#5A4A1E">Ajastus tekee järjestelmästä automaattisen. Tilannekohtainen työkaluvalinta tekee siitä agenttimaisen.</text>
</svg>
<figcaption style="font-size:13px;color:#5A6478;margin-top:10px">Esimerkki yksinkertaisesta agentista: 4 solmua peräkkäin, agentilla muutama työkalu. Tällaisen voit itse rakentaa.</figcaption>
</figure>

## n8n:n perusteet — solmut, yhteydet ja triggerit

Kun avaat n8n:n ensimmäistä kertaa, näet tyhjän kankaan. Kaikki alkaa **triggeristä** eli solmusta, joka käynnistää työnkulun. Triggeri voi olla esimerkiksi ajastin, kuten ”joka maanantai klo 8”, webhook, kuten ”kun joku lähettää viestin”, tai manuaalinen käynnistys, kuten ”kun painan käynnistä”. Ilman triggeriä työnkulku ei lähde liikkeelle.

Triggerin jälkeen lisäät **toimintasolmuja**. Jokainen solmu saa tietoa edelliseltä solmulta ja antaa sitä seuraavalle. Työnkulku voi esimerkiksi vastaanottaa viestin, pyytää kielimallia luokittelemaan sen ja ohjata tuloksen oikeaan käsittelyyn. Tämä on tekoälyavusteinen työnkulku, mutta ei vielä välttämättä agentti. Tällä kurssilla agentilta vaaditaan, että kielimalli valitsee seuraavan toiminnon tai työkalun tilanteen ja havaintojen perusteella — ohjauskehyksen asettamissa rajoissa.

n8n:ssä on valmiita solmuja esimerkiksi taulukoille, viesteille, tiedostoille, tietokannoille ja kielimalleille. Sinun ei tarvitse ohjelmoida yhteyksiä käsin. Sinun tehtäväsi on päättää, mitä tietoa saa käyttää, minkä valinnan kielimalli tekee ja mitä järjestelmä saa valinnan jälkeen tehdä.

<figure class="ai-demo"><span class="ai-demo__tag">// data virtaa solmusta toiseen — jokainen solmu tekee yhden asian</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:280px">
  <div class="l26-wrap">
    <div class="l26-wire"></div>
    <div class="l26-node n1"><b>▶</b>Trigger<span>uusi viesti</span></div>
    <div class="l26-node n2"><b>✦</b>tekoälysolmu<span>päättely</span></div>
    <div class="l26-node n3"><b>◇</b>IF-solmu<span>turvatarkistus</span></div>
    <div class="l26-node n4"><b>✉</b>Toiminto<span>lähetä vastaus</span></div>
    <div class="l26-lbl"><span class="l26-s s1">data: ”Mihin aikaan avaatte?”</span><span class="l26-s s2">data: vastausluonnos</span><span class="l26-s s3">data: tarkistettu ✓</span><span class="l26-s s4">data: lähetetty käyttäjälle ✓</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">n8n-työnkulku on putki: triggeri käynnistää, ja data kulkee solmulta toiselle. Pelkkä putki ei ole agentti. Agenttimaisuus syntyy kohdassa, jossa kielimalli valitsee rajatuista vaihtoehdoista seuraavan toiminnon havaintonsa perusteella.</figcaption></figure>
<style>
.l26-wrap{position:relative;width:560px;height:240px;font-family:var(--font-mono)}
.l26-wire{position:absolute;left:30px;right:30px;top:104px;height:3px;background:repeating-linear-gradient(90deg,#46c7cf 0 9px,#232C44 9px 22px);animation:l26flow 1.1s linear infinite}
@keyframes l26flow{to{background-position:22px 0}}
.l26-node{position:absolute;top:62px;z-index:2;width:112px;display:flex;flex-direction:column;align-items:center;gap:2px;text-align:center;font-size:11.5px;color:#FFFFFF;background:#11182A;border:2px solid #2B3552;border-radius:12px;padding:9px 6px}
.l26-node b{font-size:15px;color:oklch(0.72 0.13 208)}
.l26-node span{font-size:10px;color:#B9C2DA}
.l26-node.n1{left:0;animation:l26n1 8s infinite}
.l26-node.n2{left:149px;animation:l26n2 8s infinite}
.l26-node.n3{left:298px;animation:l26n3 8s infinite}
.l26-node.n4{left:447px;animation:l26n4 8s infinite}
@keyframes l26n1{0%,2%,16%,100%{border-color:#2B3552;box-shadow:none}5%,12%{border-color:oklch(0.72 0.13 208);box-shadow:0 0 14px oklch(0.66 0.13 208/.5)}}
@keyframes l26n2{0%,26%,42%,100%{border-color:#2B3552;box-shadow:none}29%,38%{border-color:oklch(0.72 0.13 208);box-shadow:0 0 14px oklch(0.66 0.13 208/.5)}}
@keyframes l26n3{0%,52%,68%,100%{border-color:#2B3552;box-shadow:none}55%,64%{border-color:oklch(0.72 0.13 208);box-shadow:0 0 14px oklch(0.66 0.13 208/.5)}}
@keyframes l26n4{0%,78%,94%,100%{border-color:#2B3552;box-shadow:none}81%,90%{border-color:oklch(0.72 0.13 208);box-shadow:0 0 14px oklch(0.66 0.13 208/.5)}}
.l26-lbl{position:absolute;left:0;right:0;top:158px;height:34px}
.l26-s{position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;font-size:11.5px;color:#EAEEF8;background:#0E1422;border:1px solid #232C44;border-radius:999px;padding:5px 13px;opacity:0}
.l26-s.s1{animation:l26s1 8s infinite}.l26-s.s2{animation:l26s2 8s infinite}.l26-s.s3{animation:l26s3 8s infinite}.l26-s.s4{animation:l26s4 8s infinite}
@keyframes l26s1{0%,1%{opacity:0}4%,22%{opacity:1}26%,100%{opacity:0}}
@keyframes l26s2{0%,27%{opacity:0}31%,48%{opacity:1}52%,100%{opacity:0}}
@keyframes l26s3{0%,53%{opacity:0}57%,74%{opacity:1}78%,100%{opacity:0}}
@keyframes l26s4{0%,79%{opacity:0}83%,97%{opacity:1}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l26-node,.l26-s,.l26-wire{animation:none}
.l26-s.s4{opacity:1}}
</style>

**Pysähdy hetkeksi:** Miten agentin kaikki kuusi rakennusosaa toteutuvat suunnitelmassasi? Mieti vastuita ennen solmuja: yksi solmu, sääntö tai palvelu voi kattaa useita kohtia.

## Agentin kuusi rakennusosaa n8n:ssä

Palataan hetkeksi tunnin 19 arkkitehtuuriin ja katsotaan, miten sen vastuut voidaan toteuttaa n8n:ssä tai kuvata dokumentoidussa suunnittelupolussa. Tunnilla 27 dokumentoit ensin kielimallin ja agentin ohjauskehyksen rajan ja käytät kuutta rakennusosaa kattavuuden tarkistuslistana. Tarkoitus ei ole pakottaa jokaista vastuuta yhteen lokeroon.

**Syötekäsittelijä** on triggerisolmu ja mahdolliset validointisolmut sen jälkeen. Jos rakennat chatbotin, triggeri voi olla webhook, joka vastaanottaa käyttäjän viestin. Heti sen jälkeen voit lisätä IF-solmun, joka tarkistaa esimerkiksi, onko viesti liian pitkä tai tyhjä. Tämä on samaa syötevalidointia, josta puhuttiin teoriassa. n8n:ssä se näkyy konkreettisena solmuna kankaalla.

**Päättelijä** on tekoälysolmu, esimerkiksi kielimallisolmu. Siihen kirjoitat **järjestelmäpromptin**, joka ohjaa agentin toimintaa. Tässä solmussa agentti ”ajattelee”: se saa käyttäjän viestin, mahdollisesti kontekstitietoa edellisistä solmuista sekä ohjeet siitä, miten sen pitää vastata tai toimia.

**Työkalujen suorittaja** tarkoittaa solmuja tai kuvattuja toimintoja, joilla agentti lukee rajattua tietoa tai vaikuttaa ympäristöönsä. Työkalu voi hakea hyväksytystä tietolähteestä, kirjoittaa taulukkoon tai valmistella viestin. Sopimus määrää, mitä se saa tehdä ja miten virhe käsitellään.

**Muisti ja konteksti** voidaan toteuttaa usealla tavalla. Yksinkertaisimmillaan voit tallentaa keskusteluhistorian rajattuun taulukkoon ja hakea sen jokaisen uuden viestin yhteydessä. n8n:ssä voi olla myös muistisolmuja tai muita tapoja säilyttää keskustelun kontekstia ja prosessin tilaa.

**Turvakerros** toteutuu IF-solmuilla, ehdoilla, validoinneilla ja hyväksyntäkohdilla. Voit esimerkiksi lisätä ehdon: ”Jos vastaus sisältää henkilötietoja, älä lähetä sitä eteenpäin.” Tai: ”Jos käyttäjä pyytää jotakin, mikä ei kuulu agentin tehtävään, vastaa kohteliaasti kieltäytymällä.” n8n:ssä nämä ovat konkreettisia haarautumia työnkulussa.

**Seuranta ja palautesilmukka** tarkoittavat lokitusta ja palautteen keräämistä. Lisää työnkulkuun solmu, joka tallentaa jokaisen tärkeän toiminnon esimerkiksi rajattuun taulukkoon tai tiedostoon: mitä käyttäjä kysyi, mitä agentti vastasi, mitä työkaluja käytettiin ja kauanko suoritus kesti. Näin näet jälkikäteen, miten agentti toimii, ja voit parantaa sitä.

## Iteratiivinen kehitys — rakenna pienestä isoon

Tämän tunnin tärkein periaate on: **aloita pienestä**. Rakenna ensin yksinkertaisin mahdollinen versio, joka tekee yhden asian oikein. Testaa se. Lisää vasta sen jälkeen seuraava ominaisuus. Tätä kutsutaan **iteratiiviseksi kehitykseksi**. Kokeneet käyttäjätkään eivät rakenna valmista tuotetta yhdellä kertaa.

Käytännössä tunnin 26 tavoite on **toimiva minimiversio**, jossa näkyy yksi aito agenttipäätös. Kielimalli saa esimerkiksi valita kahdesta rajatusta työkalusta, pyytää lisätietoa tai lopettaa tehtävän. Valinta ja sen tulos tallennetaan näkyvään suoritusjälkeen. Turvakerros, hyväksyntäportit ja viimeistely tehdään tunnilla 27. Jos projektisi etenee aina samaa polkua, kutsu sitä tässä vaiheessa tekoälyavusteiseksi työnkuluksi ja lisää agenttipäätös vain, jos tehtävä todella tarvitsee sellaisen.

Esimerkki iteratiivisesta rakentamisesta:

1. **Vaihe 1 — Varmista datavirta:** Manual Trigger → esimerkkisyöte. Testaa, että työnkulku käynnistyy ja syöte saapuu oikein.
2. **Vaihe 2 — Lisää rajattu päätös:** anna tekoälysolmulle kaksi sallittua toimintavaihtoehtoa ja rakenteinen tulos, esimerkiksi `hae_tietoa` tai `pyyda_lisatietoa`.
3. **Vaihe 3 — Toteuta valinta:** ohjaa tulos valittuun työkaluun tai haaraan. Tallenna valinta, työkalun tulos ja seuraava toiminto suoritusjälkeen.

Testaa jokaisen lisäyksen jälkeen, että kaikki toimii. Jos jokin menee rikki, tiedät tarkalleen, mikä muutos aiheutti ongelman. Tämä on paljon helpompaa kuin rakentaa koko työnkulku kerralla ja etsiä sen jälkeen vikaa kymmenestä eri solmusta.

**Pysähdy hetkeksi:** Kun lisäät uuden solmun, säännön tai palvelun työnkulkuusi, mieti aina: mistä vastuusta se huolehtii? Voiko sama toteutusosa kattaa syötekäsittelijän, päättelijän ja suunnittelijan, työkalujen suorittajan, muistin ja kontekstin, turvakerroksen tai seurannan ja palautesilmukan vastuuta — ja jääkö jokin olennainen vastuu vielä puuttumaan?

## Pohjapiirroksesta toteutukseen

Tällä tunnilla et aloita tyhjältä pöydältä. Sinulla on viisi pohjapiirrosta, jotka olet kerännyt edellisillä tunneilla. Niiden pohjalta tiedät jo:

- mitä ongelmaa agenttisi ratkaisee ja kenelle se on tarkoitettu — **pohjapiirros 1**
- mitä agentti muistaa ja millainen sen identiteetti on — **pohjapiirros 2**
- miten agentin havaittava toiminta etenee: ReAct-silmukkana vai eksplisiittisenä työnkulkuna — **pohjapiirros 3**
- mitä riskejä agenttiin liittyy ja miten ne torjutaan — **pohjapiirros 4**
- missä kohdissa ihminen on mukana — **pohjapiirros 5**

Tunnin alussa kokoat nämä viisi pohjapiirrosta yhdeksi suunnitelmaksi ja tarkistat, että ne sopivat yhteen. Sen jälkeen rakennat minimiversion: **triggeri + kielimallin tekemä rajattu valinta + vähintään yksi työkalu tai toiminto + näkyvä suoritusjälki**. Pohjapiirrosten 4 ja 5 sisältämät turvakerros ja ihmisen rooli viimeistellään tunnilla 27, kun testaat ja dokumentoit agentin.

Jos olet epävarma omasta projektistasi, voit arvioida vaikeustasoa seuraavien esimerkkien avulla:

**Taso 1 — FAQ-botti**

Yhteisö saa samoja kysymyksiä kymmeniä kertoja päivässä. Botti vastaa yleisimpiin kysymyksiin automaattisesti. Triggeri on viesti chat-kanavasta. Työnkulku lähettää viestin tekoälysolmulle, jolla on järjestelmäprompti ja FAQ-tietokanta kontekstina. Lopuksi vastaus lähetetään takaisin chattiin.

**Taso 2 — Sähköpostiyhteenvetoagentti**

Agentti lukee joka aamu klo 8 viimeisen 24 tunnin sähköpostit, tekee niistä yhteenvedon tekoälyllä ja lähettää yhteenvedon tiimikanavalle. Triggeri on ajastin. Työnkulku etenee näin: hae sähköpostit → kokoa yhteenveto → lähetä yhteenveto.

**Taso 3 — Tikettiagentti**

Asiakas lähettää viestin lomakkeella. Agentti luokittelee viestin, esimerkiksi tilaus, laskutus tai palaute. Sen jälkeen agentti luo tiketin rajattuun taulukkoon, vastaa asiakkaalle automaattisesti ja ilmoittaa oikealle tiimille. Jos viesti on kriittinen, se ohjataan ihmiselle hyväksyttäväksi. Tämä on esimerkki ihmisen osallistavasta rakenteesta.

## Kaksi tasavertaista toteutuspolkua

Tunnin lopussa sinulla pitäisi olla **testattava minimiversio** agentistasi. Tekninen polku osoittaa n8n:n suoritusnäkymällä, että yhteydet ja reititys toimivat käytetyssä ympäristössä. Dokumentoitu suunnittelupolku osoittaa kaavion, työkalusopimusten ja simuloitujen suoritusjälkien avulla, että suunnitelma on johdonmukainen. Jälkimmäinen ei kuitenkaan todista testaamattomien liitäntöjen tai käyttöoikeuksien toimivuutta.

Minimiversiossa tulee olla vähintään:

- **triggeri**, joka käynnistää työnkulun
- **tekoälysolmu**, joka valitsee tilanteen perusteella vähintään kahdesta sallitusta seuraavasta toiminnosta
- **työkalu tai toimintopolku**, jonka ohjauskehys antaa kielimallin käyttöön rajatuilla oikeuksilla
- **suoritusjälki**, josta näkyvät syöte, valittu toiminto, työkalun tulos ja seuraava vaihe

Lisäksi sinun kannattaa tunnin aikana kirjata muistiin:

- miten kielimallin ja ohjauskehyksen vastuut jakautuvat ja miten kaikki kuusi rakennusosaa tulevat katetuiksi
- mikä osa toimii jo
- mikä osa jäi kesken
- mitä pitää testata tai korjata tunnilla 27

**Tarkista lopuksi:** Käynnistyykö työnkulku? Kulkeeko data solmulta toiselle? Tuottaako tekoälysolmu järkevän vastauksen? Tekeekö toimintasolmu sen, mitä sen pitää tehdä? Tiedätkö, mitä korjaat tai lisäät seuraavalla tunnilla?

## Yhteenveto

Tämä tunti vie sinut suunnitelmasta testattavaan minimiversioon. Kokoat viisi pohjapiirrostasi yhteen, teet yhden tilanteen mukaan muuttuvan kielimallivalinnan ja näytät sen seuraukset suoritusjäljessä. Tekninen polku rakentaa tämän n8n:ssä. Dokumentoitu polku kuvaa rakenteen ja simuloi sen, mutta käyttää samassa kohdassa todellista kielimallipäätöstä.

Tunnin lopussa sinulla on toimiva perusversio, jonka päälle lisäät turvakerroksen, hyväksyntäportit, testauksen ja dokumentaation tunnilla 27. Tärkeintä ei ole rakentaa kaikkea valmiiksi yhdellä kertaa. Tärkeintä on saada ensimmäinen versio toimimaan, ymmärtää sen rakenne ja tietää, miten jatkat siitä eteenpäin.

> **Erota nämä:** Mitä kielimalli valitsee — ja mitkä solmut, säännöt, sopimukset tai palvelut muodostavat sitä ympäröivän agentin ohjauskehyksen?

---

## Lähteet ja tarkistuspäivä

- [NIST: Strengthening AI Agent Hijacking Evaluations](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations)
- [OWASP: Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
- [OWASP: Excessive Agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html)

Tarkistettu 15.7.2026.
