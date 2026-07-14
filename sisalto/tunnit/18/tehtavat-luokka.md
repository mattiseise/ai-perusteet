# Oma apuri-botti — viimeistele ja esittele ★

## Mitä teet?

> **HUOM:** Tätä varten sinulla tulee olla kerättynä rakennuspalikat 1–3 (tunnit 12, 14 ja 15).

Rakennat **Microsoft Copilot Agent** -alustalle oman bottisi, joka auttaa **jossakin sinulle tutussa arjen aiheessa**. Et tee asioita botin puolesta — sinä rakennat *työkalun*, joka auttaa muita (tai sinua itseäsi) onnistumaan paremmin, nopeammin ja johdonmukaisemmin.

Käytä tekoälyä apuna botin rakentamisessa. Tarkoitus ei ole, että keksit kaiken itse — vaan että **osaat ohjata tekoälyä auttamaan sinua suunnittelussa, testauksessa ja viimeistelyssä** ja teet lopulliset päätökset itse. Sinun vastuullasi on, että botti toimii hyvin, tuottaa oikeasti hyödyllisiä vastauksia ja että ymmärrät sen rakenteen kokonaan.

Valitse itseäsi kiinnostava, omasta arjestasi tuttu **aihe**. Tässä on esimerkkejä — käytä jotakin näistä tai keksi omasi:

- **Opiskelu** — esim. kertauskaveri kokeeseen, käsitteiden selittäjä, tehtävien jäsentäjä
- **Harrastus tai kerho** — esim. sääntöjen ja aikataulujen opastaja, FAQ-botti uusille jäsenille
- **Tuttu pieni palvelu** — esim. kahvilan, kirjaston tai urheiluseuran FAQ-botti
- **Pelit, musiikki tai sisältö** — esim. pelin tarinan ideointi, biisin tai videon suunnittelu
- **Arjen apuri** — esim. treeniviikon suunnittelija, viikkoaikataulun kokoaja

Bottisi auttaa juuri sinun aiheesi parissa toimivaa käyttäjää **pääsemään tavoitteeseensa** — esimerkiksi valmistautumaan kokeeseen, löytämään vastauksen kerhon FAQ:sta tai kokoamaan oman treeniviikon. Vaiheet ovat usein samankaltaiset: lähtötilanne, tavoite, vaihtoehdot ja lopputulos — mutta termit, painotukset ja sisältö ovat erilaisia eri aiheissa. Tämä on sinun bottisi erikoisosaamista.

## Miten teet sen?

Botin rakentamisessa on neljä vaihetta. Käytä niitä työvaiheina:

1. **Botin määrittely:** Päätä, kenelle botti on, mitä se osaa ja mitä se ei tee. Käytä pohjana tunnin 14 botin määrittelyäsi (rakennuspalikka 2).
2. **Järjestelmäprompti ja persoona:** Kirjoita botille ohjeet — kuka se on, miten se vastaa, missä järjestyksessä se ohjaa käyttäjää. Käytä pohjana tunnin 12 promptauspankkiasi (rakennuspalikka 1).
3. **Tietopohja:** Lataa bottiin 3–5 dokumenttia, jotka antavat sille tarvittavan asiantuntemuksen oman aiheesi tiedosta. Käytä pohjana tunnin 15 kuratoituja dokumenttejasi (rakennuspalikka 3).
4. **Testaus ja viimeistely:** Testaa bottia oikealla käyttötilanteella. Korjaa ohjeita, lisää rajoitteita, päivitä tietopohjaa. Lopullinen botti vastaa selkeästi ja luotettavasti.

## Rakennuspalikat

Olet kerännyt kolme rakennuspalikkaa aiemmilla oppitunneilla. Käytä niitä botin pohjana:

- **Rakennuspalikka 1** (oppitunti 12, promptauspankki) antaa pohjan järjestelmäpromptille. Olet jo kirjoittanut ohjeita, jotka toimivat — käytä niiden rakennetta botin pääohjeessa.
- **Rakennuspalikka 2** (oppitunti 14, botin määrittely) antaa pohjan suunnittelulle. Persoona, kohderyhmä, rajat, tavoitteet — kaikki valmiina.
- **Rakennuspalikka 3** (oppitunti 15, tietopohjan kuratointi) antaa pohjan tietopohjalle. Tiedät jo, millainen materiaali toimii ja mikä ei.

> 💡 **Vinkki:** *"Tässä on keräämäni rakennuspalikat, käytä niitä bottini ohjeen ja rakenteen pohjana… <liitä rakennuspalikkasi>"*

## Bottisi vaatimukset

Lopullisen botin tulee täyttää seuraavat kriteerit:

1. **Selkeä rooli ja kohderyhmä.** Botti tietää keneltä se saa kysymyksiä (oman aiheesi käyttäjältä) ja mitä se tekee (auttaa tehtävän tekemisessä).
2. **Strukturoitu työnkulku.** Botti ohjaa käyttäjää tehtävän vaiheiden läpi järjestelmällisesti (lähtötilanne → tavoite → vaihtoehdot → valinnat → lopputulos).
3. **Aiheesi termit ja näkökulmat.** Botti puhuu oman aiheesi kieltä — salitreenin botille eri termit kuin kerhon FAQ-botille. Tämä erottaa sinun bottisi yleisestä avustajasta.
4. **Selkeät rajat.** Botti tietää mitä se EI tee — esimerkiksi se ei tee koko hommaa käyttäjän puolesta, ei anna terveys- tai oikeudellisia neuvoja, ei toimi muissa aiheissa. Rajat ovat osa huolellisuutta.
5. **Testattu oikealla esimerkillä.** Olet ajanut botin läpi vähintään yhden oikean käyttötilanteen kanssa ja korjannut puutteet, jotka testissä paljastuivat.

## Mitä palautat?

Palauta yksi tiedosto, joka sisältää:

1. **Botin määrittely** (tunti 14:n botin määrittely, päivitettynä tähän bottiin)
2. **Bottisi järjestelmäprompti** kokonaisuudessaan kopioituna
3. **Lista tietopohjan dokumenteista** ja perustelu, miksi valitsit juuri nämä
4. **Testikeskustelu** botin kanssa: vähintään yksi täysi keskustelu, jossa botti ohjaa kuvitellun käyttäjän valitsemasi tehtävän läpi alusta loppuun (näytä kuvakaappauksina tai kopioituna)
5. **Reflektio** (200–300 sanaa): mitä opit botin rakentamisesta? Mikä toimi heti, mikä vaati monta yritystä? Mitä tekisit toisin, jos rakentaisit tämän uudelleen?

Lisäksi **linkki bottiisi** Copilotissa, jotta arvioija pääsee testaamaan sitä itse.

## Esittely (valinnainen)

Voit halutessasi pitää bottisi esittelyn ryhmälle. Esittelyssä:

- Kerro, kenelle botti on rakennettu ja mitä se ratkaisee
- Näytä yksi konkreettinen testikeskustelu
- Kerro yksi asia, jonka opit matkan varrella ja jota et osannut alussa

Esitys voi olla live ryhmän edessä, nauhoitettu video tai jaettu kuvakaappauskooste — valitse muoto, joka sopii sinulle.

## Jos et tiedä mistä aloittaa

Aloita näin:

1. Avaa **rakennuspalikka 2** (tunti 14, botin määrittely). Päivitä se kuvaamaan tätä bottia — kohderyhmä on nyt oman aiheesi käyttäjä.
2. Kirjoita botin **järjestelmäpromptin ensimmäinen versio**. Pohjana **rakennuspalikka 1** (tunti 12, promptauspankki) — ota sieltä parhaiten toimivat rakenteet.
3. Lataa **rakennuspalikka 3** (tunti 15, kuratoitu tietopohja) bottiin. Jos tietopohja ei riitä, etsi 1–2 lisädokumenttia juuri oman aiheesi näkökulmasta.
4. Aja yksi testi: keksi kuvitteellinen käyttötilanne omasta aiheestasi ja katso, miten botti ohjaa sinua.
5. Korjaa, mikä ei toimi. Toista. Yhden iteraation jälkeen ei ole valmis — kahden tai kolmen jälkeen on.

*Et opettele käyttämään tekoälyä. Opit rakentamaan sillä.*
