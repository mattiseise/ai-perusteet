# Ohjatut tehtävät — oppitunti 21

Näissä tehtävissä samaa asiakaspalvelutapausta tarkastellaan neljästä suunnasta. Tarkoitus ei ole kerätä agentille mahdollisimman paljon tietoa, vaan oppia erottamaan toisistaan hetkellinen konteksti, myöhemmin tarvittava muisti, prosessin tila ja toimintaa rajaavat säännöt. Pyydä oppijoita perustelemaan jokainen tallennuspäätös: mitä tehtävää tieto palvelee ja kuinka kauan sitä todella tarvitaan?

## Aktiviteetti 1 — Nykyhetki, rakenne, tietopohja vai tila? (15 min)

Luokittele asiakaspalvelutapauksen tiedot:

- käyttäjän juuri lähettämä viesti → konteksti
- asiakkaan sopimusnumero → rakenteinen pitkäkestoinen tieto, jos tehtävä ja käyttöoikeus sitä vaativat
- ohjeartikkeli → hyväksytty tietopohja, josta RAG voi hakea tekstikatkelman
- viime vuonna ratkaistu samankaltainen tapaus → semanttisen haun ehdokas, ei automaattisesti oikea ratkaisu
- hyvityspyyntö odottaa hyväksyntää → tila
- asiakkaan salasana → ei tallenneta

Käykää vastaukset läpi yksi kerrallaan. Jos ryhmä haluaa tallentaa tiedon ”varmuuden vuoksi”, kysy, missä tulevassa päätöksessä tietoa käytetään. Erota samalla täsmällinen tunniste semanttisesta hausta: sopimusnumero haetaan rakenteisesta järjestelmästä, kun taas RAG hakee tietopohjasta merkitykseltään sopivia tekstikatkelmia. Salasana toimii tarkoituksellisena rajatapauksena: kaikkea tehtävässä vastaan tulevaa tietoa ei saa muuttaa muistiksi.

## Aktiviteetti 2 — Väärä samankaltaisuus (15 min)

Anna kaksi aiempaa tapausta, joista toinen käyttää samoja sanoja mutta koskee eri ongelmaa. Ryhmä päättää, millä näytöllä hakutuloksen osuvuus tarkistetaan ennen käyttöä.

Tehtävän ydin on huomata, ettei samankaltaisuus vielä tarkoita soveltuvuutta. Pyydä ryhmää nimeämään vähintään yksi tieto, jonka täytyy täsmätä, ja yksi ristiriita, jonka vuoksi aiempi tapaus pitää hylätä. Purussa kannattaa erottaa toisistaan hyvä hakutulos ja oikea päätös: hakujärjestelmä voi löytää ehdokkaan, mutta agentin ohjauskehyksen tai ihmisen on vielä tarkistettava sen käyttökelpoisuus.

## Aktiviteetti 3 — Tilakone paperilla (20 min)

Oppija kuvaa kolme tilaa ja siirtymäehdot:

| Nykyinen tila | Tapahtuma tai ehto | Seuraava tila |
| --- | --- | --- |
|  |  |  |

Kysy, mikä estää saman toiminnon suorittamisen kahdesti.

Jos vastaus jää yleiseksi, tuo mukaan konkreettinen tilanne: hyvitys on jo maksettu, mutta sama viesti käsitellään uudelleen. Oppijan pitäisi pystyä osoittamaan, mikä tilatieto tai tunniste estää toisen maksun. Näin tila ei jää abstraktiksi kaavioksi, vaan sen yhteys turvalliseen toimintaan tulee näkyväksi.

## Aktiviteetti 4 — Sääntö ei ole muisto (15 min)

Anna periaate: ”Älä jaa yhden asiakkaan tietoja toiselle.” Oppijat päättävät:

- mitä kirjoitetaan järjestelmäohjeeseen
- mitä käyttöoikeutta agentin ohjauskehys rajoittaa
- missä tarvitaan tarkistus tai ihmisen hyväksyntä

Päätä tehtävä vertaamalla ryhmien ratkaisuja. Järjestelmäprompti voi ilmaista tavoitteen, mutta arkaluonteisen tiedon käyttöoikeutta ei pidä jättää pelkän tekstiohjeen varaan. Hyvä vastaus kertoo, miten agentin ohjauskehys rajoittaa pääsyä tietoihin ja mitä tapahtuu, jos sääntöä ei voida varmistaa teknisesti.

## Opettajan tarkistuslista

- Muistiin ei kerätä tietoa varmuuden vuoksi.
- Pitkäkestoinen muisti voidaan perustellusti jättää pois.
- Tilasiirtymät ovat havaittavia.
- Toimintaperiaatteita ei kuvata koneen omana identiteettinä tai arvoina.
