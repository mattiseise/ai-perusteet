# Rakenna uudelleen käytettävä promptikortti

## Johdanto: hyvä prompti osoitetaan kokeella

Tunnilla 4 opit, että konteksti muuttaa vastausta. Nyt viet taidon käytäntöön yhdessä toistuvassa tehtävässä. Tavoitteena ei ole kerätä mahdollisimman monta näyttävää promptia, vaan rakentaa **yksi promptikortti**, jonka käyttötilanteen, toimivuuden ja rajat osaat perustella.

Promptikortti yhdistää kolme asiaa:

1. pysyvän ohjeen, jota käytät uudelleen
2. vaihtuvan aineiston, jonka lisäät joka käyttökerralla
3. laatukriteerit, joilla tarkistat vastauksen

Ajattele korttia työohjeena, jonka toinenkin ihminen voisi ottaa käyttöön. Pysyvä ohje kertoo, mikä työ tehdään ja millä ehdoilla. Vaihtuva aineisto tuo jokaiseen käyttökertaan uuden sisällön. Laatukriteerit puolestaan estävät hyväksymästä vastausta vain siksi, että se kuulostaa sujuvalta. Jos jokin näistä kolmesta puuttuu, korttia on vaikea käyttää johdonmukaisesti tai kehittää havaintojen perusteella.

> **Tunnin ydinkysymys:** Mikä yksi promptimuutos paransi vastausta — ja millä havainnolla osoitat vaikutuksen?

<figure class="ai-demo"><span class="ai-demo__tag">// yksi muutos kerrallaan — vaikutus jää näkyviin</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:286px">
  <div style="display:flex;align-items:center;gap:22px;width:720px;font-family:var(--font-mono)">
    <div style="flex:1;padding:22px;color:#fff;background:#11182a;border:1.5px solid #44517a;border-radius:14px"><b>VERSIO 1</b><span style="display:block;margin-top:15px">sama tehtävä</span><span style="display:block;margin-top:8px">sama syöte</span></div>
    <div style="padding:16px;text-align:center;color:#6a309d;background:#f4effc;border-radius:12px"><b>+ yksi<br>nimetty muutos</b></div>
    <div style="flex:1;padding:22px;color:#fff;background:#211832;border:1.5px solid #b887e0;border-radius:14px"><b>VERSIO 2</b><span style="display:block;margin-top:15px">samat kriteerit</span><span style="display:block;margin-top:8px">havaittu vaikutus</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Kun tehtävä, syöte ja arviointikriteerit pysyvät samoina, yhden promptimuutoksen vaikutusta voi arvioida. Jos kaikki vaihtuu samalla kertaa, syy jää arvaukseksi.</figcaption></figure>

## Valitse toistuva tehtävä, jonka osaat arvioida

Hyvä promptikortti ratkaisee rajatun tehtävän, joka toistuu samankaltaisena mutta saa joka kerta uuden aineiston. Esimerkiksi:

- viestin muuttaminen kolmeksi toimintakohdaksi
- muistiinpanojen muuttaminen kertauskysymyksiksi
- tekstiluonnoksen muokkaaminen tietylle yleisölle
- palautteiden jäsentäminen ennalta sovittuihin teemoihin.

Viikoittaisten kokousmuistiinpanojen muuttaminen toimintakohdiksi on hyvä esimerkki. Aineisto vaihtuu joka viikko, mutta haluttu työ pysyy samana: tehtävä, vastuuhenkilö ja määräaika poimitaan näkyviin. Sen sijaan ”auta minua työssäni” ei vielä kuvaa toistettavaa tehtävää eikä anna perustaa vastauksen arvioinnille.

Vältä tehtävää, jonka hyvyyttä et pysty itse arvioimaan. Jos et tunne aihetta tai oikeaa lopputulosta, et myöskään tiedä, paransiko promptin muutos vastausta.

Kirjoita tehtävä yhdellä lauseella:

> Muunnan **[vaihtuvan aineiston]** muotoon **[haluttu tuotos]**, jotta **[käyttäjä]** voi **[käyttötarkoitus]**.

## Erota pysyvä ohje ja vaihtuva syöte

Uudelleen käytettävässä promptissa kaikkea ei kirjoiteta joka kerta uudelleen. Pysyvä osa kertoo työn ja sen ehdot. Vaihtuva osa merkitään selkeästi esimerkiksi hakasulkeilla.

```text
Muuta alla oleva [LÄHDEAINEISTO] kolmeksi toimintakohdaksi.

Kohderyhmä: [YLEISÖ]
Käyttötarkoitus: [TARKOITUS]

Säilytä lähteen nimet, päivämäärät ja vastuut täsmällisinä.
Älä lisää tietoa, jota lähteessä ei ole.

Vastausmuoto:
1. tehtävä
2. vastuuhenkilö, jos lähteessä mainitaan
3. määräaika, jos lähteessä mainitaan

LÄHDEAINEISTO:
[LIITÄ VAIHTUVA AINEISTO TÄHÄN]
```

Kortti ei ole vain pitkä prompti. Sen pitää kertoa myös, milloin rakennetta käytetään ja milloin ei.

Esimerkin hakasulkeet tekevät vastuunjaon näkyväksi. Kortti ei arvaa yleisöä, tarkoitusta tai lähdeaineistoa, vaan käyttäjä täyttää ne joka käyttökerralla. Samalla pysyvät vaatimukset — kuten lähteen nimien ja määräaikojen säilyttäminen — pysyvät samoina. Juuri tämä erottaa uudelleen käytettävän rakenteen keskusteluun kerran kirjoitetusta pyynnöstä.

## Päätä laatukriteerit ennen ensimmäistä ajoa

Ilman ennalta päätettyjä kriteereitä arvio helposti mukautuu siihen, millaisen vastauksen malli tuotti. Valitse 2–4 havaittavaa ominaisuutta.

| Epämääräinen arvio | Havaittava kriteeri |
| --- | --- |
| ”Vastaus on parempi.” | Kaikki lähteen neljä tehtävää ovat mukana. |
| ”Teksti on selkeä.” | Jokainen kohta alkaa tekemistä kuvaavalla verbillä. |
| ”Malli käytti aineistoa hyvin.” | Vastaus ei lisää nimiä, lukuja tai määräaikoja. |
| ”Muoto on käyttökelpoinen.” | Vastauksen voi siirtää tehtävälistaan ilman rakenteen korjaamista. |

Kriteeri on käyttökelpoinen, kun toinenkin ihminen voisi tarkistaa sen samasta vastauksesta.

Kriteeri toimii siis pienenä sopimuksena ennen testiä. Kun päätät etukäteen, ettei mallin pidä keksiä puuttuvia määräaikoja, voit tarkistaa vastauksesta yksiselitteisesti, tapahtuiko näin. Jos arviointiperuste syntyy vasta vastauksen jälkeen, sitä on helppo muuttaa huomaamatta mallin tuotoksen eduksi.

## Tee kaksi vertailukelpoista versiota

Aja ensin versio 1 turvallisella aineistolla ja säilytä sekä prompti että vastaus. Arvioi vastausta valituilla kriteereillä. Nimeä yksi puute, jonka haluat korjata.

Muuta seuraavaksi vain yhtä asiaa. Voit esimerkiksi:

- täsmentää kohderyhmän
- lisätä vastausrakenteen
- lisätä lähteeseen pitäytymistä koskevan rajan
- määrittää puuttuvan tiedon käsittelyn.

Avaa uusi keskustelu ja aja versio 2 samalla aineistolla. Jos jatkat samassa keskustelussa, aiempi vastaus voi vaikuttaa tulokseen. Jos vaihdat aineiston, et enää testaa vain promptin muutosta.

Tämä on eri asia kuin tavallinen keskustelullinen hiominen, jossa käyttäjä muuttaa useita asioita kerralla ja tyytyy lopulta mieluisaan vastaukseen. Hallitussa kokeessa säilytät lähtötilanteen, jotta pystyt myöhemmin sanomaan, mikä muutos todennäköisesti vaikutti tulokseen.

## Kirjaa vaikutus havaintona

Hyvä johtopäätös nimeää muutoksen, tuloksen ja näytön:

> Lisäsin ohjeen ”älä lisää puuttuvia määräaikoja”. Versio 1 keksi kahdelle tehtävälle määräajan, mutta versio 2 merkitsi ne puuttuviksi. Muutos paransi lähdeuskollisuutta tällä aineistolla.

Huomaa rajaus: yksi testi ei osoita, että kortti toimii kaikilla aineistoilla. Se osoittaa, miten kortti toimi tässä kokeessa. Seuraava hyödyllinen testi käyttää erilaista mutta samaan tehtävään kuuluvaa syötettä.

Näin kortin kehittäminen jatkuu perustellusti. Ensimmäinen koe osoittaa yhden vaikutuksen, seuraava koe koettelee rakennetta uudella aineistolla ja versiohistoria säilyttää tiedon siitä, miksi korttia muutettiin. Kortti ei ole koskaan ”valmis totuus”, vaan dokumentoitu työväline, jonka käyttöalue tunnetaan.

## Korttiin kuuluu myös tunnettu raja

Kirjaa vähintään yksi tilanne, jossa korttia ei pidä käyttää sellaisenaan. Raja voi liittyä esimerkiksi:

- aineistoon, jota ei saa lähettää palveluun
- tehtävään, jossa tarvitaan alan asiantuntijan päätös
- poikkeavaan syötteeseen, jota ei ole testattu
- tilanteeseen, jossa lähde on puutteellinen tai ristiriitainen.

Tunnettu raja ei heikennä korttia. Se estää käyttämästä toimivaa rakennetta väärässä tehtävässä.

## Yhteenveto

Yksi testattu promptikortti on hyödyllisempi kuin suuri lista prompteja, joiden toimivuudesta ei ole näyttöä. Rajaa toistuva tehtävä, erota pysyvä ohje vaihtuvasta aineistosta, päätä laatukriteerit etukäteen ja muuta vain yhtä asiaa kerrallaan.

Tallenna korttiin versiot, vastaukset, havaittu vaikutus ja tunnettu raja. Tunnilla 17 hyödynnät toimivaksi osoitettua rakennetta botin järjestelmäpromptissa.

> **Lopuksi pohdittavaksi:** Mikä promptisi osa on aidosti uudelleen käytettävä — ja mikä pitää päättää uudelleen jokaisessa käyttötilanteessa?

---

## Lähteet ja tarkistuspäivä

- [NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Microsoft: Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering)

Tarkistettu 20.7.2026.
