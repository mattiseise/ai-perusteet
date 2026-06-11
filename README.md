# Tekoälyn perusteet — Business College Helsinki

27-oppituntinen kurssi tekoälyn perusteista. Kolme kokonaisuutta: teoria, käyttö ja agentit.

## Rakenne

```
content/lessons/     # Oppituntien pääsisältö (lesson-01.md – lesson-27.md)
student/             # Opiskelijamateriaali per oppitunti
  lesson-XX/
    self-study.md        # Itseopiskelumateriaali
    student-tasks.md     # Opiskelutehtävät
    vocabulary.md        # Sanasto
teacher/             # Opettajamateriaali per oppitunti
  lesson-XX/
    teacher-led-tasks.md # Opettajavetoiset tehtävät
    teacher-materials.md # Opettajan materiaali
generate_site.py     # Sivustogeneraattori → tuottaa index.html
```

## Sivuston generointi

```bash
pip install markdown
python3 generate_site.py
# → tuottaa index.html
```

