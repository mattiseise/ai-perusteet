# AI työparina — pohja, muokkaus ja tarkistus

## Johdanto: työparuus ei tarkoita työn luovuttamista

Tekoälystä on hyötyä, kun sille annetaan rajattu rooli työprosessissa. Se voi tehdä ensimmäisen luonnoksen, ehdottaa vaihtoehtoja tai toimia kriittisenä lukijana. Ihminen päättää tavoitteen, tunnistaa virheet, tekee olennaiset valinnat ja hyväksyy lopputuloksen.

Tämän tunnin työskentelymalli on:

> **Pohja → oma muokkaus → tarkistus → päätös**

Tavoite ei ole saada tekoälyltä mahdollisimman valmis vastaus. Tavoite on tehdä oma ajattelu ja korjaukset näkyviksi.

<figure class="ai-demo"><span class="ai-demo__tag">// ehdotus kulkee kahden ihmisen päätöksen kautta</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:286px">
  <div style="display:flex;align-items:center;gap:10px;width:780px;font-family:var(--font-mono);font-size:11px">
    <div style="flex:1;padding:18px 8px;text-align:center;color:#fff;background:#211832;border:1.5px solid #b887e0;border-radius:12px"><b>IHMINEN</b><span style="display:block;margin-top:12px">rajaa tehtävän</span></div><b style="color:#863fc4">→</b>
    <div style="flex:1;padding:18px 8px;text-align:center;color:#fff;background:#11182a;border:1.5px solid #44517a;border-radius:12px"><b>TEKOÄLY</b><span style="display:block;margin-top:12px">luonnostelee</span></div><b style="color:#863fc4">→</b>
    <div style="flex:1;padding:18px 8px;text-align:center;color:#fff;background:#211832;border:1.5px solid #b887e0;border-radius:12px"><b>IHMINEN</b><span style="display:block;margin-top:12px">muokkaa</span></div><b style="color:#863fc4">→</b>
    <div style="flex:1;padding:18px 8px;text-align:center;color:#fff;background:#11182a;border:1.5px solid #44517a;border-radius:12px"><b>TEKOÄLY</b><span style="display:block;margin-top:12px">antaa palautetta</span></div><b style="color:#863fc4">→</b>
    <div style="flex:1;padding:18px 8px;text-align:center;color:#fff;background:#211832;border:1.5px solid #b887e0;border-radius:12px"><b>IHMINEN</b><span style="display:block;margin-top:12px">päättää</span></div>
  </div>
</div>
<figcaption class="ai-demo__cap">Työparisykli ei siirrä päätösvaltaa mallille. Ihminen määrittää suunnan ennen luonnosta ja hyväksyy, muokkaa tai hylkää ehdotukset myös palautekierroksen jälkeen.</figcaption></figure>

## Läpi kulkeva esimerkki: palautusohje luonnoksesta päätökseksi

Kuvittele, että kirjoitat verkkokaupan uudelle asiakkaalle lyhyen palautusohjeen. Hyväksytty lähde kertoo kolme asiaa: palautuksesta ilmoitetaan 14 päivän kuluessa, tuotteen pitää olla käyttämätön ja palautus aloitetaan tilausvahvistuksessa olevasta linkistä. Asiakaspalvelun yhteystieto on varareitti, jos linkki ei toimi.

Pyydät tekoälyltä enintään kuuden vaiheen luonnoksen. Luonnos alkaa selkeästi, mutta siinä lukee: ”Kirjaudu asiakastilillesi ja valitse Peruuta tilaus.” Lähteessä ei mainita asiakastiliä tai tämännimistä painiketta. Luonnoksesta puuttuu myös ehto, jonka mukaan tuotteen pitää olla käyttämätön. Teksti kuulostaa sujuvalta, mutta sitä ei voi julkaista sellaisenaan.

Luet luonnoksen lähteen rinnalla. Säilytät ymmärrettävän aloituksen, korvaat keksityn vaiheen ohjeella avata tilausvahvistuksen palautuslinkki ja lisäät käyttämättömyyttä koskevan ehdon. Kirjaat päätöslokiin, että ensimmäinen muutos perustuu todelliseen asiointipolkuun ja toinen palautusehtoihin. Näin oma työsi näkyy muuna kuin kieliasun silottamisena.

Seuraavaksi annat korjatun version tekoälylle testilukijan roolissa. Se huomauttaa, ettei aloittelija ehkä tiedä, mistä tilausvahvistus löytyy, ja ehdottaa samalla koko 14 päivän määräajan poistamista tekstin keventämiseksi. Hyväksyt ensimmäisen havainnon ja lisäät, että vahvistus löytyy sähköpostista. Hylkäät toisen ehdotuksen, koska määräaika on käyttäjän toiminnan kannalta olennainen lähdetieto.

Lopullinen ohje syntyy siis neljän erilaisen päätöksen kautta: tekoäly tuotti käyttökelpoisen pohjan, ihminen korjasi faktat, tekoäly auttoi löytämään yhden epäselvän kohdan ja ihminen arvioi myös palautteen. Työparuus ei näy siinä, kuinka monta virkettä tekoäly kirjoitti, vaan siinä, että jokaisen muutoksen peruste voidaan osoittaa.

## 1. Pyydä pohja, älä lopullista totuutta

Ensimmäinen versio voi olla rakenne, luonnos tai vaihtoehtojen lista. Kerro tekoälylle:

- mitä olet tekemässä
- kenelle lopputulos on tarkoitettu
- mitä lähdeaineistoa pitää käyttää
- missä muodossa pohja tarvitaan
- mitä asioita ei saa keksiä

Esimerkiksi käyttöohjeen ensimmäinen pohja voi sisältää otsikot ja työvaiheet. Se ei vielä ole julkaistava ohje. Sen tehtävä on antaa jotakin, jota voit arvioida ja muokata.

Palautusohjeen esimerkissä hyödyllinen pohja säästi rakenteen aloittamisen vaivan. Samalla keksitty painike osoitti, miksi luonnosta pitää käsitellä väitteenä, joka tarkistetaan, eikä valmiina tietona.

## 2. Lue kuin toimittaja

Älä aloita tekstin silottamisesta. Tarkista ensin sisältö:

1. Vastaako luonnos oikeaan tehtävään?
2. Säilyvätkö lähdeaineiston faktat?
3. Puuttuuko jokin olennainen vaihe?
4. Onko mukana perusteeton väite tai oletus?
5. Sopivatko rakenne ja vaikeustaso yleisölle?

Merkitse muutokset näkyviin. Voit käyttää kommentteja tai taulukkoa:

| Luonnoksen kohta | Ongelma | Oma korjaus | Peruste |
| --- | --- | --- | --- |
|  |  |  |  |

Tämä tekee ihmisen panoksen näkyväksi. Pelkkä lopullinen teksti ei kerro, ymmärsitkö, mitä piti korjata.

Päätösloki ei ole vain arviointia varten. Se auttaa myös myöhempää muokkaajaa näkemään, mikä kohta perustuu lähteeseen, mikä kohderyhmän tarpeeseen ja mikä on tietoinen rajaus. Ilman perustelua oikeakin muutos voi näyttää satunnaiselta tyylivalinnalta.

## 3. Tee itse olennaiset päätökset

Tekoäly voi ehdottaa, mutta se ei tunne tavoitettasi yhtä hyvin kuin sinä. Päätä itse ainakin:

- mitä sisältöä poistetaan tai lisätään
- mihin järjestykseen asiat asetetaan
- mikä sävy sopii tilanteeseen
- mitkä väitteet pitää tarkistaa lähteestä
- milloin luonnos hylätään kokonaan

Kaikkea ei tarvitse pelastaa. Jos luonnos perustuu väärään oletukseen, uusi rajattu prompti voi olla järkevämpi kuin pitkän tekstin paikkaaminen.

Ihmisen päätösvalta näkyy myös säilyttämisessä. Palautusohjeen selkeä aloitus kannatti pitää, vaikka seuraava vaihe oli väärä. Kriittinen lukeminen ei tarkoita kaiken tekoälyn tuottaman hylkäämistä, vaan jokaisen kohdan arvioimista tehtävän ja lähteen perusteella.

## 4. Käytä tekoälyä testilukijana

Kun olet tehnyt oman version, anna tekoälylle rajattu tarkistusrooli. Älä pyydä ”parantamaan kaikkea”, vaan etsi nimettyä ongelmaa:

- löydä kohta, jossa aloittelija voi eksyä
- osoita termi, jota ei ole selitetty
- etsi väite, jolle lähteessä ei ole tukea
- tarkista, etenevätkö vaiheet oikeassa järjestyksessä

Pyydä havainto ja kysymys, älä valmista uudelleenkirjoitusta. Näin sinä säilytät päätösvallan.

Testilukija ei tunne käyttäjää eikä todellista käyttötilannetta automaattisesti. Siksi sille annetaan kohderyhmä ja yksi tarkastelukulma. Palautusohjeessa kysymys ”Missä aloittelija voi jäädä jumiin?” toi esiin tilausvahvistuksen löytämisen, mutta ei antanut mallille oikeutta poistaa tärkeää määräaikaa.

## 5. Tarkista tarkistajan ehdotus

Tekoälyn palaute voi olla väärä, epäolennainen tai tyyliltään huono. Jokaisesta ehdotuksesta päätetään:

- hyväksyn
- muokkaan
- hylkään

Kirjaa ainakin yksi hylätty ehdotus ja sen peruste. Kriittinen työparuus näkyy myös siinä, mitä et ota mukaan.

Hyväksyminen, muokkaaminen ja hylkääminen eivät ole mielipideäänestyksiä. Ratkaisu sidotaan ennalta määriteltyyn tavoitteeseen, lähteeseen tai käyttäjän tarpeeseen. Silloin myös hylätty ehdotus osoittaa osaamista: tunnistit, miksi sujuvalta kuulostava muutos olisi heikentänyt lopputulosta.

## Sama sykli toimii eri tehtävissä

Mallia voi käyttää kirjoittamisessa, opiskelussa, suunnittelussa ja ongelmanratkaisussa. Tehtävä vaihtuu, mutta vastuunjako säilyy:

| Vaihe | Tekoälyn rooli | Ihmisen vastuu |
| --- | --- | --- |
| Pohja | tuottaa rajatun luonnoksen tai vaihtoehtoja | määrittää tehtävän ja aineiston |
| Muokkaus | voi vastata tarkentaviin kysymyksiin | korjaa sisällön, rakenteen ja sävyn |
| Tarkistus | etsii nimettyä ongelmaa | arvioi ehdotuksen ja tarkistaa lähteet |
| Päätös | ei tee lopullista hyväksyntää | hyväksyy, hylkää ja vastaa tuloksesta |

## Yhteenveto

Tekoäly on hyödyllinen työpari, kun sen rooli vaihtuu työvaiheen mukaan. Ensin se tekee pohjan. Sitten ihminen muokkaa ja perustelee muutokset. Lopuksi tekoäly voi toimia rajattuna testilukijana, mutta ihminen arvioi myös sen palautteen.

Tunnin tuotoksessa pitää näkyä ennen–jälkeen-ero, omat korjaukset ja niiden perusteet. Valmis teksti yksin ei osoita työparitaitoa.

> **Lopuksi pohdittavaksi:** Mikä lopputuloksessa on parempaa juuri sinun päätöksesi vuoksi — ja mistä toinen ihminen voi sen nähdä?

---

## Lähteet ja tarkistuspäivä

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

Tarkistettu 20.7.2026.
