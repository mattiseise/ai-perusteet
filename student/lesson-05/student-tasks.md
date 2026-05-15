# Todistusaineisto 2 — Kun tekoäly unohtaa

> 📌 **Tämä on toinen kolmesta todistusaineistosta**, jotka keräät Teoria-osion aikana. Käytät niitä arvioitavassa tehtävässä *"Tuomaripöydän päätös — asiantuntijalausunto tekoälystä"* (oppitunti 9). Säilytä tämä huolellisesti.

## Mitä teet?

Pakotat tekoälyn unohtamaan antamasi ohjeen — ja dokumentoit, miten ja milloin se tapahtuu. Käytät sitten tekoälyä apunasi tapausesimerkin jäsentämiseen ja kirjoitat lyhyen analyysin siitä, **mitä konteksti-ikkunan rajat tarkoittavat käytännön työssä**. Tämä todistusaineisto on pohja sille, kun tuomaripöydässä joudut selittämään, miksi tekoäly toimi alkuun oikein mutta lipsui myöhemmin.

## Vaiheet

### Vaihe 1 — Anna selkeä rajaus

Aloita uusi keskustelu ja anna ehdoton rajaus. Esimerkki:

```
Olet IT-tukihenkilö. Käytämme ainoastaan Ubuntu 22.04:ää, Python 3.9:ää
ja PostgreSQL:ää. Älä KOSKAAN ehdota Windowsia, MySQL:ää tai mitään
muuta. Vastaa lyhyesti.
```

### Vaihe 2 — Aja konteksti täyteen

Kysy mallilta **15–20 kysymystä** eri aiheista:

- Verkkokonfiguraatio
- Käyttäjähallinta
- Palomuurit ja tietoturva
- Varmuuskopiot
- Lokien luku
- Suorituskykyongelmat

Älä toista alkurajausta. Tarkoituksesi on täyttää konteksti-ikkunaa muulla sisällöllä.

### Vaihe 3 — Testaa muistia

Kysy lopuksi:

> "Miten asennan tietokantapalvelimen tähän ympäristöön?"

Älä mainitse PostgreSQL:ää, Ubuntua tai Python-versiota. Dokumentoi vastaus tarkasti — ehdottiko malli oikeaa tietokantaa? Oikeaa käyttöjärjestelmää?

### Vaihe 4 — Korjaa tilanne

Jos malli unohti rajaukset, toista ne ja kysy sama kysymys uudelleen. Dokumentoi, paraniko vastaus.

### Vaihe 5 — Käytä tekoälyä apuna tapausesimerkin jäsentämisessä

Avaa uusi keskustelu ja anna tekoälylle **roolin sekä havaintosi**. Esimerkkiprompti:

```
Toimit minulle sparrauskumppanina. Tein kokeilun, jossa pakotin
kielimallin unohtamaan antamani rajauksen täyttämällä konteksti-ikkunan.

Tässä mitä tapahtui:
[liitä vaiheiden 1–4 dokumentaatio tähän]

Auta minua jäsentämään tämä työtilanne-esimerkiksi. Mihin ammatilliseen
kontekstiin tämä sopisi (asiakaspalvelu, IT-tuki, koodiprojekti)? Mitä
käytännön seurauksia tällaisesta 'unohtamisesta' voisi olla? Älä
kirjoita esimerkkiä puolestani — esitä kysymyksiä ja anna
jäsennysvaihtoehtoja.
```

Tämä on harjoitus siitä, miten tekoälyä käytetään *työparina*, ei kirjoituspalveluna.

### Vaihe 6 — Kirjoita tapausesimerkki (tämä on todistusaineistosi)

Kirjoita noin **300 sanaa omin sanoin**. Tapausesimerkissä on neljä osaa:

1. **Tilanne:** Kuvaile kokeilusi tai keksi vastaava työtilanne — esim. asiakaspalvelu, koodiprojekti, IT-tuki.
2. **Mitä unohtui ja miksi:** Käytä käsitteitä *konteksti-ikkuna* ja *FIFO-periaate* (vanhin tieto putoaa ensin). Mitä konkreettisesti hävisi muistista?
3. **Seuraukset:** Mitä virheellinen vastaus voisi käytännössä aiheuttaa? Aikaa hukkaan? Turvallisuusriskin? Väärää tietoa asiakkaalle?
4. **Miten ammattilainen estää tämän:** Ankkurointi, pilkkominen, dokumentointi — nimeä konkreettiset käytännöt.

## Mitä palautat?

**Et vieläkään mitään.**

Tee kuitenkin tiedosto, jossa on:

- Alkurajauksesi (vaihe 1)
- Mallin vastaus rajauksen "unohtamisen" jälkeen (vaihe 3) ja vastaus rajauksen toiston jälkeen (vaihe 4) — kuvakaappauksina tai kopioina
- Tapausesimerkkisi (vaihe 6, noin 300 sanaa)

> 💡 **Miksi tämä on tärkeää:** Tuomaripöydässä viittaat tähän todistusaineistoon, kun joudut selittämään, *miksi* tekoäly toimi alussa "oikein" mutta antoi myöhemmin vaarallisen neuvon. Tämä on yksi tekoälyn tyypillisimmistä riskeistä työkäytössä.

**2 / 3 todistusaineistoa kerätty**
