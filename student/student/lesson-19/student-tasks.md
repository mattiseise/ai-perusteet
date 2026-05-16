# Opiskelutehtävät: Mikä agentti on — ja mitä se ei ole?

> Tämä tunti on Agentit-osion lopputyön ensimmäinen askel. Tänään kirjoitat **⭐️ Agentti: Ongelma** -pohjapiirroksen (1/5). Lopputyön kokonaisuus on osion alussa olevassa tehtävänannossa.

*Kaikkia ei tarvitse tehdä. Valitse tehtävistä 1. Suosittelen kuitenkin, että teet ainakin pohjapiirroksen — se on lopputyön osa.*

---

## ⭐️ Agentti: Ongelma 🟢 SUOSITELTU

**Miksi tämä on tärkeää:** Tunneilla 26–27 rakennat oman n8n-agentin. Tämä pohjapiirros on sen lähtökohta — kun sinulla on selkeä ongelma ja käyttäjä, kaikki myöhemmät suunnittelupäätökset (muisti, päättelymalli, turvakerros, ihmisen rooli) liittyvät konkreettiseen projektiin.

### Tehtävä

Valitse ongelma, jonka haluaisit ratkaista agentilla. Kirjoita lyhyt kuvaus (150–200 sanaa), jossa vastaat kolmeen kysymykseen:

1. Mikä ongelma on kyseessä ja kenelle se on tarkoitettu?
2. Miksi juuri agentti sopii tähän ongelmaan — eikö tavallinen automaatio tai chatbot riittäisi?
3. Mitkä kuusikomponenttisen mallin osat (syötekäsittelijä, päättelijä, työkalut, muisti, turvakerros, palautesilmukka) ovat tässä ongelmassa kriittisimpiä?

Ongelman ei tarvitse olla monimutkainen. Hyvä lähtökohta voi olla esimerkiksi "sähköpostiviestien luokittelu ja yhteenveto joka aamu" tai "asiakaspalvelun FAQ-botti, joka osaa hakea vastauksia tietokannasta". Tärkeintä on, että ongelman voi toteuttaa 3–5 solmun n8n-työnkulkuna.

### Tekoälyvaihe — sparraa ongelmavalintaa

Avaa ChatGPT, Claude tai Copilot ja käytä sitä sparrauskumppanina ongelmavalinnan haastamiseen. Älä pyydä tekoälyä keksimään ongelmaa puolestasi — pyydä sitä haastamaan oma ehdotuksesi.

```
Olen valinnut agentilleni seuraavan ongelman: [kuvaa]. Käyttäjä on
[kuvaa]. Toimi kriittisenä sparrauskumppanina ja kysy minulta 3–4
kysymystä, jotka paljastavat, onko tämä todella agenttiongelma vai
riittäisikö yksinkertaisempi ratkaisu. Älä vastaa puolestani — kysy
niin että minä ajattelen.
```

Vastaa kysymyksiin omassa pohjapiirroksessasi. Tekoäly ei tee päätöksiä — sinä päätät.

> 💡 **Vinkki muistiinpanoihin:** Tee oma muistiinpanodokumentti, johon kerää kaikki viisi ⭐️ Agentti -pohjapiirrosta omiksi alaotsikoikseen. Tunnilla 26 kasaat ne kaikki yhdeksi suunnitelmaksi.

---

## Tehtävä 19.1 — Luokittele järjestelmät 🟣 SYVENTÄVÄ

**Miksi tämä on hyödyllinen:** Tämä tehtävä harjoittaa täsmälleen sitä taitoa, jonka tarvitset pohjapiirroksesi perustelussa: mikä on agentti ja mikä ei.

### Tehtävä

Alla on kolme järjestelmän kuvausta. Tunnista jokaisen kohdalla, onko kyseessä **chatbot, agentti vai ei kumpikaan**, ja perustele valintasi käyttäen kuusikomponenttista mallia.

**Järjestelmä A: Asiakaspalvelun chatbotti.** Asiakkaat voivat kirjoittaa kysymyksiään verkkosivuston chat-ikkunaan. Järjestelmä analysoi kysymyksen ja etsii FAQ-tietokannasta sopivinta vastausta. Jos varmuusprosentti on korkea, se näyttää asiakkaalle vastauksen. Jos varmuusprosentti on matala, se ilmoittaa asiakkaalle, että ihmisen palvelutiimi ottaa yhteyttä.

**Järjestelmä B: Automaattinen palvelimen valvonta.** Palvelimen valvonta-agentti seuraa jatkuvasti palvelimen CPU-kuormaa, muistinkäyttöä ja verkkoliikennettä. Kun CPU-kuorma nousee yli 80 prosenttiin kahden minuutin ajan, agentti käynnistää automaattisesti uuden palvelininstanssin ja ohjaa liikennettä sille. Agentti lähettää myös ilmoituksen IT-tiimille ja dokumentoi tapahtumat. Seuraavan tunnin jälkeen, jos kuorma on laskenut normaaliksi, agentti sulkee ylimääräisen instanssin.

**Järjestelmä C: Kuvankäsittelyohjelma.** Kun käyttäjä lataa kuvan, ohjelma tunnistaa automaattisesti kuvan objektit ja lisää kuvailevat tagit metadataan. Ohjelma analysoi myös kuvan kirkkautta ja säätää sitä automaattisesti sopivammaksi. Ohjelma ei itse päätä, mitä kuvia käyttäjä haluaa käsitellä — se vain käsittelee jokaisen kuvan, joka sille annetaan, samalla logiikalla.

Täytä jokaisen järjestelmän kohdalle valintasi (chatbot, agentti tai ei kumpikaan) ja perustelu 2–3 lauseella. Käytä termejä *reaktiivinen, proaktiivinen, autonominen, tavoite* ja *päätöksenteko* sekä viittaa vähintään kahteen kuusikomponenttisen mallin osaan.

> 💡 **Vinkki muistiinpanoihin:** Kirjaa vastauksesi omiin muistiinpanoihisi. Tätä tehtävää ei palauteta, mutta sen havainnot tukevat pohjapiirroksen perustelua.

---

**Pohjapiirros 1/5 valmis — agenttisi ongelma on määritelty**
