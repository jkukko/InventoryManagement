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

```
SELECT Inventory.id, Inventory.name FROM Inventory WHERE Inventory.id NOT IN (SELECT inventory_users.inventory_id FROM inventory_users WHERE inventory_users.user_id = ?)
```

* Käyttäjä voi lisätä toisen varaston omaksi

```
INSERT INTO inventory_users (user_id, inventory_id) VALUES (?, ?)
```

* Käyttäjä voi poistaa toisen varaston

```
DELETE FROM Inventory_users WHERE Inventory_users.inventory_id = ? AND Inventory_users.user_id = ?
```

* Käyttäjä voi valita varaston

```
SELECT inventory.id AS inventory_id, inventory.date_created AS inventory_date_created, inventory.date_modified AS inventory_date_modified, inventory.name AS inventory_name, inventory.owner_id AS inventory_owner_id 
FROM inventory 
WHERE inventory.id = ?
```

## Varastoon liittyvä toiminnallisuus

* Käyttäjä saa summaryn varastosta (tapahtuu kun valitaan varasto)

```
SELECT COUNT(Product.id) FROM Product WHERE Product.inventory_id = ?

SELECT COUNT(Product.id) FROM Product WHERE Product.difference < 0 AND Product.inventory_id = ?

SELECT Product.name, Product.current_stock, Product.difference FROM Product LEFT JOIN Inventory ON Inventory.id = Product.inventory_id WHERE Product.difference < 0 AND Inventory.id = ?

SELECT Product.name, Product.safety_stock, Product.difference FROM Product LEFT JOIN Inventory ON Inventory.id = Product.inventory_id WHERE Product.current_stock = 0 AND Inventory.id = ?

SELECT Product.id FROM Product LEFT JOIN Inventory ON Inventory.id = Product.inventory_id WHERE Product.difference < 0 AND Inventory.id = ?

SELECT product.id AS product_id, product.date_created AS product_date_created, product.date_modified AS product_date_modified, product.name AS product_name, product.segment AS product_segment, product.current_stock AS product_current_stock, product.safety_stock AS product_safety_stock, product.difference AS product_difference, product.inventory_id AS product_inventory_id 
FROM product 
WHERE product.id = ?

```

* Tuotteen lisääminen

```
INSERT INTO product (date_created, date_modified, name, segment, current_stock, safety_stock, difference, inventory_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
```

* Tuotteiden listaaminen

```
SELECT product.id AS product_id, product.date_created AS product_date_created, product.date_modified AS product_date_modified, product.name AS product_name, product.segment AS product_segment, product.current_stock AS product_current_stock, product.safety_stock AS product_safety_stock, product.difference AS product_difference, product.inventory_id AS product_inventory_id 
FROM product 
WHERE product.inventory_id = ?
```

* Piirakka kuvion luonti

```
SELECT Product.name, Product.current_stock FROM Product WHERE Product.inventory_id = ?
```

