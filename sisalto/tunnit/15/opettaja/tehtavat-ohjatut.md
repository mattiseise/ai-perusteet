# Ohjatut tehtävät — oppitunti 15

## Aktiviteetti 1 — Tietotarve ennen dokumenttia (15 min)

Anna ryhmille käyttötapaus, jossa kerhon uusi jäsen haluaa valmistautua ensimmäisiin harjoituksiin. Pyydä heitä kuvittelemaan tulijan tilanne ennen kuin he näkevät yhtäkään lähdedokumenttia: mikä häntä jännittää, mitä hänen täytyy tietää etukäteen ja missä kohdassa väärä tieto aiheuttaisi käytännön hankaluuden? Ryhmät muotoilevat keskustelun pohjalta viisi kysymystä, joihin botin pitää pystyä vastaamaan.

Näytä vasta tämän jälkeen neljä mahdollista lähdettä: säännöt, harjoitusaikataulu, vanha markkinointiesite ja jäsenten yhteystietolista. Ryhmät valitsevat tehtävään sopivat lähteet ja perustelevat myös poisjätöt. Markkinointiesite voi liittyä aiheeseen mutta olla vanhentunut, ja yhteystietolista voi sisältää tietoa, jota botin ei pidä saada lainkaan.

Purussa korosta, ettei aiheeseen liittyminen vielä tee dokumentista tarpeellista tai sallittua.

## Aktiviteetti 2 — Lähteen kuntotarkastus (15 min)

Arvioikaa seuraavaksi yksi lähde yhdessä. Käytä alla olevia viittä kysymystä tarkistuslistana, mutta pyydä jokaiseen vastaukseen myös lyhyt perustelu:

1. Kuka sen on laatinut?
2. Milloin se on tarkistettu?
3. Mihin tietotarpeeseen se vastaa?
4. Onko se ristiriidassa muun aineiston kanssa?
5. Saako sen ladata valittuun palveluun?

Pyydä ryhmiä nimeämään lopuksi yksi asia, jota lähde ei kerro. Korosta, ettei aukon löytyminen ole epäonnistuminen. Päinvastoin: onnistunut kuratointi tekee näkyväksi sen, milloin botin pitää myöntää tiedon puute tai ohjata kysymys ihmiselle.

## Aktiviteetti 3 — Muuta vaatimus testiksi (20 min)

Anna vaatimus: **”Botti käyttää vain hyväksyttyä hinnastoa eikä arvaa puuttuvaa hintaa.”** Kysy ensin, millainen käyttäjän viesti voisi todella koetella tätä vaatimusta. Vasta sen jälkeen ryhmät täyttävät taulukon:

| Kohta | Vastaus |
| --- | --- |
| Syöte |  |
| Odotettu toiminta |  |
| Läpäisyehto |  |
| Mihin lähteeseen testi liittyy? |  |

Tee sama yhdelle botin rajalle ja yhdelle reunatapaukselle. Purussa vertaa erityisesti läpäisyehtoja. ”Vastaus on hyvä” ei vielä riitä, mutta esimerkiksi ”vastaus ei ilmoita hintaa ilman lähdettä ja ohjaa käyttäjän nimettyyn kanavaan” voidaan havaita.

## Aktiviteetti 4 — Testisuunnitelman tarkistus (15 min)

Parit vaihtavat testisuunnitelmia ja lukevat niitä kuin ulkopuolinen arvioija. Seuraavat kysymykset toimivat vertaispalautteen tarkistuslistana:

- Onko mukana yksi positiivinen, yksi negatiivinen ja yksi reunatapaus?
- Onko odotus kirjoitettu ennen testin ajamista?
- Voiko läpäisyn ratkaista havaittavan näytön perusteella?
- Paljastaako jokin testi tietopohjan nimetyn aukon?

Pyydä paria antamaan yksi täsmällinen korjausehdotus. Tavoitteena ei ole lisätä testien määrää, vaan tehdä yhdestä epäselvästä odotuksesta tai läpäisyehdosta havaittava.

## Opettajan tarkistuslista

Käytä tunnin lopussa seuraavaa listaa varmistaaksesi, että työ on valmis siirtymään rakentamisvaiheeseen:

- Oppijat eivät vielä väitä testanneensa omaa bottiaan.
- Tietopohja perustuu tunnin 14 käyttötapaukseen.
- Jokaisella lähteellä on nimetty tehtävä.
- Tietosuoja ja käyttöoikeus tarkistetaan ennen lataamista.
- Testit ovat valmiita ajettaviksi tunnilla 17 ilman jälkikäteen keksittyjä odotuksia.
