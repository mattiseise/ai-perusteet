# Anna konteksti — näin saat parempia vastauksia

## Johdanto: sama kysymys, aivan eri vastaukset

**Tämän tunnin rajaus:** Tunnilla 4 opit, mitä konteksti ja prompti tarkoittavat. Nyt viet taidon käytäntöön: rakennat uudelleen käytettävän promptin, annat lähdeaineiston, pilkot tehtävän ja dokumentoit vähintään yhden testatun parannuskierroksen omaa projektia varten.

Kuvittele tilanne. Sinulla on esseen aihe ”Tekoäly työssä”, ja pyydät tekoälyä auttamaan. Ensimmäisellä kerralla kirjoitat: ”Kerro tekoälystä.” Vastaus on yleinen eikä auta kovin paljon. Toisella kerralla kirjoitat: ”Kerro tekoälystä esseeseeni, jonka kohdeyleisö on toisen asteen opiskelijat.” Vastaus on jo parempi. Kolmannella kerralla kirjoitat: ”Kirjoita 500 sanan johdanto esseeseeni, jonka aihe on ’Tekoäly työssä’. Kohdeyleisö on toisen asteen opiskelijat, joilla ei ole teknistä taustaa. Aloita sillä, miten tekoäly muuttaa jokapäiväistä työtä.”

Jokainen kierros antaa tekoälylle lisää **kontekstia**, ja siksi jokainen vastaus on parempi kuin edellinen. Tämä ei ole magiaa, vaan järkevää viestintää: mitä tarkemmin kerrot, mitä tarvitset, sitä paremman vastauksen saat.

**Konteksti** tarkoittaa kaikkea sitä tietoa, jonka tekoäly tarvitsee ymmärtääkseen *sinun* tilanteesi. Kyse ei ole vain kysymyksestä yleisesti, vaan *sinun* kysymyksestäsi, *sinun* tavoitteistasi ja *sinun* käyttötarkoituksestasi. Tämä oppitunti opettaa, miten rakennat kontekstia käytännössä. Se on yksi tämän kurssin tärkeimmistä taidoista.

<figure class="ai-demo"><span class="ai-demo__tag">// jokainen kierros rakentuu edellisen päälle — vastaus tarkentuu</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:300px">
  <div class="l12-wrap">
    <div class="l12-row r1"><span class="l12-k">K1</span><span class="l12-p">”Tee esitelmän runko.”</span><div class="l12-qb"><i class="l12-qf q1"></i></div><span class="l12-ql">yleinen</span></div>
    <div class="l12-row r2"><span class="l12-k">K2</span><span class="l12-p">+ yleisö: lukiolaiset · kesto 5 min</span><div class="l12-qb"><i class="l12-qf q2"></i></div><span class="l12-ql">kohdennettu</span></div>
    <div class="l12-row r3"><span class="l12-k">K3</span><span class="l12-p">+ konkreettinen esimerkki joka kohtaan</span><div class="l12-qb"><i class="l12-qf q3"></i></div><span class="l12-ql">konkreettinen</span></div>
    <div class="l12-row r4"><span class="l12-k">K4</span><span class="l12-p">+ muotoile muistikorteiksi</span><div class="l12-qb"><i class="l12-qf q4"></i></div><span class="l12-ql l12-ok">✓ käyttövalmis</span></div>
    <span class="l12-note">älä aloita alusta — tarkenna jatkopromptilla</span>
  </div>
</div>
<figcaption class="ai-demo__cap">Ensimmäinen vastaus on pohja, ei lopputulos. Jokainen jatkokierros lisää kontekstia — yleisön, esimerkit, muodon — ja vastauksen käyttökelpoisuus kasvaa pykälä kerrallaan ilman, että aloitat alusta.</figcaption></figure>
<style>
.l12-wrap{position:relative;width:560px;height:262px;font-family:var(--font-mono)}
.l12-row{position:absolute;left:0;right:0;display:flex;align-items:center;gap:10px;background:#11182A;border:1.5px solid #2B3552;border-radius:11px;padding:9px 12px;opacity:0}
.l12-row.r1{top:0;animation:l12r1 13s infinite}
.l12-row.r2{top:56px;animation:l12r2 13s infinite}
.l12-row.r3{top:112px;animation:l12r3 13s infinite}
.l12-row.r4{top:168px;animation:l12r4 13s infinite;border-color:#7FD0A8}
@keyframes l12r1{0%,2%{opacity:0;transform:translateY(6px)}6%,96%{opacity:1;transform:translateY(0)}100%{opacity:0}}
@keyframes l12r2{0%,22%{opacity:0;transform:translateY(6px)}26%,96%{opacity:1;transform:translateY(0)}100%{opacity:0}}
@keyframes l12r3{0%,44%{opacity:0;transform:translateY(6px)}48%,96%{opacity:1;transform:translateY(0)}100%{opacity:0}}
@keyframes l12r4{0%,66%{opacity:0;transform:translateY(6px)}70%,96%{opacity:1;transform:translateY(0)}100%{opacity:0}}
.l12-k{font-size:10.5px;font-weight:700;letter-spacing:.06em;color:#1d1230;background:#c9b7f1;border-radius:7px;padding:3px 7px}
.l12-p{flex:1;font-size:11.5px;line-height:1.35;color:#EAEEF8}
.l12-qb{width:120px;height:9px;border-radius:99px;background:#0B0F1A;border:1px solid #232C44;overflow:hidden}
.l12-qf{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,oklch(0.6 0.14 305),#7FD0A8)}
.l12-qf.q1{width:0;animation:l12q1 13s infinite}
.l12-qf.q2{width:0;animation:l12q2 13s infinite}
.l12-qf.q3{width:0;animation:l12q3 13s infinite}
.l12-qf.q4{width:0;animation:l12q4 13s infinite}
@keyframes l12q1{0%,5%{width:0}10%,100%{width:25%}}
@keyframes l12q2{0%,25%{width:0}30%,100%{width:50%}}
@keyframes l12q3{0%,47%{width:0}52%,100%{width:75%}}
@keyframes l12q4{0%,69%{width:0}74%,100%{width:95%}}
.l12-ql{width:96px;text-align:right;font-size:10.5px;color:#B9C2DA}
.l12-ok{color:#7FD0A8;font-weight:600}
.l12-note{position:absolute;left:0;right:0;top:228px;text-align:center;font-size:11.5px;color:#c9b7f1;opacity:0;animation:l12note 13s infinite}
@keyframes l12note{0%,76%{opacity:0}82%,96%{opacity:1}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l12-row,.l12-qf,.l12-note{animation:none}
.l12-row,.l12-note{opacity:1}
.l12-qf.q1{width:25%}.l12-qf.q2{width:50%}.l12-qf.q3{width:75%}.l12-qf.q4{width:95%}}
</style>

## Konteksti: miksi se on tärkeää?

Konteksti on kaikkea tietoa, jota tekoäly tarvitsee sinusta ja tilanteestasi. Mitä haluat tehdä ja miksi? Kuka olet ja mikä on taustasi? Mihin käytät vastausta? Ketkä lukevat tai käyttävät sitä? Mitä muuta tekoälyn olisi tärkeää tietää? Nämä kaikki asiat muodostavat kontekstin.

Esimerkiksi pyyntö ”Kirjoita dokumentaatio funktiolle” on kysymys, mutta vastaus voi olla hyvin erilainen riippuen kontekstista. Funktio voidaan dokumentoida koodarille, jolloin dokumentaatio on tekninen ja sisältää yksityiskohtia. Se voidaan dokumentoida opiskelijalle, jolloin teksti on opettavainen ja etenee vaihe vaiheelta. Se voidaan dokumentoida myös käyttäjälle, jolloin teksti on yksinkertainen eikä sisällä teknistä jargonia.

Ilman kontekstia tekoäly tekee oletuksia ja arvailee. Kontekstin avulla se pystyy vastaamaan sopivalla tasolla. Esimerkiksi pyyntö ”Dokumentaatio on 15-vuotiaalle opiskelijalle, joka ei osaa koodata. Haluan, että hän ymmärtää, miten funktio toimii” ohjaa tekoälyä kirjoittamaan selkeämmin ja opetuksellisemmin.

> **Pysähdy hetkeksi:** Ajattele viimeisintä kertaa, kun käytit tekoälyä. Annoitko sille riittävästi kontekstia? Mitä muuta olisit voinut kertoa, vaikka asia olisi tuntunut sinulle itsestään selvältä?

Konteksti on tärkeää neljällä tavalla:

1. **Tarkkuus:** Kohdistettu vastaus on parempi kuin yleinen vastaus. ”Tekoäly työssä” voi tarkoittaa melkein mitä tahansa, mutta ”tekoäly opiskelijan arjessa” on jo paljon tarkempi aihe.
2. **Sopiva taso:** Konteksti kertoo, millä tasolla vastaus pitää kirjoittaa. ”Selitä tekoäly” on epäselvä pyyntö, mutta ”selitä tekoäly 15-vuotiaalle, joka ei osaa ohjelmointia” on selkeä.
3. **Käyttökelpoinen muoto:** Konteksti kertoo, mitä aiot tehdä vastauksella. ”Auta minua esseen kirjoittamisessa” tuottaa erilaisen vastauksen kuin ”auta minua koodiprojektissa”.
4. **Oikea sisältö:** Konteksti vähentää turhia korjauskierroksia. Kun kerrot alusta alkaen, mitä tarvitset, tekoäly osaa todennäköisemmin antaa hyödyllisen vastauksen heti.

## Kuinka antaa kontekstia: käytännön esimerkki

Vertaa näitä kolmea pyyntöä:

**Huono pyyntö:**
”Auta minua historian esseen kanssa.”

**Parempi pyyntö:**
”Kirjoita johdanto historian esseeseeni. Aihe on ’Digitaalinen vallankumous’. Kohderyhmä on 10. luokan opiskelijat.”

**Paras pyyntö:**
”Kirjoita 200 sanan johdanto historian esseeseeni. Aihe on ’Digitaalinen vallankumous’. Kohderyhmä on toisen asteen opiskelijat, joilla on perustiedot historiasta mutta ei erityistä tekniikan osaamista. Haluan, että lukija ymmärtää, miksi aihe on tärkeä. Johdannon pitää päättyä selkeään aiheväitteeseen.”

Kolmannessa pyynnössä kerrot selkeästi, mitä haluat: johdannon, pituuden, aiheen, kohderyhmän, lukijoiden taustan, tekstin tarkoituksen ja lopputuloksen. Nyt tekoäly ymmärtää paremmin, mitä tarvitset.

> **Pysähdy hetkeksi:** Mitä kontekstia olisit itse lisännyt edelliseen pyyntöön? Mitä siitä jäi vielä puuttumaan?

## Lähdeaineiston antaminen: tekstit, koodit ja dokumentit

Usein sinulla on olemassa olevaa aineistoa, jota haluat tekoälyn käsittelevän. Se voi olla esimerkiksi artikkeli, jonka haluat yksinkertaistaa opiskelijoille, tai koodi, jossa on virhe. Vastuullisena käyttäjänä et pyydä tekoälyä selittämään aineistoa, jota et ole antanut sille nähtäväksi. Annat ensin materiaalin ja sen jälkeen selkeän promptin.

**Esimerkki 1:** Sinulla on tiedeartikkeli kvanttimekaniikasta, jonka haluat yksinkertaistaa 15-vuotiaalle. Voit kopioida artikkelista katkelman ja sanoa: ”Tässä on teksti kvanttimekaniikasta. Kirjoita se uudelleen 15-vuotiaalle sopivaksi. Käytä esimerkkejä jokapäiväisestä elämästä.”

Vaihtoehtoisesti voit antaa pääkohdat ja sanoa: ”Artikkeli käsittelee kvanttimekaniikkaa. Pääkohdat ovat nämä: elektronit voivat olla useissa paikoissa samanaikaisesti, ja mittaaminen vaikuttaa tulokseen. Selitä nämä kahdessa lauseessa 15-vuotiaalle.”

**Esimerkki 2:** Sinulla on ryhmän tekemä raportti, jota haluat parantaa. Annat raportin tekoälylle ja sanot: ”Tässä on ryhmän raportti. Paranna sitä seuraavien kohtien osalta: 1) johdanto ei selitä aihetta riittävästi, 2) johtopäätökset ovat liian lyhyet, 3) lähdeviitteet puuttuvat.”

Tärkeä periaate on tämä: **anna ensin aineisto, sitten prompti**. Kun tekoäly näkee konkreettisen tekstin, se voi antaa tarkemman ja aineistoon perustuvan vastauksen. Sen ei tarvitse arvailla.

> **Pysähdy hetkeksi:** Missä opiskelun tilanteissa sinulla on aineistoja, joita haluaisit tekoälyn käsittelevän? Voisiko kyse olla esimerkiksi tenttiartikkeleista, muiden kirjoittamasta koodista tai vertaisarvioinnista?

## Tehtävän pilkkominen: iso ongelma pienempiin osiin

Vastuulliselle käyttäjälle tärkeä taito on **pilkkominen**. Kun tehtävä on iso ja monimutkainen, älä pyydä tekoälyä ratkaisemaan kaikkea yhdellä kertaa. Jaa tehtävä pienempiin osiin, joista jokainen on helpompi hallita.

Esimerkiksi pyyntö ”Kirjoita raportti, jossa vertaillaan kolmea eri menetelmää data-analyysiin ja sisällytetään omat tulkinnat sekä johtopäätökset” on laaja tehtävä. Sen voi pilkkoa näin:

1. Pyydä ensin: ”Kirjoita yhteenveto data-analyysin perusteista. Mitä data-analyysi tarkoittaa?”
2. Pyydä seuraavaksi: ”Kuvaile kolme data-analyysin menetelmää ja niiden perusidea. Kirjoita yksi lyhyt kappale kustakin.”
3. Pyydä sitten: ”Lisää vertailu: mitkä ovat kunkin menetelmän edut ja haitat?”
4. Jatka: ”Miten nämä menetelmät sopivat opiskelijan projektiin?”
5. Lopuksi pyydä: ”Kirjoita johtopäätös. Mitä tästä vertailusta voi oppia?”

Jokainen osio on pienempi ja selkeämpi. Tekoäly antaa yleensä parempia vastauksia, kun yksi pyyntö kohdistuu yhteen asiaan. Kun olet saanut kaikki osat, voit yhdistää ne kokonaiseksi raportiksi.

Pilkkominen säästää aikaa, koska vastaukset ovat tarkempia. Jokainen osa keskittyy yhteen asiaan, eikä tekoäly sekoita tehtävän eri tavoitteita keskenään.

> **Pysähdy hetkeksi:** Mitä hyötyä on siitä, että pilkot ongelman osiin tekoälylle? Mitä riskejä syntyy, jos pyydät tekoälyä tekemään kaiken kerralla?

## Iteraatio ja tarkentaminen: kierros kerrallaan parempi vastaus

Kun tekoäly antaa ensimmäisen vastauksen, se on usein vasta pohja. Vastuullinen käyttäjä parantaa vastausta seuraavilla kierroksilla.

1. **Ensimmäinen pyyntö:** kirjoita alkuperäinen kysymys tai tehtävänanto.
2. **Lue vastaus:** tarkista, vastaako tekoäly siihen, mitä tarvitsit.
3. **Arvioi:** puuttuuko vastauksesta jotain olennaista?
4. **Jos kyllä:** tarkenna pyyntöä ja pyydä uusi versio.
5. **Jos ei:** vastaus on valmis käytettäväksi tai muokattavaksi.

Esimerkiksi haluat oppia Python-ohjelmoinnista tenttiin. Voit edetä näin:

1. **Kierros 1:** ”Kerro Python-muuttujista.” Saat perustiedot.
2. **Kierros 2:** ”Lisää esimerkkejä muuttujista. Näytä, miten muuttujat nimetään oikein ja miksi se on tärkeää.” Saat enemmän esimerkkejä.
3. **Kierros 3:** ”Lisää yleisiä virheitä. Mitä muuttujien kanssa voi tehdä väärin?” Saat tietoa tavallisista ongelmista.
4. **Kierros 4:** ”Tee minulle lopuksi viisi harjoituskysymystä, joissa opiskelijat saattavat vastata väärin.” Saat testitehtäviä.

Jokainen kierros rakentuu edellisen päälle. Tämä on tehokas tapa työskennellä: täydennät vastausta vaihe vaiheelta ilman, että aloitat joka kerta alusta.

Tärkeä periaate on tämä: **jatkoprompti on tarkempi kuin perusprompti**. Älä kirjoita vain ”paranna tätä”, vaan kerro tarkasti, mitä haluat lisätä tai muuttaa. Esimerkiksi: ”Lisää kolme esimerkkiä, lyhennä johdantoa ja muuta kieli opiskelijalle sopivaksi.”

> **Pysähdy hetkeksi:** Milloin iteraatiosta olisi hyötyä omassa oppimisessasi? Voisiko sitä käyttää esimerkiksi tenttiin valmistautumisessa, ryhmätyössä tai esseen kirjoittamisessa?

## Kontekstin rakentaminen: käytännön esimerkki

Katsotaan koko prosessia yhden tapauksen kautta alusta loppuun.

**Tehtävä:** Haluat tekoälyn auttavan sinua valmistautumaan kokeeseen, jonka aihe on sinulle vaikea.

**Kierros 1 — yksinkertainen kysymys:**

Pyyntö: ”Auta minua valmistautumaan tenttiin.”
Tulos: yleinen ohjeistus, joka ei ole vielä kovin tarkasti sinun tilanteeseesi sopiva.

**Kierros 2 — lisää kontekstia:**

Pyyntö: ”Koe on biologiasta. Aiheita ovat solu, perimä ja evoluutio. Minulla on yksi viikko aikaa. Opin parhaiten esimerkkien avulla.”
Tulos: parempi vastaus, mutta vielä melko yleinen.

**Kierros 3 — vielä tarkempi pyyntö:**

Pyyntö: ”Koe on biologiasta. Aiheita ovat solu, perimä ja evoluutio. Minulla on yksi viikko aikaa. Opin parhaiten todellisen maailman esimerkeistä. Haluan viikko-ohjelman, jossa jokaiselle päivälle on 30 minuutin opiskelusessio. Jokaisessa sessiossa pitää olla aihe, 2–3 konkreettista esimerkkiä ja yksi testikysymys.”
Tulos: selkeä viikko-ohjelma, joka sopii paremmin juuri sinun tarpeeseesi.

**Kierros 4 — pilko osiin:**

Pyyntö: ”Aloitetaan maanantaista. Aihe on solun rakenne. Mitä olennaista opiskelijan pitää tietää? Anna kolme konkreettista esimerkkiä siitä, miten solut näkyvät jokapäiväisessä elämässä.”
Tulos: tarkasti rajattu maanantain opiskelusessio.

Koko prosessi rakentui kontekstin avulla kierros kierrokselta. Lopputuloksena saat käyttökelpoisen opiskelusuunnitelman, joka sopii sinulle paremmin kuin yleinen lista.

## Kohti omaa projektia

**Kontekstin rakentaminen** on taito, joka tekee tekoälystä oikeasti hyödyllisen työkalun. Tällä tunnilla harjoittelet, miten taustatiedot, jatkokysymykset ja iteraatio parantavat tekoälyn vastauksia.

Tehtävissä rakennat itsellesi **promptauspankin** eli **rakennuspalikka 1:n**. Se on kokoelma 5–7 omaa, testattua promptia, joita voit käyttää uudelleen. Tämä pankki toimii myöhemmin bottisi järjestelmäpromptin raaka-aineena. Kun tunnilla 17 kirjoitat botille pääohjeen, voit hyödyntää tässä pankissa toimiviksi todettuja rakenteita.

Seuraavaksi suunnittelet, kenelle bottisi on tarkoitettu ja mitä sen pitää tehdä.

## Yhteenveto: konteksti on vastuullisen käyttäjän taito

Vastuulliselle käyttäjälle kontekstin rakentaminen on selkeä prosessi:

1. **Aloita selkeällä tavoitteella.** Mitä haluat tehdä? Kirjoita yksinkertainen ja tarkka kysymys.
2. **Anna taustatiedot.** Mikä on tilanteesi? Mitä tarvitset? Kuka olet? Kenelle vastaus tulee?
3. **Jaa isot tehtävät osiin.** Pilko laajat tehtävät pienempiin vaiheisiin, joista jokainen on hallittava.
4. **Liitä olemassa oleva aineisto.** Anna tekstit, koodit tai asiakirjat tekoälyn nähtäväksi ennen kuin pyydät sitä käsittelemään niitä.
5. **Iteroi ja tarkenna.** Käytä jatkokysymyksiä, jotta vastauksesta tulee tarkempi, hyödyllisempi ja paremmin tarkoitukseen sopiva.
6. **Testaa ja arvioi.** Tarkista jokaisen kierroksen jälkeen, auttaako vastaus sinua oikeasti oppimisessa tai työn tekemisessä.

Tämä prosessi vaatii hieman enemmän aikaa ensimmäisen pyynnön laatimiseen, mutta säästää aikaa myöhemmin. Kun konteksti on kunnossa, tarvitset vähemmän korjauskierroksia ja saat käyttökelpoisempia vastauksia. Seuraavalla tunnilla harjoittelet tätä käytännössä oikeissa opiskelun tehtävissä.

---

## Lähteet ja tarkistuspäivä

- [NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [UNESCO: Recommendation on the Ethics of Artificial Intelligence](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence)
- [European Commission: GDPR principles](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr/overview-principles/what-data-can-we-process-and-under-which-conditions_en)

Tarkistettu 15.7.2026.
