# Todistusaineisto 1 — Miten kone oikeasti tuottaa tekstiä

> 📌 **Tämä on ensimmäinen kolmesta todistusaineistosta**, jotka keräät Teoria-osion aikana. Käytät niitä arvioitavassa tehtävässä *"Tuomaripöydän päätös — asiantuntijalausunto tekoälystä"* (oppitunti 9). Säilytä tämä huolellisesti.

## Mitä teet?

Ajat kolme nopeaa kokeilua tekoälyllä, käytät tekoälyä apunasi havaintojen analysointiin ja kirjoitat lyhyen analyysin siitä, mitä koneen "kirjoittaminen" oikeasti on. Tämä todistusaineisto on pohja sille, kun tuomaripöydässä joudut selittämään, **miksi tekoäly voi olla varma ja silti väärässä**.

## Vaiheet

### Vaihe 1 — Seuraavan sanan arvaus

Anna ChatGPT:lle tai Claudelle pätkä:

> "Koodi on kirjoitettu Pythonissa. Seuraava askel on…"

Pyydä jatkamaan **vain yhdellä sanalla**. Toista sama kolme kertaa *uudessa keskustelussa*. Ota kuvakaappaukset tai kopioi vastaukset talteen.

### Vaihe 2 — Sama kysymys, eri vastaus

Kysy malli kahdesti samaa asiaa uudessa keskustelussa:

> "Anna kolme nimeä uudelle kahvilalle Helsingin keskustassa."

Vertaa vastauksia. Tallenna molemmat.

### Vaihe 3 — Vakuuttava vai oikea?

Kysy mallilta yksi tarkka kysymys, jonka vastauksen voit verifioida. Esimerkkejä:

- *"Kuka oli Suomen pääministeri vuonna 1987?"*
- *"Mikä on Pythonin `random.choice()` -funktion paluuarvo, kun lista on tyhjä?"*
- *"Kerro elokuvasta 'Sininen Vuori' (1987)."* (Tämä elokuva ei ole olemassa.)

Tarkista vastaus virallisesta lähteestä. Tallenna sekä mallin vastaus että oikea vastaus.

### Vaihe 4 — Käytä tekoälyä apuna analyysissä

Avaa uusi keskustelu ja anna tekoälylle **roolin sekä havaintosi**. Esimerkkiprompti:

```
Toimit minulle sparrauskumppanina. Olen opiskelija ja teen havaintoja
siitä, miten kielimalli tuottaa tekstiä. Tässä havaintoni:

[liitä vaiheiden 1–3 tulokset tähän]

Auta minua jäsentämään, mitä nämä havainnot kertovat seuraavista
käsitteistä: token, next-token prediction, epädeterminismi, lämpötila,
hallusinaatio. Älä kirjoita lopullista vastausta puolestani — esitä
kysymyksiä ja anna jäsennysehdotuksia, joiden pohjalta voin kirjoittaa
oman analyysini.
```

Tämä ei ole oikotie — se on harjoitus siitä, miten tekoälyä käytetään *työparina*, ei kirjoituspalveluna.

### Vaihe 5 — Kirjoita analyysisi (tämä on todistusaineistosi)

Kirjoita noin **300 sanaa omin sanoin**. Vastaa kolmeen kysymykseen:

1. **Miten kone kirjoittaa?** Selitä, mitä havaitsit vaiheissa 1–2: miksi sama pyyntö tuottaa eri vastauksen, ja mitä tämä kertoo siitä, miten malli oikeasti toimii. Käytä käsitteitä *token*, *next-token prediction* ja *lämpötila / epädeterminismi*.
2. **Mitä tarkoittaa, että malli "ennustaa, ei tiedä"?** Selitä vaiheen 3 perusteella: oliko vastaus oikein vai väärin, ja miltä se *kuulosti*. Mitä tämä kertoo luotettavuudesta?
3. **Mihin tuomaripöydässä?** Yhdellä lauseella: missä tilanteessa joku voisi joutua ongelmiin juuri näistä syistä?

::: luokka
## Mitä palautat?

**Et vielä mitään. Tarvitset tämän kuitenkin osan 1 arvoitavaa tehtävää varten.**
:::
::: verkko
## Mitä tallennat itsellesi?

**Et palauta tätä minnekään. Tallenna se silti huolellisesti — tarvitset tätä lopputyössä (osa 1 kolmesta todistusaineistosta).**
:::

Tästä pitäisi saada kuitenkin yksi tiedosto (Word, PDF tai Markdown), jossa on:

- Kuvakaappaukset tai kopiot kokeiluista (vaiheet 1–3)
- Analyysisi (vaihe 5, noin 300 sanaa)

> 💡 **Miksi tämä on tärkeää:** Tuomaripöydässä viittaat tähän todistusaineistoon suoraan, kun selität, *miksi* skenaariosi tekoäly tuotti väärän vastauksen. Et toista käsitteitä — sovellat niitä.

**1 / 3 todistusaineistoa kerätty**
