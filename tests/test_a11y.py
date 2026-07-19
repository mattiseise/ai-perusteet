#!/usr/bin/env python3
"""Generoidun käyttöliittymän saavutettavuussopimukset."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    pages = list((ROOT / 'kurssi').glob('tunti-*/index.html'))
    for page in pages:
        text = page.read_text(encoding='utf-8')
        if 'role="tablist"' not in text or 'role="tab"' not in text or 'role="tabpanel"' not in text:
            errors.append(f'{page.relative_to(ROOT)}: välilehtiroolit puuttuvat')
        if 'aria-selected=' not in text or 'aria-controls=' not in text:
            errors.append(f'{page.relative_to(ROOT)}: välilehtien ARIA-tila puuttuu')
    js = (ROOT / 'assets' / 'practice.js').read_text(encoding='utf-8')
    for required in ('aria-live', "p.htmlFor=ta.id", "role','status"):
        if required not in js:
            errors.append(f'practice.js: {required!r} puuttuu')
    site_js = (ROOT / 'assets' / 'site.js').read_text(encoding='utf-8')
    for key in ('ArrowRight', 'ArrowLeft', "e.key==='Home'", "e.key==='End'"):
        if key not in site_js:
            errors.append(f'site.js: välilehtinäppäin {key} puuttuu')
    if errors:
        print(*errors, sep='\n')
        return 1
    print('OK: tabit, live-palautteet ja reflektiolabelit')
    return 0


if __name__ == '__main__':
    sys.exit(main())
