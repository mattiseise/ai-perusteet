# ai-perusteet — repo-konventiot

Tekoälyn perusteet -verkkokurssi (aiperusteet.fi). 27 oppituntia kolmessa moduulissa (Teoria 1–9, Käyttö 10–18, Agentit 19–27). Deploy: main → GitHub → Netlify (automaattinen — push mainiin menee suoraan tuotantoon).

## Generoitu vs. lähde

- **index.html on generoitu — älä koskaan muokkaa käsin.** Aja `python3 generate_site.py` (vaatii `pip install markdown`). Committaa index.html yhdessä lähdemuutosten kanssa.
- Sivuston lähde on `student/lesson-NN/` ja `teacher/lesson-NN/` — EI `content/lessons/` (ajautunut legacy-kopio, poistetaan rakenneuudistuksessa).
- Tuntien lohkot: `self-study.md` (teoria), `student-tasks.md` (luokkatehtävät), `vocabulary.md`, `practice.md` (Harjoittele), `slides.html` (SVG-diat); opettajalla `teacher-materials.md`, `teacher-led-tasks.md`.

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
- Tuotenimet ja päivämäärät vain "Tilanne heinäkuussa 2026" -laatikoissa (tunnit 19 ja 22) — ne ovat tietoisia huoltokohtia.
- Em-viiva (—) on talotyyli.

## Sisältötyön tapa

- Uusi tai muuttuva opetussisältö ajetaan portitetulla ketjulla: suunnittelu → rakentaminen → pedagoginen tarkistus (hyväksytty/korjattava) → suomen kielenhuolto (no_semantic_drift). Toteuta subagenteilla; raskas työ Opus-tasolla, orkestrointi ja lopputarkistus kevyemmin.
- Sävy: lämmin sinutteleva asiasuomi, väärästä vastauksesta ei moitita, ei emojeja opetussisällössä.
- Diat: käsin ladottua SVG:tä (960×540, `deck-slide`-divit, sivunumerot "N / M") — muutokset renderöidään ja tarkistetaan kuvana (cairosvg).

## Käynnissä: rakenneuudistus 2

Hyväksytty suunnitelma: `RAKENNEUUDISTUS-2-NAKYMAT.md` — yksi sisältöpohja, kolme näkymää (/kurssi, /luokka, /opettaja), monisivuinen generointi. Toimeksianto: `HANDOFF-RAKENNEUUDISTUS-2.md`.
