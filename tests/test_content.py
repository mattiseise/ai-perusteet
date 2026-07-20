#!/usr/bin/env python3
"""Sisältö- ja sopimustestit generaattorin ympärille."""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / 'sisalto' / 'tunnit'


def fail(message, errors):
    errors.append(message)


def main():
    errors = []
    task_count = 0
    task_types = set()
    for path in sorted(LESSONS.glob('*/harjoittele.md')):
        for raw in re.findall(r'```task\s*\n(.*?)\n```', path.read_text(encoding='utf-8'), re.S):
            task = json.loads(raw)
            task_count += 1
            task_types.add(task['type'])
    if task_count != 112:
        fail(f'Harjoittele-tehtäviä {task_count}, odotettiin 112', errors)
    expected_types = {'match', 'order', 'classify', 'quiz', 'scenario', 'spot', 'reflect'}
    if task_types != expected_types:
        fail(f'Tehtävätyypit {sorted(task_types)}', errors)

    source_demos = sum(p.read_text(encoding='utf-8').count('<figure class="ai-demo">')
                       for p in LESSONS.glob('*/teoria.md'))
    if source_demos != 26:
        fail(f'Lähteissä {source_demos} ai-demoa, odotettiin 26', errors)

    for nn in range(1, 28):
        teoria = LESSONS / f'{nn:02d}' / 'teoria.md'
        text = teoria.read_text(encoding='utf-8')
        if len(re.findall(r'^# ', text, re.M)) != 1:
            fail(f'{teoria.relative_to(ROOT)}: H1-otsikoita pitää olla yksi', errors)
        if ('## Lähteet ja tarkistuspäivä' not in text
                or not re.search(r'Tarkistettu \d{1,2}\.\d{1,2}\.2026\.', text)):
            fail(f'{teoria.relative_to(ROOT)}: lähdeosio puuttuu', errors)
        plan = LESSONS / f'{nn:02d}' / 'opettaja' / 'tuntisuunnitelma.md'
        if '## 90 minuutin toteutus ja eriyttäminen' not in plan.read_text(encoding='utf-8'):
            fail(f'{plan.relative_to(ROOT)}: 90 minuutin reitit puuttuvat', errors)

    forbidden_claims = {
        'generator/sivut.py': ['Materiaaliin on kuitenkin jätetty tarkoituksella pieniä virheitä'],
        'sisalto/tunnit/19/teoria.md': ['Jokainen agentti, olipa se yksinkertainen tai monimutkainen, rakentuu kuudesta'],
        'sisalto/tunnit/23/teoria.md': ['[AJATTELU]', 'raaka chain-of-thought'],
        'sisalto/tunnit/24/teoria.md': ['käsky tuhotaan', 'käskyltä näyttävä rivi pysäytetään ja tuhotaan'],
    }
    for rel, phrases in forbidden_claims.items():
        body = (ROOT / rel).read_text(encoding='utf-8')
        for phrase in phrases:
            if phrase in body:
                fail(f'{rel}: vanha ongelmaväite {phrase!r}', errors)

    for name in ('teoria', 'kaytto', 'agentit'):
        body = (ROOT / 'sisalto' / 'lopputyot' / f'{name}.md').read_text(encoding='utf-8')
        for level in ('Erinomainen', 'Hyvä', 'Tyydyttävä', 'Välttävä', 'Ei vielä hyväksyttävä'):
            if level not in body:
                fail(f'lopputyot/{name}.md: taso {level} puuttuu', errors)

    for view in ('kurssi', 'luokka'):
        generated = list((ROOT / view).glob('tunti-*/index.html'))
        demos = sum(p.read_text(encoding='utf-8').count('data-demo-id=') for p in generated)
        if demos != 26:
            fail(f'{view}: generoituja demoja {demos}, odotettiin 26', errors)
    course_demos = ''.join(p.read_text(encoding='utf-8') for p in (ROOT / 'kurssi').glob('tunti-*/index.html'))
    if course_demos.count('data-demo-kind="static"') != 23:
        fail('Staattisten demojen määrä ei ole 23', errors)
    if course_demos.count('<div class="ai-demo__mobile-model ') != 23:
        fail('Jokaiselta staattiselta demolta pitää löytyä yksilöllinen reflow-malli', errors)
    css = (ROOT / 'assets' / 'site.css').read_text(encoding='utf-8')
    if re.search(r'\.ai-demo[^\{]*\.ai-demo__stage\s*\{[^}]*display\s*:\s*none', css, re.S):
        fail('ai-demo-stagea ei saa piilottaa mobiilissa', errors)

    if errors:
        print(*errors, sep='\n')
        return 1
    print('OK: 112 tehtävää, 26 demoa, 27 lähdeosiota, arvioinnit ja sisältösopimukset')
    return 0


if __name__ == '__main__':
    sys.exit(main())
