# Sanasto – Lesson 21: Agentin muisti ja konteksti

## Konteksti-ikkuna (context window)
Agentin lyhytkestoinen muisti. Agentti näkee vain ikkunan sisällä olevan tiedon (viimeisimmät viestit). Kun uusi viesti tulee, vanhin poistuu.

## Pitkäaikainen muisti (long-term memory)
Pysyvä tietovarasto (kuukaudet, vuodet). Sisältää asiakkaiden historiat ja aikaisemmat tapaukset.

## Vektoritietokanta (vector database)
Erikoistunut tietokanta, joka ymmärtää merkityksiä, ei vain sanoja. "Maksuvirhe" ja "laskutusongelma" ovat semanttisesti samankaltaisia.

## Semantiikka / merkityksellinen haku (semantic search)
Haku, joka etsii samankaltaisuutta merkitykseltään, ei sanasta sanaan. "Kuinka maksan laskun" löytää myös "maksun suorittaminen".

## Vektori (vector)
Matemaattinen esitys sanan tai lauseen merkityksestä. Numerojono, joka edustaa merkityksen paikkaa suuressa tilassa.

## Tila (state)
Prosessin nykyinen vaihe. Tilauksen tilat: "luotu", "maksettu", "pakattu", "lähetetty".

## Tilamuuttuja (state variable)
Numero tai arvo, jonka agentti seuraa tietyssä tilassa. Esim. "yritykset: 2/3" tai "summa: 50€".

## Soul
Agentin pysyvä identiteetti ja syvät arvot, jotka se kantaa kaikissa tilanteissa.

## Konteksti (context)
Ympäröivät tiedot ja tilanteen tausta. Asiakkaan historia, edellinen keskustelu, nykyinen tehtävä.

## Muisti- ja kontekstijärjestelmä
Kolmen osan yhdistelmä: konteksti-ikkuna (nykyisyys), pitkäaikainen muisti (menneisyys), tila (prosessin vaihe).

## Ankkurointi (grounding)
Yhteys todellisuuteen. Agentti pysyy ankkuroituna, kun se perustaa päätökset konkreettisiin tietoihin.

## Hallusinaatio (hallucination)
Kun kielimalli keksii tosiasioita, joita ei ole. Agentti "muistaa" asiaa, jota ei koskaan tapahtunut.

## Varmuusprosentti (confidence score)
Mitta siitä, kuinka varma agentti on vastauksestaan. 95% = varma, 50% = epävarma.
