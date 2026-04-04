# Opettajavetoiset tehtävät – Lesson 19

## Tehtävä 1: Järjestelmien luokittelu ryhmissä (25 min)

### Valmistelu

Jaa opiskelijat 3-4 hengen ryhmiin. Anna jokaiselle ryhmälle yksi näistä kuvauksista.

### Kuvaelmat

**Scenario A: Laskun käsittelyagentti**
Yritys vastaanottaa joka päivä satoja sähköpostilaskuja. Agentti lukee jokaisen laskun automaattisesti, tunnistaa laskuttajan, tarkistaa laskun summan yrityksen budjetin mukaisesti, ja jos kaikki on kunnossa, tallentaa laskun kirjanpitojärjestelmään. Jos jokin on pielessä (summaa ei tunneta tai laskuttaja ei ole luotettava), agentti käyttää ihmisen hyväksyttäväksi. Agentti myös seuraa, mitkä laskuttajat maksavat ajallaan, ja siihen perusteella antaa heille paremmat ehdot.

**Scenario B: Muistutus-chatbot**
Oppilaat voivat chatissa kysyä: "Milloin on seuraava tentti?" Chatbot etsii sen hetkisellä esityksellä olevan opetuskalenterin ja vastaa: "Englannin tentti on 15. maaliskuuta." Chatbot odottaa, että oppilas kysyy seuraavan kysymyksen.

**Scenario C: Palvelimen automaattinen kuormantasaus**
Palvelinfarmi seuraa jokaisen palvelimen kuormaa reaaliajassa. Kun jokin palvelin nousee 85 % kuormaan viisi minuuttia peräkkäin, järjestelmä automaattisesti käynnistää uuden palvelimen ja alkaa reitittää uusia pyyntöjä sille. Se myös ilmoittaa IT-tiimille sähköpostilla ja auttaa selvittämään, onko kyseessä normaali kuormituspäivä vai ongelma.

### Ohjeet ryhmälle

1. Lukekaa teidän saamanne kuvaelma.
2. Keskustelkaa: Onko tämä chatbot, agentti vai jotain muuta?
3. Löydät neljä tekijää:
   - Odottaako järjestelmä syötettä vai tekee se omia päätöksiä?
   - Tekee se useita vaiheita itsenäisesti?
   - Käyttääkö se palautesilmukkaa (oppia virheistään)?
   - Onko se reaktiivinen vai proaktiivinen?
4. Kirjoittakaa paperille:
   - Valintanne (Chatbot / Agentti / Muu)
   - Perustelut 3-4 lauseessa

### Käsittely (10 min)

Kunkin ryhmän edustaja esittelee ryhmänsä valintaa ja perustelut. Opettaja tarkastelee vastauksia ja korjaa mahdollisia väärinkäsityksiä.

**Oikeat vastaukset:**
- A: Agentti (autonominen päätöksenteko, palautesilmukka, oppiminen)
- B: Chatbot (passiivinen, odottaa syötettä, reaktiivinen)
- C: Agentti (autonominen järjestelmä, tekee päätöksiä, ilmoittaa ihmiselle)

---

## Tehtävä 2: Rakenteiden analyysi — Trigger, logiikka, toiminnot, palaute (20 min)

### Valmistelu

Valitse yksi esimerkki agenttista (esim. IT-tikettien automaattinen reitittäjä):

"Yrityksen IT-tukipyyntöjä hallitaan järjestelmällä, joka:
- Vastaanottaa asiakkaan tukipyynnöt (trigger)
- Analysoi pyynnön sisältöä ja kategorisoi ongelman (logiikka)
- Lähettää pyynnön oikealle asiantuntijalle, luo tiketin ja ilmoittaa asiakkaalle (toiminnot)
- Seuraa, kuinka kauan ratkaisu kestää ja tekee muistiinpanoja tulevilla kerroin käytettäväksi (palaute)"

### Ohjeet

Piirrä taululle neljän osan kaavio tai näytä powerpoint-dia. Käy ryhmän kanssa läpi:

1. **Trigger**: Mikä sai systeemin liikkeelle? → Asiakkaan tukipyyntö
2. **Logiikka**: Mitä agentti analysoi? → Pyynnön kategoriaa ja prioriteettia
3. **Toiminnot**: Mitä se tekee? → Lähettää tiketin, ilmoittaa asiakkaalle
4. **Palaute**: Miten se oppii? → Seuraa ratkaisu-aikoja, käyttää dataa jatkoon

### Kysymyksiä ryhmälle

- "Missä pisteessä ihminen ottaa haltuun?"
- "Mitä agentti ei voi tehdä ilman ihmisen valvontaa?"
- "Mitä kävisi, jos palautesilmukka ei toimisi?"

---

## Tehtävä 3: Vaara-analyysi — Liian autonominen agentti (15 min)

### Tilanne

Näytä opiskelijoille tämä skenario:

"Sähköpostin automaattinen vastaus-agentti saa komennon: 'Vastaa kaikille asiakkaille, jotka lähettävät sähköposteja, joissa on sana lasku.' Agentti toimii hyvin muutaman viikon ajan, mutta sitten asiakas lähettää sähköpostiin: 'Miksi laskun kanssa on näin vaikea saada vastinetta teidän tuesta?' Agentti tulkitsee tämän automaattisesti laskua sisältäväksi viestiksi ja lähettää asiakkaalle robottisen vastauksen, vaikka asiakas oli loukkaantunut ja tarvitsi ihmisen vastauksen."

### Keskustelu

- Mikä meni pieleen?
- Missä pisteessä olisi tarvinnut ihmisen valvonta?
- Mikä on agentin autonomisuuden raja?

**Johtopäätös:** Agentti on hyödyllinen, mutta sen täytyy tietää, milloin kutsua ihminen mukaan. Liian laaja autonomia johtaa virheisiin.

---

## Arviointi

Opettaja arvioi opiskelijoiden kyvyä:
- Erottaa agentti chatbotista konkreettisilla perusteluilla
- Tunnistaa agentin neljä rakennusosaa
- Nähdä autonomisuuden rajat ja ihmisen rooli
