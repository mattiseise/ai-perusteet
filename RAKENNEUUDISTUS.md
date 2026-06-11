# AI Perusteet — rakenneuudistussuunnitelma

## Lähtötilanne ja ongelmat

### Havaitut päällekkäisyydet

**OSP1 ↔ OSP2 (korkea vakavuus)**

1. **Kontekstin rakentaminen** — L4 opettaa viiden komponentin kontekstin (rooli, tausta, tavoite, rajoitteet, esimerkit). L11 opettaa saman viiden elementin mallin uudestaan (tavoite, rooli, rajoitteet, muoto, esimerkit). L12 jatkaa kontekstin rakentamista iteratiivisesti. Ongelma: L11 esittää samat käsitteet kuin uudet, vaikka ne on jo opittu.

2. **Multimodaalisuus** — L6 opettaa multimodaalisuuden teorian (kuvat, ääni, teksti, turvallisuus). L14 opettaa "visuaalisen debuggauksen" mutta käytännössä kertaa L6:n sisällön (kuvakaappaukset > tekstikuvaus, tietoturva, rajattu syöte). Uutta sisältöä on hyvin vähän.

3. **Hallusinaatiot** — L7 käsittelee hallusinaatiot ja satunnaisuuden perusteellisesti. Sama asia nousee L3:ssa (mekaniikka), L9:ssä (turvallisuus) ja L23:ssa (agenttiturvallisuus) ilman selkeää "tämä on kertausta" -kehystystä.

**OSP1/2 ↔ OSP3 (keskitaso)**

4. **Konteksti-ikkuna** — L5 opettaa konteksti-ikkunan, FIFO-periaatteen, ja kolme strategiaa (tiivistys, pilkkominen, ankkurointi). L20 opettaa täsmälleen samat konseptit agentin kontekstissa. Uutta on vektoritietokanta ja tila, mutta konteksti-ikkunaosuus on puhdasta toistoa.

5. **System prompt → Soul** — L15-16 opettaa system promptin botin sydämenä. L20 opettaa "soulin" agentin identiteettinä. Konsepti on sama (pysyvät ohjeet, jotka ohjaavat käyttäytymistä), kehys eri.

### Rakenteellinen ongelma: OSP2 on sekava

OSP2 yrittää kattaa liikaa: työkaluvertailun (L10), promptauksen alusta (L11-12), rakenteisen outputin (L13), multimodaalisuuden uudestaan (L14), ammattimaisen käytön (L15), ja botin rakentamisen (L16-18). Tästä puuttuu johdonmukainen punainen lanka.

### Puuttuva sisältö: työkaluosaaminen

Kurssilta puuttuu käytännön työkaluihin tutustuminen. Opiskelijat käyttävät lähes yksinomaan ChatGPT:tä. Claude, Copilot, Gemini ja kiinalaiset mallit (DeepSeek, Qwen) mainitaan ohimennen mutta niihin ei koskaan tutustuta käytännössä.

---

## Uusi rakenne

### Suunnitteluperiaatteet

1. **Ei oppituntiviittauksia materiaalissa.** Ei "Kuten opimme L4:ssä" vaan "Kuten olemme jo aiemmin oppineet..."
2. **Kertaus kehystetään kertaukseksi.** Jos konsepti toistuu, se sanotaan ääneen: "Muistatko, kun puhuimme konteksti-ikkunasta? Nyt sovellamme samaa ideaa..."
3. **Jokainen oppitunti tuo jotain uutta.** Ei puhdasta toistoa uutena sisältönä.
4. **OSP2:een lisätään työkaluosaaminen.** Claude, Copilot, ChatGPT, kiinalaiset mallit — kädet saveen.

### OSP1: Teoria (oppitunnit 1–9)

OSP1 toimii pääosin hyvin. Pieniä tarkennuksia:

| # | Otsikko | Sisältö | Muutos |
|---|---------|---------|--------|
| 1 | Älykäs vai sääntö? | AI vs. automaatio, probabilistinen ajattelu | Ei muutoksia |
| 2 | Viisi tekoälyn tasoa | Narrow AI → ML → GenAI → AGI → ASI | Ei muutoksia |
| 3 | Miten kone kirjoittaa? | Tokenit, parametrit, next-token prediction, temperature | Ei muutoksia |
| 4 | Konteksti ratkaisee | Kontekstin 5 komponenttia, iteratiivinen rakentaminen | **Yhdistetään promptauksen perusteet tähän** (siirretty L11:sta). Tämä oppitunti opettaa sekä kontekstin merkityksen että hyvän promptin perusrakenteen. |
| 5 | Muistin rajat | Konteksti-ikkuna, FIFO, tiivistys/pilkkominen/ankkurointi | **Lyhennetään strategiaosuus**, koska nämä palautuvat agenttiosan yhteydessä käytännön kontekstissa |
| 6 | Kuvat, ääni ja teksti | Multimodaalisuus: kuvakaappaukset, lokit, tietoturva | **Yhdistetään L14:n käytännön esimerkit tähän**. Yksi kattava oppitunti multimodaalisuudesta teoriasta käytäntöön. |
| 7 | Miksi tekoäly valehtelee? | Hallusinaatiot, satunnaisuus, verifiointiprosessi | Ei muutoksia |
| 8 | Kenen teksti se on? | Etiikka, tekijänoikeus, bias, ympäristö | Ei muutoksia |
| 9 | Tuomaripöydän päätös | OSP1 arviointi: asiantuntijalausunto | Ei muutoksia |

**Muutosten vaikutus:** L4 laajenee (+ promptauksen perusteet), L5 tiivistyy, L6 laajenee (+ käytännön debuggaus). Tämä vapauttaa tilaa OSP2:ssa.

### OSP2: Käyttö ja työkalut (oppitunnit 10–18)

**Iso rakennemuutos.** OSP2 jakautuu kahteen selkeään osaan: (A) Työkaluihin tutustuminen ja (B) Oman botin rakentaminen.

| # | Otsikko | Sisältö | Muutos |
|---|---------|---------|--------|
| 10 | Työkalupaletti — ChatGPT, Claude ja Copilot | **Käytännön vertailu:** Sama tehtävä kolmella työkalulla. ChatGPT:n vahvuudet (yleiskäyttö, plugins), Clauden vahvuudet (pitkä konteksti, turvallisuus, koodaus), Copilotin vahvuudet (Microsoft-integraatio, toimistotyö). Erojen dokumentointi. | **Laajennetaan merkittävästi.** Nykyinen L10 mainitsee työkalut pintapuolisesti — uudessa versiossa opiskelijat käyttävät jokaista. |
| 11 | **UUSI: Vaihtoehtoiset mallit — Gemini, DeepSeek ja avoimet mallit** | Googlen Gemini (multimodaalinen, integraatio Google-ekosysteemiin), kiinalaiset mallit (DeepSeek, Qwen: vahvuudet, rajoitukset, tietosuojakysymykset), avoimet mallit (Ollama, lokaali ajo). Milloin mikäkin kannattaa? | **Kokonaan uusi oppitunti.** Täyttää suuren aukon: opiskelijat oppivat, että AI-kenttä on laajempi kuin ChatGPT. |
| 12 | Rakenteinen output käytännössä | Markdown, JSON, CSV, taulukot — output jota voi käyttää suoraan. Iteratiivinen tarkentaminen. | **Säilytetään** (nykyinen L13), siirretään tähän kohtaan. Promptauksen perusteet on jo opittu L4:ssä, joten L12 voi keskittyä puhtaasti outputin muotoiluun. |
| 13 | Ammattimainen AI-avusteinen työ | Dokumentaatio, lokien analysointi, CLI-komennot, koodin generointi — tekoäly työparina. | **Yhdistetään** nykyinen L15 (ammattimainen käyttö) tähän. |
| 14 | Botin suunnittelu | Tarkoitus, rooli, ohjeet, persoona, system prompt, rajoitteet | **Säilytetään** (nykyinen L15-16), tiivistetään yhteen oppituntiin koska konteksti ja promptaus on jo opittu. |
| 15 | Botin tietopohja ja testaus | Knowledge base, rajoitteet, kolme testityyppiä (positiivinen, negatiivinen, raja-arvot), iteraatio | **Säilytetään** (nykyinen L16-17), tiivistetään. |
| 16 | **UUSI: AI-työkalut erikoisaloilla** | Kuvageneraatio (DALL-E, Midjourney), musiikki (Suno), video (Runway), koodaus (Cursor, GitHub Copilot). Käytännön kokeilut: generoi kuva, kokeile koodausavustajaa. | **Uusi oppitunti.** Nykyisin nämä mainitaan L10:ssä listana — nyt opiskelijat kokeilevat käytännössä. |
| 17 | Boteista agentteihin — silta OSP3:een | Agentti ≠ chatbot ≠ workflow. Kuusi komponenttia. Suoritusputki. | **Säilytetään** (nykyinen L18), siirretään siltaluvuksi. |
| 18 | OSP2 arviointi: Feature flag -järjestelmä | Koodaa AI:n avulla, testaa, dokumentoi | **Säilytetään** (nykyinen L17-18) |

**Muutosten vaikutus:**
- L11/L12 (promptauksen toisto) **poistetaan** — sisältö on jo L4:ssä
- L14 (multimodaalisuuden toisto) **poistetaan** — sisältö on jo L6:ssa
- Vapautuvaan tilaan tulee **kaksi uutta oppituntia**: vaihtoehtoisten mallien käytännön vertailu (L11) ja erikoistyökalut (L16)
- Botin rakentaminen tiivistyy 3 → 2 oppituntiin (konteksti/promptaus ei tarvitse opettaa uudestaan)

### OSP3: Agentit (oppitunnit 19–27)

OSP3 on rakenteellisesti parhaassa kunnossa. Yksi korjaus:

| # | Otsikko | Sisältö | Muutos |
|---|---------|---------|--------|
| 19 | Automaatio vai autonomia? | Kolme tasoa, päätöspuu, milloin agentti kannattaa | Ei muutoksia |
| 20 | Agentin muisti ja konteksti | Konteksti-ikkuna, pitkäaikainen muisti, tila, soul | **Konteksti-ikkunaosuus lyhennetään** viittaukseksi: "Kuten olemme jo aiemmin oppineet, konteksti-ikkuna on rajallinen..." Sen sijaan laajennetaan vektoritietokantoja, tilanhallintaa ja soulia — nämä ovat agenteille uniikkia sisältöä. |
| 21 | Agentin työkalut | Tiedostot, verkkohaku, CLI, orkestrointi | Ei muutoksia |
| 22 | Suunnittelumallit | ReAct, ketjuajattelu, moniagenttijärjestelmät | Ei muutoksia |
| 23 | Turvallisuus ensin | Prompt injection, hallusinaatiot, minimioikeus, turvakerrokset | **Kehystetään selkeästi jatkoksi:** "Muistatko, kun puhuimme hallusinaatioista ja tietoturvasta? Agenteilla panokset ovat paljon korkeammat..." |
| 24 | Ihminen portinvartijana | Human-in-the-loop, hyväksyntäportit, timeout-strategiat | Ei muutoksia |
| 25 | Kädet saveen — n8n-paja | n8n-perusteet, komponenttien yhdistäminen, projektisuunnittelu | Ei muutoksia |
| 26 | Viimeistele ja esittele | Iteratiivinen rakentaminen, turvakerrokset, testaus, dokumentaatio | Ei muutoksia |
| 27 | OSP3 arviointi ja yhteenveto | Agenttiprojektin esittely ja arviointi | Ei muutoksia |

---

## Yhteenveto muutoksista

### Poistetaan (puhdasta overlappia)

| Vanha | Sisältö | Syy | Minne siirtyy |
|-------|---------|-----|---------------|
| L11 | Promptauksen perusteet | Identtinen L4:n kanssa | Yhdistetään L4:ään |
| L12 | Kontekstin iteratiivinen rakentaminen | Soveltava osa L4:stä | Harjoitukset siirtyvät L4:n tehtäviin |
| L14 | Visuaalinen debuggaus / multimodaalisuus | Identtinen L6:n kanssa | Yhdistetään L6:een |

### Lisätään (uutta sisältöä)

| Uusi | Sisältö | Perustelu |
|------|---------|-----------|
| L11 (uusi) | Gemini, DeepSeek, Qwen, avoimet mallit | Opiskelijat tarvitsevat laajemman kuvan AI-kentästä |
| L16 (uusi) | Erikoistyökalut: kuva, musiikki, video, koodi | Nykyisin vain mainitaan — nyt kokeillaan käytännössä |

### Muokataan (toiston poisto / kertauksen kehystys)

| Tunti | Muutos |
|-------|--------|
| L4 | Laajenee: + promptauksen perusteet (viisi elementtiä) |
| L5 | Tiivistyy: strategiat lyhyemmin, palautuvat L20:ssa |
| L6 | Laajenee: + käytännön debuggaus, lokianalyysit |
| L10 | Laajenee: syvällinen kolmen työkalun vertailu |
| L20 | Konteksti-ikkunaosuus lyhenee → laajenee vektoritietokannat + tila |
| L23 | Kehystetään jatkoksi aiemmin opitulle turvallisuudelle |

### Läpileikkaava muutos: viittaustyyli

**ENNEN:** "Kuten opimme oppitunnilla 4..."
**JÄLKEEN:** "Kuten olemme jo aiemmin oppineet..." / "Muistatko, kun puhuimme kontekstin merkityksestä?"

Tämä tekee materiaalista joustavamman — oppituntien järjestystä voi muuttaa tulevaisuudessa ilman, että viittaukset hajoavat.

---

## Pedagoginen perusteluu

### Kolme punaista lankaa säilyvät

1. **Tuomaripöytä** (L9): Arvioi tekoälyn käyttöä asiantuntijana — vaatii OSP1:n teorian
2. **Custom-GPT / botti** (L14-15 uusi, L18): Rakenna oma botti — vaatii kontekstin, promptauksen ja testauksen
3. **n8n-agentti** (L25-27): Rakenna agentti — vaatii kaikki edelliset

### Terveen kertauksen periaate

Kertaus on terveellistä kun:
- Se on **kehystetty kertaukseksi** ("Muistatko...")
- Se **soveltaa** aiempaa uuteen kontekstiin (hallusinaatiot chatissa → hallusinaatiot agentissa)
- Se **lisää jotain uutta** (konteksti-ikkuna → konteksti-ikkuna + vektoritietokanta)

Kertaus on haitallista kun:
- Se esittää vanhan asian uutena
- Se vie aikaa, joka voitaisiin käyttää uuden oppimiseen
- Se tylsistyttää opiskelijoita, jotka ovat jo ymmärtäneet asian

### Uusien oppituntien tarve

**Työkalujen monipuolisuus** on kriittinen työelämätaito. Opiskelija, joka osaa vain ChatGPT:tä, on kuin mekaanikko joka tuntee vain yhden työkalumerkin. Uudet oppitunnit (L11 vaihtoehtomallit, L16 erikoistyökalut) antavat opiskelijoille valmiudet arvioida ja valita oikea työkalu kuhunkin tehtävään — mukaan lukien tietosuoja- ja kustannusnäkökulmasta.

**Kiinalaiset mallit** (DeepSeek, Qwen) ovat erityisen ajankohtaisia: ne ovat ilmaisia tai halpoja, tehokkaita, mutta herättävät tietosuojakysymyksiä. Ammattilaisen pitää osata arvioida nämä trade-offit.
