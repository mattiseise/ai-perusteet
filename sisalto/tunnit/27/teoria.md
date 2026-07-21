# Viimeistele ja puolusta — agentti valmiiksi 90 minuutissa

## Johdanto: yksi rajattu näyttö, yksi oppitunti

Tunnilla 26 teit teknisen n8n-minimiversion tai dokumentoidun suunnitelman. Tällä tunnilla viet valitsemasi polun loppuun, testaat sen, korjaat yhden havaitun puutteen, ajat saman testin uudelleen ja puolustat ratkaisuasi lyhyesti. Koko pakollinen suoritus tehdään yhden 90 minuutin oppitunnin aikana.

| Aika | Mitä teet? |
|---|---|
| 0–8 min | Avaa työ ja rajaa tämän tunnin näyttö |
| 8–30 min | Viimeistele toteutus tai dokumentoitu suunnitelma |
| 30–48 min | Aja yksi normaali, yksi reuna- ja yksi turvallisuustesti |
| 48–63 min | Tee yksi perusteltu korjaus ja aja sama testi uudelleen |
| 63–75 min | Kokoa tiivis näyttöpaketti |
| 75–88 min | Pidä 2–3 minuutin puolustus pienryhmässä, tallenteena tai opettajan valitsemassa otoksessa |
| 88–90 min | Palauta tai tallenna näyttöpaketti |

Pakollista työtä ei jätetä kotiin. Jos jokin tekninen liitäntä ei valmistu ajassa, rajaa näyttöä ja kuvaa rajoitus rehellisesti. Lisätestit, laajemmat integraatiot ja pidempi dokumentaatio ovat vapaaehtoista syventämistä.

> **Agentin ohjauskehyksen näkökulma:** Kummassakin toteutuspolussa osoitat, missä kielimalli tekee aidon rajatun valinnan ja miten agentin ohjauskehys rajaa sallitut vaihtoehdot, työkalut, oikeudet, tilan, turvallisuuden ja lokituksen.

## Kaksi samanarvoista toteutuspolkua

**Teknisessä polussa** viimeistelet rajatun n8n-työnkulun ja näytät sen suoritusnäkymästä syötteen, kielimallin valinnan, seuraavan haaran tai toiminnon sekä tuloksen. Jos jokin ulkoinen liitäntä ei toimi, voit käyttää turvallista testiympäristöä tai rajattua korviketta, kunhan kerrot sen näkyvästi.

**Dokumentoidussa polussa** viimeistelet kaavion, työkalusopimukset ja vaihe vaiheelta seurattavan suoritusjäljen. Teet vähintään yhden todellisen kielimallikutsun, jossa malli valitsee vähintään kahdesta sallitusta vaihtoehdosta. Sen jälkeen seuraat kaavion ennalta määriteltyjä vaiheita ja erotat toteutetun mallikutsun simuloiduista toiminnoista.

Polkuja arvioidaan samalla kysymyksellä: osoittaako esitetty todistusaineisto järjestelmän rakenteen, aidon rajatun mallivalinnan, testituloksen, korjauksen, uudelleentestin ja turvallisuusratkaisun? Teknistä polkua ei palkita pelkästä toimivasta liitännästä, eikä dokumentoitua polkua rangaista siitä, ettei se väitä simuloitua toimintoa toteutetuksi.

## Viimeistele vain olennainen

Tarkista kuusi rakennusosaa niiden kanonisilla nimillä: **syötekäsittelijä**, **päättelijä ja suunnittelija**, **työkalujen suorittaja**, **muisti ja konteksti**, **turvakerros** sekä **seuranta ja palautesilmukka**. Niitä ei tarvitse toteuttaa kuutena solmuna. Merkitse kustakin lyhyesti, missä vastuu näkyy tai miksi sitä ei tarvita tässä rajatussa agentissa.

Varmista erityisesti neljä asiaa. Syöte on näkyvissä. Kielimalli tekee aidon rajatun valinnan vähintään kahdesta sallitusta vaihtoehdosta. Valintaa seuraava toiminto tai simuloitu vaihe on jäljitettävissä. Turvakerros pysäyttää tai eskaloi tilanteen havaittavan ehdon perusteella.

Havaittava eskalointiehto voi olla esimerkiksi hyväksytyn lähteen puuttuminen, lähteiden ristiriita, pakollisen tiedon puuttuminen, validoinnin epäonnistuminen, työkalun virhe tai ennalta määritelty riskiluokka. Mallin itse ilmoittama varmuusprosentti ei ole hyväksyntäraja.

## Testaa kolme erilaista tilannetta

Aja kolme testiä:

1. **Normaali tapaus**, jota varten agentti on suunniteltu.
2. **Reunatapaus**, kuten puuttuva pakollinen tieto tai ristiriitainen syöte.
3. **Turvallisuustesti**, kuten yritys ohittaa rajat tai käynnistää toiminto ilman vaadittua hyväksyntää.

Kirjaa jokaisesta testistä syöte, odotettu tulos, todellinen tulos ja johtopäätös. Tekninen polku ottaa todellisen tuloksen suoritusnäkymästä. Dokumentoitu polku kirjaa todellisen kielimallivalinnan ja sitä seuraavan käsin kuljetun suoritusjäljen. Kummassakin polussa pitää näkyä, mikä osa on toteutettu ja mikä simuloitu.

Testin ei tarvitse onnistua ensimmäisellä kerralla. Epäonnistunut testi on hyödyllinen, jos se paljastaa korjattavan puutteen.

## Tee yksi korjaus ja uudelleentesti

Valitse testeistä yksi havaittu puute. Tee yksi rajattu muutos esimerkiksi järjestelmäohjeeseen, sallittujen vaihtoehtojen kuvaukseen, validointiin, työkalusopimukseen, turvarajaan, kaavioon tai virhepolkuun. Aja sama testi uudelleen samalla syötteellä.

Kirjaa neljä kohtaa: alkuperäinen tulos, tehty muutos, uudelleentestin tulos ja johtopäätös. Näin osoitat iteratiivisen kehityksen. Pelkkä väite ”korjasin sen” ei riitä, mutta suuren ominaisuuden rakentamista ei vaadita.

## Kokoa tiivis näyttöpaketti

Näyttöpaketti voi olla yksi sivu, yksi dia tai vastaava tiivis näkymä, jonka liitteenä ovat tarvittavat kuvat tai linkit. Siinä näkyvät:

- ongelma ja valittu toteutuspolku
- työnkulku tai kaavio sekä kuuden rakennusosan kattavuus
- syöte, vähintään kaksi sallittua vaihtoehtoa, kielimallin todellinen valinta ja sitä seuraava vaihe
- kolmen testin tulokset
- yksi korjaus ja sitä koskeva uudelleentesti
- tärkein turvallisuusraja ja toteutuksen rehellinen rajoitus

Näyttöpaketti ei ole kolme erillistä pitkää dokumenttia. Tavoite on tehdä ajattelu ja todistusaineisto nopeasti arvioitaviksi.

## Puolusta ratkaisuasi 2–3 minuuttia

Puolustuksessa vastaat neljään kysymykseen:

1. Mitä ongelmaa agentti ratkaisee ja mitä polkua käytit?
2. Missä kielimalli tekee aidon rajatun valinnan?
3. Mitä testi paljasti, mitä korjasit ja mitä uudelleentesti osoitti?
4. Mikä turvallisuusraja on tärkein ja mitä työsi ei vielä todista?

Puolustus voidaan järjestää pienryhmissä, lyhyenä tallenteena tai opettajan valitsemana otoksena. Näin kaikkien ei tarvitse esiintyä peräkkäin koko luokalle. Itsenäisessä verkko-opiskelussa voit tallentaa 2–3 minuutin puheenvuoron tai kirjoittaa vastaavan lyhyen puolustuksen saman 90 minuutin aikana.

## Arviointi

Molemmat toteutuspolut arvioidaan samoilla kriteereillä ja samalla painolla.

| Kriteeri | Paino | Mitä todistusaineistosta etsitään? |
|---|---:|---|
| **Rakenne ja toteutuspolun näyttö** | 20 % | Työnkulku tai kaavio on seurattava ja kuusi rakennusosaa on käsitelty perustellusti. |
| **Aito rajattu mallivalinta** | 25 % | Syöte, vähintään kaksi sallittua vaihtoehtoa, mallin valinta ja seuraava vaihe näkyvät. |
| **Testi, korjaus ja uudelleentesti** | 25 % | Kolme testitulosta sekä yhden puutteen ennen–jälkeen-näyttö ovat jäljitettävissä. |
| **Turvallisuus ja rajat** | 20 % | Oikeudet, havaittava eskalointiehto ja tärkein rajoitus on kuvattu tai toteutettu. |
| **Puolustus** | 10 % | Opiskelija perustelee ratkaisunsa ja erottaa toteutetun simuloidusta. |

Arvioinnissa tarkastellaan todistusaineiston laatua, ei teknisten solmujen määrää. Teknisen polun suoritusnäkymä ja dokumentoidun polun todellinen mallikutsu sekä simuloitu suoritusjälki ovat erilaisia mutta samanarvoisia tapoja osoittaa osaamista.

::: luokka
## Tunnin lopussa

Palauta tai näytä opettajan ohjeen mukaan tiivis näyttöpaketti. Siinä pitää näkyä toteutuspolun näyttö, kuuden rakennusosan tarkistus, aito rajattu mallivalinta, kolme testitulosta, yksi korjaus ja uudelleentesti sekä turvallisuusraja. Tämän lisäksi pakollista kotityötä ei anneta.
:::

::: verkko
## Tunnin lopussa

Tallenna tiivis näyttöpaketti ja 2–3 minuutin tallenne tai kirjallinen puolustus omaan portfolioosi. Rajaa työ 90 minuuttiin. Jos jokin jäi kesken, nimeä se rajoitukseksi sen sijaan, että laajentaisit pakollista suoritusta.
:::

## Yhteenveto

Olet vienyt rajatun agentin suunnitelmasta arvioitavaksi näytöksi. Tekninen ja dokumentoitu polku osoittavat osaamista eri todistusaineistolla, mutta molemmissa kielimalli tekee aidon rajatun valinnan ja agentin ohjauskehys pitää toiminnan hallittuna. Kolme testiä, yksi korjaus ja uudelleentesti osoittavat, että et vain kuvannut ideaa vaan arvioit ja paransit sitä.

> **Erota nämä:** Mitä todistusaineistosi osoittaa varmasti — ja mikä jäi oletukseksi, simulaatioksi tai jatkokehitykseksi?

---

## Lähteet ja tarkistuspäivä

- [NIST: Strengthening AI Agent Hijacking Evaluations](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations)
- [OWASP: Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
- [OWASP: Excessive Agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html)

Tarkistettu 15.7.2026.
