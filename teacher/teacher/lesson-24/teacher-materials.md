# Opettajamateriaali – Lesson 24

## Oppitunnin ydinajatukset

Turvallisuus on agenttien rakentamisen pohja. Agentti tekee asioita, joten hyökkäys on vaarallisempi kuin chatissa.

Neljä pääuhkaa:
1. **Prompt injection**: Hyökkääjä piilottaa käskyt
2. **Hallusinaatiot**: Agentti keksii asioita
3. **Liian suuri pääsy**: Minimioikeusperiaate unohtaa
4. **Puutteellinen seuranta**: Virhe jää huomaamatta

---

## Prompt injection — kolme tasoa puolustusta

1. **Erittely**: Merkitse [USER INPUT] ja [SYSTEM INSTRUCTION] selvästi
2. **Validointi**: Tarkista, ettei sisällä poikkeavia merkkejä
3. **Rajoitus**: Anna agentille vain mitä se tarvitsee

---

## Hallusinaatiot — kolme keinoa estää

1. **Ankkurointi**: Agentti vastaa vain tietokannasta löytyvien tietojen perusteella
2. **Varmuuskynnys**: Jos varmuus < 70%, pyydä ihmisen apua
3. **Tarkistusaskeleet**: Erillinen komponentti tarkistaa ennen lähettämistä

---

## Minimioikeusperiaate — neljä vaihetta

1. **Inventointi**: Mitä agentti TODELLA tarvitsee?
2. **Rajoitus**: Anna vain nämä oikeudet
3. **Dokumentointi**: Miksi jokainen oikeus?
4. **Säännöllinen tarkistus**: Onko vielä tarpeen?

---

## Neljä turvakerroksen tasoa

```
1. VALIDOINTI: Tarkista syöte ennen agentin käyttöä
   ↓
2. RAJOITUS: Anna vain mitä tarvitsee, vaadi hyväksynnät
   ↓
3. SEURANTA: Jokainen operaatio loggiin
   ↓
4. PALAUTUMINEN: Osaa kumota tai korjata
```

---

## Epäonnistumisen pedagogiikka — Tehtävä 0 (Prompt injection käytännössä)

### Miksi tämä tehtävä on tärkeä
Tehtävät 1–4 käsittelevät turvallisuutta analyyttisesti: "kuvittele hyökkäys, suunnittele puolustus." Tehtävä 0 on erilainen — se on **kokemusperäinen**. Opiskelija tekee itse hyökkäyksen ja näkee sen toimivan. Tämä luo emotionaalisen muistijäljen, joka on tehokkaampi kuin mikään teoreettinen selitys.

### Fasilitointiohje
- **Tämä on turvallinen harjoitus.** Opiskelijat hyökkäävät vain omia bottejaan tai yleistä ChatGPT:tä, eivät oikeita järjestelmiä.
- Kokemus on tarkoituksellisesti hämmentävä: "En uskonut, että se toimii." Tämä hämmennys on oppimisen ydin.
- Ohjaa keskustelu AINA hyökkäyksestä puolustukseen: "Nyt tiedät, miten helppo hyökkäys on. Seuraavaksi mietitään, miten estät sen."
- Varo, ettei tehtävä muutu "kuka keksii pahimman hyökkäyksen" -kilpailuksi. Ohjaa fokus aina turvallisuusajatteluun.

### Yleisiä väärinkäsityksiä

**"Custom-GPT on turvallinen, koska sillä on ohjeet"**
- Korjaus: Ohjeet ovat vain tekstiä — ne eivät ole turvakerros. Prompt injection kiertää ne helposti.

**"Oikeat järjestelmät ovat paremmin suojattuja"**
- Osittain totta: tuotantojärjestelmissä ON lisäkerroksia. Mutta pohjaongelma on sama — kielimalli ei erottele luotettavaa ja epäluotettavaa syötettä ilman erillistä turvakerrosta.

**"Tämä on hakkeriasia, ei liity minuun"**
- Korjaus: Jokainen, joka rakentaa tai käyttää tekoälybotteja, on vastuussa niiden turvallisuudesta. Tämä ei ole hakkerin taito — se on ammattilaisen perusosaamista.

### Arviointivinkit tehtävään 0
- Hyvä: opiskelija kokeilee 5 tekniikkaa ja dokumentoi tulokset rehellisesti.
- Erinomainen: opiskelija analysoi MIKSI jotkut tekniikat toimivat ja osaa yhdistää puolustuskeinot (erittely, validointi, rajoitus) konkreettisiin hyökkäyksiin.
- Pinnallinen: "Kaikki toimi" ilman analyysia miksi tai mitä tehdä asialle.

---

## Harjoitukset

1. Prompt injection: Hyökkäykset ja puolustus
2. Hallusinaatiot: Skenaariot ja ehkäisy
3. Minimioikeusperiaate: Pääsyn suunnittelu
4. Neljä kerrosta: Yhdessä tehtävässä

---

## Yhteinen virheet

1. "Turvallisuus voidaan lisätä lopuksi" → Ei, alusta alkaen
2. "Isompi whitelist = parempi" → Ei, rajoitus tekee turvallisemmaksi
3. "Hallusinaatio on harvinaista" → Ei, riski on todellinen
4. "Lokit ovat vain vianselvitykseen" → Ei, kriittisiä turvallisuudelle
