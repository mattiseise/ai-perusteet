# Oppitunti 17 — Yhdistä rakennuspalikat ja aloita botin rakentaminen

## Mitä tällä tunnilla tapahtuu?

Tähän mennessä olet kerännyt kuuden tunnin aikana kolme **rakennuspalikkaa**. Tällä tunnilla yhdistät ne ensimmäiseksi toimivaksi botiksi Microsoft Copilotissa. Tämä on **nivelkohta**: siirryt suunnittelusta rakentamiseen.

Tällä tunnilla et opiskele enää uusia teoreettisia käsitteitä. Sen sijaan opit **siirtämään suunnitelman järjestelmäkehotteeksi**, jonka botti ymmärtää. Tämä materiaali auttaa sinua siinä. Ensimmäisen version ei tarvitse olla täydellinen. Tärkeintä on saada aikaan jotakin toimivaa, jota voit kehittää tunnilla 18.

## Mikä on järjestelmäkehote?

**Järjestelmäkehote** on tekstipätkä, jonka annat Copilotille. Se määrittää, miten botti käyttäytyy *kaikissa* keskusteluissa. Käyttäjä ei yleensä näe järjestelmäkehotetta, mutta botti noudattaa sitä toiminnassaan.

Voit ajatella järjestelmäkehotetta botin **työsopimuksena**: kuka botti on, mikä sen tehtävä on ja missä sen rajat kulkevat.

Hyvä järjestelmäkehote vastaa neljään kysymykseen:

1. **Kuka olet?** Rooli ja persoona.
2. **Mitä teet?** Tehtävä ja työnkulku.
3. **Miten puhut?** Äänensävy ja tyyli.
4. **Mitä et tee?** Rajat ja kiellot.

## Rakennuspalikat järjestelmäkehotteeksi

Kolme rakennuspalikkaasi muuttuvat järjestelmäkehotteeksi seuraavasti:

| Rakennuspalikka | Mihin osaan järjestelmäkehotetta? |
| --- | --- |
| **1: Promptauspankki** | Tyyli ja kieli. Olet jo nähnyt, millainen muotoilu toimii. Käytä sitä botin pääohjeessa. |
| **2: Määrittelydokumentti** | Sisältö. Kuusi osaa eli nimi, kohderyhmä, tarkoitus, persoona, työnkulku ja rajat muuttuvat suoraan järjestelmäkehotteen kappaleiksi. |
| **3: Tietopohja** | Asiantuntemus. Tietopohja ei ole osa järjestelmäkehotetta, vaan se ladataan erikseen Copilotiin. Järjestelmäkehotteessa voit kuitenkin viitata siihen esimerkiksi näin: *"Käytä tietopohjaan ladattuja dokumentteja referenssinä."* |

## Esimerkki: rakennuspalikoista järjestelmäkehotteeksi

Alla on yksinkertainen esimerkki siitä, miten määrittelydokumentin sisältö muuttuu järjestelmäkehotteeksi. Ota se malliksi, mutta älä kopioi sitä sellaisenaan.

### Määrittelydokumentin sisältö eli rakennuspalikka 2

> **Botin nimi:** Tapahtuman suunnitteluvalmentaja
> **Kohderyhmä:** Opiskelija, joka alkaa suunnitella tapahtumaa
> **Tarkoitus:** Ohjata käyttäjää tapahtuman suunnitteludokumentin laatimisessa kuuden osan kautta
> **Persoona:** Käytännönläheinen, kysyvä, ei jargonia
> **Työnkulku:** 1) Tapahtuman idea → 2) Kohderyhmä ja paikka → 3) Ohjelma → 4) Budjetti ja hankinnat → 5) Aikataulu → 6) Riskit
> **Rajat:** Ei kirjoita dokumenttia käyttäjän puolesta, ei arvioi kaupallista potentiaalia, ei käsittele muiden alojen projekteja

### Sama järjestelmäkehotteena

> Olet **Tapahtuman suunnitteluvalmentaja**. Autat opiskelijaa, joka alkaa suunnitella tapahtumaa, laatimaan tapahtuman suunnitteludokumentin.
>
> **Työnkulkusi:** Ohjaat käyttäjää aina järjestyksessä kuuden osan läpi: (1) tapahtuman idea, (2) kohderyhmä ja paikka, (3) ohjelma, (4) budjetti ja hankinnat, (5) aikataulu ja (6) riskit. Et siirry seuraavaan osaan ennen kuin nykyinen osa on käsitelty.
>
> **Tapasi puhua:** Olet käytännönläheinen ja kysyvä. Pyydät käyttäjältä konkreettisia vastauksia etkä hyväksy ympäripyöreitä vastauksia sellaisenaan. Et käytä akateemista jargonia. Käytät tapahtumasuunnittelun omia termejä, kuten kohderyhmä, ohjelmarunko, budjetti ja aikataulu.
>
> **Et koskaan:** kirjoita dokumenttia käyttäjän puolesta, arvioi tapahtuman kaupallista potentiaalia tai käsittele muiden alojen projekteja. Jos käyttäjä pyytää näitä, ohjaa hänet ystävällisesti takaisin aiheeseen tai oikealle asiantuntijalle.
>
> **Tietopohja:** Käytä bottiin ladattuja dokumentteja referenssinä, kun ohjaat käyttäjää.

Huomaa, että määrittelydokumentissa sisältö on kuvailevassa muodossa, kun taas järjestelmäkehotteessa puhutaan botille suoraan: "Olet…", "Työnkulkusi…" ja "Et koskaan…". Tämä on tärkein muunnos: **kuvaileva määrittely muutetaan suoraksi ohjeeksi botille**.

## Käytä tekoälyä apuna järjestelmäkehotteen kirjoittamisessa

Kun olet kirjoittanut järjestelmäkehotteen ensimmäisen version, voit pyytää tekoälyltä apua sen viimeistelyyn. Käytä esimerkiksi seuraavaa promptia:

> "Toimi sparrauskumppaninani. Olen kirjoittamassa Copilot-botin järjestelmäkehotetta. Tässä ovat määrittelydokumenttini ja ensimmäinen versio järjestelmäkehotteesta:
>
> MÄÄRITTELY: [liitä rakennuspalikka 2]
>
> JÄRJESTELMÄKEHOTE, versio 1: [liitä oma kehotteesi]
>
> Auta minua arvioimaan: onko järjestelmäkehotteessa mukana kaikki, mitä määrittelyssä oli? Onko jokin kohta botille epäselvä? Onko jokin ohje liian yleinen, esimerkiksi 'vastaa hyvin'? Älä kirjoita uutta versiota. Anna 2–3 konkreettista parannusehdotusta, joiden pohjalta voin tehdä omat muutokseni."

## Copilot Agentin luominen

Microsoft Copilotissa voit luoda oman **agentin**, jolla on omat ohjeet ja tietopohja. Luo agentti näin:

1. Avaa Copilot ja siirry **Agents** / **Agentit** -osioon.
2. Luo uusi agentti. Anna sille sama nimi kuin määrittelydokumentissasi.
3. Liitä järjestelmäkehotteesi **Instructions** / **Ohjeet** -kenttään.
4. Lataa rakennuspalikka 3:n dokumentit tietopohjaksi kohtaan **Knowledge** / **Tieto**.
5. Tallenna agentti ja aloita keskustelu.

Jos Copilotin käyttöliittymä on muuttunut tai et löydä jotakin vaihetta, kysy opettajalta tai etsi ohje hakemalla esimerkiksi *"Copilot agent create instructions"*.

## Ensimmäinen testikeskustelu

Älä yritä tehdä botista heti täydellistä. Aja yksi keskustelu läpi ja katso, mitä tapahtuu. Hyvä testaustapa etenee näin:

1. **Keksi kuvitteellinen projekti omalta alaltasi.** Kirjoita siitä lyhyt kuvaus, 2–3 lausetta.
2. **Anna botin ohjata.** Vastaa sen kysymyksiin niin kuin oikea käyttäjä vastaisi.
3. **Käy keskustelu loppuun.** Tarkista, pääsetkö valmiiseen määrittelydokumenttiin.
4. **Tallenna keskustelu** kuvakaappauksina tai kopioituna tekstinä.

## Mihin kiinnität huomiota testissä?

**Pysyykö botti roolissaan?**

Vai unohtaako se, että se on oman alasi valmentaja, ja muuttuuko se yleiseksi avustajaksi?

**Seuraako botti työnkulkua?**

Vai hyppiikö se osasta toiseen sattumanvaraisesti?

**Käyttääkö botti tietopohjaa?**

Tunnistatko sen vastauksista oman alasi termejä, vai kuulostavatko vastaukset yleiseltä projektijargonilta?

**Yrittääkö botti kirjoittaa käyttäjän puolesta?**

Jos pyydät sitä kirjoittamaan koko dokumentin puolestasi, noudattaako se ohjeitaan vai murtuuko rajaus?

## Korjauslista tunnille 18

Testin jälkeen kirjoita muistiin 3–5 asiaa, jotka eivät vielä toimi. Älä korjaa kaikkea tällä tunnilla, sillä tunti 18 on viimeistelyä varten. Esimerkkejä:

- "Botti hyppää vaiheen 2 ohi heti — työnkulun ohjetta pitää tarkentaa."
- "Botti käyttää englanninkielisiä termejä, vaikka sen pitäisi puhua suomeksi — lisää kielimääritelmä."
- "Botti antaa heti valmiita vastauksia kysymättä mitään — lisää ohje 'kysy ennen kuin ehdotat'."

## Lopuksi

Tunti 17 on raakaversion vaihe. Älä turhaudu, jos botti ei vielä toimi täydellisesti. Sen ei ole tarkoituskaan olla valmis heti. **Hyvä botti syntyy iteroinnista**. Tällä tunnilla saat ensimmäisen version toimimaan, ja tunnilla 18 viimeistelet sen.

Ensimmäinen versio on aina raaka. Hyvä botti syntyy iteroinnista.

---
