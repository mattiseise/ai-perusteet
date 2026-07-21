# Sanasto — apuri-botin viimeistely

## Apuri-botti

Rajattuun tehtävään suunniteltu keskusteleva apuri. Se auttaa käyttäjää etenemään, mutta ei poista käyttäjän vastuuta eikä muutu agentiksi pelkän järjestelmäpromptin perusteella.

## Promptikortti

Uudelleen käytettävä promptipohja, jossa näkyvät käyttötarkoitus, rakenne, laatukriteerit ja tunnettu raja. Se on ensimmäinen bottiprojektin kolmesta rakennuspalikasta.

## Botin määrittely

Kuvaus botin käyttäjästä, rajatusta tehtävästä, onnistumisen ehdoista, työnkulusta ja rajoista. Se on toinen rakennuspalikka.

## Tietopohja ja testisuunnitelma

Kolmas rakennuspalikka. Tietopohja sisältää 2–4 huolella valittua lähdettä. Testisuunnitelma sisältää kolme ennalta kirjoitettua testiä, niiden odotukset ja läpäisyehdot.

## Järjestelmäprompti

Botille annettu toteutusohje, joka kokoaa rakennuspalikoiden päätökset käytännön toiminnaksi. Se kertoo esimerkiksi roolin, työnkulun, tietopohjan käytön ja rajat. Järjestelmäprompti ei ole neljäs rakennuspalikka eikä korvaa teknistä käyttöoikeusrajaa.

## RAG

Hakua hyödyntävä vastausten muodostaminen. Järjestelmä hakee tietopohjasta kysymykseen sopivia katkelmia ja antaa ne kielimallille vastauksen tueksi. Tietopohja on aineisto; RAG on yksi tapa hakea ja käyttää sitä.

## Normaali tapaus

Testi, jossa käyttäjä pyytää botilta sen rajattuun ydintehtävään kuuluvaa tavallista apua.

## Kielteinen testi

Testi, jossa käyttäjä pyytää jotakin kiellettyä, riskialtista tai botin tehtävän ulkopuolista. Testi tarkistaa, noudattaako botti rajojaan ja eskaloiko tarvittaessa ihmiselle.

## Reunatapaus

Testi, jossa syöte on puutteellinen, epäselvä tai ristiriitainen. Hyvä toiminta voi olla tarkentavan kysymyksen esittäminen arvaamisen sijaan.

## Korjaus ja uudelleentesti

Yhteen havaittuun puutteeseen tehdään nimetty muutos, minkä jälkeen samaa asiaa koskeva testi toistetaan samalla odotuksella. Vertailu antaa näyttöä korjauksen vaikutuksesta tässä testissä, ei kaikissa mahdollisissa tilanteissa.

## Tekninen toteutuspolku

Suorituspolku, jossa botti rakennetaan käytettävälle alustalle. Näyttö voi koskea todellista toimintaa, tietopohjan kytkentää ja toteutukseen kuuluvia pääsyasetuksia.

## Dokumentoitu suunnittelupolku

Suorituspolku, jossa kuvataan toteutuskelpoinen arkkitehtuuri, simuloidut suoritusjäljet, testit ja tunnistetut rajat. Se ei todista integraatioiden tai käyttöoikeuksien toimivan teknisesti.

## Simuloitu suoritusjälki

Vaiheittainen kuvaus siitä, mitä suunniteltu järjestelmä tekisi annetulla syötteellä. Simuloiduksi merkitty jälki osoittaa suunnitelman johdonmukaisuutta, ei oikean järjestelmän toimintaa.

## Käyttöoikeusraja

Tekninen tai organisatorinen raja, joka määrittää, kuka saa käyttää bottia tai nähdä tietopohjan aineistoa. Pelkkä järjestelmäpromptin kielto ei ole tekninen käyttöoikeusraja.

## Reflektio

Perusteltu arvio omasta työstä ja oppimisesta. Tässä tehtävässä reflektio nimeää tärkeän testihavainnon, tehdyn korjauksen, uudelleentestin rajatun tuloksen ja seuraavan kehitysaskeleen.
