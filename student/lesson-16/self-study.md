# AI-avusteinen ohjelmointi I: koodin tuottaminen

## Johdanto

Olet kirjoittamassa pieniä Python-skriptejä kotitehtävää varten. Tavallisesti pysähtyt ja etsit dokumentaatiosta, kuinka tehdä jotain: "Kuinka luen CSV-tiedostoa?", "Kuinka silmukkaan listan jokaiselle riville?". Tämä vie aikaa. Nyt avaat ChatGPT:n ja kirjoitat: "Kirjoita Python-skripti, joka lukee CSV-tiedoston, käy riveillä läpi ja tulostaa jokaisen rivin kolmospalstan." Sekunnissa saat valmiin koodin. Kopioit, testat — toimii. Hetki sitten olisit käyttänyt 10 minuuttia dokumentaation etsimiseen.

Tässä oppitunnissa opit, miten käyttää tekoälyä koodin tuottamiseen. GitHub Copilot tekee sitä suoraan editoriissa — se ehdottaa koodia samalla kun kirjoitat. Chat-pohjaiset assistentit (ChatGPT, Claude) antavat sinulle kokonaisia funktioita. Näiden työkalujen käyttö on kuitenkin taito — sinun pitää osata pyytää hyvin. Lisäksi tekoäly tuottaa koodia, joka näyttää hyvältä, mutta ei välttämättä toimi — sinun pitää testata ja tarkistaa.

## GitHub Copilot ja inline-koodin ehdottaminen

GitHub Copilot on laajennus, joka toimii suoraan koodieditorissasi (VS Code, JetBrains, jne.). Se näkee koodia, jota olet kirjoittamassa, ja ehdottaa seuraavaa riviä tai funktiota.

Toimii näin: Kirjoitat kommenttia:

```python
# Lue tiedosto, joka sisältää nimet ja ikät
```

Copilot näkee kommentin ja ehdottaa:

```python
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        name, age = line.strip().split(',')
        print(f"{name} is {age} years old")
```

Jos ehdotus näyttää hyvältä, hyväksyt sen (Tab). Jos ei, voit pyytää toisenlaista ehdotusta tai kirjoittaa oman.

Copilot opetettiin miliaardeilla riveillä avoimen lähdekoodin koodia GitHubista. Se tuntee monia ohjelmointimalleja ja tyylitapoja. Siksi se on usein varsin hyvä — mutta ei täydellinen.

**Vinkkejä Copilotin käyttöön:**
- Kirjoita selkeä, kuvaava kommentti ennen koodia
- Opettele, mitä painikkeita paina muista ehdotuksista
- Tarkista aina ehdotukset — Copilot tekee virheitä

> **Pysähdy hetkeksi:** Jos et käytä Copilotia vielä, kysy opettajalta, miten se on konfiguroitu. Jos käytät, tuo nyt editorisi auki ja testaa kolmen rivin kommentilla. Mitä Copilot ehdottaa? Onko ehdotus hyvä? Mikä siinä voisi olla väärin?

## Chat-pohjaiset koodiassistentit: ChatGPT, Claude ja muut

Chat-assistentit ovat erilaisia. Ne eivät näe koodiasi real-timella — sen sijaan sinä kopioit koodia heille tai sanot, mitä haluat. Luovat usein kokonaisia funktioita tai skriptejä.

Esimerkiksi voit kirjoittaa ChatGPT:lle:

*"Kirjoita Python-funktio, joka ottaa listan numeroa, poistaa duplikaatit ja palauttaa listan pienimmästä suurimpaan. Käytä set-tietotyyppiä."*

Sekunnissa:

```python
def sort_unique(numbers):
    return sorted(set(numbers))
```

Tai pyynnöstä:

*"Kirjoita Bash-skripti, joka tarkistaa, onko tiedosto olemassa. Jos on, tulosta sen muokkauspäivä. Jos ei, tulosta virheilmoitus."*

```bash
#!/bin/bash
if [ -f "$1" ]; then
    echo "File last modified: $(date -r "$1")"
else
    echo "File not found: $1"
fi
```

**Mitä tekoäly on hyvä tekemään:**
- Kirjoittaa pieniä skriptejä (alle 100 rivi)
- Tuottaa yritys- ja virhekäsittelykoodia
- Muuttaa koodia tai korjaa pieniä bugeja
- Selittää, mitä koodi tekee

**Missä tekoäly epäonnistuu:**
- Ei ymmärrä laajaa kontekstia (jos sinulla on 1000 rivin ohjelmaa, AI näkee ehkä 100)
- Hallusinoi dokumentaatiota ja kirjastomenetelmiä
- Voi tuottaa tietoturvahaavoittuvaa koodia
- Ei automaattisesti testa koodia, jota se kirjoittaa

## Oikeat pyyntöjen tekeminen: tekniikka ja konteksti

Koodin pyytäminen on kuten reseptin antaminen. Jos sanot "tee pasta", saat ehkä mitä tahansa. Jos sanot "Tee täysteini-rigatoni-kastike (ei kermaa, kasvisperustainen) noin 30 minuutissa keittämiseen", saat paljon paremman tuloksen.

**Mitä lisätä pyyntöön:**

1. **Ohjelmointikieli ja versio**
   - "Python 3.10" on parempi kuin "kirjoita koodi"
   - "Bash 5" on parempi kuin "skripti"

2. **Mitä koodin pitäisi tehdä — konkreettisesti**
   - Huono: "Luo funktio, joka käsittelee dataa"
   - Hyvä: "Luo funktio, joka ottaa syötteeksi listan sanojen jonoja (esim. ['cat', 'dog', 'cat']) ja palauttaa sanakirjan, jossa kukin sana ja kuinka monta kertaa se esiintyi"

3. **Mitä syötteet ovat ja mitä palautetaan**
   - "Funktio ottaa syötteeksi merkkijonon ja palauttaa boolean-arvon (True jos on palindromi, False jos ei)"

4. **Miten sitä käytetään?**
   - "Käytetään näin: `result = get_max([3, 7, 1])`"

5. **Onko joitain rajoitteita?**
   - "Älä käytä for-silmukkaa, käytä list comprehensionia"
   - "Ei ulkoisia kirjastoja, vain standardikirjasto"

**Esimerkki hyvästä pyynnöstä:**

*"Kirjoita Python 3.10 -funktio nimeltä filter_words, joka ottaa syötteeksi listan merkkijonoja ja palauttaa uuden listan, jossa on vain sanat, jotka alkavat kirjaimella 'a' (isot ja pienet kirjaimet). Käytä list comprehensionia. Esimerkki: filter_words(['apple', 'banana', 'avocado']) palauttaa ['apple', 'avocado']"*

Tällaisen pyynnön jälkeen tekoäly antaa sinulle täsmälleen mitä haluat, sillä olet kertonut kontekstin.

> **Pysähdy hetkeksi:** Katso yllä oleva "hyvä pyynnön" esimerkki. Miksi se on hyvä? Mitä siinä on, mitä "huonossa" ei ole? Entä jos poistaisit yhden kohdan — missä laatu heikkenisi eniten?

## Koodin testaaminen ja verifiointi: se ei ole automaattisesti oikea

Tämä on kriittistä: **tekoäly tuottaa koodia, mutta se ei ole automaattisesti oikea.**

Tekoäly voi:
- Kirjoittaa syntaksiltaan oikean, mutta logiikallisesti väärän koodin
- Käyttää metodia, joka ei ole olemassa tai on väärän niminen
- Hallusinoida dokumentaatiota ("biblioteekin X metodi Y tekee Z" — ei se tee)
- Ohittaa reunatapauksia (esim. tyhjä lista, negatiivinen luku)

Esimerkki: pyydät ChatGPT:tä:

*"Kirjoita funktio, joka laskee listan keskiarvon"*

AI antaa:

```python
def average(numbers):
    return sum(numbers) / len(numbers)
```

Näyttää oikealta. Mutta entä jos `numbers` on tyhjä lista? Silloin `len(numbers)` on 0, ja koodi kaatuu nolla-jaon virheeseen. **Sinun pitää testata sitä:**

```python
print(average([1, 2, 3]))  # Odotus: 2.0
print(average([]))         # Odotus: ?
```

Toinen esimerkki:

```python
def remove_duplicates(items):
    return list(set(items))
```

Näyttää hyvin. Toimii myös. Mutta jos `items` on lista sanakirjoja, sanakirjoja ei voi lisätä `set`:iin, koska sanakirjat eivät ole hashattavia. Koodi kaatuu.

**Verifiointi-prosessi:**
1. Kopioi koodi
2. Aja se paikallisesti omalla koneellasi tai testialustalla
3. Testaa sekä normaalilla että reunatapauksilla
4. Lue koodi — näkeekö virheita silmällä?
5. Jos ei toimi, muokkaa tai kysy AI:lta uudelleen

## Koodin selittäminen ja omaksuminen

Kun saat tekoälyn koodin, sinun pitää ymmärtää se. Et voi vain kopioida ja lähettää opettajalle (ja opettaja osaa katsoa koodia ja huomata, ettet kirjoittanut sitä).

**Miten oppia koodista:**

1. **Lue rivi kerrallaan.** Mitä kukin rivi tekee?
2. **Kysy "miksi".** "Miksi käytetään map() täällä? Mikä olisi tapahtunut for-silmukalle?"
3. **Muokkaa ja testaa.** Muuta jokin muuttuja tai logiikka ja katso, mitä tapahtuu.
4. **Kirjoita kommentit.** Selitä koodin logiikka omalla tavallasi.
5. **Opeta toiselle.** Voisitko selittää sen kaverilleen niin, että hän ymmärtää?

Näin et vain kopioitu koodia — olet oppinut siitä.

## Yhteenveto

Tekoäly on tehokas työkalu koodin tuottamiseen. GitHub Copilot ehdottaa koodia editoriissa, ja chat-assistentit antavat sinulle kokonaisia funktioita sekuntien sisällä. Avain on oppia pyytämään hyvin: määritä kieli, versio, mitä koodi tekee, kuinka sitä käytetään ja mitä rajoitteita on. Muista, että AI:n koodi ei ole koskaan automaattisesti valmis — testaa, varmista ja ymmärrä koodi ennen käyttöä. Koodin omaksuminen on yhtä tärkeää kuin sen tuottaminen.
