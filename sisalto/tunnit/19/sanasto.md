# Sanasto – oppitunti 19

## Agentti (agent)

Tällä kurssilla agentti tarkoittaa kielimallin ja harnessin muodostamaa järjestelmää. Kielimalli tulkitsee tilannetta, ja harness välittää syötteet, työkalut, tehtävän tilan, oikeudet ja turvarajat. Kurssin kuusi kohtaa ovat suunnittelutarkistuslista, eivät jokaisen agentin pakolliset tekniset osat.

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

Tehtävän nykyinen tila voi olla keskustelun konteksti-ikkunassa tai harnessin muussa tilanhallinnassa. Pitkäkestoinen muisti tarkoittaa esimerkiksi tietokantaan tai lokiin tallennettua aiempaa tietoa, ja se lisätään vain silloin, kun myöhempi suoritus todella tarvitsee sitä. Muisti ei tarkoita, että malli oppisi automaattisesti.

## Konteksti-ikkuna (context window)

Agentin lyhytkestoinen muisti, joka sisältää nykyisen keskustelun ja viimeaikaiset tapahtumat. Se auttaa agenttia muistamaan, mitä on tapahtunut juuri nyt, mutta se ei ole pysyvä — vanhemmat tiedot häviävät, kun uutta tietoa tulee.

## Turvakerros (safety layer)

Komponentti, joka tarkistaa agentin tekemiä päätöksiä ja toimintoja. Se varmistaa, että agentti noudattaa sääntöjä ja normeja ennen toimintoa, sen aikana ja sen jälkeen. Turvakerros suojaa käyttäjiä ja järjestelmää virheiltä ja väärinkäytöksiltä.

## Palautesilmukka (feedback loop)

Valinnainen prosessi, jossa toiminnan tuloksia seurataan ja toteutusta kehitetään. Palaute voi tulla käyttäjältä, järjestelmältä, testistä tai ympäristöstä. Palautesilmukka voi olla ihmisen tekemä katselmointi eikä tarkoita automaattista oppimista.

## Suoritusputki (pipeline)

Yhden toteutuksen tapa järjestää syötteet, kielimallin päättely, työkalukutsut, turvarajat ja tulosten käsittely. Suoritusputkia voi olla erilaisia. Pitkäkestoinen muisti ja palautteesta oppiminen eivät ole jokaisessa putkessa pakollisia.

## Reititys (routing)

Agentin päätös siitä, mitä polkua tai strategiaa se käyttää tehtävän ratkaisemiseksi. Agentti valitsee reitin tavoitteen, tilanteen ja käytettävissä olevien resurssien perusteella.

## Työkalureititys (tool routing)

Agentin prosessi oikean työkalun valitsemiseksi kuhunkin tilanteeseen. Jos agentti joutuu kirjoittamaan sähköpostia, se valitsee sähköpostin lähettämisen työkalun. Jos se tarvitsee tietoa tietokannasta, se valitsee tietokantakyselyn työkalun.

## Valmisagentti (ready-made agent)

Valmiiksi rakennettu agenttituote, jossa joku muu on toteuttanut kielimallia ympäröivän harnessin. Tuotetta voi arvioida kurssin kuuden kohdan tarkistuslistalla, vaikka toteutus ei jakautuisi kuuteen erilliseen osaan.

## Agenttitila (agent mode)

Sovelluksen toimintatila, jossa tekoäly ei vain vastaa viesteihin, vaan suorittaa monivaiheisia tehtäviä työkaluilla käyttäjän puolesta.

## Harness

Kielimallin ympärille rakennettu kokonaisuus: työkalut, muisti, oikeudet ja turvarajat. Agentti = kielimalli + harness. Englannin sana harness tarkoittaa valjaita.

---
