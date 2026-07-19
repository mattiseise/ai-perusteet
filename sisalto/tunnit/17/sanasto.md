# Sanasto — Oma apuri-botti

## Botin suunnittelu

**Botin määrittely** — Lyhyt kuvaus siitä, kenelle botti on, mitä se osaa, mitä se ei tee ja mitkä ovat sen rajat. Tämä on botin "perustamisasiakirja", josta järjestelmäprompti johdetaan. Älä sekoita tätä siihen, mitä botti auttaa käyttäjää tekemään — määrittely kertoo botista itsestään.

**Kohderyhmä** — Ne käyttäjät, joita varten botti on rakennettu. Esimerkiksi luokkakaverit, kerhon uudet jäsenet tai kirjaston asiakkaat. Kun tiedät kohderyhmän, osaat valita oikean kielen ja sisällön.

**Työnkulku** — Järjestys, jossa botti ohjaa käyttäjää vaiheesta toiseen. Selkeä työnkulku auttaa botin pysymään raiteilla eikä hyppimään satunnaisesti.

**Rajat** — Määritelmä siitä, mitä botti tekee ja mitä ei. Selkeät rajat estävät bottia leviämästä hallitsemattomasti tai vastaamasta asioihin, joihin sen ei kuulu vastata.

**Tietopohja** — Kokoelma dokumentteja, joista botti ammentaa oman aiheesi tietoa. Hyvä botti nojaa kuratoituun tietopohjaan, ei pelkkiin yleisiin oletuksiin.

**Iterointi** — Botin parantaminen testaamalla, korjaamalla ja testaamalla uudelleen. Hyvä botti syntyy iteroinnista, ei heti ensimmäisellä yrityksellä.

## Custom GPT:t ja botit

**Järjestelmäprompti** — Botin toimintaa ohjaava teksti, joka määrittää botin roolin, tehtävän, toimintatavan ja rajat. Se vaikuttaa kaikkiin botin vastauksiin.

**Räätälöity GPT (Custom GPT)** — Tiettyyn tarkoitukseen määritetty ChatGPT-versio. Se voi sisältää järjestelmäpromptin, ohjeita, tiedostoja ja integraatioita.

**Persoona** — Botille määritetty viestintätapa ja sävy. Persoona voi olla esimerkiksi ystävällinen ja kärsivällinen tai suora ja asiallinen. Se tukee botin roolia, mutta ei korvaa tehtävää tai asiantuntemusta.

**Konteksti** — Taustatieto, jonka perusteella botti tulkitsee pyyntöä ja muodostaa vastauksen. Konteksti voi sisältää aiemman keskustelun tai botille annetut dokumentit.

**Iteraatio** — Prosessi, jossa testataan, parannetaan, testataan uudelleen ja parannetaan jälleen. Hyödylliset botit syntyvät iteraation kautta, ei heti täydellisesti ensimmäisellä kerralla.

## Testaus

**Positiivinen testaus** — Testataan asioita, joiden pitäisi toimia. Nähdään, vastaako botti oikein normaaleissa tilanteissa.

**Negatiivinen testaus** — Testataan asioita, joiden ei pitäisi toimia. Nähdään, kieltäytyykö botti asianmukaisesti ja suojaauko se itseään.

**Reunatapaus** — Poikkeava tai odottamaton tilanne, kuten tyhjä syöte, väärällä kielellä kirjoitettu teksti tai hyvin pitkä teksti. Reunatapausten avulla arvioidaan, kuinka luotettavasti botti toimii poikkeavissa tilanteissa.

**Testidokumentti** — Kirjallinen raportti, joka sisältää syötteen, odotetun tuloksen, todellisen tuloksen ja analyysin.

## Viestintä ja vuorovaikutus

**Vuorovaikutuksellinen** — Kaksisuuntainen: käyttäjä kysyy, botti vastaa, käyttäjä kysyy lisää. Se ei ole yhdensuuntaista tiedon jakamista.

**Täsmällisyys** — Vastauksen oikeellisuus ja osuvuus suhteessa käyttäjän pyyntöön.

**Keskustelukonteksti** — Aiemmat viestit, joita botti voi hyödyntää saman keskustelun aikana. Hyvin suunniteltu botti ei kysy uudelleen jo annettua tietoa.

**Validointi** — Tarkistaminen, että tieto on oikein ennen sen käyttämistä. Esimerkiksi: "Ymmärsinkö oikein: treenaat kolmena päivänä viikossa ja tavoitteesi on parantaa kuntoa?"

## Dokumentointi

**Dokumentaatio** — Kirjallinen tai visuaalinen kuvaus siitä, miten jotain tehdään tai miten jokin toimii. Hyvä dokumentaatio auttaa muita ymmärtämään ja jatkamaan työtä.

**Prosessin dokumentointi** — Kuvaus kaikista askeista, joita otettiin ongelman ratkaisussa. Näytetään, mitä tehtiin, mitä saatiin ja mikä meni väärin.

**Kommentti** — Ohjelmakoodi tai dokumentissa oleva teksti, joka selittää, mitä seuraava rivi tai osio tekee. Kommentit auttavat sinua ja muita ymmärtämään logiikan.

## Johtaminen ja rakentaminen

**Mentori** — Kokenut henkilö, joka ohjaa ja opastaa muita. Apuri-botti toimii mentorina, joka esittää oikeita kysymyksiä ja ohjaa käyttäjää eteenpäin.

**Kalibrointi** — Säätäminen oikealle tasolle. Esimerkiksi: ovatko botin kysymykset liian yksinkertaiset vai liian monimutkaiset? Kalibrointi paranee testaamalla.

**Palaute** — Käyttäjän arvio siitä, kuinka hyvin botti toimi. Palautetta käytetään botin kehittämiseen.

---

Käsitteet liittyvät toisiinsa. Hyvä järjestelmäprompti tukee hyödyllistä bottia, jota testataan, dokumentoidaan ja parannetaan iteratiivisesti.

---
