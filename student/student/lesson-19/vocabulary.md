# Sanasto – Lesson 19

## Agentti (agent)
Automatisoitu järjestelmä, joka tekee useita vaiheita itsenäisesti saavuttaakseen tietyn tavoitteen. Se analysoi tilanteen, tekee päätöksiä ja toimii ilman ihmisen jatkuvaa ohjausta. Agentti koostuu kuudesta keskeisestä komponentista, jotka työskentelevät yhdessä, jotta se toimisi tehokkaasti ja johdonmukaisesti.

## Chatbot
Ohjelma, joka vastaa käyttäjän kirjoittamiin viesteihin. Chatbot on passiivinen — se odottaa sinua — eikä tee päätöksiä itsenäisesti. Chatbot poikkeaa agentista siinä, että se ei toimi autonomisesti ilman käyttäjän käskyä.

## Skripti (script)
Yksinkertainen ohjelma, joka tekee aina saman asian samalla tavalla. Se ei mieti tai muuta toimintaansa tilanteen perusteella.

## Työnkulku (workflow)
Sarja vaiheita, joita ohjataan etukäteen kirjoitetuilla säännöillä ja päätöksillä. Työnkulku on älykkäämpi kuin skripti, mutta staattisempi kuin agentti.

## Autonomia (autonomy)
Kyky tehdä päätöksiä ja toimia itsenäisesti ilman jatkuvaa ulkoista ohjausta. Agentti voi muuttaa toimintaansa tilanteen perusteella ja valita eri reittejä tavoitteen saavuttamiseksi.

## Syötekäsittelijä (input handler)
Agentin silmät ja korvat. Se vastaanottaa herätteitä käyttäjältä tai ympäristöstä, muuttaa ne järjestelmän ymmärtämään muotoon ja välittää ne päättelykomponentille.

## Päättelijä (reasoner/planner)
Agentin aivot. Se analysoi tilanteen, selvittää tavoitteen, pohtii mahdollisia ratkaisuja ja tekee suunnitelman siitä, kuinka edetä. Päättelijä käyttää logiikkaa ja tietoa tehdäkseen fiksuja päätöksiä.

## Työkalujen suorittaja (tool executor)
Agentin kädet. Se kutsuu rajapintoja (API:ita) ja suorittaa konkreettisia toimintoja, kuten sähköpostien lähettämistä, tietokantojen päivittämistä tai muiden ohjelmien kutsumista. Suorittaja toteuttaa päättelykomponentin tekemät päätökset.

## Muisti ja konteksti (memory and context)
Agentin muistijärjestelmä, joka koostuu kahdesta osasta: lyhytkestoisesta muistista (nykyisen keskustelun konteksti-ikkunasta) ja pitkäkestoisesta muistista (tietokannasta tai lokista aiemmista tapahtumista). Muisti auttaa agenttia oppimaan ja tekemään parempia päätöksiä.

## Konteksti-ikkuna (context window)
Agentin lyhytkestoinen muisti, joka sisältää nykyisen keskustelun ja viimeaikaiset tapahtumat. Se auttaa agenttia muistamaan, mitä on tapahtunut juuri nyt, mutta se ei ole pysyvä — vanhemmat tiedot häviävät, kun uutta tietoa tulee.

## Turvakerros (safety layer)
Komponentti, joka tarkistaa agentin tekemiä päätöksiä ja toimintoja. Se varmistaa, että agentti noudattaa sääntöjä ja normeja ennen toimintoa, sen aikana ja sen jälkeen. Turvakerros suojaa käyttäjiä ja järjestelmää virheiltä ja väärinkäytöksiltä.

## Palautesilmukka (feedback loop)
Prosessi, jossa agentti näkee, mitä sen toiminnon jälkeen tapahtui, ja oppii siitä. Se auttaa agenttia parantamaan tuloksiaan seuraavalla kerralla. Palaute voi tulla käyttäjältä, järjestelmältä tai ympäristöstä.

## Suoritusputki (pipeline)
Järjestys, jossa agentin komponentit toimivat yhdessä. Syötekäsittelijä saa viestin, päättelijä analysoi sen, työkalujen suorittaja tekee toiminnon, turvakerros tarkistaa, muisti tallentaa ja palautesilmukka oppii tuloksesta. Pipeline varmistaa, että kaikki komponentit toimivat oikeassa järjestyksessä.

## Reititys (routing)
Agentin päätös siitä, mitä polkua tai strategiaa se käyttää tehtävän ratkaisemiseksi. Agentti valitsee reitin tavoitteen, tilanteen ja käytettävissä olevien resurssien perusteella.

## Työkalureititys (tool routing)
Agentin prosessi oikean työkalun valitsemiseksi kuhunkin tilanteeseen. Jos agentti joutuu kirjoittamaan sähköpostia, se valitsee sähköpostin lähettämisen työkalun. Jos se tarvitsee tietoa tietokannasta, se valitsee tietokantakyselyn työkalun.