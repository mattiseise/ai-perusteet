# Oma botti I — käyttäjä, tehtävä ja rajat

## Johdanto: bottia ei aloiteta ohjetekstistä

Oman botin rakentaminen houkuttelee aloittamaan järjestelmäpromptista: kirjoitetaan botille rooli, muutama sääntö ja kokeillaan, mitä tapahtuu. Silloin tärkeimmät päätökset jäävät helposti tekemättä. Kenelle botti on tarkoitettu? Mitä käyttäjä yrittää saada aikaan? Missä tilanteessa botti auttaa — ja missä sen pitää lopettaa?

Tällä tunnilla et rakenna bottia etkä kirjoita valmista järjestelmäpromptia. Laadit **määrittelydokumentin**, jonka perusteella botin voisi myöhemmin rakentaa myös joku toinen. Suunnittelu erotetaan toteutuksesta tarkoituksella: ensin päätetään, millainen työkalu tarvitaan, vasta sitten kirjoitetaan ohjeet ja valitaan alusta.

Määrittely on lupaus tulevasta toiminnasta. Se kertoo, ketä autetaan, missä tehtävässä ja millä rajoilla. Kun nämä päätökset ovat näkyvissä, myöhempää bottia voidaan arvioida muullakin kuin kysymyksellä ”vaikuttaako tämä hyvältä?”. Ilman määrittelyä jokainen sujuva vastaus voi näyttää onnistumiselta, vaikka botti ratkaisisi väärää ongelmaa.

> **Tunnin ydinkysymys:** Mitä botin pitää auttaa tiettyä käyttäjää tekemään — ja mistä huomaat, että tehtävä onnistui?

<figure class="ai-demo"><span class="ai-demo__tag">// ennen toteutusta: tarve muuttuu arvioitavaksi määrittelyksi</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:286px">
  <div style="display:flex;align-items:center;gap:16px;width:740px;font-family:var(--font-mono);font-size:11px">
    <div style="flex:1;padding:22px 10px;text-align:center;color:#fff;background:#11182a;border:1.5px solid #6f538e;border-radius:13px"><b>KÄYTTÄJÄ</b><span style="display:block;margin-top:14px">kenellä on tarve?</span></div><b style="color:#863fc4">→</b>
    <div style="flex:1;padding:22px 10px;text-align:center;color:#fff;background:#11182a;border:1.5px solid #6f538e;border-radius:13px"><b>TEHTÄVÄ</b><span style="display:block;margin-top:14px">mitä hän tekee?</span></div><b style="color:#863fc4">→</b>
    <div style="flex:1;padding:22px 10px;text-align:center;color:#fff;background:#11182a;border:1.5px solid #6f538e;border-radius:13px"><b>ONNISTUMINEN</b><span style="display:block;margin-top:14px">mistä tulos näkyy?</span></div><b style="color:#863fc4">→</b>
    <div style="flex:1;padding:22px 10px;text-align:center;color:#fff;background:#11182a;border:1.5px solid #6f538e;border-radius:13px"><b>RAJAT</b><span style="display:block;margin-top:14px">milloin pysähdytään?</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Määrittely ei vielä ole järjestelmäprompti. Se kertoo, kenelle botti rakennetaan, mitä sen pitää saada aikaan ja millä ehdoilla myöhempi toteutus voidaan hyväksyä.</figcaption></figure>

## Aloita käyttäjän tilanteesta

Hyvä botti ratkaisee rajatun ongelman rajatussa tilanteessa. ”Opiskelubotti” on liian laaja lähtökohta. ”Kertauskaveri, joka auttaa ensimmäisen vuoden opiskelijaa tunnistamaan tietoverkkojen keskeiset käsitteet ennen koetta” kertoo jo käyttäjän, tilanteen ja tavoitteen.

Kuvaa käyttötapaus yhdellä virkkeellä:

> **[Käyttäjä]** tarvitsee apua **[tehtävässä]**, jotta hän voi **[saavutettava lopputulos]**.

Esimerkiksi:

> Kerhon uusi jäsen tarvitsee apua sääntöjen ja harjoitusaikojen löytämisessä, jotta hän osaa tulla ensimmäisiin harjoituksiinsa valmistautuneena.

Tämä virke toimii koko suunnitelman mittatikkuna. Jos myöhempi ominaisuus ei auta käyttäjää tässä tehtävässä, sitä ei ehkä tarvita.

Kerhon perehdytysbotissa tämä rajaus sulkee pois esimerkiksi yleisen harjoitusohjelman laatimisen ja henkilökohtaisen terveysneuvonnan. Ne voivat liittyä harrastukseen, mutta eivät uuden jäsenen tehtävään löytää säännöt, harjoitusaika ja ensimmäisen kerran valmistautumisohjeet. Rajaus pitää botin tietopohjan, keskustelun ja vastuun hallittavina.

## Määritä onnistuminen havaittavasti

”Botti auttaa hyvin” ei ole vielä arvioitava tavoite. Onnistuminen pitää kuvata niin, että sen voi myöhemmin testata.

Havaittava onnistuminen voi tarkoittaa esimerkiksi sitä, että:

- käyttäjä löytää vastauksen nimetystä tietopohjasta
- botti kysyy puuttuvan lähtötiedon ennen ehdotusta
- vastaus etenee ennalta sovitussa rakenteessa
- botti myöntää, ettei tietopohja kata kysymystä
- käyttäjä saa seuraavan konkreettisen askeleen

Kun onnistuminen on havaittava, tunnilla 15 voidaan kirjoittaa sitä koskevat testit ja tunneilla 17–18 voidaan tarkistaa, toteutuuko se oikeassa botissa.

Havaittava tavoite muuttaa myös keskustelun suunnittelua. Jos onnistuminen tarkoittaa, että uusi jäsen löytää oikean harjoitusajan ja seuraavan askeleen, botin pitää joko antaa nämä tiedot hyväksytystä lähteestä tai kertoa avoimesti, ettei lähde kata kysymystä. Pelkkä ystävällinen keskustelu ei silloin vielä riitä onnistumiseksi.

## Kuvaa keskustelun eteneminen

Botin **työnkulku** tarkoittaa tässä keskustelun loogista etenemistä, ei vielä teknistä automaatiota. Kirjoita 4–6 vaihetta, jotka kuvaavat käyttäjän matkan alusta hyödylliseen lopputulokseen.

Kertauskaverin eteneminen voisi olla:

1. kysy aihe ja tavoite
2. selvitä käyttäjän lähtötaso yhdellä kysymyksellä
3. selitä yksi käsite kerrallaan
4. anna lyhyt harjoituskysymys
5. anna palaute käyttäjän vastauksesta
6. ehdota seuraavaa harjoiteltavaa asiaa

Vaiheet eivät vielä ole järjestelmäprompti. Ne ovat vaatimus sille, mitä myöhemmän järjestelmäpromptin ja käyttöliittymän pitää saada aikaan.

Järjestys kertoo myös, milloin botti ei vielä voi vastata. Kertauskaveri ei esimerkiksi voi valita sopivaa harjoituskysymystä ennen kuin aihe ja lähtötaso ovat selvillä. Työnkulun tehtävä ei siis ole vain järjestää tekstiä siistiksi, vaan tehdä tarvittavat päätökset näkyviksi ennen toteutusta.

## Rooli ei ole sama asia kuin persoona

**Rooli** kertoo, mistä näkökulmasta botti auttaa. **Persoona ja äänensävy** kertovat, miltä vuorovaikutus tuntuu.

”Olet ystävällinen apuri” kuvaa lähinnä sävyä. ”Olet uusien jäsenten perehdyttäjä, joka käyttää vain kerhon hyväksyttyjä sääntöjä ja harjoitusaikoja” kertoo tehtävän, tiedollisen perustan ja vastuun.

Valitse ensin asiallinen rooli. Lisää sen jälkeen tehtävään sopiva viestintätapa:

- kannustava mutta ei ylikehuva
- selkeä mutta ei alentuva
- rauhallinen riskitilanteissa
- tiivis silloin, kun käyttäjä tarvitsee toimintaohjeen

Persoona ei korvaa asiantuntemusta, lähteitä tai rajoja. Se auttaa tekemään botin toiminnasta johdonmukaista ja käyttäjälle sopivaa.

Kerhon botin rooli voi olla ”uuden jäsenen perehdyttäjä, joka käyttää hyväksyttyjä sääntöjä ja aikatauluja”. Sen sävy voi olla rauhallinen, lämmin ja tiivis. Jos sävy poistetaan, tehtävä säilyy. Jos rooli ja lähdepohja poistetaan, jäljelle jää vain miellyttävästi kirjoittava yleisbotti.

## Rajat tekevät botista käyttökelpoisen

Rajaus ei ole luettelo kaikesta pahasta. Hyvä rajaus liittyy käyttötapaukseen ja kertoo myös, mitä botti tekee rajan tullessa vastaan.

Kirjoita rajat kolmesta suunnasta:

1. **Aiheen raja:** Mihin kysymyksiin botti ei vastaa?
2. **Toiminnan raja:** Mitä botti ei tee käyttäjän puolesta?
3. **Tiedon raja:** Mitä tietoa botti ei pyydä, tallenna tai arvaa?

Pelkkä ”älä vastaa aiheen ulkopuolelle” jättää käyttäjän tyhjän päälle. Parempi ohje on: ”Jos kysymys ei koske kerhon toimintaa, kerro rajaus yhdellä lauseella ja ohjaa käyttäjä kerhon yhteyshenkilölle.”

Käyttäjän näkökulmasta raja on osa palvelua. Jos hän kysyy vamman hoitamisesta, botti ei vain vaikene tai toista kieltoa. Se kertoo, ettei anna terveysneuvontaa, ja ohjaa käyttäjän asianmukaiseen apuun. Hyvä raja siis yhdistää kolme asiaa: ehdon, botin toiminnan ja turvallisen seuraavan askeleen.

## Tee myös tietotarpeet näkyviksi

Määrittely paljastaa, mitä botin pitää tietää. Kerhon perehdytysbotti saattaa tarvita säännöt, harjoitusajat, varusteluettelon ja yhteystiedot. Se ei tarvitse koko kerhon vuosikertomusta vain siksi, että dokumentti liittyy samaan organisaatioon.

Kirjaa määrittelyyn alustava luettelo tietotarpeista. Tunnilla 15 etsit niihin sopivat lähteet ja arvioit, mitä aineisto kattaa ja mitä ei.

Tietotarpeet seuraavat suoraan käyttäjän etenemisestä. Jos botin pitää kertoa harjoitusaika, varusteet ja yhteyshenkilö, jokaiselle tiedolle tarvitaan myöhemmin nimetty ja ajantasainen lähde. Jos määrittelyssä luvataan jotakin, jolle ei löydy luotettavaa tietopohjaa, lupausta pitää rajata ennen rakentamista.

## Määrittelydokumentti on päätösten ketju

Hyvä määrittely vastaa kuuteen kysymykseen:

| Päätös | Kysymys |
| --- | --- |
| Käyttäjä | Kuka tarvitsee apua ja missä tilanteessa? |
| Tehtävä | Mitä käyttäjä yrittää saada aikaan? |
| Onnistuminen | Mitä havaittavaa tapahtuu, kun botti auttaa oikein? |
| Eteneminen | Missä järjestyksessä botti ohjaa käyttäjää? |
| Rooli ja sävy | Millaisena asiantuntijana ja millä tavalla botti viestii? |
| Rajat | Mitä botti ei tee, ja miten se toimii rajan tullessa vastaan? |

Näiden päätösten jälkeen järjestelmäpromptin kirjoittaminen on myöhemmin muuntamista, ei arvailua. Tunnilla 17 kokoat määrittelyn, promptikortin toimivan rakenteen ja tietopohjan yhdeksi toteutukseksi.

Lue taulukkoa päätösketjuna, ei kuutena irrallisena kenttänä. Käyttäjän tilanne määrittää tehtävän, tehtävä määrittää onnistumisen, onnistuminen ohjaa keskustelun etenemistä ja rajat kertovat, milloin vastuu siirtyy botilta ihmiselle. Rooli ja sävy tukevat tätä kokonaisuutta, mutta eivät muuta sen tarkoitusta.

## Yhteenveto

Tällä tunnilla suunnittelet ennen rakentamista. Rajaat käyttäjän, tehtävän, havaittavan onnistumisen, keskustelun etenemisen, roolin, äänensävyn ja toiminnan rajat. Et vielä kirjoita valmista järjestelmäpromptia tai testaa omaa bottia.

Tunnin tuotoksena syntyy **rakennuspalikka 2: botin määrittelydokumentti**. Se kertoo, mitä tunnilla 17 rakennetaan ja millä perusteella toteutusta myöhemmin arvioidaan.

> **Lopuksi pohdittavaksi:** Voisiko toinen ihminen rakentaa määrittelysi perusteella saman botin kuin sinä? Jos ei, mikä päätös on vielä vain omassa päässäsi?

---

## Lähteet ja tarkistuspäivä

- [Microsoft: Plan your agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/plan-your-agent)
- [Nielsen Norman Group: Personas](https://www.nngroup.com/articles/persona/)

Tarkistettu 20.7.2026.
