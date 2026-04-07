# Opiskelutehtävät: Bottiprojekti, osa 1 — suunnittele ja rakenna

## Tekoälyjen käyttö -osion arvioitava projekti (osa 1/2)

Oppitunneilla 17 ja 18 rakennat oman Custom-botin, testaat sen ja esittelet tuloksen. Tämä on Tekoälyjen käyttö -osion arvioitava projekti. Käytä kaikkia neljää botin rakennuspalaa, jotka olet kerännyt oppitunneilla 10, 12, 14 ja 16.

Projekti jakautuu kahteen osaan: oppitunnilla 17 suunnittelet ja rakennat botin, oppitunnilla 18 viimeistelet, testaat ja esittelet sen.

### Mitä rakennat?

Rakennat Custom-botin (Custom GPT tai vastaavan), joka toteuttaa käyttötapauksen, jonka valitsit rakennuspalassa 1. Botti käyttää system promptia ohjaamaan käyttäytymistään ja osaa kerätä kontekstia käyttäjältä vuorovaikutteisesti.

### Miten käytät rakennuspaloja?

**Rakennuspala 1** (oppitunti 10) kertoo, minkä alustan valitsit ja mitä ongelmaa ratkaiset. **Rakennuspala 2** (oppitunti 12) kertoo, miten botti kerää kontekstia käyttäjältä. **Rakennuspala 3** (oppitunti 14) kertoo, millainen botin persoonallisuus on — tarkoitus, rooli, ohjeet ja rajaukset. **Rakennuspala 4** (oppitunti 16) kertoo, miten varmistat vastuullisen käytön. Yhdessä nämä neljä rakennuspalaa muodostavat kattavan suunnitelman, jonka pohjalta kirjoitat system promptin ja rakennat botin.

---

## Tehtävä 17.1: Suunnittele botin kysymyspatteristo (30 min)

### Tavoite

Määritellä, mitä kysymyksiä botti esittää käyttäjälle ja missä järjestyksessä. Tämä perustuu rakennuspaljoihin 2 ja 3.

### Ohjeet

1. Lue uudelleen self-study-materiaali, erityisesti osio "Mitä hyvä projektisuunnitelma sisältää".

2. Kirjoita muistiin **botin tarkoitus ja rooli** (pohjaudu rakennuspalaan 3):
   - Mikä botti on? (Esimerkiksi: "Projektin mentor, jolla on kokemus projektinjohdosta")
   - Mitä se tekee? (Esimerkiksi: "Auttaa käyttäjää luomaan projektisuunnitelman")

3. Suunnittele **vähintään 15 kysymystä**, joita botti esittää (perusta rakennuspalaan 2). Ne pitäisi ryhmitellä viiteen pääosaan:
   - **Mitä?** (3–4 kysymystä): Projektin kuvaus, tuote, ominaisuudet
   - **Kenelle?** (3–4 kysymystä): Käyttäjät, asiakkaat, heidän profiili
   - **Miksi?** (2–3 kysymystä): Tarkoitus, miksi projekti on olemassa, hyödyt
   - **Milloin?** (2–3 kysymystä): Aikataulu, vaiheet, deadlinet
   - **Miten?** (3–4 kysymystä): Resurssit, tiimi, tekniikka, budjetti

4. Kirjoita jokaiseen kysymykseen **tarkennuskysymys**, jos käyttäjä vastaa epäselvästi. Esimerkiksi: "Jos käyttäjä sanoo 'nuoret', tarkentavat kysymykset: minkä ikäiset? Missä?"

### Odotettu tuotos

Dokumentti, joka sisältää:
- Botin tarkoitus ja rooli (1 kappale, pohjaudu rakennuspalaan 3)
- Viisi ryhmää kysymyksiä (vähintään 15 kysymystä yhteensä, pohjaudu rakennuspalaan 2)
- Jokaisen ryhmän jälkeen merkittävät "syvennä"-kysymykset

**Esimerkki:**
```
BOTTI: Projektin mentor
TARKOITUS: Auttaa käyttäjää luomaan selkeän projektisuunnitelman

MITÄ-osio (projektin kuvaus):
1. "Miten lyhyesti kuvaisisit projektiasi? (2-3 lausetta)"
   Syvennä: Jos epäselvää → "Entä mitä tuotetta tai palvelua rakennetaan?"
2. "Mitkä ovat projektin pääominaisuudet?"
   Syvennä: "Mikä näistä on tärkein?"
...

KENELLE-osio:
1. "Kuka käyttää tuotettasi tai palveluasi?"
...
```

---

## Tehtävä 17.2: Kirjoita system prompt ja luo botti (30 min)

### Tavoite

Kirjoittaa system prompt (botin ohjeistus) ja luoda botti, joka yhdistää kaikki neljä rakennuspalaa.

### Ohjeet

1. Käytä tehtävä 17.1:stä saatua kysymyslistaa ja kaikki neljä rakennuspalaa.

2. Kirjoita **system prompt** (300–500 sanaa), joka sisältää:
   - **Identiteetti**: Kuka botti on? (rooli, kokemus) — perustuu rakennuspalaan 3
   - **Tarkoitus**: Mitä botti tekee? — perustuu rakennuspalaan 1
   - **Ohjeet**: Miten botti kysyy ja kerää kontekstia? (järjestys, miten kuuntele, miten koota vastaukset) — perustuu rakennuspalaan 2
   - **Rajaukset ja vastuullinen käyttö**: Mitä botti ei saa tehdä? — perustuu rakennuspalaan 4

   **Esimerkki alkua:**
   > Olet Projektiseutu-niminen botti. Sinulla on 12 vuoden kokemus projektinjohdosta ja liiketoimintasuunnittelusta. Olet mentori, joka auttaa ihmisiä luomaan selkeitä, toteutettavia projektisuunnitelmia.
   >
   > Tarkoituksesi: Saada käyttäjä ajattelemaan projektin kaikki kriittiset puolet esittämällä järjestelmällisiä kysymyksiä ja kokoamalla vastaukset valmiiksi dokumentiksi.
   >
   > Ohjeet:
   > 1. Aloita aina ystävällisellä esittelyllä ja kysymällä lyhyttä projektikuvausta.
   > 2. Kysy vain yksi kysymys kerrallaan.

3. **Luo botti** yhdellä näistä tavoista:
   - **Vaihtoehto A**: Custom GPT OpenAI:ssä (jos sinulla on pääsy ChatGPT Plusiin)
   - **Vaihtoehto B**: Claude Projects -ominaisuus (jos käytät Claude Webissa)
   - **Vaihtoehto C**: Testaa Claude-chatissa kopioimalla system promptin ja testaamalla sitä suoraan

   Opettaja kertoo, kumpaa alustaa käytetään.

4. Liitä lopullinen system prompt dokumenttiin.

### Odotettu tuotos

- System prompt (300–500 sanaa), selkeästi kirjoitettu — **sisältää viitteet kaikkiin neljään rakennuspalaan**
- Kuvakaappaus tai linkki luottuun bottiin
- Lyhyt kommentti: "Miten botti käyttäytyy?" ja "Mitä haluat testata ensi tehtävässä?"

---

## Tehtävä 17.3: Testaa bottia kahdella projektiskenaarilla (30 min)

### Tavoite

Testata botti kahden eri projektikuvauksen avulla. Nähdä, kysyykö se oikeita kysymyksiä, muistaako vastaukset, ja syntyykö lopussa järkevä suunnitelma.

### Ohjeet

1. Valitse **kaksi erilaista projektiasiakirjaa** (katso esimerkkejä alla).

2. **Testaus 1**: Kirjoita ensimmäinen projektikuvaus botille ja dokumentoi:
   - **Syöte**: Alkuperäinen projektikuvaus (kopioi)
   - **Botin kysymykset**: Mitä kysyi? Missä järjestyksessä?
   - **Vastauksesi**: Mitä vastasit?
   - **Lopputulos**: Mitä botti koosti? (kopioi tai kuvakaappaa)
   - **Analyysi**: Oliko suunnitelma järkevä? Olivatko kaikki asiat oikein? Mitä puuttui? Liittyivätkö kysymykset rakennuspalaan 2?

3. **Testaus 2**: Toista sama prosessi toisella projektikuvauksella.

4. **Vertailu**: Vertaa tuloksia:
   - Kysyikö botti samoja kysymyksiä vai sopeutuiko se projektiin?
   - Oliko toinen suunnitelma parempi kuin toinen? Miksi?
   - Mitä botti teki hyvin? Mitä voisi parantaa?
   - Toteutuivatko rakennuspalat 1–4 odotetusti?

### Projektiskenaarioiden esimerkkejä

**Projekti A:** "Rakennan mobiilisovellusta, joka auttaa nuoria harjoittamaan matematiikkaa pelaamisen avulla. Idea on pelaavia oppimistehtäviä."

**Projekti B:** "Olen IT-konsultti, ja asiakkaani haluaa parantaa asiakaspalvelun tehokkuutta automatisoinnilla. Ei ole vielä tarkasti määritelty, mitä automatisoida."

(Voit käyttää omia ideoitasi, kunhan ne ovat riittävän selkeät aloituksiksi.)

### Odotettu tuotos

Dokumentaatio, joka sisältää:

**Testaus 1:**
- Projektikuvaus (2–3 lausetta)
- Botin kysymykset (numeroidusta listasta)
- Käyttäjän vastaukset
- Lopullinen suunnitelma (botin tuottama)
- Analyysi: "Botti kysyi hyviä kysymyksiä, koska... Puuttui [asia], koska..." — viittaa rakennuspalaan 2

**Testaus 2:**
- Sama rakenne kuin testaus 1

**Yhteenveto:**
- Mitkä olivat suurimmat erot kahden testin välillä?
- Oliko botti tasapainoisesti kysyvä vai painottuiko se johonkin osaan?
- Mikä oli paras vastaus botilta? Mikä pahin?
- Seuraavassa iteraatiossa, mitä haluaisit muuttaa rakennuspalista 1–4?

---

## Tehtävä 17.4: Iteraatio ja parantaminen (sisältyy 17.3:een)

### Tavoite

Testaustulosten perusteella parantaa bottia seuraavalle kerralle (oppitunti 18).

### Ohjeet

1. Lue tehtävä 17.3:n analyysi uudelleen.

2. Kirjoita **muutosluettelo** (3–5 kohtaa):
   - Mikä ei toiminut hyvin?
   - Miksi se ei toiminut?
   - Miten haluat korjata sen?
   - Mitkä osat system promptista muuttuvat?
   - Mitkä rakennuspalat (1–4) vaativat tarkennusta?

3. **Valinnainen**: Jos sinulla on aikaa, tee uudet testit korjatulla promptilla ja dokumentoi parantuminen.

### Esimerkki muutosluettelosta

```
ONGELMA 1: Botti unohti ensimmäisen vastauksen
SYY: System promptissa ei ole ohjeita muistiinpanoista (rakennuspala 2)
KORJAUS: Lisää: "Muista aina, mitä käyttäjä sanoi ensimmäisessä vastauksessa"
TULOS: Testataan seuraavalla kerralla

ONGELMA 2: Botti ei kysynnyt budjettiin liittyen
SYY: Kysymykset olivat liian vähäisiä "Miten"-osiossa (rakennuspala 2)
KORJAUS: Lisää "Mikä on budjetti?" ja "Onko sinulla rahasummaa?"
TULOS: Seuraavalla testilla pitäisi kysyä paremmin
```

### Odotettu tuotos

Dokumentaatio 3–5 muutoksesta:
- Mikä ei toiminut
- Miten korjataan
- Mitä odotetaan seuraavaksi
- **Viittaukset rakennuspaloihin 1–4**

---

## Palautusvaatimukset

Palauta kaikki 4 tehtävää yhtenäisenä dokumenttina tai kansiossa:

1. **Tehtävä 17.1:** Kysymyspatteristo (½–1 sivu)
2. **Tehtävä 17.2:** System prompt (1 sivu) + kuvakaappaus botista
3. **Tehtävä 17.3:** Kaksi testiskenaarion dokumentaatiota (1½–2 sivua) + yhteenveto
4. **Tehtävä 17.4:** Muutosluettelo (½ sivu)

**Yhteensä:** ~3–4 A4-sivua

Voit palauttaa:
- Word-dokumenttina (.docx)
- PDF:nä
- Google Docsina (jaa linkkiin)
- Tekstina Moodlessa

---

## Vihjeet onnistumiseen

- **Kysymykset**: Kirjoita ne käyttäjäystävällisesti. Kysy selkeästi, mitä tarkoitat. Älä käytä jargonia.
- **System prompt**: Ole yksityiskohtainen. "Kysy oikeat kysymykset" on liian epämääräinen. "Kysy ensin mitä projektista, sitten kenelle, sitten miksi" on selvä.
- **Rakennuspalat**: Varmista, että kaikki neljä rakennuspalaa (oppitunnit 10, 12, 14, 16) näkyvät system promptissa ja testauksessa.
- **Testaus**: Käytä kahta täysin erilaista projektia. Ei riitä, että testaat samantapaista ideaa kahdesti.
- **Dokumentaatio**: Näytä, mitä botti sanoi. Kopioi sen vastaukset. Opettaja haluaa nähdä, mitä tapahtui.
- **Rehellisyys**: Jos botti epäonnistui, se on OK. Dokumentoi epäonnistuminen. Yritä ymmärtää miksi.

---

## Aikataulu

- **Tehtävä 17.1:** 30 minuuttia
- **Tehtävä 17.2:** 30 minuuttia
- **Tehtävä 17.3:** 30 minuuttia
- **Tehtävä 17.4:** 10–15 minuuttia

**Yhteensä:** ~2 tuntia

---

## Muistutus

Tämä on Tekoälyjen käyttö -osion arvioinnin **ensimmäinen osa** kahdesta. Seuraavalla kerralla (oppitunti 18):
- Viimeistelet botin
- Parannat sitä testaustulosten perusteella
- Esittelette botin (esittelytehtävä)
- Arviointi valmistuu

Tämä oppitunti on perustan rakentaminen. Seuraava on viimeistely. Molemmat yhdessä muodostavat kokonaisuuden.

Onnea!
