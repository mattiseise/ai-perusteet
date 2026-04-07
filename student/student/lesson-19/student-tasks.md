# Opiskelutehtävät: Mikä agentti on — ja mitä se ei ole?

## Projektin aihio 1: Valitse agenttiongelmasi

Tämä on ensimmäinen viidestä projektin aihiosta, jotka keräät Agentit-osion aikana. Käytät näitä aihioita oppitunneilla 26–27, kun rakennat oman n8n-agenttityönkulun ja esittelet sen. Säilytä tämä huolellisesti.

### Tehtävä

Valitse ongelma, jonka haluaisit ratkaista agentilla. Kirjoita lyhyt kuvaus (150–200 sanaa), jossa vastaat kolmeen kysymykseen: Mikä ongelma on kyseessä ja kenelle se on tarkoitettu? Miksi juuri agentti sopii tähän ongelmaan — eikö tavallinen automaatio tai chatbot riittäisi? Mitkä kuusikomponenttisen mallin osat (syötekäsittelijä, päättelijä, työkalut, muisti, turvakerros, palautesilmukka) ovat tässä ongelmassa kriittisimpiä?

Ongelman ei tarvitse olla monimutkainen. Hyvä lähtökohta voi olla esimerkiksi "sähköpostiviestien luokittelu ja yhteenveto joka aamu" tai "asiakaspalvelun FAQ-botti, joka osaa hakea vastauksia tietokannasta". Tärkeintä on, että ongelma on sellainen, jonka voi toteuttaa 3–5 solmun n8n-työnkulkuna koulun palvelimella, jossa on käytössä paikallinen Qwen-kielimalli ja M365-integraatiot.

### Miksi tämä on tärkeä

Oppitunneilla 26–27 rakennat oman n8n-agenttityönkulun. Tämä aihio on sen pohja — kun sinulla on selkeä ongelma ja käyttäjä, kaikki myöhemmät suunnittelupäätökset (muisti, päättelymalli, turvakerros, ihmisen rooli) liittyvät konkreettiseen projektiin. Ilman selkeää ongelmaa suunnittelu jää abstraktiksi.

Alla olevat harjoitustehtävät auttavat sinua ymmärtämään, mitä agentit ovat ja miten ne eroavat yksinkertaisemmista järjestelmistä. Nämä havainnot auttavat sinua perustelemaan, miksi valitsemasi ongelma tarvitsee juuri agentin.

---

## Tehtävä 19.1: Luokittele järjestelmät

### Tavoite
Ymmärtää, mikä erottaa agentin chatbotista ja tavallisesta ohjelmasta. Tämän tehtävän opit auttavat sinua projektin aihiossa perustelemaan, miksi valitsemasi ongelma tarvitsee nimenomaan agentin.

### Ohjeet

Alla on kolme järjestelmän kuvausta. Jokaisen kohdalla sinun täytyy tunnistaa, onko kyseessä chatbot, agentti vai ei kumpikaan, ja perustella valintasi käyttäen kuuden komponentin agenttimallia (syötekäsittelijä, päättelijä, työkalut, muisti, turvakerros, palautesilmukka).

**Järjestelmä A: Asiakaspalvelun chatbotti**

Asiakkaat voivat kirjoittaa kysymyksiään verkkosivuston chat-ikkunaan. Järjestelmä analysoi kysymyksen ja etsii FAQ-tietokannasta sopivinta vastausta. Jos varmuusprosentti on korkea, se näyttää asiakkaalle vastauksen. Jos varmuusprosentti on matala, se ilmoittaa asiakkaalle, että ihmisen palvelutiimi ottaa yhteyttä.

**Järjestelmä B: Automaattinen palvelimen valvonta**

Palvelimen valvonta-agentti seuraa jatkuvasti palvelimen CPU-kuormaa, muistinkäyttöä ja verkkoliikennevirtaa. Kun CPU-kuorma nousee yli 80 prosenttiin kahden minuutin ajan, agentti käynnistää automaattisesti uuden palvelininstanssin ja ohjaa liikennettä sille. Agentti lähettää myös ilmoituksen IT-tiimille ja dokumentoi tapahtumat. Seuraavan tunnin jälkeen, jos kuorma on laskenut normaaliksi, agentti sulkee ylimääräisen instanssin.

**Järjestelmä C: Kuvankäsittelyohjelma**

Kun käyttäjä lataa kuvan, ohjelma tunnistaa automaattisesti kuvan objektit ja lisää kuvailevat tagit metadataan. Ohjelma analysoi myös kuvan kirkkautta ja säätää sitä automaattisesti sopivammaksi. Ohjelma ei itse päätä, mitä kuvia käyttäjä haluaa käsitellä — se vain käsittelee jokaisen kuvan, joka sille annetaan, samalla logiikalla.

Täytä jokaisen järjestelmän kohdalle valintasi (chatbot, agentti tai ei kumpikaan) ja perustelu 2–3 lauseella. Käytä termejä reaktiivinen, proaktiivinen, autonominen, tavoite ja päätöksenteko sekä viittaa vähintään kahteen kuusikomponenttisen mallin osaan.

---

## Tehtävä 19.2: Suoritusputki — pyyntö läpi agentin komponenttien

### Tavoite
Ymmärtää, miten agentin kuusi komponenttia toimivat yhdessä ketjuna. Tämä auttaa sinua projektin aihiossa hahmottamaan, mitkä komponentit ovat omassa ongelmassasi kriittisimpiä.

### Ohjeet

Asiakas lähettää seuraavan viestin verkkokaupan asiakaspalveluagentille:

> "Tilaamani tuote tuli viallisena. Numerona tilauksen tunnus on #42891. Haluaisin joko uuden tuotteen tai rahat takaisin."

Jäljitä pyyntö kaikkien kuuden komponentin läpi ja selitä, mitä tapahtuu jokaisessa vaiheessa. Kirjoita lyhyt selvitys (noin 300 sanaa tai taulukko), jossa käyt läpi syötekäsittelijän, muistin, turvakerroksen, päättelijän, työkalut ja palautesilmukan roolit tässä tilanteessa.

Voit vastata joko taulukkona (jokainen rivi on yksi komponentti ja sen rooli) tai narratiivina (kuvaat putken prosessina, jossa jokainen komponentti rakentuu edellisen päälle).

---

## Tehtävä 19.3: Heikoin lenkki — analyysi agenttijärjestelmästä

### Tavoite
Oppia tunnistamaan, mikä agentin komponentti on kriittisin ja mitä seurauksia sen epäonnistumisella olisi. Tämä auttaa sinua projektin aihiossa tunnistamaan oman agenttisi riskikohdat.

### Ohjeet

Valitse jokin seuraavista agenttiskenaarioista:

**A)** Lentokenttä-agentti, joka ohjaa minirobotteja lentokentän lattialla varoittamaan matkailijoita vaaroista ja esineistä

**B)** Sijoitusneuvonta-agentti, joka analysoi osakemarkkinoita ja ehdottaa sijoituspäätöksiä asiakkaille

**C)** Sairaalakeräys-agentti, joka sovittaa verenluovuttajat sairaalaan yhteydenottojen perusteella

Kirjoita lyhyt analyysi (150–200 sanaa), jossa tunnistat kriittisimmän komponentin kuuden komponentin mallista, selität mitä seurauksia sen epäonnistumisella olisi ja ehdotat, miten komponenttia voitaisiin vahvistaa. Ota huomioon sekä tekninen että eettinen näkökulma.
