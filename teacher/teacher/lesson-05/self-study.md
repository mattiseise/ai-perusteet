# Muistin rajat — kuinka paljon tekoäly oikeasti muistaa

## Johdanto

Kuvittele, että työskentelet opettajan kanssa koko viikon ajan pitkän IT-projektin parissa. Maanantaina opettaja muistaa hyvin, mistä keskustelitte edellisellä viikolla. Tiistaina hän muistaa sen edelleen. Mutta entä kahden kuukauden kuluttua? Hän on jo unohtanut.

Hänen muistinsa on rajallinen — ei siksi, että hän olisi laiska, vaan siksi, että ihmisen muisti pystyy säilyttämään vain tietyn määrän tietoa kerrallaan.

Kielimallit toimivat samalla periaatteella. Ne eivät voi säilyttää koko keskustelua rajattomasti muistissa. Sen sijaan ne käyttävät niin sanottua konteksti-ikkunaa (context window). Se on rajallinen "muisti-ikkuna", jossa säilyy vain osa keskustelusta.

Kun tämä ikkuna täyttyy, vanhimmat tiedot poistuvat ja uudet tulevat tilalle.

Tämän oppitunnin aiheena on ymmärtää tämä raja ja oppia hallitsemaan kontekstia niin, että tekoäly saa aina tarvitsemansa tiedon.

Tämän tunnin jälkeen sinulla on tuomaripöydällesi viides todistusaineisto: tekoälyllä on samat muistin rajat kuin ihmisillä — ja joskus jopa pienempiä.

## Mitä konteksti-ikkuna on?

Konteksti-ikkuna on tekoälymalleille asetettu raja, joka määrittää, kuinka paljon tekstiä malli voi käsitellä yhdessä keskustelussa. Raja määritellään tokeneina, jotka ovat pieniä tekstin palasia. Esimerkiksi ChatGPT-4:llä on konteksti-ikkuna, jossa on noin 128 000 tokenia, ja Claude 3:lla vielä suurempi. Vaikka ikkuna olisi suuri, se ei ole ääretön.

Tokenit eivät ole sama asia kuin sanat. Englannin kielessä yksi tokeni on noin 4 merkkiä, joten 128 000 tokenia vastaa noin 512 000 merkkiä eli noin 85 000 sanaa. Se kuulostaa paljolta — ja onkin, pituudeltaan lähes painetun kirjan verran. Mutta IT-projektissa, jossa on tuhansia rivejä koodia, satoja sähköposteja tai pitkiä lokitiedostoja, se täyttyy nopeasti.

Kun malli käsittelee syötettä, se menettää keskustelun vanhimman osan ja säilyttää vain uudemman osan. Tämä on kuin puhelimen tekstiviestiketju, joka näyttää vain viimeiset 100 viestiä — vanhemmat viestit liukuvat pois näkyvistä. Malli ei enää näe vanhaa kontekstia. Jos sanoit aiemmin "Käytän Ubuntu 20.04:ää", mutta keskustelu on nyt 15 000 tokenia pidemmällä, malli saattaa unohtaa sen.

> **Pysähdy hetkeksi:** Kuvittele, että neuvot ystävääsi ohjelmointiongelmassa tunnin ajan. Ystävä kysyy lopuksi: "Muistatko sen, mitä sanoin alussa?" Jos muistisi olisi silloin huono, mitä toivoisit hänen kertovan uudelleen?

## Miten tieto putoaa ulos ikkunasta

Konteksti-ikkunan täyttyminen noudattaa FIFO-periaatetta (First In, First Out) — ensimmäinen sisään, ensimmäinen ulos. Jos aloitat keskustelun antamalla paljon kontekstia ja sitten kysyt 20 kertaa peräkkäin, kunnes keskustelussa on 120 000 tokenia, alkuperäinen kontekstisi on jo kadonnut. Mallilla on käytössään vain viimeiset muutamat kysymys–vastaus-parit ja hieman muuta kontekstia.

Tämä voi johtaa häiritseviin tilanteisiin. Olet saattanut sanoa alussa: "Tarvitsen vain Linux-komentoja, en Windowsia", mutta 50 viestin jälkeen malli alkaa ehdottaa Windows-ratkaisuja, koska se on unohtanut rajauksesi. Tai olet antanut tarkat koodiesimerkit keskustelun alussa, mutta myöhemmin malli ehdottaa koodia, joka ei noudata samaa rakennetta, koska se ei enää näe esimerkkejä.

Tiedon putoaminen voi myös muuttaa keskustelun sävyä. Jos olet aluksi "opiskelija, joka oppii", mutta 30 viestin jälkeen tämä rooli unohtuu, malli saattaa alkaa pitää sinua asiantuntijana ja antaa hyvin teknisiä vastauksia ilman selityksiä.

> **Pysähdy hetkeksi:** Ajattele pitkää projektin debuggaamista. Mitä tärkeää tietoa malli voisi unohtaa niin, että se alkaisi antaa vääriä neuvoja?

## Kuinka kontekstia tiivistetään, pilkotaan ja rakennetaan uudelleen

Ammattilaisena sinun täytyy hallita konteksti-ikkunaa. Siihen on kolme päästrategiaa.

Ensimmäinen on **tiivistys**: vanha, pitkä teksti pakataan pienemmäksi niin, että olennainen säilyy. Esimerkiksi, jos sinulla on 2 000 rivin lokitiedosto, joka kertoo kuuden tunnin aikana tapahtuneista virheistä, voit pyytää tekoälyä tekemään yhteenvedon: "Mitkä olivat pääongelmat ja virheet?" Se tiivistää lokin yhteenvedoksi. Nyt loki vie 500 tokenia 5 000:n sijasta. Loput tilasta vapautuu uudelle kontekstille.

Toinen on **pilkkominen**: pitkä tehtävä jaetaan moniin pienempiin, hallittaviin osiin, ja jokaisesta osiosta käydään keskustelu erikseen. Esimerkiksi, jos sinun täytyy analysoida 10 000 rivin tietokantaskeema, älä lähetä sitä kaikkea kerralla. Jaa se osiin: "Lue taulukot 1–100" — hyvä vastaus. Sitten: "Lue taulukot 101–200" — uusi keskustelu, uusi konteksti-ikkuna. Kirjoita tulokset muistiin. Lopuksi kootaan yhteenveto. Jokainen osa on hallittava, etkä koskaan ylitä ikkunan rajaa.

Kolmas on **ankkurointi**: olennainen tieto pidetään näkyvissä ja päivitettävissä koko ajan. Esimerkiksi, kun aloitat pitkän projektin, pyydät mallia muistamaan "projektikohtaisen kontekstin", jonka toistat jokaisessa viestissä. "Muista aina: Käytämme Python 3.9:ää, PostgreSQL:ää ja käyttäjänimeä 'admin'. Nämä eivät muutu." Tämä ankkurointi varmistaa, että vaikka malli menettäisi vanhaa tekstiä, se säilyttää nämä keskeiset rajaukset.

Ammatillisessa IT-työssä näitä kolmea strategiaa käytetään yhdessä. Jos sinulla on suuri projekti, joka kestää useita päiviä:

1. Ankkuroi olennainen rooli, tausta ja rajaukset joka päivä.
2. Pilko päivän tehtävät pienemmiksi keskusteluiksi.
3. Tiivistä edellisten päivien tulokset yhteen muistioon, jonka sisällytät seuraavan päivän kontekstiin.

Näin malli säilyttää käyttökelpoisen muistin koko projektin ajan.

> **Pysähdy hetkeksi:** Ajattele omaa projektia, joka kestää viikon tai pidempään. Miten jakaisit sen osiin, jotta konteksti-ikkuna ei koskaan täyttyisi?

## Konversation hallinta käytännössä

Käytännössä konteksti-ikkunan hallinta alkaa siitä, että ymmärrät koko projektisi koon ja monimutkaisuuden. Pieni kysymys? Älä huolehdi ikkunasta — 1 000 tokenia ei ole ongelma. Suuri analyysi? Suunnittele etukäteen.

Kun aloitat keskustelun tekoälyn kanssa, pidä mielessäsi seuraavat asiat:

- **Jokainen vastaus kuluttaa ikkunaa.** Kun malli vastaa, se käyttää tokeneita. Pitkä vastaus = enemmän ikkunaa käytetty.
- **Historia kasvaa.** Jokainen uusi kysymys lisää sisältöä ikkunaan. Jos kysyt 100 kertaa, historia on paljon suurempi kuin jos kysyt kerran.
- **Vanha tieto menetetään ensin.** Jos aloitit kontekstilla "Käytän Ubuntu 20.04:ää, Python 3.9:ää ja PostgreSQL:ää", ja nyt olet 100 viestiä pidemmällä, tämä tieto voi olla jo poissa ikkunasta.

Ratkaisuksi:

- Jaa pitkä projekti useiksi lyhyiksi keskusteluiksi. Jokainen keskustelu on uusi, puhdas ikkuna.
- Dokumentoi tulokset. Kun aloitat uuden keskustelun, kopioi oleelliset tulokset mukaan kontekstiin.
- Käytä "muista aina" -tekniikkaa: muistuta mallia jokaisen viestin alussa tärkeistä asioista.

Esimerkiksi:

- **Päivä 1:** Analysoit tietokantaa. Aloita kontekstilla: "Käytämme PostgreSQL:ää, tauluja on 50, tärkein on 'users'. Analysoin nyt tauluja 1–5."
- **Päivä 2:** Aloitat uudelleen. Konteksti: "Edellispäivää jatkaen. Käytämme PostgreSQL:ää, tauluja on 50. Eilen analyysissä 1–5 paljastui: [yhteenveto]. Nyt analysoin tauluja 6–10."

Näin malli ei koskaan unohda oleellista, vaikka ikkuna olisi täyttynyt.

## Yhteenveto

Konteksti-ikkuna on tekninen raja, joka määrittää, kuinka paljon tekstiä tekoäly voi käsitellä yhdessä keskustelussa. Vanha tieto putoaa ulos, kun ikkuna täyttyy. Ammattilaisena hallitset ikkunaa kolmella tavalla: tiivistämällä vanhoja tekstejä, pilkkomalla projektit pienempiin osiin ja ankkuroimalla oleellisen tiedon jokaiseen viestiin. Näillä menetelmillä voit johtaa pitkiä, monimutkaisia projekteja tekoälyn kanssa ilman, että mallin muisti pettää. Konteksti-ikkunan ymmärtäminen on avain siihen, että tekoälystä tulee luotettava työkaveri eikä epävakaa avustaja.

Seuraavalla tunnilla laajennat näkökulmaasi: tekoäly voi käsitellä enemmän kuin pelkkää tekstiä — kuvia, ääntä, videota.