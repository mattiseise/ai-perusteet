# Itsenäinen opiskelu: Agenttien toimintalogiikka — suunnittelu, työkalut, muisti

## Johdanto: Miten agentti ajattelee

Aiemmassa oppitunnissa oppit, että agentti tekee päätöksiä autonomisesti. Mutta millä tavalla se tekee näitä päätöksiä? Kun ihminen ratkaisee ongelman, hän ajattelee: "Mitä haluan saavuttaa? Mitä tietoa tarvitsen? Mitkä ovat vaihtoehdot? Mikä on paras tapa edetä?" Agentti tekee samoin — mutta prosessi on prosessoitu ja äärimmäisen nopea. Ymmärtääksesi, miten agentti toimii käytännössä, sinun täytyy nähdä tämä "ajatteluprosessi" — millä tavalla agentti asettaa ongelman, etsii ratkaisuja ja tekee valintoja.

Tämä oppitunti käsittelee agentin sisäistä toimintalogiikkaa. Kun agentti saa tehtävän, se ei vain toimi sattumanvaraisesti. Se käy läpi **suunnittelusilmukan** (planning loop), jossa se jaottelee tehtävän pienempiin, hallittaviin askeleihin, arvioi, mitä tietoja sillä on, mitä puuttuu, ja millä **työkaluilla** se voi täyttää nämä aukot. Lisäksi agentti tarvitsee **muistin** — kyvyn muistaa, mitä se on jo oppinut tai nähnyt, jotta se ei tee samoja virheitä uudelleen.

## Suunnittelusilmukka — Miten agentti hajottaa ongelmaa

Imaaginoi, että sinulla on monimutkainen projekti. Et voi vain hypätä sisään ja alkaa tehdä — sinun täytyy suunnitella. Sanot itsellesi: "Ensin selvitän projektin vaatimukset. Sitten etsin, mitä resursseja tarvitaan. Sitten jaoin työn osiin. Sitten aloitan ensimmäisellä osalla." Tämä on järkevä, heiratullinen suunnittelu. Agentti tekee täsmälleen samaa — mutta algoritmisesti.

Kun agentti saa tehtävän "analysoi tämä asiakastukitiiketti ja anna ratkaisu", se ei heti rynnä kirjoittamaan ratkaisua. Se käy läpi **suunnittelusilmukan**:

1. **Ymmärrä tavoite**: Agentti selkiintää itselleen, mitä se yrittää tehdä. "Tavoite on antaa asiakkaalle ratkaisu heidän tekniset ongelmaan."

2. **Jaa tehtävä askeleihin**: "OK, tarvitsen ensin ymmärtää ongelman. Sitten etsiä samankaltaisia tapauksia. Sitten syntetisoida ne yhteen ratkaisuun."

3. **Tunnista puuttuvat tiedot**: Agentti kysyy itseltään: "Mitä tietoa minulla jo on? Mitä minulla ei ole?" Voi olla, että asiakastiketti ei ole riittävän yksityiskohtainen, tai tarvitsee palvelimen lokeja, joita agentti ei vielä näe.

4. **Valitse työkalut**: Agentti päättää, mitä **työkaluja** sillä täytyy käyttää. "Tarvitsen hakea tietokannasta, lukea dokumentaatioita, ehkä ajaa testejä palvelimella."

5. **Suorita ja tarkkaile**: Agentti tekee askeleet ja tarkkailee tuloksia. "Löysin kolme samankaltaista tapausta. Nyt syntetisoin niistä vastauksen."

Jokainen näistä vaiheista voi vaatia agenttia palaamaan edelliseen. Esimerkiksi, jos agentti huomaa vaiheessa 3, että asiakastiketti puuttuu kriittisiä tietoja, se voi lähettää asiakkaalle followup-kysymyksen eikä jatka muuten.

**Pysähdy hetkeksi: Ajattele oman tekemäsi monimutkaista tehtävää. Mitä askeleita sinä käyt läpi, kun jaat tehtävän pienempiin osiin? Tekisikö agentti näitä askeleita samassa järjestyksessä kuin sinä?**

Käytännössä agentti ei vain "ajattele" näitä askeleita — se tekee niin tekemällä kutsuja kielimalliin (usein suurta kielimallia, kuten GPT-4:ää tai Claude:a). Agentti lähettää kielimallille promptin, joka kuvaa ongelman, ja malli vastaa. Sitten agentti analysoinnin mallin vastauksen perusteella tekee seuraavat pyynnöt. Se on iteratiivinen prosessi, ei yksisuuntainen.

## Työkalut — Agentin ulottuvuus

Agentti ei ole hyödytön ilman työkaluja. Työkalut ovat **agentin tavat toimia todellisessa maailmassa**. Jos agentti on puhdas ajattelijaorganisaatio, työkalut ovat kädet ja jalat.

Yleisiä agenttien työkaluja:

- **Verkon haku**: Agentti voi etsiä internetistä, löytää uusinta tietoa, linkkejä. Esimerkiksi support-agentti voi hakea documentation-sivustolta ratkaisuja.

- **Koodi-ajaminen**: Agentti voi ajaa koodia. Esimerkiksi agentti voi kirjoittaa pienen SQL-kyselyn tietokannan kyselyä varten, ajaa sen ja saada tulokset.

- **Tiedostojen lukeminen ja kirjoittaminen**: Agentti voi lukea tiedostoja (kuten konfiguraatiotiedostoja, logikoita, dokumentaatioita) ja kirjoittaa tuloksia.

- **API-kutsut**: Agentti voi kutsua muita palveluja. Esimerkiksi se voi kutsua sähköpostijärjestelmää ("lähetä viesti"), kalenteria ("katso, milloin käyttäjä on vapaana"), tietokantaa ("etsi asiakastiedot").

- **Ihmisen palaaminen**: Joissain tapauksissa agentti ymmärtää, että se tarvitsee ihmisen apua, ja kutsuu ihmisen — esimerkiksi "tämä on liian monimutkainen, jaa minut ihmisen asiantuntijalle."

Jokainen näistä työkaluista avaa mahdollisuuksia, mutta ne vaativat myös huolellista suunnittelua. Jos annat agentille väärät työkalut, tai liian laajat oikeudet, se voi tehdä vahingollisia asioita. Esimerkiksi, jos agentti voi suoraan poistaa tietokantaa tauluja, ja sen tavoite on "puhdista tietokannasta", pahoin käy.

**Pysähdy hetkeksi: Jos agentti voi ajaa mitä tahansa koodia palvelimellasi, mitä pahoja asioita se voisi tehdä, jos sen tavoitteet tai säännöt olisivat virheelliset?**

Siksi tosielämän agenttijärjestelmissä työkalut ovat usein rajallistetut. Agentilla voi olla pääsy API:hin, joka sallii lukea tietoja, mutta ei poistaa. Tai agentilla voi olla pääsy sähköpostiin, mutta vain muodosteiden lähettämiseen, ei sisällön kirjoittamiseen. Rajoittaminen on turvatoimenpide.

## Muisti — Agentin oppimahdollisuus

Muisti on se, mikä erottaa agentin idioottista robottista älykkäästä järjestelmästä. Ilman muistia agentti tekisi täsmälleen samaa jokaisen kerran, riippumatta siitä, mitä tapahtui aiemmin.

On olemassa kaksi päätyyppiä muistiä:

**Konteksti-ikkuna (context window)**: Kun agentti käyttää kielimallia, mallin sisään voidaan laittaa aiempi keskustelu, tapahtumahistoria, tai asiakastiedot. Tämä "konteksti" auttaa mallia ymmärtämään, mitä tapahtuu nyt. Esimerkiksi, jos asiakastuki-agentti lukee asiakkaan koko viestintähistorian (viimeiset 10 sähköpostia), se voi ymmärtää, että asiakas on jo yrittänyt ratkaisua kerran — eikä ehdota samaa uudelleen.

**Ulkoinen muisti (vector database, knowledge base)**: Agentti voi tallentaa tietoja ulkoiseen järjestelmään, kuten tietokantaan tai vektorimuistiin (semanttinen muisti). Tämä antaa agentille kyvyn oppia pitkän aikavälin yli. Esimerkiksi, jos agentti ratkaisee asiakkaan ongelman useita kertoja, se voi tallentaa ratkaisun muistiin ("asiakkaalla XYZ oli tämä ongelma, ratkaisu oli tämä"). Seuraavalla kerralla, kun samankaltainen ongelma tulee, agentti voi hakea sen muistista ja ehdottaa ratkaisua suoraan.

Käytännössä, useimmat agenttijärjestelmät käyttävät **molempia**. Konteksti-ikkuna antaa **lyhyen aikavälin** muistin (mitä tapahtui tässä keskustelussa), ja ulkoinen muisti antaa **pitkän aikavälin** muistin (mitä agentti on oppinut yli kaikkien aikaisempien tapauksista).

## Orkestraattori — Agenttijärjestelmän sydän

Edellä mainittiin suunnittelusilmukka, työkalut ja muisti. Mutta kuka tai mikä koordinoi näiden kaiken? Se on **orkestraattori** (orchestrator) — looginen moottori, joka ohjaa agenttia.

Orkestraattori on usein suuri kielimalli, joka on saatu spesiaalisesti harjoittelulla. Tai se voi olla perinteinen ohjelmisto, joka seuraaa logiikkaa ("jos X, tee Y"). Orkestraattori säilyttää tavoitteen mielessä, päättää, mitä askelta ottaa seuraavaksi, kutsuu oikeat työkalut, ja tulkitsee tuloksia.

Yksinkertainen esimerkki: Kun asiakastuki-agenttia pyydetään ratkaisemaan tiiketti:

1. Orkestraattori lukee tiketin (tämä on **havainto**)
2. Orkestraattori kutsuu kielimallia: "Mitä tämän tiketin ratkaisemiseksi pitäisi tehdä?" (tämä on **suunnittelu**)
3. Kielimalli vastaa: "Ensin pitäisi etsiä samankaltaisia tapauksia tietokannasta."
4. Orkestraattori kutsuu tietokanta-appia ja hakee samankaltaisia tapauksia (tämä on **työkalun käyttö**)
5. Orkestraattori lähettää kielimallille tulokset ja kysyy: "Mitä teki nyt?"
6. Kielimalli vastaa: "Näiden tapausten perusteella ratkaisu näyttää tältä..."
7. Orkestraattori lähettää vastauksen asiakkaalle ja merkitsee tiketin (tämä on **toimi**)
8. Orkestraattori tarkkailee asiakkaan vastausta (tämä on **havainnointi**)

Seuraavalla kierroksella looppi alkaa uudelleen tai päättyy.

Orkestraattori on siis agenttijärjestelmän sydän — se pitää prosessia kulkemassa, varmistaa että oikeat työkalut kutsutaan, että muistista haetaan asiaa, ja että tavoite säilyy mielessä.

## Yhteenveto

Agenttien toimintalogiikka rakentuu kolmelle pilarille. Ensimmäinen on **suunnittelusilmukka** — prosessi, jossa agentti jaottelee ongelman askeleihin ja suunnittelee ratkaisua iteratiivisesti. Toinen on **työkalut** — keinot, joilla agentti toimii todellisessa maailmassa, tietokannasta hakemisesta sähköpostien lähettämiseen. Kolmas on **muisti** — kyky muistaa ja oppia aikaisemmista tapauksista. Nämä kolme komponenttia yhdessä, ohjaajina **orkestraattorin**, tekevät agentista älykkään, adaptiivisen järjestelmän, joka voi ratkaista monimutkaisia tehtäviä iteratiivisesti.
