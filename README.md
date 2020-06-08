# InventoryManagement

InventoryManagement tarjoaa mahdollisuuden varastonhallintaan. 
Järjestelmällä tarkoitus pitää kirjaa varastontilanteesta. 
Luodessaan käyttäjää käyttäjä voi tehdä itsestään pääkäyttäjän joka voi luoda varastoja ja lisätä varastolle peruskäyttäjiä.
Peruskäyttäjä näkee listaukset varastoista ja hän voi lähettää requestin pääkäyttäjälle, että hänelle lisättäisiin oikeus tähän varastoon. 
Käyttäjä voi luoda, muuttaa ja poistaa tuotteita. Käyttäjä voi kirjata varastoon tilauksia, joko sisään- tai ulosmeneviä, tuotteille. 
Sisäänmenevät tilaukset kasvattavat varastossa olevien tuotteiden saldoa ja ulosmenevät taas kuluttavat sitää.
Järjestelmässä tarjoaa erilaisia yhteenvetoraportteja: nykyinen varastotilanne ja  varastohistoria.

## Toimintoja
* Käyttäjän luominen
* Kirjautuminen
* Varaston luominen
* Varastojen listaus
* Lähettää pyyntö oikeuteen käyttää varastoa
* Tuotteen luominen
* Tuotteen muuttaminen ja poistaminen
* Tilauksen kirjaaminen
* Tilauksen muuttaminen ja poistaminen
* Varastosta tuotteen ottaminen (ulos menevän tilauksen kirjaaminen)
* Varaston nykytilanteen raportointi
* Varaston historian tarkasteleminen

## Dokumentit

[Tietokantakuvio](https://github.com/jkukko/InventoryManagement/blob/master/documents/pictures/tietokantakaavio_V3.png)

[User stories](https://github.com/jkukko/InventoryManagement/blob/master/documents/userstories.md)

[Ideoita matkanvarrelta](https://github.com/jkukko/InventoryManagement/blob/master/documents/ideoita.md)

[Asennusohje](https://github.com/jkukko/InventoryManagement/blob/master/documents/Asennusohje.md)

[Käyttöohje](https://github.com/jkukko/InventoryManagement/blob/master/documents/K%C3%A4ytt%C3%B6ohje.md)

## Linkit

[Heroku sovellus](https://manage-your-inventory.herokuapp.com/)


## Käyttöohjeet

### Kirjautuminen

`
Käyttäjätunnus: test1, salasana: test1
`
