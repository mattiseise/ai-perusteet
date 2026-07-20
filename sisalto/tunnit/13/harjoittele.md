# Harjoittele — Tekoäly ehdottaa, ihminen päättää

Tehtävät seuraavat yhtä työparisykliä luonnoksesta perusteltuun päätökseen.

## Tehtävä 1/5 — roolit työparisyklissä

```task
{"type":"match","title":"Kuka tekee mitä?","intro":"Yhdistä työvaihe sen vastuuseen.","pairs":[{"a":"Tehtävän rajaus","b":"Ihminen päättää käyttäjän, tavoitteen ja hyväksyttävän lopputuloksen.","explain":"Malli ei tunne todellista tarvetta ilman käyttäjän valintoja."},{"a":"Luonnos","b":"Tekoäly tuottaa nopeasti ensimmäisen jäsennyksen tai tekstipohjan.","explain":"Luonnos on käsiteltävää aineistoa, ei automaattisesti valmis tuotos."},{"a":"Sisällön tarkistus","b":"Ihminen vertaa väitteitä todellisuuteen ja lähteisiin.","explain":"Sujuvuus ei osoita oikeellisuutta."},{"a":"Testilukijan palaute","b":"Tekoäly auttaa löytämään mahdollisia jumiutumiskohtia annetun kohderyhmän näkökulmasta.","explain":"Palaute on ehdotus, ei käyttäjätutkimuksen korvike."},{"a":"Lopullinen päätös","b":"Ihminen hyväksyy, muokkaa tai hylkää ehdotukset ja vastaa tuotoksesta.","explain":"Vastuu ei siirry mallille missään vaiheessa."}],"summary":"Tekoäly nopeuttaa ehdottamista; ihminen määrittää, tarkistaa ja päättää."}
```

## Tehtävä 2/5 — hyvä päätösloki

```task
{"type":"quiz","title":"Mikä perustelu riittää?","intro":"Valitse päätös, joka perustuu havaintoon.","items":[{"q":"Luonnos nimeää käyttöliittymässä painikkeen, jota et löydä. Miten kirjaat päätöksen?","options":[{"text":"Poistan tai korjaan kohdan, koska todellisessa käyttöliittymässä kyseistä painiketta ei ole; tarkistin asian itse.","correct":true,"explain":"Päätös perustuu havaittuun ympäristöön."},{"text":"Säilytän kohdan, koska se kuulostaa uskottavalta.","correct":false,"explain":"Uskottava sanamuoto voi silti olla keksitty yksityiskohta."},{"text":"Pyydän samaa mallia vakuuttamaan, että painike on olemassa.","correct":false,"explain":"Saman mallin varmuus ei korvaa tarkistusta todellisesta lähteestä."}]},{"q":"Testilukija ehdottaa koko ohjeen muuttamista humoristiseksi. Kohderyhmä tarvitsee vakavan turvallisuusohjeen. Mitä teet?","options":[{"text":"Hylkään ehdotuksen, koska sävy ei sovi tehtävän riskiin ja käyttötarkoitukseen.","correct":true,"explain":"Ihminen arvioi ehdotuksen suhteessa ennalta päätettyyn tarkoitukseen."},{"text":"Hyväksyn ehdotuksen, koska tekoäly ehdotti sitä testilukijana.","correct":false,"explain":"Testilukijan rooli ei tee ehdotuksesta automaattisesti oikeaa."},{"text":"Arvon, kumpaa versiota käytän.","correct":false,"explain":"Päätös pitää perustaa tehtävän vaatimuksiin."}]}],"summary":"Hyvä päätösloki kertoo valinnan, perusteen ja tarvittaessa tarkistuslähteen."}
```

## Tehtävä 3/5 — työjärjestys

```task
{"type":"order","title":"Luonnoksesta valmiiksi","intro":"Järjestä työparisykli.","steps":["Rajaa käyttäjä, tehtävä ja laatukriteerit.","Pyydä tekoälyltä luonnos ja säilytä se versiona 1.","Tarkista sisältö ja tee omat muokkaukset versioksi 2.","Pyydä uudessa keskustelussa testilukijan palaute versiosta 2.","Hyväksy, muokkaa tai hylkää ehdotukset perustellen.","Tallenna lopullinen tuotos ja päätösloki."],"missHint":"Ihmisen tarkistus tehdään ennen testilukijan palautetta, ja lopullinen päätös vasta palautteen jälkeen.","summary":"Versiot ja päätösloki näyttävät, missä ihmisen työ vaikutti lopputulokseen."}
```

## Tehtävä 4/5 — oma päätös

```task
{"type":"reflect","title":"Mitä et ulkoista?","intro":"Ajattele tehtävää, jossa voisit käyttää tekoälyä työparina.","prompt":"Kirjoita, minkä osan antaisit tekoälyn luonnosteltavaksi, minkä tiedon tarkistaisit itse ja minkä päätöksen pitäisit aina ihmisellä.","placeholder":"Tekoäly voisi luonnostella…\nTarkistaisin itse…\nPäättäisin itse…","tips":["Valitse todellinen tehtävä.","Nimeä tarkistuslähde.","Erota ehdotus päätöksestä."],"summary":"Työparius toimii, kun vastuunjako on näkyvä eikä vain oletettu."}
```

## Tehtävä 5/5 — osoita oma työ

```task
{"type":"reflect","title":"Mikä muuttui sinun päätökselläsi?","intro":"Pelkkä lopputulos ei vielä näytä työparisykliä.","prompt":"Kirjoita yksi ennen–jälkeen-esimerkki: mitä luonnoksessa luki, mitä muutit ja mihin tarkistukseen tai tavoitteeseen päätöksesi perustui.","placeholder":"Luonnoksessa…\nMuutin…\nPerustelu…","tips":["Lainaa vain lyhyt kohta.","Nimeä oma päätöksesi.","Kerro tarkistuslähde tai laatukriteeri."],"summary":"Ennen–jälkeen-esimerkki tekee ihmisen ajattelun näkyväksi."}
```
