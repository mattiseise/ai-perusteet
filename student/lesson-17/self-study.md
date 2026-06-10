# Oppitunti 17 — Yhdistä rakennuspalikat ja aloita botin rakentaminen

## Mitä tällä tunnilla tapahtuu?

Tähän mennessä olet kerännyt kuuden tunnin aikana kolme **rakennuspalikkaa**. Tällä tunnilla yhdistät ne ensimmäiseksi toimivaksi botiksi Microsoft Copilotissa. Tämä on **nivelkohta**: siirryt suunnittelusta rakentamiseen.

Tällä tunnilla et opiskele enää uusia teoreettisia käsitteitä. Sen sijaan opit **siirtämään suunnitelman järjestelmäkehotteeksi**, jonka botti ymmärtää. Tämä materiaali auttaa sinua siinä. Ensimmäisen version ei tarvitse olla täydellinen. Tärkeintä on saada aikaan jotakin toimivaa, jota voit kehittää tunnilla 18.

## Mikä on järjestelmäkehote?

**Järjestelmäkehote** on tekstipätkä, jonka annat Copilotille. Se määrittää, miten botti käyttäytyy *kaikissa* keskusteluissa. Käyttäjä ei yleensä näe järjestelmäkehotetta, mutta botti noudattaa sitä toiminnassaan.

Voit ajatella järjestelmäkehotetta botin **työsopimuksena**: kuka botti on, mikä sen tehtävä on ja missä sen rajat kulkevat.

Hyvä järjestelmäkehote vastaa neljään kysymykseen:

1. **Kuka olet?** Rooli ja persoona.
2. **Mitä teet?** Tehtävä ja työnkulku.
3. **Miten puhut?** Äänensävy ja tyyli.
4. **Mitä et tee?** Rajat ja kiellot.

## Rakennuspalikat järjestelmäkehotteeksi

Kolme rakennuspalikkaasi muuttuvat järjestelmäkehotteeksi seuraavasti:

| Rakennuspalikka | Mihin osaan järjestelmäkehotetta? |
| --- | --- |
| **1: Promptauspankki** | Tyyli ja kieli. Olet jo nähnyt, millainen muotoilu toimii. Käytä sitä botin pääohjeessa. |
| **2: Määrittelydokumentti** | Sisältö. Kuusi osaa eli nimi, kohderyhmä, tarkoitus, persoona, työnkulku ja rajat muuttuvat suoraan järjestelmäkehotteen kappaleiksi. |
| **3: Tietopohja** | Asiantuntemus. Tietopohja ei ole osa järjestelmäkehotetta, vaan se ladataan erikseen Copilotiin. Järjestelmäkehotteessa voit kuitenkin viitata siihen esimerkiksi näin: *"Käytä tietopohjaan ladattuja dokumentteja referenssinä."* |

## Esimerkki: rakennuspalikoista järjestelmäkehotteeksi

Alla on yksinkertainen esimerkki siitä, miten määrittelydokumentin sisältö muuttuu järjestelmäkehotteeksi. Ota se malliksi, mutta älä kopioi sitä sellaisenaan.

### Määrittelydokumentin sisältö eli rakennuspalikka 2

> **Botin nimi:** Tapahtuman suunnitteluvalmentaja
> **Kohderyhmä:** Opiskelija, joka alkaa suunnitella tapahtumaa
> **Tarkoitus:** Ohjata käyttäjää tapahtuman suunnitteludokumentin laatimisessa kuuden osan kautta
> **Persoona:** Käytännönläheinen, kysyvä, ei jargonia
> **Työnkulku:** 1) Tapahtuman idea → 2) Kohderyhmä ja paikka → 3) Ohjelma → 4) Budjetti ja hankinnat → 5) Aikataulu → 6) Riskit
> **Rajat:** Ei kirjoita dokumenttia käyttäjän puolesta, ei arvioi kaupallista potentiaalia, ei käsittele muiden alojen projekteja

### Sama järjestelmäkehotteena

> Olet **Tapahtuman suunnitteluvalmentaja**. Autat opiskelijaa, joka alkaa suunnitella tapahtumaa, laatimaan tapahtuman suunnitteludokumentin.
>
> **Työnkulkusi:** Ohjaat käyttäjää aina järjestyksessä kuuden osan läpi: (1) tapahtuman idea, (2) kohderyhmä ja paikka, (3) ohjelma, (4) budjetti ja hankinnat, (5) aikataulu ja (6) riskit. Et siirry seuraavaan osaan ennen kuin nykyinen osa on käsitelty.
>
> **Tapasi puhua:** Olet käytännönläheinen ja kysyvä. Pyydät käyttäjältä konkreettisia vastauksia etkä hyväksy ympäripyöreitä vastauksia sellaisenaan. Et käytä akateemista jargonia. Käytät tapahtumasuunnittelun omia termejä, kuten kohderyhmä, ohjelmarunko, budjetti ja aikataulu.
>
> **Et koskaan:** kirjoita dokumenttia käyttäjän puolesta, arvioi tapahtuman kaupallista potentiaalia tai käsittele muiden alojen projekteja. Jos käyttäjä pyytää näitä, ohjaa hänet ystävällisesti takaisin aiheeseen tai oikealle asiantuntijalle.
>
> **Tietopohja:** Käytä bottiin ladattuja dokumentteja referenssinä, kun ohjaat käyttäjää.

Huomaa, että määrittelydokumentissa sisältö on kuvailevassa muodossa, kun taas järjestelmäkehotteessa puhutaan botille suoraan: "Olet…", "Työnkulkusi…" ja "Et koskaan…". Tämä on tärkein muunnos: **kuvaileva määrittely muutetaan suoraksi ohjeeksi botille**.

<figure class="ai-demo"><span class="ai-demo__tag">// kolme rakennuspalikkaa kasaan — kuvailevasta määrittelystä suoraksi ohjeeksi</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:300px">
  <div class="l17-wrap">
    <div class="l17-blk b1"><b>1 · Promptipankki</b><span>toimivat muotoilut</span></div>
    <div class="l17-blk b2"><b>2 · Määrittely</b><span>”Botin nimi: Valmentaja”</span></div>
    <div class="l17-blk b3"><b>3 · Tietopohja</b><span>3–5 dokumenttia</span></div>
    <span class="l17-morph">kuvaileva → suora ohje</span>
    <div class="l17-bot"><span class="l17-bhead">JÄRJESTELMÄKEHOTE</span>
      <span class="l17-line n1">Kirjoita selkeästi, kysy tarkentavia kysymyksiä.</span>
      <span class="l17-line n2"><b>”Olet Valmentaja.”</b> Ohjaat kuusi vaihetta järjestyksessä.</span>
      <span class="l17-line n3">Käytä ladattuja dokumentteja referenssinä.</span>
      <span class="l17-ready">✓ botti valmis testattavaksi</span>
    </div>
  </div>
</div>
<figcaption class="ai-demo__cap">Palikat eivät kelpaa botille sellaisenaan: promptipankista tulee tyyli, määrittelystä sisältö ja tietopohjasta asiantuntemus. Ratkaiseva muunnos on puhutella bottia suoraan — ”Botin nimi: Valmentaja” muuttuu muotoon ”Olet Valmentaja”.</figcaption></figure>
<style>
.l17-wrap{position:relative;width:560px;height:262px;font-family:var(--font-mono)}
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
</style>

## Käytä tekoälyä apuna järjestelmäkehotteen kirjoittamisessa

Kun olet kirjoittanut järjestelmäkehotteen ensimmäisen version, voit pyytää tekoälyltä apua sen viimeistelyyn. Käytä esimerkiksi seuraavaa promptia:

> "Toimi sparrauskumppaninani. Olen kirjoittamassa Copilot-botin järjestelmäkehotetta. Tässä ovat määrittelydokumenttini ja ensimmäinen versio järjestelmäkehotteesta:
>
> MÄÄRITTELY: [liitä rakennuspalikka 2]
>
> JÄRJESTELMÄKEHOTE, versio 1: [liitä oma kehotteesi]
>
> Auta minua arvioimaan: onko järjestelmäkehotteessa mukana kaikki, mitä määrittelyssä oli? Onko jokin kohta botille epäselvä? Onko jokin ohje liian yleinen, esimerkiksi 'vastaa hyvin'? Älä kirjoita uutta versiota. Anna 2–3 konkreettista parannusehdotusta, joiden pohjalta voin tehdä omat muutokseni."

## Copilot Agentin luominen

Microsoft Copilotissa voit luoda oman **agentin**, jolla on omat ohjeet ja tietopohja. Luo agentti näin:

1. Avaa Copilot ja siirry **Agents** / **Agentit** -osioon.
2. Luo uusi agentti. Anna sille sama nimi kuin määrittelydokumentissasi.
3. Liitä järjestelmäkehotteesi **Instructions** / **Ohjeet** -kenttään.
4. Lataa rakennuspalikka 3:n dokumentit tietopohjaksi kohtaan **Knowledge** / **Tieto**.
5. Tallenna agentti ja aloita keskustelu.

Jos Copilotin käyttöliittymä on muuttunut tai et löydä jotakin vaihetta, kysy opettajalta tai etsi ohje hakemalla esimerkiksi *"Copilot agent create instructions"*.

## Ensimmäinen testikeskustelu

Älä yritä tehdä botista heti täydellistä. Aja yksi keskustelu läpi ja katso, mitä tapahtuu. Hyvä testaustapa etenee näin:

1. **Keksi kuvitteellinen projekti omalta alaltasi.** Kirjoita siitä lyhyt kuvaus, 2–3 lausetta.
2. **Anna botin ohjata.** Vastaa sen kysymyksiin niin kuin oikea käyttäjä vastaisi.
3. **Käy keskustelu loppuun.** Tarkista, pääsetkö valmiiseen määrittelydokumenttiin.
4. **Tallenna keskustelu** kuvakaappauksina tai kopioituna tekstinä.

## Mihin kiinnität huomiota testissä?

**Pysyykö botti roolissaan?**

Vai unohtaako se, että se on oman alasi valmentaja, ja muuttuuko se yleiseksi avustajaksi?

**Seuraako botti työnkulkua?**

Vai hyppiikö se osasta toiseen sattumanvaraisesti?

**Käyttääkö botti tietopohjaa?**

Tunnistatko sen vastauksista oman alasi termejä, vai kuulostavatko vastaukset yleiseltä projektijargonilta?

**Yrittääkö botti kirjoittaa käyttäjän puolesta?**

Jos pyydät sitä kirjoittamaan koko dokumentin puolestasi, noudattaako se ohjeitaan vai murtuuko rajaus?

## Korjauslista tunnille 18

Testin jälkeen kirjoita muistiin 3–5 asiaa, jotka eivät vielä toimi. Älä korjaa kaikkea tällä tunnilla, sillä tunti 18 on viimeistelyä varten. Esimerkkejä:

- "Botti hyppää vaiheen 2 ohi heti — työnkulun ohjetta pitää tarkentaa."
- "Botti käyttää englanninkielisiä termejä, vaikka sen pitäisi puhua suomeksi — lisää kielimääritelmä."
- "Botti antaa heti valmiita vastauksia kysymättä mitään — lisää ohje 'kysy ennen kuin ehdotat'."

## Lopuksi

Tunti 17 on raakaversion vaihe. Älä turhaudu, jos botti ei vielä toimi täydellisesti. Sen ei ole tarkoituskaan olla valmis heti. **Hyvä botti syntyy iteroinnista**. Tällä tunnilla saat ensimmäisen version toimimaan, ja tunnilla 18 viimeistelet sen.

Ensimmäinen versio on aina raaka. Hyvä botti syntyy iteroinnista.

---
