# Agentit-osion lopputyö — rajatun agentin näyttö

> Tämä on Agentit-osion (tunnit 19–27) lopputyö. Rakennat sitä osissa oppituntien aikana. Tunnilla 27 kokoat valmiin näytön yhden 90 minuutin oppitunnin aikana.

Tällä kurssilla rakennettavalla tekoälyagentilla tarkoitetaan kielimallin ja agentin ohjauskehyksen muodostamaa järjestelmää. Kielimalli tekee vähintään yhden aidon rajatun valinnan. Agentin ohjauskehys rajaa sallitut vaihtoehdot, työkalut, oikeudet, tilan, turvan, hyväksynnät ja lokituksen.

Voit tehdä lopputyön teknisenä n8n-toteutuksena tai dokumentoituna suunnittelusuorituksena. Polut ovat samanarvoisia. Niissä käytetään erilaista todistusaineistoa, mutta arvioidaan samaa ymmärrystä.

## Kaksi toteutuspolkua

**Tekninen polku:** rakennat rajatun n8n-työnkulun. Näytät suoritusnäkymästä syötteen, vähintään kaksi sallittua vaihtoehtoa, kielimallin todellisen valinnan, seuraavan haaran tai toiminnon sekä tuloksen. Rajaat oikeudet ja näytät vähintään yhden turvallisen virhe- tai eskalointipolun.

**Dokumentoitu polku:** kuvaat n8n-rakenteen kaaviona, määrität työkalusopimukset ja seuraat suorituksen vaihe vaiheelta. Teet vähintään yhden todellisen kielimallikutsun, jossa malli valitsee vähintään kahdesta sallitusta vaihtoehdosta. Merkitset toteutetun mallikutsun, simuloidut vaiheet ja teknisesti todentamattomat liitännät erikseen.

Solmujen määrä ei ratkaise laatua. Molemmissa poluissa ratkaisevaa on näkyvä, aito ja rajattu mallivalinta sekä sitä hallitseva agentin ohjauskehys.

## Projektipolku tunneilla 19–27

| Tunti | Työvaihe | Tuotos |
|---|---|---|
| **19** | Kirjaat kaksi tai kolme mahdollista ongelmaa | Projektiehdokkaat |
| **20** | Vertaat promptausta, työnkulkua ja agenttia ja valitset lopullisen ongelman | Agentti: Ongelma 1/5 |
| **21** | Suunnittelet kontekstin, tilan ja mahdollisen pitkäkestoisen muistin | Agentti: Muisti 2/5 |
| **22** | Valitset rajatut työkalut ja oikeudet | Työkalulista |
| **23** | Valitset ReActin tai eksplisiittisen työnkulun ja määrität aidon rajatun mallivalinnan | Agentti: Päättely 3/5 |
| **24** | Suunnittelet turvakerroksen ja havaittavat eskalointiehdot | Agentti: Turva 4/5 |
| **25** | Suunnittelet ihmisen hyväksynnän ja aikarajat | Agentti: Ihminen 5/5 |
| **26** | Kokoat teknisen minimiversion tai dokumentoidun suunnitelman | Ensimmäinen toteutuspolun näyttö |
| **27** | Viimeistelet, testaat, korjaat ja puolustat 90 minuutissa | Arvioitava näyttöpaketti |

## Viisi pohjapiirrosta

**1. Agentti: Ongelma.** Kuvaa käyttäjä, ongelma ja se yksi tilanteen mukaan muuttuva päätös, jonka kielimalli tekee. Perustele, miksi ennalta määritelty työnkulku ei yksin riitä.

**2. Agentti: Muisti.** Kuvaa yhden suorituksen konteksti, prosessin tila ja mahdollinen pitkäkestoinen muisti. Perustele tallennusaika ja tietosuoja. Pidä järjestelmäohjeet erillään muistista: agentin tehtävä, rooli ja rajat kuuluvat järjestelmäpromptiin tai agentin ohjauskehyksen sääntöihin.

**3. Agentti: Päättely.** Valitse ReAct tai eksplisiittinen työnkulku. Määritä vähintään yksi vaihe, jossa kielimalli tekee aidon rajatun valinnan vähintään kahdesta sallitusta vaihtoehdosta. Kuvaa, miten syöte, vaihtoehdot, valinta ja seuraava vaihe näkyvät lokissa.

**4. Agentti: Turva.** Kuvaa oikeudet, keskeiset riskit, validointi, rajoitukset, seuranta ja palautuminen. Määritä havaittavat eskalointiehdot. Mallin itse ilmoittama varmuusprosentti ei ole hyväksyntäraja.

**5. Agentti: Ihminen.** Nimeä toiminnot, jotka vaativat ihmisen hyväksynnän. Kuvaa hyväksyjälle näytettävät tiedot, aikaraja ja turvallinen varapolku. Kriittistä toimintoa ei hyväksytä hiljaisuuden perusteella.

## Kuuden rakennusosan tarkistus

Käytä kokonaisuuden tarkistamiseen näitä kanonisia nimiä:

1. **syötekäsittelijä**
2. **päättelijä ja suunnittelija**
3. **työkalujen suorittaja**
4. **muisti ja konteksti**
5. **turvakerros**
6. **seuranta ja palautesilmukka**

Merkitse jokaisesta, missä vastuu näkyy tai miksi sitä ei tarvita. Yksi solmu, sääntö tai palvelu voi kattaa useita vastuita.

## Tunnin 27 pakollinen 90 minuutin suoritus

| Aika | Vaihe |
|---|---|
| 0–8 min | Rajaa pääpolku ja avaa aineisto |
| 8–30 min | Viimeistele toteutus tai dokumentoitu suunnitelma |
| 30–48 min | Aja normaali, reuna- ja turvallisuustesti |
| 48–63 min | Tee yksi korjaus ja aja sama testi uudelleen |
| 63–75 min | Kokoa tiivis näyttöpaketti |
| 75–88 min | Pidä 2–3 minuutin puolustus pienryhmässä, tallenteena tai otoksessa |
| 88–90 min | Palauta tai tallenna työ |

Pakollista työtä ei jätetä kotiin. Jos jokin tekninen osa ei valmistu, rajaa näyttöä ja merkitse asia rajoitukseksi. Lisätestit ja laajemmat integraatiot ovat vapaaehtoista syventämistä.

## Näyttöpaketti

Kokoa yhdelle sivulle, dialle tai vastaavaan tiiviiseen näkymään:

- ongelma ja valittu toteutuspolku
- työnkulku tai kaavio sekä kuuden rakennusosan kattavuus
- syöte, vähintään kaksi sallittua vaihtoehtoa, kielimallin todellinen valinta ja seuraava vaihe
- yksi normaali, yksi reuna- ja yksi turvallisuustesti
- yksi korjaus ja sama uudelleentesti
- tärkein turvallisuusraja ja yksi rehellinen tekninen rajoitus.

Tekninen polku liittää mukaan suoritusnäytön. Dokumentoitu polku liittää mukaan todellisen mallikutsun ja simuloidun suoritusjäljen. Kolmea erillistä pitkää dokumenttia, laajaa itsearviointia tai pakollista vertaisarviomuistiota ei vaadita.

## Puolustus 2–3 minuuttia

Puolustuksessa kerrot ongelman ja toteutuspolun, näytät aidon rajatun mallivalinnan, vertaat testiä ja uudelleentestiä sekä nimeät turvallisuusrajan ja asian, jota työsi ei vielä todista. Puolustus voidaan toteuttaa pienryhmässä, tallenteena tai opettajan valitsemana otoksena.

## Arviointi

| Kriteeri | Paino | Mitä arvioidaan? |
|---|---:|---|
| **Rakenne ja toteutuspolun näyttö** | 20 % | Työnkulku tai kaavio on seurattava ja kuusi rakennusosaa on käsitelty perustellusti. |
| **Aito rajattu mallivalinta** | 25 % | Syöte, vähintään kaksi sallittua vaihtoehtoa, mallin valinta ja seuraava vaihe näkyvät. |
| **Testi, korjaus ja uudelleentesti** | 25 % | Kolme testitulosta ja yhden puutteen ennen–jälkeen-näyttö ovat jäljitettävissä. |
| **Turvallisuus ja rajat** | 20 % | Oikeudet, havaittava eskalointiehto ja rajoitus on kuvattu tai toteutettu. |
| **Puolustus** | 10 % | Opiskelija perustelee ratkaisunsa ja erottaa toteutetun simuloidusta. |

Arviointi ei suosi teknistä polkua. Tekninen suoritusnäkymä ja dokumentoidun polun todellinen mallikutsu sekä simuloitu suoritusjälki ovat erilaisia mutta samanarvoisia tapoja osoittaa osaamista.

## Arviointitasot

| Kriteeri | Erinomainen | Hyvä | Tyydyttävä | Välttävä | Ei vielä hyväksyttävä |
|---|---|---|---|---|---|
| Rakenne ja toteutuspolun näyttö (20 p) | Työnkulku on johdonmukainen, kaikki kuusi rakennusosaa on käsitelty perustellusti ja polkukohtainen näyttö on selvästi rajattu. | Rakenne on seurattava, rakennusosat on käsitelty ja toteutettu sekä simuloitu on erotettu. | Ydinrakenne näkyy, mutta yksi rakennusosan vastuu tai näytön raja jää epäselväksi. | Rakenne on osittainen tai toteutuspolun näyttöä on vaikea seurata. | Työnkulku tai toteutuspolun olennainen näyttö puuttuu. |
| Aito rajattu mallivalinta (25 p) | Syöte, sallitut vaihtoehdot, kielimallin todellinen valinta ja seuraava vaihe ovat täysin jäljitettävissä ja valinnan tarve on vakuuttavasti perusteltu. | Vähintään kahden vaihtoehdon aito mallivalinta ja sitä seuraava vaihe näkyvät. | Mallivalinta on aito ja rajattu, mutta loki tai perustelu on osittainen. | Kielimallia käytetään, mutta valinnan vaihtoehdot tai vaikutus jäävät epäselviksi. | Aitoa rajattua kielimallivalintaa ei ole. |
| Testi, korjaus ja uudelleentesti (25 p) | Normaali, reuna- ja turvallisuustesti ovat jäljitettäviä; yksi korjaus ja sama uudelleentesti osoittavat rajatusti, mitä parani ja mitä ei voida päätellä. | Kolme testiä, yksi korjaus ja sama uudelleentesti on dokumentoitu odotuksineen. | Testit kattavat ydintoiminnan, mutta korjauksen ennen–jälkeen-näyttö on osittainen. | Testejä on liian vähän tai tuloksia ei verrata ennalta kirjattuun odotukseen. | Testaus tai korjausketju puuttuu. |
| Turvallisuus ja rajat (20 p) | Oikeudet, havaittavat eskalointiehdot, turvallinen varapolku ja ratkaisun rajat muodostavat johdonmukaisen kokonaisuuden. | Keskeiset oikeudet, eskalointiehto ja rajoitus on kuvattu tai toteutettu. | Turvallisuuden ydinratkaisu näkyy, mutta jokin oikeus, ehto tai varapolku jää yleiseksi. | Turvallisuus perustuu lähinnä promptiin tai epämääräiseen ihmisen valvontaan. | Olennaiset turvallisuusrajat puuttuvat. |
| Puolustus (10 p) | Opiskelija perustelee valintansa täsmällisesti, tulkitsee testin oikein ja erottaa toteutetun, simuloidun sekä todentamattoman. | Opiskelija perustelee ratkaisun, testin ja keskeisen rajoituksen omin sanoin. | Oma ymmärrys näkyy, mutta yksi keskeinen perustelu tai rajoitus jää yleiseksi. | Puolustus kuvaa lähinnä työvaiheita ilman riittävää perustelua. | Puolustus puuttuu tai ei osoita omaa ymmärrystä. |

## Valmiin työn tarkistus

- [ ] Työ ratkaisee yhden rajatun ongelman.
- [ ] Kielimalli tekee aidon rajatun valinnan vähintään kahdesta sallitusta vaihtoehdosta.
- [ ] Kuusi rakennusosaa on käsitelty kanonisilla nimillä.
- [ ] Kolme testitulosta on dokumentoitu.
- [ ] Yksi korjaus ja sama uudelleentesti näkyvät.
- [ ] Tärkein turvallisuusraja ja havaittava eskalointiehto on kuvattu.
- [ ] Toteutettu, simuloitu ja todentamaton on erotettu rehellisesti.
- [ ] 2–3 minuutin puolustus on valmis.

Kun nämä kohdat täyttyvät, työ on valmis. Laajempi toteutus voi olla kiinnostava jatkoprojekti, mutta se ei kuulu tämän oppitunnin pakolliseen suoritukseen.
