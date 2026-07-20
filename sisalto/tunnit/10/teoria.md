# Kilpailuta tekoälyt — vertaa ennen kuin valitset

## Johdanto: vertailu on koe, ei mielipidekysymys

Tekoälypalvelut muuttuvat nopeasti. Yksittäinen malli, ominaisuus tai hinta voi vaihtua, mutta hyvän vertailun periaate säilyy. Siksi tällä tunnilla ei opetella ulkoa, mikä tuote on ”paras”. Opit rakentamaan pienen vertailukokeen, jonka perusteella voit valita tehtävään sopivan työkalun.

Vertailun lähtökohta on aina tehtävä. Sama palvelu voi onnistua hyvin yhdessä työssä ja heikosti toisessa. Työkalun maine, tuttuus tai sujuva vastaustyyli eivät vielä osoita, että se täyttää käyttötarkoituksen.

> **Tunnin ydinkysymys:** Millä samalla aineistolla, samoilla ehdoilla ja ennalta päätetyillä kriteereillä osoitat työkalun sopivuuden?

<figure class="ai-demo"><span class="ai-demo__tag">// sama koe — alkuperä piilossa arvioinnin ajan</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:286px">
  <div style="display:flex;align-items:center;gap:28px;width:700px;font-family:var(--font-mono)">
    <div style="flex:1;padding:24px;color:#eaf0ff;background:#11182a;border:1.5px solid #6f538e;border-radius:14px"><b>VASTAUS A</b><span style="display:block;margin-top:16px">5/5 ydinkohtaa</span><span style="display:block;margin-top:9px">2 kielikorjausta</span></div>
    <strong style="color:#6a309d;text-align:center">SAMAT<br>KRITEERIT</strong>
    <div style="flex:1;padding:24px;color:#eaf0ff;background:#11182a;border:1.5px solid #6f538e;border-radius:14px"><b>VASTAUS B</b><span style="display:block;margin-top:16px">3/5 ydinkohtaa</span><span style="display:block;margin-top:9px">2 sisältökorjausta</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Arvioi ensin vastaukset A ja B samoilla ennalta päätetyillä kriteereillä. Paljasta työkalut vasta arvioinnin jälkeen, jotta tuttu tuotemerkki ei ohjaa havaintoja.</figcaption></figure>

## Määritä ensin päätös

Ennen testiä kirjoita, mitä olet valitsemassa ja mihin käyttöön. ”Vertailen tekoälyjä” on liian väljä tavoite. Parempi muoto on:

> Valitsen työkalun, jolla muokataan 500 sanan ohje aloittelijalle sopivaksi. Tärkeintä ovat sisällön säilyminen, selkeys ja tarkistettavuus.

Päätöksen pitää sisältää:

- todellinen tehtävä
- käyttäjä tai yleisö
- käytettävä aineisto
- hyväksyttävä lopputulos
- ehdot, joiden täytyy täyttyä ennen laadun vertailua

## Erota porttiehdot ja laatukriteerit

Kaikkia työkaluja ei pidä edes ottaa mukaan laadulliseen vertailuun. **Porttiehto** ratkaisee, saako työkalua käyttää tehtävään.

Porttiehtoja voivat olla:

- organisaatio on hyväksynyt palvelun kyseiselle aineistolle
- aineisto mahtuu palvelun käsiteltäväksi
- tarvittava tiedostomuoto tai toiminto on käytettävissä
- käyttäjällä on tarvittava lisenssi ja käyttöoikeus
- palvelun käyttö täyttää saavutettavuuden tai muun pakollisen vaatimuksen

Jos porttiehto ei täyty, työkalu hylätään ennen vastausten pisteytystä. Kaunis vastaus ei korjaa sitä, ettei palveluun saanut syöttää aineistoa.

**Laatukriteeri** kertoo, kuinka hyvin hyväksytty työkalu hoitaa tehtävän. Esimerkiksi:

- faktat säilyvät oikein
- vastaus noudattaa annettua rakennetta
- kieli sopii kohderyhmälle
- lähteen ja päätelmän ero näkyy
- tulos tarvitsee vähän jälkikorjausta

Valitse kokeeseen 3–5 kriteeriä. Liian pitkä lista hajottaa huomion.

## Kirjoita kriteereille havaittavat kuvaukset

Pelkkä numero 1–5 ei kerro, mitä arvioija näki. Kuvaa etukäteen, mitä asteikon päät tarkoittavat.

| Kriteeri | Heikko tulos | Hyvä tulos |
| --- | --- | --- |
| Sisällön säilyminen | Olennaisia asioita puuttuu tai uusia väitteitä ilmestyy | Keskeinen sisältö säilyy eikä uusia faktoja keksitä |
| Kohderyhmälle sopivuus | Sanasto ja oletukset ovat liian vaikeita | Aloittelija ymmärtää tekstin ilman selittämätöntä erikoissanastoa |
| Rakenteen noudattaminen | Pyydetty muoto puuttuu | Vastaus noudattaa sovittua rakennetta |
| Jälkikorjauksen määrä | Tuotos vaatii olennaisen uudelleenkirjoituksen | Tarvitaan vain pieniä tyylikorjauksia |

Näin arvio perustuu näyttöön eikä siihen, mikä vastaus ”tuntuu parhaalta”.

## Hallitse vertailun muuttujat

Reilu vertailu pitää olennaiset olosuhteet samoina:

- sama prompti
- sama lähdeaineisto
- sama tavoiteltu vastausmuoto
- uusi keskustelu jokaiselle testille
- tiedossa oleva palvelu-, malli- tai käyttöympäristö
- sama arviointitaulukko

Täydellistä laboratoriokoetta ei tavallisessa käytössä synny. Ilmais- ja maksulliset versiot voivat erota, palvelut voivat käyttää eri oletusasetuksia ja mallit voivat muuttua testien välillä. Nämä erot pitää kirjata rajoituksiksi, ei unohtaa.

Jos vertailet vain yhden kerran, satunnaisuus voi vaikuttaa tulokseen. Tärkeässä valinnassa aja sama koe useammalla edustavalla aineistolla. Tämän tunnin pieni koe opettaa menetelmän; se ei todista työkalun yleistä paremmuutta.

## Arvioi vastaukset sokkona, jos mahdollista

Tuotemerkki synnyttää ennakko-odotuksia. Jos mahdollista, kopioi vastaukset dokumenttiin nimillä **A** ja **B** ennen pisteytystä. Arvioi ensin sisältö ja paljasta palvelut vasta sen jälkeen.

Sokkoutus ei poista kaikkia vinoumia, mutta se vähentää tutun brändin ja käyttöliittymän vaikutusta. Vielä parempi on pyytää toista ihmistä arvioimaan samat vastaukset samoilla kriteereillä ja vertailla havaintoja.

## Älä pyydä yhtä kilpailijaa tuomariksi

Tekoälyä voi käyttää kysymysten esittämiseen tai arviointitaulukon puutteiden etsimiseen. Sille ei kuitenkaan kannata antaa yksin päätösvaltaa siitä, mikä vastaus voitti. Mallin arvio voi suosia tiettyä kirjoitustapaa, olla epäjohdonmukainen tai muuttua promptin mukana.

Ihminen tekee lopullisen päätöksen ja vastaa siitä. Tekoäly voi auttaa haastamaan perustelun:

> ”Mikä havainto taulukostani ei vielä tue johtopäätöstäni?”

Tämä kysymys ohjaa arvioimaan omaa näyttöä sen sijaan, että malli valitsisi työkalun puolestasi.

## Kirjaa myös käytännön työ

Paras tekstivastaus ei aina tarkoita parasta työkalua. Valintaan vaikuttavat myös:

- kuinka helposti aineisto saadaan palveluun ja tulos takaisin
- voiko työn tehdä ilman tarpeetonta kopiointia
- miten käyttöoikeudet ja tiedot hallitaan
- paljonko tuloksen tarkistamiseen ja korjaamiseen kuluu aikaa
- mitä käyttö maksaa todellisella työmäärällä
- miten tulokset voidaan dokumentoida ja toistaa

Nämä eivät ole pysyviä tuotekohtaisia totuuksia. Ne tarkistetaan siinä käyttöympäristössä ja sillä käyttäjätilillä, jota päätös koskee.

## Tee rajattu johtopäätös

Hyvä johtopäätös ei kuulu: ”Työkalu A on paras tekoäly.” Se kuuluu:

> Tässä kokeessa työkalu A sopi paremmin aloittelijan ohjeen muokkaamiseen, koska se säilytti kaikki viisi sisältökohtaa ja noudatti rakennetta. Työkalu B vaati kahden puuttuneen kohdan palauttamisen. Koe ei osoita, kumpi on parempi muissa tehtävissä.

Johtopäätös kertoo:

- mihin tehtävään valinta koskee
- mikä näyttö ratkaisi valinnan
- mitkä porttiehdot täyttyivät
- mitä kokeesta ei voi päätellä
- milloin testi pitää uusia

## Yhteenveto

Työkalun valinta on pieni tutkimusprosessi:

1. määritä tehtävä ja päätös
2. tarkista porttiehdot
3. päätä laatukriteerit ennen vastausten näkemistä
4. käytä samaa promptia ja aineistoa
5. arvioi havaittava näyttö, mielellään sokkona
6. kirjaa käytännön työ ja rajoitukset
7. tee tehtäväkohtainen, rajattu johtopäätös

Tällä menetelmällä vertailu kestää paremmin myös sen, että palvelut ja mallit muuttuvat.

> **Lopuksi pohdittavaksi:** Mikä omassa vertailussasi voisi näyttää työkalujen erolta, vaikka se johtuisi todellisuudessa erilaisesta tilistä, asetuksesta tai satunnaisuudesta?

---

## Lähteet ja tarkistuspäivä

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST: Towards a Standard for Identifying and Managing Bias in Artificial Intelligence](https://www.nist.gov/publications/towards-standard-identifying-and-managing-bias-artificial-intelligence)

Tarkistettu 20.7.2026.
