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
Painamalla "Updated" käyttäjä pääsee näkymään, missä hän voi päivittää varaston nimen. 
Painamalla "remove" käyttäjä voi poistaa varaston. 
Poistamisse huomioidaan kuitenkin onko käyttäjä omistaja vai ei. 
Jos hän ei ole varaston omistaja, varsto poistuu ainoastaan hänen listauksesta.
Jos hän on omistaja, koko varsato poistetaan.

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/kuvat/select_inventory.png" width="960">

## Muiden varastojen lisääminen omaan varasto listaukseen / oikeuden lisääminen

Valitsemalla "Add inventory" valikointinäkymästä käyttäjä saa listauksen kaikista varatoista, mihin hänellä ei ole oikeutta.
Painamalla "Select" käyttäjälle lisätään oikeus varastoon.
Tämän jälkeen varasto löytyy "Own inventories" alta.

<img src="" width="960">

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



### List of Products

### Add new Product

### List of Orders

### Add new Order

### Return to main menu
