#!/usr/bin/env python3
"""Yksikkötesti varianttilohkojen suodattimelle (generator.sisalto.filter_variants).

Aja: python3 siirtyma/testit/test_variantit.py
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from generator.sisalto import filter_variants  # noqa: E402


def test_ei_variantteja_lapi():
    t = "Tavallista tekstiä\nrivi 2."
    assert filter_variants(t, 'verkko') == t


def test_pitaa_oikean_variantin():
    t = ("Yhteistä.\n"
         "::: verkko\nVain verkkoon.\n:::\n"
         "::: luokka\nVain luokkaan.\n:::\n"
         "Loppu.")
    v = filter_variants(t, 'verkko')
    assert 'Vain verkkoon.' in v
    assert 'Vain luokkaan.' not in v
    assert 'Yhteistä.' in v and 'Loppu.' in v
    assert ':::' not in v
    l = filter_variants(t, 'luokka')
    assert 'Vain luokkaan.' in l
    assert 'Vain verkkoon.' not in l


def test_opettaja_variantti():
    t = "::: opettaja\nOhje opettajalle.\n:::\n::: verkko\nVerkko.\n:::"
    o = filter_variants(t, 'opettaja')
    assert 'Ohje opettajalle.' in o and 'Verkko.' not in o


def test_avaamaton_kaatuu():
    t = "::: verkko\nJäi auki"
    try:
        filter_variants(t, 'verkko', source='x.md')
        assert False, 'olisi pitänyt kaatua avaamattomaan lohkoon'
    except SystemExit:
        pass


def test_tuntematon_nimi_kaatuu():
    t = "::: outo\nx\n:::"
    try:
        filter_variants(t, 'verkko', source='x.md')
        assert False, 'olisi pitänyt kaatua tuntemattomaan varianttinimeen'
    except SystemExit:
        pass


def test_sulkeva_ilman_avausta_kaatuu():
    t = "tekstiä\n:::\nlisää"
    try:
        filter_variants(t, 'verkko', source='x.md')
        assert False, 'olisi pitänyt kaatua sulkevaan ilman avausta'
    except SystemExit:
        pass


if __name__ == '__main__':
    tests = [v for k, v in sorted(globals().items()) if k.startswith('test_')]
    for t in tests:
        t()
        print(f'OK  {t.__name__}')
    print(f'\n{len(tests)} testiä läpi.')
