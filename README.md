# InventoryManagement

InventoryManagement tarjoaa mahdollisuuden varastonhallintaan. 
Järjestelmällä tarkoitus pitää kirjaa varastontilanteesta. 
Luodessaan käyttäjää käyttäjä voi luoda varaston / varastoja.
Käyttäjä voi myös lisätä itselleen muiden tekemiä varastoja.
Käyttäjä voi valita varaston.  
Käyttäjä voi luoda, muuttaa ja poistaa tuotteita varastossa. Tämän lisäksi käyttäjä voi antaa tuotteelle varmuusvarstolimitin. Käyttäjä voi kirjata varastoon tilauksia, joko sisään- tai ulosmeneviä, tuotteille. 
Sisäänmenevät tilaukset kasvattavat varastossa olevien tuotteiden saldoa ja ulosmenevät taas kuluttavat sitää.
Järjestelmässä tarjoaa erilaisia yhteenvetoraportteja: nykyinen varastotilanne ja  varastohistoria, sekä alarm monitorin, mikä näyttää tuotteet, missä nykyinen varastotaso on alle varmuusvaraston.

## Toimintoja
* Käyttäjän luominen
* Kirjautuminen
* Varaston luominen
* Varastojen listaus
* Oman luodun varaston poistaminen
* Muiden varastojen listaaminen
* Muun käyttäjän varaston lisääminen "omiksi" varastoiksi
* Muun käyttäjän varaston poistaminen
* Varaston valitseminen
* Tuotteen luominen
* Tuotteen muuttaminen ja poistaminen
* Tilauksen kirjaaminen
* Varastosta tuotteen ottaminen (ulos menevän tilauksen kirjaaminen)
* Varmuusvarastotason määrittäminen tuotteelle
* Varaston nykytilanteen raportointi
* Varaston historian tarkasteleminen
* Varaston summaryn tarkistaminen

## Dokumentit

[Tietokantakuvio](https://github.com/jkukko/InventoryManagement/blob/master/documents/tietokantakaavio.md)

[User stories](https://github.com/jkukko/InventoryManagement/blob/master/documents/userstories.md)

[Asennusohje](https://github.com/jkukko/InventoryManagement/blob/master/documents/Asennusohje.md)

[Käyttöohje](https://github.com/jkukko/InventoryManagement/blob/master/documents/K%C3%A4ytt%C3%B6ohje.md)

## Linkit

[Heroku sovellus](https://manage-your-inventory.herokuapp.com/)


## Käyttöohjeet

### Kirjautuminen

`
Käyttäjätunnus: test1, salasana: test1
`
## Jatkokehitysideat

* Käyttäjä ei voisi suoraan lisätä muun varastoa omille listoille. Lähettäisi pyynnön, minkä omistaja varmistaisi.

* Kattavampi analytiikka varastotilanteesta.

* Tilauksien paremi käsittely. Jostain syystä en saanut tilauksen validointia toimimaan.Tämän lisäksi olisi pitänyt tehdä parempi käsittely tilauksille jos varasto ei riitä.

* Ennustamisominaisuus tuotteen tilaushistorian perusteella

* Admin-porttaali, mistä näkisi yleistilanteen sovelluksesta (Esim. montako käyttäjää, kuinka paljon kukin käyttäjä käyttää tietokantaa jne.)

