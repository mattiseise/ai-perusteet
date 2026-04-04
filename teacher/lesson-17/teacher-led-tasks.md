# Lesson 17: Opettajavetoiset tehtävät

## Tehtävä 1: Testauksen tärkeys — virheitä etsimässä

**Aika:** 20 min

1. Näytä opiskelijoille is_prime-funktio (tai muuta esimerkkiä):

```python
def is_prime(n):
    if n < 2:
        return True  # BUG: 1 ei ole alkuluku!
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

2. Pyydä opiskelijoita ajaa se näillä syötteillä:
   - `is_prime(7)` → True ✓
   - `is_prime(1)` → True ✗ (virhe!)
   - `is_prime(4)` → False ✓

3. Näytä, kuinka testaus paljasti virheen:
   - Ensimmäinen testi näyttää siltä että toimii
   - Toinen testi osoittaa, että logiikka on väärä (1 ei pitäisi palauttaa True)

4. Yhdessä: mitä koodi pitäisi korjata? (muuta `if n < 2: return True` → `if n < 2: return False`)

**Tekniikka:** Opiskelijat näkevät konkreettisesti, kuinka testit paljastaisivat virheitä.

---

## Tehtävä 2: Tietoturvahaavoittuvuus — SQL-injektio live demo

**Aika:** 25 min

1. Näytä epäturvallinen koodi:

```python
username = input("Username: ")
password = input("Password: ")
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
print("Query:", query)
```

2. Aja se normaalilla syötteellä:
   - Username: "alice"
   - Password: "secret123"
   - Näytä kysely: `SELECT * FROM users WHERE username = 'alice' AND password = 'secret123'`
   - Näyttää oikealta!

3. Nyt hyökkäys: anna tämä syöte:
   - Username: `admin' OR '1'='1`
   - Password: `anything`
   - Näytä kysely: `SELECT * FROM users WHERE username = 'admin' OR '1'='1' AND password = 'anything'`
   - Selitä: Ehto `'1'='1'` on aina totta, joten kysely palauttaa kaikki käyttäjät!

4. Näytä turvallinen versio:

```python
query = "SELECT * FROM users WHERE username = ? AND password = ?"
# Parametrit lähetetään erikseen, ei yhdistetty kyselyyn
db.execute(query, (username, password))
```

Selitä: Käyttäjän syötteen ei saa yhdistää kyselyyn — se pitää käyttää parametrina.

**Tekniikka:** Opiskelijat näkevät, kuinka tekoäly voi vahingossa tuottaa haavoittuvaa koodia.

---

## Tehtävä 3: Refaktorointi — parantele koodia

**Aika:** 15 min

Näytä alkuperäinen koodi:

```python
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for i in range(len(items)):
    if items[i] % 2 == 0:
        result.append(items[i] * 2)
```

Refaktoroitu versio:

```python
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [item * 2 for item in items if item % 2 == 0]
```

Vertaa:
- Molemmat tekevät saman asian
- Toinen on lyhyempi ja nopeampi
- Toinen on Python-tyylikkäämpi

Diskussio: Milloin refaktorointi on tärkeää? (laatu, nopeus, luettavuus)
