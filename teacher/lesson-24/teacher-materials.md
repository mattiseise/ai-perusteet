# Lesson 24: Opettajan materiaalit

## Oppimisen tavoitteet

Opiskelija osaa:
1. Tunnistaa eri työkalut, joita agentit käyttävät
2. Ymmärtää jokaisen työkalun riskit ja rajoitukset
3. Suunnitella turvallisuusrajoituksia (whitelist, permissions, sandbox)
4. Nähdä agentin orkestraattorina, ei yhtenä suurena neuroverkona
5. Arvioida, mitä oikeuksia agentti tarvitsee tietyssä sovelluksessa

## Yleisimmät väärinkäsitykset

1. **"Agentti on yksi suuri neuroverkko"** → Agentti on orkestraattori, joka kutsuu eri työkaluja

2. **"Mitä enemmän työkaluja, sitä parempi"** → Enemmän työkaluja = enemmän riskiä ja monimutkaisuutta

3. **"Turvallisuus on valinnainen"** → Turvallisuus on pakollista. Jokainen työkalu tarvitsee rajoitukset.

4. **"Whitelist vs. blacklist ei ole väliä"** → Whitelist on paljon turvallisempi (hyväksy vain tietyt komennot)

5. **"Sandbox on overkill"** → Sandbox on tärkeä, jos agentti ajaa ulkopuolista koodia

## Tarkistustehtävät / CFU

1. Mitä ovat agentin pää-työkalut ja mihin niitä käytetään?
2. Mitä riskejä tiedostojenjärjestelmällä on?
3. Mitä riskejä verkkohakulla on?
4. Mitä riskejä CLI:llä on?
5. Mikä on whitelist ja miksi se on parempi kuin blacklist?
6. Mitä on sandbox ja milloin sitä tarvitaan?
7. Miten agentti kutsuu työkaluja järjestyksessä?
8. Miksi agentin käyttöoikeudet pitäisi asettaa mahdollisimman pieniksi?

## Tyypilliset vaikeudet

1. **Orkestraattorin käsitys** — Opiskelijat ajattelevat agentin yhdeksi suureksi koodiksi.
   **Apua:** "Agentti ei osaa mitään itse. Se kutsuu työkaluja: 'Tiedostolukija, lue tämä!' → 'CLI, aja tämä!' → 'Haku, etsi tämä!'"

2. **Turvallisuusrajoitusten ymmärtäminen** — Opiskelijat voivat ajatella, että "jos agentille annetaan oikeudet, se osaa niitä käyttää oikein."
   **Apua:** "Agentti on logiikka, ei älykäs. Jos logiikka on virheellinen tai agentti on hakkeroitu, oikeudet voidaan väärinkäyttää."

3. **Whitelistin merkitys** — Opiskelijat eivät näe eroa whitelistin ja blacklistin välillä.
   **Apua:** "Blacklist: 'Älä ajaa rm, ne, etc.' → Uusia vaarallisia komentoja tulee. Whitelist: 'Aja vain ls, mkdir, cp' → Turvavallisuus."

4. **Resurssienkäyttö** — Opiskelijat eivät näe, että verkkohaku maksaa.
   **Apua:** "Jokainen verkkohaku maksaa 0.01€. Jos agentti hakee 1000 kertaa, maksaa 10€. Rajoita hakulaset."
