# Opettajan materiaalit — oppitunti 19: Agentin perusteet

## Osaamistavoitteet

Tämän oppitunnin tavoitteena on, että opiskelija ymmärtää, mikä **agentti** on, miten se eroaa muista automaation muodoista ja miksi agentin kuusi rakennusosaa muodostavat yhdessä toimivan kokonaisuuden.

### Muistaa ja ymmärtää

- Opiskelija osaa selittää, mikä **agentti** on ja miten se eroaa chatbotista, skriptistä ja työnkulusta.
- Opiskelija tunnistaa agentin kuusi rakennusosaa: **syötekäsittelijä**, **päättelijä**, **työkalut**, **muisti**, **turvakerros** ja **palautesilmukka**.
- Opiskelija ymmärtää **autonomisuuden** käsitteen ja sen rajat.
- Opiskelija ymmärtää **suoritusputken** käsitteen ja osaa kuvata, miten agentin komponentit toimivat yhdessä.

**Opettajan painotus:** Korosta opiskelijoille, että agentti ei ole vain “älykkäämpi chatbot”. Agentti on järjestelmä, jolla on rakenne, toimintalogiikka, rajat ja kyky käyttää työkaluja tietyn tavoitteen saavuttamiseksi.

---

## Pedagoginen lähestymistapa

### Avaus: tuttu esimerkki sähköpostin käsittelystä

Aloita oppitunti opiskelijoille tutulla esimerkillä: sähköpostin käsittelyllä. Näytä, miten sama tehtävä voidaan automatisoida kolmella eri tavalla.

| Toteutustapa | Miten se toimii? | Rajoitus |
| --- | --- | --- |
| **Skripti** | Tekee yksinkertaisen ennalta määrätyn toiminnon, esimerkiksi siirtää viestin tiettyyn kansioon. | Ei tulkitse tilannetta eikä tee itsenäisiä päätöksiä. |
| **Työnkulku** | Seuraa sääntöjä, esimerkiksi: jos viestissä lukee “lasku”, ohjaa se taloushallintoon. | Toimii hyvin vain silloin, kun säännöt kattavat tilanteen. |
| **Agentti** | Tulkitsee viestin, arvioi tilanteen, käyttää työkaluja ja päättää seuraavan toiminnon rajojensa sisällä. | Tarvitsee selkeän tavoitteen, rajoitukset, turvakerroksen ja valvonnan. |

Kysy opiskelijoilta:

- Missä tilanteessa yksinkertainen skripti riittää?
- Milloin työnkulku on parempi kuin agentti?
- Milloin tarvitaan agenttia, joka pystyy tulkitsemaan tilannetta?

### Keskeinen käsite: hype vs. todellisuus

Moni opiskelija saattaa ajatella, että agentti tarkoittaa vain tavallista chatbotia uudella nimellä tai että kaikki tekoälyautomaatio on agenttitoimintaa. Tämä käsitys kannattaa purkaa heti oppitunnin alussa.

| Virheellinen ajatus | Korjaava ajatus |
| --- | --- |
| “Agentti on vain hienompi chatbot.” | Agentilla on tavoite, työkalut, muisti, turvakerros ja kyky toimia rajatusti itsenäisesti. |
| “Kaikki tekoälyautomaatio on agenttia.” | Kaikki automaatio ei ole agenttitoimintaa. Agentilla on erityinen rakenne ja autonomisuuden aste. |

**Esimerkki opetukseen**

Kirjoita taululle: “Chatbot vastaa. Työnkulku seuraa sääntöjä. Agentti tulkitsee, päättää ja toimii rajojensa sisällä.” Palaa tähän erotteluun koko oppitunnin ajan.

---

## Suoritusputki: agentin kuusi komponenttia yhdessä

Agentin voima ei synny yksittäisestä komponentista, vaan siitä, että kuusi komponenttia muodostavat yhdessä **suoritusputken**. Suoritusputki tarkoittaa prosessia, jossa yhden vaiheen tulos vaikuttaa seuraavaan vaiheeseen.

**Agentin suoritusputki**

|  |
| --- |
| **1. Syötekäsittelijä** Vastaanottaa viestin ja tekee datasta käsiteltävää. |
| ↓ |
| **2. Päättelijä** Analysoi tilanteen ja muodostaa päätöksen. |
| ↓ |
| **3. Työkalut** Suorittavat konkreettisia toimintoja, kuten haun, viestin lähetyksen tai tietokantapäivityksen. |
| ↓ |
| **4. Muisti** Tallentaa ja hyödyntää historiaa, aiempia tapauksia tai käyttäjäkohtaisia tietoja. |
| ↓ |
| **5. Turvakerros** Validoi, rajoittaa ja estää vaarallisia tai epävarmoja toimintoja. |
| ↓ |
| **6. Palautesilmukka** Kerää tuloksia ja parantaa seuraavia kierroksia. |

### Opetuskäytäntö: piirrä sykli taululle

Piirrä taululle kuuden komponentin sykli ja käytä esimerkkinä sähköpostin käsittelyä:

1. **Sähköposti saapuu:** syötekäsittelijä muuttaa viestin agentille ymmärrettävään muotoon.
2. **Tilanne analysoidaan:** päättelijä arvioi, onko kyseessä lasku, reklamaatio, tukipyyntö vai muu viesti.
3. **Toiminto suoritetaan:** työkalut hakevat tietoja, luovat tiketin tai lähettävät vastauksen.
4. **Tulos tallennetaan:** muisti säilyttää tapahtuman ja mahdollisen asiakashistorian.
5. **Turvallisuus tarkistetaan:** turvakerros varmistaa, ettei viestissä paljasteta arkaluonteisia tietoja tai tehdä liian riskialtista päätöstä.
6. **Palaute sulkee silmukan:** asiakkaan vastaus tai työn lopputulos auttaa parantamaan seuraavaa käsittelyä.

Korosta opiskelijoille:

> Agentti ei ole vain lista osia. Se on prosessi, jossa jokainen vaihe vaikuttaa seuraavaan.

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

**Korjaava näkökulma:** Agentti toimii vain sille annettujen tavoitteiden, työkalujen, oikeuksien, muistin ja rajoitusten puitteissa. Hyvä agentti ei tee kaikkea, vaan tietää tehtävänsä ja rajansa.

### Väärinkäsitys 3: “Autonomisuus tarkoittaa, että agentti toimii ilman valvontaa.”

**Korjaava näkökulma:** Autonomisuus tarkoittaa, että agentti voi tehdä päätöksiä oman logiikkansa perusteella, mutta ihmisten määrittelemissä rajoissa. Erityisesti kriittisissä sovelluksissa valvonta, hyväksyntäportit ja turvakerrokset ovat välttämättömiä.

### Väärinkäsitys 4: “Agentti on sama kuin työnkulku.”

**Korjaava näkökulma:** Työnkulku seuraa yleensä ennalta määriteltyjä sääntöjä. Agentti voi tulkita tilannetta, käyttää muistia, valita työkaluja ja muuttaa toimintaansa palautteen perusteella. Agentti on joustavampi, mutta myös monimutkaisempi.

### Väärinkäsitys 5: “Agentin komponentit toimivat erikseen.”

**Korjaava näkökulma:** Komponentit muodostavat suoritusputken. Jos yksi osa puuttuu tai toimii heikosti, koko agentti heikkenee. Esimerkiksi ilman muistia agentti ei hyödynnä aiempia tapauksia, ja ilman turvakerrosta se voi tehdä vaarallisia päätöksiä.

### Väärinkäsitys 6: “Agentti pitää aina rakentaa itse.”

**Korjaava näkökulma:** Valmisagenteissa — esimerkiksi tekoälysovellusten agenttitiloissa — ovat samat kuusi rakennusosaa valmiiksi rakennettuina; joku muu on vain tehnyt suunnittelutyön. Kurssilla rakennetaan oma agentti, jotta valmiitakin osaa arvioida. Osta vai rakenna -valintaa käsitellään tunnilla 20.

### Väärinkäsitys 7: “ChatGPT tai muu tekoälychat on agentti.”

**Korjaava näkökulma:** Chat vastaa viesteihin, agentti suorittaa vaiheita työkaluilla omien oikeuksiensa rajoissa. Sama kielimalli voi olla kummankin sisällä — ero ei ole mallissa vaan harnessissa eli mallin ympärille rakennetuissa työkaluissa, muistissa, oikeuksissa ja turvarajoissa.

*Ajankohtaishuomio 7/2026, vanhenee:* mallien tasonimet eivät ole agenttituotteita. Esimerkiksi GPT-5.6-mallin lippulaivataso “Sol” ei ole agentti, vaan OpenAI:n agenttituote on ChatGPT Work. Jos opiskelija niputtaa nämä yhteen, erottele malli, mallin taso ja agenttituote.

---

## Luokkatehtävä — ohjeistus

### Tehtävä 1: Luokittelu

**Tavoite:** Opiskelijat harjoittelevat erottamaan **agentin**, **chatbotin**, **skriptin** ja **työnkulun** toisistaan.

Kun opiskelijat tekevät luokittelutehtävää, he saattavat ajatella liian nopeasti, että automaattinen järjestelmä on aina agentti. Ohjaa heitä kysymään tarkentavia kysymyksiä.

**Opettajan tarkistuskysymys:** Jos opiskelija sanoo “tämä on agentti, koska se on automaattinen”, kysy: “Tekeekö se päätöksiä itsenäisesti vai seuraako se vain sääntöjä? Käyttääkö se muistia? Onko sillä työkaluja? Onko siinä turvakerros?”

**Hyvä perustelu sisältää:**

- maininnan siitä, tekeekö järjestelmä itsenäisiä päätöksiä,
- kuvauksen siitä, käyttääkö järjestelmä työkaluja,
- pohdinnan siitä, onko järjestelmällä muistia tai palautetta,
- arvion siitä, onko järjestelmällä turvakerros tai rajoitukset.

### Tehtävä 2: Suoritusputken jäljittäminen

**Tavoite:** Opiskelijat tunnistavat agentin kuusi komponenttia konkreettisessa esimerkissä.

Käytä visuaalista kaaviota. Piirrä agentin komponentit silmukkana ja jäljitä, miten asiakaspalveluagentti käsittelee viestin.

| Komponentti | Asiakaspalveluagentin esimerkki |
| --- | --- |
| **Syötekäsittelijä** | Sähköposti tai chat-viesti saapuu ja siitä poimitaan tärkeät tiedot. |
| **Päättelijä** | Agentti analysoi asiakkaan ongelman, kiireellisyyden ja sopivan toimintatavan. |
| **Työkalut** | Agentti hakee tietoa tietokannasta, päivittää tiketin tai lähettää vastauksen. |
| **Muisti** | Agentti hyödyntää asiakkaan historiaa ja aiempia ratkaisuja. |
| **Turvakerros** | Agentti tarkistaa, ettei vastaus sisällä arkaluonteisia tietoja ja että toiminto on sallittu. |
| **Palautesilmukka** | Asiakkaan palaute ja ratkaisun onnistuminen parantavat seuraavaa käsittelyä. |

Kysy opiskelijoilta:

- Mikä komponentti olisi vaarallisin jättää pois?
- Mitä tapahtuu, jos agentilla ei ole muistia?
- Mitä tapahtuu, jos turvakerros puuttuu?
- Miten palautesilmukka voisi parantaa seuraavaa päätöstä?

### Tehtävä 3: Riskianalyysi

**Tavoite:** Opiskelijat ymmärtävät autonomisuuden riskit ja osaavat selittää, miksi agentille tarvitaan rajoja.

Keskustelkaa siitä, mitä tapahtuu, jos jokin agentin keskeinen komponentti epäonnistuu.

| Epäonnistuva osa | Mitä voi tapahtua? | Miten riskiä vähennetään? |
| --- | --- | --- |
| **Syötekäsittelijä** | Agentti ymmärtää asiakkaan viestin väärin ja valitsee väärän toimintatavan. | Syötteen validointi ja epäselvien viestien ohjaaminen ihmiselle. |
| **Muisti** | Agentti unohtaa aiemmat tapahtumat tai käyttää vanhentunutta tietoa. | Ajantasainen tietopohja, lokit ja muistin tarkistus. |
| **Turvakerros** | Agentti lähettää arkaluonteista tietoa tai tekee liian riskialttiin päätöksen. | Rajoitukset, hyväksyntäportit ja minimioikeusperiaate. |
| **Palautesilmukka** | Agentti ei opi virheistä tai oppii vääristä signaaleista. | Palautteen laadun tarkistus ja ihmisen ohjaama parantaminen. |

**Esimerkki opetukseen**

Käytä riskianalyysissä konkreettista tilannetta: asiakaspalveluagentti tulkitsee vihaisen reklamaation tavalliseksi laskukysymykseksi ja lähettää automaattisen rutiinivastauksen. Kysy, mikä komponentti epäonnistui ja miten tilanne olisi voitu estää.

---

## Arviointivihjeet

### Hyvä vastaus

“Tämä on agentti, koska se käsittelee syötteet syötekäsittelijällä, analysoi tilanteen päättelijällä, tekee päätöksiä ja käyttää työkaluja, hyödyntää muistia, noudattaa turvakerroksen rajoja ja parantaa toimintaansa palautesilmukan avulla. Nämä kuusi komponenttia muodostavat suoritusputken, joka erottaa agentin tavallisesta chatbotista.”

### Riittävä vastaus

“Tämä on agentti, koska se tekee päätöksiä rajatusti itsenäisesti, käyttää työkaluja ja hyödyntää aiempaa tietoa.”

### Heikko vastaus

“Tämä on agentti, koska se on tekoäly” tai “koska se on nopea.”

---

## Tuntiesityksen rakenne: 45 minuuttia

1. **Avaava keskustelu noin 5 minuuttia**

   Käytä esimerkkinä sähköpostin käsittelyä ja vertaa skriptiä, työnkulkua ja agenttia.
2. **Suoritusputken opetus noin 10 minuuttia**

   Piirrä kuuden komponentin sykli taululle ja käy läpi, miten komponentit toimivat yhdessä.
3. **Itsenäinen lukeminen noin 8 minuuttia**

   Opiskelijat lukevat aineiston ja merkitsevät kohdat, jotka auttavat erottamaan agentin chatbotista.
4. **Ryhmätehtävä: suoritusputken jäljitys noin 13 minuuttia**

   Opiskelijat tunnistavat järjestelmästä agentin komponentit ja selittävät, miten ne muodostavat prosessin.
5. **Valmisagentit ja harness noin 4 minuuttia**

   Kysy, kuka on nähnyt tekoälysovelluksen agenttitilan toiminnassa. Kiteytä kaksi asiaa: valmisagentissa ovat samat kuusi osaa, joku muu vain rakensi ne valmiiksi — ja agentti = kielimalli + harness.
6. **Yhteenveto ja riskianalyysi noin 5 minuuttia**

   Keskustelkaa autonomisuuden rajoista ja siitä, miksi turvakerros, muisti ja palautesilmukka ovat tärkeitä.

---

## Jatkoyhteys oppituntiin 20

Oppitunti 20 käsittelee sitä, **milloin agentti on oikea ratkaisu**. Tämä oppitunti luo pohjan jatkolle: opiskelijat ymmärtävät, mikä agentti on ja miten sen komponentit toimivat yhdessä suoritusputkessa. Seuraavaksi he oppivat arvioimaan, milloin agentin rakentaminen on hyödyllistä, milloin se on liian kallista ja milloin yksinkertaisempi ratkaisu riittää.

> **Pohdi seuraavaa tuntia varten:** Missä tilanteessa agentti olisi liian monimutkainen ratkaisu? Milloin tavallinen työnkulku tai chatbot riittäisi?

---
