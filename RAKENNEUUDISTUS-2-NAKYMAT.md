# Rakenneuudistus 2: yksi sisältöpohja, kolme näkymää

*Suunnitteludokumentti · 14.7.2026 · pohjana koko sivuston (aiperusteet.fi) ja sisältöpohjan läpikäynti sekä oletusskannaus*

**Suhde aiempaan:** RAKENNEUUDISTUS.md (kevät 2026) korjasi *sisällön* rakenteen — päällekkäisyydet, OSP2:n punaisen langan, kertauksen kehystämisen. Tämä dokumentti korjaa *jakelun* rakenteen: sama sisältö palvelee nyt kolmea eri käyttötapaa yhden navigaation läpi, ja se on uudistuksen varsinainen ongelma.

**Tiivistelmä johtopäätöksistä:**

1. Sisältömalli on kunnossa — jokainen tunti tuottaa jo nyt kanoniset lohkot (teoria, sanasto, harjoittelu, luokkatehtävät, diat, opettajan materiaalit). Sitä ei pidä suunnitella uusiksi.
2. Esitysmalli on rikki — kolme eri käyttäjäryhmää ohjataan yhteen navigaatioon, jossa segmentointi tapahtuu välilehtien nimillä. Se on informaatioarkkitehtuurin antipattern: roolit välilehtinä.
3. Suositus: **kolme näkymää samasta pohjasta** (täsmennetty B-vaihtoehto): Verkkokurssi, Luokkaversio, Opettajan opas. Näkymät eivät ole kolme kurssia vaan kolme suodatinta samaan sisältögraafiin — yli 80 % lohkoista on yhteisiä.
4. Uutta sisältöä tarvitaan vain kahteen kohtaan: lopputöiden verkkovariantit (itsearvioitava palautus) ja kurssitason opettajan opas. Kaikki muu on olemassa olevan valikointia.
5. Samalla kannattaa korjata tekninen perusvika: koko kurssi on yksi 2,9 Mt:n HTML-tiedosto, jolla ei ole hakukonenäkyvyyttä eikä oikeita sivu-URLeja. Monisivuinen generointi ratkaisee sekä IA:n että SEO:n.

---

## Vaihe 1 — Nykyisen sivuston analyysi

### 1.1 Rakenne sellaisena kuin kävijä sen kohtaa

**Etusivu:** hero ("AI · Perusteet — 3 OSP", edistymispalkki 0/27), kolme moduulikorttia (Teoria, Tekoälyjen käyttö, Agentit), joista aukeaa 9 oppitunnin lista + ★ Lopputyön tehtävänanto. Alimpana "Materiaalityypit"-selite, joka kertoo mitä kuusi eri sisältölajia tarkoittavat.

**Tuntisivu:** murupolku, otsikko, "~90 MIN" -merkki ja **seitsemän välilehteä**: Diat · Itseopiskelumateriaali · Opiskelutehtävät · Harjoittele · Sanasto · Opettajavetoiset tehtävät · Opettajan materiaali. Alalaidassa Edellinen/Seuraava ja "Merkitse suoritetuksi" (tallentuu selaimeen).

**Tekniikka:** yksi generoitu index.html (~2,9 Mt), jossa kaikki 27 tuntia; navigointi hash-reitityksellä (#lesson-19/practice); GA4-mittaus (lesson_open, lesson_complete, task_start/complete); ei kirjautumista, ei rooleja.

### 1.2 Mikä toimii hyvin (säilytettävä)

- **Sisältölohkojen kanoninen malli.** Jokainen tunti tuottaa samat, selkeästi erilliset lohkot. Tämä on täsmälleen se "yksi sisältöpohja", jota ylläpitovaatimuksesi edellyttää — se on jo olemassa.
- **Itseopiskelumateriaalit ovat aidosti itsenäisiä.** Oletusskannaus: 25 tunnin teksteissä on vain 2–3 kohtaa, jotka olettavat opettajan läsnäolon. Loput "opettaja"-maininnat ovat pedagogisia esimerkkihahmoja ("kuvittele, että istut opettajan työhuoneessa"), jotka toimivat kaikille yleisöille.
- **Harjoittele-kerros** (112 itsetarkistuvaa tehtävää) on verkkokurssin ydin: palaute tulee sivulta itseltään. Tämä on ainoa tehtäväkerros, joka toimii ilman opettajaa — ja se on jo olemassa joka tunnilla.
- **Sanastot** ovat lyhyitä, tarkkoja ja yleisöneutraaleja.
- **Generaattoriarkkitehtuuri.** Sivusto rakentuu komennolla lähdetiedostoista. Monninäkymäisyys on siksi halpa toteuttaa: näkymä = generaattorin konfiguraatio, ei sisällön kopio.
- **Edistymisseuranta ja GA-instrumentointi** — säilytettävä sellaisenaan, laajennettuna näkymädimensiolla.

### 1.3 Mikä on rikki

**R1 — Roolit välilehtinä.** Itsenäinen opiskelija näkee seitsemän välilehteä, joista kaksi ei ole hänelle (opettajan materiaalit) ja yksi johtaa umpikujaan (Opiskelutehtävät, ks. R2). Luokan opiskelija näkee opettajan vastauspankit — opettajan materiaali sisältää väärinkäsityslistat ja tehtävien purut, eli vastaukset. Opettaja taas ei saa mistään kurssitason ohjetta. Etusivun "Materiaalityypit"-selite on tämän ongelman oire: sivusto joutuu selittämään oman sekaannuksensa.

**R2 — Verkko-opiskelijan polku katkeaa tehtäviin.** Opiskelutehtävät on kirjoitettu luokkaan: pariporinat, opettajan purku, ⭐️-pohjapiirroksen näyttäminen tunnilla, palautus Itslearningiin. Anonyymi verkkokävijä kohtaa ohjeen "palauta Itslearningiin" — järjestelmään, johon hänellä ei ole pääsyä. Sama katko toistuu vahvempana lopputöissä (pisteytys 25/20/20/20/15, palautus ja esittely tunnilla).

**R3 — Diat väärässä roolissa.** Diakannet ovat opettajan esitysväline, mutta ne ovat tuntisivun *ensimmäinen* välilehti — verkko-opiskelijalle ne ovat itseopiskelutekstin köyhempi rinnakkaiskanava, joka kilpailee huomiosta oikean sisällön kanssa.

**R4 — Ei sisääntulon ohjausta.** Etusivu ei kysy eikä päättele, kuka olet. "3 OSP" ja "~90 MIN" ovat oppilaitoskehyksiä, jotka ovat merkityksettömiä tai hämmentäviä itsenäiselle opiskelijalle.

**R5 — Tekninen jakelu.** Yksi 2,9 Mt:n tiedosto: hidas mobiilissa, ei hakukonenäkyvyyttä yksittäisille tunneille (hash-reitit eivät indeksoidu), ei oikeita jaettavia URLeja. Avoimen verkkokurssin löydettävyys on nolla juuri siellä, mistä itsenäiset opiskelijat tulisivat: hausta.

**R6 — Piilevä ylläpitovelka.** content/lessons/ on ajautunut kopio, joka ei ole enää sivuston lähde mutta jota README yhä kutsuu pääsisällöksi.

### 1.4 Käyttäjäpolut ja katkeamiskohdat

| Käyttäjä | Polku | Katkeaa |
|---|---|---|
| Itsenäinen opiskelija | Etusivu → tunti 1 → **Diat** (väärä ensikosketus) → Itseopiskelu (hyvä) → Opiskelutehtävät | "Palauta Itslearningiin", pariporinat → umpikuja. Harjoittele pelastaa, jos hän löytää sen. Lopputyö: täysi umpikuja. |
| Luokan opiskelija | Opettaja jakaa linkin → tunti → tehtävät | Näkee opettajan materiaalit (vastaukset); seitsemästä välilehdestä relevantteja on neljä. |
| Opettaja | Etusivu → ??? | Ei sisäänkäyntiä: ei kurssiopasta, ei toteutusohjetta, ei arviointiohjetta kurssitasolla; opettajasisältö on ripoteltu 27 tuntiin. Ei tapaa jakaa opiskelijoille "puhdasta" näkymää. |

### 1.5 Vastaus kysymykseen "onko rakenne looginen?"

Rakenne on looginen *sisällöntuottajalle* (se peilaa lähdekansioita) mutta ei *yhdellekään käyttäjäryhmälle*. Tämä on klassinen organisaatiolähtöinen IA: navigaatio kertoo, miten materiaali on tuotettu, ei mitä käyttäjä on tekemässä. Siksi pelkkä uudelleenjärjestely ei riitä — esityskerros on suunniteltava uusiksi käyttötilanteiden ympärille. Sisältökerrosta sen sijaan ei pidä suunnitella uusiksi: se on uudistuksen raaka-aine ja jo oikeassa muodossa.

---

## Vaihe 2 — Uusi informaatioarkkitehtuuri

### 2.1 Suunnitteluperiaate

> **Yksi sisältöpohja → näkymät valikoivat ja kehystävät, eivät koskaan kopioi.**

Jokainen tunti tuottaa nimetyt lohkot (block contract). Näkymä on deklaratiivinen valinta: mitkä lohkot näytetään, missä järjestyksessä, millä kehystyksellä. Jos jokin lohko tarvitsee eri sisällön eri näkymässä (käytännössä vain palautusohjeet), ero tehdään **varianttilohkona saman tiedoston sisällä** — ei rinnakkaistiedostona. Näin mikään asia ei ole olemassa kahdessa paikassa.

### 2.2 Montako näkymää: kaksi vai kolme?

**Suositus: kolme (täsmennetty B).** Perustelu kahta vastaan:

- A-mallissa (verkko + opettajan johdolla) luokan opiskelijan ja opettajan tarpeet pakotetaan samaan näkymään. Silloin joko opettajan materiaali (vastauksineen) on luokkanäkymässä julkista, tai se piilotetaan — jolloin opettajalla ei taas ole omaa paikkaa. Ongelma R1 jää ratkaisematta.
- Opettajan tarve on kurssitasoinen (miten toteutan 27 × 90 min, miten arvioin, miten vien Itslearningiin), ei vain tuntitasoinen. Se ansaitsee oman kokonaisuuden, joka ei ole "kolmas kurssi" vaan opas + tuntikohtaiset ohjaimet.

Ja kolmen näkymän ylläpitohuoli torjutaan sillä, että näkymät jakavat lohkot:

| Lohko | Verkkokurssi | Luokkaversio | Opettajan opas |
|---|---|---|---|
| Teoria (itseopiskelu) | ✅ ydin | ✅ sama tiedosto | 🔗 linkki |
| Harjoittele | ✅ tehtäväkerros | ✅ sama | 🔗 linkki |
| Sanasto | ✅ | ✅ sama | 🔗 linkki |
| Luokkatehtävät (nyk. opiskelutehtävät) | — | ✅ ydin | 🔗 linkki + purkuohjeet |
| Diat | — | ✅ kertaukseen | ✅ esitystila + pptx |
| Tuntisuunnitelma, väärinkäsitykset (nyk. opettajan materiaali) | — | — | ✅ ydin |
| Opettajavetoiset tehtävät | — | — | ✅ |
| Lopputyö | ✅ verkkovariantti | ✅ luokkavariantti | ✅ + arviointiohje |
| Kurssiopas (UUSI) | — | — | ✅ |

Kaikista lohkoista vain **lopputyön palautusosio** tarvitsee varianttisisällön ja vain **kurssiopas** on kokonaan uutta. Tämä on "kolme näkymää, ei kolmea kurssia" konkreettisesti.

### 2.3 Näkymien luonnekuvaukset

**1. Verkkokurssi — oletusnäkymä.** Kohde: itsenäinen opiskelija, joka tuli hausta tai linkistä. Tuntisivu: Teoria → Harjoittele → Sanasto, ei mitään muuta. Kehystys: "n. 60–90 min" lukuaika-arviona, ei oppituntikielenä; OSP-puhe pois etusivulta (siirretään opettajan oppaaseen, jossa se on relevantti). Moduulin päätteeksi verkkolopputyö: sama tehtävä, mutta palautus = itsearviointikriteerit + oma portfolio ("tallenna itsellesi; halutessasi jaa"). Edistyminen ja "Merkitse suoritetuksi" säilyvät.

**2. Luokkaversio.** Kohde: opiskelija oppitunnilla, opettajan jakaman linkin takana. Tuntisivu: Teoria → Tehtävät (nykyiset opiskelutehtävät sellaisinaan — ne ovat hyviä, ne ovat vain olleet väärässä näkymässä) → Harjoittele → Sanasto → Diat (kertaus). Lopputyö luokkavariantilla (Itslearning, pisteet). Ei opettajan materiaaleja.

**3. Opettajan opas.** Kohde: opettaja, joka valmistelee tai vetää kurssia — tai harkitsee sen käyttöönottoa. Kurssitaso: toteutusmallit (3 OSP, jaksotus, arviointi, Itslearning-vienti, lisenssi "saa käyttää ja muokata"), lataamo (pptx-kannet, tulostettavat). Tuntitaso: tuntisuunnitelma + väärinkäsitykset + opettajavetoiset tehtävät + diat esitystilassa + "jaa tämä tunti opiskelijoille" -painike, joka antaa luokkaversion linkin. Erillinen polku ja maininta "tämä osio on opettajille" riittävät avoimessa kurssissa; vastauspankkien signalointi hoituu sillä, että ne eivät ole opiskelijanäkymien navigaatiossa lainkaan.

### 2.4 Miten käyttäjä löytää oikean version (navigaatio)

- **Etusivu = suuntaaja, ei materiaalivarasto.** Kolme selkeää ovea: "Opiskele itsenäisesti" (ensisijainen CTA, koska anonyymi kävijä on todennäköisimmin itseopiskelija), "Olemme oppitunnilla", "Olen opettaja". Valinta muistetaan (localStorage) ja headerissa on huomaamaton näkymävaihtaja.
- **Syvälinkit ohittavat etusivun:** opettaja jakaa aina suoraan /luokka/-linkin, hakukone tuo aina /kurssi/-sivulle. Suunta: suurin osa kävijöistä ei koskaan näe valintasivua — ja juuri siksi se saa olla yksinkertainen.
- **Vanhat linkit eivät katkea:** #lesson-NN-hashit uudelleenohjataan /kurssi/tunti-NN-sivuille (taulukko vaiheessa 4).

### 2.5 Laajennettavuus ilman rakennemuutoksia

- Kurssin rakenne siirretään koodista dataan: `kurssi.yaml` määrittelee moduulit, tunnit ja näkymäkonfiguraatiot. Uusi moduuli = uusi kansio + rivit manifestiin; kaikki kolme näkymää generoituvat ilman koodimuutosta.
- Block contract on laajennettavuuden ydin: uusi tunti on valmis, kun sen kansiossa on kanoniset lohkotiedostot. Uusi *näkymä* (esim. yrityskoulutuspaketti myöhemmin) = uusi näkymäkonfiguraatio, ei sisältötyötä.
- Harjoittele-moottori on jo tällainen: tehtävät ovat dataa, renderöijä yksi. Sama periaate ulotetaan koko sivustoon.

---

## Vaihe 3 — Uusi sivukartta

### 3.1 Julkinen sivukartta

```
aiperusteet.fi/
│
├── /                            Valintasivu + kurssiesittely
│                                CTA: "Aloita kurssi" → /kurssi/
│                                Toissijaiset: "Oppitunnilla" → /luokka/ · "Opettajalle" → /opettaja/
│
├── /kurssi/                     ITSENÄINEN VERKKOKURSSI (oletusnäkymä)
│   ├── /kurssi/                 Kurssin yleiskuva, eteneminen, 3 moduulia
│   ├── /kurssi/teoria/          Moduulisivu: johdanto + tunnit 1–9 + lopputyö
│   │   ├── /kurssi/tunti-01/ … /kurssi/tunti-09/
│   │   └── /kurssi/teoria/lopputyo/        (verkkovariantti: itsearviointi)
│   ├── /kurssi/kaytto/          Tunnit 10–18 + lopputyö (verkkovariantti)
│   └── /kurssi/agentit/         Tunnit 19–27 + lopputyö (verkkovariantti)
│
│   Tuntisivun sisältöjärjestys: Teoria → Harjoittele → Sanasto
│   (yhtenä vieritettävänä sivuna tai kolmena välilehtenä — suositus: välilehdet säilyvät,
│    mutta niitä on kolme, ja ensimmäinen on Teoria)
│
├── /luokka/                     OPPITUNTIEN OPISKELIJAVERSIO
│   └── /luokka/tunti-NN/        Teoria → Tehtävät → Harjoittele → Sanasto → Diat
│       /luokka/<osp>/lopputyo/  (luokkavariantti: Itslearning + pisteet)
│
├── /opettaja/                   OPETTAJAN OPAS
│   ├── /opettaja/               Kurssiopas (UUSI): toteutusmallit, 3 OSP, arviointi,
│   │                            Itslearning-vienti, lisenssi, lataamo (pptx, tulosteet)
│   ├── /opettaja/tunti-NN/      Tuntisuunnitelma → Opettajavetoiset tehtävät →
│   │                            Väärinkäsitykset → Diat (esitystila) → "Jaa opiskelijoille" -linkki
│   └── /opettaja/arviointi/     Lopputöiden arviointiohjeet (3 kpl koottuna)
│
├── /sanasto/                    Koko kurssin koottu sanasto (generoitu, aakkostettu; SEO-magneetti)
│
└── uudelleenohjaukset           /#lesson-NN → /kurssi/tunti-NN (taulukko 4.4)
```

### 3.2 Lähdekansiorakenne (yksi sisältöpohja)

```
sisalto/
├── kurssi.yaml                  Moduulit, tunnit, otsikot, kestot, näkymäkonfiguraatiot
├── tunnit/NN/
│   ├── teoria.md                ← nyk. student/lesson-NN/self-study.md
│   ├── sanasto.md               ← nyk. vocabulary.md
│   ├── harjoittele.md           ← nyk. practice.md
│   ├── tehtavat-luokka.md       ← nyk. student-tasks.md
│   ├── diat.html                ← nyk. slides.html
│   └── opettaja/
│       ├── tuntisuunnitelma.md  ← nyk. teacher/lesson-NN/teacher-materials.md
│       └── tehtavat-ohjatut.md  ← nyk. teacher-led-tasks.md
├── lopputyot/
│   ├── teoria.md · kaytto.md · agentit.md    (varianttilohkot: ::: verkko / ::: luokka / ::: opettaja)
├── opettaja/
│   └── kurssiopas.md            UUSI (ainoa kokonaan uusi sisältö)
└── media/                       kuvat ym.
```

Varianttilohkon mekanismi: saman tiedoston sisällä merkitty osio, jonka generaattori valitsee näkymän mukaan. Esimerkki lopputyön palautusosiosta:

```
::: luokka
Palauta Itslearningiin yhtenä pakettina. Arviointi: 25/20/20/20/15 p.
:::
::: verkko
Kokoa samat tuotokset itsellesi portfolioksi ja käy läpi itsearviointilista.
Halutessasi jaa tuotoksesi — mitään ei palauteta minnekään.
:::
```

Yksi tiedosto, ei rinnakkaisversioita, diff näyttää variantit vierekkäin.

### 3.3 Tekninen jakelu

- Monisivuinen staattinen generointi: jokainen tuntisivu on oma HTML-tiedostonsa (~100–300 kt) → mobiilinopeus, oikeat URLit, hakukonenäkyvyys jokaiselle tunnille. Deploy-putki ei muutu (git → Netlify).
- Edistyminen: sama localStorage-avain kuin nyt (bcai-new) → kävijöiden edistyminen ei nollaudu. Harjoittele-tulokset (bcai-practice) samoin.
- GA4: säilyy; jokaiseen tapahtumaan lisätään `view`-dimensio (kurssi/luokka/opettaja) → näet vihdoin, missä käyttötavassa mikäkin tunti ja tehtävä elää.
- Consent-banneri ja gtag-logiikka siirtyvät sellaisinaan sivupohjaan.

---

## Vaihe 4 — Siirtymäsuunnitelma

### 4.1 Sisältömappaus: nykyinen → uusi (kattava)

| Nykyinen artefakti | Uusi sijainti | Näkyy näkymissä | Muutostyö |
|---|---|---|---|
| student/lesson-NN/self-study.md (×25) | sisalto/tunnit/NN/teoria.md | kurssi, luokka | git mv; 3 pistekorjausta (4.3) |
| student/lesson-NN/practice.md (×25) | tunnit/NN/harjoittele.md | kurssi, luokka | git mv, ei sisältömuutoksia |
| student/lesson-NN/vocabulary.md (×27) | tunnit/NN/sanasto.md | kurssi, luokka (+ /sanasto/ koonti) | git mv |
| student/lesson-NN/student-tasks.md (×27) | tunnit/NN/tehtavat-luokka.md | **vain luokka** | git mv — sisältö on hyvää, vain näkyvyys muuttuu |
| student/lesson-NN/slides.html (×27) | tunnit/NN/diat.html | luokka (kertaus), opettaja (esitys) | git mv |
| teacher/lesson-NN/teacher-materials.md (×27) | tunnit/NN/opettaja/tuntisuunnitelma.md | vain opettaja | git mv |
| teacher/lesson-NN/teacher-led-tasks.md (×27) | tunnit/NN/opettaja/tehtavat-ohjatut.md | vain opettaja | git mv |
| student/lesson-18 & 27 (arviointitunnit) | tunnit/18, 27 | kurssi: verkkovariantti; luokka: nykyinen | arviointituntien self-study saa ::: verkko -palautusosion |
| *lopputyo*-tehtavananto.md (×3) | sisalto/lopputyot/*.md | kaikki (varianttilohkoin) | **kirjoitustyö: verkkovariantit** (itsearviointikriteerit) |
| — (ei ole) | sisalto/opettaja/kurssiopas.md | opettaja | **kirjoitustyö: uusi** (material-pipeline) |
| content/lessons/*.md (×27) | **poistetaan** | — | diff-tarkistus → git rm (ks. 4.5) |
| LESSONS-21-25-INDEX.md, preview-lesson-01.html | poistetaan | — | työjäänteitä |
| generate_site.py | generaattori v2 | — | monisivuisuus + näkymäkonfigit + variantit |
| index.html (generoitu) | korvautuu sivupuulla | — | redirect-sivuksi |
| slides-pptx/ (gitignored) | /opettaja/ lataamo | opettaja | linkitys Drive-kansioon tai suora lataus |
| Etusivun "Materiaalityypit"-selite | **poistetaan** | — | tarpeeton, kun näkymät eriytetty |
| "~90 MIN" -merkki | luokka+opettaja: "90 min oppitunti"; kurssi: "lukuaika n. X min" | | generaattori laskee lukuajan sanamäärästä |

### 4.2 Mitä poistetaan kokonaan (Q14)

1. content/lessons/ — ajautunut kopio; ensin `diff -r` ja aidosti uudemman sisällön poiminta, sitten poisto. README päivitetään osoittamaan sisalto/-kansioon.
2. Etusivun materiaalityyppiselite ja Google Slides -legacy-koodipolku generaattorista (SLIDE_URLS).
3. Työjäännetiedostot (LESSONS-INDEX, preview-html:t).
4. Ei muuta: varsinaista sisältöä ei poisteta — kaikelle nykyiselle on paikka jossakin näkymässä.

### 4.3 Mitä kirjoitetaan uudelleen (Q13) — täsmällinen lista

Oletusskannauksen tulos: itseopiskelutekstit ovat jo lähes puhtaita. Aidot opettajaoletukset:

1. **tunti-17 teoria, r. 127** — "kysy opettajalta tai etsi ohje hakemalla" → verkkovariantissa järjestys käännetään: "etsi ohje hakemalla; oppitunnilla voit kysyä opettajalta" (varianttilohko tai neutraali muotoilu).
2. **tunti-27 teoria, r. 132** — "Palauta tunnin lopussa tai opettajan ohjeistaman aikataulun mukaan" → ::: luokka / ::: verkko -variantti (verkossa: itsearviointi + portfolio).
3. **Lopputyöbriefit ×3** — palautus- ja arviointiosiot varianttilohkoiksi; verkkovarianttiin itsearviointikriteerit, jotka johdetaan nykyisistä pisteytyskriteereistä (sama sisältö, eri kehys — ei uutta pedagogista suunnittelua).
4. **Arviointituntien 18 ja 27 kehystys** verkossa: "esittele tunnilla" → "viimeistele ja arvioi itse; jaa halutessasi".
5. Kaikki muut "opettaja"-esiintymät ovat esimerkkihahmoja eikä niitä muuteta.

### 4.4 Uudelleenohjaukset (vanhat linkit eivät katkea)

| Vanha | Uusi |
|---|---|
| / (hash-etusivu) | / (valintasivu) |
| /#lesson-NN | /kurssi/tunti-NN/ |
| /#lesson-NN/practice | /kurssi/tunti-NN/#harjoittele |
| /#lesson-NN/stasks | /luokka/tunti-NN/#tehtavat |
| /#lesson-NN/tltasks, /#lesson-NN/tmats | /opettaja/tunti-NN/ |
| /#brief-ospN | /kurssi/<osp>/lopputyo/ |

Toteutus: index.html jää kevyeksi ohjaussivuksi, joka lukee hashin ja ohjaa; lisäksi Netlify _redirects. Erityisen tärkeää siksi, että linkkejä on jaettu Itslearning-kursseihin.

### 4.5 Työvaiheet ja mittaluokka

| # | Vaihe | Sisältö | Mittaluokka |
|---|---|---|---|
| 0 | Inventaario & jäädytys | content/lessons-diff ja poisto, README-päivitys, redirect-taulukon lukitus | 0,5 sessiota |
| 1 | Lähdepohjan siirto | git mv uuteen sisalto/-rakenteeseen (historia säilyy), kurssi.yaml | 0,5 |
| 2 | Generaattori v2 | monisivuinen tuotanto, näkymäkonfiguraatiot, varianttilohkot, lukuaika, GA view-dimensio, redirectit | 1–2 |
| 3 | Sisältövariantit | lopputöiden verkkovariantit + 4.3:n pistekorjaukset (material-pipeline: suunnittelu → portit) | 1 |
| 4 | Kurssiopas | uusi opettajan kurssitason opas (pipeline) | 1 |
| 5 | Beta rinnakkain | /v2/-esikatselu Netlifyyn, läpiklikkaustestit kolmessa näkymässä, GA-varmistus | 0,5 |
| 6 | Julkaisu | vaihto, redirectit päälle, Search Console -ilmoitus sivukartasta | 0,5 |

Yhteensä noin **5–6 työsessiota** nykyisellä työtavalla (Opus tekee, Fable orkestroi ja verifioi). Riskit: (a) hash-linkkien kattavuus — lukitaan taulukolla ennen vaihtoa; (b) edistymisdatan säilyminen — testataan betassa samoilla localStorage-avaimilla; (c) SEO-siirtymä — uusi rakenne voi vain parantaa nykyistä (nollasta ylöspäin).

---

## Vastaukset kysymyksiisi 1–15 (tiivistelmä)

1. **Looginen?** Tuotantolähtöisesti kyllä, käyttäjälähtöisesti ei. Sisältökerros säilytetään, esityskerros suunnitellaan uusiksi (1.5).
2. **Mikä toimii:** kanoninen lohkomalli, itsenäiset teoriatekstit, Harjoittele, sanastot, generaattori, edistymisseuranta (1.2).
3. **Väärässä paikassa:** opiskelutehtävät verkkonäkymässä, opettajan materiaalit opiskelijoiden navigaatiossa, diat ensimmäisenä välilehtenä, OSP-kehys etusivulla (1.3).
4. **Polku katkeaa:** verkko-opiskelijalla tehtävissä ja lopputyössä (Itslearning-umpikuja), opettajalla heti etusivulla (ei sisäänkäyntiä), luokan opiskelijalla vastausvuotoon (1.4).
5. **Uusi IA:** yksi sisältöpohja + block contract + deklaratiiviset näkymät + varianttilohkot (2.1–2.3).
6. **Kaksi vai kolme näkymää:** kolme — mutta näkymää, ei kurssia; yli 80 % lohkoista yhteisiä (2.2).
7. **Yhteistä kaikille:** teoria, sanasto, harjoittele, diat (kahdessa), kurssirakenne, edistymislogiikka.
8. **Omiksi kokonaisuuksiksi:** luokkatehtävät (luokka), tuntisuunnitelmat + ohjatut tehtävät + väärinkäsitykset (opettaja), lopputyövariantit, kurssiopas.
9. **Teoria / harjoitukset / opettajan materiaali:** teoria ja itsetarkistuvat harjoitukset kulkevat yhdessä kaikissa opiskelijanäkymissä; luokkaharjoitukset ovat oma kerroksensa luokkanäkymässä; opettajan materiaali on kokonaan oma polkunsa — ei koskaan opiskelijan navigaatiossa (2.2–2.3).
10. **Navigaatio oikeaan versioon:** etusivu suuntaajana (3 ovea), valinta muistetaan, syvälinkit ohittavat valinnan, headerin näkymävaihtaja (2.4).
11. **Laajennettavuus:** kurssi.yaml-manifesti + lohkosopimus; uusi moduuli = kansio + manifestirivi; uusi näkymä = konfiguraatio (2.5).
12. **Verkkokurssituki:** Harjoittele tehtäväkerroksena, lukuaikakehys, verkkolopputyöt itsearvioinnilla, SEO-jakelu, sanastokoonti (2.3, 3.3).
13. **Opettajaoletusten uudelleenkirjoitus:** yllättävän vähän — 2 pistekohtaa teoriateksteissä + lopputyöbriefit + arviointituntien kehystys; täsmällinen lista 4.3:ssa.
14. **Poistettavaa:** content/lessons-kopio, materiaalityyppiselite, legacy-koodipolut, työjäänteet — ei varsinaista sisältöä (4.2).
15. **Yhdistettävää:** content/lessons + self-study (yksi lähde), sanastot + koottu /sanasto/-sivu, kolmen lopputyön arviointiohjeet opettajan yhteen näkymään, README + kurssi.yaml (rakenne yhdessä paikassa) (4.1).

---

*Seuraava askel, jos suunnitelma hyväksytään: vaihe 0 (inventaario ja content/lessons-poisto) on turvallinen aloittaa heti — se parantaa ylläpidettävyyttä riippumatta siitä, missä aikataulussa näkymät toteutetaan.*

