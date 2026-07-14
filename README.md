# Tekoälyn perusteet

27-oppituntinen kurssi tekoälyn perusteista (aiperusteet.fi). Kolme moduulia:
Teoria (tunnit 1–9), Tekoälyjen käyttö (10–18) ja Agentit (19–27).

## Rakenne

```
sisalto/                 # Sivuston lähde (yksi sisältöpohja)
  kurssi.yaml                # Moduulit, tunnit, näkymäkonfiguraatiot (manifesti)
  tunnit/NN/                 # NN = 01–27
    teoria.md                  # Itseopiskelumateriaali
    tehtavat-luokka.md         # Luokkatehtävät
    harjoittele.md             # Harjoittele-tehtävät (```task-JSON; ei tunneilla 18, 27)
    sanasto.md                 # Sanasto
    diat.html                  # Diat (käsin ladottu SVG)
    opettaja/
      tuntisuunnitelma.md      # Tuntisuunnitelma, väärinkäsitykset
      tehtavat-ohjatut.md      # Opettajavetoiset tehtävät
  lopputyot/                 # Lopputöiden tehtävänannot (teoria/kaytto/agentit.md)
  _arkisto/                  # Vanhat snapshotit (ei buildissa)
generate_site.py         # Sivustogeneraattori → tuottaa index.html
siirtyma/redirectit.md   # Rakenneuudistus 2: lukittu redirect-taulukko
```

Huom: `index.html` on generoitu — älä muokkaa käsin. Repo-konventiot ja
generaattorin ansat: `CLAUDE.md`.

## Sivuston generointi

```bash
pip install markdown pyyaml
python3 generate_site.py
# → tuottaa index.html
```

## Käynnissä: rakenneuudistus 2

Sivusto ollaan muuttamassa monisivuiseksi, kolmen näkymän kokonaisuudeksi
(/kurssi, /luokka, /opettaja) yhdestä sisältöpohjasta. Suunnitelma:
`RAKENNEUUDISTUS-2-NAKYMAT.md`, toimeksianto: `HANDOFF-RAKENNEUUDISTUS-2.md`.
