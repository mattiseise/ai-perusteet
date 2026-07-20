# Kuvat, ääni ja teksti — kun sanat eivät riitä

## Johdanto: anna mallille se havainto, jota tehtävä vaatii

Jos pyydät tekoälyä selittämään kaaviota mutta kuvailet kaavion vain muistisi varassa, osa tiedosta katoaa jo ennen kuin työ alkaa. Jos taas haluat korjata yhden virkkeen ja lähetät siitä epätarkan kuvakaappauksen, valitset tehtävään hankalamman aineistomuodon kuin tarvitset.

Tämän tunnin ajatus on yksinkertainen: **valitse aineistomuoto sen perusteella, mitä tekoälyn pitää havaita**. Kuva ei ole aina tekstiä parempi. Ääni ei ole aina kuvaa rikkaampi. Useampi aineisto ei automaattisesti paranna vastausta. Hyvä käyttäjä tunnistaa, mikä tieto on tehtävän kannalta olennaista ja missä muodossa se säilyy parhaiten.

> **Tunnin ydinkysymys:** Mitä mallin pitää nähdä, kuulla tai lukea, jotta se voi auttaa — ja mitä aineistosta ei pidä lähettää lainkaan?

<figure class="ai-demo"><span class="ai-demo__tag">// sama tieto kahdessa muodossa — eri havainnot säilyvät</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:286px">
  <div style="display:flex;align-items:center;gap:26px;width:700px;font-family:var(--font-mono)">
    <div style="flex:1;padding:24px;color:#eaf0ff;background:#11182a;border:1.5px solid #44517a;border-radius:14px"><b style="color:#8fa3ff">KAAVIO</b><span style="display:block;margin-top:20px">kehityssuunta näkyy nopeasti</span></div>
    <strong style="color:#2f46b0">Mitä tehtävä vaatii?</strong>
    <div style="flex:1;padding:24px;color:#eaf0ff;background:#11182a;border:1.5px solid #44517a;border-radius:14px"><b style="color:#8fa3ff">TAULUKKO</b><span style="display:block;margin-top:20px">tarkat arvot säilyvät</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Aineistomuoto ei ole koriste. Kaavio auttaa hahmottamaan suunnan, kun taas alkuperäinen taulukko säilyttää laskennassa tarvittavat arvot. Valinta tehdään tehtävän perusteella.</figcaption></figure>

## Multimodaalisuus tarkoittaa useita tietomuotoja

**Modaliteetti** tarkoittaa tietomuotoa, kuten tekstiä, kuvaa tai ääntä. **Multimodaalinen malli** pystyy käsittelemään useampaa kuin yhtä tietomuotoa. Se voi esimerkiksi lukea käyttäjän kysymyksen ja tarkastella siihen liitettyä valokuvaa.

Eri muodot säilyttävät eri asioita:

| Aineistomuoto | Mitä se säilyttää hyvin? | Mitä siitä voi kadota? |
| --- | --- | --- |
| Teksti | Tarkka sanamuoto, nimet, luvut ja muokattavuus | Ulkoasu, sijainti ja visuaaliset suhteet |
| Kuva | Sommittelu, sijainti, muodot, värit ja näkyvä kokonaisuus | Pienen tekstin tarkkuus ja kuvan ulkopuolinen tapahtuma |
| Taulukko | Rivien, sarakkeiden ja lukujen rakenne | Alkuperäisen tilanteen tai mittauksen tausta |
| Ääni | Puhe, tauot, ääntämys ja keskustelun ajallinen kulku | Puhujan tarkoitus ei selviä varmasti pelkästä äänensävystä |
| Dokumentti | Pitkä rakenne, otsikot, kappaleet ja lähdeyhteys | Skannatun tai huonosti jäsennetyn tiedoston sisältö voi tulkkiutua väärin |

Valinta alkaa kysymyksestä, ei tiedostosta. Jos haluat mallin arvioivan painikkeiden sijoittelua, kuva on olennainen. Jos haluat muokata painikkeen tekstiä, kopioitu teksti on tarkempi. Jos haluat tarkastella myynnin kehitystä, alkuperäinen taulukko on usein parempi kuin kuva pylväsdiagrammista.

## Teksti sopii tarkkaan sisältöön ja muokkaamiseen

Käytä tekstiä, kun sanamuodon, lukujen tai rakenteen pitää säilyä täsmällisenä. Tekstiä voi lainata, hakea, vertailla ja muokata suoraan.

Hyviä tekstimuotoisia aineistoja ovat esimerkiksi:

- viesti, jonka sävyä tai rakennetta haluat muuttaa
- ohje, josta haluat selkokielisen version
- taulukon yksittäiset arvot, joiden perusteella lasketaan
- virheilmoituksen tarkka sanamuoto
- koodi tai muu rakenteinen teksti, jota pitää muokata rivi riviltä

Pelkkä aineisto ei kuitenkaan kerro tavoitetta. Lisää aina lyhyt tehtävänanto: mitä aineistosta tarkastellaan, kenelle tulos tehdään ja missä muodossa vastaus tarvitaan.

## Kuva sopii näkyvien suhteiden tarkasteluun

Kuva on hyödyllinen silloin, kun ongelma sijaitsee asioiden välisissä suhteissa: mikä on minkä vieressä, mikä puuttuu, miten kokonaisuus on jäsennelty tai mitä ympäristössä näkyy.

Esimerkkejä:

- sovelluksen painikkeet menevät päällekkäin
- kaavion asteikko tai selite on epäselvä
- laitteen merkkivaloista pitäisi päätellä käyttötila
- pakkauksen ohjeessa kuva ja teksti muodostavat kokonaisuuden
- käsin kirjoitetun muistiinpanon rakenne pitää tulkita

Hyvä kuvapyyntö kertoo kolme asiaa:

1. **Tilanne:** Mistä kuva on ja miksi se on otettu?
2. **Kohde:** Mitä kohtaa mallin pitää tarkastella?
3. **Tehtävä:** Mitä haluat mallin selittävän, vertaavan tai ehdottavan?

Esimerkiksi: ”Tämä on kuvakaappaus ilmoittautumissivusta puhelimella. Tarkastele vain lomakkeen rakennetta. Mitkä kaksi kohtaa vaikeuttavat käyttäjän etenemistä? Älä päättele kuvasta henkilön ominaisuuksia.”

## Taulukko on usein kuvaa parempi numeroille

Kaavio näyttää kehityksen nopeasti, mutta alkuperäinen taulukko kertoo arvot tarkemmin. Jos tehtävä vaatii laskemista, poikkeamien etsimistä tai rivien vertailua, anna taulukko mieluiten rakenteisessa muodossa.

Voit yhdistää muodot tarkoituksellisesti:

- kuva kaaviosta näyttää esitystavan
- taulukko antaa tarkat arvot
- teksti kertoo, mitä päätöstä varten analyysi tehdään

Tämä ei tarkoita, että mukaan lisätään kaikki mahdollinen aineisto. Jokaisella liitteellä pitää olla nimetty tehtävä.

## Ääni säilyttää ajallisen kulun

Ääntä kannattaa käyttää, kun kiinnostuksen kohde on puheessa tai tapahtumien järjestyksessä. Esimerkiksi ääntämisen harjoittelu, kokouksen puheenvuorojen jäsentäminen tai haastattelun litterointi perustuvat tietoon, jota pelkkä jälkikäteen kirjoitettu yhteenveto ei säilytä.

Ääni ei kuitenkaan ole varma ikkuna ihmisen tunteisiin tai tarkoituksiin. Malli voi tulkita tauon, painotuksen tai puhujan asenteen väärin. Siksi turvallinen tehtävä kohdistuu havaittavaan asiaan:

- ”Kirjoita puhe tekstiksi ja merkitse epäselvät kohdat.”
- ”Tunnista, missä kohdissa puhuja vaihtaa aihetta.”
- ”Vertaa ääntämystä tähän annettuun malliin.”

Vältä perusteettomia päätelmiä puhujan terveydestä, luonteesta, rehellisyydestä tai tunnetilasta.

## Vertailukoe paljastaa, mitä aineisto lisää

Tämän tunnin tehtävässä annat saman ongelman ensin sanallisesti ja sitten kuvan kanssa. Kokeen tarkoitus ei ole todistaa, että kuva voittaa. Tarkoitus on tunnistaa, **mitä uutta havaittavaa tietoa kuva toi**.

Pidä muut asiat mahdollisimman samoina:

- sama tehtävä
- sama taustatieto
- sama tavoiteltu vastausmuoto
- mahdollisuuksien mukaan sama malli ja keskustelun lähtötilanne

Vertaa vastauksia nimetyillä kriteereillä. Löysikö kuvaan perustuva vastaus sellaisen suhteen, jota tekstikuvaus ei sisältänyt? Lukiko malli pienen tekstin väärin? Keskittyikö se epäolennaiseen yksityiskohtaan? Hyvä johtopäätös voi olla myös se, että huolellinen tekstikuvaus riitti paremmin.

## Enemmän aineistoa ei tarkoita parempaa vastausta

Ylimääräinen aineisto voi lisätä kohinaa, kuluttaa konteksti-ikkunaa ja ohjata huomion pois olennaisesta. Valitse pienin aineistokokonaisuus, joka säilyttää tehtävässä tarvittavan tiedon.

Kysy jokaisesta liitteestä:

- Mitä sellaista tämä tuo, mitä muissa aineistoissa ei ole?
- Tarvitaanko koko tiedosto vai riittääkö rajattu kohta?
- Voiko tarkka sisältö antaa tekstinä kuvan sijaan?
- Miten tarkistan mallin tekemän tulkinnan?

## Turvallisuus ratkaistaan ennen lähettämistä

Kuva voi sisältää nimiä, kasvoja, osoitteita, ilmoituksia ja avoimia välilehtiä. Äänite voi sisältää sivullisten puhetta. Dokumentin metatiedoissa tai taulukon piilotetuissa sarakkeissa voi olla tietoa, jota et huomaa ensisilmäyksellä.

Ennen lähettämistä:

1. varmista, että aineiston käyttö on sallittu
2. rajaa mukaan vain tehtävässä tarvittava osa
3. poista henkilötiedot, salaisuudet ja tarpeettomat tunnisteet
4. tarkista myös kuvan reunat, tiedoston muut välilehdet ja äänen taustapuhe
5. käytä organisaation hyväksymää palvelua

Pelkkä peittäminen ei aina riitä, jos alkuperäinen tieto jää tiedostoon palautettavaksi. Tee jaettavaan käyttöön erillinen kopio ja tarkista se ennen lähettämistä.

## Mallin havainto pitää edelleen tarkistaa

Multimodaalinen malli voi lukea tekstin väärin, sekoittaa kaavion sarjat, jättää osan kuvasta huomiotta tai litteroida nimen virheellisesti. Siksi vastaus ei ole todiste aineistosta.

Tarkista tärkeä havainto alkuperäisestä materiaalista. Pyydä mallia tarvittaessa osoittamaan, mihin kuvan kohtaan, taulukon riviin tai äänitteen aikaleimaan havainto perustuu. Jos perustetta ei löydy, älä käytä väitettä päätöksen pohjana.

## Yhteenveto

Valitse aineistomuoto tehtävän mukaan:

- teksti tarkkaan sisältöön ja muokkaamiseen
- kuva näkyviin suhteisiin ja kokonaisuuteen
- taulukko lukuihin ja rakenteiseen vertailuun
- ääni puheen ja ajallisen kulun tarkasteluun
- dokumentti pidempään lähdeaineistoon

Yhdistä muotoja vain silloin, kun jokainen tuo tehtävään oman tarpeellisen havaintonsa. Rajaa aineisto, suojaa tiedot ja tarkista mallin tulkinta alkuperäisestä lähteestä.

> **Lopuksi pohdittavaksi:** Minkä tiedon menetät, jos muutat aineiston toiseen muotoon — ja onko juuri se tieto tehtäväsi kannalta olennainen?

---

## Lähteet ja tarkistuspäivä

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [W3C: Making Audio and Video Media Accessible](https://www.w3.org/WAI/media/av/)

Tarkistettu 20.7.2026.
