# Näytä kuva, saat vastauksen — visuaalinen debuggaus

## Johdanto: Näytä, älä kerro

Olet kokeillut uutta komentoriviä ja saat virheilmoituksen. Kirjoitat seuraavaksi ystävällesi: "Sain virheellisen paluuarvon satunnaisesti, ja se näyttää liittyvän tietokantaan. Voisiko sinulla olla idea?" Ystävä vastaa: "Hmm, en tiedä." Sitten otat kuvakaappauksen virheilmoituksesta, lokeista ja komennosta ja lähetät kuvan. Ystävä vastaa 10 sekunnissa: "Ah! Näen ongelman — portti 5432 ei ole auki."

Tämä on ero tekstin ja **kontekstin** välillä. Teksti on epämääräistä. Kuvakaappaus, koodi ja loki yhdessä kertovat täydellisen tarinan.

Kun käytät tekoälyä ongelmanratkaisuun, sama logiikka pätee. AI voi tulkita ongelmaa tekstin perusteella, mutta se tarvitsee **näyttöä**. Näyttö voi olla kuvakaappaus virheilmoituksesta, koodi, tiedoston sisältö, komennon tuloste tai lokimerkintöjä. Ammattilaisena sinun täytyy oppia tuomaan nämä näytöt AI:lle.

Tämä taito vie sinua lähemmäs omaa Custom-GPT:täsi: kun opit käyttämään kuvia ja multimodaalisia tietoja kontekstina, voit rakentaa botin, joka osaa analysoida ongelmia kokonaisvaltaisesti.

## Mikä on multimodaalinen ongelmanratkaisu

**Multimodaalinen** tarkoittaa, että käytät useita "moodeja" — tekstiä, kuvia, koodia ja lokeja. Perinteisessä ohjelmointityössä, kun jokin menee pieleen, otat kuvakaappauksen, tulostat lokit tai avaat debuggerin. Nyt voit ottaa nämä samat työkalut ja näyttää ne AI:lle.

Multimodaalinen ongelmanratkaisu on erityisen tehokasta, koska:

1. **Konteksti on täydellinen:** Kuvakaappaus virheilmoituksesta on paljon tarkempi kuin "sain jonkin virheen".
2. **AI näkee täsmälleen sen, mitä sinä näet:** Kun näytät virheilmoituksen, AI näkee saman koodin, saman debuggerin ja saman terminaalin värit — kaikki vihjeet, jotka ihminenkin näkee.
3. **Nopeus:** Sen sijaan, että selittäisit ongelmaa sanoin, kuvakaappaus voi ratkaista sen sekunneissa.
4. **Automatisoitavuus:** Kun dokumentoit ongelmia kuvakaappausten avulla, sinulla on arkisto ratkaisuista myöhempää käyttöä varten.

> **Pysähdy hetkeksi:** Ajattele viimeisintä teknistä ongelmaa, joka sinulla oli. Kuvailisitko sitä sanoin vai ottaisitko kuvakaappauksen? Kumpi olisi nopeampi tapa selittää?

## Kuvakaappaukset: virheilmoituksista käyttöliittymään

Kuvakaappaus (screenshot) on yksinkertaisin tapa. Kun saat virheilmoituksen, otat kuvakaappauksen. Kun näytöllä on outoa käyttäytymistä, otat kuvakaappauksen. Kun näytössä on asetusikkuna, jota et ymmärrä, otat kuvakaappauksen.

Hyvä kuvakaappaus sisältää:
- **Kontekstin:** Mikä ohjelma on kyseessä? Missä vaiheessa olit?
- **Virheilmoituksen tai outouden:** Mitä näet?
- **Tarpeeksi tietoa ratkaisuun:** Ei vain ikoneita, vaan myös tekstit, numerot ja kohtien nimet.

Esimerkiksi: "Sain virheen, kun yritin kirjautua salasanallani" on epämääräinen. Kuvakaappaus kirjautumisikkunasta, virheilmoituksesta ja mahdollisesta virhekoodista on täsmällinen.

Kun annat kuvakaappauksen AI:lle, kerro sille lyhyesti, mitä näet:

"Tässä on kuvakaappaus. Sain tämän virheilmoituksen yrittäessäni ajaa 'npm install' -komentoa projektissa, joka käyttää Node.js 18:aa. Tunnus on 'ERR! 404 Not Found'. Voiko tämä johtua väärästä paketista?"

Nyt AI:lla on:
- Kuva (visuaalinen konteksti)
- Selitys (mitä yritit tehdä)
- Konteksti (Node 18, npm install)
- Kysymys (onko paketti väärä?)

## Lokidata ja konsolilähdöt

Lokit (logs) ovat tietue kaikesta, mitä järjestelmä tekee. Kun ohjelmassa on virhe, lokit kertovat, mikä meni pieleen ja milloin.

Monesti opiskelijat sanovat: "Minulla on virhe, mutta en tiedä, mikä se on." Ensimmäinen asia, jota ammattilainen kysyy, on: "Mitä lokit sanovat?" Tämä johtuu siitä, että lokit ovat usein ihmisen luettavissa:

```
2024-03-14 10:23:45 ERROR: Failed to connect to database at localhost:5432
2024-03-14 10:23:45 ERROR: Connection timeout after 5 seconds
2024-03-14 10:23:46 WARNING: Retrying connection attempt 2 of 3
```

Kun annat lokit AI:lle, se voi lukea rivit ja sanoa: "Näen, että tietokanta ei ole saatavilla — portti 5432 ei vastaa."

Lokit voivat tulla useista lähteistä:
- **Sovelluksen lokit:** mitä koodisi tekee
- **Järjestelmän lokit:** mitä käyttöjärjestelmä tekee
- **Verkkolokit:** mitä palvelin tekee
- **Virhelokit (stderr):** mitä ohjelma sanoo virheen yhteydessä

Kun käytät AI:ta, kopioi relevantti osio lokista ja kerro konteksti:

"Tässä on sovelluksen lokin viimeiset 20 riviä. Ohjelma kaatui kohdassa 10:45. Näetkö syyn?"

AI voi sitten etsiä virheilmoituksia, tutkia ajoitusta ja ehdottaa ratkaisuja.

> **Pysähdy hetkeksi:** Missä sovelluksessa tai järjestelmässä olet nähnyt lokeja? Mitä sellaista lokeista voidaan oppia, mitä et näkisi muuten?

## Koodi ja konfiguraatiotiedostot

Monesti ongelma on itse koodissa. Ehkä skripti ei toimi, konfiguraatiotiedosto on väärä tai Python-funktio tekee outoja asioita.

Kun annat AI:lle koodia, se voi analysoida sen:

```python
def calculate_discount(price, discount_percent):
    return price - (price * discount_percent)
```

"Näetkö tässä ongelmaa? Kun discount_percent on 0.1 (10 %), tulos on oikea. Mutta kun se on 1 (100 %), hinta muuttuu negatiiviseksi. Pitäisikö lisätä tarkistus?"

Konfiguraatiotiedostot voivat myös aiheuttaa ongelmia:

```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "user": "admin",
    "password": "admin123"
  }
}
```

"Tässä on konfiguraatiotiedosto. Näetkö siinä turvallisuusongelman? Salasana on kovakoodattu."

Kun annat koodia, on kolme tärkeää asiaa:

1. **Konteksti:** Mikä ohjelma on kyseessä? Mikä ohjelmointikieli?
2. **Vika-alue:** Mitkä rivit ovat ongelmallisia?
3. **Käyttäytyminen:** Mitä haluat tapahtuvan? Mitä todellisuudessa tapahtuu?

## Yhdistäminen: teksti + kuva + koodi + lokit

Ammattilaiselle paras ongelmanratkaisu yhdistää kaikki nämä:

"Tässä on kuvakaappaus virheilmoituksesta. Tässä ovat lokin viimeiset 20 riviä. Ja tässä on koodin vika-alue (rivit 45–55). Yritin päivittää käyttäjän profiilin, mutta validointi epäonnistuu. Kunkin kentän pitäisi hyväksyä vain tietyntyyppistä dataa, mutta validointi epäonnistuu myös oikealla datalla."

Nyt AI:lla on:
- Visuaalinen konteksti (kuvakaappaus)
- Ajoituksen ja ympäristön konteksti (lokit)
- Koodin konteksti (vika-alue)
- Käyttäytymisen konteksti (mitä haluat, mitä tapahtuu)

Tämä on paljon parempi kuin "Minulla on validointivirhe."

## Turvallisuus: Mitä ei saa näyttää

Tärkeä huomio: **älä koskaan näytä salasanoja, API-avaimia tai muita salaisuuksia** AI:lle. Jos kuvakaappaus tai lokit sisältävät näitä, poista ne ennen jakamista:

- Salasanakenttä: Näytä `[REDACTED]` tai `***`
- API-avain: Näytä `sk-***...xyz`
- Tunnus: Näytä `jti_12345...abcdef`

Jos lokit sisältävät käyttäjätietoja tai asiakkaita koskevia tietoja, poista ne tai anonymisoi ne.

Tämä suojaa sekä sinua että muita. Turvallisuus ei ole valinnaista — se on ammattilaiselle pakollista.

> **Pysähdy hetkeksi:** Ajattele IT-järjestelmää, jossa käyttäjät voivat nähdä toistensa tietoja. Mitä turvallisuusriskejä olisi, jos jakaisit lokit AI:lle muokkaamatta niitä?

## Yhteenveto

Ammattilaisena et ratkaise ongelmia pelkillä sanoilla. Otat kuvakaappauksia, keräät lokeja, etsit koodia ja yhdistät ne. AI on tehokkaimmillaan, kun se näkee täsmälleen sen, mitä sinä näet. Multimodaalinen ongelmanratkaisu — teksti, kuva, koodi ja lokit — on sekä nopeampaa että tarkempaa kuin pelkkä teksti.

Kun seuraavalla kerralla sinulla on tekninen ongelma, älä vain kuvaile sitä. Näytä se. Kuvakaappaus, loki, koodi, konfiguraatio — mitä enemmän näyttöä, sitä paremman ratkaisun saat.

Viimeisellä tunnilla yhdistät kaiken: dokumentaatio, lokit, komentorivin käskyt — tekoäly työparina.