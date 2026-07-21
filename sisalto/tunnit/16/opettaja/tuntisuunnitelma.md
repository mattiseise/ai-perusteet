# Opettajan materiaalit — oppitunti 16: toteutustavan valinta ja erikoistyökalujen laboratorio

## Oppitunnin tarkoitus

Oppija tutkii neljää reittiä — kuvaa, ääntä tai musiikkia, videota ja koodia — ja kokeilee niistä yhtä samalla arviointisyklillä. Kokeilu ei jää irralliseksi tuotantolaboratorioksi, vaan johtaa oman apuri-botin toteutustapojen vertailuun sekä toteutus-, riski- ja käyttöönottopäätökseen.

Reitit ovat pedagogisesti samanarvoisia. Oppijaa ei ohjata kuvaan vain siksi, että se on opettajalle tai käytettävissä olevien palvelujen kannalta helpoin vaihtoehto. Arvioinnin kohteena on harkittu prosessi ja siitä syntyvä näyttö, ei tuotostyypin näyttävyys.

## Osaamistavoitteet

Oppija:

- valitsee tuotostyypin todellisen käyttötarkoituksen perusteella
- kirjoittaa valitulle muodolle sopivan syötteen
- päättää 3–5 havaittavaa arviointikriteeriä
- tuottaa tai analysoi kaksi versiota
- muuttaa yhtä asiaa ja arvioi sen vaikutusta
- tarkistaa oikeudet, turvallisuuden, harhaanjohtavuuden ja merkintätavan
- vertaa teknistä toteutuspolkua ja dokumentoitua suunnittelupolkua niiden omilla näytöillä
- nimeää suunnittelupolussa simuloiduiksi jäävät tekniset ominaisuudet

## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **yksi bottiprojektin valintakortti**. Sen sisällä näkyvät neljän työkalureitin tiivis vertailu, yhden reitin käytännön kokeilu, kahden botin toteutustavan vertailu sekä toteutus-, riski- ja käyttöönottopäätös. Erillistä laboratoriolokia ei vaadita. Tunnin alussa on tärkeää erottaa kriteeri mieltymyksestä.

| Aika | Vaihe | Opettajan tehtävä |
| --- | --- | --- |
| 0–10 min | Reittien esittely | Kuvaa neljä reittiä samoina oppimisvaihtoehtoina. Varmista saavutettava varareitti ilman tiliä. |
| 10–20 min | Tarkoitus ja kriteerit | Oppija määrittää käyttötarkoituksen ja 3–5 kriteeriä ennen tuottamista. |
| 20–40 min | Versio 1 | Oppija tuottaa ensimmäisen version tai arvioi opettajan esimerkin. |
| 40–55 min | Arviointi | Oppija nimeää havaittavan ongelman ja sitä vastaavan muutoksen. |
| 55–70 min | Versio 2 | Oppija muuttaa yhden asian ja tuottaa uuden version. |
| 70–80 min | Toteutustapojen vertailu | Oppija vertaa teknistä toteutusta ja dokumentoitua suunnittelua niiden omilla näytöillä. |
| 80–90 min | Päätös ja tallennus | Oppija kirjaa toteutus-, riski- ja käyttöönottopäätöksen. |

## Reittikohtainen vähimmäisohjaus

Alla oleva taulukko on opettajan nopea tarkistusväline. Sitä ei ole tarkoitettu tuoteluetteloksi eikä kaikille yhteiseksi sisältövaatimukseksi. Nosta kustakin reitistä esiin vain ne syötteen ja arvioinnin piirteet, joita oppijan valitsema käyttötarkoitus tarvitsee.

| Reitti | Syötteen ydin | Arvioinnin ydin |
| --- | --- | --- |
| Kuva | kohde, sommittelu, käyttötarkoitus, kuvasuhde, rajat | oikeellisuus, viesti, harhaanjohtamattomuus, saavutettavuus |
| Ääni tai musiikki | kesto, rakenne, tempo, äänimaailma, puhe | ymmärrettävyys, tasapaino, häiriöt, käyttöoikeus |
| Video | kuvakäsikirjoitus, kohtaukset, liike, ääni, tekstitys | jatkuvuus, viesti, liike, saavutettavuus |
| Koodi | toiminto, syöte, tulos, ympäristö, virheet, testit | testit, turvallisuus, luettavuus, pyytämättömät toiminnot |

## Läpi kulkeva mallinnus

Käytä koko tunnin ajan yhtä tapausta, jotta arviointisykli ei jää irrallisiksi työvaiheiksi. Kirjasto tarvitsee verkkosivulleen 20 sekunnin äänettömän opastusvideon kirjan palauttamisesta. Ennen tuottamista sovitaan, että kolme vaihetta näkyvät oikeassa järjestyksessä, tekstitykset ehtii lukea rauhassa, esineet ja tila säilyvät johdonmukaisina eikä kuvassa ole tunnistettavia asiakkaita.

Näytä version 1 puutteena toisen tekstityksen liian lyhyt lukuaika. Oppija ei saa korjata kaikkea samalla kertaa, vaan muuttaa vain toisen kohtauksen kestoa: se pidennetään seitsemään sekuntiin. Versiota 2 verrataan samoilla kriteereillä: tekstitys on nyt luettavissa ja muut vaatimukset täyttyvät edelleen. Vasta tämän jälkeen tehdään päätös. Video voidaan julkaista, jos aineiston käyttö on luvallista, ohjeen asiasisältö on tarkistettu ja tekoälyn osuus merkitään sovitulla tavalla; muuten se hylätään tai palautetaan korjattavaksi.

## Tyypilliset väärinkäsitykset

Näyttävyys sekoittuu helposti laatuun. Palauta arviointi silloin käyttötarkoitukseen: välittyykö oikea asia oikealle käyttäjälle suunnitellussa tilanteessa? Myös pitkä tai yksityiskohtainen prompti voi olla huono, jos sen yksityiskohdat eivät palvele tätä tavoitetta.

Koodireitillä sujuvan näköinen tuotos voi synnyttää perusteetonta luottamusta. Tekoälyn tuottama koodi on luettava ja testattava eristetyssä ympäristössä ennen käyttöä. Sama vastuu koskee muitakin reittejä: se, että palvelu tuotti sisällön, ei vielä ratkaise käyttö- tai julkaisuoikeutta.

Yksi onnistunut versio kertoo vain tästä kokeesta. Se ei osoita työkalun yleistä laatua eikä takaa, että sama syöte toimii seuraavalla kerralla. Siksi johtopäätös rajataan siihen, mitä ennen–jälkeen-vertailu todella näyttää.

## Eriyttäminen

**Tuetussa työskentelyssä** anna reittikohtainen syötepohja ja kaksi valmista versiota. Oppija tekee arvioinnin, nimeää muutoksen ja suorittaa vastuullisuustarkistuksen. Valmiit tuotokset vähentävät teknistä kuormaa, mutta niillä osoitetaan sama arviointitaito kuin itse tuotetuilla versioilla.

**Syventävällä reitillä** toinen arvioija käyttää samoja kriteerejä tietämättä ensin tekijän omaa johtopäätöstä. Oppija vertaa havaintojen eroja ja pohtii, ovatko kriteerit riittävän yksiselitteisiä. Syventävä työ ei kasvata pakollista ydintuotosta.

## Arvioitava näyttö

Hyväksyttävä valintakortti sisältää molemmat kokeiluversiot, ennalta nimetyt kriteerit, yhden muutoksen vaikutuksen ja vastuullisuustarkistuksen. Lisäksi siinä näkyvät kaksi toteutustapaa ja perusteltu valinta. Teknisen polun näyttö voi koskea todellista alustaa, tietopohjan kytkentää ja jakamista. Suunnittelupolun näyttö koskee arkkitehtuuria, simuloitua suoritusjälkeä, testitapauksia ja rajoituksia. Älä hyväksy kuivaharjoittelua todisteeksi toimivasta integraatiosta tai käyttöoikeudesta.
