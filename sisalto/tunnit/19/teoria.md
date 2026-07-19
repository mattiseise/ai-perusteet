# Boteista agentteihin — mikä muuttuu, kun tekoäly toimii itsenäisesti?

## Johdanto

Kun puhutaan tekoälystä ja automatisoinnista, sanaa **agentti** käytetään nykyään hyvin usein. Sitä esiintyy teknologiauutisissa, yritysviestinnässä ja opetuksessa, mutta käsitteen merkitys jää usein epäselväksi. Agentti ei kuitenkaan ole sama asia kuin chatbot. Se ei myöskään tarkoita mitä tahansa automaattista lajittelijaa tai yksinkertaista ohjelmaa.

Tämä oppitunti on ensimmäinen askel kohti omaa agenttiasi, jonka rakennat n8n:llä tämän osion lopussa. Oppitunneilla 26–27 toteutat tässä oppimaasi käytännössä. Kun ymmärrät nyt agentin toimintalogiikan, myöhempi rakentaminen on paljon helpompaa.

Tarkastellaan esimerkkiä. Tehtävänä on avata sähköpostisovellus, etsiä kaikki viestit, joissa esiintyy sana ”lasku”, siirtää ne kansioon ”Laskut” ja lähettää lähettäjälle automaattinen vastaus, jossa ilmoitetaan laskun vastaanottamisesta. Yksittäisenä suorituksena tehtävä on melko yksinkertainen. Jos sama toiminto täytyy kuitenkin tehdä toistuvasti, esimerkiksi joka päivä tai jatkuvasti pitkän ajan kuluessa, siitä tulee työläs ja aikaa vievä.

Tällaisessa tilanteessa agentti voisi hoitaa tehtävän itsenäisesti käyttäjän puolesta. Tämä herättää kuitenkin tärkeän kysymyksen: miten agentti eroaa tavallisesta automaatiosta, ja mikä tekee järjestelmästä juuri agentin?

Ennen kuin tarkastelemme asiaa tarkemmin, on hyödyllistä pohtia omaa arkea.

> **Pysähdy hetkeksi:** Millaisia toistuvia tehtäviä teet säännöllisesti? Mitkä niistä ovat yksinkertaisia, mutta vievät silti aikaa ja kuormittavat turhaan?

## Agentti on järjestelmä, joka tekee päätöksiä

Ensimmäinen ja keskeisin asia on tämä: **agentti** on automatisoitu järjestelmä, joka **suorittaa useita vaiheita itsenäisesti** jonkin tavoitteen saavuttamiseksi. Se ei siis vain toteuta yhtä yksittäistä käskyä. Se ei myöskään seuraa ohjeita täysin mekaanisesti tilanteesta riippumatta, vaan tekee päätelmiä tilanteen perusteella.

Jos sähköpostisovellus käy joka aamu läpi uudet viestit ja siirtää laskut automaattisesti tiettyyn kansioon, kyse ei vielä välttämättä ole agentista. Usein kyse on **skriptistä** eli yksinkertaisesta ohjelmasta, joka tekee aina saman toiminnon samalla tavalla. Tällainen ratkaisu toimii hyvin niin kauan kuin tilanne vastaa ennalta määriteltyä mallia. Jos viestin muoto poikkeaa odotetusta, skripti voi epäonnistua.

Agentti toimii toisin. Se voi vastaanottaa uuden sähköpostin, analysoida sen sisältöä ja arvioida, onko kyseessä lasku. Sen jälkeen se voi päätellä, mihin kansioon viesti kannattaa siirtää. Se voi myös tarkistaa lähettäjään liittyviä tietoja muista järjestelmistä, hyödyntää aiempia havaintoja ja päättää, voidaanko lähettäjälle lähettää automaattinen vastaus. Lopuksi se voi kirjata tekemänsä toimenpiteet. Jos jokin vaihe epäonnistuu, esimerkiksi vastaanottajan osoite on virheellinen, agentti voi tunnistaa ongelman, ilmoittaa siitä ja pyytää jatko-ohjeita.

> **Pysähdy hetkeksi:** Mitä eroa on siinä, että ohjelma tekee aina samaa, ja siinä, että se arvioi tilannetta ja muuttaa toimintaansa sen perusteella?

<figure style="margin:26px 0;text-align:center">
<svg viewBox="0 0 960 786" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:820px;height:auto" font-family="system-ui, -apple-system, 'Segoe UI', sans-serif" role="img">
  <title>Tekoälyagentti n8n-järjestelmässä – korkean tason näkymä</title>
  <desc>Kolme vaihetta selityksineen: käynnistys, agentti (kielimalli ja työkalut) ja lopputulos; alhaalla viisivaiheinen toimintaketju selityksineen ja agentin vahvuus.</desc>
  <defs>
    <g id="ovw-bolt" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M13 2 L5 13.5 H11 L10.5 22 L19 9.5 H12.5 Z" fill="currentColor" stroke="none"/></g>
    <g id="ovw-robot" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="8" width="15" height="11.5" rx="3"/><path d="M12 8 V4.5"/><circle cx="12" cy="3.4" r="1.4" fill="currentColor" stroke="none"/><circle cx="9.3" cy="13.5" r="1.3" fill="currentColor" stroke="none"/><circle cx="14.7" cy="13.5" r="1.3" fill="currentColor" stroke="none"/><path d="M9.5 16.6 H14.5"/></g>
    <g id="ovw-check" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M7.8 12.2 l2.8 2.8 l5.6-6.2"/></g>
    <g id="ovw-ai" fill="none" stroke="currentColor"><path d="M12 3 L13.8 9.6 L20.5 11.4 L13.8 13.2 L12 20 L10.2 13.2 L3.5 11.4 L10.2 9.6 Z" fill="currentColor"/></g>
    <g id="ovw-wrench" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M20 5.5 a4.2 4.2 0 0 1 -5.4 5.4 L6.5 19 a2 2 0 0 1 -2.8 -2.8 L11.8 8.2 A4.2 4.2 0 0 1 17.2 2.8 L14.4 5.6 l1.5 2.5 l2.5 1.5 Z"/></g>
    <g id="ovw-mail" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="12" rx="2.2"/><path d="M3.5 7.5 L12 13 L20.5 7.5"/></g>
    <g id="ovw-clock" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7 V12 L15.5 14"/></g>
    <g id="ovw-link" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 12 H14.5"/><path d="M10 8 H8 a4 4 0 0 0 0 8 H10"/><path d="M14 8 H16 a4 4 0 0 1 0 8 H14"/></g>
    <g id="ovw-chat" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6.5 a2 2 0 0 1 2-2 H18 a2 2 0 0 1 2 2 V14 a2 2 0 0 1 -2 2 H9.5 L5.5 19.5 V16 H6 a2 2 0 0 1 -2-2 Z"/></g>
    <g id="ovw-doc" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3.5 H14 L18.5 8 V20 a1 1 0 0 1 -1 1 H6 a1 1 0 0 1 -1 -1 V4.5 a1 1 0 0 1 1 -1 Z"/><path d="M13.5 3.5 V8 H18.5"/><path d="M8 12 H15 M8 15.5 H15"/></g>
    <g id="ovw-chart" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20 H20"/><rect x="6" y="12" width="3" height="6"/><rect x="11" y="8.5" width="3" height="9.5"/><rect x="16" y="5" width="3" height="13"/></g>
    <g id="ovw-gear" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3.3"/><path d="M12 3.5 V6 M12 18 V20.5 M3.5 12 H6 M18 12 H20.5 M5.9 5.9 L7.7 7.7 M16.3 16.3 L18.1 18.1 M18.1 5.9 L16.3 7.7 M7.7 16.3 L5.9 18.1"/></g>
    <g id="ovw-inbox" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 13 V18 a1 1 0 0 0 1 1 H19 a1 1 0 0 0 1 -1 V13 H15.5 a3.5 3.5 0 0 1 -7 0 Z"/><path d="M12 3.5 V10 M9 7.5 L12 10.5 L15 7.5"/></g>
    <g id="ovw-target" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.6"/><circle cx="12" cy="12" r="1.4" fill="currentColor"/></g>
    <g id="ovw-loop" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5.5 10 a7 7 0 0 1 11.5 -3.3 L19 8.5"/><path d="M19 4.5 V9 H14.5"/><path d="M18.5 14 a7 7 0 0 1 -11.5 3.3 L5 15.5"/><path d="M5 19.5 V15 H9.5"/></g>
    <g id="ovw-bulb" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 18 H14.5 M10.5 21 H13.5"/><path d="M12 3 a6 6 0 0 1 4 10.3 c-0.8 0.8 -1 1.7 -1 2.7 H9 c0 -1 -0.2 -1.9 -1 -2.7 A6 6 0 0 1 12 3 Z"/></g>
  </defs>
  <rect x="0" y="0" width="960" height="786" rx="18" fill="#FAFBFE"/>
  <text x="480" y="42" text-anchor="middle" font-size="24" font-weight="700" fill="#1B2336">Tekoälyagentti n8n-järjestelmässä</text>
  <text x="480" y="70" text-anchor="middle" font-size="14" fill="#5A6478">Agentti vastaanottaa tehtävän, ymmärtää sen, käyttää työkaluja ja tuottaa lopputuloksen.</text>
  <rect x="28" y="96" width="280" height="402" rx="14" fill="#F0F9F4" stroke="#CDE9D9" stroke-width="1.5"/>
  <use href="#ovw-bolt" x="46" y="114" width="22" height="22" style="color:#2F9E69"/>
  <text x="76" y="124" font-size="14.5" font-weight="700" fill="#247A52">1. KÄYNNISTYS</text>
  <text x="76" y="140" font-size="10.5" font-weight="600" fill="#3DA876">(TRIGGER)</text>
  <line x1="46" y1="152" x2="290" y2="152" stroke="#CDE9D9" stroke-width="1.3"/>
  <text x="46" y="176" font-size="12.5" fill="#3A4253">Tapahtuma, joka käynnistää</text>
  <text x="46" y="193" font-size="12.5" fill="#3A4253">agentin toiminnan.</text>
  <text x="46" y="226" font-size="12" font-weight="700" fill="#1B2336">Esimerkkejä:</text>
  <use href="#ovw-mail" x="46" y="246" width="17" height="17" style="color:#2F9E69"/><text x="72" y="259" font-size="12.5" fill="#3A4253">Sähköposti saapuu</text>
  <use href="#ovw-clock" x="46" y="284" width="17" height="17" style="color:#2F9E69"/><text x="72" y="297" font-size="12.5" fill="#3A4253">Ajastettu tehtävä</text>
  <use href="#ovw-link" x="46" y="322" width="17" height="17" style="color:#2F9E69"/><text x="72" y="335" font-size="12.5" fill="#3A4253">Webhook tai API-kutsu</text>
  <use href="#ovw-chat" x="46" y="360" width="17" height="17" style="color:#2F9E69"/><text x="72" y="373" font-size="12.5" fill="#3A4253">Viesti chatissa</text>
  <line x1="312" y1="297" x2="336" y2="297" stroke="#9AA6BD" stroke-width="2.4"/><path d="M340 297 L330 291.5 L330 302.5 Z" fill="#9AA6BD"/>
  <rect x="340" y="96" width="280" height="402" rx="14" fill="#EEF1FE" stroke="#C9D2F7" stroke-width="1.8"/>
  <use href="#ovw-robot" x="358" y="112" width="24" height="24" style="color:#3B5BDB"/>
  <text x="390" y="129" font-size="16" font-weight="700" fill="#2F46B0">2. AGENTTI</text>
  <line x1="358" y1="146" x2="602" y2="146" stroke="#C9D2F7" stroke-width="1.3"/>
  <text x="358" y="166" font-size="11.5" fill="#3A4253">Ymmärtää tehtävän, suunnittelee</text>
  <text x="358" y="182" font-size="11.5" fill="#3A4253">vaiheet ja käyttää työkaluja</text>
  <text x="358" y="198" font-size="11.5" fill="#3A4253">tavoitteen saavuttamiseksi.</text>
  <rect x="356" y="210" width="248" height="104" rx="10" fill="#FFFFFF" stroke="#C9D2F7" stroke-width="1.3"/>
  <use href="#ovw-ai" x="368" y="221" width="18" height="18" style="color:#3B5BDB"/>
  <text x="392" y="235" font-size="12.5" font-weight="700" fill="#2F46B0">KIELIMALLI (LLM)</text>
  <text x="370" y="258" font-size="11.5" fill="#3A4253">• Ymmärtää tehtävän</text>
  <text x="370" y="278" font-size="11.5" fill="#3A4253">• Tekee päätökset</text>
  <text x="370" y="298" font-size="11.5" fill="#3A4253">• Muodostaa vastaukset</text>
  <rect x="356" y="322" width="248" height="104" rx="10" fill="#FFFFFF" stroke="#C9D2F7" stroke-width="1.3"/>
  <use href="#ovw-wrench" x="368" y="333" width="18" height="18" style="color:#3B5BDB"/>
  <text x="392" y="347" font-size="12.5" font-weight="700" fill="#2F46B0">TYÖKALUT</text>
  <text x="370" y="370" font-size="11.5" fill="#3A4253">• Lukee ja kirjoittaa dataa</text>
  <text x="370" y="390" font-size="11.5" fill="#3A4253">• Suorittaa toimintoja</text>
  <text x="370" y="410" font-size="11.5" fill="#3A4253">• Integroi ulkoisiin (API:t)</text>
  <text x="358" y="452" font-size="11.5" font-style="italic" fill="#5A6478">Agentti voi suorittaa useita</text>
  <text x="358" y="468" font-size="11.5" font-style="italic" fill="#5A6478">vaiheita, kunnes tavoite täyttyy.</text>
  <line x1="624" y1="297" x2="648" y2="297" stroke="#9AA6BD" stroke-width="2.4"/><path d="M652 297 L642 291.5 L642 302.5 Z" fill="#9AA6BD"/>
  <rect x="652" y="96" width="280" height="402" rx="14" fill="#E9F6F7" stroke="#BFE6E9" stroke-width="1.5"/>
  <use href="#ovw-check" x="670" y="114" width="22" height="22" style="color:#0E9AA7"/>
  <text x="700" y="124" font-size="14.5" font-weight="700" fill="#0B7E89">3. LOPPUTULOS</text>
  <text x="700" y="140" font-size="10.5" font-weight="600" fill="#1AA1AD">(OUTPUT)</text>
  <line x1="670" y1="152" x2="914" y2="152" stroke="#BFE6E9" stroke-width="1.3"/>
  <text x="670" y="176" font-size="12.5" fill="#3A4253">Agentti tuottaa valmiin ja</text>
  <text x="670" y="193" font-size="12.5" fill="#3A4253">tarkistetun tuloksen.</text>
  <text x="670" y="226" font-size="12" font-weight="700" fill="#1B2336">Esimerkkejä:</text>
  <use href="#ovw-doc" x="670" y="246" width="17" height="17" style="color:#0E9AA7"/><text x="696" y="259" font-size="12.5" fill="#3A4253">Vastaus raporttina</text>
  <use href="#ovw-chart" x="670" y="284" width="17" height="17" style="color:#0E9AA7"/><text x="696" y="297" font-size="12.5" fill="#3A4253">Tallennus taulukkoon</text>
  <use href="#ovw-mail" x="670" y="322" width="17" height="17" style="color:#0E9AA7"/><text x="696" y="335" font-size="12.5" fill="#3A4253">Vastaus sähköpostina</text>
  <use href="#ovw-gear" x="670" y="360" width="17" height="17" style="color:#0E9AA7"/><text x="696" y="373" font-size="12.5" fill="#3A4253">Toimenpide järjestelmässä</text>
  <line x1="28" y1="524" x2="932" y2="524" stroke="#E3E7F0" stroke-width="1.3"/>
  <text x="28" y="550" font-size="13.5" font-weight="700" fill="#1B2336">Näin agentti toimii vaihe vaiheelta:</text>
  <use href="#ovw-inbox" x="28" y="566" width="19" height="19" style="color:#3B5BDB"/>
  <text x="54" y="580" font-size="12" font-weight="700" fill="#2F46B0">1. Vastaanottaa</text>
  <text x="28" y="602" font-size="10.8" fill="#5A6478">Trigger käynnistää ja</text>
  <text x="28" y="617" font-size="10.8" fill="#5A6478">välittää tehtävän tiedot.</text>
  <use href="#ovw-target" x="210" y="566" width="19" height="19" style="color:#3B5BDB"/>
  <text x="236" y="580" font-size="12" font-weight="700" fill="#2F46B0">2. Ymmärtää</text>
  <text x="210" y="602" font-size="10.8" fill="#5A6478">Kielimalli ymmärtää</text>
  <text x="210" y="617" font-size="10.8" fill="#5A6478">tehtävän ja päättää</text>
  <text x="210" y="632" font-size="10.8" fill="#5A6478">tarvittavat vaiheet.</text>
  <use href="#ovw-wrench" x="392" y="566" width="19" height="19" style="color:#3B5BDB"/>
  <text x="418" y="580" font-size="12" font-weight="700" fill="#2F46B0">3. Käyttää</text>
  <text x="392" y="602" font-size="10.8" fill="#5A6478">Hyödyntää sopivia</text>
  <text x="392" y="617" font-size="10.8" fill="#5A6478">työkaluja tiedon hakuun</text>
  <text x="392" y="632" font-size="10.8" fill="#5A6478">ja toimintoihin.</text>
  <use href="#ovw-loop" x="574" y="566" width="19" height="19" style="color:#3B5BDB"/>
  <text x="600" y="580" font-size="12" font-weight="700" fill="#2F46B0">4. Toistaa</text>
  <text x="574" y="602" font-size="10.8" fill="#5A6478">Arvioi tulokset ja palaa</text>
  <text x="574" y="617" font-size="10.8" fill="#5A6478">tarvittaessa, kunnes</text>
  <text x="574" y="632" font-size="10.8" fill="#5A6478">tavoite täyttyy.</text>
  <use href="#ovw-check" x="756" y="566" width="19" height="19" style="color:#3B5BDB"/>
  <text x="782" y="580" font-size="12" font-weight="700" fill="#2F46B0">5. Tuottaa</text>
  <text x="756" y="602" font-size="10.8" fill="#5A6478">Palauttaa vastauksen</text>
  <text x="756" y="617" font-size="10.8" fill="#5A6478">tai suorittaa</text>
  <text x="756" y="632" font-size="10.8" fill="#5A6478">toiminnon.</text>
  <g stroke="#C2CAD9" stroke-width="2" fill="#C2CAD9">
    <line x1="170" y1="575" x2="196" y2="575"/><path d="M200 575 L191 570.5 L191 579.5 Z"/>
    <line x1="352" y1="575" x2="378" y2="575"/><path d="M382 575 L373 570.5 L373 579.5 Z"/>
    <line x1="534" y1="575" x2="560" y2="575"/><path d="M564 575 L555 570.5 L555 579.5 Z"/>
    <line x1="716" y1="575" x2="742" y2="575"/><path d="M746 575 L737 570.5 L737 579.5 Z"/>
  </g>
  <rect x="28" y="676" width="904" height="86" rx="12" fill="#FFFBEC" stroke="#F2D98E" stroke-width="1.5"/>
  <use href="#ovw-bulb" x="50" y="702" width="26" height="26" style="color:#C79100"/>
  <text x="92" y="710" font-size="13.5" font-weight="700" fill="#8A6A00">Agentin vahvuus</text>
  <text x="92" y="731" font-size="12.5" fill="#5A4A1E">Agentti yhdistää kielimallin älykkyyden ja työkalujen voiman. Näin se pystyy</text>
  <text x="92" y="749" font-size="12.5" fill="#5A4A1E">hoitamaan monivaiheisia tehtäviä itsenäisesti ja joustavasti.</text>
  <use href="#ovw-ai" x="712" y="706" width="26" height="26" style="color:#3B5BDB"/>
  <text x="748" y="728" font-size="18" font-weight="700" fill="#8A6A00">+</text>
  <use href="#ovw-wrench" x="772" y="706" width="26" height="26" style="color:#3B5BDB"/>
  <text x="808" y="728" font-size="18" font-weight="700" fill="#8A6A00">=</text>
  <use href="#ovw-robot" x="832" y="704" width="30" height="30" style="color:#3B5BDB"/>
</svg>
<figcaption style="font-size:13px;color:#5A6478;margin-top:10px">Agentin toiminta kokonaisuutena: käynnistys johtaa agenttiin (kielimalli + työkalut), joka toimii vaiheittain ja tuottaa lopputuloksen.</figcaption>
</figure>

## Agentti = kielimalli + harness

Tällä kurssilla **agentti = kielimalli + harness**. Harness tarkoittaa ympäröivää ohjelmistorakennetta, joka välittää syötteet, tarjoaa työkalut, ylläpitää tehtävän tilaa, rajaa oikeuksia ja tallentaa suoritusjäljen. Pelkkä kielimalli keskustelee; harness tekee hallitusta toiminnasta mahdollista.

## Kurssin kuuden kohdan suunnittelutarkistuslista

Seuraavat kuusi kohtaa ovat tämän kurssin suunnittelutarkistuslista, eivät väite siitä, että jokaisessa agentissa olisi kuusi erillistä teknistä komponenttia. Yksinkertainen agentti voi toimia ilman pitkäkestoista muistia tai automaattista palautteesta oppimista. Tarkistuslista auttaa silti huomaamaan, mitä toteutus tarvitsee ja mitä siitä voidaan tarkoituksella jättää pois.

**Ensimmäinen komponentti: syötekäsittelijä.** Syötekäsittelijä toimii agentin aisteina. Se havaitsee, kun uusi sähköposti saapuu, palvelin lähettää hälytyksen tai käyttäjä painaa painiketta. Sen tehtävänä on vastaanottaa nämä herätteet ja käyttäjän syötteet sekä muuntaa ne muotoon, jota agentti pystyy käsittelemään.

Ilman syötekäsittelijää agentti ei tietäisi, että jotain on tapahtunut. Se ei voisi reagoida ympäristöönsä eikä käynnistää toimintaansa oikealla hetkellä.

Voit ajatella asiaa myös näin: vaikka neuvoja olisi kuinka taitava, hän ei voi ratkaista ongelmia, jos hän ei saa niistä mitään tietoa. Jos hän ei kuule puheluita eikä lue sähköposteja, hän ei edes tiedä, että apua tarvitaan.

**Toinen komponentti: päättelijä ja suunnittelija.** Päättelijä on agentin aivot. Kun tietoa on vastaanotettu, päättelijän tehtävänä on analysoida tilanne ja arvioida, mikä toimenpide on tarkoituksenmukaisin. Tässä se voi hyödyntää esimerkiksi kielimallia, joka auttaa tulkitsemaan tekstiä ja valitsemaan seuraavan vaiheen. Se voi esimerkiksi päätellä, onko viesti kiireellinen, löytyykö vastaus tietokannasta vai pitääkö asia ohjata ihmiselle.

Ilman päättelijää agentti ei tekisi päätöksiä tilanteen perusteella, vaan toimisi aina samalla tavalla. Tällöin se olisi enemmän skripti kuin varsinainen agentti.

**Kolmas komponentti: työkalujen suorittaja.** Kun päättelijä on arvioinut tilanteen ja valinnut toimintatavan, työkalujen suorittaja toteuttaa päätöksen käytännössä. Se voi kutsua rajapintoja, tehdä tietokantahakuja, lähettää sähköposteja tai muokata tiedostoja. Työkalujen suorittaja on siis se osa agenttia, joka muuttaa päätökset toiminnaksi.

Ilman tätä osaa agentti ei pystyisi vaikuttamaan ympäristöönsä. Päättelijä voisi kyllä muodostaa tarkoituksenmukaisen ratkaisun, mutta mitään ei tapahtuisi käytännössä. Tällöin agentti olisi kuin johtaja, jolla ei ole mahdollisuutta toteuttaa tekemiään päätöksiä.

**Neljäs kohta: muisti ja konteksti.** Agentti tarvitsee tehtävän nykyisen tilan, mutta ei aina pitkäkestoista muistia. **Lyhytkestoinen muisti** tarkoittaa tietoa, jota agentti pitää mukana yhden suorituksen aikana. **Pitkäkestoinen muisti** tarkoittaa pysyvämmin tallennettua tietoa, jota tarvitaan vain, jos myöhemmän suorituksen pitää hyödyntää aiempaa tietoa.

Jos tehtävä sitä vaatii, pitkäkestoinen muisti voi tuoda myöhempään suoritukseen aiempia tapauksia tai käyttäjäkohtaisia tietoja. Ilman pitkäkestoista muistia agentti voi silti hoitaa itsenäisen tehtävän nykyisen suorituksen tilan avulla. Toteutusta kehitetään testien ja seurannan perusteella riippumatta siitä, tallentaako agentti aiempia tapauksia.

**Viides komponentti: turvakerros.** Ennen kuin agentti suorittaa mitään toimintoa, sen on tarkistettava, onko toiminta sallittua. Tästä vastaa turvakerros. Sen tehtävänä on estää agenttia tekemästä vaarallisia, virheellisiä tai luvattomia toimenpiteitä. Turvakerros tarkistaa esimerkiksi, saako agentti poistaa tietokannan rivejä, siirtää rahaa tietylle tilille tai käsitellä tietyn käyttäjän tietoja.

Turvakerros toimii yleensä kolmella tasolla. Se voi tarkistaa toiminnan etukäteen ennen sen suorittamista, valvoa toimintaa sen aikana ja arvioida jälkikäteen, tapahtuiko kaikki sääntöjen mukaisesti. Näin se vähentää riskiä, että agentti toimisi tavalla, joka aiheuttaisi vahinkoa tai rikkoisi annettuja rajoja.

Ilman turvakerrosta agentti voisi tehdä vakavia virheitä tai aiheuttaa vahinkoa ympäristölleen. Turvakerros on siis se osa järjestelmää, joka pysäyttää toiminnan silloin, kun sitä ei pitäisi sallia.

**Kuudes komponentti: seuranta ja palautesilmukka.** Kun agentti suorittaa toiminnon, on tärkeää pystyä seuraamaan, mitä tapahtui. Onko tehtävä onnistunut? Vastasiko tulos odotuksia? Kuinka kauan suoritus kesti? Tästä vastaa seurantakomponentti, joka kirjaa agentin toiminnan ja sen tulokset.

Kerättyä tietoa hyödynnetään **palautesilmukassa**. Sen avulla agentin toimintaa voidaan arvioida ja kehittää. Jos jokin toimintatapa on aiemmin johtanut epäonnistumiseen, järjestelmä voi käyttää tätä tietoa myöhemmissä tilanteissa ja ohjata toimintaa toiseen suuntaan.

Palautesilmukka ei tarkoita, että malli oppisi automaattisesti jokaisesta suorituksesta. Se voi olla ihmisen tekemä katselmointi, mittari tai testitulokseen perustuva korjausprosessi. Kaikki agentit eivät tarvitse automaattista oppimista, mutta jokainen tuotantototeutus hyötyy seurattavasta suoritusjäljestä.

> **Pysähdy hetkeksi:** Mitkä kuudesta suunnittelukohdasta olisivat valitsemassasi tehtävässä tarpeellisia? Minkä voisit jättää pois ja millä perusteella?

Seuraavilla oppitunneilla avaamme jokaisen näistä komponenteista tarkemmin. Kun kohtaat uuden aiheen, mieti aina: mihin agentin osaan tämä liittyy?

## Chatbot ei ole agentti

**Chatbot** on ohjelma, joka vastaa käyttäjän kirjoittamiin viesteihin. Se voi vaikuttaa hyvinkin älykkäältä, ja erityisesti nykyaikaiset chatbotit, kuten ChatGPT, osaavat käydä sujuvaa keskustelua. Chatbotin toiminta on kuitenkin pääosin reaktiivista: se odottaa käyttäjän viestiä, vastaa siihen ja jää sitten odottamaan seuraavaa viestiä.

Agentti toimii eri tavalla. Se ei ainoastaan reagoi käyttäjän pyyntöihin, vaan voi myös tarkkailla tilannetta taustalla ja käynnistää toimintoja itsenäisesti ilman erillistä käskyä.

Ero näkyy hyvin esimerkin avulla. Jos kirjoitat ChatGPT:lle: ”Anna minulle ohje pizzan tekemiseen”, saat vastauksen. Tällöin kyse on chatbotista. Jos taas järjestelmä huomaa, että tietyt jääkaapissa olevat ruoka-aineet ovat vanhenemassa, ja lähettää sinulle oma-aloitteisesti reseptejä niiden hyödyntämiseksi, kyse on agentista.

<figure class="ai-demo"><span class="ai-demo__tag">// sama tehtävä — botti kertoo ohjeet, agentti tekee työn</span>
<div class="ai-demo__stage" style="display:flex;align-items:center;justify-content:center;height:330px">
  <div class="l19-wrap">
    <div class="l19-task">Tehtävä: ”Siirrä laskut Laskut-kansioon ja kuittaa lähettäjille.”</div>
    <div class="l19-pane l19-bot"><span class="l19-ph">CHATBOT</span>
      <span class="l19-reply">”Näin teet sen itse: 1) avaa sähköposti, 2) etsi laskut, 3) siirrä ne kansioon, 4) vastaa lähettäjille.”</span>
      <span class="l19-tag l19-tw">kertoo ohjeet — työ jää sinulle</span>
    </div>
    <div class="l19-pane l19-ag"><span class="l19-ph">AGENTTI</span>
      <span class="l19-step s1">lukee saapuneet — 24 viestiä<i>✓</i></span>
      <span class="l19-step s2">tunnistaa 3 laskua<i>✓</i></span>
      <span class="l19-step s3">siirtää kansioon Laskut<i>✓</i></span>
      <span class="l19-step s4">lähettää 3 kuittausta<i>✓</i></span>
      <span class="l19-rep">raportti: ”3 laskua käsitelty” ✓</span>
      <span class="l19-tag l19-tg">tekee vaiheet itse — ja raportoi</span>
    </div>
  </div>
</div>
<figcaption class="ai-demo__cap">Ratkaiseva ero: chatbot vastaa tekstillä ja työ jää sinulle — agentti suorittaa vaiheet itse työkaluillaan ja raportoi tuloksen. Juuri siksi agentti tarvitsee oikeudet, turvarajat ja valvonnan, joita pelkkä chatbot ei tarvitse.</figcaption></figure>
<style>
.l19-wrap{position:relative;width:560px;height:292px;font-family:var(--font-mono)}
.l19-task{position:absolute;left:50%;transform:translateX(-50%);top:0;white-space:nowrap;font-size:11.5px;font-weight:500;color:#06212A;background:#46c7cf;border-radius:10px;padding:7px 12px}
.l19-pane{position:absolute;top:48px;width:268px;min-height:240px;background:#11182A;border:2px solid #2B3552;border-radius:13px;padding:11px 13px 36px}
.l19-bot{left:0}
.l19-ag{right:0;border-color:oklch(0.66 0.13 208)}
.l19-ph{display:block;font-size:10.5px;letter-spacing:.13em;color:#B9C2DA;margin-bottom:9px}
.l19-reply{display:block;font-size:11.5px;line-height:1.55;color:#FFFFFF;background:#1E2740;border:1.5px solid #44517A;border-radius:10px;padding:9px 11px;opacity:0;animation:l19reply 19s infinite}
@keyframes l19reply{0%,4%{opacity:0}9%,96%{opacity:1}100%{opacity:0}}
.l19-step{display:flex;align-items:center;gap:8px;font-size:11px;line-height:1.35;color:#5D6880;background:#0E1422;border:1px solid #232C44;border-radius:8px;padding:6px 9px;margin-bottom:7px}
.l19-step i{margin-left:auto;font-style:normal;color:#7FD0A8;opacity:0}
.l19-step.s1{animation:l19s1 19s infinite}.l19-step.s1 i{animation:l19i1 19s infinite}
.l19-step.s2{animation:l19s2 19s infinite}.l19-step.s2 i{animation:l19i2 19s infinite}
.l19-step.s3{animation:l19s3 19s infinite}.l19-step.s3 i{animation:l19i3 19s infinite}
.l19-step.s4{animation:l19s4 19s infinite}.l19-step.s4 i{animation:l19i4 19s infinite}
@keyframes l19s1{0%,8%{color:#5D6880;border-color:#232C44}12%,22%{color:#FFFFFF;border-color:oklch(0.72 0.13 208)}26%,96%{color:#B9C2DA;border-color:#232C44}100%{color:#5D6880}}
@keyframes l19s2{0%,24%{color:#5D6880;border-color:#232C44}28%,38%{color:#FFFFFF;border-color:oklch(0.72 0.13 208)}42%,96%{color:#B9C2DA;border-color:#232C44}100%{color:#5D6880}}
@keyframes l19s3{0%,40%{color:#5D6880;border-color:#232C44}44%,54%{color:#FFFFFF;border-color:oklch(0.72 0.13 208)}58%,96%{color:#B9C2DA;border-color:#232C44}100%{color:#5D6880}}
@keyframes l19s4{0%,56%{color:#5D6880;border-color:#232C44}60%,70%{color:#FFFFFF;border-color:oklch(0.72 0.13 208)}74%,96%{color:#B9C2DA;border-color:#232C44}100%{color:#5D6880}}
@keyframes l19i1{0%,18%{opacity:0}22%,96%{opacity:1}100%{opacity:0}}
@keyframes l19i2{0%,34%{opacity:0}38%,96%{opacity:1}100%{opacity:0}}
@keyframes l19i3{0%,50%{opacity:0}54%,96%{opacity:1}100%{opacity:0}}
@keyframes l19i4{0%,66%{opacity:0}70%,96%{opacity:1}100%{opacity:0}}
.l19-rep{display:block;font-size:11px;font-weight:600;color:#06241f;background:#7FD0A8;border-radius:8px;padding:6px 9px;opacity:0;animation:l19rep 19s infinite}
@keyframes l19rep{0%,74%{opacity:0;transform:scale(1.12)}80%,96%{opacity:1;transform:scale(1)}100%{opacity:0}}
.l19-tag{position:absolute;left:13px;right:13px;bottom:10px;font-size:10.5px;letter-spacing:.04em;line-height:1.4}
.l19-tw{color:#F0A38C}
.l19-tg{color:#7FD0A8;opacity:0;animation:l19tg 19s infinite}
@keyframes l19tg{0%,80%{opacity:0}86%,96%{opacity:1}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){
.l19-reply,.l19-step,.l19-step i,.l19-rep,.l19-tg{animation:none}
.l19-reply,.l19-step i,.l19-rep,.l19-tg{opacity:1}
.l19-step{color:#B9C2DA}}
</style>


## Skripti, työnkulku ja agentti — kolme eri tasoa

Yritysmaailmassa käytettävät järjestelmät voidaan jakaa kolmeen pääkategoriaan. Näiden erojen ymmärtäminen on tärkeää, koska **skripti**, **työnkulku** ja **agentti** eivät tarkoita samaa asiaa.

**Skripti** on yksinkertainen ohjelma, joka suorittaa täsmälleen ennalta määritellyt komennot. Se ei arvioi tilannetta eikä huomioi seurauksia, vaan tekee sen, mitä sille on määrätty. Esimerkiksi komento ”poista kaikki tiedostot, joiden nimi alkaa sanalla temp\_” on skriptille tyypillinen tehtävä. Skripti ei tee päätelmiä, vaan toteuttaa ohjeen sellaisenaan.

**Työnkulku** on useasta vaiheesta koostuva prosessi, jossa toiminta etenee ennalta kirjoitettujen sääntöjen mukaan. Esimerkiksi sähköpostien käsittelyssä työnkulku voi toimia näin: jos viesti sisältää sanan ”lasku”, se siirretään kansioon A, jos se sisältää sanan ”raportti”, se siirretään kansioon B, ja muissa tapauksissa se jätetään saapuneisiin. Työnkulku on skriptiä joustavampi, koska siihen sisältyy päätöslogiikkaa. Se perustuu kuitenkin edelleen valmiiksi määriteltyihin sääntöihin, eikä se muuta toimintaansa itsenäisesti.

**Agentissa** kielimalli tulkitsee tilannetta ja valitsee toimintaa, ja harness antaa sille tehtävän tilan, työkalut, oikeudet ja rajat. Tulos voidaan tarkistaa saman suorituksen aikana tai ihmisen tekemässä jälkikatselmoinnissa. Pitkäkestoinen muisti ja automaattinen palautteesta oppiminen ovat mahdollisia lisäosia, eivät agentin tunnusmerkkejä.

Ero näkyy hyvin käytännön esimerkissä. Skripti voi lajitella tiedostot pelkän koon perusteella. Työnkulku voi lajitella ne koon ja tiedostotyypin mukaan ennalta määriteltyjen sääntöjen perusteella. Agentti taas voi tehdä lajittelua sen mukaan, mitä tiedostoja käyttäjä todennäköisesti tarvitsee myöhemmin ja miten ne olisi järkevintä järjestää tulevaa käyttöä varten.

## Miten yksi esimerkkitoteutus toimii

Nyt tiedät, että agentti muodostuu kielimallista ja harnessista. Kurssin kuutta suunnittelukohtaa voi soveltaa eri tavoin. Seuraava **suoritusputki** kuvaa yhtä neuvonta-agentin toteutusta, jossa kaikki kuusi kohtaa ovat tarpeellisia. Se ei ole kaikkien agenttien pakollinen vaiheistus.

Seuraavaksi tarkastellaan, mitä agentin sisällä tapahtuu silloin, kun se saa tehtävän. Esimerkkinä käytetään neuvonta-agenttia, joka auttaa käyttäjiä ratkaisemaan ongelmia.

**Käynnistyminen** eli **initialization**: Prosessi alkaa aina siitä, että jokin tapahtuma käynnistää agentin toiminnan. Käyttäjä voi esimerkiksi lähettää tukipyynnön viestillä: ”Tulostimeni ei toimi.” Syötekäsittelijä vastaanottaa viestin ja muuntaa sen sellaiseen muotoon, jota agentti pystyy käsittelemään. Käytännössä tämä voi tarkoittaa esimerkiksi jäsenneltyä tietuetta, johon tallennetaan viestin sisältö, lähettäjän tiedot ja aikaleima.

**Päättelijä arvioi tilanteen.** Tässä vaiheessa agentti ei vielä suorita varsinaisia toimenpiteitä, vaan arvioi tilannetta. Päättelijä lukee syötteen ja tekee kaksi keskeistä asiaa. Ensin se arvioi, mitä tehtävä edellyttää. Sen jälkeen se suunnittelee, mitä vaiheita tehtävän ratkaiseminen vaatii. Tätä vaihetta kutsutaan **reititykseksi**: agentti valitsee, mitä toimintapolkua tilanteessa kannattaa seurata. Tulostinongelman kohdalla agentti voi esimerkiksi päätyä siihen, että se hakee ensin ratkaisua tietokannasta, vastaa sitten käyttäjälle ja ohjaa asian ihmiselle, jos ratkaisu ei toimi.

Reitityspäätös ei synny sattumalta. Agentti hyödyntää kielimallia, joka analysoi tilanteen ja arvioi, mikä toimintatapa on tarkoituksenmukaisin. Tässä esimerkissä myös pitkäkestoinen muisti on valittu mukaan: aiemmat ratkaisut voivat auttaa ehdotusten järjestämisessä. Toisessa agentissa tietohaku tai nykyisen tehtävän tila voi riittää ilman aiempien suoritusten muistia.

**Tehtävän tila tuo nykyisen kontekstin.** Harness ylläpitää tietoa, jota tarvitaan juuri käsillä olevan tehtävän aikana. Siihen kuuluvat esimerkiksi nykyinen keskustelu, käyttäjän viimeisimmät viestit ja agentin edelliset vaiheet. Tässä esimerkkitoteutuksessa on lisäksi pitkäkestoinen muisti, johon tallennetaan valikoituja aiempien tehtävien tuloksia.

Tehtävän tila auttaa agenttia pysymään selvillä siitä, mitä parhaillaan tapahtuu. Pitkäkestoinen muisti on perusteltu vain, jos myöhemmän suorituksen pitää käyttää aiempaa tietoa. Muistin lisääminen kasvattaa myös tietosuoja- ja ylläpitovastuuta.

Käytännössä tämä voi tarkoittaa esimerkiksi sitä, että agentti tunnistaa saman käyttäjän aiemman ongelman ja hyödyntää sitä uuden tapauksen käsittelyssä: viimeksi tulostinongelman syynä oli se, että tulostin ei ollut samassa verkossa, joten tämä tarkistetaan ensin.

**Työkalut tekevät työn.** Kun suunnitelma on valmis, agentti alkaa toimia. Se kutsuu työkaluja: hakee tietokannasta ratkaisuehdotuksen, tarkistaa tulostimen tilan verkonhallintajärjestelmästä ja kirjoittaa vastausviestin käyttäjälle. Jokainen työkalu on kuin erikoistunut käsipari: yksi osaa lukea tietokantoja, toinen lähettää sähköposteja ja kolmas muokata tiedostoja. Agentti valitsee oikean työkalun kuhunkin tilanteeseen. Tätä valintaa kutsutaan **työkalureititykseksi**, ja se on yksi tärkeimmistä päätöksistä, joita agentti tekee.

**Turvakerros valvoo jokaista vaihetta.** Turvakerros on mukana agentin toiminnassa koko ajan, ei vain prosessin lopussa. Ennen kuin agentti esimerkiksi hakee tietoa, turvakerros tarkistaa, onko sillä oikeus käyttää kyseistä tietokantaa. Ennen viestin lähettämistä se voi arvioida, sisältääkö viesti sellaista arkaluontoista tietoa, jota ei saa jakaa. Toiminnon jälkeen turvakerros voi vielä varmistaa, että kaikki tapahtui sääntöjen ja käyttöoikeuksien mukaisesti.

Turvakerros toimii siis kolmessa vaiheessa: ennen toimintoa, sen aikana ja sen jälkeen. Sen tehtävänä on valvoa agentin toimintaa jatkuvasti ja estää virheelliset, vaaralliset tai luvattomat toimenpiteet. Jos jokin näyttää poikkeavalta tai epäilyttävältä, turvakerros voi keskeyttää toiminnan missä vaiheessa tahansa.

**Tuloksen tarkistus voi sulkea tämän esimerkin kehän.** Harness tarkistaa, onnistuiko viestin lähetys ja saatiinko työkalulta odotettu vastaus. Tämän tarkistuksen perusteella agentti voi jatkaa, yrittää rajatusti uudelleen tai eskaloida ihmiselle.

Jos kaikki on sujunut odotetusti, toteutus kirjaa onnistumisen. Ratkaisu tallennetaan pitkäkestoiseen muistiin vain, jos sille on määritelty tarve, säilytysaika ja käyttöoikeudet. Jos jokin meni pieleen, harness voi sallia toisen toimintatavan, eri työkalun tai eskaloinnin ihmiselle.

Tässä toteutuksessa seurantaa käytetään myös **palautesilmukassa**, jossa ihminen tarkastelee tuloksia ja kehittää asetuksia. Tämä ei tarkoita, että kielimalli oppisi automaattisesti jokaisesta suorituksesta.

**Esimerkin kulku kokonaisuutena.** Kun käyttäjä lähettää tukipyynnön, harness välittää viestin kielimallille. Malli arvioi tilanteen ja valitsee toimintapolun. Tähän esimerkkiin valittu pitkäkestoinen muisti tuo aiempaa kontekstia. Työkalut toteuttavat rajatut toimenpiteet, turvarajat valvovat oikeuksia ja seuranta kirjaa tuloksen. Sama kuuden kohdan tarkistuslista voi tuottaa toisessa tehtävässä yksinkertaisemman toteutuksen.

Agentin erottaa tässä kurssissa muista ratkaisuista kielimallin ja harnessin yhdistelmä: kielimalli tulkitsee tilannetta, ja harness mahdollistaa rajatun työkalujen käytön. Skripti suorittaa ennalta määrätyn toiminnon, ja työnkulku etenee valmiiksi määriteltyä polkua pitkin. Agentti ei tarvitse automaattista oppimista ollakseen agentti.

> **Pysähdy hetkeksi:** Valitse arjestasi jokin toistuva tehtävä. Kuvittele, että suunnittelet agentin hoitamaan sen. Mitkä kuudesta suunnittelukohdasta tarvitset, minkä jätät pois ja missä ihmisen valvonta olisi tärkeintä?

## Valmiit agentit — jonkun muun rakentama harness

Tässä osiossa agentti on tähän asti ollut jotain, jonka rakennat itse. Arjessa ja työpaikoilla kohtaat agentin kuitenkin useimmiten **valmisagenttina**: valmiina tuotteena, joka asuu tutun tekoälysovelluksen sisällä. Sovelluksessa on silloin **agenttitila** — toimintatila, jolle annat tehtävän ja joka tekee monivaiheisen työn puolestasi: lukee tiedostoja, käyttää työkaluja ja raportoi lopuksi, mitä sai aikaan.

Valmisagenttia voi arvioida samalla kuuden kohdan tarkistuslistalla, vaikka toteutus ei jakautuisi kuuteen erilliseen osaan ja jokin kohta olisi tarkoituksella tarpeeton. Kokeile väitettä arkiesimerkillä. Annat agenttitilalle tehtävän: ”Käy läpi tämän kansion kokousmuistiot ja kokoa taulukko päätöksistä ja vastuuhenkilöistä.” Kun sovellus ottaa tehtäväsi vastaan ja tulkitsee sen, työssä on syötekäsittelijä. Kun se näyttää sinulle vaihesuunnitelman ennen aloittamista, näet päättelijän kädenjäljen. Kun se lukee muistiot ja kirjoittaa taulukon, vuorossa on työkalujen suorittaja. Kun se kysyy ”saanko muokata tätä kansiota?”, vastassa on turvakerros. Kun se jatkaa keskeytynyttä työtä siitä, mihin jäitte, käytössä on muisti ja konteksti. Ja kun se lopuksi raportoi, mitä teki, ja korjaa huomaamansa virheen, kehän sulkevat seuranta ja palautesilmukka.

Tälle kokonaisuudelle on nimi. Kaikkea, mitä kielimallin ympärille on rakennettu — esimerkiksi syötteiden välitystä, työkaluja, tehtävän tilaa, oikeuksia ja turvarajoja — kutsutaan **harnessiksi**. Siitä saadaan tämän osion tiivein kiteytys: **agentti = kielimalli + harness**. Kurssin kuusi kohtaa auttavat arvioimaan harnessia, mutta eivät määrää sen sisäistä rakennetta.

Englannin sana harness tarkoittaa valjaita, ja vertauskuva kantaa pitkälle. Kielimalli on kuin vetohevonen: voimaa riittää, mutta ilman valjaita hevonen vain juoksee. Vasta valjaat kytkevät voiman kärryyn niin, että voimasta tulee työtä. Sama pätee malliin: ilman harnessia kielimalli vain puhuu — eli on chatbot. Tästä seuraa arkinen havainto, joka selittää tunnin aiemman väitteen ”chatbot ei ole agentti” uudesta kulmasta: täsmälleen sama kielimalli voi olla sekä chatbotin että agentin sisällä. Ero ei ole mallissa vaan sen ympärille rakennetussa harnessissa.

> **Tilanne heinäkuussa 2026 — esimerkkejä valmisagenteista.**
> Claude Cowork on Anthropicin agenttitila Claude Desktopissa: se toimii käyttäjän tiedostokansioissa, ja yli 90 prosenttia sen käytöstä on muuta kuin ohjelmointia. Cowork julkaistiin kokeiluversiona tammikuussa 2026 ja varsinaisesti huhtikuussa 2026, ja heinäkuussa 2026 se laajeni myös webiin ja mobiiliin. ChatGPT Work on OpenAI:n agenttituote, joka julkaistiin 9. heinäkuuta 2026 GPT-5.6-mallien yhteydessä: se yhdistää Codexin ja ChatGPT:n ja tekee pitkäkestoisia tehtäviä sovelluksissa ja tiedostoissa.
>
> *Tuotenimet, päivämäärät ja ominaisuudet vanhenevat nopeasti — tämä laatikko päivitetään kurssin ylläpidossa erikseen. Leipätekstin käsitteet eivät vanhene.*

Miksi siis rakennat tunneilla 26–27 oman agentin, jos valmiitakin on tarjolla? Siksi, että n8n-työnkulussasi rakennat itse pienen harnessin: valitset työkalut, määrität oikeudet ja asetat turvarajat. Sen jälkeen osaat arvioida myös valmista agenttia, koska tiedät, mitä konepellin alla on ja mitä kysymyksiä siitä kannattaa esittää. Valmisagentti ei korvaa omaa rakentamista — se on saman asian toinen muoto.

> **Pysähdy hetkeksi:** Kun seuraavan kerran käytät tekoälysovellusta, mieti: juttelenko pelkän mallin kanssa vai onko mallilla harness — työkalut, oikeudet ja turvarajat? Mistä eron huomaa käyttöliittymässä?

## Kohti omaa projektia

Agentit-osion aikana rakennat oman **n8n-agenttityönkulun**. Ensimmäinen askel on valita ongelma, jonka haluat ratkaista. Kun mietit aihetta, palaa tämän oppitunnin käsitteisiin: tarvitseeko ongelmasi autonomista päätöksentekoa vai riittäisikö yksinkertaisempi ratkaisu? Mitkä kuudesta komponentista ovat ongelmassasi kriittisimpiä? Hyvä agenttiongelma on sellainen, jossa pelkkä chatbot tai skripti ei riitä, vaan tarvitaan järjestelmä, joka arvioi tilannetta, tekee päätöksiä ja käyttää työkaluja tavoitteen saavuttamiseksi.

## Yhteenveto

**Agentti** on automatisoitu järjestelmä, joka toteuttaa useita vaiheita itsenäisesti tavoitteen saavuttamiseksi. Se eroaa chatbotista, skriptistä ja työnkulusta siinä, että se ei vain reagoi, toista samaa toimintoa tai seuraa valmiita sääntöjä, vaan arvioi tilannetta ja ohjaa toimintaansa sen perusteella.

Kurssin kuusi suunnittelukohtaa ovat **syötekäsittely**, **päättely**, **työkalut**, **muisti**, **turvakerros** ja **palautesilmukka**. Niiden avulla kysyt, mitä juuri tämä agentti tarvitsee ja mitä voidaan jättää pois. Pitkäkestoinen muisti ja palautteesta oppiminen eivät ole pakollisia.

Agentteja kohtaat myös valmiina tuotteina, sovellusten agenttitiloina. Niitä voi tarkastella samalla kuuden kohdan listalla. Tekninen ydin on kielimalli ja sen ympärille rakennettu **harness**: työkalut, muisti, oikeudet ja turvarajat. Kun tunnet osat, osaat arvioida myös valmista agenttia.


---

## Lähteet ja tarkistuspäivä

- [Anthropic: Building Effective AI Agents](https://resources.anthropic.com/building-effective-ai-agents)
- [Yao ym.: ReAct](https://arxiv.org/abs/2210.03629)
- [Model Context Protocol: server primitives](https://modelcontextprotocol.io/specification/2025-06-18/server/index)

Tarkistettu 15.7.2026.
