# Opettajan materiaalit

## Oppitunnin tavoitteet (oppimistulokset)

Tämän oppitunnin jälkeen oppilas osaa:

1. **Selittää eron tekoälyn ja koneoppimisen välillä** ja tunnistaa, mitkä järjestelmät ovat mitäkin — ja miksi ero merkitsee ammatillisesti.

2. **Ymmärtää probabilistisen vs. deterministisen järjestelmän eron** ja tietää, mitkä tehtävät voidaan delegoida tekoälylle (joissa epävarmuus on hyväksyttävää) ja mitkä vaativat determinismiä tai inhimillistä kontrolleja (joissa virheet ovat kriittisiä).

3. **Tuntea tekoälyn kolme ratkaisevaa rajaa:**
   - Kapea-alaisuus (narrow scope) — tekoäly osaa vain sille opitun tehtävän
   - Kausaliteetin puuttuminen — tekoäly näkee kuvioita, ei syy-seuraus-suhteita
   - Arvopäätösten vastuuksi — tekoäly ei voi kantaa eettistä vastuuta, ihminen tekee arvopäätökset

4. **Analysoida ammattilaisesti konkretisia tapauksia:** Osaa paikantaa riskejä, kontrollikeinoja ja inhimillisen päätöksentekovalllan välttämättömiä rajoja IT-järjestelmissä, joissa tekoälyä käytetään.

---

## Yleisiä väärinkäsityksiä ja vastaukset

**Väärinkäsitys 1: "Tekoäly ja koneoppiminen ovat sama asia."**

Vastaus: Ei. Tekoäly on laajempi käsite — mikä tahansa järjestelmä, joka tekee älykkäitä päätöksiä ilman eksplisiittistä ohjelmointia. Koneoppiminen on **yksi tapa** rakentaa tekoälyä, jossa järjestelmä oppii datasta. Tekoäly voi olla myös sääntöpohjainen (eksplisiittiset säännöt, joita ihminen kirjoitti) tai pelistrategia. Tärkeä ero ammatillisesti: koneoppimismalli on probabilistinen (ei varmuutta), kun taas sääntöpohjainen tekoäly on tavallisesti deterministinen (samat syötöt → samat tulokset).

---

**Väärinkäsitys 2: "Jos tekoäly on 95% tarkka, se on tarpeeksi hyvä käyttöön."**

Vastaus: Konteksti ratkaisee. Jos mallilla on 95% tarkkuus tuhannesta ennusteesta, viisi prosenttia tarkoittaa 50 virheellista päätöstä. Joissain tapauksissa (esim. kuvasuositusten suodattomallit) 50 virhettä on siedettävä. Toisissa tapauksissa (esim. diagnoosisuositukset) 50 virhettä ihmisistä voi olla kriittinen. Ammattilaisena sinun on ymmärrettävä konteksti ja rakennettava järjestelmän ympärille kontrollit. Numeerinen tarkkuus ei ole sama asia kuin "riittävän turvallinen". Ja mikä tärkeintä: 95% tarkkuus ei tarkoita sitä, että saatat luottaa jokaisen yksittäisen ennusteen. Se kertoo vain, kuinka monta kertaa mallilla on oikea keskimäärin.

---

**Väärinkäsitys 3: "Tekoäly voi oppia ymmärtämään mitä tahansa, kunhan sille annetaan tarpeeksi dataa."**

Vastaus: Ei. Koneoppimismalli voi oppia tilastollisia kuvioita, mutta se ei voi oppia kausaliteettia (syy-seuraus). Jos datassa näkyy, että "A tapahtuu usein ennen B:tä", malli voi oppia ennustamaan B:n kun se näkee A:n. Mutta se ei ymmärrä, onko A todellinen syy B:lle vai vain sattumanvarainen korrelaatio. Klassinen esimerkki: jos data osoittaa, että "koneet, jotka tuottavat korkean desibelin äänen, rikkoutuvat usein", malli voi oppia tämän kuvion. Mutta se ei ymmärrä, onko ääni koneen rikkoutumisen **syy** vai pelkästään **merkki**, joka näkyy samalla kun ohjaajat käyttävät sitä väärällä tavalla (joka on todellinen syy rikkoutumiseen). Tämä virhe on vakava ammatillisesti: jos kontrollimekanismit perustuvat väärään syy-arvioon, ne eivät toimi.

---

**Väärinkäsitys 4: "Tekoäly ei voi tehdä virheitä, koska se on looginen."**

Vastaus: Probabilistinen tekoäly tekee virheitä usein. Se ei ole "looginen" siinä mielessä kuin deterministinen ohjelma (joka noudattaa matemaattisia logiikan sääntöjä). Probabilistinen tekoäly tekee **tilastollisia arvioita** ja valitsee seuraavaksi todennäköisimmän merkin. Jos järjestelmä on nähnyt datassa, että ihmiset, jotka kirjoittavat pieninä kirjaimin, eivät useinkaan osta premium-palveluja, se oppi tämän kuvion. Mutta se ei ymmärrä, että kirjainten koko ei ole causuaalinen tekijä vaan vain merkki jostakin muusta (esim. nuori käyttäjä, jolla on pienempi budjetti). Tämä on klassinen bias-riski: tekoäly oppii ja vahvistaa harhaisia korrelaatioita.

---

## Fasilitoinnin kärjet

**Ennen oppituntia:**
- Lue oppilaat valitsemat ammatilliset kontekstit (jos kokouspalvelusta tai henkilökohtaisista tehtävistä tiedetään). Jos et, anna ryhmille esimerkkejä samojen alasta (pankkitoiminta, terveydenhuolto, kuvantunnistus, chatbot-palvelu).
- Valmista 2–3 omaa tapausesimerkkiä, joista olet varma, että ne vahvistavat oppitunnin perusasiat.
- Kirjoita väärinkäsitykset etukäteen tai valitse ne näistä. Valmistaudu siihen, että oppilaat eivät välttämättä tunnista niitä heti.

**Oppitunnin aikana:**
- **Aloita konkreetista.** Älä aloita määritelmillä. Kerro esimerkki: "Pankkisovellus, joka laskee korkoa, on deterministinen — sama tilinumero tuottaa aina saman koron. Mutta tekoälyä käyttävä lainansaajien ennuste-malli on probabilistinen — se antaa 78% varmuuden, ei varmuutta."
- **Kysy paljon kysymyksiä.** Älä pidä vain luentoa. Keskeytä usein: "Mitä tämä tarkoittaa sinulle ammattilaisena?" "Missä tämä vaikuttaa?"
- **Nauti ryhmien tuottamista virheistä.** Jos ryhmä sanoo "95% tarkkuus on tarpeeksi", älä korjaa heti — kysy: "Mitä tarkoittaa se, että viisi prosenttia on väärässä? Millä tavalla se vaikuttaa riskeille, joita mainitsit?" Johdattele he oikean johtopäätöksen äärelle.
- **Pysy ammattilaisena tehtäväissä.** Älä liiku liian abstraktiksi. Kaikki esimerkit pitävät olla ammattilaisesta IT-kontekstista (pankit, terveydenhuolto, e-kauppa, tuotanto, jne.).

---

## Tarkistuskysymykset oppimisen vahvistamiseksi

Käytä näitä kysymyksiä oppitunnin aikana arvioidaksesi, ovatko oppilaat omaksuneet perusasiat:

1. **Deterministisyys ja probabilistisuus:**
   - "Mitä eroa on sillä, että ohjelma antaa aina saman tuloksen samalla syötteellä, ja sillä, että tekoäly antaa eri tuloksia joka kerta?"
   - "Kuka hyötyy tämän eron ymmärtämisestä ammattilaisesti?"

2. **Kapea-alaisuus:**
   - "Kuvatunnistusmallia, joka tunnistaa koirat, käytetään tekstin analysointiin. Mitä tapahtuu?"
   - "Miksi tekoäly on kapea-alaista, vaikka se näyttää yleiseltä?"

3. **Kausaliteetti:**
   - "Malli oppii, että 'ihmiset, joiden henkilötunnus on parillinen, ostavat usein härkiä.' Mitä tämä tarkoittaa? Ostaako henkilötunnus härkiä?"
   - "Miksi kausaliteetin puuttuminen on vaarallista ammattilaisille, jotka tekevät päätöksiä mallin perusteella?"

4. **Inhimillinen pääoikeus:**
   - "Tekoäly analysoi potilastietoja ja ehdottaa diagnoosia. Kuka tekee lopullisen päätöksen diagnoosin puolesta? Miksi?"
   - "Missä kohdassa ihmisen harkinnalle ei voi antaa korvikkeeksi mallin ennustusta?"

---

## Yleisiä vaikeuksia ja ratkaisuja

**Vaikeus 1: Oppilaat pitävät "tarkkuutta" (accuracy) samana kuin "luotettavuutta".**

Ratkaisu: Käytä konkreettinen esimerkki. "Malli on 99% tarkka diagnosoimaan särkyjä. Kymmenesta tuhannesta potilaasta siis noin 100 saa väärän diagnoosin. Kuinka monta näistä saatetaan vahingoittaa väärällä hoidolla? Onko 99% tarpeeksi?" Johdattele oppilaat siihen, että tarkkuus ja riittävä turvallisuus eivät ole sama asia — ja että konteksti ratkaisee.

---

**Vaikeus 2: Oppilaat sekoittavat "oppimisen" (mallin parametrien muuttuminen) ja "ymmärtämisen" (käsitteellisen merkityksen omaksuminen).**

Ratkaisu: Käytä vertausta. "Papukaija voi oppia toistamaan lauseita, joita kuulee. Kun sanot 'hyvää huomenta', se toistaa sen. Mutta papukaija ei ymmärrä, mitä 'hyvää huomenta' tarkoittaa. Tekoälykin oppii kuvioita datasta, mutta se ei ymmärrä merkitystä samoin kuin ihminen."

---

**Vaikeus 3: Oppilaat ajattelevat, että "jos tekoäly on koulutettava, sillä on oltava tietoisuus."**

Ratkaisu: Kielellä on väliä. Älä sano "malli oppii" tai "malli ajattelee". Sano "mallin parametrit muuttuvat dataan perustuen" tai "malli omaksuu kuvioita." Tämä on teknisesti tarkempaa ja estää oikeasta väärinkäsityksestä.

---

## Mahdolliset jatkokysymykset (jos aika sallii)

- "Mitä tapahtuu, jos ammattilaisella on virheellinen ymmärrys tekoälyn kyvyistä, ja hän rakentaa kriittisen järjestelmän sen varaan?"
- "Kuinka organisaatiot voivat suojautua siltä, että tekoälyyn perustuvia päätöksiä käytetään kriittisiin tapauksiin ilman inhimillisen valvonnan?"
- "Miksi eri alat (pankkitoiminta, terveydenhuolto, HR) vaativat eri vahvuuden sääntöjä tekoälyn käytölle?"
