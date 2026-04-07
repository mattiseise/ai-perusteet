# Opettajamateriaali – Lesson 25

## Oppitunnin ydinajatukset

Agentti ei ole täysin autonominen. Kriittisissä hetkissä ihminen täytyy sisällyttää. **Human-in-the-loop** = hybridi automaatio.

Tämä on matka kohti n8n-projektia, jossa opiskelijat **rakentavat omaa agenttia**. Viimeiset 5 oppituntia ovat rakennuspalkkeja:

1. **Lesson 21**: Muisti ja konteksti — agentti muistaa
2. **Lesson 22**: Työkalut — agentti tekee asioita
3. **Lesson 23**: Suunnittelumallit — agentti ajattelee oikein
4. **Lesson 24**: Turvallisuus — agentti on turvallinen
5. **Lesson 25**: Human-in-the-loop — agentti tekee yhteistyötä

---

## Kolme sääntöä hyväksynnälle

**Rahaa/rakenne**: Alennukset, hyvitykset, tietojen muutos
**Epävarmuus**: Varmuus < 70%
**Poikkeama**: Epätavallinen tapaus

---

## Hyväksyntäportin suunnittelu

Selkeä + nopea. Sisältää:
- Mitä päätöstä?
- Kelle?
- Miksi?
- Kuka hyväksy?
- Mitä jos ei?

---

## Human-in-the-loop työnkulku

Agentti tekee:
- Analyysit (nopea)
- Rutiinit (tehokas)
- Yksinkertaiset päätökset (johdattaa)

Ihminen tekee:
- Kriittiset päätökset
- Epäselvät tilanteet
- Oppimisen ohjaaminen

---

## Oppiminen palautteesta

1. Tallennetaan jokainen hyväksyntä/hylkäys
2. Agentti analysoi kuvioita
3. Mukauttaa ehdotuksensa
4. Vaara: voi oppia väärin

---

## Harjoitukset

1. Kolme sääntöä: Päätösten luokittelu
2. Hyväksyntäportti: Suunnittelu
3. Työnkulku: Kaavio
4. Oppiminen: Mekanismi

---

## Yhteys n8n-projektiin

N8n:ssa nämä implementoituu:
- **Approval node**: Hyväksyntäportti
- **Conditional node**: Jos → hyväksy vai hylkää
- **Logging**: Kaikki tallennetaan
- **Webhook**: Ihminen vastaa
