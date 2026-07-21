# Sanasto – oppitunti 23: Suunnittelumallit

## ReAct (Reasoning + Acting)

Suunnittelumalli, jossa agentti valitsee työkalun, saa tuloksen tai virheen ja valitsee seuraavan toiminnon havainnon perusteella. Lokiin tallennetaan työkalujen käytöt, tulokset, toiminnot ja lyhyet päätösperustelut — ei mallin sisäistä päättelyä.

## Eksplisiittinen työnkulku (explicit workflow)

Suunnittelumalli, jossa agentti purkaa ongelman pienempiin osiin ja käsittelee ne järjestyksessä. Numeroidut vaiheet, yksi kerrallaan.

## Päättely (reasoning)

Mallin sisäinen prosessi, jolla se tuottaa seuraavan vastauksen tai toiminnon. Piilotettua raakaa päättelyketjua ei pyydetä eikä tallenneta; käyttäjälle voidaan antaa lyhyt perustelu ja toteutuksesta lokitetaan havaittavat tapahtumat.

## Toiminta (action)

Vaihe, jossa agentti tekee konkreettisen toiminnon — kutsuu funktiota, hakee tietoa, kirjoittaa viestin.

## Iteraatio (iteration)

Samaa havaittavaa toimintakierrosta toistetaan useita kertoja. ReAct-toteutus iteroi: työkalukutsu → tulos tai virhe → seuraava toiminto.

## Valinnainen syvennys: moniagenttijärjestelmä (multi-agent system)

Usean erikoistuneen agentin muodostama järjestelmä, jossa tehtävä jaetaan eri toimijoille. Rakenne lisää työnjaon, tiedonkulun, lokituksen ja valvonnan tarvetta. Moniagenttijärjestelmää ei tarvita tämän kurssin lopputyössä.

## Orkestraatio (orchestration)

Agentin ohjauskehyksen toteuttama koordinointi: miten työkalut tai agentit kutsutaan, miten tulokset ja virheet välitetään, milloin kierros päättyy ja mitä tapahtumia lokitetaan.

## Eskalointi (escalation)

Tehtävän siirtäminen ihmiselle tai toiselle sovitulle toimijalle, kun agentti ei pysty ratkaisemaan sitä turvallisesti.

## Palautuminen (recovery)

Prosessi, jolla agentti palautuu virheestä tai yrittää uudelleen.

## Palaute (feedback)

Tieto siitä, kuinka agentin toiminta onnistui. Palaute voidaan käyttää arviointiin tai erilliseen kehitys- ja koulutusprosessiin; käytössä oleva agentti ei automaattisesti opi siitä.

---
