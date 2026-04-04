# Lesson 22: Opettajan materiaalit

## Oppimisen tavoitteet

Opiskelija osaa:
1. Rakentaa hyvän tietopohjaa bottille
2. Asettaa rajauksia sille, mitä botti saa ja ei saa tehdä
3. Testata bottia systemaattisesti (positiiviset, negatiiviset, reunatapaukset)
4. Dokumentoida testitulokset
5. Parantaa bottia iteratiivisesti testauksen perusteella

## Yleisimmät väärinkäsitykset

1. **"Botti toimii hyvin ilman testausta"** → Jokainen botti tarvitsee systemaattisen testauksen ennen käyttöönottoa

2. **"Testaus on vain positiivisten testien tekemistä"** → Negatiiviset testit (mitä botti ei osaa) ovat yhtä tärkeitä

3. **"Tietopohja hoitaa kaiken"** → Tietopohja on tarpeen, mutta rajaukset ja ohjeistus määrittävät käyttäytymisen

4. **"Yksi testi riittää"** → Hyvä testaus sisältää kymmeniä testejä ja eri skenaarioita

5. **"Reunatapaukset eivät tärkeä"** → Reunatapaukset (tyhjät syötteet, sekavat kysymykset) paljastuvat vakavat bugit

## Tarkistustehtävät / CFU

1. Mitä on tietopohja ja mistä se voi koostua?
2. Mikä ero on positiivisella ja negatiivisella testillä?
3. Mikä on reunatapaus? Esimerkki?
4. Miksi rajaukset ovat tärkeitä?
5. Mitä tarkoittaa iteraatio bottikehityksessä?
6. Mitä pitäisi tehdä, jos botti epäonnistuu testissa?
7. Kuinka paljon testejä bottille pitäisi tehdä ennen käyttöönottoa?
8. Millä tavoin voit dokumentoida testauslokia?

## Tyypilliset vaikeudet

1. **Testauksen pinnallisuus** — Opiskelijat testaavat vain muutamia kysymyksiä ja luulevat botti olevan valmis.
   **Apua:** "Kuvittele, että testaat 100 käyttäjää. Kuinka moni kysyisi jotain outoa? Testaa sen mukaisesti."

2. **Negatiivisten testien unohtaminen** — Opiskelijat eivät testaa, mitä botti ei osaa.
   **Apua:** "Testaa: mitä botti sanoo, jos et osaa vastata? Sanoo se 'en osaa' vai jotain typerää?"

3. **Reunatapausten vähättely** — "Eihän kukaan kirjoitaisi tyhjää kysymystä."
   **Apua:** "Ehkä ei, mutta entä liian pitkä kysymys? Sekava teksti? Verkko katkeaa?" Näytä, miten botti käyttäytyy.

4. **Iteraation puuttuminen** — Opiskelijat tekevät testin, mutta eivät korjaa.
   **Apua:** "Jos testissa löydät ongelman, se on vasta alussa. Nyt korjaamme ja testataan uudelleen."

5. **Dokumentoinnin laiminlyönti** — Opiskelijat testaavat mielessään, eivätkä kirjoita tuloksia.
   **Apua:** "Dokumentointi on tärkeä. Jos botti epäonnistuu myöhemmin, sinulla täytyy olla lokit, jotka näyttävät mitä tapahtui."
