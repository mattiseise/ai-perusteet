# Oma apuri-botti — viimeistele ja esittele ★

## Mitä teet?

> **HUOM:** Tätä varten sinulla tulee olla kerättynä rakennuspalikat 1–3 (tunnit 12, 14 ja 15).

Viimeistelet oman apuri-bottisi valitsemallasi suorituspolulla. **Teknisellä toteutuspolulla** rakennat ja testaat botin saatavilla olevalla alustalla. **Dokumentoidulla suunnittelupolulla** viimeistelet arkkitehtuurin, simuloidun suoritusjäljen, tietolähteiden kuvaukset, testit ja tunnistetut rajoitukset. Polut ovat samanarvoisia, mutta suunnittelupolku ei todista teknisten yhteyksien toimivuutta.

Käytä tekoälyä apuna botin rakentamisessa. Tarkoitus ei ole, että keksit kaiken itse — vaan että **osaat ohjata tekoälyä auttamaan sinua suunnittelussa, testauksessa ja viimeistelyssä** ja teet lopulliset päätökset itse. Sinun vastuullasi on, että tekninen botti toimii tarkoituksenmukaisesti tai suunnittelupaketti kuvaa toiminnan toteutuskelpoisesti ja että ymmärrät ratkaisun rakenteen kokonaan.

Valitse itseäsi kiinnostava, omasta arjestasi tuttu **aihe**. Tässä on esimerkkejä — käytä jotakin näistä tai keksi omasi:

- **Opiskelu** — esim. kertauskaveri kokeeseen, käsitteiden selittäjä, tehtävien jäsentäjä
- **Harrastus tai kerho** — esim. sääntöjen ja aikataulujen opastaja, FAQ-botti uusille jäsenille
- **Tuttu pieni palvelu** — esim. kahvilan, kirjaston tai urheiluseuran FAQ-botti
- **Pelit, musiikki tai sisältö** — esim. pelin tarinan ideointi, biisin tai videon suunnittelu
- **Arjen apuri** — esim. treeniviikon suunnittelija, viikkoaikataulun kokoaja

Bottisi auttaa juuri sinun aiheesi parissa toimivaa käyttäjää **pääsemään tavoitteeseensa** — esimerkiksi valmistautumaan kokeeseen, löytämään vastauksen kerhon FAQ:sta tai kokoamaan oman treeniviikon. Vaiheet ovat usein samankaltaiset: lähtötilanne, tavoite, vaihtoehdot ja lopputulos — mutta termit, painotukset ja sisältö ovat erilaisia eri aiheissa. Tämä on sinun bottisi erikoisosaamista.

## Miten teet sen?

Tämän tunnin työssä on neljä vaihetta:

1. **Valitse yksi korjaus:** Palaa tunnin 17 kolmeen ensitulokseen ja valitse korjauslistalta yksi olennainen puute.
2. **Korjaa:** Tee yksi nimetty muutos järjestelmäpromptiin, tietopohjaan tai suunnittelupaketin kuvaukseen.
3. **Testaa uudelleen:** Toista juuri korjaukseen liittyvä testi samalla odotuksella ja tallenna ennen–jälkeen-vertailu.
4. **Viimeistele:** Kokoa aiemmat rakennuspalikat, kolme ensitestiä, korjausketju, reflektio ja polkukohtainen näyttö yhdeksi palautukseksi.

## Rakennuspalikat

Olet kerännyt kolme rakennuspalikkaa aiemmilla oppitunneilla. Käytä niitä botin pohjana:

- **Rakennuspalikka 1** (oppitunti 12, promptikortti) antaa testatun rakenteen järjestelmäpromptille.
- **Rakennuspalikka 2** (oppitunti 14, botin määrittely) antaa pohjan suunnittelulle. Persoona, kohderyhmä, rajat, tavoitteet — kaikki valmiina.
- **Rakennuspalikka 3** (oppitunti 15, tietopohja ja testisuunnitelma) sisältää 2–4 huolella valittua lähdettä ja kolme ennalta kirjoitettua testiä.

> **Vinkki:** *"Tässä ovat keräämäni rakennuspalikat. Käytä niitä bottini ohjeen ja rakenteen pohjana: <liitä rakennuspalikkasi>"*

## Bottisi vaatimukset

Lopullisen botin tulee täyttää seuraavat kriteerit:

1. **Selkeä rooli ja kohderyhmä.** Botti tietää keneltä se saa kysymyksiä (oman aiheesi käyttäjältä) ja mitä se tekee (auttaa tehtävän tekemisessä).
2. **Strukturoitu työnkulku.** Botti ohjaa käyttäjää tehtävän vaiheiden läpi järjestelmällisesti (lähtötilanne → tavoite → vaihtoehdot → valinnat → lopputulos).
3. **Aiheesi termit ja näkökulmat.** Botti puhuu oman aiheesi kieltä — salitreenin botille eri termit kuin kerhon FAQ-botille. Tämä erottaa sinun bottisi yleisestä avustajasta.
4. **Selkeät rajat.** Botti tietää mitä se EI tee — esimerkiksi se ei tee koko tehtävää käyttäjän puolesta, ei anna terveys- tai oikeudellisia neuvoja, ei toimi muissa aiheissa. Rajat ovat osa huolellisuutta.
5. **Testattu sovitulla aikajanalla.** Tunnin 17 normaali, kielteinen ja reunatapaus sekä tunnin 18 yksi korjaus ja sitä koskeva uudelleentesti on dokumentoitu.

## Mitä palautat?

Palauta yksi tiedosto, joka sisältää:

1. **Botin määrittely** (tunti 14:n botin määrittely, päivitettynä tähän bottiin)
2. **Bottisi järjestelmäprompti** kokonaisuudessaan kopioituna
3. **Lista tietopohjan dokumenteista** ja perustelu, miksi valitsit juuri nämä
4. **Testimatriisi ja korjausketju:** kolmesta testistä syöte, odotus, tulos ja johtopäätös sekä yhdestä korjauksesta ennen–jälkeen-näyttö
5. **Reflektio** (200–300 sanaa): mitä opit botin rakentamisesta, mikä havainto johti korjaukseen ja mitä tekisit seuraavaksi? Saavutettavana vaihtoehtona voit palauttaa 2–3 minuutin äänitteen tai selostetun 3–5 dian kuvakoosteen, joka vastaa samoihin kysymyksiin.

Lisäksi polkukohtainen näyttö. Teknisellä polulla annat linkin tai muun pääsyn bottiin sekä tallennetut testitulokset. Suunnittelupolulla annat arkkitehtuurin, simuloidun suoritusjäljen ja luettelon toteuttamatta jääneistä teknisistä ominaisuuksista.

## Lyhyt esittely ja puolustus

Pidä 2–3 minuutin esittely. Esittelyssä:

- Kerro, kenelle botti on rakennettu ja mitä se ratkaisee
- Näytä yksi ennen–jälkeen-korjaus
- Perustele yksi rajaus ja vastaa yhteen jatkokysymykseen

Esittely tehdään 2–3 hengen pienryhmässä, tallenteena tai opettajan valitsemana otoksena. Koko luokan peräkkäistä esittelykierrosta ei tehdä. Esittely ja reflektio valmistuvat tämän oppitunnin aikana.

## Jos et tiedä mistä aloittaa

Aloita näin:

1. Avaa tunnilla 17 tallentamasi kolme ensitulosta ja korjauslista.
2. Valitse yksi puute, joka liittyy suoraan ennalta kirjoitettuun odotukseen.
3. Tee yksi nimetty korjaus järjestelmäpromptiin, tietopohjaan tai suunnittelupaketin kuvaukseen.
4. Toista juuri sitä koskeva testi samalla odotuksella ja tallenna ennen–jälkeen-näyttö.
5. Tee reflektio ja 2–3 minuutin esittely tämän tunnin aikana.

*Et opettele käyttämään tekoälyä. Opit rakentamaan sillä.*
