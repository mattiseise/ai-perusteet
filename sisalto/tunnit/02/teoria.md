# Kaksi akselia — kykyjen laajuus ja toteutustapa

## Johdanto

Tekstiä tuottava chat voi näyttää yleispätevältä, vaikka se ei osaa avata ovea, tarkistaa varastoa tai päättää, mitä tietoa sillä on lupa käyttää. Toisaalta pieni roskapostisuodatin voi olla erittäin tarkka yhdessä tehtävässä. Pelkkä nimilappu ”tekoäly” ei vielä kerro, mihin järjestelmä pystyy tai miten se on rakennettu.

Tällä tunnilla kuvaat tekoälyjärjestelmää kahdella toisistaan riippumattomalla akselilla. Ensimmäinen kertoo **kykyjen laajuudesta**: onko järjestelmä tarkoitettu rajattuun tehtävään vai väitetäänkö sen toimivan laajasti monenlaisissa tehtävissä? Toinen kertoo **toteutuksesta ja toiminnallisuudesta**: tunnistaako, ennustaako, tuottaako tai toimiiko järjestelmä, ja millä menetelmällä?

## Akseli 1: kykyjen laajuus

Rajattuun tehtävään rakennettu järjestelmä voi suodattaa roskapostia, ennustaa kysyntää tai ehdottaa seuraavaa sanaa. Sen suoritus voi olla erinomainen, mutta se ei siirrä osaamistaan vapaasti mihin tahansa uuteen tehtävään. Tästä käytetään usein nimitystä **kapea tekoäly** (narrow AI).

Laaja-alaisesta, ihmisen kaltaisesti uusiin tehtäviin sopeutuvasta järjestelmästä käytetään keskusteluissa nimitystä **yleinen tekoäly** (artificial general intelligence, AGI). AGI:lle ei ole yhtä yleisesti hyväksyttyä testiä tai määritelmää. Siksi siitä puhutaan tutkimus- ja tulevaisuuskäsitteenä, ei nykyisten tuotteiden varmana kehitysvaiheena.

Kykyjen laajuus ei ole viisiportainen kehitysjärjestys. Tekstiä, kuvaa ja ääntä käsittelevä järjestelmä voi olla monipuolinen ja silti rajattu. Samalla yhden tehtävän erikoisjärjestelmä voi ylittää ihmisen juuri siinä tehtävässä ilman yleistä ymmärrystä.

> **Pysähdy hetkeksi:** Mitä tehtävää jokin käyttämäsi tekoäly tekee hyvin, ja missä täysin erilaisessa tehtävässä sen osaaminen ei riitä?

## Akseli 2: toteutus ja toiminnallisuus

Toinen akseli kuvaa, mitä järjestelmä tekee ja millä rakenteella. Sama järjestelmä voi yhdistää useita rivejä seuraavasta taulukosta.

| Toiminnallisuus tai toteutus | Mitä se tekee | Esimerkki |
|---|---|---|
| Luokittelu | Valitsee syötteelle luokan | Roskaposti / ei roskapostia |
| Ennustaminen | Arvioi tulevaa arvoa tai todennäköisyyttä | Kysynnän ennuste |
| Generointi | Tuottaa uutta tekstiä, kuvaa, ääntä tai koodia | Tekstiluonnos promptista |
| Haku ja yhdistäminen | Hakee lähteestä tietoa vastauksen tueksi | Ohjehaku hyväksytystä tietopohjasta |
| Sääntöpohjainen päättely | Soveltaa ihmisen kirjoittamia ehtoja | Hyväksyntäraja euromäärän perusteella |
| Työkaluja käyttävä agentti | Valitsee ja kutsuu rajattuja työkaluja | Kalenteria lukeva ajanvarausagentti |

Generatiivinen tekoäly ei siis ole ”seuraava taso” koneoppimisen jälkeen. Generointi kuvaa toiminnallisuutta. Toteutus voi käyttää koneoppimismallia, hakua, sääntöjä ja ohjelmakoodia samassa palvelussa. Agentti puolestaan kuvaa järjestelmää, jossa kielimallin ympärillä oleva harness tarjoaa työkaluja, tilan, oikeudet ja valvonnan.

## Kaksi akselia yhdessä

Kuvitellaan kolme järjestelmää. Ensimmäinen luokittelee tukipyynnön aihealueen. Sen kykyjen laajuus on rajattu ja toiminnallisuus on luokittelu. Toinen chat tuottaa tekstiä monista aiheista. Sen käyttöala näyttää laajalta, mutta toiminta perustuu edelleen rajattuun malliin ja ympäröiviin työkaluihin; monipuolinen keskustelu ei yksin todista AGI:sta. Kolmas järjestelmä lukee kalenteria ja ehdottaa aikaa. Se on rajattu agentti, jonka toiminnallisuus yhdistää kielimallin, kalenterityökalun ja hyväksyntäsäännön.

<figure class="ai-demo"><span class="ai-demo__tag">// kaksi akselia: kuinka laajasti järjestelmä toimii ja mitä se tekee</span>
<div class="ai-demo__stage" style="height:auto;padding:18px 20px 12px">
<svg viewBox="0 0 560 330" width="100%" role="img" aria-labelledby="l02-title l02-desc" preserveAspectRatio="xMidYMid meet">
  <title id="l02-title">Tekoälyjärjestelmien kahden akselin kartta</title>
  <desc id="l02-desc">Vaaka-akseli kuvaa kykyjen laajuutta rajatusta laaja-alaiseen väitteeseen. Pystyakseli kuvaa toiminnallisuutta luokittelusta työkaluja käyttävään toimintaan. Roskapostisuodatin, tekstichat ja kalenteriagentti sijoittuvat eri kohtiin.</desc>
  <rect x="54" y="18" width="482" height="268" rx="14" fill="#11182A" stroke="#2B3552"/>
  <line x1="92" y1="252" x2="504" y2="252" stroke="#7E88A8" stroke-width="2"/>
  <line x1="92" y1="252" x2="92" y2="54" stroke="#7E88A8" stroke-width="2"/>
  <text x="92" y="276" fill="#B9C2DA" font-size="13">rajattu tehtävä</text>
  <text x="504" y="276" text-anchor="end" fill="#B9C2DA" font-size="13">laaja-alainen väite</text>
  <text x="24" y="154" transform="rotate(-90 24 154)" text-anchor="middle" fill="#B9C2DA" font-size="13">toiminnallisuus ja toimivalta</text>
  <circle cx="150" cy="205" r="10" fill="#7FD0A8"/><text x="166" y="210" fill="#EAEEF8" font-size="14">roskapostisuodatin</text>
  <circle cx="330" cy="155" r="10" fill="#46C7CF"/><text x="346" y="160" fill="#EAEEF8" font-size="14">tekstichat</text>
  <circle cx="230" cy="92" r="10" fill="#C9B7F1"/><text x="246" y="97" fill="#EAEEF8" font-size="14">kalenteriagentti</text>
</svg>
</div>
<figcaption class="ai-demo__cap">Järjestelmä kuvataan kahdella kysymyksellä: kuinka laajalle sen kyvyt on rajattu ja mitä toiminnallisuutta toteutus sisältää. Sijoitus ei ole arvojärjestys eikä kehitysportaikko.</figcaption></figure>

Kun arvioit uutista tai tuotetta, kirjoita ensin tarkka tehtävä: ”järjestelmä tuotti tekstin annetusta aineistosta” kertoo enemmän kuin ”tekoäly ymmärsi aiheen”. Merkitse sitten lähde, käyttöympäristö, työkalut ja rajat. Vasta tämän jälkeen voit arvioida kykyjen laajuutta.

> **Pysähdy hetkeksi:** Jos järjestelmä käyttää hakua ja laskinta vastatessaan, mikä osa tuloksesta on kielimallin tuottamaa ja mikä työkalun palauttamaa?

## Yhteenveto

Tekoälyjärjestelmä ei sijoitu yhdelle viiden tason portaikolle. Kuvaa sitä kahdella akselilla: kykyjen laajuudella sekä toteutuksella ja toiminnallisuudella. Näin erotat rajatun mutta tehokkaan järjestelmän, generatiivisen toiminnon, työkaluja käyttävän agentin ja spekulatiivisen AGI-väitteen ilman, että sekoitat ne kehitysvaiheiksi.

## Lähteet ja tarkistuspäivä

- [OECD: Explanatory memorandum on the updated definition of an AI system](https://oecd.ai/en/ai-publications/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system)
- [OECD: Framework for the Classification of AI Systems](https://oecd.ai/en/ai-publications/framework-classification)
- [International AI Safety Report 2025](https://www.gov.uk/government/publications/international-ai-safety-report-2025/international-ai-safety-report-2025)

Tarkistettu 15.7.2026.
