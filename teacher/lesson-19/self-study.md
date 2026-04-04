# Mikä agentti on – ja mitä se ei ole?

## Johdanto

Kun puhutaan tekoälystä ja automatisoinnista, sana "agentti" (agent) leijuu kaikkialla. Kuulet sitä tekniikkauutisissa, startup-puffissa, opettajilta. Mutta harvoin kukaan selittää, mitä se oikeastaan tarkoittaa. Eikä se ole sama kuin chatbot, ei ole myöskään sama kuin automaattinen sähköpostin lajittelija tai yksinkertainen ohjelma.

Kuvitellaan, että sait tehtäväksi ratkaista ongelman: avaa sähköpostisovelluksesi, etsi kaikki viestit, joissa on sana "lasku", siirtä ne kansioon "Laskut" ja lähetä lähettäjälle automaattinen vastaus, jossa ilmoitat, että lasku on vastaanotettu. Seuraavat 10 vuotta, joka päivä, joka tunti. Kuka tahansa voisi tehdä tämän kerran — mutta jokainen kerta uudelleen? Se on rasittavaa.

Tässä tilanteessa agentti voisi ottaa tämän kokonaan pois käsistäsi. Se voisi tehdä kaiken itsenäisesti. Mutta miten se eroaa muista automaatioratkaisuista? Entä mikä tekee agentista agentin?

Pysähdy hetkeksi: Ajattele omaa päivääsi. Mitä toistuvia tehtäviä teet, jotka ovat yksinkertaisia mutta hankalia?

## Agentti on järjestelmä, joka päättää itse

Ensimmäinen, tärkein juttu: agentti on automatisoitu järjestelmä, joka tekee **useita vaiheita itsenäisesti** saavuttaakseen tietyn tavoitteen. Se ei vain suorita yhtä käskyä. Se ei vain seuraa listaa ohjeista riippumatta siitä, mitä tapahtuu. Se ajattelee.

Kun sähköpostisovelluksesi joka aamu käy läpi uudet viestit ja siirtää laskut automaattisesti, se ei ole agentti — se on **skripti** (script), yksinkertainen ohjelma, joka tekee aina saman asian samalla tavalla. Jos viesti on koodattu hieman eri tavalla, skripti sekoaa.

Agentti on eri tarina. Agentti näkee uuden sähköpostin. Se analysoivat sisällön. Se päättää: "Tämä näyttää laskuilta. Mikä on paras kansiota tälle?" Se tarkistaa vastaanottajan tietokannan. Se hahmottaa, että "Liisa Lindström" on toistaisesti lähettänyt laskuja, joten vastaus voidaan lähettää hänelle. Se lähetetään. Se kirjaa tehdyn toiminnon. Jos jokin meni pieleen — vaikkapa sähköpostiosoite oli virheellinen — agentti voi kertoa siitä ja kysy, mitä pitäisi tehdä seuraavaksi.

Agentti = tavoite + logiikka + toiminnot + palautesilmukka.

Pysähdy hetkeksi: Mitä eroa on siinä, että ohjelma tekee aina samaa vai että se ajattelee ja muuttaa toimintaansa tilanteen perusteella?

## Chatbot ei ole agentti

Chatbot on ohjelma, joka vastaa sinulle kirjoittamasi viesteihin. Se voi kuulostaa älykkäältä — varsinkin modernit chatbotit, kuten ChatGPT, ovat todella hyviä yhteydenpitoon. Mutta chatbot on passiivinen. Se odottaa, että sinä kirjoitat jotain. Se vastaa. Se odottaa uudelleen.

Agentti on aktiivinen. Se tarkkailee taustalla. Se toimii ilman, että sinun pitäisi sanoa sille mitään.

Kun otat yhteyttä ChatGPT:hen ja sanot "Anna minulle ohje pizzan tekemiseen", ChatGPT vastaa. Se on chatbot. Kun agentti huomaa, että ovellasi on säilöltään vanhentuneita ruoka-aineita ja päättää lähettää sinulle reseptit, jotka käyttävät niitä — se on agentti.

## Skripti, työnkulku, agentti — kolme eri tasoa

Yritysmaailmassa käytettävät järjestelmät putoavat kolmeen pääkategoriaan. On tärkeää osata erottaa ne.

**Skripti** on ohjelma, joka tekee täsmälleen mitä sinä sanot, riippumatta seurauksista. Se on automatisointi, mutta hyvin yksinkertainen. Esimerkki: "Poista kaikki tiedostot, joiden nimi alkaa sanalla 'temp_'." Skripti ei mieti. Se tekee.

**Työnkulku** (workflow) on sarja vaiheita, joita ohjataan säännöillä ja päätöksillä — mutta nämä säännöt on koodattu etukäteen. Voit tehdä työnkulun, joka sanoo: "Jos sähköposti sisältää sanan 'lasku', siirrä se kansioon A. Jos se sisältää sanan 'raportti', siirrä se kansioon B. Muuten, jätä se saapuneisiin." Tämä on älykkäämpää kuin skripti, koska siinä on päätöslogiikkaa. Mutta työnkulku on silti staattinen — sinä kirjoitat säännöt, ja ne eivät muutu.

**Agentti** on seuraava taso. Agentti näkee datan, muodostaa päätöksiä tuon datan perusteella, toimii ja seuraa tuloksia. Jos tulos ei ole odotettava, se oppii siitä ja muuttaa seuraavaa toimintaansa. Se voi myös tehdä jokapäiväisiä päätöksiä siitä, mitä tavoitteita se prioritisoi — näet vain lopputuloksen.

Tavallisesti IT-ympäristössä:
- Skripti lajittelee tiedostot koon mukaan.
- Työnkulku lajittelee tiedostot koon ja tyypin mukaan sääntöjen perusteella.
- Agentti lajittelee tiedostot miettimällä, mitä käyttäjä tulevaisuudessa halunnee.

## Rakenne näkyviin: trigger, logiikka, toiminnot, palaute

Jokaisen agentin taakse on rakenne. Se auttaa ymmärtämään, mitä tapahtuu sisällä.

1. **Trigger** (käynnistin): Mikä saa agentin liikkeelle? Uusi sähköposti? Tietty kello? Käyttäjän klikkaus?
2. **Logiikka**: Agentti analysoi tilannetta. Mitä tietoja sillä on? Mitä se voisi tehdä?
3. **Toiminnot**: Agentti tekee jotain. Se lähettää viestin. Se muuttaa tietokantaa. Se kutsuu toista ohjelmaa.
4. **Palautesilmukka** (feedback loop): Agentti näkee, mitä tapahtui. Onnistuiko se? Mitä pitäisi oppia seuraavaksi?

Oikeiden yritysten esimerkit:

**Esimerkki 1: Sähköpostin automaattinen luokittelu ja vastaus**
- Trigger: Uusi sähköposti saapuu.
- Logiikka: Agentti lukee viestin. Tunnistaa, että se on asiakastuki-kysymys.
- Toiminnot: Agentti lähettää viestin asiakastuen jonoon ja lähettää lähettäjälle automaattisen kuittauksen.
- Palaute: Agentti näkee, että kuittaus lähetettiin onnistuneesti. Se dokumentoi sen.

**Esimerkki 2: Tikettijärjestelmän automaatio**
- Trigger: Uusi IT-tukipyyntö luodaan.
- Logiikka: Agentti arvioi, kuinka kiireellinen se on. Katsoo varastosta, onko ratkaisu olemassa.
- Toiminnot: Jos ratkaisu on olemassa, agentti lähettää sen. Jos ei, se ohjaa tiketin oikealle tekijälle ja asettaa prioriteetin.
- Palaute: Agentti näkee, ratkaisiko se ongelman vai ei. Jos asiakastuki vastaa "Kiitos, se auttoi", agentti oppii, että tämä ratkaisu sopii tämäntyyppisiin tilanteisiin.

Pysähdy hetkeksi: Mitkä neljä osaa (trigger, logiikka, toiminnot, palaute) näet omissa päivittäisissä tehtävissäsi?

## Yhteenveto

Agentti on automatisoitu järjestelmä, joka tekee useita vaiheita itsenäisesti saavuttaakseen tavoitteen. Se eroaa chatbotista (joka odottaa sinua), skriptistä (joka tekee aina samaa) ja yksinkertaisesta työnkulusta (joka seuraa etukäteen kirjoitettuja sääntöjä). Agentin takaa löytyy neljä rakennuspalikkia: käynnistin, logiikka, toiminnot ja palautesilmukka. Kun ymmärrät nämä osat, ymmärrät, miksi agentti on potentialisesti hyödyllinen — mutta myös miksi se on riskialttiimpi ja kalliimpi kuin yksinkertainen automatisointi.
