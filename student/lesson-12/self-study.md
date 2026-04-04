# Promptit II: kontekstin rakentaminen käytännössä

## Johdanto: Monimutkainen IT-ongelma vaatii rakennettua ratkaisua

Kuvittele seuraavaa skenaariota. Sinulla on koodista bugi. Se ei ole pieni — se on monimutkainen. Virhe ilmenee vain tietyissä tilanteissa. Ensimmäisellä yrityksellä kysyt ChatGPT:tä: "Miksi tämä funktio ei toimi?" Vastaus on yleinen ja ei osuva. Kokeilit verkon hakuja. Pitkityt samalla kun aika kuluu.

Nyt kokeile erilaista lähestymistapaa. Ensimmäisellä kerralla annat tavoitteen: "Minulla on bugi funktioissa, jotka käsittelevät käyttäjän tietoja." Toisella kerralla annat kontekstia: "Virhe ilmenee vain, kun käyttäjä kirjoittaa erikoismerkkejä, kuten ä tai ö." Kolmannella kerralla annat koodinpätkän. Neljännellä kerralla kysyt tarkentavaa: "Miten validoidaan Suomen nimet oikein?" Jokainen kierros rakentaa edellisen päälle.

Tämä on ammattilaisesti tekemisen prosessi. Et etsi "täydellisen vastauksen" yhtä promptia kirjoittamalla. Rakennat ratkaisua iteratiivisesti, antamalla kontekstia kierros kierrokselta, kunnes päädyt käyttökelpoiseen lopputulokseen. Tämä oppitunti opettaa sinulle, kuinka rakentaa konteksti käytännössä. Se on tämän kurssin tärkein taito.

## Taustatietojen antaminen: Miksi konteksti ratkaisee

Hyvin usein tekoälyn antama vastaus on huono, koska se ei ymmärrä *kontekstia*. Konteksti on kaikki tieto, jonka tekoäly tarvitsee tehtävän ymmärtämiseen ja ratkaisemiseen hyvin.

Esimerkiksi: "Kirjoita dokumentaatio funktiolle." On prompt. Mutta dokumentaatio voi olla:
- Kehittäjäille (tekninen, alaviitteillä, koodin esimerkeillä)
- Käyttäjille (yksinkertainen, ilman teknistä jargonia)
- Opiskelijoille (opettavainen, vaihe vaiheelta)

Ilman kontekstia tekoäly tekee arvauksia. Kontekstin kanssa — esimerkiksi "dokumentaatio on 15-vuotiaille IT-opiskelijoille, jotka opettelevat ohjelmointia" — tekoäly osaa kirjoittaa sopivan tason ja sävyn.

Ammattilaisesti konteksti rakentuu useista lähteistä:
- Mitä olet jo tehnyt ja mikä on nykyinen tilanne
- Mitkä ovat vaatimukset ja rajat
- Kenen kanssa voit työskennellä (tiimi, asiakas, yleisö)
- Mitä muuta on relevanttia

Kun annat tämän kontekstin, vastaukset paranevat merkittävästi. Se vaatii enemmän aikaa promptissa, mutta säästää moninkertaisesti iteraatioissa.

> **Pysähdy hetkeksi:** Ajattele viimeistä kertaa, kun käytit tekoälyä. Annoit sille riittävästi kontekstia? Mitä tietoa olisit voinut antaa, jonka olisit luullut olevan "ilmeistä"?

## Lähdeaineistojen liittäminen: Teksti koneelle syötettäväksi

Usein tekoälyn täytyy käsitellä olemassa olevaa materiaalia — artikkeli, raportti, koodi, asiakirja. Ammattilaisesti et pyydä tekoälyä "selittämään jotain, jonka et ole sille antanut" — annat materiaalin ja sitten kehotuksen.

Konkreettinen esimerkki: sinulla on tekninen dokumentaatio, jota haluat yksinkertaistaa. Voit:
1. Kopioida dokumentaation kokonaisuudessaan ChatGPT:hen: "Tässä on dokumentaatio. Kirjoita se uudelleen 5-vuotiaan ymmärryskykylle."
2. Liittää pääkohdan: "Dokumentaatio käsittelee verkkoprotokollaa. Pääkohdat ovat: [liita 5 tärkeintä kohtaa]. Kirjoita selitys, jonka 15-vuotias ymmärtää."

Ammattilaisesti valitset, mitä liität. Kokonaisaineisto on usein liian paljon — tekoälyn konteksti-ikkuna on rajoitettu. Eli "näyt pääkohdat" usein toimii paremmin.

Koodi on erityisen tärkeä. Jos sinulla on bugi, et kysy "miksi funktio ei toimi" — annat funktion:
```python
def validate_email(email):
    return "@" in email and "." in email
```

Ja sitten kehotus: "Tämä funktio on liian yksinkertainen. Mitä siihen pitäisi lisätä tarkammaksi validaatioksi?"

Tekoäly näkee koodin ja antaa spesifisen, koodiin perustuvan vastauksen. Se ei joudu arvaamaan, mitä koodi tekee.

## Tehtävän pilkkominen: Iso ongelma, pienempiä askelia

Yksi ammattilaisesti kriittinen taito on **pilkkominen** (decomposition). Kun sinulla on iso, monimutkainen tehtävä, et pyydä tekoälyä "ratkaise se" — pilkkot sen osiin.

Esimerkki: "Rakenna sähköpostin validointi-järjestelmä, joka tarkistaa, onko osoite olemassa, estää spam-osoitteita ja tallentaa validit osoitteet tietokantaan."

Se on iso. Pilkkosi sen:
1. Ensin: "Kirjoita regex-pattern, joka validoi sähköpostiosoitteen muodon."
2. Sitten: "Lisää tarkistus, että ei ole yhteiset spam-domainit."
3. Sitten: "Integroida tietokantaan — mitä SQL-kyselyä tarvitsen?"
4. Sitten: "Kuinka yhdistää nämä kolme osaa?" (integraatio)
5. Lopuksi: "Kuinka testata koko järjestelmä?" (testaus)

Jokainen osioiden on pienempi ja hallittavampi. Tekoäly antaa parempia vastauksia pienempiin osiin. Ja lopuksi yhdistät ne.

Ammattilaisesti pilkkominen on perusstrategia. Monimutkainen ongelma ei ole yksi prompt — se on viisi tai kymmenen pienpromptia, joissa jokainen rakentuu edellisen päälle.

> **Pysähdy hetkeksi:** Mitkä ovat ammattilaiset etuja sille, että pilkkot ongelman osiin tekoälylle? Mitä riskejä syntyy, jos et pilko sitä?

## Iteraatio ja tarkentaminen: Jatkopromptit, jotka terävöittävät

Kun tekoäly antaa ensimmäisen vastauksen, se on usein pohja. Ammattilaisesti seuraavat promptit terävöittävät sitä.

Esimerkiksi:
- **Kierros 1:** "Kirjoita JavaScript-funktio, joka muotoilee päivämäärän."
  - Saat: `function formatDate(date) { return new Date(date).toLocaleDateString(); }`

- **Kierros 2:** "Lisää tuki seuraaviin muotoihin: 'DD.MM.YYYY', 'YYYY-MM-DD', 'DD Month YYYY'."
  - Saat: parannettu versio, joka tukee useita muotoja.

- **Kierros 3:** "Lisää error-käsittely. Jos päivämäärä ei ole validi, palauta virhesanoma."
  - Saat: versio, joka käsittelee virheet.

- **Kierros 4:** "Lisää testit näille kolmelle muodolle. Sisällytä edge-case: karkausvuosi, marraskuu."
  - Saat: testit.

Jokainen kierros on hyvin spesifinen ja rakentaa edellisen päälle. Se on ammattilaiset kutsuvat "iteratiiviseksi kehitykseksi" tekoälyn kanssa.

Tärkeä periaate: **jatkoprompti on tarkempi kuin peruspromt­ti**. Et kirjoita "nyt paranna sitä" — kirjoitat "lisää nämä kolme asiaa: X, Y, Z". Spesifikkointi johtaa parempiin tuloksiin.

## Kontekstin rakentamisen ammattilaisesti: Case-tutkimus

Katsotaan koko prosessia yhteen tapaukseen alusta loppuun.

**Tehtävä: Rakenna Python-hakualgoritmi, joka etsii artikkeleita tietokannasta.**

**Kierros 1 — Tavoite:**
- Prompt: "Kirjoita Python-funktio, joka hakee artikkeleita hakusanalla."
- Tulos: Perus-funktio, joka tekee yksinkertaisen tekstihaun.

**Kierros 2 — Konteksti: Tietokanta ja rakenne**
- Prompt: "Tietokanta käyttää SQLite:a. Taulussa 'articles' on sarakkeet: id, title, content, author, published_date. Nyt hakaa artikkelit, joiden title-sarake sisältää hakusanan."
- Tulos: SQL-pohjainen ratkaisu, joka vastaa tietokannan rakenteeseen.

**Kierros 3 — Rajat: Suorituskyky**
- Prompt: "Tietokannassa on 1 miljoonaa artikkelia. Yksinkertainen LIKE-haku on liian hidas. Käytä indeksointia tai tarkemmin optimoitua hakua."
- Tulos: Paremmin optimoitu versio.

**Kierros 4 — Tarkentaminen: Tulokset**
- Prompt: "Palauta tulokset järjestettynä relevanssin perusteella — tärkeimmät ensin. Sisällytä myös how many hits -laskuri."
- Tulos: Järjestetyt tulokset, jonka näyttävät relevanssin.

**Kierros 5 — Integraatio: Virheenkäsittely**
- Prompt: "Lisää error-käsittely. Jos hakusana on tyhjä, palauta kaikki artikkelit. Jos tietokanta-yhteys epäonnistuu, anna selvä virhesanoma."
- Tulos: Tuotanto­kelpoin ratkaisu, joka käsittelee virheet.

Koko prosessi rakentui konteksti kierros kierrokselta. Ammattilaisesti tämä on tehokas lähestymistapa: olet täydentänyt ratkaisua vaihe vaiheelta ilman, että etsiit kokonaan uutta koodia jokaisen kierroksen jälkeen.

## Yhteenveto: Kontekstin rakentaminen ammattilaisella

Ammattilaisesti kontekstin rakentaminen on seuraava prosessi:

1. **Aloita selkeällä tavoitteella**: "Mitä haluan tehdä?" — yksinkertainen, spesifinen prompt.

2. **Anna taustatiedot**: "Mikä on nykyinen tilanne? Mitä tarvitsen?" — konteksti rakentuu.

3. **Pilkkoa isot ongelmat**: Rakentaa pienempiin osiin, jotka voit ratkoa yksitellen.

4. **Liitä olemassa oleva aineisto**: Koodi, tiedot, vaatimukset — anna tekoälylle nähtäväksi.

5. **Iteroi ja terävöi**: Jatkopromptit tekevät vastauksesta paremmaksi, spesifimmäksi, käyttökelpoisemmaksi.

6. **Testaa ja validoi**: Jokaisen kierroksen jälkeen testaa, että vastaus toimii omassa kontekstissasi.

Tämä prosessi vaatii enemmän aikaa ensimmäisessä promptissa ja merkittävästi vähemmän iteraatioissa verrattuna "kaiken kerralla" -lähestymistapaan. Ammattilaisesti se on parempi investointi. Opit tämän harjoittelemalla oikeita IT-projekteja.
