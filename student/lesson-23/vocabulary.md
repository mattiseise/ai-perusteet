# Lesson 23: Sanasto — Agentin konteksti, muisti ja tila

| Termi | Määritelmä |
|-------|-----------|
| **Konteksti-ikkuna** (context window) | Pieni ikkuna viimeisimmistä viesteistä, joita agentti näkee kerralla. Esim. viimeinen 10 viestiä. |
| **Muisti** (memory) | Kyvyt, joilla agentti muistaa tietoja — konteksti-ikkuna ja pitkäaikainen muisti. |
| **Pitkäaikainen muisti** (long-term memory) | Tieto, joka tallennetaan ulkoiseen järjestelmään (tietokanta, vektoritietokanta), niin että agentti muistaa sen seuraavalla kerralla. |
| **Vektoritietokanta** (vector database) | Erityinen tietokanta, joka tallentaa tietoa "merkitysten" perusteella eikä vain avainsanoilla. Auttaa agentia ymmärtämään samankaltaisia asioita. |
| **Tila** (state) | Tieto siitä, missä vaiheessa prosessi on ja mitä vaatimuksia/muuttujia sillä on. Esim. "maksu suoritettu" tai "vaihe 3 käynnissä". |
| **Sessio** (session) | Yksi keskustelun istunto agenttia ja käyttäjää välillä. Sessio voi sisältää konteksti-ikkunan, mutta pitkäaikainen muisti säilyy sessioiden välillä. |
| **Stateslesspohjainen** (stateless) | Agentti, joka ei muista mitään edellisistä istunnoista — jokainen sessio on riippumaton. |
