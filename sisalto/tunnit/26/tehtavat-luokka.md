# Opiskelutehtävät: Kasaa suunnitelma ja rakenna minimiversio

> Tämä on Agentit-osion lopputyön rakennustunti. Tänään kasaat viisi pohjapiirrostasi yhdeksi suunnitelmaksi, tutustut n8n:ään ja rakennat agenttisi ensimmäisen toimivan version.

*Tunnilla on kolme vaihetta. Kaikki kuuluvat lopputyöhön — tämä ei ole "valitse 1" -tunti.*

---

## Vaihe 1: Kasaa pohjapiirrokset suunnitelmaksi 🟢 PAKOLLINEN

**Miksi tämä on tärkeää:** Yksittäisinä pohjapiirrokset ovat irrallisia päätöksiä. Yhdessä ne muodostavat suunnitelman.

### Ohjeet

1. Avaa muistiinpanodokumenttisi (johon olet kerännyt pohjapiirroksesi).
2. Luo uusi tiedosto otsikolla "Agenttisuunnitelma — [agenttisi nimi]".
3. Kopioi viisi pohjapiirrostasi tiedostoon järjestyksessä 1–5.
4. Lue ne läpi yhtenä kokonaisuutena. *Onko tämä johdonmukainen agentti?*
5. Korjaa tarvittaessa.

### Tekoälyvaihe — sparraa kokoamista

```
Olen kirjoittanut viisi pohjapiirrosta agentistani, jonka aion
rakentaa n8n:ssä. Lue ne ja kysy minulta 3–5 kysymystä, jotka
paljastavat mahdolliset ristiriidat tai aukot. Älä korjaa
puolestani — kysy niin että minä huomaan ongelmat itse.
```

> 💡 **Vinkki muistiinpanoihin:** Tämä koottu suunnitelma on osa lopputyön palautusta.

---

## Vaihe 2: Tutustu n8n:ään 🟢 PAKOLLINEN

### Ohjeet

1. Avaa n8n.
2. Luo uusi työnkulku.
3. Lisää **Manual Trigger** -solmu.
4. Lisää **HTTP Request** -solmu. Menetelmä `GET`, osoite `https://api.github.com/zen`.
5. Yhdistä solmut viivalla.
6. Klikkaa "Execute workflow" ja katso, mitä HTTP Request palauttaa.
7. Lisää kolmas solmu (IF, Set tai Edit Fields). Kokeile.

---

## Vaihe 3: Rakenna agenttisi minimiversio 🟢 PAKOLLINEN

**Tärkeä rajaus:** Tunnin tavoite on **toimiva minimiversio** — ei valmis agentti. Turvakerros, IF-tarkistukset, human-in-the-loop ja viimeistelyt rakennat tunnilla 27.

### Ohjeet — iteratiivinen rakentaminen

1. **Triggeri.** Valitse: Manual Trigger, Schedule Trigger tai Webhook.
2. **Tekoälysolmu.** Lisää AI-solmu. Kirjoita system prompt pohjapiirrosten 2 ja 3 perusteella.
3. **Toimintasolmu.** Yksi solmu, joka toteuttaa agentin tehtävän.
4. **Testaa heti.** Anna esimerkkisyöte, klikkaa "Execute".
5. **Korjaa, jos ei toimi.** Tarkista yksi solmu kerrallaan.

### Tekoälyvaihe — sparraa system promptia

```
Olen kirjoittanut system promptin n8n-agentilleni. Tehtävä on
[kuvaa]. Tässä prompti: [liitä]. Kommentoi: onko rooli selkeä?
Onko rajat selkeät? Mitä epäselvyyksiä jää? Älä kirjoita
uudelleen — kysy minulta kysymyksiä.
```

> 💡 **Älä lisää tunnilla 26 vielä näitä:** turvakerros-IF-solmut, monimutkaiset haarat, muistiratkaisut, lokitus, useat hyväksyntäportit. Ne kuuluvat tunnille 27.

---

## Tunnin lopuksi

Kirjoita muistiinpanodokumenttiisi 3–4 lausetta:

- Mihin pääsin tunnilla?
- Mihin jäin?
- Mitä viimeistelen ensimmäisenä tunnilla 27?

Ota kuvakaappaus n8n-työnkulustasi nykyisessä tilassaan. Se on osa lopputyön palautusta.

---

**Lopputyön rakentaminen 1/2 — tunnilla 27 viimeistelet ja esittelet**
