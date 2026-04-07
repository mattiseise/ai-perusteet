# Miten kone kirjoittaa? — generatiivisen AI:n mekaniikka

## Johdanto

Kun käytät ChatGPT:tä, Copilotia tai muuta kielimalliin perustuvaa tekoälyä, vastaus voi näyttää hyvin älykkäältä. Mutta mitä taustalla oikeasti tapahtuu? Et näe siellä ajattelua tai ymmärtämistä ihmisen tapaan, vaan jotain muuta.

Taustalla on kielimalli, joka on opetettu valtavalla määrällä tekstiä. Se ei ajattele kuten ihminen, vaan toimii matemaattisesti ennustamalla, mikä sana tai ilmaus sopii seuraavaksi parhaiten. Kun ymmärrät tämän, ymmärrät myös paremmin sekä mallin voiman että sen rajat.

Tämän tunnin jälkeen sinulla on tuomaripöydällesi kolmas todistusaineisto: vaikka tekoäly näyttää älykkäältä, sen perusta on mekaaninen — se ei ajattele, se ennustaa.

## Tokenit — sanat jaetaan pieniksi palasiksi

Kun ChatGPT tai muu kielimalli lukee tekstiä, se ei käsittele sitä varsinaisesti sanoina, vaan *tokeneina* eli pieninä tekstin palasina.

Joskus yksi sana vastaa yhtä tokenia. Näin voi olla esimerkiksi sanoissa ”tekoäly” tai ”koulu”. Pidemmät tai harvinaisemmat sanat voivat kuitenkin jakautua useaan tokeniin. Esimerkiksi sana ”kielentutkimusopiskelijat” voi pilkkoutua useiksi osiksi. Tämä riippuu siitä, miten tokenisaattori on suunniteltu ja opetettu.

Miksi? Koska mallia opetettaessa se oppii, mitkä yhdistelmät ovat hyödyllisiä. Yleiset sanat tai sananosat muodostavat yhden tokenin. Harvinaiset sanat jaetaan pienempiin palasiin.

> **Pysähdy hetkeksi:** Miksi pienempi tokenisarja voisi olla parempi kielimallille kuin pitkät sanat?

ChatGPT:n kaltaiselle mallille "tekoäly" on noin 1–2 tokenia. "Kielentutkimusopiskelijat" saattaa olla 4–5 tokenia. Malli "näkee" tekstin tokeneina, ei kirjaimina tai sanoina.

## Parametrit — miljardeja numeroita

Kielimallissa on *parametreja* — numeroita, jotka se on oppinut koulutuksen aikana. Alkuperäisessä vuonna 2022 julkaistussa ChatGPT-3:ssa oli noin 175 miljardia parametria. Nykyisissä malleissa on moninkertaisesti enemmän. Lukumäärä on niin valtava, että sitä on tavallisen ihmisen mahdotonta ymmärtää. Onneksi nämä ovat vain numeroita — painoja.

Ajattele asiaa näin: jos käytössäsi olisi 175 miljardia säädettävää lukuarvoa, voisiko niistä muodostua järjestelmä, joka näyttää ymmärtävän tekstiä? Kyllä voisi. Siitä tässä on pohjimmiltaan kyse. Parametrit ovat mallin eräänlaisia ”aivoja” — eivät ihmisaivojen kaltaisia, vaan matemaattisia painoja, jotka ohjaavat sitä, miten malli käsittelee tekstiä.

Nämä parametrit opitaan koulutuksen aikana. Malli käy läpi valtavan määrän tekstiesimerkkejä ja säätää parametrejaan vähitellen niin, että sen ennusteet paranevat. Käytännössä malli oppii, millaiset parametriarvot auttavat sitä ennustamaan tekstiä yhä tarkemmin. Lopulta, miljardien säätöjen jälkeen, se pystyy arvioimaan varsin hyvin, mikä sana tai tokeni todennäköisimmin tulee seuraavaksi.

## Next-token prediction — arvaa seuraava sana

Tämä on kielimallin perusmekanismi: next-token prediction (seuraavan sanan ennustus).

Kun annat ChatGPT:lle kysymyksen "Mikä on Suomen pääkaupunki", malli näkee:
- Tokeni: "Mikä"
- Tokeni: "on"
- Tokeni: "Suomen"
- Tokeni: "pääkaupunki"

Sitten parametrien perusteella se sanoo: "Seuraava sana on todennäköisesti 'Helsinki'." Se valitsee sen ja tuottaa sen.

Sitten seuraavaksi:
- Tokeni: "Mikä"
- Tokeni: "on"
- Tokeni: "Suomen"
- Tokeni: "pääkaupunki"
- Tokeni: "Helsinki" (malli valitsi tämän)

Tämä jatkuu, kunnes malli päättää, että vastaus on valmis, tai kunnes pituusraja tulee vastaan.

Tässä on avainasia: malli ei kirjoita "vastausta". Se valitsee *seuraavaa sanaa, sana kerrallaan* parametrien ja koulutuksessa näkemänsä datan perusteella. Siksi se näyttää älykkäältä — koska koulutusdata sisälsi älykästä tekstiä. Mutta se ei "ajattele". Se ennustaa.

> **Pysähdy hetkeksi:** Jos malli vain arvaa seuraavaa sanaa todennäköisyyden perusteella, miten se voi antaa oikeita vastauksia monimutkaisiin kysymyksiin?

## Koulutusdata — se, minkä malli näkee

Parametrit opitaan koulutusdatasta. Nykyiset kielimallit on koulutettu valtavilla tekstimäärillä, jotka on kerätty esimerkiksi kirjoista, artikkeleista, verkkosivuilta, koodista ja internetin keskusteluista. Varhaisetkin suuret kielimallit opetettiin jo biljoonilla (biljoona = miljoona miljoonaa) tokeneilla.

Mitä malli oppii tästä aineistosta? Se oppii tilastollisia yhteyksiä ja toistuvia kuvioita. Se voi esimerkiksi oppia, että sanat ”koodaus” ja ”Python” esiintyvät usein yhdessä, että merkkijonon ”2 + 2” jälkeen tulee usein ”= 4” tai että kysymyksen jälkeen seuraa yleensä vastaus.

Tärkeää kuitenkin on, ettei malli ymmärrä asioita samalla tavalla kuin ihminen. Se ei tiedä, miksi 2 + 2 = 4 on totta. Se on vain oppinut, että tämä yhdistelmä esiintyy aineistossa hyvin usein ja on siksi todennäköinen.

Tästä seuraa myös rajoituksia. Jos koulutusdata sisältää virheitä tai vinoumia, malli voi oppia niitäkin. Jos taas jokin aihe puuttuu datasta kokonaan tai lähes kokonaan, malli ei pysty hallitsemaan sitä hyvin.

## Hallusinaatio — kun malli valehtelee (tai *näyttää* valehtelevan)

*Hallusinaatiolla* tarkoitetaan tilannetta, jossa kielimalli tuottaa vastauksen, joka vaikuttaa uskottavalta mutta on todellisuudessa väärä.

Esimerkiksi mallilta voidaan kysyä: ”Kuka kirjoitti romaanin ‘Suuri Mahtava’?” Malli saattaa vastata: ”Jane Austen kirjoitti teoksen ‘Suuri Mahtava’ vuonna 1847.” Vastaus kuulostaa uskottavalta, mutta se on virheellinen. Jane Austen ei ole kirjoittanut tämännimistä teosta. Vastaus näyttää oikealta siksi, että malli on oppinut, että kirjailijan nimi, teoksen nimi ja vuosiluku esiintyvät usein samankaltaisissa yhteyksissä.

Tätä kutsutaan hallusinaatioksi. Malli ei valehtele tietoisesti, koska se ei ymmärrä totuutta tai valhetta ihmisen tavoin. Se ennustaa vain, mikä ilmaus vaikuttaa todennäköiseltä seuraavaksi. Joskus tämä ennuste osuu väärin, vaikka lopputulos kuulostaisi hyvin vakuuttavalta.

## Lämpötila — kontrolli satunnaisuudelle

Kielimalli ei aina valitse kaikkein *todennäköisintä* seuraavaa sanaa. Joskus se voi valita myös hieman epätodennäköisemmän vaihtoehdon, jotta vastaus olisi monipuolisempi tai luovempi.

Tähän vaikuttaa asetus, jota kutsutaan lämpötilaksi.

- **Matala lämpötila:** malli valitsee yleensä kaikkein todennäköisimmän sanan. Vastaukset ovat tasaisempia ja johdonmukaisempia.

- **Korkea lämpötila:** malli sallii enemmän vaihtelua ja voi valita myös epätodennäköisempiä sanoja. Tällöin vastaukset voivat olla luovempia, mutta myös satunnaisempia.

Käyttäjä ei tavallisesti säädä tätä itse, mutta asetus vaikuttaa silti mallin toimintaan. Siksi samaan kysymykseen voi joskus saada hieman erilaisen vastauksen eri kerroilla.

## Kuva-, musiikki- ja videomallitkin

Kielimallien taustalla oleva ajatus, eli seuraavan yksikön ennustaminen, ei rajoitu vain tekstiin. Samaa periaatetta voidaan soveltaa myös kuviin ja musiikkiin.

- **Kuvamallit** ennustavat, millaisia visuaalisia piirteitä kuvaan kannattaa muodostaa seuraavaksi.
- **Musiikkimallit** ennustavat, millainen ääni, sävel tai rytminen elementti sopii jatkoksi.

Periaate pysyy samana, vaikka sisältö muuttuu. Malli tuottaa lopputulosta vaiheittain aiemmin muodostuneen sisällön perusteella. Erona on vain se, käsitelläänkö tekstin sijaan kuvaa vai ääntä.

## Yhteenveto

Generatiivinen tekoäly ei ajattele tai ymmärrä ihmisen tavoin. Se toimii näin:

- Se pilkkoo tekstin tokeneiksi.
- Se käyttää koulutuksessa opittuja parametreja.
- Se ennustaa seuraavan tokenin todennäköisyyksien perusteella.
- Se jatkaa tätä, kunnes vastaus on valmis.

Siksi lopputulos voi näyttää älykkäältä, vaikka taustalla on ennen kaikkea matemaattinen ennustaminen. Mallin vahvuus tulee siitä, että se on oppinut valtavasta määrästä ihmisten tuottamaa aineistoa. Ammattilaiselle tämän ymmärtäminen on tärkeää, koska juuri silloin hahmottaa sekä tekoälyn hyödyt että sen rajoitukset.

Seuraavalla tunnilla opit ymmärtämään, että vastaus riippuu suuresti siitä, mitä ja miten kysyt — konteksti ratkaisee kaiken.