## Tietokantakaavio

<img src="https://github.com/jkukko/InventoryManagement/blob/master/documents/pictures/tietokantakaavio_V4.png" width="480">

## Create table-lauseet

```

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE inventory (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	owner_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owner_id) REFERENCES account (id)
);

CREATE TABLE product (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	segment VARCHAR(144) NOT NULL, 
	current_stock INTEGER, 
	safety_stock INTEGER, 
	difference INTEGER, 
	inventory_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(inventory_id) REFERENCES inventory (id)
);

CREATE TABLE inventory_users (
	user_id INTEGER NOT NULL, 
	inventory_id INTEGER NOT NULL, 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	FOREIGN KEY(inventory_id) REFERENCES inventory (id)
);

CREATE TABLE orders (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	incoming BOOLEAN, 
	amount INTEGER, 
	inventory_id INTEGER NOT NULL, 
	product_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (incoming IN (0, 1)), 
	FOREIGN KEY(inventory_id) REFERENCES inventory (id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
);
```
