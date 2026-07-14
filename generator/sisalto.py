"""Sisältöputki: tiedostojen luku, markdown-muunnos, varianttilohkot, task-parseri.

Siirretty sellaisenaan generate_site.py:n v1-versiosta (to_html-putki, task-kortit,
pause-laatikot, mermaid-stash, parse_practice, esc_js) + uudet varianttilohko- ja
lukuaika-apurit rakenneuudistus 2:ta varten.
"""

import os
import re
import json
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


# ===== Lukuaika (kurssi-näkymän kesto) =====

def _strip_markdown(text):
    text = re.sub(r'```.*?```', ' ', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]*`', ' ', text)
    text = re.sub(r'[#>*_\-|=\[\]()!]', ' ', text)
    return text


def word_count(text):
    return len(_strip_markdown(text).split())


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
