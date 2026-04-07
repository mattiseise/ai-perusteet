# Opiskelutehtävät: n8n-projektipaja, osa 1 — rakenna

## Agentit-osion arvioitava projekti (osa 1/2)

Oppitunneilla 26 ja 27 rakennat oman n8n-agenttityönkulun, testaat sen ja esittelet tuloksen. Tämä on Agentit-osion arvioitava projekti. Käytä kaikkia viittä projektin aihiota, jotka olet kerännyt oppitunneilla 19, 21, 23, 24 ja 25.

Projekti jakautuu kahteen osaan: oppitunnilla 26 rakennat työnkulun ja oppitunnilla 27 testaat, dokumentoit ja esittelet sen.

### Mitä rakennat?

Rakennat n8n-työnkulun, jossa on 3–5 solmua. Työnkulku toteuttaa ongelman, jonka valitsit projektin aihiossa 1. Käytössäsi on koulun palvelimen n8n-ympäristö, paikallinen Qwen-kielimalli ja M365-integraatiot (Outlook, Teams).

Työnkulun perusrakenne on: triggeri → tekoälyagentti (Qwen) → 1–2 työkalua → vastaus. Tämä rakenne voi vaihdella ongelmasi mukaan, mutta jokaisen työnkulun täytyy sisältää vähintään triggeri, tekoälysolmu ja yksi toimintasolmu.

### Miten käytät projektin aihioita?

Aihio 1 (oppitunti 19) kertoo, mitä ongelmaa ratkaiset ja kenelle. Aihio 2 (oppitunti 21) kertoo, miten agentti muistaa asioita. Aihio 3 (oppitunti 23) kertoo, miten agentti ajattelee. Aihio 4 (oppitunti 24) kertoo, miten agentti on turvallinen. Aihio 5 (oppitunti 25) kertoo, missä kohdissa ihminen päättää. Sinun ei tarvitse toteuttaa kaikkia aihioiden suunnitelmia — 3–5 solmun työnkulku on tarkoituksella yksinkertainen. Mutta aihiot ohjaavat suunnittelupäätöksiäsi.

---

## Tehtävä 26.1: Kokeile n8n:n perussolmut

### Tavoite
Tutustua n8n:n käyttöliittymään ja perussolmuihin ennen oman projektin rakentamista.

### Ohjeet

Avaa n8n ja rakenna yksinkertainen prototyyppityönkulku: luo uusi työnkulku, lisää Manual Trigger -solmu, lisää HTTP Request -solmu (GET-pyyntö osoitteeseen `https://api.github.com/zen`, joka palauttaa satunnaisen sitaatin) ja lisää kolmas solmu (esim. IF-ehto tai tekstinkäsittely), joka tekee jotain vastauksella. Testaa työnkulku.

Täytä havaintotaulukko:

| Solmu | Mitä se tekee | Miten se muuttaa dataa | Seuraavalle solmulle siirtyvä data |
|-------|---------------|------------------------|------------------------------------|
| Manual Trigger | | | |
| HTTP Request | | | |
| Kolmas solmu | | | |

Ota näyttökuva valmiista työnkulusta ja kirjoita 2–3 lausetta: "Mitä opin n8n:n solmujen toiminnasta?"

---

## Tehtävä 26.2: Rakenna oma agenttityönkulku

### Tavoite
Toteuttaa projektin aihioissa suunnittelemasi agentti n8n-työnkulkuna.

### Ohjeet

Rakenna oma n8n-työnkulku projektin aihioiden pohjalta. Aloita triggeristä (esim. webhook, ajastin tai manuaalinen käynnistys), lisää tekoälysolmu (AI Agent -solmu Qwen-mallilla) ja liitä siihen 1–2 työkalusolmua (esim. sähköpostin luku, tiedoston kirjoitus tai HTTP-pyyntö). Lisää tarvittaessa IF-solmu turvatarkistukseksi (projektin aihio 4).

Kirjoita system prompt tekoälysolmuun projektin aihioiden 2 ja 3 perusteella: kerro agentille sen rooli, arvot ja päättelytapa.

### Tuotos

Toimiva n8n-työnkulku (3–5 solmua), jossa on vähintään triggeri, tekoälysolmu ja yksi toimintasolmu. Näyttökuva työnkulusta ja lyhyt kuvaus siitä, mitä kukin solmu tekee.

---

## Tehtävä 26.3: Vertaisarviointi — arvioi toisen suunnitelma

### Tavoite
Löytää ongelmia ja parannusideoita toisen opiskelijan projektista ennen kuin rakentaminen on valmis.

### Ohjeet

Vaihda projektinsuunnitelma (projektin aihiot 1–5) toisen opiskelijan kanssa. Lue suunnitelma kriittisesti ja vastaa: Onko triggeri selkeä? Ovatko toiminta-askeleet realistisia 3–5 solmulle? Ovatko hyväksyntäportit oikeassa paikassa? Puuttuvatko turvakerrokset? Onko arkkitehtuuri toteutettavissa n8n:ssä?

Kirjoita palaute, jossa kuvaat vahvuudet, uhat ja heikkoudet sekä parannusehdotukset. Keskustele tekijän kanssa ja kirjoita muistiinpanot keskustelusta.

**Jos teet tehtävän yksin:** Arvioi oma suunnitelmasi kriittisesti samoilla kysymyksillä.
