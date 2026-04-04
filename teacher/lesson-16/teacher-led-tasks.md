# Lesson 16: Opettajavetoiset tehtävät

## Tehtävä 1: Pyyntöjen laadun vertaaminen — live demo

**Aika:** 20 min

1. Avaa tietokone ja näytä ChatGPT-näyttö (tai Claude, GPT-4, riippuu koulussa käytetystä palvelusta)

2. Kirjoita huono pyyntö ja näytä tulos:
   ```
   "Kirjoita funktio, joka tekee jotain numeroilla"
   ```
   Näytä opiskelijoille mitä saat — todennäköisesti epämääräinen koodi.

3. Kirjoita hyvä pyyntö samasta asiasta:
   ```
   "Kirjoita Python 3.10 -funktio nimeltä sum_even_numbers, joka ottaa syötteeksi listan kokonaislukuja 
   ja palauttaa kaikkien parillisten lukujen summan. Esimerkki: sum_even_numbers([1, 2, 3, 4]) palauttaa 6."
   ```

4. Vertaa tulokset:
   - Ensimmäinen koodi: liian yleinen, vaikea ymmärtää, ei ole testattavissa
   - Toinen koodi: selkeä, testattavissa, selitetysti dokumentoitu

5. Keskustele opiskelijoiden kanssa: "Mikä eroa? Miksi toinen on parempi?"

**Tekniikka:** Opiskelijat näkevät **konkreettisesti**, kuinka pyyntöjen laatu vaikuttaa tulokseen.

---

## Tehtävä 2: Testaamisen tärkeys — virheitä etsimässä

**Aika:** 25 min

1. Anna opiskelijoille seuraava koodi (väärä):
   ```python
   def count_vowels(text):
       vowels = "aeiouAEIOU"
       count = 0
       for char in text:
           if char in vowels:
               count += 1
       return count
   ```

2. Pyydi, että he ajavat sen näillä testisyötteillä ja dokumentoivat tulokset:
   - `count_vowels("hello")` — odotus: 2
   - `count_vowels("AEIOu")` — odotus: 5
   - `count_vowels("")` — odotus: 0
   - `count_vowels("xyz")` — odotus: 0
   - `count_vowels("aaa")` — odotus: 3

3. Kaikki testit menevät läpi! Koodi näyttää toimivan.

4. Nyt anna lisätestitapaus:
   - `count_vowels("Å on vokaali?")` — mitä saa?
   
   Koodi antaa väärän tuloksen, koska scandinavian "Å" ei ole listassa!

5. Keskustelu:
   - Miksi ensimmäiset testit menivät läpi?
   - Miksi neljäs testaus paljasti ongelman?
   - Mitä neljännen tapauksen koodi olisi pitänyt tarkistaa?

**Tekniikka:** Näytetään, että testit ovat kriittisiä ja reunatapaukset paljastuvat vasta, kun niille ajattelee.

---

## Tehtävä 3: Dokumentointi — prosessi näkyviin

**Aika:** 15 min

Näytä opiskelijoille hyvä dokumentaatio:

```
KOODIN TUOTTAMINEN — DOKUMENTAATIO

Tehtävä: Funktio, joka laskee listan keskiarvon

Pyyntö (versio 1):
"Kirjoita funktio, joka laskee listan keskiarvon"

Saatu koodi (versio 1):
def average(numbers):
    return sum(numbers) / len(numbers)

Testaus:
- average([1, 2, 3]) → 2.0 ✓
- average([]) → VIRHE: ZeroDivisionError ✗

Ongelma: Ei käsittele tyhjää listaa

Pyyntö (versio 2):
"Muokkaa funktiota. Jos lista on tyhjä, palauta 0."

Saatu koodi (versio 2):
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

Uudelleen testaus:
- average([]) → 0 ✓
- average([1, 2, 3]) → 2.0 ✓

Lopullinen koodi: OK
```

Selitä opiskelijoille:
- Dokumentaatio näyttää **prosessin**
- Se näyttää **iteraation** (versio 1 → versio 2)
- Se näyttää **testauksen**
- Se näyttää **ongelmat ja korjaukset**

**Tekniikka:** Osoita, miten dokumentoida hyvin tehtävä 1 ja 2 varten.
