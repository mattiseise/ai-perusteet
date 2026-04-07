# Opettajan johtamat tehtävät – Lesson 22

## Aktiviteetti 1: Whitelist-mallit (20 min)

**Selitys**: Whitelist = luettelo siitä, mitä agentti saa tehdä. Kaikki muu on kiellettyä.

**Esittely**: Näytä kolme erilaista whitelist:ia — tiukka, kohtuullinen, liian löysä.

```
TIUKKA (liian rajoitettu):
- CLI: vain ls
- Tiedostot: vain lukea /reports/, ei kirjoittaa
- Verkkohaku: ei millään

KOHTUULLINEN:
- CLI: ls, mkdir, cp (ei rm, rm -rf)
- Tiedostot: lukea /data/, kirjoittaa /reports/
- Verkkohaku: Wikipedia, hallitus.fi

LIIAN LÖYSÄ:
- CLI: kaikki komennot
- Tiedostot: kaikki
- Verkkohaku: kaikki sivustot
```

**Ryhmätyö**: Opiskelijat suunnittelevat whitelist:in kolmelle eri agenttityypille:
1. Asiakastuki-agentti
2. Analytiikka-agentti
3. Tietotuki-agentti

**Esitys ja keskustelu**: Ryhmät verraavat whitelist:iään. Miksi eroavat?

---

## Aktiviteetti 2: Orkestrointi — järjestys on kriittinen (20 min)

**Selitys**: Agentti kutsuu työkaluja järjestyksessä. Tämä järjestys on kriittinen.

**Esittely**: Analystiikka-agentin prosessi:
1. Lue tiedostot (myyntitiedot.csv)
2. Hae verkkoa (markkinatrendit, kilpailijat)
3. Ajaa CLI (analyysiskripti)
4. Kirjoita tiedostot (raportti)

**Väärin järjestyksessä**: 
- "Ajaa analyysiskriptin, mutta tiedostot eivät ole vielä luettu" → virhe
- "Kirjoittaa raportin, mutta analyysia ei ole vielä tehty" → tyhjä raportti

**Ryhmätyö**: Opiskelijat valitsevat prosessin ja järjestävät työkalut oikein.

**Tehtävä**: Piirrä työnkulkukaavio, jossa näkyy jokainen työkalu ja kuinka ne syöttävät toisiinsa.

---

## Aktiviteetti 3: Riskiskenaariset (20 min)

**Selitys**: Jokainen työkalu tuo riskin. Entä jos agentti tekee virheen?

**Esittely**: Kolme riskiskenaaria:

```
TIEDOSTOT: Agentti kirjoittaa väärään kansioon, poistaa tärkeät tiedostot
VERKKOHAKU: Agentti etsii salasia, maksaa kalliita hakuja
CLI: Agentti ajaa "rm -rf /", poistaa koko järjestelmän
```

**Ryhmätyö**: Opiskelijat valitsevat yhden skenaarion ja suunnittelevat:
1. Miten riski syntyy?
2. Mitä haittaa se aiheuttaa?
3. Miten sen olisi voinut estää? (whitelist, rajoitus, seuranta)

**Esitys**: Ryhmät esittelevät riskinsä ja ehkäisyn.

---

## Aktiviteetti 4: Oikea työkalu oikeaan tehtävään (15 min)

**Selitys**: Jokaiselle tehtävälle tarvitaan eri työkalut.

**Esittely**: Kolme tehtävää, joista jokaiselle selitetään, miksi tarvitsee mitä:

- **Laskun käsittely**: Tietokanta (API), lokit (tiedostot), ei verkkohakua
- **Kyberturvatila**: Verkkohaku (uutiset), lokit (CLI), raportti (tiedostot)
- **Palvelinanalyysi**: Lokit (tiedostot), ei verkkohakua, CLI (komentoja)

**Ryhmätyö**: Opiskelijat valitsevat tehtävän ja päättävät, mitä työkaluja tarvitaan.

---

## Herättimet

- "Mitä tapahtuu, jos whitelist on liian tiukka?"
- "Voiko agentti tehdä vahinkoa verkkohakulla?"
- "Mitä tapahtuu, jos agentti kutsuu työkalut väärässä järjestyksessä?"
