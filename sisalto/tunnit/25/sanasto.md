# Sanasto – oppitunti 25: Ihmisen osallistuminen päätöksentekoon

## Harness

Kielimallia ympäröivä järjestelmä, joka toteuttaa hyväksyntäportin käytännössä. Se pysäyttää suorituksen, säilyttää tilan, näyttää päätöstiedot ihmiselle ja jatkaa, hylkää tai eskaloi ennalta sovitun säännön mukaan.

## Ihmisen osallistuminen päätöksentekoon (ihminen silmukassa)

Automaatio, jossa ihminen hyväksyy kriittiset päätökset. Ei täysin automatisoitua, ei käsityötä — hybridi.

## Hyväksyntäportti (approval gate)

Harnessin toteuttama kohta, jossa suoritus pysähtyy odottamaan ihmisen vastausta. Hyvä portti näyttää selkeän kysymyksen, ehdotuksen, perustelun ja riskin.

## Eskalointi (escalation)

Tehtävän siirtäminen toiselle hyväksyjälle, kun ensimmäinen ei voi vastata.

## Aikaraja

Aika, jossa hyväksyjällä on vastata. Jos vastaus ei tule, mitä tehdään? (oletusarvo, eskalointi, tai odotetaan)

## Rahaa/rakenne -sääntö

Päätös, joka koskee rahaa (alennukset, hyvitykset) tai rakennetta (asiakkaantiedot, tilat) vaatii hyväksynnän.

## Epävarmuus-sääntö

Jos agentti on epävarma (varmuus < 70%), vaadi ihmisen vahvistus.

## Poikkeama-sääntö

Jos tilanne on poikkeuksellinen (ei rutiinitapaus), vaadi hyväksyntä.

## Validointi-agentti

Agentti, joka tarkistaa, onko toisen agentin vastaus turvallinen ja oikea.

## Palautekäytäntö (feedback loop)

Prosessi, jossa agentti oppii hyväksyntä/hylkäys-päätöksistä ja parantaa ehdotuksensa.

## Oppiminen palautteesta (learning from feedback)

Agentti analysoi, mitä hyväksyy ja hylkää, ja muuttaa käyttäytymistään.

## Monivaiheinen hyväksyntä (multi-step approval)

Prosessi, jossa päätös vaatii useiden hyväksyjien hyväksynnän peräkkäin.

## Variaatioiden hallinta (variation management)

Eri hyväksyjät, eri tiimit vaativat erilaisia prosesseja. Agentti oppii ja mukauttaa.

## Workflow

Sarja vaiheita, joissa agentti ja ihminen tekevät yhteistyötä. Vaihe vaiheelta selkeitä rooleja.

---
