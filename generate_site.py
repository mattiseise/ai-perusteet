#!/usr/bin/env python3
"""AI · Perusteet — sivustogeneraattori v2 (monisivuinen, kolme näkymää).

Ohut käynnistin: varsinainen logiikka on generator/-paketissa
(sisalto, nakymat, assets, sivut). Tuottaa kolmen näkymän (kurssi/luokka/opettaja)
staattisen sivuston repojuureen; Netlify julkaisee repojuuren.

Aja:  python3 generate_site.py   (vaatii: pip install markdown pyyaml)
"""

import os

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

    return written


def build_sitemap(pages):
    """sitemap.xml: kaikki julkiset sivut kanonisina osoitteina."""
    urls = []
    for rel in pages:
        path = '/' + rel[:-len('index.html')] if rel.endswith('index.html') else '/' + rel
        if path == '/index.html':
            path = '/'
        urls.append(sivut.DOMAIN + path)
    body = '\n'.join(
        f'  <url><loc>{u}</loc></url>' for u in urls
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f'{body}\n</urlset>\n')
    _write('sitemap.xml', xml)
    return len(urls)


def build_robots():
    _write('robots.txt', 'User-agent: *\nAllow: /\n\nSitemap: ' + sivut.DOMAIN + '/sitemap.xml\n')


def build_redirects():
    # Netlify: hash ei koskaan välity palvelimelle → varapolut. /index.html → /.
    _write('_redirects', '/index.html   /   301\n')


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
    build_redirects()

    total_kb = sum(os.path.getsize(os.path.join(ROOT, p)) for p in pages) // 1024
    largest = max(pages, key=lambda p: os.path.getsize(os.path.join(ROOT, p)))
    largest_kb = os.path.getsize(os.path.join(ROOT, largest)) // 1024
    print(f'Sivut yhteensä: {total_kb} KB · suurin: {largest} ({largest_kb} KB)')
    print('Valmis.')
