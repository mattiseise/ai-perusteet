# Oppitunti 18 — Viimeistele ja esittele bottisi ★

## Mitä tällä tunnilla tapahtuu?

Tähän mennessä olet kerännyt kahdeksan tunnin aikana taidot ja kolme rakennuspalikkaa. Nyt avaat Microsoft Copilotin ja rakennat niistä toimivan, ammattimaisen botin: **projektin määrittelydokumentin sparrauskumppanin** juuri sinun ammattialallesi.

Tällä tunnilla et opi enää uusia teoreettisia käsitteitä botin rakentamisesta. Sen sijaan opit **yhdistämään** sen, mitä jo osaat. Tämä materiaali auttaa sinua siinä — se ei kerro tekoälystä lisää, vaan kertoo, miten rakennat botin, joka toimii oikeasti ja näyttää ammattilaisen kädenjäljen.

## Mikä on hyvä projektidokumenttibotti?

Hyvä botti on **ohjaava, ei kirjoittava**. Se ei tee dokumenttia käyttäjän puolesta — se auttaa käyttäjää tekemään dokumentin paremmin kuin yksin. Käyttäjän osaaminen ja vastuu kasvavat, ei katoa.

Hyvä botti eroaa "yleisestä ChatGPT:stä" kolmella tavalla:

1. **Se tietää kontekstin.** Et joudu joka kerta selittämään olevasi pelikoodaaja tai kyberammattilainen — botti tietää sen automaattisesti.
2. **Se ohjaa työnkulkua.** Botti tietää, missä järjestyksessä projektidokumentin osat kannattaa tehdä. Käyttäjän ei tarvitse muistaa rakennetta.
3. **Sillä on rajat.** Botti tietää, milloin sen pitää sanoa "tämä ei kuulu minulle, kysy oikealta ihmiseltä". Tämä on ammattimaisuutta — ei vajavaisuutta.

## Botin rakenne

Bottisi rakentuu neljästä komponentista. Käytä niitä työvaiheina:

1. **Suunnitelma (rakennuspalikka 2:sta).** Päätä kenelle botti on, mitä se osaa, mitä se ei tee. Tämä on botin "perustamisasiakirja". Ilman tätä botti kasvaa hallitsemattomasti.
2. **Järjestelmäprompti eli pääohje (rakennuspalikka 1:stä).** Tekstipätkä, jonka annat Copilotille ja joka määrittää, miten botti käyttäytyy. Tämä on botin "DNA".
3. **Tietopohja (rakennuspalikka 3:sta).** 3–5 dokumenttia, jotka annat botille luettavaksi. Tämä on botin "kirjasto" — siitä se ammentaa oman alasi tietoa.
4. **Testaus.** Et tunne bottiasi ennen kuin olet käyttänyt sitä oikealla projekti-idealla. Ensimmäisen iteraation jälkeen botti aina paljastaa, mikä siinä mättää.

## Järjestelmäpromptin kieli

Botin järjestelmäprompti on tärkein yksittäinen tekstipätkä, jonka kirjoitat tässä projektissa. Se määrittelee kaiken: persoonan, työnkulun, rajat. Tässä esimerkki kahdesta tasosta:

### Heikko järjestelmäprompti

> Olet ystävällinen tekoälyavustaja, joka auttaa käyttäjiä projektidokumentaation kanssa. Vastaa asiantuntevasti ja kohteliaasti.

**Mikä mättää:** Liian yleinen. Ei kerro alaa, ei työnkulkua, ei rajoja. Botti voi yhtä hyvin auttaa CV:n kirjoittamisessa kuin määrittelydokumentissa — eli ei erikoistu mihinkään.

### Vahva järjestelmäprompti

> Olet kokenut pelikoodausprojektien suunnitteluvalmentaja. Autat opiskelijoita laatimaan pelikoodausprojektin määrittelydokumentin alkuvaiheessa.
>
> Työnkulkusi on aina sama: ohjaat käyttäjää järjestyksessä kuuden osan läpi — (1) pelin pääidea, (2) kohderyhmä ja alusta, (3) ydinmekaniikat, (4) tekninen toteutus, (5) aikataulu, (6) riskit. Et siirry seuraavaan osaan ennen kuin nykyinen on käsitelty riittävän tarkasti.
>
> Et kirjoita dokumenttia käyttäjän puolesta. Kysyt aina tarkentavia kysymyksiä ja autat käyttäjää muotoilemaan vastauksensa ammattimaiseen muotoon. Käytät pelikoodauksen termejä (esim. game loop, asset, mekaniikka) etkä yleistä projektinhallintajargonia.
>
> Et anna oikeudellisia neuvoja etkä arvioi pelin kaupallista potentiaalia. Jos käyttäjä kysyy näistä, ohjaat häntä asiantuntijan luokse.

**Mikä toimii:** Konkreettinen rooli ("pelikoodausprojektien suunnitteluvalmentaja"). Strukturoitu työnkulku (kuusi osaa nimettynä). Selkeä toimintatapa ("et kirjoita puolesta"). Rajat ("ei oikeudellisia neuvoja"). Alakohtaiset termit. Botti tietää nyt tasan, mitä se tekee.

## Tietopohjan kuratointi

Tietopohja on kokoelma dokumentteja, jotka botti lukee ja joista se ammentaa tietoa. Tietopohjan kuratointi on käytännössä päättelyä:

- **Mitä botti tarvitsee tietääkseen?** Esim. miltä hyvä määrittelydokumentti näyttää, mitä riskejä alalla tyypillisesti on, mitä termejä käytetään.
- **Mistä saat luotettavaa materiaalia?** Oppikirjat, kurssin omat materiaalit, alan standardit, oman koulun esimerkkityöt — ei satunnaisia blogikirjoituksia.
- **Mikä on liian paljon?** 3–5 hyvää dokumenttia voittaa 20 keskinkertaista. Botti hukuttautuu liialliseen materiaaliin.

**Hyvä tietopohja oman alasi botille voi sisältää esim.:**

- Yksi malliesimerkki onnistuneesta projektidokumentista omalta alaltasi
- Tarkistuslista tai rakennepohja, jonka botti voi opettaa käyttäjälle
- Alasi yleisten riskien tai sudenkuoppien listaus
- Termistö ja sanasto, jotta botti puhuu oikeaa kieltä

## Testaus: kun botti on melkein valmis

Et tunne bottiasi, ennen kuin olet ajanut sen läpi oikealla projekti-idealla. Testivaihe paljastaa puutteet, joita et arvannut suunnittelussa. Hyvä testikeskustelu sisältää nämä:

1. **Normaali käyttötapaus.** Anna botille oikea, alasi tyypillinen projekti-idea. Käy keskustelu loppuun. Pääsetkö valmiiseen määrittelydokumenttiin?
2. **Hämärä käyttäjä.** Kuvittele aloittelija, joka ei tiedä mitä projektidokumentti edes on. Auttaako botti silti pääsemään liikkeelle?
3. **Rajalla oleva kysymys.** Kysy bottiltasi jotain, mikä on sen alueen ulkopuolella ("Voitko arvioida tämän projektin liikevaihtopotentiaalia?"). Tunnistaako se rajan ja ohjaako oikein?
4. **Yritys saada botti tekemään puolesta.** Pyydä bottia kirjoittamaan koko dokumentti suoraan. Pidätteleekö se ohjeitaan vai murtuuko?

Jos jokin näistä epäonnistuu, botti ei ole vielä valmis. Korjaa järjestelmäpromptia, lisää tietopohjaa tai tarkenna rajauksia — ja testaa uudelleen.

## Yleisimmät sudenkuopat

**1. Liian kiltti botti.**
Jos botti vain vastaa "hyvä kysymys!" ja toistaa käyttäjän sanat, se ei ohjaa. Lisää järjestelmäpromptiin velvoite kysyä tarkentavia kysymyksiä, antaa konkreettista palautetta, ja ohjata seuraavaan vaiheeseen.

**2. Liian yleinen botti.**
Jos botti kuulostaa samalta riippumatta siitä, oletko pelikoodaaja vai IT-tuki, järjestelmäpromptissa ja tietopohjassa ei ole tarpeeksi alasi erikoispiirteitä. Lisää termistöä ja konkreettisia esimerkkejä.

**3. Liian innokas botti.**
Jos botti kirjoittaa koko dokumentin käyttäjän puolesta heti ensimmäisellä viestillä, työnkulun ohjaus on jäänyt vajaaksi. Lisää järjestelmäpromptiin vaihe-vaiheelta -periaate ja kielto kirjoittaa kokonaista dokumenttia.

## Tarkistuslista ennen palautusta

Käy nämä läpi ennen kuin painat Palauta:

- [ ] Botin järjestelmäpromptissa on selkeä rooli, työnkulku ja rajat
- [ ] Botti puhuu oman alasi kieltä, ei yleisillä projektitermeillä
- [ ] Tietopohjassa on 3–5 hyvää, perusteltua dokumenttia
- [ ] Olen testannut botin vähintään yhdellä oikealla projekti-idealla loppuun saakka
- [ ] Botti tunnistaa rajansa eikä mene oman alueensa ulkopuolelle
- [ ] Olen iteroinut järjestelmäpromptin vähintään kahdesti — ensimmäinen versio ei ole vielä lopullinen
- [ ] Reflektioni kuvaa mitä opin, ei vain mitä tein
- [ ] Bottiin pääsee linkillä — arvioija voi testata sitä itse
- [ ] Olen ylpeä tästä botista — se on minun käsialaani

## Lopuksi

Projektidokumenttibotti on **näyttö osaamisestasi** — sekä kurssin sisällöstä että siitä taidosta, jota osio 3 lähtee syventämään: tekoälyn rakentamisesta toimimaan itsenäisesti. Et osoita osaamistasi sillä, että käytät tekoälyä. Osoitat sen sillä, että **rakennat tekoälyllä** jotain, mitä joku toinen voi käyttää.

Tämä on iso askel käyttäjästä rakentajaksi. Pidä siitä kiinni.

*Et opettele käyttämään tekoälyä. Opit rakentamaan sillä.*
