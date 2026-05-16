# Projektin määrittelydokumentin sparrauskumppani ★

## Mitä teet?

> **HUOM:** Tätä varten sinulla tulee olla kerättynä rakennuspalikat 1–3 (tunnit 12, 14 ja 15).

Rakennat **Microsoft Copilot Agent** -alustalle oman bottisi, joka auttaa **oman ammattialasi projektin määrittelydokumentin laatimisessa**. Et kirjoita dokumentteja botin puolesta — sinä rakennat *työkalun*, joka auttaa muita (tai sinua itseäsi) tekemään niitä paremmin, nopeammin ja johdonmukaisemmin.

Käytä tekoälyä apuna botin rakentamisessa. Tarkoitus ei ole, että keksit kaiken itse — vaan että **osaat ohjata tekoälyä auttamaan sinua suunnittelussa, testauksessa ja viimeistelyssä** ja teet lopulliset päätökset itse. Sinun vastuullasi on, että botti toimii ammattimaisesti, tuottaa oikeasti hyödyllisiä vastauksia ja että ymmärrät sen rakenteen kokonaan.

Valitset oman **ammattialasi** seuraavista:

- **IT-tuki** — esim. käyttöönottoprojekti, järjestelmämuutos, koulutusprojekti
- **Kyberturvallisuus** — esim. tietoturva-auditointi, palvelinkovetus, koulutus
- **Pelikoodaus** — esim. uusi peli, ominaisuus, prototyyppi
- **Web-ohjelmointi** — esim. asiakassivusto, API-palvelu, sovellus

Bottisi auttaa juuri sinun alasi ammattilaista **laatimaan projektin määrittelydokumentin** — sen, jota tarvitaan ennen kuin projekti alkaa. Dokumentin osat ovat lähes samat alasta riippumatta: tausta, tavoite, laajuus, vaatimukset, riskit, aikataulu — mutta termit, painotukset ja sisältö ovat erilaisia eri aloilla. Tämä on sinun bottisi erikoisosaamista.

## Miten teet sen?

Botin rakentamisessa on neljä vaihetta. Käytä niitä työvaiheina:

1. **Suunnitelma:** Päätä, kenelle botti on, mitä se osaa ja mitä se ei tee. Käytä pohjana tunnin 14 määrittelydokumenttiasi (rakennuspalikka 2).
2. **Järjestelmäprompti ja persoona:** Kirjoita botille ohjeet — kuka se on, miten se vastaa, missä järjestyksessä se ohjaa käyttäjää. Käytä pohjana tunnin 12 promptauspankkiasi (rakennuspalikka 1).
3. **Tietopohja:** Lataa bottiin 3–5 dokumenttia, jotka antavat sille tarvittavan asiantuntemuksen oman alasi projektidokumentaatiosta. Käytä pohjana tunnin 15 kuratoituja dokumenttejasi (rakennuspalikka 3).
4. **Testaus ja viimeistely:** Testaa bottia oikealla projektitilauksella. Korjaa ohjeita, lisää rajoitteita, päivitä tietopohjaa. Lopullinen botti vastaa selkeästi ja ammattimaisesti.

## Rakennuspalikat

Olet kerännyt kolme rakennuspalikkaa aiemmilla oppitunneilla. Käytä niitä botin pohjana:

- **Rakennuspalikka 1** (oppitunti 12, promptauspankki) antaa pohjan järjestelmäpromptille. Olet jo kirjoittanut ohjeita, jotka toimivat — käytä niiden rakennetta botin pääohjeessa.
- **Rakennuspalikka 2** (oppitunti 14, botin määrittelydokumentti) antaa pohjan suunnittelulle. Persoona, kohderyhmä, rajat, tavoitteet — kaikki valmiina.
- **Rakennuspalikka 3** (oppitunti 15, tietopohjan kuratointi) antaa pohjan tietopohjalle. Tiedät jo, millainen materiaali toimii ja mikä ei.

> 💡 **Vinkki:** *"Tässä on keräämäni rakennuspalikat, käytä niitä bottini ohjeen ja rakenteen pohjana… <liitä rakennuspalikkasi>"*

## Bottisi vaatimukset

Lopullisen botin tulee täyttää seuraavat kriteerit:

1. **Selkeä rooli ja kohderyhmä.** Botti tietää keneltä se saa kysymyksiä (oman alasi ammattilaiselta) ja mitä se tekee (auttaa määrittelydokumentin laatimisessa).
2. **Strukturoitu työnkulku.** Botti ohjaa käyttäjää määrittelydokumentin osa-alueiden läpi järjestelmällisesti (tausta → tavoite → laajuus → vaatimukset → riskit → aikataulu).
3. **Alasi termit ja näkökulmat.** Botti puhuu oman alasi kieltä — IT-tuelle eri termit kuin pelikoodaajalle. Tämä erottaa sinun bottisi yleisestä projektisuunnitteluapurista.
4. **Selkeät rajat.** Botti tietää mitä se EI tee — esimerkiksi se ei kirjoita koko dokumenttia puolesta, ei anna oikeudellisia neuvoja, ei toimi muilla aloilla. Rajat ovat osa ammattimaisuutta.
5. **Testattu oikealla esimerkillä.** Olet ajanut botin läpi vähintään yhden oikean projekti-idean kanssa ja korjannut puutteet, jotka testissä paljastuivat.

## Mitä palautat?

Palauta yksi tiedosto, joka sisältää:

1. **Suunnitelmasi** (tunti 14:n määrittelydokumentti, päivitettynä tähän bottiin)
2. **Bottisi järjestelmäprompti** kokonaisuudessaan kopioituna
3. **Lista tietopohjan dokumenteista** ja perustelu, miksi valitsit juuri nämä
4. **Testikeskustelu** botin kanssa: vähintään yksi täysi keskustelu, jossa botti ohjaa kuvitellun projektin määrittelydokumentin laatimisessa alusta loppuun (näytä kuvakaappauksina tai kopioituna)
5. **Reflektio** (200–300 sanaa): mitä opit botin rakentamisesta? Mikä toimi heti, mikä vaati monta yritystä? Mitä tekisit toisin, jos rakentaisit tämän uudelleen?

Lisäksi **linkki bottiisi** Copilotissa, jotta arvioija pääsee testaamaan sitä itse.

## Esittely (valinnainen)

Voit halutessasi pitää bottisi esittelyn ryhmälle. Esittelyssä:

- Kerro, kenelle botti on rakennettu ja mitä se ratkaisee
- Näytä yksi konkreettinen testikeskustelu
- Kerro yksi asia, jonka opit matkan varrella ja jota et osannut alussa

Esitys voi olla live ryhmän edessä, nauhoitettu video tai jaettu kuvakaappauskooste — valitse muoto, joka sopii sinulle.

## Jos et tiedä mistä aloittaa

Aloita näin:

1. Avaa **rakennuspalikka 2** (tunti 14, määrittelydokumentti). Päivitä se kuvaamaan tätä bottia — kohderyhmä on nyt oman alasi ammattilainen.
2. Kirjoita botin **järjestelmäpromptin ensimmäinen versio**. Pohjana **rakennuspalikka 1** (tunti 12, promptauspankki) — ota sieltä parhaiten toimivat rakenteet.
3. Lataa **rakennuspalikka 3** (tunti 15, kuratoitu tietopohja) bottiin. Jos tietopohja ei riitä, etsi 1–2 lisädokumenttia juuri oman alasi näkökulmasta.
4. Aja yksi testi: keksi kuvitteellinen projekti omasta alastasi ja katso, miten botti ohjaa sinua.
5. Korjaa, mikä ei toimi. Toista. Yhden iteraation jälkeen ei ole valmis — kahden tai kolmen jälkeen on.

*Et opettele käyttämään tekoälyä. Opit rakentamaan sillä.*
