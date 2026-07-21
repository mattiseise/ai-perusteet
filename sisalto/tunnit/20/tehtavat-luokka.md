# Opiskelutehtävät: Automaatio vai autonomia?

> Tällä tunnilla et rakenna vielä mitään. Teet arkkitehtuuripäätöksen: ratkaistaanko tehtävä promptilla, tavallisella työnkululla vai agentilla? Hyvä päätös voi olla myös se, ettei agenttia tarvita.

## Agentti: Ongelma — valitse lopullinen projektisi — suositeltu

**Tavoite:** Osaat erottaa toisistaan kertaluonteisen promptauksen, ennalta määritellyn työnkulun ja agentin, joka valitsee toimintoja tilanteen perusteella.

### Vaihe 1 — Arvioi kolme tapausta

Täytä taulukko. Älä aloita ratkaisusta, vaan tehtävän tarpeesta.

| Tapaus | Prompti, työnkulku vai agentti? | Mikä päätös muuttuu tilanteen mukaan? | Mitä agentin ohjauskehyksen pitäisi hallita? | Miksi yksinkertaisempi ratkaisu ei riitä? |
| --- | --- | --- | --- | --- |
| Yhden raportin tiivistäminen kerran |  |  |  |  |
| Saapuvan lomakkeen tallentaminen aina samaan taulukkoon |  |  |  |  |
| Tukipyynnön tutkiminen, tarvittavan tiedon hakeminen ja epäselvän tapauksen ohjaaminen ihmiselle |  |  |  |  |

Käytä päätöksessäsi näitä kysymyksiä:

1. Toistuuko tehtävä?
2. Onko eteneminen sama joka kerta?
3. Pitääkö järjestelmän tulkita tilannetta ja valita seuraava toiminto?
4. Mitä työkaluja ja oikeuksia ratkaisu tarvitsee?
5. Mitä virhe maksaisi?
6. Missä ihminen voi valvoa tai hyväksyä toiminnan?

### Vaihe 2 — Valitse lopullinen agenttiprojektisi

Avaa Boteista agentteihin -tunnilla kirjoittamasi ongelmaehdokkaat. Aja vähintään kaksi ehdokasta saman päätöspuun läpi. Valitse vasta vertailun jälkeen lopullinen agenttiprojektisi ja kirjoita yhden sivun päätösmuistio:

- **Tehtävä:** Mitä ollaan ratkaisemassa ja kenelle?
- **Valinta:** Prompti, työnkulku vai agentti?
- **Muuttuva päätös:** Minkä seuraavan toiminnon kielimalli saa valita tilanteen perusteella?
- **Agentin ohjauskehys:** Miten syöte, työkalut, tila, oikeudet ja loki hallitaan?
- **Yksinkertaisempi vaihtoehto:** Miksi se ei riitä — tai miksi se sittenkin riittää?
- **Riski ja valvonta:** Mikä voi mennä pieleen ja missä ihminen tarvitaan?

Jos huomaat, että tavallinen työnkulku riittää, älä keksi agentille näennäistä tarvetta. Rajaa projektiasi uudelleen niin, että siinä on yksi todellinen, tilanteen mukaan muuttuva päätös. Voit myös vaihtaa aihetta.

### Tekoälyvaihe — haasta päätös

```text
Arvioin tehtävää, johon olen valinnut [promptin / työnkulun / agentin].
Tässä ovat tehtävä, muuttuva päätös, tarvittavat työkalut, riskit ja
valvonta: [liitä muistiosi]. Haasta valintani kolmella kysymyksellä.
Älä ehdota agenttia vain siksi, että tehtävässä käytetään kielimallia.
Etsi ensin yksinkertaisempi ratkaisu, joka voisi riittää.
```

Muokkaa päätösmuistiotasi saamiesi kysymysten perusteella. Merkitse loppuun yksi muutos, jonka teit, ja miksi.

## Tehtävä 20.2 — Rajatapauksen puolustus — syventävä

Valitse tehtävä, jonka voisi toteuttaa joko työnkulkuna tai agenttina. Piirrä siitä kaksi ratkaisua:

1. **Työnkulku:** ennalta määrätyt vaiheet ja ehdot.
2. **Agentti:** kohta, jossa kielimalli valitsee työkalun tai seuraavan toiminnon saadun havainnon perusteella.

Vertaa ratkaisuja kustannuksen, testattavuuden, ylläpidon ja riskin kannalta. Päätä lopuksi, kumman toteuttaisit ensimmäisenä. Perustele päätös näytöllä, älä ratkaisun uutuudella.

---

**Tallennettava tuotos:** **Agentti: Ongelma** -pohjapiirros (1/5), perusteltu päätösmuistio ja siihen tehty yksi nimetty korjaus. Tämä muistio toimii porttina agenttiprojektille: vasta hyväksytyn agenttitarpeen jälkeen siirryt muistin, työkalujen ja päättelyn suunnitteluun.
