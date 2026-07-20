# Harjoittele — Reilu työkalukoe

Harjoitukset valmistavat sinua vertailuun, jossa päätös perustuu ennalta sovittuihin ehtoihin ja näkyviin havaintoihin.

## Tehtävä 1/5 — kokeen käsitteet

```task
{"type":"match","title":"Kokeen käsitteet paikoilleen","intro":"Yhdistä käsite sitä vastaavaan kuvaukseen.","pairs":[{"a":"Porttiehto","b":"Pakollinen ehto, jonka pitää täyttyä ennen laadun vertailua.","explain":"Jos aineistoa ei saa käyttää palvelussa, hyvääkään vastausta ei pisteytetä."},{"a":"Laatukriteeri","b":"Ennalta päätetty ominaisuus, jonka perusteella vastausten onnistumista arvioidaan.","explain":"Esimerkiksi sisällön säilyminen tai kohderyhmälle sopiva kieli."},{"a":"Vakioitu ehto","b":"Asia, joka pidetään vertailussa samana, kuten prompti ja lähdeaineisto.","explain":"Näin havaittu ero voidaan yhdistää uskottavammin vertailtavaan työkaluun."},{"a":"Sokkoutus","b":"Vastausten arviointi niin, ettei arvioija tiedä niiden alkuperää.","explain":"Tämä vähentää tuotemerkkiin liittyvän ennakko-odotuksen vaikutusta."},{"a":"Rajoitus","b":"Seikka, joka kaventaa sitä, mitä kokeen perusteella voidaan päätellä.","explain":"Esimerkiksi eri tilitasot tai vain yksi testiaineisto."}],"summary":"Hyvä vertailu tarkistaa ensin porttiehdot, päättää laatukriteerit, pitää olennaiset olosuhteet samoina ja kirjaa tulkinnan rajat."}
```

## Tehtävä 2/5 — portti vai laatukriteeri?

```task
{"type":"classify","title":"Portti vai laatukriteeri?","intro":"Luokittele jokainen ehto. Porttiehto ratkaisee, saako työkalua käyttää; laatukriteeri kertoo, kuinka hyvin se hoitaa tehtävän.","categories":["Porttiehto","Laatukriteeri"],"items":[{"text":"Organisaatio on hyväksynyt palvelun tämän aineiston käsittelyyn.","answer":0,"explain":"Ilman käyttölupaa aineistoa ei syötetä palveluun."},{"text":"Vastaus säilyttää lähteen kaikki viisi ydinkohtaa.","answer":1,"explain":"Tämä on havaittava laadun ominaisuus."},{"text":"Palvelu avaa tehtävässä tarvittavan tiedostomuodon.","answer":0,"explain":"Ilman ominaisuutta tehtävää ei voi toteuttaa."},{"text":"Teksti sopii aloittelijalle ilman selittämätöntä erikoissanastoa.","answer":1,"explain":"Tämä kertoo tuotoksen sopivuudesta yleisölle."},{"text":"Käyttäjällä on tehtävään tarvittava käyttöoikeus.","answer":0,"explain":"Käyttöoikeus tarkistetaan ennen testiä."},{"text":"Tuotos tarvitsee vain vähän jälkikorjausta.","answer":1,"explain":"Jälkityön määrä on tehtäväkohtainen laatukriteeri."}],"summary":"Porttiehtoa ei voi hyvittää korkealla laatupisteellä. Vasta hyväksytyt vaihtoehdot siirtyvät laadulliseen vertailuun."}
```

## Tehtävä 3/5 — onko koe reilu?

```task
{"type":"quiz","title":"Onko koe reilu?","intro":"Valitse kussakin tilanteessa paras korjaus.","items":[{"q":"Työkalu A saa koko raportin ja työkalu B vain yhteenvedon. Miten korjaat kokeen?","options":[{"text":"Anna molemmille sama lähdeaineisto.","correct":true,"explain":"Muuten ero voi johtua aineistosta, ei työkalusta."},{"text":"Anna A:lle vielä yksi lisäprompti.","correct":false,"explain":"Tämä kasvattaa eroa olosuhteissa."},{"text":"Pisteytä vain vastausten pituus.","correct":false,"explain":"Pituus ei korjaa erilaista lähtöaineistoa."}]},{"q":"Näet palvelujen nimet ja huomaat suosivasi tuttua työkalua. Mikä auttaa?","options":[{"text":"Arvioi vastaukset A- ja B-tunnuksilla ennen alkuperän paljastamista.","correct":true,"explain":"Sokkoutus vähentää brändiodotuksen vaikutusta."},{"text":"Anna tutulle työkalulle lähtökohtaisesti yksi lisäpiste.","correct":false,"explain":"Tämä vahvistaa vinoumaa."},{"text":"Poista kaikki kriteerit.","correct":false,"explain":"Ilman kriteerejä arvio muuttuu vielä herkemmin mielipiteeksi."}]},{"q":"Yksi koe onnistui. Mitä voit päätellä?","options":[{"text":"Tulos koskee tätä tehtävää, aineistoa ja kokeen olosuhteita.","correct":true,"explain":"Yksi koe ei osoita yleistä paremmuutta."},{"text":"Voittaja on paras kaikkiin tehtäviin.","correct":false,"explain":"Johtopäätös ylittää kokeen näytön."},{"text":"Mallin satunnaisuudella ei voi olla vaikutusta.","correct":false,"explain":"Yksittäinen ajo voi vaihdella."}]}],"summary":"Reilu koe pitää promptin ja aineiston samoina, vähentää ennakko-odotuksia ja rajaa johtopäätöksen siihen, mitä todella testattiin."}
```

## Tehtävä 4/5 — muotoile johtopäätös

```task
{"type":"reflect","title":"Kirjoita rajattu johtopäätös","intro":"Kirjoita lyhyt päätelmä annetusta kokeesta.","prompt":"Työkalu A säilytti lähteen viisi ydinkohtaa ja vaati kaksi pientä kielikorjausta. Työkalu B jätti kaksi ydinkohtaa pois ja vaati niiden palauttamisen. Molemmat täyttivät porttiehdot. Kirjoita johtopäätös, joka kertoo valinnan mutta ei väitä kumpaakaan yleisesti parhaaksi.","min_chars":100,"expert":"Tässä kokeessa työkalu A sopi paremmin annetun lähdetekstin muokkaamiseen, koska se säilytti kaikki viisi ydinkohtaa ja vaati vähemmän jälkikorjausta. Tulos koskee tätä tehtävää ja aineistoa; se ei osoita työkalun olevan parempi muissa käyttötapauksissa.","checklist":["Nimesin tehtävän, jota valinta koskee.","Perustin valinnan vähintään yhteen näkyvään havaintoon.","Rajasin sen, mitä kokeesta ei voi päätellä."]}
```

## Tehtävä 5/5 — kokeen rajoitus

```task
{"type":"reflect","title":"Mitä kokeesi ei osoita?","intro":"Hyvä vertailu kertoo myös oman rajansa.","prompt":"Nimeä yksi työkalukokeen tulos ja kirjoita sen jälkeen kaksi asiaa, joita tuloksen perusteella ei vielä voi päätellä.","placeholder":"Kokeessa havaittiin…\nTämän perusteella ei voi vielä päätellä…","tips":["Rajaa väite tehtävään ja aineistoon.","Huomioi yksittäinen ajokerta.","Erota käytettävyys tuotoksen laadusta."],"summary":"Rajoitusten kirjaaminen tekee johtopäätöksestä uskottavamman."}
```
