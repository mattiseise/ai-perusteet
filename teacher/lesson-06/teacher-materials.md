# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

1. Opiskelijat ymmärtävät, mitä multimodaalisuus on — tekoälyn kyky käsitellä erilaisia tietomuotoja (tekstiä, kuvia, lokkeja, koodia).

2. Opiskelijat näkevät käytännössä, kuinka kuvakaappaukset parantavat kontekstia IT-ongelmissa.

3. Opiskelijat oppivat rakentamaan tehokkaan multimodaalisen kontekstin — milloin käyttää tekstiä, milloin kuvakaappauksia, milloin molempia.

4. Opiskelijat ymmärtävät multimodaalisten mallien rajoitukset (token-kustannukset, lukemattomuuden riskit) ja tekevät älykkäitä valintoja.

## Yleisiä väärinkäsityksiä

**Väärinkäsitys 1: "Multimodaalisuus tarkoittaa, että voin heittää kaikki materiaalit kerralla"**
- **Todellisuus:** Multimodaalisuus on työkalu, mutta kuvakaappaukset ovat suuria (10 000+ tokenia). Sinun täytyy valita strategisesti.
- **Korjaus:** Näytä token-kustannukset. "Jokainen kuva = 10 000 tokenia. Jos heität 3 kuvakaappauksia, käytät 30 000 tokenia konteksti-ikkunasta."

**Väärinkäsitys 2: "Kuvakaappaukset ovat aina parempia kuin teksti"**
- **Todellisuus:** Kuvakaappaukset ovat hyödyllisiä visuaalisissa ongelmissa, mutta koodin muokkaus vaatii tekstiä.
- **Korjaus:** Näytä esimerkki: "Jos näytän kuvakaappauksen koodista, tekoäly voi lukea sen. Mutta tekoäly ei voi muokata kuvakaappauksen koodia. Tekstiä voi muokata."

**Väärinkäsitys 3: "Kaikki mallit ovat multimodaalisia"**
- **Todellisuus:** Vanhat mallit, jotkut spesifikoituneet mallit ja halpammallit näkevät vain tekstiä.
- **Korjaus:** Opeta, että ammattilaisena tiedät mallin kyvyt ja valitset oikean mallin oikeaan tehtävään.

**Väärinkäsitys 4: "Logit ovat parempia kuvakaappaus-muodossa"**
- **Todellisuus:** Usein teksti on parempi — valittu ja suodatettu. Kuvakaappaus lokista on suuri ja hankala.
- **Korjaus:** Opeta: "Suodata olennaisten virheitä ja kopioi tekstinä. Se on pienempi ja tehokkaampi."

## Opettajan fasilitointiohjeet

### Ennen oppituntia
- Testaa tehtävä 6.1 etukäteen. Tiedä, miten eri vastaukset eroavat toisistaan.
- Valitse konkreettinen IT-ongelma, jonka opiskelijat tunnustavat — ei abstrakti, vaan oikea tapaus.
- Tutki multimodaaliset mallit (GPT-4V, Claude 3, Gemini) ja niiden kyvyt.

### Oppitunnin aikana
- **Avaa johdannolla:** "Tekoäly voi nyt nähdä kuvia. Tämä muuttaa kaiken IT-työssä — voimme näyttää ongelmasta kuvan."

- **Käytä konkreettisia esimerkkejä:** Tehtävä 6.1:n kaltainen demo on erittäin tehokas. "Näet itse, kuinka vastaus muuttuu."

- **Korostaa valinnan tärkeyttä:** Multimodaalisuus ei ole "kaikki kerralla" — se on strateginen valinta.

- **Token-kustannukset:** Mainitse joka kerta. "Kuvakaappaus maksaa 10 000 tokenia. Teksti maksaa 1000. Valitse viisaasti."

- **Opiskelijoiden IT-maailma:** Käytä esimerkkejä, jotka ovat heille relevantteja. UI-bugit, tietokanta-virheet, lokit.

### Yleisiä haasteita ja ratkaisuja

**Haaste: "Opiskelijat sanovat: 'Miksi kuvakaappaus, kun voin vain kuvailla?'"**
- Ratkaisu: Tehtävä 6.1 osoittaa tämän. Kun näet kaksi vastaustapausta rinnakkain, ero on selvä.

**Haaste: "Opiskelijat ylikuormittavat kontekstia kuvakaappuksilla"**
- Ratkaisu: Opeta valinta. "Ota vain 1-2 kuvakaappaus — kriittiset. Loput tekstinä tai logina."

**Haaste: "Opiskelijat eivät tiedä, millä mallilla on multimodaaliset kyvyt"**
- Ratkaisu: Opeta tutkimisen. "Ennen kuin käytät kuvaa, tarkista: Tukeeko tämä malli kuvia?" (ChatGPT-4V kyllä, GPT-3.5 ei, Claude 3 kyllä, jne.)

## Arviointivinkit

**Tehtävä 6.1 jälkeen:**
- Katso opiskelijoiden täytettyä vertailu-taulukkoa. Osoittaako se, että he näkivät eron kahden vastauksen välillä?
- Kysy: "Missä tilanteessa kuvakaappaus oli olennainen?" Oikea vastaus: "Kun visuaalinen tieto oli kriittiinen — väri, asettelu."

**Tehtävä 6.2 jälkeen:**
- Lue opiskelijoiden multimodaalisen kontekstin rakennusta. Osoittaako se strategista ajattelua?
- Etsi merkkejä siitä, että opiskelija ymmärtää token-kustannukset ja tekee valintoja sen perusteella.
- Kysy: "Miksi valitsit tämän materiaalin? Miksi jätit tuon pois?" Oikea vastaus: "Koska se on oleellista ja ei käytä liikaa tokeneita."

## Jatkava integraatio jatkoprojekteissa

- **Jokainen projekti käyttää multimodaalisuutta:** Kun opiskelijat käyttävät tekoälyä, he ottavat kuvakaappauksia, dokumentoivat lokkeja, ja käyttävät multimodaalista kontekstia.
- **Ammattitaidot:** Tämä on elämän taito IT-ammattilaiselle. Kuka voi käyttää kuvakaappauksia tehokkaasti, on produktiivimpi.

Tämä oppitunti sulkee kurssin "konteksti-kolmikko" — oppitunnit 4, 5 ja 6 opettavat opiskelijoille kaiken, mitä he tarvitsevat hallitakseen tekoälyä ammattilaisesti. Oppitunti 4: mitä konteksti on. Oppitunti 5: kuinka hallita se suurissa projekteissa. Oppitunti 6: kuinka käyttää eri tietomuotoja. Yhdessä nämä ovat IT-ammattilaiseen tärkeitä taitoja.
