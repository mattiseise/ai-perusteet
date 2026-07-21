# Harjoittele — Ihminen portinvartijana

## Tehtävä 1/4 — käsitteet

```task
{"type":"match","title":"Hyväksyntätyön käsitteet","intro":"Yhdistä käsite ja kuvaus.","pairs":[{"a":"Hyväksyntäportti","b":"Kohta, jossa agentin eteneminen pysähtyy ihmisen päätökseen.","explain":"Portti sijoitetaan riskikohtaan, ei jokaiseen rutiinivaiheeseen."},{"a":"Eskalointi","b":"Asian ohjaaminen toiselle vastuuhenkilölle tai korkeammalle päätöstasolle.","explain":"Sitä tarvitaan, jos ensimmäinen hyväksyjä ei vastaa tai tapaus ylittää hänen toimivaltansa."},{"a":"Oletustoiminto","b":"Ennalta määritelty turvallinen toiminta, jos päätöstä ei saada määräajassa.","explain":"Kriittistä raha- tai oikeuspäätöstä ei yleensä hyväksytä hiljaisuuden perusteella."},{"a":"Palautedata","b":"Tallennettu hyväksyntä, hylkäys, muokkaus ja perustelu myöhempää arviointia varten.","explain":"Tallennus ei vielä tarkoita, että malli olisi oppinut."},{"a":"Hyväksyntäväsymys","b":"Tilanne, jossa liian monet pyynnöt heikentävät ihmisen tarkkaavaisuutta.","explain":"Portit rajataan päätöksiin, joissa ihmisen harkinta tuo todellista arvoa."}],"summary":"Hyvä portti pysäyttää oikeassa riskikohdassa, antaa päätöksen tiedot ja määrittää myös hiljaisuuden sekä palautteen käsittelyn."}
```

## Tehtävä 2/4 — tarvitseeko ihminen?

```task
{"type":"classify","title":"Automaattisesti vai ihmiselle?","intro":"Luokittele ensisijainen toimintatapa.","categories":["Voi toimia rajatusti automaattisesti","Ihmisen hyväksyntä tarvitaan"],"items":[{"text":"Lähetä tavallinen vastaanottokuittaus hyväksytyllä mallipohjalla.","answer":0,"explain":"Matalan riskin rutiini voidaan automatisoida, jos sisältö ja vastaanottaja on rajattu."},{"text":"Myönnä asiakkaalle 40 prosentin alennus.","answer":1,"explain":"Rahaa ja sitoumusta koskeva päätös vaatii toimivallan omaavan ihmisen."},{"text":"Pyydä käyttäjää täsmentämään puuttuva päivämäärä.","answer":0,"explain":"Lisätiedon pyytäminen ei yleensä tee peruuttamatonta päätöstä."},{"text":"Poista asiakkaan tiedot pysyvästi.","answer":1,"explain":"Vaikutus on suuri ja vaikeasti peruttava."},{"text":"Ohjaa vastuuhenkilölle tapaus, josta puuttuu pakollinen tieto ja joka kuuluu korkeaan riskiluokkaan.","answer":1,"explain":"Havaittava tiedonpuute ja määritelty riskiluokka käynnistävät eskaloinnin."}],"summary":"Ihminen tarvitaan erityisesti rahaan, oikeuksiin, peruuttamattomiin toimiin ja havaittavaan tiedonpuutteeseen, ristiriitaan tai virheeseen liittyvissä tilanteissa."}
```

## Tehtävä 3/4 — palautteesta muutokseksi

```task
{"type":"order","title":"Hallittu kehitysketju","intro":"Järjestä vaiheet turvalliseen järjestykseen.","steps":["Tallenna ehdotus, ihmisen päätös ja perustelu lokiin.","Etsi useista tapauksista toistuva ongelma tai poikkeama.","Arvioi, johtuuko havainto säännöstä, virheestä vai yksittäisestä poikkeuksesta.","Ehdota rajattu muutos promptiin, tietopohjaan, sääntöön tai testiin.","Hyväksytä muutos vastuuhenkilöllä.","Aja ennalta määritellyt testit uudelleen ennen käyttöönottoa."],"missHint":"Tallennettu päätös ei saa muuttua suoraan uudeksi säännöksi. Ensin tarvitaan useamman tapauksen arviointi, hallittu muutos ja testaus.","summary":"Palautedata muuttuu toiminnaksi vasta arvioinnin, hyväksytyn muutoksen ja uudelleentestauksen kautta."}
```

## Tehtävä 4/4 — perustele oma portti

```task
{"type":"reflect","title":"Suunnittele yksi hyväksyntäportti","intro":"Kuvaa yksi oman agentti-ideasi riskikohta.","prompt":"Missä kohdassa agenttisi tarvitsee ihmisen päätöksen? Kerro, mitä portti näyttää, kuka päättää, kuinka kauan odotetaan, mitä tapahtuu ilman vastausta ja miten päätös tallennetaan kehitysaineistoksi.","min_chars":140,"expert":"Hyvä vastaus nimeää riskin, päätöksentekijän, päätöksessä tarvittavan näytön, aikarajan, eskaloinnin tai turvallisen oletustoiminnon sekä sen, että lokitettu palaute arvioidaan ennen järjestelmän muuttamista.","checklist":["Nimesin päätöksen ja riskin.","Kerroin, mitä tietoa portti näyttää.","Määritin aikarajan ja hiljaisuuden jälkeisen toiminnan.","Erotin palautteen tallentamisen automaattisesta oppimisesta."]}
```
