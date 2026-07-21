# Harjoittele — Tietopohja ja testisuunnitelma

Päätät, mitä tulevan botin pitää tietää ja miten sen toimintaa myöhemmin koetellaan. Testit kirjoitetaan ennen rakentamista.

## Tehtävä 1/6 — tietopohjan laatu

```task
{"type":"match","title":"Kuratoidun tietopohjan osat","intro":"Yhdistä arviointikysymys siihen, mitä sillä tarkistetaan.","pairs":[{"a":"Luotettavuus","b":"Kuka aineiston on tuottanut ja millä perusteella siihen voi nojata?","explain":"Lähteen alkuperä vaikuttaa siihen, mihin sitä voi käyttää."},{"a":"Ajantasaisuus","b":"Onko tieto edelleen voimassa ja näkyykö päivitysajankohta?","explain":"Vanhentunut ohje voi tuottaa johdonmukaisesti väärän vastauksen."},{"a":"Kattavuus","b":"Sisältääkö aineisto tehtävän keskeiset tilanteet ja käsitteet?","explain":"Aukot pitää tunnistaa ennen käyttöönottoa."},{"a":"Rajaus","b":"Onko mukana vain tehtävään kuuluvaa, sallittua aineistoa?","explain":"Tarpeeton aineisto lisää kohinaa ja riskejä."},{"a":"Jäljitettävyys","b":"Voidaanko vastaus palauttaa nimettyyn lähteeseen ja sen kohtaan?","explain":"Tärkeä väite pitää voida tarkistaa."}],"summary":"Tietopohja on perusteltu valinta, ei tiedostojen varasto."}
```

## Tehtävä 2/6 — kolme erilaista testiä

```task
{"type":"classify","title":"Mitä testi koettelee?","intro":"Luokittele testisyötteet.","categories":["Positiivinen testi","Negatiivinen testi","Reunatapaus"],"items":[{"text":"Käyttäjä kysyy asian, johon hyväksytyssä tietopohjassa on selkeä vastaus.","answer":0,"explain":"Positiivinen testi tarkistaa tarkoitetun ydintoiminnan."},{"text":"Käyttäjä pyytää neuvoa aiheesta, joka on nimenomaisesti rajattu botin ulkopuolelle.","answer":1,"explain":"Negatiivinen testi tarkistaa, noudattaako botti rajojaan."},{"text":"Käyttäjä lähettää tyhjän viestin tai kesken jääneen kysymyksen.","answer":2,"explain":"Reunatapaus koettelee epätavallista mutta mahdollista syötettä."}],"summary":"Testit kattavat onnistumisen lisäksi rajat ja poikkeavan syötteen."}
```

## Tehtävä 3/6 — läpäisyehto

```task
{"type":"quiz","title":"Voiko testin oikeasti tarkistaa?","intro":"Valitse täsmällisin läpäisyehto.","items":[{"q":"Positiivinen testi koskee kerhon harjoitusaikaa. Mikä läpäisyehto on paras?","options":[{"text":"Vastaus antaa hyväksytystä ohjeesta oikean päivän ja kellonajan sekä nimeää lähteen; se ei keksi puuttuvaa paikkaa.","correct":true,"explain":"Ehto sisältää havaittavat vaatimukset ja rajaa keksityn tiedon pois."},{"text":"Vastaus on hyvä ja ystävällinen.","correct":false,"explain":"Hyvyyttä ei voi tarkistaa ilman havaittavia ehtoja."},{"text":"Vastaus näyttää suunnilleen oikealta.","correct":false,"explain":"Testi tarvitsee täsmällisen vertailukohdan."}]},{"q":"Botti vastaa testissä eri tavalla kuin odotit. Mitä teet testisuunnitelmalle?","options":[{"text":"Säilytän etukäteen perustellun odotuksen ja tutkin, vaatiiko toteutus, aineisto vai testi korjausta.","correct":true,"explain":"Testin tehtävä on paljastaa ero, ei mukautua automaattisesti toteutukseen."},{"text":"Muutan odotuksen heti vastaamaan botin toimintaa.","correct":false,"explain":"Silloin testi ei enää arvioi tavoiteltua toimintaa."},{"text":"Poistan testin, koska se epäonnistui.","correct":false,"explain":"Epäonnistuminen on hyödyllistä tietoa korjaustarpeesta."}]}],"summary":"Hyvä testi sisältää syötteen, odotetun toiminnan ja havaittavan läpäisyehdon."}
```

## Tehtävä 4/6 — suunnittele ennen toteutusta

```task
{"type":"reflect","title":"Yksi valmis testitapaus","intro":"Kirjoita testi botille, jota ei ole vielä rakennettu.","prompt":"Kirjoita testin tyyppi, käyttäjän syöte, odotettu toiminta ja täsmällinen läpäisyehto. Lisää lähde, josta tulos myöhemmin tarkistetaan.","placeholder":"Testityyppi…\nSyöte…\nOdotettu toiminta…\nLäpäisyehto…\nTarkistuslähde…","tips":["Älä käytä ehtoa 'vastaa hyvin'.","Kerro, mitä vastauksessa pitää näkyä.","Pidä odotus tallessa ensimmäiseen ajoon asti."],"summary":"Ennalta kirjoitettu testi tekee ensimmäisestä toteutuksesta arvioitavan."}
```

## Tehtävä 5/6 — tietopohjan aukko

```task
{"type":"reflect","title":"Mitä aineisto ei kata?","intro":"Tietopohjan raja kuuluu testisuunnitelmaan.","prompt":"Nimeä yksi käyttäjän mahdollinen kysymys, johon tietopohja ei vastaa. Kirjoita, miten botin pitäisi toimia ja millä testillä osoitat tämän toiminnan.","placeholder":"Tietopohjasta puuttuu…\nBotin pitäisi…\nTestaan sen näin…","tips":["Älä täytä aukkoa arvauksella.","Määritä vastuun siirtyminen.","Kirjoita havaittava läpäisyehto."],"summary":"Tunnettu aukko muutetaan rajaksi ja testiksi."}
```

## Tehtävä 6/6 — missä virhe syntyi?

```task
{"type":"classify","title":"Haku, vastaus vai käyttöoikeus?","intro":"Luokittele jokainen RAG-järjestelmän ongelma sen syntypaikan mukaan.","categories":["Hakuvaiheen virhe","Vastauksen muodostamisen virhe","Käyttöoikeusvirhe"],"items":[{"text":"Ajantasainen hinnasto on tietopohjassa, mutta haku tuo vanhan markkinointiesitteen.","answer":0,"explain":"Oikea lähde ei pääty mallin käyttöön."},{"text":"Haku löytää oikean hinnan 45 euroa, mutta vastaus ilmoittaa hinnaksi 40 euroa.","answer":1,"explain":"Lähde löytyi, mutta malli muodosti sen vastaisen vastauksen."},{"text":"Opiskelija saa vastaukseen vain henkilöstölle tarkoitetun sisäisen ohjeen.","answer":2,"explain":"Rajattu lähde päätyi väärän käyttäjän hakuun tai vastaukseen."},{"text":"Kysymykseen ei löydy mitään, vaikka hyväksytyssä FAQ:ssa on täsmällinen vastaus.","answer":0,"explain":"Hakuvaihe ei löytänyt olemassa olevaa tietoa."}],"summary":"Tietopohjan laatu ei yksin takaa onnistumista: testaa erikseen haku, muodostettu vastaus ja käyttöoikeusraja."}
```
