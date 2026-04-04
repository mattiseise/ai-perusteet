# Lesson 27: Opettajan materiaalit

## Oppimisen tavoitteet (OSP3 yhteenveto)

Opiskelija osaa:
1. **Ymmärtää agenttien rakentamisen prosessin** — ideoinnista demoon
2. **Suunnitella agenttia turvallisuus mielessä** — riskit, mitigaatio, lokitus
3. **Rakentaa toimivan prototyypin** — käytännön taidot
4. **Dokumentoida projektia ammattilaisesti** — README, arkkitehtuuri, turvallisuus
5. **Esitellä tekniikkaa ei-tekniikalle yleisölle** — viestintä- ja narratiivitaidot
6. **Ajatella kriittisesti** — perustella valintoja, tunnistaa riskit, nähdä parannuksia

## Arvioinnin filosofia

Lesson 27 arviointi ei ole:
- Perinteinen testi (ei kysymyksiä, joilla on "oikea vastaus")
- Vain koodi (ei pelkästään ohjelmistojen laadun arviointia)
- Perfektion etsintä (prototyyppi riittää, jos se on hyvin dokumentoitu ja esitelty)

Lesson 27 arviointi on:
- **Summatiivinen arviointi** OSP3:sta (agenteista ja automatisoinnista)
- **Projekti-pohjainen arviointi** — oppilas näyttää mitä osaa tekemällä jotain oikeaa
- **Suoritusarviointi** — demo ja reflektio näyttävät ymmärrystä
- **Hollistinen arviointi** — katsomme tekniikkaa, turvallisuutta, viestintää ja kriittistä ajattelua

## Yksityiskohtaiset arviointiohjeet

### Dokumentaation arviointi (ennen demoa)

1. **README.md** — Pystyisikö joku muu käyttämään tätä?
   - Riittävät ohjeet? Esimerkkejä?
   - Selkeä kieli? Ei liian tekninen?

2. **ARCHITECTURE.md** — Ymmärretään rakenne?
   - Onko kaavioita tai diagrammeja?
   - Selitetään komponenttien väliset suhteet?

3. **SAFETY.md** — Näkyy turvallisuusajattelu?
   - Listattu riskit konkreettisesti?
   - Kuvattu mitigaatiot?
   - Mainittu lokitus?

4. **TESTING.md** — Osoitetaan perusteellinen testaus?
   - Normaalit tapaukset?
   - Edge casea?
   - Hyökkäykseen testaaminen?

### Demo-arviointi (demopäivässä)

1. **Toiminnallisuus:** Tekee se mitä lupasi?
   - Testaa muutamia skenaarioita live
   - Huomaa, jos häiriöitä tulee, mutta "se kuuluu asiaan" — tärkeää on miten oppilas reagoi

2. **Selitys:** Ymmärrät projektia?
   - Käyttötapaus selvä?
   - Arkkitehtuuri ymmärrettävä lyhyesti selitettynä?
   - Turvallisuus huomioitu?

3. **Esittelytaito:** Onko demo kiinnostava?
   - Live-elementti, ei pelkkää diaa?
   - Puhe selvä ja organisoitu?
   - Välttää liian teknisen terminologian?

4. **Q&A:** Ymmärrys syvällinen?
   - Pystyy perustella valintoja?
   - Näkee riskit ja parannusten kohtia?
   - Vastaukset rehellisiä (OK sanoa "En tiedä")?

## Kysymysikkunat demo-arviointia varten

**Turvallisuus-kysymykset:**
- "Mitä tapahtuu, jos agentti saa prompt injection -hyökkäyksen?"
- "Kuka pääsee näihin tietoihin?"
- "Mitä lokitetaan ja miksi?"
- "Entä GDPR/laki — onko se huomioitu?"

**Arkkitehtuuri-kysymykset:**
- "Miksi valitsit tämän lähestymistavan muiden sijasta?"
- "Missä kohdassa agentti voisi epäonnistua?"
- "Mitä tapahtuu, jos API on poissa?"

**Testaus-kysymykset:**
- "Mitä testejä ajoit?"
- "Mitä edge casea huolettaa sinua eniten?"
- "Kuinka käyttäjä voisi rikkoa agentin?"

**Reflektio-kysymykset:**
- "Mitä oprit tekemällä tämän?"
- "Mitä tekisit toisin?"
- "Mitä halusit alun perin tehdä, mutta jouduit yksinkertaistamaan?"

## Yleisimmät arviointi-virheet

1. **"Demo ei toimi, joten arvosana on pieni."** 
   → Väärin. Demo voi hieman epäonnistua, mutta oppilas osaa selittää miksi. Keskity dokumentaatioon ja selityksiin.

2. **"Koodi on kaunis, joten arvosana on korkea."**
   → Väärin. Koodi on vain yksi tekijä. Dokumentaatio, turvallisuus ja esitys ovat yhtä tärkeitä.

3. **"Oppilas ei osannut vastata kysymykseen, joten arvosana laskee."**
   → Väärin. "En tiedä, mutta voisin..." on parempi vastaus kuin valehtelu. Kerro, että se osoittaa realistisuutta.

4. **"Projekti on liian yksinkertainen, joten arvosana on pieni."**
   → Väärin. Yksinkertainen, hyvin dokumentoitu ja testattu projekti on parempi kuin suurempi, huonommin dokumentoitu.

5. **"Turvallisuus on vain bonus."**
   → Väärin. Turvallisuus on 20 % arvosanasta. Se on kriittinen.

## Vertaisarviointi (vaihtoehto)

Voit pyytää opiskelijoita arvioimaan toisiaan kevyesti:
- Jokainen esittelyn jälkeen: "Mitä oli hyvää? Mikä oli epäselvää?"
- Vertaisopiskelijat täyttävät yksinkertaisen lomakkeen (2–3 pistettä)
- Tämä ei vaikuta viralliseen arvosanaan, mutta antaa opiskelijoille rakentavaa palautetta

## OSP3 Kokonaisuus (Yhteenveto)

Kun arviointi on valmis, osassa luokkaa voi tehdä pohdintakeskustelun:
- "Mitä kasvoi OSP3:n aikana?"
- "Mikä oli vaikeinta?"
- "Mitä yllätit sinut?"
- "Mitä haluaisit tehdä seuraavaksi?"

Tämä auttaa opiskelijoita näkemään oppimisen kokonaisuuden ja motivoi heidän jatkavia hankkeita.

