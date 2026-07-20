# Opiskelutehtävät: Kasaa suunnitelma ja rakenna minimiversio

> Tämä on Agentit-osion lopputyön rakennustunti. Tänään kasaat viisi pohjapiirrostasi yhdeksi suunnitelmaksi, tutustut n8n:ään ja rakennat agenttisi ensimmäisen toimivan version.

*Tunnilla on kolme vaihetta. Kaikki kuuluvat lopputyöhön — tämä ei ole "valitse 1" -tunti.*

---

## Vaihe 1: Kasaa pohjapiirrokset suunnitelmaksi — pakollinen

**Miksi tämä on tärkeää:** Yksittäisinä pohjapiirrokset ovat irrallisia päätöksiä. Yhdessä ne muodostavat suunnitelman.

### Ohjeet

1. Avaa muistiinpanodokumenttisi (johon olet kerännyt pohjapiirroksesi).
2. Luo uusi tiedosto otsikolla "Agenttisuunnitelma — [agenttisi nimi]".
3. Kopioi viisi pohjapiirrostasi tiedostoon järjestyksessä 1–5.
4. Lue ne läpi yhtenä kokonaisuutena. *Onko tämä johdonmukainen agentti?*
5. Korjaa tarvittaessa.

### Tee ARCHITECTURE-luonnos

Tee samaan tiedostoon luonnos, jota päivität tunnilla 27. Kirjoita ensin yksi lyhyt kappale: **mitä kielimalli tekee ja mistä harness vastaa**. Kuvaa sen jälkeen 3–5 tärkeintä vaihetta:

| Vaihe | Tehtävä | Syöte → tulos | Vastuu: kielimalli vai harness |
| --- | --- | --- | --- |
| [Nimi] | [Mitä tapahtuu?] | [Mitä vaihe saa ja tuottaa?] | [Kumpi vastaa?] |

Tarkista lopuksi kuusi rakennusosaa: syötekäsittely, päättely, työkalut, muisti, turvakerros ja palaute. Merkitse jokaisesta **mukana**, **lisätään tunnilla 27** tai **ei tarvita tässä työssä**. Yksi vaihe, sääntö tai palvelu voi kattaa useita kohtia. Perustele lyhyesti mahdollinen poisjättö.

### Tekoälyvaihe — tarkista kokonaisuus

```
Olen kirjoittanut viisi pohjapiirrosta agentistani, jonka aion
rakentaa n8n:ssä. Lue ne ja kysy minulta 3–5 kysymystä, jotka
paljastavat mahdolliset ristiriidat tai aukot. Älä korjaa
puolestani — kysy niin että minä huomaan ongelmat itse.
```

> **Vinkki muistiinpanoihin:** Koottu suunnitelma ja ARCHITECTURE-luonnos ovat osa lopputyön palautusta. Tunnilla 27 et aloita dokumentointia tyhjästä, vaan päivität luonnoksen toteutuksen ja testien perusteella.

---

## Vaihe 2: Tutustu n8n:ään — pakollinen

### Ohjeet

1. Avaa n8n.
2. Luo uusi työnkulku.
3. Lisää **Manual Trigger** -solmu.
4. Lisää **HTTP Request** -solmu. Menetelmä `GET`, osoite `https://api.github.com/zen`.
5. Yhdistä solmut viivalla.
6. Klikkaa "Execute workflow" ja katso, mitä HTTP Request palauttaa.
7. Lisää kolmas solmu (IF, Set tai Edit Fields). Kokeile.

---

## Vaihe 3: Rakenna agenttisi minimiversio — pakollinen

**Tärkeä rajaus:** Tunnin tavoite on **toimiva minimiversio** — ei valmis agentti. Turvakerroksen, IF-tarkistukset, ihmisen hyväksyntää vaativat kohdat ja viimeistelyn rakennat tunnilla 27.

### Ohjeet — iteratiivinen rakentaminen

1. **Triggeri.** Valitse: Manual Trigger, Schedule Trigger tai Webhook.
2. **Tekoälysolmu.** Lisää tekoälysolmu. Kirjoita järjestelmäprompti pohjapiirrosten 2 ja 3 perusteella.
3. **Toimintasolmu.** Yksi solmu, joka toteuttaa agentin tehtävän.
4. **Testaa heti.** Anna esimerkkisyöte, klikkaa "Execute".
5. **Korjaa, jos ei toimi.** Tarkista yksi solmu kerrallaan.

### Tekoälyvaihe — tarkista järjestelmäprompti

```
Olen kirjoittanut järjestelmäpromptin n8n-agentilleni. Tehtävä on
[kuvaa]. Tässä prompti: [liitä]. Kommentoi: onko rooli selkeä?
Onko rajat selkeät? Mitä epäselvyyksiä jää? Älä kirjoita
uudelleen — kysy minulta kysymyksiä.
```

> **Älä lisää tunnilla 26 vielä näitä:** turvakerros-IF-solmut, monimutkaiset haarat, muistiratkaisut, lokitus, useat hyväksyntäportit. Ne kuuluvat tunnille 27.

---

## Tunnin lopuksi

Kirjoita muistiinpanodokumenttiisi 3–4 lausetta:

- Mihin pääsin tunnilla?
- Mihin jäin?
- Mitä viimeistelen ensimmäisenä tunnilla 27?

Ota kuvakaappaus n8n-työnkulustasi nykyisessä tilassaan. Se on osa lopputyön palautusta.

Päivitä vielä ARCHITECTURE-luonnoksen 3–5 vaiheriviä vastaamaan sitä, mitä todella rakensit. Merkitse keskeneräiset vastuut tunnin 27 tehtäviksi.

---

**Lopputyön rakentaminen 1/2 — tunnilla 27 viimeistelet ja esittelet**
