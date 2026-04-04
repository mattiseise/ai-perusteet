# AI-avusteinen ohjelmointi II: debuggaus, testaus ja verifiointi

## Johdanto

Saat ChatGPT:ltä koodin, joka näyttää täydelliseltä. Kopioit sen, ajastat sen — ja se ei toimi. Ehkä se kaatuu, ehkä se tuottaa väärän tuloksen. Nyt sinulla on kaksi vaihtoehtoa: antaa periksi tai oppia debuggaamaan. Debuggaus on prosessi, jossa etsit virheitä ja korjaat ne. Ilman sitä et voi käyttää tekoälyn tuottamaa koodia tuotannossa.

Tässä oppitunnissa opit, miten tarkistaa, testata ja korjata tekoälyn tuottamaa koodia. Opit myös, miksi ohjelmoinnin perusteita pitää edelleen osata — sinun pitää ymmärtää koodi, jotta voit korjata sen, kun se ei toimi. Tekoäly tuottaa, mutta opiskelija tarkistaa. Tietoturva on myös tärkeää — tekoäly voi tuottaa haavoittuvaa koodia, joka näyttää hyvältä mutta vaarantaa järjestelmän.

## Miksi perusteita pitää osata: "Black Box" -ongelma

Kuvittele, että pyydät tekoälyä kirjoittaa funktio, joka validoi sähköpostiosoitteen. Saat:

```python
def is_valid_email(email):
    return "@" in email and "." in email
```

Näyttää hyvin ja se toimii. Mutta onko se todella kunnollinen? Testaat:
- "test@example.com" → True (hyvä)
- "test@test" → True (HUONO! Ei ole oikea sähköposti, koska piste puuttuu)
- "test..example.com" → True (HUONO! Piste on, mutta no @)

Funktio on kelvoton. Nyt sinulla on kaksi polkua:

**Polku 1:** Et ymmärrä koodia. Kopioit sen, se epäonnistuu, ja annat periksi.

**Polku 2:** Ymmärrät sähköpostiosoitteen rakennetta. Tiedät, että sähköpostissa pitää olla @ ja piste, ja piste pitää tulla @ jälkeen. Voit nyt:
- Nähdä virheen: tämä funktio ei tarkista pisteiden järjestystä
- Korjata sen: "Piste pitää tulla @ jälkeen"
- Testata korjauksia
- Opettaa tekoälylle: "Kirjoita funktio uudelleen, varmista, että piste tulee @ jälkeen"

Polku 2 vaatii **perusteita**. Et voi korjata koodia, jota et ymmärrä.

> **Pysähdy hetkeksi:** Katsotaan yllä olevaa email-funktiota. Mitä muita tapauksia se epäonnistuisi? Ajatella kolmea tapausta, joissa tämä funktio antaisi väärän tuloksen.

## Testaus: verifikointiprosessi

Testaus tarkoittaa sitä, että ajastat koodia tunnetuilla syötteillä ja tarkistat, että tulokset ovat oikeat. Testaus on kriittistä, koska se paljastaa virheet ennen kuin käyttäjät kohtaavat ne.

**Mitä testata:**

1. **Normaalit tapaukset**
   - "Funktio pitäisi toimia näillä tavallisilla syötteillä"
   - Esimerkki: Laskija-funktio 5 + 3:lla, odotus: 8

2. **Reunatapaukset (edge cases)**
   - "Mitä tapahtuu rajatapauksissa?"
   - Tyhjä lista, negatiivinen luku, nolla, erittäin suuri luku, erittäin pitkä merkkijono
   - Esimerkki: Laskija-funktio 0:lla, negatiivisella luvulla

3. **Virhea-tapaukset**
   - "Mitä tapahtuu, kun käyttäjä antaa väärän tyypin?"
   - Merkkijono luvun sijaan, None arvon sijaan
   - Esimerkki: Laskija-funktio merkkijonolla "abc"

**Esimerkki testauksesta:**

Sait tekoälyltä funktio, joka laskee tekijän (factorial):

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

Testaat:
```python
print(factorial(5))    # Odotus: 120 — Toimii
print(factorial(0))    # Odotus: 1 — Toimii
print(factorial(-1))   # Odotus: ? — Kaatuu (rekursio ei pysähdy)
print(factorial(1000)) # Odotus: ? — Kaatuu (liian syvä rekursio)
```

Huomaat kaksi ongelmaa:
1. Negatiivinen luku aiheuttaa äärettömän rekursion
2. Liian suuri luku aiheuttaa stack overflow -virheen

Nyt voit:
- Tarkistaa virheen syyn (perusteiden ymmärrys auttaa)
- Korjata sitä: tarkistaa, että n on positiivinen, tai käyttää iteratiivista versiota
- Testata uudelleen

## Debuggaus: virheen löytäminen ja korjaaminen

Debuggaus on prosessi, jossa jäljität, miksi koodi ei toimi. Tavallisesti siihen kuuluu:

1. **Virheviesti lukeminen** — Python kertoo, mitä meni pieleen
2. **Lokit ja tulostukset** — print() auttaa näkemään, mitä koodi tekee
3. **Debuggerin käyttö** — editor voi pysäyttää koodin, näyttää muuttujan arvot

**Esimerkki:**

Sait tämän koodin:

```python
def divide_list(numbers):
    result = []
    for n in numbers:
        result.append(n / 2)
    return result
```

Kokeitat:
```python
print(divide_list([10, 20, "30"]))
```

Virheilmoitus: `TypeError: unsupported operand type(s) for /: 'str' and 'int'`

Virhe on selvä: "30" on merkkijono, ei luku. Nyt voit:
- Korjata syötteen: käytä kokonaislukuja
- Tai korjata funktiota: lisää tarkistus: `if isinstance(n, (int, float)): ...`

Logiikkaa varten voit käyttää tulostuksia:

```python
def find_max(numbers):
    max_val = numbers[0]
    for n in numbers:
        print(f"Checking {n}, current max: {max_val}")
        if n > max_val:
            max_val = n
    return max_val
```

Ajatat ja näet, mitä tapahtuu joka iteraatiolla.

## Refaktorointi: koodin parantaminen

Refaktorointi tarkoittaa koodin muuttamista paremmin ilman sen toiminnon muuttamista. Tekoäly voi antaa koodia, joka toimii, mutta on epätehokas tai vaikealukuinen.

Esimerkiksi:

```python
# Tekoälyn antama koodi — toimii, mutta hidas
result = []
for i in range(len(items)):
    if items[i] > 5:
        result.append(items[i] * 2)
```

Voit refaktoroida:

```python
# Parempi — käyttää list comprehensionia
result = [item * 2 for item in items if item > 5]
```

Molemmat tekevät saman asian, mutta jälkimmäinen on nopeampi ja lyhyempi.

> **Pysähdy hetkeksi:** Mieti yhtä funktiota, jonka olet kirjoittanut tai nähnyt. Mitä voit refaktoroida siinä? Miten tekisit siitä luettavampaa tai nopeampaa?

## Tietoturva: tekoäly voi tuottaa haavoittuvaa koodia

Tekoäly voi tuottaa koodia, joka näyttää hyvältä, mutta on tietoturvariski.

**Esimerkki 1: SQL-injektio**

Pyydät tekoälyä: "Kirjoita koodi, joka hakee käyttäjää tietokannasta käyttäjätunnuksella"

Saat:

```python
username = input("Username: ")
query = f"SELECT * FROM users WHERE username = '{username}'"
db.execute(query)
```

Näyttää OK:lle. Mutta jos käyttäjä antaa: `admin' OR '1'='1`, kysely tulee:
```
SELECT * FROM users WHERE username = 'admin' OR '1'='1'
```

Nyt se palauttaa KAIKKI käyttäjät. Tämä on **SQL-injektio-haavoittuvuus**.

**Oikea tapa:**

```python
username = input("Username: ")
query = "SELECT * FROM users WHERE username = ?"
db.execute(query, (username,))
```

Käyttäjän syötettä ei yhdistetä suoraan kyselyyn — sen sijaan se käytetään parametrina.

**Esimerkki 2: Salasanojen tallennus**

Väärä:
```python
# ÄLKÖÖN TÄTÄ TEE
password_hash = username + password  # Tämä ei ole hash!
```

Oikea:
```python
import hashlib
password_hash = hashlib.sha256(password.encode()).hexdigest()
```

**Tarkistus-lista tietoturvolle:**
- Käytetäänkö parametrisoituja kyselyitä?
- Tallennetetaanko salasanoja kunnolla (hash, ei selkokielellä)?
- Tarkistetaanko käyttäjän syötteen pituus ja tyyppi?
- Onko herkkä tieto kryptattu?

## Verifiointi-prosessi: kokonaisuus

Käy seuraava prosessi läpi jokaiselle tekoälyn koodille:

```
1. LÄHETÄ PYYNTÖ — Kerro AI:lle tarkasti mitä haluat
2. SAA KOODI — Kopioi ja tarkista sitä
3. TESTAA NORMAALIT — Aja normaaleilla syötteillä
4. TESTAA REUNAT — Testaa edge cases
5. LAINAA LOGIIKKAA — Ymmärrätkö, mitä koodi tekee?
6. TARKISTA TURVALLISUUS — Onko siinä tietoturvahaavoittuvuuksia?
7. DEBUGGAA, JOS VIRHE — Käytä tulostuksia ja logiikkaa
8. REFAKTOROI, JOS TARPEELLINEN — Parantele sitä
9. DOKUMENTOI — Kirjoita kommentit
10. HYVÄKSY — Nyt voit käyttää sitä
```

## Yhteenveto

Tekoäly tuottaa koodia, mutta sinun pitää tarkistaa se. Perusteita pitää osata, koska et voi korjata koodia, jota et ymmärrä. Testaus paljastaa virheet ennen käyttöönottoa. Debuggaus auttaa löytämään ja korjaamaan ongelmia. Refaktorointi parantaa koodia. Tietoturvasta pitää huolehtia — tekoäly voi tuottaa haavoittuvaa koodia. Verifiointi-prosessin noudattaminen varmistaa, että tekoälyn koodi on turvallista, oikea ja ymmärrettävää.
