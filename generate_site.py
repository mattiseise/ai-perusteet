#!/usr/bin/env python3
"""Generate full course website for ai-perusteet-1ov
Completely redesigned with Codecademy-inspired vertical layout, expandable accordions, and paper background."""

import os, json, re
import markdown as md_lib

_HERE = os.path.dirname(os.path.abspath(__file__))
BASE = _HERE
OUT  = os.path.join(_HERE, 'index.html')

# Lopputyön tehtävänannot per OSP (osp_id → md filename relative to repo root)
LOPPUTYO_BRIEFS = {
    "osp1": "teoria-lopputyo-tehtavananto.md",
    "osp2": "tekoalyjen-kaytto-lopputyo-tehtavananto.md",
    "osp3": "agentit-lopputyo-tehtavananto.md",
}

OSP_BLOCKS = [
    {
        "id": "osp1",
        "title": "Teoria",
        "subtitle": "Tekoälyn teoria ja toimintaperiaatteet",
        "color": "var(--blue)",
        "icon": "📐",
        "lessons": [
            ("lesson-01", "Älykäs vai sääntö? — mitä tekoäly oikeasti tekee", "teaching"),
            ("lesson-02", "Viisi tekoälyn tasoa — missä mennään ja mihin ollaan menossa", "teaching"),
            ("lesson-03", "Miten kone kirjoittaa? — generatiivisen AI:n mekaniikka", "teaching"),
            ("lesson-04", "Konteksti ratkaisee — miksi sama kysymys antaa eri vastauksen", "teaching"),
            ("lesson-05", "Muistin rajat — kuinka paljon tekoäly oikeasti muistaa", "teaching"),
            ("lesson-06", "Kuvat, ääni ja teksti — kun sanat eivät riitä", "teaching"),
            ("lesson-07", "Miksi tekoäly valehtelee? — hallusinaatiot ja satunnaisuus", "teaching"),
            ("lesson-08", "Kenen teksti se on? — etiikka, oikeudet ja vastuu", "teaching"),
            ("lesson-09", "Tuomaripöydän päätös — asiantuntijalausunto tekoälystä", "teaching"),
        ]
    },
    {
        "id": "osp2",
        "title": "Tekoälyjen käyttö",
        "subtitle": "Generatiivisten tekoälytyökalujen käyttö",
        "color": "var(--violet)",
        "icon": "🛠",
        "lessons": [
            ("lesson-10", "Kilpailuta tekoälyt — mikä työkalu mihinkin?", "teaching"),
            ("lesson-11", "Muita tekoälymalleja — kuin ChatGPT ja Claude", "teaching"),
            ("lesson-12", "Anna konteksti — rakenna oma promptauspankkisi", "teaching"),
            ("lesson-13", "AI työparina — pohja, muokkaus ja tarkistus", "teaching"),
            ("lesson-14", "Oma botti I — suunnittelu, ohjeet ja persoona", "teaching"),
            ("lesson-15", "Oma botti II — tietopohja, rajaukset ja testaus", "teaching"),
            ("lesson-16", "Tekoälytyökalut erikoisaloilla — kuva, musiikki, video ja koodi", "teaching"),
            ("lesson-17", "Projektidokumenttibotti — suunnittele ja aloita rakentaminen", "teaching"),
            ("lesson-18", "Projektidokumenttibotti — viimeistele ja esittele", "assessment"),
        ]
    },
    {
        "id": "osp3",
        "title": "Agentit",
        "subtitle": "Tekoälyagentit ja automaatio",
        "color": "var(--teal)",
        "icon": "🤖",
        "lessons": [
            ("lesson-19", "Boteista agentteihin — mikä muuttuu kun AI toimii itsenäisesti", "teaching"),
            ("lesson-20", "Automaatio vai autonomia? — milloin agentti kannattaa", "teaching"),
            ("lesson-21", "Agentin muisti ja konteksti — miten kone pysyy kartalla", "teaching"),
            ("lesson-22", "Agentin työkalut — tiedostot, haku ja komennot", "teaching"),
            ("lesson-23", "Suunnittelumallit — ReAct, ketjuajattelu ja orkestrointi", "teaching"),
            ("lesson-24", "Turvallisuus ensin — hyökkäykset, suojaukset ja lokitus", "teaching"),
            ("lesson-25", "Ihminen portinvartijana — human-in-the-loop käytännössä", "teaching"),
            ("lesson-26", "Kädet saveen — n8n-agenttipaja alkaa", "teaching"),
            ("lesson-27", "Viimeistele ja esittele — agenttisi on valmis", "assessment"),
        ]
    }
]

# Google Slides embed URLs per lesson (None = no slides for this lesson)
SLIDE_URLS = {
    "intro":     "https://docs.google.com/presentation/d/1wFcG2PM71QAN3IgFCxdMj8zZAK2Q2iGpEkW1O_sn4W0/embed?start=false&loop=false&delayms=3000",
    "lesson-01": "https://docs.google.com/presentation/d/1bWogMlO8ip24mjXfZ6vDAqXngFsAOcLy5dJ0bwZR_mA/embed?start=false&loop=false&delayms=3000",
    "lesson-02": "https://docs.google.com/presentation/d/14QH5M5HHObUlFZ_kFbmcNiNWn916HlyW10Q0kQmkTMk/embed?start=false&loop=false&delayms=3000",
    "lesson-03": "https://docs.google.com/presentation/d/18JiTuqSbkvTHbjkgmak1t4Yi6FFpws4OiQY7OlUx-VQ/embed?start=false&loop=false&delayms=3000",
    "lesson-04": "https://docs.google.com/presentation/d/1AYtG5_qN8i-peKPteaKjViK12pL9pbhVVXTRABou_P8/embed?start=false&loop=false&delayms=3000",
    "lesson-05": "https://docs.google.com/presentation/d/1hWZhtcmZrzBsIz5OxD7Khjz73GDI0wIzs78neRQTT0w/embed?start=false&loop=false&delayms=3000",
    "lesson-06": "https://docs.google.com/presentation/d/1X8X3CC9JTTkdcfZPtxuHhHCF19F6Ye3QusvphjPhzog/embed?start=false&loop=false&delayms=3000",
    "lesson-07": "https://docs.google.com/presentation/d/1NqzZSCOLQiz9eo_lZKa-_VjEmeU3MFFNgVWTiHQ_x-8/embed?start=false&loop=false&delayms=3000",
    "lesson-08": "https://docs.google.com/presentation/d/1Juoruyp1kibxlQyMreH_jDljSjFtasiTF2DvISpTZG4/embed?start=false&loop=false&delayms=3000",
    "lesson-09": "https://docs.google.com/presentation/d/1HEHaQTA_iUfOVaRwiGe_nbjDlJTi8AqE8NPJeLhOJPE/embed?start=false&loop=false&delayms=3000",
    "lesson-10": "https://docs.google.com/presentation/d/1O3_d4Mxtw9lFCxFbvg1MGq764388HcZK9HZuB-t_9VM/embed?start=false&loop=false&delayms=3000",
    "lesson-11": "https://docs.google.com/presentation/d/1F_flMJrYp_3NNtc30GfZyPyc06y9sURS_rQWpOKUIRA/embed?start=false&loop=false&delayms=3000",
    "lesson-12": None,  # Anna konteksti — puuttuu
    "lesson-13": "https://docs.google.com/presentation/d/1vnW47D7Sf50Kkrfr8S5ZWERv04krZ1RrSfdR2LPT7zk/embed?start=false&loop=false&delayms=3000",
    "lesson-14": "https://docs.google.com/presentation/d/1ftouC0GjjHegb3v0hHGFCJP8jEKGgDnAN5s2FFYML4I/embed?start=false&loop=false&delayms=3000",
    "lesson-15": "https://docs.google.com/presentation/d/1Hoif5gNFdzchpWgD1XRe_Dqa3lH5ANt8vnng0qifOYE/embed?start=false&loop=false&delayms=3000",
    "lesson-16": "https://docs.google.com/presentation/d/1MoRLKjy-Jje8wH6OPiasB3Rea0MIUNwNoGyup7N45bk/embed?start=false&loop=false&delayms=3000",
    "lesson-17": "https://docs.google.com/presentation/d/1Fg4VffcQVKhjoqd8FPKTfFVoQ7GZPa2Ro71lKJzwNk0/embed?start=false&loop=false&delayms=3000",
    "lesson-18": "https://docs.google.com/presentation/d/1g2kf-efRceTe4Ddfi0K5GP1Dgfr6f-WRFYbmJ4or1SQ/embed?start=false&loop=false&delayms=3000",
    "lesson-19": "https://docs.google.com/presentation/d/1Hd-UPJb4Kq1jTob8ZELAWOvyqVI73VzhbHn1vJtK3kc/embed?start=false&loop=false&delayms=3000",
    "lesson-20": "https://docs.google.com/presentation/d/1Z6R08URnRqV90ZilaxAOKZQmNjJzt83VV3SFUAyeGY0/embed?start=false&loop=false&delayms=3000",
    "lesson-21": "https://docs.google.com/presentation/d/1qESN1GJVfxoxmctns0hZtLjBbQppfC8NVWYpaMMFqUY/embed?start=false&loop=false&delayms=3000",
    "lesson-22": "https://docs.google.com/presentation/d/1uDG8qf8Vt6HV9a3v_sbtSzHOkappvvjzPywGNvYPA3Q/embed?start=false&loop=false&delayms=3000",
    "lesson-23": "https://docs.google.com/presentation/d/1uUElHRQ2s49QQRCyMl-Ut5nYOAGizhc4mfIW0feH2Qc/embed?start=false&loop=false&delayms=3000",
    "lesson-24": "https://docs.google.com/presentation/d/1m_NFiAz1ugEQ9tnYzADcJkE1SaubUJNKdGlfW5dz_TQ/embed?start=false&loop=false&delayms=3000",
    "lesson-25": "https://docs.google.com/presentation/d/1pIAbc7ljDWq7qRpsF3CMzVMqB5p3PbM_uH4IBkLCums/embed?start=false&loop=false&delayms=3000",
    "lesson-26": "https://docs.google.com/presentation/d/1AGsW7y5WyiGH5-5fgEchsya36cjLgIA7xmGBpyNdtI8/embed?start=false&loop=false&delayms=3000",
    "lesson-27": "https://docs.google.com/presentation/d/10g_dfNrEnFhVnV4ymbeGlAXv3oshjx-A8NoPja0bQW0/embed?start=false&loop=false&delayms=3000",
}

# Standalone review slides (shown on home page)
REVIEW_SLIDE_URL = "https://docs.google.com/presentation/d/1o2nKDyvDjkIYQtd3QUgB_z-X78iA92TQVxO7Lyk6Dqk/embed?start=false&loop=false&delayms=3000"

MD_EXTENSIONS = ['tables', 'fenced_code', 'nl2br']


def read_file(path):
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return f.read()
    return ''


def to_html(text):
    if not text:
        return '<p><em>(Tiedostoa ei löydy)</em></p>'
    # Convert mermaid fenced blocks to placeholder divs BEFORE markdown processing
    # This prevents fenced_code from turning them into <code> blocks
    mermaid_blocks = []
    def _stash_mermaid(m):
        idx = len(mermaid_blocks)
        mermaid_blocks.append(m.group(1).strip())
        return f'MERMAID_PLACEHOLDER_{idx}'
    text = re.sub(r'```mermaid\s*\n(.*?)```', _stash_mermaid, text, flags=re.DOTALL)

    text = re.sub(r'\*\*Pysähdy hetkeksi:(.*?)\*\*',
                  r'> **Pysähdy hetkeksi:\1**', text, flags=re.DOTALL)
    text = re.sub(r'^Pysähdy hetkeksi:(.*?)$',
                  r'> **Pysähdy hetkeksi:**\1', text, flags=re.MULTILINE)
    h = md_lib.markdown(text, extensions=MD_EXTENSIONS)
    h = re.sub(r'<blockquote>\s*<p>', '<blockquote class="pause"><p>', h)
    h = re.sub(r'<p><strong>Jos teet tehtävän yksin',
               '<p class="solo-note"><strong>Jos teet tehtävän yksin', h)
    h = re.sub(r'<h2>(Tehtävä \d+[\.\-]\d+.*?)</h2>',
               r'<h2 class="task-header">\1</h2>', h)

    # Restore mermaid blocks as <div class="mermaid"> elements
    for i, block in enumerate(mermaid_blocks):
        h = h.replace(f'MERMAID_PLACEHOLDER_{i}',
                       f'<div class="mermaid">\n{block}\n</div>')
        h = h.replace(f'<p>MERMAID_PLACEHOLDER_{i}</p>',
                       f'<div class="mermaid">\n{block}\n</div>')

    return h


def to_html_with_cards(text, include_h3=False):
    """Convert markdown to HTML and wrap task/section blocks in styled cards.
    Use ONLY for student-tasks, teacher-led-tasks, and teacher-materials panels.
    include_h3=True: also wrap h3-level sections as sub-cards (for teacher materials).
    include_h3=False: only wrap h2-level sections (for student/teacher-led tasks)."""
    h = to_html(text)
    return _wrap_task_cards(h, include_h3=include_h3)


def _classify_heading(title: str) -> str:
    """Determine card type from heading text."""
    title_lower = title.lower()
    if any(w in title_lower for w in ['väärinkäsitys', 'osaamistavoite', 'osaamistavoitteet',
                                       'cfu-kysym', 'cfu kysym', 'yleisi', 'yleiset']):
        return 'info'
    if any(w in title_lower for w in ['pisteet', 'arviointi', 'odotettu tuotos']):
        return 'assessment'
    if any(w in title_lower for w in ['lisäresurss', 'lisämateriaali', 'resurss']):
        return 'resource'
    return 'task'


def _wrap_task_cards(html: str, include_h3: bool = False) -> str:
    """Wrap each task/section block in a styled card div.

    include_h3=False: only h2 headings become cards (h3 stays inside the card body).
    include_h3=True:  both h2 and h3 headings become cards (for teacher materials).
    """

    htags = 'h[23]' if include_h3 else 'h2'
    heading_re = re.compile(
        rf'<({htags})[^>]*>(.*?)</\1>'
    )

    # Headings that should NOT become cards (too generic or are the page title)
    _SKIP_HEADINGS = {'Tehtävät', 'Opiskelutehtävät', 'Sanasto'}

    parts = []
    last_end = 0
    in_card = False

    for m in heading_re.finditer(html):
        tag = m.group(1)   # h2 or h3
        title = m.group(2)
        # Strip any inner HTML tags for classification
        title_text = re.sub(r'<[^>]+>', '', title).strip()

        # Skip page-level h1 (not matched anyway) and generic wrapper headings
        if title_text in _SKIP_HEADINGS:
            continue

        # Skip very short headings that are just labels (e.g. "Ohjeet")
        # But keep anything that looks like a real section
        if len(title_text) < 4:
            continue

        ct = _classify_heading(title_text)

        # For h3 inside an already-open h2 card: close the h2 card first
        # For h2 or h3: close previous card if open
        if in_card:
            content_before = html[last_end:m.start()]
            content_before = re.sub(r'\s*<hr\s*/?\s*>\s*$', '', content_before)
            parts.append(content_before)
            parts.append('</div></div>')  # close .task-card-body + .task-card

        else:
            content_before = html[last_end:m.start()]
            content_before = re.sub(r'\s*<hr\s*/?\s*>\s*$', '', content_before)
            parts.append(content_before)

        # h3 cards are slightly smaller (nested style)
        size_cls = ' task-card--sm' if tag == 'h3' else ''

        parts.append(f'<div class="task-card task-card--{ct}{size_cls}">')
        parts.append(f'<div class="task-card-header"><{tag}>{title}</{tag}></div>')
        parts.append('<div class="task-card-body">')

        in_card = True
        last_end = m.end()

    # Remaining content
    if in_card:
        remaining = html[last_end:]
        remaining = re.sub(r'\s*<hr\s*/?\s*>\s*$', '', remaining)
        parts.append(remaining)
        parts.append('</div></div>')
    else:
        parts.append(html[last_end:])

    return ''.join(parts)


def build_brief_data():
    """Read lopputyö tehtävänanto md files and convert to HTML keyed by osp_id."""
    briefs = {}
    for osp_id, fname in LOPPUTYO_BRIEFS.items():
        path = f"{BASE}/{fname}"
        if os.path.exists(path):
            briefs[osp_id] = to_html(read_file(path))
        else:
            briefs[osp_id] = ''
    return briefs


def build_lesson_data():
    data = {}
    for osp in OSP_BLOCKS:
        for lid, short_title, btype in osp['lessons']:
            sdir = f"{BASE}/student/{lid}"
            tdir = f"{BASE}/teacher/{lid}"
            slide_url = SLIDE_URLS.get(lid)
            deck_src = read_file(f"{sdir}/slides.html")
            slides_html = ''
            if deck_src.strip():
                slides_html = (
                    '<div class="deck-wrap">'
                    '<div class="deck-bar"><span class="deck-hint">Diaesitys — vieritä tai pyyhkäise sivuttain →</span>'
                    '<button class="deck-full-btn" type="button" onclick="deckFull(this)">⛶ Koko näyttö</button></div>'
                    '<div class="deck">' + deck_src + '</div>'
                    '</div>'
                )
            elif slide_url:
                slides_html = (
                    f'<div class="slides-container">'
                    f'<iframe src="{slide_url}" frameborder="0" '
                    f'width="100%" height="569" allowfullscreen="true" '
                    f'mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>'
                    f'</div>'
                )
            data[lid] = {
                'osp_id':        osp['id'],
                'osp_title':     osp['title'],
                'osp_color':     osp['color'],
                'osp_icon':      osp['icon'],
                'short_title':   short_title,
                'block_type':    btype,
                'slides':        slides_html,
                'selfstudy':     to_html(read_file(f"{sdir}/self-study.md")),
                'vocab':         to_html(read_file(f"{sdir}/vocabulary.md")),
                'stasks':        to_html_with_cards(read_file(f"{sdir}/student-tasks.md"), include_h3=False),
                'tltasks':       to_html_with_cards(read_file(f"{tdir}/teacher-led-tasks.md"), include_h3=False),
                'tmats':         to_html_with_cards(read_file(f"{tdir}/teacher-materials.md"), include_h3=True),
            }
    return data


def esc_js(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


# Animated track-icon SVGs + mono "NN · LABEL" eyebrows, keyed by OSP id.
OSP_ICONS = {
    "osp1": '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke="currentColor" stroke-width="2"><circle class="aic-ring" cx="24" cy="24" r="18"/><circle class="aic-ring" cx="24" cy="24" r="18"/><circle class="aic-ring" cx="24" cy="24" r="18"/></g><circle cx="24" cy="24" r="4.5" fill="currentColor"/></svg>',
    "osp2": '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><g stroke="currentColor" stroke-width="3" stroke-linecap="round"><line class="aic-line" x1="9" y1="16" x2="33" y2="16"/><line class="aic-line l2" x1="9" y1="24" x2="39" y2="24"/><line class="aic-line l3" x1="9" y1="32" x2="27" y2="32"/></g><rect class="aic-caret" x="41" y="11" width="3" height="26" rx="1.5" fill="currentColor"/></svg>',
    "osp3": '<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><circle class="aic-spin" cx="24" cy="24" r="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-dasharray="5 7" stroke-linecap="round"/><g class="aic-orbit"><circle cx="24" cy="8" r="3.8" fill="currentColor"/></g></svg>',
}
OSP_KN = {"osp1": "01 · TEORIA", "osp2": "02 · KÄYTTÖ", "osp3": "03 · AGENTIT"}


def generate_html(data, briefs):
    all_ids = [lid for osp in OSP_BLOCKS for lid, _, _ in osp['lessons']]

    # Build OSP accordion cards for home page
    osp_cards_html = ''
    for osp in OSP_BLOCKS:
        lessons_in_osp = osp['lessons']
        lessons_html = ''
        # Lopputyön tehtävänanto button at the top of each OSP (if brief exists)
        if briefs.get(osp['id']):
            lessons_html += f'''      <button class="acc-lesson acc-brief" onclick="loadBrief('{osp['id']}')">
        <span class="acc-l-num">★</span>
        <span class="acc-l-title">Lopputyön tehtävänanto</span>
        <span class="acc-l-icon">📄</span>
      </button>'''
        for idx, (lid, short_title, btype) in enumerate(lessons_in_osp, 1):
            global_idx = all_ids.index(lid) + 1
            icon = '★' if btype == 'assessment' else '📖'
            lessons_html += f'''      <button class="acc-lesson" onclick="loadLesson('{lid}')">
        <span class="acc-l-num">{global_idx}</span>
        <span class="acc-l-title">{short_title}</span>
        <span class="acc-l-icon">{icon}</span>
        <span class="acc-l-check" id="done-{lid}" role="checkbox" title="Merkitse suoritetuksi / poista merkintä" onclick="event.stopPropagation();toggleDone('{lid}')"></span>
      </button>'''

        track_icon = OSP_ICONS.get(osp['id'], '')
        kn_label = OSP_KN.get(osp['id'], osp['title'])
        osp_cards_html += f'''  <div class="osp-card" style="--osp-color:{osp['color']}">
    <div class="osp-card-head" onclick="toggleAcc(this)">
      <div class="osp-icon">{track_icon}</div>
      <div class="osp-card-info">
        <div class="osp-kn">{kn_label}</div>
        <div class="osp-title">{osp['title']}</div>
        <div class="osp-subtitle">{osp['subtitle']}</div>
      </div>
      <div class="osp-meta">
        <div class="osp-count">{len(lessons_in_osp)} oppituntia</div>
        <div class="acc-chevron">▼</div>
      </div>
    </div>
    <div class="osp-card-lessons">
{lessons_html}
    </div>
    <div class="osp-card-progress">
      <div class="prog-bar"><div class="prog-fill" id="pfill-{osp['id']}" style="background:{osp['color']}"></div></div>
      <span class="prog-text" id="ptxt-{osp['id']}">0 / {len(lessons_in_osp)}</span>
    </div>
  </div>
'''

    # JS lesson data
    js_items = []
    for lid, d in data.items():
        js_items.append(
            f'  "{lid}": {{\n'
            f'    ospId:"{d["osp_id"]}",ospTitle:`{esc_js(d["osp_title"])}`,\n'
            f'    ospColor:"{d["osp_color"]}",ospIcon:"{d["osp_icon"]}",\n'
            f'    shortTitle:`{esc_js(d["short_title"])}`,blockType:"{d["block_type"]}",\n'
            f'    slides:`{esc_js(d["slides"])}`,\n'
            f'    selfstudy:`{esc_js(d["selfstudy"])}`,\n'
            f'    vocab:`{esc_js(d["vocab"])}`,\n'
            f'    stasks:`{esc_js(d["stasks"])}`,\n'
            f'    tltasks:`{esc_js(d["tltasks"])}`,\n'
            f'    tmats:`{esc_js(d["tmats"])}`,\n'
            f'  }}'
        )
    js_data = 'const L={' + ',\n'.join(js_items) + '};'

    # Briefs JS data
    osp_titles = {o['id']: o['title'] for o in OSP_BLOCKS}
    osp_icons  = {o['id']: o['icon']  for o in OSP_BLOCKS}
    osp_colors = {o['id']: o['color'] for o in OSP_BLOCKS}
    brief_items = []
    for osp_id, html in briefs.items():
        if not html:
            continue
        brief_items.append(
            f'  "{osp_id}": {{\n'
            f'    ospId:"{osp_id}",ospTitle:`{esc_js(osp_titles.get(osp_id, ""))}`,\n'
            f'    ospIcon:"{osp_icons.get(osp_id, "")}",ospColor:"{osp_colors.get(osp_id, "")}",\n'
            f'    content:`{esc_js(html)}`,\n'
            f'  }}'
        )
    js_briefs = 'const BRIEFS={' + ',\n'.join(brief_items) + '};'

    osp_meta_js = json.dumps([
        {"id": o["id"], "ids": [lid for lid, _, _ in o["lessons"]]}
        for o in OSP_BLOCKS
    ])

    # Complete HTML
    return f'''<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tekoälyn perusteet</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2024%2024%22%3E%3Ccircle%20cx%3D%2212%22%20cy%3D%2212%22%20r%3D%2212%22%20fill%3D%22%23FFFFFF%22%2F%3E%3Cg%20transform%3D%22translate%281.8%2C1.8%29%20scale%280.85%29%22%3E%3Cpath%20d%3D%22M12%2012%20V4.6%20M12%2012%20L5.6%2017.6%20M12%2012%20L18.4%2017.6%22%20stroke%3D%22%230B0F1A%22%20stroke-width%3D%221.5%22%20fill%3D%22none%22%2F%3E%3Ccircle%20cx%3D%2212%22%20cy%3D%2212%22%20r%3D%222.7%22%20fill%3D%22%230B0F1A%22%2F%3E%3Ccircle%20cx%3D%2212%22%20cy%3D%224.6%22%20r%3D%222.05%22%20fill%3D%22%230B0F1A%22%2F%3E%3Ccircle%20cx%3D%225.6%22%20cy%3D%2217.6%22%20r%3D%222.05%22%20fill%3D%22%230B0F1A%22%2F%3E%3Ccircle%20cx%3D%2218.4%22%20cy%3D%2217.6%22%20r%3D%222.05%22%20fill%3D%22%230B0F1A%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Hanken+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>

:root{{
  --hero:#0B0F1A;--hero-2:#11182a;--hero-line:#232c44;
  --blue:oklch(0.66 0.15 264);--violet:oklch(0.66 0.15 305);--teal:oklch(0.66 0.13 208);
  --bc-primary:oklch(0.55 0.17 266);--bc-dark:oklch(0.46 0.15 266);
  --bg-paper:#F4F6FB;--bg-white:#FFFFFF;
  --border-soft:#E2E5EE;--border-light:#EAEDF4;
  --text-dark:#15171E;--text-muted:#5A6072;--text-light:#9AA1B4;
  --r:14px;--r-sm:10px;
  --font-sans:'Hanken Grotesk',system-ui,-apple-system,BlinkMacSystemFont,sans-serif;
  --font-serif:'Newsreader',Georgia,'Times New Roman',serif;
  --font-mono:'JetBrains Mono','SF Mono',Consolas,monospace;
}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{font-size:16px}}
body{{
  font-family:var(--font-sans);
  background:var(--bg-paper);
  color:var(--text-dark);
  line-height:1.6;
}}

/* ============ TOP NAVIGATION ============ */
.topbar{{
  background:var(--bg-white);
  border-bottom:1px solid var(--border-soft);
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:17px 40px;
  gap:20px;
  position:sticky;
  top:0;
  z-index:100;
}}
.logo-group{{
  display:flex;
  align-items:center;
  gap:12px;
}}
.logo-text{{
  display:flex;
  flex-direction:column;
  line-height:1.1;
  cursor:pointer;
}}
.brand-mark{{width:28px;height:28px;color:var(--blue);flex-shrink:0;display:block}}
.logo-text{{flex-direction:row;align-items:center;gap:0}}
.logo-text .logo-main{{
  font-family:var(--font-serif);
  font-size:21px;
  font-weight:500;
  color:var(--text-dark);
  letter-spacing:-0.01em;
  white-space:nowrap;
}}
.logo-text .logo-main b{{font-weight:600}}
.topbar-title{{display:none}}
.topbar-right{{
  display:flex;
  align-items:center;
  gap:20px;
  margin-left:auto;
}}
.progress-bar{{
  width:120px;
  height:5px;
  background:var(--border-light);
  border-radius:3px;
  overflow:hidden;
}}
.progress-fill{{
  height:100%;
  background:linear-gradient(90deg,var(--blue),var(--violet));
  width:0;
  transition:width 0.4s ease;
  border-radius:3px;
}}
.progress-text{{
  font-family:var(--font-mono);
  font-size:11px;
  font-weight:500;
  color:var(--text-muted);
  white-space:nowrap;
  letter-spacing:0.04em;
}}

/* ============ MAIN LAYOUT ============ */
.container{{
  max-width:1080px;
  margin:0 auto;
  padding:64px 40px 80px;
}}

/* ============ HERO (HOME) — dark two-tone block ============ */
.hero{{
  background:var(--hero);
  color:#fff;
  padding:60px 40px 84px;
  border-radius:0 0 28px 28px;
  margin-bottom:0;
}}
.hero-inner{{
  max-width:1180px;
  margin:0 auto;
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:56px;
  align-items:center;
}}
.hero-eyebrow{{
  font-family:var(--font-mono);
  font-size:12px;
  font-weight:500;
  color:var(--blue);
  text-transform:uppercase;
  letter-spacing:0.3em;
  margin-bottom:22px;
}}
.hero-title{{
  font-family:var(--font-serif);
  font-size:60px;
  font-weight:500;
  color:#fff;
  line-height:1.03;
  letter-spacing:-0.025em;
  margin-bottom:22px;
}}
.hero-title em{{font-style:italic;color:var(--violet)}}
.hero-subtitle{{
  font-size:18px;
  color:#9aa3bd;
  margin-bottom:34px;
  line-height:1.55;
  max-width:40ch;
}}
.hero-stats{{
  display:flex;
  gap:36px;
  flex-wrap:wrap;
}}
.stat-chip{{
  background:none;
  border:none;
  border-radius:0;
  padding:0;
  text-align:left;
  min-width:0;
}}
.stat-value{{
  font-family:var(--font-serif);
  font-size:36px;
  font-weight:600;
  color:#fff;
  line-height:1;
}}
.stat-label{{
  font-family:var(--font-mono);
  font-size:10.5px;
  color:#7e88a8;
  margin-top:8px;
  letter-spacing:0.16em;
  text-transform:uppercase;
}}
/* hero demo console */
.hero-demo{{
  background:var(--hero-2);
  border:1px solid var(--hero-line);
  border-radius:16px;
  overflow:hidden;
  box-shadow:0 30px 70px -30px rgba(0,0,0,.7);
}}
.hd-bar{{display:flex;align-items:center;gap:7px;padding:13px 16px;border-bottom:1px solid #1d2540}}
.hd-bar i{{width:10px;height:10px;border-radius:50%;background:#2c3552}}
.hd-bar span{{margin-left:8px;font-family:var(--font-mono);font-size:11px;color:#6f7aa0}}
.hd-body{{padding:22px 22px 24px;min-height:184px}}
.hd-prompt{{font-family:var(--font-mono);font-size:13.5px;color:#8b94b3;margin-bottom:16px}}
.hd-prompt b{{color:#cdd4ec;font-weight:400}}
.hd-resp{{font-family:var(--font-serif);font-size:22px;line-height:1.5;color:#fff}}
.hd-resp .w{{opacity:.15;animation:hdWord 5s ease-in-out infinite}}
@keyframes hdWord{{0%,5%{{opacity:.15}}15%{{opacity:1}}90%{{opacity:1}}100%{{opacity:.15}}}}
.hd-cur{{display:inline-block;width:9px;height:21px;background:var(--violet);margin-left:4px;vertical-align:-3px;animation:hdCaret .85s step-end infinite}}
@keyframes hdCaret{{50%{{opacity:0}}}}
.hd-meta{{margin-top:22px;font-family:var(--font-mono);font-size:10.5px;color:#5a6488;letter-spacing:0.04em;white-space:nowrap}}
.hd-meta b{{color:var(--teal);font-weight:400}}

/* ============ OSP CARDS (ACCORDION) ============ */
.osp-cards{{
  margin:60px 0;
}}
.osp-label{{
  font-family:var(--font-mono);
  font-size:11px;
  letter-spacing:0.24em;
  text-transform:uppercase;
  color:var(--text-muted);
  margin-bottom:18px;
}}
.osp-card{{
  background:var(--bg-white);
  border:1px solid var(--border-soft);
  border-radius:var(--r);
  margin-bottom:16px;
  overflow:hidden;
  box-shadow:0 1px 3px rgba(20,30,60,0.04);
  transition:transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}}
.osp-card:hover{{
  box-shadow:0 16px 40px -24px rgba(20,30,60,0.45);
  border-color:var(--osp-color);
}}
.osp-card-head{{
  position:relative;
  padding:26px 30px 26px 36px;
  display:flex;
  align-items:center;
  gap:22px;
  cursor:pointer;
  user-select:none;
  transition:background 0.18s;
}}
.osp-card-head::before{{
  content:'';
  position:absolute;
  left:0; top:18px; bottom:18px;
  width:5px; border-radius:0 5px 5px 0;
  background:var(--osp-color);
}}
.osp-card-head:hover{{
  background:color-mix(in srgb, var(--osp-color) 5%, transparent);
}}
.osp-icon{{
  width:54px; height:54px;
  color:var(--osp-color);
  flex-shrink:0;
}}
.osp-icon svg{{width:100%;height:100%;overflow:visible;display:block}}
.osp-card-info{{
  flex:1;
  text-align:left;
}}
.osp-kn{{
  font-family:var(--font-mono);
  font-size:11px;
  letter-spacing:0.16em;
  color:var(--osp-color);
  margin-bottom:6px;
}}
.osp-title{{
  font-family:var(--font-serif);
  font-size:27px;
  font-weight:500;
  letter-spacing:-0.01em;
  color:var(--text-dark);
  margin-bottom:3px;
}}
.osp-subtitle{{
  font-size:14.5px;
  color:var(--text-muted);
  line-height:1.4;
}}
.osp-meta{{
  display:flex;
  flex-direction:column;
  align-items:flex-end;
  gap:8px;
  flex-shrink:0;
}}
.osp-count{{
  font-family:var(--font-mono);
  font-size:11px;
  color:var(--text-muted);
  letter-spacing:0.06em;
  white-space:nowrap;
}}
.acc-chevron{{
  font-size:11px;
  color:var(--text-light);
  transition:transform 0.3s ease;
}}
.osp-card-head[onclick].open .acc-chevron{{
  transform:rotate(180deg);
}}
.osp-card-lessons{{
  border-top:1px solid var(--border-light);
  display:flex;
  flex-direction:column;
  max-height:0;
  overflow:hidden;
}}
.osp-card-lessons.open{{
  max-height:2000px;
}}
.acc-lesson{{
  display:flex;
  align-items:center;
  gap:12px;
  padding:14px 24px;
  border:none;
  background:none;
  text-align:left;
  cursor:pointer;
  border-bottom:1px solid var(--border-light);
  font-size:14px;
  color:var(--text-dark);
  transition:background 0.1s;
}}
.acc-lesson:last-child{{
  border-bottom:none;
}}
.acc-lesson:hover{{
  background:color-mix(in srgb, var(--osp-color) 5%, transparent);
}}
.acc-lesson.done{{
  color:var(--text-light);
}}
.acc-l-num{{
  display:flex;
  align-items:center;
  justify-content:center;
  min-width:32px;
  height:32px;
  background:var(--osp-color,var(--bc-primary));
  color:#fff;
  border-radius:50%;
  font-family:var(--font-mono);
  font-size:11.5px;
  font-weight:500;
  flex-shrink:0;
}}
.acc-l-title{{
  flex:1;
  font-weight:500;
}}
.acc-lesson.done .acc-l-title{{
  text-decoration:line-through;
}}
.acc-l-icon{{
  display:none;
}}
.acc-l-check{{
  width:20px;
  height:20px;
  border:2px solid var(--border-soft);
  border-radius:3px;
  flex-shrink:0;
  transition:all 0.2s;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:12px;
  font-weight:700;
  color:var(--bg-white);
}}
.acc-lesson.done .acc-l-check{{
  background:#059669;
  border-color:#059669;
}}
.acc-lesson.done .acc-l-check::after{{
  content:'✓';
}}
.acc-l-check{{cursor:pointer}}
.acc-l-check:hover{{
  border-color:#059669;
  box-shadow:0 0 0 3px color-mix(in srgb,#059669 18%,transparent);
}}
.acc-lesson.done .acc-l-check:hover{{
  background:#04734f;
  border-color:#04734f;
}}
.osp-card-progress{{
  padding:16px 24px;
  border-top:1px solid var(--border-light);
  display:flex;
  align-items:center;
  gap:12px;
}}
.prog-bar{{
  flex:1;
  height:6px;
  background:var(--border-light);
  border-radius:3px;
  overflow:hidden;
}}
.prog-fill{{
  height:100%;
  width:0;
  transition:width 0.5s ease;
}}
.prog-text{{
  font-family:var(--font-mono);
  font-size:11px;
  color:var(--text-muted);
  font-weight:500;
  min-width:60px;
  text-align:right;
}}

/* ============ ANIMATED TRACK ICONS ============ */
.aic-ring,.aic-line,.aic-spin,.aic-orbit{{transform-box:fill-box}}
.aic-ring{{transform-origin:center;animation:aicPulse 2.8s ease-out infinite}}
.aic-ring:nth-child(2){{animation-delay:.93s}}.aic-ring:nth-child(3){{animation-delay:1.86s}}
@keyframes aicPulse{{0%{{transform:scale(.28);opacity:1}}100%{{transform:scale(1);opacity:0}}}}
.aic-line{{transform-origin:left center;animation:aicType 3.4s ease-in-out infinite}}
.aic-line.l2{{animation-delay:.45s}}.aic-line.l3{{animation-delay:.9s}}
@keyframes aicType{{0%,6%{{transform:scaleX(0)}}32%,68%{{transform:scaleX(1)}}96%,100%{{transform:scaleX(0)}}}}
.aic-caret{{animation:aicBlink 1.05s steps(1) infinite}}
@keyframes aicBlink{{0%,50%{{opacity:1}}51%,100%{{opacity:0}}}}
.aic-spin,.aic-orbit{{transform-box:view-box;transform-origin:24px 24px}}
.aic-spin{{animation:aicSpin 9s linear infinite}}
.aic-orbit{{animation:aicSpin 3.6s linear infinite}}
@keyframes aicSpin{{to{{transform:rotate(360deg)}}}}

/* ============ INFO BOX ============ */
.info-box{{
  background:var(--bg-white);
  border:1px solid var(--border-soft);
  border-radius:var(--r);
  padding:30px 32px;
  margin:44px 0 0;
  color:var(--text-muted);
}}
.legend-title{{font-family:var(--font-mono);font-size:11px;letter-spacing:0.2em;text-transform:uppercase;color:var(--text-muted);margin-bottom:22px}}
.legend-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px 36px}}
.legend-item{{display:flex;align-items:flex-start;gap:13px}}
.lg-ic{{width:32px;height:32px;flex-shrink:0;color:var(--bc-primary);display:flex;align-items:center;justify-content:center;background:color-mix(in srgb,var(--bc-primary) 9%,transparent);border-radius:9px}}
.lg-ic svg{{width:17px;height:17px}}
.legend-item .lg-txt{{display:flex;flex-direction:column;gap:2px}}
.legend-item b{{font-size:14px;font-weight:600;color:var(--text-dark)}}
.legend-item span{{font-size:13px;color:var(--text-muted);line-height:1.4}}
.legend-note{{margin-top:26px;padding-top:20px;border-top:1px solid var(--border-light);font-size:13.5px;color:var(--text-muted);line-height:1.7}}
@media (max-width:640px){{.legend-grid{{grid-template-columns:1fr}}}}

/* ============ LESSON VIEW ============ */
.lesson-view{{
  display:none;
}}
.lesson-view.active{{
  display:flex;
  flex-direction:column;
  min-height:100vh;
}}
.lesson-header{{
  background:var(--bg-white);
  border-bottom:1px solid var(--border-soft);
  padding:40px 32px;
  margin-bottom:0;
}}
.breadcrumb{{
  font-family:var(--font-mono);
  font-size:11px;
  letter-spacing:0.04em;
  color:var(--text-muted);
  margin-bottom:14px;
  display:flex;
  align-items:center;
  gap:8px;
  white-space:nowrap;
}}
.bc-link{{
  color:var(--bc-primary);
  cursor:pointer;
  font-weight:600;
}}
.bc-link:hover{{
  text-decoration:underline;
}}
.lesson-title{{
  font-family:var(--font-serif);
  font-size:40px;
  font-weight:500;
  color:var(--text-dark);
  line-height:1.12;
  letter-spacing:-0.02em;
  margin-bottom:16px;
}}
.lesson-badges{{
  display:flex;
  gap:10px;
  flex-wrap:wrap;
}}
.badge{{
  display:inline-flex;
  align-items:center;
  gap:4px;
  font-family:var(--font-mono);
  font-size:10.5px;
  font-weight:500;
  padding:6px 12px;
  border-radius:20px;
  text-transform:uppercase;
  letter-spacing:0.1em;
  white-space:nowrap;
}}
.badge-osp{{
  background:color-mix(in srgb, var(--bc-primary) 12%, transparent);
  color:var(--bc-primary);
}}
.badge-type{{
  background:#EFF6FF;
  color:#1D4ED8;
}}
.badge-assess{{
  background:#FEF3C7;
  color:#92400E;
}}

/* ============ TABS ============ */
.lesson-tabs{{
  display:flex;
  border-bottom:2px solid var(--border-soft);
  background:var(--bg-white);
  padding:0 32px;
  overflow-x:auto;
  gap:0;
}}
.tab-btn{{
  display:inline-flex;
  align-items:center;
  gap:7px;
  padding:14px 18px;
  border:none;
  background:none;
  cursor:pointer;
  font-size:14px;
  font-weight:600;
  color:var(--text-muted);
  border-bottom:3px solid transparent;
  margin-bottom:-2px;
  transition:all 0.2s;
  white-space:nowrap;
}}
.tab-btn:hover{{
  color:var(--bc-primary);
}}
.tab-btn.active{{
  color:var(--bc-primary);
  border-bottom-color:var(--bc-primary);
}}
.tab-btn svg{{width:15px;height:15px;flex-shrink:0}}

/* ============ LESSON CONTENT ============ */
.lesson-panels{{
  flex:1;
  padding:40px 32px;
  overflow-y:auto;
}}
.panel{{
  display:none;
  max-width:780px;
  margin:0 auto;
}}
.panel.active{{
  display:block;
}}
.slides-container{{
  position:relative;
  width:100%;
  padding-top:8px;
}}
.slides-container iframe{{
  width:100%;
  height:min(569px,56vw);
  border:1px solid var(--border-soft);
  border-radius:var(--r-sm);
}}
.deck-wrap{{margin-top:6px}}
.deck-hint{{font-family:var(--font-mono);font-size:11px;letter-spacing:.04em;color:var(--text-muted);margin-bottom:8px}}
.deck{{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;padding-bottom:12px}}
.deck::-webkit-scrollbar{{height:8px}}
.deck::-webkit-scrollbar-thumb{{background:var(--border-soft);border-radius:8px}}
.deck-slide{{flex:0 0 100%;scroll-snap-align:center;border:1px solid var(--border-soft);border-radius:var(--r-sm);overflow:hidden;background:#FAFBFE}}
.deck-slide svg{{display:block;width:100%;height:auto}}
.deck-bar{{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:8px}}
.deck-full-btn{{font-family:var(--font-mono);font-size:12px;color:var(--bc-primary);background:none;border:1px solid var(--border-soft);border-radius:8px;padding:5px 12px;cursor:pointer;white-space:nowrap}}
.deck-full-btn:hover{{background:color-mix(in srgb,var(--bc-primary) 8%,transparent)}}
.deck-wrap:fullscreen{{background:#0B0F1A;padding:0;margin:0;display:flex;flex-direction:column;justify-content:center}}
.deck-wrap:fullscreen .deck-bar{{position:fixed;top:14px;right:18px;margin:0;z-index:5}}
.deck-wrap:fullscreen .deck-hint{{display:none}}
.deck-wrap:fullscreen .deck-full-btn{{color:#EAEEF8;border-color:#44517A;background:rgba(255,255,255,.08)}}
.deck-wrap:fullscreen .deck{{gap:0;padding:0;height:100vh;align-items:center}}
.deck-wrap:fullscreen .deck-slide{{flex:0 0 100%;height:100vh;display:flex;align-items:center;justify-content:center;border:none;border-radius:0;background:#0B0F1A}}
.deck-wrap:fullscreen .deck-slide svg{{width:min(100vw,177.78vh);height:auto}}
.panel h1{{
  font-family:var(--font-serif);
  font-size:27px;
  font-weight:600;
  margin:28px 0 12px;
  color:var(--text-dark);
  letter-spacing:-0.01em;
}}
.panel h1:first-child{{
  margin-top:0;
}}
.panel h2{{
  font-family:var(--font-serif);
  font-size:20px;
  font-weight:600;
  margin:24px 0 10px;
  color:var(--text-dark);
}}
.panel h3{{
  font-size:15px;
  font-weight:700;
  margin:16px 0 8px;
  color:var(--text-dark);
}}
.panel p{{
  margin:0 0 14px;
  color:var(--text-muted);
  line-height:1.75;
}}
.panel strong{{
  color:var(--text-dark);
  font-weight:700;
}}
.panel em{{
  font-style:italic;
}}
.panel a{{
  color:var(--bc-primary);
  text-decoration:none;
  font-weight:600;
}}
.panel a:hover{{
  text-decoration:underline;
}}
.panel ul,.panel ol{{
  margin:10px 0 14px 22px;
}}
.panel li{{
  margin-bottom:6px;
  color:var(--text-muted);
  line-height:1.7;
}}
.panel code{{
  background:#F3F4F6;
  padding:3px 8px;
  border-radius:4px;
  font-family:"Fira Code","SF Mono",Consolas,monospace;
  font-size:13px;
  color:var(--bc-dark);
}}
.panel pre{{
  background:#1E293B;
  color:#E2E8F0;
  padding:16px 20px;
  border-radius:var(--r-sm);
  overflow-x:auto;
  margin:16px 0 18px;
  font-family:"Fira Code","SF Mono",Consolas,monospace;
  font-size:13px;
  line-height:1.6;
}}
.panel pre code{{
  background:none;
  padding:0;
  color:inherit;
  font-size:inherit;
  font-family:inherit;
}}
.panel table{{
  border-collapse:collapse;
  width:100%;
  margin:14px 0 18px;
  font-size:14px;
}}
.panel th{{
  background:#F8FAFC;
  padding:10px 14px;
  text-align:left;
  border:1px solid var(--border-soft);
  font-weight:700;
  font-size:12px;
  color:var(--text-dark);
}}
.panel td{{
  padding:10px 14px;
  border:1px solid var(--border-soft);
  color:var(--text-muted);
}}
.panel hr{{
  border:none;
  border-top:1px solid var(--border-light);
  margin:24px 0;
}}
.panel blockquote{{
  border-left:4px solid var(--border-light);
  padding:14px 18px;
  background:#F9FAFB;
  border-radius:0 var(--r-sm) var(--r-sm) 0;
  margin:16px 0;
  color:var(--text-muted);
}}
.panel blockquote.pause{{
  background:#FEF9EC;
  border-left-color:#F59E0B;
  padding:16px 20px;
}}
.panel blockquote.pause p{{
  color:#78350F;
  font-weight:600;
  margin:0;
}}
.panel .solo-note{{
  background:#ECFDF5;
  border-left:4px solid #10B981;
  padding:14px 18px;
  border-radius:0 var(--r-sm) var(--r-sm) 0;
  font-size:13px;
  color:#065F46;
  margin:14px 0;
}}
.panel h2.task-header{{
  background:#F7F8FA;
  border-left:4px solid var(--bc-primary);
  padding:12px 16px;
  border-radius:0 var(--r-sm) var(--r-sm) 0;
  color:var(--bc-primary);
  font-size:15px;
  margin:20px 0 12px;
}}

/* ============ TASK CARDS ============ */
.task-card{{
  background:var(--bg-white);
  border:1px solid var(--border-soft);
  border-radius:12px;
  margin:24px 0;
  overflow:hidden;
  box-shadow:0 1px 4px rgba(0,0,0,0.04);
  transition:box-shadow 0.2s;
}}
.task-card:hover{{
  box-shadow:0 3px 12px rgba(0,0,0,0.08);
}}
.task-card-header{{
  padding:16px 20px 14px;
  border-bottom:1px solid var(--border-soft);
  display:flex;
  align-items:center;
  gap:10px;
}}
.task-card-header h2{{
  margin:0;
  font-size:16px;
  font-weight:700;
  color:var(--text-dark);
  line-height:1.3;
}}
.task-card-body{{
  padding:20px 24px;
}}
.task-card-body > :first-child{{
  margin-top:0;
}}
.task-card-body > :last-child{{
  margin-bottom:0;
}}

/* Task type: regular task — purple-ish left accent */
.task-card--task{{
  border-left:4px solid var(--bc-primary);
}}
.task-card--task .task-card-header{{
  background:linear-gradient(135deg, #F1F4FE 0%, #EAEFFD 100%);
}}
.task-card--task .task-card-header h2{{
  color:var(--bc-primary);
}}
.task-card--task .task-card-header::before{{
  content:'';width:10px;height:10px;border-radius:3px;flex-shrink:0;
  background:var(--bc-primary);
}}

/* Task type: info — blue accent (väärinkäsitykset, osaamistavoitteet, CFU) */
.task-card--info{{
  border-left:4px solid #8E7BE6;
}}
.task-card--info .task-card-header{{
  background:linear-gradient(135deg, #F5F2FE 0%, #EFEAFD 100%);
}}
.task-card--info .task-card-header h2{{
  color:#6A48C9;
}}
.task-card--info .task-card-header::before{{
  content:'';width:10px;height:10px;border-radius:3px;flex-shrink:0;
  background:#6A48C9;
}}

/* Task type: assessment — amber accent */
.task-card--assessment{{
  border-left:4px solid #D97706;
}}
.task-card--assessment .task-card-header{{
  background:linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);
}}
.task-card--assessment .task-card-header h2{{
  color:#92400E;
}}
.task-card--assessment .task-card-header::before{{
  content:'';width:10px;height:10px;border-radius:3px;flex-shrink:0;
  background:#D97706;
}}

/* Task type: resource — green accent */
.task-card--resource{{
  border-left:4px solid #059669;
}}
.task-card--resource .task-card-header{{
  background:linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
}}
.task-card--resource .task-card-header h2{{
  color:#065F46;
}}
.task-card--resource .task-card-header::before{{
  content:'';width:10px;height:10px;border-radius:3px;flex-shrink:0;
  background:#059669;
}}

/* Remove hr separators inside card panels — cards do the separating now */
.task-card + hr,
.task-card-body hr{{
  display:none;
}}

/* Small cards (h3-level) — slightly less prominent */
.task-card--sm{{
  margin:16px 0;
  border-radius:10px;
  box-shadow:0 1px 3px rgba(0,0,0,0.03);
}}
.task-card--sm .task-card-header{{
  padding:12px 16px 10px;
}}
.task-card--sm .task-card-header h3{{
  margin:0;
  font-size:14px;
  font-weight:700;
  line-height:1.3;
}}
.task-card--sm .task-card-body{{
  padding:14px 18px;
}}
.task-card--sm .task-card-header::before{{
  width:8px;height:8px;
}}

/* Nested h3 inside task cards (when not a card themselves) */
.task-card-body h3{{
  font-size:14px;
  font-weight:700;
  color:var(--text-dark);
  margin:18px 0 8px;
  padding-bottom:6px;
  border-bottom:1px solid #ECEFF6;
}}

/* ============ LESSON FOOTER ============ */
.lesson-footer{{
  border-top:1px solid var(--border-soft);
  padding:24px 32px;
  background:var(--bg-white);
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:16px;
}}
.nav-buttons{{
  display:flex;
  gap:12px;
}}
.btn{{
  padding:10px 20px;
  border:1px solid var(--border-soft);
  border-radius:var(--r-sm);
  background:var(--bg-white);
  color:var(--text-muted);
  font-size:13px;
  font-weight:600;
  cursor:pointer;
  transition:all 0.2s;
  display:flex;
  align-items:center;
  gap:6px;
}}
.btn:hover:not(:disabled){{
  background:color-mix(in srgb, var(--bc-primary) 6%, transparent);
  color:var(--bc-primary);
  border-color:var(--bc-primary);
}}
.btn:disabled{{
  opacity:0.4;
  cursor:not-allowed;
}}
.btn-primary{{
  background:var(--bc-primary);
  color:var(--bg-white);
  border-color:var(--bc-primary);
}}
.btn-primary:hover{{
  background:var(--bc-dark);
  border-color:var(--bc-dark);
}}
.done-btn{{
  padding:10px 20px;
  border:2px solid var(--border-soft);
  border-radius:var(--r-sm);
  background:transparent;
  color:var(--text-muted);
  font-size:13px;
  font-weight:600;
  cursor:pointer;
  transition:all 0.2s;
}}
.done-btn.marked{{
  background:#ECFDF5;
  border-color:#059669;
  color:#059669;
}}
.done-btn:hover{{
  background:#ECFDF5;
  border-color:#059669;
  color:#059669;
}}

/* ============ MERMAID DIAGRAMS ============ */
.mermaid{{
  margin:32px 0;
  padding:24px 20px;
  background:linear-gradient(135deg, #FBFCFF 0%, #EEF1FA 100%);
  border:1px solid var(--border-soft);
  border-left:4px solid var(--bc-primary);
  border-radius:12px;
  text-align:center;
  overflow-x:auto;
  box-shadow:0 2px 8px rgba(20,30,60,0.06);
}}
.mermaid svg{{
  max-width:100%;
  height:auto;
  filter:saturate(0.9);
}}
/* Override mermaid node styles for course brand */
.mermaid .node rect,
.mermaid .node circle,
.mermaid .node polygon{{
  stroke-width:1.5px !important;
  rx:8 !important;
  ry:8 !important;
}}
.mermaid .edgePath .path{{
  stroke-width:1.8px !important;
  stroke:#6B5B73 !important;
}}
.mermaid .edgeLabel{{
  font-size:13px !important;
  background:#FDFCFA !important;
  padding:2px 6px !important;
}}
.mermaid .cluster rect{{
  rx:12 !important;
  ry:12 !important;
  stroke:#C4CCF2 !important;
  fill:#F2F5FE !important;
}}
.mermaid .label{{
  font-size:14px !important;
  color:#2D2D2D !important;
}}

/* ============ READER MODERNIZATION (v2) — contrast, rhythm, hierarchy ============ */
:root{{
  --text-muted:#4A5161;
  --reader-body:#363C4C;
}}
.lesson-panels{{padding:48px 32px 72px}}
.panel{{max-width:744px}}
.panel h1{{font-family:var(--font-serif);font-size:31px;font-weight:600;letter-spacing:-0.018em;color:var(--text-dark);margin:0 0 20px}}
.panel h2{{font-family:var(--font-serif);font-size:23px;font-weight:600;letter-spacing:-0.01em;color:var(--text-dark);margin:40px 0 12px}}
.panel h3{{font-family:var(--font-sans);font-size:15px;font-weight:700;letter-spacing:0.005em;color:var(--text-dark);margin:26px 0 8px}}
.panel p,.panel li{{color:var(--reader-body);font-size:15.5px;line-height:1.8}}
.panel li{{margin-bottom:8px}}
.panel ul,.panel ol{{margin:12px 0 16px 22px}}
.panel strong{{color:var(--text-dark);font-weight:600}}
.panel a{{color:var(--bc-primary);text-decoration-thickness:1px;text-underline-offset:2px}}
.panel hr{{border-top:1px solid var(--border-soft);margin:30px 0}}
.panel table{{font-size:14.5px;border:1px solid var(--border-soft);border-radius:10px;overflow:hidden}}
.panel th{{background:#EBEEF7;color:var(--text-dark);font-family:var(--font-mono);font-size:11px;font-weight:500;letter-spacing:0.03em;text-transform:uppercase;border-color:var(--border-soft)}}
.panel td{{color:var(--reader-body);border-color:var(--border-soft)}}
.panel code{{font-family:var(--font-mono);background:#EEF1FA;color:#3A3FA6;border:1px solid #E2E6F3;border-radius:5px;text-decoration:none}}
.panel pre{{font-family:var(--font-mono);background:#0E1320;border:1px solid #1C2438;border-radius:12px;color:#E6EAF5;white-space:pre-wrap;word-break:break-word;text-decoration:none;line-height:1.65;font-size:13px}}
.panel pre code{{font-family:var(--font-mono);white-space:pre-wrap;text-decoration:none;border:none;background:none;padding:0}}
.panel blockquote{{border-left:3px solid var(--border-soft);background:#F6F8FC;color:var(--reader-body);border-radius:0 10px 10px 0}}
.panel blockquote.pause{{background:#FFF8EC;border-left-color:#E0982E}}
.panel blockquote.pause p{{color:#7A4E12}}
.panel .solo-note{{background:#E9F7F0;border-left-color:#23A578;color:#175C44}}

/* Task cards — flatter, cleaner, stronger header type */
.task-card{{border:1px solid var(--border-soft);border-radius:14px;box-shadow:0 1px 2px rgba(20,30,60,.045);margin:22px 0}}
.task-card:hover{{box-shadow:0 10px 30px -18px rgba(20,30,60,.35)}}
.task-card-header{{padding:15px 22px;border-bottom:1px solid var(--border-soft);gap:11px}}
.task-card-header h2{{font-family:var(--font-sans);font-size:16.5px;font-weight:700;line-height:1.35;color:var(--text-dark);flex:1}}
.task-card-header h3{{flex:1}}
.task-card-body{{padding:20px 24px}}
.task-card-body p,.task-card-body li{{color:var(--reader-body)}}
.task-card--task .task-card-header{{background:#EEF1FD}}
.task-card--info .task-card-header{{background:#F2EFFD}}
.task-card--info{{border-left-color:#8E7BE6}}
.task-card--assessment .task-card-header{{background:#FFF6E6}}
.task-card--assessment{{border-left-color:#D9930B}}
.task-card--resource .task-card-header{{background:#E9F7F0}}
.task-card--resource{{border-left-color:#14A06F}}

/* Small (h3) cards — nested look under their section heading */
.task-card--sm{{margin:11px 0 11px 24px;background:#FBFCFE;box-shadow:none;border-radius:11px}}
.task-card--sm .task-card-header{{padding:12px 18px;border-bottom-color:var(--border-light)}}
.task-card--sm .task-card-header h3{{font-size:14.5px;font-weight:700;color:var(--text-dark)}}
.task-card--sm .task-card-body{{padding:14px 18px}}

/* Header-only cards (empty body) → render as a SECTION HEADING, not a card */
.task-card.is-sectionhead{{
  border:none;background:none;box-shadow:none;overflow:visible;border-radius:0;margin:44px 0 8px;
}}
.task-card.is-sectionhead:hover{{box-shadow:none}}
.task-card.is-sectionhead > .task-card-body{{display:none}}
.task-card.is-sectionhead .task-card-header{{
  background:none;border:none;border-bottom:2px solid var(--border-soft);padding:0 0 10px;border-radius:0;gap:12px;
}}
.task-card.is-sectionhead .task-card-header h2{{
  font-family:var(--font-serif);font-size:23px;font-weight:600;color:var(--text-dark);
}}
.task-card.is-sectionhead .task-card-header::before{{width:11px;height:11px;border-radius:3px}}
.task-card--info.is-sectionhead .task-card-header{{border-bottom-color:#C9BEF1}}
.task-card--info.is-sectionhead .task-card-header::before{{background:#8E7BE6}}
.task-card--task.is-sectionhead .task-card-header::before{{background:var(--bc-primary)}}

/* Status pills (Suositeltu / Syventävä) */
.pill{{display:inline-flex;align-items:center;gap:5px;font-family:var(--font-mono);font-size:10px;font-weight:500;letter-spacing:0.08em;text-transform:uppercase;padding:3px 10px 3px 9px;border-radius:999px;white-space:nowrap;line-height:1.5;margin-left:4px;position:relative;top:-1px}}
.pill::before{{content:'';width:6px;height:6px;border-radius:50%;background:currentColor;flex-shrink:0}}
.pill--rec{{background:#E1F4EA;color:#0E7D55}}
.pill--adv{{background:#EFEAFB;color:#6A48C9}}

@media (prefers-reduced-motion: reduce){{
  .hd-resp .w{{opacity:1 !important;animation:none}}
  .hd-cur{{animation:none}}
}}

/* —— Variant: KORTIT (soft, rounded, colourful) —— */
#lesson-panels.rv-soft .panel > h2{{position:relative;padding-left:17px}}
#lesson-panels.rv-soft .panel > h2::before{{content:'';position:absolute;left:0;top:.16em;bottom:.16em;width:4px;border-radius:3px;background:linear-gradient(var(--blue),var(--violet))}}
#lesson-panels.rv-soft .task-card:not(.is-sectionhead){{border-radius:20px;border-color:transparent;box-shadow:0 16px 42px -24px rgba(20,30,60,.55)}}
#lesson-panels.rv-soft .task-card:not(.is-sectionhead):hover{{transform:translateY(-2px)}}
#lesson-panels.rv-soft .task-card:not(.is-sectionhead) .task-card-header{{padding:18px 24px;border-bottom:none}}
#lesson-panels.rv-soft .task-card--task:not(.is-sectionhead) .task-card-header{{background:linear-gradient(135deg,#EDF1FE,#E5ECFD)}}
#lesson-panels.rv-soft .task-card--info:not(.is-sectionhead) .task-card-header{{background:linear-gradient(135deg,#F4F0FE,#EBE4FC)}}
#lesson-panels.rv-soft .task-card--assessment:not(.is-sectionhead) .task-card-header{{background:linear-gradient(135deg,#FFF6E6,#FDEDC9)}}
#lesson-panels.rv-soft .task-card--resource:not(.is-sectionhead) .task-card-header{{background:linear-gradient(135deg,#E7F7EF,#D8F2E4)}}
#lesson-panels.rv-soft .task-card--sm{{border-radius:16px;background:#fff;border-color:var(--border-soft)}}
#lesson-panels.rv-soft .panel blockquote{{border-radius:16px;border-left-width:4px}}
#lesson-panels.rv-soft .panel pre{{border-radius:16px}}
#lesson-panels.rv-soft .panel table{{border-radius:14px}}

/* —— Variant: LEHTI (editorial, ruled, minimal chrome) —— */
#lesson-panels.rv-mag .panel{{max-width:680px}}
#lesson-panels.rv-mag .panel > h1{{font-size:39px;line-height:1.07;margin-bottom:26px}}
#lesson-panels.rv-mag .panel > h2{{font-size:26px;border-top:1.5px solid var(--text-dark);padding-top:15px;margin-top:48px}}
#lesson-panels.rv-mag .panel > h3{{font-family:var(--font-serif);font-size:18px;font-weight:600}}
#lesson-panels.rv-mag .panel p,#lesson-panels.rv-mag .panel li{{font-size:16.5px;line-height:1.86}}
#lesson-panels.rv-mag .task-card:not(.is-sectionhead){{border:none;border-left:2px solid #8E7BE6;border-radius:0;box-shadow:none;background:none;margin:28px 0}}
#lesson-panels.rv-mag .task-card:not(.is-sectionhead):hover{{box-shadow:none;transform:none}}
#lesson-panels.rv-mag .task-card:not(.is-sectionhead) .task-card-header{{background:none!important;border:none;padding:0 0 4px 22px}}
#lesson-panels.rv-mag .task-card:not(.is-sectionhead) .task-card-header h2{{font-family:var(--font-serif);font-size:21px}}
#lesson-panels.rv-mag .task-card:not(.is-sectionhead) .task-card-header::before{{display:none}}
#lesson-panels.rv-mag .task-card:not(.is-sectionhead) .task-card-body{{padding:6px 0 0 22px}}
#lesson-panels.rv-mag .task-card--task:not(.is-sectionhead){{border-left-color:var(--bc-primary)}}
#lesson-panels.rv-mag .task-card--assessment:not(.is-sectionhead){{border-left-color:#D9930B}}
#lesson-panels.rv-mag .task-card--resource:not(.is-sectionhead){{border-left-color:#14A06F}}
#lesson-panels.rv-mag .task-card--sm{{margin:14px 0 14px 22px;background:none;border:none;border-left:2px solid var(--border-soft);border-radius:0}}
#lesson-panels.rv-mag .task-card--sm .task-card-header h3{{font-family:var(--font-serif);font-size:17px}}
#lesson-panels.rv-mag .task-card.is-sectionhead .task-card-header{{border-bottom:none;border-top:2px solid var(--text-dark);padding-top:13px}}
#lesson-panels.rv-mag .task-card.is-sectionhead .task-card-header h2{{font-size:25px}}
#lesson-panels.rv-mag .panel blockquote:not(.pause){{background:none;border-left:3px solid var(--blue);border-radius:0;padding-left:18px;font-style:italic;color:var(--text-dark)}}

/* —— Variant: KONSOLI (technical, mono, crisp) —— */
#lesson-panels.rv-tech{{background:#ECEFF7}}
#lesson-panels.rv-tech .panel > h2{{font-family:var(--font-mono);font-size:17px;font-weight:500;letter-spacing:0;color:var(--text-dark);margin-top:38px}}
#lesson-panels.rv-tech .panel > h2::before{{content:'## ';color:var(--blue)}}
#lesson-panels.rv-tech .panel > h3{{font-family:var(--font-mono);font-size:13.5px;font-weight:500}}
#lesson-panels.rv-tech .panel > h3::before{{content:'# ';color:var(--violet)}}
#lesson-panels.rv-tech .task-card:not(.is-sectionhead){{border-radius:8px;border:1px solid #D3D9E8;box-shadow:none;background:#fff;position:relative;overflow:hidden}}
#lesson-panels.rv-tech .task-card:not(.is-sectionhead)::after{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--bc-primary)}}
#lesson-panels.rv-tech .task-card--info:not(.is-sectionhead)::after{{background:#8E7BE6}}
#lesson-panels.rv-tech .task-card--assessment:not(.is-sectionhead)::after{{background:#D9930B}}
#lesson-panels.rv-tech .task-card--resource:not(.is-sectionhead)::after{{background:#14A06F}}
#lesson-panels.rv-tech .task-card:not(.is-sectionhead) .task-card-header{{background:#F5F8FD!important;border-bottom:1px solid #E4E8F2}}
#lesson-panels.rv-tech .task-card:not(.is-sectionhead) .task-card-header h2,#lesson-panels.rv-tech .task-card:not(.is-sectionhead) .task-card-header h3{{font-family:var(--font-mono);font-size:14px;font-weight:500;letter-spacing:0}}
#lesson-panels.rv-tech .task-card:not(.is-sectionhead) .task-card-header::before{{border-radius:2px}}
#lesson-panels.rv-tech .task-card--sm{{border-radius:6px;margin-left:24px}}
#lesson-panels.rv-tech .panel pre{{border-radius:8px}}
#lesson-panels.rv-tech .panel table{{border-radius:6px}}
#lesson-panels.rv-tech .panel th{{font-family:var(--font-mono)}}
#lesson-panels.rv-tech .panel blockquote{{border-radius:6px}}
#lesson-panels.rv-tech .task-card.is-sectionhead .task-card-header h2{{font-family:var(--font-mono);font-size:15px;font-weight:600;letter-spacing:.01em}}
#lesson-panels.rv-tech .task-card.is-sectionhead .task-card-header::before{{border-radius:2px}}

/* ============ LESSON FRAME — cohesive with the home editorial look ============ */
.lesson-header{{
  background:var(--hero);
  border:none;
  border-radius:0 0 26px 26px;
  padding:40px 40px 32px;
}}
.lesson-header .breadcrumb{{color:#8b94b3;margin-bottom:16px}}
.lesson-header .bc-link{{color:var(--blue)}}
.lesson-header .bc-link:hover{{color:#aeb9ff}}
.lesson-header .lesson-title{{color:#fff;font-size:38px}}
.badge-osp{{background:rgba(124,141,240,.16);color:#aeb9ff}}
.badge-type{{background:rgba(255,255,255,.09);color:#c3cbe6}}
.badge-assess{{background:rgba(217,147,11,.2);color:#f0c071}}

.lesson-tabs{{
  background:transparent;
  border-bottom:1px solid var(--border-soft);
  padding:10px 40px 0;
  margin-top:4px;
}}
.tab-btn{{font-family:var(--font-mono);font-size:12px;font-weight:500;letter-spacing:.01em;color:var(--text-muted);border-bottom-width:2px;padding:12px 16px}}
.tab-btn:hover{{color:var(--text-dark)}}
.tab-btn.active{{color:var(--bc-primary);border-bottom-color:var(--bc-primary)}}

.lesson-footer{{border-top:1px solid var(--border-soft);padding:22px 40px}}
.btn{{border-radius:999px;font-family:var(--font-mono);font-size:12px;font-weight:500;letter-spacing:.02em;padding:11px 20px;white-space:nowrap}}
.btn-primary{{background:var(--bc-primary);border-color:var(--bc-primary);color:#fff}}
.btn-primary:hover:not(:disabled){{background:var(--bc-dark);border-color:var(--bc-dark);color:#fff}}
.done-btn{{border-radius:999px;font-family:var(--font-mono);font-size:12px;font-weight:500;letter-spacing:.03em;white-space:nowrap}}

/* ============ READER STYLE SWITCHER ============ */
.rv-switch{{position:fixed;right:20px;bottom:92px;z-index:300;display:none;align-items:center;gap:3px;
  background:rgba(255,255,255,.94);backdrop-filter:blur(10px);border:1px solid var(--border-soft);
  border-radius:999px;padding:5px;box-shadow:0 12px 34px -14px rgba(20,30,60,.5)}}
body:has(#lesson.active) .rv-switch{{display:flex}}
.rv-switch .lab{{font-family:var(--font-mono);font-size:9.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--text-light);padding:0 6px 0 10px}}
.rv-switch button{{font-family:var(--font-mono);font-size:11px;font-weight:500;letter-spacing:.03em;border:none;background:none;color:var(--text-muted);padding:7px 14px;border-radius:999px;cursor:pointer}}
.rv-switch button:hover{{color:var(--text-dark)}}
.rv-switch button.on{{background:var(--bc-primary);color:#fff}}

/* ============ RESPONSIVE ============ */
@media (max-width:900px){{
  .hero-inner{{grid-template-columns:1fr;gap:36px}}
  .hero{{padding:48px 24px 60px}}
  .hero-title{{font-size:46px}}
}}
@media (max-width:768px) {{
  .topbar{{padding:12px 16px}}
  .container{{padding:40px 16px}}
  .hero{{padding:40px 18px 52px}}
  .hero-title{{font-size:36px}}
  .hero-subtitle{{font-size:15px}}
  .hero-stats{{gap:24px}}
  .osp-card-head{{padding:18px 18px 18px 24px;gap:16px}}
  .osp-title{{font-size:22px}}
  .acc-lesson{{padding-left:18px;padding-right:18px}}
  .lesson-header{{padding:24px 16px}}
  .lesson-title{{font-size:28px}}
  .lesson-panels{{padding:24px 16px}}
  .lesson-footer{{padding:16px;flex-direction:column-reverse}}
}}

/* ============ ANIMATED CONCEPT FIGURES (.ai-demo wrapper) ============ */
.ai-demo{{margin:28px 0;border-radius:16px;overflow:hidden;border:1px solid #232C44;
  background:radial-gradient(120% 120% at 70% 10%,#161C2E 0%,#0B0F1A 60%)}}
.ai-demo__tag{{display:block;padding:16px 20px 0;font-family:var(--font-mono);font-size:10.5px;
  letter-spacing:.18em;text-transform:uppercase;color:#7E88A8}}
.ai-demo__stage{{position:relative;height:230px;overflow:hidden}}
.ai-demo__cap{{padding:14px 20px;margin:0;font-family:var(--font-mono);font-size:11px;
  color:#8B94B3;border-top:1px solid #1C2438;background:#0B0F1A}}

/* ============ SITE FOOTER ============ */
.site-footer{{
  margin-top:56px;
  padding:26px 20px 34px;
  text-align:center;
  font-family:var(--font-mono);
  font-size:11.5px;
  letter-spacing:.05em;
  color:var(--text-muted);
  border-top:1px solid var(--border-light);
}}
.site-footer a{{
  color:inherit;
  text-decoration:none;
  border-bottom:1px solid var(--border-soft);
  transition:color .2s,border-color .2s;
}}
.site-footer a:hover{{
  color:var(--text-dark);
  border-color:currentColor;
}}

/* ============ MOBILE ============ */
@media (max-width:680px){{
  .ai-demo__stage{{
    overflow-x:auto;
    -webkit-overflow-scrolling:touch;
    justify-content:flex-start!important;
    scrollbar-width:thin;
  }}
  .ai-demo__stage>*{{margin-left:auto;margin-right:auto;flex-shrink:0}}
  .ai-demo::after{{
    content:'⟷ vieritä kuvaa sivusuunnassa';
    display:block;
    padding:0 20px 10px;
    font-family:var(--font-mono);
    font-size:9.5px;
    letter-spacing:.08em;
    text-transform:uppercase;
    color:#5D6880;
  }}
  .panel table{{display:block;max-width:100%;overflow-x:auto}}
}}
@media (max-width:480px){{
  .topbar{{padding:10px 14px;gap:10px}}
  .topbar .progress-text{{display:none}}
  .topbar .progress-bar{{width:56px}}
}}

</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{
  startOnLoad:false,
  theme:'base',
  fontFamily:'Hanken Grotesk, system-ui, sans-serif',
  themeVariables:{{
    primaryColor:'#EEF1FD',
    primaryTextColor:'#15171E',
    primaryBorderColor:'#5B68C6',
    lineColor:'#6B5B73',
    secondaryColor:'#EFEAFB',
    tertiaryColor:'#E9F7F0',
    noteBkgColor:'#FFF6E6',
    noteTextColor:'#15171E',
    noteBorderColor:'#D9930B',
    fontSize:'14px',
    edgeLabelBackground:'#FDFCFA'
  }}
}});</script>
</head>
<body>

<!-- TOP NAVIGATION -->
<nav class="topbar">
  <div class="logo-group" onclick="showHome()" style="cursor:pointer">
    <span class="brand-mark"><svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 12 V4.6 M12 12 L5.6 17.6 M12 12 L18.4 17.6" stroke="currentColor" stroke-width="1.5"/><circle cx="12" cy="12" r="2.7" fill="currentColor"/><circle cx="12" cy="4.6" r="2.05" fill="currentColor"/><circle cx="5.6" cy="17.6" r="2.05" fill="currentColor"/><circle cx="18.4" cy="17.6" r="2.05" fill="currentColor"/></svg></span>
    <div class="logo-text">
      <span class="logo-main">Tekoälyn <b>perusteet</b></span>
    </div>
  </div>
  <div class="topbar-right">
    <div class="progress-bar"><div class="progress-fill" id="pb"></div></div>
    <div class="progress-text" id="pt">0/27</div>
  </div>
</nav>

<!-- HOME VIEW -->
<div id="home" class="home-view">
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-copy">
        <div class="hero-eyebrow">AI · Perusteet — 3 OSP</div>
        <h1 class="hero-title">Ymmärrä tekoäly <em>teoriasta</em> agentteihin.</h1>
        <p class="hero-subtitle">27 oppituntia, jotka avaavat tekoälyn — teoriasta käytäntöön ja itsenäisiin agentteihin.</p>
        <div class="hero-stats">
          <div class="stat-chip">
            <div class="stat-value">27</div>
            <div class="stat-label">Oppituntia</div>
          </div>
          <div class="stat-chip">
            <div class="stat-value">3</div>
            <div class="stat-label">Kokonaisuutta</div>
          </div>
          <div class="stat-chip">
            <div class="stat-value" id="done-cnt">0</div>
            <div class="stat-label">Suoritettu</div>
          </div>
        </div>
      </div>
      <div class="hero-demo">
        <div class="hd-bar"><i></i><i></i><i></i><span>perusteet · esimerkki</span></div>
        <div class="hd-body">
          <div class="hd-prompt">&gt; <b>Selitä tekoäly yhdellä lauseella.</b></div>
          <div class="hd-resp"><span class="w" style="animation-delay:0s">Ohjelma,</span> <span class="w" style="animation-delay:.13s">joka</span> <span class="w" style="animation-delay:.26s">oppii</span> <span class="w" style="animation-delay:.39s">datasta</span> <span class="w" style="animation-delay:.52s">—</span> <span class="w" style="animation-delay:.65s">ei</span> <span class="w" style="animation-delay:.78s">noudata</span> <span class="w" style="animation-delay:.91s">sääntöjä.</span><span class="hd-cur"></span></div>
          <div class="hd-meta"><b>▍</b>&nbsp; 0.4&nbsp;s &nbsp;·&nbsp; 38 tokenia &nbsp;·&nbsp; perus-LLM</div>
        </div>
      </div>
    </div>
  </section>

  <div class="container">

    <!-- OSP CARDS WITH ACCORDION -->
    <div class="osp-cards">
      <div class="osp-label">Kolme kokonaisuutta · 27 oppituntia</div>
{osp_cards_html}
    </div>

    <!-- INFO BOX -->
    <div class="info-box">
      <div class="legend-title">Materiaalityypit</div>
      <div class="legend-grid">
        <div class="legend-item"><span class="lg-ic"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="1.5" y="2.5" width="13" height="9" rx="1.5"></rect><path d="M8 11.5V14M5.5 14h5" stroke-linecap="round"></path></svg></span><div class="lg-txt"><b>Diat</b><span>Oppitunnin diaesitys</span></div></div>
        <div class="legend-item"><span class="lg-ic"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M8 4.2C8 3.3 6.8 2.5 4.8 2.5 3.2 2.5 2 3 2 3v9s1.2-.5 2.8-.5S8 12.2 8 13M8 4.2C8 3.3 9.2 2.5 11.2 2.5 12.8 2.5 14 3 14 3v9s-1.2-.5-2.8-.5S8 12.2 8 13M8 4.2V13"></path></svg></span><div class="lg-txt"><b>Itseopiskelumateriaali</b><span>Oppitunnin sisältö</span></div></div>
        <div class="legend-item"><span class="lg-ic"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><path d="M6.5 4H14M6.5 8H14M6.5 12H14M2 4l.9.9L4.6 3M2 8l.9.9L4.6 7M2 12l.9.9L4.6 11"></path></svg></span><div class="lg-txt"><b>Opiskelutehtävät</b><span>Itsenäisesti tai pareittain tehtävät harjoitukset</span></div></div>
        <div class="legend-item"><span class="lg-ic"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M3 3.5A1.5 1.5 0 014.5 2H13v9.5H4.5A1.5 1.5 0 003 13V3.5z"></path><path d="M3 13a1.5 1.5 0 011.5-1.5H13V14H4.5A1.5 1.5 0 013 12.5"></path></svg></span><div class="lg-txt"><b>Sanasto</b><span>Tunnin keskeisimmät käsitteet ja termit</span></div></div>
        <div class="legend-item"><span class="lg-ic"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="5.8" cy="5" r="2.1"></circle><path d="M2.5 13c0-2 1.5-3.2 3.3-3.2S9.1 11 9.1 13" stroke-linecap="round"></path><path d="M10.6 3.5A2 2 0 0113 5.4a2 2 0 01-1.3 1.9M11 9.9c1.5.3 2.5 1.5 2.5 3.1" stroke-linecap="round"></path></svg></span><div class="lg-txt"><b>Opettajavetoiset tehtävät</b><span>Luokassa yhdessä tehtävät harjoitukset</span></div></div>
        <div class="legend-item"><span class="lg-ic"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><rect x="3" y="3" width="10" height="11" rx="1.5"></rect><path d="M6 3.2V2.2h4v1M6 7h4M6 10h2.5" stroke-linecap="round"></path></svg></span><div class="lg-txt"><b>Opettajan materiaali</b><span>Ohjeet ja taustatiedot tunnin pitämiseen</span></div></div>
      </div>
      <p class="legend-note">Merkitse tunti suoritetuksi valitsemalla oppitunti ja klikkaamalla "Merkitse suoritetuksi" — edistyminen tallentuu selaimeesi.</p>
    </div>
  </div>
</div>

<!-- LESSON VIEW -->
<div id="lesson" class="lesson-view">
  <div id="lesson-header" class="lesson-header"></div>
  <div id="lesson-tabs" class="lesson-tabs"></div>
  <div id="lesson-panels" class="lesson-panels rv-tech"></div>
  <div id="lesson-footer" class="lesson-footer"></div>
</div>

<script>
{js_data}
{js_briefs}
const ALLIDS={json.dumps(all_ids)};
const OSPM={osp_meta_js};
let cid=null,ctab='selfstudy';

// Mark header-only task-cards (empty body) so they render as section headings,
// and convert inline "🟢 SUOSITELTU" / "🟣 SYVENTÄVÄ" markers into pill tags.
function enhancePanels(){{
  const root=document.getElementById('lesson-panels');
  if(!root) return;
  root.querySelectorAll('.task-card').forEach(c=>{{
    const body=c.querySelector(':scope > .task-card-body');
    if(body && body.children.length===0 && body.textContent.trim()===''){{
      c.classList.add('is-sectionhead');
    }}
  }});
  root.querySelectorAll('h1,h2,h3,h4').forEach(h=>{{
    if(!/SUOSITELTU|SYVENT[ÄA]V[ÄA]/.test(h.textContent)) return;
    h.innerHTML=h.innerHTML
      .replace(/(?:🟢\uFE0F?\s*)?SUOSITELTU/g,'<span class="pill pill--rec">Suositeltu</span>')
      .replace(/(?:🟣\uFE0F?\s*)?SYVENT[ÄA]V[ÄA]/g,'<span class="pill pill--adv">Syventävä</span>');
  }});
}}

// Line-icon SVG map for tab labels (Konsoli reader — no emoji)
const TABICONS={{
  slides:`<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="1.5" y="2.5" width="13" height="9" rx="1.5"/><path d="M8 11.5V14M5.5 14h5" stroke-linecap="round"/></svg>`,
  selfstudy:`<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M8 4.2C8 3.3 6.8 2.5 4.8 2.5 3.2 2.5 2 3 2 3v9s1.2-.5 2.8-.5S8 12.2 8 13M8 4.2C8 3.3 9.2 2.5 11.2 2.5 12.8 2.5 14 3 14 3v9s-1.2-.5-2.8-.5S8 12.2 8 13M8 4.2V13"/></svg>`,
  stasks:`<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><path d="M6.5 4H14M6.5 8H14M6.5 12H14M2 4l.9.9L4.6 3M2 8l.9.9L4.6 7M2 12l.9.9L4.6 11"/></svg>`,
  vocab:`<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M3 3.5A1.5 1.5 0 014.5 2H13v9.5H4.5A1.5 1.5 0 003 13V3.5z"/><path d="M3 13a1.5 1.5 0 011.5-1.5H13V14H4.5A1.5 1.5 0 013 12.5"/></svg>`,
  tltasks:`<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="5.8" cy="5" r="2.1"/><path d="M2.5 13c0-2 1.5-3.2 3.3-3.2S9.1 11 9.1 13" stroke-linecap="round"/><path d="M10.6 3.5A2 2 0 0113 5.4a2 2 0 01-1.3 1.9M11 9.9c1.5.3 2.5 1.5 2.5 3.1" stroke-linecap="round"/></svg>`,
  tmats:`<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><rect x="3" y="3" width="10" height="11" rx="1.5"/><path d="M6 3.2V2.2h4v1M6 7h4M6 10h2.5" stroke-linecap="round"/></svg>`,
  brief:`<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M8 1.7l1.7 3.6 3.9.5-2.9 2.7.8 3.9L8 12.6 4.5 14.6l.8-3.9L2.4 6.3l3.9-.5z"/></svg>`
}};

function loadBrief(ospId,pushState){{
  const b=BRIEFS[ospId];if(!b)return;
  cid='brief-'+ospId;ctab='brief';
  document.getElementById('home').style.display='none';
  document.getElementById('lesson').classList.add('active');
  if(pushState!==false){{ history.pushState(null,'','#brief-'+ospId); }}
  document.getElementById('lesson-header').innerHTML=`
    <div class="breadcrumb">
      <span class="bc-link" onclick="showHome()">${{b.ospTitle}}</span>
      <span>›</span>
      <span>Lopputyön tehtävänanto</span>
    </div>
    <div class="lesson-title">★ Lopputyön tehtävänanto</div>
    <div class="lesson-badges">
      <span class="badge badge-osp">${{b.ospTitle}}</span>
      <span class="badge badge-assess">★ Arviointi</span>
    </div>`;
  document.getElementById('lesson-tabs').innerHTML='';
  document.getElementById('lesson-panels').innerHTML=
    `<div class="panel active" data-tab="brief">${{b.content}}</div>`;
  enhancePanels();
  document.getElementById('lesson-footer').innerHTML=`
    <div class="nav-buttons">
      <button class="btn" onclick="showHome()">← Takaisin etusivulle</button>
    </div>`;
  window.scrollTo(0,0);
  mermaid.run({{querySelector:'.panel.active .mermaid'}});
}}

function getDone(){{try{{return JSON.parse(localStorage.getItem('bcai-new')||'[]')}}catch{{return[]}}}}
function setDone(a){{try{{localStorage.setItem('bcai-new',JSON.stringify(a))}}catch{{}}}}
function isDone(id){{return getDone().includes(id)}}
function toggleDone(id){{const a=getDone(),i=a.indexOf(id);if(i>=0)a.splice(i,1);else a.push(id);setDone(a);updProg();updCards();updDoneBtn(id);}}
function updDoneBtn(id){{const btn=document.querySelector('.done-btn');if(!btn)return;const d=isDone(id);btn.classList.toggle('marked',d);btn.textContent=d?'✓ Suoritettu':'Merkitse suoritetuksi';}}

function updProg(){{
  const done=getDone(),n=ALLIDS.filter(id=>done.includes(id)).length;
  document.getElementById('pb').style.width=(n/ALLIDS.length*100)+'%';
  document.getElementById('pt').textContent=n+'/'+ALLIDS.length;
  const dc=document.getElementById('done-cnt');if(dc)dc.textContent=Math.round(n/ALLIDS.length*100)+'%';
}}

function updCards(){{
  const done=getDone();
  OSPM.forEach(o=>{{
    const ids=o.ids,c=ids.filter(id=>done.includes(id)).length;
    const pf=document.getElementById('pfill-'+o.id);
    const pt=document.getElementById('ptxt-'+o.id);
    if(pf)pf.style.width=(c/ids.length*100)+'%';
    if(pt)pt.textContent=c+' / '+ids.length;
    ids.forEach(id=>{{
      const btn=document.querySelector(`[onclick="loadLesson('${{id}}')"]`);
      if(!btn)return;
      btn.classList.toggle('done',done.includes(id));
    }});
  }});
}}

function toggleAcc(el){{
  const head=el;
  const lessons=head.nextElementSibling;
  head.classList.toggle('open');
  lessons.classList.toggle('open');
}}

function showHome(pushState){{
  document.getElementById('home').style.display='block';
  document.getElementById('lesson').classList.remove('active');
  cid=null;
  if(pushState!==false) history.pushState(null,'',location.pathname);
  updProg();
  window.scrollTo(0,0);
}}

function loadLesson(id,tab,pushState){{
  const d=L[id];if(!d)return;
  const defTab=(d.slides&&d.slides.length>0)?'slides':'selfstudy';
  cid=id;ctab=tab||defTab;
  document.getElementById('home').style.display='none';
  document.getElementById('lesson').classList.add('active');
  const idx=ALLIDS.indexOf(id),num=idx+1,isA=d.blockType==='assessment';
  if(pushState!==false){{
    const hash=(ctab==='selfstudy'||ctab==='slides')?'#'+id:'#'+id+'/'+ctab;
    history.pushState(null,'',hash);
  }}

  document.getElementById('lesson-header').innerHTML=`
    <div class="breadcrumb">
      <span class="bc-link" onclick="showHome()">${{d.ospTitle}}</span>
      <span>›</span>
      <span>Oppitunti ${{num}}</span>
    </div>
    <div class="lesson-title">${{d.shortTitle}}</div>
    <div class="lesson-badges">
      <span class="badge badge-osp">${{d.ospTitle}}</span>
      <span class="badge ${{isA?'badge-assess':'badge-type'}}">${{isA?'★ Arviointi':'~90 min'}}</span>
    </div>`;

  const hasSlides=d.slides&&d.slides.length>0;
  const tabs=isA
    ?[...(hasSlides?[['slides','Diat']]:[]),['selfstudy','Arviointitehtävä'],['stasks','Tehtävä'],['tmats','Opettajan opas']]
    :[...(hasSlides?[['slides','Diat']]:[]),['selfstudy','Itseopiskelumateriaali'],['stasks','Opiskelutehtävät'],['vocab','Sanasto'],['tltasks','Opettajavetoiset tehtävät'],['tmats','Opettajan materiaali']];

  const tabNames=tabs.map(t=>t[0]);
  document.getElementById('lesson-tabs').innerHTML=tabs.map(([tid,lbl])=>
    `<button class="tab-btn ${{tid===ctab?'active':''}}" onclick="showTab('${{tid}}',this)">${{TABICONS[tid]||''}}<span>${{lbl}}</span></button>`
  ).join('');

  document.getElementById('lesson-panels').innerHTML=tabs.map(([tid])=>
    `<div class="panel ${{tid===ctab?'active':''}}" data-tab="${{tid}}">${{d[tid]||'<p>(Sisältöä ei ole saatavilla)</p>'}}</div>`
  ).join('');
  enhancePanels();

  document.getElementById('lesson-footer').innerHTML=`
    <div class="nav-buttons">
      <button class="btn" onclick="nav(-1)" ${{idx===0?'disabled':''}}>← Edellinen</button>
      <button class="btn btn-primary" onclick="nav(1)" ${{idx===ALLIDS.length-1?'disabled':''}}>Seuraava →</button>
    </div>
    <button class="done-btn ${{isDone(id)?'marked':''}}" onclick="toggleDone('${{id}}')">
      ${{isDone(id)?'✓ Suoritettu':'Merkitse suoritetuksi'}}
    </button>`;
  window.scrollTo(0,0);
  mermaid.run({{querySelector:'.panel.active .mermaid'}});
}}

function showTab(name,btn,pushState){{
  ctab=name;
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(t=>t.classList.remove('active'));
  const panels=document.querySelectorAll('.panel');
  const tabs=document.querySelectorAll('.tab-btn');
  if(btn){{
    const tabIdx=Array.from(tabs).indexOf(btn);
    if(tabIdx>=0&&panels[tabIdx]){{
      panels[tabIdx].classList.add('active');
      btn.classList.add('active');
    }}
  }}else{{
    // Find tab by name (for hash navigation)
    const panel=document.querySelector(`.panel[data-tab="${{name}}"]`);
    if(panel)panel.classList.add('active');
    const tabBtns=Array.from(tabs);
    const panelArr=Array.from(panels);
    const pi=panelArr.indexOf(panel);
    if(pi>=0&&tabBtns[pi])tabBtns[pi].classList.add('active');
  }}
  if(pushState!==false&&cid){{
    const hash=(name==='selfstudy'||name==='slides')?'#'+cid:'#'+cid+'/'+name;
    history.pushState(null,'',hash);
  }}
  document.getElementById('lesson-panels').scrollTop=0;
  mermaid.run({{querySelector:'.panel.active .mermaid'}});
}}

function nav(dir){{
  const i=ALLIDS.indexOf(cid),next=ALLIDS[i+dir];
  if(next)loadLesson(next);
}}

function routeFromHash(pushState){{
  const h=location.hash.replace('#','');
  if(!h){{ showHome(false); return; }}
  // Brief route: #brief-osp1, #brief-osp2, #brief-osp3
  if(h.startsWith('brief-')){{
    const ospId=h.slice(6);
    if(BRIEFS[ospId]){{ loadBrief(ospId,false); return; }}
    showHome(false); return;
  }}
  const parts=h.split('/');
  const lid=parts[0],tab=parts[1]||'selfstudy';
  if(L[lid]){{ loadLesson(lid,tab,pushState===true?true:false); }}
  else{{ showHome(false); }}
}}

function deckFull(btn){{
  var w=btn.closest('.deck-wrap'); if(!w) return;
  var fs=document.fullscreenElement||document.webkitFullscreenElement;
  if(!fs){{ (w.requestFullscreen||w.webkitRequestFullscreen).call(w); }}
  else {{ (document.exitFullscreen||document.webkitExitFullscreen).call(document); }}
}}
function deckFullSync(){{
  var fs=document.fullscreenElement||document.webkitFullscreenElement;
  document.querySelectorAll('.deck-full-btn').forEach(function(b){{ b.textContent=fs?'⤢ Poistu koko näytöstä':'⛶ Koko näyttö'; }});
}}
document.addEventListener('fullscreenchange',deckFullSync);
document.addEventListener('webkitfullscreenchange',deckFullSync);
document.addEventListener('keydown',function(e){{
  var fe=document.fullscreenElement||document.webkitFullscreenElement;
  if(!fe||!fe.classList||!fe.classList.contains('deck-wrap')) return;
  var d=fe.querySelector('.deck'); if(!d) return;
  if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){{ d.scrollBy({{left:d.clientWidth,behavior:'smooth'}}); e.preventDefault(); }}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){{ d.scrollBy({{left:-d.clientWidth,behavior:'smooth'}}); e.preventDefault(); }}
}});
window.addEventListener('popstate',()=>routeFromHash(false));

// Initial route from hash on page load
updProg();updCards();
routeFromHash(false);
</script>

<footer class="site-footer">© Matti Seise · <a href="https://www.seise.org" target="_blank" rel="noopener">www.seise.org</a></footer>

</body>
</html>'''


if __name__ == '__main__':
    print("Reading lesson content...")
    data = build_lesson_data()
    print(f"Loaded {len(data)} lessons")
    print("Reading lopputyö briefs...")
    briefs = build_brief_data()
    print(f"Loaded {sum(1 for v in briefs.values() if v)} briefs")
    print("Generating HTML...")
    out = generate_html(data, briefs)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(out)
    size_kb = os.path.getsize(OUT) // 1024
    print(f"Written: {OUT}")
    print(f"Size: {size_kb} KB")
