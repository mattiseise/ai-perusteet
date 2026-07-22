# ai-perusteet — repo-konventiot

Tekoälyn perusteet -verkkokurssi (aiperusteet.fi). 27 oppituntia kolmessa moduulissa (Teoria 1–9, Käyttö 10–18, Agentit 19–27). Deploy: main → GitHub → Netlify (automaattinen — push mainiin menee suoraan tuotantoon).

## Generoitu vs. lähde

- **index.html on generoitu — älä koskaan muokkaa käsin.** Aja `python3 generate_site.py` (vaatii `pip install markdown pyyaml`). Committaa index.html yhdessä lähdemuutosten kanssa.
- Sivuston lähde on `sisalto/tunnit/NN/` (NN = 01–27) + manifesti `sisalto/kurssi.yaml` (moduulit, tunnit, näkymäkonfiguraatiot — rakennemuutokset manifestiin, ei koodiin).
- Tuntien lohkot: `teoria.md`, `tehtavat-luokka.md`, `harjoittele.md` (Harjoittele; puuttuu arviointitunneilta 18 ja 27), `sanasto.md`, `diat.html` (SVG-diat); `opettaja/tuntisuunnitelma.md`, `opettaja/tehtavat-ohjatut.md`. Lopputyöbriefit: `sisalto/lopputyot/{teoria,kaytto,agentit}.md`.
- Tunti-id:t (`lesson-NN`) ovat localStorage-, GA- ja hash-avaimia — kansiot on numeroitu `NN`, mutta id:itä ei saa muuttaa.

## generate_site.py — ansat

- Pääosa sivusta on jättimäinen f-string: **kirjaimelliset aaltosulkeet tuplataan `{{ }}`**, eikä f-string-lausekkeissa saa olla kenoviivaa (laske arvo muuttujaan ennen f-stringiä).
- `PRACTICE_CSS` ja `PRACTICE_JS` ovat tavallisia moduulitason merkkijonovakioita, jotka interpoloidaan templaattiin — niissä yksinkertaiset aaltosulkeet.
- `esc_js()` escapettaa backtickit/`${`}; ptasks-JSON emittoidaan raakana ja `</` escapetaan muotoon `<\/`.
- Arviointitunneilla (18, 27; `block_type: assessment`) on eri välilehtihaara kuin opetustunneilla — ei practice-välilehteä, tarkoituksella.
- Legacy: `SLIDE_URLS` (Google Slides -embedit) — kuollut koodipolku.

## Harjoittele-tehtävämoottori

- Tehtävät kirjoitetaan `practice.md`-tiedostoihin aidattuina ` ```task `-JSON-lohkoina; `parse_practice()` kaatuu buildissa virheelliseen JSONiin (tarkoituksella).
- 7 tyyppiä: match, order, classify, quiz, scenario, spot, reflect. Moottori sekoittaa quiz-vaihtoehdot ja match-B-sarakkeen — sisällön ei tarvitse.
- Validointi muutosten jälkeen: parsi kaikki lohkot json.loads:lla + `node --check` index.html:n pää-scriptille.

## Ei saa rikkoa

- **localStorage-avaimet:** `bcai-new` (edistyminen), `bcai-practice` (tehtävätulokset), `bcai-consent` (GA-suostumus), `bcai-reflect` (reflect-vastaukset). Nimet eivät saa muuttua — kävijöiden data nollautuisi.
- **GA4:** G-4ZLJF4THGV, basic consent mode (gtag latautuu vasta bannerin hyväksynnästä, `loadGA()`), tapahtumat `lesson_open`, `lesson_complete`, `task_start`, `task_complete` + `trackEvent()`-apuri. Consent-logiikka säilytettävä.
- **Vanhat linkit:** hash-reitit `#lesson-NN`, `#lesson-NN/<tab>` (tabit: slides, selfstudy, stasks, practice, vocab, tltasks, tmats), `#brief-ospN` — linkkejä on jaettu Itslearning-kursseihin; muutokset vain redirectien kautta.

## Termilukot (koko kurssi)

- **prompti** (ei "kehote" — paitsi kertamaininta tunnin 4 teoriassa ja sanastossa: "suomeksi myös kehote"). Yhdyssanat: järjestelmäprompti.
- **pitkäkestoinen muisti** (ei pitkäaikainen), **eskalointi** (ei eskalaatio/eskalatio), **agentti = kielimalli + harness**, kuusi rakennusosaa tunnin 19 nimillä.
- **Tuotenimet: sallittuja esimerkkeinä, kiellettyjä faktoina.** Aloittelija tarvitsee konkreettisen ankkurin, joten nimeä tuotteita vapaasti havainnollistamaan (ChatGPT, Claude, Microsoft Copilot, Google Gemini, Microsoft Azure, Amazon Web Services, DeepSeek, KIMI, Mistral, Midjourney). **Älä koskaan kirjoita versionumeroita, hintoja, käyttörajoja tai konteksti-ikkunan kokoja leipätekstiin** — ne vanhenevat kuukausissa. Pidä väitteet kestävissä eroissa: vahvuusalue, ekosysteemi, mistä data tulee, kuka määrittää ehdot.
- Nopeasti muuttuvat tuotetiedot kuuluvat "Tilanne heinäkuussa 2026" -laatikoihin (tunnit 10, 19 ja 22) — ne ovat tietoisia huoltokohtia.
- **Kohderyhmä:** kurssi on kaikille avoin, ei vain työelämässä oleville. Älä oleta lukijalla työpaikkaa tai organisaatiota ("Ammattilaisena…", "organisaatiosi…"). `tests/test_yleiso.py` vahtii tätä; perustellut poikkeukset `tests/allowlists/yleiso.yaml`.
- Em-viiva (—) on talotyyli.

## Sisältötyön tapa

- Uusi tai muuttuva opetussisältö ajetaan portitetulla ketjulla: suunnittelu → rakentaminen → pedagoginen tarkistus (hyväksytty/korjattava) → suomen kielenhuolto (no_semantic_drift). Toteuta subagenteilla; raskas työ Opus-tasolla, orkestrointi ja lopputarkistus kevyemmin.
- Sävy: lämmin sinutteleva asiasuomi, väärästä vastauksesta ei moitita, ei emojeja opetussisällössä.
- **Proosa on oletus, lista poikkeus.** Aloittelijalle suunnattu teoria selitetään kappaleina. Lista on perusteltu vain kun se on aidosti listamainen: tarkistuslista, menettelyn askeleet, vertailutaulukko tai lähdeluettelo. Jos osiossa on 4+ listariviä ja alle ~90 proosasanaa, se on todennäköisesti kirjoitettava auki. Yhteenveto ei saa olla pelkkiä lihavoituja fragmentteja.
- Diat: käsin ladottua SVG:tä (960×540, `deck-slide`-divit, sivunumerot "N / M") — muutokset renderöidään ja tarkistetaan kuvana (cairosvg).

## Käynnissä: rakenneuudistus 2

Hyväksytty suunnitelma: `RAKENNEUUDISTUS-2-NAKYMAT.md` — yksi sisältöpohja, kolme näkymää (/kurssi, /luokka, /opettaja), monisivuinen generointi. Toimeksianto: `HANDOFF-RAKENNEUUDISTUS-2.md`.
