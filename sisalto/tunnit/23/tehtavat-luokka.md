# Opiskelutehtävät: Suunnittelumallit — ReAct ja ketjuajattelu

> Tämä tunti rakentaa lopputyösi kolmatta osaa. Tänään päätät, miten agenttisi ajattelee. Tuotos: **⭐️ Agentti: Päättely** (3/5).

*Kaikkia ei tarvitse tehdä. Valitse tehtävistä 1. Suosittelen kuitenkin ⭐️ Agentti: Päättely -tehtävää.*

---

## ⭐️ Agentti: Päättely 🟢 SUOSITELTU

**Miksi tämä on tärkeää:** Päättelymalli määrittää, miten agenttisi ajattelee. Väärä valinta johtaa joko turhiin iteraatioihin tai liian jäykkään prosessiin.

### Tehtävä

Avaa muistiinpanoistasi aiemmat ⭐️ Agentti -pohjapiirroksesi. Kirjoita 150–200 sanaa, jaettuna kolmeen osaan:

**1. Päättelymalli (ReAct vai ketjuajattelu).** Kumpi malli sopii paremmin omaan ongelmaasi? **ReAct** (ajattele → toimi → havainnoi → ajattele uudelleen) sopii, kun agentti tarvitsee reagoida työkalujen palautteeseen. **Ketjuajattelu** (vaihe 1 → vaihe 2 → vaihe 3) sopii, kun prosessi on selkeästi peräkkäinen.

**2. Perustelu.** Miksi tämä malli sopii juuri sinun käyttötapaukseesi?

**3. Päättelymalli n8n-rakenteena.** Miten päättelymallisi näkyy konkreettisesti n8n-työnkulussa? ReActissa tarvitset usein silmukan tekoälysolmun ja työkalujen välillä. Ketjuajattelussa työnkulku on lineaarisempi.

> **Sivumaininta: moniagenttijärjestelmät.** Monimutkaisissa, oikean elämän projekteissa agentit voivat tehdä yhteistyötä — yksi erikoistuu tiedonhakuun, toinen kirjoittaa, kolmas tarkistaa lopputuloksen. Tätä kutsutaan moniagenttijärjestelmäksi. Lopputyösi mittakaavassa (3–5 solmua) tämä on yliampuva ratkaisu. Yksi hyvin suunniteltu agentti riittää.

### Tekoälyvaihe — sparraa päättelyvalintaa

```
Olen valinnut agentilleni [ReAct / ketjuajattelu] -mallin. Agenttini
tehtävä on [kuvaa]. Perusteluni on [kuvaa]. Toimi sparrauskumppanina
ja kysy 2–3 kysymystä, jotka paljastavat, onko valintani perusteltu
vai sopisiko toinen malli paremmin.
```

> 💡 **Vinkki muistiinpanoihin:** Tämä on 3/5 lopputyösi osista.

---

## Tehtävä 23.1 — ReAct vs. ketjuajattelu — milloin käytät mitä? 🟣 SYVENTÄVÄ

### Tehtävä

Neljä tehtävää. Päätä jokaisen kohdalla, sopiiko ReAct vai ketjuajattelu paremmin:

- **A:** "Asiakkaan tili on jäädytetty. Avaa se."
- **B:** "Asiakas ei ole varma, mitä tuotetta hän haluaa. Auta valitsemaan."
- **C:** "Tilaus on epätavallinen (negatiivinen hinta). Tarkista."
- **D:** "Asiakkaalle tulee joka kuukausi tilaukseen ongelma. Ratkaise juurisyy."

Jokaisesta tehtävästä: päättelymalli, perustelu 1–2 lauseella, arvio kuinka monta vaihetta/iteraatiota.

> 💡 **Vinkki muistiinpanoihin:** Jos analyysi muuttaa käsitystäsi oman agenttisi sopivasta mallista, päivitä ⭐️ Agentti: Päättely.

---

**⭐️ Agentti: Päättely valmis — 3/5 lopputyöstä koossa**
