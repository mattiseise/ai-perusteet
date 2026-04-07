# Opettajamateriaali – Lesson 22

## Oppitunnin ydinajatukset

Agentti näkee ja muistaa. Mutta voima tulee siitä, että se voi **tehdä todellisia asioita**. Kolme perustyökalua:
1. **Tiedostot**: lukea ja kirjoittaa tietoa
2. **Verkkohaku**: noutaa ajankohtaista tietoa
3. **CLI**: ajaa palvelinkomentoja

---

## Tiedostotyökalu — turvallisuus

**Lukuoikeus**: Anna pääsy vain välttämättömiin tiedostoihin
**Kirjoitusoikeus**: Rajoita erityisiin kansioihin (esim. /reports/)
**Poistooikeus**: Älä anna, ellei kriittinen

Esimerkki:
- Lukea: /data/, /customer_info/
- Kirjoittaa: /reports/, /temp/
- Ei poistooikeutta mihinkään

---

## Verkkohakutyökalu — kolme riskiä

1. **Väärä tieto**: Whitelist lähteistä (vain Wikipedia, hallitus, ei satunnaisia blogeja)
2. **Kustannukset**: Rajoita kuinka monta hakua per päivä
3. **Yksityisyys**: Älä hae henkilötietoja tai salasia

---

## CLI-työkalu — vaarallisempi kuin muut

**Whitelist-malli**: 
- Hyväksi: `ls`, `mkdir`, `cp`
- Kielletty: `rm`, `rm -rf`, `sudo`, `shutdown`

**Hiekkalaatikko**: Ajaa komennot erillään oikeasta järjestelmästä

**Hyväksynnät**: Kriittiset komennot vaativat ihmisen hyväksynnän

---

## Orkestrointi — järjestys

Agentti kutsuu työkaluja **järjestyksessä**:
1. Tiedostot: lue perustiedot
2. Verkkohaku: hae konteksti
3. CLI: tee analyysi
4. Tiedostot: kirjoita raportti

Väärä järjestys = virhe. Oikea järjestys = toimii.

---

## Neljä kerrosta turvallisuudelle

1. **Validointi**: Tarkista syöte ennen agentin käyttöä
2. **Rajoitus**: Anna vain minimaalinen pääsy (whitelist)
3. **Seuranta**: Jokainen operaatio loggiin
4. **Palautuminen**: Osaa kumota tai korjata virheitä

---

## Harjoitukset

1. **Whitelist**: Opiskelijat suunnittelevat whitelist:in eri agenteille
2. **Orkestrointi**: Opiskelijat piirrävät työnkulkukaavion
3. **Riskit**: Opiskelijat kuvailevat, mitä menee pieleen
4. **Oikea työkalu**: Opiskelijat valitsevat työkalut tehtävän mukaan

---

## Yhteiset virheet

1. "Isompi whitelist = parempi" → Ei, rajoitus tekee turvallisemmaksi
2. "Verkkohaku on turvallista" → Ei, väärä tieto on riski
3. "CLI on tehokas, käytetään paljon" → Varo, vaarallisempi
4. "Orkestrointi ei ole tärkeä" → Väärä järjestys = virhe

---

## n8n-tutustumisharjoitus — opettajan ohje

### Tavoite
Opiskelijat näkevät ensimmäistä kertaa, miltä tekoälyagentti näyttää n8n:ssä. He eivät rakenna mitään — he tunnistavat osat ja jäljittävät tiedon kulun.

### Valmistelu
1. Jaa opiskelijoille tiedosto `esimerkki-agentti.json` (löytyy kurssin materiaalikansiosta)
2. Varmista, että opiskelijoilla on pääsy n8n:ään (joko paikallinen tai pilvipalvelu)
3. Varaa 15–20 minuuttia harjoitukseen

### Odotetut vastaukset

| Solmu | Agentin osa | Selitys |
|---|---|---|
| Chat Trigger | Syötekäsittelijä | Ottaa vastaan käyttäjän viestin |
| AI Agent | Päättelijä | Päättää mitä tehdä viestin perusteella |
| Calculator | Työkalu | Tekee laskutoimituksia agentin puolesta |
| HTTP Request | Työkalu | Hakee tietoa verkosta |
| Respond to Chat | Tulosteen muotoilija | Lähettää vastauksen käyttäjälle |

### Jos opiskelija ei tunnista osia
Ohjaa: "Katso solmun nimeä ja ikonia. 'Chat Trigger' — mikä laukaisee keskustelun? 'AI Agent' — kuka tekee päätöksiä?"

### Yhteys teoriaan
Tämä harjoitus silloittaa oppituntien 19–22 teorian konkreettiseen n8n-käyttöliittymään. Opiskelijat palaavat tähän kokemukseen oppitunnilla 26, kun he rakentavat oman agentin.
