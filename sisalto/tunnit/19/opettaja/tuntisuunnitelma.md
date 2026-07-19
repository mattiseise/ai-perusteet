# Opettajan materiaalit — oppitunti 19: Agentin perusteet

## Osaamistavoitteet

Tavoitteena on ymmärtää määritelmä **agentti = kielimalli + harness** ja käyttää kuutta rakennusosaa kurssin suunnittelutarkistuslistana. Kaikki kuusi kohtaa eivät ole jokaisessa toteutuksessa pakollisia.

### Muistaa ja ymmärtää

- Opiskelija osaa selittää, mikä **agentti** on ja miten se eroaa chatbotista, skriptistä ja työnkulusta.
- Oppija tunnistaa kurssin kuusi suunnittelukohtaa: **syötekäsittelijä**, **päättelijä**, **työkalut**, **muisti**, **turvakerros** ja **palautesilmukka**.
- Oppija osaa perustella, milloin pitkäkestoinen muisti tai palautteesta oppiminen jätetään pois.
- Opiskelija ymmärtää **autonomisuuden** käsitteen ja sen rajat.
- Opiskelija osaa kuvata yhden toteutuksen **suoritusputken** ja erottaa sen kaikille agenteille pakollisten vaiheiden väitteestä.

**Opettajan painotus:** Korosta opiskelijoille, että agentti ei ole vain “älykkäämpi chatbot”. Agentti on järjestelmä, jolla on rakenne, toimintalogiikka, rajat ja kyky käyttää työkaluja tietyn tavoitteen saavuttamiseksi.

---

## Pedagoginen lähestymistapa

### Avaus: tuttu esimerkki sähköpostin käsittelystä

Aloita oppitunti opiskelijoille tutulla esimerkillä: sähköpostin käsittelyllä. Näytä, miten sama tehtävä voidaan automatisoida kolmella eri tavalla.

| Toteutustapa | Miten se toimii? | Rajoitus |
| --- | --- | --- |
| **Skripti** | Tekee yksinkertaisen ennalta määrätyn toiminnon, esimerkiksi siirtää viestin tiettyyn kansioon. | Ei tulkitse tilannetta eikä tee itsenäisiä päätöksiä. |
| **Työnkulku** | Seuraa sääntöjä, esimerkiksi: jos viestissä lukee “lasku”, ohjaa se taloushallintoon. | Toimii hyvin vain silloin, kun säännöt kattavat tilanteen. |
| **Agentti** | Kielimalli tulkitsee viestin, ja harness antaa sille tehtävän tilan, työkalut, oikeudet ja rajat. | Tarvitsee selkeän tavoitteen, rajatut oikeudet ja valvonnan. |

Kysy opiskelijoilta:

- Missä tilanteessa yksinkertainen skripti riittää?
- Milloin työnkulku on parempi kuin agentti?
- Milloin tarvitaan agenttia, joka pystyy tulkitsemaan tilannetta?

### Keskeinen käsite: hype vs. todellisuus

Moni opiskelija saattaa ajatella, että agentti tarkoittaa vain tavallista chatbotia uudella nimellä tai että kaikki tekoälyautomaatio on agenttitoimintaa. Tämä käsitys kannattaa purkaa heti oppitunnin alussa.

| Virheellinen ajatus | Korjaava ajatus |
| --- | --- |
| “Agentti on vain hienompi chatbot.” | Agentissa kielimallin ympärillä on harness: esimerkiksi tehtävän tila, työkalut, oikeudet ja turvarajat. Pitkäkestoinen muisti ei ole pakollinen. |
| “Kaikki tekoälyautomaatio on agenttia.” | Kaikki automaatio ei ole agenttitoimintaa. Agentilla on erityinen rakenne ja autonomisuuden aste. |

**Esimerkki opetukseen**

Kirjoita taululle: “Chatbot vastaa. Työnkulku seuraa sääntöjä. Agentti tulkitsee, päättää ja toimii rajojensa sisällä.” Palaa tähän erotteluun koko oppitunnin ajan.

---

## Kuuden kohdan tarkistuslista yhdessä esimerkkitoteutuksessa

Kurssin kuusi kohtaa ovat suunnittelutarkistuslista. Alla oleva **suoritusputki** on yksi sähköpostiesimerkki, johon kaikki kuusi kohtaa on valittu. Se ei tarkoita, että jokaisessa agentissa olisi nämä kuusi erillistä osaa tai sama järjestys.

**Sähköpostiagentin yksi mahdollinen suoritusputki**

|  |
| --- |
| **1. Syötekäsittelijä** Vastaanottaa viestin ja tekee datasta käsiteltävää. |
| ↓ |
| **2. Päättelijä** Analysoi tilanteen ja muodostaa päätöksen. |
| ↓ |
| **3. Työkalut** Suorittavat konkreettisia toimintoja, kuten haun, viestin lähetyksen tai tietokantapäivityksen. |
| ↓ |
| **4. Muisti — valinnainen** Tallentaa historiaa vain, jos myöhempi suoritus tarvitsee sitä ja käyttöoikeudet on määritelty. |
| ↓ |
| **5. Turvakerros** Validoi, rajoittaa ja estää vaarallisia tai epävarmoja toimintoja. |
| ↓ |
| **6. Palautesilmukka — valinnainen** Tuottaa seurantatietoa, jonka perusteella ihminen tai erikseen suunniteltu prosessi kehittää toteutusta. |

### Opetuskäytäntö: piirrä valinnat taululle

Piirrä taululle ensin ydin **kielimalli + harness**. Lisää kuusi tarkistuskohtaa ja käytä esimerkkinä sähköpostin käsittelyä:

1. **Sähköposti saapuu:** syötekäsittelijä muuttaa viestin agentille ymmärrettävään muotoon.
2. **Tilanne analysoidaan:** päättelijä arvioi, onko kyseessä lasku, reklamaatio, tukipyyntö vai muu viesti.
3. **Toiminto suoritetaan:** työkalut hakevat tietoja, luovat tiketin tai lähettävät vastauksen.
4. **Muistin tarve päätetään:** historia tallennetaan vain, jos myöhempi suoritus tarvitsee sitä.
5. **Turvallisuus tarkistetaan:** turvakerros varmistaa, ettei viestissä paljasteta arkaluonteisia tietoja tai tehdä liian riskialtista päätöstä.
6. **Seuranta suunnitellaan:** loki auttaa ihmistä testaamaan ja parantamaan toteutusta; kielimalli ei opi automaattisesti.

Korosta opiskelijoille:

> Agentti = kielimalli + harness. Kuusi kohtaa auttavat perustelemaan toteutusvalinnat, eivät määrää yhtä pakollista putkea.

---

## Opiskelijoiden kokemusten hyödyntäminen

Kiinnitä oppiminen opiskelijoiden omiin kokemuksiin kysymällä:

- Kuinka moni teistä on käyttänyt chatbottia asiakaspalvelussa?
- Oletteko nähneet järjestelmää, joka tekee jotakin automaattisesti ilman käyttäjän suoraa toimintaa?
- Missä arjen tilanteessa järjestelmä tekee päätöksen puolestanne?
- Mistä tietää, onko kyseessä vain sääntö vai agenttimainen toiminta?

Voit kirjata opiskelijoiden esimerkit taululle kolmeen sarakkeeseen: **chatbot**, **työnkulku** ja **agentti**.

---

## Yleisiä väärinkäsityksiä

### Väärinkäsitys 1: “Agentti on aina parempi kuin chatbot.”

**Korjaava näkökulma:** Agentti on monimutkaisempi, kalliimpi ja riskialttiimpi kuin tavallinen chatbot. Agentti on järkevä silloin, kun tehtävä on toistuva, monivaiheinen ja vaatii itsenäisiä päätöksiä tai työkalujen käyttöä.

### Väärinkäsitys 2: “Agentti voi tehdä mitä tahansa.”

**Korjaava näkökulma:** Agentti toimii vain harnessin antamien tavoitteiden, työkalujen, oikeuksien ja rajoitusten puitteissa. Pitkäkestoinen muisti lisätään vain perustellusta tarpeesta.

### Väärinkäsitys 3: “Autonomisuus tarkoittaa, että agentti toimii ilman valvontaa.”

**Korjaava näkökulma:** Autonomisuus tarkoittaa, että agentti voi tehdä päätöksiä oman logiikkansa perusteella, mutta ihmisten määrittelemissä rajoissa. Erityisesti kriittisissä sovelluksissa valvonta, hyväksyntäportit ja turvakerrokset ovat välttämättömiä.

### Väärinkäsitys 4: “Agentti on sama kuin työnkulku.”

**Korjaava näkökulma:** Työnkulku seuraa yleensä ennalta määriteltyjä sääntöjä. Agentissa kielimalli voi tulkita tilannetta ja valita harnessin sallimia työkaluja. Muisti tai automaattinen palautteesta oppiminen eivät ratkaise luokitusta.

### Väärinkäsitys 5: “Jokaisessa agentissa on samat kuusi osaa.”

**Korjaava näkökulma:** Kuusi kohtaa ovat kurssin suunnittelutarkistuslista. Agentin ydin on kielimalli + harness. Pitkäkestoinen muisti tai palautekierros voidaan jättää pois, jos tehtävä ei niitä tarvitse; mukaan valittujen osien pitää toimia ja oikeuksien olla rajatut.

### Väärinkäsitys 6: “Agentti pitää aina rakentaa itse.”

**Korjaava näkökulma:** Valmisagenteissa — esimerkiksi tekoälysovellusten agenttitiloissa — voidaan arvioida samalla kuuden kohdan suunnittelutarkistuslistalla; joku muu on vain tehnyt suunnittelutyön. Kurssilla rakennetaan oma agentti, jotta valmiitakin osaa arvioida. Osta vai rakenna -valintaa käsitellään tunnilla 20.

### Väärinkäsitys 7: “ChatGPT tai muu tekoälychat on agentti.”

**Korjaava näkökulma:** Chat vastaa viesteihin, agentti suorittaa vaiheita työkaluilla omien oikeuksiensa rajoissa. Sama kielimalli voi olla kummankin sisällä — ero ei ole mallissa vaan harnessissa eli mallin ympärille rakennetuissa työkaluissa, muistissa, oikeuksissa ja turvarajoissa.

*Ajankohtaishuomio 7/2026, vanhenee:* mallien tasonimet eivät ole agenttituotteita. Esimerkiksi GPT-5.6-mallin lippulaivataso “Sol” ei ole agentti, vaan OpenAI:n agenttituote on ChatGPT Work. Jos opiskelija niputtaa nämä yhteen, erottele malli, mallin taso ja agenttituote.

---

## Luokkatehtävä — ohjeistus

### Tehtävä 1: Luokittelu

**Tavoite:** Opiskelijat harjoittelevat erottamaan **agentin**, **chatbotin**, **skriptin** ja **työnkulun** toisistaan.

Kun opiskelijat tekevät luokittelutehtävää, he saattavat ajatella liian nopeasti, että automaattinen järjestelmä on aina agentti. Ohjaa heitä kysymään tarkentavia kysymyksiä.

**Opettajan tarkistuskysymys:** Jos opiskelija sanoo “tämä on agentti, koska se on automaattinen”, kysy: “Missä kielimalli tulkitsee tilanteen ja mitä työkaluja, oikeuksia tai turvarajoja harness antaa sille?”

**Hyvä perustelu sisältää:**

- maininnan siitä, tekeekö järjestelmä itsenäisiä päätöksiä,
- kuvauksen siitä, käyttääkö järjestelmä työkaluja,
- perustelun siitä, tarvitaanko pitkäkestoista muistia tai palautekierrosta,
- arvion siitä, onko järjestelmällä turvakerros tai rajoitukset.

### Tehtävä 2: Toteutusvalintojen jäljittäminen

**Tavoite:** Opiskelijat soveltavat kuuden kohdan tarkistuslistaa konkreettiseen esimerkkiin ja nimeävät myös tarpeettoman kohdan.

Käytä visuaalista kaaviota. Piirrä agentin komponentit silmukkana ja jäljitä, miten asiakaspalveluagentti käsittelee viestin.

| Komponentti | Asiakaspalveluagentin esimerkki |
| --- | --- |
| **Syötekäsittelijä** | Sähköposti tai chat-viesti saapuu ja siitä poimitaan tärkeät tiedot. |
| **Päättelijä** | Agentti analysoi asiakkaan ongelman, kiireellisyyden ja sopivan toimintatavan. |
| **Työkalut** | Agentti hakee tietoa tietokannasta, päivittää tiketin tai lähettää vastauksen. |
| **Muisti — valinnainen** | Agentti hyödyntää asiakkaan historiaa vain, jos myöhempi suoritus tarvitsee sitä ja käsittely on sallittu. |
| **Turvakerros** | Agentti tarkistaa, ettei vastaus sisällä arkaluonteisia tietoja ja että toiminto on sallittu. |
| **Palautesilmukka — valinnainen** | Loki ja asiakaspalaute auttavat ihmistä arvioimaan ja korjaamaan toteutusta. |

Kysy opiskelijoilta:

- Mikä tarkistuskohta on tässä tehtävässä välttämätön ja miksi?
- Voiko agentti toimia ilman pitkäkestoista muistia tässä tapauksessa?
- Mitä tapahtuu, jos turvakerros puuttuu?
- Miten seurantatieto voisi auttaa ihmistä parantamaan toteutusta?

### Tehtävä 3: Riskianalyysi

**Tavoite:** Opiskelijat ymmärtävät autonomisuuden riskit ja osaavat selittää, miksi agentille tarvitaan rajoja.

Keskustelkaa siitä, mitä tapahtuu, jos jokin agentin keskeinen komponentti epäonnistuu.

| Epäonnistuva osa | Mitä voi tapahtua? | Miten riskiä vähennetään? |
| --- | --- | --- |
| **Syötekäsittelijä** | Agentti ymmärtää asiakkaan viestin väärin ja valitsee väärän toimintatavan. | Syötteen validointi ja epäselvien viestien ohjaaminen ihmiselle. |
| **Muisti** | Agentti unohtaa aiemmat tapahtumat tai käyttää vanhentunutta tietoa. | Ajantasainen tietopohja, lokit ja muistin tarkistus. |
| **Turvakerros** | Agentti lähettää arkaluonteista tietoa tai tekee liian riskialttiin päätöksen. | Rajoitukset, hyväksyntäportit ja minimioikeusperiaate. |
| **Palautesilmukka** | Toteutuksen laatua ei seurata tai palautetta tulkitaan väärin. | Palautteen laadun tarkistus ja ihmisen ohjaama parantaminen. |

**Esimerkki opetukseen**

Käytä riskianalyysissä konkreettista tilannetta: asiakaspalveluagentti tulkitsee vihaisen reklamaation tavalliseksi laskukysymykseksi ja lähettää automaattisen rutiinivastauksen. Kysy, mikä komponentti epäonnistui ja miten tilanne olisi voitu estää.

---

## Arviointivihjeet

### Hyvä vastaus

“Tämä on agentti, koska kielimalli tulkitsee tilanteen ja harness antaa sille rajatut työkalut tavoitteen saavuttamiseen. Tässä tehtävässä nykyisen suorituksen tila riittää, joten pitkäkestoinen muisti voidaan jättää pois. Tulokset kirjataan ihmisen tekemää arviointia varten.”

### Riittävä vastaus

“Tämä on agentti, koska siinä on kielimalli ja sille työkalut sekä rajat antava harness.”

### Heikko vastaus

“Tämä on agentti, koska se on tekoäly” tai “koska se on nopea.”

---

## Jatkoyhteys oppituntiin 20

Oppitunti 20 käsittelee sitä, **milloin agentti on oikea ratkaisu**. Tämä oppitunti luo pohjan jatkolle: opiskelijat ymmärtävät määritelmän kielimalli + harness ja osaavat käyttää kuutta kohtaa valinnaisena suunnittelutarkistuslistana. Seuraavaksi he arvioivat, milloin agentti on hyödyllinen ja milloin yksinkertaisempi ratkaisu riittää.

> **Pohdi seuraavaa tuntia varten:** Missä tilanteessa agentti olisi liian monimutkainen ratkaisu? Milloin tavallinen työnkulku tai chatbot riittäisi?

---


## 90 minuutin toteutus ja eriyttäminen

Tallennettava tuotos on **agenttiongelman suunnittelupohja ja kuuden kohdan soveltuvuus**. Pakollinen ydintuotos pidetään samana kaikilla reiteillä.

| Aika | Vaihe | Opettajan tehtävä |
|---|---|---|
| 0–10 min | Virittäytyminen | Kytke ydinkysymys tuttuun tilanteeseen ja tarkista lähtötaso. |
| 10–25 min | Ydinkäsite | Mallinna tunnin keskeinen ero yhdellä vastaesimerkillä. |
| 25–65 min | Perustuotos | Oppija täyttää yhdestä ongelmasta agentticavaksen ja arvioi kuuden suunnittelukohdan tarpeen. Tämä 40 minuutin jakso on itsenäistä tai parin kanssa tehtävää työskentelyä. |
| 65–80 min | Testaus ja purku | Testauta tuotos annetulla tapauksella ja pura yksi onnistuminen sekä yksi korjaus. |
| 80–90 min | Tallennus ja lopputehtävä | Varmista tiedoston nimi, tallennuspaikka ja yhden lauseen johtopäätös. |

### Tukireitti

Oppija käyttää annettua esimerkkitapausta ja tarkistuslistaa. Tuki vähentää valintojen määrää, mutta säilyttää saman ydintuotoksen ja perustelun.

### Syventävä reitti

Kun perustuotos on valmis, oppija perustelee, miksi pitkäkestoinen muisti tai palautteesta oppiminen jätetään pois. Syventävä työ ei kasvata pakollista ydintuotosta.
