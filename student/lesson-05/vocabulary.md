# Sanasto

## Konteksti-ikkuna (context window)
Tokeneista määritellyt raja, joka rajoittaa kuinka paljon tekstiä tekoälymallit voivat käsitellä yhdessä keskustelussa. Kun raja täyttyy, vanhin tieto häviää. Esim. ChatGPT-4:n ikkuna on 128 000 tokenia.

## Token
Pienin tekstin yksikkö, jonka tekoäly käsittelee. Ei täsmälleen sana — noin 4 merkkiä = 1 tokeni. Tarkka suhde riippuu kielestä ja mallista.

## Tiivistys (summarization)
Tekniikka, jossa pitkä teksti (esim. lokitiedosto tai keskustelu) pakataan pienemmäksi, oleellisen säilyttäen. Auttaa konteksti-ikkunan hallinnassa vapauttamalla tilaa.

## Pilkkominen (chunking)
Strategia, jossa jaetaan suuri tehtävä moneen pienempään osaan. Jokainen osa käsitellään omassa keskustelussa, omassa puhtaassa ikkunassa.

## Ankkurointi (anchoring)
Tekniikka, jossa tärkeä konteksti (rooli, rajaukset, project-spesificiset oletukset) toistetaan joka viestissä, varmistamalla että se ei unohdu vaikka ikkuna täyttyisi.

## FIFO (First In, First Out)
Periaate, jolla konteksti-ikkuna toimii: ensimmäinen teksti sisään on ensimmäinen ulos. Vanhempi tieto poistetaan ensin.

## Konversaation hallinta (conversation management)
Strategiat, joilla hallitaan pitkiä tekoäly-keskusteluja niin että oleellinen tieto säilyy. Sisältää tiivistystä, pilkkomista ja ankkurointia.

## Muistin rajoitus (memory limitation)
Tekninen rajoitus, joka estää tekoälyä muistamasta rajattomasti kaikkea. Johtaa konteksti-ikkunan tarpeellisuuteen.

## Projekti-konteksti (project context)
Tiedot, jotka ovat tärkeät tietyn IT-projektin kaikkiin keskusteluihin — kehys-teknologia, käyttäjä-roolit, tietokanta. Ankkuroidaan toistamisesti.

## Uuden ikkunan avaava (opening a new window)
Käytäntö, jossa aloitetaan uusi keskustelu tekoälyn kanssa "puhtaalla" konteksti-ikkunalla, sen sijaan että jatkettaisiin vanhaa, täyttynyttä ikkunaa.

## Dokumento versio-hallinta (version tracking)
Käytäntö, jossa dokumentoidaan tekoälyn kanssa tehdyt tulokset päiväkohtaisesti tai vaiheittain, jotta tiedot eivät menesty uusiin ikkunoihin.
