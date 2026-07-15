# AI · Perusteet — korjaushandoff agenttiputkelle

*Toimeksianto. Codex aloitti toteutuksen (ks. haaran `korjaus-handoff` WIP-commit);
ajastettu Cowork/Claude Code -putki jatkaa ja vie loppuun. Työ tehdään haaralla
`korjaus-handoff`, EI mainiin ennen kuin kaikki portit (`npm run verify:all` +
alla oleva "Valmis, kun" -lista) läpäisevät.*

## Tehtävä

Paranna kurssia niin, että:
- kurssi puhuttelee aidosti kaikkia aloittelijoita eikä oleta, että oppija on
  ammattilainen, IT-alan opiskelija tai jo työelämässä;
- kaikki kuviot, animaatiot ja interaktiiviset grafiikat toimivat puhelimella
  ilman sisällön katoamista, leikkautumista tai hankalaa sivuttaisvieritystä;
- alla luetellut sisältö- ja saavutettavuusongelmat korjataan.

Tee muutokset LÄHDETIEDOSTOIHIN (`sisalto/`, `generator/`, `assets/`,
`generate_site.py`). `index.html` ja muut julkaistavat sivut ovat generoituja —
älä korjaa niitä käsin. Noudata `CLAUDE.md`-ohjeita ja generoi lopuksi
`python3 generate_site.py`. Älä koske `sisalto/_arkisto/`-hakemistoon.

## P0 — yhtenäistä kohderyhmä kaikille

Yleisölupaus (käytä kaikkialla sama): *AI · Perusteet on avoin, suomenkielinen
alkeiskurssi kaikille tekoälyn perusteista kiinnostuneille. Aiempi tekninen
osaaminen, tietty opiskeluala tai työkokemus ei ole edellytys. Luokka- ja
opettajanäkymät tarjoavat lisäksi oppilaitoskäyttöön sovitetun toteutuksen.*

- Päivitä yleisökuvaus: `sisalto/opettaja/kurssiopas.md`, `generate_site.py`,
  `generator/sivut.py` + kaikki meta-, JSON-LD-, `llms.txt`- ja esittelytekstit.
- Rakenteinen data `educationalLevel`: käytä `perustaso`/`aloittelija`, älä sido
  koko sivustoa toiselle asteelle. Oppilaitosnäkymä kuvataan erikseen.
- 3 OSP täsmällisesti: avoin verkkokurssi on mitoitettu kolmen osaamispisteen
  laajuiseksi; osaamispisteiden myöntämisestä päättää oppilaitos.
- Korvauslinja (ei sokkoa globaalia korvausta): "ammattilaisena sinun pitää" →
  "kun käytät tekoälyä"; "ammattilainen tarkistaa" → "tarkista"/"luotettava
  käyttäjä tarkistaa"; "ammattilaisen tarkistuslista" → "luotettavan tekoälyn
  käytön tarkistuslista"; "omalla alallasi" → "valitsemassasi aiheessa";
  "työssäsi" → "arjessa, opiskelussa tai työssä"; "ammatillinen kieli"
  (arviointi) → "selkeä, asiallinen ja perusteltu kieli"; "ammatillisesti
  uskottava" → "uskottava ja toteuttamiskelpoinen".
- Säilytä "ammattilainen/ammatillinen" vain: tietyn ammatin vastuu (lääkäri,
  tietosuojavastaava), eksplisiittinen työelämäsimulaatio, tai ammatillisen
  koulutuksen toteutus opettajan ohjeissa. Dokumentoi sallitut osumat
  allowlistaan (`tests/allowlists/`).
- Anna tehtävissä aina ≥3 reittiä: arki/harrastus, opiskelu, työelämä.
- Portti: `python3 tests/test_yleiso.py` (kohderyhäskanni) ei löydä uusia
  perustelemattomia olettamia.

## P0 — korjaa mobiiligrafiikat (26 .ai-demo, tunnit 01–08,10–17,19–26)

- Ei-interaktiiviset: responsiivinen SVG (`viewBox`, `width:100%`, `height:auto`,
  `preserveAspectRatio="xMidYMid meet"`).
- Interaktiiviset (tunnit 07, 20, 24): aito mobiilitaitto — pinoa kortit,
  vaihtoehdot, palaute yhteen sarakkeeseen < 680 px. Älä skaalaa 560 px
  käyttöliittymää pieneksi kuvaksi.
- Standardoi yhteinen komponentti; siirrä responsiivinen logiikka
  `assets/site.css`:ään. Poista "vieritä sivusuunnassa" -fallback korjatuilta.
- Kosketuskohde ≥ 44×44 px; leipäteksti ≥ 12–14 px mobiilissa; ei hoveria
  ainoana vihjeenä. Kunnioita `prefers-reduced-motion: reduce`.
- SVG-semantiikka: informatiiviselle `<title>`/`<desc>` + `role="img"`;
  koristeelliselle `aria-hidden="true"`.
- Diat: responsiivinen SVG + koko näytön tila; koko näytön painike mobiilissa
  näkyvä ja ≥ 44×44 px.
- Mobiilin regressiotestit leveyksille 320/375/390/430/768 px (Playwright,
  `tests/visual/`): `document.scrollWidth ≤ clientWidth`, mikään valinta/
  palaute/painike ei jää näkymän ulkopuolelle, 200 % zoom ei peitä ohjaimia,
  toimii `/kurssi/`- ja `/luokka/`-näkymissä.

## P1 — sisältövirheet ja liian vahvat väitteet

- Tunti 01: älä määrittele KAIKKEA tekoälyä datasta oppivaksi (se on
  koneoppimista); tee selväksi ettei käyttöön otettu malli opi joka syötteestä.
- Tunti 02: älä esitä kapea AI / AGI / ASI / koneoppiminen / generatiivinen
  yhtenä viisiportaisena asteikkona — erota kykyjen laajuus ja toteutus.
- Tunti 19: kuusi komponenttia = "tämän kurssin kuusiosainen suunnittelu-
  tarkistuslista", ei agentin universaali määritelmä; vältä "sielu"-termiä
  yleisenä käsitteenä.
- Tunti 23: erota mallin piilotettu päättely, käyttäjälle annettava perustelu ja
  toteutuksen työnkulku; älä opeta tallentamaan raakaa chain-of-thoughtia;
  lokita työkalukutsut, syötteet/tulokset, toiminnot, virheet, lyhyet perustelut.
- Tunti 24: poista väite että validointi tunnistaa/tuhoaa kaikki haitalliset
  käskyt; opeta ulkoinen sisältö epäluotettavana datana, oikeuksien minimointi,
  kriittisten toimien hyväksyntä, salaisuuksien eristäminen, kerroksittainen suoja.

## P1 — pedagoginen rytmi ja arviointi

- Vähennä päällekkäisyyttä pareissa 04/12, 10/11, 07/24; kirjaa jokaiselle
  tunnille oma ydinkysymys ja tuotos.
- Tunti 16: laajasta työkalukatsauksesta valinnainen valintalaboratorio.
- Yhtenäistä aikamitoitus (tunti 19 lukuarvio; tunti 27 tehtävät ≤ 90 min).
  Määritä jokaiselle luokkatunnille 90 min perusreitti, tukireitti, syventävä
  reitti ja tallennettava tuotos.
- Teoria-lopputyö: vaadi prosessinäyttö (käytetty pyyntö/keskustelu, ≥3
  todennettua korjausta, lähteet, lyhyt suullinen puolustus) — ei "tekoäly
  kirjoittaa tekstin".
- Arviointi: "ammatillinen kieli" → "selkeä, asiallinen ja perusteltu kieli";
  lisää 100 pisteen rubriikkiin tasokuvaukset.
- Lisää itseopiskelun aloitussivu (kohderyhmä, esitiedot, ajankäyttö, tilit/
  kustannukset, tietosuoja, tuotosten tallennus; vienti md/Word/PDF).
  (Codex on aloittanut: `sisalto/aloitus.md`.)
- Tarjoa toimittajariippumaton vaihtoehto Copilotille ja n8n:lle.

## P2 — lähteet, saavutettavuus, ylläpidettävyys

- Jokaisen `teoria.md`:n loppuun 2–5 luotettavaa lähdettä + tarkistuspäivä;
  erottele vakaa teoria nopeasti muuttuvista tuote-/hintatiedoista.
- Välilehtien semantiikka: `tablist`/`tab`/`tabpanel`/`aria-selected` +
  nuolinäppäinnavigaatio. Palautteisiin `aria-live`; reflektiokentille nimi.
- Korjaa tuntien 16 ja 27 päällekkäiset H1:t ja sisäkkäiset "Pysähdy
  hetkeksi" -blockquotet.
- Lukuaika näkyvästä tekstistä (ei SVG/CSS/UI-koodia).
- Kiinnitä riippuvuusversiot; `LICENSE` juureen (CC BY-SA 4.0). (Codex tehnyt.)
- Buildiin sisältö-, linkki-, saavutettavuus- ja responsiivisuustestit.
  (Codex tehnyt: `npm run verify` / `verify:all`.)
- Merkitse tarkoitukselliset virheet/artefaktit — jos virheenetsintä on
  oppimistavoite, tee siitä selkeä tehtävä ja tarjoa oikeat vastaukset.

## Toteutuksen rajat

- Säilytä kolme näkymää (`/kurssi`, `/luokka`, `/opettaja`) ja yksi sisältölähde.
- Älä poista työelämäesimerkkejä; muuta vain oletus että oppija on ammattilainen.
- Ei prosentuaalista koko UI:n pienennystä mobiilissa — aito uudelleentaitto.
- Ei uusia tuotekohtaisia väitteitä ilman lähdettä ja tarkistuspäivää.
- Älä muuta `sisalto/_arkisto/`.

## Valmis, kun (kaikkien oltava tosi ennen mainiin mergeä)

1. Yleisölupaus sama etusivulla, metadatassa, `llms.txt`:ssä, opettajan
   oppaassa ja kurssitekstissä.
2. Satunnainen lukija voi tehdä tehtävät ilman omaa alaa/työpaikkaa/tiliä.
3. `python3 tests/test_yleiso.py` ei löydä uusia perustelemattomia olettamia
   (sallitut osumat allowlistattu).
4. Kaikki 26 .ai-demoa läpäisevät mobiilitestit; tuntien 07/20/24 interaktiiviset
   tilat toimivat kosketuksella ja näppäimistöllä.
5. Ei vaakasivuylivuotoa leveyksillä 320–768 px.
6. `python3 generate_site.py` ilman virheitä; sisäiset linkit toimivat;
   `npm run verify:all` vihreä (sisältö + js + Playwright-selain/a11y).
7. Ei merkitsemättömiä tarkoituksellisia virheitä tuotantomateriaalissa.

## Työtapa (jokainen ajokerta)

- Käytä CLAUDE.md:n portitettua ketjua uuteen/muuttuvaan opetussisältöön
  (suunnittelu → rakentaminen → pedagoginen tarkistus → kielenhuolto), Opus/
  Sonnet-subagenteilla. Säilytä sävy, termilukot, em-viiva, ei emojeja.
- Committaa pienissä erissä suomeksi. ÄLÄ pushaa mainiin ennen kuin KAIKKI
  "Valmis, kun" -kohdat täyttyvät ja `npm run verify:all` on vihreä.
