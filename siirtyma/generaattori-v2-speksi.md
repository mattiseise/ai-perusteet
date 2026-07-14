# Generaattori v2 — arkkitehtuurispeksi (vaihe 2)

*Fable-suunnittelu 14.7.2026 · toteutus Opus-subagentilla · pohjana
RAKENNEUUDISTUS-2-NAKYMAT.md (vaiheet 2–3) ja HANDOFF-RAKENNEUUDISTUS-2.md.*

## Tavoite

`generate_site.py` tuottaa yhden 3,3 Mt:n index.html:n sijaan monisivuisen
staattisen sivuston kolmella näkymällä. Lähteet: `sisalto/` (kurssi.yaml +
tunnit/NN + lopputyot). Deploy-malli ei muutu: generoidut sivut committoidaan
repoon, Netlify julkaisee repojuuren.

## Tuotettavat sivut (repojuureen)

```
index.html                       Hash-redirect + valintasivu (3 ovea)
kurssi/index.html                Verkkokurssin yleiskuva (hero, edistyminen, 3 moduulikorttia)
kurssi/<slug>/index.html         Moduulisivut (teoria|kaytto|agentit): intro + tuntilista + lopputyölinkki
kurssi/tunti-NN/index.html       27 kpl: Teoria → Harjoittele → Sanasto
kurssi/<slug>/lopputyo/index.html  3 kpl (verkko-varianttilohkot)
luokka/index.html                Tuntilista moduuleittain + lopputyölinkit
luokka/tunti-NN/index.html       27 kpl: Teoria → Tehtävät → Harjoittele → Sanasto → Diat
luokka/<slug>/lopputyo/index.html  3 kpl (luokka-variantti)
opettaja/index.html              Kurssiopas (sisalto/opettaja/kurssiopas.md jos on; muuten
                                 siisti runko: kurssirakenne + tuntilinkit + arviointi-linkki
                                 + "kurssiopas täydentyy" -laatikko) — vaihe 4 tuo sisällön
opettaja/tunti-NN/index.html     27 kpl: Tuntisuunnitelma → Opettajavetoiset tehtävät → Diat
                                 (esitystila) + "Jaa tämä tunti opiskelijoille" (kopioi
                                 /luokka/tunti-NN/-linkin) + linkkirivi tunnin opiskelija-
                                 materiaaleihin (osoittavat /luokka/-näkymään)
opettaja/arviointi/index.html    Lopputöiden arviointiosiot koottuna (3 briefiä) +
                                 tunnin 18 arviointiohje (sisalto/tunnit/18/opettaja/arviointiohje.md)
sanasto/index.html               Koko kurssin sanasto aakkostettuna (SEO); jokaisen termin
                                 perässä linkki /kurssi/tunti-NN/#sanasto
assets/site.css                  Yhteinen CSS (nykyisestä f-string-CSS:stä)
assets/site.js                   Yhteinen JS (edistyminen, tabit, consent/GA, näkymävaihtaja)
assets/practice.js               Harjoittele-moottori (nykyinen PRACTICE_JS sellaisenaan)
_redirects                       Netlify-redirectit (polkumuodot)
sitemap.xml                      Kaikki julkiset sivut, https://aiperusteet.fi/...
robots.txt                       Allow all + Sitemap-osoitin
```

Tuntisivut ovat välilehtisivuja: näkymän kaikki lohkot yhdessä HTML:ssä,
välilehdet client-side. Ankkuri `#harjoittele|#sanasto|#tehtavat|#diat|#teoria`
valitsee välilehden (redirect-taulukko nojaa näihin!).

## Koodirakenne

- Entry point säilyy: `python3 generate_site.py`.
- Saa (ja kannattaa) jakaa paketiksi, esim. `generator/`-kansio:
  `sisalto.py` (luku+markdown+varianttilohkot+task-parseri), `nakymat.py`
  (näkymäkokoonpano kurssi.yaml:sta), `sivut.py` (sivupohjat), `assets.py`.
  generate_site.py jää ohueksi käynnistimeksi.
- Jinja2:ta EI oteta käyttöön (ei uusia riippuvuuksia; markdown + pyyaml riittävät).
  F-string-ansat: ks. CLAUDE.md — kirjaimelliset `{{ }}`, esc_js, `</`→`<\/`.
- Nykyisestä generaattorista SIIRRETÄÄN sellaisenaan: to_html-putki
  (mermaid-stash, tehtäväkortit, pause-laatikot ym.), PRACTICE_CSS/JS,
  parse_practice, esc_js, deck-wrap-rakenne, consent/GA-lohko, fontit,
  mermaid-CDN + initialize-config.

## Säilytettävät sopimukset (EI SAA MUUTTUA)

1. **localStorage:** `bcai-new` = JSON-lista id:itä `lesson-NN`;
   `bcai-practice` = objekti avaimin `lesson-NN/<taskIndex>` (prKey);
   `bcai-consent`; `bcai-reflect` (säilytä nykyinen muoto — katso koodista).
   Tehtäväjärjestys per tunti ei saa muuttua (indeksi on avain).
2. **GA4:** G-4ZLJF4THGV, loadGA/consentChoice-logiikka sama, tapahtumat
   `lesson_open`, `lesson_complete`, `task_start`, `task_complete` samoilla
   parametreilla + UUSI parametri `view: 'kurssi'|'luokka'|'opettaja'`
   jokaiseen tapahtumaan. lesson_open laukeaa tuntisivun latauksessa.
3. **Tunti-id:t** `lesson-NN` GA:ssa ja localStoragessa; URLeissa `tunti-NN`.
4. Diaesitys: nykyinen deck-wrap + koko näyttö -nappi; opettajan
   esitystila = sama deck isompana oletuksena (ei uutta teknologiaa).

## Näkymäsäännöt

- Näkymien lohkot ja järjestys luetaan `sisalto/kurssi.yaml`:n `nakymat`-osasta
  — EI kovakoodata sivupohjiin.
- Välilehtinimet: kurssi: Teoria · Harjoittele · Sanasto; luokka: Teoria ·
  Tehtävät · Harjoittele · Sanasto · Diat; opettaja: Tuntisuunnitelma ·
  Opettajavetoiset tehtävät · Diat. Arviointitunneilla (block_type
  assessment, tunnit 18 ja 27) Teoria-välilehden nimi on "Arviointitehtävä"
  eikä Harjoittele-välilehteä ole (harjoittele.md puuttuu). Puuttuva lohko
  jätetään pois välilehdistä (ei tyhjää paneelia).
- **Kesto:** kurssi-näkymässä "Lukuaika n. X min" (teoria+sanasto-sanamäärä
  / 200 sanaa/min, pyöristys ylös 5 minuutin tarkkuuteen); luokka/opettaja:
  "90 min oppitunti". Arviointitunnin badge "★ Arviointi" säilyy.
- **Kehystys:** kurssi-näkymässä EI OSP-puhetta eikä oppilaitoskehystä
  (ei "3 OSP", ei "oppitunti N/27" — käytä "Osa N/27"). OSP-kieli vain
  /opettaja/-sivuilla. Luokkanäkymässä "Oppitunti N".
- **Kriittinen (hyväksymiskriteeri d):** /kurssi/- ja /luokka/-sivuilla ei
  saa olla YHTÄÄN linkkiä /opettaja/-polkuun eikä opettajamateriaalisisältöä.
  Näkymävaihtaja opiskelijasivuilla tarjoaa vain Verkkokurssi ↔ Luokkaversio.
  Vain / (valintasivu) ja /opettaja/-sivut linkittävät opettajanäkymään.
- Näkymävaihtaja headerissa: vaihtaa saman tunnin toiseen näkymään;
  tallentaa valinnan localStorage-avaimeen `bcai-view` (uusi avain, sallittu).
  Valintasivu korostaa muistettua ovea, EI ohjaa automaattisesti.
- Navigointi tuntisivulla: murupolku (näkymän etusivu › moduuli › tunti),
  Edellinen/Seuraava samassa näkymässä, "Merkitse suoritetuksi" kurssi- ja
  luokkanäkymissä (sama toggleDone-logiikka), ei opettajanäkymässä.

## Varianttilohkot

Markdown-tiedostoissa mekanismi:

```
::: verkko
...vain verkkokurssiin...
:::
::: luokka
...vain luokkaversioon...
:::
::: opettaja
...vain opettajan oppaaseen...
:::
```

Parseri suodattaa lohkot ENNEN markdown-muunnosta: näkymän
`lopputyo_variantti` (kurssi.yaml) kertoo mikä variantti pidetään; muut
poistetaan; merkitsemätön sisältö näkyy kaikissa. Sisäkkäisiä ei tarvitse
tukea (virhe buildissa jos avaamaton `:::`). Vaiheen 2 lopussa yksikään
sisältötiedosto ei vielä käytä variantteja — parseri testataan
yksikkötestillä (esim. pieni pytest- tai assert-pohjainen testitiedosto
`siirtyma/testit/`-kansioon).

## Etusivu (valintasivu) ja hash-redirect

- index.html alkuun inline-skripti ENNEN sisällön renderöintiä: jos
  `location.hash` täsmää `siirtyma/redirectit.md`-taulukkoon →
  `location.replace(uusi)`. Taulukko generoidaan datana kurssi.yaml:sta
  (NN-silmukka), ei käsin. Tuntematon hash → näytä valintasivu.
- Valintasivu: kurssin nimi + 1–2 kappaleen esittely + kolme ovea:
  "Opiskele itsenäisesti" (ensisijainen CTA → /kurssi/), "Olemme
  oppitunnilla" (→ /luokka/), "Olen opettaja" (→ /opettaja/).
  Ei materiaalityyppiselitettä (poistetaan kokonaan).
- Consent-banneri + GA myös valintasivulla (redirect tapahtuu ennen GA-latausta).

## Poistettava kuollut koodi

- `SLIDE_URLS`, `REVIEW_SLIDE_URL` (Google Slides -legacy; deck tulee aina
  diat.html:stä), materiaalityyppiselite (`legend-*`), hash-SPA-reititys
  (routeFromHash/loadLesson/showTab datablobeineen `L={...}`), BRIEFS-blob.

## Hyväksymiskriteerit (todennettava, raportoi jokainen)

a. Jokainen generoitu HTML-sivu < 400 kt.
b. `node --check` läpäisee jokaisen sivun inline-skriptit (pura script-tagit
   väliaikaistiedostoihin) ja assets/*.js:n.
c. sitemap.xml generoituu ja kattaa kaikki julkiset sivut.
d. `grep -rl "/opettaja" kurssi/ luokka/` palauttaa tyhjän; kurssi/luokka-
   sivuilla ei esiinny tuntisuunnitelma- eikä opettajavetoiset-sisältöä.
e. Redirect-testi: node-skripti (siirtyma/testit/) joka evaluoi index.html:n
   hash-mappauksen jokaiselle redirectit.md-taulukon vanhalle osoitteelle
   (27 tuntia × kaikki tabit + briefit + tuntematon) ja vertaa odotettuun.
f. Edistymis-avaimet: kurssi- ja luokkatuntisivujen JS lukee/kirjoittaa
   `bcai-new`-listaa id-muodolla `lesson-NN` ja practice käyttää prKey-muotoa
   `lesson-NN/<idx>` — todenna generoidusta HTML:stä/JS:stä grepillä.
g. 112 harjoittelutehtävää: task-widgetien määrä /kurssi/tunti-*-sivuilla
   yhteensä 112 ja /luokka/tunti-*-sivuilla 112.
h. `python3 generate_site.py` ajaa puhtaasti; kaikki sivut syntyvät (määrä:
   1 + 1+3+27+3 (kurssi) + 1+27+3 (luokka) + 1+27+1 (opettaja) + 1 sanasto = 96 HTML-sivua).

## Työtapa

- Committaa pienissä erissä suomeksi (esim. 1) sisältöputki+parserit,
  2) sivupohjat+assets, 3) kurssi-näkymä, 4) luokka+opettaja, 5) etusivu+
  redirectit+sitemap, 6) kuolleen koodin poisto + kriteeriajot).
- Vanha index.html korvautuu vasta kun uusi kokonaisuus generoituu —
  generaattorin vanhaa yksisivutuotantoa ei tarvitse säilyttää rinnalla.
- ÄLÄ muuta sisältötiedostoja (sisalto/**) tässä vaiheessa lainkaan.
- ÄLÄ pushaa. Työ jää haaraan rakenneuudistus-2.
