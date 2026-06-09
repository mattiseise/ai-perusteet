# Sanasto – Lesson 26: n8n-projektipaja, osa 1

| Termi | Selitys |
| --- | --- |
| **n8n** (n-eight-n) | Avoimeen lähdekoodiin perustuva automaatioalusta, jossa rakennetaan visuaalisesti työnkulkuja vetämällä ja pudottamalla solmuja kankaalle. |
| **Solmu** (node) | Yksittäinen komponentti n8n-työnkulussa, joka tekee yhden konkreettisen tehtävän (esim. vastaanottaa viestin, kutsuu tekoälyä, lähettää sähköpostia). |
| **Työnkulku** (workflow) | Sarja solmuja, jotka on kytketty yhteen viivalla. Data virtaa solmusta toiseen automaattisesti työnkulun logiikan mukaisesti. |
| **Triggeri** (trigger) | Solmu, joka aloittaa työnkulun. Se voi olla ajastin (Schedule Trigger), webhook, käyttäjän painallama nappi (Manual Trigger) tai muu tapahtuma. |
| **Webhook** | URL-osoite, jonka kautta ulkoinen järjestelmä voi lähettää tietoja n8n-työnkululle. Esimerkiksi Discord-viesti tai Slack-ilmoitus käynnistää työnkulun webhoakin kautta. |
| **Validointi** (validation) | Prosessi, jossa n8n tarkistaa, että saapuva data on oikean muotoista ja turvallista käsitellä. Toteutetaan usein IF-solmuilla. |
| **IF-solmu** | Päätössolmu, joka tarkistaa ehtoa (esim. "onko viesti alle 500 merkkiä?") ja ohjaa datan eri haaraan (true/false). |
| **HTTP Request** | Solmu, joka lähettää pyynnön ulkoiselle API:lle (esim. tekoäly-palvelulle tai tietokannan rajapinnalle). Se saa vastauksen ja välittää sen eteenpäin. |
| **OpenAI-solmu** | Erityinen solmu, joka kommunikoi OpenAI:n palvelun kanssa (ChatGPT, tekoäly-päättely). Sisältää system promptin ja pyytää tekoälyä päättelemään. |
| **Google Sheets -solmu** | Solmu, joka lukee tai kirjoittaa tietoja Google Sheets -taulukkoihin. Usein käytetään muistin ja tietokannan toteuttamiseen. |
| **Discord-solmu** (tai Slack-solmu) | Solmu, joka lähettää viestejä Discord- tai Slack-kanavalle. Yhteydenpito käyttäjien kanssa. |
| **Arkkitehtuuri** (architecture) | Työnkulun rakenne ja layout: mistä se alkaa (trigger), mitä solmuja se sisältää, miten ne liittyvät yhteen ja missä järjestyksessä data kulkee. |
| **System prompt** | Teksti, joka määrittää tekoälyn käyttäytymisen. Esimerkiksi FAQ-botissa system prompt on: "Olet FAQ-botti, vastaa lyhyesti ja selkeästi." |
| **Konteksti** (context) | Taustatieto, jota agentti käyttää päätöksenteossa. Esimerkiksi FAQ-tietokanta on konteksti OpenAI-solmulle. |
| **Muisti** (memory) | Mekanismi, jolla agentti tallentaa ja muistaa aikaisempia tapahtumia. n8n:ssä se voi olla Google Sheets -taulukko tai Memory-solmu. |
| **Turvakerros** (safety layer) | Joukko validointi- ja IF-solmuja, jotka tarkistavat agentin vastaukset ennen lähettämistä. Suojaa käyttäjiä ja tietoja. |
| **Human-in-the-loop** | Rakenne, jossa kriittisissä tilanteissa ihminen hyväksyy agentin päätöksen ennen kuin se toteutetaan. |
| **Hyväksyntäportti** (approval gate) | Kohta työnkulussa, jossa ihminen ilmoitetaan ja häneltä pyydetään päätös ennen jatkamista. |
| **Integraatio** (integration) | Yhteys ulkoiseen palveluun (Discord, Slack, sähköposti, tekoäly-API). n8n:ssä on satoja valmiita integraatioita. |
| **Iteratiivinen kehitys** (iterative development) | Rakentamisen tapa, jossa rakennetaan ensin yksinkertainen versio, testataan, ja lisätään sitten uusia ominaisuuksia vaihe vaiheelta. |
| **Reunatapaukset** (edge cases) | Poikkeukselliset tilanteet, joita ei odoteta normaalisti mutta jotka voivat silti tapahtua (esim. tyhjä syöte, erittäin pitkä teksti, väärä kieli). |

---
