# AI työparina — dokumentointi, lokit ja komentorivi

## Johdanto: AI ei ole vain koodaajien apulainen

Monella opiskelijalla on yhä käsitys, että tekoäly on työkalu "ohjelmoijille" — se auttaa kirjoittamaan Python-koodia tai korjaamaan virheitä. Todellisuudessa tekoäly on hyödyllinen lähes jokaisessa IT-tehtävässä. Se voi auttaa dokumentaation kirjoittamisessa, lokien tulkinnassa, komentorivin komentojen oppimisessa ja tikettien kirjoittamisessa. Jos haluat työskennellä IT-alalla — koodarina, järjestelmänvalvojana, IT-tukihenkilönä tai tietoturvassa — tämä koskee sinua.

Ammattilaiselle dokumentaatio on yhtä tärkeää kuin koodi. README-tiedosto, josta uudet tiimiläiset saavat selkeät ohjeet, asennusohje, jota asiakkaat voivat seurata, ja tiketti, joka kuvaa ongelman selkeästi — nämä ovat ammattilaisuuden merkkejä. CLI-komennot ja lokit voivat tuntua mysteerisiltä, mutta kun osaat käyttää AI:ta apuna, ne muuttuvat hallittaviksi.

Tämä on viimeinen askel kohti omaa Custom-GPT:täsi: kun olet oppinut kaikki nämä taidot, voit rakentaa botin, joka on sinun täydellinen digitaalinen työparina IT-tehtävissä.

## Dokumentaation kirjoittaminen AI:n avulla

Dokumentaatio on kaikille tärkeää, mutta monet välttelevät sen kirjoittamista. "Se on tylsää", "En tiedä, mistä aloittaa", "Minulla ei ole aikaa". Sitten pari kuukautta myöhemmin uusi tiimiläinen tulee ja kysyy: "Kuinka tämä asennetaan? Mitä riippuvuuksia se tarvitsee? Miten sitä käytetään?" Eikä dokumentaatiota ole.

AI voi auttaa tässä merkittävästi. Se ei kirjoita täydellistä dokumentaatiota, mutta se antaa pohjan, jonka voit muokata ja parantaa.

**README-tiedostot** ovat kriittisiä. Uusien tiimiläisten ensimmäinen paikka on GitHub-sivu, ja ensimmäinen asia, jota he etsivät, on README. Siinä pitäisi olla:
- Mitä tämä projekti tekee?
- Miten se asennetaan?
- Miten sitä käytetään?
- Miten se testataan?
- Miten siihen kontribuoidaan?

Voit pyytää AI:ta: "Luo README-pohja Node.js-projektille, joka on REST API. Sisällytä osat: Kuvaus, Asennus (npm install), Käyttö (npm start), Testit (npm test) ja Kontribuointi. Jokainen osio 3–5 lausetta."

AI antaa sinulle pohjan, jonka voit sitten muokata projektiin sopivaksi.

**Asennusohjeet** ovat toinen kriittinen osa. Erityisesti silloin, jos asiakkaat tai muut tiimiläiset käyttävät projektia, heidän täytyy pystyä asentamaan se. Voit pyytää AI:ta: "Luo asennusohje Ubuntu 22.04:lle PostgreSQL-tietokantaa käyttävälle Python-sovellukselle. Sisällytä: riippuvuuksien asennus, tietokannan konfigurointi, sovelluksen käynnistys. Jokainen vaihe on yksi tai kaksi komentoa."

> **Pysähdy hetkeksi:** Ajattele projektia, johon osallistuit. Oliko dokumentaatio hyvää? Mitä dokumentaatiosta puuttui? Mikä olisi auttanut?

**Tikettien kirjoittaminen** on myös tärkeää. Kun raportoit virheen tai ehdotat uutta ominaisuutta, täytyy kirjoittaa selkeä tiketti. Voit pyytää AI:ta auttamaan:

"Tarvitsemme uuden ominaisuuden: käyttäjä voi eksportoida tiedot CSV:ksi. Kirjoita GitHub Issue -pohja, jossa on osat: Kuvaus, Kohderyhmä (kuka tarvitsee), Hyväksymiskriteerit (mitä testataan) ja Tekniset tiedot."

AI antaa strukturoidun pohjan, jonka voit täyttää.

## Lokien tulkinta ja vianseuranta

Lokit voivat näyttää mysteerisiltä: rivejä tekstiä, aikoja, virhekoodeja. Mutta lokit kertovat tarkalleen, mitä järjestelmä tekee. Ammattilaiselle lokianalyysissa on kolme vaihetta:

1. **Löydä virhe tai merkintä:** etsi ERROR- tai CRITICAL-rivit.
2. **Ymmärrä ajoitus:** katso, milloin virhe tapahtui ja mitä tapahtui sen ympärillä.
3. **Seuraa syytä:** lue lokia kuin tarinaa — mikä tapahtui ensin, mitä sen jälkeen?

Voit pyytää AI:ta: "Analysoi tämän sovelluksen lokit viimeiseltä tunnilta. Etsi ERROR- tai WARNING-rivit. Kerro: mitä virheitä on, kuinka monta ja mitkä ovat säännöllisiä?"

AI voi lukea 1000 riviä lokia ja kertoa sinulle tärkeimmät osat.

**Vianseuranta (debugging)** on seuraava taso. Jos lokeissa näkyy virhe, mutta et ymmärrä, miksi se tapahtuu, voit antaa AI:lle lokin ja koodin yhdessä:

"Tässä on loki, jossa käyttäjä ei voi kirjautua. Tässä on login-funktion koodi. Koodin mukaan pitäisi tarkistaa salasana ja vertailla hashia. Lokin mukaan se ei koskaan pääse vertailuun — miksi?"

AI voi tutkia sekä lokia että koodia ja sanoa: "Näen, että hash-funktio heittää exceptionin ennen vertailua — virhe on rivillä 45."

> **Pysähdy hetkeksi:** Kun olet havainnut, että ohjelma ei toimi, mitkä ovat ensimmäiset asiat, joihin katsot? Lokit? Koodi? Näyttö?

## CLI-komennot ja turvallinen generointi

Komentorivikomennot (CLI-komennot) voivat tuntua pelottavilta. Tuhansia komentoja, outoja vipuja, kuten `-r` ja `--recursive`. Monet opiskelijat pelkäävät tehdä virheen ja rikkoa kaiken.

Tämä on järkevää varovaisuutta. Jotkut komennot voivat poistaa tiedostoja tai muuttaa järjestelmää pysyvästi. Mutta pelko ei ole hyvä neuvonantaja.

**Turvallisuus ensin:** Kun AI:ta pyydetään generoimaan komentoja, sinun täytyy ymmärtää ne ennen kuin ajat niitä. Et koskaan kopioi ja liitä komentoa suoraan.

Hyvä prosessi:
1. Pyydä AI:ta: "Kirjoita komento, joka poistaa tiedostot, joiden nimi alkaa 'temp_' nykyisestä hakemistosta."
2. AI antaa: `find . -name "temp_*" -type f -delete`
3. **Sinä kysyt:**
   - Mitä `find` tekee? (etsii tiedostoja)
   - Mitä `-name "temp_*"` tarkoittaa? (nimi alkaa temp_)
   - Mitä `-type f` tarkoittaa? (vain tiedostot, ei hakemistoja)
   - Mitä `-delete` tekee? (poistaa ne!)
4. Sinä ajat komennon **turvallisesti:** ensin `find` ilman `-delete`-valintaa nähdäksesi, mitä se löytää, sitten testaat poistamista.

Ammattilaisena et koskaan kopioi komentoja sokeasti. Sinä:
- ymmärrät, mitä komento tekee
- luot testiskenaarion ensin
- ajat sen turvallisesti (esikatselu ensin, sitten oikea toiminto)

AI voi auttaa **shell-skriptien** kirjoittamisessa. Jos sinulla on sarja komentoja, joita joudut ajamaan usein, voit pyytää AI:ta:

"Kirjoita shell-skripti, joka:
1. Varmuuskopioi kaikki .txt-tiedostot hakemistoon 'backups/'
2. Kirjaa varmuuskopioinnin ajan tiedostoon 'backup.log'
3. Poistaa yli 30 päivää vanhat varmuuskopiot
Skripti saa kutsua: `./backup.sh`"

AI antaa sinulle pohjan. Sinä testaat sitä, muokkaat sitä ja hyväksyt sen.

## Yhteenveto: AI on koko IT-urasi ajan yksi työkalu

Ammattilaisena — riippumatta siitä, minkä IT-alan valitset — käytät AI:ta koko urasi ajan. Se ei ole vain koodaajille. Se on tukenasi, kun kirjoitat dokumentaatiota, analysoit lokeja, opettelet uuden komentorivikomennon tai ratkaiset ongelmaa.

Avain on **ymmärrys ja kriittinen ajattelu**. AI antaa ehdotuksia — koodia, komentoja ja dokumentaatiota — mutta sinä validoit ja hyväksyt ne. Ammattilaisena olet vastuussa.

Neljä tärkeintä asiaa:

1. **Dokumentaatio** on ammattilaisuutta. AI voi auttaa, mutta sinä olet vastuussa siitä, että se on oikea ja ajantasainen.

2. **Lokit** ovat paras ystäväsi. Kun jokin menee pieleen, lokit kertovat, mitä tapahtui. AI voi auttaa lukemaan niitä.

3. **CLI-komennot** eivät ole pelottavia, jos ymmärrät ne ensin. Turvallisuus ensin, sitten toiminta.

4. **AI on apulainen, ei johtaja.** Sinä päätät, mitä tehdä. AI antaa ehdotuksia.

Tämä on ammattilaisuutta.

Olet nyt valmis: 15 oppitunnin, niiden teorioiden ja käytäntöjen kautta olet oppinut, mitä tekoäly on, mitä se tekee hyvin, mitä se tekee huonosti, ja kuinka käyttää sitä ammatillisesti ja vastuullisesti. Nyt voit rakentaa omasi Custom-GPT:n — digitaalisen työparisi, joka kuuntelee sinua ja auttaa sinua IT-projekteissasi.