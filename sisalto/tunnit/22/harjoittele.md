# Harjoittele: Agentin työkalut ja rajat

## 1. Käsitteet paikoilleen

```task
{"type":"match","title":"Käsitteet paikoilleen","intro":"Yhdistä käsite ja sitä kuvaava selitys.","pairs":[{"a":"Työkalu","b":"Rajattu tapa hakea tietoa tai tehdä toiminto agentin puolesta.","explain":"Kielimalli pyytää työkalua, mutta agentin ohjauskehys tarkistaa ja suorittaa pyynnön."},{"a":"Työkalusopimus","b":"Kuvaus työkalun tarkoituksesta, syötteestä, tuloksesta, rajoista ja virheistä.","explain":"Sopimus tekee toiminnasta ennakoitavaa ja testattavaa."},{"a":"Minimioikeusperiaate","b":"Työkalulle annetaan vain tehtävän vaatima pääsy.","explain":"Jokainen ylimääräinen oikeus kasvattaa mahdollisen vahingon laajuutta."},{"a":"Hyväksyntäportti","b":"Kohta, jossa ihminen päättää ennen kriittistä toimintoa.","explain":"Hyväksyntä tarvitaan ennen peruuttamatonta tai muuten merkittävää toimintoa."}],"summary":"Työkalu on rajattu toiminto. Työkalusopimus, minimioikeudet ja hyväksyntäportit määräävät, miten sitä käytetään turvallisesti."}
```

## 2. Valitse turvallinen ratkaisu

```task
{"type":"quiz","title":"Valitse turvallinen ratkaisu","intro":"Valitse vaihtoehto, joka rajaa työkalun käytön parhaiten.","items":[{"q":"Agentti valmistelee asiakkaalle viestin. Mitä sille kannattaa sallia ensimmäisessä versiossa?","options":[{"text":"Viestiluonnoksen tekeminen, jonka ihminen tarkistaa ennen lähetystä.","correct":true,"explain":"Luonnos antaa hyödyn ilman, että agentti saa itsenäisen lähetysoikeuden."},{"text":"Kaikkien viestien lähettäminen ilman tarkistusta.","correct":false,"explain":"Laaja lähetysoikeus kasvattaa virheen seurauksia tarpeettomasti."},{"text":"Pääsy kaikkiin asiakasrekisterin tietoihin varmuuden vuoksi.","correct":false,"explain":"Minimioikeusperiaate rajaa pääsyn vain tehtävässä tarvittavaan tietoon."}]},{"q":"Hakutyökalu palauttaa kaksi ristiriitaista ohjetta. Miten agentin tulee toimia?","options":[{"text":"Keskeyttää toiminta ja ohjata ristiriita tarkistettavaksi.","correct":true,"explain":"Ristiriitaiset lähteet ovat havaittava eskalointiehto."},{"text":"Valita ensimmäinen tulos, jotta työ etenee nopeasti.","correct":false,"explain":"Tulosten järjestys ei kerro, kumpi lähde on oikea."},{"text":"Yhdistää ohjeet uudeksi säännöksi.","correct":false,"explain":"Agentti ei saa keksiä ristiriitaisista lähteistä omaa toimintaohjetta."}]}],"summary":"Turvallinen työkalu on tarkoitukseen rajattu. Ristiriita, puuttuva tieto tai virhe pysäyttää toiminnan ja käynnistää sovitun eskaloinnin."}
```

## 3. Tieto vai toiminto

```task
{"type":"classify","title":"Tieto vai toiminto","intro":"Luokittele, lukeeko työkalu tietoa vai vaikuttaako se ympäristöön.","categories":["Lukee tietoa","Tekee toiminnon"],"items":[{"text":"Hakee hyväksytystä tietopohjasta palautusehdon.","answer":0,"explain":"Työkalu lukee rajattua lähdettä."},{"text":"Tallentaa hyväksytyn luokituksen taulukkoon.","answer":1,"explain":"Tallennus muuttaa ympäristön tilaa."},{"text":"Tarkistaa tilauksen nykyisen tilan.","answer":0,"explain":"Tilatiedon tarkistus on lukutoiminto."},{"text":"Lähettää asiakkaalle viestin.","answer":1,"explain":"Viestin lähettäminen vaikuttaa ulkomaailmaan ja vaatii tavallisesti tiukemman rajan."}],"summary":"Lukeminenkin pitää rajata, mutta ympäristöä muuttava toiminto vaatii tavallisesti tiukemmat oikeudet, lokituksen ja tarvittaessa hyväksynnän."}
```

## 4. Turvallinen työkalukutsu

```task
{"type":"order","title":"Turvallinen työkalukutsu","intro":"Järjestä vaiheet turvalliseen järjestykseen.","steps":["Kielimalli valitsee yhden sallituista työkaluista.","Agentin ohjauskehys tarkistaa pyynnön ja käyttöoikeuden.","Tarvittaessa ihminen hyväksyy kriittisen toiminnon.","Ohjauskehys suorittaa rajatun toiminnon.","Tulos tai virhe palautetaan ja kirjataan lokiin."],"missHint":"Mieti, mikä tarkistetaan ennen toimintoa ja mitä kirjataan sen jälkeen.","summary":"Kielimalli ehdottaa, mutta agentin ohjauskehys tarkistaa oikeudet, pyytää tarvittavan hyväksynnän, suorittaa toiminnon ja kirjaa tuloksen."}
```

## 5. Kirjoita työkalusopimus

```task
{"type":"reflect","title":"Kirjoita työkalusopimus","prompt":"Valitse yksi oman agenttisi työkalu. Kuvaa proosana sen tarkoitus, tarvitsemat tiedot, palauttama tulos, kielletyt toiminnot, hyväksyntää vaativa kohta ja toiminta virhetilanteessa.","minWords":60,"summary":"Hyvä työkalusopimus kertoo sekä sen, mitä työkalu tekee, että sen, mitä se ei saa tehdä."}
```
