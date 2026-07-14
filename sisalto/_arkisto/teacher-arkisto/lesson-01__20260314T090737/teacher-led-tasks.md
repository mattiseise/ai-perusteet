# Opettajavetoiset tehtävät

## Opettajavetoiset tehtävät: tapausanalyysit ja väärinkäsitysten purkaminen

### Tehtävä 1: Deterministisen vs. probabilistisen järjestelmän vertailu pienryhmissä

Jaa oppilaat 2–3 henkilön ryhmiin. Jokainen ryhmä saa yhden tapauksen:

1. **Tapaus A:** "Pankkisovellus hyväksyy tai hylkää lainahakemuksia automaattisesti säännön perusteella: 'Jos asiakkaan maksuhistoria on puhdas ja tulot ovat yhtä suuret kuin kuukausittain myönnettävien lainojen määrä, hyväksy.'"

2. **Tapaus B:** "Tekoälymalli analysoi asiakkaan profiilin (ikä, tulot, maksutietue) ja antaa todennäköisyyden sille, että asiakas maksaa lainansa takaisin (esim. 85 % varmuus)."

3. **Tapaus C:** "Neuroverkkomalli tunnistaa potilastiedoista riskitekijöitä sepelvaltimotaudille ja esittää riskiprosentin (esim. 72 %)."

Ryhmän tehtävä:
- Selvittää, mitä **deterministisiä** ja mitä **probabilistisia** elementtejä kunkin tapauksen järjestelmässä on.
- Kuvitella, mitä tapahtuu, jos järjestelmän ennuste **on väärä** (laina-asiakas ei maksa, potilas sairastuu odottamatta). Mitä **vastuukysymyksiä** syntyy? Kuka kantaa riskin?
- Ehdottaa **kontrollikeinoja** ja **inhimillisen vastuun rajaa** jokaiselle tapaukselle.

Ryhmät esittelevät löydöksensä plenarissa (5 min per ryhmä). Opettaja johtaa keskustelua seuraavilla tarkistuskysymyksillä:

- "Missä kohdassa ihmisen päätös on välttämätön, eikä sitä voida siirtää mallille?"
- "Miksi probabilistinen ennuste ei ole riittävä lainapäätökseen, mutta saattaa olla riittävä alustavaan asiakkaan segmentointiin?"
- "Mitä tapahtuu, jos ryhmät päätyvät siihen, että deterministinen sääntö on parempi? Missä tapauksessa se on toimiva valinta?"

**Odotettu ryhmätuotos:**
Jokainen ryhmä esittää 1–2 sivua analyysia (tai PowerPoint-diaesityksen), jossa on:
- Determinististen ja probabilististen osien tunnistaminen omassa tapauksessa
- Riskianalyysi (mitä voi mennä pieleen)
- Kontrollistrategia (mitkä mekanismit pitävät järjestelmän turvassa)
- Inhimillisen vastuun raja

**Solo-vaihtoehto:** Jos oppilas tekee tehtävän yksin, hän analysoi kaikki kolme tapausta (A, B, C) ja kirjoittaa niistä analyysin 600–800 sanalla. Sama rakenne: deterministisyys, riskit, kontrollimekanismit, ihmisen päätösvalta.

---

### Tehtävä 2: Väärinkäsitysten tunnistaminen plenarissa ja moderoitu debatti

Opettaja esittää seuraavat väitteet ja antaa oppilaille 3 min hiljaista ajattelua (ajattele itse), sitten 10 min pienryhmäkeskustelua:

1. *"Tekoäly on älykäs, koska se oppii kuten ihminen — datasta."*
2. *"Jos tekoäly tuottaa 95 prosentin tarkkuuden, voimme luottaa sen päätöksiin ilman inhimillistä valvontaa."*
3. *"Tekoäly voi olla yleisintelligenssi, kunhan sille annetaan tarpeeksi dataa."*
4. *"Tekoäly ymmärtää syy-seuraussuhteita, koska malli on opittu datasta, jossa nämä suhteet näkyvät."*

Kunkin väitteen jälkeen:
- Opettaja kysyy: "Mikä tässä väitteessä on väärää tai harhaanjohtavaa?"
- Oppilaat tuovat näkemyksensä esiin, ja opettaja rakentaa niiden pohjalta oikean tulkinnan
- Opettaja antaa konkreettisen esimerkin IT-ammatista, joka osoittaa, miksi väärinkäsitys on vaarallinen

**Odotettava oppilastuotos:** Oppilaat ottavat osaa keskusteluun ja pystyvät selittämään, miksi väite on väärä (esim. "95 % tarkkuus ei tarkoita sitä, etteivät seuraukset voisi olla vakavia viidessä prosentissa" tai "tekoäly näkee vain kuvioita, ei syiden ja seurausten yhteyksiä").