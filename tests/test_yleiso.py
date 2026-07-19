#!/usr/bin/env python3
"""Estä perusteettomien opiskeluala- ja työpaikkaoletusten palaaminen."""

from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
ALLOW_PATH = ROOT / 'tests' / 'allowlists' / 'yleiso.yaml'
FORBIDDEN = [
    # Suorat koulutusaste- ja ammattirooliolettamat.
    r'\btoisen asteen opiskelijoille\b',
    r'\b(?:IT|TVT)[ -]?ammattilai\w*\b',
    r'(?<![-\w])\bammattilai\w*\b',
    r'\bammatilli\w*\b',
    # Lukijan alaa, työpaikkaa, ammattia tai tunnuksia koskevat oletukset.
    r'\boman alasi\b',
    r'\bomalla alallasi\b',
    r'\balaltasi\b',
    r'\balallesi\b',
    r'\boppilaitoksesi\b',
    r'\btyökaverisi\b',
    r'\bkollegasi\b',
    r'\burallasi\b',
    r'\btyöpaikkasi\b',
    r'\borganisaatiosi\b',
    r'\borganisaatiossasi\b',
    r'\byrityksesi\b',
    r'\bomalla työpaikallasi\b',
    r'\btyöpaikallasi\b',
    r'\btyössäsi\b',
    r'\bammatissasi\b',
    r'\borganisaatiotili\w*\b',
    r'\boppilaitostili\w*\b',
]


def main():
    data = yaml.safe_load(ALLOW_PATH.read_text(encoding='utf-8')) or {}
    allow_items = data.get('allow', [])
    allowed = set()
    for item in allow_items:
        if not all(isinstance(item.get(key), str) and item[key].strip()
                   for key in ('file', 'text', 'reason')):
            print(f'Virheellinen allowlist-rivi: {item!r}')
            return 1
        allowed.add((item['file'], item['text']))
    used = set()
    errors = []
    for path in sorted((ROOT / 'sisalto').rglob('*')):
        if not path.is_file() or '_arkisto' in path.parts:
            continue
        if path.suffix not in {'.md', '.html', '.yaml'}:
            continue
        rel = str(path.relative_to(ROOT))
        for line_no, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            for pattern in FORBIDDEN:
                for match in re.finditer(pattern, line, flags=re.IGNORECASE):
                    text = match.group(0)
                    key = (rel, text)
                    if key in allowed:
                        used.add(key)
                    else:
                        errors.append(f'{rel}:{line_no}: {text!r}')
    unused = sorted(allowed - used)
    if unused:
        errors.extend(f'Käyttämätön allowlist-rivi: {file}: {text!r}' for file, text in unused)
    if errors:
        print('Kohderyhmäskanni löysi allowlistamattomia oletuksia:', *errors, sep='\n')
        return 1
    print('OK: kohderyhmäskanni')
    return 0


if __name__ == '__main__':
    sys.exit(main())
