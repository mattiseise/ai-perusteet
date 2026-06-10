# Sanasto

## Konteksti-ikkuna (context window)

Tokeneina määritelty raja, joka rajoittaa sitä, kuinka paljon tekstiä tekoälymallit voivat käsitellä yhdessä keskustelussa. Kun raja täyttyy, vanhin tieto häviää. Esim. GPT-4-mallin ikkuna oli 128 000 tokenia; uudemmissa malleissa ikkuna voi olla paljon suurempi.

## Token

Pienin tekstin yksikkö, jonka tekoäly käsittelee. Ei täsmälleen sana — noin 4 merkkiä = 1 tokeni. Tarkka suhde riippuu kielestä ja mallista.

## Tiivistys (summarization)

Tekniikka, jossa pitkä teksti (esim. lokitiedosto tai keskustelu) pakataan pienemmäksi oleellisen säilyttäen. Auttaa konteksti-ikkunan hallinnassa vapauttamalla tilaa.

## Pilkkominen (chunking)

Strategia, jossa suuri tehtävä jaetaan moneen pienempään osaan. Jokainen osa käsitellään omassa keskustelussaan, omassa puhtaassa ikkunassaan.

## Ankkurointi (anchoring)

Tekniikka, jossa tärkeä konteksti (rooli, rajaukset, projektikohtaiset oletukset) toistetaan joka viestissä ja varmistetaan, ettei se unohdu, vaikka ikkuna täyttyisi.

## FIFO (First In, First Out)

Periaate, jolla konteksti-ikkuna toimii: ensimmäinen teksti sisään on ensimmäinen ulos. Vanhempi tieto poistetaan ensin.

## Konversaation hallinta (conversation management)

Strategiat, joilla hallitaan pitkiä tekoälykeskusteluja niin, että oleellinen tieto säilyy. Sisältää tiivistystä, pilkkomista ja ankkurointia.

## Muistin rajoitus (memory limitation)

Tekninen rajoitus, joka estää tekoälyä muistamasta rajattomasti kaikkea. Johtaa konteksti-ikkunan tarpeellisuuteen.

## Projektikonteksti (project context)

Tiedot, jotka ovat tärkeitä tietyn projektin kaikissa keskusteluissa — esimerkiksi aihe, tavoite, tyyli ja keskeiset rajaukset. Ankkuroidaan toistuvasti.

## Uuden ikkunan avaaminen (opening a new window)

Käytäntö, jossa aloitetaan uusi keskustelu tekoälyn kanssa "puhtaalla" konteksti-ikkunalla sen sijaan, että jatkettaisiin vanhaa, täyttynyttä ikkunaa.

## Dokumentin versiohallinta (version tracking)

Käytäntö, jossa dokumentoidaan tekoälyn kanssa tehdyt tulokset päiväkohtaisesti tai vaiheittain, jotta tiedot eivät häviä uusiin ikkunoihin.

---
