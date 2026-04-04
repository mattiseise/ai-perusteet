# Omat botit I – ohjeistetut botit ja GPT:t

## Johdanto: Näkeminen "sisäpuolelle"

Aiemmissa oppitunneissa olet oppinut, että agentit suunnittelevat, käyttävät työkaluja ja muistavat. Nyt on aika nähdä, miten nämä komponentit liitetään yhteen todelliseksi järjestelmäksi. Et ole rakentamassa agentia itse — tämä ei ole ohjelmointi-oppitunti. Sen sijaan olet **analysoimassa ja ymmärtämässä**, miten yksinkertainen agentti on rakennettu. Tämä on keskeistä ammattilaiselle, joka joutuu arvioimaan agenttijärjestelmiä, kehittämään niille vaatimuksia tai vianmäärittelemään niitä.

Yksinkertaisin agentti noudattaa **tehtäväjonoa** (task queue). Jokainen tehtävä koostuu askelista, jotka agentti käy läpi järjestyksessä. Kun yksi askel on valmis, agentti siirtyy seuraavaan. Jos askel epäonnistuu, agentti voi joko pysähtyä, kokeilla uudelleen tai kutsua ihmisen apuun.

## Tehtäväjono ja askeleet

Kuvitele tätä ongelmaa: yritys haluaa automatisoida sen, että joka päivä kerätään myyntidata kolmesta eri lähteestä, yhdistetään tiedot, ja lähetetään raportti johdolle. Ilman agentia ihminen tekisi tämän manuaalisesti joka päivä — vie tunnin, on virhealtista, ja ihminen voi unohtaa sen.

Agentti voi automatisoida tämän rakentamalla **tehtäväjonon**:

```
Tehtäväjono: "Kerää päivittäinen myyntiraportti"
├─ Vaihe 1: Hae myyntidata lähteestä A
├─ Vaihe 2: Hae myyntidata lähteestä B
├─ Vaihe 3: Hae myyntidata lähteestä C
├─ Vaihe 4: Yhdistä tiedot yhteen tiedostoon
├─ Vaihe 5: Laske yhteenvedot (kokonaismyynti, kategoriaa kohti)
├─ Vaihe 6: Lähetä raportti johdolle sähköpostilla
└─ Vaihe 7: Merkitse tehtävä "valmis"
```

Jokainen vaihe on yksinkertainen ja konkreettinen — ne ei ole "ratkaise jokin monimutkainen ongelma". Ne ovat pikemminkin "kutsua tätä API:ta" tai "suorita tätä skriptiä".

Agentti käy nämä askeleet läpi järjestyksessä. Kun vaihe 1 on valmis, siirrytään vaiheelle 2. Vaikein osa on kunkin vaiheen välillä tapahtuva **vianmääritys**. Entä jos vaihe 1 epäonnistuu, koska lähde A ei ole saatavilla? Agentti tarvitsee **logiikan** sille, miten reagoida. Esimerkiksi:
- Kokeile uudelleen 3 kertaa, 5 minuutin väleillä
- Jos 3. yrityskin epäonnistuu, lähetä hälytys IT-tiimille
- Odota, kunnes IT-tiimi vahvistaa, että lähde on taas saatavilla

Tämä logiikka on agenttijärjestelmän "aivot". Se ei ole älykäs tekoäly — se on yksinkertainen, vaikkakin hyvin tarkkaa suorittava sarja sääntöjä.

**Pysähdy hetkeksi: Kun katsot tehtäväjonoa, näetkö kohdat, joissa ihmisen pitäisi tehdä päätös, eikä agentti? Missä agentti riittää?**

## Agenttikehykset — rakentamisen lohkot

Käytännössä agenttijärjestelmät rakennetaan usein **agenttikehyksillä** (agent frameworks). Kehys on ohjelmistokirjasto, joka tarjoaa valmiita rakennuspaloja, joiden avulla voit rakentaa agentteja nopeammin. Esimerkkejä agenttikehyksistä ovat LangChain, Autogen ja Camel.

Nämä kehykset tarjoavat:
- **Askelte hallinta**: Logiikka, joka suorittaa askeleet järjestyksessä
- **Virheenkäsittely**: Mekanismi, jolla selvitään virheistä
- **Logiikka**: Ehdolliset haarat ("jos tämä, tee tämä; muuten tee tuo")
- **Muisti**: Integraatio väliaikaismuistiin ja pysyväismuistiin
- **Integraatiot**: Valmiit liitännät API:hin ja muihin järjestelmiin

Kehys tekee siis paljon raskasta nostosta. Sen sijaan että sinun pitäisi kirjoittaa jokainen pala alusta, voit koota agentin valmiista paloista.

Ammattilaisena sinun ei tarvitse osata koodia näille kehyksille, mutta sinun täytyy **ymmärtää**, mitä ne tekevät ja mitä vaihtoehtoja ne tarjoavat. Joskus yksinkertainen, omaksi koodattu agentti on parempi. Joskus olemassaoleva kehys säästää kuukauden kehitystä.

## Yksinkertainen agentti — esimerkki arkistarinasta

Kuvitele, että sinulla on web-shop ja haluat automatisoida asiakkaiden uusien tilauksien käsittelyä. Ilman agentia:
1. Myyjä lukee sähköpostissa olevan tilauksen
2. Myyjä kirjoittaa tilauksen varaston järjestelmään
3. Myyjä lähettää tilausvahvistuksen asiakkaalle
4. Myyjä ilmoittaa varastoon, että tavara pitää poimia

Neljä askelta, jotka tekee ihminen. Agentti voi automatisoida kaiken.

Agentin rakennus näyttää tältä:
1. **Vaihe: Havaitse uusi tilaus** — Agentti tarkkailee sähköpostissa olevia tilausviestejä
2. **Vaihe: Rakenna tilaus** — Agentti kutsuu varaston API:ta ja luo tilauksen
3. **Vaihe: Varmista varasto** — Agentti kutsuu varaston API:ta ja tarkistaa, onko tavara varastossa
4. **Vaihe: Lähetä vahvistus** — Agentti lähettää vahvistussähköpostin asiakkaalle
5. **Vaihe: Ilmoita varastolle** — Agentti kutsuu varaston poiminta-API:ta

Jokainen vaihe on yksinkertainen, mutta yhdessä ne ratkaisevat monimutkaisen tehtävän. Lisäksi agentti tekee tämän **joka päivä automaattisesti**, ilman ihmisen osallistumista.

**Pysähdy hetkeksi: Missä vaiheessa näistä ihminen pitäisi tehdä päätös? Mitä voisi mennä pieleen, jos agentti tekee kaiken automaattisesti?**

## Rakentamisen näkökulma — Arkkitehtuuri

Kun arvioit agenttijärjestelmää, on hyödyllistä ajatella sen **rakennetta** kolmesta näkökulmasta:

1. **Sisäänkäynnit (Inputs)**: Mitä agentti ottaa vastaan? Esimerkiksi uutta sähköpostia, palvelimen ilmoitusta, käyttäjän pyyntöä.

2. **Vaiheet (Steps)**: Mitä agentti tekee näillä syötteillä? Käy vaiheet läpi ja varmista, että logiikka tekee järkeä.

3. **Ulostulot (Outputs)**: Mitä agentti tuottaa? Sähköposteja, tietokantamuutoksia, lokikirjoituksia, hälytyksiä.

Rakentamisen näkökulma on tärkeä, koska se auttaa sinua näkemään agentin **toiminnot ja rajat** selvästi. Jos näet, että agentti voi poistaa tietokantanrekisterejä (output), voit kysyä: "Miksi sillä on tämä oikeus? Voiko se vahingolla poistaa tärkeitä rekistereitä?"

## Yhteenveto

Yksinkertainen agentti noudattaa **tehtäväjonoa** — sarjaa askeleita, jotka suoritetaan järjestyksessä, kunnes tehtävä on valmis. Agenttien rakentaminen käyttää usein **agenttikehyksiä**, jotka tarjoavat valmiit rakennuspalat. Ammattilaisena, vaikka et rakenna agenteja, sinun täytyy **ymmärtää niiden rakennetta**: mistä ne saavat syötteensä, mitä askeleita ne käyvät läpi, ja mitä ne tuottavat. Tämä ymmärrys auttaa sinua evaluoimaan agenttijärjestelmiä ja tunnistamaan riskejä.
