"""Näkymäkokoonpano: lukee kurssi.yaml-manifestin ja rakentaa näkymät (kurssi/luokka/
opettaja) saman sisältögraafin suodattimina. Lohkot, järjestys ja variantit tulevat
manifestista — ei kovakoodata sivupohjiin.
"""

import os
import re
import yaml

from . import sisalto

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_HERE)
SISALTO = os.path.join(ROOT, 'sisalto')

with open(os.path.join(SISALTO, 'kurssi.yaml'), encoding='utf-8') as _f:
    KURSSI = yaml.safe_load(_f)

# ---- Moduulit / tunnit ----
MODUULIT = KURSSI['moduulit']

# Lyhyt mono-tunniste moduulikorteille ("01 · TEORIA"). Slug → näyttönimi.
_KN_NAME = {'teoria': 'TEORIA', 'kaytto': 'KÄYTTÖ', 'agentit': 'AGENTIT'}

OSP_BLOCKS = [
    {
        'id': m['id'],
        'slug': m['slug'],
        'title': m['otsikko'],
        'subtitle': m['alaotsikko'],
        'color': m['vari'],
        'icon': m['ikoni'],
        'ikoni_kn': f"{i:02d} · {_KN_NAME.get(m['slug'], m['slug'].upper())}",
        'lopputyo': m.get('lopputyo'),
        'lessons': [(t['id'], t['otsikko'], t['tyyppi'], t['kansio']) for t in m['tunnit']],
    }
    for i, m in enumerate(MODUULIT, 1)
]

ALL_LESSONS = [
    {'id': t['id'], 'kansio': t['kansio'], 'otsikko': t['otsikko'], 'tyyppi': t['tyyppi'],
     'lopputyon_askel': t.get('lopputyon_askel'),
     'osp_id': m['id'], 'slug': m['slug'], 'osp_title': m['otsikko'],
     'osp_color': m['vari'], 'osp_icon': m['ikoni']}
    for m in MODUULIT for t in m['tunnit']
]
ALL_IDS = [l['id'] for l in ALL_LESSONS]

# ---- Näkymäkonfiguraatiot ----
NAKYMAT = KURSSI['nakymat']   # kurssi / luokka / opettaja
VARIANTTI = {name: cfg['lopputyo_variantti'] for name, cfg in NAKYMAT.items()}

# ---- Lohkosopimus ----
BLOCK_FILE = {
    'teoria': 'teoria.md',
    'sanasto': 'sanasto.md',
    'harjoittele': 'harjoittele.md',
    'tehtavat-luokka': 'tehtavat-luokka.md',
    'lopputyon-askel': 'tehtavat-luokka.md',   # osatuotos-osio poimitaan tästä
    'diat': 'diat.html',
    'tuntisuunnitelma': 'opettaja/tuntisuunnitelma.md',
    'tehtavat-ohjatut': 'opettaja/tehtavat-ohjatut.md',
}

BLOCK_ANCHOR = {
    'teoria': 'teoria',
    'harjoittele': 'harjoittele',
    'sanasto': 'sanasto',
    'tehtavat-luokka': 'tehtavat',
    'lopputyon-askel': 'lopputyon-askel',
    'diat': 'diat',
    'tuntisuunnitelma': 'tuntisuunnitelma',
    'tehtavat-ohjatut': 'ohjatut',
}

BLOCK_LABEL = {
    'teoria': 'Teoria',
    'harjoittele': 'Harjoittele',
    'sanasto': 'Sanasto',
    'tehtavat-luokka': 'Tehtävät',
    'lopputyon-askel': '★ Lopputyön askel',
    'diat': 'Diat',
    'tuntisuunnitelma': 'Tuntisuunnitelma',
    'tehtavat-ohjatut': 'Opettajavetoiset tehtävät',
}

# Ikonit tab-napeille (Konsoli-lukija, ei emojia) — siirretty v1:n TABICONS-kartasta.
BLOCK_ICON = {
    'teoria': '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M8 4.2C8 3.3 6.8 2.5 4.8 2.5 3.2 2.5 2 3 2 3v9s1.2-.5 2.8-.5S8 12.2 8 13M8 4.2C8 3.3 9.2 2.5 11.2 2.5 12.8 2.5 14 3 14 3v9s-1.2-.5-2.8-.5S8 12.2 8 13M8 4.2V13"/></svg>',
    'tehtavat-luokka': '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><path d="M6.5 4H14M6.5 8H14M6.5 12H14M2 4l.9.9L4.6 3M2 8l.9.9L4.6 7M2 12l.9.9L4.6 11"/></svg>',
    'harjoittele': '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="8" cy="8" r="6"/><circle cx="8" cy="8" r="3"/><circle cx="8" cy="8" r=".9" fill="currentColor" stroke="none"/></svg>',
    'sanasto': '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M3 3.5A1.5 1.5 0 014.5 2H13v9.5H4.5A1.5 1.5 0 003 13V3.5z"/><path d="M3 13a1.5 1.5 0 011.5-1.5H13V14H4.5A1.5 1.5 0 013 12.5"/></svg>',
    'lopputyon-askel': '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M8 1.8l1.9 3.85 4.25.62-3.07 3 .72 4.23L8 11.5 4.27 13.5l.72-4.23-3.07-3 4.25-.62z"/></svg>',
    'diat': '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="1.5" y="2.5" width="13" height="9" rx="1.5"/><path d="M8 11.5V14M5.5 14h5" stroke-linecap="round"/></svg>',
    'tuntisuunnitelma': '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><rect x="3" y="3" width="10" height="11" rx="1.5"/><path d="M6 3.2V2.2h4v1M6 7h4M6 10h2.5" stroke-linecap="round"/></svg>',
    'tehtavat-ohjatut': '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="5.8" cy="5" r="2.1"/><path d="M2.5 13c0-2 1.5-3.2 3.3-3.2S9.1 11 9.1 13" stroke-linecap="round"/><path d="M10.6 3.5A2 2 0 0113 5.4a2 2 0 01-1.3 1.9M11 9.9c1.5.3 2.5 1.5 2.5 3.1" stroke-linecap="round"/></svg>',
}


def lesson_dir(kansio):
    return os.path.join(SISALTO, 'tunnit', kansio)


# --- Diojen SVG-semantiikka: informatiiviselle role="img" + <title>, tekstittömälle aria-hidden ---
_SVG_OPEN_RE = re.compile(r'<svg\b[^>]*>')
_SVG_TEXT_RE = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
_SVG_FS_RE = re.compile(r'font-size="([0-9.]+)"')
_SVG_TAG_RE = re.compile(r'<[^>]+>')


def _slide_title(svg_body):
    """Poimi dian otsikko: suurimman font-sizen <text>-sisältö (tspanit litistetty)."""
    best, best_fs = None, -1.0
    for m in _SVG_TEXT_RE.finditer(svg_body):
        fs_m = _SVG_FS_RE.search(m.group(1))
        fs = float(fs_m.group(1)) if fs_m else 0.0
        txt = ' '.join(_SVG_TAG_RE.sub(' ', m.group(2)).split())
        if txt and fs > best_fs:
            best, best_fs = txt, fs
    return best


def _annotate_deck_svgs(deck_src):
    """Lisää jokaiseen dia-SVG:hen saavutettavuussemantiikka (role + <title>).

    Diat ovat käsin ladottua SVG:tä ilman semantiikkaa; ruudunlukijalle
    absoluuttisesti sijoitetut tekstinpätkät ovat sekava lukujärjestys, joten
    dia nimetään otsikollaan ja sisältö vastaa oppitunnin leipätekstiä.
    """
    parts = deck_src.split('</svg>')
    total = len(parts) - 1 if len(parts) > 1 else 0
    out = []
    num = 0
    for part in parts:
        m = _SVG_OPEN_RE.search(part)
        if m is None or 'role=' in m.group(0) or 'aria-hidden' in m.group(0):
            out.append(part)
            continue
        num += 1
        open_tag, body = m.group(0), part[m.end():]
        title = _slide_title(body)
        if title:
            new_open = (open_tag[:-1] + ' role="img">'
                        + f'<title>Dia {num}/{total}: {title}</title>')
        else:
            new_open = open_tag[:-1] + ' aria-hidden="true">'
        out.append(part[:m.start()] + new_open + body)
    return '</svg>'.join(out)


def _deck_html(deck_src):
    return (
        '<div class="deck-wrap">'
        '<div class="deck-bar"><span class="deck-hint">Diaesitys — vieritä tai pyyhkäise sivuttain →</span>'
        '<button class="deck-full-btn" type="button" aria-label="Avaa diaesitys koko näytön tilaan" '
        'onclick="deckFull(this)">⛶ Koko näyttö</button></div>'
        '<div class="deck">' + _annotate_deck_svgs(deck_src) + '</div>'
        '</div>'
    )


def render_block(kansio, block, variant, lid, lopputyon_askel=None):
    """Renderöi yksi lohko yhtä näkymää varten.

    Palauttaa dictin {'html', 'tasks'} tai None jos lähdetiedosto puuttuu/tyhjä.
    """
    ldir = lesson_dir(kansio)
    fname = BLOCK_FILE[block]
    raw = sisalto.read_file(os.path.join(ldir, fname))
    if not raw.strip():
        return None
    source = f"tunnit/{kansio}/{fname}"

    if block == 'diat':
        return {'html': _deck_html(raw), 'tasks': None}

    if block == 'lopputyon-askel':
        # Välilehti syntyy vain tunneille, joilla manifestikenttä on. Osatuotos-osio
        # poimitaan raa'asta tekstistä (otsikko osuu alkuperäiseen luokkatekstiin) ja
        # suodatetaan sitten näkymän variantilla (kurssi = verkko).
        if not lopputyon_askel:
            return None
        section = sisalto.extract_lopputyo_section(raw, lopputyon_askel, source=source)
        filtered = sisalto.filter_variants(section, variant, source=source)
        return {'html': sisalto.to_html_with_cards(filtered, include_h3=False), 'tasks': None}

    filtered = sisalto.filter_variants(raw, variant, source=source)

    if block == 'harjoittele':
        html, tasks = sisalto.parse_practice(filtered, lid)
        if not tasks and not html.strip():
            return None
        return {'html': html, 'tasks': tasks}
    if block in ('tehtavat-luokka', 'tehtavat-ohjatut'):
        return {'html': sisalto.to_html_with_cards(filtered, include_h3=False), 'tasks': None}
    if block == 'tuntisuunnitelma':
        return {'html': sisalto.to_html_with_cards(filtered, include_h3=True), 'tasks': None}
    # teoria, sanasto
    html = sisalto.to_html(filtered)
    if block == 'teoria':
        html = sisalto.annotate_demos(html, lid)
    return {'html': html, 'tasks': None}


def tab_label(block, is_assessment):
    """Välilehden nimi. Arviointitunneilla teoria → 'Arviointitehtävä'."""
    if is_assessment and block == 'teoria':
        return 'Arviointitehtävä'
    return BLOCK_LABEL[block]


def build_lesson_blocks(lesson, view):
    """Rakentaa yhden tunnin näytettävät lohkot yhdessä näkymässä.

    Palauttaa listan dictejä: {block, anchor, label, icon, html, tasks}
    Puuttuvat lohkot jätetään pois. Arviointitunnilta harjoittele puuttuu (ei tiedostoa).
    """
    cfg = NAKYMAT[view]
    variant = cfg['lopputyo_variantti']
    is_assessment = lesson['tyyppi'] == 'assessment'
    out = []
    for block in cfg['lohkot']:
        rendered = render_block(lesson['kansio'], block, variant, lesson['id'],
                                lopputyon_askel=lesson.get('lopputyon_askel'))
        if rendered is None:
            continue
        out.append({
            'block': block,
            'anchor': BLOCK_ANCHOR[block],
            'label': tab_label(block, is_assessment),
            'icon': BLOCK_ICON.get(block, ''),
            'html': rendered['html'],
            'tasks': rendered['tasks'],
        })
    return out


def lopputyo_html(osp, view):
    """Lopputyöbriefin HTML yhdelle näkymälle (varianttisuodatettu)."""
    fname = osp.get('lopputyo')
    if not fname:
        return ''
    raw = sisalto.read_file(os.path.join(SISALTO, fname))
    if not raw.strip():
        return ''
    variant = VARIANTTI[view]
    filtered = sisalto.filter_variants(raw, variant, source=fname)
    return sisalto.to_html(filtered)
