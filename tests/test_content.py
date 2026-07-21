#!/usr/bin/env python3
"""Sisältö- ja sopimustestit generaattorin ympärille."""

from pathlib import Path
import json
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / 'sisalto' / 'tunnit'


def fail(message, errors):
    errors.append(message)


def main():
    errors = []
    manifest = yaml.safe_load((ROOT / 'sisalto' / 'kurssi.yaml').read_text(encoding='utf-8'))
    thinking = manifest.get('ajattelu', {})
    moves = thinking.get('liikkeet', [])
    move_ids = [move.get('id') for move in moves]
    expected_moves = ['tunnista', 'selita', 'testaa', 'arvioi', 'perustele']
    if move_ids != expected_moves or len(set(move_ids)) != 5:
        fail(f'Ajatteluliikkeet {move_ids}, odotettiin {expected_moves}', errors)
    if not thinking.get('lupaus', '').strip():
        fail('Ajattelumallin lupaus puuttuu', errors)

    lesson_thoughts = []
    for module in manifest.get('moduulit', []):
        arc = module.get('ajattelukaari', {})
        if set(arc) != set(expected_moves) or any(not str(arc.get(mid, '')).strip() for mid in expected_moves):
            fail(f'{module.get("id")}: ajattelukaari on puutteellinen', errors)
        for lesson in module.get('tunnit', []):
            thought = lesson.get('ajattelu', {})
            lesson_thoughts.append((lesson.get('id'), thought))
            if thought.get('painotus') not in expected_moves:
                fail(f'{lesson.get("id")}: virheellinen ajattelupainotus {thought.get("painotus")!r}', errors)
            if not thought.get('kysymys', '').strip():
                fail(f'{lesson.get("id")}: ajattelukysymys puuttuu', errors)
    if len(lesson_thoughts) != 27:
        fail(f'Ajattelukysymyksiä {len(lesson_thoughts)}, odotettiin 27', errors)

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
    if source_demos != 27:
        fail(f'Lähteissä {source_demos} ai-demoa, odotettiin 27', errors)

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
        if demos != 27:
            fail(f'{view}: generoituja demoja {demos}, odotettiin 27', errors)
    course_demos = ''.join(p.read_text(encoding='utf-8') for p in (ROOT / 'kurssi').glob('tunti-*/index.html'))
    if course_demos.count('data-demo-kind="static"') != 24:
        fail('Staattisten demojen määrä ei ole 24', errors)
    if course_demos.count('<div class="ai-demo__mobile-model ') != 24:
        fail('Jokaiselta staattiselta demolta pitää löytyä yksilöllinen reflow-malli', errors)
    for view in ('kurssi', 'luokka', 'opettaja'):
        generated = list((ROOT / view).glob('tunti-*/index.html'))
        thinking_paths = sum(
            p.read_text(encoding='utf-8').count('thinking-path thinking-path--lesson')
            for p in generated
        )
        if thinking_paths != 27:
            fail(f'{view}: tuntien ajattelupolkuja {thinking_paths}, odotettiin 27', errors)
    overview = (ROOT / 'kurssi' / 'index.html').read_text(encoding='utf-8')
    if overview.count('thinking-path thinking-path--course') != 1:
        fail('Verkkokurssin ajattelulupaus puuttuu tai toistuu', errors)
    for slug in ('teoria', 'kaytto', 'agentit'):
        module_page = (ROOT / 'kurssi' / slug / 'index.html').read_text(encoding='utf-8')
        if module_page.count('thinking-path thinking-path--module') != 1:
            fail(f'{slug}: moduulin ajattelukaari puuttuu tai toistuu', errors)
    # ARIA-viitteet: aria-labelledby/-describedby -kohteiden pitää löytyä samasta figuresta
    for page in (ROOT / 'kurssi').glob('tunti-*/index.html'):
        body = page.read_text(encoding='utf-8')
        for fig_html in re.findall(r'<figure class="ai-demo"[^>]*>.*?</figure>', body, re.S):
            ids = set(re.findall(r'id="([^"]+)"', fig_html))
            for attr in ('aria-labelledby', 'aria-describedby'):
                for ref in re.findall(rf'{attr}="([^"]+)"', fig_html):
                    for token in ref.split():
                        if token not in ids:
                            fail(f'{page.relative_to(ROOT)}: {attr}="{token}" ei löydy samasta figuurista', errors)

    css = (ROOT / 'assets' / 'site.css').read_text(encoding='utf-8')
    if re.search(r'\.ai-demo[^\{]*\.ai-demo__stage\s*\{[^}]*display\s*:\s*none', css, re.S):
        fail('ai-demo-stagea ei saa piilottaa mobiilissa', errors)

    if errors:
        print(*errors, sep='\n')
        return 1
    print('OK: 112 tehtävää, 27 demoa, 27 lähdeosiota, arvioinnit ja sisältösopimukset')
    return 0


if __name__ == '__main__':
    sys.exit(main())
