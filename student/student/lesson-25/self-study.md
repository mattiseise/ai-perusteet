# Ihminen portinvartijana — human-in-the-loop käytännössä

## Johdanto

Kaikki, mitä olet oppinut — muisti, konteksti, työkalut, suunnittelumallit, turvallisuus — johtaa yhdelle tärkeälle ajatukselle: **agentti ei voi tehdä kaikesta yksin**. Joissain tilanteissa agentti täytyy pysäyttää ja odottaa, kunnes ihminen sanoo "kyllä, jatka" tai "ei, älä tee sitä".

Tämä on **human-in-the-loop** — ihmisen osallistuminen automaation silmukkaan kriittisiä hetkillä. Se ei tarkoita, että ihminen tekee kaikkea — se tarkoittaa, että ihminen hyväksyy suuret päätökset, tarkistaa vaarallisia toimintoja ja ohjaa agenttia, kun agentti on epävarma.

Tässä oppitunnissa opit, **milloin ihmiset täytyy sisällyttää, kuinka suunnitella hyväksyntäportit ja kuinka rakentaa työnkulkuja, joissa agentti ja ihminen tekevät yhteistyötä**. Nämä periaatteet tulevat suoraan käytäntöön seuraavissa oppitunneissa, kun rakennat omaa agenttia n8n:llä.

## Milloin ihminen täytyy päätökseen

Ei jokainen agentin päätös tarvitse ihmisen hyväksyntää. Jos siihen vaikutuisi, seurauksena voisi olla, että ihminen olisi ylikuormitettu päätöksistä eikä ehdi. Sinun täytyy **valita strategisesti**, mitkä päätökset ovat niin kriittisiä, että ne vaativat hyväksynnän.

Kolme sääntöä auttavat päättämään:

**Sääntö 1: Rahaa tai rakenne**. Jos päätös liittyy rahaan (diskontti, hyvitys, palkkio), se vaatii hyväksynnän. Diskontti 10 % asiakkaalle — ehkä agentti voi tehdä sen yksin. Mutta 50 % alennus — siihen tarvitaan johtajan hyväksyntä, koska sillä on suuri taloudellinen vaikutus. Sama koskee rakennetta: jos päätös muuttaa asiakkaan tietoja, tilaa tai tulevaa suhde, vaadi hyväksyntä.

**Sääntö 2: Epävarmuus**. Jos agentti ei ole varma päätöksestään — varmuus on alle 70 % — vaadi ihmisen vahvistusta. Agentti sanoo "Olen 65 % varma, että tämä on lasku" — ihminen tarkistaa ja vahvistaa tai korjaa. Ihmisen silmät näkevät asioita, joita agentti ei osaa.

**Sääntö 3: Poikkeamat**. Jos tilanne ei ole rutiinitapaukselta vaan poikkeavuus, vaadi hyväksyntä. Asiakas tekee tavallisen tilauksen — agentti hoitaa yksin. Asiakas tekee epätavallisen tilauksen (negatiivinen hinta, miljoonan euron arvoinen osto, uusi tuote), hälytys aktivoituu, ja ihminen täytyy hyväksyä.

Näillä säännöillä voit jakaa päätöksistä. Neljäsosa päätöksistä agentti tekee yksin (rutiinit), ja neljäsosa vaatii ihmisen hyväksyntää (kriittiset päätökset). Loput puoli jakautuu — jotkut vaativat hyväksyntää varmautumisvaiheessa, toiset vasta jälkikäteen, kun ihminen tarkistaa lokeja.

**Pysähdy hetkeksi: Ajattele omaa työtäsi. Mitä päätöksiä sinä tekisit yksin ja mitkä johtaisit esimiehellesi? Mitkä olivat rahaa, rakennetta tai epävarmuutta liittyvät?**

## Hyväksyntäportit rakentaminen

Kun tiedät, mitkä päätökset vaativat hyväksyntä, seuraava askel on **rakentaa hyväksyntäportit**. Portti on järjestelmässä piste, jossa agentti pysähtyy ja odottaa ihmisen vastausta.

Käytännössä portti näyttää ihmiselle **selkeän kysymyksen ja ehdotuksen**, johon hän voi vastata "hyväksy" tai "hylkää". Esimerkiksi:

```
HYVÄKSYNTÄPYYNTÖ
Asiakas: John Smith
Pyyntö: 50 % alennus (tavallinen hinta 100€, ehdotettu 50€)
Perustelu: Asiakas on lojaali, 5 ostoa. Kilpailija tarjosi halvempaa.
Päätös vaaditaan: Myyntipäällikön
Vastaa: [HYVÄKSY] [HYLKÄÄ] [KYSY LISÄÄ]
```

Hyväksyntäportin täytyy olla **selkeä ja nopea vastata**. Ihminen näkee:
- **Mitä päätöstä vaaditaan** — 50 % alennus
- **Kelle** — John Smithille
- **Miksi** — lojaalisuus ja kilpailu
- **Kenen täytyy vahvistaa** — myyntipäällikön
- **Mitä tapahtuu, jos hylkää** — agentti ottaa yhteyttä asiakkaalle ja selittää, miksi alennus ei ole mahdollinen

Hyväksyntäportin jälkeen tapahtuva on kriittistä. Jos ihminen hyväksyy, agentti jatkaa. Jos hylkää, agentti tekee vaihtoehtoisen toiminnon — esimerkiksi tarjoaa asiakkaalle muuta, kuten ilmaisen toimituksen koko tilauksen arvosta. Agentti ei vain kaadu — sillä on vaihtoehtoinen polku.

Hyväksyntäportit kannattaa suunnitella myös **aikakysymysten** kanssa. Jos ihminen ei vastaa 24 tunnissa, mitä tapahtuu? Vaihtoehdot:
- **Oletusarvo**: Jos ei vastausta, hyväksyntä katsotaan annetuksi (vaatii varovaisuutta — esim. asiakkaalle varattu tuote myydään muille).
- **Escalation**: Lähetetään viesti toiselle hyväksyjälle.
- **Timeout**: Agentti peruuttaa pyynnön ja ilmoittaa asiakkaalle, että prosessi ei pysty jatkumaan nyt.

Valinta riippuu siitä, kuinka paljon **odottaminen maksaa**. Jos asiakas odottaa 24 tuntia vastausta, hän saattaa lähteä kilpailijalle. Jos tuote on rajallinen ja odottaa, se menettää myynnin. Näissä tapauksissa oletusarvo tai escalation on parempi. Mutta jos päätös on hyvin kriittinen ja väärä päätös on kallis (esim. miljoonan euron sopimus), timeout on parempi — parempi odottaa, kun ihminen ei ole saatavilla, kuin tehdä väärä päätös.

## Hyväksyntäportit käytännössä: kolme esimerkkiä

Katsotaan kolmea erilaista hyväksyntäporttia, jotta näet, kuinka ne toimivat.

**Esimerkki 1: Pienet päätökset — nopea hyväksyntä**

Agentti: "Asiakas haluaa vaihtaa tuotteen värissä. Väri on varastossa."
Portti näyttää: "Vaihda keltainen kaikella punaiselle?"
Hyväksyjä: Asiakaspalvelupäällikkö voi vastata 30 sekunnissa koko työpäivän aikana.
Oletusarvo: Jos ei vastausta 1 tunnissa, hyväksy automaattisesti (asiakasta ei haluta irritoida pitkällä odotuksella).

**Esimerkki 2: Suuret päätökset — perusteellinen hyväksyntä**

Agentti: "Asiakas haluaa 50 % alennuksen pitkässä sopimuksessa."
Portti näyttää: Koko asiakkaiden historia, kilpailijoiden tarjoukset, tuotteen voittomarginaali ja ehdotettu alennus prosentteina.
Hyväksyjä: Myyntipäällikkö tarkistaa kaikki tiedot ennen vastaamista.
Oletusarvo: Jos ei vastausta 4 tunnissa, timeout — agentti lähettää asiakkaalle viestin "Tarjouksia arvioidaan tiimissämme. Palaamme sinulle pian."

**Esimerkki 3: Vakavat päätökset — monivaiheinen hyväksyntä**

Agentti: "Uusi liikekumppani haluaa integroida tietokantamme."
Portti näyttää: Tietoturvanalyysi, integratiiviset riskit, liiketoiminnan hyödyt.
Hyväksyjä: Ensimmäinen tekniikka-johtaja, sitten liiketoimintajohtaja — kaksi hyväksyntää peräkkäin.
Oletusarvo: Jos jompikumpi hylkää, prosessi pysähtyy, ja agentti ilmoittaa integraatiokumppanille "Emme voi jatkaa nyt."

Näissä esimerkeissä näet, kuinka hyväksyntäportin **laajuus ja nopeusvaatimus** vaihtelevat päätöksellä. Pienet päätökset vaativat nopean hyväksynnän (ehkä automaattisen oletusarvon), suuret vaativat huolellista arviointia ja vakavat vaativat usean kerroksen tarkistusta.

## Työnkulut, joissa agentti ja ihminen tekevät yhteistyötä

Hyväksyntäportit ovat vain yksi osa human-in-the-loop-työnkulusta. Koko prosessi on **työnkulku, jossa agentti ja ihminen tekevät yhteistyötä**. Agentti tekee sitä, mitä se osaa — nopea analyysi, tietoa haku, yksinkertaiset päätökset. Ihminen tekee sitä, mitä agentti ei voi — kriittiset päätökset, empatiaa, tutkinta epäselvissä tapauksissa.

Kuvittele asiakaspalvelun työnkulkua:

**1. Syöte**: Asiakas lähettää viestin "Haluan palauttaa tuotteen."

**2. Agentti-analyysi**: Agentti lukee viestin, etsii asiakkaan tilauksen historiasta ja analysoi. Löytää: "Tilaus tehty 5 päivää sitten. Palautusaika on 14 päivää. Asiakas on oikeutettu."

**3. Hyväksyntäportti 1**: "Oletko varma, että palautusaika on voimassa?" Agentti näyttää perustelut. Ihminen vahvistaa yhdessä sekunnissa. "Kyllä, vahvistettu."

**4. Agentti-toiminta**: Agentti lähettää asiakkaalle palautuksesta tarvittavat tiedot — palautuslomake, kuljetusohjeet, takuun ehdot.

**5. Hyväksyntäportti 2**: "Asiakas on lojaali (5 ostoa). Halutessaan voimme tarjota 10 % alennusta seuraavaan tilaukseen." Ihminen vahvistaa. "Kyllä, tarjoa."

**6. Agentti-lopetus**: Agentti lähettää asiakkaalle jatkoviestin "Anteeksi, että palautus oli tarpeellinen. Tässä on 10 % alennus seuraavaan tilaukseen. Toivomme näkevämme sinut uudelleen."

Koko prosessi on hybridi. Agentti tekee rutiinianalyysia, ihminen tekee päätöksiä, agentti toteuttaa. Näin saavutetaan sekä nopeus (agentti on nopea analyysissä) että laatu (ihminen tekee järkeviä päätöksiä).

**Pysähdy hetkeksi: Ajattele omaa tulevaa työtäsi. Mitä prosessia voitaisiin automatisoida agentin avulla, mutta vaatii ihmisen hyväksyntöjä kriittisistä vaiheista? Missä vaiheissa ihminen täytyy sisällyttää?**

## Agentin oppiminen ihmisen palautteesta

Human-in-the-loop ei tarkoita vain sitä, että ihminen hyväksyy päätöksiä. Se tarkoittaa myös sitä, että **agentti oppii** ihmisen palautteesta. Kun ihminen hylkää agentin ehdotuksen, agentti voi kysyä "Miksi hylkäsit sen?". Kun ihminen hyväksyy, agentti voi tallentaa, mitä hyväksyt ja miksi.

Esimerkiksi agentti tekee alennusehdotuksia. Yksi myyntipäällikkö hyväksyy 40 % alennuksina, toinen vain 15 %. Agentti voi oppia: "Kun myyntipäällikkö A arvioi, hän hyväksyy suurempia alennuksia. Kun myyntipäällikkö B arvioi, hän on tiukempi." Agentti voi mukauttaa ehdotuksiaan — ehkä ehdottaa 30 % pää­miehelle A (koska hän todennäköisesti hyväksyy), mutta 10 % päällikölle B (koska se on hänen vaatimuksensa).

Tämä oppiminen tehdään **lokista ja palautteesta**. Jokainen hyväksyntä/hylkäys tallennetaan, ja agentti hakee näistä tiedoista kaavoja. Se ei ole automaattista — sinun täytyy nimenomaisesti kertoa agentille "opi näistä päätöksistä". Mutta kun opit, agentti alkaa tekemään parempia ehdotuksia ja vähemmän ihmisen hyväksyntää tarvitsee.

## Kohti n8n-projekteja — kaikki yhdistyy

Tämä on viimeinen teoriapainotteinen oppitunti ennen kuin pääset rakentamaan. Katsotaan, kuinka **kaikki oppituntien aiheet** yhdistyvät yhdeksi kokonaisuudeksi n8n:ssä:

| Aihe | Opit | Miten näkyy n8n:ssä |
|---|---|---|
| Agentin rakenne | 6 komponenttia | Jokainen komponentti on yksi tai useampi n8n-solmu |
| Automaatio vs. autonomia | Päätöspuu: promptaus / työnkulku / agentti | Valitsetko yhden AI Agent -solmun vai monivaiheisen ketjun |
| Muisti ja konteksti | Konteksti-ikkuna, pitkäkestoinen muisti, tila | Memory-solmu, Google Sheets -tila, system prompt |
| Työkalut | Tiedostot, haku, CLI | Read File, HTTP Request, Execute Command -solmut |
| Suunnittelumallit | ReAct, ketjuajattelu, moniagentti | AI Agent (ReAct), solmuketju (CoT), webhook-kutsut (moniagentti) |
| Turvallisuus | Injection, hallusinaatiot, minimioikeus | IF-solmut validointiin, rajoitetut API-avaimet |
| **Human-in-the-loop** | **Hyväksyntäportit, palaute, oppiminen** | **Hyväksyntäsolmu, Slack-ilmoitus, lokisolmu** |

Kaikki, mitä olet oppinut — hyväksyntäportit, human-in-the-loop-työnkulut, agentin oppiminen — tulevat elämään käytännössä. N8n on **visuaalinen automaatioalusta**, jossa näet konkreettisesti, kuinka:

- Rakennat **hyväksyntäportit** ja liität ne agentin päätöksiin
- Suunnittelet **työnkulkuja**, joissa agentti ja ihminen tekevät yhteistyötä
- Tallennat **palautteen** jokaisen hyväksynnän
- Lokit näyttävät, **mitä tapahtui ja miksi**
- Voit **kumota tai korjata** virheitä nopeasti

N8n:ssä näet visuaalisesti pisteitä, joissa työnkulku pysähtyy ja odottaa ihmisen hyväksyntää, ehtoja ("if X, then Y"), looppeja ("tee tämä kaikille asiakkaille") ja virheenkäsittelyä ("jos API epäonnistuu, mitä tehdään seuraavaksi").

Kun opit käyttämään n8n:ää, muista: **jokainen lohko, jonka vedät ruudulle, on vaihe agentin ajattelussa**. Hyväksyntälohko on piste, jossa agentti pysähtyy ja odottaa ihmisen sanaa. API-haku on vaihe, jossa agentti noutaa tietoa. Ehdolohko on vaihe, jossa agentti tekee päätöksen. Yhdessä nämä lohkot muodostavat toimivan agentin.

## Kohti omaa projektia

Tämä on viimeinen suunnitteluaskel ennen rakentamista. Sinulla on nyt kaikki viisi projektin aihiota: ongelma (oppitunti 19), muisti (oppitunti 21), päättelymalli (oppitunti 23), turvakerros (oppitunti 24) ja ihmisen rooli (tämä oppitunti). Yhdessä ne muodostavat kattavan suunnitelman, jonka pohjalta rakennat n8n-työnkulun oppitunneilla 26–27. Käy aihiot vielä kerran läpi ennen rakentamista ja varmista, että ne muodostavat yhtenäisen kokonaisuuden.

## Yhteenveto

Human-in-the-loop ei tarkoita "ihminen tekee kaiken" — se tarkoittaa "ihminen hyväksyy suuret päätökset ja ohjaa agenttia epäselvissä tilanteissa". Kolme sääntöä auttavat sinua valitsemaan, mitkä päätökset vaativat hyväksyntä: rahaa/rakennetta, epävarmuutta, poikkeamia. Hyväksyntäportit tehdään selkeiksi ja nopeiksi, jotta ihminen voi vastata ilman, että koko prosessi viivästyy. Koko prosessi on hybridi, jossa agentti ja ihminen tekevät yhteistyötä. Agentti oppii ihmisen palautteesta ja tekee parempia ehdotuksia myöhemmin. Seuraavissa oppitunneissa näet, kuinka n8n:llä **rakennat nämä työnkulut konkreettisesti** — vedät lohkoja, kytket hyväksyntäportit ja näet, kuinka automaatio ja inhimillinen ohjaus toimivat yhdessä. Tämä on tie, joissa yritykset tekevät automaatiosta oikeastaan **hyödyllista** — ei pelkästään nopeaa, vaan älykästä ja turvallista.
