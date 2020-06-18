# User Stroies

## Tunnuksen Luominen ja kirjautuminen

* Käyttäjä voi luoda tunnuksen itselleen

```
INSERT INTO account (date_created, date_modified, username, password) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
```

* Käyttäjä voi kirjautua sovellukseen

```
SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.username AS account_username, account.password AS account_password 
FROM account 
WHERE account.username = ? AND account.password = ?
```

## Varastoon liittyvät toiminnallisuudet

* Käyttäjä voi luoda varaston

```
INSERT INTO inventory (date_created, date_modified, name, owner_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
```

* Käyttäjä voi listata omat varastot

```
SELECT Inventory.id, Inventory.name FROM Inventory WHERE Inventory.id IN (SELECT inventory_users.inventory_id FROM inventory_users WHERE inventory_users.user_id = ?)
```

* Käyttäjä voi poistaa oman varaston

```
DELETE FROM Orders WHERE Orders.inventory_id = ?

DELETE FROM Product WHERE Product.inventory_id = ?

DELETE FROM Inventory WHERE Inventory.id = ?

DELETE FROM Inventory_users WHERE Inventory_users.inventory_id = ?
```

* Käyttäjä voi listata muut varastot

* Käyttäjä voi lisätä toisen varaston omaksi

* Käyttäjä voi poistaa toisen varaston

* Käyttäjä voi valita varaston
## Käyttäjän lisääminen varastoon

* Käyttäjä voi pyytää oikeuksia varaston käyttämiseen

* Hallinoiva käyttäjä voi lisätä peruskäyttäjiä varastoon

## Tilauksen luominen 

* Käyttäjä voi kirjata tilauksen varastoon

* Käyttäjä voi ottaa varastosta

## Yhteenvetoraportteja

* Käyttäjä voi tutkia varaston nykytilanteen

* Käyttäjä ajaa yksittäisen tuotteen historiaraportin
