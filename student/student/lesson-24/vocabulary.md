# Sanasto – Lesson 24: Turvallisuus

## Prompt injection
Hyökkäys, jossa hyökkääjä piilottaa ohjeita käyttäjän syötteeseen. Agentti sekoittaa ohjeistuksensa ja hyökkäyskäskyn.

## Hallusinaatio (hallucination)
Kun kielimalli keksii tosiasioita, joita ei ole. Agentti "muistaa" asiaa, jota ei tapahtunut.

## Minimioikeusperiaate (least privilege)
Anna agentille vain minimaalinen pääsy, jonka se tarvitsee. Rajoitus tekee turvallisemmaksi.

## Validointi (validation)
Tarkistus, että syöte on järkevä ennen kuin annetaan agentille. Poistaa selvästi väärät syötteet.

## Rajoitus (restriction)
Toiminta, joka estää agentin tekemästä vaarallisia asioita. Esim. whitelist, maksimirahat, hyväksynnät.

## Seuranta (monitoring)
Jokaisen agentin toiminnon kirjaus lokiin. Mahdollistaa virheenetsinnän ja turvallisuusanalyysin.

## Lokitus (logging)
Kirjaus siitä, mitä agentti teki. Milloin aloitti, mitä kutsui, mitä tapahtui.

## Palautuminen (recovery)
Kyky kumota virheitä tai palautua kriisistä. Jos menee pieleen, osaa korjata.

## Turvakerros (security layer)
Komponentti, joka tarkistaa agentin päätöksiä. Varmistaa, että agentti noudattaa sääntöjä.

## Erittely (separation)
Selvästi erottaa agentin ohjeistus käyttäjän syötteestä. Merkitse [USER INPUT] ja [SYSTEM].

## Ankkurointi (grounding)
Yhteys todellisuuteen. Agentti perustaa päätöksensä konkreettisiin tietoihin, ei hallusinaatioihin.

## Varmuuskynnys (confidence threshold)
Jos agentti on alle 70% varma, se ei toimi vaan pyytää ihmisen apua.

## Tarkistusaskeleet (verification steps)
Erilliset askeleet, jotka tarkistavat agentin vastauksia ennen kuin ne lähetetään.

## Audit trail
Jälki siitä, mitä agentti teki ja miksi. Tärkeä oikeudellisesti ja turvallisuuden kannalta.
