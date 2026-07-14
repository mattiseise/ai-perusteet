# Uudelleenohjaukset: vanhat hash-osoitteet → uudet sivut

*Lukittu vaiheessa 0 (rakenneuudistus 2) · 14.7.2026 · lähde: generate_site.py:n reititys (routeFromHash, loadLesson, showTab, loadBrief) baseline-commitissa cc2372b.*

Tämä taulukko on siirtymän sopimus: jokainen tähän kirjattu vanha osoite ohjataan
uuteen osoitteeseen, eikä yksikään saa antaa 404:ää. Linkkejä on jaettu
Itslearning-kursseihin, joten kattavuus todennetaan vaiheen 2 redirect-testeissä
(hyväksymiskriteeri 2e) ja ennen julkaisua (definition of done, kohta 2).

## Vanhan sivuston kaikki osoitemuodot

Yhden sivun sovellus reitittää hashilla. Generaattorista kerätyt muodot:

| Muoto | Syntyy | Huomiot |
|---|---|---|
| `/` (ei hashia) | etusivu | |
| `#lesson-NN` | tunnin avaus (oletusvälilehti) | NN = 01–27; oletusvälilehti oli Diat jos diat on, muuten Itseopiskelu |
| `#lesson-NN/slides` | Diat-välilehti | vain showTab kirjoittaa muodon `#lesson-NN` ilman tabia myös slides/selfstudy-tabeille, mutta vanhoja `/slides`-linkkejä voi olla manuaalisesti jaettuna |
| `#lesson-NN/selfstudy` | Itseopiskelu-välilehti | sama huomio kuin yllä |
| `#lesson-NN/stasks` | Opiskelutehtävät | arviointitunneilla (18, 27) nimellä "Tehtävä" |
| `#lesson-NN/practice` | Harjoittele | ei arviointitunneilla |
| `#lesson-NN/vocab` | Sanasto | ei arviointitunneilla |
| `#lesson-NN/tltasks` | Opettajavetoiset tehtävät | ei arviointitunneilla |
| `#lesson-NN/tmats` | Opettajan materiaali | arviointitunneilla "Opettajan opas" |
| `#brief-osp1` `#brief-osp2` `#brief-osp3` | lopputyön tehtävänanto | |
| tuntematon hash | reititys palautti etusivun | säilytetään sama käyttäytyminen |

## Lukittu ohjaustaulukko (vanha → uusi)

| Vanha | Uusi | Peruste |
|---|---|---|
| `/` (hash-etusivu) | `/` (valintasivu) | suunnitelma 4.4 |
| `/#lesson-NN` | `/kurssi/tunti-NN/` | suunnitelma 4.4 |
| `/#lesson-NN/selfstudy` | `/kurssi/tunti-NN/` | teoria on kurssinäkymän ydin |
| `/#lesson-NN/practice` | `/kurssi/tunti-NN/#harjoittele` | suunnitelma 4.4 |
| `/#lesson-NN/vocab` | `/kurssi/tunti-NN/#sanasto` | sanasto on kurssinäkymässä |
| `/#lesson-NN/stasks` | `/luokka/tunti-NN/#tehtavat` | suunnitelma 4.4 |
| `/#lesson-NN/slides` | `/luokka/tunti-NN/#diat` | diat-linkkejä jaetaan luokalle; opettajalla on oma esitystila |
| `/#lesson-NN/tltasks` | `/opettaja/tunti-NN/` | suunnitelma 4.4 |
| `/#lesson-NN/tmats` | `/opettaja/tunti-NN/` | suunnitelma 4.4 |
| `/#brief-osp1` | `/kurssi/teoria/lopputyo/` | suunnitelma 4.4 (`/kurssi/<osp>/lopputyo/`) |
| `/#brief-osp2` | `/kurssi/kaytto/lopputyo/` | — " — |
| `/#brief-osp3` | `/kurssi/agentit/lopputyo/` | — " — |
| tuntematon hash | `/` | vastaa vanhaa käyttäytymistä |

NN käy läpi arvot 01–27 kaikissa riveissä. Arviointituntien (18, 27) hash-muodot
ovat samat kuin opetustuntien; niiltä ei ole koskaan syntynyt `/practice`-,
`/vocab`- eikä `/tltasks`-osoitteita, mutta jos sellainen linkki jostain tulee,
se ohjataan kuten tuntematon tab: `/kurssi/tunti-NN/`.

Yleissääntö tuntemattomalle tabille: `/#lesson-NN/<mikä tahansa muu>` → `/kurssi/tunti-NN/`.

## Toteutus (vaihe 2)

Kaksi kerrosta, koska hash ei koskaan välity palvelimelle:

1. **Kevyt ohjaussivu** vanhassa osoitteessa `/index.html`: lukee `location.hash`in,
   kääntää sen tämän taulukon mukaan ja tekee `location.replace(...)`. Ilman hashia
   näyttää uuden valintasivun (tai ohjaa siihen).
2. **Netlify `_redirects`** polkumuotoisille osoitteille ja varalle
   (esim. mahdolliset `/index.html`-suorat linkit → `/`).

Huomiot toteuttajalle:

- Ankkurit (`#harjoittele`, `#sanasto`, `#tehtavat`, `#diat`) ovat uusien sivujen
  sisäisiä ankkureita/välilehtivalintoja — uuden sivupohjan pitää tukea niitä.
- Suunta on aina opiskelijanäkymään päin: vanhoja opettajamateriaalilinkkejä
  (`tltasks`, `tmats`) EI ohjata opiskelijanäkymiin vaan `/opettaja/`-polulle.
- GA: ohjaussivu ei lataa GA:ta (ei consent-tarvetta, välitön replace).
