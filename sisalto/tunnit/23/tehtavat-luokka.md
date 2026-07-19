# Opiskelutehtävät: Suunnittelumallit — ReAct ja eksplisiittinen työnkulku

> Tämä tunti rakentaa lopputyösi kolmatta osaa. Tänään päätät, miten agenttisi havaittava työnkulku etenee. Tuotos: **Agentti: Päättely** (3/5).

*Kaikkia ei tarvitse tehdä. Valitse tehtävistä 1. Suosittelen kuitenkin Agentti: Päättely -tehtävää.*

---

## Agentti: Päättely — suositeltu

**Miksi tämä on tärkeää:** Suunnittelumalli määrittää, miten agenttisi valitsee työkalut, käsittelee tulokset ja etenee toiminnosta toiseen. Väärä valinta johtaa joko turhiin iteraatioihin tai liian jäykkään prosessiin.

### Tehtävä

Avaa muistiinpanoistasi aiemmat Agentti-pohjapiirroksesi. Kirjoita 150–200 sanaa, jaettuna kolmeen osaan:

**1. Suunnittelumalli (ReAct vai eksplisiittinen työnkulku).** Kumpi malli sopii paremmin omaan ongelmaasi? **ReAct** (työkalukutsu → tulos tai virhe → seuraava toiminto) sopii, kun agentin pitää reagoida työkalujen palautteeseen. **Eksplisiittinen työnkulku** (vaihe 1 → vaihe 2 → vaihe 3) sopii, kun prosessi on selkeästi peräkkäinen.

**2. Perustelu.** Miksi tämä malli sopii juuri sinun käyttötapaukseesi?

**3. Malli n8n-rakenteena ja lokina.** Miten malli näkyy konkreettisesti työnkulussa? Kirjaa esimerkki, jossa näkyvät lyhyt päätösperustelu, rakenteinen työkalukutsu, tulos tai virhe ja seuraava toiminto. Älä pyydä tai tallenna mallin raakaa chain-of-thoughtia. ReActissa tarvitset usein rajatun silmukan tekoälysolmun ja työkalujen välillä. Eksplisiittisessä työnkulussa rakenne on lineaarisempi.

> **Sivumaininta: moniagenttijärjestelmät.** Monimutkaisissa, oikean elämän projekteissa agentit voivat tehdä yhteistyötä — yksi erikoistuu tiedonhakuun, toinen kirjoittaa, kolmas tarkistaa lopputuloksen. Tätä kutsutaan moniagenttijärjestelmäksi. Lopputyösi mittakaavassa (3–5 solmua) tämä on yliampuva ratkaisu. Yksi hyvin suunniteltu agentti riittää.

### Tekoälyvaihe — arvioi päättelyvalinta

```
Olen valinnut agentilleni [ReAct / eksplisiittinen työnkulku] -mallin. Agenttini
tehtävä on [kuvaa]. Perusteluni on [kuvaa]. Toimi sparrauskumppanina
ja kysy 2–3 kysymystä, jotka paljastavat, onko valintani perusteltu
vai sopisiko toinen malli paremmin.
```

> **Vinkki muistiinpanoihin:** Tämä on 3/5 lopputyösi osista.

---

## Tehtävä 23.1 — ReAct vs. eksplisiittinen työnkulku — milloin käytät mitä? — syventävä

### Tehtävä

Neljä tehtävää. Päätä jokaisen kohdalla, sopiiko ReAct vai eksplisiittinen työnkulku paremmin:

- **A:** "Asiakkaan tili on jäädytetty. Avaa se."
- **B:** "Asiakas ei ole varma, mitä tuotetta hän haluaa. Auta valitsemaan."
- **C:** "Tilaus on epätavallinen (negatiivinen hinta). Tarkista."
- **D:** "Asiakkaalle tulee joka kuukausi tilaukseen ongelma. Ratkaise juurisyy."

Jokaisesta tehtävästä: päättelymalli, perustelu 1–2 lauseella, arvio kuinka monta vaihetta/iteraatiota.

> **Vinkki muistiinpanoihin:** Jos analyysi muuttaa käsitystäsi oman agenttisi sopivasta mallista, päivitä Agentti: Päättely.

---

**Agentti: Päättely valmis — 3/5 lopputyöstä koossa**
