# Opiskelutehtävät: Kasaa suunnitelma ja tee toimiva minimiversio

> Tämä on Agentit-osion ensimmäinen rakennustunti. Tänään kokoat viisi pohjapiirrostasi yhtenäiseksi suunnitelmaksi ja teet agentistasi ensimmäisen testattavan version. Voit edetä teknistä n8n-polkua tai dokumentoitua suunnittelupolkua. Molemmissa kielimallin on tehtävä vähintään yksi todellinen, tilanteen mukaan muuttuva valinta.

## Vaihe 1: Kasaa pohjapiirrokset suunnitelmaksi

Lue viisi pohjapiirrostasi yhtenä kokonaisuutena. Korjaa ristiriidat ja varmista, että ratkaisu vastaa Automaatio vai autonomia -tunnilla valitsemaasi ongelmaan. Kirjoita sen jälkeen lyhyt arkkitehtuuriluonnos. Kuvaa ensin, mitä kielimalli tekee ja mistä agentin ohjauskehys vastaa. Esitä sitten ratkaisun tärkeimmät vaiheet, niiden syötteet ja tulokset. Vaiheiden määrää ei ole määrätty: mukana ovat vain tehtävän kannalta tarpeelliset vastuut.

Tarkista luonnoksesta kuusi rakennusosaa: **syötekäsittelijä**, **päättelijä ja suunnittelija**, **työkalujen suorittaja**, **muisti ja konteksti**, **turvakerros** sekä **seuranta ja palautesilmukka**. Merkitse jokaisesta, onko se mukana, lisätäänkö se Agentin viimeistelytunnilla vai eikö sitä tarvita tässä työssä. Perustele poisjättö lyhyesti.

Voit pyytää tekoälyä esittämään suunnitelmastasi kysymyksiä:

```text
Olen koonnut viisi pohjapiirrosta agentistani. Lue ne ja kysy
minulta kysymyksiä, jotka paljastavat mahdolliset ristiriidat tai
aukot. Älä korjaa puolestani, vaan auta minua huomaamaan ongelmat.
```

## Vaihe 2: Valitse toteutuspolkusi

Valitse polku, jolla pystyt osoittamaan ymmärryksesi luotettavimmin.

**Tekninen n8n-polku.** Rakenna n8n:ssä toimiva minimiversio. Tallenna suoritusnäkymästä syöte, kielimallin valinta, mahdollisen työkalun tulos ja seuraava vaihe. Tekninen näyttö osoittaa, että yhteydet, reititys ja rajaukset toimivat käytetyssä ympäristössä.

**Dokumentoitu suunnittelupolku.** Kuvaa sama kokonaisuus n8n-kaaviona tai selkeänä vaihekuvauksena. Tee työkalusopimukset, oikeusrajat ja kaksi käsin seurattavaa suoritusjälkeä. Tämä polku osoittaa suunnittelun johdonmukaisuuden, mutta ei väitä testaamattomien liitäntöjen tai käyttöoikeuksien toimivan.

Kumpikaan polku ei ole helpotettu versio. Näyttö on erilainen, mutta molemmissa tarvitaan oikea kielimallikutsu. Malli valitsee tilanteen perusteella vähintään kahdesta sallitusta vaihtoehdosta, esimerkiksi `hae hyväksytystä lähteestä`, `pyydä lisätietoa` tai `ohjaa ihmiselle`.

## Vaihe 3: Tee ja testaa minimiversio

Anna järjestelmälle turvallinen esimerkkisyöte. Määritä kielimallille tehtävä ja vähintään kaksi sallittua vaihtoehtoa. Rajaa, milloin kukin vaihtoehto on käytettävissä, ja päätä, miten valinta näkyy suoritusjäljessä. Lisää ainakin yksi työkalu tai toimintopolku, jonka käyttöä agentin ohjauskehys rajaa.

Testaa kahdella erilaisella syötteellä. Valinnan pitää muuttua perustellusti tilanteen mukana. Kirjaa kummastakin testistä syöte, valittu vaihtoehto, perusteluna käytetty havaittava ehto, työkalun tai toimintopolun tulos ja seuraava vaihe. Jos järjestelmä kulkee aina samaa ennalta määrättyä reittiä, tarkista, onko kyse agentin sijasta työnkulusta.

Korjaa yksi testeissä löytynyt ongelma ja aja sitä koskeva testi uudelleen. Teknisen polun opiskelija tekee korjauksen työnkulkuun. Dokumentoidun polun opiskelija päivittää kaavion, sopimuksen tai rajauksen ja tuottaa uuden suoritusjäljen.

## Tunnin lopuksi

Kirjoita lyhyt tilannekuva: mihin pääsit, mikä jäi kesken ja mitä viimeistelet ensimmäisenä Agentin viimeistelytunnilla. Liitä mukaan toteutuspolkusi näyttö: teknisessä polussa kuva työnkulusta ja suoritusnäkymästä, dokumentoidussa polussa kaavio ja kaksi jäljitettävää suoritusjälkeä. Merkitse selvästi kohta, jossa kielimalli tekee tilanteen mukaan muuttuvan valinnan.

**Lopputyön rakentaminen 1/2 — Agentin viimeistelytunnilla viimeistelet, testaat ja esittelet**
