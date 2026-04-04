# AI dokumentoinnissa, lokien tulkinnassa ja CLI-työssä

## Johdanto: AI ei ole vain koodaajien apulainen

Monella opiskelijalla on vielä käsitys, että tekoäly on työkalu "ohjelmoijille" — se auttaa kirjoittamaan Python-koodia tai korjaamaan bugeja. Todellisuudessa tekoäly on hyödyllinen lähes jokaisessa IT-tehtävässä. Se voi auttaa dokumentaation kirjoittamisessa, lokeista ymmärtämisessä, komentorivin komennoista oppimisessa ja tikettien kirjoittamisessa. Jos haluat työskennellä IT-alalla — koodarina, järjestelmänvalvojana, IT-tukihenkilönä, tietoturvassa — tämä on sinulle.

Ammattilaisesti dokumentaatio on yhtä tärkeää kuin koodi. README-tiedosto, josta uusille tiimiläisille selvät ohjeet, asennusohje, jota asiakkaat voivat seurata, tiketti, joka selvästi kuvaa ongelman — nämä ovat ammattilaisuuden merkkejä. CLI-komennot ja lokit voivat tuntua mysteerisiltä, mutta kun osaat käyttää AI:ta auttamaan, ne muuttuvat hallittaviksi.

## Dokumentaation kirjoittaminen AI:n avulla

Dokumentaatio on kaikille tärkeää, mutta monet välttävät sen kirjoittamista. "Se on tylsää", "En tiedä mistä aloittaa", "Minulla ei ole aikaa". Sitten pari kuukautta myöhemmin uusi tiimiläinen tulee ja kysyy: "Kuinka tämä asennetaan? Mitä riippuvuuksia se tarvitsee? Miten sen käyttää?" Eikä ole dokumentaatiota.

AI voi auttaa tässä merkittävästi. Se ei kirjoita täydellistä dokumentaatiota, mutta se antaa pohjan, jonka voit muokata ja parantaa.

**README-tiedostot** ovat kriittisiä. Uusien tiimiläisten ensimmäinen rako on GitHub-sivu, ja ensimmäinen asia, jonka he etsivät, on README. Siinä pitäisi olla:
- Mitä tämä projekti tekee?
- Miten se asennetaan?
- Miten sitä käytetään?
- Miten se testataan?
- Miten siihen kontribuoidaan?

Voit pyytää AI:ta: "Luo README-pohja Node.js-projektille, joka on REST API. Sisällytä osat: Kuvaus, Asennus (npm install), Käyttö (npm start), Testit (npm test), ja Kontribuointi. Jokainen osio 3-5 lausetta."

AI antaa sinulle pohjan, jonka voit sitten muokata projektiin sopivaksi.

**Asennusohjeet** ovat toinen kriittinen osa. Erityisesti jos asiakkaat tai muut tiimiläiset käyttävät projektia, heidän täytyy pystyä asentamaan se. Voit pyytää AI:ta: "Luo asennusohje Ubuntu 22.04:lle PostgreSQL-tietokantaa käyttävälle Python-sovellukselle. Sisällytä: riippuvuuksien asennus, tietokannan konfigurointi, sovelluksen käynnistys. Jokainen vaihe on yksi tai kaksi komentoa."

> **Pysähdy hetkeksi:** Ajattele projektia, johon osallistuit. Oliko dokumentaatio hyvää? Mitä dokumentaatiosta puuttui? Mitä olisi auttanut?

**Tikettien kirjoittaminen** on myös tärkeää. Kun raportoit bugin tai asetat uuden ominaisuuden, täytyy kirjoittaa selkeä tiketti. Voit pyytää AI:ta auttamaan:

"Tarvitsemme uuden ominaisuuden: käyttäjä voi eksportoida tiedot CSV:ksi. Kirjoita GitHub Issue -pohja, jossa on osat: Kuvaus, Kohderyhmä (kuka tarvitsee), Hyväksymiskriteerit (mitä testataan), ja Tekniset tiedot."

AI antaa strukturoidun pohjan, jonka voit täyttää.

## Lokien tulkinta ja vianseuranta

Lokit voivat näyttää mysteerisiltä: rivejä tekstiä, aikoja, virhekoodeja. Mutta lokit kertovat tarkalleen mitä järjestelmä tekee. Ammattilaisesti loki-analyysilla on kolme vaihetta:

1. **Löydä virhe tai merkintä:** Etsi ERROR tai CRITICAL -rivit
2. **Ymmärrä ajoitus:** Katso, milloin virhe tapahtui ja mitä tapahtui sen ympärillä
3. **Seuraa syy:** Lue lokit kuten tarinaa — mikä tapahtui ensin, mikä sen jälkeen?

Voit pyytää AI:ta: "Analysoi tämän sovelluksen lokit viimeiseltä tunnilta. Etsi ERROR tai WARNING -rivit. Kerro: mitä virheitä on, kuinka monta, mitkä ovat säännöllisiä?"

AI voi lukea 1000 riviä lokia ja kertoa sinulle tärkeimmät osat.

**Vianseuranta (debugging)** on seuraava taso. Jos lokeissa näkyy virhe, mutta et ymmärrä, miksi se tapahtuu, voit antaa AI:lle lokin ja koodin yhdessä:

"Tässä on logi, jossa käyttäjä ei voi kirjautua. Tässä on login-funktion koodi. Koodin mukaan pitäisi tarkistaa salasana ja vertailla hashia. Lokin mukaan se ei koskaan pääse vertailuun — miksi?"

AI voi tutkia sekä lokin että koodin ja sanoa: "Näen, että hash-funktio heittää exception ennen vertailua — virhe on line 45."

> **Pysähdy hetkeksi:** Kun olet havainnut, että ohjelma ei toimi, mitkä ovat ensimmäiset asiat, joihin katsot? Lokit? Koodi? Näyttö?

## CLI-komennot ja turvallinen generointi

Komentorivi-käyttöjärjestelmät (CLI) voivat tuntua pelottavilta. Tuhat komentoa, oudot vipuja, kuten `-r` ja `--recursive`. Monet opiskelijat pelkäävät tehdä virheen "ja rikkoa kaiken".

Tämä on järkevä varovaisuus. Jotkut komennot voivat poistaa tiedostoja tai muuttaa järjestelmää pysyvästi. Mutta pelko ei ole hyvä neuvonantaja.

**Turvallisuus ensin:** Kun AI:ta pyydetään generoimaan komentoja, sinun täytyy ymmärtää niitä ennen kuin ajat. Et koskaan kopioi ja liitä komentoa suoraan.

Hyvä prosessi:
1. Pyydä AI:ta: "Kirjoita komento, joka poistaa tiedostot, joiden nimi alkaa 'temp_' nykyisestä hakemistosta."
2. AI antaa: `find . -name "temp_*" -type f -delete`
3. **Sinä kysyt:**
   - Mitä `find` tekee? (etsii tiedostoja)
   - Mitä `-name "temp_*"` tarkoittaa? (nimestä alkaa temp_)
   - Mitä `-type f` tarkoittaa? (vain tiedostot, ei hakemistot)
   - Mitä `-delete` tekee? (poistaa ne!)
4. Sinä ajat komennon **turvallisesti:** ensin kokeilla kanssa `ls` sen sijaan `-delete`, nähdä mitä se löytää, sitten kokeilla poistamista.

Ammattilaisesti et koskaan kopioi komentoja sokeasti. Sinä:
- Ymmärrät, mitä komento tekee
- Luot testiskenaarion ensimmäiseksi
- Ajat sen turvallisesti (preview ensin, sitten oikea)

AI voi auttaa **shell-skriptien** kirjoittamisessa. Jos sinulla on sarja komentoja, joita joudut ajamaan usein, voit pyytää AI:ta:

"Kirjoita shell-skripti, joka:
1. Varmuuskopioi kaikki .txt-tiedostot hakemistoon 'backups/'
2. Kirjaa backup-ajan tiedostoon 'backup.log'
3. Poistaa yli 30 päivää vanhat varmuuskopiot
Skripti saa kutsua: `./backup.sh`"

AI antaa sinulle pohjan. Sinä testat sitä, muokkaat ja hyväksyt.

## Yhteenveto: AI koko IT-uraasi yksi työkalu

Ammattilaisena — riippumatta siitä, mitä IT-alaa valitset — käytät AI:ta jonakin pitkän ajan. Se ei ole koodaajalle. Se on sinulla, kun kirjoitat dokumentaatiota, analysoit lokeja, opettelet uuden komentorivikäskyn tai ratkaiset ongelmaa.

Avain on **ymmärrys ja kriittinen ajattelu**. AI antaa ehdotuksia — koodi, komennot, dokumentaation — mutta sinä validoit ja hyväksyt. Ammattilaisena olet vastuussa.

Neljä tärkeintä asiaa:

1. **Dokumentaatio** on ammattilaisuutta. AI voi auttaa, mutta sinä olet vastuussa, että se on oikea ja ajantasainen.

2. **Lokit** ovat sinun paras ystävä. Kun jotain menee pieleen, lokit kertovat mitä tapahtui. AI voi auttaa lukemaan niitä.

3. **CLI-komennot** eivät ole pelottavia, jos ymmärrät ne ensin. Turvallisuus ensin, sitten toiminta.

4. **AI on apulainen, et johtaja.** Sinä päätät, mitä tehdä. AI antaa ehdotuksia.

Tämä on ammattilaisuutta.

