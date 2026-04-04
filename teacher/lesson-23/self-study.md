# Agentin konteksti, muisti ja tila

## Johdanto: Mitä botti muistaa?

Ajattele hetki: kun keskustelet bottia kanssa, muistaa se, mitä sinä sanoit minuutti sitten? Entä tunti sitten? Entä eilen? Vastaus on: riippuu siitä, miten agentti on suunniteltu.

Tässä oppitunnissa käsittelemme kolme asiaa, jotka tekevät agentista "älykkään": **konteksti**, **muisti** ja **tila**. Nämä ovat tekniikkaa, joiden avulla agentti näyttää ymmärtävän, mitä tapahtuu, vaikka se ei oikeasti ajattele. Se on kuin näytelmä: näytelmässä näyttelijä muistaa, mitä hän sanoi edellisessä kohtauksessa, vaikka hän unohtaa sen kahden tunnin välityönnillä.

## Konteksti-ikkuna: mitä agentti näkee nyt

Agentti ei näe koko keskustelua kerralla. Se näkee vain pienen ikkunan viimeisistä viesteistä. Tätä kutsutaan **konteksti-ikkunaksi** (context window).

Esimerkiksi: chat-botti, jossa konteksti-ikkuna on viimeinen 10 viestia. Kun käyttäjä kirjoittaa 11. viestin, agentti unohtaa ensimmäisen viestin automaattisesti. Se on kuin katsoit näyttöä, joka näyttää vain kymmenen viimeistä tekstiä samalla, kun loput pyyhkiytyy pois.

Konteksti-ikkunan koko on tärkeä:
- **Liian pieni**: Agentti unohtaa tärkeitä tietoja nopeasti. "Mikä oli nimesi? En muista, että olisit sanonut."
- **Liian suuri**: Agentti joutuu käsittelemään paljon vanhoja tietoja, mikä tekee siitä hitaampaa ja kalliimpaa.

Ammattilaisena sinun täytyy ymmärtää, millainen konteksti-ikkuna on sopiva tietylle sovellukselle.

**Pysähdy hetkeksi: Kuvittele asiakaspalvelubottia. Kuinka monta viimeistä viestiä sen pitäisi muistaa, että se ymmärtää asiakkaan ongelman?**

## Pitkäaikainen muisti: mitä agentti muistaa seuraavalla kerralla

Konteksti-ikkuna auttaa agentin ymmärtää *nykyistä* keskustelua. Mutta entä jos agentti täytyy muistaa, mitä käyttäjä sanoi viime viikolla?

Tätä varten agentti tarvitsee **pitkäaikaista muistia** (long-term memory). Pitkäaikainen muisti tallennetaan ulkoiseen järjestelmään — tietokantaan, tiedostoihin tai **vektoritietokantaan**.

**Vektoritietokanta** (vector database) on erityinen tyyppi tietokantaa, joka tallentaa tietoa "merkitysten" perusteella, ei vain avainsanoilla. Esimerkiksi:
- Käyttäjä sanoo: "Minulla on vihertävä tuote, joka ei toimi."
- Agentti muuntaa tämän vektoreiksi (matemaattiseksi koodiksi)
- Myöhemmin, kun käyttäjä palaa, agentti voi hakea: "Millä tuotteella sinulla oli ongelma?" ja löytää "vihertävän tuotteen" nopeasti, vaikka käyttäjä ei käytä täsmälleen samoja sanoja.

Pitkäaikainen muisti auttaa agentin ymmärtää käyttäjän historiaa:
- "Viime viikolla sinulla oli ongelma X. Onko se nyt ratkaistu?"
- "Sinä olet ostanut meiltä 10 kertaa. Tässä on VIP-alennuksesi."

Tämä tekee agentista paljon hyödyllisemmän, koska se ei aina kysy samoja kysymyksiä.

**Pysähdy hetkeksi: Ajattele sopimusta, jonka allekirjoitit kuukausi sitten. Mitä agentti pitäisi muistaa siitä sopimuksesta seuraavalla kerralla, kun kirjoitat?**

## Tila: missä vaiheessa prosessi on?

Tila (state) on tieto siitä, **missä vaiheessa agentti on**. Se on kuin tehtävälista:
- Asiakas tilaa tuotteen (vaihe 1: "tilaus luotu")
- Agentti lähettää vahvistuksen (vaihe 2: "vahvistus lähetetty")
- Varasto pakkaa tuotteen (vaihe 3: "pakattavana")
- Tuote lähetetään (vaihe 4: "lähetetty")
- Asiakas vastaanottaa (vaihe 5: "toimitettu")

Jokainen vaihe on eri **tila**. Agentti muistaa, missä vaiheessa tilaus on, jotta se ei lähetä useita vahvistuksia tai yrityä lähettää tuotetta, joka on jo lähtenyt.

Tila voi myös sisältää muuttujia:
- "Asiakas hyväksyi: KYLLÄ/EI"
- "Maksu suoritettu: 45€"
- "Uudelleenyritykset: 2/3"

Ilman tilaa agentti olisi sotkuinen. Se ei tietäisi, mitä se oli tekemässä, ja tekisi samoja asioita uudelleen.

## Käytännön esimerkki: Tiketti-agentti

Kuvittele IT-tuki-agentia, joka käsittelee asiakastukitikettejä:

**Konteksti:**
- Agentti näkee viimeisen 20 viestiä tikettistä
- Näkee asiakkaan viimeisen kysymyksen ja IT-henkilön vastauksen
- Voi ymmärtää: "Mitä asiakkaan ongelma on tällä hetkellä?"

**Pitkäaikainen muisti:**
- Agentti muistaa, että tämä asiakas on ollut meillä 2 vuotta
- Muistaa, että hänellä oli samanlainen ongelma 3 kuukautta sitten
- Muistaa, mitä ratkaisuja kokeiltiin
- Voi ehdottaa: "Viime kerralla ratkaisi vaihtamalla välimuistin. Haluat kokeilla uudelleen?"

**Tila:**
- Tiketti on tilassa "AVOIN"
- Asiakkaalla ole vastannut 2 päivään
- Escalation-taso: "taso 1" (helpdesk)
- Yritykset: 1 / 3

Nämä kolme tekijää tekevät tuesta paljon paremmaksi kuin naiivin agentin, joka kysyy samoja kysymyksiä joka kerta.

## Yhteenveto

Agentti ei ole koskaan yksinään. Sillä on **konteksti-ikkuna**, joka näyttää nykyisen keskustelun (10-100 viimeistä viestiä). Sillä voi olla **pitkäaikainen muisti**, joka muistaa käyttäjän historian (vektoritietokantaa käyttämällä). Ja sillä on **tila**, joka muistaa, missä vaiheessa prosessi on. Nämä kolme tekijää tekevät agentista näennäisesti älykkään ja käyttökelpoisen. Ammattilaisena sinun täytyy ymmärtää, mitä muistia agentti tarvitsee, jotta se voi tehdä hyödyllisiä asioita.
