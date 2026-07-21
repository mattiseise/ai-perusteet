# Harjoittele — Minimiversio ja toteutuspolun näyttö

## 1. Käsitteet paikoilleen

```task
{"type":"match","title":"Käsitteet paikoilleen","intro":"Yhdistä käsite ja sitä kuvaava selitys.","pairs":[{"a":"Kielimallivalinta","b":"Tilanteen mukaan muuttuva valinta vähintään kahdesta sallitusta vaihtoehdosta.","explain":"Valinta erottaa kurssin agentin ennalta määrätystä työnkulusta."},{"a":"Suoritusjälki","b":"Näyttö syötteestä, valinnasta, työkalun tuloksesta ja seuraavasta vaiheesta.","explain":"Jälki tekee toiminnan arvioitavaksi ilman mallin sisäisen päättelyn tallentamista."},{"a":"Tekninen n8n-polku","b":"Toimiva työnkulku, jonka yhteydet ja reititys todennetaan käytetyssä ympäristössä.","explain":"Näyttö kertoo teknisestä toiminnasta kyseisessä toteutuksessa."},{"a":"Dokumentoitu suunnittelupolku","b":"Kaavio, työkalusopimukset, todellinen mallivalinta ja simuloitu suoritusjälki.","explain":"Näyttö kertoo suunnitelman johdonmukaisuudesta, ei testaamattomien liitäntöjen toimivuudesta."}],"summary":"Molemmat polut tarvitsevat todellisen rajatun kielimallivalinnan. Niiden tuottama muu näyttö on erilaista."}
```

## 2. Agentti vai työnkulku

```task
{"type":"quiz","title":"Agentti vai työnkulku","intro":"Tunnista, missä tilanteessa kurssin agenttirajaus täyttyy.","items":[{"q":"Järjestelmä lähettää jokaisen hyväksytyn lomakkeen samaan osoitteeseen. Onko rajattu kielimallivalinta tarpeen?","options":[{"text":"Ei. Kiinteä sääntö kuuluu työnkululle.","correct":true,"explain":"Tilannearviota ei tarvita, koska seuraava vaihe on aina sama."},{"text":"Kyllä, koska mukana on monta vaihetta.","correct":false,"explain":"Vaiheiden määrä ei tee järjestelmästä agenttia."}]},{"q":"Kielimalli tulkitsee vaihtelevan tukiviestin ja valitsee vaihtoehdoista pyydä lisätietoa, hae hyväksytystä tietopohjasta tai ohjaa ihmiselle. Mitä tämä osoittaa?","options":[{"text":"Tilanteen mukaan muuttuvan rajatun mallivalinnan.","correct":true,"explain":"Valinta on kurssin agenttirajauksen kannalta olennainen näyttö."},{"text":"Rajoittamattoman autonomian.","correct":false,"explain":"Vaihtoehdot ja oikeudet ovat tarkoituksella rajatut."}]}],"summary":"Agentin tunnusmerkki ei ole solmujen tai vaiheiden määrä vaan kielimallin tekemä tilanteen mukaan muuttuva valinta ohjauskehyksen rajoissa."}
```

## 3. Mikä näyttö kuuluu polulle

```task
{"type":"classify","title":"Mikä näyttö kuuluu polulle","intro":"Luokittele näyttö ensisijaisen toteutuspolun mukaan.","categories":["Tekninen n8n-polku","Dokumentoitu suunnittelupolku","Molemmat"],"items":[{"text":"n8n:n suoritusnäkymä, jossa valittu haara näkyy.","answer":0,"explain":"Tämä todentaa teknisen reitityksen käytetyssä ympäristössä."},{"text":"Kaavio, jossa simuloidut vaiheet on merkitty erilleen toteutetusta kielimallikutsusta.","answer":1,"explain":"Merkintä tekee suunnitelman näytön ja rajoituksen näkyväksi."},{"text":"Kaksi erilaista syötettä ja niiden todelliset kielimallivalinnat.","answer":2,"explain":"Todellinen rajattu mallivalinta vaaditaan molemmissa poluissa."},{"text":"Työkalusopimus, jossa näkyvät oikeudet ja virhepolku.","answer":2,"explain":"Työkalujen rajat pitää ymmärtää kummassakin polussa."},{"text":"Maininta siitä, ettei kaavio todista liitännän toimivuutta.","answer":1,"explain":"Dokumentoidun polun pitää nimetä teknisen todennuksen puute."}],"summary":"Toteutuspolut osoittavat samaa ymmärrystä eri näytöllä. Näyttöä ei pidä kuvata laajemmaksi kuin se on."}
```

## 4. Minimiversion työjärjestys

```task
{"type":"order","title":"Minimiversion työjärjestys","intro":"Järjestä työvaiheet niin, että virhe löytyy ajoissa.","steps":["Rajaa ongelma ja kielimallin sallitut vaihtoehdot.","Tee pienin testattava rakenne valitulla toteutuspolulla.","Aja kaksi erilaista syötettä ja tallenna suoritusjäljet.","Vertaa tuloksia odotettuun toimintaan.","Korjaa yksi havaittu ongelma ja tee testi uudelleen."],"missHint":"Aloita rajauksesta ja päätä uudelleentestiin.","summary":"Iteratiivinen kehitys tekee yhden pienen, arvioitavan muutoksen kerrallaan."}
```

## 5. Perustele toteutuspolkusi

```task
{"type":"reflect","title":"Perustele toteutuspolkusi","prompt":"Kerro, valitsetko teknisen n8n-polun vai dokumentoidun suunnittelupolun. Perustele, millä näytöllä osoitat todellisen kielimallivalinnan, agentin ohjauskehyksen rajat ja yhden korjatun ongelman. Nimeä myös yksi asia, jota näyttösi ei todista.","minWords":70,"summary":"Hyvä perustelu kertoo sekä valitun näytön vahvuuden että sen rajoituksen."}
```
