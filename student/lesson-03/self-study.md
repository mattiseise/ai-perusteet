# Miten generatiivinen tekoäly toimii perustasolla

## Johdanto

Käytät ChatGPT:tä ja saat vastaukseen näytön täyden tekstiä. Se näyttää älykäältä — mutta mitä todella tapahtuu taustalla? Et ole koskaan nähnyt "ajattelua" tai "ymmärtämistä". Mitä oikeasti tapahtuu?

Tämä on kielimalli (language model). Se on nähnyt miljardeja sanoja, miljardeja tekstin kappaleita. Se ei "ajattele" kuten ihminen. Se tekee jotain, joka näyttää samankaltaiselta — mutta se on pohjimmiltaan matematiikkaa. Kun ymmärrät, miten tämä toimii, näet sekä sen voimat että rajoitukset.

## Tokenit — Sanat jaetaan pieniksi palasiksi

Kun ChatGPT lukee tekstiä, se ei lue "sanoja". Se lue *tokeneita* — pieniä palasia.

Esimerkiksi sana "tekoäly" saattaa olla yksi tokeni. Sana "koulu" saattaa olla yksi tokeni. Mutta sana "kielentutkimus" voisi olla kolme tokenia: "kieli", "en", "tutkimus". Tai kahta: "kieli", "tutkimus". Riippuu siitä, miten tokenisaattori on opittu.

Miksi? Koska mallia opittaessa se oppii, mitä yhdistelmät ovat hyödyllisiä. Yleiset sanat tai sanat-osat ovat yksi tokeni. Harvinaiset sanat jaetaan pieniksi palasiksi.

> **Pysähdy hetkeksi:** Miksi pienempi tokeni-sarja voisi olla parempi kielimallille kuin pitkät sanat?

ChatGPT:n kaltaiselle mallille "tekoäly" on noin 1-2 tokenia. "Kielentutkimusopiskelijat" saattaa olla 4-5 tokenia. Malli "näkee" tekstin tokeneina, ei kirjaimina tai sanaina.

## Parametrit — Miljardeja numeroita

Kielimallissa on parametreja — numeroita, joita se on oppinut koulutuksessa. ChatGPT-3:ssa on noin 175 miljardia parametria. GPT-4:ssä enemmän. Nämä ovat vain numeroita — painoja.

Ajattele näin: Jos sinulla olisi 175 miljardia numeroita, joita voisit säätää, voitko niillä luoda käyttäytymistä, joka näyttää ymmärtävän tekstiä? Kyllä. Se on tämä. Parametrit ovat "aivot" — ei aivoja kuten ihmisen, vaan matemaattisia painoja, jotka määrittävät, miten malli prosessoi tekstiä.

Nämä parametrit oppitään koulutuksesta. Malli näkee miljardeja tekstin esimerkkejä ja säätää parametreja: "Nämä parametrit tekevät parempia ennustuksia tästä textista." Lopussa — miljardeja säätöjä jälkeen — malli pystyy ennustamaan, mikä sana tulee seuraavaksi, melko hyvin.

## Next-Token Prediction — Arvaa seuraavaa sanaa

Tämä on kielimallin perusmekanismi: Next-token prediction (seuraavan sanan ennustus).

Kun annat ChatGPT:lle kysymyksen "Mikä on pääkaupunki", malli näkee:
- Tokeni: "Mikä"
- Tokeni: "on"
- Tokeni: "pääkaupunki"

Sitten parametrien perusteella se sanoo: "Seuraava sana on todennäköisesti 'Suomesta'." Se valitsee sen ja tuottaa sen.

Sitten seuraavaksi:
- Tokeni: "Mikä"
- Tokeni: "on"
- Tokeni: "pääkaupunki"
- Tokeni: "Suomesta" (malli valitsi tämän)

"Seuraava sana on todennäköisesti 'Helsinki'." Valitsee sen.

Tämä jatkuu, kunnes malli päättää, että vastaus on valmis tai saavuttaa pituusrajan.

Tässä avain: Malli ei kirjoita "vastaus". Se valitsee *seuraavaa sanaa, sanaa kerrallaan*, perustuen parametreihin ja dataan, jonka näki koulutuksessa. Siksi se näyttää älykäältä — koska koulutusdata sisälsi älykästä tekstiä. Mutta se ei "ajattele". Se ennustaa.

> **Pysähdy hetkeksi:** Jos malli vain arvaa seuraavaa sanaa todennäköisyyden perusteella, miten se voi antaa oikeita vastauksia monimutkaisiin kysymyksiin?

## Koulutusdata — Se mikä malli näkee

Parametrit tulevat koulutus-datasta. GPT-4 on opittu tekemällä (loukkaavasti arvioitu) noin 15 triljoona tokenia tekstistä — kirjat, artikkelit, koodia, keskusteluja internetistä.

Kun näistä 15 triljoona tokenista pois, mitä malli oppii? Se oppii tilastollisia kuvioita: "Sanojen 'koodaus' ja 'Python' näkyvät usein yhdessä." "Kun joku kirjoittaa '2 + 2', seuraavaksi voi tulla '='." "Kyshymyksen jälkeen tulee yleensä vastaus, ei uusi kysymys."

Mutta se ei ymmärrä *miksi*. Se ei tiedä, että 2 + 2 = 4 on matemaattinen totuus. Se vain näki tämän kombinaation miljardeja kertoja datassa ja "oppi", että se on tavallinen.

Tämän seurauksena malli tekee virheitä. Jos koulutusdata oli väärä tai harhainen, parametrit tulevat vääriltä. Jos tietty aihe puuttui datasta, malli ei osaa sitä.

## Hallusinaatio — Kun malli valehtelee (tai *näyttää* valehtelevan)

"Hallusinaatio" on termi, jota käytetään, kun kielimalli tuottaa jotain, joka näyttää oikealta, mutta on täysin väärää.

Esimerkiksi: "Kuka kirjoitti romaanin 'Suuri Mahtava'?" Malli vastaa: "Jane Austen kirjoitti 'Suuri Mahtava' vuonna 1847." Väärä. Jane Austenilla ei ole kirjoitusta tällä nimellä. Mutta vastaustapa näyttää oikealta, koska malli on nähnyt tekstissä "Jane Austen" ja "romaani" ja "vuosi" yhdessä niin monesti, että se arvaa yhteyttä, jota ei ole.

Tämä on hallusinaatio. Malli ei ole "valehdeleven" — se ei ymmärrä totuutta tai valheita. Se vain ennustaa, mikä sana tulee todennäköisesti seuraavaksi, ja joskus nämä ennustukset ovat vaarallisesti väärillä.

## Lämpötila — Kontrolli satunnaisuudelle

Kielimalli ei aina valitse *todennäköisintä* sanaa. Se voisi valita toisen, harvemmin todennäköisen sanan "luovuudelle" tai vaihtelulle.

Tämä kontrolloidaan parametrilla, jota kutsutaan "lämpötilaksi" (temperature):
- Matala lämpötila = Valitse lähes aina todennäköisin sana. Vastaukset ovat konsistenteja.
- Korkea lämpötila = Valitse myös epätodennäköisiä sanoja. Vastaukset ovat satunnaisempia ja luovempia.

Käyttäjänä et yleensä säädä tätä, mutta se on olemassa. Siksi ChatGPT:tä pyydetään kahta kertaa, vastaukset voivat olla hieman erilaisia — jos lämpötila sallii vaihtelua.

## Kuva-, musiikki- ja videomallitkin

Kielimallien periaate (next-token prediction) toimii myös kuville ja musiikille:
- Kuvamallit (Dall-E) ennustavat: "Mikä on seuraava piksel?" Pikselillä kerrallaan.
- Musiikkimodelu (Suno) ennustaa: "Mikä on seuraava nuotti tai ääni?"

Periaate on sama — vain input ja output ovat erilaisia (tokenit voivat olla pikselejä tai ääntöä).

## Yhteenveto

Generatiivinen tekoäly ei "ajattele", "ymmärrä" tai "luo". Se:
1. Näkee tekstin tokeneina (pienissä palasissa).
2. Käyttää miljardeja parametreja (numeroita), joita se oppi datasta.
3. Ennustaa seuraavaa tokenia todennäköisyyden perusteella.
4. Toistaa vaihe 3, kunnes vastaus on valmis.

Siksi se näyttää älykäältä — koska koulutusdata oli älykästä. Mutta mikä se oikeasti tekee on matemaattista ennustamista. Sinä, ammattilaisena, ymmärrät tämän ja näet sekä mahdollisuudet että rajat.
