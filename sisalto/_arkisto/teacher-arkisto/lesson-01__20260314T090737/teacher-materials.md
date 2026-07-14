# Opettajan materiaalit

## Oppitunnin tavoitteet (oppimistulokset)

Tämän oppitunnin jälkeen oppilas osaa:

1. **Selittää eron tekoälyn ja koneoppimisen välillä** ja tunnistaa, mitkä järjestelmät ovat mitäkin — ja miksi ero merkitsee ammatillisesti.

2. **Ymmärtää probabilistisen ja deterministisen järjestelmän eron** ja tietää, mitkä tehtävät voidaan delegoida tekoälylle (joissa epävarmuus on hyväksyttävää) ja mitkä vaativat determinismiä tai inhimillistä kontrollia (joissa virheet ovat kriittisiä).

3. **Tuntea tekoälyn kolme ratkaisevaa rajaa:**
   - Kapea-alaisuus (narrow scope) — tekoäly osaa vain sille opetetun tehtävän
   - Kausaliteetin puuttuminen — tekoäly näkee kuvioita, ei syy-seuraussuhteita
   - Arvopäätösten vastuu — tekoäly ei voi kantaa eettistä vastuuta, ihminen tekee arvopäätökset

4. **Analysoida ammattilaisena konkreettisia tapauksia:** Osaa paikantaa riskejä, kontrollikeinoja ja inhimillisen päätöksentekovallan välttämättömiä rajoja IT-järjestelmissä, joissa tekoälyä käytetään.

---

## Yleisiä väärinkäsityksiä ja vastaukset

**Väärinkäsitys 1: "Tekoäly ja koneoppiminen ovat sama asia."**

Vastaus: Ei. Tekoäly on laajempi käsite — mikä tahansa järjestelmä, joka tekee älykkäitä päätöksiä ilman eksplisiittistä ohjelmointia. Koneoppiminen on **yksi tapa** rakentaa tekoälyä, jossa järjestelmä oppii datasta. Tekoäly voi olla myös sääntöpohjainen (eksplisiittiset säännöt, jotka ihminen on kirjoittanut) tai pelistrategia. Tärkeä ero ammatillisesti: koneoppimismalli on probabilistinen (ei varmuutta), kun taas sääntöpohjainen tekoäly on tavallisesti deterministinen (samat syötteet → samat tulokset).

---

**Väärinkäsitys 2: "Jos tekoäly on 95 % tarkka, se on tarpeeksi hyvä käyttöön."**

Vastaus: Konteksti ratkaisee. Jos mallilla on 95 % tarkkuus tuhannesta ennusteesta, viisi prosenttia tarkoittaa 50 virheellistä päätöstä. Joissain tapauksissa (esim. kuvasuositusten suodatinmallit) 50 virhettä on siedettävä. Toisissa tapauksissa (esim. diagnoosisuositukset) 50 virhettä ihmisistä voi olla kriittistä. Ammattilaisena sinun on ymmärrettävä konteksti ja rakennettava järjestelmän ympärille kontrollit. Numeerinen tarkkuus ei ole sama asia kuin "riittävän turvallinen". Ja mikä tärkeintä: 95 % tarkkuus ei tarkoita sitä, että voisit luottaa jokaiseen yksittäiseen ennusteeseen. Se kertoo vain, kuinka monta kertaa malli on keskimäärin oikeassa.

---

**Väärinkäsitys 3: "Tekoäly voi oppia ymmärtämään mitä tahansa, kunhan sille annetaan tarpeeksi dataa."**

Vastaus: Ei. Koneoppimismalli voi oppia tilastollisia kuvioita, mutta se ei voi oppia kausaliteettia (syy-seuraussuhteita). Jos datassa näkyy, että "A tapahtuu usein ennen B:tä", malli voi oppia ennustamaan B:n, kun se näkee A:n. Mutta se ei ymmärrä, onko A todellinen syy B:lle vai vain sattumanvarainen korrelaatio. Klassinen esimerkki: jos data osoittaa, että "koneet, jotka tuottavat korkean desibelin äänen, rikkoutuvat usein", malli voi oppia tämän kuvion. Mutta se ei ymmärrä, onko ääni koneen rikkoutumisen **syy** vai pelkästään **merkki**, joka näkyy samalla, kun ohjaajat käyttävät sitä väärällä tavalla (joka on todellinen syy rikkoutumiseen). Tämä virhe on vakava ammatillisesti: jos kontrollimekanismit perustuvat väärään syy-arvioon, ne eivät toimi.

---

**Väärinkäsitys 4: "Tekoäly ei voi tehdä virheitä, koska se on looginen."**

Vastaus: Probabilistinen tekoäly tekee virheitä usein. Se ei ole "looginen" siinä mielessä kuin deterministinen ohjelma, joka noudattaa matemaattisen logiikan sääntöjä. Probabilistinen tekoäly tekee **tilastollisia arvioita** ja valitsee seuraavaksi todennäköisimmän merkin. Jos järjestelmä on nähnyt datassa, että ihmiset, jotka kirjoittavat pienillä kirjaimilla, eivät useinkaan osta premium-palveluja, se oppii tämän kuvion. Mutta se ei ymmärrä, että kirjainten koko ei ole kausaalinen tekijä vaan vain merkki jostakin muusta (esim. nuori käyttäjä, jolla on pienempi budjetti). Tämä on klassinen bias-riski: tekoäly oppii ja vahvistaa harhaisia korrelaatioita.

---

## Fasilitoinnin kärjet

**Ennen oppituntia:**
- Lue oppilaiden valitsemat ammatilliset kontekstit (jos ne tiedetään kokouspalvelusta tai henkilökohtaisista tehtävistä). Jos et, anna ryhmille esimerkkejä samalta alalta (pankkitoiminta, terveydenhuolto, kuvantunnistus, chatbot-palvelu).
- Valmista 2–3 omaa tapausesimerkkiä, joista olet varma, että ne vahvistavat oppitunnin perusasiat.
- Kirjoita väärinkäsitykset etukäteen tai valitse ne näistä. Valmistaudu siihen, että oppilaat eivät välttämättä tunnista niitä heti.

**Oppitunnin aikana:**
- **Aloita konkreettisesta.** Älä aloita määritelmillä. Kerro esimerkki: "Pankkisovellus, joka laskee korkoa, on deterministinen — sama tilinumero tuottaa aina saman koron. Mutta tekoälyä käyttävä lainansaajien ennustemalli on probabilistinen — se antaa 78 % varmuuden, ei varmuutta."
- **Kysy paljon kysymyksiä.** Älä pidä vain luentoa. Keskeytä usein: "Mitä tämä tarkoittaa sinulle ammattilaisena?" "Missä tämä vaikuttaa?"
- **Hyödynnä ryhmien tuottamia virheitä.** Jos ryhmä sanoo "95 % tarkkuus on tarpeeksi", älä korjaa heti — kysy: "Mitä tarkoittaa se, että viisi prosenttia on väärässä? Millä tavalla se vaikuttaa riskeihin, joita mainitsit?" Johdattele heidät oikean johtopäätöksen äärelle.
- **Pysy ammatillisissa tehtävissä.** Älä liiku liian abstraktille tasolle. Kaikkien esimerkkien pitää olla ammatillisesta IT-kontekstista (pankit, terveydenhuolto, e-kauppa, tuotanto jne.).

---

## Tarkistuskysymykset oppimisen vahvistamiseksi

Käytä näitä kysymyksiä oppitunnin aikana arvioidaksesi, ovatko oppilaat omaksuneet perusasiat:

1. **Deterministisyys ja probabilistisuus:**
   - "Mitä eroa on sillä, että ohjelma antaa aina saman tuloksen samalla syötteellä, ja sillä, että tekoäly antaa eri tuloksia joka kerta?"
   - "Kuka hyötyy tämän eron ymmärtämisestä ammattilaisena?"

2. **Kapea-alaisuus:**
   - "Kuvatunnistusmallia, joka tunnistaa koirat, käytetään tekstin analysointiin. Mitä tapahtuu?"
   - "Miksi tekoäly on kapea-alaista, vaikka se näyttää yleiseltä?"

3. **Kausaliteetti:**
   - "Malli oppii, että 'ihmiset, joiden henkilötunnus on parillinen, ostavat usein härkiä.' Mitä tämä tarkoittaa? Ostaako henkilötunnus härkiä?"
   - "Miksi kausaliteetin puuttuminen on vaarallista ammattilaisille, jotka tekevät päätöksiä mallin perusteella?"

4. **Inhimillinen päätösvalta:**
   - "Tekoäly analysoi potilastietoja ja ehdottaa diagnoosia. Kuka tekee lopullisen päätöksen diagnoosista? Miksi?"
   - "Missä kohdassa ihmisen harkintaa ei voi korvata mallin ennusteella?"

---

## Yleisiä vaikeuksia ja ratkaisuja

**Vaikeus 1: Oppilaat pitävät "tarkkuutta" (accuracy) samana kuin "luotettavuutta".**

Ratkaisu: Käytä konkreettista esimerkkiä. "Malli on 99 % tarkka diagnosoimaan särkyjä. Kymmenestä tuhannesta potilaasta siis noin 100 saa väärän diagnoosin. Kuinka monta näistä saatetaan vahingoittaa väärällä hoidolla? Onko 99 % tarpeeksi?" Johdattele oppilaat siihen, että tarkkuus ja riittävä turvallisuus eivät ole sama asia — ja että konteksti ratkaisee.

---

**Vaikeus 2: Oppilaat sekoittavat "oppimisen" (mallin parametrien muuttuminen) ja "ymmärtämisen" (käsitteellisen merkityksen omaksuminen).**

Ratkaisu: Käytä vertausta. "Papukaija voi oppia toistamaan lauseita, joita se kuulee. Kun sanot 'hyvää huomenta', se toistaa sen. Mutta papukaija ei ymmärrä, mitä 'hyvää huomenta' tarkoittaa. Tekoälykin oppii kuvioita datasta, mutta se ei ymmärrä merkitystä samoin kuin ihminen."

---

**Vaikeus 3: Oppilaat ajattelevat, että "jos tekoäly on koulutettava, sillä on oltava tietoisuus."**

Ratkaisu: Kielellä on väliä. Älä sano "malli oppii" tai "malli ajattelee". Sano "mallin parametrit muuttuvat dataan perustuen" tai "malli omaksuu kuvioita". Tämä on teknisesti tarkempaa ja estää väärinkäsityksiä.

---

## Mahdolliset jatkokysymykset (jos aika sallii)

- "Mitä tapahtuu, jos ammattilaisella on virheellinen ymmärrys tekoälyn kyvyistä, ja hän rakentaa kriittisen järjestelmän sen varaan?"
- "Kuinka organisaatiot voivat suojautua siltä, että tekoälyyn perustuvia päätöksiä käytetään kriittisissä tapauksissa ilman inhimillistä valvontaa?"
- "Miksi eri alat (pankkitoiminta, terveydenhuolto, HR) vaativat eri vahvuisia sääntöjä tekoälyn käytölle?"