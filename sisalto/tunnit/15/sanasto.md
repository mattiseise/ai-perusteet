# Sanasto

## Tietopohja (knowledge base)

Tieto, jonka varassa botti vastaa — esimerkiksi tuotelista, ohjeet ja usein kysytyt kysymykset. Ilman ajantasaista tietopohjaa botti arvailee ja voi antaa virheellisiä vastauksia.

## RAG (retrieval-augmented generation)

Haulla täydennetty tekstintuotto: tapa, jolla botti käyttää tietopohjaa. Ensin **hakuvaihe** etsii tietopohjasta kysymykseen osuvimmat tekstikatkelmat, sitten kielimalli muodostaa vastauksen niiden pohjalta. Botti ei siis lue koko tietopohjaa joka kysymyksellä, vaan vastaa löydettyjen katkelmien varassa.

## Hakuvaihe

RAG:n ensimmäinen vaihe: järjestelmä etsii tietopohjasta ne kohdat, jotka muistuttavat eniten käyttäjän kysymystä, ja poimii niistä osuvimmat. Jos haku ei osu, tieto voi silti olla aineistossa — erota siksi tilanne "tietoa ei ole aineistossa" tilanteesta "järjestelmä ei löytänyt aineistossa olevaa tietoa".

## Tekstikatkelma

Tietopohjan aineistosta pilkottu pieni pala, tyypillisesti muutaman kappaleen mittainen, jota haku voi käsitellä yksitellen. Hakuvaihe poimii kysymykseen osuvimmat katkelmat ja liittää ne mallin kontekstiin vastausta varten.

## Rajaus

Botin "en osaa" tai "en saa tehdä tätä" -kohdat: mihin aiheisiin botti vastaa ja mitä se ei saa tehdä. Rajaukset asetetaan ohjeistuksella ja suojaavat sekä käyttäjää että bottia.

## Varmuuskynnys

Jos botti ei ole riittävän varma vastauksestaan, sen pitää sanoa, ettei se tiedä, eikä yrittää arvata.

## Positiivinen testi

Testi, jossa kokeillaan tilanteita, joiden pitäisi toimia — kysymyksiä, joihin botti on suunniteltu vastaamaan.

## Negatiivinen testi

Testi, jossa kokeillaan tilanteita, joiden ei pitäisi toimia: botin pitää osata kieltäytyä, rajata vastaustaan tai ohjata käyttäjä oikeaan paikkaan.

## Reunatapaus

Outo tai epätavallinen syöte, kuten tyhjä tai hyvin sekava kysymys. Reunatapaukset paljastavat, kuinka kestävä botti on.

## Iterointi

Testaa–korjaa–testaa uudelleen -kierros, jolla bottia parannetaan vähitellen. Normaali osa botin kehittämistä — ensimmäinen versio on harvoin valmis.

## Eskalointi

Asian ohjaaminen ihmiselle silloin, kun botti ei osaa tai saa hoitaa sitä.

## Kuratointi

Sisällön valitsemista, järjestämistä ja esittämistä niin, että se palvelee tiettyä tarkoitusta tai kohderyhmää — esimerkiksi botin tietopohjan kokoaminen selkeäksi kokonaisuudeksi.

---
