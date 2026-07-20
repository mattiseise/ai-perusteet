# Sanasto – oppitunti 24: Turvallisuus

## Harness

Kielimallia ympäröivä järjestelmä, joka toimeenpanee turvarajat. Harness tarkistaa syötteitä, rajaa oikeuksia, vaatii tarvittaessa hyväksynnän, lokittaa toiminnan ja huolehtii virheistä palautumisesta.

## Promptihyökkäys

Hyökkäys, jossa hyökkääjä piilottaa ohjeita käyttäjän syötteeseen. Agentti sekoittaa ohjeistuksensa ja hyökkäyskäskyn.

## Hallusinaatio (hallucination)

Kun kielimalli keksii tosiasioita, joita ei ole. Agentti "muistaa" asiaa, jota ei tapahtunut.

## Minimioikeusperiaate (least privilege)

Harness antaa agentille vain tehtävän kannalta välttämättömät oikeudet. Näin mahdollisen virheen tai hyökkäyksen seuraukset jäävät pienemmiksi.

## Validointi (validation)

Rakenteen, tietotyyppien, pituuden ja arvorajojen tarkistus ennen käsittelyä. Validointi voi hylätä väärän muodon, mutta ei luotettavasti tunnista kaikkia haitallisia ohjeita eikä todista sisältöä turvalliseksi.

## Rajoitus (restriction)

Rakenteiset työkalut, minimioikeudet, sallittujen toimintojen lista, arvorajat, salaisuuksien eristys ja hyväksyntäportit, joilla mahdollinen vahinko rajataan.

## Seuranta (monitoring)

Jokaisen agentin toiminnon kirjaus lokiin. Mahdollistaa virheenetsinnän ja turvallisuusanalyysin.

## Lokitus (logging)

Kirjaus siitä, mitä agentti teki. Milloin aloitti, mitä kutsui, mitä tapahtui.

## Palautuminen (recovery)

Kyky kumota virheitä tai palautua kriisistä. Jos menee pieleen, osaa korjata.

## Turvakerros (security layer)

Yksi osa kerroksittaista suojausta. Se voi tarkistaa rakenteen, rajata toimintaa, vaatia hyväksynnän, lokittaa tai tukea palautumista. Yksikään turvakerros ei yksin takaa sääntöjen noudattamista.

## Erittely (separation)

Järjestelmän ohjeiden, käyttäjän syötteen ja ulkoisen sisällön rakenteellinen erottaminen. Ulkoinen sisältö käsitellään epäluotettavana datana, mutta merkintä ei yksin estä promptihyökkäyksiä.

## Ankkurointi (grounding)

Yhteys todellisuuteen. Agentti perustaa päätöksensä konkreettisiin tietoihin, ei hallusinaatioihin.

## Varmuuskynnys (confidence threshold)

Jos agentti on alle 70% varma, se ei toimi vaan pyytää ihmisen apua.

## Tarkistusaskeleet (verification steps)

Erilliset askeleet, jotka tarkistavat agentin vastauksia ennen kuin ne lähetetään.

## Audit trail

Jälki siitä, mitä agentti teki ja miksi. Tärkeä oikeudellisesti ja turvallisuuden kannalta.

---
