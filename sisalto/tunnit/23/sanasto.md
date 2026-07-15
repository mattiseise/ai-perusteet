# Sanasto – oppitunti 23: Suunnittelumallit

## ReAct (Reasoning + Acting)

Suunnittelumalli, jossa agentti valitsee työkalun, saa tuloksen tai virheen ja valitsee seuraavan toiminnon havainnon perusteella. Lokiin tallennetaan rakenteiset kutsut, tulokset, toiminnot ja lyhyet päätösperustelut — ei raakaa chain-of-thoughtia.

## Eksplisiittinen työnkulku (explicit workflow)

Suunnittelumalli, jossa agentti purkaa ongelman pienempiin osiin ja käsittelee ne järjestyksessä. Numeroidut vaiheet, yksi kerrallaan.

## Päättely (reasoning)

Mallin sisäinen prosessi, jolla se tuottaa seuraavan vastauksen tai toiminnon. Piilotettua raakaa päättelyketjua ei pyydetä eikä tallenneta; käyttäjälle voidaan antaa lyhyt perustelu ja toteutuksesta lokitetaan havaittavat tapahtumat.

## Toiminta (action)

Vaihe, jossa agentti tekee konkreettisen toiminnon — kutsuu funktiota, hakee tietoa, kirjoittaa viestin.

## Iteraatio (iteration)

Samaa havaittavaa toimintakierrosta toistetaan useita kertoja. ReAct-toteutus iteroi: työkalukutsu → tulos tai virhe → seuraava toiminto.

## Moniagenttijärjestelmä (multi-agent system)

Useita erikoistuneet agentteja, jotka tekevät yhteistyötä. Jokainen agentti on erikoistunut omaan alueeseen.

## Hierarkkinen malli (hierarchical model)

Moniagenttijärjestelmän rakenne, jossa yksi agentti on johtaja ja jakaa tehtäviä muille.

## Yhteistyömalli (collaborative model)

Moniagenttijärjestelmän rakenne, jossa agentit keskustelevat keskenään ilman johtajaa.

## Orkestraatio (orchestration)

Koordinointi — kuinka agentit kutsutaan järjestyksessä ja kuinka tieto kulkee niiden välillä.

## Eskalointi (escalation)

Tehtävän siirtäminen ihmiselle tai toiselle sovitulle toimijalle, kun agentti ei pysty ratkaisemaan sitä turvallisesti.

## Palautuminen (recovery)

Prosessi, jolla agentti palautuu virheestä tai yrittää uudelleen.

## Palaute (feedback)

Tieto siitä, kuinka agentin toiminta onnistui. Palaute voidaan käyttää arviointiin tai erilliseen kehitys- ja koulutusprosessiin; käytössä oleva agentti ei automaattisesti opi siitä.

---
