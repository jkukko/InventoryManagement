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

[Tietokantakuvio](https://github.com/jkukko/InventoryManagement/blob/master/documents/pictures/tietokantakaavio.png)
