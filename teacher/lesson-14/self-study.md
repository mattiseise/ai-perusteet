# Kuvakaappaukset ja multimodaalinen ongelmanratkaisu

## Johdanto: Näytä, älä kerro

Olet kokeilut uutta komentoriviä ja saat virheilmoituksen. Kirjoitat seuraavaksi ystävällesi: "Sain virheellisen paluuarvon satunnaisesti, ja se näyttää liittyvän tietokantaan. Voisiko sinulla olla idea?" Ystävä vastaa: "Hmm, ei tietoa." Sitten otat kuvakaappauksen virheilmoituksesta, lokeista ja komennosta, lähettää kuvan. Ystävä vastaa 10 sekunnissa: "Ah! Näen ongelman — portin 5432 ei ole auki."

Tämä on ero tekstin ja **kontekstin** välillä. Teksti on epämääräinen. Kuvakaappaus, koodi ja loki yhdessä kertovat täydellisen tarinan.

Kun käytät tekoälyä ongelmanratkaisuun, sama logiikka pätee. AI voi kuvata ongelmaa tekstissä, mutta se tarvitsee **näyttöä**. Näyttö voi olla kuvakaappaus virheilmoituksesta, koodi, tiedoston sisältö, komennon tuloste tai loki-merkinnät. Ammattilaisena sinun täytyy oppia tuomaan nämä näytöt AI:lle.

## Mikä on multimodaalinen ongelmanratkaisu

**Multimodaalinen** tarkoittaa, että käytät useita "moodeja" — tekstiä, kuvia, koodia, lokit. Perinteisen ohjelmoinnissa, kun jokin menee pieleen, otat kuvakaappauksen, tulostat lokit tai avaat debuggerin. Nyt voit ottaa nämä samat työkalut ja antaa ne AI:lle.

Multimodaalinen ongelmanratkaisu on erityisen tehokas, koska:

1. **Konteksti on täydellinen:** Kuvakaappaus virheilmoituksesta on paljon tarkempi kuin "sain jonkin virheen".
2. **AI näkee täsmälleen mitä sinä näet:** Kun näytät virheilmoituksen, AI näkee saman koodin, saman debuggerin, saman terminal-värin — kaikki vihjeet, jotka ihminen näkee.
3. **Nopeus:** Sen sijaan että selittäisit ongelmaa sanoja, kuvakaappaus ratkaisee sen sekunneissa.
4. **Automatisoitavissa:** Kun dokumentoit ongelmia kuvakaappausten kanssa, sinulla on arkisto ratkaisuista myöhempää käyttöä varten.

> **Pysähdy hetkeksi:** Ajattele viimeistä tekniikan ongelmaa, joka sinulla oli. Kuvailisit sitä sanoin vai otat kuvakaappauksen? Mikä olisi nopeampaa selittää?

## Kuvakaappaukset: Virheilmoituksista käyttöliittymään

Kuvakaappaus (screenshot) on yksinkertaisin tapa. Kun saat virheilmoituksen, otat kuvakaappauksen. Kun näytöllä on outoa käyttäytymistä, otat kuvakaappauksen. Kun näytetään asetusikkuna, jota et ymmärrä, otat kuvakaappauksen.

Hyvä kuvakaappaus sisältää:
- **Kontekstin:** Mitä ohjelmaa? Mitä vaiheessa olit?
- **Virheilmoituksen tai outouden:** Mitä näet?
- **Tarpeeksi tietoa ratkaisuun:** Ei vain ikonit, vaan tekstit, numerot, kohtien nimet.

Esimerkiksi: "Sain virheen, kun yritin kirjautua salasanastamme" on epämääräinen. Kuvakaappaus kirjautumisikkunasta, virheilmoituksesta ja mahdollisesta error-koodista on täsmällinen.

Kun annät kuvakaappauksen AI:lle, kerro sille lyhyesti, mitä näet:

"Tässä on kuvakaappaus. Sain tämän virheilmoituksen yritessä ajaa 'npm install' projektissa, joka käyttää Node.js 18. Tunnus on 'ERR! 404 Not Found'. Voiko tämä johtua väärästä paketista?"

Nyt AI:lla on:
- Kuva (visuaalinen konteksti)
- Selitys (mitä yritit tehdä)
- Konteksti (Node 18, npm install)
- Kysymys (onko paketti väärä?)

## Loki-data ja konsolilähdöt

Lokit (logs) ovat tietokantaa varten kaikesta, mitä järjestelmä tekee. Kun ohjelmassa on virhe, lokit kertovat mikä meni pieleen ja milloin.

Monesti opiskelijat sanovat: "Minulla on virhe, mutta en tiedä mitä se on." Ensimmäinen asia, joka ammattilaiselta kysytään: "Mitä lokit sanovat?" Koska lokit ovat usein ihmisen luettavia:

```
2024-03-14 10:23:45 ERROR: Failed to connect to database at localhost:5432
2024-03-14 10:23:45 ERROR: Connection timeout after 5 seconds
2024-03-14 10:23:46 WARNING: Retrying connection attempt 2 of 3
```

Kun annat lokit AI:lle, se voi lukea rivit ja sanoa: "Näen, että tietokanta ei ole käytettävissä — portti 5432 ei vastaa."

Lokit voivat tulla useista lähteistä:
- **Sovelluksen lokit:** Mitä koodisi sanoo
- **Järjestelmän lokit:** Mitä käyttöjärjestelmä sanoo
- **Verkko-lokit:** Mitä palvelin sanoo
- **Virhelokit (stderr):** Mitä ohjelma sanoi virheen yhteydessä

Kun käytät AI:ta, kopioi relevantti osio logista ja kerro konteksti:

"Tässä on sovelluksen lokin viimeinen 20 riviä. Ohjelma kaatui 10:45 kohdalla. Näetkö syyn?"

AI voi sitten etsiä virheilmoituksia, tutkia ajoitusta ja ehdottaa ratkaisuja.

> **Pysähdy hetkeksi:** Missä sovelluksessa tai järjestelmässä olet nähnyt lokeja? Mitä lokeista voidaan oppia, jota et näkisi muuten?

## Koodi ja konfiguraatiotiedostot

Monesti ongelma on koodi itsessään. Ehkä skripti ei toimi, tai konfiguraatiotiedosto on väärä, tai Python-funktio tekee outoja asioita.

Kun annat AI:lle koodia, se voi analysoida sen:

```python
def calculate_discount(price, discount_percent):
    return price - (price * discount_percent)
```

"Näkikö sinä ongelmaa? Kun discount_percent on 0.1 (10%), tulos on oikea. Mutta kun se on 1 (100%), hinta muuttuu negatiiviseksi. Pitäisikö lisätä tarkistus?"

Konfiguraatiotiedostot voivat olla myös ongelmallisia:

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

"Tässä on Dockerfilen konfiguraatio. Näkikö sinä turvallisuusongelmaa? Salasana on hardkoodattu."

Kun annat koodia, on kolme tärkeää asiaa:

1. **Konteksti:** Mitä ohjelmaa? Mitä ohjelmointikieltä?
2. **Vika-alue:** Mitkä rivit ovat ongelmaallisia?
3. **Käyttäytyminen:** Mitä haluaa tapahtua? Mitä todellisuudessa tapahtuu?

## Yhdistäminen: Teksti + kuva + koodi + lokit

Ammattilaisesti paras ongelmanratkaisu yhdistää kaikki näistä:

"Tässä on kuvakaappaus virheilmoituksesta. Tässä on lokeista viimeinen 20 riviä. Ja tässä on koodin vika-alue (rivit 45-55). Yritin päivittää käyttäjän profiilin, mutta validointi epäonnistuu. Kunkin kentän pitäisi hyväksyä vain tietyntyyppisellä dataa, mutta se epäonnistuu myös oikealla datalla."

Nyt AI:lla on:
- Visuaalinen konteksti (kuvakaappaus)
- Ajoituksen ja ympäristön konteksti (lokit)
- Koodin konteksti (vika-alue)
- Käyttäytymisen konteksti (mitä haluaa, mitä tapahtuu)

Tämä on paljon parempi kuin "Minulla on validointivirhe."

## Turvallisuus: Mitä ei saa näyttää

Tärkeä huomio: **älä koskaan näytä salasanoja, API-avaimia tai muita salaisuuksia** AI:lle. Jos kuvakaappaus tai lokit sisältävät näitä, muokkaa ne pois:

- Salasanakenttä: Näytä `[REDACTED]` tai `***`
- API-avain: Näytä `sk-***...xyz`
- Tunnus: Näytä `jti_12345...abcdef`

Jos lokit sisältävät käyttäjätietoja tai asiakkaita koskevia tietoja, poista ne tai anonymisoi.

Tämä suojaa sekä sinua että muita. Turvallisuus ei ole valinnaista — se on ammattilaisesti pakollista.

> **Pysähdy hetkeksi:** Ajattele IT-järjestelmää, jossa käyttäjät voivat nähdä toisiensa tietoja. Mitä turvallisuusriskejä olisi, jos jakaisi lokit AI:lle muokkaamatta?

## Yhteenveto

Ammattilaisena et ratkaise ongelmia pelkillä sanoilla. Otat kuvakaappauksia, keräät lokeja, etsit koodia ja yhdistät ne. AI on tehokkain, kun se näkee täsmälleen mitä sinä näet. Multimodaalinen ongelmanratkaisu — teksti, kuva, koodi, lokit — on sekä nopeampaa että tarkempaa kuin puhdas teksti.

Kun seuraavalla kerralla sinulla on tekninen ongelma, älä vain kuvaile sitä. Näytä se. Kuvakaappaus, loki, koodi, konfiguraatio — mitä enemmän näyttöä, sitä parempi ratkaisu saat.
