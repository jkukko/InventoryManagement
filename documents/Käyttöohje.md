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

Seuraavaksi on "Allar monitor". 
Siinä ensimmäiseksi on listattu tuotteet, missä nykyinen vastotilanne on 0.
Toiseksi siinä on listattu tuotteet, missä nykyinen varastotilanne on alle varmuusvarastotason.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/inventory_summary_alerm_monitor.png" width="960">

Tämän jälkeen systeemi tarjoaa varmuusvarastotason alla olevien tuotteiden varastotilanne graafit allekkain.

<img src="" width="">

### List of Products

### Add new Product

### List of Orders

### Add new Order

### Return to main menu
