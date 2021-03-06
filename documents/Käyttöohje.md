# Käyttöohje

## Rekisteröityminen ja kirjautuminen

Sovellukseen rekisteröidytään ja kirjaudutaan yläpalkin oikeassa laidassa olevista linkeistä.
Rekisteröityessä käyttäjänimen ja salasanan tulee olla vähintään 3 merkkiä pitkät ja 15 merkkiä pitkä.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/create_an_user_and_login.png" width="960">

## Luo varasto ja valitse

Valitse navikointivalikosta "Add new inventory". Tämän jälkeen keksi varstolle nimi. Sen pitää olla vähintään 5 merkkiä pitkä. Tämän jälkeen tallenna uusi varasto.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/create_an_inventory.png" width="960">

Uuden varaston luonnin jälkeen sovellus vie suoraan "Own inventories" näkymään.
Sinne pääsee myös valitsemalla navikointivalikosta "Own inventories".

Listauksessa käyttäjän tekemät varastot, sekä toisten käyttäjien varastot, mihin hänellä on oikeus.
Painamalla "select" käyttäjä voi valita varaston, ja tämä vie käyttäjän kyseisen varaston näkymään. 
Painamalla "Update" käyttäjä pääsee näkymään, missä hän voi päivittää varaston nimen. 
Painamalla "remove" käyttäjä voi poistaa varaston. 
Poistamisse huomioidaan kuitenkin onko käyttäjä omistaja vai ei. 
Jos hän ei ole varaston omistaja, varsto poistuu ainoastaan hänen listauksesta.
Jos hän on omistaja, koko varsato poistetaan.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/select_inventory.png" width="960">

## Muiden varastojen lisääminen omaan varasto listaukseen / oikeuden lisääminen

Valitsemalla "Add inventory" valikointinäkymästä käyttäjä saa listauksen kaikista varatoista, mihin hänellä ei ole oikeutta.
Painamalla "Select" käyttäjälle lisätään oikeus varastoon.
Tämän jälkeen varasto löytyy "Own inventories" alta.
Kun käyttäjä poistaa varaston, minkä omistaja hän ei ole, se palautuu takaisin tähän listaan.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/all_inventories.png" width="960">

## Varastonäkymä

Varastonäkymä sisältää seuraavat toiminnallisuudet/näkymät:
* Summary (yleisnäkymä, allert monitor)
* List Products
* Add new Product
* List Orders
* Add new Order
* Return to main menu

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/inventory_summary_menu.png" width="960">


### Summary

Summary näkymistä ilmenee varaston yleistilanne. 
Ensimmäisenä ilmoitetaan varaston tuotteiden lkm, sekä tuotteiden lukumäärä, mitkä ovat alle varmuuusvarastotason.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/inventory_summary_header_information.png" width="480">

Seuraavaksi on "Allerm monitor". 
Siinä ensimmäiseksi on listattu tuotteet, missä nykyinen vastotilanne on 0.
Toiseksi siinä on listattu tuotteet, missä nykyinen varastotilanne on alle varmuusvarastotason.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/inventory_summary_alerm_monitor.png" width="960">

Tämän jälkeen systeemi tarjoaa varmuusvarastotason alla olevien tuotteiden varastotilanne graafit allekkain.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/inventory_summary_chart.png" width="480">


### Add new Product

"Add new Product" -näkymässä voidaan lisätä tuote varastoon. Käyttäjän pitää täyttää tuotteen nimi ja segmentti.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/product_create.png" withd="960">

### List of Product

"List of Product" -näkymästä nähdään kaikki tuotteet, mitä on varastoon perustettu, sekä niiden kyseisen tilanteen.
Tämän lisäksi systeemi näyttää piirakkakuvion varaston nykyvarastotilanteen jakautumisesta eri tuotteille.
Listasta käyttäjä voi poistaa ("remove"-painike) tuotteet tai päivittää ("updated"-painike)  sen.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/list_of_products.png" width="960">

Käyttäjän valitessa päivitä valikko, pääsee hän päivittämään tuotteen tietoja. 
Päivitettäviä tietoja ovat: nimi, segmentti ja varmuusvarastotaso.
Tämän lisäksi täältä näkee tuotteen varastohistoria.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/product_update.png" width="960">

### Add new Order

"Add new Order" -näkymästä käyttäjä voi lisätä uuden tilauksen. 
Käyttäjä täytyy valita tuote alasvetovalikosta.
Tämän lisäksi käyttäjän pitää lisätä haluttu määrä.
Tilaus voi olla joko sisään- tai ulostuleva. 
Sisääntuleva tilaus kasvattaa tuotteen varastosaldoa ja ulostuleva kuluttaa varastosaldoa.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/order_create.png" width="960">

### List Orders

"List Orders" -näkymästä käyttäjä näkee kaikki tilaukset.

### Return to main menu

"Return to main menu" -valikko palauttaa käyttäjän sovelluksen alkuun.
