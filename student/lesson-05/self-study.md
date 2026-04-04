# Konteksti II: konteksti-ikkuna ja hallinta

## Johdanto

Kuvittele, että istut opettajan kanssa tämän viikon aikana pitkään IT-projektiin liittyen. Maanantaina opettaja muistaa, mitä keskustelitte edellisellä viikolla. Tiistaina hän muistaa vielä. Mutta kahden kuukauden jälkeen? Hän unohtaa. Hänen muistinsa on rajallinen — ei siksi, että hän olisi laiska, vaan koska ihmisen muisti voi säilyttää vain tietyn määrän tietoa kerralla. Kielimallit ovat samoin. Ne eivät voi säilyttää koko keskustelua muistissa rajattomasti. Ne käyttävät konteksti-ikkunaa (context window) — rajallista "muistiruutua", joka säilyttää vain viimeaikaisen keskustelun. Kun ikkuna täyttyy, vanha tieto häviää. Tämän oppitunnin aiheena on, miten ymmärrät tämän rajan, ja kuinka hallitset kontekstia niin, että tekoäly saa aina tarvitsemansa tieto.

## Mitä konteksti-ikkuna on

Konteksti-ikkuna on tokenit (tokens) — pienet tekstin palat, joita tekoälymallit käsittelevät — määritellyt raja, joka rajoittaa kuinka paljon tekstiä malli voi käsitellä yhdessä keskustelussa. Esimerkiksi ChatGPT-4:llä on konteksti-ikkuna noin 128 000 tokenia. Claude 3:lla vielä enemmän. Mutta vaikka se olisi suuri, se ei ole ääretön.

Tokenit eivät ole täsmälleen sanat. Englannin kielessä yksi toki on noin 4 merkkiä, joten 128 000 tokenia on suunnilleen 512 000 merkkiä tai noin 85 000 sanaa. Se kuulostaa paljon — ja se onkin, alle paperiosaamisen kirjasta. Mutta IT-projektissa, jossa on tuhansia koodeja, satoja sähköposteja tai pitkiä lokeja, se täyttyy nopeasti.

Kun malli käsittelee syötettä, se menettää vanhimman osan (vanhat viestit) ja säilyttää vain uudemman osan (uusimmat viestit). Tämä on kuin puhelimen tekstiviesti-chat, joka näyttää vain viimeiset 100 viestiä — vanhemmat viestit liukuvat pois näkyvistä. Malli ei näe enää vanhaa kontekstia. Jos aiemmin sanoit "Käytän Ubuntu 20.04:ää", mutta keskustelu on nyt 15 000 tokenia eteenpäin, malli saattaa unohtaa sen.

> **Pysähdy hetkeksi:** Kuvittele, että neuvot ystävääsi ohjelmointiongelmassa tunnin ajan. Ystävä kysyy lopuksi: "Muista se mitä sanottimet alussa?" Jos sinulla olisi silloin huono muisti, mitä kaipaisit hän kertomaan uusiksi?

## Miten tieto putoaa ulos ikkunasta

Konteksti-ikkunan täyttyminen on systemaattista: ensimmäinen sisään, ensimmäinen ulos (FIFO, First In First Out). Jos aloitat keskustelun ja antaa paljon kontekstia, sitten kysyt 20 kertaa peräkkäin, kunnes keskustelulla on 120 000 tokenia — alkuperäinen kontekstisi on jo poissa. Mallin näkemykset käsillä ovat vain 10 viimeiset kysymys-vastaus-paria ja vähän kontekstia.

Tämä voi johtaa häiritseviin tilanteisiin. Olet saattanut sanoa "Tarvitsen vain Linux-komentoja, en Windowsia" alussa, mutta 50 viestin jälkeen malli alkaa ehdottaa Windows-ratkaisuja, koska se on unohtanut rajoituksesi. Tai olet antanut tarkemmat esimerkit koodista alussa, mutta myöhemmin malli ehdottaa koodia, joka ei noudatta samaa rakennetta, koska se ei näe enää esimerkkejä.

Tiedon putoaminen voi myös muuttaa keskustelun sävyä. Jos olet aluksi "opiskelijana, joka oppii", mutta 30 viestin jälkeen tämä rooli unohdetaan, malli saattaa alkaa pitää sinua asiantuntijana ja antaa hyvin teknisiä vastauksia ilman selityksiä.

> **Pysähdy hetkeksi:** Ajattele pitkää projektin debuggaamista. Mitä "väärää tietoa" voisi malli unohtaa, joka aiheuttaisi väärää neuvoja?

## Kuinka kontekstia tiivistetään, pilkotaan ja rakennetaan uudelleen

Ammattilaisena sinun täytyy hallita konteksti-ikkuna. On kolme päästrategiaa.

Ensimmäinen on **tiivistys**: ottaa vanha, pitkä teksti ja pakkaa se pienemmäksi, oleellisen säilyttäen. Esimerkiksi, jos sinulla on 2000 rivin lokitiedosto, joka kertoo kuuden tunnin kuluessa tapahtuneet virheet, voit pyytää tekoälyä "yhteenveto: mitkä olivat pääongelmien virheitä?" Se tiivistää lokin yhteenvedoksi. Nyt lokit ottavat 500 tokenia 5000:n sijasta. Loput pinta-alasta vapauttaa uudelle kontekstille.

Toinen on **pilkkominen**: jakaa pitkä tehtävä moniin pienemmiksi, hallittaviksi osiksi, ja käydä keskustelu kunkin osion kanssa erikseen. Esimerkiksi, jos sinun täytyy analyysi analysoida 10 000 rivin tietokanta-skeemaa, älä lähetä sitä kaikkea kerralla. Jaa se: "Lue taulukot 1-100" — hyvä vastaus. Sitten "Lue taulukot 101-200" — uusi keskustelu, uusi konteksti-ikkuna. Kirjoita tulokset muistiin. Lopuksi kootaan yhteenveto. Jokainen osa on hallittava, ja et koskaan ylitä ikkunaa.

Kolmas on **ankkurointi**: pitää olennainen tieto näkyvissä ja päivitettävissä koko ajan. Esimerkiksi, kun aloitat pitkän projektin, pyydät mallia luomaan "projektierityisen kontekstin", jonka antisissa jokaisessa viestissä. "Muista aina: Käytämme Python 3.9:ää, PostgreSQL:ää, ja käyttäjänä 'admin'. Nämä eivät muutu." Tämä ankkurointi varmistaa, että vaikka malli menettää vanhaa tekstiä, se säilyy nämä ydinrajoitukset.

Ammattilaisessa IT-työssä näitä kolmea käytetään yhdessä. Jos sinulla on suuri projekti, jonka täytyy kestää useita päiviä:
1. Ankkuroi olennainen rooli, tausta ja rajaukset joka päivä.
2. Pilko päivän tehtävät pienemmiksi keskusteluiksi.
3. Tiivistä edellisten päivien tulokset yhteen muistioon, jonka lisäät kontekstiin.

Näin malli säilyttää käyttökelpoisen muistin koko projektin ajan.

> **Pysähdy hetkeksi:** Ajattele omaa projektia, joka kestää viikon tai enemmän. Kuinka jakaisit sen osiin, jotta konteksti-ikkuna ei koskaan täyttyisi?

## Konversaation hallinta käytännössä

Käytännössä konteksti-ikkunan hallinta alkaa siitä, että ymmärrät koko projektisi koon ja kompleksiteetin. Pieni kysymys? Älä huoli ikkunasta — 1000 tokenia ei ole ongelma. Suuri analyysi? Suunnittele etukäteen.

Kun aloitat tekoälyn kanssa keskustelun, pidä mielessä:

- **Jokainen vastaus kuluttaa ikkunaa.** Kun malli vastaa, se käyttää tokeneita. Pitkä vastaus = enemmän ikkunaa käytetty.
- **Historia kasvaa.** Jokainen uusi kysymys lisää ikkunaan. Jos kysyt 100 kertaa, historia on paljon suurempi kuin kun kysyt kerran.
- **Vanha tieto menetetään ensin.** Jos aloitit kontekstilla "Käytän Ubuntu 20.04:ää, Python 3.9:ää ja PostgreSQL:ää", ja nyt olet 100 viestiä eteenpäin, se tieto voi olla pois ikkunasta.

Ratkaisuksi:
- Jaa pitkä projekti useiksi lyhyiksi keskusteluiksi. Jokainen keskustelu on uusi, puhdas ikkuna.
- Dokumentoi tulokset. Kun aloitat uuden keskustelun, kopioi oleelliset tulokset kontekstiin.
- Käytä "muista aina" -tekniikkaa: jokaisen viestin alussa, muistuta mallia tärkeistä asioista.

Esimerkiksi:
- **Päivä 1:** Analysoit tietokantaa. Alusta kontekstista: "Käytämme PostgreSQL:ää, tauluja on 50, tärkein on 'users'. Analysoin nyt tauluja 1-5."
- **Päivä 2:** Aloitat uudesta. Konteksti: "Edellispäivää jatkaen. Käytämme PostgreSQL:ää, 50 taulua. Eilen analyysissä 1-5 paljastui: [yhteenveto]. Nyt analysoin tauluja 6-10."

Näin malli ei koskaan unohda oleellista, vaikka ikkuna olisi täyttynyt.

## Yhteenveto

Konteksti-ikkuna on tekninen raja, joka rajoittaa kuinka paljon tekstiä tekoäly voi käsitellä yhdessä keskustelussa. Vanha tieto putoaa ulos, kun ikkuna täyttyy. Ammattilaisena hallitset ikkunaa kolmella tavalla: tiivistämällä vanhat teksti, pilkomalla projektit pienempiin osiin ja ankkuroimalla oleellisen tiedon joka viestiin. Näillä menetelmillä voit johtaa pitkiä, monimutkaisia projekteja tekoälyn kanssa ilman, että mallin muisti pettää. Konteksti-ikkunan ymmärtäminen on avain siihen, että tekoälystä tulee luotettava työkaveri, ei epävakaa avustaja.
