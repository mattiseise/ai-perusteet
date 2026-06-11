# Lessons 21–25: Rakenna oma agentti n8n:llä — Tiedostoindeksi

## Luetteloimaton sisältö

Luotu **20 uutta tiedostoa** seuraavaan hakemistorakenteeseen:

```
ai-perusteet/
├── student/
│   ├── lesson-21/
│   │   ├── student-tasks.md (4 tehtävää: konteksti-ikkuna, vektoritietokanta, tila, soul)
│   │   ├── vocabulary.md (13 termiä)
│   │   └── self-study.md (olemassa)
│   │
│   ├── lesson-22/
│   │   ├── student-tasks.md (4 tehtävää: whitelist, orkestrointi, riskit, tools)
│   │   ├── vocabulary.md (14 termiä)
│   │   └── self-study.md (olemassa)
│   │
│   ├── lesson-23/
│   │   ├── student-tasks.md (4 tehtävää: ReAct, ketjuajattelu, valinta, moniagentti)
│   │   ├── vocabulary.md (12 termiä)
│   │   └── self-study.md (olemassa)
│   │
│   ├── lesson-24/
│   │   ├── student-tasks.md (4 tehtävää: injection, hallusinaatiot, oikeudet, 4-kerros)
│   │   ├── vocabulary.md (14 termiä)
│   │   └── self-study.md (olemassa)
│   │
│   └── lesson-25/
│       ├── student-tasks.md (4 tehtävää: säännöt, portti, työnkulku, oppiminen)
│       ├── vocabulary.md (13 termiä)
│       └── self-study.md (olemassa)
│
└── teacher/
    ├── lesson-21/
    │   ├── teacher-led-tasks.md (5 aktiviteettiä, 95 min yhteensä)
    │   ├── teacher-materials.md (pedagogiset selitykset)
    │   └── self-study.md (olemassa)
    │
    ├── lesson-22/
    │   ├── teacher-led-tasks.md (4 aktiviteettiä, 75 min yhteensä)
    │   ├── teacher-materials.md (pedagogiset selitykset)
    │   └── self-study.md (olemassa)
    │
    ├── lesson-23/
    │   ├── teacher-led-tasks.md (4 aktiviteettiä, 75 min yhteensä)
    │   ├── teacher-materials.md (pedagogiset selitykset)
    │   └── self-study.md (olemassa)
    │
    ├── lesson-24/
    │   ├── teacher-led-tasks.md (4 aktiviteettiä, 80 min yhteensä)
    │   ├── teacher-materials.md (pedagogiset selitykset)
    │   └── self-study.md (olemassa)
    │
    └── lesson-25/
        ├── teacher-led-tasks.md (4 aktiviteettiä, 75 min yhteensä)
        ├── teacher-materials.md (pedagogiset selitykset)
        └── self-study.md (olemassa)
```

---

## Oppituntien pääaiheet

| Lesson | Pääaihe | Red thread | Keskeinen oppiminen |
|--------|---------|-----------|---------------------|
| 21 | Muisti ja konteksti | Agentti näkee, muistaa ja seuraa | Konteksti-ikkuna, vektoritietokanta, tila, soul |
| 22 | Työkalut | Agentti kutsuu työkaluja järjestyksessä | Whitelist, orkestrointi, riskinhallinta |
| 23 | Suunnittelumallit | Agentti ajattelee oikein | ReAct, ketjuajattelu, moniagentti |
| 24 | Turvallisuus | Agentti on suojattu hyökkäyksiltä | Injection, hallusinaatiot, minimioikeudet |
| 25 | Human-in-the-loop | Agentti tekee yhteistyötä ihmisen kanssa | Hyväksyntäportit, feedback, oppiminen |

---

## Tehtävien rakenne

Jokainen oppitunti sisältää **4 tehtävää**, jotka ovat:

- **TT-A**: Rakentaminen/suunnittelu (whitelistit, tilakaaviot, työnkulut)
- **TT-B**: Analyysi/vertailu (semanttiset haut, mallinvalinta)
- **TT-C**: Päätöksenteko/validointi (turvallisuus, oikeudet)
- **TT-D**: Synteesi/integraatio (kokonaisuus, moniagentti, hybridi-prosessit)

Kaikki tehtävät ovat **artifakti-tyyppisiä** — opiskelijat rakentavat konkreettisia asioita (taulukoita, kaavioita, dokumentteja), eivät kirjoita esseitä.

---

## Opettajan aktiviteetit

Jokaisen oppitunnin opettaja johtaa **4–5 aktiviteettiä**, yhteensä 75–95 minuuttia:

- Demo/esittely
- Käsityöt (ryhmissä)
- Kaavioiden piirtäminen
- Esitys ja keskustelu
- Herättimet syvemmälle pohdinalle

---

## Sanasto

Jokaisen oppitunnin sanasto sisältää 12–15 keskeistä termiä + määritelmät:

**Lesson 21**: konteksti-ikkuna, pitkäaikainen muisti, vektoritietokanta, tila, soul...
**Lesson 22**: työkalu, whitelist, API, loggaus, riskinhallinta, hiekkalaatikko...
**Lesson 23**: ReAct, ketjuajattelu, iteraatio, moniagentti, orkestraatio...
**Lesson 24**: prompt injection, hallusinaatio, minimioikeusperiaate, validointi...
**Lesson 25**: human-in-the-loop, hyväksyntäportti, eskalatio, feedback...

---

## n8n-yhteys

Jokainen oppitunti liittyy suoraan n8n-agentin rakentamiseen:

- **Lesson 21**: Conversation history ja muistin hallinta n8n:ssa
- **Lesson 22**: API-kutsujen, tiedostojen ja CLI-komentojen integrointi
- **Lesson 23**: ReAct/chain-of-thought lohkot n8n:ssa
- **Lesson 24**: Validointi-, rajoitus- ja seuranta-lohkot
- **Lesson 25**: Approval-lohkot ja human-in-the-loop toteutus

---

## Käyttöohjeet opettajille

1. **Ennen oppituntia**: Lue `teacher-materials.md` pedagogisesta näkökulmasta
2. **Aktiviteetit**: Seuraa `teacher-led-tasks.md`:n aktiviteetteja ajallaan
3. **Keskustelu**: Käytä herättimiaä syvemmälle pohdinalle
4. **Kotitehtävät**: Opiskelijat tekevät `student-tasks.md`:n tehtävät

---

## Sisältöominaisuudet

- Kaikki suomeksi ✓
- Agent-fokusoidtu (ei abstraktion) ✓
- LLM-resistentit tehtävät (rakentaminen, ei esseet) ✓
- N8n-integroitu (konkreettinen linkitys) ✓
- Pedagogisesti strukturoitu (Demo → Ryhmä → Esitys → Keskustelu) ✓

---

## Tiedostojen yhteenveto

```
OPISKELIJAMATERIAALI (10 tiedostoa):
- 5 × student-tasks.md (4 tehtävää kukin) = 20 tehtävää
- 5 × vocabulary.md (12-15 termiä kukin) = 67 termiä

OPETTAJAMATERIAALI (10 tiedostoa):
- 5 × teacher-led-tasks.md (4-5 aktiviteettiä kukin) = 22 aktiviteettiä
- 5 × teacher-materials.md (pedagogiset selitykset)

YHTEENSÄ: 20 UUTTA TIEDOSTOA
```

---

## Miksi nämä oppitunnit?

Red thread-polku kohti n8n-projektin: Opiskelijat oppivat, mitä agentti on (Lesson 19–20), kuinka se toimii (Lesson 21–25) ja sitten rakennetaan oma agentti n8n:ssä.

Sekvenssi:
1. **Lesson 21**: Agentti **näkee** ja **muistaa** (perusta)
2. **Lesson 22**: Agentti **tekee** asioita (toiminta)
3. **Lesson 23**: Agentti **ajattelee** oikein (äly)
4. **Lesson 24**: Agentti on **turvallinen** (luottamus)
5. **Lesson 25**: Agentti **tekee yhteistyötä** ihmisen kanssa (hybridi)

= Valmis n8n-agentti
