# Etiikka, tekijänoikeudet ja ympäristövaikutukset

## Johdanto

Olet juuri käyttänyt ChatGPT:tä kirjoittamaan asiakkaalle raportin. Raportti on erinomainen. Asiakkaasi on tyytyväinen. Pari viikkoa myöhemmin huomaat, että samantyyppinen raportti ilmestyi kilpailija-yrityksen sivuille. Miten se mahdollista oli? Vai huolet: ChatGPT koulutettiin sivustojesi teksteillä — ilman kysymistä, ilman korvausta. Nyt kilpailijoilla on sama "oppi" saatavilla.

Tai: Käytät ChatGPT:tä asiakaspalvelussa. Malli on opetettu miljoonista asiakaspalvelun teksteistä, joiden kirjoittajat eivät tienneet, että heidät "kuunnellaan" koulutusta varten. Monet heistä ovat globaalissa etelässä: Bangladeshin merkintätyöntekijät, jotka saivat 2 dollaria tunti merkitsemään kuvia AI:tä varten. Heidät kouluttivat mallia, jonka tulot menevät Silicon Valleyyn.

Tai: Tietokeskus, joka ajaa ChatGPT:tä käyttää yhtä paljon vettä kuin 50 amerikkalaista kodissa vuodessa. Vesi tulee paikallisesta joesta. Joella ei enää ole riittävästi vettä kastelun jälkeen.

Nämä ovat eettisiä kysymyksiä — ja ne eivät ole marginaalisia. Ne ovat tekoälyn sydämessä.

## Tekijänoikeudet ja koulutusdata

Kun ChatGPT vastaa sinulle, se käyttää tietoa, jonka sille opetettiin. Mutta mistä tieto tulee? Vastauksena: miljaardeista teksteistä Internetistä — ja niiden tekijöille ei ole maksettua.

ChatGPT on opetettu miljaardeilla sanoilla. Paljon niistä tulevat verkkosivustoilta, blogeista, kirjoista, tieteellisistä artikkeleista. Kirjoittajat — journalistit, kirjailijat, tutkijat, bloggaajat — eivät koskaan antaneet lupaa. OpenAI yksinkertaisesti latasi tekstit ja opetti mallia.

Tämä on johtanut oikeustapauksiin. Kirjailijoiden yhdistys on nostanut kanteen, että OpenAI varastaa teoksia. Kuvataiteilijat ovat nostanut kanteen, että Midjourney ja Stability AI koulutettiin heidän kuviensa avulla. Näissä tapauksissa logiikka on sama: "Teidän työkalut on opetettu meidän luomuksilla ilman lupaa ja ilman korvausta."

Juridisesti tämä on sekava. Tekijänoikeuslaissa on "reilu käyttö" (fair use) -käsite, joka joskus sallii datan käytön ilman lupaa, jos se on "transformatiivista". Onko kielimallin koulutus "transformatiivista"? Tuomioistuimet näyttävät erimielisiltä.

Mutta eettisesti se on selkeä: tekijät eivät ole suostuneet tai saaneet korvausta. Kun käytät tekoälyä ammattilaisesti ja tiedät tämän, sinulla on vastuu. Ei riittää sanoa "OpenAI teki sen". Sinä käytät mallia, sinä vastaat.

> **Pysähdy hetkeksi:** Kuvittele, että kirjoitit artikkelin blogiin. Ilman tietäväsi se päätyi ChatGPT:n koulutusdata. Nyt ChatGPT tuottaa tekstiä, joka muistuttaa sinua. Kuinka sinulle tuntuisi? Pitäisikö sinulla olla oikeus tietää ja halutessaan kieltää pääsy tekstiinsi?

## Algoritminen harha: kuka päättelee oikein?

Algoritminen harha (algorithmic bias) on tilanne, jossa AI:n päätökset diskriminoivat tiettyä ryhmää.

Konkreettinen esimerkki: Amazon kehitti rekrytointialgoritmia, joka käytti historiallista palkkaamistietoa opetukseen. Koska historiassa oli enemmän miehiä teknologia-alalla, algoritmi oppi: "miehen valmistuminen = hyvä, naisen valmistuminen = huono". Algoritmi hylkäsi naisista hakijoita. Amazon lopetti algoritmin.

Miten näin käy? Koska kielimallit oppivat kuvioista datassa. Jos data heijastaa historiallista syrjintää, malli oppii syrjinnän. Se ei ole mallin "rasismi" — se on historiallisen datan ohjaavaisuus.

Toinen esimerkki: kasvojen tunnistusalgoritmit ovat huonompia tummaihoisille ihmisille kuin vaaleaihoisille. Miksi? Koska koulutusdata sisälsi enemmän vaaleaihoisista. Algoritmi oli "puolueellinen" siksi, koska sen opettajat valitsivat väärin datasta.

Ammattilaisena, sinun on tiedettävä: **jos käytät AI:ta päätöksiin, jotka vaikuttavat ihmisiin (palkkaus, luottotarina, oikeusisto), sinun on tutkittava, millä datalla se on opetettu ja mitä harhoja sillä voi olla.**

> **Pysähdy hetkeksi:** Kuvittele, että organisaatiosi käyttää tekoälyä palkkaamisen seulontaan ja se systemaattisesti siivilöi pois tiettyä etnistä ryhmää. Kuka on vastuussa? Tekijät? Organisaatio? Sinä, joka päätit ottaa algoritmin käyttöön?

## Datan merkitsijät: globaali työssä

Monet eivät tiedä, että AI:n opetukseen tarvitaan, että ihmisten merkkaa tietoja. "Merkkääminen" tarkoittaa kertomalla mallille, mitä kuva sisältää ("tämä on kissa"), mitä teksti kertoo ("tämä on negatiivinen arvostelu"), jne.

Tämä merkkäämistyö tehdään usein globaalin etelässä — Bangladeshissa, Intiassa, Filippiineillä — joissa palkat ovat alhaiset. Työntekijät istuvat tietokoneille ja merkitsevät kuvia. He saavat 2–5 dollaria tunti. He eivät tiedä, mihin dataa käytetään — usein "sopimukset" kieltävät heille sanomasta.

Joskus työ on traumaattista. Koska merkintätyö usein sisältää väkivaltaisia, seksuaalisesti hyväksikäytettäviä tai muita inhimillisiä kuvia, joita "puhdistetaan" datasta. Näiden ihmisten mielenterveys kärsii — ja he saavat minimipalkkaa.

Kun käytät ChatGPT:tä, käytät mallia, jonka opetukseen osallistuivat nämä ihmiset. Et näe heitä. Organisaatiosi ei maksa heille. Mutta heidän työnsä mahdollistaa sinun tuottavuutesi.

Ammattilaisena eettinen vastuu on: **tiedä, mistä mallit tulevat. Tiedä, kuka opetti ne. Ja pidä se mielessä, kun käytät niitä.**

## Ympäristövaikutukset

Tekoäly vaatii energiaa. Paljon energiaa.

Yksi ChatGPT-query käyttää vähintään 0,29 wattituntia sähköä. Tämä kuulostaa pieneltä. Mutta kun OpenAI käsittelee 200 miljoonaa kyselyä kuukaudessa, se vaatii valtavan määrän sähkötä.

Tämän sähkön pitää tulla jostain. OpenAI väittää käyttävänsä uusiutuvia energialähteitä, mutta totta se on: data-keskuksilla on jäätävät sähkötarpeet. Yksittäinen data-keskus voi käyttää enemmän sähköä kuin pieni kaupunki.

Entä vesi? Datakeskukset jäähdyttelevät palvelimia veden avulla. OpenAI:n data-keskus Texasissa käyttää arviolta 37 miljoonaa gallonaa vettä vuodessa. Texaskaan ei ole vesinnäkymä — Texas kuivuu.

Ja valmistus. Tekoälymallin opettamiseen tarvitaan erityisiä siruja (GPU:t), joiden valmistus kuluttaa energiaa ja vettä. Näiden sirujen louhinta vaatii mineraalien louhintaa.

Ammattilaisesti merkitsee se: **jokainen kerta kun käytät tekoälyä, sinulla on pieni vesijalanjälki ja sähköjalanjälki. Jos organisaatiosi käyttää massiivisesti tekoälyä, nämä jalanjäljet kasautuvat.**

Tämä ei ole syy boikotoida tekoälyä. Mutta se on syy käyttää sitä harkiten.

> **Pysähdy hetkeksi:** Jos käyttäisit tekoälyä miljoonista kyselyistä päivässä organisaatiossasi, kuinka mieltä olisi, kun ymmärrät, että se kuivattaa paikallista vesivarantoa?

## Vastuullinen käyttö ja professionaalinen etiikka

Mitä tämä merkitsee ammattilaisena?

1. **Tiedä, mistä data tulee.** Jos käytät tekoälypalvelua, etsi niiden tietosuojakäytäntöjä ja opetusdata-lähteistä. Valitsemalla palvelun, joka on läpinäkyvä, tuet vastuullisia käytäntöjä.

2. **Tiedä, mitä harjoja mallilla voi olla.** Jos käytät tekoälyä päätöksiin (esim. palkkaus, krediitti), testaa sitä vinoutumisuuden varalta. Pyydä tilastotieteilijä tai etiikkaspesialisti analysoimaan.

3. **Dokumentoi käyttö.** Jos organisaatiosi käyttää tekoälyä, dokumentoi se: miksi, mihin tarkoitukseen, millä datalla, mitä vaaroja on huomioitu.

4. **Käytä harkiten.** Älä käytä tekoälyä jokaiseen tehtävään. Käytä sitä silloin, kun se on perusteltua. Jotkut tehtävät ovat liian tärkeitä hallusinaatioille, jotkut liian arkaluontoiset datan yksityisyydelle.

5. **Puhu äänellä.** Jos organisaatiosi käyttää tekoälyä vastuuttomasti, ota kantaa. Ammattilaiset ovat ne, jotka ymmärtävät riskit.

## Yhteenveto

Tekoäly ei ole neutraali työkalu. Se on rakennettu tekijöillä, jotka eivät ole saaneet lupaa tai korvausta. Sen opetukseen osallistuivat ihmisiä, jotka saivat minimipalkkaa. Se on harhainen historiallisen datan kautta. Se kuluttaa merkittäviä ympäristöresursseja.

Ammattilaisena ei riitä, että käytät tekoälyä hyvin — teknisesti. Sinulla on vastuu ymmärtää, mitä näiden valintojen takana on, ja tehdä eettisiä valintoja sen tiedon kanssa. "Kaikki käyttävät sitä" ei ole eettinen perustelu. Ammattilaisuus tarkoittaa sitä, että ajattelet syvemmin.
