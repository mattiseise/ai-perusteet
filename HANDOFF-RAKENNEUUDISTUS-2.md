# Handoff: Rakenneuudistus 2 — toteutus

*Toimeksianto Claude Codelle · 14.7.2026 · tila hyväksytty, baseline-commit cc2372b*

## Missio

Toteuta `RAKENNEUUDISTUS-2-NAKYMAT.md`:n hyväksytty suunnitelma: nykyisestä yhden tiedoston sivustosta tehdään monisivuinen, kolmen näkymän kokonaisuus (**/kurssi**, **/luokka**, **/opettaja**) yhdestä sisältöpohjasta. Lue suunnitelma kokonaan ennen aloitusta — se sisältää analyysin, sivukartan (vaihe 3) ja siirtymämappauksen (vaihe 4). Tämä dokumentti antaa toteutusjärjestyksen, hyväksymiskriteerit ja päätökset, joita ei neuvotella uudelleen.

## Lukitut päätökset (älä avaa uudelleen)

1. Kolme näkymää, ei kahta eikä yhtä. Näkymät ovat saman sisältögraafin suodattimia.
2. Yksi sisältöpohja: eroavat kohdat varianttilohkoina (`::: verkko` / `::: luokka` / `::: opettaja`) saman tiedoston sisällä — ei koskaan rinnakkaistiedostoja.
3. Monisivuinen staattinen generointi (sivu per tunti per näkymä) — yhden index.html:n malli poistuu.
4. Vanhat hash-linkit ohjataan uusiin osoitteisiin (suunnitelman 4.4-taulukko); Itslearningiin jaetut linkit eivät saa katketa.
5. localStorage-avaimet ja GA-mittaus säilyvät (ks. CLAUDE.md); GA-tapahtumiin lisätään `view`-dimensio (kurssi/luokka/opettaja).
6. Luokkatehtäviä (student-tasks) EI kirjoiteta uusiksi — ne siirtyvät luokkanäkymään sellaisinaan. Uudelleenkirjoituslista on suppea ja täsmällinen (suunnitelman 4.3): 2 pistekohtaa teoriateksteissä, 3 lopputyöbriefin palautus-/arviointiosiot varianteiksi, arviointituntien 18 ja 27 verkkokehystys.

## Toteutusjärjestys

Tee vaiheet järjestyksessä; jokainen päättyy commitiin ja tarkistuslistaan. Työskentele feature-haarassa `rakenneuudistus-2` — **älä pushaa mainiin kesken työn** (Netlify vie mainin suoraan tuotantoon). Netlifyn branch deploy / deploy preview kelpaa betaksi (suunnitelman vaihe 5).

### Vaihe 0 — Inventaario ja jäädytys
- `diff -r content/lessons/ student/` -henkinen vertailu: varmista ettei content/lessons sisällä mitään, mikä puuttuu student-puolelta (self-studyt ovat ajautuneet — student on uudempi). Jos yksittäinen kohta on legacy-puolella parempi, poimi se talteen ennen poistoa.
- Poista content/lessons/, LESSONS-21-25-INDEX.md, preview-lesson-01.html. Päivitä README kuvaamaan todellinen lähdehierarkia.
- Lukitse redirect-taulukko: kerää generaattorista kaikki hash-muodot ja kirjaa lopullinen vanha→uusi-taulukko tiedostoon `siirtyma/redirectit.md`.
- Hyväksymiskriteeri: `python3 generate_site.py` tuottaa identtisen sivuston (diff tyhjä index.html:lle) — vaihe 0 ei muuta mitään käyttäjälle.

### Vaihe 1 — Lähdepohjan siirto
- `git mv` uuteen rakenteeseen (suunnitelman 3.2): `sisalto/tunnit/NN/{teoria,sanasto,harjoittele,tehtavat-luokka}.md`, `diat.html`, `opettaja/{tuntisuunnitelma,tehtavat-ohjatut}.md`, `sisalto/lopputyot/*.md`. Säilytä git-historia (mv, ei copy).
- Luo `sisalto/kurssi.yaml`: moduulit, tunnit, otsikot, block_type, näkymäkonfiguraatiot (mitkä lohkot missäkin näkymässä — suunnitelman 2.2-taulukko datana).
- Päivitä generaattori lukemaan uusista poluista (tässä vaiheessa yhä vanha yhden sivun tuotanto — ei toiminnallista muutosta).
- Hyväksymiskriteeri: sivusto generoituu ja on sisällöltään identtinen; kaikki 112 task-JSONia parsiutuvat.

### Vaihe 2 — Generaattori v2
- Monisivuinen tuotanto: `/kurssi/tunti-NN/`, `/luokka/tunti-NN/`, `/opettaja/tunti-NN/`, moduulisivut, etusivu-suuntaaja, `/sanasto/`-koonti, lopputyösivut per näkymä.
- Varianttilohkojen parseri (`::: verkko` jne.), lukuaika sanamäärästä /kurssi-näkymään ("~90 min" vain luokka/opettaja), GA `view`-dimensio, consent + practice-moottori sivupohjaan, hash-redirect-sivu + Netlify `_redirects`.
- Poista kuollut koodi (SLIDE_URLS, materiaalityyppiselite).
- Hyväksymiskriteerit: (a) jokainen generoitu sivu < 400 kt; (b) `node --check` läpi jokaisen sivun skripteille; (c) sitemap.xml generoituu; (d) /luokka- ja /kurssi-sivuilla ei ole yhtään linkkiä opettajamateriaaliin; (e) redirect-testit: jokainen 4.4-taulukon vanha osoite päätyy oikealle sivulle; (f) localStorage-edistyminen luettavissa uusilla sivuilla (sama avain, sama id-muoto).

### Vaihe 3 — Sisältövariantit (portitettu sisältötyö)
- Lopputyöbriefien verkkovariantit: palautus/arviointi → itsearviointikriteerit (johda nykyisistä pistekriteereistä, älä keksi uusia). Tunti-17 ja tunti-27 pistekorjaukset, arviointituntien verkkokehystys.
- Aja CLAUDE.md:n sisältötyötavalla: suunnittelu → rakentaminen → pedagoginen tarkistusportti → kielenhuolto. Käytä subagentteja (Task tool); pedagoginen portti antaa eksplisiittisen HYVÄKSYTTY/KORJATTAVA-päätöksen ennen integrointia.
- Hyväksymiskriteeri: verkkonäkymässä ei ole yhtään mainintaa Itslearningistä, palautuksesta opettajalle tai pisteistä (grep-todennus).

### Vaihe 4 — Opettajan kurssiopas
- Uusi `sisalto/opettaja/kurssiopas.md`: toteutusmallit (3 OSP, 27 × 90 min jaksotus), arviointi (lopputyöt + kriteerit koottuna), Itslearning-vienti, diat/pptx-lataamo, lisenssi. Lähteet: README, lopputyöbriefit, teacher-materials-tiedostojen yhteiset rakenteet.
- Sama portitettu työtapa kuin vaiheessa 3.

### Vaihe 5 — Beta ja julkaisu
- Branch deploy Netlifyyn; läpiklikkaustestit kolmessa näkymässä (vähintään: tunti 1, 19 ja yksi lopputyö per näkymä; yksi practice-tehtävä loppuun asti → task_complete näkyy GA:ssa view-dimensiolla).
- Kerro Matille beta-URL ja odota hyväksyntä ennen mainiin mergeä. Julkaisun jälkeen: Search Console -sivukartta.

## Työtapa

- Committaa pienissä erissä, viestit suomeksi. Jokaisen vaiheen lopuksi: mitä tehtiin, mitkä kriteerit todennettiin, mitä jäi auki.
- Kun kosket generaattoriin, lue ensin CLAUDE.md:n ansat (f-string-tuplasulkeet, esc_js, assessment-haara).
- Älä muuta opetussisällön merkitystä missään siirto- tai muotoiluvaiheessa — jos siirto vaatii tekstimuutoksen, joka ei ole 4.3-listalla, kirjaa se ja kysy ennen toteutusta.
- Epäselvässä kohdassa suunnitelmadokumentti voittaa tämän handoffin, ja Matti voittaa molemmat.

## Definition of done (koko projekti)

1. Kolme näkymää tuotannossa, etusivu suuntaa, näkymävaihtaja toimii.
2. Yksikään 4.4-taulukon vanha linkki ei anna 404:ää.
3. Kävijän edistyminen ja tehtävätulokset säilyivät (localStorage-avaimet ennallaan).
4. GA raportoi tapahtumat view-dimensiolla; consent-banneri toimii kuten ennen.
5. /kurssi-näkymä on Itslearning- ja opettajaviittauksista puhdas (grep-todennus).
6. Lähdepuussa ei ole enää content/lessons-kopiota eikä kuollutta koodia; README ja CLAUDE.md vastaavat todellisuutta.
7. Kaikki 112 harjoittelutehtävää toimivat kaikissa opiskelijanäkymissä.
