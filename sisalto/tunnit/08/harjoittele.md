# Harjoittele vastuullista käyttöönottoa

Harjoittelet datan edustavuuden, toimijaroolien ja ihmisen valvonnan arviointia. Tehtävät tarkistuvat heti, eikä kukaan arvioi vastauksiasi.

## Tehtävä 1/4 — käsitteet paikoilleen

```task
{"type":"match","title":"Käsitteet paikoilleen","intro":"Yhdistä käsite ja selitys.","pairs":[{"a":"Edustavuus","b":"Aineisto kuvaa riittävästi todellisia käyttäjiä ja käyttötilanteita.","explain":"Suuri aineisto ei vielä takaa edustavuutta."},{"a":"Tarjoaja","b":"Toimija saattaa järjestelmän markkinoille tai käyttöön omalla nimellään.","explain":"Tarjoaja vastaa säädöksessä omista velvollisuuksistaan."},{"a":"Käyttöönottaja","b":"Toimija käyttää järjestelmää omassa toiminnassaan.","explain":"Käyttöönottajalla on velvollisuuksia myös silloin, kun järjestelmä on ostettu muualta."},{"a":"Tekoälylukutaito","b":"Kyky käyttää tekoälyä tietoisesti ja tunnistaa sen rajat ja riskit.","explain":"Tarvittava osaaminen riippuu tehtävästä ja käyttötilanteesta."},{"a":"Ihmisen valvonta","b":"Osaava ihminen voi seurata, poiketa ehdotuksesta ja keskeyttää käytön.","explain":"Pelkkä hyväksymispainike ei vielä tee valvonnasta todellista."}],"summary":"Vastuullinen käyttö yhdistää edustavan datan, selvät roolit, osaamisen ja todellisen valvonnan."}
```

## Tehtävä 2/4 — mitä edustavuudesta puuttuu?

```task
{"type":"quiz","title":"Onko aineisto edustava?","intro":"Rekrytointimallia on opetettu yhden suuren kaupungin saman alan aiemmilla rekrytoinneilla.","items":[{"q":"Mikä on paras ensimmäinen kysymys ennen valtakunnallista käyttöä?","options":[{"text":"Kuvaako aineisto eri alueiden, taustojen ja uusien hakijaryhmien todellista hakijajoukkoa?","correct":true,"explain":"Edustavuus arvioidaan suhteessa tulevaan käyttöön."},{"text":"Onko aineistossa mahdollisimman monta riviä?","correct":false,"explain":"Määrä ei korjaa yksipuolista otantaa."},{"text":"Tuottaako malli vastauksen nopeasti?","correct":false,"explain":"Nopeus ei kerro aineiston edustavuudesta."}]},{"q":"Mikä testi tukee reiluuden arviointia?","options":[{"text":"Vertaa virhetyyppejä olennaisissa ryhmissä ja poikkeavissa tilanteissa.","correct":true,"explain":"Keskimääräinen tulos voi peittää ryhmien väliset erot."},{"text":"Testaa vain aineistolla, jolla malli opetettiin.","correct":false,"explain":"Opetusdata ei osoita yleistymistä uuteen käyttöön."},{"text":"Pyydä mallia itse kertomaan, onko se puolueeton.","correct":false,"explain":"Väite ei korvaa riippumatonta testausta."}]}],"summary":"Edustavuus ja reiluus arvioidaan todellisessa käyttökontekstissa, ei pelkän aineiston koon perusteella."}
```

## Tehtävä 3/4 — kenen vastuulla?

```task
{"type":"classify","title":"Tarjoaja vai käyttöönottaja?","intro":"Luokittele ensisijainen rooli tässä yksinkertaistetussa esimerkissä.","categories":["Tarjoaja","Käyttöönottaja"],"items":[{"text":"Yritys kehittää järjestelmän ja myy sen omalla nimellään.","answer":0,"explain":"Se saattaa järjestelmän markkinoille omalla nimellään."},{"text":"Oppilaitos käyttää ostettua järjestelmää hakijoiden arvioinnin tukena.","answer":1,"explain":"Oppilaitos käyttää järjestelmää omassa toiminnassaan."},{"text":"Organisaatio seuraa käyttämänsä järjestelmän tuloksia ja ilmoittaa vakavasta ongelmasta.","answer":1,"explain":"Seuranta kuuluu käyttöönottajan käytännön vastuisiin."},{"text":"Toimija laatii markkinoille tuomansa järjestelmän teknisen dokumentaation.","answer":0,"explain":"Dokumentaatio liittyy tarjoajan velvollisuuksiin."}],"summary":"Roolit jakavat velvollisuuksia, mutta vastuu ei katoa järjestelmän ostamisen yhteydessä."}
```

## Tehtävä 4/4 — ihmisen valvonta

```task
{"type":"reflect","title":"Millainen valvonta on todellista?","intro":"Kuvaa ihmiseen vaikuttava tekoälypäätös. Mitä valvojan pitää tietää, milloin hänen pitää poiketa ehdotuksesta ja miten päätöksen kohde voi pyytää oikaisua?","placeholder":"Kirjoita 3–5 virkettä...","minWords":20,"summary":"Ihmisen valvonta tarvitsee osaamista, aikaa, tietoa ja todellisen vallan muuttaa tai keskeyttää päätös."}
```
