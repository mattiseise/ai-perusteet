# Harjoittele — Muisti, konteksti ja tila

## Tehtävä 1/5 — käsitteet paikoilleen

```task
{"type":"match","title":"Mikä tieto kuuluu minne?","intro":"Yhdistä käsite ja kuvaus.","pairs":[{"a":"Konteksti-ikkuna","b":"Tieto, jonka malli näkee tässä suorituksessa.","explain":"Nykyhetken työpöytä, ei pysyvä arkisto."},{"a":"Pitkäkestoinen muisti","b":"Erilliseen varastoon myöhempiä suorituksia varten tallennettu tieto.","explain":"Tarvitaan vain, jos myöhempi tehtävä hyötyy aiemmasta tiedosta."},{"a":"Tila","b":"Rakenteinen tieto prosessin nykyisestä vaiheesta.","explain":"Esimerkiksi odottaa hyväksyntää tai valmis."},{"a":"Vektoritietokanta","b":"Varasto, josta haetaan merkitykseltään samankaltaista aineistoa.","explain":"Samankaltaisuus ei takaa, että tulos on tapaukseen osuva."},{"a":"Pysyvät toimintaperiaatteet","b":"Järjestelmäohjeet ja harnessin säännöt, jotka rajaavat toimintaa.","explain":"Ne eivät ole muistia tai koneen omia arvoja."}],"summary":"Pidä erillään se, mitä malli näkee nyt, mitä säilytetään myöhemmäksi, missä vaiheessa prosessi on ja mitkä säännöt rajaavat toimintaa."}
```

## Tehtävä 2/5 — mikä mekanismi?

```task
{"type":"classify","title":"Konteksti, muisti, tila vai sääntö?","intro":"Luokittele jokainen tilanne.","categories":["Konteksti","Pitkäkestoinen muisti","Tila","Toimintaperiaate"],"items":[{"text":"Agentti näkee käyttäjän juuri lähettämän kysymyksen.","answer":0,"explain":"Tieto kuuluu nykyiseen suoritukseen."},{"text":"Agentti hakee viime vuonna ratkaistun aiemman tapauksen.","answer":1,"explain":"Tieto säilyy suoritusten välillä."},{"text":"Pyyntö odottaa ihmisen hyväksyntää.","answer":2,"explain":"Tämä kertoo prosessin vaiheen."},{"text":"Agentti ei saa lähettää viestiä organisaation ulkopuolelle.","answer":3,"explain":"Kyse on toimintaa rajaavasta säännöstä, joka kannattaa toimeenpanna harnessissa."},{"text":"Vahvistus on jo lähetetty eikä sitä lähetetä uudelleen.","answer":2,"explain":"Tilamuuttuja estää toiminnon toistumisen."},{"text":"Asiakkaan aiempi valinta haetaan uutta käyntiä varten.","answer":1,"explain":"Kyse on myöhempää suoritusta varten säilytetystä tiedosta."}],"summary":"Muisti ja tila eivät ole sama asia, eikä turvasääntö ole muistettava asiakastieto."}
```

## Tehtävä 3/5 — minimimuisti

```task
{"type":"quiz","title":"Mitä kannattaa säilyttää?","intro":"Valitse turvallisin ja tehtävän kannalta perusteltu vaihtoehto.","items":[{"q":"Agentti hoitaa yhden kertaluonteisen tiivistyksen. Tarvitseeko se pitkäkestoista muistia?","options":[{"text":"Ei välttämättä; nykyisen suorituksen konteksti voi riittää.","correct":true,"explain":"Muistia ei lisätä ilman tehtävää."},{"text":"Kyllä, jokainen agentti tarvitsee pysyvän asiakashistorian.","correct":false,"explain":"Tämä kasvattaisi riskiä ilman hyötyä."}]},{"q":"Vektoritietokanta löytää samankaltaisen tapauksen. Mitä seuraavaksi?","options":[{"text":"Tarkista, onko tapaus oikeasti relevantti ennen kuin käytät sitä.","correct":true,"explain":"Samankaltaisuus ei ole sama kuin osuvuus."},{"text":"Käytä sitä suoraan, koska haku takaa oikean tuloksen.","correct":false,"explain":"Haku voi nostaa väärän tapauksen."}]},{"q":"Missä kriittinen kielto kannattaa toteuttaa?","options":[{"text":"Järjestelmäohjeen lisäksi harnessin oikeuksina tai tarkistuksina.","correct":true,"explain":"Tekninen raja ei jää mallin muistettavaksi."},{"text":"Vain agentin persoonakuvauksessa.","correct":false,"explain":"Persoonakuvaus ei toimeenpane oikeusrajaa."}]}],"summary":"Säilytä vain tarpeellinen tieto, tarkista haun osuvuus ja toteuta kriittiset rajat harnessissa."}
```

## Tehtävä 4/5 — muistipäätöksen järjestys

```task
{"type":"order","title":"Tarvitaanko pitkäkestoista muistia?","intro":"Järjestä päätökset niin, ettei muistia lisätä varmuuden vuoksi.","steps":["Nimeä myöhempi tehtävä, joka tarvitsee aiempaa tietoa.","Määritä pienin tieto, joka tehtävää varten pitää säilyttää.","Tarkista lupa, säilytysaika ja poistaminen.","Päätä haku- ja käyttöehdot harnessissa.","Testaa myös väärän tai vanhentuneen muistiosuman käsittely."],"missHint":"Aloita todellisesta myöhemmästä käyttötarpeesta, älä tietokannasta.","summary":"Muisti suunnitellaan tehtävän, minimoinnin ja hallintaehtojen kautta."}
```

## Tehtävä 5/5 — sääntö vai muistettava tieto?

```task
{"type":"reflect","title":"Pidä ohje ja muisti erillään","intro":"Kaikkea pysyvää ei pidä tallentaa muistiksi.","prompt":"Kirjoita yksi tieto, joka agentin kannattaa mahdollisesti muistaa myöhempää tehtävää varten, ja yksi toimintaperiaate, joka kuuluu järjestelmäohjeeseen tai harnessiin. Perustele ero.","placeholder":"Muistettava tieto…\nToimintaperiaate…\nEro…","tips":["Muisti palvelee myöhempää tehtävää.","Toimintaperiaate rajaa toimintaa kaikissa suorituksissa.","Kriittinen raja toimeenpannaan harnessissa."],"summary":"Pitkäkestoinen muisti säilyttää tehtävään tarvittavaa tietoa; pysyvät säännöt ohjaavat toimintaa."}
```
