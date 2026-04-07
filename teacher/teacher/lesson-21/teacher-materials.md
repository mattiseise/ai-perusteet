# Opettajamateriaali – Lesson 21

## Oppitunnin ydinajatukset

Agentti näyttää älykkäältä neljästä syystä:
1. Se näkee nykyisen tilanteen (konteksti-ikkuna)
2. Se muistaa menneisyyttä (vektoritietokanta)
3. Se seuraa prosessin vaihetta (tila ja muuttujat)
4. Se toimii johdonmukaisesti (soul)

---

## Konteksti-ikkuna — pedagoginen selitys

**Liian pieni**: Agentti unohtaa alkuperäisen kontekstin, toistaa itseään.
**Liian iso**: Agentti hidastuu, maksaa enemmän (API-kutsut).
**Oikea koko**: Riippuu tehtävästä. Tekniikka vaatii suurempaa (monivaiheinen), yksinkertainen kysymys pienempää.

---

## Vektoritietokanta — yksinkertainen analogia

**Perinteinen tietokanta**: etsit "maksu", löydät vain "maksu"
**Vektoritietokanta**: etsit "maksu", löydät "kortin hylkääminen", "laskutus" — kaikki samalla merkitysalueella

---

## Tila ja muuttujat — suunnittelumalli

1. Listaa kaikki vaiheet prosessissa
2. Nimeä jokainen tila selkeästi
3. Määritä muuttujat kussakin tilassa
4. Määritä siirtymän ehdot

**Tärkeää**: Agentti ei hypi tilaa. Se noudattaa aina järjestystä.

---

## Soul — miksi se on kriittinen?

Soul tekee agentista johdonmukaisen. Ilman sitä agentti voisi:
- Hyväksyä 50% alennusta yhdelle ja hylätä 20% toiselle (epäjohdonmukainen)
- Antaa asiakkaan tietoja kolmansille (vaarallinen)
- Tehdä mitä tahansa ottamatta huomioon arvoja (käyttökelvoton)

---

## Harjoitukset

1. **Ikkunan koko**: Näytä sama logi 10, 50, 100 viestin ikkunalla
2. **Semanttinen haku**: Anna opiskelijoille tapausten tietokanta, kysy "mitä hakisit?"
3. **Viallinen tila**: Näytä prosessi, jossa tila ei muutu oikein
4. **Soul-ristiriidat**: Kaksi soul:ia, sama tilanne, eri reaktiot

---

## Yhteiset virheet

1. Isompi ikkuna = aina parempi → Näytä kustannukset
2. Vektoritietokanta = täydellinen → Kerro false positiveista
3. Tilasiirtymien ehdot unohdetaan → Näytä, mitä tapahtuu jos "kiinnittyy"
4. Soul liian abstrakti → Soul pitää olla konkreettinen
