# Sanasto — Oma apuri-botti

## Botin suunnittelu

**Botin määrittely** — Lyhyt kuvaus siitä, kenelle botti on, mitä se osaa, mitä se ei tee ja mitkä ovat sen rajat. Tämä on botin "perustamisasiakirja", josta järjestelmäprompti johdetaan. Älä sekoita tätä siihen, mitä botti auttaa käyttäjää tekemään — määrittely kertoo botista itsestään.

**Kohderyhmä** — Ne käyttäjät, joita varten botti on rakennettu. Esimerkiksi luokkakaverit, kerhon uudet jäsenet tai kirjaston asiakkaat. Kun tiedät kohderyhmän, osaat valita oikean kielen ja sisällön.

**Työnkulku** — Järjestys, jossa botti ohjaa käyttäjää vaiheesta toiseen. Selkeä työnkulku auttaa botin pysymään raiteilla eikä hyppimään satunnaisesti.

**Rajat** — Määritelmä siitä, mitä botti tekee ja mitä ei. Selkeät rajat estävät bottia leviämästä hallitsemattomasti tai vastaamasta asioihin, joihin sen ei kuulu vastata.

**Tietopohja** — Kokoelma dokumentteja, joista botti ammentaa oman aiheesi tietoa. Hyvä botti nojaa kuratoituun tietopohjaan, ei pelkkiin yleisiin oletuksiin.

**Iterointi** — Botin parantaminen testaamalla, korjaamalla ja testaamalla uudelleen. Hyvä botti syntyy iteroinnista, ei heti ensimmäisellä yrityksellä.

## Custom GPT:t ja botit

**System prompt** (järjestelmäprompti) — Pitkä, yksityiskohtainen ohjeistus, joka kerrotaan kielimallille botin alussa. Se määrittelee, kuka botti on, mitä se tekee ja miten se käyttäytyy. System prompt vaikuttaa kaikkiin botin vastauksiin.

**Custom GPT** — Mukautettu ChatGPT-versio, joka on konfiguroitu tiettyyn tarkoitukseen. Se voi sisältää system promptin, ohjeita, tiedostoja ja integraatioita.

**Persona** — Botin rooli tai persoona. Esimerkiksi: "Olet Python-tutori" tai "Olet asiakaspalvelun edustaja." Persona tekee botista uskottavan ja johdonmukaisen.

**Context** (konteksti) — Taustatieto, jonka botti käyttää ymmärtääkseen ja vastatakseen kysymyksiin. Esimerkiksi edellinen keskustelu tai dokumentit, jotka on syötetty bottiin.

**Iteraatio** — Prosessi, jossa testataan, parannetaan, testataan uudelleen ja parannetaan jälleen. Hyödylliset botit syntyvät iteraation kautta, ei heti täydellisesti ensimmäisellä kerralla.

## Testaus

**Positiivinen testaus** — Testataan asioita, joiden pitäisi toimia. Nähdään, vastaako botti oikein normaaleissa tilanteissa.

**Negatiivinen testaus** — Testataan asioita, joiden ei pitäisi toimia. Nähdään, kieltäytyykö botti asianmukaisesti ja suojaauko se itseään.

**Reunatapaus** (edge case) — Poikkeava tai odottamaton tilanne. Esimerkiksi: tyhjä syöte, vääränä kielellä kirjoitettu teksti, hyvin pitkä teksti. Reunatapaukset osoittavat, kuinka robust botti on.

**Testidokumentti** — Kirjallinen raportti testistä, joka sisältää: syöte, odotettava tulos, todellinen tulos ja analyysin.

## Viestintä ja vuorovaikutus

**Vuorovaikutuksellinen** — Kaksisuuntainen: käyttäjä kysyy, botti vastaa, käyttäjä kysyy lisää. Se ei ole yhdensuuntaista tiedon jakamista.

**Täsmällisyys** — Vastauksen oikeellisuus ja relevanssi. Botti, joka vastaa epätäsmällisesti, on hyödytön.

**Muistinvaraus** — Botin kyky muistaa aiempia vastauksia samassa keskustelussa. Hyvin suunniteltu botti ei kysy samaa asiaa kahdesti.

**Validointi** — Tarkistaminen, että tieto on oikein ennen sen käyttämistä. Esimerkiksi: "Ymmärsinkö oikein: treenaat kolmena päivänä viikossa ja tavoitteesi on parantaa kuntoa?"

## Dokumentointi

**Dokumentaatio** — Kirjallinen tai visuaalinen kuvaus siitä, miten jotain tehdään tai miten jokin toimii. Hyvä dokumentaatio auttaa muita ymmärtämään ja jatkamaan työtä.

**Prosessin dokumentointi** — Kuvaus kaikista askeista, joita otettiin ongelman ratkaisussa. Näytetään, mitä tehtiin, mitä saatiin ja mikä meni väärin.

**Kommentti** — Ohjelmakoodi tai dokumentissa oleva teksti, joka selittää, mitä seuraava rivi tai osio tekee. Kommentit auttavat sinua ja muita ymmärtämään logiikan.

## Johtaminen ja rakentaminen

**Mentori** — Kokenut henkilö, joka ohjaa ja opastaa muita. Apuri-botti toimii mentorina, joka esittää oikeita kysymyksiä ja ohjaa käyttäjää eteenpäin.

**Kalibrointi** — Säätäminen oikealle tasolle. Esimerkiksi: ovatko botin kysymykset liian yksinkertaiset vai liian monimutkaiset? Kalibrointi paranee testaamalla.

**Feedback** — Palaute. Käyttäjän mielipide siitä, kuinka hyvin botti toimi. Feedback auttaa parantamaan bottia.

---

Muista, että nämä käsitteet eivät ole isoloituja — ne linkittyvät toisiinsa. Hyvä system prompt johtaa hyödylliseen bottiin, jota voidaan testata, dokumentoida ja parantaa iteraation kautta.

---
