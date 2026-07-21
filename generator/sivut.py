"""Sivupohjat: yhteinen kehys + valintasivu, yleiskuva, moduulit, tunnit, sanasto,
lopputyöt ja opettajanäkymä. HTML rakennetaan f-stringeillä; per-sivu-data (CI, ptasks)
serialisoidaan json.dumps:lla, joten f-string-aaltosulkeita ei tarvitse tuplata.
"""

import json
from html import escape
from . import nakymat as N
from . import sisalto as S

DOMAIN = 'https://aiperusteet.fi'

FAVICON = ("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22"
           "%20viewBox%3D%220%200%2024%2024%22%3E%3Ccircle%20cx%3D%2212%22%20cy%3D%2212%22"
           "%20r%3D%2212%22%20fill%3D%22%23FFFFFF%22%2F%3E%3Cg%20transform%3D%22translate"
           "%281.8%2C1.8%29%20scale%280.85%29%22%3E%3Cpath%20d%3D%22M12%2012%20V4.6%20M12"
           "%2012%20L5.6%2017.6%20M12%2012%20L18.4%2017.6%22%20stroke%3D%22%230B0F1A%22"
           "%20stroke-width%3D%221.5%22%20fill%3D%22none%22%2F%3E%3Ccircle%20cx%3D%2212%22"
           "%20cy%3D%2212%22%20r%3D%222.7%22%20fill%3D%22%230B0F1A%22%2F%3E%3Ccircle%20cx"
           "%3D%2212%22%20cy%3D%224.6%22%20r%3D%222.05%22%20fill%3D%22%230B0F1A%22%2F%3E"
           "%3Ccircle%20cx%3D%225.6%22%20cy%3D%2217.6%22%20r%3D%222.05%22%20fill%3D%22"
           "%230B0F1A%22%2F%3E%3Ccircle%20cx%3D%2218.4%22%20cy%3D%2217.6%22%20r%3D%222.05"
           "%22%20fill%3D%22%230B0F1A%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E")

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;'
         '0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Hanken+Grotesk:wght@400;500;600;700&'
         'family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

LOGO_SVG = ('<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M12 12 V4.6 M12 12 L5.6 17.6 M12 12 L18.4 17.6" stroke="currentColor" stroke-width="1.5"/>'
            '<circle cx="12" cy="12" r="2.7" fill="currentColor"/><circle cx="12" cy="4.6" r="2.05" fill="currentColor"/>'
            '<circle cx="5.6" cy="17.6" r="2.05" fill="currentColor"/><circle cx="18.4" cy="17.6" r="2.05" fill="currentColor"/></svg>')

VIEW_META = {
    'kurssi':  {'home': '/kurssi/',  'label': 'Verkkokurssi'},
    'luokka':  {'home': '/luokka/',  'label': 'Luokkaversio'},
    'opettaja': {'home': '/opettaja/', 'label': 'Opettajan opas'},
}

TOTAL = len(N.ALL_IDS)
COURSE = N.KURSSI['kurssi']
AUDIENCE_PROMISE = COURSE['yleisolupaus']
PREREQUISITES = COURSE['esitiedot']
SCOPE_DESCRIPTION = COURSE['laajuuskuvaus']
EDUCATIONAL_LEVEL = COURSE['educational_level']

# Lookup id -> lesson dict (järjestyksessä)
_BY_ID = {l['id']: l for l in N.ALL_LESSONS}


def _topbar():
    return (
        '<nav class="topbar">'
        '<a class="logo-group" href="/" style="text-decoration:none">'
        f'<span class="brand-mark">{LOGO_SVG}</span>'
        '<div class="logo-text"><span class="logo-main">Tekoälyn <b>perusteet</b></span></div>'
        '</a>'
        '<div class="topbar-right">'
        '<div class="progress-bar"><div class="progress-fill" id="pb"></div></div>'
        f'<div class="progress-text" id="pt">0/{TOTAL}</div>'
        '</div></nav>'
    )


CONSENT = (
    '<div id="consent-banner" role="dialog" aria-label="Evästeasetukset" aria-live="polite">'
    '<span>Sivusto käyttää Google Analyticsia kävijätilastointiin. '
    'Analytiikkaevästeet otetaan käyttöön vain hyväksynnälläsi.</span>'
    '<div class="consent-actions">'
    '<button class="consent-accept" onclick="consentChoice(\'granted\')">Hyväksy</button>'
    '<button class="consent-decline" onclick="consentChoice(\'denied\')">Vain välttämättömät</button>'
    '</div></div>'
)

FOOTER = ('<footer class="site-footer">© Matti Seise · Avoin kurssi — saa käyttää ja muokata · '
          'Tekoälykoulutukset organisaatioille: '
          '<a href="https://seise.org/?utm_source=ai-perusteet&utm_medium=referral&utm_campaign=kurssi" '
          'target="_blank" rel="noopener">seise.org</a></footer>')


SITE_NAME = 'AI · Perusteet'
LICENSE_URL = 'https://creativecommons.org/licenses/by-sa/4.0/'
PROVIDER = {'@type': 'Organization', 'name': SITE_NAME, 'url': DOMAIN}


def _jsonld_html(json_ld):
    if not json_ld:
        return ''
    blocks = json_ld if isinstance(json_ld, list) else [json_ld]
    out = []
    for obj in blocks:
        j = json.dumps(obj, ensure_ascii=False).replace('</', '<\\/')
        out.append(f'<script type="application/ld+json">{j}</script>')
    return '\n'.join(out)


def page_shell(title, description, canonical_path, body, ci=None, include_practice=False,
               extra_head='', pre_body_script='', og_type='website', json_ld=None):
    """Rakentaa täyden HTML-dokumentin. ci = dict → window.CI inline-config."""
    ci = ci or {}
    ci.setdefault('allIds', N.ALL_IDS)
    ci_json = json.dumps(ci, ensure_ascii=False).replace('</', '<\\/')
    canonical = DOMAIN + canonical_path
    desc = S.esc_attr(description)
    title_a = S.esc_attr(title)
    social = (
        f'<meta property="og:type" content="{og_type}">'
        f'<meta property="og:site_name" content="{S.esc_attr(SITE_NAME)}">'
        '<meta property="og:locale" content="fi_FI">'
        f'<meta property="og:title" content="{title_a}">'
        f'<meta property="og:description" content="{desc}">'
        f'<meta property="og:url" content="{canonical}">'
        '<meta name="twitter:card" content="summary">'
        f'<meta name="twitter:title" content="{title_a}">'
        f'<meta name="twitter:description" content="{desc}">'
    )
    ld_html = _jsonld_html(json_ld)
    scripts = ['<script src="https://cdn.jsdelivr.net/npm/mermaid@11.12.0/dist/mermaid.min.js"></script>']
    if include_practice:
        scripts.append('<script src="/assets/practice.js"></script>')
    scripts.append(f'<script>window.CI={ci_json};</script>')
    scripts.append('<script src="/assets/site.js"></script>')
    scripts_html = '\n'.join(scripts)
    return f'''<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="google-site-verification" content="40PEbUdB2o-sX8ibIU6TqrFwksYDFy5XrP465BNnVDw">
<title>{title_a}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{social}
{ld_html}
<link rel="icon" type="image/svg+xml" href="{FAVICON}">
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
{extra_head}
</head>
<body>
{pre_body_script}
{_topbar()}
{body}
{FOOTER}
{CONSENT}
{scripts_html}
</body>
</html>'''


# ==================== TUNTISIVUT ====================

def _view_switch(view, kansio):
    if view == 'opettaja':
        opts = [('kurssi', 'Verkkokurssi'), ('luokka', 'Luokkaversio'), ('opettaja', 'Opettajan opas')]
    else:
        opts = [('kurssi', 'Verkkokurssi'), ('luokka', 'Luokkaversio')]
    parts = ['<div class="view-switch"><span class="vs-lab">Näkymä</span>']
    for v, lbl in opts:
        on = ' on' if v == view else ''
        href = f'/{v}/tunti-{kansio}/'
        parts.append(f'<a class="vw{on}" href="{href}" data-view="{v}">{lbl}</a>')
    parts.append('</div>')
    return ''.join(parts)


def _duration_badge(lesson, view):
    is_a = lesson['tyyppi'] == 'assessment'
    if is_a:
        return '<span class="badge badge-assess">★ Arviointi</span>'
    if view == 'kurssi':
        ldir_teoria = S.read_file(N.os.path.join(N.lesson_dir(lesson['kansio']), 'teoria.md'))
        ldir_sanasto = S.read_file(N.os.path.join(N.lesson_dir(lesson['kansio']), 'sanasto.md'))
        mins = S.reading_time_min(ldir_teoria, ldir_sanasto)
        return f'<span class="badge badge-type">Lukuaika n. {mins} min</span>'
    return '<span class="badge badge-type">90 min oppitunti</span>'


def _tunti_label(view, num):
    if view == 'kurssi':
        return f'Osa {num}/{TOTAL}'
    return f'Oppitunti {num}'


def _breadcrumb(view, lesson, num):
    vm = VIEW_META[view]
    module_title = lesson['osp_title']
    if view == 'kurssi':
        mod_link = f'<a class="bc-link" href="/kurssi/{lesson["slug"]}/">{module_title}</a>'
    else:
        mod_link = f'<span>{module_title}</span>'
    return (
        '<div class="breadcrumb">'
        f'<a class="bc-link" href="{vm["home"]}">{vm["label"]}</a>'
        '<span>›</span>'
        f'{mod_link}'
        '<span>›</span>'
        f'<span>{_tunti_label(view, num)}</span>'
        '</div>'
    )


def _thinking_steps(details=None, active=None, labelled_by=None):
    """Renderöi kurssin viisi ajatteluliikettä yhteisestä manifestidatasta."""
    details = details or {}
    label_attr = f' aria-labelledby="{escape(labelled_by)}"' if labelled_by else ''
    items = []
    for move in N.AJATTELU['liikkeet']:
        mid = move['id']
        is_active = mid == active
        active_cls = ' is-active' if is_active else ''
        current = ' aria-current="step"' if is_active else ''
        description = details.get(mid, move['ohje'])
        items.append(
            f'<li class="thinking-step{active_cls}"{current}>'
            f'<span class="thinking-step__name">{escape(move["nimi"])}</span>'
            f'<span class="thinking-step__desc">{escape(description)}</span>'
            '</li>'
        )
    return (
        f'<div class="thinking-path__scroller" role="region" tabindex="0"{label_attr}>'
        f'<ol class="thinking-path__steps">{"".join(items)}</ol>'
        '</div>'
    )


def _course_thinking_path():
    title_id = 'course-thinking-title'
    return (
        '<section class="thinking-path thinking-path--course">'
        '<div class="thinking-path__eyebrow">Kurssin ajattelutapa</div>'
        f'<h2 id="{title_id}">Näin opit ajattelemaan</h2>'
        f'<p class="thinking-path__lead">{escape(N.AJATTELU["lupaus"])}</p>'
        f'{_thinking_steps(labelled_by=title_id)}'
        '</section>'
    )


def _module_thinking_path(osp):
    title_id = f'module-{escape(osp["id"])}-thinking-title'
    return (
        '<section class="thinking-path thinking-path--module">'
        '<div class="thinking-path__eyebrow">Moduulin ajattelukaari</div>'
        f'<h2 id="{title_id}">Tunnistamisesta perusteltuun lopputuotokseen</h2>'
        f'{_thinking_steps(details=osp["ajattelukaari"], labelled_by=title_id)}'
        '</section>'
    )


def _lesson_thinking_path(lesson):
    thought = lesson['ajattelu']
    items = []
    for index, move in enumerate(N.AJATTELU['liikkeet'], 1):
        is_active = move['id'] == thought['painotus']
        active_cls = ' is-active' if is_active else ''
        current = ' aria-current="step"' if is_active else ''
        items.append(
            f'<li class="lesson-thinking-step{active_cls}"{current}>'
            f'<span class="lesson-thinking-step__index" aria-hidden="true">{index}</span>'
            f'<span class="lesson-thinking-step__name">{escape(move["nimi"])}</span>'
            '</li>'
        )
    return (
        '<aside class="thinking-path thinking-path--lesson" aria-label="Ajattelun selkäranka">'
        '<div class="thinking-path__lesson-inner">'
        '<ol class="lesson-thinking-steps" aria-label="Ajattelun vaiheet">'
        f'{"".join(items)}</ol>'
        '<p class="thinking-path__question">'
        '<span class="thinking-path__question-label">Ajattelukysymys</span>'
        f'<span>{escape(thought["kysymys"])}</span></p>'
        '</div></aside>'
    )


def build_tunti_page(lesson, view):
    num = N.ALL_IDS.index(lesson['id']) + 1
    idx = num - 1
    kansio = lesson['kansio']
    is_a = lesson['tyyppi'] == 'assessment'
    blocks = N.build_lesson_blocks(lesson, view)

    # ptasks (harjoittele-lohkon tehtävät)
    ptasks = None
    for b in blocks:
        if b['block'] == 'harjoittele' and b['tasks']:
            ptasks = b['tasks']

    # --- Oppimispolun ohjaus (kurssi/luokka) -------------------------------
    # Ketju johdetaan näkymän OMASTA lohkojärjestyksestä (kurssi.yaml), koska
    # järjestys ja lohkot eroavat näkymittäin: kurssissa työlohkot ovat
    # harjoittele + lopputyon-askel, luokassa tehtavat-luokka + harjoittele
    # (luokan Tehtävät-välilehti sisältää saman osatuotoksen, jonka kurssi-
    # näkymä nostaa omaksi ★-välilehdekseen). Arviointitunneilla 18/27 luokka-
    # näkymän ainoa työlohko on Tehtävät — juuri ne ovat lopputyön palautus-
    # tunnit, joten ne tarvitsevat ohjauksen kaikkein eniten.
    # Pehmeä ohjaus: mitään ei estetä, vain visuaalinen hierarkia elää.
    WORK_BLOCKS = ('tehtavat-luokka', 'harjoittele', 'lopputyon-askel')
    work = ([b for b in blocks if b['block'] in WORK_BLOCKS]
            if view in ('kurssi', 'luokka') else [])
    guide = bool(work)
    next_url = ''
    if idx < TOTAL - 1:
        next_url = f'/{view}/tunti-{N.ALL_LESSONS[idx + 1]["kansio"]}/'

    def _next_card(target, gated):
        """Kortti, joka ohjaa ketjun seuraavaan työlohkoon."""
        blk = target['block']
        if blk == 'harjoittele':
            desc = f'<span data-flow-count>{len(ptasks or [])} tehtävää</span>'
            cta = 'Siirry harjoituksiin →'
        elif blk == 'lopputyon-askel':
            desc = '<span>Osatuotos, joka kerryttää lopputyötäsi</span>'
            cta = 'Avaa lopputyön askel →'
        else:
            desc = ('<span>Tunnin tehtävät — sisältää lopputyön askeleen</span>'
                    if lesson.get('lopputyon_askel')
                    else '<span>Tunnin tehtävät ja tuotokset</span>')
            cta = 'Siirry tehtäviin →'
        attrs = ' data-flow-gate="practice" hidden' if gated else ''
        return (f'<div class="practice-bridge"{attrs}>'
                f'<div class="pb-txt"><b>Seuraavaksi: {target["label"]}</b>{desc}</div>'
                '<button type="button" class="btn btn-primary" '
                f'onclick="showTab(\'{target["anchor"]}\')">{cta}</button></div>')

    def _complete_card(last_block, gated):
        """Ketjun päätekortti: merkintä + seuraava tunti."""
        if last_block == 'lopputyon-askel':
            head, txt = ('Tunnin lopputyöosuus valmis?',
                         'Tallenna osatuotos työkirjaasi — se on osa lopputyötäsi. '
                         'Merkitse tunti sitten suoritetuksi.')
        elif last_block == 'tehtavat-luokka':
            head, txt = ('Tunnin tehtävät tehty?',
                         'Tallenna tuotoksesi työkirjaasi ja merkitse tunti suoritetuksi.')
        else:
            head, txt = ('Kaikki tehtävät tehty ✓',
                         'Hieno työ. Palaa vielä tunnin ajattelukysymykseen ja merkitse '
                         'tunti sitten suoritetuksi.')
        next_a = (f'<a class="btn btn-primary" href="{next_url}">Seuraava tunti →</a>'
                  if next_url else '')
        attrs = ' data-flow-gate="practice" hidden' if gated else ''
        return (f'<div class="practice-complete"{attrs}>'
                f'<b>{head}</b><span>{txt}</span><div class="pc-actions">'
                f'<button type="button" class="done-btn" onclick="toggleDone(\'{lesson["id"]}\')">'
                f'Merkitse suoritetuksi</button>{next_a}</div></div>')

    # Kortti kunkin lohkon loppuun: teoria → 1. työlohko → … → päätekortti.
    # Navigointikortit ovat AINA näkyvissä — lopputyön askel on kurssin
    # suorittamisen kannalta liian tärkeä piilotettavaksi harjoitusten taakse.
    # Portitus koskee vain päätekorttia harjoittelun jälkeen, koska sen väite
    # ("Kaikki tehtävät tehty ✓") on tosi vasta silloin.
    extras = {}
    if guide:
        extras['teoria'] = _next_card(work[0], gated=False)
        for i, b in enumerate(work):
            last = i + 1 >= len(work)
            extras[b['block']] = (_next_card(work[i + 1], gated=False)
                                  if not last
                                  else _complete_card(b['block'],
                                                      gated=b['block'] == 'harjoittele'))

    # Tabit + panelit
    tab_btns, panels = [], []
    for i, b in enumerate(blocks):
        act = ' active' if i == 0 else ''
        selected = 'true' if i == 0 else 'false'
        tabindex = '0' if i == 0 else '-1'
        tab_id = f'tab-{lesson["id"]}-{b["anchor"]}'
        panel_id = f'panel-{lesson["id"]}-{b["anchor"]}'
        count = (' <span class="tab-count" data-practice-tabcount hidden></span>'
                 if guide and b['block'] == 'harjoittele' else '')
        tab_btns.append(
            f'<button id="{tab_id}" class="tab-btn{act}" role="tab" '
            f'aria-selected="{selected}" aria-controls="{panel_id}" tabindex="{tabindex}" '
            f'data-tab="{b["anchor"]}" onclick="showTab(\'{b["anchor"]}\')">'
            f'{b["icon"]}<span>{b["label"]}</span>{count}</button>')
        hidden = '' if i == 0 else ' hidden'
        extra = extras.get(b['block'], '')
        panels.append(
            f'<div id="{panel_id}" class="panel{act}" role="tabpanel" '
            f'aria-labelledby="{tab_id}" data-tab="{b["anchor"]}"{hidden}>{b["html"]}{extra}</div>')

    header = (
        '<div id="lesson-header" class="lesson-header">'
        f'{_breadcrumb(view, lesson, num)}'
        f'<div class="lesson-title">{lesson["otsikko"]}</div>'
        '<div class="lesson-badges">'
        f'<span class="badge badge-osp">{lesson["osp_title"]}</span>'
        f'{_duration_badge(lesson, view)}'
        '</div>'
        f'{_view_switch(view, kansio)}'
        '</div>'
    )

    # Opettajan jakostrippi
    strip = ''
    if view == 'opettaja':
        luokka_url = f'/luokka/tunti-{kansio}/'
        strip = (
            '<div class="lesson-strip"><div class="share-box">'
            '<div class="sb-txt"><b>Jaa tämä tunti opiskelijoille</b>'
            '<span>Opiskelijat näkevät luokkaversion: teoria, tehtävät, harjoittele, sanasto ja diat.</span></div>'
            f'<a class="sb-go" href="{luokka_url}" data-view="luokka">Avaa luokkaversio →</a>'
            f'<button type="button" onclick="copyShare(this)" data-url="{luokka_url}">Kopioi linkki</button>'
            '</div></div>'
        )

    # Footer: nav + (kurssi/luokka) merkitse suoritetuksi
    prev_html = '<button class="btn" disabled>← Edellinen</button>'
    next_html = '<button class="btn btn-primary" disabled>Seuraava →</button>'
    if idx > 0:
        p = N.ALL_LESSONS[idx - 1]
        prev_html = f'<a class="btn" href="/{view}/tunti-{p["kansio"]}/">← Edellinen</a>'
    if idx < TOTAL - 1:
        nx = N.ALL_LESSONS[idx + 1]
        next_html = f'<a class="btn btn-primary" href="/{view}/tunti-{nx["kansio"]}/">Seuraava →</a>'
    done_html = ''
    if view in ('kurssi', 'luokka'):
        done_html = (f'<button class="done-btn" onclick="toggleDone(\'{lesson["id"]}\')">'
                     'Merkitse suoritetuksi</button>')
    chip_html = ''
    if guide and ptasks:  # chip näyttää mitattavan Harjoittele-tilan
        chip_html = ('<button type="button" class="practice-chip" data-practice-chip hidden '
                     'onclick="showTab(\'harjoittele\')">Harjoittele · '
                     '<span data-practice-chip-count></span></button>')
    footer = (
        '<div id="lesson-footer" class="lesson-footer">'
        f'<div class="nav-buttons">{prev_html}{next_html}</div>'
        f'{chip_html}{done_html}'
        '</div>'
    )

    body = (
        '<div id="lesson" class="lesson-view active">'
        f'{header}{_lesson_thinking_path(lesson)}{strip}'
        f'<div id="lesson-tabs" class="lesson-tabs" role="tablist" aria-label="Oppitunnin sisältö">{"".join(tab_btns)}</div>'
        f'<div id="lesson-panels" class="lesson-panels rv-tech">{"".join(panels)}</div>'
        f'{footer}</div>'
    )

    ci = {'view': view, 'lid': lesson['id'], 'num': num, 'title': lesson['otsikko']}
    if ptasks is not None:
        ci['ptasks'] = ptasks
    vm = VIEW_META[view]
    title = f'{lesson["otsikko"]} — {vm["label"]} — AI · Perusteet'
    # Meta description: teorian ensimmäinen leipätekstikappale (SEO); jos puuttuu, geneerinen.
    variant = N.NAKYMAT[view]['lopputyo_variantti']
    teoria_raw = S.read_file(N.os.path.join(N.lesson_dir(kansio), 'teoria.md'))
    teoria_txt = S.filter_variants(teoria_raw, variant, source=f'tunnit/{kansio}/teoria.md')
    desc = S.excerpt(teoria_txt, 160) or (
        f'{lesson["otsikko"]}. {vm["label"]}, AI · Perusteet -verkkokurssi tekoälyn perusteista.')
    canonical = f'/{view}/tunti-{kansio}/'
    json_ld = _tunti_jsonld(lesson, view, num, canonical, desc)
    return page_shell(title, desc, canonical, body, ci=ci, include_practice=(ptasks is not None),
                      og_type='article', json_ld=json_ld)


def _tunti_jsonld(lesson, view, num, canonical, desc):
    """LearningResource + BreadcrumbList tuntisivulle."""
    vm = VIEW_META[view]
    learning = {
        '@context': 'https://schema.org',
        '@type': 'LearningResource',
        'name': lesson['otsikko'],
        'description': desc,
        'url': DOMAIN + canonical,
        'isPartOf': {'@type': 'Course', 'name': SITE_NAME, 'url': f'{DOMAIN}/kurssi/'},
        'inLanguage': 'fi',
        'license': LICENSE_URL,
        'isAccessibleForFree': True,
        'educationalLevel': EDUCATIONAL_LEVEL,
        'learningResourceType': ('Arviointitehtävä' if lesson['tyyppi'] == 'assessment' else 'Oppitunti'),
    }
    crumbs = [{'@type': 'ListItem', 'position': 1, 'name': vm['label'], 'item': DOMAIN + vm['home']}]
    if view == 'kurssi':
        crumbs.append({'@type': 'ListItem', 'position': 2, 'name': lesson['osp_title'],
                       'item': f'{DOMAIN}/kurssi/{lesson["slug"]}/'})
    else:
        crumbs.append({'@type': 'ListItem', 'position': 2, 'name': lesson['osp_title']})
    crumbs.append({'@type': 'ListItem', 'position': 3, 'name': _tunti_label(view, num)})
    breadcrumb = {'@context': 'https://schema.org', '@type': 'BreadcrumbList',
                  'itemListElement': crumbs}
    return [learning, breadcrumb]


# ==================== VALINTASIVU (etusivu) ====================

def build_redirect_map():
    """Vanha hash → uusi URL, generoituna kurssi.yaml:n NN-silmukasta (redirectit.md)."""
    m = {
        'brief-osp1': '/kurssi/teoria/lopputyo/',
        'brief-osp2': '/kurssi/kaytto/lopputyo/',
        'brief-osp3': '/kurssi/agentit/lopputyo/',
    }
    for l in N.ALL_LESSONS:
        nn = l['kansio']
        lid = l['id']
        is_a = l['tyyppi'] == 'assessment'
        m[lid] = f'/kurssi/tunti-{nn}/'
        m[f'{lid}/selfstudy'] = f'/kurssi/tunti-{nn}/'
        m[f'{lid}/stasks'] = f'/luokka/tunti-{nn}/#tehtavat'
        m[f'{lid}/slides'] = f'/luokka/tunti-{nn}/#diat'
        m[f'{lid}/tmats'] = f'/opettaja/tunti-{nn}/'
        if is_a:
            # arviointitunneilta ei ole koskaan syntynyt näitä — kuten tuntematon tab
            m[f'{lid}/practice'] = f'/kurssi/tunti-{nn}/'
            m[f'{lid}/vocab'] = f'/kurssi/tunti-{nn}/'
            m[f'{lid}/tltasks'] = f'/kurssi/tunti-{nn}/'
        else:
            m[f'{lid}/practice'] = f'/kurssi/tunti-{nn}/#harjoittele'
            m[f'{lid}/vocab'] = f'/kurssi/tunti-{nn}/#sanasto'
            m[f'{lid}/tltasks'] = f'/opettaja/tunti-{nn}/'
    return m


def build_index_page():
    redir = build_redirect_map()
    redir_json = json.dumps(redir, ensure_ascii=False)
    # Hash-ohjaus ENNEN sisällön renderöintiä (ja ennen GA-latausta).
    pre = (
        '<script>(function(){'
        f'var R={redir_json};'
        'var h=location.hash.replace(/^#/,"");'
        'if(!h)return;'
        'if(R[h]){location.replace(R[h]);return;}'
        'var m=h.match(/^(lesson-\\d{2})\\//);'
        'if(m&&R[m[1]]){location.replace(R[m[1]]);return;}'
        '})();</script>'
    )
    doors = (
        '<div class="doors">'
        '<a class="door door--primary" href="/kurssi/" data-view="kurssi">'
        '<span class="door-ic">📘</span>'
        '<span class="door-title">Opiskele itsenäisesti</span>'
        '<span class="door-desc">Verkkokurssi omaan tahtiin: teoria, itsetarkistuvat harjoitukset ja sanasto. '
        'Etenemisesi tallentuu selaimeesi.</span>'
        '<span class="door-cta">Aloita kurssi →</span></a>'
        '<a class="door" href="/luokka/" data-view="luokka">'
        '<span class="door-ic">👥</span>'
        '<span class="door-title">Opiskele oppitunnilla</span>'
        '<span class="door-desc">Oppitunnin opiskelijaversio: teoria, luokkatehtävät, harjoittele, sanasto ja diat.</span>'
        '<span class="door-cta">Avaa luokkaversio →</span></a>'
        '<a class="door" href="/opettaja/" data-view="opettaja">'
        '<span class="door-ic">🎓</span>'
        '<span class="door-title">Avaa opettajan aineistot</span>'
        '<span class="door-desc">Kurssiopas ja tuntikohtaiset ohjeet: tuntisuunnitelmat, opettajavetoiset tehtävät, '
        'diat esitystilassa ja arviointi.</span>'
        '<span class="door-cta">Avaa opettajan opas →</span></a>'
        '</div>'
    )
    made_note = (
        '<div class="made-note">'
        '<div class="made-note-kn">Miten tämä kurssi on tehty</div>'
        '<p>Koko kurssi on tuotettu tekoälyn avulla. Ensisijaisena kielimallina on käytetty '
        'Clauden eri malleja, mutta työn aikana on hyödynnetty myös ChatGPT:tä sekä avoimia '
        'kielimalleja.</p>'
        '<p>Claude Coworkin ja Hermes-agenttijärjestelmän muodostama agenttiputki käsitteli '
        'jokaisen oppitunnin monivaiheisesti. Se suunnitteli oppitunnin, tuotti sisällön, '
        'arvioi sitä pedagogisesta näkökulmasta ja teki suomen kielenhuollon.</p>'
        '<p>Kurssin tekijä vastasi kokonaisuuden suunnittelusta, ohjasi agenttiprosessia, '
        'teki tarvittavat muutokset ja hyväksyi jokaisen oppitunnin ennen sen julkaisemista. '
        'Myös tämä verkkosivusto on rakennettu tekoälyn avulla.</p>'
        '<p>Materiaali tarkistetaan ennen julkaisemista, mutta myös tarkistettuun aineistoon '
        'kannattaa suhtautua kriittisesti. Ilmoita havaitsemastasi virheestä tekijälle ja varmista '
        'ajankohtaiset tiedot alkuperäislähteestä. <strong><em>Kriittinen tekoälyn lukutaito on yksi '
        'kurssin keskeisistä tavoitteista.</em></strong></p>'
        '</div>'
    )
    lic_footer = (
        '<footer class="license-footer">'
        '<p>Sisältö on lisensoitu <a href="' + LICENSE_URL + 'deed.fi" '
        'rel="license noopener" target="_blank">Creative Commons Nimeä-JaaSamoin 4.0 '
        '(CC BY-SA 4.0)</a> -lisenssillä — saat käyttää, jakaa ja muokata materiaalia, '
        'kunhan mainitset tekijän ja jaat johdannaiset samalla lisenssillä.</p>'
        '</footer>'
    )
    body = (
        # --intro: kahden palstan hero (ks. site.css) — vain etusivulla
        '<section class="page-hero page-hero--intro"><div class="page-hero-inner">'
        '<div class="eyebrow">AI · Perusteet</div>'
        '<h1>Ymmärrä tekoäly teoriasta agentteihin.</h1>'
        f'<p>{AUDIENCE_PROMISE}</p>'
        f'<p>{SCOPE_DESCRIPTION}</p>'
        '</div></section>'
        '<div class="valinta">'
        '<div class="valinta-lead"><p>Sama kurssi on käytettävissä kolmella tavalla: itsenäiseen '
        'opiskeluun, oppitunnille ja opetuksen suunnitteluun. Valitse sinulle sopiva vaihtoehto. '
        'Voit vaihtaa näkymää myöhemmin.</p></div>'
        f'{doors}'
        f'{made_note}'
        '</div>'
        f'{lic_footer}'
    )
    return page_shell(
        'AI · Perusteet — tekoälyn perusteet -verkkokurssi',
        AUDIENCE_PROMISE,
        '/', body, pre_body_script=pre,
        json_ld=_course_jsonld(f'{DOMAIN}/'))


def _course_jsonld(url):
    """schema.org Course etusivulle ja /kurssi/-yleiskuvalle."""
    return {
        '@context': 'https://schema.org',
        '@type': 'Course',
        'name': SITE_NAME,
        'description': AUDIENCE_PROMISE,
        'url': url,
        'provider': PROVIDER,
        'inLanguage': 'fi',
        'isAccessibleForFree': True,
        'license': LICENSE_URL,
        'educationalLevel': EDUCATIONAL_LEVEL,
        'coursePrerequisites': PREREQUISITES,
        'hasCourseInstance': {'@type': 'CourseInstance', 'courseMode': 'online',
                              'courseWorkload': 'PT40H', 'inLanguage': 'fi'},
    }


# ==================== KURSSI: YLEISKUVA + MODUULIT ====================

def build_kurssi_overview():
    cards = []
    for osp in N.OSP_BLOCKS:
        ids = ','.join(lid for lid, _, _, _ in osp['lessons'])
        n = len(osp['lessons'])
        cards.append(
            f'<a class="mod-card" href="/kurssi/{osp["slug"]}/" style="--osp-color:{osp["color"]}">'
            f'<div class="mod-kn">{osp["ikoni_kn"]}</div>'
            f'<div class="mod-title">{osp["title"]}</div>'
            f'<div class="mod-sub">{osp["subtitle"]}</div>'
            '<div class="mod-foot">'
            f'<div class="prog-bar"><div class="prog-fill" data-ospfill="{osp["id"]}" '
            f'data-ids="{ids}" style="background:{osp["color"]}"></div></div>'
            f'<span class="mod-count"><span data-osptxt="{osp["id"]}">0 / {n}</span></span>'
            '</div></a>'
        )
    intro_path = N.os.path.join(N.SISALTO, 'aloitus.md')
    intro = S.to_html(S.read_file(intro_path))
    body = (
        '<section class="page-hero"><div class="page-hero-inner">'
        '<div class="eyebrow">Verkkokurssi</div>'
        '<h1>AI · Perusteet</h1>'
        f'<p>{AUDIENCE_PROMISE}</p>'
        '</div></section>'
        '<div class="page-body">'
        f'<div class="reading panel active course-start">{intro}</div>'
        f'{_course_thinking_path()}'
        f'<div class="mod-grid">{"".join(cards)}</div>'
        '</div>'
    )
    return page_shell('AI · Perusteet — verkkokurssi',
                      AUDIENCE_PROMISE,
                      '/kurssi/', body,
                      json_ld=_course_jsonld(f'{DOMAIN}/kurssi/'))


def build_kurssi_module(osp):
    rows = []
    for lid, title, btype, kansio in osp['lessons']:
        num = N.ALL_IDS.index(lid) + 1
        star = '★' if btype == 'assessment' else num
        rows.append(
            f'<a class="ll-row" href="/kurssi/tunti-{kansio}/" style="--osp-color:{osp["color"]}">'
            f'<span class="ll-num">{star}</span>'
            f'<span class="ll-title">{title}</span>'
            f'<span class="ll-done" data-doneid="{lid}"></span>'
            '</a>'
        )
    final = ''
    if osp.get('lopputyo'):
        final = (
            f'<a class="final-cta" href="/kurssi/{osp["slug"]}/lopputyo/">'
            '<span class="fc-star">★</span>'
            '<span class="fc-txt"><b>Osion lopputyö</b>'
            '<span>Kokoa oppimasi — itsearvioitava lopputyö tähän kokonaisuuteen.</span></span>'
            '</a>'
        )
    body = (
        '<section class="page-hero"><div class="page-hero-inner">'
        f'<div class="eyebrow"><a class="bc-link" href="/kurssi/" style="color:var(--blue)">Verkkokurssi</a> · {osp["ikoni_kn"]}</div>'
        f'<h1>{osp["title"]}</h1>'
        f'<p>{osp["subtitle"]}</p>'
        '</div></section>'
        '<div class="page-body">'
        f'{_module_thinking_path(osp)}'
        f'<div class="lesson-list" style="--osp-color:{osp["color"]}">{"".join(rows)}</div>'
        f'{final}'
        '</div>'
    )
    return page_shell(f'{osp["title"]} — AI · Perusteet',
                      f'{osp["title"]}: {osp["subtitle"]}. Tekoälyn perusteet -verkkokurssin osa.',
                      f'/kurssi/{osp["slug"]}/', body)


# ==================== LUOKKA: INDEKSI ====================

def build_luokka_index():
    groups = []
    for osp in N.OSP_BLOCKS:
        rows = []
        for lid, title, btype, kansio in osp['lessons']:
            num = N.ALL_IDS.index(lid) + 1
            star = '★' if btype == 'assessment' else num
            rows.append(
                f'<a class="ll-row" href="/luokka/tunti-{kansio}/" style="--osp-color:{osp["color"]}">'
                f'<span class="ll-num">{star}</span>'
                f'<span class="ll-title">{title}</span>'
                f'<span class="ll-done" data-doneid="{lid}"></span></a>'
            )
        final = ''
        if osp.get('lopputyo'):
            final = (f'<a class="final-cta" href="/luokka/{osp["slug"]}/lopputyo/">'
                     '<span class="fc-star">★</span>'
                     '<span class="fc-txt"><b>Osion lopputyö</b>'
                     '<span>Lopputyön tehtävänanto ja palautus.</span></span></a>')
        groups.append(
            f'<div class="ll-group-title">{osp["ikoni_kn"]} · {osp["title"]}</div>'
            f'<div class="lesson-list" style="--osp-color:{osp["color"]}">{"".join(rows)}</div>'
            f'{final}'
        )
    body = (
        '<section class="page-hero"><div class="page-hero-inner">'
        '<div class="eyebrow">Luokkaversio</div>'
        '<h1>Oppituntien opiskelijaversio</h1>'
        '<p>Valitse oppitunti. Jokainen tunti sisältää teorian, luokkatehtävät, harjoittelun, '
        'sanaston ja diat.</p>'
        '</div></section>'
        f'<div class="page-body">{"".join(groups)}</div>'
    )
    return page_shell('AI · Perusteet — luokkaversio',
                      'Tekoälyn perusteet -kurssin luokkaversio: 27 oppitunnin opiskelijamateriaalit.',
                      '/luokka/', body)


# ==================== LOPPUTYÖSIVUT ====================

def build_lopputyo_page(osp, view):
    html = N.lopputyo_html(osp, view)
    vm = VIEW_META[view]
    body = (
        '<section class="page-hero"><div class="page-hero-inner">'
        f'<div class="eyebrow"><a class="bc-link" href="{vm["home"]}" style="color:var(--blue)">{vm["label"]}</a> · '
        f'{osp["title"]}</div>'
        '<h1>★ Osion lopputyö</h1>'
        f'<p>{osp["title"]} — {osp["subtitle"]}.</p>'
        '</div></section>'
        '<div class="page-body"><div class="reading panel active">'
        f'{html}'
        '</div></div>'
    )
    return page_shell(f'Lopputyö — {osp["title"]} — {vm["label"]}',
                      f'{osp["title"]}-osion lopputyön tehtävänanto. {vm["label"]}.',
                      f'/{view}/{osp["slug"]}/lopputyo/', body)


# ==================== SANASTO ====================

import re as _re

# Yksikirjaimiset (tai numero-)väliotsikot ovat aakkosjaottimia, eivät termejä.
# Ne esiintyvät arviointituntien (18, 27) yhteenvetosanastoissa, joiden termit ovat
# jo teoriatunneilla — koottu sanasto rakennetaan vain kanonisesta '## Termi' -muodosta.
_SANASTO_DIVIDER = _re.compile(r'^[A-ZÅÄÖ0-9]$')


def _parse_sanasto(kansio):
    raw = S.read_file(N.os.path.join(N.lesson_dir(kansio), 'sanasto.md'))
    terms = []
    cur_term = None
    cur_body = []

    def flush():
        if cur_term is not None:
            terms.append((cur_term, '\n'.join(cur_body).strip()))

    for line in raw.split('\n'):
        st = line.strip()
        if st.startswith('## '):
            flush()
            name = st[3:].strip()
            if _SANASTO_DIVIDER.match(name):
                cur_term = None   # aakkosjaotin — ohitetaan
            else:
                cur_term = name
            cur_body = []
        elif st == '---' or st.startswith('# '):
            continue
        else:
            if cur_term is not None:
                cur_body.append(line)
    flush()
    return terms


def build_sanasto_page():
    entries = []
    seen = set()
    # Teoriatunnit ensin, arviointitunnit viimeisenä → linkki osoittaa opetustuntiin.
    ordered = ([l for l in N.ALL_LESSONS if l['tyyppi'] != 'assessment'] +
               [l for l in N.ALL_LESSONS if l['tyyppi'] == 'assessment'])
    for l in ordered:
        num = N.ALL_IDS.index(l['id']) + 1
        for term, definition in _parse_sanasto(l['kansio']):
            key = term.lower()
            if key in seen:
                continue
            seen.add(key)
            entries.append((term, definition, l['kansio'], num))
    entries.sort(key=lambda e: e[0].lower())
    items = []
    for term, definition, kansio, num in entries:
        dhtml = S.to_html(definition)
        items.append(
            '<div class="sanasto-term">'
            f'<h2>{term}</h2>'
            f'{dhtml}'
            f'<a class="st-src" href="/kurssi/tunti-{kansio}/#sanasto">Osa {num}/{TOTAL}</a>'
            '</div>'
        )
    body = (
        '<section class="page-hero"><div class="page-hero-inner">'
        '<div class="eyebrow">Sanasto</div>'
        '<h1>Tekoälyn perusteet — sanasto</h1>'
        f'<p>Koko kurssin käsitteet aakkosjärjestyksessä ({len(entries)} termiä). '
        'Jokainen termi linkittää siihen tuntiin, jossa se opitaan.</p>'
        '</div></section>'
        f'<div class="page-body"><div class="reading">{"".join(items)}</div></div>'
    )
    terms_ld = [
        {'@type': 'DefinedTerm', 'name': term, 'description': S.excerpt(definition, 200),
         'inLanguage': 'fi'}
        for term, definition, _kansio, _num in entries
    ]
    dts = {
        '@context': 'https://schema.org',
        '@type': 'DefinedTermSet',
        'name': 'Tekoälyn perusteet — sanasto',
        'url': f'{DOMAIN}/sanasto/',
        'inLanguage': 'fi',
        'license': LICENSE_URL,
        'hasDefinedTerm': terms_ld,
    }
    return page_shell('Tekoälyn sanasto — AI · Perusteet',
                      'Tekoälyn perusteet -kurssin koottu sanasto: kaikki keskeiset käsitteet '
                      'aakkosjärjestyksessä ja linkit oppitunteihin.',
                      '/sanasto/', body, json_ld=dts)


# ==================== OPETTAJA: KURSSIOPAS + ARVIOINTI ====================

def build_opettaja_index():
    import os as _os
    guide_path = N.os.path.join(N.SISALTO, 'opettaja', 'kurssiopas.md')
    if _os.path.exists(guide_path) and S.read_file(guide_path).strip():
        content = S.to_html(S.filter_variants(S.read_file(guide_path), 'opettaja', source='opettaja/kurssiopas.md'))

        # Kurssioppaan jälkeen: opettajan tuntimateriaalit moduuleittain.
        mat_groups = []
        for osp in N.OSP_BLOCKS:
            rows = []
            for lid, title, btype, kansio in osp['lessons']:
                num = N.ALL_IDS.index(lid) + 1
                star = '★' if btype == 'assessment' else num
                label = f'Oppitunti {num}: {title}'
                rows.append(
                    f'<a class="ll-row" href="/opettaja/tunti-{kansio}/" style="--osp-color:{osp["color"]}">'
                    f'<span class="ll-num">{star}</span>'
                    f'<span class="ll-title">{label}</span></a>'
                )
            mat_groups.append(
                f'<div class="ll-group-title">{osp["ikoni_kn"]} · {osp["title"]} — {osp["subtitle"]}</div>'
                f'<div class="lesson-list" style="--osp-color:{osp["color"]}">{"".join(rows)}</div>'
            )
        materials = (
            '<h2 style="font-family:var(--font-serif);font-size:26px;margin:36px 0 8px">'
            'Opettajan materiaalit tunneittain</h2>'
            '<p>Kunkin tunnin opettajan tuntisivu sisältää tuntisuunnitelman, '
            'väärinkäsityslistat ja opettajavetoiset tehtävät.</p>'
            f'{"".join(mat_groups)}'
            '<a class="final-cta" href="/opettaja/arviointi/">'
            '<span class="fc-star">★</span><span class="fc-txt"><b>Arviointi</b>'
            '<span>Lopputöiden arviointiohjeet koottuna.</span></span></a>'
        )

        body = (
            '<section class="page-hero"><div class="page-hero-inner">'
            '<div class="eyebrow">Opettajan opas</div>'
            '<h1>Kurssiopas</h1>'
            '</div></section>'
            f'<div class="page-body"><div class="reading panel active">{content}</div>'
            f'{materials}</div>'
        )
        return page_shell('Opettajan opas — AI · Perusteet',
                          'Tekoälyn perusteet -kurssin opettajan kurssiopas: toteutus, arviointi ja materiaalit.',
                          '/opettaja/', body)

    # Siisti runko (vaihe 4 tuo varsinaisen sisällön)
    mod_lists = []
    for osp in N.OSP_BLOCKS:
        rows = []
        for lid, title, btype, kansio in osp['lessons']:
            num = N.ALL_IDS.index(lid) + 1
            star = '★' if btype == 'assessment' else num
            rows.append(
                f'<a class="ll-row" href="/opettaja/tunti-{kansio}/" style="--osp-color:{osp["color"]}">'
                f'<span class="ll-num">{star}</span>'
                f'<span class="ll-title">{title}</span></a>'
            )
        mod_lists.append(
            f'<div class="ll-group-title">{osp["ikoni_kn"]} · {osp["title"]} — {osp["subtitle"]}</div>'
            f'<div class="lesson-list" style="--osp-color:{osp["color"]}">{"".join(rows)}</div>'
        )
    body = (
        '<section class="page-hero"><div class="page-hero-inner">'
        '<div class="eyebrow">Opettajan opas</div>'
        '<h1>Kurssiopas</h1>'
        f'<p>{AUDIENCE_PROMISE}</p><p>{SCOPE_DESCRIPTION}</p>'
        '</div></section>'
        '<div class="page-body">'
        '<div class="info-note"><b>Kurssiopas täydentyy.</b> Toteutusmallit, jaksotus, '
        'Itslearning-vienti ja lataamo (pptx-kannet, tulosteet) lisätään tähän myöhemmin. '
        'Alta pääset jo tuntikohtaisiin opettajan materiaaleihin ja arviointiohjeisiin.</div>'
        '<a class="final-cta" href="/opettaja/arviointi/">'
        '<span class="fc-star">★</span><span class="fc-txt"><b>Arviointi</b>'
        '<span>Lopputöiden arviointiohjeet koottuna.</span></span></a>'
        '<h2 style="font-family:var(--font-serif);font-size:26px;margin:16px 0 4px">Kurssirakenne</h2>'
        f'{"".join(mod_lists)}'
        '</div>'
    )
    return page_shell('Opettajan opas — AI · Perusteet',
                      'Tekoälyn perusteet -kurssin opettajan opas: kurssirakenne, tuntikohtaiset '
                      'materiaalit ja lopputöiden arviointiohjeet.',
                      '/opettaja/', body)


def build_opettaja_arviointi():
    sections = []
    for osp in N.OSP_BLOCKS:
        html = N.lopputyo_html(osp, 'opettaja')
        if not html:
            continue
        sections.append(
            f'<h2 style="font-family:var(--font-serif);font-size:26px;margin:36px 0 8px">'
            f'{osp["ikoni_kn"]} · {osp["title"]} — lopputyö</h2>'
            f'<div class="reading panel active">{html}</div>'
        )
    # Tunnin 18 arviointiohje
    ao_path = N.os.path.join(N.lesson_dir('18'), 'opettaja', 'arviointiohje.md')
    ao_raw = S.read_file(ao_path)
    if ao_raw.strip():
        sections.append(
            '<h2 style="font-family:var(--font-serif);font-size:26px;margin:36px 0 8px">'
            'Tunnin 18 arviointiohje</h2>'
            f'<div class="reading panel active">{S.to_html(ao_raw)}</div>'
        )
    body = (
        '<section class="page-hero"><div class="page-hero-inner">'
        '<div class="eyebrow"><a class="bc-link" href="/opettaja/" style="color:var(--blue)">Opettajan opas</a> · Arviointi</div>'
        '<h1>Lopputöiden arviointi</h1>'
        '<p>Kolmen osion lopputyöt ja niiden arviointiohjeet koottuna.</p>'
        '</div></section>'
        f'<div class="page-body">{"".join(sections)}</div>'
    )
    return page_shell('Lopputöiden arviointi — Opettajan opas — AI · Perusteet',
                      'Tekoälyn perusteet -kurssin lopputöiden arviointiohjeet opettajalle.',
                      '/opettaja/arviointi/', body)
