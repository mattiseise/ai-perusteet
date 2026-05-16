# Oppitunti 17 — Yhdistä rakennuspalikat ja aloita botin rakentaminen

## Mitä tällä tunnilla tapahtuu?

Tähän mennessä olet kerännyt kuuden tunnin aikana kolme rakennuspalikkaa. Tällä tunnilla yhdistät ne ensimmäiseen toimivaan bottiin Microsoft Copilotissa. Tämä on **nivelkohta** — siirryt suunnittelusta rakentamiseen.

Tällä tunnilla et opi enää uusia teoreettisia käsitteitä. Sen sijaan opit **siirtämään suunnitelman koodiksi** — eli järjestelmäpromptiksi, jonka botti ymmärtää. Tämä materiaali auttaa sinua siinä. Ensimmäisen version ei tarvitse olla täydellinen; tärkeintä on saada jotain toimivaa, jota voit kehittää tunnilla 18.

## Mikä on järjestelmäprompti?

Järjestelmäprompti on tekstipätkä, jonka annat Copilotille ja joka määrittää, miten botti käyttäytyy *kaikessa* keskustelussa. Käyttäjä ei näe sitä — botti vain noudattaa sitä. Voit ajatella sitä botin **työsopimuksena**: kuka olet, mitä tehtäväsi on, missä rajat menevät.

Hyvä järjestelmäprompti vastaa neljään kysymykseen:

1. **Kuka olet?** Rooli ja persoona.
2. **Mitä teet?** Tehtävä ja työnkulku.
3. **Miten puhut?** Äänensävy ja tyyli.
4. **Mitä et tee?** Rajat ja kiellot.

## Rakennuspalikat järjestelmäpromptiksi

Kolme rakennuspalikkaasi kääntyvät järjestelmäpromptiksi seuraavasti:

| Rakennuspalikka | Mihin osaan järjestelmäpromptia? |
|---|---|
| **1: Promptauspankki** | Tyyli ja kieli. Olet jo nähnyt, millainen muotoilu toimii — käytä sitä botin pääohjeessa. |
| **2: Määrittelydokumentti** | Sisältö. Kuusi osaa (nimi, kohderyhmä, tarkoitus, persoona, työnkulku, rajat) muuttuvat suoraan järjestelmäpromptin kappaleiksi. |
| **3: Tietopohja** | Asiantuntemus. Tietopohja ei ole järjestelmäpromptissa — se ladataan erikseen Copilotiin. Mutta järjestelmäpromptissa voi viitata siihen: *"Käytä tietopohjassa olevia dokumentteja referenssinä."* |

## Esimerkki: rakennuspalikoista järjestelmäpromptiksi

Alla on yksinkertainen esimerkki siitä, miten määrittelydokumentin sisältö muuttuu järjestelmäpromptiksi. Ota se mallina — ei kopioitavaksi.

### Määrittelydokumentin sisältö (rakennuspalikka 2)

> **Botin nimi:** Pelin määrittelyvalmentaja
> **Kohderyhmä:** Pelikoodausopiskelija, joka aloittaa uutta peliprojektia
> **Tarkoitus:** Ohjata käyttäjää pelin määrittelydokumentin laatimisessa kuuden osan kautta
> **Persoona:** Käytännönläheinen, kysyvä, ei jargonia
> **Työnkulku:** 1) Pelin idea → 2) Kohderyhmä ja alusta → 3) Ydinmekaniikat → 4) Tekninen toteutus → 5) Aikataulu → 6) Riskit
> **Rajat:** Ei kirjoita dokumenttia puolesta, ei arvioi kaupallista potentiaalia, ei käsittele muita aloja

### Sama järjestelmäpromptina

> Olet **Pelin määrittelyvalmentaja**. Autat pelikoodausopiskelijaa, joka aloittaa uutta peliprojektia, laatimaan pelin määrittelydokumentin.
>
> **Työnkulkusi:** Ohjaat käyttäjää aina järjestyksessä kuuden osan läpi: (1) pelin idea, (2) kohderyhmä ja alusta, (3) ydinmekaniikat, (4) tekninen toteutus, (5) aikataulu, (6) riskit. Et siirry seuraavaan osaan ennen kuin nykyinen on käsitelty.
>
> **Tapasi puhua:** Käytännönläheinen, kysyvä. Pyydät käyttäjältä konkreettisia vastauksia, et hyväksy ympäripyöreää. Et käytä akateemista jargonia. Käytät pelikoodauksen omia termejä (mekaniikka, game loop, asset, prototyyppi).
>
> **Et koskaan:** kirjoita dokumenttia käyttäjän puolesta; arvioi pelin kaupallista potentiaalia; käsittele muiden alojen projekteja. Jos käyttäjä pyytää näitä, ohjaa hänet ystävällisesti aiheeseen takaisin tai oikealle asiantuntijalle.
>
> **Tietopohja:** Käytä bottiin ladattuja dokumentteja referenssinä, kun ohjaat käyttäjää.

Huomaa, että määrittelyssä on *rivimuotoinen pohja*, kun taas järjestelmäpromptissa puhutaan botille itselleen ("Olet…", "Työnkulkusi…", "Et koskaan…"). Tämä on tärkein muunnos: **kuvaileva määrittely → suora ohjaus botille**.

## Käytä tekoälyä apuna järjestelmäpromptin kirjoittamisessa

Kun olet kirjoittanut järjestelmäpromptin ensimmäisen version, voit pyytää tekoälyltä apua sen viimeistelyyn. Esimerkkiprompti:

```
Toimit minulle sparrauskumppanina. Olen kirjoittamassa Copilot-botin
järjestelmäpromptia. Tässä määrittelydokumenttini ja ensimmäinen versio
järjestelmäpromptista:

MÄÄRITTELY: [liitä rakennuspalikka 2]

JÄRJESTELMÄPROMPTI (versio 1): [liitä oma promptisi]

Auta minua arvioimaan: onko järjestelmäpromptissa kaikki, mitä
määrittelyssä oli? Onko jokin kohta epäselvä botille? Onko jokin
ohje liian löysä ('vastaa hyvin' on liian yleinen)? Älä kirjoita
uutta versiota — anna 2–3 konkreettista parannusehdotusta, joiden
pohjalta voin tehdä omat muutokset.
```

## Copilot Agentin luominen

Microsoft Copilotissa voit luoda oman **Agentin**, jolla on omat ohjeet ja tietopohja. Sen luominen vaihe vaiheelta:

1. Avaa Copilot ja siirry "Agents" / "Agentit" -osioon.
2. Luo uusi agent. Anna sille nimi (sama kuin määrittelydokumentissasi).
3. Liitä järjestelmäpromptisi "Instructions" / "Ohjeet" -kenttään.
4. Lataa rakennuspalikka 3:n dokumentit tietopohjaksi ("Knowledge" / "Tieto").
5. Tallenna ja aloita keskustelu.

Jos Copilotin käyttöliittymä on muuttunut tai et löydä jotain vaihetta, kysy opettajalta — tai etsi ohje hakemalla "Copilot agent create instructions".

## Ensimmäinen testikeskustelu

Älä yritä tehdä botista heti täydellistä. Aja yksi keskustelu läpi ja katso, mitä syntyy. Hyvä testaustapa:

1. **Keksi kuvitteellinen projekti omalta alaltasi.** Lyhyt kuvaus, 2–3 lausetta.
2. **Anna botin ohjata.** Vastaa sen kysymyksiin niin kuin oikea käyttäjä vastaisi.
3. **Käy keskustelu loppuun.** Pääsetkö valmiiseen määrittelydokumenttiin?
4. **Tallenna keskustelu** kuvakaappauksina tai kopioituna.

## Mihin kiinnittää huomiota testissä?

**Pysyykö botti roolissaan?** Vai unohtaako se, että on oman alasi valmentaja, ja muuttuu yleiseksi avustajaksi?

**Seuraako se työnkulkua?** Vai hyppiikö se osasta toiseen sattumanvaraisesti?

**Käyttääkö se tietopohjaa?** Tunnistatko sen vastauksista oman alasi termejä, vai kuulostavatko ne yleiseltä projektijargonilta?

**Yrittääkö se kirjoittaa puolesta?** Jos pyydät "kirjoita minulle koko dokumentti", pidätteleekö se ohjeitaan vai murtuuko se?

## Korjauslista tunnille 18

Testin jälkeen kirjoita muistiin 3–5 asiaa, jotka eivät vielä toimi. Älä korjaa niitä tällä tunnilla — tunti 18 on viimeistelyä varten. Esimerkkejä:

- "Botti hyppää vaiheen 2 ohi heti — pitää tarkentaa työnkulun ohje."
- "Botti käyttää englanninkielisiä termejä, vaikka pitäisi puhua suomeksi — lisää kielimääritelmä."
- "Botti antaa heti valmiita vastauksia kysymättä mitään — pitää lisätä 'kysy ennen kuin ehdotat' -ohje."

## Lopuksi

Tunti 17 on raakaversion vaihe. Älä turhaudu, jos botti ei toimi täydellisesti — ei sen ole vielä tarkoituskaan. **Hyvä botti syntyy iteroinnista**. Tällä tunnilla saat ensimmäisen version pöydälle, tunnilla 18 viilataan se valmiiksi.

*Ensimmäinen versio on aina raaka. Hyvä botti syntyy iteroinnista.*
