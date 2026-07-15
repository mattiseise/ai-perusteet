#!/usr/bin/env python3
"""Tarkista generoituja sisäisiä sivulinkkejä."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            href = dict(attrs).get('href')
            if href:
                self.hrefs.append(href)


def main():
    errors = []
    for page in sorted(ROOT.rglob('index.html')):
        if '.git' in page.parts or 'node_modules' in page.parts:
            continue
        parser = Links()
        parser.feed(page.read_text(encoding='utf-8'))
        for href in parser.hrefs:
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or href.startswith(('#', 'mailto:')):
                continue
            target = ROOT / parsed.path.lstrip('/')
            if parsed.path.endswith('/'):
                target /= 'index.html'
            if not target.exists():
                errors.append(f'{page.relative_to(ROOT)} → {href}')
    if errors:
        print('Rikkinäiset sisäiset linkit:', *errors, sep='\n')
        return 1
    print('OK: sisäiset sivulinkit')
    return 0


if __name__ == '__main__':
    sys.exit(main())
