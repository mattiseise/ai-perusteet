# Lesson 17: Opettajan materiaalit

## Oppimistulokset ja konteksti

**Mitä opiskelija pitää ymmärtää:**
1. Tekoäly voi tuottaa virheitä, joita ei näe silmällä
2. Testaus on kriittistä ja paljastaa virheitä
3. Perusteita pitää osata korjatakseen koodia
4. Tietoturva on tärkeää — tekoäly voi tuottaa haavoittuvaa koodia
5. Refaktorointi parantaa koodeja

## Yleisiä väärinkäsityksiä

| Väärinkäsitys | Oikea ymmärrys |
|---|---|
| "Hyvältä näyttävä koodi on automaattisesti oikea" | Testaus paljastaa virheet, joita silmällä ei näe |
| "En ymmärrä koodia, mutta se toimii, niin se on OK" | Ymmärrys on kriittistä debuggaukselle |
| "Tekoäly ei voi tuottaa turvattomia koodia" | Tekoäly hallusinoi turvallisuudesta — tarkista aina |
| "Refaktorointi on turhaa, jos koodi toimii" | Refaktorointi parantaa laatu, nopeus ja ylläpitävyyttä |

## "Check For Understanding" -kysymykset

- Miksi testaus on tärkeää, vaikka koodi näyttää hyvälle?
- Mitä eroa on normaalilla testisyötteella ja reunatapauksella?
- Kuinka korjaisit koodia, jota et ymmärrä?
- Mikä on SQL-injektio ja kuinka se toimii?
- Mitä on refaktorointi ja milloin sitä tehdään?

## Oppitunnin rakenne (90 min)

| Aika | Vaihe |
|------|-------|
| 0–10 min | Johdanto: "Tekoäly ei ole täydellinen" |
| 10–35 min | Itsenäinen lukeminen + keskustelu perusteista |
| 35–55 min | Tehtävä 1 — opiskelijat testaa ja debuggaa (opettaja kiertää) |
| 55–75 min | Tehtävä 2 — tietoturvaongelmat ja korjaukset |
| 75–90 min | Yhteenveto + verifiointi-prosessi + kotitehtävät |

## Opettajan checklist

- [ ] Esimerkkikoodi on valmiina (is_prime, divide_list, SQL-kysely)
- [ ] Dokumentointilomakkeita on tulostettuna
- [ ] Opiskelijat tietävät, miten ajaa Python-koodia
- [ ] Opiskelijat ymmärtävät, mitä "testaus" tarkoittaa
- [ ] Opiskelijat tietävät ainakin yhden tietoturvariski-esimerkin
