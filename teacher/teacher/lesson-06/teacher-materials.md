# Opettajan materiaalit

## Oppimisen tavoitteet tälle lohkolle

1. Opiskelijat ymmärtävät, mitä multimodaalisuus on — tekoälyn kyky käsitellä erilaisia tietomuotoja (tekstiä, kuvia, lokeja, koodia).

2. Opiskelijat näkevät käytännössä, kuinka kuvakaappaukset parantavat kontekstia IT-ongelmissa.

3. Opiskelijat oppivat rakentamaan tehokkaan multimodaalisen kontekstin — milloin käyttää tekstiä, milloin kuvakaappauksia ja milloin molempia.

4. Opiskelijat ymmärtävät multimodaalisten mallien rajoitukset (token-kustannukset, lukemisen riskit) ja tekevät älykkäitä valintoja.

## Yleisiä väärinkäsityksiä

**Väärinkäsitys 1: "Multimodaalisuus tarkoittaa, että voin heittää kaikki materiaalit kerralla"**
- **Todellisuus:** Multimodaalisuus on työkalu, mutta kuvakaappaukset ovat suuria (10 000+ tokenia). Sinun täytyy valita strategisesti.
- **Korjaus:** Näytä token-kustannukset. "Jokainen kuva = 10 000 tokenia. Jos käytät 3 kuvakaappausta, käytät 30 000 tokenia konteksti-ikkunasta."

**Väärinkäsitys 2: "Kuvakaappaukset ovat aina parempia kuin teksti"**
- **Todellisuus:** Kuvakaappaukset ovat hyödyllisiä visuaalisissa ongelmissa, mutta koodin muokkaus vaatii tekstiä.
- **Korjaus:** Näytä esimerkki: "Jos näytän kuvakaappauksen koodista, tekoäly voi lukea sen. Mutta tekoäly ei pysty muokkaamaan kuvakaappauksessa olevaa koodia. Tekstinä esitettyä koodia se voi muokata."

**Väärinkäsitys 3: "Kaikki mallit ovat multimodaalisia"**
- **Todellisuus:** Vanhat mallit, jotkin erikoistuneet mallit ja halvemmat mallit näkevät vain tekstiä.
- **Korjaus:** Opeta, että ammattilaisena tiedät mallin kyvyt ja valitset sopivan mallin tehtävään.

**Väärinkäsitys 4: "Lokit ovat parempia kuvakaappausmuodossa"**
- **Todellisuus:** Usein teksti on parempi — valittuna ja suodatettuna. Kuvakaappaus lokista on suuri ja hankala.
- **Korjaus:** Opeta: "Suodata olennaiset virheet ja kopioi ne tekstinä. Se on pienempi ja tehokkaampi."

## Opettajan fasilitointiohjeet

### Ennen oppituntia
- Testaa tehtävä 6.1 etukäteen. Tiedä, miten eri vastaukset eroavat toisistaan.
- Valitse konkreettinen IT-ongelma, jonka opiskelijat tunnistavat — ei abstrakti, vaan oikea tapaus.
- Tutustu multimodaalisiin malleihin (GPT-4V, Claude 3, Gemini) ja niiden kykyihin.

### Oppitunnin aikana
- **Avaa johdannolla:** "Tekoäly voi nyt nähdä kuvia. Tämä muuttaa kaiken IT-työssä — voimme näyttää ongelmasta kuvan."

- **Käytä konkreettisia esimerkkejä:** Tehtävän 6.1 kaltainen demo on erittäin tehokas. "Näet itse, kuinka vastaus muuttuu."

- **Korosta valinnan tärkeyttä:** Multimodaalisuus ei ole "kaikki kerralla" — se on strateginen valinta.

- **Token-kustannukset:** Mainitse ne joka kerta. "Kuvakaappaus maksaa 10 000 tokenia. Teksti maksaa 1000. Valitse viisaasti."

- **Opiskelijoiden IT-maailma:** Käytä esimerkkejä, jotka ovat heille relevantteja. Käyttöliittymävirheet, tietokantavirheet, lokit.

### Yleisiä haasteita ja ratkaisuja

**Haaste: "Opiskelijat sanovat: 'Miksi kuvakaappaus, kun voin vain kuvata?'"**
- Ratkaisu: Tehtävä 6.1 osoittaa tämän. Kun näet kaksi vastaustapausta rinnakkain, ero on selvä.

**Haaste: "Opiskelijat ylikuormittavat kontekstia kuvakaappauksilla"**
- Ratkaisu: Opeta valintaa. "Ota vain 1–2 kuvakaappausta — olennaiset. Loput tekstinä tai lokina."

**Haaste: "Opiskelijat eivät tiedä, millä mallilla on multimodaaliset kyvyt"**
- Ratkaisu: Opeta selvittämään asia. "Ennen kuin käytät kuvaa, tarkista: tukeeko tämä malli kuvia?" (ChatGPT-4V kyllä, GPT-3.5 ei, Claude 3 kyllä jne.)

## Arviointivinkit

**Tehtävä 6.1 jälkeen:**
- Katso opiskelijoiden täyttämää vertailutaulukkoa. Osoittaako se, että he näkivät eron kahden vastauksen välillä?
- Kysy: "Missä tilanteessa kuvakaappaus oli olennainen?" Oikea vastaus: "Kun visuaalinen tieto oli kriittinen — väri, asettelu."

**Tehtävä 6.2 jälkeen:**
- Lue opiskelijoiden multimodaalisen kontekstin rakentamista. Osoittaako se strategista ajattelua?
- Etsi merkkejä siitä, että opiskelija ymmärtää token-kustannukset ja tekee valintoja niiden perusteella.
- Kysy: "Miksi valitsit tämän materiaalin? Miksi jätit tuon pois?" Oikea vastaus: "Koska se on oleellista eikä käytä liikaa tokeneita."

## Jatkuva integraatio jatkoprojekteissa

- **Jokainen projekti käyttää multimodaalisuutta:** Kun opiskelijat käyttävät tekoälyä, he ottavat kuvakaappauksia, dokumentoivat lokeja ja käyttävät multimodaalista kontekstia.
- **Ammattitaidot:** Tämä on tärkeä taito IT-ammattilaiselle. Se, joka osaa käyttää kuvakaappauksia tehokkaasti, on tuottavampi.

Tämä oppitunti viimeistelee kurssin "konteksti-kolmikon" — kolme peräkkäistä oppituntia opettavat opiskelijoille kaiken, mitä he tarvitsevat hallitakseen tekoälyä ammattimaisesti. Ensin opittiin, mitä konteksti ja promptaus ovat. Sitten opittiin hallitsemaan kontekstia suurissa projekteissa. Nyt opittiin käyttämään erilaisia tietomuotoja. Yhdessä nämä ovat IT-ammattilaiselle tärkeitä taitoja.