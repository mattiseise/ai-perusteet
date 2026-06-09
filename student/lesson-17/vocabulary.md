# Sanasto — Projektidokumenttibotti

## Projektin suunnittelu

**Projektisuunnitelma** — Kirjallinen dokumentti, joka kuvaa projektin tavoitteen, käyttäjät, aikataulun, resurssit ja menetelmät. Hyvä suunnitelma vastaa kysymyksiin: mitä, kenelle, miksi, milloin ja miten.

**Stakeholder** (sidosryhmä) — Henkilö tai organisaatio, jolla on intressi projektiin. Esimerkiksi asiakkaat, sijoittajat, tiimin jäsenet tai käyttäjät.

**Scope** (projektin laajuus) — Määritelmä siitä, mitä projektiin sisältyy ja mitä ei. Selkeä scope estää projektia laajenemasta kontrolloimattomasti.

**Aikataulu** — Suunnitelma siitä, mitä tehdään milloin. Sisältää vaiheet (fase), deadlinet ja riippuvuudet.

**Resurssi** — Mitä tarvitaan projektin tekemiseen. Ihmisiä (tiimi), rahaa (budjetti), teknologiaa, prosesseja.

**Riskianalyysi** — Tunnistaminen ja arviointi asioista, jotka voivat mennä pieleen, ja niiden ratkaisuista.

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

**Validointi** — Tarkistaminen, että tieto on oikein ennen sen käyttämistä. Esimerkiksi: "Ymmärsinkö oikein: sinulla on 3 kehittäjää ja 50 000 euron budjetti?"

## Dokumentointi

**Dokumentaatio** — Kirjallinen tai visuaalinen kuvaus siitä, miten jotain tehdään tai miten jokin toimii. Hyvä dokumentaatio auttaa muita ymmärtämään ja jatkamaan työtä.

**Prosessin dokumentointi** — Kuvaus kaikista askeista, joita otettiin ongelman ratkaisussa. Näytetään, mitä tehtiin, mitä saatiin ja mikä meni väärin.

**Kommentti** — Ohjelmakoodi tai dokumentissa oleva teksti, joka selittää, mitä seuraava rivi tai osio tekee. Kommentit auttavat sinua ja muita ymmärtämään logiikan.

## Johtaminen ja rakentaminen

**Mentori** — Kokenut henkilö, joka ohjaa ja opastaa muita. Projektidokumenttibotti toimii mentorina, joka esittää oikeita kysymyksiä.

**Kalibrointi** — Säätäminen oikealle tasolle. Esimerkiksi: ovatko botin kysymykset liian yksinkertaiset vai liian monimutkaiset? Kalibrointi paranee testaamalla.

**Feedback** — Palaute. Käyttäjän mielipide siitä, kuinka hyvin botti toimi. Feedback auttaa parantamaan bottia.

---

Muista, että nämä käsitteet eivät ole isoloituja — ne linkittyvät toisiinsa. Hyvä system prompt johtaa hyödylliseen bottiin, jota voidaan testata, dokumentoida ja parantaa iteraation kautta.

---
