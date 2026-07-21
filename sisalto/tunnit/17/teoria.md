# Oppitunti 17 — Yhdistä rakennuspalikat ja aloita botin rakentaminen

## Mitä tällä tunnilla tapahtuu?

Tähän mennessä olet kerännyt kolme **rakennuspalikkaa** ja tehnyt toteutuspäätöksen. Tällä tunnilla yhdistät ne ensimmäiseksi arvioitavaksi versioksi. Teknisen toteutuspolun valinnut rakentaa botin saatavilla olevalle alustalle. Dokumentoidun suunnittelupolun valinnut tuottaa arkkitehtuurin ja simuloidun suoritusjäljen, josta käy täsmällisesti ilmi, mitä valmis järjestelmä tekisi ja mikä jää toteuttamatta.

Tällä tunnilla et opiskele enää uusia teoreettisia käsitteitä. Sen sijaan siirrät suunnitelman järjestelmäpromptiksi ja toteutuskuvaukseksi. Ensimmäisen version ei tarvitse olla täydellinen. Tärkeintä on saada aikaan näyttöä, jota voit testata, korjata ja puolustaa Apuri-botin viimeistelytunnilla. Polut ovat samanarvoisia, mutta ne eivät todista samoja asioita.

## Mikä on järjestelmäprompti?

**Järjestelmäprompti** on botin pääohje, jonka annat valitulle alustalle tai liität suunnittelupolun toteutuskuvaukseen. Se määrittää, miten botin on tarkoitus käyttäytyä keskusteluissa. Käyttäjä ei yleensä näe järjestelmäpromptia, mutta arvioinnissa se kuuluu näkyvään dokumentaatioon.

Voit ajatella järjestelmäpromptia botin **työsopimuksena**: kuka botti on, mikä sen tehtävä on ja missä sen rajat kulkevat.

Työsopimuksen tavoin hyvä järjestelmäprompti vastaa neljään kysymykseen. Ensin se kertoo, kuka botti on: mikä rooli sillä on ja millaisena se esittäytyy käyttäjälle. Toiseksi se kertoo, mitä botti tekee — mikä on sen varsinainen tehtävä ja missä järjestyksessä se etenee, kun käyttäjä ottaa yhteyttä. Kolmanneksi se määrittää, miten botti puhuu: teitittelee vai sinuttelee, vastaa lyhyesti vai perusteellisesti, käyttää ammattitermejä vai selittää ne auki.

Neljäs kysymys on se, joka useimmin unohtuu ja joka useimmin ratkaisee botin laadun: mitä botti **ei** tee. Rajat ja kiellot kertovat, mihin kysymyksiin botin ei pidä vastata, milloin sen pitää ohjata käyttäjä ihmisen puheille ja mitä sen ei pidä väittää tietävänsä. Ilman tätä osaa botti vastaa mielellään kaikkeen, myös siihen mistä se ei tiedä mitään.

## Rakennuspalikat järjestelmäpromptiksi

Kolme rakennuspalikkaasi muuttuvat järjestelmäpromptiksi seuraavasti:

| Rakennuspalikka | Mihin osaan järjestelmäpromptia? |
| --- | --- |
| **1: Promptikortti** | Testattu rakenne ja kieli. Käytä pääohjeessa ratkaisuja, joiden vaikutuksen osoitit Promptikortti-tunnilla. |
| **2: Botin määrittely** | Sisältö. Kuusi osaa eli nimi, kohderyhmä, tarkoitus, persoona, työnkulku ja rajat muuttuvat suoraan järjestelmäpromptin kappaleiksi. |
| **3: Tietopohja ja testisuunnitelma** | Hyväksytty aineisto ja kolme ennalta kirjoitettua testiä. Tekninen polku kytkee aineiston alustan tietopohjaksi. Suunnittelupolku kuvaa hakutavan, käyttöoikeusrajauksen ja mallille annettavat lähdekatkelmat. Järjestelmäprompti kertoo, miten löydettyä lähdettä käytetään, mutta ei korvaa hakua tai käyttöoikeuksia. |

Järjestelmäprompti ei ole neljäs rakennuspalikka. Se on näiden kolmen rakennuspalikan päätöksistä koottu toteutusohje.

## Esimerkki: rakennuspalikoista järjestelmäpromptiksi

Alla on yksinkertainen esimerkki siitä, miten botin määrittelyn sisältö muuttuu järjestelmäpromptiksi. Ota se malliksi, mutta älä kopioi sitä sellaisenaan.

### Botin määrittelyn sisältö eli rakennuspalikka 2

> **Botin nimi:** Treenikaveri
> **Kohderyhmä:** Opiskelija, joka aloittaa salitreenin ja haluaa suunnitella oman viikko-ohjelman
> **Tarkoitus:** Ohjata käyttäjää kokoamaan itselleen sopiva treeniviikko kuuden vaiheen kautta
> **Persoona:** Kannustava, käytännönläheinen, kysyvä, ei jargonia
> **Työnkulku:** 1) Tavoite → 2) Lähtötaso ja kokemus → 3) Käytettävissä olevat päivät → 4) Liikkeiden valinta → 5) Viikko-ohjelman kokoaminen → 6) Palautuminen ja seuranta
> **Rajat:** Ei kirjoita ohjelmaa valmiiksi käyttäjän puolesta kysymättä mitään, ei anna lääketieteellisiä neuvoja, ei käsittele muita aiheita kuin treenausta

### Sama järjestelmäpromptina

> Olet **Treenikaveri**. Autat opiskelijaa, joka aloittaa salitreenin, kokoamaan itselleen sopivan treeniviikon.
>
> **Työnkulkusi:** Ohjaat käyttäjää aina järjestyksessä kuuden vaiheen läpi: (1) tavoite, (2) lähtötaso ja kokemus, (3) käytettävissä olevat päivät, (4) liikkeiden valinta, (5) viikko-ohjelman kokoaminen ja (6) palautuminen ja seuranta. Et siirry seuraavaan vaiheeseen ennen kuin nykyinen vaihe on käsitelty.
>
> **Tapasi puhua:** Olet kannustava, käytännönläheinen ja kysyvä. Pyydät käyttäjältä konkreettisia vastauksia etkä hyväksy ympäripyöreitä vastauksia sellaisenaan. Et käytä vaikeaa jargonia. Käytät treenauksen omia termejä, kuten sarja, toisto, palautuminen ja viikko-ohjelma.
>
> **Et koskaan:** kokoa ohjelmaa valmiiksi käyttäjän puolesta kysymättä mitään, anna lääketieteellisiä neuvoja tai käsittele muita aiheita kuin treenausta. Jos käyttäjä pyytää näitä, ohjaa hänet ystävällisesti takaisin aiheeseen tai oikean asiantuntijan puoleen.
>
> **Tietopohja:** Käytä bottiin ladattuja dokumentteja referenssinä, kun ohjaat käyttäjää.

Huomaa, että botin määrittelyssä sisältö on kuvailevassa muodossa, kun taas järjestelmäpromptissa puhutaan botille suoraan: "Olet…", "Työnkulkusi…" ja "Et koskaan…". Tämä on tärkein muunnos: **kuvaileva määrittely muutetaan suoraksi ohjeeksi botille**.

<figure class="ai-demo"><span class="ai-demo__tag">// kolme rakennuspalikkaa kasaan — kuvailevasta määrittelystä suoraksi ohjeeksi</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:300px">
  <div class="l17-wrap" data-once>
    <div class="l17-blk b1"><b>1 · Promptikortti</b><span>toimivat muotoilut</span></div>
    <div class="l17-blk b2"><b>2 · Botin määrittely</b><span>”Botin nimi: Treenikaveri”</span></div>
    <div class="l17-blk b3"><b>3 · Tietopohja ja testit</b><span>2–4 dokumenttia, kolme testiä</span></div>
    <span class="l17-morph">kuvaileva → suora ohje</span>
    <div class="l17-bot"><span class="l17-bhead">JÄRJESTELMÄPROMPTI</span>
      <span class="l17-line n1">Kirjoita selkeästi, kysy tarkentavia kysymyksiä.</span>
      <span class="l17-line n2"><b>”Olet Treenikaveri.”</b> Ohjaat kuusi vaihetta järjestyksessä.</span>
      <span class="l17-line n3">Käytä ladattuja dokumentteja referenssinä.</span>
      <span class="l17-ready">✓ botti valmis testattavaksi</span>
    </div>
  </div>
</div>
<figcaption class="ai-demo__cap">Palikat eivät kelpaa botille sellaisenaan: promptikortista tulee testattu rakenne, määrittelystä sisältö ja tietopohjasta asiantuntemus. Ratkaiseva muunnos on puhutella bottia suoraan — ”Botin nimi: Treenikaveri” muuttuu muotoon ”Olet Treenikaveri”.</figcaption></figure>
<style>
.l17-wrap{position:relative;width:560px;height:262px;font-family:var(--font-mono);animation:l17wrapw 18s 1 forwards}
.l17-blk{position:absolute;left:0;width:190px;display:flex;flex-direction:column;gap:2px;background:#1E2740;border:1.5px solid #44517A;border-radius:11px;padding:9px 12px}
.l17-blk b{font-size:12px;color:#FFFFFF}
.l17-blk span{font-size:10.5px;color:#B9C2DA}
.l17-blk.b1{top:12px;animation:l17b1 18s infinite}
.l17-blk.b2{top:96px;animation:l17b2 18s infinite}
.l17-blk.b3{top:180px;animation:l17b3 18s infinite}
@keyframes l17b1{0%,8%{transform:translateX(0);opacity:1}20%,97%{transform:translateX(108px);opacity:0}100%{transform:translateX(0);opacity:1}}
@keyframes l17b2{0%,28%{transform:translateX(0);opacity:1}40%,97%{transform:translateX(108px);opacity:0}100%{transform:translateX(0);opacity:1}}
@keyframes l17b3{0%,48%{transform:translateX(0);opacity:1}60%,97%{transform:translateX(108px);opacity:0}100%{transform:translateX(0);opacity:1}}
.l17-morph{position:absolute;left:198px;top:74px;font-size:10.5px;letter-spacing:.05em;color:#c9b7f1;transform:rotate(-90deg) translateX(-50%);transform-origin:left top;opacity:0;animation:l17morph 18s infinite}
@keyframes l17morph{0%,30%{opacity:0}36%,60%{opacity:1}66%,100%{opacity:0}}
.l17-bot{position:absolute;right:0;top:12px;width:268px;min-height:230px;background:#11182A;border:2px solid oklch(0.66 0.15 305);border-radius:13px;padding:13px 15px}
.l17-bhead{display:block;font-size:10.5px;letter-spacing:.14em;color:#B9C2DA;margin-bottom:10px}
.l17-line{display:block;font-size:11.5px;line-height:1.45;color:#EAEEF8;background:#0E1422;border:1px solid #232C44;border-left:3px solid oklch(0.72 0.15 305);border-radius:8px;padding:7px 10px;margin-bottom:8px;opacity:0}
.l17-line b{color:#FFFFFF}
.l17-line.n1{animation:l17n1 18s infinite}
.l17-line.n2{animation:l17n2 18s infinite}
.l17-line.n3{animation:l17n3 18s infinite}
@keyframes l17n1{0%,17%{opacity:0;transform:translateY(4px)}22%,96%{opacity:1;transform:translateY(0)}100%{opacity:0}}
@keyframes l17n2{0%,37%{opacity:0;transform:translateY(4px)}42%,96%{opacity:1;transform:translateY(0)}100%{opacity:0}}
@keyframes l17n3{0%,57%{opacity:0;transform:translateY(4px)}62%,96%{opacity:1;transform:translateY(0)}100%{opacity:0}}
.l17-ready{display:inline-block;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:#06241a;background:#7FD0A8;border-radius:999px;padding:2px 9px;opacity:0;animation:l17ready 18s infinite}
@keyframes l17ready{0%,70%{opacity:0;transform:scale(1.25)}76%,96%{opacity:1;transform:scale(1)}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l17-blk,.l17-morph,.l17-line,.l17-ready{animation:none}
.l17-line,.l17-ready,.l17-morph{opacity:1}}
@keyframes l17wrapw{0%,100%{opacity:1}}
</style>

## Käytä tekoälyä apuna järjestelmäpromptin kirjoittamisessa

Kun olet kirjoittanut järjestelmäpromptin ensimmäisen version, voit pyytää tekoälyltä apua sen viimeistelyyn. Käytä esimerkiksi seuraavaa promptia:

> "Toimi sparrauskumppaninani. Olen kirjoittamassa apuri-botin järjestelmäpromptia. Tässä ovat määrittelydokumenttini ja ensimmäinen versio järjestelmäpromptista:
>
> MÄÄRITTELY: [liitä rakennuspalikka 2]
>
> JÄRJESTELMÄPROMPTI, versio 1: [liitä oma promptisi]
>
> Auta minua arvioimaan: onko järjestelmäpromptissa mukana kaikki, mitä määrittelyssä oli? Onko jokin kohta botille epäselvä? Onko jokin ohje liian yleinen, esimerkiksi 'vastaa hyvin'? Älä kirjoita uutta versiota. Anna 2–3 konkreettista parannusehdotusta, joiden pohjalta voin tehdä omat muutokseni."

## Tee ensimmäinen versio valitsemallasi polulla

Tästä eteenpäin polut eroavat. Jos sinulla on käytössä alusta, jolle botin voi rakentaa, teet toimivan version. Jos ei ole, teet dokumentoidun suunnitelman, joka arvioidaan samoilla kriteereillä — kumpikaan polku ei ole toista arvokkaampi, ja molemmissa ratkaisee sama asia: miten hyvin määrittelysi kestää testin.

**Teknisellä toteutuspolulla** luot botin saatavilla olevalle alustalle:

1. Luo uusi botti ja anna sille sama nimi kuin määrittelydokumentissasi.
2. Liitä järjestelmäprompti alustan ohjekenttään.
3. Kytke rakennuspalikka 3:n sallitut dokumentit tietopohjaksi.
4. Tarkista jakamisasetus ja se, kuka voi käyttää bottia tai sen aineistoa.
5. Tallenna versio ja aloita testikeskustelu.

**Dokumentoidulla suunnittelupolulla** teet toteutuspaketin:

1. Piirrä osat: käyttäjä, käyttöliittymä, järjestelmäprompti, tietopohjan haku ja vastaus.
2. Kirjoita jokaiselle osalle syöte, tuotos ja vastuu.
3. Kuvaa käyttöoikeusraja ja se, mitä aineistoa käyttäjän roolilla saa hakea.
4. Laadi simuloitu suoritusjälki, jossa näkyvät käyttäjän viesti, haettu lähdekatkelma, muodostettu vastaus ja tarkistus.
5. Merkitse näkyvästi, mitkä yhteydet, käyttöoikeudet ja tallennukset ovat vasta suunnitelmia.

## Kolme ensimmäistä testiä

Älä yritä tehdä botista heti täydellistä. Aja tai simuloi nyt ensimmäisen kerran kaikki kolme Oma botti II -tunnilla kirjoittamaasi testiä: normaali tapaus, kielteinen testi ja reunatapaus.

Tärkein sääntö on, että käytät samoja testejä ja samoja odotuksia kuin kirjoitit Oma botti II -tunnilla. Houkutus muuttaa odotusta ensimmäisen tuloksen jälkeen on suuri — jos botti vastaa toisin kuin odotit, on helppo ajatella että odotus olikin väärä. Silloin testi lakkaa mittaamasta mitään.

Teknisellä polulla ajat testit oikealla botilla ja tallennat jokaisesta syötteen, vastauksen ja mahdollisen lähdeviitteen. Suunnittelupolulla käyt testit läpi vaihe vaiheelta ja merkitset jokaisen simuloidun haun, tarkistuksen ja vastauksen erikseen. Kummallakin polulla vertaat tulosta siihen, mitä odotit — ja kirjaat myös sen, mitä oma polkusi ei pysty todentamaan. Rehellinen maininta puuttuvasta todisteesta on arvioinnissa parempi kuin vaikutelma, että kaikki toimi.

## Mihin kiinnität huomiota testissä?

**Pysyykö botti roolissaan?**

Vai unohtaako se, että se on oman aiheesi apuri, ja muuttuuko se yleiseksi avustajaksi?

**Seuraako botti työnkulkua?**

Vai hyppiikö se osasta toiseen sattumanvaraisesti?

**Käyttääkö botti tietopohjaa oikein?**

Löytyikö oikea lähde, ja tukeeko lähde muodostettua vastausta? Suunnittelupolulla tämä on simuloitu tarkistus, ei todiste toimivasta hausta.

**Yrittääkö botti tehdä työn käyttäjän puolesta?**

Jos pyydät sitä tekemään koko tehtävää puolestasi, noudattaako se ohjeitaan vai murtuuko rajaus?

## Korjauslista Apuri-botin viimeistelytunnille

Kolmen testin jälkeen kirjoita tiivis korjauslista havainnoista, jotka eivät vielä toimi. Älä tee vielä arvioitavaa korjausta, sillä nimetty korjaus ja sen uudelleentesti kuuluvat Apuri-botin viimeistelytunnille. Esimerkkejä:

- "Botti hyppää vaiheen 2 ohi heti — työnkulun ohjetta pitää tarkentaa."
- "Botti käyttää englanninkielisiä termejä, vaikka sen pitäisi puhua suomeksi — lisää kielimääritelmä."
- "Botti antaa heti valmiita vastauksia kysymättä mitään — lisää ohje 'kysy ennen kuin ehdotat'."

## Lopuksi

Tunti 17 on raakaversion vaihe. Älä turhaudu, jos tekninen botti ei vielä toimi täydellisesti tai suunnitelman aukko tulee näkyviin. **Hyvä botti syntyy iteroinnista**. Tällä tunnilla tuotat ensimmäisen todennettavan teknisen version tai ensimmäisen tarkistettavan suunnittelupaketin, ja Apuri-botin viimeistelytunnilla viimeistelet sen.

Ensimmäinen versio on aina raaka. Hyvä botti syntyy iteroinnista.

---

## Lähteet ja tarkistuspäivä

- [NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [UNESCO: Recommendation on the Ethics of Artificial Intelligence](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence)
- [European Commission: GDPR principles](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr/overview-principles/what-data-can-we-process-and-under-which-conditions_en)

Tarkistettu 15.7.2026.
