# Lesson 25: Sanasto — Turvallinen agentti

| Termi | Määritelmä |
|-------|-----------|
| **Prompt injection** (agentissa) | Hyökkäys, jossa ulkoinen syöte sisältää piilotetun ohjeistuksen, jonka agentti noudattaa. Agentin kontekstissa vaarallisempi, koska agentti tekee todellisia toimintoja. |
| **Minimioikeus-periaate** (principle of least privilege) | Periaate, jossa agentille annetaan VAIN minimaalinen pääsy, jonka se tarvitsee tehtäväänsä varten. |
| **Lokitus** (logging) | Prosessi, jossa kirjoitetaan muistiin kaikki agentin toiminnot: funktio-kutsut, päätökset, virheet. |
| **Audit trail** | Kronologinen kirjaus siitä, mitä agentti teki, kuka hyväksyi mitä, ja milloin. Lakisääteinen vaatimus monissa yhteyksissä. |
| **Validointi** (input validation) | Prosessi, jossa tarkistetaan, että ulkoinen syöte on oikean muotoinen ja oikean pituinen ennen kuin se annetaan agentille. |
| **Konteksti rajoitus** (context isolation) | Käytäntö, jossa agentti näkee VAIN sen tiedon, jota se tarvitsee. Ehkäisee tietojen leviämisen. |
| **Vaarallinen operaatio** (hazardous operation) | Agentin operaatio, joka voi aiheuttaa merkittävää vahinkoa, jos se menee pieleen (esim. maksujen käsittely, tietojen poisto). |
| **Turvallisuuskerrostus** (security layer) | Yksi kerroksista, joka suojaa agentin epäonnistumiselta: validointi, rajoitus, seuranta, palautuminen. |
