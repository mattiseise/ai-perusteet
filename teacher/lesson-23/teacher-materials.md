# Lesson 23: Opettajan materiaalit

## Oppimisen tavoitteet

Opiskelija osaa:
1. Ymmärtää konteksti-ikkunan rajat ja merkityksen
2. Erottaa lyhytaikaisen (konteksti) ja pitkäaikaisen muistin
3. Tunnistaa tilan merkityksen prosessien hallinassa
4. Nähdä, että agentti ei ole "tietävä vaan "rakennettu"
5. Käyttää näitä käsitteitä analysoimaan agenttijärjestelmiä

## Yleisimmät väärinkäsitykset

1. **"Agentti muistaa kaiken kuten ihminen"** → Agentti muistaa vain konteksti-ikkunan (viimeinen 10-100 viestiä)

2. **"Pitkäaikainen muisti on vain database"** → Se on strateginen valinta siitä, mitä agentti "tarvitsee" muistaa seuraavalla kerralla

3. **"Tila on vain tekniikkaa"** → Tila määrittää, mitä agentti tekee seuraavaksi — se on liiketoimintalogiikan ydin

4. **"Uusi istunto = uusi agentti"** → Istunto muuttuu, mutta pitkäaikainen muisti ei — agentti voi tunnistaa vanhan asiakkaan

5. **"Konteksti-ikkuna on aina riittävä"** → Sen koko riippuu sovelluksesta; liian pieni → agentti unohti; liian suuri → hidas ja kallis

## Tarkistustehtävät / CFU

1. Mikä on konteksti-ikkunan tyypillinen koko? Miksi se on tärkeä?
2. Mitä eroa on konteksti-ikkunan ja pitkäaikaisen muistin välillä?
3. Mitä vektoritietokanta tekee ja miksi se auttaa agentia?
4. Mitä on "tila" ja miksi se agenteille tärkeä?
5. Antaa esimerkki tilasta, joka olisi kriittinen pelastaa/muistaa
6. Mitä tapahtuu, jos konteksti-ikkuna on liian pieni?
7. Kuinka agentti "tietää", millä vaiheessa prosessi on?
8. Voiko agentti unohtaa asiakkaan välillä istunoissa? Miten?

## Tyypilliset vaikeudet

1. **Muistin abstraktio** — Opiskelijat kuvittelevat agentin "muistavan" kuten ihminen.
   **Apua:** "Agentti ei ajattele. Se näkee vain viimeiset 20 viestiä. Sitten ne katoavat pysyvästi, ellei niitä tallennettu."

2. **Konteksti vs. pitkäaikainen muisti** — Opiskelijat sekoittavat nämä kaksi.
   **Apua:** "Konteksti = nyt näkyvät sanat. Pitkäaikainen muisti = tietokanta, jossa on asiakkaan historia."

3. **Tilan merkitys** — Opiskelijat eivät näe, kuinka tila ohjaa agentin käyttäytymistä.
   **Apua:** "Kun tilaus on 'MAKSETTU', agentti tekee X. Kun se on 'ODOTTAA MAKSUA', agentti tekee Y. Tila kertoo mitä tehdä."

4. **Vektoritietokannan ymmärtäminen** — Se on liian abstrakti.
   **Apua:** "Se on kuten Google. Voit hakea 'pikkulanta' ja se löytää 'pieni hanki' vaikka et käytä täsmälleen samoja sanoja."
