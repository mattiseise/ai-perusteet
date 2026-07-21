# Harjoittele tekoälytuloksen arviointia

Harjoittelet hallusinaation tarkistamista sekä väärien positiivisten ja väärien negatiivisten tulkintaa. Tehtävät tarkistuvat heti, eikä kukaan arvioi vastauksiasi.

## Tehtävä 1/4 — käsitteet paikoilleen

```task
{"type":"match","title":"Käsitteet paikoilleen","intro":"Yhdistä käsite ja selitys.","pairs":[{"a":"Hallusinaatio","b":"Uskottavasti esitetty mutta mahdollisesti virheellinen tai keksitty väite.","explain":"Sujuvuus ei ole todiste totuudesta."},{"a":"Väärä positiivinen","b":"Tavallinen maksu pysäytetään petoksena.","explain":"Järjestelmä antaa hälytyksen, vaikka etsittyä tapausta ei ole."},{"a":"Väärä negatiivinen","b":"Petos pääsee läpi tavallisena maksuna.","explain":"Todellinen petos jää tunnistamatta."},{"a":"Osumatarkkuus","b":"Oikeiden petosten osuus kaikista petoshälytyksistä.","explain":"Mittari kertoo hälytysten osuvuuden."},{"a":"Kattavuus","b":"Löydettyjen petosten osuus kaikista todellisista petoksista.","explain":"Mittari kertoo, kuinka suuri osa petoksista löydettiin."}],"summary":"Virhetyypit ja mittarit vastaavat eri kysymyksiin. Niitä ei pidä vaihtaa keskenään."}
```

## Tehtävä 2/4 — petosmallin tulos

```task
{"type":"quiz","title":"Mitä luvut kertovat?","intro":"Tuhannesta maksusta kymmenen on petoksia. Malli löytää kahdeksan petosta ja pysäyttää lisäksi 42 tavallista maksua.","items":[{"q":"Kuinka monta väärää positiivista syntyy?","options":[{"text":"42","correct":true,"explain":"Nämä ovat tavallisia maksuja, jotka malli merkitsi petoksiksi."},{"text":"2","correct":false,"explain":"Kaksi on väärien negatiivisten määrä: kaksi petosta jäi löytymättä."},{"text":"50","correct":false,"explain":"50 on kaikkien hälytysten määrä."}]},{"q":"Mikä on mallin kattavuus?","options":[{"text":"80 prosenttia","correct":true,"explain":"Malli löysi kahdeksan kaikkiaan kymmenestä petoksesta."},{"text":"16 prosenttia","correct":false,"explain":"16 prosenttia on osumatarkkuus: kahdeksan oikeaa petosta 50 hälytyksestä."},{"text":"99 prosenttia","correct":false,"explain":"Korkea kokonaistarkkuus ei vastaa kysymykseen löydettyjen petosten osuudesta."}]},{"q":"Miksi kokonaistarkkuus voi johtaa harhaan?","options":[{"text":"Pienessä petosjoukossa lähes kaikki maksut voi luokitella tavallisiksi ja saada silti korkean luvun.","correct":true,"explain":"Harvinainen luokka voi jäädä kokonaan löytämättä, vaikka suurin osa kaikista tapauksista luokitellaan oikein."},{"text":"Kokonaistarkkuus mittaa vain käsittelyn nopeutta.","correct":false,"explain":"Se mittaa oikein luokiteltujen osuutta, ei nopeutta."},{"text":"Kokonaistarkkuus on aina sama kuin kattavuus.","correct":false,"explain":"Mittarit vastaavat eri kysymyksiin."}]}],"summary":"Petosmallia arvioidaan ainakin virhetyyppien, osumatarkkuuden, kattavuuden ja seurausten avulla."}
```

## Tehtävä 3/4 — kumpi virhe?

```task
{"type":"classify","title":"Väärä positiivinen vai väärä negatiivinen?","intro":"Luokittele tilanne.","categories":["Väärä positiivinen","Väärä negatiivinen"],"items":[{"text":"Tavallinen verkkokauppaostos estetään petosepäilyn vuoksi.","answer":0,"explain":"Hälytys syntyi ilman todellista petosta."},{"text":"Varastosta poistuva viallinen tuote hyväksytään tarkastuksessa kunnossa olevaksi.","answer":1,"explain":"Todellinen vika jäi tunnistamatta."},{"text":"Terve potilas ohjataan lisätutkimuksiin virheellisen hälytyksen vuoksi.","answer":0,"explain":"Järjestelmä ilmoitti löydöksestä, jota ei ollut."},{"text":"Todellinen petos luokitellaan tavalliseksi maksuksi.","answer":1,"explain":"Etsitty tapaus jäi löytymättä."}],"summary":"Positiivinen ja negatiivinen kuvaavat mallin antamaa luokkaa, eivät seurauksen hyvyyttä."}
```

## Tehtävä 4/4 — oma tarkistusraja

```task
{"type":"reflect","title":"Milloin ihminen tarkistaa?","intro":"Valitse jokin tekoälyä hyödyntävä käyttötilanne. Kuvaa, millainen virhe olisi vakava, mitä mittaria tai lähdettä käyttäisit ja milloin ihminen tarkistaisi tuloksen.","placeholder":"Kirjoita 3–5 virkettä...","minWords":20,"summary":"Luotettavuus ei ole vain mallin ominaisuus. Se syntyy tehtävään sopivasta näytöstä, tarkistusrajasta ja nimetystä vastuusta."}
```
