#!/usr/bin/env python3
"""AI · Perusteet — sivustogeneraattori v2 (monisivuinen, kolme näkymää).

Ohut käynnistin: varsinainen logiikka on generator/-paketissa
(sisalto, nakymat, assets, sivut). Tuottaa kolmen näkymän (kurssi/luokka/opettaja)
staattisen sivuston repojuureen; Netlify julkaisee repojuuren.

Aja:  python3 generate_site.py   (vaatii: pip install markdown pyyaml)
"""

import os
import re

from generator import nakymat as N
from generator import assets
from generator import sivut

ROOT = os.path.dirname(os.path.abspath(__file__))


def _write(relpath, html):
    path = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    return relpath


def build_pages():
    written = []

    # Etusivu (valintasivu + hash-redirect)
    written.append(_write('index.html', sivut.build_index_page()))

    # Kurssi-näkymä: yleiskuva + moduulit + tunnit + lopputyöt
    written.append(_write('kurssi/index.html', sivut.build_kurssi_overview()))
    for osp in N.OSP_BLOCKS:
        written.append(_write(f'kurssi/{osp["slug"]}/index.html', sivut.build_kurssi_module(osp)))
        written.append(_write(f'kurssi/{osp["slug"]}/lopputyo/index.html',
                              sivut.build_lopputyo_page(osp, 'kurssi')))
    for l in N.ALL_LESSONS:
        written.append(_write(f'kurssi/tunti-{l["kansio"]}/index.html',
                              sivut.build_tunti_page(l, 'kurssi')))

    # Luokka-näkymä: yksi tuntilista + tunnit + lopputyöt
    written.append(_write('luokka/index.html', sivut.build_luokka_index()))
    for l in N.ALL_LESSONS:
        written.append(_write(f'luokka/tunti-{l["kansio"]}/index.html',
                              sivut.build_tunti_page(l, 'luokka')))
    for osp in N.OSP_BLOCKS:
        written.append(_write(f'luokka/{osp["slug"]}/lopputyo/index.html',
                              sivut.build_lopputyo_page(osp, 'luokka')))

    # Opettaja-näkymä: kurssiopas + tunnit + arviointi
    written.append(_write('opettaja/index.html', sivut.build_opettaja_index()))
    for l in N.ALL_LESSONS:
        written.append(_write(f'opettaja/tunti-{l["kansio"]}/index.html',
                              sivut.build_tunti_page(l, 'opettaja')))
    written.append(_write('opettaja/arviointi/index.html', sivut.build_opettaja_arviointi()))

    # Sanasto
    written.append(_write('sanasto/index.html', sivut.build_sanasto_page()))

    # Englanninkielinen tiivistelmä (kansainvälinen löydettävyys; ei käännös)
    written.append(_write('en/index.html', sivut.build_en_page()))

    return written


def build_sitemap(pages):
    """sitemap.xml: vain itseensä kanonisoivat sivut.

    Sivu, jonka rel=canonical osoittaa muualle (luokkaversion tunti- ja lopputyösivut →
    kurssiversio), jätetään pois: sitemapissa oleva ei-kanoninen URL on ristiriitainen
    signaali hakukoneelle. Canonical luetaan generoidusta HTML:stä, jolloin sitemap pysyy
    synkassa automaattisesti, jos kanonisointisääntöjä myöhemmin muutetaan.
    """
    urls, skipped = [], 0
    for rel in pages:
        path = '/' + rel[:-len('index.html')] if rel.endswith('index.html') else '/' + rel
        if path == '/index.html':
            path = '/'
        url = sivut.DOMAIN + path
        with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
            m = re.search(r'<link rel="canonical" href="([^"]+)">', f.read())
        if m and m.group(1) != url:
            skipped += 1
            continue
        urls.append(url)
    if skipped:
        print(f'  ohitettu {skipped} ei-kanonista sivua (duplikaattinäkymät)')
    body = '\n'.join(
        f'  <url><loc>{u}</loc></url>' for u in urls
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f'{body}\n</urlset>\n')
    _write('sitemap.xml', xml)
    return len(urls)


# Kielimallien ja tekoälyhakujen crawlerit sallitaan eksplisiittisesti. Ne olisivat
# sallittuja jo "User-agent: *" -säännöllä, mutta nimetty Allow dokumentoi valinnan
# tietoiseksi: kurssi on CC BY-SA 4.0 ja sen halutaan näkyvän myös generatiivisissa
# hauissa (ChatGPT, Claude, Perplexity, Gemini). Jos linjaa joskus muutetaan, muutos
# tehdään tähän — älä poista listaa "turhana toistona".
AI_CRAWLERS = [
    'GPTBot',            # OpenAI, ChatGPT-haun indeksointi
    'OAI-SearchBot',     # OpenAI, hakutulosten näyttö
    'ChatGPT-User',      # OpenAI, käyttäjän pyytämä sivunhaku
    'ClaudeBot',         # Anthropic
    'Claude-User',       # Anthropic, käyttäjän pyytämä sivunhaku
    'PerplexityBot',     # Perplexity
    'Google-Extended',   # Google Gemini / AI Overviews
    'Applebot-Extended', # Apple Intelligence
    'CCBot',             # Common Crawl (moni malli kouluttaa tästä)
]


def build_robots():
    lines = ['User-agent: *', 'Allow: /', '']
    for bot in AI_CRAWLERS:
        lines += [f'User-agent: {bot}', 'Allow: /', '']
    lines += [
        'Sitemap: ' + sivut.DOMAIN + '/sitemap.xml',
        '# LLM-ystävällinen tiivistelmä (GEO): ' + sivut.DOMAIN + '/llms.txt',
        '',
    ]
    _write('robots.txt', '\n'.join(lines))


def build_llms():
    """/llms.txt — tiivis markdown-kuvaus kielimalleille (GEO)."""
    D = sivut.DOMAIN
    lines = [
        '# AI · Perusteet',
        '',
        '> ' + N.KURSSI['kurssi']['yleisolupaus'],
        '',
        N.KURSSI['kurssi']['laajuuskuvaus'],
        '',
        'Kurssin sisältö on vapaasti käytettävissä Creative Commons Nimeä-JaaSamoin 4.0 '
        '(CC BY-SA 4.0) -lisenssillä: saat käyttää, jakaa ja muokata materiaalia myös '
        'kaupallisesti, kunhan mainitset tekijän ja jaat johdannaiset samalla lisenssillä.',
        '',
        '## Kolme näkymää samaan sisältöön',
        '',
        f'- [Verkkokurssi]({D}/kurssi/) (`/kurssi/`) — itsenäinen opiskelu omaan tahtiin: '
        'teoria, itsetarkistuvat harjoitukset, sanasto, diat ja lopputyön askeleet '
        '(lopputyön osatuotostehtävät verkko-opiskelijalle kehystettyinä).',
        f'- [Luokkaversio]({D}/luokka/) (`/luokka/`) — oppituntien opiskelijamateriaali: '
        'teoria, luokkatehtävät, harjoittele, sanasto ja diat.',
        f'- [Opettajan opas]({D}/opettaja/) (`/opettaja/`) — kurssiopas, tuntisuunnitelmat, '
        'opettajavetoiset tehtävät ja arviointi.',
        f'- [Sanasto]({D}/sanasto/) (`/sanasto/`) — koko kurssin käsitteet aakkosjärjestyksessä.',
        f'- [In English]({D}/en/) (`/en/`) — englanninkielinen tiivistelmä kurssista '
        '(kurssin sisältö on suomeksi; tämä sivu ei ole käännös).',
        '',
        '## Moduulit ja oppitunnit',
        '',
    ]
    for osp in N.OSP_BLOCKS:
        lines.append(f'### {osp["title"]} — {osp["subtitle"]}')
        lines.append('')
        for lid, title, btype, kansio in osp['lessons']:
            num = N.ALL_IDS.index(lid) + 1
            suffix = ' (arviointitunti)' if btype == 'assessment' else ''
            lines.append(f'- [Tunti {num}: {title}]({D}/kurssi/tunti-{kansio}/){suffix}')
        lines.append('')
    lines += [
        '## Lisenssi',
        '',
        'CC BY-SA 4.0 — https://creativecommons.org/licenses/by-sa/4.0/deed.fi',
        '',
    ]
    _write('llms.txt', '\n'.join(lines))


def build_redirects():
    # Hash-osoitteet (#lesson-NN ym.) eivät välity palvelimelle — ne ohjataan
    # etusivun inline-skriptillä (ks. sivut.build_index_page). Netlify ei salli
    # /index.html → / -sääntöä (silmukka), joten palvelinpuolen sääntöjä ei tarvita.
    _write('_redirects', '# Hash-redirectit hoidetaan client-side etusivulla.\n')


if __name__ == '__main__':
    print('Kirjoitetaan assetit (site.js, practice.js)...')
    assets.write_assets(ROOT)
    if not os.path.exists(os.path.join(ROOT, 'assets', 'site.css')):
        raise SystemExit('VIRHE: assets/site.css puuttuu (committoitu lähde).')

    print('Generoidaan sivut...')
    pages = build_pages()
    print(f'  {len(pages)} HTML-sivua')

    n = build_sitemap(pages)
    print(f'Sitemap: {n} osoitetta')
    build_robots()
    build_llms()
    build_redirects()

    total_kb = sum(os.path.getsize(os.path.join(ROOT, p)) for p in pages) // 1024
    largest = max(pages, key=lambda p: os.path.getsize(os.path.join(ROOT, p)))
    largest_kb = os.path.getsize(os.path.join(ROOT, largest)) // 1024
    print(f'Sivut yhteensä: {total_kb} KB · suurin: {largest} ({largest_kb} KB)')
    print('Valmis.')
