"""Sisältöputki: tiedostojen luku, markdown-muunnos, varianttilohkot, task-parseri.

Siirretty sellaisenaan generate_site.py:n v1-versiosta (to_html-putki, task-kortit,
pause-laatikot, mermaid-stash, parse_practice, esc_js) + uudet varianttilohko- ja
lukuaika-apurit rakenneuudistus 2:ta varten.
"""

import os
import re
import json
from html.parser import HTMLParser
import markdown as md_lib

MD_EXTENSIONS = ['tables', 'fenced_code', 'nl2br']


def read_file(path):
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return f.read()
    return ''


# ===== Varianttilohkot (::: verkko / ::: luokka / ::: opettaja) =====
# Suodatetaan ENNEN markdown-muunnosta. Näkymän variantti pidetään, muut poistetaan;
# merkitsemätön sisältö näkyy kaikissa. Sisäkkäisiä ei tueta (avaamaton ::: = buildivirhe).

VARIANT_NAMES = {'verkko', 'luokka', 'opettaja'}
_FENCE_RE = re.compile(r'^:::[ \t]*([A-Za-z0-9_-]*)[ \t]*$')


def filter_variants(text, variant, source='?'):
    """Pidä vain annettua varianttia vastaavat ::: -lohkot; poista muut.

    variant: 'verkko' | 'luokka' | 'opettaja' tai lista niitä (näkymän
    lopputyo_variantti; opettaja näkee sekä luokka- että opettaja-lohkot).
    Merkitsemätön (fenceton) sisältö säilyy aina.
    Avaamaton tai tuntematon fence kaataa buildin (SystemExit).
    """
    variants = {variant} if isinstance(variant, str) else set(variant)
    if ':::' not in text:
        return text
    out = []
    in_block = False
    keep = False
    block_name = None
    for i, line in enumerate(text.split('\n'), 1):
        m = _FENCE_RE.match(line.strip())
        if m is not None and (not in_block or m.group(1) == ''):
            name = m.group(1)
            if not in_block:
                # avaava fence — nimi vaaditaan
                if name == '':
                    raise SystemExit(
                        f"VIRHE: {source} rivi {i}: sulkeva ':::' ilman avausta.")
                if name not in VARIANT_NAMES:
                    raise SystemExit(
                        f"VIRHE: {source} rivi {i}: tuntematon varianttinimi '{name}' "
                        f"(sallitut: {', '.join(sorted(VARIANT_NAMES))}).")
                in_block = True
                block_name = name
                keep = (name in variants)
                continue
            else:
                # sulkeva fence
                in_block = False
                block_name = None
                keep = False
                continue
        if in_block:
            if keep:
                out.append(line)
        else:
            out.append(line)
    if in_block:
        raise SystemExit(
            f"VIRHE: {source}: avaamaton varianttilohko ':::' {block_name!r} "
            f"jäi sulkematta.")
    return '\n'.join(out)


# ===== Lopputyön askel: osatuotos-osion poiminta tehtavat-luokka.md:stä =====
# Verkkokurssinäkymä nostaa lopputyön osatuotostehtävän omaksi välilehdeksi. Osio
# tunnistetaan kurssi.yaml:n lopputyon_askel-kentästä: '*' = koko tiedosto, muuten
# h2-otsikon (osa)teksti. Poiminta tapahtuu ENNEN varianttisuodatusta, jotta manifestin
# otsikko osuu alkuperäiseen (luokka)tekstiin.

def extract_lopputyo_section(text, heading, source='?'):
    """Palauta lopputyön askel -osio. heading == '*' (tai None) → koko tiedosto.

    Muuten palautetaan se h2-osio, jonka otsikko sisältää annetun merkkijonon:
    otsikkorivistä seuraavaan h2-otsikkoon (tai tiedoston loppuun). Otsikkorivi on
    mukana; perässä roikkuvat tyhjät rivit ja '---'-erottimet siivotaan. Jos otsikkoa
    ei löydy, build kaatuu (tarkoituksella — sama malli kuin muualla putkessa).
    """
    if not heading or heading == '*':
        return text
    lines = text.split('\n')
    start = None
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith('## ') and heading in s[3:]:
            start = i
            break
    if start is None:
        raise SystemExit(
            f"VIRHE: {source}: lopputyön askel -otsikkoa '{heading}' ei löytynyt "
            f"(tarkista kurssi.yaml:n lopputyon_askel-kenttä).")
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].strip().startswith('## '):
            end = j
            break
    section = lines[start:end]
    while section and (not section[-1].strip() or section[-1].strip() == '---'):
        section.pop()
    # Luokan tehtävätaksonomia (🟢 SUOSITELTU / 🟣 SYVENTÄVÄ) ei kuulu verkko-
    # opiskelijan otsikkoon — askel on lopputyön pakollinen osa, ei valinnainen.
    section[0] = re.sub(r'\s*(🟢\s*SUOSITELTU|🟣\s*SYVENTÄVÄ)\s*$', '', section[0])
    return '\n'.join(section)


# ===== Markdown → HTML (siirretty v1:stä sellaisenaan) =====

def to_html(text):
    if not text:
        return '<p><em>(Tiedostoa ei löydy)</em></p>'
    mermaid_blocks = []

    def _stash_mermaid(m):
        idx = len(mermaid_blocks)
        mermaid_blocks.append(m.group(1).strip())
        return f'MERMAID_PLACEHOLDER_{idx}'
    text = re.sub(r'```mermaid\s*\n(.*?)```', _stash_mermaid, text, flags=re.DOTALL)

    # Muunna vain lainaamattomat, kokonaisella rivillä olevat Pysähdy-kehotukset.
    # Valmiiksi muodossa ``> **Pysähdy hetkeksi:** ...`` oleva rivi jätetään
    # koskematta, jotta to_html() on idempotentti eikä synnytä sisäkkäisiä lainauksia.
    text = re.sub(
        r'^(?![ \t]*>)[ \t]*\*\*Pysähdy hetkeksi:\*\*[ \t]*(.*?)\s*$',
        r'> **Pysähdy hetkeksi:** \1', text, flags=re.MULTILINE)
    text = re.sub(
        r'^(?![ \t]*>)[ \t]*Pysähdy hetkeksi:[ \t]*(.*?)\s*$',
        r'> **Pysähdy hetkeksi:** \1', text, flags=re.MULTILINE)
    h = md_lib.markdown(text, extensions=MD_EXTENSIONS)
    h = re.sub(r'<blockquote>\s*<p>', '<blockquote class="pause"><p>', h)
    h = re.sub(r'<p><strong>Jos teet tehtävän yksin',
               '<p class="solo-note"><strong>Jos teet tehtävän yksin', h)
    h = re.sub(r'<h2>(Tehtävä \d+[\.\-]\d+.*?)</h2>',
               r'<h2 class="task-header">\1</h2>', h)

    for i, block in enumerate(mermaid_blocks):
        h = h.replace(f'MERMAID_PLACEHOLDER_{i}',
                      f'<div class="mermaid">\n{block}\n</div>')
        h = h.replace(f'<p>MERMAID_PLACEHOLDER_{i}</p>',
                      f'<div class="mermaid">\n{block}\n</div>')
    return h


def to_html_with_cards(text, include_h3=False):
    """markdown → HTML + tehtävä-/osiokortit (student-tasks, teacher-led, teacher-materials)."""
    h = to_html(text)
    return _wrap_task_cards(h, include_h3=include_h3)


TASK_BLOCK_RE = re.compile(r'```task\s*\n(.*?)\n```', re.S)


def parse_practice(text, lid='?'):
    """practice/harjoittele.md: markdown + ```task JSON-lohkot → (html, tasks).

    Jokainen task-lohko korvautuu <div class="task-widget" data-ti="N"></div>-paikalla,
    ja JSON kerätään listaan. Virheelliseen JSONiin kaadutaan (tarkoituksella).
    """
    if not text.strip():
        return '', []
    tasks = []

    def _repl(m):
        try:
            tasks.append(json.loads(m.group(1)))
        except json.JSONDecodeError as e:
            raise SystemExit(f"VIRHE: {lid}/harjoittele.md task-lohkon JSON ei jäsenny: {e}")
        return f'\n\n<div class="task-widget" data-ti="{len(tasks)-1}"></div>\n\n'
    md_text = TASK_BLOCK_RE.sub(_repl, text)
    return to_html(md_text), tasks


def _classify_heading(title):
    title_lower = title.lower()
    if any(w in title_lower for w in ['väärinkäsitys', 'osaamistavoite', 'osaamistavoitteet',
                                      'cfu-kysym', 'cfu kysym', 'yleisi', 'yleiset']):
        return 'info'
    if any(w in title_lower for w in ['pisteet', 'arviointi', 'odotettu tuotos']):
        return 'assessment'
    if any(w in title_lower for w in ['lisäresurss', 'lisämateriaali', 'resurss']):
        return 'resource'
    return 'task'


def _wrap_task_cards(html, include_h3=False):
    htags = 'h[23]' if include_h3 else 'h2'
    heading_re = re.compile(rf'<({htags})[^>]*>(.*?)</\1>')
    _SKIP_HEADINGS = {'Tehtävät', 'Opiskelutehtävät', 'Sanasto'}

    parts = []
    last_end = 0
    in_card = False

    for m in heading_re.finditer(html):
        tag = m.group(1)
        title = m.group(2)
        title_text = re.sub(r'<[^>]+>', '', title).strip()
        if title_text in _SKIP_HEADINGS:
            continue
        if len(title_text) < 4:
            continue
        ct = _classify_heading(title_text)
        if in_card:
            content_before = html[last_end:m.start()]
            content_before = re.sub(r'\s*<hr\s*/?\s*>\s*$', '', content_before)
            parts.append(content_before)
            parts.append('</div></div>')
        else:
            content_before = html[last_end:m.start()]
            content_before = re.sub(r'\s*<hr\s*/?\s*>\s*$', '', content_before)
            parts.append(content_before)
        size_cls = ' task-card--sm' if tag == 'h3' else ''
        parts.append(f'<div class="task-card task-card--{ct}{size_cls}">')
        parts.append(f'<div class="task-card-header"><{tag}>{title}</{tag}></div>')
        parts.append('<div class="task-card-body">')
        in_card = True
        last_end = m.end()

    if in_card:
        remaining = html[last_end:]
        remaining = re.sub(r'\s*<hr\s*/?\s*>\s*$', '', remaining)
        parts.append(remaining)
        parts.append('</div></div>')
    else:
        parts.append(html[last_end:])
    return ''.join(parts)


def esc_js(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


def esc_attr(s):
    """HTML-attribuutin escapetus (breadcrumb-linkit, alt-tekstit yms.)."""
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;'))


# Staattisten konseptikuvioiden puhelinversiot. Jokainen malli säilyttää kyseisen
# työpöytäkuvion olennaisen suhteen (virta, vertailu, silmukka tai suojakerrokset)
# luettavana HTML:nä ilman 560 px koordinaatistoa.
_DEMO_MOBILE_MODELS = {
    'lesson-01-01': ('compare', ['SÄÄNTÖ: yksi euromääräraja → iso siirto hälyttää, outo pieni siirto pääsee läpi',
                                 'OPITTU MALLI: useita painotettuja signaaleja → molemmat poikkeamat ylittävät kynnyksen']),
    'lesson-02-01': ('compare', ['SÄÄNTÖ: ihminen kirjoittaa ehdon — jos summa ylittää rajan → tarkistus',
                                 'OPITTU MALLI: esimerkkidata → malli → arvio uudesta tapauksesta',
                                 'Sääntöpohjainen järjestelmä ei välttämättä ole tekoälyä']),
    'lesson-02-02': ('compare', ['KÄYTÖSSÄ NYT: sääntöpohjainen · kapea · generatiivinen — kapea ja generatiivinen voivat olla sama järjestelmä',
                                 'TULEVAISUUSPUHE: AGI (ei hyväksyttyä nykyesimerkkiä) · ASI (hypoteettinen)',
                                 'Sujuva teksti ei ylitä nykyisyyden rajaa — käsitteet eivät ole kehitysaskelmia']),
    'lesson-03-01': ('loop', ['Syöte ja tähänastinen teksti', 'Laske seuraavien tokenien todennäköisyydet',
                              'Valitse tokeni', 'Liitä tekstiin', 'Toista, kunnes vastaus päättyy']),
    'lesson-04-01': ('compare', ['ILMAN KONTEKSTIA: sama pyyntö → monta mahdollista tulkintaa',
                                 'ROOLI + TAVOITE + RAJAUS → väärät tulkinnat karsiutuvat → osuvampi vastaus']),
    'lesson-05-01': ('flow', ['Keskustelu kasvaa', 'Konteksti-ikkuna täyttyy',
                              'Vanhin tieto putoaa ulos', 'Tiivistä tai anna olennainen tieto uudelleen']),
    'lesson-06-01': ('compare', ['TEHTÄVÄ 1 · tarkka muutos: kaaviosta arvio, taulukosta tarkka +44,4 % → piste taulukolle',
                              'TEHTÄVÄ 2 · harhaanjohtava asteikko: näkyy kaaviosta, ei taulukosta → piste kuvalle',
                              'Kumpikin muoto voitti kerran — muoto valitaan tehtävän mukaan']),
    'lesson-08-01': ('layers', ['Näkyvä AI-vastaus', 'Koulutusdata ja tekijöiden työ',
                                'Aineiston merkintä- ja ylläpitotyö', 'Energia, vesi ja laitteisto', 'Vastuu käytöstä']),
    'lesson-10-01': ('flow', ['1 · LUKITSE kriteerit ennen katselua: sisältö, rakenne, kieli',
                              '2 · PISTEYTÄ sokkona: A 3/3 · B 1/3 — merkit piilossa',
                              '3 · PALJASTA vasta lopuksi: A oli uusi, B tuttu — näyttö ratkaisi, ei merkki']),
    'lesson-11-01': ('compare', ['PILVIPALVELU: tiedosto ylittää verkon rajan — kopio voi säilyä, tarkista ehdot',
                              'ORGANISAATION PALVELU: ylittää rajan — sopimus ja ohjeet määrittävät',
                              'PAIKALLINEN AJO: ei ylitä rajaa — silti tarkista yhteydet ja päivitykset']),
    'lesson-12-01': ('flow', ['Kriteerit lukitaan ennen ajoa → V1: kaksi täyttyy, yksi ei (keksityt määräajat)',
                              'Täsmälleen yksi nimetty muutos korttiin — muut rivit ennallaan',
                              'V2 samalla aineistolla: juuri se kriteeri kääntyy → ero on muutoksen ansiota']),
    'lesson-13-01': ('flow', ['POHJA: sinä annat tavoitteen ja aineiston, AI tuottaa luonnoksen',
                              'MUOKKAUS + TARKISTUS: näkyvät muutokset, ehdotuksista 1 hyväksytty ja 1 hylätty perustellen',
                              'PÄÄTÖS: ihminen päättää — työn jälki -loki näyttää jokaisen vaiheen tekijän']),
    'lesson-14-01': ('flow', ['Sumea idea → mittatikku: käyttäjä tarvitsee apua tehtävään, jotta lopputulos',
                              '”Auttaa hyvin?” hylätään → havaittava kriteeri: vastaus löytyy tietopohjasta',
                              'Rajakysymys ohjataan yhteyshenkilölle — määrittely valmis ennen promptia']),
    'lesson-15-01': ('compare', ['ILMAN ENNAKKO-ODOTUSTA: läpäisyehto siirtyy vastauksen luo → kaikki ”läpäisee”',
                              'LUKITTU ENNEN: sama vastaus jää vajaaksi → aukko paljastuu',
                              'Hylkäys on tietoa — vain lukittu odotus paljastaa aukon']),
    'lesson-16-01': ('loop', ['Sama sykli joka välineellä: tavoite → versio → arvio → 1 muutos → versio 2',
                              'Kuva, ääni ja koodi: eri havainto, silti täsmälleen yksi nimetty muutos',
                              'Loki kerää havainnon ja muutoksen — väline vaihtuu, sykli ei']),
    'lesson-17-01': ('flow', ['Promptipankin tyyli', 'Botin tarkoitus ja rajat', 'Hyväksytty tietopohja',
                              'Yhdistä järjestelmäpromptiksi', 'Aja testi → kirjaa korjaus']),
    'lesson-19-01': ('compare', ['CHATBOT: kertoo vaiheet tekstinä → työ jää käyttäjälle',
                                 'AGENTTI = kielimalli + harness → käyttää rajattuja työkaluja → raportoi toiminnan']),
    'lesson-20-01': ('branch', ['RUTIINI: työnkulku nopein ja halvin — promptaus sitoo sinut, agentin joka ajo maksaa',
                              'POIKKEUS: työnkulku jumittuu ilman sääntöä — agentti arvioi ja ratkaisee tai ohjaa ihmiselle',
                              'Väline valitaan tehtävävirran vaihtelun mukaan — monimutkaisempi ei ole automaattisesti parempi']),
    'lesson-21-01': ('layers', ['KONTEKSTI-IKKUNA: näkee vain viimeisimmät viestit — vanhin putoaa pois',
                              'VEKTORITIETOKANTA: harness hakee merkityksellä palan ikkunaan — eri sanat, sama merkitys',
                              'TILA: vaihe ja yritysmäärä säilyvät — ikkuna unohtaa, tila muistaa. Periaatteet eivät ole muistia']),
    'lesson-22-01': ('flow', ['Käyttäjän tarve', 'Agentti valitsee sallitun työkalun',
                              'Rakenteinen kutsu ja minimioikeudet', 'Työkalu palauttaa tuloksen tai virheen', 'Agentti vastaa tuloksen perusteella']),
    'lesson-23-01': ('loop', ['Lyhyt päätösperustelu', 'Rakenteinen työkalukutsu', 'Havainto tai virhe',
                              'Tieto riittää? kyllä → valmis; ei → uusi rajattu vaihe', 'Lokiin kutsut, tulokset, toiminnot ja virheet']),
    'lesson-24-02': ('layers', ['Ulkoinen sisältö = epäluotettava data', 'Rakenteinen työkalurajapinta',
                                'Minimioikeudet ja salaisuuksien eristys', 'Kriittisen toiminnon hyväksyntäportti', 'Tarkistettava loki ja palautuminen']),
    'lesson-25-01': ('branch', ['Rutiini + pieni vaikutus → sallittu automaatio',
                                'Kriittinen toiminto → hyväksyntäportti', 'Hyväksy → toteuta ja lokita',
                                'Hylkää tai aikakatkaisu → peruuta tai käytä turvallista fallbackia']),
    'lesson-26-01': ('flow', ['Triggeri käynnistää', 'Agenttisolmu arvioi seuraavan rajatun vaiheen',
                              'Työkalu tekee yhden asian', 'Tulos tai virhe palaa', 'Loki + lopputulos / eskalointi']),
}


def annotate_demos(html, lid):
    """Lisää kaikille konseptikuvioille yhteinen responsiivinen sopimus.

    Vanhojen kuvioiden kuviokohtainen piirroskoodi säilyy lähteessä, mutta
    generoitu HTML saa yksilöivän id:n, tyypin ja yhteiset osaluokat.
    """
    if 'ai-demo' not in html:
        return html
    counter = 0

    def figure(match):
        nonlocal counter
        counter += 1
        demo_id = f'{lid}-{counter:02d}'
        interactive = (lid == 'lesson-07' or
                       (lid == 'lesson-20' and counter == 2) or
                       (lid == 'lesson-24' and counter == 1))
        kind = 'interactive' if interactive else 'static'
        return (f'<figure class="ai-demo" data-demo-id="{demo_id}" '
                f'data-demo-kind="{kind}">')

    html = re.sub(r'<figure class="ai-demo">', figure, html)
    html = html.replace('class="ai-demo__tag"', 'class="ai-demo__tag ai-demo__title"')

    def stage(match):
        opening = match.group(0)
        before = html[:match.start()]
        figure_start = before.rfind('<figure class="ai-demo"')
        header = before[figure_start:] if figure_start >= 0 else ''
        part = ('ai-demo__interaction' if 'data-demo-kind="interactive"' in header
                else 'ai-demo__viewport')
        return opening.replace('ai-demo__stage', f'ai-demo__stage {part}', 1)

    html = re.sub(r'<div class="ai-demo__stage"[^>]*>', stage, html)

    def add_mobile_model(match):
        figure_html = match.group(0)
        id_match = re.search(r'data-demo-id="([^"]+)"', figure_html)
        if not id_match or id_match.group(1) not in _DEMO_MOBILE_MODELS:
            return figure_html
        demo_id = id_match.group(1)
        relation, nodes = _DEMO_MOBILE_MODELS[demo_id]
        rendered_nodes = [f'<li class="ai-demo__mobile-node">{node}</li>' for node in nodes]
        mobile = (
            f'<div class="ai-demo__mobile-model ai-demo__mobile-model--{relation}">'
            '<span class="ai-demo__mobile-kicker">KUVION MOBIILIESITYS</span>'
            f'<ol class="ai-demo__mobile-steps">{"".join(rendered_nodes)}</ol></div>')
        return re.sub(r'(<div class="ai-demo__stage ai-demo__viewport"[^>]*>)',
                      r'\1' + mobile, figure_html, count=1)

    html = re.sub(
        r'<figure class="ai-demo" data-demo-id="[^"]+" data-demo-kind="static">.*?</figure>',
        add_mobile_model, html, flags=re.DOTALL)
    return html


# ===== Lukuaika (kurssi-näkymän kesto) =====

class _VisibleTextParser(HTMLParser):
    """Poimi renderöidystä HTML:stä lukijalle näkyvä teksti.

    Demoissa näkyvä kuvateksti lasketaan, mutta niiden käyttöliittymä, SVG,
    tyylit ja skriptit eivät kasvata lukuaikaa.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self._ignored = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set(attrs.get('class', '').split())
        ignore = bool(self._ignored) or tag in {'style', 'script', 'svg'}
        if 'ai-demo__stage' in classes or 'ai-demo__interaction' in classes:
            ignore = True
        self._ignored.append(ignore)

    def handle_startendtag(self, tag, attrs):
        return

    def handle_endtag(self, tag):
        if self._ignored:
            self._ignored.pop()

    def handle_data(self, data):
        if not any(self._ignored):
            self.parts.append(data)


def visible_text(text):
    """Renderöi Markdown ja palauta vain näkyvä lukuteksti."""
    if not text:
        return ''
    parser = _VisibleTextParser()
    parser.feed(to_html(text))
    return re.sub(r'\s+', ' ', ' '.join(parser.parts)).strip()


def word_count(text):
    return len(visible_text(text).split())


# ===== Meta-description-poiminta (SEO: teorian ensimmäinen leipätekstikappale) =====

def excerpt(text, maxlen=160):
    """Poimii ensimmäisen leipätekstikappaleen tiiviiksi meta descriptioniksi.

    Ohittaa otsikot (#), listat, lainaukset ja taulukot; poistaa markdown-korostukset
    ja linkit; katkaisee sanarajalle (~maxlen merkkiä) ja lisää katkoviivan (…).
    """
    if not text:
        return ''
    para = []
    for line in text.split('\n'):
        s = line.strip()
        if not s:
            if para:
                break              # ensimmäinen kappale päättyi
            continue
        if s.startswith(('#', ':::', '>', '|', '- ', '* ', '+ ')) or _re_list.match(s):
            if para:
                break
            continue               # ohita otsikot/listat kappaleen alussa
        para.append(s)
    p = ' '.join(para)
    p = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', p)   # [teksti](url) → teksti
    p = re.sub(r'[*_`]', '', p)                       # korostukset pois
    p = re.sub(r'\s+', ' ', p).strip()
    if len(p) <= maxlen:
        return p
    cut = p[:maxlen].rsplit(' ', 1)[0].rstrip(' ,.;:—-')
    return cut + '…'


_re_list = re.compile(r'^\d+[.)]\s')


def reading_time_min(*texts, wpm=200):
    """Sanamäärä yhteensä / wpm, pyöristys ylös 5 minuutin tarkkuuteen (väh. 5)."""
    words = sum(word_count(t) for t in texts if t)
    import math
    mins = math.ceil(words / wpm) if words else 0
    rounded = int(math.ceil(mins / 5.0) * 5)
    return max(rounded, 5)
