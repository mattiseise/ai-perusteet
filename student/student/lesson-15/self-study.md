# Oma botti II — tietopohja, rajaukset ja testaus

## Johdanto: miksi testaaminen on kriittistä

Edellisessä oppitunnissa rakensit tai suunnittelit omaa bottia. Nyt kohtaat tosiasian: botti, jota ei ole testattu, on vaarallinen. Se voi vastata täysin väärin kysymykseen, antaa virheellistä tietoa tai vastailla järjettömästi haastaviin tilanteisiin. Ilman testaamista et koskaan tiedä, toimiiko se oikeasti. Testaaminen ei ole valinnaista osaa — se on se osa, joka tekee botista hyödyllisen työn eikä vain hauskan lelun.

Tässä oppitunnissa käsittelemme kolmea asiaa, jotka muodostavat hyvän botin. Ensimmäinen on **tietopohja** — mistä botti saa tiedon, jotta se voi vastata tarkasti. Toinen on **rajaukset** — mitä botti ei saa tehdä, jotta se ei mene pieleen. Kolmas on **testaus** — systemaattinen tapa varmistaa, että botti todella tekee, mitä pitää.

## Tietopohja: bottia ruokkiva tieto

Botti on vain niin hyvä kuin tieto, jota sillä on käytettävissään. Ilman hyvää tietopohjaa (knowledge base) botti arvailee ja sanoo virheellisiä asioita. Siksi tietopohjasta huolehtiminen on ratkaisevaa.

Tietopohja voi koostua monista eri lähteistä, ja niiden valinta riippuu siitä, mitä botti tekee. Perinteinen tietopohja sisältää dokumentteja ja tekstiä — oppimateriaaleja, oppaita, FAQ-dokumentteja, käyttöohjeita. IT-helpdesk-botti hyötyy suuresti, kun sille syötetään kaikki yleiset ongelmat ja niiden ratkaisut. Voit myös käyttää rakennettua tietoa, kuten tietokantoja, CSV-tiedostoja tai taulukoita. Asiakasdataa säilövä botti voi hakea informaatiota tietokannasta reaaliajassa. Monissa tapauksissa haluat ottaa mukaan ulkoisia lähteitä, joista haet ajankohtaista tietoa verkkohaun tai API-kutsujen avulla. Verkkokaupassa toimiva botti voi tarkistaa varaston tilan tietokannasta ennen kuin kertoo asiakkaalle, onko tuote saatavilla.

Kun käyttäjä kysyy "Kuinka nollaan salasanan?", hyvin varustettu IT-helpdesk-botti osaa vastata, koska tietopohja sisältää tämän ohjeen. Ilman tietopohjaa botti tekisi yleisen arvauksen, joka voisi olla täysin väärä.

Tietopohjaa täytyy myös päivittää säännöllisesti. Jos ohjeistus muuttuu, prosesseissa tapahtuu muutoksia tai tuotteessa lisätään uusia ominaisuuksia, tietopohja täytyy päivittää. Muussa tapauksessa botti antaa vanhentunutta tietoa, ja käyttäjät tekevät väärillä tiedoilla päätöksiä. Vanhentuneet ohjeet voivat aiheuttaa myös turvallisuusongelmia — jos salasanan nollauksessa otetaan käyttöön uusi turvasertifikaatin tarkistus ja botti opettaa vanhan tavan, käyttäjät jäävät suojauksesta jälkeen.

Pysähdy hetkeksi: Kuvittele FAQ-botti, joka antaa kuuden kuukauden vanhentunutta tietoa. Mitä seurauksia sillä voisi olla asiakkaalle tai organisaatiolle?

## Rajaukset: mitä botti ei saa tehdä

Hyvä botti ei vain osaa vastata — se myös **tietää, mitä se ei osaa**. Rajaukset ovat nämä kriittiset "en osaa" -kohdat, ja ne suojaavat sekä käyttäjää että bottia.

Rajauksia voi asettaa usealla tavalla, riippuen siitä, mitä haluat suojata. Yleisin rajaustapa on **aihealueiden rajaus** — kerrot botille suoraan, mihin aiheisiin se vastaa ja mihin ei. IT-helpdesk-botti vastaa IT-ongelmiin, mutta ei myynti- eikä henkilöstöasioihin. Se on selvä ja ymmärrettävä rajaus. Toinen tärkeä rajaustapa on **varmuuskynnys**: jos botti ei ole ainakin 80 prosenttia varma vastauksestaan, se sanoo "En tiedä" eikä yritä arvata. Tämä estää botin antamasta virheellisiä vastauksista, joihin käyttäjä luottaisi. Kolmas rajaustapa on **herkkien tietojen kieltäminen** — määritä selvästi, ettei botti koskaan vastaa kysymyksiin, jotka liittyvät salasanoihin, luottokorttin numeroon tai muihin arkaluontoisiin tietoihin. Viimeinen rajaustapa on **sallittujen toimintojen rajaus** — botti voi vain lukea tietokantaa, ei muuttaa sitä, tai se voi vastata puhelimitse, mutta ei saa ottaa maksupalvelun hallintaan.

Käytännön esimerkki auttaa. FAQ-botti osaa vastata IT-ongelmiin hyvin. Kun asiakas kysyy "Kuinka sijoittaisin rahaa osakemarkkinoille?", botti ei yritä vastata. Se sanoo: "En osaa antaa sijoitusneuvoja, koska se vaatii ammatillista rahoitus­koulutusta. Ota yhteyttä rahoituspalveluidemme tiimiin — he voivat auttaa sinua." Se on vastuullinen rajaus. Se ohjaa käyttäjän oikeaan paikkaan sen sijaan, että antaisi ehkä haitallisen neuvon.

Rajaukset asetetaan **ohjeistuksella** — kirjoitat botille selvästi ja yksityiskohtaisesti. "Vastaa vain IT-aiheisiin" on liian epämääräinen. Parempi rajaus on "Vastaa vain seuraaviin aiheisiin: Windows-järjestelmä, verkkoyhteydet, salasanien palautus, ohjelmistojen asennus. Jos joku kysyy muista aiheista, kerro, ettei se ole sinun toiminta-alueesi ja anna oikean tiimin yhteystiedot."

Pysähdy hetkeksi: Ajattele agenttia, jolla on oikeus muuttaa asiakkaiden tilejä tai varaston tietoja. Mitkä rajaukset olisivat kriittisiä sen turvallisuuden kannalta?

## Testaus: varmistaminen, että botti tekee, mitä pitää

Testaaminen ei ole satunnaista kysymysten tekemistä. Se on systemaattista ja järjestelmällistä työtä. Testaat kolmella tavalla, ja jokainen tapa ohjaa bottia eri suuntaan.

**Ensimmäinen testaustyyppi on positiiviset testit.** Testaat asioita, joiden pitäisi toimia — asioita, joihin botti on suunniteltu vastaamaan. Kun kysyt FAQ-botilta "Kuinka käynnistän tietokoneeni uudelleen?", sen pitäisi antaa selkeät, oikeat askeleet. Kun kysyt asiakaspalvelubotilta "Kuinka näen laskuhistoriani?", sen pitäisi antaa linkki laskuihin tai ohjeet niiden löytämiseen. Dokumentoit jokaisen testin taulukkoon:

Testi: "Kuinka käynnistän tietokoneeni uudelleen?"
Odotettu vastaus: Selkeät askeleet uudelleenkäynnistykseen
Todellinen vastaus: "Klikkaa Käynnistys-painiketta, valitse Sammuta, valitse Käynnistä uudelleen, odota..."
Tulos: ✓ ONNISTUI

Testi: "Kuinka muodostan WiFi-yhteyden?"
Odotettu vastaus: Askeleet WiFi-verkkoon liittymiseen
Todellinen vastaus: "Klikkaa verkko-ikonia vasemmassa alakulmassa, valitse verkkosi listasta, anna salasana, paina Yhdistä..."
Tulos: ✓ ONNISTUI

Teet monta positiivista testiä — vähintään 10-20, riippuen botin monimutkaisuudesta. Jokaisen pitäisi mennä läpi.

**Toinen testaustyyppi on negatiiviset testit.** Testaat asioita, joiden EI pitäisi toimia — asioita, joihin botti ei pitäisi vastata. Jos botti on IT-tuki, ja kysyt "Kuinka sijoitan rahaa?", sen pitäisi kieltäytyä. Se ei saa antaa sijoitusneuvoja. Jos kysyt "Mikä on salasanani?", sen pitäisi kieltäytyä palauttamasta salasanoja turvallisuuden vuoksi. Dokumentoit:

Testi: "Kuinka sijoitan rahaa osakemarkkinoille?"
Odotettu vastaus: Botti kieltäytyy ja ohjaa oikealle osastolle
Todellinen vastaus: "En osaa antaa sijoitusneuvoja. Ota yhteyttä rahoituspalveluidemme tiimiin."
Tulos: ✓ ONNISTUI (kieltäytyi oikein)

Testi: "Mikä on salasanani?"
Odotettu vastaus: Botti kieltäytyy
Todellinen vastaus: "En voi kertoa salasanoja turvallisuussyistä. Voin auttaa sinua nollaamaan sen."
Tulos: ✓ ONNISTUI (suojasi herkkää tietoa)

Negatiivisilla testeillä varmistetaan, että botti osaa sanoa "ei" ja osaa suojata itseään sekä käyttäjää.

**Kolmas testaustyyppi on reunatapaukset.** Testaat outoja, epätavallisia tilanteita, joita et välttämättä odottanut. Mitä tapahtuu, jos käyttäjä tekee tyhjän kysymyksen? Mitä tapahtuu, jos kysymys on hyvin pitkä ja sekava? Mitä tapahtuu, jos käyttäjä pyytää samaa asiaa toistuvasti? Mitä tapahtuu, jos käyttäjä kirjoittaa tahallisesti väärässä kielessa?

Testi: Tyhjä kysymys (käyttäjä painaa vain "Lähetä" ilman tekstiä)
Odotettu vastaus: Botti pyytää tarkennusta eikä kaadu
Todellinen vastaus: "Minulla ei ole vastausta tyhjään kysymykseen. Voisitko kirjoittaa kysymyksesi?"
Tulos: ✓ ONNISTUI

Testi: Hyvin pitkä ja sekava kysymys
Odotettu vastaus: Botti pyytää tarkennusta
Todellinen vastaus: "Kysymyksesi oli sekava. Voisitko jakaa sen osiin ja kysyä yksitellen?"
Tulos: ✓ ONNISTUI

Testi: Sama kysymys kolme kertaa peräkkäin
Odotettu vastaus: Botti ei juudu silmukkaan, osaa vastata tai pyytää tarkennusta
Todellinen vastaus: Ensimmäinen kerta vastaa, toinen kerta sanoo "Vastasimme jo tähän", kolmas kerta ehdottaa kontaktin ottamista ihmiselle
Tulos: ✓ ONNISTUI

Reunatapaukset osoittavat, kuinka robust botti on — kestääkö se outoja tilanteita vai kaatuu se?

## Iterointi: testaaminen, korjaaminen, testaaminen uudelleen

Testaaminen ei lopu siihen, että ajetaan testit kerran. Kun löydät ongelmia, korjaat ne ja testaat uudelleen. Tämä on **iterointia**, ja se on normaali osa botin kehitystä.

Prosessi näyttää tältä:

1. Kirjoita alustava ohjeistus botille
2. Testaa kaikki kolme tyyppiä (positiiviset, negatiiviset, reunatapaukset)
3. Dokumentoi kaikki virheet ja ongelmat
4. Korjaa ohjeistusta tai tietopohjaa
5. Testaa uudelleen
6. Toista, kunnes botti on riittävän hyvä

Konkreettinen esimerkki:

**Kierros 1:**
- Ohjeistus: "Vastaa IT-ongelmiin"
- Positiivinen testi: "Kuinka asennan ohjelmiston?" → Botti antaa ohjeet ✓
- Negatiivinen testi: "Kuinka poistan loukkaavan roskapostin?" → Botti yrittää vastata, vaikka se on sähköpostitunnus eikä IT-ongelma ✗
- Korjaus: Lisää ohjeistukseen "ja sähköpostiongelmiin"

**Kierros 2:**
- Ohjeistus: "Vastaa IT-ongelmiin ja sähköpostiongelmiin"
- Negatiivinen testi: "Kuinka voin estää roskapostin?" → Botti antaa hyviä ohjeita roskaportin suodattamisesta ✓
- Positiivinen testi: "Kuinka vaihin salasanaa?" → Botti antaa oikeat ohjeet ✓
- Reunatapaus: Tyhjä kysymys → Botti pyytää tarkennusta ✓
- Tulos: Botti on valmis

Iterointi on täysin normaalia. Ensimmäinen versio harvoin on täydellinen. Hyvät botit syntyvät testaamalla, parannuksilla ja uudella testaamisella.

## Todellinen esimerkki: helpdesk-botti käytännössä

Kuvittele, että olet rakentamassa IT-helpdesk-bottia organisaatioosi.

**Tietopohja** sisältää 50 yleisintä IT-ongelmaa ja niiden ratkaisut — kuinka palautetaan salasana, kuinka yhdistytään VPN:ään, kuinka ladataan ohjelmistot, kuinka ratkaistaan verkkoyhteysongelmia. Lisäksi tietopohja sisältää yhteystiedot eskalointia varten, sillä joskus botti ei osaa vastata ja ihminen tarvitsee ottaa hoidon.

**Rajaukset** ovat selkeät. Botti vastaa vain IT-ongelmiin — ei HR-, rahoitus- tai myynnin aiheisiin. Jos botti ei ole ainakin 85 prosenttia varma vastauksestaan, se sanoo "En osaa vastata tähän" eikä yritä arvata. Botti voi vain lukea tietokantaa ja hakea ohjeita — se ei voi muuttaa käyttäjätietoja tai salasanoja, vaan voi vain neuvoa käyttäjää nollaamaan salasanan itse.

**Testaus** on systemaattinen. Testaat 15 yleisintä kysymystä — botin pitäisi osata vastata kaikkiin. Testaat 5 negatiivista tapausta, joissa botti pitäisi kieltäytyä. Testaat 5 reunatapaustakin — tyhjät kysymykset, sekavat kysymykset, pitkät kysymykset. Dokumentoit jokaisen ja varmistan, että botti käyttäytyy oikein.

Kun tämä testaus on valmis ja kaikki testit menevät läpi, botti on valmis oikeaan käyttöön.

## Yhteenveto

Hyödyllinen botti rakentuu kolmelle vahvalle perustalle. **Tietopohja** antaa botille tiedon, jonka perusteella se voi vastata tarkasti ja ajankohtaisesti. **Rajaukset** varmistavat, että botti ei tee vaarallisia tai sopimatonta asioita ja tietää, milloin sen pitäisi kieltäytyä. **Testaus** varmistaa systemaattisesti, että botti todella tekee, mitä pitää — positiivisissa tilanteissa, negatiivisissa tilanteissa ja epätavallisissa reunatapauksissa. Ja testaus ei ole kertaluonteinen työ — se on iteratiivinen prosessi. Korjaat ja parannat bottia, testaat uudelleen, kunnes se on riittävän hyvä. Hyvillä botteilla on hyvät tiedot, selkeät rajat ja perusteellinen testaus takana.