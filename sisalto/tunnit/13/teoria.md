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

## 1. Pyydä pohja, älä lopullista totuutta

Ensimmäinen versio voi olla rakenne, luonnos tai vaihtoehtojen lista. Kerro tekoälylle:

- mitä olet tekemässä
- kenelle lopputulos on tarkoitettu
- mitä lähdeaineistoa pitää käyttää
- missä muodossa pohja tarvitaan
- mitä asioita ei saa keksiä

Esimerkiksi käyttöohjeen ensimmäinen pohja voi sisältää otsikot ja työvaiheet. Se ei vielä ole julkaistava ohje. Sen tehtävä on antaa jotakin, jota voit arvioida ja muokata.

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

## 3. Tee itse olennaiset päätökset

Tekoäly voi ehdottaa, mutta se ei tunne tavoitettasi yhtä hyvin kuin sinä. Päätä itse ainakin:

- mitä sisältöä poistetaan tai lisätään
- mihin järjestykseen asiat asetetaan
- mikä sävy sopii tilanteeseen
- mitkä väitteet pitää tarkistaa lähteestä
- milloin luonnos hylätään kokonaan

Kaikkea ei tarvitse pelastaa. Jos luonnos perustuu väärään oletukseen, uusi rajattu prompti voi olla järkevämpi kuin pitkän tekstin paikkaaminen.

## 4. Käytä tekoälyä testilukijana

Kun olet tehnyt oman version, anna tekoälylle rajattu tarkistusrooli. Älä pyydä ”parantamaan kaikkea”, vaan etsi nimettyä ongelmaa:

- löydä kohta, jossa aloittelija voi eksyä
- osoita termi, jota ei ole selitetty
- etsi väite, jolle lähteessä ei ole tukea
- tarkista, etenevätkö vaiheet oikeassa järjestyksessä

Pyydä havainto ja kysymys, älä valmista uudelleenkirjoitusta. Näin sinä säilytät päätösvallan.

## 5. Tarkista tarkistajan ehdotus

Tekoälyn palaute voi olla väärä, epäolennainen tai tyyliltään huono. Jokaisesta ehdotuksesta päätetään:

- hyväksyn
- muokkaan
- hylkään

Kirjaa ainakin yksi hylätty ehdotus ja sen peruste. Kriittinen työparuus näkyy myös siinä, mitä et ota mukaan.

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
