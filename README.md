# Tekoälyn perusteet

27-oppituntinen kurssi tekoälyn perusteista (aiperusteet.fi). Kolme moduulia:
Teoria (tunnit 1–9), Tekoälyjen käyttö (10–18) ja Agentit (19–27).

## Rakenne

```
student/                 # Sivuston lähde: opiskelijamateriaali per oppitunti
  lesson-NN/
    self-study.md            # Itseopiskelumateriaali (teoria)
    student-tasks.md         # Opiskelutehtävät (luokkatehtävät)
    practice.md              # Harjoittele-tehtävät (```task-JSON-lohkot)
    vocabulary.md            # Sanasto
    slides.html              # Diat (käsin ladottu SVG)
teacher/                 # Sivuston lähde: opettajamateriaali per oppitunti
  lesson-NN/
    teacher-materials.md     # Tuntisuunnitelma, väärinkäsitykset
    teacher-led-tasks.md     # Opettajavetoiset tehtävät
*-lopputyo-tehtavananto.md   # Lopputöiden tehtävänannot (3 kpl, juuressa)
generate_site.py         # Sivustogeneraattori → tuottaa index.html
siirtyma/redirectit.md   # Rakenneuudistus 2: lukittu redirect-taulukko
```

Huom: `index.html` on generoitu — älä muokkaa käsin. Repo-konventiot ja
generaattorin ansat: `CLAUDE.md`.

## Sivuston generointi

```bash
pip install markdown
python3 generate_site.py
# → tuottaa index.html
```

## Käynnissä: rakenneuudistus 2

Sivusto ollaan muuttamassa monisivuiseksi, kolmen näkymän kokonaisuudeksi
(/kurssi, /luokka, /opettaja) yhdestä sisältöpohjasta. Suunnitelma:
`RAKENNEUUDISTUS-2-NAKYMAT.md`, toimeksianto: `HANDOFF-RAKENNEUUDISTUS-2.md`.
