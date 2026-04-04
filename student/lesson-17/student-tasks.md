# Lesson 17: Opiskelijan tehtävät

## Tehtävä 1: Debuggaa ja testaa — virheitä etsimässä (TT-D2)

**Tavoite:** Löytää ja korjata virheitä tekoälyn tuottamassa koodissa.

Saat seuraavan koodin, joka on "melkein oikea", mutta siinä on virheitä. Sinun tehtävä on:
1. Ajaa koodi useilla syötteillä
2. Löytää virheet
3. Dokumentoida, mitä meni pieleen
4. Korjata koodi (joko itse tai pyytämällä tekoälyltä)

**Esimerkkikoodi (valitse yksi, tai opettaja antaa):**

```python
# Funktio, joka tarkistaa, onko luku alkuluku
def is_prime(n):
    if n < 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

**Dokumentointilomake:**

```
VIRHEIDEN ETSINTÄ JA KORJAUS

Alkuperäinen koodi:
[liitä koodi]

TESTAUKSET:

Test 1 — Normaali tapaus:
  Syöte: is_prime(7)
  Odottu: True (7 on alkuluku)
  Saatu: [kirjoita tulos]
  Oikein? [ ] Kyllä [ ] Ei

Test 2 — Reuna tapaus:
  Syöte: is_prime(1)
  Odottu: False (1 ei ole alkuluku määritelmän mukaan)
  Saatu: [tulos]
  Oikein? [ ] Kyllä [ ] Ei
  
Test 3 — Reuna tapaus:
  Syöte: is_prime(2)
  Odottu: True (2 on pienin alkuluku)
  Saatu: [tulos]
  Oikein? [ ] Kyllä [ ] Ei

VIRHEET LÖYDETTY:
- Virhe 1: [kuvaus]
  Syy: [miksi se tapahtuu logiikassa]
  Oikea käyttäytyminen: [mitä pitäisi tapahtua]
  
- Virhe 2: [seuraava virhe, jos löydät]

KORJAUS:

Korjattu koodi:
[kirjoita korjattu versio]

Testasin uudelleen:
- Test 1: [tulos] ✓
- Test 2: [tulos] ✓
- Test 3: [tulos] ✓

Kaikki testit menivät läpi!
```

**Arvioinnin kriteerit:**
- Testit ovat dokumentoituja
- Virheet on tunnistettu oikein
- Korjaukset ovat loogisia
- Uudelleen testaus osoittaa, että korjaukset toimivat

---

## Tehtävä 2: Tietoturva — haavoittuvuuksien etsintä (A2-TT)

**Tavoite:** Nähdä, kuinka tekoäly voi tuottaa turvattomia koodia.

Annetaan seuraava koodi. Sinun tehtävä on:
1. Lue koodi kriittisesti
2. Etsi tietoturvaongelmia
3. Dokumentoi, miksi se on ongelma
4. Kirjoita turvallinen versio

**Esimerkkikoodi (valitse yksi, tai opettaja antaa):**

```python
# Käyttäjän kirjautuminen
def login(username, password):
    # Tietokanta kysely
    user_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    user = database.execute(user_query)
    if user:
        return "Login successful"
    else:
        return "Login failed"
```

**Analyysi-lomake:**

```
TIETOTURVAHAAVOITTUVUUKSIEN ETSINTÄ

Koodi:
[liitä alkuperäinen koodi]

HAAVOITTUVUUS 1:
Ongelma: [mikä on turvaton]
Hyökkäys-skenario: Kuvittele, että hyökkääjä antaa syötteeksi...
[kuvaile, mitä voisi käydä]

Miksi se on riski?
[selitys]

HAAVOITTUVUUS 2:
[seuraava ongelma, jos näet]

TURVALLINEN VERSIO:

Korjattu koodi:
[kirjoita turvallinen versio, käyttäen parametrisoituja kyselyitä tai muita teknikoita]

Miksi tämä on turvallisempaa?
[selitys]
```

**Arvioinnin kriteerit:**
- Vähintään yksi haavoittuvuus on tunnistettu oikein
- Hyökkäys-skenario on realistinen
- Korjaus käyttää oikeaa tekniikkaa (esim. parametrisoidut kyselyt)

---

## Kotitehtävä

Valitse tehtävä 1 tai 2. Tee sitä vähintään 45 minuuttia. Palauta dokumentointilomake opettajallesi seuraavalla tunnilla.

**Bonus:** Jos haluat harjoitella enemmän, tee molemmat tehtävät tai kysy opettajalta muita koodeita analysoitavaksi.
