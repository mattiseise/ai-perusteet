# Opettajavetoiset tehtävät — oppitunti 26

## Tehtävä 1: Sama päätös kahdella toteutuspolulla

Näytä luokalle kaksi turvallista esimerkkiviestiä. Toisesta puuttuu pakollinen tieto, toisessa tieto on mukana. Tee kielimallikutsu, jonka sallitut tulokset ovat `pyyda_lisatietoa` ja `jatka`. Näytä, että sama malli valitsee eri tilanteissa eri vaihtoehdon.

Esitä tulos ensin teknisenä n8n-suoritusjälkenä ja sitten dokumentoituna suoritusjälkenä. Tekninen näyttö kertoo, että reititys toimii käytetyssä ympäristössä. Dokumentoitu näyttö kertoo, miten suunniteltu reitti etenee, mutta simuloituja liitäntöjä ei väitetä toimiviksi.

## Tehtävä 2: Arkkitehtuurin vastuunjako

Piirrä taululle kielimalli ja sitä ympäröivä agentin ohjauskehys. Pyydä opiskelijoita sijoittamaan **syötekäsittelijä**, **päättelijä ja suunnittelija**, **työkalujen suorittaja**, **muisti ja konteksti**, **turvakerros** sekä **seuranta ja palautesilmukka** oikeaan vastuualueeseen. Korosta, että kuusi rakennusosaa ovat kattavuuden tarkistuslista. Ne eivät määrää solmujen tai vaiheiden määrää.

Kysy jokaisesta kohdasta, mitä tietoa se saa, mitä se tuottaa ja miten virhe näkyy. Kielimallin tehtävä on tehdä rajattu tilannearvio. Ohjauskehys tarkistaa syötteen, rajaa vaihtoehdot ja oikeudet, suorittaa työkalut sekä kirjaa tuloksen.

## Tehtävä 3: Toteutuspolun valinta

Opiskelija perustelee, valitseeko hän teknisen n8n-polun vai dokumentoidun suunnittelupolun. Perustelussa pitää nimetä, millä näytöllä hän osoittaa todellisen mallivalinnan, agentin ohjauskehyksen rajat ja yhden korjatun ongelman.

Muistuta, että dokumentoitu polku ei ole kevyt versio. Siinä tarvitaan todellinen kielimallikutsu, kaavio, työkalusopimukset, simuloidut suoritusjäljet ja teknisten rajoitusten arvio. Tekninen polku puolestaan tarvitsee toimivan työnkulun, suoritusnäkymän ja virhepolun.

## Tehtävä 4: Minimiversion klinikka

Opiskelija tekee turvallisella aineistolla kaksi testiä, joiden pitäisi johtaa eri sallittuun valintaan. Pari tarkistaa suoritusjäljestä syötteen, mallin valinnan, työkalun tuloksen tai simuloidun vastineen ja seuraavan vaiheen.

Jos molemmat tapaukset kulkevat aina samaa reittiä, kysy, tarvitaanko tehtävässä kielimallin tilannearviota vai riittäisikö tavallinen työnkulku. Jos valinta on perusteltu mutta suoritusjälki epäselvä, opiskelija korjaa dokumentointia. Jos valinta on väärä, hän tarkentaa järjestelmäpromptia tai sallittujen vaihtoehtojen ehtoja ja testaa uudelleen.

## Tehtävä 5: Tunnin lopun katselmus

Jokainen opiskelija näyttää yhden alkuperäisen testin, tehdyn korjauksen ja uudelleentestin. Tekninen polku näyttää tämän n8n:n suoritusnäkymästä. Dokumentoitu polku näyttää todellisen mallivalinnan ja sitä seuraavan päivitetyn simulaation.

Hyväksyttävä välituotos sisältää kootun suunnitelman, toteutuspolun valinnan, vähintään kaksi sallittua mallivaihtoehtoa, kaksi testijälkeä ja yhden korjatun ongelman. Lisäksi opiskelija nimeää yhden asian, jota hänen näyttönsä ei vielä todista.
