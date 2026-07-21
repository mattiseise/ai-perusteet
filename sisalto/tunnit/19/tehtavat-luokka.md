# Opiskelutehtävät: Mikä agentti on — ja mitä se ei ole?

> Tämä tunti valmistelee Agentit-osion lopputyötä. Tänään kirjoitat alustavia ongelmaehdokkaita. Valitset lopullisen projektin vasta Automaatio vai autonomia -tunnin lopussa, kun olet arvioinut, tarvitseeko ongelma todella agenttia.

*Kaikkia ei tarvitse tehdä. Valitse tehtävistä 1. Suosittelen kuitenkin, että teet ainakin pohjapiirroksen — se on lopputyön osa.*

---

## Ongelmaehdokkaat — suositeltu

**Miksi tämä on tärkeää:** Hyvä projekti alkaa ongelmasta, ei työkalusta. Tässä vaiheessa vaihtoehtoja saa olla useita. Automaatio vai autonomia -tunnilla testaat ne päätöspuulla ja valitset vasta sitten projektin, jota jatkat tunneilla 21–27.

### Tehtävä

Kirjaa kaksi tai kolme ongelmaa, joita voisi ehkä ratkaista agentilla. Valitse niistä yksi alustava ehdokas ja kirjoita lyhyt kuvaus (100–150 sanaa), jossa vastaat kolmeen kysymykseen:

1. Mikä ongelma on kyseessä ja kenelle se on tarkoitettu?
2. Missä kohdassa tilanteet vaihtelevat niin, että kielimallin rajattu valinta voisi olla hyödyllinen?
3. Mikä yksinkertaisempi ratkaisu saattaisi silti riittää?

Ongelman ei tarvitse olla monimutkainen, ja sen voi valita arjesta, harrastuksesta, opiskelusta tai työelämästä. Älä vielä lupaa tiettyä teknistä toteutusta. Tärkeintä on kuvata käyttäjän todellinen tarve ja kohta, jossa tilanteen mukaan muuttuva valinta voisi tuoda hyötyä.

### Tekoälyvaihe — arvioi alustavaa ehdokasta

Avaa käytettävissäsi oleva kielimallisovellus ja käytä sitä sparrauskumppanina alustavan ehdokkaan haastamiseen. Älä pyydä tekoälyä keksimään ongelmaa puolestasi — pyydä sitä tutkimaan oman ehdotuksesi oletuksia.

```
Arvioin agenttiprojektin mahdollisena ehdokkaana seuraavaa ongelmaa: [kuvaa]. Käyttäjä on
[kuvaa]. Toimi kriittisenä sparrauskumppanina ja kysy minulta 3–4
kysymystä, jotka paljastavat, onko tämä todella agenttiongelma vai
riittäisikö yksinkertaisempi ratkaisu. Älä vastaa puolestani — kysy
niin että minä ajattelen.
```

Vastaa kysymyksiin omassa pohjapiirroksessasi. Tekoäly ei tee päätöksiä — sinä päätät.

> **Vinkki muistiinpanoihin:** Tee oma muistiinpanodokumentti, johon kerää kaikki viisi Agentti-pohjapiirrosta omiksi alaotsikoikseen. Agentin minimiversion rakennustunnilla kasaat ne kaikki yhdeksi suunnitelmaksi.

---

## Tehtävä 19.1 — Luokittele järjestelmät — syventävä

**Miksi tämä on hyödyllinen:** Tämä tehtävä harjoittaa täsmälleen sitä taitoa, jonka tarvitset pohjapiirroksesi perustelussa: mikä on agentti ja mikä ei.

### Tehtävä

Alla on neljä järjestelmän kuvausta. Tunnista jokaisen kohdalla, onko kyseessä **chatbot, tämän kurssin rajauksen mukainen tekoälyagentti vai ei kumpikaan**, ja perustele valintasi kuuden rakennusosan tarkistuslistan avulla.

**Järjestelmä A: Asiakaspalvelun chatbotti.** Asiakkaat voivat kirjoittaa kysymyksiään verkkosivuston chat-ikkunaan. Järjestelmä etsii hyväksytystä tietopohjasta sopivaa vastausta. Jos hyväksyttyä lähdettä ei löydy, lähteet ovat ristiriidassa tai pakollinen tieto puuttuu, se ilmoittaa asiakkaalle, että ihmisen palvelutiimi ottaa yhteyttä.

**Järjestelmä B: Automaattinen kasvihuoneen ilmaston valvonta.** Valvonta-agentti seuraa jatkuvasti kasvihuoneen lämpötilaa, ilmankosteutta ja maan kuivuutta. Kun lämpötila nousee yli 28 asteeseen kahden minuutin ajan, agentti avaa automaattisesti tuuletusluukut ja käynnistää kastelun. Agentti lähettää myös ilmoituksen vastuuhenkilölle ja dokumentoi tapahtumat. Tunnin kuluttua, jos olosuhteet ovat palautuneet normaaleiksi, agentti sulkee luukut.

**Järjestelmä C: Kuvankäsittelyohjelma.** Kun käyttäjä lataa kuvan, ohjelma tunnistaa automaattisesti kuvan objektit ja lisää kuvailevat tagit metadataan. Ohjelma analysoi myös kuvan kirkkautta ja säätää sitä automaattisesti sopivammaksi. Ohjelma ei itse päätä, mitä kuvia käyttäjä haluaa käsitellä — se vain käsittelee jokaisen kuvan, joka sille annetaan, samalla logiikalla.

**Järjestelmä D: Tekoälysovelluksen agenttitila.** Toimiston tietokoneella on tekoälysovellus, jossa on agenttitila. Käyttäjä kirjoittaa: "Käy läpi tämän kansion 12 kokousmuistiota ja kokoa taulukko kaikista päätöksistä ja vastuuhenkilöistä." Sovellus pyytää ensin luvan kansioon ja näyttää vaihesuunnitelmansa. Sitten se lukee tiedostot, pysähtyy kysymään lupaa ennen uuden tiedoston kirjoittamista ja raportoi lopuksi, mitä teki ja minkä muistion kohdalla se jäi epävarmaksi.

Täytä jokaisen järjestelmän kohdalle valintasi (chatbot, tämän kurssin rajauksen mukainen tekoälyagentti tai ei kumpikaan) ja perustelu 2–3 lauseella. Käytä termejä *reaktiivinen, proaktiivinen, autonominen, tavoite* ja *päätöksenteko* sekä viittaa vähintään kahteen kuuden rakennusosan tarkistuslistan kohtaan.

Vastaa järjestelmän D kohdalla lisäksi kahteen kysymykseen:

1. Osoita kuvauksen tekstistä kohdat, joista tunnistat vähintään neljä kuudesta rakennusosasta — mikä lause paljastaa minkä osan? Mitkä osat eivät näy kuvauksessa suoraan, ja miksi ne silti todennäköisesti ovat olemassa?
2. Vertaa alustavaan ongelmaehdokkaaseesi: valmisagentissa joku muu on rakentanut kielimallia ympäröivän agentin ohjauskehyksen. Mitkä kuudesta suunnittelukohdasta näkyvät tuotteessa, mitkä eivät ole tarpeellisia ja mitä mahdollinen oma projekti vaatisi?

> **Vinkki muistiinpanoihin:** Kirjaa vastauksesi omiin muistiinpanoihisi. Tätä tehtävää ei palauteta, mutta sen havainnot tukevat pohjapiirroksen perustelua.

---

**Ongelmaehdokkaat valmiina — lopullinen projektivalinta tehdään Automaatio vai autonomia -tunnilla**
